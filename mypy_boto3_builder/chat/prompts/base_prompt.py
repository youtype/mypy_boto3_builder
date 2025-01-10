"""
Base wrapper for questionary.Question.

Copyright 2024 Vlad Emelianov
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any, ClassVar, Final, Generic, TypeVar
from unittest.mock import patch

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding.key_bindings import Binding
from prompt_toolkit.keys import Keys
from questionary.question import Question

from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message

_R = TypeVar("_R")


class BasePrompt(ABC, Generic[_R]):
    """
    Base wrapper for questionary.Question.
    """

    PROMPT_SESSION_MODULE: ClassVar = "questionary.prompts.common.PromptSession"
    STYLE: Final = TextStyle.get_style()
    HELP_MESSAGE: ClassVar[Message] = ()

    def __init__(self) -> None:
        self._question: Question | None = None
        self._result: _R | None = None

    def get_help_message(self) -> Message:
        """
        Get help message.
        """
        return self.HELP_MESSAGE

    @property
    def question(self) -> Question:
        """
        PromptSession of a currently running application.
        """
        if self._question is None:
            raise ValueError("Question is not set")
        return self._question

    def _get_enter_key_binding(self) -> Binding:
        key_bindings = self.question.application.key_bindings
        if not key_bindings:
            raise ValueError("Key bindings are not set")
        for key_binding in reversed(key_bindings.bindings):
            if key_binding.keys == (Keys.ControlM,):
                return key_binding
        raise ValueError("Key binding for Enter not found.")

    @contextmanager
    def _patch_session(self) -> Iterator[None]:
        message = self.get_prompt_tokens

        class PatchedPromptSession(PromptSession[Any]):
            """
            Patched PromptSession with custom message.
            """

            def __init__(self, *args: Any, **kwargs: Any) -> None:  # noqa: ANN401
                if args:
                    args = (message, *args[1:])
                super().__init__(*args, **kwargs)

        with patch(self.PROMPT_SESSION_MODULE, PatchedPromptSession):
            yield

    def get_prompt_tokens(self) -> list[tuple[str, str]]:
        """
        Get prompt tokens for PromptSession.
        """
        return TextStyle.text.stylize(self._get_prompt_tokens())

    @abstractmethod
    def _get_prompt_tokens(self) -> Message:
        raise NotImplementedError("Method is not implemented")

    def _is_answered(self) -> bool:
        return self._result is not None

    def get_question(self) -> Question:
        """
        Create an underlying question.
        """
        if self._question:
            return self._question
        with self._patch_session():
            self._question = self._create_question()
        self._patch_answer()
        return self._question

    @abstractmethod
    def _create_question(self) -> Question:
        raise NotImplementedError("Method is not implemented")

    def _patch_answer(self) -> None:
        pass

    def ask(self) -> _R:
        """
        Ask a question and return a result.
        """
        question = self.get_question()
        question.unsafe_ask()
        if self._result is None:
            raise ValueError("Result is not set")
        return self._result

    def _set_result(self, result: _R) -> None:
        """
        Set a result.
        """
        self._result = result
