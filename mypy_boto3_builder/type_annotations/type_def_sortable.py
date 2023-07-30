"""
Sortable protocol for TypeDefSorter.
"""
from typing_extensions import Protocol, runtime_checkable

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


@runtime_checkable
class TypeDefSortable(Protocol):
    """
    Sortable protocol for TypeDefSorter.
    """

    name: str
    _stringify: bool
    replace_with_dict: set[str]

    def __gt__(self, other: FakeAnnotation) -> bool:
        ...

    def __lt__(self, other: FakeAnnotation) -> bool:
        ...

    def get_sortable_children(self) -> list["TypeDefSortable"]:
        """
        Extract required sortable TypeDef list from attributes.
        """
        ...

    def is_stringified(self) -> bool:
        """
        Whether TypeDef usage should be rendered as a string.
        """
        ...

    def stringify(self) -> None:
        """
        Render TypeDef usage as a string.
        """
        ...

    def get_children_types(self) -> set[FakeAnnotation]:
        """
        Extract required type annotations from attributes.
        """
        ...

    def debug_render(self) -> str:
        """
        Render type annotation for debug purposes.
        """
        ...
