"""
Helper for Python import strings.
"""
from functools import total_ordering
from typing import Any, Optional, Tuple

from mypy_boto3_builder.constants import MODULE_NAME, TYPE_DEFS_NAME
from mypy_boto3_builder.import_helpers.import_string import ImportString


@total_ordering
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

    type_defs_import_string = ImportString(TYPE_DEFS_NAME)
    builtins_import_string = ImportString("builtins")
    third_party_import_strings = (
        ImportString("boto3"),
        ImportString("botocore"),
    )

    def __init__(
        self,
        source: ImportString,
        name: str = "",
        alias: str = "",
        min_version: Tuple[int, ...] = (3, 8),
        fallback: Optional["ImportRecord"] = None,
    ) -> None:
        self.source = source
        self.name = name
        self.alias = alias
        self.min_version = min_version
        self.fallback = fallback

    def __bool__(self) -> bool:
        return bool(self.source)

    @classmethod
    def empty(cls) -> "ImportRecord":
        return cls(ImportString.empty())

    def render(self) -> str:
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

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ImportRecord):
            raise ValueError(f"Cannot compare ImportString with {other}")

        return str(self) == str(other)

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, ImportRecord):
            raise ValueError(f"Cannot compare ImportString with {other}")

        return not self == other

    def __gt__(self, other: "ImportRecord") -> bool:
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
        return self.source.startswith(self.type_defs_import_string)

    def is_third_party(self) -> bool:
        """
        Whether import is from 3rd party module.
        """
        for third_party_import_string in self.third_party_import_strings:
            if self.source.startswith(third_party_import_string):
                return True

        return False

    def is_local(self) -> bool:
        """
        Whether import is from local module.
        """
        if not self.source:
            return False

        if self.source.master_name.startswith(MODULE_NAME):
            return True

        if self.is_type_defs():
            return True

        return False

    def get_external(self, _module_name: str) -> "ImportRecord":
        """
        Get itself.

        Overriden by `InternalImportRecord`.
        """
        return self

    def is_standalone(self) -> bool:
        """
        Whether import record should not be grouped.
        """
        if not self.name or self.fallback:
            return True

        return False
