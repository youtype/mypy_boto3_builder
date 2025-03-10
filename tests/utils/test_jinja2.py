from pathlib import Path
from unittest.mock import MagicMock, patch

from mypy_boto3_builder.utils.jinja2 import render_jinja2_template


class TestJinja2:
    @patch("mypy_boto3_builder.utils.jinja2.JinjaManager")
    def test_render_jinja2_template(self, JinjaManagerMock: MagicMock) -> None:
        template_path = Path("template.jinja2")
        result = render_jinja2_template(template_path, {"key": "Value"})
        JinjaManagerMock().get_template.assert_called_once_with(template_path)
        JinjaManagerMock().get_template().render.assert_called_once_with({"key": "Value"})
        assert result == JinjaManagerMock().get_template().render()
