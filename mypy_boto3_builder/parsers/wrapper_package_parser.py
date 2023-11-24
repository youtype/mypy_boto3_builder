"""
Parser that produces `structures.wrapper_package.WrapperPackage`.
"""

from boto3.session import Session
from botocore.config import Config

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.wrapper_package import WrapperPackage
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.named_unions import VerifyTypeDef
from mypy_boto3_builder.utils.boto3_utils import get_boto3_resource


class WrapperPackageParser:
    """
    Parser for boto3-stubs/types-aiobotocore/types-aioboto3 package.

    Arguments:
        session -- boto3 session
        package -- Prepared wrapper package with data
    """

    init_arguments = [
        Argument("region_name", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("api_version", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("use_ssl", TypeSubscript(Type.Optional, [Type.bool]), Type.Ellipsis),
        Argument("verify", VerifyTypeDef, Type.Ellipsis),
        Argument("endpoint_url", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("aws_access_key_id", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("aws_secret_access_key", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument("aws_session_token", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
        Argument(
            "config",
            TypeSubscript(Type.Optional, [ExternalImport.from_class(Config)]),
            Type.Ellipsis,
        ),
    ]

    def __init__(self, session: Session, package: WrapperPackage) -> None:
        self.session = session
        self.package = package
        self._logger = get_logger()

    def _get_service_name_argument(self, service_name: ServiceName) -> Argument:
        """
        Get service_name argument for init functions.
        """
        return Argument(
            "service_name",
            TypeLiteral(
                f"{service_name.class_name}Type",
                [service_name.boto3_name],
            ),
        )

    def parse_clients(self) -> None:
        """
        Extract client data for wrapper package.
        """
        add_overload = len(self.package.service_packages) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in self.package.service_names:
            self._parse_client(service_name, decorators)

    def parse_session_clients(self) -> None:
        """
        Extract client data for wrapper package.
        """
        add_overload = len(self.package.service_packages) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in self.package.service_names:
            package_name = self.package.data.get_service_package_name(service_name)
            service_name_argument = self._get_service_name_argument(service_name)
            return_type = ExternalImport(
                source=ImportString(package_name, ServiceModuleName.client.value),
                name=Client.get_class_name(service_name),
            )
            self.package.session_class.methods.append(
                Method(
                    name="create_client",
                    decorators=decorators,
                    arguments=[
                        Argument("self", None),
                        service_name_argument,
                        *self.init_arguments,
                    ],
                    return_type=return_type,
                    body_lines=["..."],
                )
            )

    def parse_resources(self) -> None:
        """
        Extract resource data for wrapper package.
        """
        resource_service_names: list[ServiceName] = []
        for service_name in self.package.service_names:
            boto3_resource = get_boto3_resource(self.session, service_name)
            if boto3_resource is not None:
                resource_service_names.append(service_name)
        add_overload = len(resource_service_names) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in resource_service_names:
            self._parse_resource(service_name, decorators)

    def _parse_client(self, service_name: ServiceName, decorators: list[TypeAnnotation]) -> None:
        package_name = self.package.data.get_service_package_name(service_name)
        service_name_argument = self._get_service_name_argument(service_name)
        return_type = ExternalImport(
            source=ImportString(package_name, ServiceModuleName.client.value),
            name=Client.get_class_name(service_name),
        )
        client_function = Function(
            name="client",
            decorators=decorators,
            arguments=[
                service_name_argument,
                *self.init_arguments,
            ],
            return_type=return_type,
            body_lines=["..."],
        )
        self.package.init_functions.append(client_function)
        self.package.session_class.methods.append(
            Method(
                name="client",
                decorators=decorators,
                arguments=[
                    Argument("self", None),
                    service_name_argument,
                    *self.init_arguments,
                ],
                return_type=return_type,
                body_lines=["..."],
            )
        )

    def _parse_resource(self, service_name: ServiceName, decorators: list[TypeAnnotation]) -> None:
        package_name = self.package.data.get_service_package_name(service_name)
        service_name_argument = self._get_service_name_argument(service_name)
        return_type = ExternalImport(
            source=ImportString(package_name, ServiceModuleName.service_resource.value),
            name=ServiceResource.get_class_name(service_name),
        )
        resource_function = Function(
            name="resource",
            decorators=decorators,
            arguments=[
                service_name_argument,
                *self.init_arguments,
            ],
            return_type=return_type,
            body_lines=["..."],
        )
        self.package.init_functions.append(resource_function)
        resource_method = Method(
            name="resource",
            decorators=decorators,
            arguments=[
                Argument("self", None),
                service_name_argument,
                *self.init_arguments,
            ],
            return_type=return_type,
            body_lines=["..."],
        )
        self.package.session_class.methods.append(resource_method)
