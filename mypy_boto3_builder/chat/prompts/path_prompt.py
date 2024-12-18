"""
Path prompt based on questionary.path.

Copyright 2024 Vlad Emelianov
"""

from pathlib import Path

import questionary
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.shortcuts.prompt import CompleteStyle
from prompt_toolkit.validation import ValidationError

from mypy_boto3_builder.chat.prompts.base_prompt import BasePrompt
from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message, MessageToken
from mypy_boto3_builder.chat.utils import as_message


class PathPrompt(BasePrompt[Path]):
    """
    Path prompt based on questionary.path.
    """

    PROMPT_SESSION_MODULE = "questionary.prompts.path.PromptSession"
    HELP_MESSAGE = (
        "Enter a ",
        TextStyle.tag.wrap("path"),
        " to output directory.",
    )

    def __init__(
        self,
        message: Message | str,
        default: Path | None = None,
        instruction: Message | str = "",
    ) -> None:
        super().__init__()
        self.message = as_message(message)
        self.instruction = as_message(instruction) or self.get_help_message()
        self.default = default
        self._result: Path | None = None

    def _validate(self, path: Path | None) -> bool:
        if not path:
            raise ValidationError(0, "Path should not be empty")
        path = Path(path)
        if path.exists() and not path.is_dir():
            raise ValidationError(0, "Path should be a directory")
        return True

    def _patch_answer(self) -> None:
        enter_key_binding = self._get_enter_key_binding()
        orig_set_answer = enter_key_binding.handler

        def set_answer(event: KeyPressEvent) -> None:
            if event.current_buffer.complete_state is None and event.app.current_buffer.validate(
                set_cursor=True
            ):
                self._set_result(Path(event.app.current_buffer.document.text))
            orig_set_answer(event)

        enter_key_binding.handler = set_answer

    def _get_prompt_tokens(self) -> Message:
        tokens: list[MessageToken] = []
        if not self._is_answered():
            tokens.extend(TextStyle.dim.apply(self.instruction))

        tokens.extend(TextStyle.text.apply(self.message))
        return tokens

    def _create_question(self) -> questionary.Question:
        """
        Create an underlying question.
        """
        return questionary.path(
            "",
            default=self.default.as_posix() if self.default is not None else "",
            complete_style=CompleteStyle.READLINE_LIKE,
            style=self.STYLE,
            validate=self._validate,
            only_directories=True,
        )
