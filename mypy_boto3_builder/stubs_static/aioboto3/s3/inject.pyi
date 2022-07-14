import logging
from typing import IO, Any, BinaryIO, Callable, Dict, List, Optional, Sequence

from boto3.s3.transfer import TransferConfig as S3TransferConfig

logger: logging.Logger

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
    Callback: Optional[Callable[[int], None]] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def download_fileobj(
    self: Any,
    Bucket: str,
    Key: str,
    Fileobj: IO[Any],
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[Callable[[int], None]] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def upload_fileobj(
    self: Any,
    Fileobj: BinaryIO,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[Callable[[int], None]] = ...,
    Config: Optional[S3TransferConfig] = ...,
    Processing: Optional[Callable[[bytes], bytes]] = ...,
) -> Any: ...
async def upload_file(
    self: Any,
    Filename: str,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[Callable[[int], None]] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def copy(
    self: Any,
    CopySource: Any,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = ...,
    Callback: Optional[Callable[[int], None]] = ...,
    SourceClient: Optional[Any] = ...,
    Config: Optional[S3TransferConfig] = ...,
) -> None: ...
async def bucket_load(self: Any, *args: Any, **kwargs: Any) -> None: ...
