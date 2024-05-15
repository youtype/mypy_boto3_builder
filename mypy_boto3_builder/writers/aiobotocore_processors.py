"""
Processors for parsing and writing `aiobotocore` modules.
"""

from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import AIOBOTOCORE_STUBS_STATIC_PATH, TEMPLATES_PATH
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import (
    BasePackageData,
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_aiobotocore_stubs_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.types_aiobotocore_package import TypesAioBotocorePackage
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `aiobotocore-stubs`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocorePackageData
    )
    aiobotocore_stubs_package.version = version
    logger.debug(f"Writing {aiobotocore_stubs_package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path, generate_setup=generate_setup, cleanup=True
    )
    package_writer.write_package(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=AIOBOTOCORE_STUBS_STATIC_PATH,
    )
    return aiobotocore_stubs_package


def process_aiobotocore_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `aiobotocore-stubs-lite`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocoreLitePackageData
    )
    aiobotocore_stubs_package.version = version
    logger.debug(f"Writing {aiobotocore_stubs_package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_setup=generate_setup,
        cleanup=True,
    )
    package_writer.write_package(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=AIOBOTOCORE_STUBS_STATIC_PATH,
        exclude_template_names=["session.pyi.jinja2"],
    )
    return aiobotocore_stubs_package


def process_aiobotocore_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> TypesAioBotocorePackage:
    """
    Parse and write master package docs.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocorePackageData
    )

    logger.debug(f"Writing {aiobotocore_stubs_package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=False, cleanup=True)
    package_writer.write_docs(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore_stubs_docs",
    )

    return aiobotocore_stubs_package


def process_aiobotocore_stubs_full(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
    package_data: type[BasePackageData],
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `types-aiobotocore-full`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
        package_data -- Package data

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    boto3_stubs_package = parse_aiobotocore_stubs_package(
        session=session,
        service_names=service_names,
        package_data=package_data,
    )
    boto3_stubs_package.version = version
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path, generate_setup=generate_setup, cleanup=True
    )
    package_writer.write_package(
        boto3_stubs_package,
        templates_path=TEMPLATES_PATH / "types-aiobotocore-full",
    )

    return boto3_stubs_package
