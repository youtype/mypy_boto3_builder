"""
Jinja2 renderer and black formatter.
"""

import tempfile
from collections.abc import Iterable
from pathlib import Path
from typing import Literal

import mdformat
from black import format_file_contents
from black.mode import Mode, TargetVersion
from black.parsing import InvalidInput
from black.report import NothingChanged
from isort.api import sort_code_string
from isort.settings import Config

from mypy_boto3_builder.constants import LINE_LENGTH
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.utils.jinja2 import render_jinja2_template
from mypy_boto3_builder.utils.markdown import TableOfContents
from mypy_boto3_builder.utils.version import get_supported_python_versions


def blackify(content: str, file_path: Path) -> str:
    """
    Format `content` with `black` if `file_path` is `*.py` or `*.pyi`.

    On error writes invalid `content` to `file_path` to check for errors.

    Arguments:
        content -- Python code to format.
        file_path -- Target file path.

    Returns:
        Formatted python code.

    Raises:
        ValueError -- If `content` is not a valid Python code.
    """
    if file_path.suffix.lower() not in (".py", ".pyi"):
        return content

    is_pyi = file_path.suffix.lower() == ".pyi"
    python_versions = get_supported_python_versions()
    target_versions: set[TargetVersion] = set()
    for version in python_versions:
        key = f"PY{version.replace('.', '')}"
        if key in TargetVersion.__members__:
            target_versions.add(TargetVersion[key])
    file_mode = Mode(
        target_versions=target_versions, is_pyi=is_pyi, line_length=LINE_LENGTH, preview=True
    )
    try:
        content = format_file_contents(content, fast=True, mode=file_mode)
    except NothingChanged:
        pass
    except (IndentationError, InvalidInput) as e:
        if not file_path.parent.exists():
            file_path.parent.mkdir(exist_ok=True, parents=True)
        file_path.write_text(content)
        raise ValueError(f"Cannot parse {file_path.as_posix()}: {e}") from e

    return content


def sort_imports(
    content: str,
    module_name: str,
    extension: Literal["py", "pyi"] = "py",
    third_party: Iterable[str] = (),
) -> str:
    """
    Sort imports with `isort`.

    Arguments:
        content -- File content.
        module_name -- Current module name.
        extension -- py or pyi
        third_party -- List of module names to be marked as third-party.

    Returns:
        New file content.
    """
    known_third_party = list(third_party) or [
        "aiobotocore",
        "boto3",
        "botocore",
        "typing_extensions",
        "mypy_boto3",
    ]
    if module_name in known_third_party:
        known_third_party.remove(module_name)

    result = sort_code_string(
        code=content,
        extension=extension,
        config=Config(
            profile="black",
            known_first_party=[module_name],
            known_third_party=known_third_party,
            line_length=LINE_LENGTH,
        ),
    )
    return result or ""


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
        package=package,
        service_name=package.service_name if len(package.service_names) == 1 else None,
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
    return mdformat.text(  # type: ignore
        text,
        options={
            "wrap": 79,
            "number": True,
        },
    )


def blackify_markdown(text: str) -> str:
    """
    Blackify python codeblocks.
    """
    result: list[str] = []
    blocks = text.split("\n```")
    for block in blocks:
        if block.startswith("python"):
            path = Path(tempfile.gettempdir()) / "output.py"
            blackified = blackify(block, path).rstrip()
            result.append(blackified)
        else:
            result.append(block)
    return "\n```".join(result)
