import logging
from io import BytesIO
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Iterator,
    Mapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

# FIXME: awscrt is untyped
from awscrt.auth import AwsCredentials  # type: ignore
from awscrt.http import HttpRequest  # type: ignore
from awscrt.s3 import S3Client, S3Request  # type: ignore
from botocore.credentials import CredentialProvider
from botocore.session import Session
from s3transfer.constants import GB as GB
from s3transfer.constants import MB as MB
from s3transfer.exceptions import TransferNotDoneError as TransferNotDoneError
from s3transfer.futures import BaseTransferFuture as BaseTransferFuture
from s3transfer.futures import BaseTransferMeta as BaseTransferMeta
from s3transfer.subscribers import BaseSubscriber
from s3transfer.utils import CallArgs as CallArgs
from s3transfer.utils import OSUtils as OSUtils
from s3transfer.utils import get_callbacks as get_callbacks

_R = TypeVar("_R")

logger: logging.Logger

class CRTCredentialProviderAdapter:
    def __init__(self, botocore_credential_provider: CredentialProvider) -> None: ...
    def __call__(self) -> AwsCredentials: ...

def create_s3_crt_client(
    region: str,
    botocore_credential_provider: Optional[CredentialProvider] = ...,
    num_threads: Optional[int] = ...,
    target_throughput: float = ...,
    part_size: int = ...,
    use_ssl: bool = ...,
    verify: Optional[Union[bool, str]] = ...,
) -> S3Client: ...

class CRTTransferManager:
    def __init__(
        self,
        crt_s3_client: S3Client,
        crt_request_serializer: BaseCRTRequestSerializer,
        osutil: Optional[OSUtils] = ...,
    ) -> None: ...
    def __enter__(self: _R) -> _R: ...
    def __exit__(self, exc_type: Type[BaseException], exc_value: Any, *args: Any) -> None: ...
    def download(
        self,
        bucket: str,
        key: str,
        fileobj: IO[Any],
        extra_args: Optional[Mapping[str, Any]] = ...,
        subscribers: Optional[Sequence[BaseSubscriber]] = ...,
    ) -> CRTTransferFuture: ...
    def upload(
        self,
        fileobj: IO[Any],
        bucket: str,
        key: str,
        extra_args: Optional[Mapping[str, Any]] = ...,
        subscribers: Optional[Sequence[BaseSubscriber]] = ...,
    ) -> CRTTransferFuture: ...
    def delete(
        self,
        bucket: str,
        key: str,
        extra_args: Optional[Mapping[str, Any]] = ...,
        subscribers: Optional[Sequence[BaseSubscriber]] = ...,
    ) -> CRTTransferFuture: ...
    def shutdown(self, cancel: bool = ...) -> None: ...

class CRTTransferMeta(BaseTransferMeta):
    def __init__(
        self, transfer_id: Optional[str] = ..., call_args: Optional[Mapping[str, Any]] = ...
    ) -> None: ...
    @property
    def call_args(self) -> Dict[str, Any]: ...
    @property
    def transfer_id(self) -> str: ...
    @property
    def user_context(self) -> Dict[str, Any]: ...

class CRTTransferFuture(BaseTransferFuture):
    def __init__(
        self,
        meta: Optional[CRTTransferMeta] = ...,
        coordinator: Optional[CRTTransferCoordinator] = ...,
    ) -> None: ...
    @property
    def meta(self) -> CRTTransferMeta: ...
    def done(self) -> bool: ...
    # FIXME: Signature of "result" incompatible with supertype "BaseTransferFuture"
    def result(self, timeout: Optional[float] = ...) -> None: ...  # type: ignore
    def cancel(self) -> None: ...
    def set_exception(self, exception: BaseException) -> None: ...

class BaseCRTRequestSerializer:
    def serialize_http_request(self, transfer_type: str, future: CRTTransferFuture) -> None: ...

class BotocoreCRTRequestSerializer(BaseCRTRequestSerializer):
    def __init__(
        self, session: Session, client_kwargs: Optional[Mapping[str, Any]] = ...
    ) -> None: ...
    def serialize_http_request(
        self, transfer_type: str, future: CRTTransferFuture
    ) -> HttpRequest: ...

class FakeRawResponse(BytesIO):
    def stream(self, amt: int = ..., decode_content: Optional[bool] = ...) -> Iterator[bytes]: ...

class CRTTransferCoordinator:
    def __init__(
        self, transfer_id: Optional[str] = ..., s3_request: Optional[S3Request] = ...
    ) -> None:
        self.transfer_id: str
    @property
    def s3_request(self) -> S3Request: ...
    def set_done_callbacks_complete(self) -> None: ...
    def wait_until_on_done_callbacks_complete(self, timeout: Optional[float] = ...) -> None: ...
    def set_exception(self, exception: BaseException, override: bool = ...) -> None: ...
    def cancel(self) -> None: ...
    def result(self, timeout: Optional[float] = ...) -> None: ...
    def done(self) -> bool: ...
    def set_s3_request(self, s3_request: S3Request) -> None: ...

class S3ClientArgsCreator:
    def __init__(
        self, crt_request_serializer: BaseCRTRequestSerializer, os_utils: OSUtils
    ) -> None: ...
    def get_make_request_args(
        self,
        request_type: str,
        call_args: Mapping[str, Any],
        coordinator: CRTTransferCoordinator,
        future: CRTTransferFuture,
        on_done_after_calls: Sequence[Callable[..., Any]],
    ) -> Dict[str, Any]: ...
    def get_crt_callback(
        self,
        future: CRTTransferFuture,
        callback_type: str,
        before_subscribers: Optional[Sequence[BaseSubscriber]] = ...,
        after_subscribers: Optional[Sequence[BaseSubscriber]] = ...,
    ) -> Callable[..., Any]: ...

class RenameTempFileHandler:
    def __init__(
        self,
        coordinator: CRTTransferCoordinator,
        final_filename: str,
        temp_filename: str,
        osutil: OSUtils,
    ) -> None: ...
    def __call__(self, **kwargs: Any) -> None: ...

class AfterDoneHandler:
    def __init__(self, coordinator: CRTTransferCoordinator) -> None: ...
    def __call__(self, **kwargs: Any) -> None: ...
