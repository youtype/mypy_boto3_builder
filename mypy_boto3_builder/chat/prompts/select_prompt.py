"""
Select prompt based on questionary.path.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator, Sequence
from contextlib import contextmanager

import questionary
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout import ConditionalContainer, Window
from questionary.prompts.common import InquirerControl

from mypy_boto3_builder.chat.choice import Choice
from mypy_boto3_builder.chat.prompts.base_prompt import BasePrompt
from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message, MessageToken
from mypy_boto3_builder.chat.utils import as_message


class SelectPrompt(BasePrompt[list[Choice]]):
    """
    Select prompt based on questionary.path.
    """

    PROMPT_SESSION_MODULE = "questionary.prompts.common.PromptSession"
    HELP_MESSAGE = (
        "Select item using ",
        TextStyle.tag.wrap("arrow keys"),
        ", then press ",
        TextStyle.tag.wrap("Enter"),
        " to continue.",
    )

    def __init__(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        default: Choice | str | None = None,
        message_end: Message | str = "",
        instruction: Message | str = "",
    ) -> None:
        super().__init__()
        self.message = as_message(message)
        self.choices = tuple(Choice.create(choice) for choice in choices)
        self.message_end = as_message(message_end)
        self.instruction = as_message(instruction) or self.get_help_message()
        self.default = default
        self._inquirer_control: InquirerControl | None = None

    @property
    def inquirer_control(self) -> InquirerControl:
        """
        InquirerControl of a currently running application.
        """
        if self._inquirer_control is None:
            raise ValueError("InquirerControl is not set")
        return self._inquirer_control

    def _get_pointed_at(self) -> Choice:
        choice = self.inquirer_control.get_pointed_at()
        if not isinstance(choice, Choice):
            raise TypeError(f"Expected Choice, got {choice}")
        return choice

    def _patch_answer(self) -> None:
        enter_key_binding = self._get_enter_key_binding()

        def set_answer(event: KeyPressEvent) -> None:
            selected_choice = self._get_pointed_at()
            result = [selected_choice]
            self._set_result(result)
            self.inquirer_control.is_answered = True
            event.app.exit(result=result)

        enter_key_binding.handler = set_answer

    @contextmanager
    def _patch_session(self) -> Iterator[None]:
        with super()._patch_session():
            # patch shortcut keys because questionary.select check is incorrect
            original_shortcut_keys = list(InquirerControl.SHORTCUT_KEYS)
            InquirerControl.SHORTCUT_KEYS = original_shortcut_keys * 100
            yield
            InquirerControl.SHORTCUT_KEYS = original_shortcut_keys
            self._inquirer_control = self._get_inquirer_control()

    def _get_prompt_tokens(self) -> Message:
        selected_choices = sorted(
            filter(lambda x: x.is_selected and not x.disabled, self.choices),
            key=lambda x: x.select_index,
        )

        tokens: list[MessageToken] = []
        if not self.inquirer_control.is_answered:
            tokens.extend(TextStyle.dim.apply(self.instruction))

        tokens.extend(as_message(self.message))

        selected_choice = self._get_pointed_at()
        selected_tokens = (
            *(i.tag for i in selected_choices),
            *(
                (selected_choice.answer,)
                if selected_choice.text and not selected_choice.is_selected
                else ()
            ),
        )
        tokens.extend(self._format_selected_tokens(selected_tokens))
        tokens.extend(as_message(self.message_end))

        return tokens

    def _format_selected_tokens(self, raw_selected: Sequence[Message]) -> Message:
        selected = [item for item in raw_selected if item]
        if not selected:
            return []

        if len(selected) == 1:
            return selected[0]

        if len(selected) == 1 + 1:
            return [*selected[0], " and ", *selected[1]]

        result: list[MessageToken] = []
        for item in selected[:-1]:
            result.extend((*item, ", "))
        result.extend(("and ", *selected[-1]))
        return result

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

    def _get_inquirer_control(self) -> InquirerControl:
        window_container = self.question.application.layout.container.get_children()[1]
        if not isinstance(window_container, ConditionalContainer):
            raise TypeError("Unexpected layout")

        window = window_container.content
        if not isinstance(window, Window):
            raise TypeError("Unexpected layout")

        result = window.content
        if not isinstance(result, InquirerControl):
            raise TypeError("Unexpected layout")
        return result
