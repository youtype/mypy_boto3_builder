"""
Utils for markdown rendering.
"""

from typing import Iterable, Type, TypeVar

from mypy_boto3_builder.utils.strings import get_anchor_link

_TableOfContents = TypeVar("_TableOfContents", bound="TableOfContents")


class Header:
    """
    Markdown header.

    Arguments:
        title -- Header title
        level -- Header level, 1-6
    """

    def __init__(self, title: str, level: int) -> None:
        self.title = title
        self.level = level

    @property
    def anchor(self) -> str:
        return get_anchor_link(self.title)

    def render(self) -> str:
        indent = "  " * (self.level - 1)
        return f"{indent}- [{self.title}](#{self.anchor})"


class TableOfContents:
    """
    MarkDown Table of Contents.

    Arguments:
        headers -- List of headers
    """

    def __init__(self, headers: Iterable[Header]) -> None:
        self.headers = list(headers)

    @classmethod
    def parse(cls: Type[_TableOfContents], text: str) -> _TableOfContents:
        """
        Parse table of Contents for MarkDown text.

        Arguments:
            text -- MarkDown text.
        """
        headers = []
        in_codeblock = False
        for line in text.splitlines():
            if line.startswith("```"):
                in_codeblock = not in_codeblock
            if in_codeblock:
                continue
            if not line.startswith("#"):
                continue

            level, title = line.split(" ", 1)
            headers.append(Header(title.strip(), len(level)))

        return cls(headers)

    def render(self, max_level: int = 3) -> str:
        result = []
        for header in self.headers:
            if header.level > max_level:
                continue
            result.append(header.render())
        return "\n".join(result)


def fix_pypi_headers(text: str) -> str:
    """
    Parse table of Contents for MarkDown text.

    Arguments:
        text -- MarkDown text.
    """
    result = []
    in_codeblock = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_codeblock = not in_codeblock
        if in_codeblock:
            result.append(line)
            continue
        if not line.startswith("#"):
            result.append(line)
            continue

        level, title = line.split(" ", 1)
        header = Header(title.strip(), len(level))
        result.append(f'<a id="{header.anchor}"></a>')
        result.append("")
        result.append(line)

    return "\n".join(result)
