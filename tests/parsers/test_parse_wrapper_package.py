from unittest.mock import MagicMock

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_boto3_stubs_package


class TestParseWrapperPackage:
    def test_parse_boto3_stubs_package(self) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        service_name_mock.underscore_name = "service_name"
        service_name2_mock = MagicMock()
        service_name2_mock.underscore_name = "service_name2"

        session_mock.resource.return_value = None
        result = parse_boto3_stubs_package(
            session_mock,
            [service_name_mock, service_name2_mock],
            Boto3StubsPackageData,
        )
        assert result.essential_service_names == [service_name_mock, service_name2_mock]
        assert len(result.session_class.methods) == 2
