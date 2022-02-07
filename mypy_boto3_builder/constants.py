"""
Constants and paths.
"""
from pathlib import Path

# Master module name
MODULE_NAME = "mypy_boto3"

# aiobotocore module name
AIOBOTOCORE_MODULE_NAME = "types_aiobotocore"

# PyPI module name
PYPI_NAME = "mypy-boto3"

# boto3-stubs lite PyPI module name
BOTO3_STUBS_LITE_PYPI_NAME = "boto3-stubs-lite"

# types-aiobotocore lite PyPI module name
AIOBOTOCORE_STUBS_LITE_PYPI_NAME = "types-aiobotocore-lite"

# aiobotocore PyPI module name
AIOBOTOCORE_PYPI_NAME = "types-aiobotocore"

# Random region to initialize services
DUMMY_REGION = "us-west-2"

# Jinja2 templates for boto3-stubs
TEMPLATES_PATH = Path(__file__).parent / "templates"

# Static *.pyi files for boto3-stubs
BOTO3_STUBS_STATIC_PATH = Path(__file__).parent / "boto3_stubs_static"

# Static *.pyi files for botocore-stubs
BOTOCORE_STUBS_STATIC_PATH = Path(__file__).parent / "botocore_stubs_static"

# Static *.pyi files for aiobotocore-stubs
AIOBOTOCORE_STUBS_STATIC_PATH = Path(__file__).parent / "aiobotocore_stubs_static"

# Boto3 stubs module name
BOTO3_STUBS_NAME = "boto3-stubs"

# Botocore stubs module name
BOTOCORE_STUBS_NAME = "botocore-stubs"

# aiobotocore stubs module name
AIOBOTOCORE_STUBS_NAME = "aiobotocore-stubs"

# Max line length for boto3 docs
LINE_LENGTH = 100

# type defs module name
TYPE_DEFS_NAME = "type_defs"

# Main logger name
LOGGER_NAME = "mypy_boto3_builder"

# builder CLI entrypoint name
PROG_NAME = "mypy_boto3_builder"

# builder package name
PACKAGE_NAME = "mypy-boto3-builder"
