# Type annotations for boto3 Budgets module

> [Index](../index.md) > Budgets

Auto-generated documentation for [Budgets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html#Budgets)
type annotations stubs module [mypy_boto3_budgets](https://pypi.org/project/mypy-boto3-budgets/).

```bash
pip install mypy-boto3-budgets
```

- [Type annotations for boto3 Budgets module](#type-annotations-for-boto3-budgets-module)
  - [BudgetsClient](#budgetsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## BudgetsClient

Type annotations for  `boto3.client("budgets")` as [BudgetsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_budgets.client import BudgetsClient
```


BudgetsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_budget](./client.md#create-budget)
- [create_budget_action](./client.md#create-budget-action)
- [create_notification](./client.md#create-notification)
- [create_subscriber](./client.md#create-subscriber)
- [delete_budget](./client.md#delete-budget)
- [delete_budget_action](./client.md#delete-budget-action)
- [delete_notification](./client.md#delete-notification)
- [delete_subscriber](./client.md#delete-subscriber)
- [describe_budget](./client.md#describe-budget)
- [describe_budget_action](./client.md#describe-budget-action)
- [describe_budget_action_histories](./client.md#describe-budget-action-histories)
- [describe_budget_actions_for_account](./client.md#describe-budget-actions-for-account)
- [describe_budget_actions_for_budget](./client.md#describe-budget-actions-for-budget)
- [describe_budget_performance_history](./client.md#describe-budget-performance-history)
- [describe_budgets](./client.md#describe-budgets)
- [describe_notifications_for_budget](./client.md#describe-notifications-for-budget)
- [describe_subscribers_for_notification](./client.md#describe-subscribers-for-notification)
- [execute_budget_action](./client.md#execute-budget-action)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [update_budget](./client.md#update-budget)
- [update_budget_action](./client.md#update-budget-action)
- [update_notification](./client.md#update-notification)
- [update_subscriber](./client.md#update-subscriber)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [CreationLimitExceededException](./client.md#creationlimitexceededexception)
- [DuplicateRecordException](./client.md#duplicaterecordexception)
- [ExpiredNextTokenException](./client.md#expirednexttokenexception)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [NotFoundException](./client.md#notfoundexception)
- [ResourceLockedException](./client.md#resourcelockedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("budgets").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_budgets.paginators import DescribeBudgetActionHistoriesPaginator, ...
```

- [DescribeBudgetActionHistoriesPaginator](./paginators.md#describebudgetactionhistoriespaginator)
- [DescribeBudgetActionsForAccountPaginator](./paginators.md#describebudgetactionsforaccountpaginator)
- [DescribeBudgetActionsForBudgetPaginator](./paginators.md#describebudgetactionsforbudgetpaginator)
- [DescribeBudgetPerformanceHistoryPaginator](./paginators.md#describebudgetperformancehistorypaginator)
- [DescribeBudgetsPaginator](./paginators.md#describebudgetspaginator)
- [DescribeNotificationsForBudgetPaginator](./paginators.md#describenotificationsforbudgetpaginator)
- [DescribeSubscribersForNotificationPaginator](./paginators.md#describesubscribersfornotificationpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_budgets.literals import ActionStatus, ...
```

- [ActionStatus](./literals.md#actionstatus)
- [ActionSubType](./literals.md#actionsubtype)
- [ActionType](./literals.md#actiontype)
- [ApprovalModel](./literals.md#approvalmodel)
- [BudgetType](./literals.md#budgettype)
- [ComparisonOperator](./literals.md#comparisonoperator)
- [DescribeBudgetActionHistoriesPaginatorName](./literals.md#describebudgetactionhistoriespaginatorname)
- [DescribeBudgetActionsForAccountPaginatorName](./literals.md#describebudgetactionsforaccountpaginatorname)
- [DescribeBudgetActionsForBudgetPaginatorName](./literals.md#describebudgetactionsforbudgetpaginatorname)
- [DescribeBudgetPerformanceHistoryPaginatorName](./literals.md#describebudgetperformancehistorypaginatorname)
- [DescribeBudgetsPaginatorName](./literals.md#describebudgetspaginatorname)
- [DescribeNotificationsForBudgetPaginatorName](./literals.md#describenotificationsforbudgetpaginatorname)
- [DescribeSubscribersForNotificationPaginatorName](./literals.md#describesubscribersfornotificationpaginatorname)
- [EventType](./literals.md#eventtype)
- [ExecutionType](./literals.md#executiontype)
- [NotificationState](./literals.md#notificationstate)
- [NotificationType](./literals.md#notificationtype)
- [SubscriptionType](./literals.md#subscriptiontype)
- [ThresholdType](./literals.md#thresholdtype)
- [TimeUnit](./literals.md#timeunit)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef, ...
```

- [ActionHistoryDetailsTypeDef](./type_defs.md#actionhistorydetailstypedef)
- [ActionHistoryTypeDef](./type_defs.md#actionhistorytypedef)
- [ActionThresholdTypeDef](./type_defs.md#actionthresholdtypedef)
- [ActionTypeDef](./type_defs.md#actiontypedef)
- [BudgetPerformanceHistoryTypeDef](./type_defs.md#budgetperformancehistorytypedef)
- [BudgetTypeDef](./type_defs.md#budgettypedef)
- [BudgetedAndActualAmountsTypeDef](./type_defs.md#budgetedandactualamountstypedef)
- [CalculatedSpendTypeDef](./type_defs.md#calculatedspendtypedef)
- [CostTypesTypeDef](./type_defs.md#costtypestypedef)
- [DefinitionTypeDef](./type_defs.md#definitiontypedef)
- [IamActionDefinitionTypeDef](./type_defs.md#iamactiondefinitiontypedef)
- [NotificationTypeDef](./type_defs.md#notificationtypedef)
- [ScpActionDefinitionTypeDef](./type_defs.md#scpactiondefinitiontypedef)
- [SpendTypeDef](./type_defs.md#spendtypedef)
- [SsmActionDefinitionTypeDef](./type_defs.md#ssmactiondefinitiontypedef)
- [SubscriberTypeDef](./type_defs.md#subscribertypedef)
- [TimePeriodTypeDef](./type_defs.md#timeperiodtypedef)
- [CreateBudgetActionResponseTypeDef](./type_defs.md#createbudgetactionresponsetypedef)
- [DeleteBudgetActionResponseTypeDef](./type_defs.md#deletebudgetactionresponsetypedef)
- [DescribeBudgetActionHistoriesResponseTypeDef](./type_defs.md#describebudgetactionhistoriesresponsetypedef)
- [DescribeBudgetActionResponseTypeDef](./type_defs.md#describebudgetactionresponsetypedef)
- [DescribeBudgetActionsForAccountResponseTypeDef](./type_defs.md#describebudgetactionsforaccountresponsetypedef)
- [DescribeBudgetActionsForBudgetResponseTypeDef](./type_defs.md#describebudgetactionsforbudgetresponsetypedef)
- [DescribeBudgetPerformanceHistoryResponseTypeDef](./type_defs.md#describebudgetperformancehistoryresponsetypedef)
- [DescribeBudgetResponseTypeDef](./type_defs.md#describebudgetresponsetypedef)
- [DescribeBudgetsResponseTypeDef](./type_defs.md#describebudgetsresponsetypedef)
- [DescribeNotificationsForBudgetResponseTypeDef](./type_defs.md#describenotificationsforbudgetresponsetypedef)
- [DescribeSubscribersForNotificationResponseTypeDef](./type_defs.md#describesubscribersfornotificationresponsetypedef)
- [ExecuteBudgetActionResponseTypeDef](./type_defs.md#executebudgetactionresponsetypedef)
- [NotificationWithSubscribersTypeDef](./type_defs.md#notificationwithsubscriberstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateBudgetActionResponseTypeDef](./type_defs.md#updatebudgetactionresponsetypedef)
