# CloudWatchLogsClient for boto3 CloudWatchLogs module

> [Index](../index.md) > [CloudWatchLogs](./index.md) > CloudWatchLogsClient

Auto-generated documentation for [CloudWatchLogs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs)
type annotations stubs module [mypy_boto3_logs](https://pypi.org/project/mypy-boto3-logs/).

- [CloudWatchLogsClient for boto3 CloudWatchLogs module](#cloudwatchlogsclient-for-boto3-cloudwatchlogs-module)
  - [CloudWatchLogsClient](#cloudwatchlogsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_kms_key](#associate_kms_key)
    - [can_paginate](#can_paginate)
    - [cancel_export_task](#cancel_export_task)
    - [create_export_task](#create_export_task)
    - [create_log_group](#create_log_group)
    - [create_log_stream](#create_log_stream)
    - [delete_destination](#delete_destination)
    - [delete_log_group](#delete_log_group)
    - [delete_log_stream](#delete_log_stream)
    - [delete_metric_filter](#delete_metric_filter)
    - [delete_query_definition](#delete_query_definition)
    - [delete_resource_policy](#delete_resource_policy)
    - [delete_retention_policy](#delete_retention_policy)
    - [delete_subscription_filter](#delete_subscription_filter)
    - [describe_destinations](#describe_destinations)
    - [describe_export_tasks](#describe_export_tasks)
    - [describe_log_groups](#describe_log_groups)
    - [describe_log_streams](#describe_log_streams)
    - [describe_metric_filters](#describe_metric_filters)
    - [describe_queries](#describe_queries)
    - [describe_query_definitions](#describe_query_definitions)
    - [describe_resource_policies](#describe_resource_policies)
    - [describe_subscription_filters](#describe_subscription_filters)
    - [disassociate_kms_key](#disassociate_kms_key)
    - [filter_log_events](#filter_log_events)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_log_events](#get_log_events)
    - [get_log_group_fields](#get_log_group_fields)
    - [get_log_record](#get_log_record)
    - [get_query_results](#get_query_results)
    - [list_tags_log_group](#list_tags_log_group)
    - [put_destination](#put_destination)
    - [put_destination_policy](#put_destination_policy)
    - [put_log_events](#put_log_events)
    - [put_metric_filter](#put_metric_filter)
    - [put_query_definition](#put_query_definition)
    - [put_resource_policy](#put_resource_policy)
    - [put_retention_policy](#put_retention_policy)
    - [put_subscription_filter](#put_subscription_filter)
    - [start_query](#start_query)
    - [stop_query](#stop_query)
    - [tag_log_group](#tag_log_group)
    - [test_metric_filter](#test_metric_filter)
    - [untag_log_group](#untag_log_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)

## CloudWatchLogsClient

Type annotations for `boto3.client("logs")`

Can be used directly:

```python
from mypy_boto3_logs.client import CloudWatchLogsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_logs.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DataAlreadyAcceptedException`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidSequenceTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.MalformedQueryException`
- `Exceptions.OperationAbortedException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.UnrecognizedClientException`


## Methods


### associate_kms_key

Type annotations for `boto3.client("logs").associate_kms_key` method.

[Client.associate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.associate_kms_key)

```python
def associate_kms_key(
    self,
    logGroupName: str,
    kmsKeyId: str
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("logs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_export_task

Type annotations for `boto3.client("logs").cancel_export_task` method.

[Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.cancel_export_task)

```python
def cancel_export_task(
    self,
    taskId: str
) -> None:
    pass
```

### create_export_task

Type annotations for `boto3.client("logs").create_export_task` method.

[Client.create_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.create_export_task)

```python
def create_export_task(
    self,
    logGroupName: str,
    fromTime: int,
    to: int,
    destination: str,
    taskName: str = None,
    logStreamNamePrefix: str = None,
    destinationPrefix: str = None
) -> CreateExportTaskResponseTypeDef:
    pass
```

### create_log_group

Type annotations for `boto3.client("logs").create_log_group` method.

[Client.create_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.create_log_group)

```python
def create_log_group(
    self,
    logGroupName: str,
    kmsKeyId: str = None,
    tags: Dict[str, str] = None
) -> None:
    pass
```

### create_log_stream

Type annotations for `boto3.client("logs").create_log_stream` method.

[Client.create_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.create_log_stream)

```python
def create_log_stream(
    self,
    logGroupName: str,
    logStreamName: str
) -> None:
    pass
```

### delete_destination

Type annotations for `boto3.client("logs").delete_destination` method.

[Client.delete_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_destination)

```python
def delete_destination(
    self,
    destinationName: str
) -> None:
    pass
```

### delete_log_group

Type annotations for `boto3.client("logs").delete_log_group` method.

[Client.delete_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group)

```python
def delete_log_group(
    self,
    logGroupName: str
) -> None:
    pass
```

### delete_log_stream

Type annotations for `boto3.client("logs").delete_log_stream` method.

[Client.delete_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_log_stream)

```python
def delete_log_stream(
    self,
    logGroupName: str,
    logStreamName: str
) -> None:
    pass
```

### delete_metric_filter

Type annotations for `boto3.client("logs").delete_metric_filter` method.

[Client.delete_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_metric_filter)

```python
def delete_metric_filter(
    self,
    logGroupName: str,
    filterName: str
) -> None:
    pass
```

### delete_query_definition

Type annotations for `boto3.client("logs").delete_query_definition` method.

[Client.delete_query_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_query_definition)

```python
def delete_query_definition(
    self,
    queryDefinitionId: str
) -> DeleteQueryDefinitionResponseTypeDef:
    pass
```

### delete_resource_policy

Type annotations for `boto3.client("logs").delete_resource_policy` method.

[Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_resource_policy)

```python
def delete_resource_policy(
    self,
    policyName: str = None
) -> None:
    pass
```

### delete_retention_policy

Type annotations for `boto3.client("logs").delete_retention_policy` method.

[Client.delete_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_retention_policy)

```python
def delete_retention_policy(
    self,
    logGroupName: str
) -> None:
    pass
```

### delete_subscription_filter

Type annotations for `boto3.client("logs").delete_subscription_filter` method.

[Client.delete_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter)

```python
def delete_subscription_filter(
    self,
    logGroupName: str,
    filterName: str
) -> None:
    pass
```

### describe_destinations

Type annotations for `boto3.client("logs").describe_destinations` method.

[Client.describe_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_destinations)

```python
def describe_destinations(
    self,
    DestinationNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None
) -> DescribeDestinationsResponseTypeDef:
    pass
```

### describe_export_tasks

Type annotations for `boto3.client("logs").describe_export_tasks` method.

[Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks)

```python
def describe_export_tasks(
    self,
    taskId: str = None,
    statusCode: ExportTaskStatusCode = None,
    nextToken: str = None,
    limit: int = None
) -> DescribeExportTasksResponseTypeDef:
    pass
```

### describe_log_groups

Type annotations for `boto3.client("logs").describe_log_groups` method.

[Client.describe_log_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups)

```python
def describe_log_groups(
    self,
    logGroupNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None
) -> DescribeLogGroupsResponseTypeDef:
    pass
```

### describe_log_streams

Type annotations for `boto3.client("logs").describe_log_streams` method.

[Client.describe_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams)

```python
def describe_log_streams(
    self,
    logGroupName: str,
    logStreamNamePrefix: str = None,
    orderBy: OrderBy = None,
    descending: bool = None,
    nextToken: str = None,
    limit: int = None
) -> DescribeLogStreamsResponseTypeDef:
    pass
```

### describe_metric_filters

Type annotations for `boto3.client("logs").describe_metric_filters` method.

[Client.describe_metric_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_metric_filters)

```python
def describe_metric_filters(
    self,
    logGroupName: str = None,
    filterNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None,
    metricName: str = None,
    metricNamespace: str = None
) -> DescribeMetricFiltersResponseTypeDef:
    pass
```

### describe_queries

Type annotations for `boto3.client("logs").describe_queries` method.

[Client.describe_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_queries)

```python
def describe_queries(
    self,
    logGroupName: str = None,
    status: QueryStatus = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeQueriesResponseTypeDef:
    pass
```

### describe_query_definitions

Type annotations for `boto3.client("logs").describe_query_definitions` method.

[Client.describe_query_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_query_definitions)

```python
def describe_query_definitions(
    self,
    queryDefinitionNamePrefix: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeQueryDefinitionsResponseTypeDef:
    pass
```

### describe_resource_policies

Type annotations for `boto3.client("logs").describe_resource_policies` method.

[Client.describe_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_resource_policies)

```python
def describe_resource_policies(
    self,
    nextToken: str = None,
    limit: int = None
) -> DescribeResourcePoliciesResponseTypeDef:
    pass
```

### describe_subscription_filters

Type annotations for `boto3.client("logs").describe_subscription_filters` method.

[Client.describe_subscription_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.describe_subscription_filters)

```python
def describe_subscription_filters(
    self,
    logGroupName: str,
    filterNamePrefix: str = None,
    nextToken: str = None,
    limit: int = None
) -> DescribeSubscriptionFiltersResponseTypeDef:
    pass
```

### disassociate_kms_key

Type annotations for `boto3.client("logs").disassociate_kms_key` method.

[Client.disassociate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.disassociate_kms_key)

```python
def disassociate_kms_key(
    self,
    logGroupName: str
) -> None:
    pass
```

### filter_log_events

Type annotations for `boto3.client("logs").filter_log_events` method.

[Client.filter_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events)

```python
def filter_log_events(
    self,
    logGroupName: str,
    logStreamNames: List[str] = None,
    logStreamNamePrefix: str = None,
    startTime: int = None,
    endTime: int = None,
    filterPattern: str = None,
    nextToken: str = None,
    limit: int = None,
    interleaved: bool = None
) -> FilterLogEventsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("logs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.generate_presigned_url)

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

### get_log_events

Type annotations for `boto3.client("logs").get_log_events` method.

[Client.get_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.get_log_events)

```python
def get_log_events(
    self,
    logGroupName: str,
    logStreamName: str,
    startTime: int = None,
    endTime: int = None,
    nextToken: str = None,
    limit: int = None,
    startFromHead: bool = None
) -> GetLogEventsResponseTypeDef:
    pass
```

### get_log_group_fields

Type annotations for `boto3.client("logs").get_log_group_fields` method.

[Client.get_log_group_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.get_log_group_fields)

```python
def get_log_group_fields(
    self,
    logGroupName: str,
    time: int = None
) -> GetLogGroupFieldsResponseTypeDef:
    pass
```

### get_log_record

Type annotations for `boto3.client("logs").get_log_record` method.

[Client.get_log_record documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.get_log_record)

```python
def get_log_record(
    self,
    logRecordPointer: str
) -> GetLogRecordResponseTypeDef:
    pass
```

### get_query_results

Type annotations for `boto3.client("logs").get_query_results` method.

[Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.get_query_results)

```python
def get_query_results(
    self,
    queryId: str
) -> GetQueryResultsResponseTypeDef:
    pass
```

### list_tags_log_group

Type annotations for `boto3.client("logs").list_tags_log_group` method.

[Client.list_tags_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.list_tags_log_group)

```python
def list_tags_log_group(
    self,
    logGroupName: str
) -> ListTagsLogGroupResponseTypeDef:
    pass
```

### put_destination

Type annotations for `boto3.client("logs").put_destination` method.

[Client.put_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_destination)

```python
def put_destination(
    self,
    destinationName: str,
    targetArn: str,
    roleArn: str
) -> PutDestinationResponseTypeDef:
    pass
```

### put_destination_policy

Type annotations for `boto3.client("logs").put_destination_policy` method.

[Client.put_destination_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_destination_policy)

```python
def put_destination_policy(
    self,
    destinationName: str,
    accessPolicy: str
) -> None:
    pass
```

### put_log_events

Type annotations for `boto3.client("logs").put_log_events` method.

[Client.put_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_log_events)

```python
def put_log_events(
    self,
    logGroupName: str,
    logStreamName: str,
    logEvents: List[InputLogEventTypeDef],
    sequenceToken: str = None
) -> PutLogEventsResponseTypeDef:
    pass
```

### put_metric_filter

Type annotations for `boto3.client("logs").put_metric_filter` method.

[Client.put_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_metric_filter)

```python
def put_metric_filter(
    self,
    logGroupName: str,
    filterName: str,
    filterPattern: str,
    metricTransformations: List["MetricTransformationTypeDef"]
) -> None:
    pass
```

### put_query_definition

Type annotations for `boto3.client("logs").put_query_definition` method.

[Client.put_query_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_query_definition)

```python
def put_query_definition(
    self,
    name: str,
    queryString: str,
    queryDefinitionId: str = None,
    logGroupNames: List[str] = None
) -> PutQueryDefinitionResponseTypeDef:
    pass
```

### put_resource_policy

Type annotations for `boto3.client("logs").put_resource_policy` method.

[Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_resource_policy)

```python
def put_resource_policy(
    self,
    policyName: str = None,
    policyDocument: str = None
) -> PutResourcePolicyResponseTypeDef:
    pass
```

### put_retention_policy

Type annotations for `boto3.client("logs").put_retention_policy` method.

[Client.put_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_retention_policy)

```python
def put_retention_policy(
    self,
    logGroupName: str,
    retentionInDays: int
) -> None:
    pass
```

### put_subscription_filter

Type annotations for `boto3.client("logs").put_subscription_filter` method.

[Client.put_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter)

```python
def put_subscription_filter(
    self,
    logGroupName: str,
    filterName: str,
    filterPattern: str,
    destinationArn: str,
    roleArn: str = None,
    distribution: Distribution = None
) -> None:
    pass
```

### start_query

Type annotations for `boto3.client("logs").start_query` method.

[Client.start_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.start_query)

```python
def start_query(
    self,
    startTime: int,
    endTime: int,
    queryString: str,
    logGroupName: str = None,
    logGroupNames: List[str] = None,
    limit: int = None
) -> StartQueryResponseTypeDef:
    pass
```

### stop_query

Type annotations for `boto3.client("logs").stop_query` method.

[Client.stop_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.stop_query)

```python
def stop_query(
    self,
    queryId: str
) -> StopQueryResponseTypeDef:
    pass
```

### tag_log_group

Type annotations for `boto3.client("logs").tag_log_group` method.

[Client.tag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.tag_log_group)

```python
def tag_log_group(
    self,
    logGroupName: str,
    tags: Dict[str, str]
) -> None:
    pass
```

### test_metric_filter

Type annotations for `boto3.client("logs").test_metric_filter` method.

[Client.test_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.test_metric_filter)

```python
def test_metric_filter(
    self,
    filterPattern: str,
    logEventMessages: List[str]
) -> TestMetricFilterResponseTypeDef:
    pass
```

### untag_log_group

Type annotations for `boto3.client("logs").untag_log_group` method.

[Client.untag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Client.untag_log_group)

```python
def untag_log_group(
    self,
    logGroupName: str,
    tags: List[str]
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDestinationsPaginatorName
) -> DescribeDestinationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeExportTasksPaginatorName
) -> DescribeExportTasksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeLogGroupsPaginatorName
) -> DescribeLogGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeLogStreamsPaginatorName
) -> DescribeLogStreamsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMetricFiltersPaginatorName
) -> DescribeMetricFiltersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeQueriesPaginatorName
) -> DescribeQueriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeResourcePoliciesPaginatorName
) -> DescribeResourcePoliciesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSubscriptionFiltersPaginatorName
) -> DescribeSubscriptionFiltersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("logs").get_paginator` method.

[Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: FilterLogEventsPaginatorName
) -> FilterLogEventsPaginator:
    pass
```