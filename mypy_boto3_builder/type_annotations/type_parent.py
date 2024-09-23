"""
Protocol for types with children.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import Self

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable


class TypeParent(FakeAnnotation, ABC):
    """
    Protocol for types with children.
    """

    @abstractmethod
    def replace_child(self, child: FakeAnnotation, new_child: FakeAnnotation) -> Self:
        """
        Replace child type annotation with a new one.
        """
        ...

    @abstractmethod
    def iterate_children_type_annotations(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over children type annotations.
        """
        ...

    @abstractmethod
    def get_children_types(self) -> set[FakeAnnotation]:
        """
        Extract required type annotations from attributes.
        """
        ...

    def find_type_annotation_parents(
        self, type_annotation: FakeAnnotation, skip: Iterable[FakeAnnotation] = ()
    ) -> "set[TypeParent]":
        """
        Check recursively if child is present in type def.
        """
        result: set[TypeParent] = set()
        for child_type in self.iterate_children_type_annotations():
            if child_type == type_annotation:
                result.add(self)
            if not isinstance(child_type, TypeParent):
                continue

            if child_type in skip:
                continue

            parents = child_type.find_type_annotation_parents(
                type_annotation, skip={*skip, child_type}
            )
            result.update(parents)

        return result

    def replace_self_references(self, replacement: FakeAnnotation) -> "set[TypeParent]":
        """
        Replace self references with a new type annotation to avoid recursion.
        """
        """
        Replace self references with a new type annotation to avoid recursion.
        """
        parents = self.find_type_annotation_parents(self)
        for parent in parents:
            parent.replace_child(self, replacement)
        return parents

    def get_sortable_children(self) -> list[TypeDefSortable]:
        """
        Extract required TypeDefSortable list from attributes.
        """
        result: list[TypeDefSortable] = []
        children_types = self.get_children_types()
        for type_annotation in children_types:
            if not isinstance(type_annotation, TypeDefSortable):
                continue
            result.append(type_annotation)

        return result
