"""
Structure for boto3-stubs module.
"""
from collections.abc import Iterable

from boto3 import __version__ as boto3_version

from mypy_boto3_builder.constants import MODULE_NAME, PYPI_NAME
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage


class MasterPackage(Package):
    """
    Structure for mypy-boto3 package.

    Arguments:
        name -- Module name.
        pypi_name -- Module PyPI name.
        service_names -- List of included service names.
        service_packages -- List of included service packages.
    """

    def __init__(
        self,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
        super().__init__(name=MODULE_NAME, pypi_name=PYPI_NAME, service_names=service_names)
        self.service_packages = list(service_packages)
        self.library_name = "boto3"
        self.library_version = boto3_version

    @property
    def essential_service_names(self) -> list[ServiceName]:
        """
        List of services maked as essential.
        """
        result: list[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result
