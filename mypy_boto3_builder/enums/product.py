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

    types_aiobotocore = "aiobotocore"
    types_aiobotocore_lite = "aiobotocore-lite"
    types_aiobotocore_services = "aiobotocore-services"
    types_aiobotocore_full = "aiobotocore-full"
    types_aiobotocore_custom = "aiobotocore-custom"
    types_aiobotocore_docs = "aiobotocore-docs"

    types_aioboto3 = "aioboto3"
    types_aioboto3_lite = "aioboto3-lite"
    types_aioboto3_custom = "aioboto3-custom"
    types_aioboto3_docs = "aioboto3-docs"

    boto3_stubs = "boto3"
    boto3_stubs_lite = "boto3-lite"
    boto3_stubs_services = "boto3-services"
    boto3_stubs_full = "boto3-full"
    boto3_stubs_custom = "boto3-custom"
    boto3_stubs_docs = "boto3-docs"

    mypy_boto3 = "mypy-boto3"

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
                Product.boto3_stubs
                | Product.boto3_stubs_lite
                | Product.boto3_stubs_services
                | Product.boto3_stubs_full
                | Product.boto3_stubs_docs
                | Product.boto3_stubs_custom
            ):
                return ProductLibrary.boto3_legacy
            case (
                Product.types_aiobotocore
                | Product.types_aiobotocore_lite
                | Product.types_aiobotocore_services
                | Product.types_aiobotocore_full
                | Product.types_aiobotocore_docs
                | Product.types_aiobotocore_custom
            ):
                return ProductLibrary.aiobotocore
            case (
                Product.types_aioboto3
                | Product.types_aioboto3_lite
                | Product.types_aioboto3_docs
                | Product.types_aioboto3_custom
            ):
                return ProductLibrary.aioboto3
            case Product.mypy_boto3:
                return ProductLibrary.mypy_boto3

    def get_type(self) -> ProductType:
        """
        Get product type.
        """
        match self:
            case (
                Product.types_boto3
                | Product.boto3_stubs
                | Product.types_aiobotocore
                | Product.types_aioboto3
                | Product.mypy_boto3
            ):
                return ProductType.stubs
            case (
                Product.types_boto3_lite
                | Product.boto3_stubs_lite
                | Product.types_aiobotocore_lite
                | Product.types_aioboto3_lite
            ):
                return ProductType.stubs_lite
            case (
                Product.types_boto3_services
                | Product.boto3_stubs_services
                | Product.types_aiobotocore_services
            ):
                return ProductType.service_stubs
            case (
                Product.types_boto3_docs
                | Product.boto3_stubs_docs
                | Product.types_aiobotocore_docs
                | Product.types_aioboto3_docs
            ):
                return ProductType.docs
            case (
                Product.types_boto3_full | Product.boto3_stubs_full | Product.types_aiobotocore_full
            ):
                return ProductType.full
            case (
                Product.types_boto3_custom
                | Product.boto3_stubs_custom
                | Product.types_aiobotocore_custom
                | Product.types_aioboto3_custom
            ):
                return ProductType.custom
