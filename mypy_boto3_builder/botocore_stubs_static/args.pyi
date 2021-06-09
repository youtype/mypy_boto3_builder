from typing import Any

from botocore.config import Config as Config
from botocore.endpoint import EndpointCreator as EndpointCreator
from botocore.loaders import Loader
from botocore.signers import RequestSigner as RequestSigner

VALID_REGIONAL_ENDPOINTS_CONFIG: Any
LEGACY_GLOBAL_STS_REGIONS: Any

class ClientArgsCreator:
    def __init__(
        self,
        event_emitter: Any,
        user_agent: Any,
        response_parser_factory: Any,
        loader: Loader,
        exceptions_factory: Any,
        config_store: Any,
    ) -> None: ...
    def get_client_args(
        self,
        service_model: Any,
        region_name: Any,
        is_secure: Any,
        endpoint_url: Any,
        verify: Any,
        credentials: Any,
        scoped_config: Any,
        client_config: Any,
        endpoint_bridge: Any,
    ) -> Any: ...
    def compute_client_args(
        self,
        service_model: Any,
        client_config: Any,
        endpoint_bridge: Any,
        region_name: Any,
        endpoint_url: Any,
        is_secure: Any,
        scoped_config: Any,
    ) -> Any: ...
    def compute_s3_config(self, client_config: Any) -> Any: ...
