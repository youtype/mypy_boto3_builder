import sys
from decimal import Context
from typing import Any, Dict, Tuple

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

DynamoDBDataType = Literal["S", "N", "B", "SS", "NS", "BS", "NULL", "BOOL", "M", "L"]

STRING: Literal["S"]
NUMBER: Literal["N"]
BINARY: Literal["B"]
STRING_SET: Literal["SS"]
NUMBER_SET: Literal["NS"]
BINARY_SET: Literal["BS"]
NULL: Literal["NULL"]
BOOLEAN: Literal["BOOL"]
MAP: Literal["M"]
LIST: Literal["L"]

DYNAMODB_CONTEXT: Context

BINARY_TYPES: Tuple[type]

class Binary:
    def __init__(self, value: Any) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...

class TypeSerializer:
    def serialize(self, value: Any) -> Dict[DynamoDBDataType, Any]: ...

class TypeDeserializer:
    def deserialize(self, value: Dict[DynamoDBDataType, Any]) -> Any: ...
