"""
Processors for parsing and writing `boto3` modules.
"""
from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import (
    BOTO3_STUBS_STATIC_PATH,
    BOTOCORE_STUBS_STATIC_PATH,
    TEMPLATES_PATH,
)
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import Boto3StubsLitePackageData, Boto3StubsPackageData
from mypy_boto3_builder.parsers.boto3_stubs_package import parse_boto3_stubs_package
from mypy_boto3_builder.parsers.master_package import parse_master_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.botocore_stubs_package import BotocoreStubsPackage
from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_boto3_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3_stubs`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsPackageData
    logger.debug(f"Parsing {Boto3StubsPackageData.PYPI_NAME}")
    boto3_stubs_package = parse_boto3_stubs_package(session, service_names, package_data)
    boto3_stubs_package.version = version
    logger.debug(f"Writing {Boto3StubsPackageData.PYPI_NAME} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        boto3_stubs_package,
        templates_path=TEMPLATES_PATH / "boto3-stubs",
        static_files_path=BOTO3_STUBS_STATIC_PATH,
    )

    return boto3_stubs_package


def process_boto3_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3-stubs-lite`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsLitePackageData
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    boto3_stubs_package = parse_boto3_stubs_package(
        session=session,
        service_names=service_names,
        package_data=package_data,
    )
    boto3_stubs_package.version = version
    logger.debug(f"Writing {package_data.PYPI_NAME} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        boto3_stubs_package,
        templates_path=TEMPLATES_PATH / "boto3-stubs",
        static_files_path=BOTO3_STUBS_STATIC_PATH,
        exclude_template_names=[
            "session.pyi.jinja2",
            "__init__.pyi.jinja2",
        ],
    )

    return boto3_stubs_package


def process_botocore_stubs(
    output_path: Path,
    generate_setup: bool,
    version: str,
) -> None:
    """
    Parse and write stubs package `botocore_stubs`.

    Arguments:
        output_path -- Package output path
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
    """
    logger = get_logger()
    logger.debug(f"Writing botocore stubs to {NicePath(output_path)}")

    botocore_stubs_package = BotocoreStubsPackage()
    botocore_stubs_package.version = version
    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        botocore_stubs_package,
        templates_path=TEMPLATES_PATH / "botocore-stubs",
        static_files_path=BOTOCORE_STUBS_STATIC_PATH,
    )


def process_master(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> MasterPackage:
    """
    Parse and write master package `mypy_boto3`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed MasterPackage.
    """
    logger = get_logger()
    logger.debug("Parsing master")
    master_package = parse_master_package(session, service_names)
    master_package.version = version
    logger.debug(f"Writing master to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        master_package,
        templates_path=TEMPLATES_PATH / "master",
    )

    return master_package


def process_boto3_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> Boto3StubsPackage:
    """
    Parse and write master package docs.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsPackageData
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    boto3_stubs_package = parse_boto3_stubs_package(session, service_names, package_data)
    logger.debug(f"Writing {package_data.PYPI_NAME} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path)
    package_writer.write_docs(
        boto3_stubs_package,
        templates_path=TEMPLATES_PATH / "boto3_stubs_docs",
    )

    return boto3_stubs_package
