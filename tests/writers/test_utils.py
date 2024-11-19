from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.writers.utils import (
    format_md,
    insert_md_toc,
    render_jinja2_package_template,
)


class TestUtils:
    @patch("mypy_boto3_builder.writers.utils.render_jinja2_template")
    def test_render_jinja2_package_template(self, render_jinja2_template_mock: MagicMock) -> None:
        template_path = Path("template.jinja2")
        package = Package(Boto3StubsPackageData, [ServiceNameCatalog.ec2, ServiceNameCatalog.s3])
        result = render_jinja2_package_template(template_path, package)
        render_jinja2_template_mock.assert_called_once_with(
            template_path,
            {"package": package, "service_name": None},
        )
        assert result == render_jinja2_template_mock()
        render_jinja2_template_mock.reset_mock()

        package = Package(Boto3StubsPackageData, [ServiceNameCatalog.s3])
        result = render_jinja2_package_template(template_path, package)
        render_jinja2_template_mock.assert_called_once_with(
            template_path,
            {"package": package, "service_name": ServiceNameCatalog.s3},
        )
        render_jinja2_template_mock.reset_mock()

        package = Package(Boto3StubsPackageData, [])
        result = render_jinja2_package_template(template_path, package)
        render_jinja2_template_mock.assert_called_once_with(
            template_path,
            {"package": package, "service_name": None},
        )

    def test_insert_md_toc(self) -> None:
        assert (
            insert_md_toc("# a\ntest\n## b\n## c\ntest2")
            == "# a\ntest\n- [a](#a)\n  - [b](#b)\n  - [c](#c)\n\n## b\n## c\ntest2"
        )
        assert insert_md_toc("# a\n") == "# a\n- [a](#a)\n"

    def test_format_md(self) -> None:
        assert format_md(" # a") == "# a\n"
