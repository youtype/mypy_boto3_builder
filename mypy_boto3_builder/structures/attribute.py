"""
Class or module attribute.
"""
from typing import Optional, Set

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class Attribute:
    """
    Class or module attribute.

    Attributes:
        name -- Attribute name.
        type -- Attribute type annotation.
        value -- Attribute value.
    """

    def __init__(
        self,
        name: str,
        type_annotation: FakeAnnotation,
        value: Optional[TypeConstant] = None,
    ):
        self.name = name
        self.type_annotation = type_annotation
        self.value = value

    def get_types(self) -> Set[FakeAnnotation]:
        """
        Return all type annotations used.

        Returns:
            A set of type annotations.
        """
        return self.type_annotation.get_types()
