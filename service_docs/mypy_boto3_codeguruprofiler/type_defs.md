# Structures for boto3 CodeGuruProfiler module

> [Index](../index.md) > [CodeGuruProfiler](./index.md) > Structures

Auto-generated documentation for [CodeGuruProfiler](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler)
type annotations stubs module [mypy_boto3_codeguruprofiler](https://pypi.org/project/mypy-boto3-codeguruprofiler/).

- [Structures for boto3 CodeGuruProfiler module](#structures-for-boto3-codeguruprofiler-module)
  - [AddNotificationChannelsResponseTypeDef](#addnotificationchannelsresponsetypedef)
  - [AgentConfigurationTypeDef](#agentconfigurationtypedef)
  - [AgentOrchestrationConfigTypeDef](#agentorchestrationconfigtypedef)
  - [AggregatedProfileTimeTypeDef](#aggregatedprofiletimetypedef)
  - [AnomalyInstanceTypeDef](#anomalyinstancetypedef)
  - [AnomalyTypeDef](#anomalytypedef)
  - [BatchGetFrameMetricDataResponseTypeDef](#batchgetframemetricdataresponsetypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [ConfigureAgentResponseTypeDef](#configureagentresponsetypedef)
  - [CreateProfilingGroupResponseTypeDef](#createprofilinggroupresponsetypedef)
  - [DescribeProfilingGroupResponseTypeDef](#describeprofilinggroupresponsetypedef)
  - [FindingsReportSummaryTypeDef](#findingsreportsummarytypedef)
  - [FrameMetricDatumTypeDef](#framemetricdatumtypedef)
  - [FrameMetricTypeDef](#framemetrictypedef)
  - [GetFindingsReportAccountSummaryResponseTypeDef](#getfindingsreportaccountsummaryresponsetypedef)
  - [GetNotificationConfigurationResponseTypeDef](#getnotificationconfigurationresponsetypedef)
  - [GetPolicyResponseTypeDef](#getpolicyresponsetypedef)
  - [GetProfileResponseTypeDef](#getprofileresponsetypedef)
  - [GetRecommendationsResponseTypeDef](#getrecommendationsresponsetypedef)
  - [ListFindingsReportsResponseTypeDef](#listfindingsreportsresponsetypedef)
  - [ListProfileTimesResponseTypeDef](#listprofiletimesresponsetypedef)
  - [ListProfilingGroupsResponseTypeDef](#listprofilinggroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MatchTypeDef](#matchtypedef)
  - [MetricTypeDef](#metrictypedef)
  - [NotificationConfigurationTypeDef](#notificationconfigurationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PatternTypeDef](#patterntypedef)
  - [ProfileTimeTypeDef](#profiletimetypedef)
  - [ProfilingGroupDescriptionTypeDef](#profilinggroupdescriptiontypedef)
  - [ProfilingStatusTypeDef](#profilingstatustypedef)
  - [PutPermissionResponseTypeDef](#putpermissionresponsetypedef)
  - [RecommendationTypeDef](#recommendationtypedef)
  - [RemoveNotificationChannelResponseTypeDef](#removenotificationchannelresponsetypedef)
  - [RemovePermissionResponseTypeDef](#removepermissionresponsetypedef)
  - [TimestampStructureTypeDef](#timestampstructuretypedef)
  - [UpdateProfilingGroupResponseTypeDef](#updateprofilinggroupresponsetypedef)
  - [UserFeedbackTypeDef](#userfeedbacktypedef)

## AddNotificationChannelsResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import AddNotificationChannelsResponseTypeDef
```




Optional fields:
- `notificationConfiguration`: `"NotificationConfigurationTypeDef"`


## AgentConfigurationTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import AgentConfigurationTypeDef
```


Required fields:
- `periodInSeconds`: `int`
- `shouldProfile`: `bool`



Optional fields:
- `agentParameters`: `Dict[AgentParameterField, str]`


## AgentOrchestrationConfigTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import AgentOrchestrationConfigTypeDef
```


Required fields:
- `profilingEnabled`: `bool`




## AggregatedProfileTimeTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import AggregatedProfileTimeTypeDef
```




Optional fields:
- `period`: `AggregationPeriod`
- `start`: `datetime`


## AnomalyInstanceTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import AnomalyInstanceTypeDef
```


Required fields:
- `id`: `str`
- `startTime`: `datetime`



Optional fields:
- `endTime`: `datetime`
- `userFeedback`: `"UserFeedbackTypeDef"`


## AnomalyTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import AnomalyTypeDef
```


Required fields:
- `instances`: `List["AnomalyInstanceTypeDef"]`
- `metric`: `"MetricTypeDef"`
- `reason`: `str`




## BatchGetFrameMetricDataResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import BatchGetFrameMetricDataResponseTypeDef
```


Required fields:
- `endTime`: `datetime`
- `endTimes`: `List["TimestampStructureTypeDef"]`
- `frameMetricData`: `List["FrameMetricDatumTypeDef"]`
- `resolution`: `AggregationPeriod`
- `startTime`: `datetime`
- `unprocessedEndTimes`: `Dict[str, List["TimestampStructureTypeDef"]]`




## ChannelTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ChannelTypeDef
```


Required fields:
- `eventPublishers`: `List[Literal['AnomalyDetection']]`
- `uri`: `str`



Optional fields:
- `id`: `str`


## ConfigureAgentResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ConfigureAgentResponseTypeDef
```


Required fields:
- `configuration`: `"AgentConfigurationTypeDef"`




## CreateProfilingGroupResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import CreateProfilingGroupResponseTypeDef
```


Required fields:
- `profilingGroup`: `"ProfilingGroupDescriptionTypeDef"`




## DescribeProfilingGroupResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import DescribeProfilingGroupResponseTypeDef
```


Required fields:
- `profilingGroup`: `"ProfilingGroupDescriptionTypeDef"`




## FindingsReportSummaryTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import FindingsReportSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `profileEndTime`: `datetime`
- `profileStartTime`: `datetime`
- `profilingGroupName`: `str`
- `totalNumberOfFindings`: `int`


## FrameMetricDatumTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import FrameMetricDatumTypeDef
```


Required fields:
- `frameMetric`: `"FrameMetricTypeDef"`
- `values`: `List[float]`




## FrameMetricTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import FrameMetricTypeDef
```


Required fields:
- `frameName`: `str`
- `threadStates`: `List[str]`
- `type`: `Literal['AggregatedRelativeTotalTime']`




## GetFindingsReportAccountSummaryResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import GetFindingsReportAccountSummaryResponseTypeDef
```


Required fields:
- `reportSummaries`: `List["FindingsReportSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## GetNotificationConfigurationResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import GetNotificationConfigurationResponseTypeDef
```


Required fields:
- `notificationConfiguration`: `"NotificationConfigurationTypeDef"`




## GetPolicyResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import GetPolicyResponseTypeDef
```


Required fields:
- `policy`: `str`
- `revisionId`: `str`




## GetProfileResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import GetProfileResponseTypeDef
```


Required fields:
- `contentType`: `str`
- `profile`: `Union[bytes, IO[bytes]]`



Optional fields:
- `contentEncoding`: `str`


## GetRecommendationsResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import GetRecommendationsResponseTypeDef
```


Required fields:
- `anomalies`: `List["AnomalyTypeDef"]`
- `profileEndTime`: `datetime`
- `profileStartTime`: `datetime`
- `profilingGroupName`: `str`
- `recommendations`: `List["RecommendationTypeDef"]`




## ListFindingsReportsResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ListFindingsReportsResponseTypeDef
```


Required fields:
- `findingsReportSummaries`: `List["FindingsReportSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListProfileTimesResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ListProfileTimesResponseTypeDef
```


Required fields:
- `profileTimes`: `List["ProfileTimeTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListProfilingGroupsResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ListProfilingGroupsResponseTypeDef
```


Required fields:
- `profilingGroupNames`: `List[str]`



Optional fields:
- `nextToken`: `str`
- `profilingGroups`: `List["ProfilingGroupDescriptionTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## MatchTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import MatchTypeDef
```




Optional fields:
- `frameAddress`: `str`
- `targetFramesIndex`: `int`
- `thresholdBreachValue`: `float`


## MetricTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import MetricTypeDef
```


Required fields:
- `frameName`: `str`
- `threadStates`: `List[str]`
- `type`: `Literal['AggregatedRelativeTotalTime']`




## NotificationConfigurationTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import NotificationConfigurationTypeDef
```




Optional fields:
- `channels`: `List["ChannelTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PatternTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import PatternTypeDef
```




Optional fields:
- `countersToAggregate`: `List[str]`
- `description`: `str`
- `id`: `str`
- `name`: `str`
- `resolutionSteps`: `str`
- `targetFrames`: `List[List[str]]`
- `thresholdPercent`: `float`


## ProfileTimeTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ProfileTimeTypeDef
```




Optional fields:
- `start`: `datetime`


## ProfilingGroupDescriptionTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ProfilingGroupDescriptionTypeDef
```




Optional fields:
- `agentOrchestrationConfig`: `"AgentOrchestrationConfigTypeDef"`
- `arn`: `str`
- `computePlatform`: `ComputePlatform`
- `createdAt`: `datetime`
- `name`: `str`
- `profilingStatus`: `"ProfilingStatusTypeDef"`
- `tags`: `Dict[str, str]`
- `updatedAt`: `datetime`


## ProfilingStatusTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import ProfilingStatusTypeDef
```




Optional fields:
- `latestAgentOrchestratedAt`: `datetime`
- `latestAgentProfileReportedAt`: `datetime`
- `latestAggregatedProfile`: `"AggregatedProfileTimeTypeDef"`


## PutPermissionResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import PutPermissionResponseTypeDef
```


Required fields:
- `policy`: `str`
- `revisionId`: `str`




## RecommendationTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import RecommendationTypeDef
```


Required fields:
- `allMatchesCount`: `int`
- `allMatchesSum`: `float`
- `endTime`: `datetime`
- `pattern`: `"PatternTypeDef"`
- `startTime`: `datetime`
- `topMatches`: `List["MatchTypeDef"]`




## RemoveNotificationChannelResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import RemoveNotificationChannelResponseTypeDef
```




Optional fields:
- `notificationConfiguration`: `"NotificationConfigurationTypeDef"`


## RemovePermissionResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import RemovePermissionResponseTypeDef
```


Required fields:
- `policy`: `str`
- `revisionId`: `str`




## TimestampStructureTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import TimestampStructureTypeDef
```


Required fields:
- `value`: `datetime`




## UpdateProfilingGroupResponseTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import UpdateProfilingGroupResponseTypeDef
```


Required fields:
- `profilingGroup`: `"ProfilingGroupDescriptionTypeDef"`




## UserFeedbackTypeDef

```python
from mypy_boto3_codeguruprofiler.type_defs import UserFeedbackTypeDef
```


Required fields:
- `type`: `FeedbackType`



