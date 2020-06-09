from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.writers.master_package import write_master_package


class TestMasterPackage:
    @patch("mypy_boto3_builder.writers.master_package.blackify")
    @patch("mypy_boto3_builder.writers.master_package.render_jinja2_template")
    def test_write_master_package(
        self, render_jinja2_template_mock: MagicMock, blackify_mock: MagicMock
    ) -> None:
        package_mock = MagicMock()
        output_path_mock = MagicMock()
        output_path_mock.__truediv__.return_value = output_path_mock
        assert (
            write_master_package(package_mock, output_path_mock)
            == [output_path_mock] * 14
        )
        render_jinja2_template_mock.assert_called_with(
            Path("master/master/submodules.py.jinja2"), package=package_mock,
        )
        blackify_mock.assert_called_with(
            render_jinja2_template_mock(), output_path_mock
        )
