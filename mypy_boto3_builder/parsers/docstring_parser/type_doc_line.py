"""
Structure for parsed as dict `:type:` or `:rtype:` nested lines.
"""
from typing import Any, Iterable, List


class TypeDocLine:
    """
    Structure for parsed as dict `:type:` or `:rtype:` nested lines.

    Arguments:
        name -- Argument or TypedDict key name
        type_name -- Argument or TypedDict key type string.
        line -- Raw original line parts.
        description -- Rest of line for argument or TypedDict key definition.
        indented -- Intended lines.
    """

    def __init__(
        self,
        name: str = "",
        type_name: str = "",
        line: Iterable[str] = tuple(),
        description: str = "",
        indented: Iterable[Any] = tuple(),
    ) -> None:
        self.line = "".join(line)
        self.name = name
        self.type_name = type_name
        self.description = description
        self._indented = indented

    @property
    def indented(self) -> List["TypeDocLine"]:
        """
        Get indented lines list.

        Returns:
            A list of `TypeDocLine`.
        """
        result: List[TypeDocLine] = []
        for line in self._indented:
            result.append(TypeDocLine(**line))
        return result

    @property
    def required(self) -> bool:
        """
        Whether the argument or TypedDict key is required.
        """
        return "REQUIRED" in self.description or "**must**" in self.description

    def render(self) -> str:
        """
        Get original string with indentation.

        Returns:
            A string as close as possible to original.
        """
        result: List[str] = []
        indent = "  " if self.line else ""
        if self.line:
            result.append(self.line)
            result.append("")
        for indented_line in self.indented:
            for indented_line_line in indented_line.render().splitlines():
                result.append(f"{indent}{indented_line_line}")
        return "\n".join(result)
