"""
Wrapper for name Union type annotations, like `MyUnion = Union[str, int]`.
"""
from typing import Iterable, TypeVar

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript

_R = TypeVar("_R", bound="TypeUnion")


class TypeUnion(TypeSubscript):
    """
    Wrapper for name Union type annotations, like `MyUnion = Union[str, int]`.
    """

    def __init__(
        self,
        children: Iterable[FakeAnnotation] = (),
        name: str = "",
        stringify: bool = False,
    ) -> None:
        self.name = name
        self.parent = Type.Union
        self.children: list[FakeAnnotation] = list(children)
        self._stringify = stringify
        print(self.render_definition())

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if not self.is_named():
            return super().render(parent_name)

        result = self.name

        if self._stringify:
            result = f'"{result}"'

        return result

    def is_named(self) -> bool:
        """
        Check if type annotation is a named type annotation.
        """
        return bool(self.name)

    def render_definition(self) -> str:
        """
        Render named Union type definition.
        """
        return f"{self.name} = {super().render()}"

    def copy(self: _R) -> _R:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(
            children=list(self.children),
            name=self.name,
            stringify=self._stringify,
        )
