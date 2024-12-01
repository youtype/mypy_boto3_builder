"""
Product choice for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum

from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.enums.product_type import ProductType


class Product(Enum):
    """
    Product choice for CLI.
    """

    types_boto3 = "types-boto3"
    types_boto3_lite = "types-boto3-lite"
    types_boto3_services = "types-boto3-services"
    types_boto3_full = "types-boto3-full"
    types_boto3_custom = "types-boto3-custom"
    types_boto3_docs = "types-boto3-docs"

    aiobotocore = "aiobotocore"
    aiobotocore_lite = "aiobotocore-lite"
    aiobotocore_services = "aiobotocore-services"
    aiobotocore_full = "aiobotocore-full"
    aiobotocore_custom = "aiobotocore-custom"
    aiobotocore_docs = "aiobotocore-docs"

    aioboto3 = "aioboto3"
    aioboto3_lite = "aioboto3-lite"
    aioboto3_custom = "aioboto3-custom"
    aioboto3_docs = "aioboto3-docs"

    boto3 = "boto3"
    boto3_lite = "boto3-lite"
    boto3_services = "boto3-services"
    boto3_full = "boto3-full"
    boto3_custom = "boto3-custom"
    boto3_docs = "boto3-docs"

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
            case (
                Product.types_boto3
                | Product.types_boto3_lite
                | Product.types_boto3_services
                | Product.types_boto3_full
                | Product.types_boto3_docs
                | Product.types_boto3_custom
            ):
                return ProductLibrary.boto3
            case (
                Product.boto3
                | Product.boto3_lite
                | Product.boto3_services
                | Product.boto3_full
                | Product.boto3_docs
                | Product.boto3_custom
            ):
                return ProductLibrary.boto3_legacy
            case (
                Product.aiobotocore
                | Product.aiobotocore_lite
                | Product.aiobotocore_services
                | Product.aiobotocore_full
                | Product.aiobotocore_docs
                | Product.aiobotocore_custom
            ):
                return ProductLibrary.aiobotocore
            case (
                Product.aioboto3
                | Product.aioboto3_lite
                | Product.aioboto3_docs
                | Product.aioboto3_custom
            ):
                return ProductLibrary.aioboto3

    def get_type(self) -> ProductType:
        """
        Get product type.
        """
        match self:
            case Product.types_boto3 | Product.boto3 | Product.aiobotocore | Product.aioboto3:
                return ProductType.stubs
            case (
                Product.types_boto3_lite
                | Product.boto3_lite
                | Product.aiobotocore_lite
                | Product.aioboto3_lite
            ):
                return ProductType.stubs_lite
            case (
                Product.types_boto3_services
                | Product.boto3_services
                | Product.aiobotocore_services
            ):
                return ProductType.service_stubs
            case (
                Product.types_boto3_docs
                | Product.boto3_docs
                | Product.aiobotocore_docs
                | Product.aioboto3_docs
            ):
                return ProductType.docs
            case Product.types_boto3_full | Product.boto3_full | Product.aiobotocore_full:
                return ProductType.full
            case (
                Product.types_boto3_custom
                | Product.boto3_custom
                | Product.aiobotocore_custom
                | Product.aioboto3_custom
            ):
                return ProductType.custom
