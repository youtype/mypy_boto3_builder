# Type annotations for boto3 KinesisVideoMedia module

> [Index](../index.md) > KinesisVideoMedia

Auto-generated documentation for [KinesisVideoMedia](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html#KinesisVideoMedia)
type annotations stubs module [mypy_boto3_kinesis_video_media](https://pypi.org/project/mypy-boto3-kinesis-video-media/).

```bash
pip install mypy-boto3-kinesis-video-media
```

- [Type annotations for boto3 KinesisVideoMedia module](#type-annotations-for-boto3-kinesisvideomedia-module)
  - [KinesisVideoMediaClient](#kinesisvideomediaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisVideoMediaClient

Type annotations for  `boto3.client("kinesis-video-media")` as [KinesisVideoMediaClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesis_video_media.client import KinesisVideoMediaClient
```


KinesisVideoMediaClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_media](./client.md#get-media)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ClientLimitExceededException](./client.md#clientlimitexceededexception)
- [ConnectionLimitExceededException](./client.md#connectionlimitexceededexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidEndpointException](./client.md#invalidendpointexception)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis_video_media.literals import StartSelectorType, ...
```

- [StartSelectorType](./literals.md#startselectortype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesis_video_media.type_defs import GetMediaOutputTypeDef, ...
```

- [GetMediaOutputTypeDef](./type_defs.md#getmediaoutputtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [StartSelectorTypeDef](./type_defs.md#startselectortypedef)
