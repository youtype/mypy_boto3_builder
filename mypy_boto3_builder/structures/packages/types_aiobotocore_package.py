"""
Structure for types-aiobotocore module.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.structures.packages.wrapper_package import WrapperPackage


class TypesAioBotocorePackage(WrapperPackage):
    """
    Structure for types-aiobotocore module.
    """

    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` directive.
        """
        result = [
            "get_session",
            "Session",
        ]
        return sorted(result)
