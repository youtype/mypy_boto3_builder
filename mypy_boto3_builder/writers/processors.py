"""
Processors for parsing and writing `boto3` modules.
"""

from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

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
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
    static_files_path: Path,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3_stubs`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed Boto3StubsPackage.
    """
    logger = get_logger()
    package_data = Boto3StubsPackageData
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    boto3_stubs_package = parse_boto3_stubs_package(
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
        package=boto3_stubs_package,
        templates_path=TemplatePath.boto3_stubs,
        static_files_path=static_files_path,
    )

    return boto3_stubs_package


def process_boto3_stubs_lite(
    *,
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
    static_files_path: Path,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3-stubs-lite`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

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
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path, generate_setup=generate_setup, cleanup=True
    )
    package_writer.write_package(
        package=boto3_stubs_package,
        templates_path=TemplatePath.boto3_stubs,
        static_files_path=static_files_path,
        exclude_template_names=[
            "session.pyi.jinja2",
            "__init__.pyi.jinja2",
        ],
    )

    return boto3_stubs_package


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
    logger.debug(f"Writing master to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path, generate_setup=generate_setup, cleanup=True
    )
    package_writer.write_package(
        master_package,
        templates_path=TemplatePath.master,
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
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=False, cleanup=True)
    package_writer.write_docs(
        boto3_stubs_package,
        templates_path=TemplatePath.boto3_stubs_docs,
    )

    return boto3_stubs_package


def process_boto3_stubs_full(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> Boto3StubsPackage:
    """
    Parse and write stubs package `boto3-stubs-full`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed Boto3StubsPackage.
    """
    package_data = Boto3StubsFullPackageData
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    boto3_stubs_package = parse_boto3_stubs_package(
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
        package=boto3_stubs_package,
        templates_path=TemplatePath.boto3_stubs_full,
    )

    return boto3_stubs_package
