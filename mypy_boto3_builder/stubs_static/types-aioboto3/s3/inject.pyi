import logging
from abc import abstractmethod
from typing import Any, BinaryIO, Callable, Dict, List, Optional, Sequence, Union

from boto3.s3.transfer import TransferConfig as S3TransferConfig

logger: logging.Logger
TransferCallback = Callable[[int], None]

class _AsyncBinaryIO:
    @abstractmethod
    async def seek(self, offset: int, whence: int = 0) -> int:
        pass

    @abstractmethod
    async def write(self, s: Union[bytes, bytearray]) -> int:
        pass

AnyFileObject = Union[_AsyncBinaryIO, BinaryIO]

def inject_s3_transfer_methods(class_attributes: Sequence[Any], **kwargs: Any) -> None: ...
def inject_object_summary_methods(class_attributes: Sequence[Any], **kwargs: Any) -> None: ...
def inject_bucket_methods(class_attributes: Sequence[Any], **kwargs: Any) -> None: ...
async def object_summary_load(self: Any, *args: Any, **kwargs: Any) -> None: ...
async def download_file(
    self: Any,
    Bucket: str,
    Key: str,
    Filename: str,
    ExtraArgs: Optional[List[str]] = ...,
    Callback: Optional[TransferCallback] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def download_fileobj(
    self: Any,
    Bucket: str,
    Key: str,
    Fileobj: AnyFileObject,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[TransferCallback] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def upload_fileobj(
    self: Any,
    Fileobj: AnyFileObject,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[TransferCallback] = ...,
    Config: Optional[S3TransferConfig] = ...,
    Processing: Optional[Callable[[bytes], bytes]] = ...,
) -> Any: ...
async def upload_file(
    self: Any,
    Filename: str,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[TransferCallback] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def copy(
    self: Any,
    CopySource: Any,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[TransferCallback] = ...,
    SourceClient: Optional[Any] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def bucket_load(self: Any, *args: Any, **kwargs: Any) -> None: ...
