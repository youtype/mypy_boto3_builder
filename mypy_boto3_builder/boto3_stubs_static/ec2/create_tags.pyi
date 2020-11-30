import sys
from typing import Any, Dict, Iterable, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class Tag(TypedDict):
    Key: str
    Value: str

def inject_create_tags(
    event_name: str, class_attributes: Dict[str, Any], **kwargs: Any
) -> None: ...
def create_tags(self: Any, **kwargs: Iterable[Any]) -> List[Tag]: ...
