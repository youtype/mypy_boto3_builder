"""
Helper for Python import strings.

Copyright 2024 Vlad Emelianov
"""

import copy
import functools
from typing import Self

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_string import ImportString


@functools.total_ordering
class ImportRecord:
    """
    Helper for Python import strings.

    Arguments:
        source -- Source of import.
        name -- Import name.
        alias -- Import local name.
        min_version -- Minimum Python version, used for fallback.
        fallback -- Fallback ImportRecord.
    """

    def __init__(
        self,
        source: ImportString,
        name: str = "",
        alias: str = "",
        min_version: tuple[int, ...] | None = None,
        fallback: Self | None = None,
    ) -> None:
        self.source = source
        self.name = name
        self.alias = alias
        self.min_version = min_version
        self.fallback = fallback

    def render_name(self) -> str:
        """
        Get rendered import name.
        """
        if not self.name:
            raise StructureError(f"ImportRecord {self} has no name")

        if self.alias:
            return f"{self.name} as {self.alias}"

        return self.name

    def render(self) -> str:
        """
        Get rendered string.
        """
        if self.name:
            return f"from {self.source} import {self.render_name()}"
        if self.alias:
            return f"import {self.source} as {self.alias}"

        return f"import {self.source}"

    def __str__(self) -> str:
        """
        Render as a valid Python import statement.
        """
        return self.render()

    def __hash__(self) -> int:
        """
        Calculate hash value based on source, name and alias.
        """
        return hash(
            (
                self.source,
                self.name,
                self.alias,
                self.min_version,
                self.fallback,
            ),
        )

    def __eq__(self, other: object) -> bool:
        """
        Whether two import records produce the same render.
        """
        if not isinstance(other, ImportRecord):
            return False

        return str(self) == str(other)

    def __gt__(self, other: Self) -> bool:
        """
        Compare two import records for sorting.

        Emulates `isort` logic.
        """
        if self == other:
            return False

        if self.min_version != other.min_version:
            return (self.min_version or ()) > (other.min_version or ())

        if bool(self.fallback) != bool(other.fallback):
            return bool(self.fallback) > bool(other.fallback)

        if self.source != other.source:
            return self.source > other.source

        return self.name > other.name

    def get_local_name(self) -> str:
        """
        Get local import name.
        """
        return self.alias or self.name or self.source.render()

    def needs_sys_fallback(self) -> bool:
        """
        Whether ImportString requires `sys` module.
        """
        return bool(self.fallback and self.min_version)

    def __copy__(self) -> Self:
        """
        Create a copy of the record.
        """
        return self.__class__(
            source=self.source,
            name=self.name,
            alias=self.alias,
            min_version=self.min_version,
            fallback=self.fallback.copy() if self.fallback else None,
        )

    def copy(self) -> Self:
        """
        Create a copy of the record.
        """
        return copy.copy(self)
