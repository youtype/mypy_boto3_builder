#!/usr/bin/env python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests",
#   "setuptools",
#   "twine",
#   "wheel",
#   "loguru",
# ]
# ///
"""
Publish packages to PyPI.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import argparse
import itertools
import os
import shutil
import subprocess
import sys
import time
from contextlib import contextmanager
from dataclasses import dataclass
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import patch

from loguru import logger
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import HTTPError
from twine.commands.upload import upload
from twine.exceptions import TwineException
from twine.settings import Settings

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

MAIN_PACKAGES = [
    "types_aiobotocore_lite",
    "types_aiobotocore_full",
    "types_aiobotocore",
    "mypy_boto3",
    "types_boto3_lite",
    "types_boto3",
    "types_boto3_full",
    "boto3_stubs_lite",
    "boto3_stubs_full",
    "boto3_stubs",
    "types_aioboto3_lite",
    "types_aioboto3",
]
MAIN_DIRECTORIES = [f"{i}_package" for i in MAIN_PACKAGES]
LOGGER_NAME = "release"


class Config:
    """
    Global configuration to access from ThreadPool.
    """

    max_retries: int = 10


@dataclass
class CLINamespace:
    """
    CLI arguments.
    """

    path: Path
    publish_threads: int
    filter: tuple[Path, ...]
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
    parser.add_argument("-t", "--threads", type=int, default=3)
    parser.add_argument("-f", "--filter", nargs="+", type=Path, default=[])
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--skip-publish", action="store_true")
    parser.add_argument("-r", "--retries", type=int, default=10)
    args = parser.parse_args()
    return CLINamespace(
        path=args.path,
        publish_threads=args.threads,
        filter=tuple(args.filter),
        skip_build=args.skip_build,
        skip_publish=args.skip_publish,
        retries=args.retries,
    )


def check_call(cmd: Sequence[str], *, print_error: bool = True) -> str:
    """
    Check command exit code and output on error.

    Returns:
        Command output.
    """
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, encoding="utf-8")
    except subprocess.CalledProcessError as e:
        if print_error:
            for line in e.output.splitlines():
                logger.warning(line)
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
    Remove build directories.
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
    attempt = 1
    last_error = Exception("Unknown error")
    while attempt <= max_retries:
        cleanup(path)

        try:
            with chdir(path):
                check_call(("uv", "build", "--sdist", "--wheel"))

            whl_path = next(iter((path / "dist").glob("*.whl")))
            tar_path = next(iter((path / "dist").glob("*.tar.gz")))
            check_call(("tar", "-tzf", tar_path.as_posix()))
            check_call((sys.executable, "-m", "zipfile", "--list", whl_path.as_posix()))
        except (subprocess.CalledProcessError, IndexError) as e:
            attempt += 1
            last_error = e
            logger.warning(f"Failed building {path.name} {attempt} attempt: {e}")
            continue

        return path

    raise last_error


def publish(paths: Sequence[Path]) -> Sequence[Path]:
    """
    Publish packages from dist directory to PyPI.
    """
    for path in paths:
        attempt = 1
        while attempt <= Config.max_retries:
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
                        [path.as_posix()],
                    )
            except TwineException as e:
                logger.warning(f"Configuration error while publishing {path.name}")
                raise e from None
            except HTTPError as e:
                attempt += 1
                response = e.response.text
                if "File already exists" in response:
                    logger.info(f"Already published {path.name}")
                    continue

                logger.warning(f"Error while publishing {path.name}: {e}")
                logger.warning(f"Response: {response}")
                if attempt >= Config.max_retries:
                    raise e from None
                logger.info(f"Retrying {path.name} {attempt} time in 10 seconds")
                time.sleep(10)
            except RequestsConnectionError as e:
                attempt += 1
                logger.warning(f"Error while publishing {path.name}: {e}")
                if attempt >= Config.max_retries:
                    raise e from None
                logger.info(f"Retrying {path.name} {attempt} time in 10 seconds")
                time.sleep(10)
            else:
                break

    return paths


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
    text = (path / "pyproject.toml").read_text().split("\n")
    for line in text:
        if line.strip().startswith("name="):
            return line.split("=")[1].strip().replace('"', "").replace(",", "")

    return ""


def get_version(path: Path) -> str:
    """
    Get package version.
    """
    text = (path / "pyproject.toml").read_text().split("\n")
    for line in text:
        if line.strip().startswith("version="):
            return line.split("=")[1].strip().replace('"', "").replace(",", "")

    return ""


def publish_batches(args: CLINamespace, path_batches: Sequence[Sequence[Sequence[Path]]]) -> None:
    """
    Publish packages in batches.
    """
    total = sum(len(i) for i in path_batches)
    current_total = 0
    for path_batch in path_batches:
        if args.publish_threads == 1:
            for index, paths in enumerate(map(publish, path_batch)):
                current_index = current_total + index
                path_names = " ".join(path.name for path in paths)
                logger.info(
                    f"{get_progress_str(current_index, total)} Published {path_names}",
                )
        else:
            with ThreadPool(processes=args.publish_threads) as pool:
                for index, paths in enumerate(pool.imap(publish, path_batch)):
                    current_index = current_total + index
                    path_names = " ".join(path.name for path in paths)
                    logger.info(
                        f"{get_progress_str(current_index, total)} Published {path_names}",
                    )
        current_total += len(path_batch)


def publish_directories(args: CLINamespace) -> None:
    """
    Build and publish packages from directories.
    """
    paths = [i for i in args.path.iterdir() if i.is_dir()]
    paths.sort(key=lambda x: x.name)
    if args.filter:
        filters = tuple(i.name for i in args.filter)
        paths = list(filter(lambda path: any(i in path.name for i in filters), paths))

    main_paths = [p for p in paths if p.name in MAIN_DIRECTORIES]
    main_paths.sort(key=lambda x: MAIN_DIRECTORIES.index(x.name))

    service_paths = [p for p in paths if p not in main_paths]
    service_paths.sort(key=lambda x: x.name)

    if not args.skip_build:
        total = len(paths)
        for index, path in enumerate(paths):
            build(path, args.retries)
            package_name = get_package_name(path)
            version = get_version(path)
            logger.info(
                f"{get_progress_str(index, total)} Built {package_name} {version}",
            )

    service_paths_batch = tuple(
        tuple(filter(None, i))
        for i in itertools.zip_longest(
            sorted(itertools.chain(*[i.glob("dist/*.whl") for i in service_paths])),
            sorted(itertools.chain(*[i.glob("dist/*.tar.gz") for i in service_paths])),
        )
    )
    main_paths_batch = tuple(
        tuple(filter(None, i))
        for i in itertools.zip_longest(
            sorted(itertools.chain(*[i.glob("dist/*.whl") for i in main_paths])),
            sorted(itertools.chain(*[i.glob("dist/*.tar.gz") for i in main_paths])),
        )
    )

    if not args.skip_publish:
        publish_batches(args, (service_paths_batch, main_paths_batch))


def publish_packages(args: CLINamespace) -> None:
    """
    Publish pre-built packages.
    """
    package_paths = [i for i in args.path.iterdir() if i.is_file() and i.suffix in {".whl", ".gz"}]
    package_paths.sort(key=lambda x: x.name)
    if args.filter:
        filters = tuple(i.name for i in args.filter)
        package_paths = list(
            filter(lambda path: any(i in path.name for i in filters), package_paths)
        )

    main_paths = [p for p in package_paths if p.stem.split("-", 1)[0] in MAIN_PACKAGES]
    main_paths.sort(key=lambda p: MAIN_PACKAGES.index(p.stem.split("-", 1)[0]))

    service_paths = [p for p in package_paths if p not in main_paths]
    service_paths.sort(key=lambda x: x.name)

    service_paths_batch = tuple(
        tuple(filter(None, i))
        for i in itertools.zip_longest(
            tuple(p for p in service_paths if p.suffix == ".whl"),
            tuple(p for p in service_paths if p.suffix == ".gz"),
        )
    )
    main_paths_batch = tuple(
        tuple(filter(None, i))
        for i in itertools.zip_longest(
            tuple(p for p in main_paths if p.suffix == ".whl"),
            tuple(p for p in main_paths if p.suffix == ".gz"),
        )
    )

    if not args.skip_publish:
        publish_batches(args, (service_paths_batch, main_paths_batch))


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    Config.max_retries = args.retries
    publish_directories(args)
    publish_packages(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
