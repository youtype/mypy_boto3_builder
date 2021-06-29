from typing import Dict, Tuple, TypeVar, Union

from botocore.compat import OrderedDict as OrderedDict
from botocore.endpoint import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from botocore.endpoint import MAX_POOL_CONNECTIONS as MAX_POOL_CONNECTIONS
from botocore.exceptions import InvalidMaxRetryAttemptsError as InvalidMaxRetryAttemptsError
from botocore.exceptions import InvalidRetryConfigurationError as InvalidRetryConfigurationError
from botocore.exceptions import InvalidRetryModeError as InvalidRetryModeError
from botocore.exceptions import InvalidS3AddressingStyleError as InvalidS3AddressingStyleError
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

_Config = TypeVar("_Config", bound="Config")

class Config:
    OPTION_DEFAULTS: OrderedDict[str, None]
    def __init__(
        self,
        region_name: str = ...,
        signature_version: str = ...,
        user_agent: str = ...,
        user_agent_extra: str = ...,
        connect_timeout: Union[float, int] = ...,
        read_timeout: Union[float, int] = ...,
        parameter_validation: bool = ...,
        max_pool_connections: int = ...,
        proxies: Dict[str, str] = ...,
        s3: _S3Dict = ...,
        retries: _RetryDict = ...,
        client_cert: Union[str, Tuple[str, str]] = ...,
        inject_host_prefix: bool = ...,
    ) -> None: ...
    def merge(self: _Config, other_config: _Config) -> _Config: ...
