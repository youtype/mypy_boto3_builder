"""
Processors for parsing and writing `aiobotocore` modules.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from pathlib import Path

from mypy_boto3_builder.constants import TemplatePath
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import (
    BasePackageData,
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_types_aiobotocore_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.types_aiobotocore_package import TypesAioBotocorePackage
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_types_aiobotocore(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_package: bool,
    version: str,
    static_files_path: Path,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `types-aiobotocore`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    package = parse_types_aiobotocore_package(
        service_names,
        TypesAioBotocorePackageData,
        version,
    )
    logger.debug(f"Writing {package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package,
        templates_path=TemplatePath.types_aiobotocore,
        static_files_path=static_files_path,
    )
    return package


def process_types_aiobotocore_lite(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_package: bool,
    version: str,
    static_files_path: Path,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `types-aiobotocore-lite`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    package = parse_types_aiobotocore_package(
        service_names,
        TypesAioBotocoreLitePackageData,
        version,
    )
    logger.debug(f"Writing {package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_package=generate_package,
        cleanup=True,
    )
    package_writer.write_package(
        package,
        templates_path=TemplatePath.types_aiobotocore,
        static_files_path=static_files_path,
        exclude_template_names=["session.pyi.jinja2"],
    )
    return package


def process_types_aiobotocore_docs(
    output_path: Path,
    service_names: Iterable[ServiceName],
    version: str,
) -> TypesAioBotocorePackage:
    """
    Parse and write package docs.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        version -- Package version

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    package = parse_types_aiobotocore_package(
        service_names,
        TypesAioBotocorePackageData,
        version,
    )

    logger.debug(f"Writing {package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_package=False, cleanup=True)
    package_writer.write_docs(
        package,
        templates_path=TemplatePath.types_aiobotocore_docs,
    )

    return package


def process_types_aiobotocore_full(
    *,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_package: bool,
    version: str,
    package_data: type[BasePackageData],
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `types-aiobotocore-full`.

    Arguments:
        output_path -- Package output path
        service_names -- List of known service names
        generate_package -- Generate ready-to-install or to-use package
        version -- Package version
        package_data -- Package data

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_FULL_NAME}")
    package = parse_types_aiobotocore_package(
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
        package,
        templates_path=TemplatePath.types_aiobotocore_full,
    )

    return package
