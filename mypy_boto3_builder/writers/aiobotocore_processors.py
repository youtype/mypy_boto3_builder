"""
Processors for parsing and writing `aiobotocore` modules.
"""
from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import AIOBOTOCORE_STUBS_STATIC_PATH, TEMPLATES_PATH
from mypy_boto3_builder.logger import get_logger
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
    logger.debug("Parsing aiobotocore stubs")
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session=session, service_names=service_names
    )
    aiobotocore_stubs_package.version = version
    logger.debug(f"Writing aiobotocore stubs to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=AIOBOTOCORE_STUBS_STATIC_PATH,
    )
    return aiobotocore_stubs_package


def process_aiobotocore_service(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    generate_setup: bool,
    service_names: Iterable[ServiceName],
    version: str,
):
    """
    Parse and write service package `mypy_aiobotocore_*`.

    Arguments:
        session -- boto3 session
        service_name -- Target service name
        output_path -- Package output path
        generate_setup -- Generate ready-to-install or to-use package
        service_names -- List of known service names
        version -- Package version

    Return:
        Parsed ServicePackage.
    """
    pass


def process_aiobotocore_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
):
    """
    Parse and write master package docs.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed AioBotocoreStubsPackage.
    """


def process_aiobotocore_service_docs(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    service_names: Iterable[ServiceName],
):
    """
    Parse and write service package docs.

    Arguments:
        session -- boto3 session
        service_name -- Target service name
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed ServicePackage.
    """
    pass
