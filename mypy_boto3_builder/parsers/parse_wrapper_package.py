"""
Parsers that produces `structures.wrapper_package.WrapperPackage`.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.wrapper_package_parser import WrapperPackageParser
from mypy_boto3_builder.postprocessors.aio_imports import replace_imports_with_aio
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.packages.types_aioboto3_package import TypesAioBoto3Package
from mypy_boto3_builder.structures.packages.types_aiobotocore_package import TypesAioBotocorePackage
from mypy_boto3_builder.structures.packages.types_boto3_package import TypesBoto3Package
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


def parse_types_boto3_package(
    service_names: Iterable[ServiceName],
    package_data: BasePackageData,
    version: str,
) -> TypesBoto3Package:
    """
    Parse data for types-boto3 package.

    Arguments:
        service_names -- All available service names
        package_data -- Package data
        version -- Package version

    Returns:
        Boto3StubsPackage structure.
    """
    package = TypesBoto3Package(package_data, service_names, version)
    parser = WrapperPackageParser(package)
    package.init_functions.extend(parser.get_init_client_functions())
    package.init_functions.extend(parser.get_init_resource_functions())
    package.session_class.methods.extend(parser.get_session_client_methods())
    package.session_class.methods.extend(parser.get_session_resource_methods())
    return package


def parse_types_aiobotocore_package(
    service_names: Iterable[ServiceName],
    package_data: BasePackageData,
    version: str,
) -> TypesAioBotocorePackage:
    """
    Parse data for types-aiobotocore package.

    Arguments:
        service_names -- All available service names
        package_data -- Package data
        version -- Package version

    Returns:
        TypesAioBotocorePackage structure.
    """
    package = TypesAioBotocorePackage(package_data, service_names, version)
    parser = WrapperPackageParser(package)
    for method in parser.get_session_client_methods("create_client"):
        method.return_type = TypeSubscript(
            InternalImport("ClientCreatorContext"),
            [method.return_type],
        )
        method.type_ignore = "override"
        package.session_class.methods.append(method)

    replace_imports_with_aio(package.session_class.iterate_types())
    return package


def parse_types_aioboto3_package(
    service_names: Iterable[ServiceName],
    package_data: BasePackageData,
    version: str,
) -> TypesAioBoto3Package:
    """
    Parse data for types-aioboto3 package.

    Arguments:
        service_names -- All available service names
        package_data -- Package data
        version -- Package version

    Returns:
        TypesAioBoto3Package structure.
    """
    package = TypesAioBoto3Package(package_data, service_names, version)
    parser = WrapperPackageParser(package)
    for method in parser.get_session_client_methods():
        method.return_type = TypeSubscript(
            ExternalImport(Import.aiobotocore + "session", "ClientCreatorContext"),
            [method.return_type],
        )
        package.session_class.methods.append(method)
    for method in parser.get_session_resource_methods():
        method.return_type = TypeSubscript(
            InternalImport("ResourceCreatorContext"),
            [method.return_type],
        )
        package.session_class.methods.append(method)

    replace_imports_with_aio(package.session_class.iterate_types())
    return package
