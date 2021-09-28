"""
Wrapper for classes like `Paginator`.
"""
import inspect

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class TypeClass(FakeAnnotation):
    """
    Wrapper for classes like `Paginator`.

    Arguments:
        value -- Any Class.
        alias -- Local name.
    """

    def __init__(self, value: type, alias: str = "") -> None:
        self.value: type = value
        self.alias: str = alias

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.alias:
            return self.alias

        return self.get_import_name()

    def get_import_name(self) -> str:
        """
        Get name for import string.
        """
        return self.value.__name__

    def get_import_record(self) -> ImportRecord:
        """
        Create an impoort record to insert where TypeClass is used.
        """
        module = inspect.getmodule(self.value)
        if module is None:
            raise ValueError(f"Unknown module for {self.value}")

        module_name = module.__name__
        return ImportRecord(
            source=ImportString.from_str(module_name),
            name=self.get_import_name(),
            alias=self.alias,
        )

    def copy(self) -> "TypeClass":
        """
        Create a copy of type annotation wrapper.
        """
        return TypeClass(self.value, self.alias)
