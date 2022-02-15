"""
Structure for boto3-stubs module.
"""
from collections.abc import Iterable

from mypy_boto3_builder.package_data import MypyBoto3PackageData
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
        super().__init__(MypyBoto3PackageData, service_names)
        self.service_packages = list(service_packages)

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
