# Structures for boto3 KinesisVideo module

> [Index](../index.md) > [KinesisVideo](./index.md) > Structures

Auto-generated documentation for [KinesisVideo](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html#KinesisVideo)
type annotations stubs module [mypy_boto3_kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/).

- [Structures for boto3 KinesisVideo module](#structures-for-boto3-kinesisvideo-module)
  - [ChannelInfoTypeDef](#channelinfotypedef)
  - [ChannelNameConditionTypeDef](#channelnameconditiontypedef)
  - [CreateSignalingChannelOutputTypeDef](#createsignalingchanneloutputtypedef)
  - [CreateStreamOutputTypeDef](#createstreamoutputtypedef)
  - [DescribeSignalingChannelOutputTypeDef](#describesignalingchanneloutputtypedef)
  - [DescribeStreamOutputTypeDef](#describestreamoutputtypedef)
  - [GetDataEndpointOutputTypeDef](#getdataendpointoutputtypedef)
  - [GetSignalingChannelEndpointOutputTypeDef](#getsignalingchannelendpointoutputtypedef)
  - [ListSignalingChannelsOutputTypeDef](#listsignalingchannelsoutputtypedef)
  - [ListStreamsOutputTypeDef](#liststreamsoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ListTagsForStreamOutputTypeDef](#listtagsforstreamoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResourceEndpointListItemTypeDef](#resourceendpointlistitemtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SingleMasterChannelEndpointConfigurationTypeDef](#singlemasterchannelendpointconfigurationtypedef)
  - [SingleMasterConfigurationTypeDef](#singlemasterconfigurationtypedef)
  - [StreamInfoTypeDef](#streaminfotypedef)
  - [StreamNameConditionTypeDef](#streamnameconditiontypedef)
  - [TagTypeDef](#tagtypedef)

## ChannelInfoTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ChannelInfoTypeDef
```




Optional fields:
- `ChannelName`: `str`
- `ChannelARN`: `str`
- `ChannelType`: `Literal['SINGLE_MASTER']`
- `ChannelStatus`: `Status`
- `CreationTime`: `datetime`
- `SingleMasterConfiguration`: `"SingleMasterConfigurationTypeDef"`
- `Version`: `str`


## ChannelNameConditionTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ChannelNameConditionTypeDef
```




Optional fields:
- `ComparisonOperator`: `Literal['BEGINS_WITH']`
- `ComparisonValue`: `str`


## CreateSignalingChannelOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import CreateSignalingChannelOutputTypeDef
```




Optional fields:
- `ChannelARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStreamOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import CreateStreamOutputTypeDef
```




Optional fields:
- `StreamARN`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSignalingChannelOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import DescribeSignalingChannelOutputTypeDef
```




Optional fields:
- `ChannelInfo`: `"ChannelInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStreamOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import DescribeStreamOutputTypeDef
```




Optional fields:
- `StreamInfo`: `"StreamInfoTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetDataEndpointOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import GetDataEndpointOutputTypeDef
```




Optional fields:
- `DataEndpoint`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetSignalingChannelEndpointOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import GetSignalingChannelEndpointOutputTypeDef
```




Optional fields:
- `ResourceEndpointList`: `List["ResourceEndpointListItemTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSignalingChannelsOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ListSignalingChannelsOutputTypeDef
```




Optional fields:
- `ChannelInfoList`: `List["ChannelInfoTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStreamsOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ListStreamsOutputTypeDef
```




Optional fields:
- `StreamInfoList`: `List["StreamInfoTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForStreamOutputTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ListTagsForStreamOutputTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResourceEndpointListItemTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import ResourceEndpointListItemTypeDef
```




Optional fields:
- `Protocol`: `ChannelProtocol`
- `ResourceEndpoint`: `str`


## ResponseMetadata

```python
from mypy_boto3_kinesisvideo.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SingleMasterChannelEndpointConfigurationTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import SingleMasterChannelEndpointConfigurationTypeDef
```




Optional fields:
- `Protocols`: `List[ChannelProtocol]`
- `Role`: `ChannelRole`


## SingleMasterConfigurationTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import SingleMasterConfigurationTypeDef
```




Optional fields:
- `MessageTtlSeconds`: `int`


## StreamInfoTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import StreamInfoTypeDef
```




Optional fields:
- `DeviceName`: `str`
- `StreamName`: `str`
- `StreamARN`: `str`
- `MediaType`: `str`
- `KmsKeyId`: `str`
- `Version`: `str`
- `Status`: `Status`
- `CreationTime`: `datetime`
- `DataRetentionInHours`: `int`


## StreamNameConditionTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import StreamNameConditionTypeDef
```




Optional fields:
- `ComparisonOperator`: `Literal['BEGINS_WITH']`
- `ComparisonValue`: `str`


## TagTypeDef

```python
from mypy_boto3_kinesisvideo.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`



