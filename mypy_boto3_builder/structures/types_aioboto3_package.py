"""
Structure for types-aioboto3 module.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.structures.wrapper_package import WrapperPackage


class TypesAioBoto3Package(WrapperPackage):
    """
    Structure for types-aioboto3 module.
    """

    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` directive.
        """
        result = [
            "Session",
        ]
        return sorted(result)
