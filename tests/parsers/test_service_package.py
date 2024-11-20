from unittest.mock import MagicMock, patch

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.service_package_parser import ServicePackageParser


class TestBoto3StubsPackage:
    @patch("mypy_boto3_builder.parsers.client.ClientExceptionsFactory")
    def test_parse_boto3_stubs_package(
        self,
        ClientExceptionsFactoryMock: MagicMock,
        boto3_session_mock: MagicMock,
    ) -> None:
        service_name_mock = MagicMock()
        boto3_session_mock().resource.return_value = None
        service_name_mock.boto3_name = "s3"
        ClientExceptionsFactoryMock.create_client_exceptions.return_value = []

        parser = ServicePackageParser(
            service_name_mock,
            package_data=Boto3StubsPackageData,
            version="1.2.3",
        )
        result = parser.parse()
        assert result.service_name == service_name_mock
