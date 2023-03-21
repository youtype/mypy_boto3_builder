"""
Jinja2 `Environment` manager.
"""
from collections.abc import Callable
from typing import Any

import jinja2

from mypy_boto3_builder.constants import TEMPLATES_PATH

__all__ = ["JinjaManager"]


class JinjaManager:
    """
    Jinja2 `Environment` manager.
    """

    _environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
        undefined=jinja2.StrictUndefined,
    )

    @classmethod
    def update_globals(cls, **kwargs: str | bool | Callable[..., Any]) -> None:
        """
        Update global variables in `jinja2.Environment`.

        Arguments:
            kwargs -- Globals to set.
        """
        cls._environment.globals.update(kwargs)  # type: ignore

    @staticmethod
    def escape_md(value: str) -> str:
        """
        Escape underscore characters.
        """
        return value.replace("_", r"\_")

    @classmethod
    def get_environment(cls) -> jinja2.Environment:
        """
        Get `jinja2.Environment`.
        """
        cls._environment.filters["escape_md"] = cls.escape_md  # type: ignore
        return cls._environment
