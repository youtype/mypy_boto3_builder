"""
Boto3 Client.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator
from typing import Final

from botocore.client import BaseClient
from botocore.errorfactory import BaseClientExceptions

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
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

    def __init__(self, name: str, service_name: ServiceName) -> None:
        super().__init__(name=name, bases=[ExternalImport.from_class(BaseClient)])
        self.service_name = service_name
        self.exceptions_class = ClassRecord(
            name="Exceptions",
            bases=(ExternalImport.from_class(BaseClientExceptions),),
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

    @property
    def boto3_doc_link(self) -> str:
        """
        List to boto3 docs page.
        """
        return (
            f"{self.service_name.boto3_doc_link_parent}.html"
            f"#{self.service_name.class_name}.Client"
        )

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
            ),
            docstring=f"{self.name} exceptions.",
            boto3_doc_link=self.boto3_doc_link,
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
