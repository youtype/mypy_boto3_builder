"""
Type annotations for aiobotocore.parsers module.

Copyright 2025 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Any

from aiobotocore.eventstream import AioEventStream as AioEventStream
from botocore.model import Shape
from botocore.parsers import (
    EC2QueryParser,
    JSONParser,
    QueryParser,
    ResponseParser,
    ResponseParserFactory,
    RestJSONParser,
    RestXMLParser,
)

class AioRestXMLParser(RestXMLParser): ...
class AioEC2QueryParser(EC2QueryParser): ...
class AioQueryParser(QueryParser): ...

class AioJSONParser(JSONParser):
    async def parse(self, response: Mapping[str, Any], shape: Shape) -> dict[str, Any]: ...

class AioRestJSONParser(RestJSONParser): ...

PROTOCOL_PARSERS: dict[str, ResponseParser] = ...

class AioResponseParserFactory(ResponseParserFactory):
    def create_parser(self, protocol_name: str) -> ResponseParser: ...

def create_parser(protocol: str) -> ResponseParser: ...
