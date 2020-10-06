"""
Structure for boto3-stubs module.
"""
from typing import Iterable, List

from mypy_boto3_builder.constants import MODULE_NAME, PYPI_NAME
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage


class MasterPackage(Package):
    """
    Structure for mypy-boto3 package.
    """

    def __init__(
        self,
        name: str = MODULE_NAME,
        pypi_name: str = PYPI_NAME,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
        super().__init__(name=name, pypi_name=pypi_name)
        self.service_names = list(service_names)
        self.service_packages = list(service_packages)

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result
