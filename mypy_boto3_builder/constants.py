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
BOTO3_STUBS_STATIC_PATH = Path(__file__).parent / "boto3_stubs_static"

# Static *.pyi files for botocore-stubs
BOTOCORE_STUBS_STATIC_PATH = Path(__file__).parent / "botocore_stubs_static"

# Static *.pyi files for aiobotocore-stubs
AIOBOTOCORE_STUBS_STATIC_PATH = Path(__file__).parent / "aiobotocore_stubs_static"

# Max line length for boto3 docs
LINE_LENGTH = 100


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
