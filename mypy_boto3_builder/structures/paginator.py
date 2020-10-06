"""
Boto3 client Paginator.
"""
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class Paginator(ClassRecord):
    """
    Boto3 client Paginator.
    """

    def __init__(
        self,
        name: str,
        operation_name: str,
        service_name: ServiceName,
        docstring: str = "",
    ):
        super().__init__(
            name=name,
            docstring=docstring,
            bases=[TypeClass(Boto3Paginator, alias="Boto3Paginator")],
        )
        self.operation_name = operation_name
        self.service_name = service_name

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
