"""
Processors for parsing and writing `aiobotocore` modules.
"""
from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import AIOBOTOCORE_STUBS_STATIC_PATH, TEMPLATES_PATH
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import (
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.parsers.aiobotocore_stubs_package import parse_aiobotocore_stubs_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.aiobotocore_stubs_package import AioBotocoreStubsPackage
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
    """
    Parse and write stubs package `aiobotocore-stubs`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed AioBotocoreStubsPackage.
    """
    logger = get_logger()
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocorePackageData
    )
    aiobotocore_stubs_package.version = version
    logger.debug(f"Writing {aiobotocore_stubs_package.pypi_name} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
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
) -> AioBotocoreStubsPackage:
    """
    Parse and write stubs package `aiobotocore-stubs-lite`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed AioBotocoreStubsPackage.
    """
    logger = get_logger()
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocoreLitePackageData
    )
    aiobotocore_stubs_package.version = version
    logger.debug(f"Writing {aiobotocore_stubs_package.pypi_name} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
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
) -> AioBotocoreStubsPackage:
    """
    Parse and write master package docs.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed AioBotocoreStubsPackage.
    """
    logger = get_logger()
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocorePackageData
    )

    logger.debug(f"Writing {aiobotocore_stubs_package.pypi_name} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path)
    package_writer.write_docs(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore_stubs_docs",
    )

    return aiobotocore_stubs_package
