# Paginators for boto3 SFN module

> [Index](../index.md) > [SFN](./index.md) > Paginators

Auto-generated documentation for [SFN](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN)
type annotations stubs module [mypy_boto3_stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/).

- [Paginators for boto3 SFN module](#paginators-for-boto3-sfn-module)
  - [GetExecutionHistoryPaginator](#getexecutionhistorypaginator)
  - [ListActivitiesPaginator](#listactivitiespaginator)
  - [ListExecutionsPaginator](#listexecutionspaginator)
  - [ListStateMachinesPaginator](#liststatemachinespaginator)

## GetExecutionHistoryPaginator

Type annotations for `boto3.client("stepfunctions").get_paginator("get_execution_history")`.

Can be used directly:

```python
from mypy_boto3_stepfunctions.paginators import GetExecutionHistoryPaginator

def get_get_execution_history_paginator() -> GetExecutionHistoryPaginator:
    return boto3.client("stepfunctions").get_paginator("get_execution_history")
```

[Paginator.GetExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Paginator.GetExecutionHistory)

```python
class GetExecutionHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        executionArn: str,
        reverseOrder: bool = None,
        includeExecutionData: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetExecutionHistoryOutputTypeDef]:
        pass
```
## ListActivitiesPaginator

Type annotations for `boto3.client("stepfunctions").get_paginator("list_activities")`.

Can be used directly:

```python
from mypy_boto3_stepfunctions.paginators import ListActivitiesPaginator

def get_list_activities_paginator() -> ListActivitiesPaginator:
    return boto3.client("stepfunctions").get_paginator("list_activities")
```

[Paginator.ListActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Paginator.ListActivities)

```python
class ListActivitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActivitiesOutputTypeDef]:
        pass
```
## ListExecutionsPaginator

Type annotations for `boto3.client("stepfunctions").get_paginator("list_executions")`.

Can be used directly:

```python
from mypy_boto3_stepfunctions.paginators import ListExecutionsPaginator

def get_list_executions_paginator() -> ListExecutionsPaginator:
    return boto3.client("stepfunctions").get_paginator("list_executions")
```

[Paginator.ListExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Paginator.ListExecutions)

```python
class ListExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        stateMachineArn: str,
        statusFilter: ExecutionStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExecutionsOutputTypeDef]:
        pass
```
## ListStateMachinesPaginator

Type annotations for `boto3.client("stepfunctions").get_paginator("list_state_machines")`.

Can be used directly:

```python
from mypy_boto3_stepfunctions.paginators import ListStateMachinesPaginator

def get_list_state_machines_paginator() -> ListStateMachinesPaginator:
    return boto3.client("stepfunctions").get_paginator("list_state_machines")
```

[Paginator.ListStateMachines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Paginator.ListStateMachines)

```python
class ListStateMachinesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStateMachinesOutputTypeDef]:
        pass
```