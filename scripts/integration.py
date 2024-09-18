#!/usr/bin/env python
"""
Integration tests.
"""

import argparse
import difflib
import enum
import json
import logging
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence, Tuple

ROOT_PATH = Path(__file__).parent.parent.resolve()
PYRIGHT_CONFIG_PATH = Path(__file__).parent / "pyrightconfig_output.json"
EXAMPLES_PATH = ROOT_PATH / "examples"
AIO_EXAMPLES_PATH = ROOT_PATH / "aio_examples"
SCRIPTS_PATH = ROOT_PATH / "scripts"
LOGGER_NAME = "integration"


class SnapshotMismatchError(Exception):
    """
    Exception for e2e failures.
    """

    def __init__(self, path: Path) -> None:
        super().__init__(f"Snapshot {path} is different")


@dataclass
class Product:
    """
    Product to test.
    """

    name: str
    examples_path: Path
    install_script_path: Path
    build_product: str
    prerequisites: Tuple[str, ...] = ()
    master_build_products: Tuple[str, ...] = ()


class ProductChoices(enum.Enum):
    """
    Product to test.
    """

    boto3 = Product(
        name="boto3",
        examples_path=EXAMPLES_PATH,
        install_script_path=SCRIPTS_PATH / "install.sh",
        build_product="boto3-services",
        master_build_products=("boto3",),
    )
    aioboto3 = Product(
        name="aioboto3",
        prerequisites=("aioboto3",),
        examples_path=AIO_EXAMPLES_PATH,
        install_script_path=SCRIPTS_PATH / "install_aiobotocore.sh",
        build_product="aiobotocore-services",
        master_build_products=("aioboto3", "aiobotocore"),
    )


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Logging level

    Returns:
        Created Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


def print_path(path: Path) -> str:
    """
    Get path as a string relative to current workdir.
    """
    if path.is_absolute():
        cwd = Path.cwd()
        if path == cwd or path.parts <= cwd.parts:
            return path.as_posix()

        try:
            path = path.relative_to(cwd)
        except ValueError:
            return str(path)

    if len(path.parts) == 1:
        return f"./{path.as_posix()}"

    return path.as_posix()


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    log_level: int
    product: Product
    fast: bool
    update: bool
    services: Tuple[str, ...]


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-f", "--fast", action="store_true")
    parser.add_argument("-u", "--update", action="store_true")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-p",
        "--product",
        choices=[i.name for i in ProductChoices],
        default=ProductChoices.boto3.name,
        help=f"Product to test. Default: {ProductChoices.boto3.name}",
    )
    parser.add_argument("services", nargs="*")
    args = parser.parse_args()
    return CLINamespace(
        log_level=logging.DEBUG if args.debug else logging.INFO,
        product=ProductChoices[args.product].value,
        fast=args.fast,
        update=args.update,
        services=tuple(args.services),
    )


def check_call(cmd: Sequence[str]) -> None:
    """
    Check command exit code and output on error.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        for line in e.output.decode().splitlines():
            logger.warning(line)
        raise


def install_master(product: Product) -> None:
    """
    Build and install master stubs.

    - boto3: `boto3-stubs`
    - aioboto3: `types-aioboto3` and `types-aiobotocore`
    """
    if product.prerequisites:
        check_call([sys.executable, "-m", "pip", "install", *product.prerequisites])
    check_call(
        [
            print_path(SCRIPTS_PATH / "build.sh"),
            "--product",
            *product.master_build_products,
            "--no-smart-version",
        ]
    )
    check_call([print_path(product.install_script_path), "master"])


def install_service(service_name: str, product: Product) -> None:
    """
    Build and install a service subpackage.

    - boto3: `mypy-boto3-*`
    - aioboto3: `types-aiobotocore-*`
    """
    check_call(
        [
            print_path(SCRIPTS_PATH / "build.sh"),
            "-s",
            service_name,
            "--product",
            product.build_product,
            "--no-smart-version",
        ]
    )
    check_call([print_path(product.install_script_path), service_name])


def compare(data: str, snapshot_path: Path, update: bool) -> None:
    """
    Compare tool output with a snapshot.
    """
    data = data.strip()
    logger = logging.getLogger(LOGGER_NAME)
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {print_path(snapshot_path)}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.debug(f"Matched {print_path(snapshot_path)}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {print_path(snapshot_path)}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(), data.strip().splitlines(), lineterm=""
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(snapshot_path)


def run_pyright(path: Path, snapshot_path: Path, update: bool) -> None:
    """
    Run `pyright` and compare output.
    """
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    try:
        output = subprocess.check_output(
            [sys.executable, "-m", "pyright", path.as_posix(), "--outputjson"],
            stderr=subprocess.DEVNULL,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output
    finally:
        Path(config_path).unlink(missing_ok=True)

    data = json.loads(output).get("generalDiagnostics", [])
    for diag in data:
        if "file" in diag:
            del diag["file"]
        if "uri" in diag:
            del diag["uri"]

    new_data = json.dumps(data, indent=4)
    compare(new_data, snapshot_path, update)


def run_mypy(path: Path, snapshot_path: Path, update: bool) -> None:
    """
    Run `mypy` and compare output.
    """
    try:
        output = subprocess.check_output(
            [sys.executable, "-m", "mypy", path.as_posix()],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    new_data_lines: list[str] = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    compare(new_data, snapshot_path, update)


def run_call(path: Path) -> None:
    """
    Run submodule for sanity.
    """
    logger = logging.getLogger(LOGGER_NAME)
    try:
        subprocess.check_output([sys.executable, path.as_posix()])
    except subprocess.CalledProcessError as e:
        logger.warning(f"Call output: {e.output.decode()}")
        logger.warning(f"Call error: {e.stderr.decode()}")
        raise


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger = setup_logging(args.log_level)
    if not args.fast:
        logger.info("Installing master...")
        install_master(args.product)
    error: Optional[Exception] = None
    for file in args.product.examples_path.iterdir():
        if not file.name.endswith("_example.py"):
            continue
        service_name = file.name.replace("_example.py", "")
        if args.services and service_name not in args.services:
            continue
        logger.info(f"Checking {service_name}...")
        if not args.fast:
            logger.debug(f"Installing {service_name}...")
            install_service(service_name, args.product)
        try:
            logger.debug(f"Running {print_path(file)} ...")
            run_call(file)
            logger.debug(f"Running mypy for {print_path(file)} ...")
            snapshot_path = args.product.examples_path / "mypy" / f"{file.name}.out"
            run_mypy(file, snapshot_path, args.update)
            logger.debug(f"Running pyright for {print_path(file)} ...")
            snapshot_path = args.product.examples_path / "pyright" / f"{file.name}.json"
            run_pyright(file, snapshot_path, args.update)
        except SnapshotMismatchError as e:
            logger.warning(f"Snapshot mismatch: {e}")
            error = e
    if error:
        logger.error(error)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
