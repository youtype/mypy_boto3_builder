"""
Mapping for choices.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from mypy_boto3_builder.chat.choice import Choice


class ChoiceMap:
    """
    Mapping for choices.
    """

    def __init__(self, choices: Sequence[Choice]) -> None:
        self._choices: dict[str, Choice] = {}
        for choice in choices:
            for alias in choice.aliases:
                self._choices[alias] = choice

    def get(self, alias: str) -> Choice:
        """
        Get choice by key.
        """
        return self._choices[alias]

    def has(self, alias: str) -> bool:
        """
        Check if choice exists.
        """
        return alias in self._choices

    def __iter__(self) -> list[Choice]:
        """
        Get all choices.
        """
        return list(self._choices.values())
