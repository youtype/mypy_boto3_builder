"""
Jinja2 `Environment` manager.
"""
from typing import Any

import jinja2

from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.version import __version__ as version

__all__ = ["JinjaManager"]


class JinjaManager:
    """
    Jinja2 `Environment` manager.
    """

    _environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH.as_posix()), undefined=jinja2.StrictUndefined,
    )

    @classmethod
    def update_globals(cls, **kwargs: Any) -> None:
        """
        Update global variables in `jinja2.Environment`.

        Arguments:
            kwargs -- Globals to set.
        """
        cls._environment.globals.update(kwargs)

    @classmethod
    def get_environment(cls) -> jinja2.Environment:
        """
        Get `jinja2.Environment`.
        """
        return cls._environment
