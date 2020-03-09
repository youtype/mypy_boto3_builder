from unittest.mock import patch, MagicMock

from mypy_boto3_builder.utils.nice_path import NicePath


class TestNicePath:
    @patch("mypy_boto3_builder.utils.nice_path.Path")
    def test_init(self, PathMock: MagicMock) -> None:
        path_mock = MagicMock()
        path_mock.as_posix.return_value = "absolute"
        path_mock.relative_to().as_posix.return_value = "relative"
        assert NicePath(path_mock).path == path_mock
        assert str(NicePath(path_mock)) == "relative"
        path_mock.relative_to.assert_called_with(PathMock.cwd())

        path_mock.relative_to.side_effect = ValueError()
        assert str(NicePath(path_mock)) == "absolute"
