"""
Type annotations for aiobotocore.awsrequest module.

Copyright 2025 Vlad Emelianov
"""

from botocore.awsrequest import AWSResponse

class AioAWSResponse(AWSResponse):
    @property
    def content(self) -> bytes: ...
    @property
    def text(self) -> str: ...

class HttpxAWSResponse(AioAWSResponse): ...
