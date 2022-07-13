import logging
from queue import Queue
from typing import IO, Any, Callable, Dict, Iterator, List, Mapping, Optional, Type, TypeVar

from botocore.client import BaseClient
from s3transfer.exceptions import RetriesExceededError as RetriesExceededError
from s3transfer.exceptions import S3UploadFailedError as S3UploadFailedError

_R = TypeVar("_R")

class NullHandler(logging.Handler):
    def emit(self, record) -> None: ...

logger: logging.Logger
MB: int
SHUTDOWN_SENTINEL: Any

def random_file_extension(num_digits: int = ...) -> str: ...
def disable_upload_callbacks(request: Any, operation_name: str, **kwargs: Any) -> None: ...
def enable_upload_callbacks(request: Any, operation_name: str, **kwargs: Any) -> None: ...

class QueueShutdownError(Exception): ...

class ReadFileChunk:
    def __init__(
        self,
        fileobj: IO[Any],
        start_byte: int,
        chunk_size: int,
        full_file_size: int,
        callback: Optional[Callable[..., Any]] = ...,
        enable_callback: bool = ...,
    ) -> None: ...
    @classmethod
    def from_filename(
        cls: Type[_R],
        filename: str,
        start_byte: int,
        chunk_size: int,
        callback: Optional[Callable[..., Any]] = ...,
        enable_callback: bool = ...,
    ) -> _R: ...
    def read(self, amount: Optional[int] = ...) -> str: ...
    def enable_callback(self) -> None: ...
    def disable_callback(self) -> None: ...
    def seek(self, where: int) -> None: ...
    def close(self) -> None: ...
    def tell(self) -> int: ...
    def __len__(self) -> int: ...
    def __enter__(self: _R) -> _R: ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Iterator[str]: ...

class StreamReaderProgress:
    def __init__(self, stream: Any, callback: Optional[Callable[..., Any]] = ...) -> None: ...
    def read(self, *args: Any, **kwargs: Any) -> str: ...

class OSUtils:
    def get_file_size(self, filename: str) -> int: ...
    def open_file_chunk_reader(
        self, filename: str, start_byte: int, size: int, callback: Callable[..., Any]
    ) -> IO[Any]: ...
    def open(self, filename: str, mode: str) -> IO[Any]: ...
    def remove_file(self, filename: str) -> None: ...
    def rename_file(self, current_filename: str, new_filename: str) -> None: ...

class MultipartUploader:
    UPLOAD_PART_ARGS: List[str]
    def __init__(
        self, client: BaseClient, config: TransferConfig, osutil: OSUtils, executor_cls: Any = ...
    ) -> None: ...
    def upload_file(
        self,
        filename: str,
        bucket: str,
        key: str,
        callback: Callable[..., Any],
        extra_args: Mapping[str, Any],
    ) -> None: ...

class ShutdownQueue(Queue[Any]):
    def trigger_shutdown(self) -> None: ...
    # FIXME: Signature of "put" incompatible with supertype "Queue
    def put(self, item: Any) -> None: ...  # type: ignore

class MultipartDownloader:
    def __init__(
        self, client: BaseClient, config: TransferConfig, osutil: OSUtils, executor_cls: Any = ...
    ) -> None: ...
    def download_file(
        self,
        bucket: str,
        key: str,
        filename: str,
        object_size: int,
        extra_args: Dict[str, Any],
        callback: Optional[Callable[..., Any]] = ...,
    ) -> None: ...

class TransferConfig:
    multipart_threshold: int
    max_concurrency: int
    multipart_chunksize: int
    num_download_attempts: int
    max_io_queue: int
    def __init__(
        self,
        multipart_threshold: int = ...,
        max_concurrency: int = ...,
        multipart_chunksize: int = ...,
        num_download_attempts: int = ...,
        max_io_queue: int = ...,
    ) -> None: ...

class S3Transfer:
    ALLOWED_DOWNLOAD_ARGS: List[str]
    ALLOWED_UPLOAD_ARGS: List[str]
    def __init__(
        self,
        client: BaseClient,
        config: Optional[TransferConfig] = ...,
        osutil: Optional[OSUtils] = ...,
    ) -> None: ...
    def upload_file(
        self,
        filename: str,
        bucket: str,
        key: str,
        callback: Optional[Callable[..., Any]] = ...,
        extra_args: Optional[Dict[str, Any]] = ...,
    ) -> None: ...
    def download_file(
        self,
        bucket: str,
        key: str,
        filename: str,
        extra_args: Optional[Dict[str, Any]] = ...,
        callback: Optional[Callable[..., Any]] = ...,
    ) -> None: ...
