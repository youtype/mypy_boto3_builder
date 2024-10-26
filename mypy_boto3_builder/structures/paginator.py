"""
Boto3 client Paginator.
"""

import functools
from typing import Self

from botocore.paginate import Paginator as BotocorePaginator

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


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
    ) -> None:
        super().__init__(
            name=name,
            bases=[ExternalImport.from_class(BotocorePaginator)],
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

    def __gt__(self: Self, other: Self) -> bool:
        """
        Compare two annotations for sorting.
        """
        return self.get_sort_key() > other.get_sort_key()

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return self.service_name.get_boto3_doc_link("Paginator", self.paginator_name)

    def get_client_method(self) -> Method:
        """
        Get `get_paginator` method for `Client`.
        """
        return Method(
            name="get_paginator",
            decorators=[Type.overload],
            docstring=self.docstring,
            arguments=[
                Argument.self(),
                Argument(
                    "operation_name",
                    TypeLiteral(f"{self.name}Name", [self.operation_name]),
                ),
            ],
            return_type=ExternalImport(
                source=ImportString("", ServiceModuleName.paginator.value),
                name=self.name,
            ),
        )
