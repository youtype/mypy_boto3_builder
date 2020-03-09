from pathlib import Path
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.writers.boto3_stubs_package import write_boto3_stubs_package


class TestBoto3StubsPackage:
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.shutil")
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.filecmp")
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.BOTO3_STUBS_STATIC_PATH")
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.blackify")
    @patch("mypy_boto3_builder.writers.boto3_stubs_package.render_jinja2_template")
    def test_write_master_package(
        self,
        render_jinja2_template_mock: MagicMock,
        blackify_mock: MagicMock,
        BOTO3_STUBS_STATIC_PATH_MOCK: MagicMock,
        filecmp_mock: MagicMock,
        shutil_mock: MagicMock,
    ) -> None:
        package_mock = MagicMock()
        output_path_mock = MagicMock()
        static_path_mock = MagicMock()
        BOTO3_STUBS_STATIC_PATH_MOCK.glob.return_value = [
            static_path_mock,
        ]
        output_path_mock.__truediv__.return_value = output_path_mock
        assert (
            write_boto3_stubs_package(package_mock, output_path_mock)
            == [output_path_mock] * 7
        )
        render_jinja2_template_mock.assert_called_with(
            Path("boto3-stubs/boto3-stubs/version.py.jinja2"), package=package_mock,
        )
        blackify_mock.assert_called_with(
            render_jinja2_template_mock(), output_path_mock
        )

        filecmp_mock.cmp.return_value = False
        assert (
            write_boto3_stubs_package(package_mock, output_path_mock)
            == [output_path_mock] * 8
        )
        shutil_mock.copy.assert_called()
