"""
Parser that produces `structures.Boto3StubsPackage`.
"""

from collections.abc import Iterable

from boto3.session import Session

from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.wrapper_package_parser import WrapperPackageParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.types_aioboto3_package import TypesAioBoto3Package
from mypy_boto3_builder.structures.types_aiobotocore_package import TypesAioBotocorePackage


def parse_boto3_stubs_package(
    session: Session, service_names: Iterable[ServiceName], package_data: type[BasePackageData]
) -> Boto3StubsPackage:
    """
    Parse data for boto3-stubs package.

    Arguments:
        session -- boto3 session
        service_names -- All available service names
        package_data -- Package data

    Returns:
        Boto3StubsPackage structure.
    """
    package = Boto3StubsPackage(package_data, service_names=service_names)
    parser = WrapperPackageParser(session, package)
    parser.parse_clients()
    parser.parse_resources()
    return package


def parse_aiobotocore_stubs_package(
    session: Session, service_names: Iterable[ServiceName], package_data: type[BasePackageData]
) -> TypesAioBotocorePackage:
    """
    Parse data for types-aiobotocore package.

    Arguments:
        session -- boto3 session
        service_names -- All available service names
        package_data -- Package data

    Returns:
        TypesAioBotocorePackage structure.
    """
    package = TypesAioBotocorePackage(package_data, service_names=service_names)
    parser = WrapperPackageParser(session, package)
    parser.parse_session_clients()
    return package


def parse_types_aioboto3_package(
    session: Session, service_names: Iterable[ServiceName], package_data: type[BasePackageData]
) -> TypesAioBoto3Package:
    """
    Parse data for types-aioboto3 package.

    Arguments:
        session -- boto3 session
        service_names -- All available service names
        package_data -- Package data

    Returns:
        TypesAioBoto3Package structure.
    """
    package = TypesAioBoto3Package(package_data, service_names=service_names)
    parser = WrapperPackageParser(session, package)
    parser.parse_clients()
    parser.parse_resources()
    return package
