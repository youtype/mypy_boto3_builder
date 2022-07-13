import os
from typing import Type

SOCKET_ERROR: Type[ConnectionError]

def filter_python_deprecation_warnings() -> None: ...

rename_file = os.rename
