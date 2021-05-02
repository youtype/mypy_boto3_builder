# IVSClient for boto3 IVS module

> [Index](../index.md) > [IVS](./index.md) > IVSClient

Auto-generated documentation for [IVS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS)
type annotations stubs module [mypy_boto3_ivs](https://pypi.org/project/mypy-boto3-ivs/).

- [IVSClient for boto3 IVS module](#ivsclient-for-boto3-ivs-module)
  - [IVSClient](#ivsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_get_channel](#batch_get_channel)
    - [batch_get_stream_key](#batch_get_stream_key)
    - [can_paginate](#can_paginate)
    - [create_channel](#create_channel)
    - [create_recording_configuration](#create_recording_configuration)
    - [create_stream_key](#create_stream_key)
    - [delete_channel](#delete_channel)
    - [delete_playback_key_pair](#delete_playback_key_pair)
    - [delete_recording_configuration](#delete_recording_configuration)
    - [delete_stream_key](#delete_stream_key)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_channel](#get_channel)
    - [get_playback_key_pair](#get_playback_key_pair)
    - [get_recording_configuration](#get_recording_configuration)
    - [get_stream](#get_stream)
    - [get_stream_key](#get_stream_key)
    - [import_playback_key_pair](#import_playback_key_pair)
    - [list_channels](#list_channels)
    - [list_playback_key_pairs](#list_playback_key_pairs)
    - [list_recording_configurations](#list_recording_configurations)
    - [list_stream_keys](#list_stream_keys)
    - [list_streams](#list_streams)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_metadata](#put_metadata)
    - [stop_stream](#stop_stream)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_channel](#update_channel)
    - [get_paginator](#get_paginator)

## IVSClient

Type annotations for `boto3.client("ivs")`

Can be used directly:

```python
from mypy_boto3_ivs.client import IVSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ivs.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ChannelNotBroadcasting`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.PendingVerification`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.StreamUnavailable`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### batch_get_channel

Type annotations for `boto3.client("ivs").batch_get_channel` method.

[Client.batch_get_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.batch_get_channel)

```python
def batch_get_channel(
    self,
    arns: List[str]
) -> BatchGetChannelResponseTypeDef:
    pass
```

### batch_get_stream_key

Type annotations for `boto3.client("ivs").batch_get_stream_key` method.

[Client.batch_get_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.batch_get_stream_key)

```python
def batch_get_stream_key(
    self,
    arns: List[str]
) -> BatchGetStreamKeyResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("ivs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_channel

Type annotations for `boto3.client("ivs").create_channel` method.

[Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.create_channel)

```python
def create_channel(
    self,
    name: str = None,
    latencyMode: ChannelLatencyMode = None,
    type: ChannelType = None,
    authorized: bool = None,
    recordingConfigurationArn: str = None,
    tags: Dict[str, str] = None
) -> CreateChannelResponseTypeDef:
    pass
```

### create_recording_configuration

Type annotations for `boto3.client("ivs").create_recording_configuration` method.

[Client.create_recording_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.create_recording_configuration)

```python
def create_recording_configuration(
    self,
    destinationConfiguration: "DestinationConfigurationTypeDef",
    name: str = None,
    tags: Dict[str, str] = None
) -> CreateRecordingConfigurationResponseTypeDef:
    pass
```

### create_stream_key

Type annotations for `boto3.client("ivs").create_stream_key` method.

[Client.create_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.create_stream_key)

```python
def create_stream_key(
    self,
    channelArn: str,
    tags: Dict[str, str] = None
) -> CreateStreamKeyResponseTypeDef:
    pass
```

### delete_channel

Type annotations for `boto3.client("ivs").delete_channel` method.

[Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.delete_channel)

```python
def delete_channel(
    self,
    arn: str
) -> None:
    pass
```

### delete_playback_key_pair

Type annotations for `boto3.client("ivs").delete_playback_key_pair` method.

[Client.delete_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.delete_playback_key_pair)

```python
def delete_playback_key_pair(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_recording_configuration

Type annotations for `boto3.client("ivs").delete_recording_configuration` method.

[Client.delete_recording_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.delete_recording_configuration)

```python
def delete_recording_configuration(
    self,
    arn: str
) -> None:
    pass
```

### delete_stream_key

Type annotations for `boto3.client("ivs").delete_stream_key` method.

[Client.delete_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.delete_stream_key)

```python
def delete_stream_key(
    self,
    arn: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ivs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.generate_presigned_url)

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

### get_channel

Type annotations for `boto3.client("ivs").get_channel` method.

[Client.get_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.get_channel)

```python
def get_channel(
    self,
    arn: str
) -> GetChannelResponseTypeDef:
    pass
```

### get_playback_key_pair

Type annotations for `boto3.client("ivs").get_playback_key_pair` method.

[Client.get_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.get_playback_key_pair)

```python
def get_playback_key_pair(
    self,
    arn: str
) -> GetPlaybackKeyPairResponseTypeDef:
    pass
```

### get_recording_configuration

Type annotations for `boto3.client("ivs").get_recording_configuration` method.

[Client.get_recording_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.get_recording_configuration)

```python
def get_recording_configuration(
    self,
    arn: str
) -> GetRecordingConfigurationResponseTypeDef:
    pass
```

### get_stream

Type annotations for `boto3.client("ivs").get_stream` method.

[Client.get_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.get_stream)

```python
def get_stream(
    self,
    channelArn: str
) -> GetStreamResponseTypeDef:
    pass
```

### get_stream_key

Type annotations for `boto3.client("ivs").get_stream_key` method.

[Client.get_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.get_stream_key)

```python
def get_stream_key(
    self,
    arn: str
) -> GetStreamKeyResponseTypeDef:
    pass
```

### import_playback_key_pair

Type annotations for `boto3.client("ivs").import_playback_key_pair` method.

[Client.import_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.import_playback_key_pair)

```python
def import_playback_key_pair(
    self,
    publicKeyMaterial: str,
    name: str = None,
    tags: Dict[str, str] = None
) -> ImportPlaybackKeyPairResponseTypeDef:
    pass
```

### list_channels

Type annotations for `boto3.client("ivs").list_channels` method.

[Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.list_channels)

```python
def list_channels(
    self,
    filterByName: str = None,
    filterByRecordingConfigurationArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListChannelsResponseTypeDef:
    pass
```

### list_playback_key_pairs

Type annotations for `boto3.client("ivs").list_playback_key_pairs` method.

[Client.list_playback_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.list_playback_key_pairs)

```python
def list_playback_key_pairs(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListPlaybackKeyPairsResponseTypeDef:
    pass
```

### list_recording_configurations

Type annotations for `boto3.client("ivs").list_recording_configurations` method.

[Client.list_recording_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.list_recording_configurations)

```python
def list_recording_configurations(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListRecordingConfigurationsResponseTypeDef:
    pass
```

### list_stream_keys

Type annotations for `boto3.client("ivs").list_stream_keys` method.

[Client.list_stream_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.list_stream_keys)

```python
def list_stream_keys(
    self,
    channelArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListStreamKeysResponseTypeDef:
    pass
```

### list_streams

Type annotations for `boto3.client("ivs").list_streams` method.

[Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.list_streams)

```python
def list_streams(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListStreamsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("ivs").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_metadata

Type annotations for `boto3.client("ivs").put_metadata` method.

[Client.put_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.put_metadata)

```python
def put_metadata(
    self,
    channelArn: str,
    metadata: str
) -> None:
    pass
```

### stop_stream

Type annotations for `boto3.client("ivs").stop_stream` method.

[Client.stop_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.stop_stream)

```python
def stop_stream(
    self,
    channelArn: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("ivs").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("ivs").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_channel

Type annotations for `boto3.client("ivs").update_channel` method.

[Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html#IVS.Client.update_channel)

```python
def update_channel(
    self,
    arn: str,
    name: str = None,
    latencyMode: ChannelLatencyMode = None,
    type: ChannelType = None,
    authorized: bool = None,
    recordingConfigurationArn: str = None
) -> UpdateChannelResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("ivs").get_paginator` method with overloads.

- `client.get_paginator("list_channels")` -> [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- `client.get_paginator("list_playback_key_pairs")` -> [ListPlaybackKeyPairsPaginator](./paginators.md#listplaybackkeypairspaginator)
- `client.get_paginator("list_recording_configurations")` -> [ListRecordingConfigurationsPaginator](./paginators.md#listrecordingconfigurationspaginator)
- `client.get_paginator("list_stream_keys")` -> [ListStreamKeysPaginator](./paginators.md#liststreamkeyspaginator)
- `client.get_paginator("list_streams")` -> [ListStreamsPaginator](./paginators.md#liststreamspaginator)


