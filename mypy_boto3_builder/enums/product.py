"""
Product-related enums.
"""

from enum import Enum


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
    full = "full"


class Product(Enum):
    """
    Product choice for CLI.
    """

    boto3 = "boto3"
    boto3_services = "boto3-services"
    boto3_full = "boto3-full"
    boto3_docs = "boto3-docs"
    aiobotocore = "aiobotocore"
    aiobotocore_services = "aiobotocore-services"
    aiobotocore_docs = "aiobotocore-docs"
    aiobotocore_full = "aiobotocore-full"
    aioboto3 = "aioboto3"
    aioboto3_docs = "aioboto3-docs"

    def __str__(self) -> str:
        """
        Get string representation for debugging.
        """
        return self.value

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
        if self.value.endswith("-full"):
            return ProductType.full
        raise ValueError(f"No type found for {self.value}")
