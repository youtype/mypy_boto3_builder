import tempfile
from pathlib import Path
from unittest.mock import patch

from mypy_boto3_builder.utils.path import print_path, walk_path


class TestPath:
    def test_print_path(self) -> None:
        with patch.object(Path, "cwd") as cwd_mock:
            cwd_mock.return_value = Path("/absolute/")
            assert print_path(Path("./relative")) == "./relative"
            assert print_path(Path("/absolute/path/test")) == "path/test"
            assert print_path(Path("/absolute/path")) == "./path"
            assert print_path(Path("/absolute")) == "/absolute"
            assert print_path(Path("/")) == "/"
            assert print_path(Path(".")) == "."

    def test_walk_path(self) -> None:
        with tempfile.TemporaryDirectory() as output_dir:
            output_path = Path(output_dir)
            (output_path / "one.txt").touch()
            (output_path / "two.txt").touch()
            result = list(sorted(walk_path(output_path)))
            assert result == [output_path / "one.txt", output_path / "two.txt"]
            result = list(walk_path(output_path, [output_path / "one.txt"]))
            assert result == [output_path / "two.txt"]
