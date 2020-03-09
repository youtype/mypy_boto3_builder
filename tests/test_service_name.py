import pytest

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog


class TestServiceName:
    def test_init(self) -> None:
        service_name = ServiceName("my-service", "MyService")
        assert service_name.name == "my-service"
        assert service_name.import_name == "my_service"
        assert service_name.class_name == "MyService"
        assert service_name.boto3_version == "latest"
        assert service_name.boto3_name == "my-service"
        assert service_name.module_name == "mypy_boto3_my_service"
        assert service_name.pypi_name == "mypy-boto3-my-service"
        assert service_name.extras_name == "my-service"
        assert (
            service_name.doc_link
            == "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/my-service.html#MyService"
        )

    def test_special_name(self) -> None:
        assert ServiceName("lambda", "MyService").import_name == "lambda_"
        assert ServiceName("lambda", "MyService").module_name == "mypy_boto3_lambda"

    def test_is_essential(self) -> None:
        assert not ServiceName("my-service", "MyService").is_essential()
        assert ServiceName("lambda", "MyService").is_essential()


class TestServiceNameCatalog:
    def test_find(self) -> None:
        assert ServiceNameCatalog.find("ec2").name == "ec2"

        with pytest.raises(ValueError):
            ServiceNameCatalog.find("unknown")
