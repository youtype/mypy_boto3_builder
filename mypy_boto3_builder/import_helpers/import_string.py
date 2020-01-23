"""
Wrapper for Python import strings.
"""
from typing import Any, List


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
        self.parts: List[str] = []
        all_parts = [master_name, *parts]
        for part in all_parts:
            if not part or "." in part:
                raise ValueError(f"Invalid ImportString parts: {parts}")
            self.parts.append(part)

    @classmethod
    def from_str(cls, import_string: str) -> "ImportString":
        return cls(*import_string.split("."))

    @classmethod
    def empty(cls) -> "ImportString":
        result = cls("fake")
        result.parts.clear()
        return result

    def __bool__(self) -> bool:
        return bool(self.parts)

    def __str__(self) -> str:
        return self.render()

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return str(self) == str(other)

    def __gt__(self, other: Any) -> bool:
        return str(self) > str(other)

    def __add__(self, other: "ImportString") -> "ImportString":
        parts = self.parts + other.parts
        return ImportString(*parts)

    def startswith(self, other: "ImportString") -> bool:
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
