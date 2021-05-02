# Paginators for boto3 CodeStarNotifications module

> [Index](../index.md) > [CodeStarNotifications](./index.md) > Paginators

Auto-generated documentation for [CodeStarNotifications](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications)
type annotations stubs module [mypy_boto3_codestar_notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/).

- [Paginators for boto3 CodeStarNotifications module](#paginators-for-boto3-codestarnotifications-module)
  - [ListEventTypesPaginator](#listeventtypespaginator)
  - [ListNotificationRulesPaginator](#listnotificationrulespaginator)
  - [ListTargetsPaginator](#listtargetspaginator)

## ListEventTypesPaginator

Type annotations for `boto3.client("codestar-notifications").get_paginator("list_event_types")`.

Can be used directly:

```python
from mypy_boto3_codestar_notifications.paginators import ListEventTypesPaginator

def get_list_event_types_paginator() -> ListEventTypesPaginator:
    return boto3.client("codestar-notifications").get_paginator("list_event_types")
```

[Paginator.ListEventTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes)

```python
class ListEventTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ListEventTypesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventTypesResultTypeDef]:
        pass
```
## ListNotificationRulesPaginator

Type annotations for `boto3.client("codestar-notifications").get_paginator("list_notification_rules")`.

Can be used directly:

```python
from mypy_boto3_codestar_notifications.paginators import ListNotificationRulesPaginator

def get_list_notification_rules_paginator() -> ListNotificationRulesPaginator:
    return boto3.client("codestar-notifications").get_paginator("list_notification_rules")
```

[Paginator.ListNotificationRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules)

```python
class ListNotificationRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ListNotificationRulesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationRulesResultTypeDef]:
        pass
```
## ListTargetsPaginator

Type annotations for `boto3.client("codestar-notifications").get_paginator("list_targets")`.

Can be used directly:

```python
from mypy_boto3_codestar_notifications.paginators import ListTargetsPaginator

def get_list_targets_paginator() -> ListTargetsPaginator:
    return boto3.client("codestar-notifications").get_paginator("list_targets")
```

[Paginator.ListTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets)

```python
class ListTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ListTargetsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsResultTypeDef]:
        pass
```