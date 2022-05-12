"""
Sorter for TypeTypedDict to prevent import errors.
"""
from collections.abc import Iterable
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from graphlib import TopologicalSorter, CycleError
from mypy_boto3_builder.logger import get_logger


class TypedDictSorter:
    """
    Sorter for TypeTypedDict to prevent import errors.
    """

    ATTEMPTS = 5

    def __init__(self, typed_dicts: Iterable[TypeTypedDict]):
        self.typed_dicts = list(typed_dicts)
        self.typed_dicts.sort()
        self.typed_dicts_map = self._get_typed_dicts_map(self.typed_dicts)
        self.logger = get_logger()

    @classmethod
    def _get_typed_dicts_map(
        cls, typed_dicts: Iterable[TypeTypedDict], skip: Iterable[str] = ()
    ) -> dict[str, TypeTypedDict]:
        result = {}
        for typed_dict in typed_dicts:
            result[typed_dict.name] = typed_dict
            children = typed_dict.get_children_typed_dicts()
            child_skip = set([*skip, *result.keys()])
            new_children = [i for i in children if i.name not in child_skip]
            if new_children:
                result.update(cls._get_typed_dicts_map(new_children, skip=child_skip))

        return result

    def sort(self) -> list[TypeTypedDict]:
        """
        Sort items with TopologicalSorter or stringify as a fallback.
        """
        for _ in range(self.ATTEMPTS):
            try:
                return self._sort_topological()
            except CycleError as e:
                for typed_dict in self._get(*e.args[-1]):
                    self.logger.info(f"Stringifying {typed_dict.name}")
                    typed_dict.stringify()

        self.logger.warn("Topological sort failed, stringifying TypedDicts")
        return self._sort_stringified()

    def _get(self, *names: str) -> list[TypeTypedDict]:
        result = []
        for name in names:
            typed_dict = self.typed_dicts_map[name]
            if typed_dict in result:
                continue

            result.append(typed_dict)

        return result

    @staticmethod
    def _get_children_names(typed_dict: TypeTypedDict) -> list[str]:
        return [i.name for i in typed_dict.get_children_typed_dicts() if not i.is_stringified()]

    def _create_graph(self) -> dict[str, set[str]]:
        result = {}
        for typed_dict in self.typed_dicts_map.values():
            result[typed_dict.name] = self._get_children_names(typed_dict)

        return result

    def _sort_topological(self) -> list[TypeTypedDict]:
        graph = self._create_graph()
        names_sorted = list(TopologicalSorter(graph).static_order())
        result = self._get(*names_sorted)
        return result

    def _sort_stringified(self) -> list[TypeTypedDict]:
        added_hashes: list[int] = []
        result: list[TypeTypedDict] = []
        discovered: list[TypeTypedDict] = []

        for type_annotation in sorted(self.typed_dicts):
            if hash(type_annotation) in added_hashes:
                continue

            result.append(type_annotation)
            added_hashes.append(hash(type_annotation))
            discovered.append(type_annotation)

        while discovered:
            child = discovered.pop()
            sub_typed_dicts = child.get_children_typed_dicts()
            for child_typed_dict in sorted(sub_typed_dicts):
                child_typed_dict.stringify()

                if hash(child_typed_dict) in added_hashes:
                    continue

                result.append(child_typed_dict)
                added_hashes.append(hash(child_typed_dict))
                discovered.append(child_typed_dict)

        result.sort()
        return result
