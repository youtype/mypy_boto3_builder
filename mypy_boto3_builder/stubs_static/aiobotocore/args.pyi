import sys
from typing import Any, Optional, Union

import botocore.parsers
import botocore.serialize
from aiobotocore.config import AioConfig
from aiobotocore.endpoint import AioEndpoint
from aiobotocore.signers import AioRequestSigner
from botocore.args import ClientArgsCreator
from botocore.loaders import Loader
from botocore.model import ServiceModel

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class GetClientArgsTypeDef(TypedDict):
    serializer: botocore.serialize.BaseRestSerializer
    endpoint: AioEndpoint
    response_parser: botocore.parsers.ResponseParser
    event_emitter: Any
    request_signer: AioRequestSigner
    service_model: ServiceModel
    loader: Loader
    client_config: AioConfig
    partition: Optional[str]
    exceptions_factory: Any

class AioClientArgsCreator(ClientArgsCreator):
    def get_client_args(
        self,
        service_model: ServiceModel,
        region_name: str,
        is_secure: bool,
        endpoint_url: Optional[str],
        verify: Optional[Union[str, bool]],
        credentials: Optional[Any],
        scoped_config: Optional[Any],
        client_config: Optional[AioConfig],  # type: ignore
        endpoint_bridge: Optional[Any],
    ) -> GetClientArgsTypeDef: ...
