# Paginators for boto3 DevopsGuru module

> [Index](../index.md) > [DevopsGuru](./index.md) > Paginators

Auto-generated documentation for [DevopsGuru](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru)
type annotations stubs module [mypy_boto3_devops_guru](https://pypi.org/project/mypy-boto3-devops-guru/).

- [Paginators for boto3 DevopsGuru module](#paginators-for-boto3-devopsguru-module)
  - [DescribeResourceCollectionHealthPaginator](#describeresourcecollectionhealthpaginator)
  - [GetResourceCollectionPaginator](#getresourcecollectionpaginator)
  - [ListAnomaliesForInsightPaginator](#listanomaliesforinsightpaginator)
  - [ListEventsPaginator](#listeventspaginator)
  - [ListInsightsPaginator](#listinsightspaginator)
  - [ListNotificationChannelsPaginator](#listnotificationchannelspaginator)
  - [ListRecommendationsPaginator](#listrecommendationspaginator)
  - [SearchInsightsPaginator](#searchinsightspaginator)

## DescribeResourceCollectionHealthPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("describe_resource_collection_health")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import DescribeResourceCollectionHealthPaginator

def get_describe_resource_collection_health_paginator() -> DescribeResourceCollectionHealthPaginator:
    return boto3.client("devops-guru").get_paginator("describe_resource_collection_health")
```

[Paginator.DescribeResourceCollectionHealth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.DescribeResourceCollectionHealth)

```python
class DescribeResourceCollectionHealthPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceCollectionType: ResourceCollectionType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourceCollectionHealthResponseTypeDef]:
        pass
```
## GetResourceCollectionPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("get_resource_collection")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import GetResourceCollectionPaginator

def get_get_resource_collection_paginator() -> GetResourceCollectionPaginator:
    return boto3.client("devops-guru").get_paginator("get_resource_collection")
```

[Paginator.GetResourceCollection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.GetResourceCollection)

```python
class GetResourceCollectionPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceCollectionType: ResourceCollectionType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceCollectionResponseTypeDef]:
        pass
```
## ListAnomaliesForInsightPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("list_anomalies_for_insight")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import ListAnomaliesForInsightPaginator

def get_list_anomalies_for_insight_paginator() -> ListAnomaliesForInsightPaginator:
    return boto3.client("devops-guru").get_paginator("list_anomalies_for_insight")
```

[Paginator.ListAnomaliesForInsight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListAnomaliesForInsight)

```python
class ListAnomaliesForInsightPaginator(Boto3Paginator):
    def paginate(
        self,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnomaliesForInsightResponseTypeDef]:
        pass
```
## ListEventsPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("list_events")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import ListEventsPaginator

def get_list_events_paginator() -> ListEventsPaginator:
    return boto3.client("devops-guru").get_paginator("list_events")
```

[Paginator.ListEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListEvents)

```python
class ListEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: ListEventsFiltersTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventsResponseTypeDef]:
        pass
```
## ListInsightsPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("list_insights")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import ListInsightsPaginator

def get_list_insights_paginator() -> ListInsightsPaginator:
    return boto3.client("devops-guru").get_paginator("list_insights")
```

[Paginator.ListInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListInsights)

```python
class ListInsightsPaginator(Boto3Paginator):
    def paginate(
        self,
        StatusFilter: ListInsightsStatusFilterTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInsightsResponseTypeDef]:
        pass
```
## ListNotificationChannelsPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("list_notification_channels")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import ListNotificationChannelsPaginator

def get_list_notification_channels_paginator() -> ListNotificationChannelsPaginator:
    return boto3.client("devops-guru").get_paginator("list_notification_channels")
```

[Paginator.ListNotificationChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListNotificationChannels)

```python
class ListNotificationChannelsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationChannelsResponseTypeDef]:
        pass
```
## ListRecommendationsPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("list_recommendations")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import ListRecommendationsPaginator

def get_list_recommendations_paginator() -> ListRecommendationsPaginator:
    return boto3.client("devops-guru").get_paginator("list_recommendations")
```

[Paginator.ListRecommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListRecommendations)

```python
class ListRecommendationsPaginator(Boto3Paginator):
    def paginate(
        self,
        InsightId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        pass
```
## SearchInsightsPaginator

Type annotations for `boto3.client("devops-guru").get_paginator("search_insights")`.

Can be used directly:

```python
from mypy_boto3_devops_guru.paginators import SearchInsightsPaginator

def get_search_insights_paginator() -> SearchInsightsPaginator:
    return boto3.client("devops-guru").get_paginator("search_insights")
```

[Paginator.SearchInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.SearchInsights)

```python
class SearchInsightsPaginator(Boto3Paginator):
    def paginate(
        self,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightType,
        Filters: SearchInsightsFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchInsightsResponseTypeDef]:
        pass
```