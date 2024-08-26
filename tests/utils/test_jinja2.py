from pathlib import Path
from typing import Any
from unittest.mock import patch

from mypy_boto3_builder.utils.jinja2 import render_jinja2_template


class TestJinja2:
    @patch("mypy_boto3_builder.utils.jinja2.JinjaManager")
    def test_render_jinja2_template(self, JinjaManagerMock: Any) -> None:
        template_path = Path("template.jinja2")
        result = render_jinja2_template(template_path, {"key": "Value"})
        JinjaManagerMock.singleton().get_template.assert_called_once_with(template_path)
        JinjaManagerMock.singleton().get_template().render.assert_called_once_with({"key": "Value"})
        assert result == JinjaManagerMock.singleton().get_template().render()
