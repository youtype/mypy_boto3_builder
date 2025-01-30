from unittest.mock import MagicMock, patch

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.service_package_parser import ServicePackageParser


class TestServicePackageParser:
    @patch("mypy_boto3_builder.parsers.client_parser.ClientExceptionsFactory")
    def test_parse(
        self,
        ClientExceptionsFactoryMock: MagicMock,
        botocore_session_mock: MagicMock,
    ) -> None:
        service_name_mock = MagicMock()
        botocore_session_mock().resource.return_value = None
        service_name_mock.boto3_name = "s3"

        class FakeExceptions:
            _internal = True
            __magic = True
            skip_lowecase = True
            RealException = True
            RealExceptionToo = True

        ClientExceptionsFactoryMock().create_client_exceptions.return_value = FakeExceptions()

        parser = ServicePackageParser(
            service_name_mock,
            package_data=Boto3StubsPackageData(),
            version="1.2.3",
        )
        result = parser.parse()
        assert len(result.client.exceptions_class.attributes) == 2
        assert result.client.exceptions_class.attributes[0].name == "RealException"
        assert result.client.exceptions_class.attributes[1].name == "RealExceptionToo"
        assert result.service_name == service_name_mock
