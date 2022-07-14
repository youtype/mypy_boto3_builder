#!/usr/bin/env python
"""
Check static stubs.
"""
import argparse
import difflib
import logging
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from mypy_boto3_builder.utils.nice_path import NicePath

ROOT_PATH = Path(__file__).parent.parent.resolve()
EXAMPLES_PATH = ROOT_PATH / "examples"
SCRIPTS_PATH = ROOT_PATH / "scripts"
LOGGER_NAME = "check_stubs"
OUTPUT_PATH = ROOT_PATH / "mypy_boto3_output"
HASH_RE = re.compile(r"0x[0-9a-f]{12}")


def get_replace_paths() -> list[str]:
    """
    Generate a list of paths to replace in snapshot.
    """
    root_path = f"{ROOT_PATH.as_posix()}/"
    result = [*sys.path, *[i.replace(root_path, "") for i in sys.path]]
    result = list(filter(lambda x: "/" in x, result))
    result.sort(key=lambda x: len(x), reverse=True)
    return result


REPLACE_PATHS = get_replace_paths()


class SnapshotMismatchError(Exception):
    """
    Exception for e2e failures.
    """


def setup_logging(level: int = 0) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Logging level

    Returns:
        Created Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


@dataclass
class Package:
    """
    Package to be tested.
    """

    name: str
    requirements: list[Path]
    products: set[str] = field(default_factory=set)
    uninstall: set[str] = field(default_factory=set)

    def __repr__(self) -> str:
        return self.name

    @property
    def snapshot_path(self) -> Path:
        return ROOT_PATH / "check_stubs_snapshots" / f"{self.name}.txt"


PACKAGES: list[Package] = [
    Package(
        name="boto3",
        products={"boto3"},
        uninstall={"boto3-stubs"},
        requirements=[
            ROOT_PATH / "types_s3transfer",
            OUTPUT_PATH / "boto3_stubs_lite_package",
            OUTPUT_PATH / "botocore_stubs_package",
        ],
    ),
    Package(
        name="botocore",
        products={"boto3"},
        requirements=[
            OUTPUT_PATH / "botocore_stubs_package",
        ],
    ),
    Package(
        name="s3transfer",
        requirements=[
            ROOT_PATH / "types_s3transfer",
        ],
    ),
    Package(
        name="aioboto3",
        products={"aioboto3", "aiobotocore"},
        uninstall={"types-aioboto3"},
        requirements=[
            ROOT_PATH / "types_s3transfer",
            OUTPUT_PATH / "types_aiobotocore_lite_package",
            OUTPUT_PATH / "types_aioboto3_lite_package",
        ],
    ),
    Package(
        name="aiobotocore",
        products={"aiobotocore"},
        requirements=[
            OUTPUT_PATH / "types_aiobotocore_lite_package",
        ],
    ),
]


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    clean: bool
    build: bool
    install: bool
    update: bool
    log_level: int
    packages: list[Package]


def get_package(name: str) -> Package:
    """
    Get package by name.
    """
    for package in PACKAGES:
        if package.name == name:
            return package
    choices = ", ".join([i.name for i in PACKAGES])
    raise argparse.ArgumentTypeError(f"Unknown package {name}, choices are {choices}")


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-c", "--clean", action="store_true", help="Uninstall full packages")
    parser.add_argument("-b", "--build", action="store_true", help="Generate packages")
    parser.add_argument("-i", "--install", action="store_true", help="Install packages")
    parser.add_argument("-u", "--update", action="store_true", help="Update snapshots")
    parser.add_argument("-d", "--debug", action="store_true", help="Verbose output")
    parser.add_argument(
        "packages",
        type=get_package,
        nargs="+",
        help="Packages to check",
    )
    args = parser.parse_args()
    return CLINamespace(
        clean=args.clean,
        build=args.build,
        install=args.install,
        update=args.update,
        packages=args.packages,
        log_level=logging.DEBUG if args.debug else logging.INFO,
    )


def check_call(cmd: list[str]) -> None:
    """
    Check command exit code and output on error.
    """
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        logger = logging.getLogger(LOGGER_NAME)
        for line in e.output.decode().splitlines():
            logger.error(line)
        raise


def install_package(path: Path) -> None:
    """
    Build and install Python package from path.
    """
    check_call([sys.executable, "-m", "pip", "install", path.as_posix()])


def compare(data: str, snapshot_path: Path, update: bool) -> None:
    """
    Compare tool output with a snapshot.
    """
    logger = logging.getLogger(LOGGER_NAME)
    data = data.strip()
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {NicePath(snapshot_path)}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.info(f"Matched {NicePath(snapshot_path)}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {NicePath(snapshot_path)}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(), data.strip().splitlines(), lineterm=""
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(f"Snapshot {snapshot_path} is different")


def replace_paths(line: str) -> str:
    """
    Replace system paths to avoid snapshot mismatch.
    """
    for path in REPLACE_PATHS:
        line = line.replace(path, ".")
    return line


def run_stubtest(package: Package, update: bool) -> None:
    """
    Run `mypy` and compare output.
    """
    logger = logging.getLogger(LOGGER_NAME)
    try:
        output = subprocess.check_output(
            [sys.executable, "-m", "mypy.stubtest", package.name],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    new_data_lines = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        line = HASH_RE.sub("HASH", line)
        line = replace_paths(line)
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    compare(new_data, package.snapshot_path, update)


def build_requirements(packages: list[Package]) -> None:
    """
    Install requirements.
    """
    logger = logging.getLogger(LOGGER_NAME)
    products = set()
    for package in packages:
        products.update(package.products)

    if not products:
        return

    build_cmd = [
        sys.executable,
        "-m",
        "mypy_boto3_builder",
        OUTPUT_PATH.as_posix(),
        "--product",
        *sorted(products),
    ]
    logger.debug(f"  Running {' '.join(build_cmd)}")
    check_call(build_cmd)


def install_requirements(packages: list[Package]) -> None:
    """
    Install requirements.
    """
    logger = logging.getLogger(LOGGER_NAME)
    requirements = []
    for package in packages:
        for requirement in package.requirements:
            if requirement not in requirements:
                requirements.append(requirement)
    for requirement in requirements:
        logger.debug(f"  Installing {NicePath(requirement)}")
        install_package(requirement)


def main() -> None:
    """
    Main CLI entrypoint.
    """
    args = parse_args()
    logger = setup_logging(args.log_level)
    if args.clean:
        uninstall = set()
        for package in args.packages:
            uninstall.update(package.uninstall)

        logger.info("Uninstalling stubs...")
        check_call([sys.executable, "-m", "pip", "uninstall", "-y", *sorted(uninstall)])
    if args.build:
        logger.info("Building requirements...")
        build_requirements(args.packages)
    if args.install:
        logger.info("Installing requirements...")
        install_requirements(args.packages)

    error: BaseException | None = None
    logger.info("Checking stubs...")
    for package in args.packages:
        logger.debug(f"  Checking {package.name}")
        try:
            run_stubtest(package, args.update)
        except SnapshotMismatchError as e:
            logger.error(e)
            error = e

    if error:
        exit(1)


if __name__ == "__main__":
    main()
