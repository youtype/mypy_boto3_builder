"""
Wrapper for TypedDict maps.
"""

from collections.abc import Iterator

from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.utils.type_def_sorter import TypeDefSorter


class TypedDictMap(dict[str, TypeTypedDict]):
    """
    Wrapper for TypedDict maps.
    """

    def add(self, item: TypeTypedDict) -> None:
        """
        Add new item.
        """
        self[item.name] = item

    def iterate_pairs(self, name: str) -> Iterator[tuple[str, TypeTypedDict]]:
        """
        Iterate over pairs mathed by real dict name.
        """
        for key, value in list(self.items()):
            if value.name == name:
                yield key, value

    def rename(self, item: TypeTypedDict, new_name: str) -> None:
        """
        Rename item and change mapping.
        """
        for key, value in list(self.items()):
            if value == item:
                del self[key]

        item.name = new_name
        self[new_name] = item

    def get_sorted_names(self) -> list[str]:
        """
        Get real TypedDict names topologically sorted.
        """
        sorted_values = TypeDefSorter(self.values()).sort()
        allowed_names = {i.name for i in self.values()}
        return [i.name for i in sorted_values if i.name in allowed_names]
