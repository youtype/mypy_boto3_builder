"""
Wrapper for subscript type annotations, like `List[str]`.
"""
from typing import Iterable, Set

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation


class TypeSubscript(FakeAnnotation):
    """
    Wrapper for subscript type annotations, like `List[str]`.

    Arguments:
        parent -- Parent type annotation.
        children -- Children type annotations.
    """

    def __init__(self, parent: TypeAnnotation, children: Iterable[FakeAnnotation] = (),) -> None:
        self.parent = parent
        self.children = list(children)

    def __hash__(self) -> int:
        return hash(f"{self.parent}.{self.children}")

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if not self.children:
            return f"{self.parent.render()}"

        children = ", ".join([i.render(parent_name) for i in self.children])
        return f"{self.parent.render()}[{children}]"

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        return self.parent.get_import_record()

    def get_types(self) -> Set[FakeAnnotation]:
        result = self.parent.get_types()
        for child in self.children:
            result.update(child.get_types())
        return result

    def add_child(self, child: FakeAnnotation) -> None:
        self.children.append(child)

    def is_dict(self) -> bool:
        return self.parent.is_dict()

    def is_list(self) -> bool:
        return self.parent.is_list()

    def copy(self) -> "TypeSubscript":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeSubscript(self.parent, list(self.children))
