# Paginators for boto3 CloudWatchLogs module

> [Index](../index.md) > [CloudWatchLogs](./index.md) > Paginators

Auto-generated documentation for [CloudWatchLogs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs)
type annotations stubs module [mypy_boto3_logs](https://pypi.org/project/mypy-boto3-logs/).

- [Paginators for boto3 CloudWatchLogs module](#paginators-for-boto3-cloudwatchlogs-module)
  - [DescribeDestinationsPaginator](#describedestinationspaginator)
  - [DescribeExportTasksPaginator](#describeexporttaskspaginator)
  - [DescribeLogGroupsPaginator](#describeloggroupspaginator)
  - [DescribeLogStreamsPaginator](#describelogstreamspaginator)
  - [DescribeMetricFiltersPaginator](#describemetricfilterspaginator)
  - [DescribeQueriesPaginator](#describequeriespaginator)
  - [DescribeResourcePoliciesPaginator](#describeresourcepoliciespaginator)
  - [DescribeSubscriptionFiltersPaginator](#describesubscriptionfilterspaginator)
  - [FilterLogEventsPaginator](#filterlogeventspaginator)

## DescribeDestinationsPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_destinations")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeDestinationsPaginator

def get_describe_destinations_paginator() -> DescribeDestinationsPaginator:
    return boto3.client("logs").get_paginator("describe_destinations")
```

[Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)

```python
class DescribeDestinationsPaginator(Boto3Paginator):
    def paginate(
        self,
        DestinationNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDestinationsResponseTypeDef]:
        pass
```
## DescribeExportTasksPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_export_tasks")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeExportTasksPaginator

def get_describe_export_tasks_paginator() -> DescribeExportTasksPaginator:
    return boto3.client("logs").get_paginator("describe_export_tasks")
```

[Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)

```python
class DescribeExportTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        taskId: str = None,
        statusCode: ExportTaskStatusCode = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportTasksResponseTypeDef]:
        pass
```
## DescribeLogGroupsPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_log_groups")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeLogGroupsPaginator

def get_describe_log_groups_paginator() -> DescribeLogGroupsPaginator:
    return boto3.client("logs").get_paginator("describe_log_groups")
```

[Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)

```python
class DescribeLogGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        logGroupNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLogGroupsResponseTypeDef]:
        pass
```
## DescribeLogStreamsPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_log_streams")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeLogStreamsPaginator

def get_describe_log_streams_paginator() -> DescribeLogStreamsPaginator:
    return boto3.client("logs").get_paginator("describe_log_streams")
```

[Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)

```python
class DescribeLogStreamsPaginator(Boto3Paginator):
    def paginate(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: OrderBy = None,
        descending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLogStreamsResponseTypeDef]:
        pass
```
## DescribeMetricFiltersPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_metric_filters")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeMetricFiltersPaginator

def get_describe_metric_filters_paginator() -> DescribeMetricFiltersPaginator:
    return boto3.client("logs").get_paginator("describe_metric_filters")
```

[Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)

```python
class DescribeMetricFiltersPaginator(Boto3Paginator):
    def paginate(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        metricName: str = None,
        metricNamespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMetricFiltersResponseTypeDef]:
        pass
```
## DescribeQueriesPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_queries")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeQueriesPaginator

def get_describe_queries_paginator() -> DescribeQueriesPaginator:
    return boto3.client("logs").get_paginator("describe_queries")
```

[Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)

```python
class DescribeQueriesPaginator(Boto3Paginator):
    def paginate(
        self,
        logGroupName: str = None,
        status: QueryStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeQueriesResponseTypeDef]:
        pass
```
## DescribeResourcePoliciesPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_resource_policies")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeResourcePoliciesPaginator

def get_describe_resource_policies_paginator() -> DescribeResourcePoliciesPaginator:
    return boto3.client("logs").get_paginator("describe_resource_policies")
```

[Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)

```python
class DescribeResourcePoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourcePoliciesResponseTypeDef]:
        pass
```
## DescribeSubscriptionFiltersPaginator

Type annotations for `boto3.client("logs").get_paginator("describe_subscription_filters")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeSubscriptionFiltersPaginator

def get_describe_subscription_filters_paginator() -> DescribeSubscriptionFiltersPaginator:
    return boto3.client("logs").get_paginator("describe_subscription_filters")
```

[Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)

```python
class DescribeSubscriptionFiltersPaginator(Boto3Paginator):
    def paginate(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubscriptionFiltersResponseTypeDef]:
        pass
```
## FilterLogEventsPaginator

Type annotations for `boto3.client("logs").get_paginator("filter_log_events")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import FilterLogEventsPaginator

def get_filter_log_events_paginator() -> FilterLogEventsPaginator:
    return boto3.client("logs").get_paginator("filter_log_events")
```

[Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)

```python
class FilterLogEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        interleaved: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[FilterLogEventsResponseTypeDef]:
        pass
```