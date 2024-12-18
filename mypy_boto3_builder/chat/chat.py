"""
Chat assistant.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Sequence
from pathlib import Path

from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from mypy_boto3_builder.chat.choice import Choice
from mypy_boto3_builder.chat.prompts.multiselect_prompt import MultiSelectPrompt
from mypy_boto3_builder.chat.prompts.path_prompt import PathPrompt
from mypy_boto3_builder.chat.prompts.select_prompt import SelectPrompt
from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message
from mypy_boto3_builder.chat.utils import as_message


class Chat:
    """
    Chat assistant.
    """

    BOT_NAME = "NotAI: "
    USER_NAME = "You:   "
    HELP_NAME = "Note:  "

    STYLE = TextStyle.get_style()

    def select_output_path(
        self,
        message: Message | str,
        default: Path | None = None,
    ) -> Path:
        """
        Ask to select an output directory.
        """
        return PathPrompt(
            message=(
                TextStyle.user.wrap(self.USER_NAME),
                *as_message(message),
                " " if message else "",
            ),
            instruction=(
                TextStyle.help.wrap(self.HELP_NAME),
                *PathPrompt.HELP_MESSAGE,
                "\n\n",
            ),
            default=default,
        ).ask()

    def confirm(
        self,
        message: Message | str = "",
        message_end: Message | str = "",
        message_yes: Message | str = "I agree",
        message_no: Message | str = "I disagree",
    ) -> bool:
        """
        Confirm a message.
        """
        choices = [
            Choice(
                title=("Yes ", TextStyle.dim.wrap("(y)")),
                key="yes",
                text=message_yes,
                shortcut_key="y",
            ),
            Choice(
                title=("No ", TextStyle.dim.wrap("(n)")),
                key="no",
                text=message_no,
                shortcut_key="n",
            ),
        ]
        response = self.select(
            message=message,
            message_end=message_end,
            choices=choices,
        )
        return response == "yes"

    def select(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        default: Choice | str | None = None,
        message_end: Message | str = "",
        instruction: Message | str = "",
    ) -> str:
        """
        Select one item from list.
        """
        result = SelectPrompt(
            message=(
                TextStyle.user.wrap(self.USER_NAME),
                *as_message(message),
                " " if message else "",
            ),
            choices=choices,
            instruction=(
                TextStyle.help.wrap(self.HELP_NAME),
                *as_message(instruction or SelectPrompt.HELP_MESSAGE),
                "\n\n",
            ),
            message_end=message_end,
            default=default,
        ).ask()
        return result[0].key

    def select_multiple(
        self,
        message: Message | str,
        choices: Sequence[Choice | str],
        *,
        default: Choice | str | None = None,
        message_end: Message | str = "",
        instruction: Message | str = "",
        finish_choice: Choice | str = "Go back",
        finish_selected_text: Message | str | None = None,
    ) -> list[str]:
        """
        Select multiple items from list.
        """
        prompt = MultiSelectPrompt(
            message=(
                TextStyle.user.wrap(self.USER_NAME),
                *as_message(message),
                " " if message else "",
            ),
            choices=choices,
            instruction=(
                TextStyle.help.wrap(self.HELP_NAME),
                *MultiSelectPrompt.HELP_MESSAGE,
                "\n\n",
            ),
            finish_choice=finish_choice,
            finish_selected_text=finish_selected_text,
            message_end=message_end,
            default=default,
        )
        prompt.instruction = (
            TextStyle.help.wrap(self.HELP_NAME),
            *prompt.get_help_message(),
            " " if instruction else "",
            *as_message(instruction),
            "\n\n",
        )
        result = prompt.ask()
        return [i.key for i in result]

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
