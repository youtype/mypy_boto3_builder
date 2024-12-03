from unittest.mock import MagicMock

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_types_boto3_package


class TestParseWrapperPackage:
    def test_parse_types_boto3_package(self, botocore_session_mock: MagicMock) -> None:
        service_name_mock = MagicMock()
        service_name_mock.underscore_name = "service_name"
        service_name2_mock = MagicMock()
        service_name2_mock.underscore_name = "service_name2"
        botocore_session_mock().resource.return_value = None

        result = parse_types_boto3_package(
            [service_name_mock, service_name2_mock],
            package_data=Boto3StubsPackageData(),
            version="1.2.3",
        )
        assert len(result.session_class.methods) == 2
