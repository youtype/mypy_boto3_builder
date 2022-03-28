#!/usr/bin/env python
"""
Publish packages to PyPI.
"""
import argparse
import logging
import os
import shutil
import subprocess
import time
from contextlib import contextmanager
from multiprocessing import Pool
from pathlib import Path
from typing import Iterator

MASTER_PACKAGES = [
    "botocore_stubs_package",
    "types_aiobotocore_package",
    "types_aiobotocore_lite_package",
    "mypy_boto3_package",
    "boto3_stubs_package",
    "boto3_stubs_lite_package",
]
LOGGER_NAME = "release"
MAX_RETRIES = 5


def setup_logging(level: int = 0) -> logging.Logger:
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


def build(path: Path) -> None:
    """
    Build package.
    """
    cleanup(path)
    with chdir(path):
        check_call(["python", "setup.py", "build", "sdist", "bdist_wheel"])


def publish(path: Path) -> None:
    """
    Publish to PyPI.
    """
    logger = logging.getLogger(LOGGER_NAME)
    attempt = 1
    while attempt < MAX_RETRIES:
        logger.info(f"Publishing {path.name}")
        try:
            check_call(
                ["twine", "upload", "--non-interactive", f"{path.as_posix()}/dist/*"],
                print_error=False,
            )
            return
        except subprocess.CalledProcessError as e:
            if "File already exists" in e.output:
                logger.info(f"Already published {path.name}")
                return
            for line in e.output.splitlines():
                logger.error(line)

            attempt += 1
            logger.warning(f"Retrying {path.name} {attempt} time in 10 seconds")
            time.sleep(10)

    raise RuntimeError(f"Failed {path.name} after {attempt} attempts")


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
        paths = [p for p in paths if p.name in args.filter]

    master_paths = [p for p in paths if p.name in MASTER_PACKAGES]
    master_paths.sort(key=lambda x: MASTER_PACKAGES.index(x.name))

    service_paths = [p for p in paths if p.name not in MASTER_PACKAGES]

    if not args.skip_build:
        build_paths = [
            *master_paths,
            *service_paths,
        ]
        for index, path in enumerate(build_paths):
            logger.info(f"[{index + 1:03d}/{len(service_paths):03d}] Building {path.name}")
            build(path)

    if not args.skip_publish:
        with Pool(args.threads) as pool:
            pool.map(publish, service_paths)

        for path in master_paths:
            publish(path)


if __name__ == "__main__":
    main()
