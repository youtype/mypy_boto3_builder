# Structures for boto3 CloudTrail module

> [Index](../index.md) > [CloudTrail](./index.md) > Structures

Auto-generated documentation for [CloudTrail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail)
type annotations stubs module [mypy_boto3_cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/).

- [Structures for boto3 CloudTrail module](#structures-for-boto3-cloudtrail-module)
  - [AdvancedEventSelectorTypeDef](#advancedeventselectortypedef)
  - [AdvancedFieldSelectorTypeDef](#advancedfieldselectortypedef)
  - [CreateTrailResponseTypeDef](#createtrailresponsetypedef)
  - [DataResourceTypeDef](#dataresourcetypedef)
  - [DescribeTrailsResponseTypeDef](#describetrailsresponsetypedef)
  - [EventSelectorTypeDef](#eventselectortypedef)
  - [EventTypeDef](#eventtypedef)
  - [GetEventSelectorsResponseTypeDef](#geteventselectorsresponsetypedef)
  - [GetInsightSelectorsResponseTypeDef](#getinsightselectorsresponsetypedef)
  - [GetTrailResponseTypeDef](#gettrailresponsetypedef)
  - [GetTrailStatusResponseTypeDef](#gettrailstatusresponsetypedef)
  - [InsightSelectorTypeDef](#insightselectortypedef)
  - [ListPublicKeysResponseTypeDef](#listpublickeysresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [ListTrailsResponseTypeDef](#listtrailsresponsetypedef)
  - [LookupAttributeTypeDef](#lookupattributetypedef)
  - [LookupEventsResponseTypeDef](#lookupeventsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PublicKeyTypeDef](#publickeytypedef)
  - [PutEventSelectorsResponseTypeDef](#puteventselectorsresponsetypedef)
  - [PutInsightSelectorsResponseTypeDef](#putinsightselectorsresponsetypedef)
  - [ResourceTagTypeDef](#resourcetagtypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TrailInfoTypeDef](#trailinfotypedef)
  - [TrailTypeDef](#trailtypedef)
  - [UpdateTrailResponseTypeDef](#updatetrailresponsetypedef)

## AdvancedEventSelectorTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import AdvancedEventSelectorTypeDef
```


Required fields:
- `FieldSelectors`: `List["AdvancedFieldSelectorTypeDef"]`



Optional fields:
- `Name`: `str`


## AdvancedFieldSelectorTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import AdvancedFieldSelectorTypeDef
```


Required fields:
- `Field`: `str`



Optional fields:
- `Equals`: `List[str]`
- `StartsWith`: `List[str]`
- `EndsWith`: `List[str]`
- `NotEquals`: `List[str]`
- `NotStartsWith`: `List[str]`
- `NotEndsWith`: `List[str]`


## CreateTrailResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import CreateTrailResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `S3BucketName`: `str`
- `S3KeyPrefix`: `str`
- `SnsTopicName`: `str`
- `SnsTopicARN`: `str`
- `IncludeGlobalServiceEvents`: `bool`
- `IsMultiRegionTrail`: `bool`
- `TrailARN`: `str`
- `LogFileValidationEnabled`: `bool`
- `CloudWatchLogsLogGroupArn`: `str`
- `CloudWatchLogsRoleArn`: `str`
- `KmsKeyId`: `str`
- `IsOrganizationTrail`: `bool`


## DataResourceTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import DataResourceTypeDef
```




Optional fields:
- `Type`: `str`
- `Values`: `List[str]`


## DescribeTrailsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import DescribeTrailsResponseTypeDef
```




Optional fields:
- `trailList`: `List["TrailTypeDef"]`


## EventSelectorTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import EventSelectorTypeDef
```




Optional fields:
- `ReadWriteType`: `ReadWriteType`
- `IncludeManagementEvents`: `bool`
- `DataResources`: `List["DataResourceTypeDef"]`
- `ExcludeManagementEventSources`: `List[str]`


## EventTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import EventTypeDef
```




Optional fields:
- `EventId`: `str`
- `EventName`: `str`
- `ReadOnly`: `str`
- `AccessKeyId`: `str`
- `EventTime`: `datetime`
- `EventSource`: `str`
- `Username`: `str`
- `Resources`: `List["ResourceTypeDef"]`
- `CloudTrailEvent`: `str`


## GetEventSelectorsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import GetEventSelectorsResponseTypeDef
```




Optional fields:
- `TrailARN`: `str`
- `EventSelectors`: `List["EventSelectorTypeDef"]`
- `AdvancedEventSelectors`: `List["AdvancedEventSelectorTypeDef"]`


## GetInsightSelectorsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import GetInsightSelectorsResponseTypeDef
```




Optional fields:
- `TrailARN`: `str`
- `InsightSelectors`: `List["InsightSelectorTypeDef"]`


## GetTrailResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import GetTrailResponseTypeDef
```




Optional fields:
- `Trail`: `"TrailTypeDef"`


## GetTrailStatusResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import GetTrailStatusResponseTypeDef
```




Optional fields:
- `IsLogging`: `bool`
- `LatestDeliveryError`: `str`
- `LatestNotificationError`: `str`
- `LatestDeliveryTime`: `datetime`
- `LatestNotificationTime`: `datetime`
- `StartLoggingTime`: `datetime`
- `StopLoggingTime`: `datetime`
- `LatestCloudWatchLogsDeliveryError`: `str`
- `LatestCloudWatchLogsDeliveryTime`: `datetime`
- `LatestDigestDeliveryTime`: `datetime`
- `LatestDigestDeliveryError`: `str`
- `LatestDeliveryAttemptTime`: `str`
- `LatestNotificationAttemptTime`: `str`
- `LatestNotificationAttemptSucceeded`: `str`
- `LatestDeliveryAttemptSucceeded`: `str`
- `TimeLoggingStarted`: `str`
- `TimeLoggingStopped`: `str`


## InsightSelectorTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import InsightSelectorTypeDef
```




Optional fields:
- `InsightType`: `Literal['ApiCallRateInsight']`


## ListPublicKeysResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import ListPublicKeysResponseTypeDef
```




Optional fields:
- `PublicKeyList`: `List["PublicKeyTypeDef"]`
- `NextToken`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `ResourceTagList`: `List["ResourceTagTypeDef"]`
- `NextToken`: `str`


## ListTrailsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import ListTrailsResponseTypeDef
```




Optional fields:
- `Trails`: `List["TrailInfoTypeDef"]`
- `NextToken`: `str`


## LookupAttributeTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import LookupAttributeTypeDef
```


Required fields:
- `AttributeKey`: `LookupAttributeKey`
- `AttributeValue`: `str`




## LookupEventsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import LookupEventsResponseTypeDef
```




Optional fields:
- `Events`: `List["EventTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PublicKeyTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import PublicKeyTypeDef
```




Optional fields:
- `Value`: `Union[bytes, IO[bytes]]`
- `ValidityStartTime`: `datetime`
- `ValidityEndTime`: `datetime`
- `Fingerprint`: `str`


## PutEventSelectorsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import PutEventSelectorsResponseTypeDef
```




Optional fields:
- `TrailARN`: `str`
- `EventSelectors`: `List["EventSelectorTypeDef"]`
- `AdvancedEventSelectors`: `List["AdvancedEventSelectorTypeDef"]`


## PutInsightSelectorsResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import PutInsightSelectorsResponseTypeDef
```




Optional fields:
- `TrailARN`: `str`
- `InsightSelectors`: `List["InsightSelectorTypeDef"]`


## ResourceTagTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import ResourceTagTypeDef
```




Optional fields:
- `ResourceId`: `str`
- `TagsList`: `List["TagTypeDef"]`


## ResourceTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import ResourceTypeDef
```




Optional fields:
- `ResourceType`: `str`
- `ResourceName`: `str`


## TagTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## TrailInfoTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import TrailInfoTypeDef
```




Optional fields:
- `TrailARN`: `str`
- `Name`: `str`
- `HomeRegion`: `str`


## TrailTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import TrailTypeDef
```




Optional fields:
- `Name`: `str`
- `S3BucketName`: `str`
- `S3KeyPrefix`: `str`
- `SnsTopicName`: `str`
- `SnsTopicARN`: `str`
- `IncludeGlobalServiceEvents`: `bool`
- `IsMultiRegionTrail`: `bool`
- `HomeRegion`: `str`
- `TrailARN`: `str`
- `LogFileValidationEnabled`: `bool`
- `CloudWatchLogsLogGroupArn`: `str`
- `CloudWatchLogsRoleArn`: `str`
- `KmsKeyId`: `str`
- `HasCustomEventSelectors`: `bool`
- `HasInsightSelectors`: `bool`
- `IsOrganizationTrail`: `bool`


## UpdateTrailResponseTypeDef

```python
from mypy_boto3_cloudtrail.type_defs import UpdateTrailResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `S3BucketName`: `str`
- `S3KeyPrefix`: `str`
- `SnsTopicName`: `str`
- `SnsTopicARN`: `str`
- `IncludeGlobalServiceEvents`: `bool`
- `IsMultiRegionTrail`: `bool`
- `TrailARN`: `str`
- `LogFileValidationEnabled`: `bool`
- `CloudWatchLogsLogGroupArn`: `str`
- `CloudWatchLogsRoleArn`: `str`
- `KmsKeyId`: `str`
- `IsOrganizationTrail`: `bool`

