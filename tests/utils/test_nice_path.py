from pathlib import Path
from unittest.mock import patch

from mypy_boto3_builder.utils.nice_path import NicePath


class TestNicePath:
    def test_init(self) -> None:
        with patch.object(Path, "cwd") as cwd_mock:
            cwd_mock.return_value = Path("/absolute/")
            assert str(NicePath("./relative")) == "./relative"
            assert str(NicePath("/absolute/path/test")) == "path/test"
            assert str(NicePath("/absolute/path")) == "./path"
            assert str(NicePath("/absolute")) == "/absolute"
            assert str(NicePath("/")) == "/"
            assert str(NicePath(".")) == "."
