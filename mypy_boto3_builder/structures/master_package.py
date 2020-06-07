"""
Structure for boto3-stubs module.
"""

from dataclasses import dataclass, field
from typing import List

from mypy_boto3_builder.constants import MODULE_NAME, PYPI_NAME
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage


@dataclass
class MasterPackage(Package):
    """
    Structure for mypy-boto3 package.
    """

    name: str = MODULE_NAME
    pypi_name: str = PYPI_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_packages: List[ServicePackage] = field(default_factory=lambda: [])

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result
