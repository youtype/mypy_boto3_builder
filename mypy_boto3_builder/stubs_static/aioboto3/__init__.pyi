import logging
from typing import Any

from aioboto3.session import Session as Session

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> Any: ...
