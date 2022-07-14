"""
Parser that produces `structures.TypesAioBoto3Package`.
"""
from collections.abc import Iterable

from boto3.session import Session

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.types_aioboto3_package import TypesAioBoto3Package
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


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
        AioBotocoreStubsPackage structure.
    """
    result = TypesAioBoto3Package(package_data, service_names=service_names)
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
        Argument(
            "config",
            TypeSubscript(
                Type.Optional, [ExternalImport(ImportString("aiobotocore", "config"), "AioConfig")]
            ),
            Type.Ellipsis,
        ),
    ]

    client_function_decorators: list[TypeAnnotation] = []
    if len(result.service_packages) > 1:
        client_function_decorators.append(Type.overload)
    for service_package in result.service_packages:
        service_argument = Argument(
            "service_name",
            TypeLiteral(
                service_package.service_name.class_name + "Type",
                [service_package.service_name.boto3_name],
            ),
        )
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
                    source=ImportString(
                        package_data.get_service_package_name(service_package.service_name),
                        ServiceModuleName.client.value,
                    ),
                    name=service_package.client.name,
                ),
                body_lines=["..."],
                is_async=False,
            )
        )

    service_resource_packages = [i for i in result.service_packages if i.service_resource]
    resource_function_decorators: list[TypeAnnotation] = []
    if len(service_resource_packages) > 1:
        resource_function_decorators.append(Type.overload)
    for service_package in service_resource_packages:
        assert service_package.service_resource
        package_name = package_data.get_service_package_name(service_package.service_name)
        service_argument = Argument(
            "service_name",
            TypeLiteral(
                service_package.service_name.class_name + "Type",
                [service_package.service_name.boto3_name],
            ),
        )
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

    return result
