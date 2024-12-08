"""
prompt_toolkit style wrapper.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from prompt_toolkit.styles import Style

if TYPE_CHECKING:
    from prompt_toolkit.formatted_text import StyleAndTextTuples

    from mypy_boto3_builder.chat.type_defs import Message


class TextStyle(Enum):
    """
    prompt_toolkit style wrapper.
    """

    bot = "bot"
    user = "user"
    help = "help"
    text = "text"
    tag = "tag"
    dim = "dim"
    hilight = "hilight"

    @property
    def style(self) -> str:
        """
        Class usage name.
        """
        return f"class:{self.value}"

    @property
    def css(self) -> str:  # noqa: PLR0911
        """
        CSS properties for class.
        """
        match self:
            case TextStyle.bot:
                return "fg:#762671 bold"
            case TextStyle.user:
                return "fg:#39B54A bold"
            case TextStyle.help:
                return "fg:cyan bold"
            case TextStyle.text:
                return ""
            case TextStyle.tag:
                return "fg:#2CB5E9 bold"
            case TextStyle.dim:
                return "fg:gray"
            case TextStyle.hilight:
                return "fg:#FF9D00 bold"

    @classmethod
    def get_style(cls) -> Style:
        """
        Generate prompt_toolkit.Style.
        """
        return Style([(i.value, i.css) for i in cls])

    def apply(self, message: Message | str) -> list[tuple[TextStyle, str]]:
        """
        Apply styling for internal usage.
        """
        if not message:
            return []
        if isinstance(message, str):
            return [(self, message)]

        result: list[tuple[TextStyle, str]] = []
        for item in message:
            if isinstance(item, str):
                result.append((self, item))
                continue
            item_style, item_text = item
            if isinstance(item_style, str):
                result.append((self.__class__(item_style.replace("class:", "")), item_text))
                continue
            result.append((item_style, item_text))
        return result

    def stylize(self, message: Message | str) -> StyleAndTextTuples:
        """
        Stylize for prompt_toolkit.
        """
        if not message:
            return []
        if isinstance(message, str):
            return [(self.style, message)]

        result: StyleAndTextTuples = []
        for item in message:
            if isinstance(item, str):
                result.append((self.style, item))
                continue
            item_style, item_text = item
            if isinstance(item_style, str):
                result.append((item_style, item_text))
                continue
            result.append((item_style.style, item_text))
        return result
