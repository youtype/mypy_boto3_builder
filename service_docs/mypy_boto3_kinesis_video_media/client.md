# KinesisVideoMediaClient for boto3 KinesisVideoMedia module

> [Index](../index.md) > [KinesisVideoMedia](./index.md) > KinesisVideoMediaClient

Auto-generated documentation for [KinesisVideoMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html#KinesisVideoMedia)
type annotations stubs module [mypy_boto3_kinesis_video_media](https://pypi.org/project/mypy-boto3-kinesis-video-media/).

- [KinesisVideoMediaClient for boto3 KinesisVideoMedia module](#kinesisvideomediaclient-for-boto3-kinesisvideomedia-module)
  - [KinesisVideoMediaClient](#kinesisvideomediaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_media](#get_media)

## KinesisVideoMediaClient

Type annotations for `boto3.client("kinesis-video-media")`

Can be used directly:

```python
from mypy_boto3_kinesis_video_media.client import KinesisVideoMediaClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kinesis_video_media.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ClientLimitExceededException`
- `Exceptions.ConnectionLimitExceededException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidEndpointException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("kinesis-video-media").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kinesis-video-media").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_media

Type annotations for `boto3.client("kinesis-video-media").get_media` method.

[Client.get_media documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.get_media)

```python
def get_media(
    self,
    StartSelector: StartSelectorTypeDef,
    StreamName: str = None,
    StreamARN: str = None
) -> GetMediaOutputTypeDef:
    pass
```



