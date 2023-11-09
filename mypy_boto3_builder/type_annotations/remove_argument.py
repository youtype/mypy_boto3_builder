"""
Annotation to mark argument for removal.
"""

from typing_extensions import Self

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class RemoveArgument(FakeAnnotation):
    """
    Annotation to mark argument for removal.
    """

    def render(self) -> str:
        """
        Not used.
        """
        return "None"

    def __copy__(self) -> Self:
        """
        Not used.
        """
        return self
