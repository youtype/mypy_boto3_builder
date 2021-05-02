# MediaTailorClient for boto3 MediaTailor module

> [Index](../index.md) > [MediaTailor](./index.md) > MediaTailorClient

Auto-generated documentation for [MediaTailor](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor)
type annotations stubs module [mypy_boto3_mediatailor](https://pypi.org/project/mypy-boto3-mediatailor/).

- [MediaTailorClient for boto3 MediaTailor module](#mediatailorclient-for-boto3-mediatailor-module)
  - [MediaTailorClient](#mediatailorclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_channel](#create_channel)
    - [create_program](#create_program)
    - [create_source_location](#create_source_location)
    - [create_vod_source](#create_vod_source)
    - [delete_channel](#delete_channel)
    - [delete_channel_policy](#delete_channel_policy)
    - [delete_playback_configuration](#delete_playback_configuration)
    - [delete_program](#delete_program)
    - [delete_source_location](#delete_source_location)
    - [delete_vod_source](#delete_vod_source)
    - [describe_channel](#describe_channel)
    - [describe_program](#describe_program)
    - [describe_source_location](#describe_source_location)
    - [describe_vod_source](#describe_vod_source)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_channel_policy](#get_channel_policy)
    - [get_channel_schedule](#get_channel_schedule)
    - [get_playback_configuration](#get_playback_configuration)
    - [list_channels](#list_channels)
    - [list_playback_configurations](#list_playback_configurations)
    - [list_source_locations](#list_source_locations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_vod_sources](#list_vod_sources)
    - [put_channel_policy](#put_channel_policy)
    - [put_playback_configuration](#put_playback_configuration)
    - [start_channel](#start_channel)
    - [stop_channel](#stop_channel)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_channel](#update_channel)
    - [update_source_location](#update_source_location)
    - [update_vod_source](#update_vod_source)
    - [get_paginator](#get_paginator)

## MediaTailorClient

Type annotations for `boto3.client("mediatailor")`

Can be used directly:

```python
from mypy_boto3_mediatailor.client import MediaTailorClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediatailor.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`


## Methods


### can_paginate

Type annotations for `boto3.client("mediatailor").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_channel

Type annotations for `boto3.client("mediatailor").create_channel` method.

[Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.create_channel)

```python
def create_channel(
    self,
    ChannelName: str,
    Outputs: List[RequestOutputItemTypeDef],
    PlaybackMode: Literal['LOOP'],
    Tags: Dict[str, str] = None
) -> CreateChannelResponseTypeDef:
    pass
```

### create_program

Type annotations for `boto3.client("mediatailor").create_program` method.

[Client.create_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.create_program)

```python
def create_program(
    self,
    ChannelName: str,
    ProgramName: str,
    ScheduleConfiguration: ScheduleConfigurationTypeDef,
    SourceLocationName: str,
    VodSourceName: str,
    AdBreaks: List["AdBreakTypeDef"] = None
) -> CreateProgramResponseTypeDef:
    pass
```

### create_source_location

Type annotations for `boto3.client("mediatailor").create_source_location` method.

[Client.create_source_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.create_source_location)

```python
def create_source_location(
    self,
    HttpConfiguration: "HttpConfigurationTypeDef",
    SourceLocationName: str,
    AccessConfiguration: "AccessConfigurationTypeDef" = None,
    DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef" = None,
    Tags: Dict[str, str] = None
) -> CreateSourceLocationResponseTypeDef:
    pass
```

### create_vod_source

Type annotations for `boto3.client("mediatailor").create_vod_source` method.

[Client.create_vod_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.create_vod_source)

```python
def create_vod_source(
    self,
    HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"],
    SourceLocationName: str,
    VodSourceName: str,
    Tags: Dict[str, str] = None
) -> CreateVodSourceResponseTypeDef:
    pass
```

### delete_channel

Type annotations for `boto3.client("mediatailor").delete_channel` method.

[Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.delete_channel)

```python
def delete_channel(
    self,
    ChannelName: str
) -> Dict[str, Any]:
    pass
```

### delete_channel_policy

Type annotations for `boto3.client("mediatailor").delete_channel_policy` method.

[Client.delete_channel_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.delete_channel_policy)

```python
def delete_channel_policy(
    self,
    ChannelName: str
) -> Dict[str, Any]:
    pass
```

### delete_playback_configuration

Type annotations for `boto3.client("mediatailor").delete_playback_configuration` method.

[Client.delete_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.delete_playback_configuration)

```python
def delete_playback_configuration(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_program

Type annotations for `boto3.client("mediatailor").delete_program` method.

[Client.delete_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.delete_program)

```python
def delete_program(
    self,
    ChannelName: str,
    ProgramName: str
) -> Dict[str, Any]:
    pass
```

### delete_source_location

Type annotations for `boto3.client("mediatailor").delete_source_location` method.

[Client.delete_source_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.delete_source_location)

```python
def delete_source_location(
    self,
    SourceLocationName: str
) -> Dict[str, Any]:
    pass
```

### delete_vod_source

Type annotations for `boto3.client("mediatailor").delete_vod_source` method.

[Client.delete_vod_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.delete_vod_source)

```python
def delete_vod_source(
    self,
    SourceLocationName: str,
    VodSourceName: str
) -> Dict[str, Any]:
    pass
```

### describe_channel

Type annotations for `boto3.client("mediatailor").describe_channel` method.

[Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.describe_channel)

```python
def describe_channel(
    self,
    ChannelName: str
) -> DescribeChannelResponseTypeDef:
    pass
```

### describe_program

Type annotations for `boto3.client("mediatailor").describe_program` method.

[Client.describe_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.describe_program)

```python
def describe_program(
    self,
    ChannelName: str,
    ProgramName: str
) -> DescribeProgramResponseTypeDef:
    pass
```

### describe_source_location

Type annotations for `boto3.client("mediatailor").describe_source_location` method.

[Client.describe_source_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.describe_source_location)

```python
def describe_source_location(
    self,
    SourceLocationName: str
) -> DescribeSourceLocationResponseTypeDef:
    pass
```

### describe_vod_source

Type annotations for `boto3.client("mediatailor").describe_vod_source` method.

[Client.describe_vod_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.describe_vod_source)

```python
def describe_vod_source(
    self,
    SourceLocationName: str,
    VodSourceName: str
) -> DescribeVodSourceResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediatailor").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.generate_presigned_url)

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

### get_channel_policy

Type annotations for `boto3.client("mediatailor").get_channel_policy` method.

[Client.get_channel_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.get_channel_policy)

```python
def get_channel_policy(
    self,
    ChannelName: str
) -> GetChannelPolicyResponseTypeDef:
    pass
```

### get_channel_schedule

Type annotations for `boto3.client("mediatailor").get_channel_schedule` method.

[Client.get_channel_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.get_channel_schedule)

```python
def get_channel_schedule(
    self,
    ChannelName: str,
    DurationMinutes: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetChannelScheduleResponseTypeDef:
    pass
```

### get_playback_configuration

Type annotations for `boto3.client("mediatailor").get_playback_configuration` method.

[Client.get_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.get_playback_configuration)

```python
def get_playback_configuration(
    self,
    Name: str
) -> GetPlaybackConfigurationResponseTypeDef:
    pass
```

### list_channels

Type annotations for `boto3.client("mediatailor").list_channels` method.

[Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.list_channels)

```python
def list_channels(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListChannelsResponseTypeDef:
    pass
```

### list_playback_configurations

Type annotations for `boto3.client("mediatailor").list_playback_configurations` method.

[Client.list_playback_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.list_playback_configurations)

```python
def list_playback_configurations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPlaybackConfigurationsResponseTypeDef:
    pass
```

### list_source_locations

Type annotations for `boto3.client("mediatailor").list_source_locations` method.

[Client.list_source_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.list_source_locations)

```python
def list_source_locations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSourceLocationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mediatailor").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_vod_sources

Type annotations for `boto3.client("mediatailor").list_vod_sources` method.

[Client.list_vod_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.list_vod_sources)

```python
def list_vod_sources(
    self,
    SourceLocationName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListVodSourcesResponseTypeDef:
    pass
```

### put_channel_policy

Type annotations for `boto3.client("mediatailor").put_channel_policy` method.

[Client.put_channel_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.put_channel_policy)

```python
def put_channel_policy(
    self,
    ChannelName: str,
    Policy: str
) -> Dict[str, Any]:
    pass
```

### put_playback_configuration

Type annotations for `boto3.client("mediatailor").put_playback_configuration` method.

[Client.put_playback_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.put_playback_configuration)

```python
def put_playback_configuration(
    self,
    AdDecisionServerUrl: str = None,
    AvailSuppression: "AvailSuppressionTypeDef" = None,
    Bumper: "BumperTypeDef" = None,
    CdnConfiguration: "CdnConfigurationTypeDef" = None,
    ConfigurationAliases: Dict[str, Dict[str, str]] = None,
    DashConfiguration: DashConfigurationForPutTypeDef = None,
    LivePreRollConfiguration: "LivePreRollConfigurationTypeDef" = None,
    ManifestProcessingRules: "ManifestProcessingRulesTypeDef" = None,
    Name: str = None,
    PersonalizationThresholdSeconds: int = None,
    SlateAdUrl: str = None,
    Tags: Dict[str, str] = None,
    TranscodeProfileName: str = None,
    VideoContentSourceUrl: str = None
) -> PutPlaybackConfigurationResponseTypeDef:
    pass
```

### start_channel

Type annotations for `boto3.client("mediatailor").start_channel` method.

[Client.start_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.start_channel)

```python
def start_channel(
    self,
    ChannelName: str
) -> Dict[str, Any]:
    pass
```

### stop_channel

Type annotations for `boto3.client("mediatailor").stop_channel` method.

[Client.stop_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.stop_channel)

```python
def stop_channel(
    self,
    ChannelName: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("mediatailor").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("mediatailor").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_channel

Type annotations for `boto3.client("mediatailor").update_channel` method.

[Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.update_channel)

```python
def update_channel(
    self,
    ChannelName: str,
    Outputs: List[RequestOutputItemTypeDef]
) -> UpdateChannelResponseTypeDef:
    pass
```

### update_source_location

Type annotations for `boto3.client("mediatailor").update_source_location` method.

[Client.update_source_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.update_source_location)

```python
def update_source_location(
    self,
    HttpConfiguration: "HttpConfigurationTypeDef",
    SourceLocationName: str,
    AccessConfiguration: "AccessConfigurationTypeDef" = None,
    DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef" = None
) -> UpdateSourceLocationResponseTypeDef:
    pass
```

### update_vod_source

Type annotations for `boto3.client("mediatailor").update_vod_source` method.

[Client.update_vod_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html#MediaTailor.Client.update_vod_source)

```python
def update_vod_source(
    self,
    HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"],
    SourceLocationName: str,
    VodSourceName: str
) -> UpdateVodSourceResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mediatailor").get_paginator` method with overloads.

- `client.get_paginator("get_channel_schedule")` -> [GetChannelSchedulePaginator](./paginators.md#getchannelschedulepaginator)
- `client.get_paginator("list_channels")` -> [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- `client.get_paginator("list_playback_configurations")` -> [ListPlaybackConfigurationsPaginator](./paginators.md#listplaybackconfigurationspaginator)
- `client.get_paginator("list_source_locations")` -> [ListSourceLocationsPaginator](./paginators.md#listsourcelocationspaginator)
- `client.get_paginator("list_vod_sources")` -> [ListVodSourcesPaginator](./paginators.md#listvodsourcespaginator)


