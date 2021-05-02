# Type annotations for boto3 KinesisVideo module

> [Index](../index.md) > KinesisVideo

Auto-generated documentation for [KinesisVideo](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo)
type annotations stubs module [mypy_boto3_kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/).

```bash
pip install mypy-boto3-kinesisvideo
```

- [Type annotations for boto3 KinesisVideo module](#type-annotations-for-boto3-kinesisvideo-module)
  - [KinesisVideoClient](#kinesisvideoclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisVideoClient

Type annotations for  `boto3.client("kinesisvideo")` as [KinesisVideoClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesisvideo.client import KinesisVideoClient
```


KinesisVideoClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_signaling_channel](./client.md#create-signaling-channel)
- [create_stream](./client.md#create-stream)
- [delete_signaling_channel](./client.md#delete-signaling-channel)
- [delete_stream](./client.md#delete-stream)
- [describe_signaling_channel](./client.md#describe-signaling-channel)
- [describe_stream](./client.md#describe-stream)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_data_endpoint](./client.md#get-data-endpoint)
- [get_paginator](./client.md#get-paginator)
- [get_signaling_channel_endpoint](./client.md#get-signaling-channel-endpoint)
- [list_signaling_channels](./client.md#list-signaling-channels)
- [list_streams](./client.md#list-streams)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_tags_for_stream](./client.md#list-tags-for-stream)
- [tag_resource](./client.md#tag-resource)
- [tag_stream](./client.md#tag-stream)
- [untag_resource](./client.md#untag-resource)
- [untag_stream](./client.md#untag-stream)
- [update_data_retention](./client.md#update-data-retention)
- [update_signaling_channel](./client.md#update-signaling-channel)
- [update_stream](./client.md#update-stream)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AccountChannelLimitExceededException](./client.md#accountchannellimitexceededexception)
- [AccountStreamLimitExceededException](./client.md#accountstreamlimitexceededexception)
- [ClientError](./client.md#clienterror)
- [ClientLimitExceededException](./client.md#clientlimitexceededexception)
- [DeviceStreamLimitExceededException](./client.md#devicestreamlimitexceededexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidDeviceException](./client.md#invaliddeviceexception)
- [InvalidResourceFormatException](./client.md#invalidresourceformatexception)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TagsPerResourceExceededLimitException](./client.md#tagsperresourceexceededlimitexception)
- [VersionMismatchException](./client.md#versionmismatchexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("kinesisvideo").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_kinesisvideo.paginators import ListSignalingChannelsPaginator, ...
```

- [ListSignalingChannelsPaginator](./paginators.md#listsignalingchannelspaginator)
- [ListStreamsPaginator](./paginators.md#liststreamspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesisvideo.literals import APIName, ...
```

- [APIName](./literals.md#apiname)
- [ChannelProtocol](./literals.md#channelprotocol)
- [ChannelRole](./literals.md#channelrole)
- [ChannelType](./literals.md#channeltype)
- [ComparisonOperator](./literals.md#comparisonoperator)
- [ListSignalingChannelsPaginatorName](./literals.md#listsignalingchannelspaginatorname)
- [ListStreamsPaginatorName](./literals.md#liststreamspaginatorname)
- [Status](./literals.md#status)
- [UpdateDataRetentionOperation](./literals.md#updatedataretentionoperation)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesisvideo.type_defs import ChannelInfoTypeDef, ...
```

- [ChannelInfoTypeDef](./type_defs.md#channelinfotypedef)
- [ChannelNameConditionTypeDef](./type_defs.md#channelnameconditiontypedef)
- [CreateSignalingChannelOutputTypeDef](./type_defs.md#createsignalingchanneloutputtypedef)
- [CreateStreamOutputTypeDef](./type_defs.md#createstreamoutputtypedef)
- [DescribeSignalingChannelOutputTypeDef](./type_defs.md#describesignalingchanneloutputtypedef)
- [DescribeStreamOutputTypeDef](./type_defs.md#describestreamoutputtypedef)
- [GetDataEndpointOutputTypeDef](./type_defs.md#getdataendpointoutputtypedef)
- [GetSignalingChannelEndpointOutputTypeDef](./type_defs.md#getsignalingchannelendpointoutputtypedef)
- [ListSignalingChannelsOutputTypeDef](./type_defs.md#listsignalingchannelsoutputtypedef)
- [ListStreamsOutputTypeDef](./type_defs.md#liststreamsoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ListTagsForStreamOutputTypeDef](./type_defs.md#listtagsforstreamoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResourceEndpointListItemTypeDef](./type_defs.md#resourceendpointlistitemtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SingleMasterChannelEndpointConfigurationTypeDef](./type_defs.md#singlemasterchannelendpointconfigurationtypedef)
- [SingleMasterConfigurationTypeDef](./type_defs.md#singlemasterconfigurationtypedef)
- [StreamInfoTypeDef](./type_defs.md#streaminfotypedef)
- [StreamNameConditionTypeDef](./type_defs.md#streamnameconditiontypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
