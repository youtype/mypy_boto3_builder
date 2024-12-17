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
PYRIGHT_IGNORED_MESSAGES = (
    'Import "types_aiobotocore_',
    'Import "mypy_boto3_',
    'Import "types_boto3_',
    'Function with declared return type "NoReturn" cannot return "None"',
    "is marked as overload, but no implementation is provided",
    '"client" overrides symbol of same name in class "ResourceMeta"',
    "must return value on all code paths",
)
MYPY_IGNORED_MESSAGES = ("note:",)

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
    logger: logging.Logger
    args: CLINamespace

    @classmethod
    def get_uvx_cmd(cls) -> tuple[str, ...]:
        """
        Get uvx command prefix.
        """
        result: list[str] = ["uvx", "-q"]
        if cls.args.python_version:
            result.extend(("--python", cls.args.python_version))
        return tuple(result)


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
    python_version: str | None


def parse_args() -> CLINamespace:
    """
    Parse CLI arguments.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-x", "--exit-on-error", action="store_true")
    parser.add_argument("-p", "--path", type=Path, default=ROOT_PATH / "mypy_boto3_output")
    parser.add_argument(
        "--python",
        type=str,
        default=None,
        help="Python version for checkers. Default: None",
    )
    parser.add_argument("filter", nargs="*")
    args = parser.parse_args()
    return CLINamespace(
        debug=args.debug,
        path=args.path,
        filter=args.filter,
        exit_on_error=args.exit_on_error,
        python_version=args.python,
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
        "T",
        "LOG",
        "Q",
        "RSE",
        "RET",
        "TID",
        "TC",
        "S",
        "BLE",
        "ANN",
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
        "E501",  # line-too-long
        "E741",  # ambiguous-variable-name
        "N802",  # invalid-function-name
        "N803",  # invalid-argument-name
        "N812",  # lowercase-imported-as-non-lowercase
        "UP013",  # convert-typed-dict-functional-to-class
        "TC001",  # typing-only-first-party-import
        "TC002",  # typing-only-third-party-import
        "TC003",  # typing-only-standard-library-import
        # ruff does not support conditional import syntax for aio libs
        "UP004",  # useless-object-inheritance
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


def find_ignored_message(message: str, ignored: Sequence[str]) -> str | None:
    """
    Find ignored error if it is present in message.
    """
    for error in ignored:
        if error in message:
            return error
    return None


def run_pyright(path: Path) -> None:
    """
    Check output with pyright.
    """
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    cmd = [
        *Config.get_uvx_cmd(),
        *get_with_arguments(),
        "pyright",
        path.as_posix(),
        "--outputjson",
    ]
    Config.logger.debug(f"Running subprocess: {' '.join(cmd)}")
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
            ignored_message = find_ignored_message(message, PYRIGHT_IGNORED_MESSAGES)
            if ignored_message:
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
    cmd = [*Config.get_uvx_cmd(), *get_with_arguments(), "mypy", path.as_posix()]
    Config.logger.debug(f"Running subprocess: {' '.join(cmd)}")
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
            ignored_message = find_ignored_message(message, MYPY_IGNORED_MESSAGES)
            if ignored_message:
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
        subprocess.check_call(run_cmd, stdout=subprocess.DEVNULL)
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
    logger = Config.logger
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


def get_package_paths(path: Path) -> list[Path]:
    """
    Find package directory inside `path`.
    """
    result = [package_path for package_path in path.iterdir() if is_package_dir(package_path)]
    result.sort(key=lambda x: x.name)
    return result


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    Config.path = args.path
    Config.args = args
    Config.logger = setup_logging(logging.DEBUG if args.debug else logging.INFO)
    logger = Config.logger
    has_errors = False
    for directory in sorted(args.path.iterdir()):
        if not directory.is_dir():
            continue
        if not directory.name.endswith("_package"):
            continue

        if args.filter and not any(
            s in directory.relative_to(args.path).as_posix() for s in args.filter
        ):
            continue

        package_paths = get_package_paths(directory)
        for package_path in package_paths:
            logger.info(f"Checking {package_path.absolute().relative_to(Path.cwd())} ...")
            try:
                check_snapshot(package_path)
            except SnapshotMismatchError as e:
                logger.warning(e)
                has_errors = True
                if args.exit_on_error:
                    break

        if has_errors and args.exit_on_error:
            break

    if has_errors:
        logger.error("Snapshot mismatch")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
