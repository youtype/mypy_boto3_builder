"""
Constants and paths.
"""
from enum import Enum
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


class ProductLibrary(Enum):
    """
    Product library for Generator.
    """

    boto3 = "boto3"
    aiobotocore = "aiobotocore"
    aioboto3 = "aioboto3"


class ProductType(Enum):
    """
    Product type for Generator.
    """

    stubs = "stubs"
    service_stubs = "service_stubs"
    docs = "docs"


class Product(Enum):
    """
    Product choice for CLI.
    """

    boto3 = "boto3"
    boto3_services = "boto3-services"
    boto3_docs = "boto3-docs"
    aiobotocore = "aiobotocore"
    aiobotocore_services = "aiobotocore-services"
    aiobotocore_docs = "aiobotocore-docs"
    aioboto3 = "aioboto3"
    aioboto3_docs = "aioboto3-docs"

    def __str__(self) -> str:
        return self.name

    def get_library(self) -> ProductLibrary:
        """
        Get library name.
        """
        for library in ProductLibrary:
            if self.value.startswith(library.value):
                return library
        raise ValueError(f"No library found for {self.value}")

    def get_type(self) -> ProductType:
        """
        Get product type.
        """
        if "-" not in self.value:
            return ProductType.stubs
        if self.value.endswith("-services"):
            return ProductType.service_stubs
        if self.value.endswith("-docs"):
            return ProductType.docs
        raise ValueError(f"No type found for {self.value}")
