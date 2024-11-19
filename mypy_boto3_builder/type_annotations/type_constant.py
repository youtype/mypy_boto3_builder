"""
Wrapper for constant like `False` or `"test"`.

Copyright 2024 Vlad Emelianov
"""

from typing import Final, Self

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class EllipsisType:
    """
    Placeholder for `...`.
    """


ValueType = str | int | float | EllipsisType | None


class TypeConstant(FakeAnnotation):
    """
    Wrapper for constant like `False` or `"test"`.

    Arguments:
        value -- Constant value.
    """

    Ellipsis: Final[EllipsisType] = EllipsisType()

    def __init__(self, value: ValueType) -> None:
        self.value: ValueType = value

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.value is self.Ellipsis:
            return "..."

        return repr(self.value)

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(self.value)
