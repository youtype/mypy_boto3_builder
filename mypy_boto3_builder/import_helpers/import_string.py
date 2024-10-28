"""
Wrapper for Python import strings.
"""

import functools
from typing import Final, Self

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import BuildInternalError, StructureError
from mypy_boto3_builder.package_data import Boto3StubsPackageData, TypesAioBotocorePackageData


@functools.total_ordering
class ImportString:
    """
    Wrapper for Python import strings.

    Arguments:
        master -- Master module name
        parts -- Other import parts

    Examples::

        import_string = ImportString("my", "name")

        str(import_string)
        'my.name'

        import_string.render()
        'my.name'
    """

    BUILTINS: Final[str] = "builtins"
    _THIRD_PARTY: Final[set[str]] = {
        "boto3",
        "botocore",
        "aioboto3",
        "aiobotocore",
        "s3transfer",
        "awscrt",
    }

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
                    f"ImportString cannot have empty parts after parents: {all_parts}"
                )

        self.parts: Final[tuple[str, ...]] = tuple(all_parts)

    @classmethod
    def from_str(cls, import_string: str) -> Self:
        """
        Create from string.
        """
        return cls(*import_string.split("."))

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

        if self.is_local() != other.is_local():
            return self.is_local() > other.is_local()

        if self.is_third_party() != other.is_third_party():
            return self.is_third_party() > other.is_third_party()

        return self.parts > other.parts

    def __add__(self: Self, other: Self | str) -> Self:
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
        if self.parent.startswith(Boto3StubsPackageData.SERVICE_PREFIX):
            return True

        if self.parent.startswith(TypesAioBotocorePackageData.SERVICE_PREFIX):
            return True

        return self.is_type_defs()

    def is_builtins(self) -> bool:
        """
        Whether import is from Python `builtins` module.
        """
        return self.parent == self.BUILTINS

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
        return self.parent in self._THIRD_PARTY
