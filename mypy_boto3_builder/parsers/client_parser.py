"""
Parser for botocore Client, produces `structures.Client`.

Copyright 2025 Vlad Emelianov
"""

from botocore.client import ClientMeta
from botocore.errorfactory import ClientExceptionsFactory
from botocore.exceptions import ClientError

from mypy_boto3_builder.constants import CLIENT
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.service_stub_map import get_stub_method_map
from mypy_boto3_builder.utils.strings import get_class_prefix


class ClientParser:
    """
    Parser for botocore Client, produces `structures.Client`.

    Arguments:
        service_name -- Target service name.
        shape_parser -- ShapeParser instance.
    """

    def __init__(
        self,
        service_name: ServiceName,
        shape_parser: ShapeParser,
    ) -> None:
        self.name = CLIENT
        self.alias = service_name.get_client_name()
        self.service_name = service_name
        self.shape_parser = shape_parser
        self._logger = get_logger()

    def _parse_method_map(self) -> dict[str, Method]:
        shape_method_map = self.shape_parser.get_client_method_map()
        stub_method_map = get_stub_method_map(self.service_name, self.name)
        for method in stub_method_map.values():
            self.shape_parser.create_request_type_annotation(
                method=method,
                name=f"{self.name}{get_class_prefix(method.name)}Request",
            )
        return {**shape_method_map, **stub_method_map}

    def _parse_exception_class_attributes(self) -> list[Attribute]:
        result: list[Attribute] = []
        client_exceptions = ClientExceptionsFactory().create_client_exceptions(
            self.shape_parser.service_model
        )
        for exception_class_name in dir(client_exceptions):
            if exception_class_name.startswith("_"):
                continue
            if not exception_class_name[0].isupper():
                continue
            result.append(
                Attribute(
                    exception_class_name,
                    TypeSubscript(
                        Type.Type,
                        [ExternalImport.from_class(ClientError, alias="BotocoreClientError")],
                    ),
                ),
            )
        return result

    def parse(self) -> Client:
        """
        Parse botocore Client.

        Returns:
            Client structure.
        """
        self._logger.debug(f"Parsing {self.alias}", tags=self.alias)

        result = Client(
            name=self.alias,
            service_name=self.service_name,
        )

        method_map = self._parse_method_map()
        result.methods.append(result.get_exceptions_property())
        result.methods.extend(method_map.values())

        result.attributes.append(Attribute("meta", ExternalImport.from_class(ClientMeta)))

        result.exceptions_class.attributes.extend(self._parse_exception_class_attributes())

        return result
