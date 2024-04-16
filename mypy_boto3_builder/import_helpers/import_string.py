"""
Wrapper for Python import strings.
"""

import functools

from typing_extensions import Self


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

    def __init__(self, master_name: str, *parts: str) -> None:
        self.parts: list[str] = []
        all_parts = [master_name, *parts]
        for part in all_parts:
            if not part or "." in part:
                raise ValueError(f"Invalid ImportString parts: {parts} - {part}")
            self.parts.append(part)

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
        result.parts.clear()
        return result

    @classmethod
    def parent(cls: type[Self]) -> Self:
        """
        Get parent ImportString.
        """
        result = cls.empty()
        result.parts.append("")
        return result

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
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        """
        Whether import strings produce the same render.
        """
        return str(self) == str(other)

    def __gt__(self, other: object) -> bool:
        """
        Compare import strings for sorting.

        Emulates `isort` logic.
        """
        return str(self) > str(other)

    def __add__(self: Self, other: Self | str) -> Self:
        """
        Create a new import string by adding another import string parts to the end.
        """
        other_import_string = other if isinstance(other, ImportString) else ImportString(other)
        result = self.__class__.empty()
        result.parts = self.parts + other_import_string.parts
        return result

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

            ImportString('my', 'name').startswith(ImportString.empty())
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
            return "builtins"

        return self.parts[0]
