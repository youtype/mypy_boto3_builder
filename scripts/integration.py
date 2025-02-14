#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "loguru",
# ]
# ///
"""
Integration tests.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import argparse
import difflib
import enum
import json
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING

from loguru import logger

if TYPE_CHECKING:
    from collections.abc import Sequence

ROOT_PATH = Path(__file__).parent.parent.resolve()
PYRIGHT_CONFIG_PATH = Path(__file__).parent / "pyrightconfig_output.json"
TYPES_BOTO3_PATH = ROOT_PATH / "integration" / "types-boto3"
TYPES_AIOBOTO3_PATH = ROOT_PATH / "integration" / "types-aioboto3"
SCRIPTS_PATH = ROOT_PATH / "scripts"
TEMP_PATH = Path(tempfile.TemporaryDirectory().name)


class Config:
    """
    Config for integration tests.
    """

    python_version: str | None = None
    products: tuple[Product, ...] = ()
    install_paths: Sequence[Path] = ()

    @classmethod
    def get_uvx_arguments(cls) -> list[str]:
        """
        Get `uvx` arguments.
        """
        result: list[str] = ["-q"]
        if cls.python_version:
            result.extend(["--python", cls.python_version])
        with_libraries = list(chain.from_iterable(p.prerequisites for p in cls.products))
        for library_name in with_libraries:
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

    name: str
    examples_path: Path
    prerequisites: tuple[str, ...] = ()
    build_products: Sequence[str] = ()

    def get_service_names(self, filter_names: Sequence[str]) -> tuple[str, ...]:
        """
        Find service names from examples.
        """
        result: list[str] = []
        for file in self.examples_path.iterdir():
            if not file.name.endswith("_example.py"):
                continue
            service_name = file.name.replace("_example.py", "")
            if filter_names and service_name not in filter_names:
                continue
            result.append(service_name)

        return tuple(result)


class ProductChoices(enum.Enum):
    """
    Product to test.
    """

    types_boto3 = Product(
        name="types-boto3",
        examples_path=ROOT_PATH / "integration" / "types_boto3",
        prerequisites=("boto3",),
        build_products=("types-boto3", "types-boto3-services"),
    )
    types_boto3_lite = Product(
        name="types-boto3-lite",
        examples_path=ROOT_PATH / "integration" / "types_boto3_lite",
        prerequisites=("boto3",),
        build_products=("types-boto3-lite", "types-boto3-services"),
    )
    types_boto3_full = Product(
        name="types-boto3-full",
        examples_path=ROOT_PATH / "integration" / "types_boto3",
        prerequisites=("boto3",),
        build_products=("types-boto3", "types-boto3-full"),
    )
    types_boto3_custom = Product(
        name="types-boto3-custom",
        examples_path=ROOT_PATH / "integration" / "types_boto3",
        prerequisites=("boto3",),
        build_products=("types-boto3-custom",),
    )
    boto3_stubs = Product(
        name="boto3-stubs",
        examples_path=ROOT_PATH / "integration" / "boto3_stubs",
        prerequisites=("boto3",),
        build_products=("boto3", "boto3-services"),
    )
    boto3_stubs_lite = Product(
        name="boto3-stubs-lite",
        examples_path=ROOT_PATH / "integration" / "boto3_stubs_lite",
        prerequisites=("boto3",),
        build_products=("boto3-lite", "boto3-services"),
    )
    boto3_stubs_full = Product(
        name="boto3-stubs-full",
        examples_path=ROOT_PATH / "integration" / "boto3_stubs",
        prerequisites=("boto3",),
        build_products=("boto3", "boto3-full"),
    )
    boto3_stubs_custom = Product(
        name="boto3-stubs-custom",
        examples_path=ROOT_PATH / "integration" / "boto3_stubs",
        prerequisites=("boto3",),
        build_products=("boto3-custom",),
    )
    types_aioboto3 = Product(
        name="types-aioboto3",
        prerequisites=("aioboto3",),
        examples_path=ROOT_PATH / "integration" / "types_aioboto3",
        build_products=("types-boto3-lite", "aioboto3", "aiobotocore", "aiobotocore-services"),
    )
    types_aioboto3_lite = Product(
        name="types-aioboto3-lite",
        prerequisites=("aioboto3",),
        examples_path=ROOT_PATH / "integration" / "types_aioboto3_lite",
        build_products=("types-boto3-lite", "aioboto3-lite", "aiobotocore", "aiobotocore-services"),
    )
    types_aioboto3_full = Product(
        name="types-aioboto3-full",
        examples_path=ROOT_PATH / "integration" / "types_aioboto3",
        prerequisites=("aioboto3",),
        build_products=("types-boto3-lite", "aioboto3", "aiobotocore-full"),
    )
    types_aioboto3_custom = Product(
        name="types-aioboto3-custom",
        examples_path=ROOT_PATH / "integration" / "types_aioboto3",
        prerequisites=("aioboto3",),
        build_products=("types-boto3-lite", "aioboto3-custom"),
    )
    types_aiobotocore = Product(
        name="types-aiobotocore",
        prerequisites=("aiobotocore",),
        examples_path=ROOT_PATH / "integration" / "types_aiobotocore",
        build_products=("aiobotocore", "aiobotocore-services"),
    )
    types_aiobotocore_lite = Product(
        name="types-aiobotocore-lite",
        prerequisites=("aiobotocore",),
        examples_path=ROOT_PATH / "integration" / "types_aiobotocore_lite",
        build_products=("aiobotocore-lite", "aiobotocore-services"),
    )
    types_aiobotocore_full = Product(
        name="types-aiobotocore-full",
        examples_path=ROOT_PATH / "integration" / "types_aiobotocore",
        prerequisites=("aiobotocore",),
        build_products=("aiobotocore", "aiobotocore-full"),
    )
    types_aiobotocore_custom = Product(
        name="types-aiobotocore-custom",
        examples_path=ROOT_PATH / "integration" / "types_aiobotocore",
        prerequisites=("aiobotocore",),
        build_products=("aiobotocore-custom",),
    )

    @classmethod
    def get_names(cls) -> tuple[str, ...]:
        """
        Get product names.
        """
        return tuple(i.value.name for i in cls)

    @classmethod
    def get(cls, name: str) -> Product:
        """
        Get product by name.
        """
        for product in cls:
            if product.value.name == name:
                return product.value
        raise ValueError(f"Unknown product: {name}")


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

    log_level: str
    products: tuple[Product, ...]
    fast: bool
    update: bool
    services: tuple[str, ...]
    output_path: Path
    wheel: bool
    python_version: str | None


def parse_args() -> CLINamespace:
    """
    CLI parser.
    """
    product_names = ProductChoices.get_names()
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-f", "--fast", action="store_true")
    parser.add_argument("-u", "--update", action="store_true")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-p",
        "--product",
        nargs="*",
        choices=product_names,
        default=product_names,
        help="Product to test. Default: all",
    )
    parser.add_argument(
        "--python",
        type=str,
        default=None,
        help="Python version for checkers. Default: None",
    )
    parser.add_argument("--filter", type=str, default=None, help="Filter for services")
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
        log_level="DEBUG" if args.debug else "INFO",
        products=tuple(ProductChoices.get(name) for name in args.product),
        fast=args.fast,
        update=args.update,
        services=tuple(args.filter) if args.filter else (),
        output_path=args.output_path or TEMP_PATH,
        wheel=args.wheel,
        python_version=args.python,
    )


def check_call(cmd: Sequence[str]) -> str:
    """
    Check command exit code and output on error.
    """
    logger.debug(f"Running process: {' '.join(cmd)}")
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        for line in e.output.decode().splitlines():
            logger.warning(line)
        raise


def build_packages(
    products: Sequence[Product],
    output_path: Path,
    output_type: str,
    filter_service_names: Sequence[str],
) -> list[Path]:
    """
    Build and install stubs.

    - boto3: `types-boto3`
    - aioboto3: `types-aioboto3` and `types-aiobotocore`
    """
    prerequisites: set[str] = set()
    build_products: set[str] = set()
    service_names: set[str] = set()
    for product in products:
        build_products.update(product.build_products)
        prerequisites.update(product.prerequisites)
        service_names.update(product.get_service_names(filter_service_names))

    with_prerequisites = list(chain.from_iterable(("--with", i) for i in sorted(prerequisites)))
    cmd = [
        "uvx",
        "--no-cache",
        *with_prerequisites,
        "--with",
        ".",
        "mypy_boto3_builder",
        output_path.as_posix(),
        "--services",
        *sorted(service_names),
        "--product",
        *sorted(build_products),
        "--no-smart-version",
        "--output-type",
        output_type,
    ]
    check_call(cmd)
    return list(output_path.iterdir())


def compare(data: str, snapshot_path: Path, *, update: bool) -> None:
    """
    Compare tool output with a snapshot.
    """
    data = data.strip()
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
    logger.debug(f"Running process: {' '.join(cmd)}")
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
    logger.debug(f"Running process: {' '.join(cmd)}")
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


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "level": args.log_level,
                "format": (
                    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                    "<level>{level: <8}</level> | "
                    f"<cyan>{Path(__file__).stem}</cyan> - "
                    "<white>{message}</white>"
                ),
            }
        ]
    )
    Config.python_version = args.python_version
    Config.products = args.products
    error: Exception | None = None

    if not args.fast:
        logger.info("Building packages...")
        install_paths = build_packages(
            products=args.products,
            output_path=args.output_path,
            output_type="wheel" if args.wheel else "package",
            filter_service_names=args.services,
        )
        Config.install_paths = install_paths

    for product in args.products:
        service_names = product.get_service_names(args.services)
        if not service_names:
            logger.warning(f"No matching services found for {product.name}")

        for service_name in service_names:
            file_path = product.examples_path / f"{service_name}_example.py"
            logger.info(f"Checking {product.name} {service_name}...")
            try:
                logger.debug(f"Running mypy for {print_path(file_path)} ...")
                snapshot_path = product.examples_path / "mypy" / f"{file_path.name}.out"
                run_mypy(file_path, snapshot_path, update=args.update)
                logger.debug(f"Running pyright for {print_path(file_path)} ...")
                snapshot_path = product.examples_path / "pyright" / f"{file_path.name}.json"
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
