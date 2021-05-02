# Paginators for boto3 SWF module

> [Index](../index.md) > [SWF](./index.md) > Paginators

Auto-generated documentation for [SWF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF)
type annotations stubs module [mypy_boto3_swf](https://pypi.org/project/mypy-boto3-swf/).

- [Paginators for boto3 SWF module](#paginators-for-boto3-swf-module)
  - [GetWorkflowExecutionHistoryPaginator](#getworkflowexecutionhistorypaginator)
  - [ListActivityTypesPaginator](#listactivitytypespaginator)
  - [ListClosedWorkflowExecutionsPaginator](#listclosedworkflowexecutionspaginator)
  - [ListDomainsPaginator](#listdomainspaginator)
  - [ListOpenWorkflowExecutionsPaginator](#listopenworkflowexecutionspaginator)
  - [ListWorkflowTypesPaginator](#listworkflowtypespaginator)
  - [PollForDecisionTaskPaginator](#pollfordecisiontaskpaginator)

## GetWorkflowExecutionHistoryPaginator

Type annotations for `boto3.client("swf").get_paginator("get_workflow_execution_history")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import GetWorkflowExecutionHistoryPaginator

def get_get_workflow_execution_history_paginator() -> GetWorkflowExecutionHistoryPaginator:
    return boto3.client("swf").get_paginator("get_workflow_execution_history")
```

[Paginator.GetWorkflowExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)

```python
class GetWorkflowExecutionHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        execution: "WorkflowExecutionTypeDef",
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[HistoryTypeDef]:
        pass
```
## ListActivityTypesPaginator

Type annotations for `boto3.client("swf").get_paginator("list_activity_types")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import ListActivityTypesPaginator

def get_list_activity_types_paginator() -> ListActivityTypesPaginator:
    return boto3.client("swf").get_paginator("list_activity_types")
```

[Paginator.ListActivityTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListActivityTypes)

```python
class ListActivityTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        registrationStatus: RegistrationStatus,
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ActivityTypeInfosTypeDef]:
        pass
```
## ListClosedWorkflowExecutionsPaginator

Type annotations for `boto3.client("swf").get_paginator("list_closed_workflow_executions")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import ListClosedWorkflowExecutionsPaginator

def get_list_closed_workflow_executions_paginator() -> ListClosedWorkflowExecutionsPaginator:
    return boto3.client("swf").get_paginator("list_closed_workflow_executions")
```

[Paginator.ListClosedWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)

```python
class ListClosedWorkflowExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef = None,
        closeTimeFilter: ExecutionTimeFilterTypeDef = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        closeStatusFilter: CloseStatusFilterTypeDef = None,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[WorkflowExecutionInfosTypeDef]:
        pass
```
## ListDomainsPaginator

Type annotations for `boto3.client("swf").get_paginator("list_domains")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import ListDomainsPaginator

def get_list_domains_paginator() -> ListDomainsPaginator:
    return boto3.client("swf").get_paginator("list_domains")
```

[Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListDomains)

```python
class ListDomainsPaginator(Boto3Paginator):
    def paginate(
        self,
        registrationStatus: RegistrationStatus,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DomainInfosTypeDef]:
        pass
```
## ListOpenWorkflowExecutionsPaginator

Type annotations for `boto3.client("swf").get_paginator("list_open_workflow_executions")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import ListOpenWorkflowExecutionsPaginator

def get_list_open_workflow_executions_paginator() -> ListOpenWorkflowExecutionsPaginator:
    return boto3.client("swf").get_paginator("list_open_workflow_executions")
```

[Paginator.ListOpenWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)

```python
class ListOpenWorkflowExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        startTimeFilter: ExecutionTimeFilterTypeDef,
        typeFilter: WorkflowTypeFilterTypeDef = None,
        tagFilter: TagFilterTypeDef = None,
        reverseOrder: bool = None,
        executionFilter: WorkflowExecutionFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[WorkflowExecutionInfosTypeDef]:
        pass
```
## ListWorkflowTypesPaginator

Type annotations for `boto3.client("swf").get_paginator("list_workflow_types")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import ListWorkflowTypesPaginator

def get_list_workflow_types_paginator() -> ListWorkflowTypesPaginator:
    return boto3.client("swf").get_paginator("list_workflow_types")
```

[Paginator.ListWorkflowTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)

```python
class ListWorkflowTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        registrationStatus: RegistrationStatus,
        name: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[WorkflowTypeInfosTypeDef]:
        pass
```
## PollForDecisionTaskPaginator

Type annotations for `boto3.client("swf").get_paginator("poll_for_decision_task")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import PollForDecisionTaskPaginator

def get_poll_for_decision_task_paginator() -> PollForDecisionTaskPaginator:
    return boto3.client("swf").get_paginator("poll_for_decision_task")
```

[Paginator.PollForDecisionTask documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)

```python
class PollForDecisionTaskPaginator(Boto3Paginator):
    def paginate(
        self,
        domain: str,
        taskList: "TaskListTypeDef",
        identity: str = None,
        reverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DecisionTaskTypeDef]:
        pass
```