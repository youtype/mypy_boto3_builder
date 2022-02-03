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
        self.version = "0.0.0"
        self.service_names: list[ServiceName] = list(service_names)
        self.logger = get_logger()

    @property
    def directory_name(self) -> str:
        """
        Directory name to store generated package.
        """
        underscore_package_name = self.name.replace("-", "_")
        return f"{underscore_package_name}_package"

    @property
    def non_stubs_name(self) -> str:
        """
        Original package name for stubs package.
        """
        if self.name.endswith("-stubs"):
            return self.name.rsplit("-", 1)[0]

        return self.name
