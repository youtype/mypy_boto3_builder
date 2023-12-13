"""
Class or module attribute.
"""

from collections.abc import Iterator
from dataclasses import dataclass

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


@dataclass
class Attribute:
    """
    Class or module attribute.

    Attributes:
        name -- Attribute name.
        type -- Attribute type annotation.
        value -- Attribute value.
        type_ignore -- Add type: ignore comment.
        is_reference -- Whether the attribute parsed from references.
        is_identifier -- Whether the attribute parsed from identifiers.
        is_collection -- Whether the attribute parsed from collections.
    """

    name: str
    type_annotation: FakeAnnotation
    value: TypeConstant | None = None
    type_ignore: bool = False
    is_reference: bool = False
    is_identifier: bool = False
    is_collection: bool = False

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

    def is_autoload_property(self) -> bool:
        """
        Whether the attribute is an autoload property.
        """
        return not self.is_reference and not self.is_identifier and not self.is_collection
