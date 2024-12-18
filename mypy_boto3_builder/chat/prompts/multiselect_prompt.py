"""
Select multiple prompt based on questionary.path.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Sequence

import questionary
from prompt_toolkit.key_binding.key_processor import KeyPressEvent

from mypy_boto3_builder.chat.choice import Choice
from mypy_boto3_builder.chat.prompts.select_prompt import SelectPrompt
from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message
from mypy_boto3_builder.chat.utils import as_string


class MultiSelectPrompt(SelectPrompt):
    """
    Select multiple prompt based on questionary.path.
    """

    HELP_MESSAGE = (
        "Select items using ",
        TextStyle.tag.wrap("arrow keys"),
        ", press ",
        TextStyle.tag.wrap("Enter"),
        " to add or remove item.",
    )

    def __init__(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        default: Choice | str | None = None,
        message_end: Message | str = "",
        instruction: Message | str = "",
        finish_choice: Choice | str = "Go back",
        finish_selected_text: Message | str | None = None,
    ) -> None:
        self.finish_choice = Choice.create(finish_choice)
        self.finish_text = self.finish_choice.text
        self.finish_selected_text = (
            finish_selected_text if finish_selected_text is not None else self.finish_text
        )
        self._selected_choices: list[Choice] = []
        super().__init__(
            message=message,
            choices=(self.finish_choice, *choices),
            default=default,
            message_end=message_end,
            instruction=instruction,
        )
        self._selectable_choices = tuple(
            i for i in self.choices if i != self.finish_choice and not i.disabled
        )

    def get_help_message(self) -> Message:
        """
        Get help message.
        """
        return (
            *super().get_help_message(),
            " Select ",
            TextStyle.tag.wrap(as_string(self.finish_choice.raw_title)),
            " to continue.",
        )

    def _is_all_selected(self) -> bool:
        return len(self._selected_choices) == len(self._selectable_choices)

    def _update_result(self) -> None:
        selected_choice = self._get_pointed_at()
        if selected_choice == self.finish_choice:
            self._set_result(self._selected_choices)
            return
        if selected_choice in self._selected_choices:
            self._selected_choices.remove(selected_choice)
            selected_choice.deselect()
        else:
            self._selected_choices.append(selected_choice)
            select_index = max(i.select_index for i in self.choices) + 1
            selected_choice.select(select_index)
        self.finish_choice.text = (
            self.finish_selected_text if self._selected_choices else self.finish_text
        )
        if self._is_all_selected():
            self._set_result(self._selected_choices)

    def _patch_answer(self) -> None:
        enter_key_binding = self._get_enter_key_binding()

        def set_answer(event: KeyPressEvent) -> None:
            self._update_result()
            if self._result is not None:
                self.inquirer_control.is_answered = True
                event.app.exit(result=self._result)

        enter_key_binding.handler = set_answer

    def _create_question(self) -> questionary.Question:
        """
        Create an underlying question.
        """
        return questionary.select(
            message="",
            choices=self.choices,
            default=self.default,
            style=self.STYLE,
            use_shortcuts=True,
            use_jk_keys=False,
        )
