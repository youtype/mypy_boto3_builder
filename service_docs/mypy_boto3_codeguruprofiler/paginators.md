# Paginators for boto3 CodeGuruProfiler module

> [Index](../index.md) > [CodeGuruProfiler](./index.md) > Paginators

Auto-generated documentation for [CodeGuruProfiler](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler)
type annotations stubs module [mypy_boto3_codeguruprofiler](https://pypi.org/project/mypy-boto3-codeguruprofiler/).

- [Paginators for boto3 CodeGuruProfiler module](#paginators-for-boto3-codeguruprofiler-module)
  - [ListProfileTimesPaginator](#listprofiletimespaginator)

## ListProfileTimesPaginator

Type annotations for `boto3.client("codeguruprofiler").get_paginator("list_profile_times")`.

Can be used directly:

```python
from mypy_boto3_codeguruprofiler.paginators import ListProfileTimesPaginator

def get_list_profile_times_paginator() -> ListProfileTimesPaginator:
    return boto3.client("codeguruprofiler").get_paginator("list_profile_times")
```

[Paginator.ListProfileTimes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html#CodeGuruProfiler.Paginator.ListProfileTimes)

```python
class ListProfileTimesPaginator(Boto3Paginator):
    def paginate(
        self,
        endTime: datetime,
        period: AggregationPeriod,
        profilingGroupName: str,
        startTime: datetime,
        orderBy: OrderBy = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProfileTimesResponseTypeDef]:
        pass
```