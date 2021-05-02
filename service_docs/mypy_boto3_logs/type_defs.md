# Structures for boto3 CloudWatchLogs module

> [Index](../index.md) > [CloudWatchLogs](./index.md) > Structures

Auto-generated documentation for [CloudWatchLogs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs)
type annotations stubs module [mypy_boto3_logs](https://pypi.org/project/mypy-boto3-logs/).

- [Structures for boto3 CloudWatchLogs module](#structures-for-boto3-cloudwatchlogs-module)
  - [DestinationTypeDef](#destinationtypedef)
  - [ExportTaskExecutionInfoTypeDef](#exporttaskexecutioninfotypedef)
  - [ExportTaskStatusTypeDef](#exporttaskstatustypedef)
  - [ExportTaskTypeDef](#exporttasktypedef)
  - [FilteredLogEventTypeDef](#filteredlogeventtypedef)
  - [LogGroupFieldTypeDef](#loggroupfieldtypedef)
  - [LogGroupTypeDef](#loggrouptypedef)
  - [LogStreamTypeDef](#logstreamtypedef)
  - [MetricFilterMatchRecordTypeDef](#metricfiltermatchrecordtypedef)
  - [MetricFilterTypeDef](#metricfiltertypedef)
  - [MetricTransformationTypeDef](#metrictransformationtypedef)
  - [OutputLogEventTypeDef](#outputlogeventtypedef)
  - [QueryDefinitionTypeDef](#querydefinitiontypedef)
  - [QueryInfoTypeDef](#queryinfotypedef)
  - [QueryStatisticsTypeDef](#querystatisticstypedef)
  - [RejectedLogEventsInfoTypeDef](#rejectedlogeventsinfotypedef)
  - [ResourcePolicyTypeDef](#resourcepolicytypedef)
  - [ResultFieldTypeDef](#resultfieldtypedef)
  - [SearchedLogStreamTypeDef](#searchedlogstreamtypedef)
  - [SubscriptionFilterTypeDef](#subscriptionfiltertypedef)
  - [CreateExportTaskResponseTypeDef](#createexporttaskresponsetypedef)
  - [DeleteQueryDefinitionResponseTypeDef](#deletequerydefinitionresponsetypedef)
  - [DescribeDestinationsResponseTypeDef](#describedestinationsresponsetypedef)
  - [DescribeExportTasksResponseTypeDef](#describeexporttasksresponsetypedef)
  - [DescribeLogGroupsResponseTypeDef](#describeloggroupsresponsetypedef)
  - [DescribeLogStreamsResponseTypeDef](#describelogstreamsresponsetypedef)
  - [DescribeMetricFiltersResponseTypeDef](#describemetricfiltersresponsetypedef)
  - [DescribeQueriesResponseTypeDef](#describequeriesresponsetypedef)
  - [DescribeQueryDefinitionsResponseTypeDef](#describequerydefinitionsresponsetypedef)
  - [DescribeResourcePoliciesResponseTypeDef](#describeresourcepoliciesresponsetypedef)
  - [DescribeSubscriptionFiltersResponseTypeDef](#describesubscriptionfiltersresponsetypedef)
  - [FilterLogEventsResponseTypeDef](#filterlogeventsresponsetypedef)
  - [GetLogEventsResponseTypeDef](#getlogeventsresponsetypedef)
  - [GetLogGroupFieldsResponseTypeDef](#getloggroupfieldsresponsetypedef)
  - [GetLogRecordResponseTypeDef](#getlogrecordresponsetypedef)
  - [GetQueryResultsResponseTypeDef](#getqueryresultsresponsetypedef)
  - [InputLogEventTypeDef](#inputlogeventtypedef)
  - [ListTagsLogGroupResponseTypeDef](#listtagsloggroupresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutDestinationResponseTypeDef](#putdestinationresponsetypedef)
  - [PutLogEventsResponseTypeDef](#putlogeventsresponsetypedef)
  - [PutQueryDefinitionResponseTypeDef](#putquerydefinitionresponsetypedef)
  - [PutResourcePolicyResponseTypeDef](#putresourcepolicyresponsetypedef)
  - [StartQueryResponseTypeDef](#startqueryresponsetypedef)
  - [StopQueryResponseTypeDef](#stopqueryresponsetypedef)
  - [TestMetricFilterResponseTypeDef](#testmetricfilterresponsetypedef)

## DestinationTypeDef

```python
from mypy_boto3_logs.type_defs import DestinationTypeDef
```




Optional fields:
- `destinationName`: `str`
- `targetArn`: `str`
- `roleArn`: `str`
- `accessPolicy`: `str`
- `arn`: `str`
- `creationTime`: `int`


## ExportTaskExecutionInfoTypeDef

```python
from mypy_boto3_logs.type_defs import ExportTaskExecutionInfoTypeDef
```




Optional fields:
- `creationTime`: `int`
- `completionTime`: `int`


## ExportTaskStatusTypeDef

```python
from mypy_boto3_logs.type_defs import ExportTaskStatusTypeDef
```




Optional fields:
- `code`: `ExportTaskStatusCode`
- `message`: `str`


## ExportTaskTypeDef

```python
from mypy_boto3_logs.type_defs import ExportTaskTypeDef
```




Optional fields:
- `taskId`: `str`
- `taskName`: `str`
- `logGroupName`: `str`
- `from`: `int`
- `to`: `int`
- `destination`: `str`
- `destinationPrefix`: `str`
- `status`: `"ExportTaskStatusTypeDef"`
- `executionInfo`: `"ExportTaskExecutionInfoTypeDef"`


## FilteredLogEventTypeDef

```python
from mypy_boto3_logs.type_defs import FilteredLogEventTypeDef
```




Optional fields:
- `logStreamName`: `str`
- `timestamp`: `int`
- `message`: `str`
- `ingestionTime`: `int`
- `eventId`: `str`


## LogGroupFieldTypeDef

```python
from mypy_boto3_logs.type_defs import LogGroupFieldTypeDef
```




Optional fields:
- `name`: `str`
- `percent`: `int`


## LogGroupTypeDef

```python
from mypy_boto3_logs.type_defs import LogGroupTypeDef
```




Optional fields:
- `logGroupName`: `str`
- `creationTime`: `int`
- `retentionInDays`: `int`
- `metricFilterCount`: `int`
- `arn`: `str`
- `storedBytes`: `int`
- `kmsKeyId`: `str`


## LogStreamTypeDef

```python
from mypy_boto3_logs.type_defs import LogStreamTypeDef
```




Optional fields:
- `logStreamName`: `str`
- `creationTime`: `int`
- `firstEventTimestamp`: `int`
- `lastEventTimestamp`: `int`
- `lastIngestionTime`: `int`
- `uploadSequenceToken`: `str`
- `arn`: `str`
- `storedBytes`: `int`


## MetricFilterMatchRecordTypeDef

```python
from mypy_boto3_logs.type_defs import MetricFilterMatchRecordTypeDef
```




Optional fields:
- `eventNumber`: `int`
- `eventMessage`: `str`
- `extractedValues`: `Dict[str, str]`


## MetricFilterTypeDef

```python
from mypy_boto3_logs.type_defs import MetricFilterTypeDef
```




Optional fields:
- `filterName`: `str`
- `filterPattern`: `str`
- `metricTransformations`: `List["MetricTransformationTypeDef"]`
- `creationTime`: `int`
- `logGroupName`: `str`


## MetricTransformationTypeDef

```python
from mypy_boto3_logs.type_defs import MetricTransformationTypeDef
```


Required fields:
- `metricName`: `str`
- `metricNamespace`: `str`
- `metricValue`: `str`



Optional fields:
- `defaultValue`: `float`


## OutputLogEventTypeDef

```python
from mypy_boto3_logs.type_defs import OutputLogEventTypeDef
```




Optional fields:
- `timestamp`: `int`
- `message`: `str`
- `ingestionTime`: `int`


## QueryDefinitionTypeDef

```python
from mypy_boto3_logs.type_defs import QueryDefinitionTypeDef
```




Optional fields:
- `queryDefinitionId`: `str`
- `name`: `str`
- `queryString`: `str`
- `lastModified`: `int`
- `logGroupNames`: `List[str]`


## QueryInfoTypeDef

```python
from mypy_boto3_logs.type_defs import QueryInfoTypeDef
```




Optional fields:
- `queryId`: `str`
- `queryString`: `str`
- `status`: `QueryStatus`
- `createTime`: `int`
- `logGroupName`: `str`


## QueryStatisticsTypeDef

```python
from mypy_boto3_logs.type_defs import QueryStatisticsTypeDef
```




Optional fields:
- `recordsMatched`: `float`
- `recordsScanned`: `float`
- `bytesScanned`: `float`


## RejectedLogEventsInfoTypeDef

```python
from mypy_boto3_logs.type_defs import RejectedLogEventsInfoTypeDef
```




Optional fields:
- `tooNewLogEventStartIndex`: `int`
- `tooOldLogEventEndIndex`: `int`
- `expiredLogEventEndIndex`: `int`


## ResourcePolicyTypeDef

```python
from mypy_boto3_logs.type_defs import ResourcePolicyTypeDef
```




Optional fields:
- `policyName`: `str`
- `policyDocument`: `str`
- `lastUpdatedTime`: `int`


## ResultFieldTypeDef

```python
from mypy_boto3_logs.type_defs import ResultFieldTypeDef
```




Optional fields:
- `field`: `str`
- `value`: `str`


## SearchedLogStreamTypeDef

```python
from mypy_boto3_logs.type_defs import SearchedLogStreamTypeDef
```




Optional fields:
- `logStreamName`: `str`
- `searchedCompletely`: `bool`


## SubscriptionFilterTypeDef

```python
from mypy_boto3_logs.type_defs import SubscriptionFilterTypeDef
```




Optional fields:
- `filterName`: `str`
- `logGroupName`: `str`
- `filterPattern`: `str`
- `destinationArn`: `str`
- `roleArn`: `str`
- `distribution`: `Distribution`
- `creationTime`: `int`


## CreateExportTaskResponseTypeDef

```python
from mypy_boto3_logs.type_defs import CreateExportTaskResponseTypeDef
```




Optional fields:
- `taskId`: `str`


## DeleteQueryDefinitionResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DeleteQueryDefinitionResponseTypeDef
```




Optional fields:
- `success`: `bool`


## DescribeDestinationsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeDestinationsResponseTypeDef
```




Optional fields:
- `destinations`: `List["DestinationTypeDef"]`
- `nextToken`: `str`


## DescribeExportTasksResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeExportTasksResponseTypeDef
```




Optional fields:
- `exportTasks`: `List["ExportTaskTypeDef"]`
- `nextToken`: `str`


## DescribeLogGroupsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeLogGroupsResponseTypeDef
```




Optional fields:
- `logGroups`: `List["LogGroupTypeDef"]`
- `nextToken`: `str`


## DescribeLogStreamsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeLogStreamsResponseTypeDef
```




Optional fields:
- `logStreams`: `List["LogStreamTypeDef"]`
- `nextToken`: `str`


## DescribeMetricFiltersResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeMetricFiltersResponseTypeDef
```




Optional fields:
- `metricFilters`: `List["MetricFilterTypeDef"]`
- `nextToken`: `str`


## DescribeQueriesResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeQueriesResponseTypeDef
```




Optional fields:
- `queries`: `List["QueryInfoTypeDef"]`
- `nextToken`: `str`


## DescribeQueryDefinitionsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeQueryDefinitionsResponseTypeDef
```




Optional fields:
- `queryDefinitions`: `List["QueryDefinitionTypeDef"]`
- `nextToken`: `str`


## DescribeResourcePoliciesResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeResourcePoliciesResponseTypeDef
```




Optional fields:
- `resourcePolicies`: `List["ResourcePolicyTypeDef"]`
- `nextToken`: `str`


## DescribeSubscriptionFiltersResponseTypeDef

```python
from mypy_boto3_logs.type_defs import DescribeSubscriptionFiltersResponseTypeDef
```




Optional fields:
- `subscriptionFilters`: `List["SubscriptionFilterTypeDef"]`
- `nextToken`: `str`


## FilterLogEventsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import FilterLogEventsResponseTypeDef
```




Optional fields:
- `events`: `List["FilteredLogEventTypeDef"]`
- `searchedLogStreams`: `List["SearchedLogStreamTypeDef"]`
- `nextToken`: `str`


## GetLogEventsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import GetLogEventsResponseTypeDef
```




Optional fields:
- `events`: `List["OutputLogEventTypeDef"]`
- `nextForwardToken`: `str`
- `nextBackwardToken`: `str`


## GetLogGroupFieldsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import GetLogGroupFieldsResponseTypeDef
```




Optional fields:
- `logGroupFields`: `List["LogGroupFieldTypeDef"]`


## GetLogRecordResponseTypeDef

```python
from mypy_boto3_logs.type_defs import GetLogRecordResponseTypeDef
```




Optional fields:
- `logRecord`: `Dict[str, str]`


## GetQueryResultsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import GetQueryResultsResponseTypeDef
```




Optional fields:
- `results`: `List[List["ResultFieldTypeDef"]]`
- `statistics`: `"QueryStatisticsTypeDef"`
- `status`: `QueryStatus`


## InputLogEventTypeDef

```python
from mypy_boto3_logs.type_defs import InputLogEventTypeDef
```


Required fields:
- `timestamp`: `int`
- `message`: `str`




## ListTagsLogGroupResponseTypeDef

```python
from mypy_boto3_logs.type_defs import ListTagsLogGroupResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_logs.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutDestinationResponseTypeDef

```python
from mypy_boto3_logs.type_defs import PutDestinationResponseTypeDef
```




Optional fields:
- `destination`: `"DestinationTypeDef"`


## PutLogEventsResponseTypeDef

```python
from mypy_boto3_logs.type_defs import PutLogEventsResponseTypeDef
```




Optional fields:
- `nextSequenceToken`: `str`
- `rejectedLogEventsInfo`: `"RejectedLogEventsInfoTypeDef"`


## PutQueryDefinitionResponseTypeDef

```python
from mypy_boto3_logs.type_defs import PutQueryDefinitionResponseTypeDef
```




Optional fields:
- `queryDefinitionId`: `str`


## PutResourcePolicyResponseTypeDef

```python
from mypy_boto3_logs.type_defs import PutResourcePolicyResponseTypeDef
```




Optional fields:
- `resourcePolicy`: `"ResourcePolicyTypeDef"`


## StartQueryResponseTypeDef

```python
from mypy_boto3_logs.type_defs import StartQueryResponseTypeDef
```




Optional fields:
- `queryId`: `str`


## StopQueryResponseTypeDef

```python
from mypy_boto3_logs.type_defs import StopQueryResponseTypeDef
```




Optional fields:
- `success`: `bool`


## TestMetricFilterResponseTypeDef

```python
from mypy_boto3_logs.type_defs import TestMetricFilterResponseTypeDef
```




Optional fields:
- `matches`: `List["MetricFilterMatchRecordTypeDef"]`

