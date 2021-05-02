# CodeStarNotificationsClient for boto3 CodeStarNotifications module

> [Index](../index.md) > [CodeStarNotifications](./index.md) > CodeStarNotificationsClient

Auto-generated documentation for [CodeStarNotifications](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications)
type annotations stubs module [mypy_boto3_codestar_notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/).

- [CodeStarNotificationsClient for boto3 CodeStarNotifications module](#codestarnotificationsclient-for-boto3-codestarnotifications-module)
  - [CodeStarNotificationsClient](#codestarnotificationsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_notification_rule](#create_notification_rule)
    - [delete_notification_rule](#delete_notification_rule)
    - [delete_target](#delete_target)
    - [describe_notification_rule](#describe_notification_rule)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_event_types](#list_event_types)
    - [list_notification_rules](#list_notification_rules)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_targets](#list_targets)
    - [subscribe](#subscribe)
    - [tag_resource](#tag_resource)
    - [unsubscribe](#unsubscribe)
    - [untag_resource](#untag_resource)
    - [update_notification_rule](#update_notification_rule)
    - [get_paginator](#get_paginator)

## CodeStarNotificationsClient

Type annotations for `boto3.client("codestar-notifications")`

Can be used directly:

```python
from mypy_boto3_codestar_notifications.client import CodeStarNotificationsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codestar_notifications.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConfigurationException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("codestar-notifications").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_notification_rule

Type annotations for `boto3.client("codestar-notifications").create_notification_rule` method.

[Client.create_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.create_notification_rule)

```python
def create_notification_rule(
    self,
    Name: str,
    EventTypeIds: List[str],
    Resource: str,
    Targets: List[TargetTypeDef],
    DetailType: DetailType,
    ClientRequestToken: str = None,
    Tags: Dict[str, str] = None,
    Status: NotificationRuleStatus = None
) -> CreateNotificationRuleResultTypeDef:
    pass
```

### delete_notification_rule

Type annotations for `boto3.client("codestar-notifications").delete_notification_rule` method.

[Client.delete_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_notification_rule)

```python
def delete_notification_rule(
    self,
    Arn: str
) -> DeleteNotificationRuleResultTypeDef:
    pass
```

### delete_target

Type annotations for `boto3.client("codestar-notifications").delete_target` method.

[Client.delete_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_target)

```python
def delete_target(
    self,
    TargetAddress: str,
    ForceUnsubscribeAll: bool = None
) -> Dict[str, Any]:
    pass
```

### describe_notification_rule

Type annotations for `boto3.client("codestar-notifications").describe_notification_rule` method.

[Client.describe_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.describe_notification_rule)

```python
def describe_notification_rule(
    self,
    Arn: str
) -> DescribeNotificationRuleResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codestar-notifications").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.generate_presigned_url)

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

### list_event_types

Type annotations for `boto3.client("codestar-notifications").list_event_types` method.

[Client.list_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_event_types)

```python
def list_event_types(
    self,
    Filters: List[ListEventTypesFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEventTypesResultTypeDef:
    pass
```

### list_notification_rules

Type annotations for `boto3.client("codestar-notifications").list_notification_rules` method.

[Client.list_notification_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_notification_rules)

```python
def list_notification_rules(
    self,
    Filters: List[ListNotificationRulesFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListNotificationRulesResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("codestar-notifications").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    Arn: str
) -> ListTagsForResourceResultTypeDef:
    pass
```

### list_targets

Type annotations for `boto3.client("codestar-notifications").list_targets` method.

[Client.list_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_targets)

```python
def list_targets(
    self,
    Filters: List[ListTargetsFilterTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTargetsResultTypeDef:
    pass
```

### subscribe

Type annotations for `boto3.client("codestar-notifications").subscribe` method.

[Client.subscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.subscribe)

```python
def subscribe(
    self,
    Arn: str,
    Target: TargetTypeDef,
    ClientRequestToken: str = None
) -> SubscribeResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("codestar-notifications").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.tag_resource)

```python
def tag_resource(
    self,
    Arn: str,
    Tags: Dict[str, str]
) -> TagResourceResultTypeDef:
    pass
```

### unsubscribe

Type annotations for `boto3.client("codestar-notifications").unsubscribe` method.

[Client.unsubscribe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.unsubscribe)

```python
def unsubscribe(
    self,
    Arn: str,
    TargetAddress: str
) -> UnsubscribeResultTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("codestar-notifications").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.untag_resource)

```python
def untag_resource(
    self,
    Arn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_notification_rule

Type annotations for `boto3.client("codestar-notifications").update_notification_rule` method.

[Client.update_notification_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.update_notification_rule)

```python
def update_notification_rule(
    self,
    Arn: str,
    Name: str = None,
    Status: NotificationRuleStatus = None,
    EventTypeIds: List[str] = None,
    Targets: List[TargetTypeDef] = None,
    DetailType: DetailType = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("codestar-notifications").get_paginator` method with overloads.

- `client.get_paginator("list_event_types")` -> [ListEventTypesPaginator](./paginators.md#listeventtypespaginator)
- `client.get_paginator("list_notification_rules")` -> [ListNotificationRulesPaginator](./paginators.md#listnotificationrulespaginator)
- `client.get_paginator("list_targets")` -> [ListTargetsPaginator](./paginators.md#listtargetspaginator)


