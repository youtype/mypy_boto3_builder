"""
Boto3 client Waiter.
"""
from dataclasses import dataclass, field
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


@dataclass
class Waiter(ClassRecord):
    """
    Boto3 client Waiter.
    """

    waiter_name: str = "waiter_name"
    service_name: ServiceName = ServiceNameCatalog.ec2
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [TypeClass(Boto3Waiter, alias="Boto3Waiter")]
    )

    def get_client_method(self) -> Method:
        return Method(
            name="get_waiter",
            decorators=[Type.overload],
            docstring=self.docstring,
            arguments=[
                Argument("self", None),
                Argument("waiter_name", TypeLiteral(self.waiter_name)),
            ],
            return_type=ExternalImport(
                source=ImportString(self.service_name.module_name, ServiceModuleName.waiter.value),
                name=self.name,
            ),
        )

    @staticmethod
    def get_base_client_method() -> Method:
        return Method(
            name="get_waiter",
            arguments=[Argument("self", None), Argument("waiter_name", Type.str)],
            return_type=TypeClass(Boto3Waiter, alias="Boto3Waiter"),
        )
