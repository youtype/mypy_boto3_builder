from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from black.mode import TargetVersion
from black.report import NothingChanged

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.writers.utils import (
    blackify,
    blackify_markdown,
    insert_md_toc,
    render_jinja2_package_template,
    sort_imports,
)


class TestUtils:
    @patch("mypy_boto3_builder.writers.utils.format_file_contents")
    @patch("mypy_boto3_builder.writers.utils.Mode")
    def test_blackify(self, ModeMock: MagicMock, format_file_contents_mock: MagicMock):
        file_path_mock = MagicMock()
        file_path_mock.suffix = ".txt"
        result = blackify("my content", file_path_mock)
        assert result == "my content"

        file_path_mock.suffix = ".py"
        result = blackify("my content", file_path_mock)
        assert result == format_file_contents_mock()
        target_versions = {
            TargetVersion.PY38,
            TargetVersion.PY39,
            TargetVersion.PY310,
            TargetVersion.PY311,
            TargetVersion.PY312,
        }
        ModeMock.assert_called_with(
            target_versions=target_versions, is_pyi=False, line_length=100, preview=True
        )

        file_path_mock.suffix = ".pyi"
        result = blackify("my content", file_path_mock)
        assert result == format_file_contents_mock()
        ModeMock.assert_called_with(
            target_versions=target_versions, is_pyi=True, line_length=100, preview=True
        )

        format_file_contents_mock.side_effect = IndentationError()
        with pytest.raises(ValueError):
            blackify("my content", file_path_mock)

        format_file_contents_mock.side_effect = NothingChanged()
        assert blackify("my content", file_path_mock) == "my content"

    @patch("mypy_boto3_builder.writers.utils.sort_code_string")
    def test_sort_imports(self, sort_code_string_mock: MagicMock):
        sort_code_string_mock.return_value = "output"
        assert sort_imports("test", "mymodule") == "output"
        sort_code_string_mock.assert_called()
        assert sort_imports("test", "boto3") == "output"

    @patch("mypy_boto3_builder.writers.utils.render_jinja2_template")
    def test_render_jinja2_package_template(self, render_jinja2_template_mock: MagicMock) -> None:
        template_path = Path("template.jinja2")
        package = Package(Boto3StubsPackageData, [ServiceNameCatalog.ec2, ServiceNameCatalog.s3])
        result = render_jinja2_package_template(template_path, package)
        render_jinja2_template_mock.assert_called_once_with(
            template_path, package=package, service_name=None
        )
        assert result == render_jinja2_template_mock()
        render_jinja2_template_mock.reset_mock()

        package = Package(Boto3StubsPackageData, [ServiceNameCatalog.s3])
        result = render_jinja2_package_template(template_path, package)
        render_jinja2_template_mock.assert_called_once_with(
            template_path, package=package, service_name=ServiceNameCatalog.s3
        )
        render_jinja2_template_mock.reset_mock()

        package = Package(Boto3StubsPackageData, [])
        result = render_jinja2_package_template(template_path, package)
        render_jinja2_template_mock.assert_called_once_with(
            template_path, package=package, service_name=None
        )

    def test_insert_md_toc(self) -> None:
        assert (
            insert_md_toc("# a\ntest\n## b\n## c\ntest2")
            == "# a\ntest\n- [a](#a)\n  - [b](#b)\n  - [c](#c)\n\n## b\n## c\ntest2"
        )
        assert insert_md_toc("# a\n") == "# a\n- [a](#a)\n"

    def test_blackify_markdown(self) -> None:
        assert blackify_markdown("") == ""
        assert blackify_markdown("# a\ntest\n## b\n## c\ntest2") == "# a\ntest\n## b\n## c\ntest2"
        assert blackify_markdown("# a\n```python\na=5\n```") == "# a\n```python\na = 5\n```"
        assert blackify_markdown("# a\n```bash\na=5\n```") == "# a\n```bash\na=5\n```"
