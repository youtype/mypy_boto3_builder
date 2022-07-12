import sys
from typing import Dict, Optional, Tuple, TypeVar, Union

from botocore.compat import OrderedDict as OrderedDict
from botocore.endpoint import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from botocore.endpoint import MAX_POOL_CONNECTIONS as MAX_POOL_CONNECTIONS
from botocore.exceptions import InvalidMaxRetryAttemptsError as InvalidMaxRetryAttemptsError
from botocore.exceptions import InvalidRetryConfigurationError as InvalidRetryConfigurationError
from botocore.exceptions import InvalidRetryModeError as InvalidRetryModeError
from botocore.exceptions import InvalidS3AddressingStyleError as InvalidS3AddressingStyleError

if sys.version_info >= (3, 9):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict

class _RetryDict(TypedDict, total=False):
    total_max_attempts: int
    max_attempts: int
    mode: Literal["legacy", "standard", "adaptive"]

class _S3Dict(TypedDict, total=False):
    use_accelerate_endpoint: bool
    payload_signing_enabled: bool
    addressing_style: Literal["auto", "virtual", "path"]
    us_east_1_regional_endpoint: Literal["regional", "legacy"]

class _ProxiesConfigDict(TypedDict, total=False):
    proxy_ca_bundle: str
    proxy_client_cert: Union[str, Tuple[str, str]]
    proxy_use_forwarding_for_https: bool

_Config = TypeVar("_Config", bound="Config")

class Config:
    OPTION_DEFAULTS: OrderedDict[str, None]
    NON_LEGACY_OPTION_DEFAULTS: Dict[str, None]
    def __init__(
        self,
        region_name: Optional[str] = ...,
        signature_version: Optional[str] = ...,
        user_agent: Optional[str] = ...,
        user_agent_extra: Optional[str] = ...,
        connect_timeout: Optional[Union[float, int]] = ...,
        read_timeout: Optional[Union[float, int]] = ...,
        parameter_validation: Optional[bool] = ...,
        max_pool_connections: Optional[int] = ...,
        proxies: Optional[Dict[str, str]] = ...,
        proxies_config: Optional[_ProxiesConfigDict] = ...,
        s3: Optional[_S3Dict] = ...,
        retries: Optional[_RetryDict] = ...,
        client_cert: Optional[Union[str, Tuple[str, str]]] = ...,
        inject_host_prefix: Optional[bool] = ...,
    ) -> None: ...
    def merge(self: _Config, other_config: _Config) -> _Config: ...
