"""
CLI parser.
"""
import argparse
import logging
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import List

import pkg_resources

from mypy_boto3_builder.constants import PACKAGE_NAME, PROG_NAME, Product


def get_absolute_path(path: str) -> Path:
    """
    Get absolute path from a string.

    Arguments:
        path -- String containing path.

    Returns:
        Absolute path.
    """
    return Path(path).absolute()


@dataclass
class Namespace:
    """
    CLI arguments namespace.
    """

    log_level: int
    output_path: Path
    service_names: list[str]
    build_version: str
    installed: bool
    products: List[Product]
    builder_version: str
    list_services: bool
    partial_overload: bool
    skip_published: bool
    disable_smart_version: bool


def parse_args(args: Sequence[str]) -> Namespace:
    """
    Main CLI parser for builder.

    Returns:
        Argument parser.
    """
    try:
        version = pkg_resources.get_distribution(PACKAGE_NAME).version
    except pkg_resources.DistributionNotFound:
        version = "0.0.0"

    parser = argparse.ArgumentParser(PROG_NAME, description="Builder for mypy-boto3.")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-b",
        "--build-version",
        help="Set custom output version, otherwise smart versioning is used.",
    )
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument(
        "--product",
        dest="products",
        type=Product,
        choices=list(Product),
        nargs="+",
        default=[Product.boto3, Product.boto3_services],
        help="Select package to create annotations for",
    )
    parser.add_argument(
        "--skip-published", action="store_true", help="Skip packages that are already on PyPI"
    )
    parser.add_argument(
        "--no-smart-version",
        action="store_true",
        help="Disable version bump if package is already published",
    )
    parser.add_argument(
        "--panic",
        action="store_true",
        help="Raise exception on logger warning and above",
    )
    parser.add_argument(
        "output_path", metavar="OUTPUT_PATH", help="Output path", type=get_absolute_path
    )
    parser.add_argument(
        "-s",
        "--services",
        dest="service_names",
        nargs="*",
        metavar="SERVICE_NAME",
        help=(
            "List of AWS services, by default all services are used."
            " Use `updated` to build only services updated in the release."
            " Use `all` to build all services."
        ),
        default=["all"],
    )
    parser.add_argument(
        "--partial-overload",
        action="store_true",
        help="Build boto3-stubs client/service overload only for selected services",
    )
    parser.add_argument(
        "--installed",
        action="store_true",
        help="Generate already installed packages for typings folder.",
    )
    parser.add_argument(
        "--list-services",
        action="store_true",
        help="List supported boto3 service names.",
    )
    result = parser.parse_args(args)
    result.builder_version = version
    return Namespace(
        log_level=logging.DEBUG if result.debug else logging.INFO,
        output_path=result.output_path,
        service_names=result.service_names,
        products=result.products,
        build_version=result.build_version,
        installed=result.installed,
        builder_version=result.builder_version,
        list_services=result.list_services,
        partial_overload=result.partial_overload,
        skip_published=result.skip_published,
        disable_smart_version=result.no_smart_version,
    )
