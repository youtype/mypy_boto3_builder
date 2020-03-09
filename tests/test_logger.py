from unittest.mock import patch, MagicMock

from mypy_boto3_builder.logger import get_logger, Logger
import pytest


class TestGetLogger:
    @patch("mypy_boto3_builder.logger.logger")
    @patch("mypy_boto3_builder.logger.logging")
    def test_get_logger(self, logging_mock: MagicMock, logger_mock: MagicMock) -> None:
        logger_mock.handlers = []
        result = get_logger(verbose=True)
        assert result == logger_mock
        logging_mock.StreamHandler.assert_called_with()
        logger_mock.set_level.assert_called_with(logging_mock.DEBUG)

        logging_mock.reset_mock()
        HandlerMock = MagicMock()
        logger_mock.handlers = [HandlerMock]
        result = get_logger()
        logging_mock.StreamHandler.assert_not_called()
        logger_mock.setLevel.assert_not_called()

        result = get_logger(verbose=True, panic=True)
        result.panic = True


class TestLogger:
    @patch("mypy_boto3_builder.logger.logging.Logger.warning")
    def test_warning(self, warning_mock: MagicMock) -> None:
        logger = Logger("name")
        assert logger.warning("test") is None
        warning_mock.assert_called_with("test")
        logger.panic = True

        with pytest.raises(RuntimeError):
            logger.warning("test")

    @patch("mypy_boto3_builder.logger.logging.Logger.setLevel")
    def test_set_level(self, set_level_mock: MagicMock) -> None:
        logger = Logger("name")
        handler_mock = MagicMock()
        logger.handlers = [handler_mock]
        assert logger.set_level(123) is None
        set_level_mock.assert_called_with(123)
        handler_mock.setLevel.assert_called_with(123)
