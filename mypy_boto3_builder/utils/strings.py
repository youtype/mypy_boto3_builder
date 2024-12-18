"""
Multiple string utils collection.

Copyright 2024 Vlad Emelianov
"""

import builtins
import datetime
import keyword
import re
import typing
from types import MappingProxyType
from typing import Final, Literal
from unittest.mock import MagicMock

from botocore import xform_name as botocore_xform_name
from botocore.utils import get_service_module_name

from mypy_boto3_builder.constants import DOCSTRING_LINE_LENGTH, DOCSTRING_MAX_LENGTH
from mypy_boto3_builder.exceptions import BuildInternalError, TypeAnnotationError

RESERVED_NAMES: Final = {
    *dir(typing),
    *dir(builtins),
    *keyword.kwlist,
}
AWS_LINK_RE: Final = re.compile(r"`([^`]+\S)\s*<https://(\S+)>`\_*")
REPLACE_DOCSTRING_CHARS: Final = MappingProxyType({"’": "'", "–": "-", " ": " "})  # noqa: RUF001


def get_class_prefix(func_name: str) -> str:
    """
    Get a valid Python class prefix from `func_name`.

    Arguments:
        func_name -- Any string.

    Returns:
        String with a class prefix.
    """
    parts = [capitalize(i) for i in func_name.split("_") if i]
    return "".join(parts)


def get_anchor_link(text: str) -> str:
    """
    Convert header to markdown anchor link.
    """
    return text.strip().replace(" ", "-").replace(".", "").lower()


def is_reserved(word: str) -> bool:
    """
    Check whether variable name conflicts with Python reserved names.
    """
    return word in RESERVED_NAMES


def get_short_docstring(doc: str) -> str:
    """
    Create a short docstring from boto3 documentation.

    Trims docstring to 300 chars.
    Removes double and triple backticks.
    Stops on `**Request syntax**` and `::`.
    Ensures that backticks are closed.
    Replaces `Text <link>` with [Text](link).
    Wraps docstring to 80 chars.
    """
    doc = str(doc)
    if len(doc) > DOCSTRING_MAX_LENGTH:
        doc = f"{doc[:DOCSTRING_MAX_LENGTH - 3]}..."
    result: list[str] = []
    if not doc:
        return ""
    for raw_line in doc.splitlines():
        line = raw_line.strip().removesuffix("::")
        if not line:
            continue
        if line.startswith(":") or line.lower().startswith("**request syntax**"):
            break
        if ". " in line:
            result.append(line.split(". ")[0])
            break
        result.append(line)
        if line.endswith("."):
            break

    result_str = " ".join(result).replace("```", "`").replace("``", "`").replace("\n", " ").strip()
    return clean_artifacts(result_str)


def clean_artifacts(line: str) -> str:
    """
    Remove common artifacts in botocre docs.
    """
    if line.count("`") % 2:
        line = f"{line}`"
    if line and not line.endswith("."):
        line = f"{line}."

    for ch, replacement in REPLACE_DOCSTRING_CHARS.items():
        if ch in line:
            line = line.replace(ch, replacement)

    if "<https:" in line:
        line = AWS_LINK_RE.sub(r"[\g<1>](https://\g<2>)", line)
        # FIXME: temporary fix for pca-connector-ad service
        line = line.replace("https\\:", "https:")
        # FIXME: temporary fix for neptunedata service
        line = line.replace("neptune-db\\:", "neptune-db:")

    return line


def textwrap(text: str, width: int = DOCSTRING_LINE_LENGTH) -> str:
    """
    Wrap text to `width` chars.
    """
    result: list[str] = []
    for raw_line in text.splitlines():
        if len(raw_line) <= width:
            result.append(raw_line)
            continue

        line = raw_line
        while line:
            if len(line) < width:
                result.append(line)
                break
            space_index = line.rfind(" ", 0, width)
            if space_index < 0:
                space_index = line.find(" ", width)

            if space_index < 0:
                result.append(line)
                break

            sub_line = line[:space_index].rstrip()
            next_index = space_index + 1
            line = line[next_index:].lstrip()
            result.append(sub_line)

    return "\n".join(result)


def get_botocore_class_name(metadata: dict[str, str]) -> str:
    """
    Get Botocore class name from Service metadata.
    """
    service_model = MagicMock()
    service_model.service_name = metadata.get("serviceId", "")
    service_model.metadata = metadata
    name = get_service_module_name(service_model)
    return capitalize(name)


def get_type_def_name(*parts: str) -> str:
    """
    Get a valid Python TypeDef class name from `parts`.

    Examples:
        ```python
        get_type_def_name("MyClass", "my_method")  # MyClassMyMethodTypeDef
        ```
    """
    if not parts:
        raise TypeAnnotationError("At least one part is required")

    parts_camelcased = [get_class_prefix(i) for i in parts]
    name = "".join(parts_camelcased)
    return f"{name}TypeDef"


def capitalize(s: str) -> str:
    """
    Capitalize first letter of a string.
    """
    return f"{s[:1].upper()}{s[1:]}"


def xform_name(name: str, sep: str = "_") -> str:
    """
    Convert name to snake_case.

    Arguments:
        name -- Any string.
        sep -- Separator.
    """
    if not sep:
        raise BuildInternalError("Separator is required")
    return botocore_xform_name(name, sep)


def get_pypi_link(package_name: str) -> str:
    """
    Get link to PyPI.
    """
    if not package_name:
        raise BuildInternalError("package_name is required")
    return f"https://pypi.org/project/{package_name}/"


def get_copyright() -> str:
    """
    Get copyright notice.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    return f"Copyright {now.year} Vlad Emelianov"


def extract_docstring_from_html(html: str) -> str:
    """
    Extract docstring from HTML.
    """
    text = str(html)
    start_index = text.find("<p>")
    if start_index < 0:
        return text
    end_index = text.find("</p>", start_index)
    if end_index < 0:
        return text
    return text[start_index + 3 : end_index].strip()


def get_md_doc_link(
    file: Literal[
        "client",
        "service_resource",
        "waiters",
        "paginators",
        "type_defs",
        "literals",
    ],
    *parts: str,
) -> str:
    """
    Get link to MD docs with anchor.

    Arguments:
        file -- HTML file name
        parts -- Anchor parts
    """
    link = f"./{file}.md"
    if not parts:
        return link
    anchor = "".join([get_anchor_link(part) for part in parts])
    return f"{link}#{anchor}"


def escape_md(value: str) -> str:
    """
    Escape underscore characters.
    """
    return value.replace("_", r"\_")
