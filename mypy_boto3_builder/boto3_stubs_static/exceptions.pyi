from typing import Any, Iterable

import botocore.exceptions

class Boto3Error(Exception): ...
class ResourceLoadException(Boto3Error): ...
class NoVersionFound(Boto3Error): ...

class UnknownAPIVersionError(Boto3Error, botocore.exceptions.DataNotFoundError):
    def __init__(
        self,
        service_name: str,
        bad_api_version: str,
        available_api_versions: Iterable[str],
    ): ...

class ResourceNotExistsError(Boto3Error, botocore.exceptions.DataNotFoundError):
    def __init__(
        self,
        service_name: str,
        available_services: Iterable[str],
        has_low_level_client: bool,
    ) -> None: ...

class RetriesExceededError(Boto3Error):
    def __init__(self, last_exception: Boto3Error, msg: str = "Max Retries Exceeded") -> None: ...

class S3TransferFailedError(Boto3Error):
    pass

class S3UploadFailedError(Boto3Error):
    pass

class DynamoDBOperationNotSupportedError(Boto3Error):
    def __init__(self, operation: str, value: Any) -> None: ...

DynanmoDBOperationNotSupportedError = DynamoDBOperationNotSupportedError

class DynamoDBNeedsConditionError(Boto3Error):
    def __init__(self, value: Any) -> None: ...

class DynamoDBNeedsKeyConditionError(Boto3Error): ...
