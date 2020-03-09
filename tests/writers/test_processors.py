from pathlib import Path
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_master,
    process_service,
)


class TestProcessors:
    @patch("mypy_boto3_builder.writers.processors.write_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.get_logger")
    def test_process_boto3_stubs(
        self, _get_logger_mock: MagicMock, write_boto3_stubs_package_mock: MagicMock
    ) -> None:
        write_boto3_stubs_package_mock.return_value = [Path("modified_path")]
        result = process_boto3_stubs(Path("my_path"), ["service_name"])
        assert isinstance(result, Boto3StubsPackage)
        write_boto3_stubs_package_mock.assert_called_with(result, Path("my_path"))

    @patch("mypy_boto3_builder.writers.processors.parse_master_package")
    @patch("mypy_boto3_builder.writers.processors.write_master_package")
    @patch("mypy_boto3_builder.writers.processors.get_logger")
    def test_process_master(
        self,
        _get_logger_mock: MagicMock,
        write_master_package_mock: MagicMock,
        parse_master_package_mock: MagicMock,
    ) -> None:
        write_master_package_mock.return_value = [Path("modified_path")]
        result = process_master("session", Path("my_path"), ["service_name"])
        write_master_package_mock.assert_called_with(result, Path("my_path"))
        parse_master_package_mock.assert_called_with("session", ["service_name"])
        assert result == parse_master_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_service_package")
    @patch("mypy_boto3_builder.writers.processors.write_service_package")
    @patch("mypy_boto3_builder.writers.processors.get_logger")
    def test_process_service(
        self,
        _get_logger_mock: MagicMock,
        write_service_package_mock: MagicMock,
        parse_service_package_mock: MagicMock,
    ) -> None:
        write_service_package_mock.return_value = [
            Path("modified_path"),
            Path("client.py"),
        ]
        service_name_mock = MagicMock()
        result = process_service("session", service_name_mock, Path("my_path"))
        write_service_package_mock.assert_called_with(result, Path("my_path"))
        parse_service_package_mock.assert_called_with("session", service_name_mock)
        assert result == parse_service_package_mock()
