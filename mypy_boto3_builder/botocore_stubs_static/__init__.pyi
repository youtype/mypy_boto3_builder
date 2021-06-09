import logging
from typing import Any, Dict, Tuple

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...

log: logging.Logger
ScalarTypes: Tuple[str, ...]
BOTOCORE_ROOT: str

UNSIGNED: Any
__version__: str

def xform_name(name: str, sep: str = ..., _xform_cache: Dict[str, str] = ...) -> str: ...
