#!/usr/bin/env python
"""
Checker of generated packages.

- [x] import generated package
- [x] flake8
- [x] pyright
- [x] mypy
"""
import argparse
import json
import logging
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.resolve()
LOGGER_NAME = "check_output"
IGNORE_PYRIGHT_ERRORS = (
    '"get_paginator" is marked as overload, but no implementation is provided',
    '"get_waiter" is marked as overload, but no implementation is provided',
    # 'Expected type arguments for generic class "ResourceCollection"',
    # 'Type "None" cannot be assigned to type',
    # '"__next__" is not present',
    # 'Import "boto3.s3.transfer" could not be resolved',
    # "is partially unknown",
    'Method "paginate" overrides class "Paginator" in an incompatible manner',
    'Method "wait" overrides class "Waiter" in an incompatible manner',
    "must return value",
)
IGNORE_MYPY_ERRORS = (
    'Signature of "paginate" incompatible with supertype "Paginator"',
    'Signature of "wait" incompatible with supertype "Waiter"',
)


class SnapshotMismatchError(Exception):
    """
    Main snapshot mismatch exception.
    """


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
    Setup CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-p", "--path", type=Path, default=ROOT_PATH / "mypy_boto3_output")
    parser.add_argument("services", nargs="*")
    return parser.parse_args()


def run_flake8(path: Path) -> None:
    """
    Check output with flake8.
    """
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "flake8",
                    "--ignore",
                    "E203,W503,E501,D200,D107,D401,D105,D205,D400,D101,D102,D403",
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
    """
    Check output with pyright.
    """
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                ["npx", "pyright", path.as_posix(), "--outputjson"],
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
            if any(imsg in message for imsg in IGNORE_PYRIGHT_ERRORS):
                continue
            errors.append(error)

        if errors:
            messages = []
            for error in errors:
                messages.append(
                    f'{error["file"]}:{error["range"]["start"]["line"]} {error.get("message", "")}'
                )
            raise SnapshotMismatchError("\n".join(messages))


def run_mypy(path: Path) -> None:
    """
    Check output with mypy.
    """
    try:
        output = subprocess.check_output(
            [sys.executable, "-m", "mypy", path.as_posix()],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output
        errors = []
        for message in output.splitlines():
            if not message or message.startswith("Found"):
                continue
            if any(imsg in message for imsg in IGNORE_MYPY_ERRORS):
                continue
            errors.append(message)

        if errors:
            raise SnapshotMismatchError("\n".join(errors)) from None


def run_call(path: Path) -> None:
    """
    Check output by importing it.
    """
    try:
        subprocess.check_call([sys.executable, path.as_posix()], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(f"Path {path} cannot be imported: {e}") from None


def main() -> None:
    """
    Main CLI entrypoint.
    """
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
            logger.info(f"Checking {package.name} ...")
            try:
                logger.debug(f"Running call for {package.name} ...")
                run_call(package)
                logger.debug(f"Running mypy for {package.name} ...")
                run_mypy(package)
                logger.debug(f"Running flake8 for {package.name} ...")
                run_flake8(package)
                logger.debug(f"Running pyright for {package.name} ...")
                run_pyright(package)
            except SnapshotMismatchError as e:
                logger.error(e)
                has_errors = True

    if has_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
