"""
Class or module attribute.
"""
from dataclasses import dataclass
from typing import Optional, Set

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
    """

    name: str
    type: FakeAnnotation
    value: Optional[TypeConstant] = None

    def get_types(self) -> Set[FakeAnnotation]:
        """
        Return all type annotations used.

        Returns:
            A set of type annotations.
        """
        return self.type.get_types()
