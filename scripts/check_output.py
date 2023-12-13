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
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

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
)


class SnapshotMismatchError(Exception):
    """
    Main snapshot mismatch exception.
    """


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
    formatter = logging.Formatter("%(levelname)s %(message)s", datefmt="%H:%M:%S")
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
    filter: List[str]
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


def run_flake8(path: Path) -> None:
    """
    Check output with flake8.
    """
    ignore_errors = [
        "E203",
        "W503",
        "E501",
        "E704",
        "D200",
        "D107",
        "D401",
        "D105",
        "D205",
        "D400",
        "D101",
        "D102",
        "D403",
        "N802",
        "N803",
        "B014",
    ]
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "flake8",
                    "--ignore",
                    ",".join(ignore_errors),
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
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                ["npx", "pyright", path.as_posix(), "--outputjson"],
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
        errors: List[Dict[str, Any]] = []
        for error in data:
            message = error.get("message", "")
            if any(imsg in message for imsg in IGNORE_PYRIGHT_ERRORS):
                continue
            errors.append(error)

        if errors:
            messages: List[str] = []
            for error in errors:
                file_path = ""
                if error.get("file"):
                    file_path = error["file"]
                if error.get("uri"):
                    file_path = error["uri"]["_filePath"]

                messages.append(
                    "pyright:"
                    f" {file_path}:{error['range']['start']['line']} {error.get('message', '')}"
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
        output: str = e.output
        errors: List[str] = []
        for message in output.splitlines():
            if not message or message.startswith("Found"):
                continue
            if any(imsg in message for imsg in IGNORE_MYPY_ERRORS):
                continue
            errors.append(f"mypy: {message}")

        if errors:
            raise SnapshotMismatchError("\n".join(errors)) from None


def run_call(path: Path) -> None:
    """
    Check output by running it.
    """
    if not (path / "__main__.py").exists():
        return
    try:
        subprocess.check_call([sys.executable, path.as_posix()], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(f"Path {path} cannot be imported: {e}") from None


def run_import(path: Path) -> None:
    """
    Check output by installing and importing it.
    """
    if not (path / "__main__.py").exists():
        return
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--no-input", path.parent.as_posix()],
            stdout=subprocess.DEVNULL,
        )
        if (path / "__main__.py").exists():
            subprocess.check_call(
                [sys.executable, "-c", f"import {path.name}"],
                stdout=subprocess.DEVNULL,
            )
        subprocess.check_call(
            [sys.executable, "-m", "pip", "uninstall", "--no-input", "-y", path.name],
            stdout=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(f"Path {path} cannot be imported: {e}") from None


def is_package_dir(path: Path) -> bool:
    """
    Check whether `path` contains a service package.
    """
    if not path.is_dir():
        return False
    if path.name.endswith(".egg-info"):
        return False
    if (path / "__init__.pyi").exists():
        return True
    return False


def check_snapshot(path: Path) -> None:
    """
    Check package type checkers snapshot.

    Raises:
        SnapshotMismatchError -- If snapshot is not equal to current output.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug(f"Running flake8 for {path.name} ...")
    run_flake8(path)
    logger.debug(f"Running mypy for {path.name} ...")
    run_mypy(path)
    logger.debug(f"Running pyright for {path.name} ...")
    run_pyright(path)

    if (path / "__main__.py").exists():
        logger.debug(f"Running call for {path.name} ...")
        run_call(path)
        logger.debug(f"Running import for {path.name} ...")
        run_import(path)


def find_package_path(path: Path) -> Optional[Path]:
    """
    Find package directory inside `path`.
    """
    for package_path in path.iterdir():
        if is_package_dir(package_path):
            return package_path


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger = setup_logging(logging.DEBUG if args.debug else logging.INFO)
    has_errors = False
    for folder in sorted(args.path.iterdir()):
        if not folder.name.endswith("_package"):
            continue

        if args.filter and not any(s in folder.as_posix() for s in args.filter):
            continue

        package_path = find_package_path(folder)
        if not package_path:
            continue
        logger.info(f"Checking {folder.name}/{package_path.name} ...")
        try:
            check_snapshot(package_path)
        except SnapshotMismatchError as e:
            logger.error(e)
            has_errors = True
            if args.exit_on_error:
                break

    if has_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
