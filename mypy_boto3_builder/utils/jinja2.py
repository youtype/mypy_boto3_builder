"""
Jinja2-related utils.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from mypy_boto3_builder.jinja_manager import JinjaManager


def render_jinja2_template(template_path: Path, context: Mapping[str, Any]) -> str:
    """
    Render Jinja2 template to a string.

    Arguments:
        template_path -- Relative path to template in `TEMPLATES_PATH`
        kwargs -- Render arguments

    Returns:
        A rendered template.
    """
    template = JinjaManager().get_template(template_path)
    return template.render(context)
