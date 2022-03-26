"""
Parser that produces `structures.Boto3StubsPackage`.
"""
from collections.abc import Iterable

from boto3.session import Session
from botocore.config import Config

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.package_data import BasePackageData, Boto3StubsPackageData
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.utils.boto3_utils import get_region_name_literal


def parse_boto3_stubs_package(
    session: Session, service_names: Iterable[ServiceName], package_data: type[BasePackageData]
) -> Boto3StubsPackage:
    """
    Parse data for boto3_stubs package.

    Arguments:
        session -- boto3 session.
        service_names -- All available service names.

    Returns:
        Boto3StubsPackage structure.
    """
    result = Boto3StubsPackage(package_data, service_names=service_names)
    for service_name in result.service_names:
        result.service_packages.append(
            parse_fake_service_package(session, service_name, package_data)
        )

    init_arguments = [
        Argument("region_name", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("api_version", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("use_ssl", TypeSubscript(Type.Optional, [Type.bool]), Type.Ellipsis),
        Argument(
            "verify",
            TypeSubscript(Type.Union, [Type.bool, Type.str, Type.none]),
            Type.Ellipsis,
        ),
        Argument("endpoint_url", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("aws_access_key_id", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("aws_secret_access_key", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("aws_session_token", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("config", TypeSubscript(Type.Optional, [TypeClass(Config)]), Type.Ellipsis),
    ]

    client_function_decorators: list[TypeAnnotation] = []
    if len(result.service_packages) > 1:
        client_function_decorators.append(Type.overload)
    for service_package in result.service_packages:
        package_name = Boto3StubsPackageData.get_service_package_name(service_package.service_name)
        service_argument = Argument(
            "service_name",
            TypeLiteral(
                service_package.service_name.class_name + "Type",
                [service_package.service_name.boto3_name],
            ),
        )
        client_function = Function(
            name="client",
            decorators=client_function_decorators,
            docstring="",
            arguments=[
                service_argument,
                *init_arguments,
            ],
            return_type=ExternalImport(
                source=ImportString(package_name, ServiceModuleName.client.value),
                name=service_package.client.name,
            ),
            body_lines=["..."],
        )
        result.init_functions.append(client_function)
        result.session_class.methods.append(
            Method(
                name="client",
                decorators=client_function_decorators,
                docstring="",
                arguments=[
                    Argument("self", None),
                    service_argument,
                    *init_arguments,
                ],
                return_type=ExternalImport(
                    source=ImportString(package_name, ServiceModuleName.client.value),
                    name=service_package.client.name,
                ),
                body_lines=["..."],
            )
        )

    service_resource_packages = [i for i in result.service_packages if i.service_resource]
    resource_function_decorators: list[TypeAnnotation] = []
    if len(service_resource_packages) > 1:
        resource_function_decorators.append(Type.overload)
    for service_package in service_resource_packages:
        assert service_package.service_resource
        package_name = Boto3StubsPackageData.get_service_package_name(service_package.service_name)
        service_argument = Argument(
            "service_name",
            TypeLiteral(
                service_package.service_name.class_name + "Type",
                [service_package.service_name.boto3_name],
            ),
        )
        resource_function = Function(
            name="resource",
            decorators=resource_function_decorators,
            docstring="",
            arguments=[
                service_argument,
                *init_arguments,
            ],
            return_type=ExternalImport(
                source=ImportString(package_name, ServiceModuleName.service_resource.value),
                name=service_package.service_resource.name,
            ),
            body_lines=["..."],
        )
        result.init_functions.append(resource_function)
        result.session_class.methods.append(
            Method(
                name="resource",
                decorators=resource_function_decorators,
                docstring="",
                arguments=[
                    Argument("self", None),
                    service_argument,
                    *init_arguments,
                ],
                return_type=ExternalImport(
                    source=ImportString(package_name, ServiceModuleName.service_resource.value),
                    name=service_package.service_resource.name,
                ),
                body_lines=["..."],
            )
        )

    region_name_literal = get_region_name_literal(session, service_names)
    if region_name_literal:
        region_name_literal.name = "_RegionName"
        result.literals.append(region_name_literal)

    return result
