"""
Boto3 client Paginator.

Copyright 2024 Vlad Emelianov
"""

import functools
from typing import Self

from botocore.paginate import Paginator as BotocorePaginator

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


@functools.total_ordering
class Paginator(ClassRecord):
    """
    Boto3 client Paginator.
    """

    def __init__(
        self,
        name: str,
        paginator_name: str,
        operation_name: str,
        service_name: ServiceName,
        return_type: FakeAnnotation | None = None,
    ) -> None:
        base_class = ExternalImport.from_class(BotocorePaginator)
        super().__init__(
            name=name,
            bases=[base_class if not return_type else TypeSubscript(base_class, [return_type])],
        )
        self.operation_name = operation_name
        self.paginator_name = paginator_name
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
        if not isinstance(other, Paginator):
            raise BuildInternalError(f"{other} is not Paginator")

        return self.get_sort_key() == other.get_sort_key()

    def __gt__(self, other: Self) -> bool:
        """
        Compare two annotations for sorting.
        """
        return self.get_sort_key() > other.get_sort_key()

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return (
            f"{self.service_name.boto3_doc_link_parent}"
            f"/paginator/{self.paginator_name}.html"
            f"#{self.service_name.class_name}.Paginator.{self.paginator_name}"
        )

    def get_client_method(self) -> Method:
        """
        Get `get_paginator` method for `Client`.
        """
        return Method(
            name="get_paginator",
            decorators=[Type.overload],
            docstring="Create a paginator for an operation.",
            arguments=[
                Argument.self(),
                Argument(
                    "operation_name",
                    TypeLiteral(f"{self.name}Name", [self.operation_name]),
                ),
            ],
            return_type=ExternalImport(
                source=Import.local(ServiceModuleName.paginator.value),
                name=self.name,
            ),
            type_ignore="override",
        )
