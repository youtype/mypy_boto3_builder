import logging
from typing import Any, Optional, Type, TypeVar

from aiobotocore.client import AioBaseClient
from aiobotocore.config import AioConfig as AioConfig
from aiobotocore.session import AioSession
from aiobotocore.utils import AioContainerMetadataFetcher as AioContainerMetadataFetcher
from aiobotocore.utils import AioInstanceMetadataFetcher as AioInstanceMetadataFetcher
from botocore.credentials import (
    AssumeRoleCredentialFetcher,
    AssumeRoleProvider,
    AssumeRoleWithWebIdentityProvider,
    BaseAssumeRoleCredentialFetcher,
    BotoProvider,
    CachedCredentialFetcher,
    CanonicalNameCredentialSourcer,
    ConfigProvider,
    ContainerProvider,
    CredentialResolver,
    Credentials,
    EnvProvider,
    InstanceMetadataProvider,
    OriginalEC2Provider,
    ProcessProvider,
    ProfileProviderBuilder,
    RefreshableCredentials,
    SharedCredentialProvider,
    SSOProvider,
)

logger: logging.Logger

def create_credential_resolver(
    session: AioSession,  # type: ignore
    cache: Optional[Any] = ...,
    region_name: Optional[str] = ...,
) -> AioCredentialResolver: ...

class AioProfileProviderBuilder(ProfileProviderBuilder): ...

async def get_credentials(
    session: AioSession,  # type: ignore
) -> AioCredentials: ...
def create_assume_role_refresher(
    client: AioBaseClient,  # type: ignore
    params: Any,
) -> Any: ...
def create_aio_mfa_serial_refresher(actual_refresh: Any) -> Any: ...

_R = TypeVar("_R")

class AioCredentials(Credentials):
    async def get_frozen_credentials(self) -> AioRefreshableCredentials: ...  # type: ignore
    @classmethod
    def from_credentials(cls: Type[_R], obj: Optional[Credentials]) -> _R: ...

_AioRefreshableCredentials = TypeVar(
    "_AioRefreshableCredentials", bound="AioRefreshableCredentials"
)

class AioRefreshableCredentials(RefreshableCredentials):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def from_refreshable_credentials(
        cls: Type[_R], obj: Optional[RefreshableCredentials]
    ) -> _R: ...
    @property  # type: ignore
    def access_key(self) -> str: ...  # type: ignore
    @access_key.setter
    def access_key(self, value: str) -> None: ...
    @property  # type: ignore
    def secret_key(self) -> str: ...  # type: ignore
    @secret_key.setter
    def secret_key(self, value: str) -> None: ...
    @property  # type: ignore
    def token(self) -> str: ...  # type: ignore
    @token.setter
    def token(self, value: str) -> None: ...
    async def get_frozen_credentials(self) -> RefreshableCredentials: ...  # type: ignore

class AioDeferredRefreshableCredentials(AioRefreshableCredentials):
    method: Any
    def __init__(self, refresh_using: Any, method: Any, time_fetcher: Any = ...) -> None: ...
    def refresh_needed(self, refresh_in: Optional[Any] = ...) -> bool: ...

class AioCachedCredentialFetcher(CachedCredentialFetcher):
    async def fetch_credentials(self) -> Any: ...

class AioBaseAssumeRoleCredentialFetcher(
    BaseAssumeRoleCredentialFetcher, AioCachedCredentialFetcher
): ...
class AioAssumeRoleCredentialFetcher(
    AssumeRoleCredentialFetcher, AioBaseAssumeRoleCredentialFetcher
): ...

class AioAssumeRoleWithWebIdentityCredentialFetcher(AioBaseAssumeRoleCredentialFetcher):
    def __init__(
        self,
        client_creator: Any,
        web_identity_token_loader: Any,
        role_arn: str,
        extra_args: Optional[Any] = ...,
        cache: Optional[Any] = ...,
        expiry_window_seconds: Optional[Any] = ...,
    ) -> None: ...

class AioProcessProvider(ProcessProvider):
    def __init__(self, *args: Any, popen: Any = ..., **kwargs: Any) -> None: ...
    async def load(self) -> AioCredentials: ...

class AioInstanceMetadataProvider(InstanceMetadataProvider):
    async def load(self) -> AioRefreshableCredentials: ...

class AioEnvProvider(EnvProvider):
    async def load(self) -> Any: ...

class AioOriginalEC2Provider(OriginalEC2Provider):
    async def load(self) -> AioCredentials: ...

class AioSharedCredentialProvider(SharedCredentialProvider):
    async def load(self) -> AioCredentials: ...

class AioConfigProvider(ConfigProvider):
    async def load(self) -> AioCredentials: ...

class AioBotoProvider(BotoProvider):
    async def load(self) -> AioCredentials: ...  # type: ignore

class AioAssumeRoleProvider(AssumeRoleProvider):
    async def load(self) -> AioDeferredRefreshableCredentials: ...  # type: ignore

class AioAssumeRoleWithWebIdentityProvider(AssumeRoleWithWebIdentityProvider):
    async def load(self) -> AioDeferredRefreshableCredentials: ...  # type: ignore

class AioCanonicalNameCredentialSourcer(CanonicalNameCredentialSourcer):
    async def source_credentials(self, source_name: str) -> Any: ...  # type: ignore

class AioContainerProvider(ContainerProvider):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def load(self) -> AioRefreshableCredentials: ...  # type: ignore

class AioCredentialResolver(CredentialResolver):
    async def load_credentials(self) -> Any: ...  # type: ignore

class AioSSOCredentialFetcher(AioCachedCredentialFetcher):
    def __init__(
        self,
        start_url: str,
        sso_region: str,
        role_name: str,
        account_id: str,
        client_creator: Any,
        token_loader: Optional[Any] = ...,
        cache: Optional[Any] = ...,
        expiry_window_seconds: Optional[Any] = ...,
    ) -> None: ...

class AioSSOProvider(SSOProvider):
    async def load(self) -> AioDeferredRefreshableCredentials: ...  # type: ignore
