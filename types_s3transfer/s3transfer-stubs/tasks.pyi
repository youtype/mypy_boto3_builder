import logging
from typing import Any, Callable, Dict, Optional, Sequence

from s3transfer.futures import TransferCoordinator
from s3transfer.utils import get_callbacks as get_callbacks

logger: logging.Logger

class Task:
    def __init__(
        self,
        transfer_coordinator: TransferCoordinator,
        main_kwargs: Optional[Dict[str, Any]] = ...,
        pending_main_kwargs: Optional[Dict[str, Any]] = ...,
        done_callbacks: Optional[Sequence[Callable[..., Any]]] = ...,
        is_final: bool = ...,
    ) -> None: ...
    @property
    def transfer_id(self) -> str: ...
    def __call__(self) -> None: ...

class SubmissionTask(Task): ...
class CreateMultipartUploadTask(Task): ...
class CompleteMultipartUploadTask(Task): ...
