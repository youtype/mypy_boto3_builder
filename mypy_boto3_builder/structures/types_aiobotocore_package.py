"""
Structure for types-aiobotocore module.
"""

from mypy_boto3_builder.structures.wrapper_package import WrapperPackage


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
