"""
Structure for types-aioboto3 module.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.structures.packages.wrapper_package import WrapperPackage
from mypy_boto3_builder.utils.version import get_max_build_version, get_min_build_version
from mypy_boto3_builder.utils.version_getters import get_aiobotocore_version


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

    @property
    def min_library_version(self) -> str:
        """
        Minimum required library version.
        """
        return get_min_build_version(get_aiobotocore_version())

    @property
    def max_library_version(self) -> str:
        """
        Minimum required library version.
        """
        return get_max_build_version(get_aiobotocore_version())
