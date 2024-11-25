"""
Product library for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class ProductLibrary(Enum):
    """
    Product library for CLI.
    """

    boto3 = "boto3"
    aiobotocore = "aiobotocore"
    aioboto3 = "aioboto3"
