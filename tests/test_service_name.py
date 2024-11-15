from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog


class TestServiceName:
    def test_init(self) -> None:
        service_name = ServiceName("my-service", "MyService")
        assert service_name.name == "my-service"
        assert service_name.import_name == "my_service"
        assert service_name.class_name == "MyService"
        assert service_name.boto3_version == "latest"
        assert service_name.boto3_name == "my-service"
        assert service_name.extras_name == "my-service"
        assert (
            service_name.boto3_doc_link
            == "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/my-service.html#myservice"
        )
        assert (
            service_name.boto3_doc_link_parent
            == "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/my-service"
        )

    def test_special_name(self) -> None:
        assert ServiceName("lambda", "MyService").import_name == "lambda_"

    def test_is_essential(self) -> None:
        assert not ServiceName("my-service", "MyService").is_essential()
        assert ServiceName("lambda", "MyService").is_essential()


class TestServiceNameCatalog:
    def test_add(self) -> None:
        assert ServiceNameCatalog.add("test", "Test").name == "test"
        assert ServiceNameCatalog.add("test", "Test").name == "test"
