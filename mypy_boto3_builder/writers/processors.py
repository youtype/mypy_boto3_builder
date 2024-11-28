"""
Processors for parsing and writing `boto3` modules.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from pathlib import Path

from mypy_boto3_builder.constants import TemplatePath
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.mypy_boto3_package import parse_mypy_boto3_package
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_types_boto3_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.mypy_boto3_package import MypyBoto3Package
from mypy_boto3_builder.structures.types_boto3_package import TypesBoto3Package
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_types_boto3(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
    generate_package: bool,
    version: str,
    static_files_path: Path,
) -> TypesBoto3Package:
    """
    Parse and write stubs package `types-boto3`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed TypesBoto3Package.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    package = parse_types_boto3_package(
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
        templates_path=TemplatePath.types_boto3,
        static_files_path=static_files_path,
    )

    return package


def process_types_boto3_lite(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
    generate_package: bool,
    version: str,
    static_files_path: Path,
) -> TypesBoto3Package:
    """
    Parse and write stubs package `types-boto3-lite`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed TypesBoto3Package.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    package = parse_types_boto3_package(
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
        templates_path=TemplatePath.types_boto3,
        static_files_path=static_files_path,
        exclude_template_names=[
            "session.pyi.jinja2",
            "__init__.pyi.jinja2",
        ],
    )

    return package


def process_mypy_boto3(
    output_path: Path,
    service_names: Iterable[ServiceName],
    version: str,
    *,
    generate_package: bool,
) -> MypyBoto3Package:
    """
    Parse and write package `mypy_boto3`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version
        generate_package -- Generate ready-to-install or to-use package

    Return:
        Parsed MypyBoto3Package.
    """
    logger = get_logger()
    logger.debug("Parsing mypy_boto3")
    package = parse_mypy_boto3_package(service_names=service_names, version=version)
    logger.debug(f"Writing mypy_boto3 to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package,
        templates_path=TemplatePath.mypy_boto3,
    )

    return package


def process_types_boto3_docs(
    output_path: Path,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
    version: str,
) -> TypesBoto3Package:
    """
    Parse and write package docs.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version

    Return:
        Parsed TypesBoto3Package.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    package = parse_types_boto3_package(
        service_names=service_names,
        package_data=package_data,
        version=version,
    )
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_package=False, cleanup=True)
    package_writer.write_docs(
        package=package,
        templates_path=TemplatePath.types_boto3_docs,
    )

    return package


def process_types_boto3_full(
    output_path: Path,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
    version: str,
    *,
    generate_package: bool,
) -> TypesBoto3Package:
    """
    Parse and write stubs package `types-boto3-full`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version
        generate_package -- Generate ready-to-install or to-use package

    Return:
        Parsed TypesBoto3Package.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_FULL_NAME}")
    package = parse_types_boto3_package(
        service_names=service_names,
        package_data=package_data,
        version=version,
    )
    logger.debug(f"Writing {package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package=package,
        templates_path=TemplatePath.types_boto3_full,
    )

    return package
