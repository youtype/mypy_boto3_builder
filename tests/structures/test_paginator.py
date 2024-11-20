from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.paginator import Paginator


class TestPaginator:
    paginator: Paginator

    def setup_method(self) -> None:
        self.paginator = Paginator(
            name="name",
            operation_name="my_operation_name",
            service_name=ServiceNameCatalog.s3,
            paginator_name="paginator_name",
        )

    def test_init(self) -> None:
        assert self.paginator.name == "name"
        assert self.paginator.operation_name == "my_operation_name"
        assert self.paginator.service_name == ServiceNameCatalog.s3

    def test_boto3_doc_link(self) -> None:
        assert (
            self.paginator.boto3_doc_link
            == "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/paginator/paginator_name.html#S3.Paginator.paginator_name"
        )

    def test_get_client_method(self) -> None:
        result = self.paginator.get_client_method()
        assert result.name == "get_paginator"
        assert result.return_type.name == "name"
        assert result.arguments[1].type_annotation.children == {"my_operation_name"}
