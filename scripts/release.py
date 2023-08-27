#!/usr/bin/env python
"""
Publish packages to PyPI.
"""
import argparse
import logging
import os
import shutil
import subprocess
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from multiprocessing.pool import ThreadPool
from pathlib import Path
from unittest.mock import patch

from requests.exceptions import ConnectionError, HTTPError
from twine.commands.upload import upload
from twine.exceptions import TwineException
from twine.settings import Settings

MASTER_PACKAGES = [
    "types_aiobotocore_package",
    "types_aiobotocore_lite_package",
    "mypy_boto3_package",
    "boto3_stubs_package",
    "boto3_stubs_lite_package",
    "types_aioboto3_package",
    "types_aioboto3_lite_package",
]
LOGGER_NAME = "release"


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        verbose -- Set log level to DEBUG.
        panic -- Raise RuntimeError on warning.

    Returns:
        Overriden Logger.
    """
    logging.getLogger("twine").disabled = True
    logging.getLogger("twine.commands.upload").disabled = True

    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


@dataclass
class CLINamespace:
    """
    CLI arguments.
    """

    path: Path
    threads: int
    publish_threads: int
    filter: list[Path]
    skip_build: bool
    skip_publish: bool
    retries: int


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument(
        "-p",
        "--path",
        type=Path,
        default=Path().parent.parent / "mypy_boto3_output",
    )
    parser.add_argument("-t", "--threads", type=int, default=10)
    parser.add_argument("--publish-threads", type=int, default=3)
    parser.add_argument("-f", "--filter", nargs="+", type=Path, default=[])
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--skip-publish", action="store_true")
    parser.add_argument("-r", "--retries", type=int, default=10)
    args = parser.parse_args()
    return CLINamespace(
        path=args.path,
        threads=args.threads,
        publish_threads=args.publish_threads,
        filter=args.filter,
        skip_build=args.skip_build,
        skip_publish=args.skip_publish,
        retries=args.retries,
    )


def check_call(cmd: list[str], print_error: bool = True) -> str:
    """
    Check command exit code and output on error.

    Returns:
        Command output.
    """
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, encoding="utf-8")
    except subprocess.CalledProcessError as e:
        if print_error:
            logger = logging.getLogger(LOGGER_NAME)
            for line in e.output.splitlines():
                logger.error(line)
        raise


@contextmanager
def chdir(path: Path) -> Iterator[Path]:
    """
    Change working directory and return to previous on exit.

    Arguments:
        path -- Target path.

    Yields:
        Target path.
    """
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(prev_cwd)


def cleanup(path: Path) -> None:
    """
    Remove build folders.
    """
    if (path / "build").exists():
        shutil.rmtree(path / "build")
    if (path / "dist").exists():
        shutil.rmtree(path / "dist")
    for rm_path in path.glob("*.egg-info"):
        shutil.rmtree(rm_path)


def build(path: Path, max_retries: int = 10) -> Path:
    """
    Build package.
    """
    logger = logging.getLogger(LOGGER_NAME)
    attempt = 1
    while attempt <= max_retries:
        cleanup(path)

        try:
            with chdir(path):
                check_call([sys.executable, "setup.py", "build", "sdist", "bdist_wheel"])

            whl_path = list((path / "dist").glob("*.whl"))[0]

            tar_path = list((path / "dist").glob("*.tar.gz"))[0]
            check_call(["tar", "-tzf", tar_path.as_posix()])
            check_call([sys.executable, "-m", "zipfile", "--list", whl_path.as_posix()])
        except subprocess.CalledProcessError as e:
            attempt += 1
            logger.error(f"Failed building {path.name} {attempt} attempt: {e}")
            continue

        return path

    raise RuntimeError(f"Failed building {path.name} after {attempt} attempts")


def publish(path: Path, max_retries: int = 10) -> Path:
    """
    Publish to PyPI.
    """
    attempt = 1
    dist_path = path / "dist"
    packages = [i.as_posix() for i in dist_path.glob("*")]
    logger = logging.getLogger(LOGGER_NAME)
    while attempt <= max_retries:
        try:
            with patch("twine.repository.print"), patch("twine.commands.upload.print"):
                upload(
                    Settings(
                        username=os.getenv("PYPI_USERNAME"),
                        password=os.getenv("PYPI_PASSWORD"),
                        non_interactive=True,
                        disable_progress_bar=True,
                        skip_existing=True,
                    ),
                    packages,
                )
            return path

        except TwineException as e:
            logger.error(f"Configuration error while publishing {path.name}: {e}")
            raise e
        except HTTPError as e:
            attempt += 1
            response = e.response.text
            if "File already exists" in response:
                logger.info(f"Already published {path.name}")
                return path

            logger.warning(f"Error while publishing {path.name}: {e}")
            logger.warning(f"Response: {response}")
            logger.info(f"Retrying {path.name} {attempt} time in 10 seconds")
        except ConnectionError as e:
            attempt += 1
            logger.warning(f"Error while publishing {path.name}: {e}")
            logger.info(f"Retrying {path.name} {attempt} time in 10 seconds")

    raise RuntimeError(f"Failed {path.name} after {attempt} attempts")


def get_progress_str(index: int, total: int) -> str:
    """
    Get `index` progress in `total`.
    """
    total_str = f"{total}"
    current_str = f"{{:0{len(total_str)}}}".format(index + 1)
    return f"[{current_str}/{total_str}]"


def get_package_name(path: Path) -> str:
    """
    Get package version.
    """
    text = (path / "setup.py").read_text().split("\n")
    for line in text:
        if line.strip().startswith("name="):
            return line.split("=")[1].strip().replace('"', "").replace(",", "")

    return ""


def get_version(path: Path) -> str:
    """
    Get package version.
    """
    text = (path / "setup.py").read_text().split("\n")
    for line in text:
        if line.strip().startswith("version="):
            return line.split("=")[1].strip().replace('"', "").replace(",", "")

    return ""


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    setup_logging(logging.DEBUG)
    logger = logging.getLogger(LOGGER_NAME)
    paths = [i for i in args.path.absolute().iterdir() if i.is_dir()]
    paths.sort(key=lambda x: x.name)
    if args.filter:
        filters = [i.name for i in args.filter]
        filtered_paths: list[Path] = []
        for path in paths:
            if any(i in path.name for i in filters):
                filtered_paths.append(path)
        paths = filtered_paths

    master_paths = [p for p in paths if p.name in MASTER_PACKAGES]
    master_paths.sort(key=lambda x: MASTER_PACKAGES.index(x.name))

    service_paths = [p for p in paths if p.name not in MASTER_PACKAGES]
    build_paths = [
        *master_paths,
        *service_paths,
    ]

    if not args.skip_build:
        with ThreadPool(args.threads) as pool:
            build_paths_with_retries = [(i, args.retries) for i in build_paths]
            for index, path in enumerate(pool.starmap(build, build_paths_with_retries)):
                package_name = get_package_name(path)
                version = get_version(path)
                logger.info(
                    f"{get_progress_str(index, len(build_paths))} Built {package_name} {version}"
                )

    if not args.skip_publish:
        with ThreadPool(processes=args.publish_threads) as pool:
            service_paths_with_retries = [(i, args.retries) for i in service_paths]
            for index, path in enumerate(pool.starmap(publish, service_paths_with_retries)):
                package_name = get_package_name(path)
                version = get_version(path)
                logger.info(
                    f"{get_progress_str(index, len(build_paths))} Published"
                    f" {package_name} {version}"
                )

        for index, path in enumerate(master_paths):
            publish(path, args.retries)
            total_index = len(service_paths) + index
            package_name = get_package_name(path)
            version = get_version(path)
            logger.info(
                f"{get_progress_str(total_index, len(build_paths))} Published"
                f" {package_name} {version}"
            )


if __name__ == "__main__":
    main()
