"""
Constants and paths.
"""

from pathlib import Path

# Random region to initialize services
DUMMY_REGION = "us-west-2"

# Jinja2 templates for boto3-stubs
TEMPLATES_PATH = Path(__file__).parent / "templates"

# Static *.pyi files for boto3-stubs
BOTO3_STUBS_STATIC_PATH = Path(__file__).parent / "stubs_static" / "boto3"

# Static *.pyi files for types-aiobotocore
AIOBOTOCORE_STUBS_STATIC_PATH = Path(__file__).parent / "stubs_static" / "aiobotocore"

# Static *.pyi files for types-aioboto3
AIOBOTO3_STUBS_STATIC_PATH = Path(__file__).parent / "stubs_static" / "aioboto3"

# Max line length for boto3 docs
LINE_LENGTH = 100

# mypy-boto3-builder GitHub link
BUILDER_REPO_URL = "https://github.com/youtype/mypy_boto3_builder"


# Main logger name
LOGGER_NAME = "mypy_boto3_builder"

# builder CLI entrypoint name
PROG_NAME = "mypy_boto3_builder"

# builder package name
PACKAGE_NAME = "mypy-boto3-builder"

# universal mask for all resources
ALL = "*"

# keys to mark as NotRequired for output TypeDicts
NOT_REQUIRED_OUTPUT_KEYS = ("NextToken", "Contents", "Item", "CommonPrefixes")
