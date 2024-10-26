"""
Parser that produces `structures.wrapper_package.WrapperPackage`.
"""

from typing import Final

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
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_maps.named_unions import VerifyTypeDef
from mypy_boto3_builder.utils.boto3_utils import get_boto3_resource
from mypy_boto3_builder.utils.type_checks import get_optional


class WrapperPackageParser:
    """
    Parser for boto3-stubs/types-aiobotocore/types-aioboto3 package.

    Arguments:
        session -- boto3 session
        package -- Prepared wrapper package with data
    """

    _INIT_ARGUMENTS: Final[tuple[Argument, ...]] = (
        Argument("region_name", get_optional(Type.str), Type.Ellipsis),
        Argument("api_version", get_optional(Type.str), Type.Ellipsis),
        Argument("use_ssl", get_optional(Type.bool), Type.Ellipsis),
        Argument("verify", VerifyTypeDef, Type.Ellipsis),
        Argument("endpoint_url", get_optional(Type.str), Type.Ellipsis),
        Argument("aws_access_key_id", get_optional(Type.str), Type.Ellipsis),
        Argument("aws_secret_access_key", get_optional(Type.str), Type.Ellipsis),
        Argument("aws_session_token", get_optional(Type.str), Type.Ellipsis),
        Argument(
            "config",
            get_optional(ExternalImport.from_class(Config)),
            Type.Ellipsis,
        ),
    )

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

    def get_client_service_names(self) -> tuple[ServiceName, ...]:
        """
        Get service names that have a Client.
        """
        return self.package.service_names

    def get_resource_service_names(self) -> list[ServiceName]:
        """
        Get service names that have a ServiceResource.
        """
        result: list[ServiceName] = []
        for service_name in self.package.service_names:
            boto3_resource = get_boto3_resource(self.session, service_name)
            if boto3_resource is not None:
                result.append(service_name)
        return result

    def get_init_client_functions(self, name: str = "client") -> list[Function]:
        """
        Extract client data for wrapper package.
        """
        result: list[Function] = []
        client_service_names = self.get_client_service_names()
        add_overload = len(client_service_names) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in client_service_names:
            package_name = self.package.data.get_service_package_name(service_name)
            service_name_argument = self._get_service_name_argument(service_name)
            return_type = ExternalImport(
                source=ImportString(package_name, ServiceModuleName.client.value),
                name=Client.get_class_name(service_name),
            )
            arguments = [
                service_name_argument,
                *self._INIT_ARGUMENTS,
            ]
            client_function = Function(
                name=name,
                decorators=decorators,
                arguments=arguments,
                return_type=return_type,
                body_lines=["..."],
            )
            result.append(client_function)
        return result

    def get_session_client_methods(self, name: str = "client") -> list[Method]:
        """
        Extract client data for wrapper package.
        """
        result: list[Method] = []
        client_service_names = self.get_client_service_names()
        add_overload = len(client_service_names) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in client_service_names:
            package_name = self.package.data.get_service_package_name(service_name)
            service_name_argument = self._get_service_name_argument(service_name)
            return_type = ExternalImport(
                source=ImportString(package_name, ServiceModuleName.client.value),
                name=Client.get_class_name(service_name),
            )
            arguments = [
                Argument.self(),
                service_name_argument,
                *self._INIT_ARGUMENTS,
            ]
            method = Method(
                name=name,
                decorators=decorators,
                arguments=arguments,
                return_type=return_type,
                body_lines=["..."],
            )
            result.append(method)
        return result

    def get_init_resource_functions(self, name: str = "resource") -> list[Function]:
        """
        Extract resource data for wrapper package.
        """
        result: list[Function] = []
        resource_service_names = self.get_resource_service_names()
        add_overload = len(resource_service_names) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in resource_service_names:
            package_name = self.package.data.get_service_package_name(service_name)
            service_name_argument = self._get_service_name_argument(service_name)
            return_type = ExternalImport(
                source=ImportString(package_name, ServiceModuleName.service_resource.value),
                name=ServiceResource.get_class_name(service_name),
            )
            arguments = [
                service_name_argument,
                *self._INIT_ARGUMENTS,
            ]
            resource_function = Function(
                name=name,
                decorators=decorators,
                arguments=arguments,
                return_type=return_type,
                body_lines=["..."],
            )
            result.append(resource_function)
        return result

    def get_session_resource_methods(self, name: str = "resource") -> list[Method]:
        """
        Extract resource data for wrapper package.
        """
        result: list[Method] = []
        resource_service_names = self.get_resource_service_names()
        add_overload = len(resource_service_names) > 1
        decorators = [Type.overload] if add_overload else []
        for service_name in resource_service_names:
            package_name = self.package.data.get_service_package_name(service_name)
            service_name_argument = self._get_service_name_argument(service_name)
            return_type = ExternalImport(
                source=ImportString(package_name, ServiceModuleName.service_resource.value),
                name=ServiceResource.get_class_name(service_name),
            )
            arguments = [
                Argument.self(),
                service_name_argument,
                *self._INIT_ARGUMENTS,
            ]
            resource_method = Method(
                name=name,
                decorators=decorators,
                arguments=arguments,
                return_type=return_type,
                body_lines=["..."],
            )
            result.append(resource_method)
        return result
