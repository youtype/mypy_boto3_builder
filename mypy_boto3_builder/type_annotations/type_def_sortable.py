"""
Sortable protocol for TypeDefSorter.
"""
from collections.abc import Iterable, Iterator

from typing_extensions import Protocol, runtime_checkable

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


@runtime_checkable
class TypeDefSortable(Protocol):
    """
    Sortable protocol for TypeDefSorter.
    """

    name: str
    _stringify: bool

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

    def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]:
        """
        Extract required TypeLiteral list from attributes.
        """
        ...

    def is_type_def(self) -> bool:
        """
        Whether type annotation is a TypeDef.
        """
        ...

    @property
    def type_hint_annotations(self) -> list[FakeAnnotation]:
        """
        Type annotations list from arguments and return type with internal types.
        """
        ...

    def get_typing_import_records(self) -> set[ImportRecord]:
        """
        Get import record required for using TypeAnnotation.
        """
        ...

    def is_typed_dict(self) -> bool:
        """
        Whether type annotation is a TypedDict.
        """
        ...

    def is_union(self) -> bool:
        """
        Whether type annotation is a TypeUnion.
        """
        ...

    def replace_self_references(self) -> None:
        """
        Replace self references with `Dict[str, Any]` to avoid circular dependencies.
        """
        ...

    def iterate_children(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over children.
        """
        ...
