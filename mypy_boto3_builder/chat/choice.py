"""
Choice for select.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from questionary.prompts.common import Choice as QuestionaryChoice

from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.utils import as_message, as_string

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mypy_boto3_builder.chat.type_defs import Message


class Choice(QuestionaryChoice):
    """
    Choice for select.
    """

    def __init__(
        self,
        title: Message | str,
        *,
        key: str | None = None,
        text: Message | str | None = None,
        aliases: Sequence[str] = (),
        shortcut_key: str | None = None,
        selected_suffix: Message | str | None = None,
        disabled: bool = False,
    ) -> None:
        self.raw_title = title
        self.selected_suffix = TextStyle.hilight.apply(selected_suffix or " ✓")
        choice_title = TextStyle.text.stylize(title)
        self.key = key or as_string(choice_title) or "(empty)"
        super().__init__(
            title=choice_title,
            value=self.key,
            shortcut_key=shortcut_key or False,
            disabled="✓" if disabled else None,
        )
        self.text: Message | str = self.key if text is None else text
        self.aliases = aliases or (self.key,)
        self._is_selected = False
        self.select_index = 0

    def __hash__(self) -> int:
        """
        Hashable by key.
        """
        return hash(self.value)

    @classmethod
    def create(cls, choice: Choice | str) -> Choice:
        """
        Create choice from string.
        """
        return cls(choice) if isinstance(choice, str) else choice

    @property
    def tag(self) -> Message:
        """
        Previous answers.
        """
        return TextStyle.tag.apply(self.text)

    @property
    def answer(self) -> Message:
        """
        Current answer.
        """
        return TextStyle.hilight.apply(self.text)

    @property
    def is_selected(self) -> bool:
        """
        Whether choice is selected.
        """
        return self._is_selected

    def select(self, index: int = 0) -> None:
        """
        Select choice.
        """
        self.title = TextStyle.dim.stylize(
            (
                *as_message(self.raw_title),
                *self.selected_suffix,
            )
        )
        self.select_index = index
        self._is_selected = True

    def deselect(self) -> None:
        """
        Deselect choice.
        """
        self.title = TextStyle.text.stylize(self.raw_title)
        self.select_index = 0
        self._is_selected = False
