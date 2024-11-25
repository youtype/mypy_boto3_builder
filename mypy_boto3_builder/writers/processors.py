"""
Processors for parsing and writing `boto3` modules.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from pathlib import Path

from mypy_boto3_builder.constants import TemplatePath
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import (
    Boto3StubsFullPackageData,
    Boto3StubsLitePackageData,
    Boto3StubsPackageData,
)
from mypy_boto3_builder.parsers.master_package import parse_master_package
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_boto3_stubs_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_boto3_stubs(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_package: bool,
    version: str,
    static_files_path: Path,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3_stubs`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsPackageData
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    package = parse_boto3_stubs_package(
        service_names=service_names,
        package_data=package_data,
        version=version,
    )
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package=package,
        templates_path=TemplatePath.boto3_stubs,
        static_files_path=static_files_path,
    )

    return package


def process_boto3_stubs_lite(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_package: bool,
    version: str,
    static_files_path: Path,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3-stubs-lite`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsLitePackageData
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    package = parse_boto3_stubs_package(
        service_names=service_names,
        package_data=package_data,
        version=version,
    )
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package=package,
        templates_path=TemplatePath.boto3_stubs,
        static_files_path=static_files_path,
        exclude_template_names=[
            "session.pyi.jinja2",
            "__init__.pyi.jinja2",
        ],
    )

    return package


def process_master(
    output_path: Path,
    service_names: Iterable[ServiceName],
    version: str,
    *,
    generate_package: bool,
) -> MasterPackage:
    """
    Parse and write master package `mypy_boto3`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version
        generate_package -- Generate ready-to-install or to-use package

    Return:
        Parsed MasterPackage.
    """
    logger = get_logger()
    logger.debug("Parsing master")
    package = parse_master_package(service_names=service_names, version=version)
    logger.debug(f"Writing master to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package,
        templates_path=TemplatePath.master,
    )

    return package


def process_boto3_stubs_docs(
    output_path: Path,
    service_names: Iterable[ServiceName],
    version: str,
) -> Boto3StubsPackage:
    """
    Parse and write master package docs.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsPackageData
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    package = parse_boto3_stubs_package(
        service_names=service_names,
        package_data=package_data,
        version=version,
    )
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_package=False, cleanup=True)
    package_writer.write_docs(
        package=package,
        templates_path=TemplatePath.boto3_stubs_docs,
    )

    return package


def process_boto3_stubs_full(
    output_path: Path,
    service_names: Iterable[ServiceName],
    version: str,
    *,
    generate_setup: bool,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3-stubs-full`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version
        generate_setup -- Generate ready-to-install or to-use package

    Return:
        Parsed Boto3StubsPackage.
    """
    package_data = Boto3StubsFullPackageData
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_FULL_NAME}")
    package = parse_boto3_stubs_package(
        service_names=service_names,
        package_data=package_data,
        version=version,
    )
    logger.debug(f"Writing {package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_setup,
        cleanup=True,
    )
    package_writer.write_package(
        package=package,
        templates_path=TemplatePath.boto3_stubs_full,
    )

    return package
