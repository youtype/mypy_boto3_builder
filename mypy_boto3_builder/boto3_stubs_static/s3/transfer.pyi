from typing import Any, Callable, List, Mapping, Optional

from botocore.client import BaseClient
from botocore.config import Config
from s3transfer.manager import TransferConfig as S3TransferConfig
from s3transfer.manager import TransferManager
from s3transfer.subscribers import BaseSubscriber
from s3transfer.utils import OSUtils

KB: int
MB: int

def create_transfer_manager(
    client: BaseClient,
    config: Config,
    osutil: Optional[OSUtils] = ...,  # type: ignore
) -> TransferManager: ...

class TransferConfig(S3TransferConfig):
    def __init__(
        self,
        multipart_threshold: int = ...,
        max_concurrency: int = ...,
        multipart_chunksize: int = ...,
        num_download_attempts: int = ...,
        max_io_queue: int = ...,
        io_chunksize: int = ...,
        use_threads: bool = ...,
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
        osutil: Optional[OSUtils] = None,  # type: ignore
        manager: Optional[TransferManager] = None,  # type: ignore
    ) -> None: ...
    def upload_file(
        self,
        filename: str,
        bucket: str,
        key: str,
        callback: Callable[[int], Any] = ...,
        extra_args: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    def download_file(
        self,
        bucket: str,
        key: str,
        filename: str,
        extra_args: Optional[Mapping[str, Any]] = ...,
        callback: Callable[[int], Any] = ...,
    ) -> None: ...

class ProgressCallbackInvoker(BaseSubscriber):
    def __init__(self, callback: Callable[[int], Any]) -> None: ...
    def on_progress(self, bytes_transferred: int, **kwargs: Any) -> None: ...
