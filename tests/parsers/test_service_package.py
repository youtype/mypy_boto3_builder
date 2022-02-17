from unittest.mock import MagicMock, patch

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.service_package import parse_service_package
from mypy_boto3_builder.service_name import ServiceName


class TestBoto3StubsPackage:
    @patch("mypy_boto3_builder.parsers.client.ClientExceptionsFactory")
    def test_parse_boto3_stubs_package(self, ClientExceptionsFactoryMock: MagicMock) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        session_mock.resource().meta.service_name = "s3"
        session_mock.resource().meta.client.meta.service_model.service_name = "s3"
        service_name_mock.boto3_name = "s3"
        ClientExceptionsFactoryMock.create_client_exceptions.return_value = []

        result = parse_service_package(session_mock, service_name_mock, Boto3StubsPackageData)
        assert result.service_name == service_name_mock
