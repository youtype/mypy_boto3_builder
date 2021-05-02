# Literals for boto3 Budgets module

> [Index](../index.md) > [Budgets](./index.md) > Literals

Auto-generated documentation for [Budgets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets)
type annotations stubs module [mypy_boto3_budgets](https://pypi.org/project/mypy-boto3-budgets/).

- [Literals for boto3 Budgets module](#literals-for-boto3-budgets-module)
  - [ActionStatus](#actionstatus)
  - [ActionSubType](#actionsubtype)
  - [ActionType](#actiontype)
  - [ApprovalModel](#approvalmodel)
  - [BudgetType](#budgettype)
  - [ComparisonOperator](#comparisonoperator)
  - [DescribeBudgetActionHistoriesPaginatorName](#describebudgetactionhistoriespaginatorname)
  - [DescribeBudgetActionsForAccountPaginatorName](#describebudgetactionsforaccountpaginatorname)
  - [DescribeBudgetActionsForBudgetPaginatorName](#describebudgetactionsforbudgetpaginatorname)
  - [DescribeBudgetPerformanceHistoryPaginatorName](#describebudgetperformancehistorypaginatorname)
  - [DescribeBudgetsPaginatorName](#describebudgetspaginatorname)
  - [DescribeNotificationsForBudgetPaginatorName](#describenotificationsforbudgetpaginatorname)
  - [DescribeSubscribersForNotificationPaginatorName](#describesubscribersfornotificationpaginatorname)
  - [EventType](#eventtype)
  - [ExecutionType](#executiontype)
  - [NotificationState](#notificationstate)
  - [NotificationType](#notificationtype)
  - [SubscriptionType](#subscriptiontype)
  - [ThresholdType](#thresholdtype)
  - [TimeUnit](#timeunit)

## ActionStatus

```python
from mypy_boto3_budgets.literals import ActionStatus
```

Values:

- `EXECUTION_FAILURE`
- `EXECUTION_IN_PROGRESS`
- `EXECUTION_SUCCESS`
- `PENDING`
- `RESET_FAILURE`
- `RESET_IN_PROGRESS`
- `REVERSE_FAILURE`
- `REVERSE_IN_PROGRESS`
- `REVERSE_SUCCESS`
- `STANDBY`

## ActionSubType

```python
from mypy_boto3_budgets.literals import ActionSubType
```

Values:

- `STOP_EC2_INSTANCES`
- `STOP_RDS_INSTANCES`

## ActionType

```python
from mypy_boto3_budgets.literals import ActionType
```

Values:

- `APPLY_IAM_POLICY`
- `APPLY_SCP_POLICY`
- `RUN_SSM_DOCUMENTS`

## ApprovalModel

```python
from mypy_boto3_budgets.literals import ApprovalModel
```

Values:

- `AUTOMATIC`
- `MANUAL`

## BudgetType

```python
from mypy_boto3_budgets.literals import BudgetType
```

Values:

- `COST`
- `RI_COVERAGE`
- `RI_UTILIZATION`
- `SAVINGS_PLANS_COVERAGE`
- `SAVINGS_PLANS_UTILIZATION`
- `USAGE`

## ComparisonOperator

```python
from mypy_boto3_budgets.literals import ComparisonOperator
```

Values:

- `EQUAL_TO`
- `GREATER_THAN`
- `LESS_THAN`

## DescribeBudgetActionHistoriesPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeBudgetActionHistoriesPaginatorName
```

Values:

- `describe_budget_action_histories`

## DescribeBudgetActionsForAccountPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeBudgetActionsForAccountPaginatorName
```

Values:

- `describe_budget_actions_for_account`

## DescribeBudgetActionsForBudgetPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeBudgetActionsForBudgetPaginatorName
```

Values:

- `describe_budget_actions_for_budget`

## DescribeBudgetPerformanceHistoryPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeBudgetPerformanceHistoryPaginatorName
```

Values:

- `describe_budget_performance_history`

## DescribeBudgetsPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeBudgetsPaginatorName
```

Values:

- `describe_budgets`

## DescribeNotificationsForBudgetPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeNotificationsForBudgetPaginatorName
```

Values:

- `describe_notifications_for_budget`

## DescribeSubscribersForNotificationPaginatorName

```python
from mypy_boto3_budgets.literals import DescribeSubscribersForNotificationPaginatorName
```

Values:

- `describe_subscribers_for_notification`

## EventType

```python
from mypy_boto3_budgets.literals import EventType
```

Values:

- `CREATE_ACTION`
- `DELETE_ACTION`
- `EXECUTE_ACTION`
- `SYSTEM`
- `UPDATE_ACTION`

## ExecutionType

```python
from mypy_boto3_budgets.literals import ExecutionType
```

Values:

- `APPROVE_BUDGET_ACTION`
- `RESET_BUDGET_ACTION`
- `RETRY_BUDGET_ACTION`
- `REVERSE_BUDGET_ACTION`

## NotificationState

```python
from mypy_boto3_budgets.literals import NotificationState
```

Values:

- `ALARM`
- `OK`

## NotificationType

```python
from mypy_boto3_budgets.literals import NotificationType
```

Values:

- `ACTUAL`
- `FORECASTED`

## SubscriptionType

```python
from mypy_boto3_budgets.literals import SubscriptionType
```

Values:

- `EMAIL`
- `SNS`

## ThresholdType

```python
from mypy_boto3_budgets.literals import ThresholdType
```

Values:

- `ABSOLUTE_VALUE`
- `PERCENTAGE`

## TimeUnit

```python
from mypy_boto3_budgets.literals import TimeUnit
```

Values:

- `ANNUALLY`
- `DAILY`
- `MONTHLY`
- `QUARTERLY`
