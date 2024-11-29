from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

from mypy_boto3_builder.constants import TemplatePath
from mypy_boto3_builder.package_data import (
    TypesBoto3LitePackageData,
    TypesBoto3PackageData,
)
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.writers.processors import (
    process_mypy_boto3,
    process_types_boto3,
    process_types_boto3_docs,
    process_types_boto3_lite,
)


class TestProcessors:
    @patch("mypy_boto3_builder.writers.processors.parse_types_boto3_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_types_boto3(
        self,
        PackageWriterMock: MagicMock,
        parse_types_boto3_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        package_mock = MagicMock()
        parse_types_boto3_package_mock.return_value = package_mock
        result = process_types_boto3(
            output_path=Path("my_path"),
            service_names=[ServiceNameCatalog.ec2],
            generate_package=True,
            package_data=TypesBoto3PackageData,
            version="1.2.3",
            template_path=TemplatePath.types_boto3,
            static_files_path=Path("static_files_path"),
        )
        PackageWriterMock().write_package.assert_called_once_with(
            package=package_mock,
            template_path=ANY,
            static_files_path=ANY,
        )
        parse_types_boto3_package_mock.assert_called_once_with(
            service_names=[ServiceNameCatalog.ec2],
            package_data=TypesBoto3PackageData,
            version="1.2.3",
        )
        assert result == package_mock

    @patch("mypy_boto3_builder.writers.processors.parse_types_boto3_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_types_boto3_lite(
        self,
        PackageWriterMock: MagicMock,
        parse_types_boto3_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        package_mock = MagicMock()
        parse_types_boto3_package_mock.return_value = package_mock
        result = process_types_boto3_lite(
            output_path=Path("my_path"),
            service_names=[ServiceNameCatalog.ec2],
            generate_package=True,
            package_data=TypesBoto3LitePackageData,
            version="1.2.3",
            static_files_path=Path("static_files_path"),
        )
        PackageWriterMock().write_package.assert_called_once_with(
            package=package_mock,
            template_path=ANY,
            static_files_path=ANY,
            exclude_template_names=[
                "session.pyi.jinja2",
                "__init__.pyi.jinja2",
            ],
        )
        parse_types_boto3_package_mock.assert_called_once_with(
            service_names=[ServiceNameCatalog.ec2],
            package_data=TypesBoto3LitePackageData,
            version="1.2.3",
        )
        assert result == package_mock

    @patch("mypy_boto3_builder.writers.processors.parse_mypy_boto3_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_mypy_boto3(
        self,
        PackageWriterMock: MagicMock,
        parse_mypy_boto3_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        service_name_mock = MagicMock()
        result = process_mypy_boto3(
            output_path=Path("my_path"),
            service_names=[service_name_mock],
            version="1.2.3",
            generate_package=True,
        )
        PackageWriterMock().write_package.assert_called()
        parse_mypy_boto3_package_mock.assert_called_with(
            service_names=[service_name_mock],
            version="1.2.3",
        )
        assert result == parse_mypy_boto3_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_types_boto3_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_types_boto3_docs(
        self,
        PackageWriterMock: MagicMock,
        parse_types_boto3_package_mock: MagicMock,
    ) -> None:
        service_name_mock = MagicMock()
        result = process_types_boto3_docs(
            output_path=Path("my_path"),
            service_names=[service_name_mock],
            package_data=TypesBoto3PackageData,
            version="1.2.3",
        )
        PackageWriterMock().write_docs.assert_called()
        parse_types_boto3_package_mock.assert_called_with(
            service_names=[service_name_mock],
            package_data=TypesBoto3PackageData,
            version="1.2.3",
        )
        assert result == parse_types_boto3_package_mock()
