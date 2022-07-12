"""
Class or module attribute.
"""
from typing import Iterator

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class Attribute:
    """
    Class or module attribute.

    Attributes:
        name -- Attribute name.
        type -- Attribute type annotation.
        value -- Attribute value.
        type_ignore -- Add type: ignore comment.
    """

    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation,
        value: TypeConstant | None = None,
        type_ignore: bool = False,
    ):
        self.name: str = name
        self.type_annotation: FakeAnnotation = type_annotation
        self.value: TypeConstant | None = value
        self.type_ignore = type_ignore

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over all type annotations used.

        Yields:
            Type annotation.
        """
        return self.type_annotation.iterate_types()

    def render(self) -> str:
        """
        Render to a string.
        """
        line = f"{self.name}: {self.type_annotation.render()}"
        if self.type_ignore:
            return f"{line}  # type: ignore"
        return line
