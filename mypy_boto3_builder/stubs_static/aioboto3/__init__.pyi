import logging
from typing import Any

from aioboto3.session import Session as Session

__author__: str
__email__: str
__version__: str

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> Any: ...
