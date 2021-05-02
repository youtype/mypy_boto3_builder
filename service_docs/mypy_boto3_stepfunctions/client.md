# SFNClient for boto3 SFN module

> [Index](../index.md) > [SFN](./index.md) > SFNClient

Auto-generated documentation for [SFN](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN)
type annotations stubs module [mypy_boto3_stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/).

- [SFNClient for boto3 SFN module](#sfnclient-for-boto3-sfn-module)
  - [SFNClient](#sfnclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_activity](#create_activity)
    - [create_state_machine](#create_state_machine)
    - [delete_activity](#delete_activity)
    - [delete_state_machine](#delete_state_machine)
    - [describe_activity](#describe_activity)
    - [describe_execution](#describe_execution)
    - [describe_state_machine](#describe_state_machine)
    - [describe_state_machine_for_execution](#describe_state_machine_for_execution)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_activity_task](#get_activity_task)
    - [get_execution_history](#get_execution_history)
    - [list_activities](#list_activities)
    - [list_executions](#list_executions)
    - [list_state_machines](#list_state_machines)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [send_task_failure](#send_task_failure)
    - [send_task_heartbeat](#send_task_heartbeat)
    - [send_task_success](#send_task_success)
    - [start_execution](#start_execution)
    - [start_sync_execution](#start_sync_execution)
    - [stop_execution](#stop_execution)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_state_machine](#update_state_machine)
    - [get_paginator](#get_paginator)

## SFNClient

Type annotations for `boto3.client("stepfunctions")`

Can be used directly:

```python
from mypy_boto3_stepfunctions.client import SFNClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_stepfunctions.client import Exceptions

def handle_error(exc: Exceptions.ActivityDoesNotExist) -> None:
    ...
```


Exceptions:

- `Exceptions.ActivityDoesNotExist`
- `Exceptions.ActivityLimitExceeded`
- `Exceptions.ActivityWorkerLimitExceeded`
- `Exceptions.ClientError`
- `Exceptions.ExecutionAlreadyExists`
- `Exceptions.ExecutionDoesNotExist`
- `Exceptions.ExecutionLimitExceeded`
- `Exceptions.InvalidArn`
- `Exceptions.InvalidDefinition`
- `Exceptions.InvalidExecutionInput`
- `Exceptions.InvalidLoggingConfiguration`
- `Exceptions.InvalidName`
- `Exceptions.InvalidOutput`
- `Exceptions.InvalidToken`
- `Exceptions.InvalidTracingConfiguration`
- `Exceptions.MissingRequiredParameter`
- `Exceptions.ResourceNotFound`
- `Exceptions.StateMachineAlreadyExists`
- `Exceptions.StateMachineDeleting`
- `Exceptions.StateMachineDoesNotExist`
- `Exceptions.StateMachineLimitExceeded`
- `Exceptions.StateMachineTypeNotSupported`
- `Exceptions.TaskDoesNotExist`
- `Exceptions.TaskTimedOut`
- `Exceptions.TooManyTags`


## Methods


### can_paginate

Type annotations for `boto3.client("stepfunctions").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_activity

Type annotations for `boto3.client("stepfunctions").create_activity` method.

[Client.create_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.create_activity)

```python
def create_activity(
    self,
    name: str,
    tags: List["TagTypeDef"] = None
) -> CreateActivityOutputTypeDef:
    pass
```

### create_state_machine

Type annotations for `boto3.client("stepfunctions").create_state_machine` method.

[Client.create_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.create_state_machine)

```python
def create_state_machine(
    self,
    name: str,
    definition: str,
    roleArn: str,
    type: StateMachineType = None,
    loggingConfiguration: "LoggingConfigurationTypeDef" = None,
    tags: List["TagTypeDef"] = None,
    tracingConfiguration: "TracingConfigurationTypeDef" = None
) -> CreateStateMachineOutputTypeDef:
    pass
```

### delete_activity

Type annotations for `boto3.client("stepfunctions").delete_activity` method.

[Client.delete_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.delete_activity)

```python
def delete_activity(
    self,
    activityArn: str
) -> Dict[str, Any]:
    pass
```

### delete_state_machine

Type annotations for `boto3.client("stepfunctions").delete_state_machine` method.

[Client.delete_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)

```python
def delete_state_machine(
    self,
    stateMachineArn: str
) -> Dict[str, Any]:
    pass
```

### describe_activity

Type annotations for `boto3.client("stepfunctions").describe_activity` method.

[Client.describe_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_activity)

```python
def describe_activity(
    self,
    activityArn: str
) -> DescribeActivityOutputTypeDef:
    pass
```

### describe_execution

Type annotations for `boto3.client("stepfunctions").describe_execution` method.

[Client.describe_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_execution)

```python
def describe_execution(
    self,
    executionArn: str
) -> DescribeExecutionOutputTypeDef:
    pass
```

### describe_state_machine

Type annotations for `boto3.client("stepfunctions").describe_state_machine` method.

[Client.describe_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)

```python
def describe_state_machine(
    self,
    stateMachineArn: str
) -> DescribeStateMachineOutputTypeDef:
    pass
```

### describe_state_machine_for_execution

Type annotations for `boto3.client("stepfunctions").describe_state_machine_for_execution` method.

[Client.describe_state_machine_for_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)

```python
def describe_state_machine_for_execution(
    self,
    executionArn: str
) -> DescribeStateMachineForExecutionOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("stepfunctions").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)

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

### get_activity_task

Type annotations for `boto3.client("stepfunctions").get_activity_task` method.

[Client.get_activity_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_activity_task)

```python
def get_activity_task(
    self,
    activityArn: str,
    workerName: str = None
) -> GetActivityTaskOutputTypeDef:
    pass
```

### get_execution_history

Type annotations for `boto3.client("stepfunctions").get_execution_history` method.

[Client.get_execution_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_execution_history)

```python
def get_execution_history(
    self,
    executionArn: str,
    maxResults: int = None,
    reverseOrder: bool = None,
    nextToken: str = None,
    includeExecutionData: bool = None
) -> GetExecutionHistoryOutputTypeDef:
    pass
```

### list_activities

Type annotations for `boto3.client("stepfunctions").list_activities` method.

[Client.list_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_activities)

```python
def list_activities(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListActivitiesOutputTypeDef:
    pass
```

### list_executions

Type annotations for `boto3.client("stepfunctions").list_executions` method.

[Client.list_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_executions)

```python
def list_executions(
    self,
    stateMachineArn: str,
    statusFilter: ExecutionStatus = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListExecutionsOutputTypeDef:
    pass
```

### list_state_machines

Type annotations for `boto3.client("stepfunctions").list_state_machines` method.

[Client.list_state_machines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_state_machines)

```python
def list_state_machines(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListStateMachinesOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("stepfunctions").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### send_task_failure

Type annotations for `boto3.client("stepfunctions").send_task_failure` method.

[Client.send_task_failure documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.send_task_failure)

```python
def send_task_failure(
    self,
    taskToken: str,
    error: str = None,
    cause: str = None
) -> Dict[str, Any]:
    pass
```

### send_task_heartbeat

Type annotations for `boto3.client("stepfunctions").send_task_heartbeat` method.

[Client.send_task_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)

```python
def send_task_heartbeat(
    self,
    taskToken: str
) -> Dict[str, Any]:
    pass
```

### send_task_success

Type annotations for `boto3.client("stepfunctions").send_task_success` method.

[Client.send_task_success documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.send_task_success)

```python
def send_task_success(
    self,
    taskToken: str,
    output: str
) -> Dict[str, Any]:
    pass
```

### start_execution

Type annotations for `boto3.client("stepfunctions").start_execution` method.

[Client.start_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.start_execution)

```python
def start_execution(
    self,
    stateMachineArn: str,
    name: str = None,
    input: str = None,
    traceHeader: str = None
) -> StartExecutionOutputTypeDef:
    pass
```

### start_sync_execution

Type annotations for `boto3.client("stepfunctions").start_sync_execution` method.

[Client.start_sync_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.start_sync_execution)

```python
def start_sync_execution(
    self,
    stateMachineArn: str,
    name: str = None,
    input: str = None,
    traceHeader: str = None
) -> StartSyncExecutionOutputTypeDef:
    pass
```

### stop_execution

Type annotations for `boto3.client("stepfunctions").stop_execution` method.

[Client.stop_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.stop_execution)

```python
def stop_execution(
    self,
    executionArn: str,
    error: str = None,
    cause: str = None
) -> StopExecutionOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("stepfunctions").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("stepfunctions").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_state_machine

Type annotations for `boto3.client("stepfunctions").update_state_machine` method.

[Client.update_state_machine documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.update_state_machine)

```python
def update_state_machine(
    self,
    stateMachineArn: str,
    definition: str = None,
    roleArn: str = None,
    loggingConfiguration: "LoggingConfigurationTypeDef" = None,
    tracingConfiguration: "TracingConfigurationTypeDef" = None
) -> UpdateStateMachineOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("stepfunctions").get_paginator` method with overloads.

- `client.get_paginator("get_execution_history")` -> [GetExecutionHistoryPaginator](./paginators.md#getexecutionhistorypaginator)
- `client.get_paginator("list_activities")` -> [ListActivitiesPaginator](./paginators.md#listactivitiespaginator)
- `client.get_paginator("list_executions")` -> [ListExecutionsPaginator](./paginators.md#listexecutionspaginator)
- `client.get_paginator("list_state_machines")` -> [ListStateMachinesPaginator](./paginators.md#liststatemachinespaginator)


