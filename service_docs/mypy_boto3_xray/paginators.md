# Paginators for boto3 XRay module

> [Index](../index.md) > [XRay](./index.md) > Paginators

Auto-generated documentation for [XRay](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay)
type annotations stubs module [mypy_boto3_xray](https://pypi.org/project/mypy-boto3-xray/).

- [Paginators for boto3 XRay module](#paginators-for-boto3-xray-module)
  - [BatchGetTracesPaginator](#batchgettracespaginator)
  - [GetGroupsPaginator](#getgroupspaginator)
  - [GetSamplingRulesPaginator](#getsamplingrulespaginator)
  - [GetSamplingStatisticSummariesPaginator](#getsamplingstatisticsummariespaginator)
  - [GetServiceGraphPaginator](#getservicegraphpaginator)
  - [GetTimeSeriesServiceStatisticsPaginator](#gettimeseriesservicestatisticspaginator)
  - [GetTraceGraphPaginator](#gettracegraphpaginator)
  - [GetTraceSummariesPaginator](#gettracesummariespaginator)

## BatchGetTracesPaginator

Type annotations for `boto3.client("xray").get_paginator("batch_get_traces")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import BatchGetTracesPaginator

def get_batch_get_traces_paginator() -> BatchGetTracesPaginator:
    return boto3.client("xray").get_paginator("batch_get_traces")
```

[Paginator.BatchGetTraces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.BatchGetTraces)

```python
class BatchGetTracesPaginator(Boto3Paginator):
    def paginate(
        self,
        TraceIds: List[str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[BatchGetTracesResultTypeDef]:
        pass
```
## GetGroupsPaginator

Type annotations for `boto3.client("xray").get_paginator("get_groups")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetGroupsPaginator

def get_get_groups_paginator() -> GetGroupsPaginator:
    return boto3.client("xray").get_paginator("get_groups")
```

[Paginator.GetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetGroups)

```python
class GetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetGroupsResultTypeDef]:
        pass
```
## GetSamplingRulesPaginator

Type annotations for `boto3.client("xray").get_paginator("get_sampling_rules")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetSamplingRulesPaginator

def get_get_sampling_rules_paginator() -> GetSamplingRulesPaginator:
    return boto3.client("xray").get_paginator("get_sampling_rules")
```

[Paginator.GetSamplingRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetSamplingRules)

```python
class GetSamplingRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSamplingRulesResultTypeDef]:
        pass
```
## GetSamplingStatisticSummariesPaginator

Type annotations for `boto3.client("xray").get_paginator("get_sampling_statistic_summaries")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetSamplingStatisticSummariesPaginator

def get_get_sampling_statistic_summaries_paginator() -> GetSamplingStatisticSummariesPaginator:
    return boto3.client("xray").get_paginator("get_sampling_statistic_summaries")
```

[Paginator.GetSamplingStatisticSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetSamplingStatisticSummaries)

```python
class GetSamplingStatisticSummariesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSamplingStatisticSummariesResultTypeDef]:
        pass
```
## GetServiceGraphPaginator

Type annotations for `boto3.client("xray").get_paginator("get_service_graph")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetServiceGraphPaginator

def get_get_service_graph_paginator() -> GetServiceGraphPaginator:
    return boto3.client("xray").get_paginator("get_service_graph")
```

[Paginator.GetServiceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetServiceGraph)

```python
class GetServiceGraphPaginator(Boto3Paginator):
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetServiceGraphResultTypeDef]:
        pass
```
## GetTimeSeriesServiceStatisticsPaginator

Type annotations for `boto3.client("xray").get_paginator("get_time_series_service_statistics")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetTimeSeriesServiceStatisticsPaginator

def get_get_time_series_service_statistics_paginator() -> GetTimeSeriesServiceStatisticsPaginator:
    return boto3.client("xray").get_paginator("get_time_series_service_statistics")
```

[Paginator.GetTimeSeriesServiceStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetTimeSeriesServiceStatistics)

```python
class GetTimeSeriesServiceStatisticsPaginator(Boto3Paginator):
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        GroupName: str = None,
        GroupARN: str = None,
        EntitySelectorExpression: str = None,
        Period: int = None,
        ForecastStatistics: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTimeSeriesServiceStatisticsResultTypeDef]:
        pass
```
## GetTraceGraphPaginator

Type annotations for `boto3.client("xray").get_paginator("get_trace_graph")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetTraceGraphPaginator

def get_get_trace_graph_paginator() -> GetTraceGraphPaginator:
    return boto3.client("xray").get_paginator("get_trace_graph")
```

[Paginator.GetTraceGraph documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetTraceGraph)

```python
class GetTraceGraphPaginator(Boto3Paginator):
    def paginate(
        self,
        TraceIds: List[str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTraceGraphResultTypeDef]:
        pass
```
## GetTraceSummariesPaginator

Type annotations for `boto3.client("xray").get_paginator("get_trace_summaries")`.

Can be used directly:

```python
from mypy_boto3_xray.paginators import GetTraceSummariesPaginator

def get_get_trace_summaries_paginator() -> GetTraceSummariesPaginator:
    return boto3.client("xray").get_paginator("get_trace_summaries")
```

[Paginator.GetTraceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Paginator.GetTraceSummaries)

```python
class GetTraceSummariesPaginator(Boto3Paginator):
    def paginate(
        self,
        StartTime: datetime,
        EndTime: datetime,
        TimeRangeType: TimeRangeType = None,
        Sampling: bool = None,
        SamplingStrategy: SamplingStrategyTypeDef = None,
        FilterExpression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTraceSummariesResultTypeDef]:
        pass
```