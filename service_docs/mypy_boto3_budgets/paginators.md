# Paginators for boto3 Budgets module

> [Index](../index.md) > [Budgets](./index.md) > Paginators

Auto-generated documentation for [Budgets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets)
type annotations stubs module [mypy_boto3_budgets](https://pypi.org/project/mypy-boto3-budgets/).

- [Paginators for boto3 Budgets module](#paginators-for-boto3-budgets-module)
  - [DescribeBudgetActionHistoriesPaginator](#describebudgetactionhistoriespaginator)
  - [DescribeBudgetActionsForAccountPaginator](#describebudgetactionsforaccountpaginator)
  - [DescribeBudgetActionsForBudgetPaginator](#describebudgetactionsforbudgetpaginator)
  - [DescribeBudgetPerformanceHistoryPaginator](#describebudgetperformancehistorypaginator)
  - [DescribeBudgetsPaginator](#describebudgetspaginator)
  - [DescribeNotificationsForBudgetPaginator](#describenotificationsforbudgetpaginator)
  - [DescribeSubscribersForNotificationPaginator](#describesubscribersfornotificationpaginator)

## DescribeBudgetActionHistoriesPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_budget_action_histories")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeBudgetActionHistoriesPaginator

def get_describe_budget_action_histories_paginator() -> DescribeBudgetActionHistoriesPaginator:
    return boto3.client("budgets").get_paginator("describe_budget_action_histories")
```

[Paginator.DescribeBudgetActionHistories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories)

```python
class DescribeBudgetActionHistoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetActionHistoriesResponseTypeDef]:
        pass
```
## DescribeBudgetActionsForAccountPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_budget_actions_for_account")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeBudgetActionsForAccountPaginator

def get_describe_budget_actions_for_account_paginator() -> DescribeBudgetActionsForAccountPaginator:
    return boto3.client("budgets").get_paginator("describe_budget_actions_for_account")
```

[Paginator.DescribeBudgetActionsForAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount)

```python
class DescribeBudgetActionsForAccountPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetActionsForAccountResponseTypeDef]:
        pass
```
## DescribeBudgetActionsForBudgetPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_budget_actions_for_budget")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeBudgetActionsForBudgetPaginator

def get_describe_budget_actions_for_budget_paginator() -> DescribeBudgetActionsForBudgetPaginator:
    return boto3.client("budgets").get_paginator("describe_budget_actions_for_budget")
```

[Paginator.DescribeBudgetActionsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget)

```python
class DescribeBudgetActionsForBudgetPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetActionsForBudgetResponseTypeDef]:
        pass
```
## DescribeBudgetPerformanceHistoryPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_budget_performance_history")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeBudgetPerformanceHistoryPaginator

def get_describe_budget_performance_history_paginator() -> DescribeBudgetPerformanceHistoryPaginator:
    return boto3.client("budgets").get_paginator("describe_budget_performance_history")
```

[Paginator.DescribeBudgetPerformanceHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)

```python
class DescribeBudgetPerformanceHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetPerformanceHistoryResponseTypeDef]:
        pass
```
## DescribeBudgetsPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_budgets")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeBudgetsPaginator

def get_describe_budgets_paginator() -> DescribeBudgetsPaginator:
    return boto3.client("budgets").get_paginator("describe_budgets")
```

[Paginator.DescribeBudgets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)

```python
class DescribeBudgetsPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBudgetsResponseTypeDef]:
        pass
```
## DescribeNotificationsForBudgetPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_notifications_for_budget")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeNotificationsForBudgetPaginator

def get_describe_notifications_for_budget_paginator() -> DescribeNotificationsForBudgetPaginator:
    return boto3.client("budgets").get_paginator("describe_notifications_for_budget")
```

[Paginator.DescribeNotificationsForBudget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)

```python
class DescribeNotificationsForBudgetPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNotificationsForBudgetResponseTypeDef]:
        pass
```
## DescribeSubscribersForNotificationPaginator

Type annotations for `boto3.client("budgets").get_paginator("describe_subscribers_for_notification")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeSubscribersForNotificationPaginator

def get_describe_subscribers_for_notification_paginator() -> DescribeSubscribersForNotificationPaginator:
    return boto3.client("budgets").get_paginator("describe_subscribers_for_notification")
```

[Paginator.DescribeSubscribersForNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)

```python
class DescribeSubscribersForNotificationPaginator(Boto3Paginator):
    def paginate(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubscribersForNotificationResponseTypeDef]:
        pass
```