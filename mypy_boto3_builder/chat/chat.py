"""
Question CLI interface.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

import questionary
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.filters.base import Always
from prompt_toolkit.formatted_text import AnyFormattedText, FormattedText
from prompt_toolkit.layout import ConditionalContainer, FloatContainer, HSplit, Window
from prompt_toolkit.shortcuts.prompt import CompleteStyle
from prompt_toolkit.validation import ValidationError
from questionary.prompts.common import InquirerControl

from mypy_boto3_builder.chat.choice import Choice
from mypy_boto3_builder.chat.choice_map import ChoiceMap
from mypy_boto3_builder.chat.text_style import TextStyle

if TYPE_CHECKING:
    from collections.abc import Sequence

    from questionary.question import Question

    from mypy_boto3_builder.chat.type_defs import Message, MessageToken


class Chat:
    """
    Question CLI interface.
    """

    BOT_NAME = "NotAI: "
    USER_NAME = "You:   "
    HELP_NAME = "Note:  "

    STYLE = TextStyle.get_style()

    SELECT_HELP: Final[Message] = (
        "Use ",
        TextStyle.tag.wrap("arrow keys"),
        " to select an item, then press ",
        TextStyle.tag.wrap("Enter"),
        ".",
    )
    PATH_HELP: Final[Message] = (
        "Enter a ",
        TextStyle.tag.wrap("path"),
        " to output directory.",
    )

    def __init__(self) -> None:
        self.session: PromptSession[Any] = PromptSession()
        self._inquirer_control: InquirerControl | None = None

    @property
    def inquirer_control(self) -> InquirerControl:
        """
        InquirerControl of a currently running application.
        """
        if self._inquirer_control is None:
            raise ValueError("InquirerControl is not set")
        return self._inquirer_control

    def _patch_question(
        self,
        question: Question,
        get_tokens: AnyFormattedText,
    ) -> None:
        self.session = PromptSession(get_tokens, reserve_space_for_menu=0)
        question.application.erase_when_done = True

        hsplit = question.application.layout.container.get_children()[0]
        if not isinstance(hsplit, HSplit):
            raise TypeError("Unexpected layout")

        float_container = self.session.layout.container.get_children()[0]
        if not isinstance(float_container, FloatContainer):
            raise TypeError("Unexpected layout")

        window_container = float_container.content.get_children()[1]
        if not isinstance(window_container, ConditionalContainer):
            raise TypeError("Unexpected layout")

        default_buffer_window = window_container.content
        if not isinstance(default_buffer_window, Window):
            raise TypeError("Unexpected layout")

        default_buffer_window.dont_extend_height = Always()
        default_buffer_window.always_hide_cursor = Always()
        hsplit.children[0] = self.session.layout.container

    def _get_inquirer_control(self, question: Question) -> InquirerControl:
        window_container = question.application.layout.container.get_children()[1]
        if not isinstance(window_container, ConditionalContainer):
            raise TypeError("Unexpected layout")

        window = window_container.content
        if not isinstance(window, Window):
            raise TypeError("Unexpected layout")

        result = window.content
        if not isinstance(result, InquirerControl):
            raise TypeError("Unexpected layout")
        return result

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

    def select_multiple(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        default: str | None = None,
        message_end: Message | str = "",
        instruction: Message | str = "",
        finish: Choice | str = "nothing",
        finish_selected: Choice | str | None = None,
        erase_when_done: bool = False,
    ) -> list[str]:
        """
        Select multiple items from list.
        """
        result: list[Choice] = []
        select_choices = self._format_choices(choices)
        finish_choice = finish if isinstance(finish, Choice) else Choice(finish)
        finish_selected = (
            finish_selected
            if finish_selected is not None
            else Choice(title=finish_choice.key, text="")
        )
        finish_selected_choice = (
            finish_selected if isinstance(finish_selected, Choice) else Choice(finish_selected)
        )
        choice_map = ChoiceMap(select_choices)
        while True:
            remaining_choices = [c for c in select_choices if c not in result]
            if not remaining_choices:
                break

            select_finish_choice = finish_selected_choice if result else finish_choice

            selected_str = self.select(
                message=message,
                message_end=message_end,
                instruction=instruction,
                choices=(
                    select_finish_choice,
                    *remaining_choices,
                ),
                selected_choices=result,
                default=default,
                erase_when_done=True,
            )
            if not choice_map.has(selected_str):
                break
            selected = choice_map.get(selected_str)
            result.append(selected)

        if not erase_when_done:
            self.respond(
                (
                    *self._as_message(message),
                    " " if message else "",
                    *self._format_selected_tokens([i.tag for i in (result or [finish_choice])]),
                    *self._as_message(message_end),
                )
            )

        return [i.key for i in result]

    def _as_message(self, message: Message | str) -> Message:
        if isinstance(message, str):
            return (message,)

        return message

    def _format_choices(self, choices: Sequence[Choice | str]) -> tuple[Choice, ...]:
        return tuple(Choice(choice) if isinstance(choice, str) else choice for choice in choices)

    def select_output_path(
        self,
        message: str,
        default: Path | None = None,
        *,
        erase_when_done: bool = False,
    ) -> Path:
        """
        Ask to select an output directory.
        """

        def _validate(path: Path | None) -> bool:
            if not path:
                raise ValidationError(0, "Path should not be empty")
            path = Path(path)
            if path.exists() and not path.is_dir():
                raise ValidationError(0, "Path should be a directory")
            return True

        question = questionary.path(
            message=message,
            qmark=self.USER_NAME[:-1],
            default=default.as_posix() if default else "",
            complete_style=CompleteStyle.READLINE_LIKE,
            style=self.STYLE,
            validate=_validate,
            only_directories=True,
        )
        question.application.erase_when_done = True

        self.say_help(self.PATH_HELP)
        result = question.unsafe_ask()

        if not erase_when_done:
            self.respond((message, " ", TextStyle.tag.wrap(result)))
        return Path(result)

    def confirm(
        self,
        message: Message | str = "",
        message_end: Message | str = "",
        message_yes: Message | str = "I agree",
        message_no: Message | str = "I disagree",
        *,
        erase_when_done: bool = False,
    ) -> bool:
        """
        Confirm a message.
        """
        choices = [
            Choice(title="Yes", key="yes", text=message_yes, shortcut_key="y"),
            Choice(title="No", key="no", text=message_no, shortcut_key="n"),
        ]
        response = self.select(
            message=message,
            message_end=message_end,
            choices=choices,
            erase_when_done=erase_when_done,
        )
        return response == "yes"

    def select(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        selected_choices: Sequence[Choice] = (),
        default: str | None = None,
        message_end: Message | str = "",
        instruction: Message | str = "",
        erase_when_done: bool = False,
    ) -> str:
        """
        Select one item from list.
        """
        select_choices = self._format_choices(choices)
        choice_map = ChoiceMap(select_choices)
        original_shortcut_keys = list(InquirerControl.SHORTCUT_KEYS)
        InquirerControl.SHORTCUT_KEYS = original_shortcut_keys * 100
        question = questionary.select(
            message="",
            choices=select_choices,
            default=default,
            style=self.STYLE,
            use_shortcuts=True,
            use_jk_keys=False,
        )
        InquirerControl.SHORTCUT_KEYS = original_shortcut_keys

        def get_tokens() -> list[tuple[str, str]]:
            tokens: list[MessageToken] = [
                TextStyle.help.wrap(self.HELP_NAME),
                *TextStyle.dim.apply(instruction or self.SELECT_HELP),
                "\n\n",
                TextStyle.user.wrap(self.USER_NAME),
                *self._as_message(message),
                " " if message else "",
            ]

            title = str(self.inquirer_control.get_pointed_at().value)
            selected = choice_map.get(title)
            selected_tokens = (
                *(i.tag for i in selected_choices),
                *((selected.answer,) if selected.text else ()),
            )
            tokens.extend(self._format_selected_tokens(selected_tokens))
            tokens.extend(self._as_message(message_end))

            return TextStyle.text.stylize(tokens)

        self._inquirer_control = self._get_inquirer_control(question)
        self._patch_question(question, get_tokens)
        response = question.unsafe_ask()
        selected = choice_map.get(response)
        if not erase_when_done:
            self.respond(
                [
                    *self._as_message(message),
                    " " if message else "",
                    *self._format_selected_tokens([selected.tag]),
                    *self._as_message(message_end),
                ]
            )

        return selected.key

    def respond(self, message: Message | str) -> None:
        """
        Respond as a User.
        """
        result = FormattedText(
            [*TextStyle.user.stylize(self.USER_NAME), *TextStyle.text.stylize(message)]
        )
        print_formatted_text(result, style=self.STYLE, end="\n\n")

    def say(self, message: Message | str) -> None:
        """
        Say as a Bot.
        """
        formatted_text = FormattedText(
            [*TextStyle.bot.stylize(self.BOT_NAME), *TextStyle.text.stylize(message)]
        )
        print_formatted_text(formatted_text, style=self.STYLE, end="\n\n")

    def say_help(self, message: Message | str) -> None:
        """
        Say as a Help.
        """
        formatted_text = FormattedText(
            [*TextStyle.help.stylize(self.HELP_NAME), *TextStyle.dim.stylize(message)]
        )
        print_formatted_text(formatted_text, style=self.STYLE, end="\n\n")
