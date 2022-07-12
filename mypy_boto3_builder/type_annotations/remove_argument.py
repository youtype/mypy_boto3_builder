"""
Annotation to mark argument for removal.
"""
from typing import TypeVar

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation

_R = TypeVar("_R", bound="RemoveArgument")


class RemoveArgument(FakeAnnotation):
    """
    Annotation to mark argument for removal.
    """

    def render(self, parent_name: str = "") -> str:
        """
        Not used.
        """
        return "None"

    def copy(self: _R) -> _R:
        """
        Not used.
        """
        return self

    def get_import_record(self) -> ImportRecord:
        """
        Not used.
        """
        return ImportRecord.empty()
