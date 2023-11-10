"""
Helper for Python import strings.
"""

import functools
from typing import TypeVar

from typing_extensions import Self

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.package_data import Boto3StubsPackageData, TypesAioBotocorePackageData

_R = TypeVar("_R", bound="ImportRecord")


@functools.total_ordering
class ImportRecord:
    """
    Helper for Python import strings.

    Arguments:
        source -- Source of import.
        name -- Import name.
        alias -- Import local name.
        min_version -- Minimum Python version, used for fallback.
        fallback -- Fallback ImportRecord.
    """

    builtins_import_string = ImportString("builtins")
    third_party_import_strings = (
        ImportString("boto3"),
        ImportString("botocore"),
    )

    def __init__(
        self: _R,
        source: ImportString,
        name: str = "",
        alias: str = "",
        min_version: tuple[int, ...] | None = None,
        fallback: _R | None = None,
    ) -> None:
        self.source = source
        self.name = name
        self.alias = alias
        self.min_version = min_version
        self.fallback = fallback

    def __bool__(self) -> bool:
        return not self.is_empty()

    def is_empty(self) -> bool:
        """
        Whether import record is an empty string.
        """
        return not self.source

    @classmethod
    def empty(cls) -> Self:
        """
        Whether import record is an empty string.
        """
        return cls(ImportString.empty())

    def render(self) -> str:
        """
        Get rendered string.
        """
        if self.name and self.alias:
            return f"from {self.source} import {self.name} as {self.alias}"
        if self.name:
            return f"from {self.source} import {self.name}"
        if self.alias:
            return f"import {self.source} as {self.alias}"
        if self.source:
            return f"import {self.source}"

        return ""

    def __str__(self) -> str:
        return self.render()

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ImportRecord):
            return False

        return str(self) == str(other)

    def __gt__(self: _R, other: _R) -> bool:
        if self.fallback is not None and other.fallback is None:
            return True

        if other.fallback is not None and self.fallback is None:
            return False

        if self.source == other.source:
            return self.name > other.name

        if self.is_local() and not other.is_local():
            return True

        if other.is_local() and not self.is_local():
            return False

        if self.is_third_party() and not other.is_third_party():
            return True

        if other.is_third_party() and not self.is_third_party():
            return False

        return self.source > other.source

    def get_local_name(self) -> str:
        """
        Get local import name.
        """
        return self.alias or self.name or self.source.render()

    def is_builtins(self) -> bool:
        """
        Whether import is from Python `builtins` module.
        """
        return self.source.startswith(self.builtins_import_string)

    def is_type_defs(self) -> bool:
        """
        Whether import is from `type_defs` module.
        """
        return self.source.parts[-1] == ServiceModuleName.type_defs.value

    def is_third_party(self) -> bool:
        """
        Whether import is from 3rd party module.
        """
        return any(
            self.source.startswith(third_party_import_string)
            for third_party_import_string in self.third_party_import_strings
        )

    def is_local(self) -> bool:
        """
        Whether import is from local module.
        """
        if not self.source:
            return False

        if self.source.master_name.startswith(Boto3StubsPackageData.SERVICE_PREFIX):
            return True

        if self.source.master_name.startswith(TypesAioBotocorePackageData.SERVICE_PREFIX):
            return True

        if self.is_type_defs():
            return True

        return False

    def needs_sys_fallback(self) -> bool:
        """
        Whether ImportString requires `sys` module.
        """
        return bool(self.fallback and self.min_version)
