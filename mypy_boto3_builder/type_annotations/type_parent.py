"""
Protocol for types with children.

Copyright 2024 Vlad Emelianov
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
    def iterate_direct_type_annotations(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over type annotations directly present in parent.
        """
        ...

    @abstractmethod
    def get_children_types(self) -> set[FakeAnnotation]:
        """
        Extract required type annotations from attributes.
        """
        ...

    def find_type_annotation_parents(self, type_annotation: FakeAnnotation) -> "set[TypeParent]":
        """
        Check recursively if child is present in type def.

        Arguments:
            type_annotation -- Type annotation to search for.
        """
        return (
            self.find_type_annotation_parent_map(
                {type_annotation},
                shallow=False,
            ).get(type_annotation)
            or set()
        )

    def find_type_annotation_parent_map(
        self, type_annotations: Iterable[FakeAnnotation], *, shallow: bool
    ) -> "dict[FakeAnnotation, set[TypeParent]]":
        """
        Check recursively if children are present in type def.

        Arguments:
            type_annotations -- Type annotations to search for.
            shallow -- Skip TypeDefSortable types.

        Can be used for non-overlapping type annotations.
        """
        result: dict[FakeAnnotation, set[TypeParent]] = {}
        for parent in self.find_parents(shallow=shallow):
            for child_type in parent.iterate_direct_type_annotations():
                if child_type not in type_annotations:
                    continue

                if child_type not in result:
                    result[child_type] = set()

                result[child_type].add(parent)

        return result

    def find_parents(self, *, shallow: bool) -> "set[TypeParent]":
        """
        Find all parents recursively including self.

        Arguments:
            shallow -- Skip TypeDefSortable types.
        """
        result: set[TypeParent] = {self}
        stack: list[TypeParent] = [self]

        while stack:
            current = stack.pop()
            for child_type in current.iterate_direct_type_annotations():
                if not isinstance(child_type, TypeParent):
                    continue
                if child_type in result:
                    continue
                if shallow and isinstance(child_type, TypeDefSortable):
                    continue

                result.add(child_type)
                stack.append(child_type)

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
