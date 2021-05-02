# HealthClient for boto3 Health module

> [Index](../index.md) > [Health](./index.md) > HealthClient

Auto-generated documentation for [Health](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health)
type annotations stubs module [mypy_boto3_health](https://pypi.org/project/mypy-boto3-health/).

- [HealthClient for boto3 Health module](#healthclient-for-boto3-health-module)
  - [HealthClient](#healthclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_affected_accounts_for_organization](#describe_affected_accounts_for_organization)
    - [describe_affected_entities](#describe_affected_entities)
    - [describe_affected_entities_for_organization](#describe_affected_entities_for_organization)
    - [describe_entity_aggregates](#describe_entity_aggregates)
    - [describe_event_aggregates](#describe_event_aggregates)
    - [describe_event_details](#describe_event_details)
    - [describe_event_details_for_organization](#describe_event_details_for_organization)
    - [describe_event_types](#describe_event_types)
    - [describe_events](#describe_events)
    - [describe_events_for_organization](#describe_events_for_organization)
    - [describe_health_service_status_for_organization](#describe_health_service_status_for_organization)
    - [disable_health_service_access_for_organization](#disable_health_service_access_for_organization)
    - [enable_health_service_access_for_organization](#enable_health_service_access_for_organization)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## HealthClient

Type annotations for `boto3.client("health")`

Can be used directly:

```python
from mypy_boto3_health.client import HealthClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_health.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.InvalidPaginationToken`
- `Exceptions.UnsupportedLocale`


## Methods


### can_paginate

Type annotations for `boto3.client("health").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_affected_accounts_for_organization

Type annotations for `boto3.client("health").describe_affected_accounts_for_organization` method.

[Client.describe_affected_accounts_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_affected_accounts_for_organization)

```python
def describe_affected_accounts_for_organization(
    self,
    eventArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeAffectedAccountsForOrganizationResponseTypeDef:
    pass
```

### describe_affected_entities

Type annotations for `boto3.client("health").describe_affected_entities` method.

[Client.describe_affected_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_affected_entities)

```python
def describe_affected_entities(
    self,
    filter: EntityFilterTypeDef,
    locale: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeAffectedEntitiesResponseTypeDef:
    pass
```

### describe_affected_entities_for_organization

Type annotations for `boto3.client("health").describe_affected_entities_for_organization` method.

[Client.describe_affected_entities_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_affected_entities_for_organization)

```python
def describe_affected_entities_for_organization(
    self,
    organizationEntityFilters: List[EventAccountFilterTypeDef],
    locale: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeAffectedEntitiesForOrganizationResponseTypeDef:
    pass
```

### describe_entity_aggregates

Type annotations for `boto3.client("health").describe_entity_aggregates` method.

[Client.describe_entity_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_entity_aggregates)

```python
def describe_entity_aggregates(
    self,
    eventArns: List[str] = None
) -> DescribeEntityAggregatesResponseTypeDef:
    pass
```

### describe_event_aggregates

Type annotations for `boto3.client("health").describe_event_aggregates` method.

[Client.describe_event_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_event_aggregates)

```python
def describe_event_aggregates(
    self,
    aggregateField: eventAggregateField,
    filter: EventFilterTypeDef = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeEventAggregatesResponseTypeDef:
    pass
```

### describe_event_details

Type annotations for `boto3.client("health").describe_event_details` method.

[Client.describe_event_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_event_details)

```python
def describe_event_details(
    self,
    eventArns: List[str],
    locale: str = None
) -> DescribeEventDetailsResponseTypeDef:
    pass
```

### describe_event_details_for_organization

Type annotations for `boto3.client("health").describe_event_details_for_organization` method.

[Client.describe_event_details_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_event_details_for_organization)

```python
def describe_event_details_for_organization(
    self,
    organizationEventDetailFilters: List[EventAccountFilterTypeDef],
    locale: str = None
) -> DescribeEventDetailsForOrganizationResponseTypeDef:
    pass
```

### describe_event_types

Type annotations for `boto3.client("health").describe_event_types` method.

[Client.describe_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_event_types)

```python
def describe_event_types(
    self,
    filter: EventTypeFilterTypeDef = None,
    locale: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeEventTypesResponseTypeDef:
    pass
```

### describe_events

Type annotations for `boto3.client("health").describe_events` method.

[Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_events)

```python
def describe_events(
    self,
    filter: EventFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None,
    locale: str = None
) -> DescribeEventsResponseTypeDef:
    pass
```

### describe_events_for_organization

Type annotations for `boto3.client("health").describe_events_for_organization` method.

[Client.describe_events_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_events_for_organization)

```python
def describe_events_for_organization(
    self,
    filter: OrganizationEventFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None,
    locale: str = None
) -> DescribeEventsForOrganizationResponseTypeDef:
    pass
```

### describe_health_service_status_for_organization

Type annotations for `boto3.client("health").describe_health_service_status_for_organization` method.

[Client.describe_health_service_status_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.describe_health_service_status_for_organization)

```python
def describe_health_service_status_for_organization(
    self
) -> DescribeHealthServiceStatusForOrganizationResponseTypeDef:
    pass
```

### disable_health_service_access_for_organization

Type annotations for `boto3.client("health").disable_health_service_access_for_organization` method.

[Client.disable_health_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.disable_health_service_access_for_organization)

```python
def disable_health_service_access_for_organization(
    self
) -> None:
    pass
```

### enable_health_service_access_for_organization

Type annotations for `boto3.client("health").enable_health_service_access_for_organization` method.

[Client.enable_health_service_access_for_organization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.enable_health_service_access_for_organization)

```python
def enable_health_service_access_for_organization(
    self
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("health").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client.generate_presigned_url)

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

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeAffectedAccountsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeAffectedAccountsForOrganization)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAffectedAccountsForOrganizationPaginatorName
) -> DescribeAffectedAccountsForOrganizationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeAffectedEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeAffectedEntities)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAffectedEntitiesPaginatorName
) -> DescribeAffectedEntitiesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeAffectedEntitiesForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeAffectedEntitiesForOrganization)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAffectedEntitiesForOrganizationPaginatorName
) -> DescribeAffectedEntitiesForOrganizationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeEventAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeEventAggregates)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventAggregatesPaginatorName
) -> DescribeEventAggregatesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeEventTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventTypesPaginatorName
) -> DescribeEventTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsPaginatorName
) -> DescribeEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("health").get_paginator` method.

[Paginator.DescribeEventsForOrganization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Paginator.DescribeEventsForOrganization)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEventsForOrganizationPaginatorName
) -> DescribeEventsForOrganizationPaginator:
    pass
```