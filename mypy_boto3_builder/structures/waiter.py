"""
Boto3 client Waiter.

Copyright 2024 Vlad Emelianov
"""

import functools
from typing import Self

from botocore.waiter import Waiter as BotocoreWaiter

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


@functools.total_ordering
class Waiter(ClassRecord):
    """
    Boto3 client Waiter.
    """

    def __init__(
        self,
        name: str,
        waiter_name: str,
        attribute_name: str,
        service_name: ServiceName,
    ) -> None:
        super().__init__(
            name=name,
            bases=[ExternalImport.from_class(BotocoreWaiter)],
        )
        self.waiter_name = waiter_name
        self.attribute_name = attribute_name
        self.service_name = service_name

    def __hash__(self) -> int:
        """
        Hash paginators by name.
        """
        return hash(self.get_sort_key())

    def get_sort_key(self) -> str:
        """
        Sort paginators by name.
        """
        return self.name

    def __eq__(self, other: object) -> bool:
        """
        Whether two annotations are equal.
        """
        if not isinstance(other, Waiter):
            raise BuildInternalError(f"{other} is not Waiter")

        return self.get_sort_key() == other.get_sort_key()

    def __gt__(self, other: Self) -> bool:
        """
        Compare two annotations for sorting.
        """
        return self.get_sort_key() > other.get_sort_key()

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to waiter boto3 docs.
        """
        return (
            f"{self.service_name.boto3_doc_link_parent}"
            f"/waiter/{self.waiter_name}.html"
            f"#{self.service_name.class_name}.Waiter.{self.waiter_name}"
        )

    def get_client_method(self) -> Method:
        """
        Get `get_waiter` method for `Client`.
        """
        return Method(
            name="get_waiter",
            decorators=[Type.overload],
            docstring="Returns an object that can wait for some condition.",
            arguments=(
                Argument.self(),
                Argument("waiter_name", TypeLiteral(f"{self.name}Name", [self.attribute_name])),
            ),
            return_type=ExternalImport(
                source=Import.local(ServiceModuleName.waiter.value),
                name=self.name,
            ),
            type_ignore="override",
        )
