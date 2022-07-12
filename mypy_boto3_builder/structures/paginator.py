"""
Boto3 client Paginator.
"""

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class Paginator(ClassRecord):
    """
    Boto3 client Paginator.
    """

    def __init__(
        self,
        name: str,
        paginator_name: str,
        operation_name: str,
        service_name: ServiceName,
    ):
        super().__init__(
            name=name,
            bases=[ExternalImport(ImportString("botocore", "paginate"), "Paginator")],
        )
        self.operation_name = operation_name
        self.paginator_name = paginator_name
        self.service_name = service_name

    @property
    def boto3_doc_link(self) -> str:
        """
        Link to boto3 docs.
        """
        return self.service_name.get_boto3_doc_link("Paginator", self.paginator_name)

    def get_client_method(self) -> Method:
        """
        Get `get_paginator` method for `Client`.
        """
        return Method(
            name="get_paginator",
            decorators=[Type.overload],
            docstring=self.docstring,
            arguments=[
                Argument("self", None),
                Argument(
                    "operation_name",
                    TypeLiteral(f"{self.name}Name", [self.operation_name]),
                ),
            ],
            return_type=ExternalImport(
                source=ImportString.parent() + ImportString(ServiceModuleName.paginator.value),
                name=self.name,
            ),
        )
