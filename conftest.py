"""
Common pytest fixtures.

Copyright 2025 Vlad Emelianov
"""

from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

BOTOCORE_SESSION = MagicMock()


@pytest.fixture(autouse=True)
def botocore_session_mock(mocker: MockerFixture) -> MagicMock:
    """
    Mock boto3 session to avoid real AWS calls."""
    mocker.patch("mypy_boto3_builder.utils.boto3_utils.get_session", return_value=BOTOCORE_SESSION)
    return BOTOCORE_SESSION


@pytest.fixture(autouse=True)
def import_version_mock(mocker: MockerFixture) -> MagicMock:
    """
    Mock _import_version to always return 1.2.3.
    """
    return mocker.patch(
        "mypy_boto3_builder.utils.version_getters._import_version",
        return_value="1.2.3",
    )
