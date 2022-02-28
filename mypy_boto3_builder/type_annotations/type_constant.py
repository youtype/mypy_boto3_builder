"""
Wrapper for constant like `False` or `"test"`.
"""
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeConstant(FakeAnnotation):
    """
    Wrapper for constant like `False` or `"test"`.

    Arguments:
        value -- Constant value.
    """

    def __init__(self, value: object) -> None:
        self.value: object = value

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
        """
        Get empty import record, because constants do not require imports.
        """
        return ImportRecord.empty()

    def copy(self) -> "TypeConstant":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeConstant(self.value)

    def is_none(self) -> bool:
        """
        Whether value is None.
        """
        return self.value is None
