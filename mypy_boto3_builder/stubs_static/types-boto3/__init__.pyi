"""
Type annotations for boto3 module.

Copyright 2024 Vlad Emelianov
"""

import logging

from boto3 import session as session
from boto3.resources.base import ServiceResource
from boto3.session import Session as Session
from botocore.client import BaseClient
from botocore.config import Config
from botocore.session import Session as BotocoreSession

__author__: str = ...
__version__: str = ...

DEFAULT_SESSION: Session | None = ...

def setup_default_session(
    *,
    aws_access_key_id: str | None = ...,
    aws_secret_access_key: str | None = ...,
    aws_session_token: str | None = ...,
    region_name: str | None = ...,
    botocore_session: BotocoreSession | None = ...,
    profile_name: str | None = ...,
) -> None: ...
def set_stream_logger(
    name: str = ...,
    level: int = ...,
    format_string: str | None = ...,
) -> None: ...
def _get_default_session() -> Session: ...

class NullHandler(logging.Handler): ...

def client(
    service_name: str,
    region_name: str | None = ...,
    api_version: str | None = ...,
    use_ssl: bool | None = ...,
    verify: bool | str | None = ...,
    endpoint_url: str | None = ...,
    aws_access_key_id: str | None = ...,
    aws_secret_access_key: str | None = ...,
    aws_session_token: str | None = ...,
    config: Config | None = ...,
) -> BaseClient: ...
def resource(
    service_name: str,
    region_name: str | None = ...,
    api_version: str | None = ...,
    use_ssl: bool | None = ...,
    verify: bool | str | None = ...,
    endpoint_url: str | None = ...,
    aws_access_key_id: str | None = ...,
    aws_secret_access_key: str | None = ...,
    aws_session_token: str | None = ...,
    config: Config | None = ...,
) -> ServiceResource: ...
