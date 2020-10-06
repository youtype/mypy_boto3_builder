"""
Boto3 Client.
"""
from typing import List

from botocore.client import BaseClient

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript


class Client(ClassRecord):
    """
    Boto3 Client.
    """

    _alias_name: str = "Client"

    def __init__(
        self, name: str, service_name: ServiceName, boto3_client: BaseClient, docstring: str = ""
    ):
        super().__init__(name=name, docstring=docstring)
        self.service_name = service_name
        self.boto3_client = boto3_client
        self.exceptions_class = ClassRecord(name="Exceptions")
        self.client_error_class = ClassRecord(
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
