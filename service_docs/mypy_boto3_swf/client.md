# SWFClient for boto3 SWF module

> [Index](../index.md) > [SWF](./index.md) > SWFClient

Auto-generated documentation for [SWF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF)
type annotations stubs module [mypy_boto3_swf](https://pypi.org/project/mypy-boto3-swf/).

- [SWFClient for boto3 SWF module](#swfclient-for-boto3-swf-module)
  - [SWFClient](#swfclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [count_closed_workflow_executions](#count_closed_workflow_executions)
    - [count_open_workflow_executions](#count_open_workflow_executions)
    - [count_pending_activity_tasks](#count_pending_activity_tasks)
    - [count_pending_decision_tasks](#count_pending_decision_tasks)
    - [deprecate_activity_type](#deprecate_activity_type)
    - [deprecate_domain](#deprecate_domain)
    - [deprecate_workflow_type](#deprecate_workflow_type)
    - [describe_activity_type](#describe_activity_type)
    - [describe_domain](#describe_domain)
    - [describe_workflow_execution](#describe_workflow_execution)
    - [describe_workflow_type](#describe_workflow_type)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_workflow_execution_history](#get_workflow_execution_history)
    - [list_activity_types](#list_activity_types)
    - [list_closed_workflow_executions](#list_closed_workflow_executions)
    - [list_domains](#list_domains)
    - [list_open_workflow_executions](#list_open_workflow_executions)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_workflow_types](#list_workflow_types)
    - [poll_for_activity_task](#poll_for_activity_task)
    - [poll_for_decision_task](#poll_for_decision_task)
    - [record_activity_task_heartbeat](#record_activity_task_heartbeat)
    - [register_activity_type](#register_activity_type)
    - [register_domain](#register_domain)
    - [register_workflow_type](#register_workflow_type)
    - [request_cancel_workflow_execution](#request_cancel_workflow_execution)
    - [respond_activity_task_canceled](#respond_activity_task_canceled)
    - [respond_activity_task_completed](#respond_activity_task_completed)
    - [respond_activity_task_failed](#respond_activity_task_failed)
    - [respond_decision_task_completed](#respond_decision_task_completed)
    - [signal_workflow_execution](#signal_workflow_execution)
    - [start_workflow_execution](#start_workflow_execution)
    - [tag_resource](#tag_resource)
    - [terminate_workflow_execution](#terminate_workflow_execution)
    - [undeprecate_activity_type](#undeprecate_activity_type)
    - [undeprecate_domain](#undeprecate_domain)
    - [undeprecate_workflow_type](#undeprecate_workflow_type)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)

## SWFClient

Type annotations for `boto3.client("swf")`

Can be used directly:

```python
from mypy_boto3_swf.client import SWFClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_swf.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DefaultUndefinedFault`
- `Exceptions.DomainAlreadyExistsFault`
- `Exceptions.DomainDeprecatedFault`
- `Exceptions.LimitExceededFault`
- `Exceptions.OperationNotPermittedFault`
- `Exceptions.TooManyTagsFault`
- `Exceptions.TypeAlreadyExistsFault`
- `Exceptions.TypeDeprecatedFault`
- `Exceptions.UnknownResourceFault`
- `Exceptions.WorkflowExecutionAlreadyStartedFault`


## Methods


### can_paginate

Type annotations for `boto3.client("swf").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### count_closed_workflow_executions

Type annotations for `boto3.client("swf").count_closed_workflow_executions` method.

[Client.count_closed_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.count_closed_workflow_executions)

```python
def count_closed_workflow_executions(
    self,
    domain: str,
    startTimeFilter: ExecutionTimeFilterTypeDef = None,
    closeTimeFilter: ExecutionTimeFilterTypeDef = None,
    executionFilter: WorkflowExecutionFilterTypeDef = None,
    typeFilter: WorkflowTypeFilterTypeDef = None,
    tagFilter: TagFilterTypeDef = None,
    closeStatusFilter: CloseStatusFilterTypeDef = None
) -> WorkflowExecutionCountTypeDef:
    pass
```

### count_open_workflow_executions

Type annotations for `boto3.client("swf").count_open_workflow_executions` method.

[Client.count_open_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.count_open_workflow_executions)

```python
def count_open_workflow_executions(
    self,
    domain: str,
    startTimeFilter: ExecutionTimeFilterTypeDef,
    typeFilter: WorkflowTypeFilterTypeDef = None,
    tagFilter: TagFilterTypeDef = None,
    executionFilter: WorkflowExecutionFilterTypeDef = None
) -> WorkflowExecutionCountTypeDef:
    pass
```

### count_pending_activity_tasks

Type annotations for `boto3.client("swf").count_pending_activity_tasks` method.

[Client.count_pending_activity_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.count_pending_activity_tasks)

```python
def count_pending_activity_tasks(
    self,
    domain: str,
    taskList: "TaskListTypeDef"
) -> PendingTaskCountTypeDef:
    pass
```

### count_pending_decision_tasks

Type annotations for `boto3.client("swf").count_pending_decision_tasks` method.

[Client.count_pending_decision_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.count_pending_decision_tasks)

```python
def count_pending_decision_tasks(
    self,
    domain: str,
    taskList: "TaskListTypeDef"
) -> PendingTaskCountTypeDef:
    pass
```

### deprecate_activity_type

Type annotations for `boto3.client("swf").deprecate_activity_type` method.

[Client.deprecate_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.deprecate_activity_type)

```python
def deprecate_activity_type(
    self,
    domain: str,
    activityType: "ActivityTypeTypeDef"
) -> None:
    pass
```

### deprecate_domain

Type annotations for `boto3.client("swf").deprecate_domain` method.

[Client.deprecate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.deprecate_domain)

```python
def deprecate_domain(
    self,
    name: str
) -> None:
    pass
```

### deprecate_workflow_type

Type annotations for `boto3.client("swf").deprecate_workflow_type` method.

[Client.deprecate_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.deprecate_workflow_type)

```python
def deprecate_workflow_type(
    self,
    domain: str,
    workflowType: "WorkflowTypeTypeDef"
) -> None:
    pass
```

### describe_activity_type

Type annotations for `boto3.client("swf").describe_activity_type` method.

[Client.describe_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.describe_activity_type)

```python
def describe_activity_type(
    self,
    domain: str,
    activityType: "ActivityTypeTypeDef"
) -> ActivityTypeDetailTypeDef:
    pass
```

### describe_domain

Type annotations for `boto3.client("swf").describe_domain` method.

[Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.describe_domain)

```python
def describe_domain(
    self,
    name: str
) -> DomainDetailTypeDef:
    pass
```

### describe_workflow_execution

Type annotations for `boto3.client("swf").describe_workflow_execution` method.

[Client.describe_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.describe_workflow_execution)

```python
def describe_workflow_execution(
    self,
    domain: str,
    execution: "WorkflowExecutionTypeDef"
) -> WorkflowExecutionDetailTypeDef:
    pass
```

### describe_workflow_type

Type annotations for `boto3.client("swf").describe_workflow_type` method.

[Client.describe_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.describe_workflow_type)

```python
def describe_workflow_type(
    self,
    domain: str,
    workflowType: "WorkflowTypeTypeDef"
) -> WorkflowTypeDetailTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("swf").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.generate_presigned_url)

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

### get_workflow_execution_history

Type annotations for `boto3.client("swf").get_workflow_execution_history` method.

[Client.get_workflow_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.get_workflow_execution_history)

```python
def get_workflow_execution_history(
    self,
    domain: str,
    execution: "WorkflowExecutionTypeDef",
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None
) -> HistoryTypeDef:
    pass
```

### list_activity_types

Type annotations for `boto3.client("swf").list_activity_types` method.

[Client.list_activity_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_activity_types)

```python
def list_activity_types(
    self,
    domain: str,
    registrationStatus: RegistrationStatus,
    name: str = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None
) -> ActivityTypeInfosTypeDef:
    pass
```

### list_closed_workflow_executions

Type annotations for `boto3.client("swf").list_closed_workflow_executions` method.

[Client.list_closed_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_closed_workflow_executions)

```python
def list_closed_workflow_executions(
    self,
    domain: str,
    startTimeFilter: ExecutionTimeFilterTypeDef = None,
    closeTimeFilter: ExecutionTimeFilterTypeDef = None,
    executionFilter: WorkflowExecutionFilterTypeDef = None,
    closeStatusFilter: CloseStatusFilterTypeDef = None,
    typeFilter: WorkflowTypeFilterTypeDef = None,
    tagFilter: TagFilterTypeDef = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None
) -> WorkflowExecutionInfosTypeDef:
    pass
```

### list_domains

Type annotations for `boto3.client("swf").list_domains` method.

[Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_domains)

```python
def list_domains(
    self,
    registrationStatus: RegistrationStatus,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None
) -> DomainInfosTypeDef:
    pass
```

### list_open_workflow_executions

Type annotations for `boto3.client("swf").list_open_workflow_executions` method.

[Client.list_open_workflow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_open_workflow_executions)

```python
def list_open_workflow_executions(
    self,
    domain: str,
    startTimeFilter: ExecutionTimeFilterTypeDef,
    typeFilter: WorkflowTypeFilterTypeDef = None,
    tagFilter: TagFilterTypeDef = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None,
    executionFilter: WorkflowExecutionFilterTypeDef = None
) -> WorkflowExecutionInfosTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("swf").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_workflow_types

Type annotations for `boto3.client("swf").list_workflow_types` method.

[Client.list_workflow_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.list_workflow_types)

```python
def list_workflow_types(
    self,
    domain: str,
    registrationStatus: RegistrationStatus,
    name: str = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None
) -> WorkflowTypeInfosTypeDef:
    pass
```

### poll_for_activity_task

Type annotations for `boto3.client("swf").poll_for_activity_task` method.

[Client.poll_for_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.poll_for_activity_task)

```python
def poll_for_activity_task(
    self,
    domain: str,
    taskList: "TaskListTypeDef",
    identity: str = None
) -> ActivityTaskTypeDef:
    pass
```

### poll_for_decision_task

Type annotations for `boto3.client("swf").poll_for_decision_task` method.

[Client.poll_for_decision_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.poll_for_decision_task)

```python
def poll_for_decision_task(
    self,
    domain: str,
    taskList: "TaskListTypeDef",
    identity: str = None,
    nextPageToken: str = None,
    maximumPageSize: int = None,
    reverseOrder: bool = None
) -> DecisionTaskTypeDef:
    pass
```

### record_activity_task_heartbeat

Type annotations for `boto3.client("swf").record_activity_task_heartbeat` method.

[Client.record_activity_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.record_activity_task_heartbeat)

```python
def record_activity_task_heartbeat(
    self,
    taskToken: str,
    details: str = None
) -> ActivityTaskStatusTypeDef:
    pass
```

### register_activity_type

Type annotations for `boto3.client("swf").register_activity_type` method.

[Client.register_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.register_activity_type)

```python
def register_activity_type(
    self,
    domain: str,
    name: str,
    version: str,
    description: str = None,
    defaultTaskStartToCloseTimeout: str = None,
    defaultTaskHeartbeatTimeout: str = None,
    defaultTaskList: "TaskListTypeDef" = None,
    defaultTaskPriority: str = None,
    defaultTaskScheduleToStartTimeout: str = None,
    defaultTaskScheduleToCloseTimeout: str = None
) -> None:
    pass
```

### register_domain

Type annotations for `boto3.client("swf").register_domain` method.

[Client.register_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.register_domain)

```python
def register_domain(
    self,
    name: str,
    workflowExecutionRetentionPeriodInDays: str,
    description: str = None,
    tags: List["ResourceTagTypeDef"] = None
) -> None:
    pass
```

### register_workflow_type

Type annotations for `boto3.client("swf").register_workflow_type` method.

[Client.register_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.register_workflow_type)

```python
def register_workflow_type(
    self,
    domain: str,
    name: str,
    version: str,
    description: str = None,
    defaultTaskStartToCloseTimeout: str = None,
    defaultExecutionStartToCloseTimeout: str = None,
    defaultTaskList: "TaskListTypeDef" = None,
    defaultTaskPriority: str = None,
    defaultChildPolicy: ChildPolicy = None,
    defaultLambdaRole: str = None
) -> None:
    pass
```

### request_cancel_workflow_execution

Type annotations for `boto3.client("swf").request_cancel_workflow_execution` method.

[Client.request_cancel_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.request_cancel_workflow_execution)

```python
def request_cancel_workflow_execution(
    self,
    domain: str,
    workflowId: str,
    runId: str = None
) -> None:
    pass
```

### respond_activity_task_canceled

Type annotations for `boto3.client("swf").respond_activity_task_canceled` method.

[Client.respond_activity_task_canceled documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.respond_activity_task_canceled)

```python
def respond_activity_task_canceled(
    self,
    taskToken: str,
    details: str = None
) -> None:
    pass
```

### respond_activity_task_completed

Type annotations for `boto3.client("swf").respond_activity_task_completed` method.

[Client.respond_activity_task_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.respond_activity_task_completed)

```python
def respond_activity_task_completed(
    self,
    taskToken: str,
    result: str = None
) -> None:
    pass
```

### respond_activity_task_failed

Type annotations for `boto3.client("swf").respond_activity_task_failed` method.

[Client.respond_activity_task_failed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.respond_activity_task_failed)

```python
def respond_activity_task_failed(
    self,
    taskToken: str,
    reason: str = None,
    details: str = None
) -> None:
    pass
```

### respond_decision_task_completed

Type annotations for `boto3.client("swf").respond_decision_task_completed` method.

[Client.respond_decision_task_completed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.respond_decision_task_completed)

```python
def respond_decision_task_completed(
    self,
    taskToken: str,
    decisions: List[DecisionTypeDef] = None,
    executionContext: str = None
) -> None:
    pass
```

### signal_workflow_execution

Type annotations for `boto3.client("swf").signal_workflow_execution` method.

[Client.signal_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.signal_workflow_execution)

```python
def signal_workflow_execution(
    self,
    domain: str,
    workflowId: str,
    signalName: str,
    runId: str = None,
    input: str = None
) -> None:
    pass
```

### start_workflow_execution

Type annotations for `boto3.client("swf").start_workflow_execution` method.

[Client.start_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.start_workflow_execution)

```python
def start_workflow_execution(
    self,
    domain: str,
    workflowId: str,
    workflowType: "WorkflowTypeTypeDef",
    taskList: "TaskListTypeDef" = None,
    taskPriority: str = None,
    input: str = None,
    executionStartToCloseTimeout: str = None,
    tagList: List[str] = None,
    taskStartToCloseTimeout: str = None,
    childPolicy: ChildPolicy = None,
    lambdaRole: str = None
) -> RunTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("swf").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["ResourceTagTypeDef"]
) -> None:
    pass
```

### terminate_workflow_execution

Type annotations for `boto3.client("swf").terminate_workflow_execution` method.

[Client.terminate_workflow_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.terminate_workflow_execution)

```python
def terminate_workflow_execution(
    self,
    domain: str,
    workflowId: str,
    runId: str = None,
    reason: str = None,
    details: str = None,
    childPolicy: ChildPolicy = None
) -> None:
    pass
```

### undeprecate_activity_type

Type annotations for `boto3.client("swf").undeprecate_activity_type` method.

[Client.undeprecate_activity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.undeprecate_activity_type)

```python
def undeprecate_activity_type(
    self,
    domain: str,
    activityType: "ActivityTypeTypeDef"
) -> None:
    pass
```

### undeprecate_domain

Type annotations for `boto3.client("swf").undeprecate_domain` method.

[Client.undeprecate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.undeprecate_domain)

```python
def undeprecate_domain(
    self,
    name: str
) -> None:
    pass
```

### undeprecate_workflow_type

Type annotations for `boto3.client("swf").undeprecate_workflow_type` method.

[Client.undeprecate_workflow_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.undeprecate_workflow_type)

```python
def undeprecate_workflow_type(
    self,
    domain: str,
    workflowType: "WorkflowTypeTypeDef"
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("swf").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.GetWorkflowExecutionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.GetWorkflowExecutionHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetWorkflowExecutionHistoryPaginatorName
) -> GetWorkflowExecutionHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.ListActivityTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListActivityTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListActivityTypesPaginatorName
) -> ListActivityTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.ListClosedWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListClosedWorkflowExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListClosedWorkflowExecutionsPaginatorName
) -> ListClosedWorkflowExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListDomains)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDomainsPaginatorName
) -> ListDomainsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.ListOpenWorkflowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListOpenWorkflowExecutions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOpenWorkflowExecutionsPaginatorName
) -> ListOpenWorkflowExecutionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.ListWorkflowTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.ListWorkflowTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListWorkflowTypesPaginatorName
) -> ListWorkflowTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("swf").get_paginator` method.

[Paginator.PollForDecisionTask documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF.Paginator.PollForDecisionTask)

```python
@overload
def get_paginator(
    self,
    operation_name: PollForDecisionTaskPaginatorName
) -> PollForDecisionTaskPaginator:
    pass
```