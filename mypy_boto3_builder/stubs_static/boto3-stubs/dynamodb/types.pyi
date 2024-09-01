import sys
from decimal import Context
from typing import Any, Mapping, Sequence, Tuple

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

_AttributeValueTypeDef = TypedDict(
    "_AttributeValueTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": Sequence[str],
        "NS": Sequence[str],
        "BS": Sequence[bytes],
        "M": Mapping[str, Any],
        "L": Sequence[Any],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

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

BINARY_TYPES: Tuple[Any, ...]

class Binary:
    def __init__(self, value: Any) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __bytes__(self) -> str: ...
    def __hash__(self) -> int: ...

class TypeSerializer:
    def serialize(self, value: Any) -> _AttributeValueTypeDef: ...

class TypeDeserializer:
    def deserialize(self, value: _AttributeValueTypeDef) -> Any: ...
