from botocore.args import ClientArgsCreator
from typing import Optional, Union, Dict, Any
from botocore.model import ServiceModel
from botocore.config import Config
from botocore.client import ClientEndpointBridge
from botocore.serialize import BaseRestSerializer
from botocore.signers import RequestSigner
from botocore.hooks import BaseEventHooks
from aiobotocore.endpoint import AioEndpoint
from botocore.credentials import Credentials
from botocore.parsers import ResponseParser
from botocore.loaders import Loader
import sys

if sys.version_info >= (3, 9):
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
    ) -> _GetClientArgsTypeDef: ...
