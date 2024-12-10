"""
Choice for select.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from questionary.prompts.common import Choice as QuestionaryChoice

from mypy_boto3_builder.chat.text_style import TextStyle

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mypy_boto3_builder.chat.type_defs import Message, MessagePair


class Choice(QuestionaryChoice):
    """
    Choice for select.
    """

    def __init__(
        self,
        title: Message | str,
        key: str | None = None,
        text: str | None = None,
        aliases: Sequence[str] = (),
        shortcut_key: str | None = None,
    ) -> None:
        choice_title = TextStyle.text.stylize(title)
        self.key = key or TextStyle.to_str(choice_title) or "(empty)"
        super().__init__(
            title=choice_title,
            value=self.key,
            shortcut_key=shortcut_key or False,
        )
        self.text = self.key if text is None else text
        self.aliases = aliases or (self.key,)

    def __hash__(self) -> int:
        """
        Hashable by key.
        """
        return hash(self.value)

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
