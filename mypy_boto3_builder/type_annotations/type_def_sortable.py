"""
Sortable abstractclass for TypeDefSorter.

Copyright 2024 Vlad Emelianov
"""

from abc import ABC, abstractmethod
from collections.abc import Iterable

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class TypeDefSortable(FakeAnnotation, ABC):
    """
    Sortable abstractclass for TypeDefSorter.
    """

    name: str
    _stringify: bool

    @abstractmethod
    def get_sortable_children(self) -> list["TypeDefSortable"]:
        """
        Extract required sortable TypeDef list from attributes.
        """

    @abstractmethod
    def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]:
        """
        Extract required TypeLiteral list from attributes.
        """

    @property
    @abstractmethod
    def type_hint_annotations(self) -> list[FakeAnnotation]:
        """
        Type annotations list from arguments and return type with internal types.
        """

    @abstractmethod
    def get_definition_import_records(self) -> set[ImportRecord]:
        """
        Get import record required for using TypeAnnotation.
        """

    def is_stringified(self) -> bool:
        """
        Whether TypeDef usage should be rendered as a string.
        """
        return self._stringify

    def stringify(self) -> None:
        """
        Render TypeDef usage as a string.
        """
        self._stringify = True

    @abstractmethod
    def get_children_types(self) -> set[FakeAnnotation]:
        """
        Extract required type annotations from attributes.
        """
