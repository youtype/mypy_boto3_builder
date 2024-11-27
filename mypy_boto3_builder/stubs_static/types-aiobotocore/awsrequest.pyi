"""
Type annotations for aiobotocore.awsrequest module.

Copyright 2024 Vlad Emelianov
"""

from botocore.awsrequest import AWSResponse

class AioAWSResponse(AWSResponse):
    @property
    def content(self) -> bytes: ...
    @property
    def text(self) -> str: ...
