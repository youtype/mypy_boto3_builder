"""
Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.
"""
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class ExternalImport(FakeAnnotation):
    """
    Wrapper for type annotations imported from 3rd party libraries, like
    `boto3.service.Service`.

    Arguments:
        source -- Module import string.
        name -- Import name.
        alias -- Import local name.
    """

    def __init__(self, source: ImportString, name: str = "", alias: str = "",) -> None:
        self.source = source
        self.name = name
        self.alias = alias
        self.import_record = ImportRecord(source=source, name=name, alias=alias)

    def render(self, parent_name: str = "") -> str:
        """
        Get string with local name to use.

        Returns:
            Import record local name.
        """
        return self.import_record.get_local_name()

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        return self.import_record

    def copy(self) -> "ExternalImport":
        """
        Create a copy of type annotation wrapper.
        """
        return ExternalImport(self.source, self.name, self.alias)
