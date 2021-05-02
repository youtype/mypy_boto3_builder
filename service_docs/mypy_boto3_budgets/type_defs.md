# Structures for boto3 Budgets module

> [Index](../index.md) > [Budgets](./index.md) > Structures

Auto-generated documentation for [Budgets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets)
type annotations stubs module [mypy_boto3_budgets](https://pypi.org/project/mypy-boto3-budgets/).

- [Structures for boto3 Budgets module](#structures-for-boto3-budgets-module)
  - [ActionHistoryDetailsTypeDef](#actionhistorydetailstypedef)
  - [ActionHistoryTypeDef](#actionhistorytypedef)
  - [ActionThresholdTypeDef](#actionthresholdtypedef)
  - [ActionTypeDef](#actiontypedef)
  - [BudgetPerformanceHistoryTypeDef](#budgetperformancehistorytypedef)
  - [BudgetTypeDef](#budgettypedef)
  - [BudgetedAndActualAmountsTypeDef](#budgetedandactualamountstypedef)
  - [CalculatedSpendTypeDef](#calculatedspendtypedef)
  - [CostTypesTypeDef](#costtypestypedef)
  - [CreateBudgetActionResponseTypeDef](#createbudgetactionresponsetypedef)
  - [DefinitionTypeDef](#definitiontypedef)
  - [DeleteBudgetActionResponseTypeDef](#deletebudgetactionresponsetypedef)
  - [DescribeBudgetActionHistoriesResponseTypeDef](#describebudgetactionhistoriesresponsetypedef)
  - [DescribeBudgetActionResponseTypeDef](#describebudgetactionresponsetypedef)
  - [DescribeBudgetActionsForAccountResponseTypeDef](#describebudgetactionsforaccountresponsetypedef)
  - [DescribeBudgetActionsForBudgetResponseTypeDef](#describebudgetactionsforbudgetresponsetypedef)
  - [DescribeBudgetPerformanceHistoryResponseTypeDef](#describebudgetperformancehistoryresponsetypedef)
  - [DescribeBudgetResponseTypeDef](#describebudgetresponsetypedef)
  - [DescribeBudgetsResponseTypeDef](#describebudgetsresponsetypedef)
  - [DescribeNotificationsForBudgetResponseTypeDef](#describenotificationsforbudgetresponsetypedef)
  - [DescribeSubscribersForNotificationResponseTypeDef](#describesubscribersfornotificationresponsetypedef)
  - [ExecuteBudgetActionResponseTypeDef](#executebudgetactionresponsetypedef)
  - [IamActionDefinitionTypeDef](#iamactiondefinitiontypedef)
  - [NotificationTypeDef](#notificationtypedef)
  - [NotificationWithSubscribersTypeDef](#notificationwithsubscriberstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ScpActionDefinitionTypeDef](#scpactiondefinitiontypedef)
  - [SpendTypeDef](#spendtypedef)
  - [SsmActionDefinitionTypeDef](#ssmactiondefinitiontypedef)
  - [SubscriberTypeDef](#subscribertypedef)
  - [TimePeriodTypeDef](#timeperiodtypedef)
  - [UpdateBudgetActionResponseTypeDef](#updatebudgetactionresponsetypedef)

## ActionHistoryDetailsTypeDef

```python
from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef
```


Required fields:
- `Message`: `str`
- `Action`: `"ActionTypeDef"`




## ActionHistoryTypeDef

```python
from mypy_boto3_budgets.type_defs import ActionHistoryTypeDef
```


Required fields:
- `Timestamp`: `datetime`
- `Status`: `ActionStatus`
- `EventType`: `EventType`
- `ActionHistoryDetails`: `"ActionHistoryDetailsTypeDef"`




## ActionThresholdTypeDef

```python
from mypy_boto3_budgets.type_defs import ActionThresholdTypeDef
```


Required fields:
- `ActionThresholdValue`: `float`
- `ActionThresholdType`: `ThresholdType`




## ActionTypeDef

```python
from mypy_boto3_budgets.type_defs import ActionTypeDef
```


Required fields:
- `ActionId`: `str`
- `BudgetName`: `str`
- `NotificationType`: `NotificationType`
- `ActionType`: `ActionType`
- `ActionThreshold`: `"ActionThresholdTypeDef"`
- `Definition`: `"DefinitionTypeDef"`
- `ExecutionRoleArn`: `str`
- `ApprovalModel`: `ApprovalModel`
- `Status`: `ActionStatus`
- `Subscribers`: `List["SubscriberTypeDef"]`




## BudgetPerformanceHistoryTypeDef

```python
from mypy_boto3_budgets.type_defs import BudgetPerformanceHistoryTypeDef
```




Optional fields:
- `BudgetName`: `str`
- `BudgetType`: `BudgetType`
- `CostFilters`: `Dict[str, List[str]]`
- `CostTypes`: `"CostTypesTypeDef"`
- `TimeUnit`: `TimeUnit`
- `BudgetedAndActualAmountsList`: `List["BudgetedAndActualAmountsTypeDef"]`


## BudgetTypeDef

```python
from mypy_boto3_budgets.type_defs import BudgetTypeDef
```


Required fields:
- `BudgetName`: `str`
- `TimeUnit`: `TimeUnit`
- `BudgetType`: `BudgetType`



Optional fields:
- `BudgetLimit`: `"SpendTypeDef"`
- `PlannedBudgetLimits`: `Dict[str, "SpendTypeDef"]`
- `CostFilters`: `Dict[str, List[str]]`
- `CostTypes`: `"CostTypesTypeDef"`
- `TimePeriod`: `"TimePeriodTypeDef"`
- `CalculatedSpend`: `"CalculatedSpendTypeDef"`
- `LastUpdatedTime`: `datetime`


## BudgetedAndActualAmountsTypeDef

```python
from mypy_boto3_budgets.type_defs import BudgetedAndActualAmountsTypeDef
```




Optional fields:
- `BudgetedAmount`: `"SpendTypeDef"`
- `ActualAmount`: `"SpendTypeDef"`
- `TimePeriod`: `"TimePeriodTypeDef"`


## CalculatedSpendTypeDef

```python
from mypy_boto3_budgets.type_defs import CalculatedSpendTypeDef
```


Required fields:
- `ActualSpend`: `"SpendTypeDef"`



Optional fields:
- `ForecastedSpend`: `"SpendTypeDef"`


## CostTypesTypeDef

```python
from mypy_boto3_budgets.type_defs import CostTypesTypeDef
```




Optional fields:
- `IncludeTax`: `bool`
- `IncludeSubscription`: `bool`
- `UseBlended`: `bool`
- `IncludeRefund`: `bool`
- `IncludeCredit`: `bool`
- `IncludeUpfront`: `bool`
- `IncludeRecurring`: `bool`
- `IncludeOtherSubscription`: `bool`
- `IncludeSupport`: `bool`
- `IncludeDiscount`: `bool`
- `UseAmortized`: `bool`


## CreateBudgetActionResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import CreateBudgetActionResponseTypeDef
```


Required fields:
- `AccountId`: `str`
- `BudgetName`: `str`
- `ActionId`: `str`




## DefinitionTypeDef

```python
from mypy_boto3_budgets.type_defs import DefinitionTypeDef
```




Optional fields:
- `IamActionDefinition`: `"IamActionDefinitionTypeDef"`
- `ScpActionDefinition`: `"ScpActionDefinitionTypeDef"`
- `SsmActionDefinition`: `"SsmActionDefinitionTypeDef"`


## DeleteBudgetActionResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DeleteBudgetActionResponseTypeDef
```


Required fields:
- `AccountId`: `str`
- `BudgetName`: `str`
- `Action`: `"ActionTypeDef"`




## DescribeBudgetActionHistoriesResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetActionHistoriesResponseTypeDef
```


Required fields:
- `ActionHistories`: `List["ActionHistoryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeBudgetActionResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetActionResponseTypeDef
```


Required fields:
- `AccountId`: `str`
- `BudgetName`: `str`
- `Action`: `"ActionTypeDef"`




## DescribeBudgetActionsForAccountResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetActionsForAccountResponseTypeDef
```


Required fields:
- `Actions`: `List["ActionTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeBudgetActionsForBudgetResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetActionsForBudgetResponseTypeDef
```


Required fields:
- `Actions`: `List["ActionTypeDef"]`



Optional fields:
- `NextToken`: `str`


## DescribeBudgetPerformanceHistoryResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetPerformanceHistoryResponseTypeDef
```




Optional fields:
- `BudgetPerformanceHistory`: `"BudgetPerformanceHistoryTypeDef"`
- `NextToken`: `str`


## DescribeBudgetResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetResponseTypeDef
```




Optional fields:
- `Budget`: `"BudgetTypeDef"`


## DescribeBudgetsResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeBudgetsResponseTypeDef
```




Optional fields:
- `Budgets`: `List["BudgetTypeDef"]`
- `NextToken`: `str`


## DescribeNotificationsForBudgetResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeNotificationsForBudgetResponseTypeDef
```




Optional fields:
- `Notifications`: `List["NotificationTypeDef"]`
- `NextToken`: `str`


## DescribeSubscribersForNotificationResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import DescribeSubscribersForNotificationResponseTypeDef
```




Optional fields:
- `Subscribers`: `List["SubscriberTypeDef"]`
- `NextToken`: `str`


## ExecuteBudgetActionResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import ExecuteBudgetActionResponseTypeDef
```


Required fields:
- `AccountId`: `str`
- `BudgetName`: `str`
- `ActionId`: `str`
- `ExecutionType`: `ExecutionType`




## IamActionDefinitionTypeDef

```python
from mypy_boto3_budgets.type_defs import IamActionDefinitionTypeDef
```


Required fields:
- `PolicyArn`: `str`



Optional fields:
- `Roles`: `List[str]`
- `Groups`: `List[str]`
- `Users`: `List[str]`


## NotificationTypeDef

```python
from mypy_boto3_budgets.type_defs import NotificationTypeDef
```


Required fields:
- `NotificationType`: `NotificationType`
- `ComparisonOperator`: `ComparisonOperator`
- `Threshold`: `float`



Optional fields:
- `ThresholdType`: `ThresholdType`
- `NotificationState`: `NotificationState`


## NotificationWithSubscribersTypeDef

```python
from mypy_boto3_budgets.type_defs import NotificationWithSubscribersTypeDef
```


Required fields:
- `Notification`: `"NotificationTypeDef"`
- `Subscribers`: `List["SubscriberTypeDef"]`




## PaginatorConfigTypeDef

```python
from mypy_boto3_budgets.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ScpActionDefinitionTypeDef

```python
from mypy_boto3_budgets.type_defs import ScpActionDefinitionTypeDef
```


Required fields:
- `PolicyId`: `str`
- `TargetIds`: `List[str]`




## SpendTypeDef

```python
from mypy_boto3_budgets.type_defs import SpendTypeDef
```


Required fields:
- `Amount`: `str`
- `Unit`: `str`




## SsmActionDefinitionTypeDef

```python
from mypy_boto3_budgets.type_defs import SsmActionDefinitionTypeDef
```


Required fields:
- `ActionSubType`: `ActionSubType`
- `Region`: `str`
- `InstanceIds`: `List[str]`




## SubscriberTypeDef

```python
from mypy_boto3_budgets.type_defs import SubscriberTypeDef
```


Required fields:
- `SubscriptionType`: `SubscriptionType`
- `Address`: `str`




## TimePeriodTypeDef

```python
from mypy_boto3_budgets.type_defs import TimePeriodTypeDef
```




Optional fields:
- `Start`: `datetime`
- `End`: `datetime`


## UpdateBudgetActionResponseTypeDef

```python
from mypy_boto3_budgets.type_defs import UpdateBudgetActionResponseTypeDef
```


Required fields:
- `AccountId`: `str`
- `BudgetName`: `str`
- `OldAction`: `"ActionTypeDef"`
- `NewAction`: `"ActionTypeDef"`



