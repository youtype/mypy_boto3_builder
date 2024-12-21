"""
Wrapper for Python import strings.

Copyright 2024 Vlad Emelianov
"""

import functools
from typing import Final, Self

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError, StructureError
from mypy_boto3_builder.import_helpers.import_parent import ImportParent
from mypy_boto3_builder.package_data import (
    Boto3StubsPackageData,
    TypesAioBotocorePackageData,
    TypesBoto3PackageData,
)


@functools.total_ordering
class ImportString:
    """
    Wrapper for Python import strings.

    Arguments:
        parent -- Parent module name
        parts -- Other import parts

    Examples::

        import_string = ImportString("my", "name")

        str(import_string)
        'my.name'

        import_string.render()
        'my.name'
    """

    def __init__(self, parent: str, *parts: str) -> None:
        all_parts = (parent, *parts)
        if not parent and not parts:
            raise StructureError("ImportString cannot be empty")
        has_not_empty_part = False
        for part in all_parts:
            if "." in part:
                raise StructureError(f"ImportString parts are not splitted correctly: {all_parts}")
            if part:
                has_not_empty_part = True
            elif has_not_empty_part:
                raise StructureError(
                    f"ImportString cannot have empty parts after parents: {all_parts}",
                )

        self.parts: Final[tuple[str, ...]] = tuple(all_parts)

    def __str__(self) -> str:
        """
        Render as a part of a valid Python import statement.
        """
        return self.render()

    def __hash__(self) -> int:
        """
        Calculate hash value based on all parts.
        """
        return hash(self.parts)

    def __eq__(self, other: object) -> bool:
        """
        Whether import strings produce the same render.
        """
        if not isinstance(other, ImportString):
            raise BuildInternalError(f"{other} is not ImportString")

        return self.parts == other.parts

    def __gt__(self, other: Self) -> bool:
        """
        Compare import strings for sorting.

        Emulates `isort` logic.
        """
        if self == other:
            return False

        self_is_local, other_is_local = self.is_local(), other.is_local()
        if self_is_local != other_is_local:
            return self_is_local > other_is_local

        self_is_third_party, other_is_third_party = self.is_third_party(), other.is_third_party()
        if self_is_third_party != other_is_third_party:
            return self_is_third_party > other_is_third_party

        return self.parts > other.parts

    def __add__(self, other: Self | str) -> Self:
        """
        Create a new import string by adding another import string parts to the end.
        """
        other_import_string = other if isinstance(other, ImportString) else ImportString(other)
        return self.__class__(*self.parts, *other_import_string.parts)

    def render(self) -> str:
        """
        Render to string.

        Returns:
            Ready to use import string.
        """
        return ".".join(self.parts)

    @property
    def parent(self) -> str:
        """
        Get first import string part or `builtins`.
        """
        return self.parts[0]

    def is_local(self) -> bool:
        """
        Whether import is from local module.
        """
        if self.parent.startswith(TypesBoto3PackageData.service_prefix):
            return True

        if self.parent.startswith(Boto3StubsPackageData.service_prefix):
            return True

        if self.parent.startswith(TypesAioBotocorePackageData.service_prefix):
            return True

        return self.is_type_defs()

    def is_builtins(self) -> bool:
        """
        Whether import is from Python `builtins` module.
        """
        return ImportParent.is_builtins(self.parent)

    def is_type_defs(self) -> bool:
        """
        Whether import is from `type_defs` module.
        """
        if not self.parts:
            return False
        return self.parts[-1] == ServiceModuleName.type_defs.value

    def is_third_party(self) -> bool:
        """
        Whether import is from 3rd party module.
        """
        return ImportParent.is_third_party(self.parent)

    def startswith(self, other: "ImportString") -> bool:
        """
        Whether import string starts with another import string.
        """
        return self.parts[: len(other.parts)] == other.parts
