"""
Type annotations for aiobotocore.args module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, TypedDict

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

class _GetClientArgsTypeDef(TypedDict):
    serializer: BaseRestSerializer
    endpoint: AioEndpoint
    response_parser: ResponseParser
    event_emitter: BaseEventHooks
    request_signer: RequestSigner
    service_model: ServiceModel
    loader: Loader
    client_config: Config
    partition: str | None
    exceptions_factory: Any

class AioClientArgsCreator(ClientArgsCreator):
    def get_client_args(  # type: ignore[override]
        self,
        service_model: ServiceModel,
        region_name: str,
        is_secure: bool,
        endpoint_url: str,
        verify: str | bool | None,
        credentials: Credentials,
        scoped_config: dict[str, Any] | None,
        client_config: Config | None,
        endpoint_bridge: ClientEndpointBridge,
        auth_token: str | None = ...,
        endpoints_ruleset_data: dict[str, Any] | None = ...,
        partition_data: dict[str, Any] | None = ...,
    ) -> _GetClientArgsTypeDef: ...
