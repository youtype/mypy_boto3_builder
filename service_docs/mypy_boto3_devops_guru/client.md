# DevopsGuruClient for boto3 DevopsGuru module

> [Index](../index.md) > [DevopsGuru](./index.md) > DevopsGuruClient

Auto-generated documentation for [DevopsGuru](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru)
type annotations stubs module [mypy_boto3_devops_guru](https://pypi.org/project/mypy-boto3-devops-guru/).

- [DevopsGuruClient for boto3 DevopsGuru module](#devopsguruclient-for-boto3-devopsguru-module)
  - [DevopsGuruClient](#devopsguruclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_notification_channel](#add_notification_channel)
    - [can_paginate](#can_paginate)
    - [describe_account_health](#describe_account_health)
    - [describe_account_overview](#describe_account_overview)
    - [describe_anomaly](#describe_anomaly)
    - [describe_feedback](#describe_feedback)
    - [describe_insight](#describe_insight)
    - [describe_resource_collection_health](#describe_resource_collection_health)
    - [describe_service_integration](#describe_service_integration)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_resource_collection](#get_resource_collection)
    - [list_anomalies_for_insight](#list_anomalies_for_insight)
    - [list_events](#list_events)
    - [list_insights](#list_insights)
    - [list_notification_channels](#list_notification_channels)
    - [list_recommendations](#list_recommendations)
    - [put_feedback](#put_feedback)
    - [remove_notification_channel](#remove_notification_channel)
    - [search_insights](#search_insights)
    - [update_resource_collection](#update_resource_collection)
    - [update_service_integration](#update_service_integration)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)

## DevopsGuruClient

Type annotations for `boto3.client("devops-guru")`

Can be used directly:

```python
from mypy_boto3_devops_guru.client import DevopsGuruClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_devops_guru.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### add_notification_channel

Type annotations for `boto3.client("devops-guru").add_notification_channel` method.

[Client.add_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.add_notification_channel)

```python
def add_notification_channel(
    self,
    Config: "NotificationChannelConfigTypeDef"
) -> AddNotificationChannelResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("devops-guru").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_account_health

Type annotations for `boto3.client("devops-guru").describe_account_health` method.

[Client.describe_account_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_account_health)

```python
def describe_account_health(
    self
) -> DescribeAccountHealthResponseTypeDef:
    pass
```

### describe_account_overview

Type annotations for `boto3.client("devops-guru").describe_account_overview` method.

[Client.describe_account_overview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_account_overview)

```python
def describe_account_overview(
    self,
    FromTime: datetime,
    ToTime: datetime = None
) -> DescribeAccountOverviewResponseTypeDef:
    pass
```

### describe_anomaly

Type annotations for `boto3.client("devops-guru").describe_anomaly` method.

[Client.describe_anomaly documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_anomaly)

```python
def describe_anomaly(
    self,
    Id: str
) -> DescribeAnomalyResponseTypeDef:
    pass
```

### describe_feedback

Type annotations for `boto3.client("devops-guru").describe_feedback` method.

[Client.describe_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_feedback)

```python
def describe_feedback(
    self,
    InsightId: str = None
) -> DescribeFeedbackResponseTypeDef:
    pass
```

### describe_insight

Type annotations for `boto3.client("devops-guru").describe_insight` method.

[Client.describe_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_insight)

```python
def describe_insight(
    self,
    Id: str
) -> DescribeInsightResponseTypeDef:
    pass
```

### describe_resource_collection_health

Type annotations for `boto3.client("devops-guru").describe_resource_collection_health` method.

[Client.describe_resource_collection_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_resource_collection_health)

```python
def describe_resource_collection_health(
    self,
    ResourceCollectionType: ResourceCollectionType,
    NextToken: str = None
) -> DescribeResourceCollectionHealthResponseTypeDef:
    pass
```

### describe_service_integration

Type annotations for `boto3.client("devops-guru").describe_service_integration` method.

[Client.describe_service_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.describe_service_integration)

```python
def describe_service_integration(
    self
) -> DescribeServiceIntegrationResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("devops-guru").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.generate_presigned_url)

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

### get_resource_collection

Type annotations for `boto3.client("devops-guru").get_resource_collection` method.

[Client.get_resource_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.get_resource_collection)

```python
def get_resource_collection(
    self,
    ResourceCollectionType: ResourceCollectionType,
    NextToken: str = None
) -> GetResourceCollectionResponseTypeDef:
    pass
```

### list_anomalies_for_insight

Type annotations for `boto3.client("devops-guru").list_anomalies_for_insight` method.

[Client.list_anomalies_for_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.list_anomalies_for_insight)

```python
def list_anomalies_for_insight(
    self,
    InsightId: str,
    StartTimeRange: "StartTimeRangeTypeDef" = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAnomaliesForInsightResponseTypeDef:
    pass
```

### list_events

Type annotations for `boto3.client("devops-guru").list_events` method.

[Client.list_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.list_events)

```python
def list_events(
    self,
    Filters: ListEventsFiltersTypeDef,
    MaxResults: int = None,
    NextToken: str = None
) -> ListEventsResponseTypeDef:
    pass
```

### list_insights

Type annotations for `boto3.client("devops-guru").list_insights` method.

[Client.list_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.list_insights)

```python
def list_insights(
    self,
    StatusFilter: ListInsightsStatusFilterTypeDef,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInsightsResponseTypeDef:
    pass
```

### list_notification_channels

Type annotations for `boto3.client("devops-guru").list_notification_channels` method.

[Client.list_notification_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.list_notification_channels)

```python
def list_notification_channels(
    self,
    NextToken: str = None
) -> ListNotificationChannelsResponseTypeDef:
    pass
```

### list_recommendations

Type annotations for `boto3.client("devops-guru").list_recommendations` method.

[Client.list_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.list_recommendations)

```python
def list_recommendations(
    self,
    InsightId: str,
    NextToken: str = None
) -> ListRecommendationsResponseTypeDef:
    pass
```

### put_feedback

Type annotations for `boto3.client("devops-guru").put_feedback` method.

[Client.put_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.put_feedback)

```python
def put_feedback(
    self,
    InsightFeedback: "InsightFeedbackTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### remove_notification_channel

Type annotations for `boto3.client("devops-guru").remove_notification_channel` method.

[Client.remove_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.remove_notification_channel)

```python
def remove_notification_channel(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### search_insights

Type annotations for `boto3.client("devops-guru").search_insights` method.

[Client.search_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.search_insights)

```python
def search_insights(
    self,
    StartTimeRange: "StartTimeRangeTypeDef",
    Type: InsightType,
    Filters: SearchInsightsFiltersTypeDef = None,
    MaxResults: int = None,
    NextToken: str = None
) -> SearchInsightsResponseTypeDef:
    pass
```

### update_resource_collection

Type annotations for `boto3.client("devops-guru").update_resource_collection` method.

[Client.update_resource_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.update_resource_collection)

```python
def update_resource_collection(
    self,
    Action: UpdateResourceCollectionAction,
    ResourceCollection: UpdateResourceCollectionFilterTypeDef
) -> Dict[str, Any]:
    pass
```

### update_service_integration

Type annotations for `boto3.client("devops-guru").update_service_integration` method.

[Client.update_service_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Client.update_service_integration)

```python
def update_service_integration(
    self,
    ServiceIntegration: UpdateServiceIntegrationConfigTypeDef
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.DescribeResourceCollectionHealth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.DescribeResourceCollectionHealth)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeResourceCollectionHealthPaginatorName
) -> DescribeResourceCollectionHealthPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.GetResourceCollection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.GetResourceCollection)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourceCollectionPaginatorName
) -> GetResourceCollectionPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.ListAnomaliesForInsight documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListAnomaliesForInsight)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAnomaliesForInsightPaginatorName
) -> ListAnomaliesForInsightPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.ListEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: ListEventsPaginatorName
) -> ListEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.ListInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListInsights)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInsightsPaginatorName
) -> ListInsightsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.ListNotificationChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListNotificationChannels)

```python
@overload
def get_paginator(
    self,
    operation_name: ListNotificationChannelsPaginatorName
) -> ListNotificationChannelsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.ListRecommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.ListRecommendations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListRecommendationsPaginatorName
) -> ListRecommendationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("devops-guru").get_paginator` method.

[Paginator.SearchInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevopsGuru.Paginator.SearchInsights)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchInsightsPaginatorName
) -> SearchInsightsPaginator:
    pass
```