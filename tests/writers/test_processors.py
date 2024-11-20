from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

from mypy_boto3_builder.package_data import (
    Boto3StubsFullPackageData,
    Boto3StubsLitePackageData,
    Boto3StubsPackageData,
)
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_boto3_stubs_full,
    process_boto3_stubs_lite,
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
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        package_mock = MagicMock()
        parse_boto3_stubs_package_mock.return_value = package_mock
        result = process_boto3_stubs(
            output_path=Path("my_path"),
            service_names=[ServiceNameCatalog.ec2],
            generate_setup=True,
            version="1.2.3",
            static_files_path=Path("static_files_path"),
        )
        PackageWriterMock().write_package.assert_called_once_with(
            package=package_mock,
            templates_path=ANY,
            static_files_path=ANY,
        )
        parse_boto3_stubs_package_mock.assert_called_once_with(
            service_names=[ServiceNameCatalog.ec2],
            package_data=Boto3StubsPackageData,
            version="1.2.3",
        )
        assert result == package_mock

    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_boto3_stubs_lite(
        self,
        PackageWriterMock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        package_mock = MagicMock()
        parse_boto3_stubs_package_mock.return_value = package_mock
        result = process_boto3_stubs_lite(
            output_path=Path("my_path"),
            service_names=[ServiceNameCatalog.ec2],
            generate_setup=True,
            version="1.2.3",
            static_files_path=Path("static_files_path"),
        )
        PackageWriterMock().write_package.assert_called_once_with(
            package=package_mock,
            templates_path=ANY,
            static_files_path=ANY,
            exclude_template_names=[
                "session.pyi.jinja2",
                "__init__.pyi.jinja2",
            ],
        )
        parse_boto3_stubs_package_mock.assert_called_once_with(
            service_names=[ServiceNameCatalog.ec2],
            package_data=Boto3StubsLitePackageData,
            version="1.2.3",
        )
        assert result == package_mock

    @patch("mypy_boto3_builder.writers.processors.parse_master_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_master(
        self,
        PackageWriterMock: MagicMock,
        parse_master_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        service_name_mock = MagicMock()
        result = process_master(
            output_path=Path("my_path"),
            service_names=[service_name_mock],
            version="1.2.3",
            generate_setup=True,
        )
        PackageWriterMock().write_package.assert_called()
        parse_master_package_mock.assert_called_with(
            service_names=[service_name_mock],
            version="1.2.3",
        )
        assert result == parse_master_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_boto3_stubs_docs(
        self,
        PackageWriterMock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        service_name_mock = MagicMock()
        result = process_boto3_stubs_docs(
            output_path=Path("my_path"),
            service_names=[service_name_mock],
            version="1.2.3",
        )
        PackageWriterMock().write_docs.assert_called()
        parse_boto3_stubs_package_mock.assert_called_with(
            service_names=[service_name_mock],
            package_data=Boto3StubsPackageData,
            version="1.2.3",
        )
        assert result == parse_boto3_stubs_package_mock()

    @patch("mypy_boto3_builder.writers.processors.parse_boto3_stubs_package")
    @patch("mypy_boto3_builder.writers.processors.PackageWriter")
    def test_process_boto3_stubs_full(
        self,
        PackageWriterMock: MagicMock,
        parse_boto3_stubs_package_mock: MagicMock,
    ) -> None:
        PackageWriterMock().write_package.return_value = [Path("modified_path")]
        package_mock = MagicMock()
        parse_boto3_stubs_package_mock.return_value = package_mock
        result = process_boto3_stubs_full(
            output_path=Path("my_path"),
            service_names=[ServiceNameCatalog.ec2],
            version="1.2.3",
            generate_setup=True,
        )
        PackageWriterMock().write_package.assert_called_once_with(
            package=package_mock,
            templates_path=ANY,
        )
        parse_boto3_stubs_package_mock.assert_called_once_with(
            service_names=[ServiceNameCatalog.ec2],
            package_data=Boto3StubsFullPackageData,
            version="1.2.3",
        )
        assert result == package_mock
