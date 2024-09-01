import sys
from typing import Any, Dict, Optional, Union

from aiobotocore.endpoint import AioEndpoint
from botocore.args import ClientArgsCreator
from botocore.client import ClientEndpointBridge
from botocore.config import Config
from botocore.credentials import Credentials
from botocore.hooks import BaseEventHooks
from botocore.loaders import Loader
from botocore.model import ServiceModel
from botocore.parsers import ResponseParser
from botocore.serialize import BaseRestSerializer
from botocore.signers import RequestSigner

if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class _GetClientArgsTypeDef(TypedDict):
    serializer: BaseRestSerializer
    endpoint: AioEndpoint
    response_parser: ResponseParser
    event_emitter: BaseEventHooks
    request_signer: RequestSigner
    service_model: ServiceModel
    loader: Loader
    client_config: Config
    partition: Optional[str]
    exceptions_factory: Any

class AioClientArgsCreator(ClientArgsCreator):
    def get_client_args(  # type: ignore [override]
        self,
        service_model: ServiceModel,
        region_name: str,
        is_secure: bool,
        endpoint_url: str,
        verify: Optional[Union[str, bool]],
        credentials: Credentials,
        scoped_config: Optional[Dict[str, Any]],
        client_config: Optional[Config],
        endpoint_bridge: ClientEndpointBridge,
        auth_token: Optional[str] = ...,
        endpoints_ruleset_data: Optional[Dict[str, Any]] = ...,
        partition_data: Optional[Dict[str, Any]] = ...,
    ) -> _GetClientArgsTypeDef: ...
