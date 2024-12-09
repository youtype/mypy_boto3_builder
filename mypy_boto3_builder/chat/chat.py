"""
Question CLI interface.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any, Final

import questionary
from prompt_toolkit import Application, PromptSession, print_formatted_text
from prompt_toolkit.formatted_text import AnyFormattedText, FormattedText, StyleAndTextTuples
from prompt_toolkit.layout import ConditionalContainer, HSplit, Window
from questionary.prompts.common import InquirerControl

from mypy_boto3_builder.chat.choice import Choice
from mypy_boto3_builder.chat.choice_map import ChoiceMap
from mypy_boto3_builder.chat.text_style import TextStyle

if TYPE_CHECKING:
    from collections.abc import Sequence

    from prompt_toolkit.renderer import Renderer
    from questionary.question import Question

    from mypy_boto3_builder.chat.type_defs import Message, MessagePair, MessageToken


class Chat:
    """
    Question CLI interface.
    """

    BOT_NAME = "NotAI: "
    USER_NAME = "You:   "
    HELP_NAME = "Note:  "

    STYLE = TextStyle.get_style()

    style = TextStyle

    PAIR: Final = 2

    SELECT_HELP: Final[Message] = (
        "Use ",
        (TextStyle.tag, "arrow keys"),
        " or ",
        (TextStyle.tag, "j/k"),
        " to select an item, then press ",
        (TextStyle.tag, "Enter"),
        ".",
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

    # def _create_inquirer_layout(
    #     self,
    #     ic: InquirerControl,
    #     get_prompt_tokens: AnyFormattedText,
    # ) -> Layout:
    #     """
    #     Create a layout combining question and inquirer selection.
    #     """
    #     ps: PromptSession[Any] = PromptSession(get_prompt_tokens, reserve_space_for_menu=0)
    #     # _fix_unecessary_blank_lines(ps)

    #     validation_prompt: PromptSession[Any] = PromptSession(
    #         bottom_toolbar=lambda: ic.error_message
    #     )

    #     return Layout(
    #         HSplit(
    #             [
    #                 ps.layout.container,
    #                 ConditionalContainer(Window(ic), filter=~IsDone()),
    #                 ConditionalContainer(
    #                     validation_prompt.layout.container,
    #                     filter=Condition(lambda: ic.error_message is not None),
    #                 ),
    #             ]
    #         )
    #     )

    def _patch_question(
        self,
        question: Question,
        get_tokens: AnyFormattedText,
    ) -> None:
        hsplit = question.application.layout.container
        self.session.message = get_tokens
        if not isinstance(hsplit, HSplit):
            raise TypeError("Unexpected layout")
        hsplit.children[0] = self.session.layout.container
        question.application.erase_when_done = True

    def _get_inquirer_control(self, question: Question) -> InquirerControl:
        hsplit = question.application.layout.container
        if not isinstance(hsplit, HSplit):
            raise TypeError("Unexpected layout")
        window_container = hsplit.children[1]
        if not isinstance(window_container, ConditionalContainer):
            raise TypeError("Unexpected layout")

        window = window_container.content
        if not isinstance(window, Window):
            raise TypeError("Unexpected layout")

        result = window.content
        if not isinstance(result, InquirerControl):
            raise TypeError("Unexpected layout")
        return result

    def _format_selected_tokens(self, raw_selected: Sequence[MessagePair]) -> Message:
        selected = [item for item in raw_selected if item]
        if not selected:
            return []

        if len(selected) == 1:
            return [" ", selected[0]]

        if len(selected) == self.PAIR:
            return [" ", selected[0], " and ", selected[1]]

        result: list[MessageToken] = [" "]
        for item in selected[:-1]:
            result.extend((item, ", "))
        result.extend(("and ", selected[-1]))
        return result

    def select_multiple(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        default: str | None = None,
        message_end: Message | str = "",
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
            else Choice(key=finish_choice.key, text="")
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
                choices=(
                    select_finish_choice,
                    *remaining_choices,
                ),
                selected_choices=result,
                default=default,
                erase_when_done=True,
            )
            selected = choice_map.get(selected_str)
            if not selected:
                break

            result.append(selected)

        if not erase_when_done:
            self.respond(
                (
                    *self._as_message(message),
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
        question = questionary.select(
            message="",
            choices=[i.key for i in select_choices],
            default=default,
            style=self.STYLE,
        )

        def get_tokens() -> StyleAndTextTuples:
            tokens: list[MessageToken] = [
                *TextStyle.user.apply(self.HELP_NAME),
                *TextStyle.dim.apply(instruction or self.SELECT_HELP),
                "\n\n",
                *TextStyle.user.apply(self.USER_NAME),
                *self._as_message(message),
            ]

            title = str(self.inquirer_control.get_pointed_at().title)
            selected = choice_map.get(title)
            selected_tokens = [
                *(i.tag for i in selected_choices),
                *((selected.answer,) if selected.text else ()),
            ]
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
        renderer: Renderer = Application().renderer
        formatted_text = FormattedText(
            [*TextStyle.bot.stylize(self.BOT_NAME), *TextStyle.text.stylize(message)]
        )
        print_formatted_text(formatted_text, style=self.STYLE, end="\n\n", output=renderer.output)
        time.sleep(0.1)
        renderer.erase()
