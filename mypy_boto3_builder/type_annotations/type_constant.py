"""
Wrapper for constant like `False` or `"test"`.
"""
from typing import Any

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeConstant(FakeAnnotation):
    """
    Wrapper for constant like `False` or `"test"`.

    Arguments:
        value -- Constant value.
    """

    def __init__(self, value: Any) -> None:
        self.value = value

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.value is Ellipsis:
            return "..."

        return repr(self.value)

    def get_import_record(self) -> ImportRecord:
        return ImportRecord.empty()

    def copy(self) -> "TypeConstant":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeConstant(self.value)
