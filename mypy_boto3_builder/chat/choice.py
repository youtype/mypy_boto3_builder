"""
Choice for select.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from mypy_boto3_builder.chat.text_style import TextStyle

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mypy_boto3_builder.chat.type_defs import MessagePair


class Choice:
    """
    Choice for select.
    """

    def __init__(
        self,
        key: str,
        text: str | None = None,
        aliases: Sequence[str] = (),
    ) -> None:
        self.key = key or "(empty)"
        self.text = key if text is None else text
        self.aliases = aliases or (self.key,)

    def __hash__(self) -> int:
        """
        Hashable by key.
        """
        return hash(self.key)

    @property
    def tag(self) -> MessagePair:
        """
        Previous answers.
        """
        return (TextStyle.tag, self.text)

    @property
    def answer(self) -> MessagePair:
        """
        Current answer.
        """
        return (TextStyle.hilight, self.text)
