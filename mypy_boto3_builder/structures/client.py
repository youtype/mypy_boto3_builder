"""
Boto3 Client.
"""
from dataclasses import dataclass, field
from typing import List

from botocore.client import BaseClient

from build.lib.mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass


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
    client_error_class = ClassRecord(
        name="BotocoreClientError",
        attributes=[
            Attribute("MSG_TEMPLATE", Type.str),
        ],
        bases=[TypeClass(BaseException)],
        methods=[
            Method(
                name="__init__",
                arguments=[
                    Argument("self", None),
                    Argument("error_response", TypeSubscript(Type.Dict, [Type.str, Type.Any])),
                    Argument("operation_name", Type.str),
                ],
                return_type=Type.none,
                body_lines=[
                    "self.response: Dict[str, Any]",
                    "self.operation_name: str",
                ],
            ),
        ],
    )

    def __hash__(self) -> int:
        return hash(self.service_name)

    def get_all_names(self) -> List[str]:
        return [self.name]
