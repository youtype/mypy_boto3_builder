"""
Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.
"""

import inspect
from typing import Self

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class ExternalImport(FakeAnnotation):
    """
    Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.

    Arguments:
        source -- Module import string.
        name -- Import name.
        alias -- Import local name.
        safe -- Whether import is wrapped in try-except.
    """

    def __init__(
        self,
        source: ImportString,
        name: str = "",
        alias: str = "",
        safe: bool = False,
    ) -> None:
        self.source: ImportString = source
        self.name: str = name
        self.alias: str = alias
        self.safe: bool = safe

    @classmethod
    def from_class(cls, obj: type, alias: str = "", safe: bool = False) -> Self:
        """
        Create an instance from an imported class.

        Arguments:
            value -- Any Class.
            alias -- Local name.
            safe -- Whether import is wrapped in try-except.
        """
        module = inspect.getmodule(obj)
        if module is None:
            raise TypeAnnotationError(f"Unknown module for {obj}")

        module_name = module.__name__
        return cls(
            source=ImportString.from_str(module_name),
            name=obj.__name__,
            alias=alias,
            safe=safe,
        )

    @property
    def import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        if self.safe:
            return ImportRecord(
                self.source,
                self.name,
                self.alias,
                min_version=None,
                fallback=ImportRecord(ImportString(ImportString.BUILTINS), "object", self.name),
            )
        return ImportRecord(source=self.source, name=self.name, alias=self.alias)

    def __hash__(self) -> int:
        """
        Calcualte hash value based on import record.
        """
        return hash((self.source, self.name, self.alias, self.safe))

    def render(self) -> str:
        """
        Get string with local name to use.

        Returns:
            Import record local name.
        """
        return self.import_record.get_local_name()

    def _get_import_records(self) -> set[ImportRecord]:
        """
        Get import record required for using type annotation.
        """
        return {self.import_record}

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(self.source, self.name, self.alias, self.safe)

    def copy_from(self: Self, other: Self) -> None:
        """
        Copy all fileds from another instance.
        """
        self.source = other.source
        self.name = other.name
        self.safe = other.safe
