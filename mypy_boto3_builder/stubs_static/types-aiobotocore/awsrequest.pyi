from botocore.awsrequest import AWSResponse

class AioAWSResponse(AWSResponse):
    @property
    def content(self) -> bytes: ...
    @property
    def text(self) -> str: ...
