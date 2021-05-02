# BudgetsClient for boto3 Budgets module

> [Index](../index.md) > [Budgets](./index.md) > BudgetsClient

Auto-generated documentation for [Budgets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets)
type annotations stubs module [mypy_boto3_budgets](https://pypi.org/project/mypy-boto3-budgets/).

- [BudgetsClient for boto3 Budgets module](#budgetsclient-for-boto3-budgets-module)
  - [BudgetsClient](#budgetsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_budget](#create_budget)
    - [create_budget_action](#create_budget_action)
    - [create_notification](#create_notification)
    - [create_subscriber](#create_subscriber)
    - [delete_budget](#delete_budget)
    - [delete_budget_action](#delete_budget_action)
    - [delete_notification](#delete_notification)
    - [delete_subscriber](#delete_subscriber)
    - [describe_budget](#describe_budget)
    - [describe_budget_action](#describe_budget_action)
    - [describe_budget_action_histories](#describe_budget_action_histories)
    - [describe_budget_actions_for_account](#describe_budget_actions_for_account)
    - [describe_budget_actions_for_budget](#describe_budget_actions_for_budget)
    - [describe_budget_performance_history](#describe_budget_performance_history)
    - [describe_budgets](#describe_budgets)
    - [describe_notifications_for_budget](#describe_notifications_for_budget)
    - [describe_subscribers_for_notification](#describe_subscribers_for_notification)
    - [execute_budget_action](#execute_budget_action)
    - [generate_presigned_url](#generate_presigned_url)
    - [update_budget](#update_budget)
    - [update_budget_action](#update_budget_action)
    - [update_notification](#update_notification)
    - [update_subscriber](#update_subscriber)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## BudgetsClient

Type annotations for `boto3.client("budgets")`

Can be used directly:

```python
from mypy_boto3_budgets.client import BudgetsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_budgets.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.CreationLimitExceededException`
- `Exceptions.DuplicateRecordException`
- `Exceptions.ExpiredNextTokenException`
- `Exceptions.InternalErrorException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceLockedException`


## Methods


### can_paginate

Type annotations for `boto3.client("budgets").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_budget

Type annotations for `boto3.client("budgets").create_budget` method.

[Client.create_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.create_budget)

```python
def create_budget(
    self,
    AccountId: str,
    Budget: "BudgetTypeDef",
    NotificationsWithSubscribers: List[NotificationWithSubscribersTypeDef] = None
) -> Dict[str, Any]:
    pass
```

### create_budget_action

Type annotations for `boto3.client("budgets").create_budget_action` method.

[Client.create_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.create_budget_action)

```python
def create_budget_action(
    self,
    AccountId: str,
    BudgetName: str,
    NotificationType: NotificationType,
    ActionType: ActionType,
    ActionThreshold: "ActionThresholdTypeDef",
    Definition: "DefinitionTypeDef",
    ExecutionRoleArn: str,
    ApprovalModel: ApprovalModel,
    Subscribers: List["SubscriberTypeDef"]
) -> CreateBudgetActionResponseTypeDef:
    pass
```

### create_notification

Type annotations for `boto3.client("budgets").create_notification` method.

[Client.create_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.create_notification)

```python
def create_notification(
    self,
    AccountId: str,
    BudgetName: str,
    Notification: "NotificationTypeDef",
    Subscribers: List["SubscriberTypeDef"]
) -> Dict[str, Any]:
    pass
```

### create_subscriber

Type annotations for `boto3.client("budgets").create_subscriber` method.

[Client.create_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.create_subscriber)

```python
def create_subscriber(
    self,
    AccountId: str,
    BudgetName: str,
    Notification: "NotificationTypeDef",
    Subscriber: "SubscriberTypeDef"
) -> Dict[str, Any]:
    pass
```

### delete_budget

Type annotations for `boto3.client("budgets").delete_budget` method.

[Client.delete_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.delete_budget)

```python
def delete_budget(
    self,
    AccountId: str,
    BudgetName: str
) -> Dict[str, Any]:
    pass
```

### delete_budget_action

Type annotations for `boto3.client("budgets").delete_budget_action` method.

[Client.delete_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.delete_budget_action)

```python
def delete_budget_action(
    self,
    AccountId: str,
    BudgetName: str,
    ActionId: str
) -> DeleteBudgetActionResponseTypeDef:
    pass
```

### delete_notification

Type annotations for `boto3.client("budgets").delete_notification` method.

[Client.delete_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.delete_notification)

```python
def delete_notification(
    self,
    AccountId: str,
    BudgetName: str,
    Notification: "NotificationTypeDef"
) -> Dict[str, Any]:
    pass
```

### delete_subscriber

Type annotations for `boto3.client("budgets").delete_subscriber` method.

[Client.delete_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.delete_subscriber)

```python
def delete_subscriber(
    self,
    AccountId: str,
    BudgetName: str,
    Notification: "NotificationTypeDef",
    Subscriber: "SubscriberTypeDef"
) -> Dict[str, Any]:
    pass
```

### describe_budget

Type annotations for `boto3.client("budgets").describe_budget` method.

[Client.describe_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budget)

```python
def describe_budget(
    self,
    AccountId: str,
    BudgetName: str
) -> DescribeBudgetResponseTypeDef:
    pass
```

### describe_budget_action

Type annotations for `boto3.client("budgets").describe_budget_action` method.

[Client.describe_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budget_action)

```python
def describe_budget_action(
    self,
    AccountId: str,
    BudgetName: str,
    ActionId: str
) -> DescribeBudgetActionResponseTypeDef:
    pass
```

### describe_budget_action_histories

Type annotations for `boto3.client("budgets").describe_budget_action_histories` method.

[Client.describe_budget_action_histories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budget_action_histories)

```python
def describe_budget_action_histories(
    self,
    AccountId: str,
    BudgetName: str,
    ActionId: str,
    TimePeriod: "TimePeriodTypeDef" = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBudgetActionHistoriesResponseTypeDef:
    pass
```

### describe_budget_actions_for_account

Type annotations for `boto3.client("budgets").describe_budget_actions_for_account` method.

[Client.describe_budget_actions_for_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_account)

```python
def describe_budget_actions_for_account(
    self,
    AccountId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBudgetActionsForAccountResponseTypeDef:
    pass
```

### describe_budget_actions_for_budget

Type annotations for `boto3.client("budgets").describe_budget_actions_for_budget` method.

[Client.describe_budget_actions_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_budget)

```python
def describe_budget_actions_for_budget(
    self,
    AccountId: str,
    BudgetName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBudgetActionsForBudgetResponseTypeDef:
    pass
```

### describe_budget_performance_history

Type annotations for `boto3.client("budgets").describe_budget_performance_history` method.

[Client.describe_budget_performance_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)

```python
def describe_budget_performance_history(
    self,
    AccountId: str,
    BudgetName: str,
    TimePeriod: "TimePeriodTypeDef" = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBudgetPerformanceHistoryResponseTypeDef:
    pass
```

### describe_budgets

Type annotations for `boto3.client("budgets").describe_budgets` method.

[Client.describe_budgets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_budgets)

```python
def describe_budgets(
    self,
    AccountId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBudgetsResponseTypeDef:
    pass
```

### describe_notifications_for_budget

Type annotations for `boto3.client("budgets").describe_notifications_for_budget` method.

[Client.describe_notifications_for_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)

```python
def describe_notifications_for_budget(
    self,
    AccountId: str,
    BudgetName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeNotificationsForBudgetResponseTypeDef:
    pass
```

### describe_subscribers_for_notification

Type annotations for `boto3.client("budgets").describe_subscribers_for_notification` method.

[Client.describe_subscribers_for_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)

```python
def describe_subscribers_for_notification(
    self,
    AccountId: str,
    BudgetName: str,
    Notification: "NotificationTypeDef",
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeSubscribersForNotificationResponseTypeDef:
    pass
```

### execute_budget_action

Type annotations for `boto3.client("budgets").execute_budget_action` method.

[Client.execute_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.execute_budget_action)

```python
def execute_budget_action(
    self,
    AccountId: str,
    BudgetName: str,
    ActionId: str,
    ExecutionType: ExecutionType
) -> ExecuteBudgetActionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("budgets").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.generate_presigned_url)

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

### update_budget

Type annotations for `boto3.client("budgets").update_budget` method.

[Client.update_budget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.update_budget)

```python
def update_budget(
    self,
    AccountId: str,
    NewBudget: "BudgetTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_budget_action

Type annotations for `boto3.client("budgets").update_budget_action` method.

[Client.update_budget_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.update_budget_action)

```python
def update_budget_action(
    self,
    AccountId: str,
    BudgetName: str,
    ActionId: str,
    NotificationType: NotificationType = None,
    ActionThreshold: "ActionThresholdTypeDef" = None,
    Definition: "DefinitionTypeDef" = None,
    ExecutionRoleArn: str = None,
    ApprovalModel: ApprovalModel = None,
    Subscribers: List["SubscriberTypeDef"] = None
) -> UpdateBudgetActionResponseTypeDef:
    pass
```

### update_notification

Type annotations for `boto3.client("budgets").update_notification` method.

[Client.update_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.update_notification)

```python
def update_notification(
    self,
    AccountId: str,
    BudgetName: str,
    OldNotification: "NotificationTypeDef",
    NewNotification: "NotificationTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_subscriber

Type annotations for `boto3.client("budgets").update_subscriber` method.

[Client.update_subscriber documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Client.update_subscriber)

```python
def update_subscriber(
    self,
    AccountId: str,
    BudgetName: str,
    Notification: "NotificationTypeDef",
    OldSubscriber: "SubscriberTypeDef",
    NewSubscriber: "SubscriberTypeDef"
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeBudgetActionHistories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBudgetActionHistoriesPaginatorName
) -> DescribeBudgetActionHistoriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeBudgetActionsForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBudgetActionsForAccountPaginatorName
) -> DescribeBudgetActionsForAccountPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeBudgetActionsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBudgetActionsForBudgetPaginatorName
) -> DescribeBudgetActionsForBudgetPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeBudgetPerformanceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBudgetPerformanceHistoryPaginatorName
) -> DescribeBudgetPerformanceHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBudgetsPaginatorName
) -> DescribeBudgetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeNotificationsForBudgetPaginatorName
) -> DescribeNotificationsForBudgetPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("budgets").get_paginator` method.

[Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSubscribersForNotificationPaginatorName
) -> DescribeSubscribersForNotificationPaginator:
    pass
```