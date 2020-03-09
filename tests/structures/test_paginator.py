from mypy_boto3_builder.structures.paginator import Paginator


class TestPaginator:
    def test_init(self) -> None:
        paginator = Paginator(
            name="name", operation_name="my_operation_name", service_name="service_name"
        )
        assert paginator.name == "name"
        assert paginator.operation_name == "my_operation_name"
        assert paginator.service_name == "service_name"

    def test_get_client_method(self) -> None:
        paginator = Paginator(name="name", operation_name="my_operation_name")
        result = paginator.get_client_method()
        assert result.name == "get_paginator"
        assert result.return_type.name == "name"
        assert result.arguments[1].type.children[0] == "my_operation_name"
