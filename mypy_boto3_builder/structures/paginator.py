"""
Boto3 client Paginator.
"""
from dataclasses import dataclass, field
from typing import List

from botocore.paginate import Paginator as Boto3Paginator

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
class Paginator(ClassRecord):
    """
    Boto3 client Paginator.
    """

    operation_name: str = "operation_name"
    service_name: ServiceName = ServiceNameCatalog.ec2
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [TypeClass(Boto3Paginator, alias="Boto3Paginator")]
    )

    def get_client_method(self) -> Method:
        return Method(
            name="get_paginator",
            decorators=[Type.overload],
            docstring=self.docstring,
            arguments=[
                Argument("self", None),
                Argument("operation_name", TypeLiteral(self.operation_name)),
            ],
            return_type=ExternalImport(
                source=ImportString(
                    self.service_name.module_name, ServiceModuleName.paginator.value
                ),
                name=self.name,
            ),
        )

    @staticmethod
    def get_base_client_method() -> Method:
        return Method(
            name="get_paginator",
            arguments=[Argument("self", None), Argument("operation_name", Type.str)],
            return_type=TypeClass(Boto3Paginator, alias="Boto3Paginator"),
        )
