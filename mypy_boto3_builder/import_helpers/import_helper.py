"""
Wrapper for ImportString usage.

Copyright 2024 Vlad Emelianov
"""

from typing import Final

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.import_helpers.import_parent import ImportParent
from mypy_boto3_builder.import_helpers.import_string import ImportString


class Import:
    """
    Wrapper for ImportString usage.
    """

    future: Final = ImportString(ImportParent.future.value)
    builtins: Final = ImportString(ImportParent.builtins.value)
    boto3: Final = ImportString(ImportParent.boto3.value)
    botocore: Final = ImportString(ImportParent.botocore.value)
    typing: Final = ImportString(ImportParent.typing.value)
    awscrt: Final = ImportString(ImportParent.awscrt.value)
    s3transfer: Final = ImportString(ImportParent.s3transfer.value)
    aiobotocore: Final = ImportString(ImportParent.aiobotocore.value)
    aioboto3: Final = ImportString(ImportParent.aioboto3.value)
    typing_extensions: Final = ImportString(ImportParent.typing_extensions.value)
    types: Final = ImportString(ImportParent.types.value)
    sys: Final = ImportString(ImportParent.sys.value)

    @classmethod
    def local(cls, module_name: str) -> ImportString:
        """
        Create local import string.
        """
        if not module_name:
            raise StructureError("Module name cannot be empty for local import")
        return ImportString("", module_name)

    @classmethod
    def from_str(cls, import_string: str) -> ImportString:
        """
        Create from string.
        """
        return cls.from_parts(*import_string.split("."))

    @classmethod
    def from_parts(cls, parent: str, *parts: str) -> ImportString:
        """
        Create from string.
        """
        if not parent:
            raise StructureError("Parent cannot be empty")
        return ImportString(parent, *parts)
