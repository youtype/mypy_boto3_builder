"""
Structure for boto34 package.

Copyright 2025 Vlad Emelianov
"""

from mypy_boto3_builder.structures.package import Package


class Boto34Package(Package):
    """
    Structure for boto34 package.
    """

    @property
    def pypi_name(self) -> str:
        """
        PyPI package name.
        """
        return "boto34"

    @pypi_name.setter
    def pypi_name(self, value: str) -> None:
        raise NotImplementedError("boto34 package name is fixed")

    @property
    def name(self) -> str:
        """
        Package name.
        """
        return "boto34"
