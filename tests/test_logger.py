from unittest.mock import MagicMock, patch

from mypy_boto3_builder.logger import get_logger


class TestLogger:
    @patch("mypy_boto3_builder.logger.logging")
    def test_get_logger(self, logging_mock: MagicMock) -> None:
        logger_mock = MagicMock()
        logging_mock.getLogger.return_value = logger_mock
        logger_mock.handlers = []
        result = get_logger(logging_mock.DEBUG)
        assert result == logger_mock
        logging_mock.StreamHandler.assert_called_with()
        logger_mock.setLevel.assert_called_with(logging_mock.DEBUG)

        logging_mock.reset_mock()
        handler_mock = MagicMock()
        logger_mock.handlers = [handler_mock]
        result = get_logger()
        logging_mock.StreamHandler.assert_not_called()
        logger_mock.setLevel.assert_not_called()
