"""
Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.

Copyright 2024 Vlad Emelianov
"""

import inspect
from typing import Self

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.import_helpers.import_helper import Import
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
        *,
        safe: bool = False,
        fallback: ImportRecord | None = None,
    ) -> None:
        self.source: ImportString = source
        self.name: str = name
        self.alias: str = alias
        self.fallback: ImportRecord | None = fallback
        if safe and not self.fallback:
            self.add_fallback(ImportRecord(Import.builtins, "object", self.name))

    @classmethod
    def from_class(cls, obj: type, alias: str = "", *, safe: bool = False) -> Self:
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
            source=Import.from_str(module_name),
            name=obj.__name__,
            alias=alias,
            safe=safe,
        )

    @property
    def import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        if self.fallback:
            fallback = self.fallback or ImportRecord(Import.builtins, "object", self.name)
            return ImportRecord(
                self.source,
                self.name,
                self.alias,
                min_version=None,
                fallback=fallback,
            )
        return ImportRecord(
            source=self.source,
            name=self.name,
            alias=self.alias,
            min_version=None,
            fallback=self.fallback,
        )

    def __hash__(self) -> int:
        """
        Calcualte hash value based on import record.
        """
        return hash((self.source, self.name, self.alias, self.fallback))

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
        return self.__class__(self.source, self.name, self.alias, fallback=self.fallback)

    def copy_from(self, other: Self) -> None:
        """
        Copy all fileds from another instance.
        """
        self.source = other.source
        self.name = other.name
        self.fallback = other.fallback

    def add_fallback(self, fallback: ImportRecord | None = None) -> None:
        """
        Add fallback import record.
        """
        self.fallback = fallback or ImportRecord(Import.builtins, "object", self.name)
