import unittest
from unittest.mock import patch, MagicMock

from mypy_boto3_builder.utils.nice_path import NicePath


class NicePathTestCase(unittest.TestCase):
    @patch("mypy_boto3_builder.utils.nice_path.Path")
    def test_init(self, PathMock: MagicMock) -> None:
        path_mock = MagicMock()
        path_mock.as_posix.return_value = "absolute"
        path_mock.relative_to().as_posix.return_value = "relative"
        self.assertEqual(NicePath(path_mock).path, path_mock)
        self.assertEqual(str(NicePath(path_mock)), "relative")
        path_mock.relative_to.assert_called_with(PathMock.cwd())

        path_mock.relative_to.side_effect = ValueError()
        self.assertEqual(str(NicePath(path_mock)), "absolute")
