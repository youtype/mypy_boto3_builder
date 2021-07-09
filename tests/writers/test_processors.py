from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_botocore_stubs,
    process_master,
    process_service,
    process_service_docs,
)


class TestProcessors:
    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.write_boto3_stubs_package")
    def test_process_boto3_stubs(
        self,
        write_boto3_stubs_package_mock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        write_boto3_stubs_package_mock.return_value = [Path("modified_path")]
        result = process_boto3_stubs(session_mock, Path("my_path"), [service_name_mock], True)
        write_boto3_stubs_package_mock.assert_called_with(
            result,
            Path("my_path"),
            generate_setup=True,
        )
        parse_boto3_stubs_package_mock.assert_called_with(
            session=session_mock, service_names=[service_name_mock]
        )
        assert result == parse_boto3_stubs_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_master_package")
    @patch("mypy_boto3_builder.writers.processors.write_master_package")
    def test_process_master(
        self,
        write_master_package_mock: MagicMock,
        parse_master_package_mock: MagicMock,
    ) -> None:
        write_master_package_mock.return_value = [Path("modified_path")]
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        result = process_master(session_mock, Path("my_path"), [service_name_mock], True)
        write_master_package_mock.assert_called_with(
            result,
            output_path=Path("my_path"),
            generate_setup=True,
        )
        parse_master_package_mock.assert_called_with(session_mock, [service_name_mock])
        assert result == parse_master_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_service_package")
    @patch("mypy_boto3_builder.writers.processors.write_service_package")
    def test_process_service(
        self,
        write_service_package_mock: MagicMock,
        parse_service_package_mock: MagicMock,
    ) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        parse_service_package_mock().typed_dicts = [MagicMock()]
        result = process_service(session_mock, service_name_mock, Path("my_path"), True)
        write_service_package_mock.assert_called_with(
            result,
            output_path=Path("my_path"),
            generate_setup=True,
        )
        parse_service_package_mock.assert_called_with(session_mock, service_name_mock)
        assert result == parse_service_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_service_package")
    @patch("mypy_boto3_builder.writers.processors.write_service_docs")
    def test_process_service_docs(
        self,
        write_service_docs_mock: MagicMock,
        parse_service_package_mock: MagicMock,
    ) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        result = process_service_docs(session_mock, service_name_mock, Path("my_path"))
        write_service_docs_mock.assert_called_with(
            result,
            output_path=Path("my_path"),
        )
        parse_service_package_mock.assert_called_with(session_mock, service_name_mock)
        assert result == parse_service_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.write_boto3_stubs_docs")
    def test_process_boto3_stubs_docs(
        self,
        write_boto3_stubs_docs_mock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        result = process_boto3_stubs_docs(session_mock, Path("my_path"), [service_name_mock])
        write_boto3_stubs_docs_mock.assert_called_with(
            result,
            output_path=Path("my_path"),
        )
        parse_boto3_stubs_package_mock.assert_called_with(session_mock, [service_name_mock])
        assert result == parse_boto3_stubs_package_mock()

    @patch("mypy_boto3_builder.writers.processors.write_botocore_stubs_package")
    def test_process_botocore_stubs(self, write_botocore_stubs_package: MagicMock) -> None:
        process_botocore_stubs(Path("my_path"), False)
        write_botocore_stubs_package.assert_called_with(Path("my_path"), generate_setup=False)
