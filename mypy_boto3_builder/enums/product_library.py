"""
Product library choice for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class ProductLibrary(Enum):
    """
    Product library choice for CLI.
    """

    boto3 = "boto3"
    boto3_legacy = "boto3-legacy"
    aiobotocore = "aiobotocore"
    aioboto3 = "aioboto3"

    def get_library_name(self) -> str:
        """
        Get library name.
        """
        match self:
            case ProductLibrary.boto3:
                return "boto3"
            case ProductLibrary.boto3_legacy:
                return "boto3"
            case ProductLibrary.aiobotocore:
                return "aiobotocore"
            case ProductLibrary.aioboto3:
                return "aioboto3"

    def get_chat_choice(self) -> str:
        """
        Get chat choice.
        """
        match self:
            case ProductLibrary.boto3:
                return "boto3"
            case ProductLibrary.boto3_legacy:
                return "boto3-stubs"
            case ProductLibrary.aiobotocore:
                return "aiobotocore"
            case ProductLibrary.aioboto3:
                return "aioboto3"
