"""
Class or module attribute.

Copyright 2024 Vlad Emelianov
"""

import copy
from collections.abc import Iterator
from typing import Literal, Self

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant

_TypeIgnore = Literal["override"] | None


class Attribute:
    """
    Class or module attribute.

    Arguments:
        name -- Attribute name.
        type -- Attribute type annotation.
        value -- Attribute value.
        type_ignore -- Add type: ignore[<type_ignore>] comment.
        is_reference -- Whether the attribute parsed from references.
        is_identifier -- Whether the attribute parsed from identifiers.
        is_collection -- Whether the attribute parsed from collections.
    """

    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation,
        value: TypeConstant | None = None,
        *,
        type_ignore: _TypeIgnore = None,
        is_reference: bool = False,
        is_identifier: bool = False,
        is_collection: bool = False,
    ) -> None:
        self.name = name
        self.type_annotation = type_annotation
        self.value = value
        self.type_ignore: _TypeIgnore = type_ignore
        self.is_reference = is_reference
        self.is_identifier = is_identifier
        self.is_collection = is_collection

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over all type annotations used.

        Yields:
            Type annotation.
        """
        return self.type_annotation.iterate_types()

    def render(self) -> str:
        """
        Render to a string.
        """
        line = f"{self.name}: {self.type_annotation.render()}"
        if self.type_ignore:
            return f"{line}  # type: ignore[{self.type_ignore}]"
        return line

    def is_autoload_property(self) -> bool:
        """
        Whether the attribute is an autoload property.
        """
        if self.name == "meta":
            return False

        return not self.is_reference and not self.is_identifier and not self.is_collection

    def copy(self) -> Self:
        """
        Deep copy attribute.
        """
        return copy.copy(self)

    def __copy__(self) -> Self:
        """
        Deep copy attribute.
        """
        return self.__class__(
            name=self.name,
            type_annotation=self.type_annotation.copy(),
            value=self.value.copy() if self.value else None,
            type_ignore=self.type_ignore,
            is_reference=self.is_reference,
            is_identifier=self.is_identifier,
            is_collection=self.is_collection,
        )
