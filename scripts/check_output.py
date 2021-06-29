#!/usr/bin/env python
import argparse
import difflib
import json
import logging
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.resolve()
LOGGER_NAME = "check_output"
IGNORE_ERRORS = (
    '"get_paginator" is marked as overload, but no implementation is provided',
    '"get_waiter" is marked as overload, but no implementation is provided',
    # 'Expected type arguments for generic class "ResourceCollection"',
    'Type "None" cannot be assigned to type',
    '"__next__" is not present',
    # 'Import "boto3.s3.transfer" could not be resolved',
    # "is partially unknown",
    'Method "paginate" overrides class "Paginator" in an incompatible manner',
    'Method "wait" overrides class "Waiter" in an incompatible manner',
)


class SnapshotMismatchError(Exception):
    pass


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
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-p", "--path", type=Path, default=ROOT_PATH / "mypy_boto3_output")
    parser.add_argument("services", nargs="*")
    return parser.parse_args()


def compare(data: str, snapshot_path: Path, update: bool) -> None:
    data = data.strip()
    logger = logging.getLogger(LOGGER_NAME)
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {snapshot_path}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.info(f"Matched {snapshot_path}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {snapshot_path}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(), data.strip().splitlines(), lineterm=""
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(f"Snapshot {snapshot_path} is different")


def run_flake8(path: Path) -> None:
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                [
                    "python",
                    "-m",
                    "flake8",
                    "--ignore",
                    "E203,W503,E501,D200,D107,D401,D105,D205,D400,D101,D102",
                    path.as_posix(),
                ],
                stderr=f,
                stdout=f,
            )
        except subprocess.CalledProcessError:
            temp_path = Path(f.name)
            output = temp_path.read_text()
            raise SnapshotMismatchError(output)


def run_pyright(path: Path) -> None:
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                ["pyright", path.as_posix(), "--outputjson"],
                stderr=subprocess.DEVNULL,
                stdout=f,
            )
            return
        except subprocess.CalledProcessError:
            pass

        temp_path = Path(f.name)
        output = temp_path.read_text()

        data = json.loads(output).get("generalDiagnostics", [])
        errors = []
        for error in data:
            message = error.get("message", "")
            if any(imsg in message for imsg in IGNORE_ERRORS):
                continue
            errors.append(error)
            raise SnapshotMismatchError(error)


def run_mypy(path: Path) -> None:
    try:
        output = subprocess.check_output(
            ["python", "-m", "mypy", path.as_posix()],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output
        raise SnapshotMismatchError(output)
    print(output)


def main() -> None:
    args = parse_args()
    setup_logging(logging.INFO)
    logger = logging.getLogger(LOGGER_NAME)
    folder: Path
    has_errors = False
    for folder in sorted(args.path.iterdir()):
        if not folder.name.endswith("_package"):
            continue
        for package in folder.iterdir():
            if not package.is_dir() or not package.name.startswith("mypy_boto3_"):
                continue
            if args.services:
                if not any(s in package.name for s in args.services):
                    continue
            try:
                # logger.info(f"Running mypy for {package.name} ...")
                # run_mypy(package)
                logger.info(f"Running flake8 for {package.name} ...")
                run_flake8(package)
                logger.info(f"Running pyright for {package.name} ...")
                run_pyright(package)
            except SnapshotMismatchError as e:
                logger.error(e)
                has_errors = True

    if has_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
