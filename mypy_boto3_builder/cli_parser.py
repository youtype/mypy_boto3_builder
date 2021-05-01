"""
CLI parser.
"""
import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence

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


@dataclass
class Namespace:
    log_level: int
    output_path: Path
    service_names: List[ServiceName]
    build_version: str
    installed: bool
    skip_master: bool
    skip_services: bool
    builder_version: str
    generate_docs: bool


def parse_args(args: Sequence[str]) -> Namespace:
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
    parser.add_argument("--docs", action="store_true", help="Generate docs for modules")
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
    return Namespace(
        log_level=logging.DEBUG if result.debug else logging.INFO,
        output_path=result.output_path,
        service_names=result.service_names,
        skip_master=result.skip_master,
        skip_services=result.skip_services,
        build_version=result.build_version,
        installed=result.installed,
        builder_version=result.builder_version,
        generate_docs=result.docs,
    )
