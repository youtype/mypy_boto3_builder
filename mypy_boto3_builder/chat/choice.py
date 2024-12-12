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
        self._raw_title = title
        self.selected_suffix = TextStyle.hilight.apply(selected_suffix or " ✓")
        choice_title = TextStyle.text.stylize(title)
        self.key = key or TextStyle.to_str(choice_title) or "(empty)"
        super().__init__(
            title=choice_title,
            value=self.key,
            shortcut_key=shortcut_key or False,
            disabled="✓" if disabled else None,
        )
        self.text: Message | str = self.key if text is None else text
        self.aliases = aliases or (self.key,)
        self._is_selected = False

    def __hash__(self) -> int:
        """
        Hashable by key.
        """
        return hash(self.value)

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

    def select(self) -> None:
        """
        Select choice.
        """
        self.title = TextStyle.dim.stylize(
            (
                *TextStyle.to_message(self._raw_title),
                *self.selected_suffix,
            )
        )
        self._is_selected = True

    def deselect(self) -> None:
        """
        Deselect choice.
        """
        self.title = TextStyle.text.stylize(self._raw_title)
        self._is_selected = False
