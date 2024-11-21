from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture


@pytest.fixture(autouse=True)
def botocore_session_mock(mocker: MockerFixture) -> MagicMock:
    mock = MagicMock()
    mocker.patch("mypy_boto3_builder.utils.boto3_utils.get_session", mock)
    return mock
