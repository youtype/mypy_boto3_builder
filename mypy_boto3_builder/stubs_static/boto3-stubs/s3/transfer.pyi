import logging
from types import TracebackType
from typing import Any, Callable, Dict, List, Mapping, Optional, Type, TypeVar

from botocore.client import BaseClient
from botocore.config import Config
from s3transfer.manager import TransferConfig as S3TransferConfig
from s3transfer.manager import TransferManager
from s3transfer.subscribers import BaseSubscriber
from s3transfer.utils import OSUtils

_R = TypeVar("_R")

KB: int
MB: int

logger: logging.Logger = ...

def create_transfer_manager(
    client: BaseClient,
    config: TransferConfig,
    osutil: Optional[OSUtils] = ...,
) -> TransferManager: ...
def has_minimum_crt_version(minimum_version: str) -> bool: ...

class TransferConfig(S3TransferConfig):
    ALIAS: Dict[str, str]

    def __init__(
        self,
        multipart_threshold: int = ...,
        max_concurrency: int = ...,
        multipart_chunksize: int = ...,
        num_download_attempts: int = ...,
        max_io_queue: int = ...,
        io_chunksize: int = ...,
        use_threads: bool = ...,
        max_bandwidth: Optional[int] = ...,
        preferred_transfer_client: str = ...,
    ) -> None:
        self.use_threads: bool

    def __setattr__(self, name: str, value: int) -> None: ...

class S3Transfer:
    ALLOWED_DOWNLOAD_ARGS: List[str]
    ALLOWED_UPLOAD_ARGS: List[str]
    def __init__(
        self,
        client: Optional[BaseClient] = ...,
        config: Optional[Config] = ...,
        osutil: Optional[OSUtils] = ...,
        manager: Optional[TransferManager] = ...,
    ) -> None: ...
    def upload_file(
        self,
        filename: str,
        bucket: str,
        key: str,
        callback: Optional[Callable[[int], Any]] = ...,
        extra_args: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    def download_file(
        self,
        bucket: str,
        key: str,
        filename: str,
        extra_args: Optional[Mapping[str, Any]] = ...,
        callback: Optional[Callable[[int], Any]] = ...,
    ) -> None: ...
    def __enter__(self: _R) -> _R: ...
    def __exit__(
        self,
        exc_type: Optional[Type[Exception]],
        exc_value: Optional[Exception],
        tb: Optional[TracebackType],
    ) -> None: ...

class ProgressCallbackInvoker(BaseSubscriber):
    def __init__(self, callback: Callable[[int], Any]) -> None: ...
    # FIXME: signature incompatible with BaseSubscriber
    def on_progress(  # type: ignore [override]
        self, bytes_transferred: int, **kwargs: Any
    ) -> None: ...
