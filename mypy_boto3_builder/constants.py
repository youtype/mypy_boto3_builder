"""
Constants and paths.
"""

from pathlib import Path
from typing import Final

# Random region to initialize services
DUMMY_REGION: Final[str] = "us-west-2"

# Root path for the project
ROOT_PATH: Final[Path] = Path(__file__).parent

# Jinja2 templates for boto3-stubs
TEMPLATES_PATH: Final[Path] = ROOT_PATH / "templates"

# Max line length for formatting
LINE_LENGTH: Final[int] = 100

# mypy-boto3-builder GitHub link
BUILDER_REPO_URL: Final[str] = "https://github.com/youtype/mypy_boto3_builder"

# Main logger name
LOGGER_NAME: Final[str] = "mypy_boto3_builder"

# builder CLI entrypoint name
PROG_NAME: Final[str] = "mypy_boto3_builder"

# builder package name
PACKAGE_NAME: Final[str] = "mypy-boto3-builder"

# universal mask for all resources
ALL: Final[str] = "*"
ATTRIBUTES: Final[str] = "_attributes"
SERVICE_RESOURCE: Final[str] = "ServiceResource"
CLIENT: Final[str] = "Client"

# keys to mark as NotRequired for output TypeDicts
NOT_REQUIRED_OUTPUT_KEYS: Final[tuple[str, ...]] = (
    "NextToken",
    "Contents",
    "Item",
    "CommonPrefixes",
)

# python versions supported by output stubs
SUPPORTED_PY_VERSIONS: Final[set[tuple[int, int]]] = {
    (3, 8),
    (3, 9),
    (3, 10),
    (3, 11),
    (3, 12),
    (3, 13),
}

# default timeout for HTTP requests
REQUEST_TIMEOUT: Final[int] = 120


class TemplatePath:
    """
    Template paths.
    """

    master: Final[Path] = TEMPLATES_PATH / "master"

    boto3_stubs: Final[Path] = TEMPLATES_PATH / "boto3-stubs"
    boto3_stubs_docs: Final[Path] = TEMPLATES_PATH / "boto3-stubs-docs"
    boto3_stubs_service: Final[Path] = TEMPLATES_PATH / "boto3-stubs-service"
    boto3_stubs_service_docs: Final[Path] = TEMPLATES_PATH / "boto3-stubs-service-docs"
    boto3_stubs_full: Final[Path] = TEMPLATES_PATH / "boto3-stubs-full"

    types_aioboto3: Final[Path] = TEMPLATES_PATH / "types-aioboto3"
    types_aioboto3_docs: Final[Path] = TEMPLATES_PATH / "types-aioboto3-docs"
    types_aioboto3_service_docs: Final[Path] = TEMPLATES_PATH / "types-aioboto3-service-docs"

    types_aiobotocore: Final[Path] = TEMPLATES_PATH / "types-aiobotocore"
    types_aiobotocore_docs: Final[Path] = TEMPLATES_PATH / "types-aiobotocore-docs"
    types_aiobotocore_service: Final[Path] = TEMPLATES_PATH / "types-aiobotocore-service"
    types_aiobotocore_service_docs: Final[Path] = TEMPLATES_PATH / "types-aiobotocore-service-docs"
    types_aiobotocore_full: Final[Path] = TEMPLATES_PATH / "types-aiobotocore-full"


class StaticStubsPath:
    """
    Static *.pyi files path.
    """

    boto3_stubs: Final[Path] = ROOT_PATH / "stubs_static" / "boto3-stubs"
    types_aiobotocore: Final[Path] = ROOT_PATH / "stubs_static" / "types-aiobotocore"
    types_aioboto3: Final[Path] = ROOT_PATH / "stubs_static" / "types-aioboto3"


class StaticStubsPullURL:
    """
    Static *.pyi files zip download URL.
    """

    boto3_stubs: Final[str] = "https://api.github.com/repos/youtype/boto3-stubs/zipball/main"
    types_aiobotocore: Final[str] = (
        "https://api.github.com/repos/youtype/types-aiobotocore/zipball/main"
    )
    types_aioboto3: Final[str] = "https://api.github.com/repos/youtype/types-aioboto3/zipball/main"
