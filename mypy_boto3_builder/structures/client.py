"""
Boto3 Client.
"""
from dataclasses import dataclass, field
from typing import List

from botocore.client import BaseClient

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.class_record import ClassRecord


@dataclass
class Client(ClassRecord):
    """
    Boto3 Client.
    """

    name: str = "Client"
    alias_name: str = "Client"
    service_name: ServiceName = ServiceNameCatalog.ec2
    boto3_client: BaseClient = None
    exceptions_class: ClassRecord = field(default_factory=lambda: ClassRecord(name="Exceptions"))

    def __hash__(self) -> int:
        return hash(self.service_name)

    def get_all_names(self) -> List[str]:
        return [self.name]
