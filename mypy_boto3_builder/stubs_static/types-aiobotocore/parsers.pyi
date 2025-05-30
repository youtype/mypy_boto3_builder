"""
Type annotations for aiobotocore.parsers module.

Copyright 2025 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Any

from aiobotocore.eventstream import AioEventStream as AioEventStream
from botocore.model import Shape
from botocore.parsers import (
    BaseCBORParser,
    BaseEventStreamParser,
    BaseJSONParser,
    BaseRestParser,
    BaseRpcV2Parser,
    BaseXMLResponseParser,
    EC2QueryParser,
    EventStreamCBORParser,
    EventStreamJSONParser,
    EventStreamXMLParser,
    JSONParser,
    QueryParser,
    ResponseParser,
    ResponseParserFactory,
    RestJSONParser,
    RestXMLParser,
    RpcV2CBORParser,
)

class AioResponseParserFactory(ResponseParserFactory):
    def create_parser(self, protocol_name: str) -> ResponseParser: ...

def create_parser(protocol: str) -> ResponseParser: ...

class AioResponseParser(ResponseParser):
    async def parse(self, response: Mapping[str, Any], shape: Shape) -> dict[str, Any]: ...

class AioBaseXMLResponseParser(BaseXMLResponseParser, AioResponseParser): ...
class AioQueryParser(QueryParser, AioBaseXMLResponseParser): ...
class AioEC2QueryParser(EC2QueryParser, AioQueryParser): ...
class AioBaseJSONParser(BaseJSONParser, AioResponseParser): ...
class AioBaseCBORParser(BaseCBORParser, AioResponseParser): ...
class AioBaseEventStreamParser(BaseEventStreamParser, AioResponseParser): ...
class AioEventStreamJSONParser(
    EventStreamJSONParser, AioBaseEventStreamParser, AioBaseJSONParser
): ...
class AioEventStreamXMLParser(
    EventStreamXMLParser, AioBaseEventStreamParser, AioBaseXMLResponseParser
): ...
class AioEventStreamCBORParser(
    EventStreamCBORParser, AioBaseEventStreamParser, AioBaseCBORParser
): ...
class AioJSONParser(JSONParser, AioBaseJSONParser): ...
class AioBaseRestParser(BaseRestParser, AioResponseParser): ...
class AioBaseRpcV2Parser(BaseRpcV2Parser, AioResponseParser): ...
class AioRestJSONParser(RestJSONParser, AioBaseRestParser, AioBaseJSONParser): ...
class AioRpcV2CBORParser(RpcV2CBORParser, AioBaseRpcV2Parser, AioBaseCBORParser): ...
class AioRestXMLParser(RestXMLParser, AioBaseRestParser, AioBaseXMLResponseParser): ...

PROTOCOL_PARSERS: dict[str, ResponseParser] = ...
