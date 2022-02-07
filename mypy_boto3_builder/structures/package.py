"""
Parent class for all package structures.
"""
from collections.abc import Iterable
from typing import Literal

from mypy_boto3_builder.constants import AIOBOTOCORE_PYPI_NAME, BOTO3_STUBS_NAME
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
        self.library_name: Literal["boto3", "botocore", "aiobotocore"] = "boto3"
        self.version = "0.0.0"
        self.library_version = "0.0.0"
        self.service_names: list[ServiceName] = list(service_names)
        self.logger = get_logger()

    @property
    def docs_package_name(self) -> str:
        """
        Docs library name.
        """
        if self.library_name == "aiobotocore":
            return AIOBOTOCORE_PYPI_NAME
        return BOTO3_STUBS_NAME

    @property
    def directory_name(self) -> str:
        """
        Directory name to store generated package.
        """
        underscore_package_name = self.pypi_name.replace("-", "_")
        return f"{underscore_package_name}_package"

    def __str__(self) -> str:
        return f"{self.name} {self.version} ({self.library_name} {self.library_version})"

    def get_local_doc_link(self, service_name: ServiceName | None = None) -> str:
        """
        Get link to local docs.
        """
        urls = {
            "boto3": "https://vemel.github.io/boto3_stubs_docs/",
            "botocore": "https://vemel.github.io/boto3_stubs_docs/",
            "aiobotocore": "https://vemel.github.io/types_aiobotocore_docs/",
        }
        url = urls[self.library_name]
        if service_name:
            url = f"{url}{self.get_module_name(service_name)}/"
        return url

    def get_module_name(self, service_name: ServiceName) -> str:
        """
        Get service module name.
        """
        return {
            "boto3": service_name.module_name,
            "botocore": service_name.module_name,
            "aiobotocore": service_name.aiobotocore_module_name,
        }[self.library_name]

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get PyPI package name for a service package.
        """
        return {
            "boto3": service_name.pypi_name,
            "botocore": service_name.pypi_name,
            "aiobotocore": service_name.aiobotocore_pypi_name,
        }[self.library_name]

    def get_service_pypi_link(self, service_name: ServiceName) -> str:
        """
        Get link to PyPI.
        """
        return f"https://pypi.org/project/{self.get_service_pypi_name(service_name)}/"
