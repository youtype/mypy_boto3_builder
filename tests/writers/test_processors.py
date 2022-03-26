from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_botocore_stubs,
    process_master,
)


class TestProcessors:
    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_boto3_stubs(
        self,
        PackageWriterMock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        result = process_boto3_stubs(
            session_mock,
            Path("my_path"),
            [service_name_mock],
            True,
            version="1.2.3",
        )
        PackageWriterMock().write_package.assert_called()
        parse_boto3_stubs_package_mock.assert_called_with(
            session_mock, [service_name_mock], Boto3StubsPackageData
        )
        assert result == parse_boto3_stubs_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_master_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_master(
        self,
        PackageWriterMock: MagicMock,
        parse_master_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        result = process_master(
            session_mock,
            Path("my_path"),
            [service_name_mock],
            True,
            version="1.2.3",
        )
        PackageWriterMock().write_package.assert_called()
        parse_master_package_mock.assert_called_with(session_mock, [service_name_mock])
        assert result == parse_master_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_boto3_stubs_docs(
        self,
        PackageWriterMock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        result = process_boto3_stubs_docs(session_mock, Path("my_path"), [service_name_mock])
        PackageWriterMock().write_docs.assert_called()
        parse_boto3_stubs_package_mock.assert_called_with(
            session_mock, [service_name_mock], Boto3StubsPackageData
        )
        assert result == parse_boto3_stubs_package_mock()

    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_botocore_stubs(self, PackageWriterMock: MagicMock) -> None:
        process_botocore_stubs(Path("my_path"), False, "1.2.3")
        PackageWriterMock().write_package.assert_called()
