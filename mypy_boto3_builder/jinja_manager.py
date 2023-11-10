"""
Jinja2 `Environment` manager.
"""

import datetime
from collections.abc import Callable
from pathlib import Path
from typing import Any

from jinja2.environment import Environment, Template
from jinja2.loaders import FileSystemLoader
from jinja2.runtime import StrictUndefined
from typing_extensions import Self

from mypy_boto3_builder.constants import BUILDER_REPO_URL, TEMPLATES_PATH
from mypy_boto3_builder.utils.strings import get_anchor_link
from mypy_boto3_builder.utils.version import get_builder_version

__all__ = ["JinjaManager", "JinjaManagerError"]


class JinjaManagerError(Exception):
    """
    Base JinjaManager exception.
    """


class JinjaManager:
    """
    Jinja2 `Environment` manager.
    """

    _environment = Environment(
        loader=FileSystemLoader(TEMPLATES_PATH.as_posix()),
        undefined=StrictUndefined,
    )
    _singleton: Self | None = None

    def __init__(self) -> None:
        self._environment.filters["escape_md"] = self.escape_md  # type: ignore
        self.update_globals(
            builder_version=get_builder_version(),
            current_year=str(datetime.datetime.now(datetime.timezone.utc).year),
            get_anchor_link=get_anchor_link,
            hasattr=hasattr,
            len=len,
            sorted=sorted,
            repr=repr,
            builder_repo_url=BUILDER_REPO_URL,
        )
        self._template_cache: dict[Path, Template] = {}

    @classmethod
    def singleton(cls) -> "JinjaManager":
        """
        Get singleton instance.
        """
        if cls._singleton is None:
            cls._singleton = cls()
        return cls._singleton

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

    def get_template(self, template_path: Path) -> Template:
        """
        Get `jinja2.Template`.
        """
        if template_path.is_absolute():
            template_path = template_path.relative_to(TEMPLATES_PATH)

        if template_path in self._template_cache:
            return self._template_cache[template_path]

        template_full_path = TEMPLATES_PATH / template_path

        if not template_full_path.exists():
            raise JinjaManagerError(f"Template {template_full_path} not found")

        template = self._environment.get_template(template_path.as_posix())
        self._template_cache[template_path] = template

        return template
