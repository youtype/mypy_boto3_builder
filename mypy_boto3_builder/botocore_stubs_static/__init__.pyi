import logging
from typing import Any, Callable, Dict, Tuple

from botocore.session import Session

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...

log: logging.Logger
ScalarTypes: Tuple[str, ...]
BOTOCORE_ROOT: str

UNSIGNED: Any
__version__: str

def xform_name(name: str, sep: str = ..., _xform_cache: Dict[str, str] = ...) -> str: ...
def register_initializer(callback: Callable[[Session], None]) -> None: ...
def unregister_initializer(callback: Callable[[Session], None]) -> None: ...
def invoke_initializers(session: Session) -> None: ...
