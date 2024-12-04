"""
Constants and paths.

Copyright 2024 Vlad Emelianov
"""

from pathlib import Path
from typing import Final

# Root path for the project
ROOT_PATH: Final = Path(__file__).parent

# Jinja2 templates
TEMPLATES_PATH: Final = ROOT_PATH / "templates"

# Max line length for formatting
LINE_LENGTH: Final = 100

# Max line length for formatting docstrings
DOCSTRING_LINE_LENGTH: Final = 80

# Max docstring length extracted from method
DOCSTRING_MAX_LENGTH: Final = 300

# mypy-boto3-builder GitHub link
BUILDER_REPO_URL: Final = "https://github.com/youtype/mypy_boto3_builder"

# Main logger name
LOGGER_NAME: Final = "mypy_boto3_builder"

# builder CLI entrypoint name
PROG_NAME: Final = "mypy_boto3_builder"

# builder package name
PACKAGE_NAME: Final = "mypy-boto3-builder"

# universal mask for all resources
ALL: Final = "*"
ATTRIBUTES: Final = "_attributes"
SERVICE_RESOURCE: Final = "ServiceResource"
CLIENT: Final = "Client"

# python versions supported by output stubs
SUPPORTED_PY_VERSIONS: Final = {
    (3, 8),
    (3, 9),
    (3, 10),
    (3, 11),
    (3, 12),
    (3, 13),
    (3, 14),
}

# default timeout for HTTP requests
REQUEST_TIMEOUT: Final = 120

# Sentinel value for output path for CLI
OUTPUT_PATH_SENTINEL = Path("/tmp/output_path_sentinel")  # noqa: S108


class TemplatePath:
    """
    Template paths.
    """

    mypy_boto3: Final = TEMPLATES_PATH / "mypy-boto3"

    types_boto3: Final = TEMPLATES_PATH / "types-boto3"
    types_boto3_docs: Final = TEMPLATES_PATH / "types-boto3-docs"
    types_boto3_service: Final = TEMPLATES_PATH / "types-boto3-service"
    types_boto3_service_docs: Final = TEMPLATES_PATH / "types-boto3-service-docs"
    types_boto3_full: Final = TEMPLATES_PATH / "types-boto3-full"
    types_boto3_custom: Final = TEMPLATES_PATH / "types-boto3-custom"

    types_aioboto3: Final = TEMPLATES_PATH / "types-aioboto3"
    types_aioboto3_docs: Final = TEMPLATES_PATH / "types-aioboto3-docs"
    types_aioboto3_service_docs: Final = TEMPLATES_PATH / "types-aioboto3-service-docs"
    types_aioboto3_custom: Final = TEMPLATES_PATH / "types-aioboto3-custom"

    types_aiobotocore: Final = TEMPLATES_PATH / "types-aiobotocore"
    types_aiobotocore_docs: Final = TEMPLATES_PATH / "types-aiobotocore-docs"
    types_aiobotocore_service: Final = TEMPLATES_PATH / "types-aiobotocore-service"
    types_aiobotocore_service_docs: Final = TEMPLATES_PATH / "types-aiobotocore-service-docs"
    types_aiobotocore_full: Final = TEMPLATES_PATH / "types-aiobotocore-full"
    types_aiobotocore_custom: Final = TEMPLATES_PATH / "types-aiobotocore-custom"


class StaticStubsPath:
    """
    Static *.pyi files path.
    """

    types_boto3: Final = ROOT_PATH / "stubs_static" / "types-boto3"
    types_aiobotocore: Final = ROOT_PATH / "stubs_static" / "types-aiobotocore"
    types_aioboto3: Final = ROOT_PATH / "stubs_static" / "types-aioboto3"


class StaticStubsPullURL:
    """
    Static *.pyi files zip download URL.
    """

    types_boto3: Final = "https://api.github.com/repos/youtype/types-boto3/zipball/main"
    types_aiobotocore: Final = "https://api.github.com/repos/youtype/types-aiobotocore/zipball/main"
    types_aioboto3: Final = "https://api.github.com/repos/youtype/types-aioboto3/zipball/main"
