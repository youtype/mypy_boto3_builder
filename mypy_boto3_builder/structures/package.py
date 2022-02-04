"""
Parent class for all package structures.
"""
from collections.abc import Iterable

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(
        self,
        name: str,
        pypi_name: str,
        service_names: Iterable[ServiceName] = tuple(),
    ) -> None:
        self.name = name
        self.pypi_name = pypi_name
        self.library_name = name
        self.version = "0.0.0"
        self.library_version = "0.0.0"
        self.service_names: list[ServiceName] = list(service_names)
        self.logger = get_logger()

    @property
    def directory_name(self) -> str:
        """
        Directory name to store generated package.
        """
        underscore_package_name = self.name.replace("-", "_")
        return f"{underscore_package_name}_package"

    def __str__(self) -> str:
        return f"{self.name} {self.version} ({self.library_name} {self.library_version})"
