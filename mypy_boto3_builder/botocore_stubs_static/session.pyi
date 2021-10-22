import sys
from typing import IO, Any, Dict, Iterator, List, Optional, Tuple, Union

from botocore import UNSIGNED as UNSIGNED
from botocore import handlers as handlers
from botocore import monitoring as monitoring
from botocore import paginate as paginate
from botocore import retryhandler as retryhandler
from botocore import translate as translate
from botocore import utils as utils
from botocore import waiter as waiter
from botocore.client import BaseClient, Config
from botocore.configprovider import (
    BOTOCORE_DEFAUT_SESSION_VARIABLES as BOTOCORE_DEFAUT_SESSION_VARIABLES,
)
from botocore.configprovider import ConfigChainFactory as ConfigChainFactory
from botocore.configprovider import ConfigValueStore as ConfigValueStore
from botocore.configprovider import (
    create_botocore_default_config_mapping as create_botocore_default_config_mapping,
)
from botocore.credentials import Credentials
from botocore.errorfactory import ClientExceptionsFactory as ClientExceptionsFactory
from botocore.exceptions import ConfigNotFound as ConfigNotFound
from botocore.exceptions import PartialCredentialsError as PartialCredentialsError
from botocore.exceptions import ProfileNotFound as ProfileNotFound
from botocore.exceptions import UnknownServiceError as UnknownServiceError
from botocore.hooks import BaseEventHooks
from botocore.hooks import EventAliaser as EventAliaser
from botocore.hooks import HierarchicalEmitter as HierarchicalEmitter
from botocore.hooks import first_non_none_response as first_non_none_response
from botocore.loaders import create_loader as create_loader
from botocore.model import ServiceModel as ServiceModel
from botocore.parsers import ResponseParserFactory as ResponseParserFactory
from botocore.regions import EndpointResolver as EndpointResolver
from botocore.utils import EVENT_ALIASES as EVENT_ALIASES
from botocore.utils import validate_region_name as validate_region_name

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping  # type: ignore

if sys.version_info >= (3, 9):
    from typing import Protocol
else:
    from typing_extensions import Protocol

_EnvDict = Dict[str, Tuple[Any, Any, Any, Any]]

class _EventHandler(Protocol):
    def __call__(self, **kwargs: Any) -> None: ...

class Session:
    SESSION_VARIABLES: _EnvDict
    LOG_FORMAT: str
    user_agent_name: str
    user_agent_version: str
    user_agent_extra: str
    session_var_map: SessionVarDict
    def __init__(
        self,
        session_vars: Optional[_EnvDict] = ...,
        event_hooks: Optional[BaseEventHooks] = ...,
        include_builtin_handlers: bool = ...,
        profile: Optional[str] = ...,
    ) -> None: ...
    @property
    def available_profiles(self) -> List[str]: ...
    @property
    def profile(self) -> Optional[str]: ...
    def get_config_variable(self, logical_name: str, methods: Optional[Any] = ...) -> Any: ...
    def set_config_variable(self, logical_name: str, value: Any) -> None: ...
    def instance_variables(self) -> Dict[str, Any]: ...
    def get_scoped_config(self) -> Dict[str, Any]: ...
    @property
    def full_config(self) -> Dict[str, Any]: ...
    def get_default_client_config(self) -> Config: ...
    def set_default_client_config(self, client_config: Config) -> None: ...
    def set_credentials(
        self, access_key: str, secret_key: str, token: Optional[str] = ...
    ) -> None: ...
    def get_credentials(self) -> Credentials: ...
    def user_agent(self) -> str: ...
    def get_data(self, data_path: str) -> Any: ...
    def get_service_model(
        self, service_name: str, api_version: Optional[str] = ...
    ) -> ServiceModel: ...
    def get_waiter_model(
        self, service_name: str, api_version: Optional[str] = ...
    ) -> waiter.WaiterModel: ...
    def get_paginator_model(
        self, service_name: str, api_version: Optional[str] = ...
    ) -> paginate.PaginatorModel: ...
    def get_service_data(self, service_name: str, api_version: Optional[str] = ...) -> Any: ...
    def get_available_services(self) -> Any: ...
    def set_debug_logger(self, logger_name: str = ...) -> None: ...
    def set_stream_logger(
        self,
        logger_name: str,
        log_level: str,
        stream: Optional[IO[str]] = ...,
        format_string: Optional[str] = ...,
    ) -> None: ...
    def set_file_logger(self, log_level: str, path: str, logger_name: str = ...) -> None: ...
    def register(
        self,
        event_name: str,
        handler: _EventHandler,
        unique_id: Optional[str] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def unregister(
        self,
        event_name: str,
        handler: Optional[_EventHandler] = ...,
        unique_id: Optional[str] = ...,
        unique_id_uses_count: bool = ...,
    ) -> None: ...
    def emit(self, event_name: str, **kwargs: Any) -> Any: ...
    def emit_first_non_none_response(self, event_name: Any, **kwargs: Any) -> Any: ...
    def get_component(self, name: Any) -> Any: ...
    def register_component(self, name: Any, component: Any) -> None: ...
    def lazy_register_component(self, name: Any, component: Any) -> None: ...
    def create_client(
        self,
        service_name: str,
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: Optional[Union[bool, str]] = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[Config] = ...,
    ) -> BaseClient: ...
    def get_available_partitions(self) -> List[str]: ...
    def get_available_regions(
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> List[str]: ...

class ComponentLocator:
    def __init__(self) -> None: ...
    def get_component(self, name: str) -> Any: ...
    def register_component(self, name: str, component: Any) -> None: ...
    def lazy_register_component(self, name: str, no_arg_factory: Any) -> None: ...

class SessionVarDict(MutableMapping[str, Any]):
    def __init__(self, session: Session, session_vars: Dict[str, Any]) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...

class SubsetChainConfigFactory:
    def __init__(self, session: Session, methods: Any, environ: Optional[Any] = ...) -> None: ...
    def create_config_chain(
        self,
        instance_name: Optional[Any] = ...,
        env_var_names: Optional[Any] = ...,
        config_property_name: Optional[Any] = ...,
        default: Optional[Any] = ...,
        conversion_func: Optional[Any] = ...,
    ) -> Any: ...

def get_session(env_vars: Optional[_EnvDict] = ...) -> Session: ...
