"""
Enum with all parent imports.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum
from typing import Final


class ImportParent(Enum):
    """
    Enum with all parent imports.
    """

    future = "__future__"
    builtins = "builtins"
    boto3 = "boto3"
    botocore = "botocore"
    typing = "typing"
    awscrt = "awscrt"
    s3transfer = "s3transfer"
    aiobotocore = "aiobotocore"
    aioboto3 = "aioboto3"
    typing_extensions = "typing_extensions"
    types = "types"
    sys = "sys"

    @classmethod
    def is_third_party(cls, parent_name: str) -> bool:
        """
        Whether import is from 3rd party module.
        """
        return parent_name in _THIRD_PARTY

    @classmethod
    def is_builtins(cls, parent_name: str) -> bool:
        """
        Whether import is from Python `builtins` module.
        """
        return parent_name == cls.builtins.value


_THIRD_PARTY: Final = frozenset(
    (
        ImportParent.boto3.value,
        ImportParent.botocore.value,
        ImportParent.aioboto3.value,
        ImportParent.aiobotocore.value,
        ImportParent.s3transfer.value,
        ImportParent.awscrt.value,
    )
)
