"""
Parsers that produces `structures.wrapper_package.WrapperPackage`.
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
    package = Boto3StubsPackage(package_data, service_names)
    parser = WrapperPackageParser(session, package)
    package.init_functions.extend(parser.get_init_client_functions())
    package.init_functions.extend(parser.get_init_resource_functions())
    package.session_class.methods.extend(parser.get_session_client_methods())
    package.session_class.methods.extend(parser.get_session_resource_methods())
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
    package = TypesAioBotocorePackage(package_data, service_names)
    parser = WrapperPackageParser(session, package)
    package.session_class.methods.extend(parser.get_session_client_methods("create_client"))
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
    package = TypesAioBoto3Package(package_data, service_names)
    parser = WrapperPackageParser(session, package)
    package.init_functions.extend(parser.get_init_client_functions())
    package.init_functions.extend(parser.get_init_resource_functions())
    package.session_class.methods.extend(parser.get_session_client_methods())
    package.session_class.methods.extend(parser.get_session_resource_methods())
    return package
