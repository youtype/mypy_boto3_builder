import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.writers.boto3_stubs_package import (
    write_boto3_stubs_docs,
    write_boto3_stubs_package,
)


class TestBoto3StubsPackage:
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.sort_imports")
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.blackify")
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.render_jinja2_template")
    def test_write_master_package(
        self,
        render_jinja2_template_mock: MagicMock,
        blackify_mock: MagicMock,
        sort_imports_mock: MagicMock,
    ) -> None:
        package_mock = MagicMock()
        package_mock.name = "package"
        package_mock.service_name.module_name = "module"

        blackify_mock.return_value = "blackify"
        sort_imports_mock.return_value = "sort_imports"
        render_jinja2_template_mock.return_value = "render_jinja2_template_mock"

        with tempfile.TemporaryDirectory() as output_dir:
            output_path = Path(output_dir)
            write_boto3_stubs_package(package_mock, output_path, True)
            render_jinja2_template_mock.assert_called_with(
                Path("boto3-stubs/boto3-stubs/version.py.jinja2"),
                package=package_mock,
            )
            assert len(blackify_mock.mock_calls) == 6
            assert len(sort_imports_mock.mock_calls) == 6

    def test_write_boto3_stubs_docs(self) -> None:
        package_mock = MagicMock()
        package_mock.name = "package"
        package_mock.service_name.module_name = "module"

        with tempfile.TemporaryDirectory() as output_dir:
            output_path = Path(output_dir)
            write_boto3_stubs_docs(package_mock, output_path)
