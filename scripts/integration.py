#!/usr/bin/env python
"""
Integration tests.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import argparse
import difflib
import enum
import json
import logging
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from mypy_boto3_builder.cli_parser import CLINamespace as BuilderCLINamespace
from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.enums.product import Product as BuilderProduct
from mypy_boto3_builder.main import run as run_builder

ROOT_PATH = Path(__file__).parent.parent.resolve()
PYRIGHT_CONFIG_PATH = Path(__file__).parent / "pyrightconfig_output.json"
EXAMPLES_PATH = ROOT_PATH / "examples"
AIO_EXAMPLES_PATH = ROOT_PATH / "aio_examples"
SCRIPTS_PATH = ROOT_PATH / "scripts"
LOGGER_NAME = "integration"
TEMP_PATH = Path(tempfile.TemporaryDirectory().name)


class Config:
    """
    Config for integration tests.
    """

    args: CLINamespace
    logger: logging.Logger
    install_paths: Sequence[Path] = ()

    @classmethod
    def get_uvx_arguments(cls) -> list[str]:
        """
        Get `uvx` arguments.
        """
        result: list[str] = ["-q"]
        for library_name in cls.args.product.with_libraries:
            result.extend(["--with", library_name])
        for install_path in cls.install_paths:
            result.extend(["--with", install_path.as_posix()])

        return result


class SnapshotMismatchError(Exception):
    """
    Exception for e2e failures.
    """

    def __init__(self, path: Path) -> None:
        super().__init__(f"Snapshot {path} is different")


@dataclass
class Product:
    """
    Product to test.
    """

    examples_path: Path
    prerequisites: tuple[str, ...] = ()
    with_libraries: tuple[str, ...] = ()
    build_products: Sequence[BuilderProduct] = ()


class ProductChoices(enum.Enum):
    """
    Product to test.
    """

    boto3 = Product(
        examples_path=EXAMPLES_PATH,
        with_libraries=("boto3",),
        build_products=(BuilderProduct.types_boto3, BuilderProduct.types_boto3_services),
    )
    aioboto3 = Product(
        prerequisites=("aioboto3",),
        examples_path=AIO_EXAMPLES_PATH,
        with_libraries=("aioboto3",),
        build_products=(
            BuilderProduct.types_boto3_lite,
            BuilderProduct.aioboto3,
            BuilderProduct.aiobotocore,
            BuilderProduct.aiobotocore_services,
        ),
    )
    boto3_custom = Product(
        examples_path=EXAMPLES_PATH,
        with_libraries=("boto3",),
        build_products=(BuilderProduct.types_boto3_custom,),
    )
    aioboto3_custom = Product(
        examples_path=AIO_EXAMPLES_PATH,
        with_libraries=(
            "boto3",
            "aioboto3",
        ),
        build_products=(
            BuilderProduct.types_boto3_lite,
            BuilderProduct.aioboto3_custom,
        ),
    )


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Logging level

    Returns:
        Created Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s %(name)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S"
    )
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


def print_path(path: Path) -> str:
    """
    Get path as a string relative to current workdir.
    """
    if path.is_absolute():
        cwd = Path.cwd()
        if path == cwd or path.parts <= cwd.parts:
            return path.as_posix()

        try:
            path = path.relative_to(cwd)
        except ValueError:
            return str(path)

    if len(path.parts) == 1:
        return f"./{path.as_posix()}"

    return path.as_posix()


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    log_level: int
    product: Product
    fast: bool
    update: bool
    services: tuple[str, ...]
    output_path: Path
    wheel: bool


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
        choices=[i.name for i in ProductChoices],
        default=ProductChoices.boto3.name,
        help=f"Product to test. Default: {ProductChoices.boto3.name}",
    )
    parser.add_argument("services", nargs="*")
    parser.add_argument(
        "-o",
        "--output-path",
        type=Path,
        required=False,
        help="Packages output path",
    )
    parser.add_argument("-w", "--wheel", action="store_true", help="Build wheel packages")
    args = parser.parse_args()
    return CLINamespace(
        log_level=logging.DEBUG if args.debug else logging.INFO,
        product=ProductChoices[args.product].value,
        fast=args.fast,
        update=args.update,
        services=tuple(args.services),
        output_path=args.output_path or TEMP_PATH,
        wheel=args.wheel,
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
            logger.warning(line)
        raise


def build_packages(
    product: Product,
    service_names: list[str],
    output_path: Path,
    output_type: OutputType,
    log_level: int,
) -> list[Path]:
    """
    Build and install stubs.

    - boto3: `types-boto3`
    - aioboto3: `types-aioboto3` and `types-aiobotocore`
    """
    if product.prerequisites:
        check_call([sys.executable, "-m", "pip", "install", *product.prerequisites])

    run_builder(
        BuilderCLINamespace(
            log_level=log_level,
            output_path=output_path,
            service_names=service_names,
            build_version="",
            output_types=[output_type],
            products=list(product.build_products),
            disable_smart_version=True,
            download_static_stubs=False,
            skip_published=False,
            partial_overload=False,
            list_services=False,
        )
    )
    return list(output_path.iterdir())


def compare(data: str, snapshot_path: Path, *, update: bool) -> None:
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
        old_data.strip().splitlines(),
        data.strip().splitlines(),
        lineterm="",
    )
    for line in diff:
        logger.warning(line)
    raise SnapshotMismatchError(snapshot_path)


def run_pyright(path: Path, snapshot_path: Path, *, update: bool) -> None:
    """
    Run `pyright` and compare output.
    """
    config_path = ROOT_PATH / "pyrightconfig.json"
    shutil.copyfile(PYRIGHT_CONFIG_PATH, config_path)
    cmd = ["uvx", *Config.get_uvx_arguments(), "pyright", path.as_posix(), "--outputjson"]
    Config.logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, encoding="utf8")
    except subprocess.CalledProcessError as e:
        output = e.output
    finally:
        Path(config_path).unlink(missing_ok=True)

    data = json.loads(output).get("generalDiagnostics", [])
    for diag in data:
        if "file" in diag:
            del diag["file"]
        if "uri" in diag:
            del diag["uri"]

    new_data = json.dumps(data, indent=4)
    compare(new_data, snapshot_path, update=update)


def run_mypy(path: Path, snapshot_path: Path, *, update: bool) -> None:
    """
    Run `mypy` and compare output.
    """
    cmd = ["uvx", *Config.get_uvx_arguments(), "mypy", path.as_posix(), "--no-incremental"]
    Config.logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, encoding="utf8")
    except subprocess.CalledProcessError as e:
        output = e.output

    new_data_lines: list[str] = []
    for line in output.splitlines():
        if line.endswith("defined here"):
            continue
        new_data_lines.append(line)
    new_data = "\n".join(new_data_lines)
    compare(new_data, snapshot_path, update=update)


def get_service_names(args: CLINamespace) -> list[str]:
    """
    Get service names from config.
    """
    service_names: list[str] = []
    for file in args.product.examples_path.iterdir():
        if not file.name.endswith("_example.py"):
            continue
        service_name = file.name.replace("_example.py", "")
        if args.services and service_name not in args.services:
            continue
        service_names.append(service_name)

    return service_names


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger = setup_logging(args.log_level)
    Config.args = args
    Config.logger = logger
    error: Exception | None = None
    service_names = get_service_names(args)
    logger.debug(f"Running for service names: {' '.join(service_names)}")

    if not args.fast:
        logger.info("Building packages...")
        install_paths = build_packages(
            product=args.product,
            service_names=service_names,
            output_path=args.output_path,
            output_type=OutputType.wheel if args.wheel else OutputType.package,
            log_level=args.log_level,
        )
        Config.install_paths = install_paths

    for service_name in service_names:
        file_path = args.product.examples_path / f"{service_name}_example.py"
        logger.info(f"Checking {service_name}...")
        try:
            logger.debug(f"Running mypy for {print_path(file_path)} ...")
            snapshot_path = args.product.examples_path / "mypy" / f"{file_path.name}.out"
            run_mypy(file_path, snapshot_path, update=args.update)
            logger.debug(f"Running pyright for {print_path(file_path)} ...")
            snapshot_path = args.product.examples_path / "pyright" / f"{file_path.name}.json"
            run_pyright(file_path, snapshot_path, update=args.update)
        except SnapshotMismatchError as e:
            logger.warning(f"Snapshot mismatch: {e}")
            error = e

    if error:
        logger.error(error)
        sys.exit(1)

    if TEMP_PATH.exists():
        shutil.rmtree(TEMP_PATH)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
