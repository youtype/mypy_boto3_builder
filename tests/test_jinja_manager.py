from pathlib import Path

import pytest

from mypy_boto3_builder.jinja_manager import JinjaManager, JinjaManagerError


class TestJinjaManager:
    def test_init(self):
        JinjaManager()

    def test_get_template(self):
        manager = JinjaManager()
        assert manager.get_template(Path("common/named_union.py.jinja2"))
        assert manager.get_template(Path("common/named_union.py.jinja2"))
        with pytest.raises(JinjaManagerError):
            manager.get_template(Path("common/unknown.jinja2"))
