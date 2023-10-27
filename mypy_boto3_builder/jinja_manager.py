"""
Jinja2 `Environment` manager.
"""

import datetime
from collections.abc import Callable
from typing import Any

import jinja2

from mypy_boto3_builder.constants import BUILDER_REPO_URL, TEMPLATES_PATH
from mypy_boto3_builder.utils.strings import get_anchor_link
from mypy_boto3_builder.utils.version import get_builder_version

__all__ = ["JinjaManager"]


class JinjaManager:
    """
    Jinja2 `Environment` manager.
    """

    _environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()),
        undefined=jinja2.StrictUndefined,
    )

    def __init__(self) -> None:
        self._environment.filters["escape_md"] = self.escape_md  # type: ignore
        self.update_globals(
            builder_version=get_builder_version(),
            current_year=str(datetime.datetime.utcnow().year),
            get_anchor_link=get_anchor_link,
            hasattr=hasattr,
            len=len,
            sorted=sorted,
            repr=repr,
            builder_repo_url=BUILDER_REPO_URL,
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

    def get_environment(self) -> jinja2.Environment:
        """
        Get `jinja2.Environment`.
        """
        return self._environment
