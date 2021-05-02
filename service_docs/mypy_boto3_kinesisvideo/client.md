# KinesisVideoClient for boto3 KinesisVideo module

> [Index](../index.md) > [KinesisVideo](./index.md) > KinesisVideoClient

Auto-generated documentation for [KinesisVideo](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo)
type annotations stubs module [mypy_boto3_kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/).

- [KinesisVideoClient for boto3 KinesisVideo module](#kinesisvideoclient-for-boto3-kinesisvideo-module)
  - [KinesisVideoClient](#kinesisvideoclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_signaling_channel](#create_signaling_channel)
    - [create_stream](#create_stream)
    - [delete_signaling_channel](#delete_signaling_channel)
    - [delete_stream](#delete_stream)
    - [describe_signaling_channel](#describe_signaling_channel)
    - [describe_stream](#describe_stream)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_data_endpoint](#get_data_endpoint)
    - [get_signaling_channel_endpoint](#get_signaling_channel_endpoint)
    - [list_signaling_channels](#list_signaling_channels)
    - [list_streams](#list_streams)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_tags_for_stream](#list_tags_for_stream)
    - [tag_resource](#tag_resource)
    - [tag_stream](#tag_stream)
    - [untag_resource](#untag_resource)
    - [untag_stream](#untag_stream)
    - [update_data_retention](#update_data_retention)
    - [update_signaling_channel](#update_signaling_channel)
    - [update_stream](#update_stream)
    - [get_paginator](#get_paginator)

## KinesisVideoClient

Type annotations for `boto3.client("kinesisvideo")`

Can be used directly:

```python
from mypy_boto3_kinesisvideo.client import KinesisVideoClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kinesisvideo.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AccountChannelLimitExceededException`
- `Exceptions.AccountStreamLimitExceededException`
- `Exceptions.ClientError`
- `Exceptions.ClientLimitExceededException`
- `Exceptions.DeviceStreamLimitExceededException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidDeviceException`
- `Exceptions.InvalidResourceFormatException`
- `Exceptions.NotAuthorizedException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TagsPerResourceExceededLimitException`
- `Exceptions.VersionMismatchException`


## Methods


### can_paginate

Type annotations for `boto3.client("kinesisvideo").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_signaling_channel

Type annotations for `boto3.client("kinesisvideo").create_signaling_channel` method.

[Client.create_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.create_signaling_channel)

```python
def create_signaling_channel(
    self,
    ChannelName: str,
    ChannelType: Literal['SINGLE_MASTER'] = None,
    SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None,
    Tags: List[TagTypeDef] = None
) -> CreateSignalingChannelOutputTypeDef:
    pass
```

### create_stream

Type annotations for `boto3.client("kinesisvideo").create_stream` method.

[Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.create_stream)

```python
def create_stream(
    self,
    StreamName: str,
    DeviceName: str = None,
    MediaType: str = None,
    KmsKeyId: str = None,
    DataRetentionInHours: int = None,
    Tags: Dict[str, str] = None
) -> CreateStreamOutputTypeDef:
    pass
```

### delete_signaling_channel

Type annotations for `boto3.client("kinesisvideo").delete_signaling_channel` method.

[Client.delete_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_signaling_channel)

```python
def delete_signaling_channel(
    self,
    ChannelARN: str,
    CurrentVersion: str = None
) -> Dict[str, Any]:
    pass
```

### delete_stream

Type annotations for `boto3.client("kinesisvideo").delete_stream` method.

[Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_stream)

```python
def delete_stream(
    self,
    StreamARN: str,
    CurrentVersion: str = None
) -> Dict[str, Any]:
    pass
```

### describe_signaling_channel

Type annotations for `boto3.client("kinesisvideo").describe_signaling_channel` method.

[Client.describe_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_signaling_channel)

```python
def describe_signaling_channel(
    self,
    ChannelName: str = None,
    ChannelARN: str = None
) -> DescribeSignalingChannelOutputTypeDef:
    pass
```

### describe_stream

Type annotations for `boto3.client("kinesisvideo").describe_stream` method.

[Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_stream)

```python
def describe_stream(
    self,
    StreamName: str = None,
    StreamARN: str = None
) -> DescribeStreamOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kinesisvideo").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.generate_presigned_url)

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

### get_data_endpoint

Type annotations for `boto3.client("kinesisvideo").get_data_endpoint` method.

[Client.get_data_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_data_endpoint)

```python
def get_data_endpoint(
    self,
    APIName: APIName,
    StreamName: str = None,
    StreamARN: str = None
) -> GetDataEndpointOutputTypeDef:
    pass
```

### get_signaling_channel_endpoint

Type annotations for `boto3.client("kinesisvideo").get_signaling_channel_endpoint` method.

[Client.get_signaling_channel_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.get_signaling_channel_endpoint)

```python
def get_signaling_channel_endpoint(
    self,
    ChannelARN: str,
    SingleMasterChannelEndpointConfiguration: SingleMasterChannelEndpointConfigurationTypeDef = None
) -> GetSignalingChannelEndpointOutputTypeDef:
    pass
```

### list_signaling_channels

Type annotations for `boto3.client("kinesisvideo").list_signaling_channels` method.

[Client.list_signaling_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_signaling_channels)

```python
def list_signaling_channels(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    ChannelNameCondition: ChannelNameConditionTypeDef = None
) -> ListSignalingChannelsOutputTypeDef:
    pass
```

### list_streams

Type annotations for `boto3.client("kinesisvideo").list_streams` method.

[Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_streams)

```python
def list_streams(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    StreamNameCondition: StreamNameConditionTypeDef = None
) -> ListStreamsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("kinesisvideo").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str,
    NextToken: str = None
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_tags_for_stream

Type annotations for `boto3.client("kinesisvideo").list_tags_for_stream` method.

[Client.list_tags_for_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_stream)

```python
def list_tags_for_stream(
    self,
    NextToken: str = None,
    StreamARN: str = None,
    StreamName: str = None
) -> ListTagsForStreamOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("kinesisvideo").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List[TagTypeDef]
) -> Dict[str, Any]:
    pass
```

### tag_stream

Type annotations for `boto3.client("kinesisvideo").tag_stream` method.

[Client.tag_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_stream)

```python
def tag_stream(
    self,
    Tags: Dict[str, str],
    StreamARN: str = None,
    StreamName: str = None
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("kinesisvideo").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeyList: List[str]
) -> Dict[str, Any]:
    pass
```

### untag_stream

Type annotations for `boto3.client("kinesisvideo").untag_stream` method.

[Client.untag_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_stream)

```python
def untag_stream(
    self,
    TagKeyList: List[str],
    StreamARN: str = None,
    StreamName: str = None
) -> Dict[str, Any]:
    pass
```

### update_data_retention

Type annotations for `boto3.client("kinesisvideo").update_data_retention` method.

[Client.update_data_retention documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_data_retention)

```python
def update_data_retention(
    self,
    CurrentVersion: str,
    Operation: UpdateDataRetentionOperation,
    DataRetentionChangeInHours: int,
    StreamName: str = None,
    StreamARN: str = None
) -> Dict[str, Any]:
    pass
```

### update_signaling_channel

Type annotations for `boto3.client("kinesisvideo").update_signaling_channel` method.

[Client.update_signaling_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_signaling_channel)

```python
def update_signaling_channel(
    self,
    ChannelARN: str,
    CurrentVersion: str,
    SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_stream

Type annotations for `boto3.client("kinesisvideo").update_stream` method.

[Client.update_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo.Client.update_stream)

```python
def update_stream(
    self,
    CurrentVersion: str,
    StreamName: str = None,
    StreamARN: str = None,
    DeviceName: str = None,
    MediaType: str = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("kinesisvideo").get_paginator` method with overloads.

- `client.get_paginator("list_signaling_channels")` -> [ListSignalingChannelsPaginator](./paginators.md#listsignalingchannelspaginator)
- `client.get_paginator("list_streams")` -> [ListStreamsPaginator](./paginators.md#liststreamspaginator)


