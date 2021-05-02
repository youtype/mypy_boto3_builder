# KinesisVideoSignalingChannelsClient for boto3 KinesisVideoSignalingChannels module

> [Index](../index.md) > [KinesisVideoSignalingChannels](./index.md) > KinesisVideoSignalingChannelsClient

Auto-generated documentation for [KinesisVideoSignalingChannels](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels)
type annotations stubs module [mypy_boto3_kinesis_video_signaling](https://pypi.org/project/mypy-boto3-kinesis-video-signaling/).

- [KinesisVideoSignalingChannelsClient for boto3 KinesisVideoSignalingChannels module](#kinesisvideosignalingchannelsclient-for-boto3-kinesisvideosignalingchannels-module)
  - [KinesisVideoSignalingChannelsClient](#kinesisvideosignalingchannelsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_ice_server_config](#get_ice_server_config)
    - [send_alexa_offer_to_master](#send_alexa_offer_to_master)

## KinesisVideoSignalingChannelsClient

Type annotations for `boto3.client("kinesis-video-signaling")`

Can be used directly:

```python
from mypy_boto3_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kinesis_video_signaling.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ClientLimitExceededException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidClientException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.SessionExpiredException`


## Methods


### can_paginate

Type annotations for `boto3.client("kinesis-video-signaling").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kinesis-video-signaling").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.generate_presigned_url)

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

### get_ice_server_config

Type annotations for `boto3.client("kinesis-video-signaling").get_ice_server_config` method.

[Client.get_ice_server_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.get_ice_server_config)

```python
def get_ice_server_config(
    self,
    ChannelARN: str,
    ClientId: str = None,
    Service: Service = None,
    Username: str = None
) -> GetIceServerConfigResponseTypeDef:
    pass
```

### send_alexa_offer_to_master

Type annotations for `boto3.client("kinesis-video-signaling").send_alexa_offer_to_master` method.

[Client.send_alexa_offer_to_master documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.send_alexa_offer_to_master)

```python
def send_alexa_offer_to_master(
    self,
    ChannelARN: str,
    SenderClientId: str,
    MessagePayload: str
) -> SendAlexaOfferToMasterResponseTypeDef:
    pass
```