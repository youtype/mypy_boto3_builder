"""
CLI parser.
"""
import argparse
from pathlib import Path
from typing import Sequence

import pkg_resources

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog


def get_absolute_path(path: str) -> Path:
    """
    Get absolute path from a string.

    Arguments:
        path -- String containing path.

    Returns:
        Absolute path.
    """
    return Path(path).absolute()


def get_service_name(name: str) -> ServiceName:
    """
    Convert boto3 service name to ServiceName.

    Arguments:
        name -- Service name.

    Raises:
        argparse.ArgumentTypeError -- If service not found.
    """
    try:
        return ServiceNameCatalog.find(name)
    except ValueError:
        pass

    return ServiceNameCatalog.create(name)


def parse_args(args: Sequence[str]) -> argparse.Namespace:
    """
    Main CLI parser for builder.

    Returns:
        Argument parser.
    """
    try:
        version = pkg_resources.get_distribution("mypy-boto3-builder").version
    except pkg_resources.DistributionNotFound:
        version = "0.0.0"

    parser = argparse.ArgumentParser("mypy_boto3_builder", description="Builder for mypy-boto3.")
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-b",
        "--build-version",
        help="Set custom output version, otherwise boto3 version is used.",
    )
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument(
        "--skip-master",
        action="store_true",
        help="Whether to skip master and stubs modules",
    )
    parser.add_argument(
        "--skip-services", action="store_true", help="Whether to skip service modules"
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
        help="List of AWS services, by default all services are used",
        type=get_service_name,
        default=[],
    )
    parser.add_argument(
        "--installed",
        action="store_true",
        help="Generate already installed packages for typings folder.",
    )
    result = parser.parse_args(args)
    result.builder_version = version
    return result
