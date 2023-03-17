#!/usr/bin/env python
"""
Integration tests.
"""
import argparse
import difflib
import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from mypy_boto3_builder.utils.nice_path import NicePath

ROOT_PATH = Path(__file__).parent.parent.resolve()
EXAMPLES_PATH = ROOT_PATH / "examples"
PYRIGHT_SNAPSHOTS_PATH = EXAMPLES_PATH / "pyright"
MYPY_SNAPSHOTS_PATH = EXAMPLES_PATH / "mypy"
SCRIPTS_PATH = ROOT_PATH / "scripts"
LOGGER_NAME = "integration"


class SnapshotMismatchError(Exception):
    """
    Exception for e2e failures.
    """


def setup_logging(level: int = 0) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Logging level

    Returns:
        Created Logger.
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

    fast: bool
    update: bool
    services: list[str]


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-f", "--fast", action="store_true")
    parser.add_argument("-u", "--update", action="store_true")
    parser.add_argument("services", nargs="*")
    args = parser.parse_args()
    return CLINamespace(
        fast=args.fast,
        update=args.update,
        services=args.services,
    )


def check_call(cmd: list[str]) -> None:
    """
    Check command exit code and output on error.
    """
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        logger = logging.getLogger(LOGGER_NAME)
        for line in e.output.decode().splitlines():
            logger.error(line)
        raise


def install_master() -> None:
    """
    Build and install `boto3-stubs`.
    """
    check_call([(SCRIPTS_PATH / "build.sh").as_posix(), "--product", "boto3"])
    check_call([(SCRIPTS_PATH / "install.sh").as_posix(), "master"])


def install_service(service_name: str) -> None:
    """
    Build and install `mypy-boto3-*` subpackage.
    """
    check_call(
        [(SCRIPTS_PATH / "build.sh").as_posix(), "-s", service_name, "--product", "boto3-services"]
    )
    check_call([(SCRIPTS_PATH / "install.sh").as_posix(), service_name])


def compare(data: str, snapshot_path: Path, update: bool) -> None:
    """
    Compare tool output with a snapshot.
    """
    data = data.strip()
    logger = logging.getLogger(LOGGER_NAME)
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {NicePath(snapshot_path)}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.info(f"Matched {NicePath(snapshot_path)}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {NicePath(snapshot_path)}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(), data.strip().splitlines(), lineterm=""
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(f"Snapshot {snapshot_path} is different")


def run_pyright(path: Path, update: bool) -> None:
    """
    Run `pyright` and compare output.
    """
    try:
        output = subprocess.check_output(
            ["pyright", path.as_posix(), "--outputjson"],
            stderr=subprocess.DEVNULL,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output

    data = json.loads(output).get("generalDiagnostics", [])
    for diag in data:
        del diag["file"]

    new_data = json.dumps(data, indent=4)
    snapshot_path = PYRIGHT_SNAPSHOTS_PATH / f"{path.name}.json"
    compare(new_data, snapshot_path, update)


def run_mypy(path: Path, update: bool) -> None:
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

    new_data_lines = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    snapshot_path = MYPY_SNAPSHOTS_PATH / f"{path.name}.out"
    compare(new_data, snapshot_path, update)


def run_call(path: Path) -> None:
    """
    Run submodule for sanity.
    """
    subprocess.check_call([sys.executable, path.as_posix()])


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger = setup_logging(logging.INFO)
    if not args.fast:
        logger.info("Installing master...")
        install_master()
    error: BaseException | None = None
    for file in EXAMPLES_PATH.iterdir():
        if "_example.py" not in file.name:
            continue
        service_name = file.name.replace("_example.py", "")
        if args.services and service_name not in args.services:
            continue
        if not args.fast:
            logger.info(f"Installing {service_name}...")
            install_service(service_name)
        try:
            logger.info(f"Running {NicePath(file)} ...")
            run_call(file)
            logger.info(f"Running mypy for {NicePath(file)} ...")
            run_mypy(file, args.update)
            logger.info(f"Running pyright for {NicePath(file)} ...")
            run_pyright(file, args.update)
        except SnapshotMismatchError as e:
            logger.error(e)
            error = e
    if error:
        logger.error(error)
        exit(1)


if __name__ == "__main__":
    main()
