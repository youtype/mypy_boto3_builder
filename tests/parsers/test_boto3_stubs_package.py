from unittest.mock import MagicMock, patch

from botocore.exceptions import UnknownServiceError

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.boto3_stubs_package import parse_boto3_stubs_package
from mypy_boto3_builder.service_name import ServiceName


class TestBoto3StubsPackage:
    def test_parse_boto3_stubs_package(self) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        service_name_mock.underscore_name = "service_name"
        service_name2_mock = MagicMock()
        service_name2_mock.underscore_name = "service_name2"

        result = parse_boto3_stubs_package(
            session_mock,
            [service_name_mock, service_name2_mock],
            Boto3StubsPackageData,
        )
        assert result.essential_service_names == [service_name_mock, service_name2_mock]

        session_mock.resource.return_value = None
        parse_boto3_stubs_package(
            session_mock,
            [service_name_mock, service_name2_mock],
            Boto3StubsPackageData,
        )
