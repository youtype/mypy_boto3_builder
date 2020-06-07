"""
Structure for boto3-stubs module.
"""

from dataclasses import dataclass, field
from typing import List

from mypy_boto3_builder.constants import BOTO3_STUBS_NAME
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package


@dataclass
class Boto3StubsPackage(Package):
    """
    Structure for boto3-stubs module.
    """

    name: str = BOTO3_STUBS_NAME
    pypi_name: str = BOTO3_STUBS_NAME
    service_names: List[ServiceName] = field(default_factory=lambda: [])

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result
