"""
Parent class for all type annotation wrappers.

Copyright 2024 Vlad Emelianov
"""

import copy
import functools
from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import Self

from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord


@functools.total_ordering
class FakeAnnotation(ABC):
    """
    Parent class for all type annotation wrappers.
    """

    def __hash__(self) -> int:
        """
        Calculate hash value based on string render.
        """
        return hash(self.get_sort_key())

    def __eq__(self, other: object) -> bool:
        """
        Whether two annotations are equal.
        """
        if not isinstance(other, FakeAnnotation):
            raise BuildInternalError(f"{other} is not FakeAnnotation")

        return self.get_sort_key() == other.get_sort_key()

    def __gt__(self, other: "FakeAnnotation") -> bool:
        """
        Compare two annotations for sorting.
        """
        return self.get_sort_key() > other.get_sort_key()

    def get_sort_key(self) -> str:
        """
        Get string to sort annotations.
        """
        return str(self)

    def __str__(self) -> str:
        """
        Render annotation usage as a valid Python statement.
        """
        return self.render()

    @abstractmethod
    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.
        """

    def _get_import_records(self) -> set[ImportRecord]:
        """
        Get import record required for using type annotation.
        """
        return set()

    def get_import_records(self) -> set[ImportRecord]:
        """
        Get all import records required for using type annotation.
        """
        return {
            import_record
            for import_record in self._get_import_records()
            if not import_record.is_implicit()
        }

    def iterate_types(self) -> Generator["FakeAnnotation"]:
        """
        Iterate over all used type annotations recursively including self.
        """
        yield self

    def is_dict(self) -> bool:
        """
        Whether type annotation is `Dict` or `TypedDict`.
        """
        return False

    def is_list(self) -> bool:
        """
        Whether type annotation is `List`.
        """
        return False

    def is_literal(self) -> bool:
        """
        Whether type annotation is `Literal`.
        """
        return False

    @abstractmethod
    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """

    def copy(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return copy.copy(self)

    def get_local_types(self) -> list["FakeAnnotation"]:
        """
        Get internal types generated by builder.
        """
        return []

    def render_definition(self) -> str:
        """
        Render type annotation for debug purposes.
        """
        return self.render()
