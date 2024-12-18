"""
Sorter for TypeDefSorter to prevent import errors.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable
from graphlib import CycleError, TopologicalSorter

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable


class TypeDefSorter:
    """
    Sorter for TypeDefs to prevent import errors.
    """

    ATTEMPTS = 20

    def __init__(self, type_defs: Iterable[TypeDefSortable]) -> None:
        self.typed_defs = list(type_defs)
        self.typed_defs.sort(key=lambda x: x.name)
        self.typed_def_map = self._get_type_defs_map(self.typed_defs)
        self.logger = get_logger()

    @classmethod
    def _get_type_defs_map(
        cls,
        type_defs: Iterable[TypeDefSortable],
        skip: Iterable[str] = (),
    ) -> dict[str, TypeDefSortable]:
        result: dict[str, TypeDefSortable] = {}
        for type_def in type_defs:
            result[type_def.name] = type_def
            children = type_def.get_sortable_children()
            child_skip = {*skip, *result.keys()}
            new_children = [i for i in children if i.name not in child_skip]
            if new_children:
                result.update(cls._get_type_defs_map(new_children, skip=child_skip))

        return result

    def sort(self) -> list[TypeDefSortable]:
        """
        Sort items with TopologicalSorter or stringify as a fallback.
        """
        for attempt in range(self.ATTEMPTS):
            try:
                result = self._sort_topological()
            except CycleError as e:
                for type_def in self._get(*e.args[-1]):
                    self.logger.debug(
                        f"Stringifying {type_def.name}: unsortable children"
                        f" {self.typed_def_map[type_def.name]}",
                    )
                    type_def.stringify()
            else:
                if attempt:
                    self.logger.debug(f"Topological sort succeeded after {attempt + 1} attempts")
                return result

        self.logger.warning("Topological sort failed, stringifying TypedDicts")
        return self._sort_stringified()

    def _get(self, *names: str) -> list[TypeDefSortable]:
        result: list[TypeDefSortable] = []
        for name in names:
            type_def = self.typed_def_map[name]
            if type_def in result:
                continue

            result.append(type_def)

        return result

    def _create_graph(self) -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        for name in sorted(self.typed_def_map):
            type_def = self.typed_def_map[name]
            children_names = {
                child.name
                for child in type_def.get_sortable_children()
                if not child.is_stringified()
            }
            result[name] = sorted(children_names)

        return result

    def _sort_topological(self) -> list[TypeDefSortable]:
        graph = self._create_graph()
        names_sorted = list(TopologicalSorter(graph).static_order())
        return self._get(*names_sorted)

    def _sort_stringified(self) -> list[TypeDefSortable]:
        added_hashes: list[int] = []
        result: list[TypeDefSortable] = []
        discovered: list[TypeDefSortable] = []

        for type_annotation in sorted(self.typed_defs):
            if hash(type_annotation) in added_hashes:
                continue

            result.append(type_annotation)
            added_hashes.append(hash(type_annotation))
            discovered.append(type_annotation)

        while discovered:
            child = discovered.pop()
            sub_typed_defs = child.get_sortable_children()
            for child_type_def in sorted(sub_typed_defs):
                child_type_def.stringify()

                if hash(child_type_def) in added_hashes:
                    continue

                result.append(child_type_def)
                added_hashes.append(hash(child_type_def))
                discovered.append(child_type_def)

        result.sort()
        return result
