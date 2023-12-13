#!/usr/bin/env python
"""
Integration tests.
"""
import argparse
import difflib
import enum
import json
import logging
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from mypy_boto3_builder.utils.path import print_path

ROOT_PATH = Path(__file__).parent.parent.resolve()
PYRIGHT_CONFIG_PATH = Path(__file__).parent / "pyrightconfig_output.json"
EXAMPLES_PATH = ROOT_PATH / "examples"
AIO_EXAMPLES_PATH = ROOT_PATH / "aio_examples"
SCRIPTS_PATH = ROOT_PATH / "scripts"
LOGGER_NAME = "integration"


class SnapshotMismatchError(Exception):
    """
    Exception for e2e failures.
    """


class Product(enum.Enum):
    """
    Product to test.
    """

    boto3 = "boto3"
    aioboto3 = "aioboto3"


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

    log_level: int
    product: Product
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
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-p",
        "--product",
        choices=("boto3", "aioboto3"),
        default="boto3",
        help="Product to test. Default: boto3",
    )
    parser.add_argument("services", nargs="*")
    args = parser.parse_args()
    return CLINamespace(
        log_level=logging.DEBUG if args.debug else logging.INFO,
        product=Product(args.product),
        fast=args.fast,
        update=args.update,
        services=args.services,
    )


def check_call(cmd: Sequence[str]) -> None:
    """
    Check command exit code and output on error.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        for line in e.output.decode().splitlines():
            logger.error(line)
        raise


def install_master(product: Product) -> None:
    """
    Build and install master stubs.

    - boto3: `boto3-stubs`
    - aioboto3: `types-aioboto3` and `types-aiobotocore`
    """
    if product == Product.boto3:
        check_call([print_path(SCRIPTS_PATH / "build.sh"), "--product", "boto3"])
        check_call([print_path(SCRIPTS_PATH / "install.sh"), "master"])

    if product == Product.aioboto3:
        check_call([print_path(SCRIPTS_PATH / "build.sh"), "--product", "aioboto3", "aiobotocore"])
        check_call([print_path(SCRIPTS_PATH / "install_aiobotocore.sh"), "master"])


def install_service(service_name: str, product: Product) -> None:
    """
    Build and install a service subpackage.

    - boto3: `mypy-boto3-*`
    - aioboto3: `types-aiobotocore-*`
    """
    if product == Product.boto3:
        check_call(
            [
                print_path(SCRIPTS_PATH / "build.sh"),
                "-s",
                service_name,
                "--product",
                "boto3-services",
            ]
        )
        check_call([print_path(SCRIPTS_PATH / "install.sh"), service_name])
    if product == Product.aioboto3:
        check_call(
            [
                print_path(SCRIPTS_PATH / "build.sh"),
                "-s",
                service_name,
                "--product",
                "aiobotocore-services",
            ]
        )
        check_call([print_path(SCRIPTS_PATH / "install_aiobotocore.sh"), service_name])


def get_examples_path(product: Product) -> Path:
    """
    Get path to examples for a product.
    """
    if product == Product.boto3:
        return EXAMPLES_PATH
    if product == Product.aioboto3:
        return AIO_EXAMPLES_PATH

    raise ValueError(f"Unknown product: {product}")


def compare(data: str, snapshot_path: Path, update: bool) -> None:
    """
    Compare tool output with a snapshot.
    """
    data = data.strip()
    logger = logging.getLogger(LOGGER_NAME)
    if not snapshot_path.exists():
        snapshot_path.write_text(data)
        logger.info(f"Created {print_path(snapshot_path)}")
        return

    old_data = snapshot_path.read_text().strip()
    if old_data == data:
        logger.debug(f"Matched {print_path(snapshot_path)}")
        return

    if update:
        snapshot_path.write_text(data)
        logger.info(f"Updated {print_path(snapshot_path)}")
        return

    diff = difflib.unified_diff(
        old_data.strip().splitlines(), data.strip().splitlines(), lineterm=""
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(f"Snapshot {snapshot_path} is different")


def run_pyright(path: Path, snapshot_path: Path, update: bool) -> None:
    """
    Run `pyright` and compare output.
    """
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    try:
        output = subprocess.check_output(
            ["pyright", path.as_posix(), "--outputjson"],
            stderr=subprocess.DEVNULL,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output
    finally:
        os.remove(config_path)

    data = json.loads(output).get("generalDiagnostics", [])
    for diag in data:
        del diag["file"]

    new_data = json.dumps(data, indent=4)
    compare(new_data, snapshot_path, update)


def run_mypy(path: Path, snapshot_path: Path, update: bool) -> None:
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

    new_data_lines: list[str] = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    compare(new_data, snapshot_path, update)


def run_call(path: Path) -> None:
    """
    Run submodule for sanity.
    """
    logger = logging.getLogger(LOGGER_NAME)
    try:
        subprocess.check_output([sys.executable, path.as_posix()])
    except subprocess.CalledProcessError as e:
        logger.error(f"Call output: {e.output.decode()}")
        logger.error(f"Call error: {e.stderr.decode()}")
        raise


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger = setup_logging(args.log_level)
    if not args.fast:
        logger.info("Installing master...")
        install_master(args.product)
    error: Exception | None = None
    examples_path = get_examples_path(args.product)
    for file in examples_path.iterdir():
        if not file.name.endswith("_example.py"):
            continue
        service_name = file.name.replace("_example.py", "")
        logger.info(f"Checking {service_name}...")
        if args.services and service_name not in args.services:
            continue
        if not args.fast:
            logger.debug(f"Installing {service_name}...")
            install_service(service_name, args.product)
        try:
            logger.debug(f"Running {print_path(file)} ...")
            run_call(file)
            logger.debug(f"Running mypy for {print_path(file)} ...")
            snapshot_path = examples_path / "mypy" / f"{file.name}.out"
            run_mypy(file, snapshot_path, args.update)
            logger.debug(f"Running pyright for {print_path(file)} ...")
            snapshot_path = examples_path / "pyright" / f"{file.name}.json"
            run_pyright(file, snapshot_path, args.update)
        except SnapshotMismatchError as e:
            logger.error(e)
            error = e
    if error:
        logger.error(error)
        exit(1)


if __name__ == "__main__":
    main()
