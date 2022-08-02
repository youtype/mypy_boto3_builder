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
import time
from collections.abc import Sequence
from contextlib import contextmanager
from multiprocessing import Pool
from pathlib import Path
from typing import Any, Iterator

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
MAX_RETRIES = 10


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        verbose -- Set log level to DEBUG.
        panic -- Raise RuntimeError on warning.

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


def parse_args() -> argparse.Namespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument(
        "-p",
        "--path",
        type=Path,
        default=Path(__file__).parent.parent / "mypy_boto3_output",
    )
    parser.add_argument("-t", "--threads", type=int, default=10)
    parser.add_argument("-r", "--retries", type=int, default=5)
    parser.add_argument("-f", "--filter", nargs="+", default=[])
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--skip-publish", action="store_true")
    return parser.parse_args()


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
            return ""
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


def build(path: Path) -> Path:
    """
    Build package.
    """
    cleanup(path)
    with chdir(path):
        check_call([sys.executable, "setup.py", "build", "sdist", "bdist_wheel"])
    return path


def publish(path: Path) -> Path:
    """
    Publish to PyPI.
    """
    attempt = 1
    while attempt < MAX_RETRIES:
        try:
            check_call(
                [
                    sys.executable,
                    "-m",
                    "twine",
                    "upload",
                    "--non-interactive",
                    f"{path.as_posix()}/dist/*",
                ],
                print_error=False,
            )
            return path
        except subprocess.CalledProcessError as e:
            logger = logging.getLogger(LOGGER_NAME)
            if "File already exists" in e.output:
                logger.info(f"Already published {path.name}")
                return path
            for line in e.output.splitlines():
                logger.error(line)

            attempt += 1
            logger.warning(f"Retrying {path.name} {attempt} time in 10 seconds")
            time.sleep(10)

    raise RuntimeError(f"Failed {path.name} after {attempt} attempts")


def get_progress_str(index: int, seq: Sequence[Any]) -> str:
    """
    Get `index` progress in `seq` sequence.
    """
    total_str = f"{len(seq)}"
    current_str = f"{{:0{len(total_str)}}}".format(index + 1)
    return f"[{current_str}/{total_str}]"


def main() -> None:
    """
    Main CLI entrypoint.
    """
    args = parse_args()
    setup_logging(logging.DEBUG)
    logger = logging.getLogger(LOGGER_NAME)
    paths = [i for i in args.path.absolute().iterdir() if i.is_dir()]
    paths.sort(key=lambda x: x.name)
    if args.filter:
        filtered_paths = []
        for path in paths:
            if any(i in path.name for i in args.filter):
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
        with Pool(args.threads) as pool:
            for index, path in enumerate(pool.imap(build, build_paths)):
                logger.info(f"{get_progress_str(index, build_paths)} Built {path.name}")

    if not args.skip_publish:
        with Pool(args.threads) as pool:
            for index, path in enumerate(pool.imap(publish, service_paths)):
                logger.info(f"{get_progress_str(index, build_paths)} Published {path.name}")

        for index, path in enumerate(master_paths):
            publish(path)
            total_index = len(service_paths) + index
            logger.info(f"{get_progress_str(total_index, build_paths)} Published {path.name}")


if __name__ == "__main__":
    main()
