"""
Protocol for types with children.
"""

from collections.abc import Iterator
from typing import Any, Protocol, Self, runtime_checkable

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


@runtime_checkable
class TypeParent(Protocol):
    """
    Protocol for types with children.
    """

    def iterate_children(self) -> Iterator[Any]:
        """
        Iterate over children.
        """
        ...

    def replace_child(self, child: FakeAnnotation, new_child: FakeAnnotation) -> Self:
        """
        Replace child type annotation with a new one.
        """
        ...

    def find_type_annotation_parent(self, type_annotation: FakeAnnotation) -> "TypeParent | None":
        """
        Check recursively if child is present in type def.
        """
        ...

    def iterate_children_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over children type annotations.
        """
        ...

    def replace_self_references(self, replacement: FakeAnnotation) -> "list[TypeParent]":
        """
        Replace self references with a new type annotation to avoid recursion.
        """
        ...

    def render(self) -> str:
        """
        Render type annotation.
        """
        ...
