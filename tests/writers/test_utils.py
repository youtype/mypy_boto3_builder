from unittest.mock import MagicMock, patch

import pytest
from black import NothingChanged

from mypy_boto3_builder.writers.utils import (
    blackify,
    blackify_markdown,
    insert_md_toc,
    render_jinja2_template,
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
        ModeMock.assert_called_with(is_pyi=False, line_length=100, preview=True)

        file_path_mock.suffix = ".pyi"
        result = blackify("my content", file_path_mock)
        assert result == format_file_contents_mock()
        ModeMock.assert_called_with(is_pyi=True, line_length=100, preview=True)

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

    @patch("mypy_boto3_builder.writers.utils.TEMPLATES_PATH")
    @patch("mypy_boto3_builder.writers.utils.JinjaManager")
    def test_render_jinja2_template(
        self, JinjaManagerMock: MagicMock, TEMPLATES_PATH_MOCK: MagicMock
    ) -> None:
        template_path_mock = MagicMock()
        package_mock = MagicMock()
        service_name_mock = MagicMock()
        result = render_jinja2_template(template_path_mock, package_mock, service_name_mock)
        JinjaManagerMock.get_environment.assert_called_with()
        JinjaManagerMock.get_environment().get_template.assert_called()
        JinjaManagerMock.get_environment().get_template().render.assert_called_with(
            package=package_mock, service_name=service_name_mock
        )
        assert result == JinjaManagerMock.get_environment().get_template().render()

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
