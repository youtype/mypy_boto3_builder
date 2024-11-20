"""
Jinja2 renderer and formatters.

Copyright 2024 Vlad Emelianov
"""

from pathlib import Path

import mdformat

from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.utils.jinja2 import render_jinja2_template
from mypy_boto3_builder.utils.markdown import TableOfContents


def render_jinja2_package_template(template_path: Path, package: Package) -> str:
    """
    Render Jinja2 package template to a string.

    Arguments:
        template_path -- Relative path to template in `TEMPLATES_PATH`
        package -- Service or wrapper package

    Returns:
        A rendered template.
    """
    return render_jinja2_template(
        template_path,
        {
            "package": package,
            "service_name": package.service_name if len(package.service_names) == 1 else None,
        },
    )


def insert_md_toc(text: str) -> str:
    """
    Insert Table of Contents before the first second-level header.
    """
    toc = TableOfContents.parse(text)
    toc_lines = toc.render().splitlines()
    lines = text.splitlines()
    result: list[str] = []
    inserted = False
    for line in lines:
        if not inserted and line.startswith("## "):
            result.extend(toc_lines)
            result.append("")
            inserted = True

        result.append(line)

    if not inserted:
        result.extend(toc_lines)
        result.append("")

    return "\n".join(result)


def format_md(text: str) -> str:
    """
    Format MarkDown with mdformat.
    """
    return mdformat.text(  # type: ignore[partially-unknown]
        text,
        options={
            "wrap": 79,
            "number": True,
        },
    )
