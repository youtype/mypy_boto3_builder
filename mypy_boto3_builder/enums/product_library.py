"""
Product library choice for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class ProductLibrary(Enum):
    """
    Product library choice for CLI.
    """

    types_boto3 = "types-boto3"
    boto3 = "boto3"
    aiobotocore = "aiobotocore"
    aioboto3 = "aioboto3"
