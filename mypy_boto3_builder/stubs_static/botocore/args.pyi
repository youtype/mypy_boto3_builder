import sys
from typing import Any, Dict, List, Optional, Union

from botocore.config import Config as Config
from botocore.configprovider import ConfigValueStore
from botocore.endpoint import Endpoint
from botocore.endpoint import EndpointCreator as EndpointCreator
from botocore.hooks import BaseEventHooks
from botocore.loaders import Loader
from botocore.model import ServiceModel
from botocore.parsers import ResponseParser, ResponseParserFactory
from botocore.serialize import BaseRestSerializer
from botocore.signers import RequestSigner as RequestSigner

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

VALID_REGIONAL_ENDPOINTS_CONFIG: List[str]
LEGACY_GLOBAL_STS_REGIONS: List[str]

class _GetClientArgsTypeDef(TypedDict):
    serializer: BaseRestSerializer
    endpoint: Endpoint
    response_parser: ResponseParser
    event_emitter: BaseEventHooks
    request_signer: RequestSigner
    service_model: ServiceModel
    loader: Loader
    client_config: Config
    partition: Optional[str]
    exceptions_factory: Any

class ClientArgsCreator:
    def __init__(
        self,
        event_emitter: BaseEventHooks,
        user_agent: Any,
        response_parser_factory: ResponseParserFactory,
        loader: Loader,
        exceptions_factory: Any,
        config_store: ConfigValueStore,
    ) -> None: ...
    def get_client_args(
        self,
        service_model: ServiceModel,
        region_name: str,
        is_secure: bool,
        endpoint_url: Optional[str],
        verify: Optional[Union[str, bool]],
        credentials: Optional[Any],
        scoped_config: Optional[Any],
        client_config: Optional[Config],
        endpoint_bridge: Optional[Any],
    ) -> _GetClientArgsTypeDef: ...
    def compute_client_args(
        self,
        service_model: ServiceModel,
        client_config: Optional[Config],
        endpoint_bridge: Optional[Any],
        region_name: str,
        endpoint_url: str,
        is_secure: bool,
        scoped_config: Optional[Any],
    ) -> Any: ...
    def compute_s3_config(self, client_config: Optional[Config]) -> Dict[str, Any]: ...
