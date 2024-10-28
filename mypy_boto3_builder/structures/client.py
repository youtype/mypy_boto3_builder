"""
Boto3 Client.
"""

from collections.abc import Iterator
from typing import Final

from botocore.client import BaseClient

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.utils.type_checks import is_typed_dict


class Client(ClassRecord):
    """
    Service Client.
    """

    _OWN_METHOD_NAMES: Final = {
        "get_waiter",
        "get_paginator",
        "exceptions",
    }

    def __init__(self, name: str, service_name: ServiceName, boto3_client: BaseClient) -> None:
        super().__init__(name=name)
        self.service_name = service_name
        self.boto3_client = boto3_client
        self.exceptions_class = ClassRecord(name="Exceptions")
        self.bases = [ExternalImport.from_class(BaseClient)]
        self.client_error_class = ClassRecord(
            name="BotocoreClientError",
            attributes=[
                Attribute(name="MSG_TEMPLATE", type_annotation=Type.str),
            ],
            bases=[ExternalImport.from_class(Exception)],
            methods=[
                Method(
                    name="__init__",
                    arguments=(
                        Argument.self(),
                        Argument("error_response", Type.MappingStrAny),
                        Argument("operation_name", Type.str),
                    ),
                    return_type=Type.none,
                    body_lines=[
                        "self.response: Dict[str, Any]",
                        "self.operation_name: str",
                    ],
                ),
            ],
        )

    def __hash__(self) -> int:
        """
        Calculate hash from client service name.
        """
        return hash(self.service_name)

    @property
    def alias_name(self) -> str:
        """
        Class alias name for safe import.
        """
        return "Client"

    @staticmethod
    def get_class_name(service_name: ServiceName) -> str:
        """
        Get class name for ServiceName.
        """
        return f"{service_name.class_name}Client"

    @property
    def boto3_doc_link(self) -> str:
        """
        List to boto3 docs page.
        """
        return self.service_name.get_boto3_doc_link("Client")

    def get_all_names(self) -> list[str]:
        """
        Get a list of names for `__all__` statement.
        """
        return [self.name]

    @property
    def own_methods(self) -> Iterator[Method]:
        """
        Get a list of auto-generated methods.
        """
        for method in self.methods:
            if method.name not in self._OWN_METHOD_NAMES:
                yield method

    def get_exceptions_property(self) -> Method:
        """
        Generate Client exceptions property.
        """
        return Method(
            name="exceptions",
            decorators=[ExternalImport.from_class(property)],
            arguments=[
                Argument.self(),
            ],
            return_type=InternalImport(
                name=self.exceptions_class.name,
                module_name=ServiceModuleName.client,
                service_name=self.service_name,
                stringify=False,
            ),
            docstring=f"{self.name} exceptions.",
        )

    def get_required_import_records(self) -> set[ImportRecord]:
        """
        Extract import records from required type annotations.
        """
        result = super().get_required_import_records()
        result.update(Type.DictStrAny.get_import_records())
        return result

    def get_example_method(self) -> Method | None:
        """
        Get a nice method with return TypedDict for documentation.
        """
        for method in self.methods:
            if not method.request_type_annotation:
                continue
            if not method.return_type:
                continue
            if not is_typed_dict(method.return_type):
                continue

            return method

        return None
