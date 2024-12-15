#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# ///
"""
Checker of generated packages.

- [x] import generated package
- [x] ruff
- [x] pyright
- [x] mypy

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

ROOT_PATH = Path(__file__).parent.parent.resolve()
PYRIGHT_CONFIG_PATH = Path(__file__).parent / "pyrightconfig_output.json"
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
    'Method "get_paginator" overrides class "AioBaseClient" in an incompatible manner',
    'Method "get_waiter" overrides class "AioBaseClient" in an incompatible manner',
    'Method "wait" overrides class "AIOWaiter" in an incompatible manner',
    'Method "create_client" overrides class "Session" in an incompatible manner',
    'define variable "items" in incompatible way',
    'define variable "values" in incompatible way',
    "must return value",
    'Import "types_aiobotocore_',
    'Import "mypy_boto3_',
    'Import "types_boto3_',
    "Argument to class must be a base class",
    'Function with declared type of "NoReturn" cannot return "None"',
    'Function with declared return type "NoReturn" cannot return "None"',
    '"ellipsis" cannot be assigned to ',
    '"client" overrides symbol of same name in class "ResourceMeta"',
    '"meta" overrides symbol of same name in class "ServiceResource"',
)
IGNORE_MYPY_ERRORS = (
    'Signature of "create_client" incompatible with supertype "Session"',
    'Signature of "paginate" incompatible with supertype "Paginator"',
    'Signature of "wait" incompatible with supertype "Waiter"',
    'Signature of "get_paginator" incompatible with supertype "AioBaseClient"',
    'Signature of "get_waiter" incompatible with supertype "AioBaseClient"',
    'Argument 1 of "get_paginator" is incompatible with supertype "AioBaseClient"',
    'Argument 1 of "get_waiter" is incompatible with supertype "AioBaseClient"',
    'Return type "Coroutine[Any, Any, None]" of "close" incompatible with return type "None"',
    'Signature of "wait" incompatible with supertype "AIOWaiter"',
    'imported name has type "type[object]", local name has type',
    'incompatible with return type "Iterator[list[Any]]" in supertype "ResourceCollection"',
    "note:",
    "invalid syntax; you likely need to run mypy using Python 3.12 or newer",
)

DEPENDENCIES = [
    "types-boto3-lite",
    "types-aiobotocore-lite",
    "types-aioboto3-lite",
    "aioboto3",
    "botocore-stubs",
    "types-s3transfer",
    "types-requests",
    "cryptography",
]

LOCAL_DEPENDENCIES = {
    "types-aiobotocore-lite": ["types_aiobotocore_lite_package", "types_aiobotocore_package"],
    "types-aioboto3-lite": ["types_aioboto3_lite_package", "types_aioboto3_package"],
    "types-boto3-lite": [
        "types_boto3_lite_package",
        "types_boto3_package",
        "boto3_stubs_lite_package",
        "boto3_stubs_package",
    ],
}


class Config:
    """
    Local configuration.
    """

    path: Path


def _find_existing_local_path(local_package_names: Sequence[str]) -> Path | None:
    for local_package_name in local_package_names:
        local_package_path = Config.path / local_package_name
        if local_package_path.exists():
            return local_package_path
    return None


def get_with_arguments() -> list[str]:
    """
    Get --with arguments for uv command.
    """
    result: list[str] = []
    for name in DEPENDENCIES:
        local_package_path = _find_existing_local_path(LOCAL_DEPENDENCIES.get(name, []))
        if local_package_path:
            result.extend(["--with", local_package_path.as_posix()])
            continue

        result.extend(["--with", name])

    return result


class SnapshotMismatchError(Exception):
    """
    Main snapshot mismatch exception.
    """

    def __init__(self, path: Path, error: str) -> None:
        super().__init__(f"Snapshot mismatch for {path}: {error}")
        self.path = path
        self.errors = error


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Log level

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    debug: bool
    path: Path
    filter: list[str]
    exit_on_error: bool


def parse_args() -> CLINamespace:
    """
    Parse CLI arguments.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-x", "--exit-on-error", action="store_true")
    parser.add_argument("-p", "--path", type=Path, default=ROOT_PATH / "mypy_boto3_output")
    parser.add_argument("filter", nargs="*")
    args = parser.parse_args()
    return CLINamespace(
        debug=args.debug,
        path=args.path,
        filter=args.filter,
        exit_on_error=args.exit_on_error,
    )


def run_ruff(path: Path) -> None:
    """
    Check output with ruff.
    """
    select_checks = [
        "E",
        "W",
        "F",
        "B",
        "I",
        "N",
        "C4",
        "C90",
        "RUF",
        "SIM",
        "PYI",
        "PT",
        # "T",
        "LOG",
        "Q",
        "RSE",
        "RET",
        "TID",
        # "TCH",
        "S",
        "BLE",
        # "ANN",
        "A",
        "PTH",
        "YTT",
        "UP",
        "TRY",
        "PERF",
        "FURB",
    ]
    ignore_errors = [
        "A002",  # builtin-argument-shadowing
        "B014",  # duplicate-handler-exception
        "E203",  # whitespace-before-comment
        "E501",  # line-too-long
        "E741",  # ambiguous-variable-name
        "N802",  # invalid-function-name
        "N803",  # invalid-argument-name
        "N812",  # lowercase-imported-as-non-lowercase
        "PYI036",  # bad-exit-annotation
        "RET503",  # implicit-return
        "UP004",  # useless-object-inheritance
        "UP013",  # convert-typed-dict-functional-to-class
    ]
    with tempfile.NamedTemporaryFile("w+b") as f:
        cmd = [
            "uvx",
            "ruff",
            "check",
            "--target-version",
            "py38",
            "--select",
            ",".join(select_checks),
            "--ignore",
            ",".join(ignore_errors),
            path.as_posix(),
        ]
        try:
            subprocess.check_call(
                cmd,
                stderr=f,
                stdout=f,
            )
        except subprocess.CalledProcessError:
            temp_path = Path(f.name)
            output = temp_path.read_text()
            raise SnapshotMismatchError(path, output) from None


def run_pyright(path: Path) -> None:
    """
    Check output with pyright.
    """
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    cmd = [
        "uvx",
        "-q",
        *get_with_arguments(),
        "pyright",
        path.as_posix(),
        "--outputjson",
    ]
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                cmd,
                stderr=subprocess.DEVNULL,
                stdout=f,
            )
        except subprocess.CalledProcessError:
            pass
        else:
            return
        finally:
            if config_path.exists():
                config_path.unlink()

        temp_path = Path(f.name)
        output = temp_path.read_text()

        data = json.loads(output).get("generalDiagnostics", [])
        errors: list[dict[str, Any]] = []
        for error in data:
            message = error.get("message", "")
            if any(imsg in message for imsg in IGNORE_PYRIGHT_ERRORS):
                continue
            errors.append(error)

        if errors:
            messages: list[str] = []
            for error in errors:
                file_path = ""
                if error.get("file"):
                    file_path = error["file"]
                if error.get("uri"):
                    file_path = error["uri"]["_filePath"]

                messages.append(
                    "pyright:"
                    f" {file_path}:{error['range']['start']['line']} {error.get('message', '')}",
                )
            raise SnapshotMismatchError(path, "\n".join(messages))


def run_mypy(path: Path) -> None:
    """
    Check output with mypy.
    """
    cmd = ["uvx", "-q", *get_with_arguments(), "mypy", path.as_posix()]
    try:
        output = subprocess.check_output(
            cmd,
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output: str = e.output
        errors: list[str] = []
        for message in output.splitlines():
            if not message or message.startswith("Found"):
                continue
            if any(imsg in message for imsg in IGNORE_MYPY_ERRORS):
                continue
            errors.append(f"mypy: {message}")

        if errors:
            raise SnapshotMismatchError(path, "\n".join(errors)) from None


def run_call(path: Path) -> None:
    """
    Check output by running it.
    """
    if not (path / "__main__.py").exists():
        return
    try:
        subprocess.check_call([sys.executable, path.as_posix()], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(path, f"Cannot be called: {e}") from None


def run_import(path: Path) -> None:
    """
    Check output by installing and importing it.
    """
    if not (path / "__main__.py").exists():
        return

    run_cmd = [
        "uv",
        "run",
        "-q",
        *get_with_arguments(),
        "--with",
        path.parent.as_posix(),
        "python",
        "-c",
        f"import {path.name}",
    ]
    try:
        subprocess.check_call(
            run_cmd,
            stdout=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(path, f"Cannot be imported: {e}") from None


def is_package_dir(path: Path) -> bool:
    """
    Check whether `path` contains a service package.
    """
    if not path.is_dir():
        return False
    if path.name.endswith(".egg-info"):
        return False
    return (path / "__init__.pyi").exists()


def check_snapshot(path: Path) -> None:
    """
    Check package type checkers snapshot.

    Raises:
        SnapshotMismatchError -- If snapshot is not equal to current output.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug(f"Running ruff for {path.name} ...")
    run_ruff(path)
    logger.debug(f"Running mypy for {path.name} ...")
    run_mypy(path)
    logger.debug(f"Running pyright for {path.name} ...")
    run_pyright(path)

    if (path / "__main__.py").exists():
        logger.debug(f"Running call for {path.name} ...")
        run_call(path)
        logger.debug(f"Running import for {path.name} ...")
        run_import(path)


def find_package_path(path: Path) -> Path | None:
    """
    Find package directory inside `path`.
    """
    for package_path in path.iterdir():
        if is_package_dir(package_path):
            return package_path

    return None


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    Config.path = args.path
    logger = setup_logging(logging.DEBUG if args.debug else logging.INFO)
    has_errors = False
    for directory in sorted(args.path.iterdir()):
        if not directory.is_dir():
            continue
        if not directory.name.endswith("_package"):
            continue

        if args.filter and not any(s in directory.as_posix() for s in args.filter):
            continue

        package_path = find_package_path(directory)
        if not package_path:
            continue
        logger.info(f"Checking {directory.name}/{package_path.name} ...")
        try:
            check_snapshot(package_path)
        except SnapshotMismatchError as e:
            logger.warning(e)
            has_errors = True
            if args.exit_on_error:
                break

    if has_errors:
        logger.error("Snapshot mismatch")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
