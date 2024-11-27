"""
Type annotations for aiobotocore.parsers module.

Copyright 2024 Vlad Emelianov
"""

from typing import Any

from aiobotocore.eventstream import AioEventStream as AioEventStream
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
    async def parse(self, response: Any, shape: Any) -> Any: ...

class AioRestJSONParser(RestJSONParser): ...

PROTOCOL_PARSERS: Any

class AioResponseParserFactory(ResponseParserFactory):
    def create_parser(self, protocol_name: str) -> ResponseParser: ...

def create_parser(protocol: Any) -> ResponseParser: ...
