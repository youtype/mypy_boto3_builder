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
        match self:
            case Product.boto3 | Product.boto3_services | Product.boto3_full | Product.boto3_docs:
                return ProductLibrary.boto3
            case (
                Product.aiobotocore
                | Product.aiobotocore_services
                | Product.aiobotocore_full
                | Product.aiobotocore_docs
            ):
                return ProductLibrary.aiobotocore
            case Product.aioboto3 | Product.aioboto3_docs:
                return ProductLibrary.aioboto3

    def get_type(self) -> ProductType:
        """
        Get product type.
        """
        match self:
            case Product.boto3 | Product.aiobotocore | Product.aioboto3:
                return ProductType.stubs
            case Product.boto3_services | Product.aiobotocore_services:
                return ProductType.service_stubs
            case Product.boto3_docs | Product.aiobotocore_docs | Product.aioboto3_docs:
                return ProductType.docs
            case Product.boto3_full | Product.aiobotocore_full:
                return ProductType.full
