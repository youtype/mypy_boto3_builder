# Type annotations for boto3 KinesisVideoSignalingChannels module

> [Index](../index.md) > KinesisVideoSignalingChannels

Auto-generated documentation for [KinesisVideoSignalingChannels](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels)
type annotations stubs module [mypy_boto3_kinesis_video_signaling](https://pypi.org/project/mypy-boto3-kinesis-video-signaling/).

```bash
pip install mypy-boto3-kinesis-video-signaling
```

- [Type annotations for boto3 KinesisVideoSignalingChannels module](#type-annotations-for-boto3-kinesisvideosignalingchannels-module)
  - [KinesisVideoSignalingChannelsClient](#kinesisvideosignalingchannelsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisVideoSignalingChannelsClient

Type annotations for  `boto3.client("kinesis-video-signaling")` as [KinesisVideoSignalingChannelsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient
```


KinesisVideoSignalingChannelsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_ice_server_config](./client.md#get-ice-server-config)
- [send_alexa_offer_to_master](./client.md#send-alexa-offer-to-master)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ClientLimitExceededException](./client.md#clientlimitexceededexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidClientException](./client.md#invalidclientexception)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [SessionExpiredException](./client.md#sessionexpiredexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis_video_signaling.literals import Service, ...
```

- [Service](./literals.md#service)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis_video_signaling.type_defs import IceServerTypeDef, ...
```

- [IceServerTypeDef](./type_defs.md#iceservertypedef)
- [GetIceServerConfigResponseTypeDef](./type_defs.md#geticeserverconfigresponsetypedef)
- [SendAlexaOfferToMasterResponseTypeDef](./type_defs.md#sendalexaoffertomasterresponsetypedef)
