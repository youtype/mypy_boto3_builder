import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.writers.service_package import write_service_docs, write_service_package


class TestServicePackage:
    @patch("mypy_boto3_builder.writers.service_package.sort_imports")
    @patch("mypy_boto3_builder.writers.service_package.blackify")
    @patch("mypy_boto3_builder.writers.service_package.render_jinja2_template")
    def test_write_service_package(
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
            write_service_package(package_mock, output_path, True)
            render_jinja2_template_mock.assert_called_with(
                Path("service/service/type_defs.pyi.jinja2"),
                package=package_mock,
                service_name=package_mock.service_name,
            )
            assert len(blackify_mock.mock_calls) == 17
            assert len(sort_imports_mock.mock_calls) == 17

    def test_write_service_docs(self) -> None:
        package_mock = MagicMock()
        package_mock.name = "package"
        package_mock.service_name.module_name = "module"

        with tempfile.TemporaryDirectory() as output_dir:
            output_path = Path(output_dir)
            write_service_docs(package_mock, output_path)
