"""
Wrapper for Python import strings.
"""
from __future__ import annotations


class ImportString:
    """
    Wrapper for Python import strings.

    Arguments:
        import_string -- Wrapped import string.

    Examples::

        import_string = ImportString('my.name')

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
    def from_str(cls, import_string: str) -> "ImportString":
        """
        Create from string.
        """
        return cls(*import_string.split("."))

    @classmethod
    def empty(cls) -> ImportString:
        """
        Create an empty ImportString.
        """
        result = cls("fake")
        result.parts.clear()
        return result

    @classmethod
    def parent(cls) -> ImportString:
        """
        Get parent ImportString.
        """
        result = cls.empty()
        result.parts.append("")
        return result

    def __bool__(self) -> bool:
        return bool(self.parts)

    def __str__(self) -> str:
        return self.render()

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        return str(self) == str(other)

    def __gt__(self, other: object) -> bool:
        return str(self) > str(other)

    def __add__(self, other: ImportString) -> "ImportString":
        result = ImportString.empty()
        result.parts = self.parts + other.parts
        return result

    def startswith(self, other: ImportString) -> bool:
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
