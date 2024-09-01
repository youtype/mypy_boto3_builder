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

        import_string.parts.append('test')
        import_string.render()
        'my.name.test'
    """

    _BUILTINS: Final[str] = "builtins"
    _THIRD_PARTY: Final[tuple[str, ...]] = ("boto3", "botocore")

    def __init__(self, master_name: str, *parts: str) -> None:
        all_parts = [master_name, *parts]
        for part in all_parts:
            if "." in part:
                raise StructureError(f"Invalid ImportString parts: {all_parts} - {part}")

        self.parts: tuple[str, ...] = tuple(all_parts)

    @classmethod
    def from_str(cls: type[Self], import_string: str) -> Self:
        """
        Create from string.
        """
        return cls(*import_string.split("."))

    @classmethod
    def empty(cls: type[Self]) -> Self:
        """
        Create an empty ImportString.
        """
        result = cls("fake")
        result.parts = ()
        return result

    @classmethod
    def parent(cls: type[Self]) -> Self:
        """
        Get parent ImportString.
        """
        return cls("")

    def __bool__(self) -> bool:
        """
        Whether import string is not empty.
        """
        return bool(self.parts)

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

    def __gt__(self, other: object) -> bool:
        """
        Compare import strings for sorting.

        Emulates `isort` logic.
        """
        if not isinstance(other, ImportString):
            raise BuildInternalError(f"{other} is not ImportString")

        if self == other:
            return False

        if self.is_local() and not other.is_local():
            return True

        if other.is_local() and not self.is_local():
            return False

        if self.is_third_party() and not other.is_third_party():
            return True

        if other.is_third_party() and not self.is_third_party():
            return False

        return self.parts > other.parts

    def __add__(self: Self, other: Self | str) -> Self:
        """
        Create a new import string by adding another import string parts to the end.
        """
        other_import_string = other if isinstance(other, ImportString) else ImportString(other)
        return self.__class__(*self.parts, *other_import_string.parts)

    def startswith(self: Self, other: Self) -> bool:
        """
        Check if import string starts with `other`.

        Examples::

            ImportString('my', 'name').startswith(ImportString('my'))
            True

            ImportString('my_module', 'name').startswith(ImportString('my'))
            False

            ImportString('my', 'name').startswith(ImportString('my, 'name'))
            True

        Arguments:
            other -- Other import string.
        """
        for part_index, part in enumerate(other.parts):
            try:
                self_part = self.parts[part_index]
            except IndexError:
                return False

            if self_part != part:
                return False

        return True

    def render(self) -> str:
        """
        Render to string.

        Returns:
            Ready to use import string.
        """
        return ".".join(self.parts)

    @property
    def master_name(self) -> str:
        """
        Get first import string part or `builtins`.
        """
        if not self.parts:
            return self._BUILTINS

        return self.parts[0]

    def is_local(self) -> bool:
        """
        Whether import is from local module.
        """
        if self.master_name.startswith(Boto3StubsPackageData.SERVICE_PREFIX):
            return True

        if self.master_name.startswith(TypesAioBotocorePackageData.SERVICE_PREFIX):
            return True

        return self.is_type_defs()

    def is_builtins(self) -> bool:
        """
        Whether import is from Python `builtins` module.
        """
        return self.master_name == self._BUILTINS

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
        return self.master_name in self._THIRD_PARTY
