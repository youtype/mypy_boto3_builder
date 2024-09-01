import logging
from typing import Any, Optional, Union

from boto3 import session as session
from boto3.session import Session as Session
from botocore.config import Config
from botocore.session import Session as BotocoreSession

__author__: str
__version__: str

DEFAULT_SESSION: Optional[Session]

def setup_default_session(
    *,
    aws_access_key_id: Optional[str] = ...,
    aws_secret_access_key: Optional[str] = ...,
    aws_session_token: Optional[str] = ...,
    region_name: Optional[str] = ...,
    botocore_session: Optional[BotocoreSession] = ...,
    profile_name: Optional[str] = ...,
) -> None: ...
def set_stream_logger(
    name: str = ..., level: int = ..., format_string: Optional[str] = ...
) -> None: ...
def _get_default_session() -> Session: ...

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> Any: ...

def client(
    service_name: str,
    region_name: Optional[str] = ...,
    api_version: Optional[str] = ...,
    use_ssl: Optional[bool] = ...,
    verify: Union[bool, str, None] = ...,
    endpoint_url: Optional[str] = ...,
    aws_access_key_id: Optional[str] = ...,
    aws_secret_access_key: Optional[str] = ...,
    aws_session_token: Optional[str] = ...,
    config: Optional[Config] = ...,
) -> Any: ...
def resource(
    service_name: str,
    region_name: Optional[str] = ...,
    api_version: Optional[str] = ...,
    use_ssl: Optional[bool] = ...,
    verify: Union[bool, str, None] = ...,
    endpoint_url: Optional[str] = ...,
    aws_access_key_id: Optional[str] = ...,
    aws_secret_access_key: Optional[str] = ...,
    aws_session_token: Optional[str] = ...,
    config: Optional[Config] = ...,
) -> Any: ...
