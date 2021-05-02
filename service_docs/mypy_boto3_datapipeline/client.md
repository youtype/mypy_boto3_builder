# DataPipelineClient for boto3 DataPipeline module

> [Index](../index.md) > [DataPipeline](./index.md) > DataPipelineClient

Auto-generated documentation for [DataPipeline](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline)
type annotations stubs module [mypy_boto3_datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/).

- [DataPipelineClient for boto3 DataPipeline module](#datapipelineclient-for-boto3-datapipeline-module)
  - [DataPipelineClient](#datapipelineclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [activate_pipeline](#activate_pipeline)
    - [add_tags](#add_tags)
    - [can_paginate](#can_paginate)
    - [create_pipeline](#create_pipeline)
    - [deactivate_pipeline](#deactivate_pipeline)
    - [delete_pipeline](#delete_pipeline)
    - [describe_objects](#describe_objects)
    - [describe_pipelines](#describe_pipelines)
    - [evaluate_expression](#evaluate_expression)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_pipeline_definition](#get_pipeline_definition)
    - [list_pipelines](#list_pipelines)
    - [poll_for_task](#poll_for_task)
    - [put_pipeline_definition](#put_pipeline_definition)
    - [query_objects](#query_objects)
    - [remove_tags](#remove_tags)
    - [report_task_progress](#report_task_progress)
    - [report_task_runner_heartbeat](#report_task_runner_heartbeat)
    - [set_status](#set_status)
    - [set_task_status](#set_task_status)
    - [validate_pipeline_definition](#validate_pipeline_definition)
    - [get_paginator](#get_paginator)

## DataPipelineClient

Type annotations for `boto3.client("datapipeline")`

Can be used directly:

```python
from mypy_boto3_datapipeline.client import DataPipelineClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_datapipeline.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServiceError`
- `Exceptions.InvalidRequestException`
- `Exceptions.PipelineDeletedException`
- `Exceptions.PipelineNotFoundException`
- `Exceptions.TaskNotFoundException`


## Methods


### activate_pipeline

Type annotations for `boto3.client("datapipeline").activate_pipeline` method.

[Client.activate_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.activate_pipeline)

```python
def activate_pipeline(
    self,
    pipelineId: str,
    parameterValues: List["ParameterValueTypeDef"] = None,
    startTimestamp: datetime = None
) -> Dict[str, Any]:
    pass
```

### add_tags

Type annotations for `boto3.client("datapipeline").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.add_tags)

```python
def add_tags(
    self,
    pipelineId: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("datapipeline").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_pipeline

Type annotations for `boto3.client("datapipeline").create_pipeline` method.

[Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.create_pipeline)

```python
def create_pipeline(
    self,
    name: str,
    uniqueId: str,
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> CreatePipelineOutputTypeDef:
    pass
```

### deactivate_pipeline

Type annotations for `boto3.client("datapipeline").deactivate_pipeline` method.

[Client.deactivate_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.deactivate_pipeline)

```python
def deactivate_pipeline(
    self,
    pipelineId: str,
    cancelActive: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_pipeline

Type annotations for `boto3.client("datapipeline").delete_pipeline` method.

[Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.delete_pipeline)

```python
def delete_pipeline(
    self,
    pipelineId: str
) -> None:
    pass
```

### describe_objects

Type annotations for `boto3.client("datapipeline").describe_objects` method.

[Client.describe_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.describe_objects)

```python
def describe_objects(
    self,
    pipelineId: str,
    objectIds: List[str],
    evaluateExpressions: bool = None,
    marker: str = None
) -> DescribeObjectsOutputTypeDef:
    pass
```

### describe_pipelines

Type annotations for `boto3.client("datapipeline").describe_pipelines` method.

[Client.describe_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.describe_pipelines)

```python
def describe_pipelines(
    self,
    pipelineIds: List[str]
) -> DescribePipelinesOutputTypeDef:
    pass
```

### evaluate_expression

Type annotations for `boto3.client("datapipeline").evaluate_expression` method.

[Client.evaluate_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.evaluate_expression)

```python
def evaluate_expression(
    self,
    pipelineId: str,
    objectId: str,
    expression: str
) -> EvaluateExpressionOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("datapipeline").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.generate_presigned_url)

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

### get_pipeline_definition

Type annotations for `boto3.client("datapipeline").get_pipeline_definition` method.

[Client.get_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.get_pipeline_definition)

```python
def get_pipeline_definition(
    self,
    pipelineId: str,
    version: str = None
) -> GetPipelineDefinitionOutputTypeDef:
    pass
```

### list_pipelines

Type annotations for `boto3.client("datapipeline").list_pipelines` method.

[Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.list_pipelines)

```python
def list_pipelines(
    self,
    marker: str = None
) -> ListPipelinesOutputTypeDef:
    pass
```

### poll_for_task

Type annotations for `boto3.client("datapipeline").poll_for_task` method.

[Client.poll_for_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.poll_for_task)

```python
def poll_for_task(
    self,
    workerGroup: str,
    hostname: str = None,
    instanceIdentity: InstanceIdentityTypeDef = None
) -> PollForTaskOutputTypeDef:
    pass
```

### put_pipeline_definition

Type annotations for `boto3.client("datapipeline").put_pipeline_definition` method.

[Client.put_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.put_pipeline_definition)

```python
def put_pipeline_definition(
    self,
    pipelineId: str,
    pipelineObjects: List["PipelineObjectTypeDef"],
    parameterObjects: List["ParameterObjectTypeDef"] = None,
    parameterValues: List["ParameterValueTypeDef"] = None
) -> PutPipelineDefinitionOutputTypeDef:
    pass
```

### query_objects

Type annotations for `boto3.client("datapipeline").query_objects` method.

[Client.query_objects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.query_objects)

```python
def query_objects(
    self,
    pipelineId: str,
    sphere: str,
    query: QueryTypeDef = None,
    marker: str = None,
    limit: int = None
) -> QueryObjectsOutputTypeDef:
    pass
```

### remove_tags

Type annotations for `boto3.client("datapipeline").remove_tags` method.

[Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.remove_tags)

```python
def remove_tags(
    self,
    pipelineId: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### report_task_progress

Type annotations for `boto3.client("datapipeline").report_task_progress` method.

[Client.report_task_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.report_task_progress)

```python
def report_task_progress(
    self,
    taskId: str,
    fields: List["FieldTypeDef"] = None
) -> ReportTaskProgressOutputTypeDef:
    pass
```

### report_task_runner_heartbeat

Type annotations for `boto3.client("datapipeline").report_task_runner_heartbeat` method.

[Client.report_task_runner_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.report_task_runner_heartbeat)

```python
def report_task_runner_heartbeat(
    self,
    taskrunnerId: str,
    workerGroup: str = None,
    hostname: str = None
) -> ReportTaskRunnerHeartbeatOutputTypeDef:
    pass
```

### set_status

Type annotations for `boto3.client("datapipeline").set_status` method.

[Client.set_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.set_status)

```python
def set_status(
    self,
    pipelineId: str,
    objectIds: List[str],
    status: str
) -> None:
    pass
```

### set_task_status

Type annotations for `boto3.client("datapipeline").set_task_status` method.

[Client.set_task_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.set_task_status)

```python
def set_task_status(
    self,
    taskId: str,
    taskStatus: TaskStatus,
    errorId: str = None,
    errorMessage: str = None,
    errorStackTrace: str = None
) -> Dict[str, Any]:
    pass
```

### validate_pipeline_definition

Type annotations for `boto3.client("datapipeline").validate_pipeline_definition` method.

[Client.validate_pipeline_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client.validate_pipeline_definition)

```python
def validate_pipeline_definition(
    self,
    pipelineId: str,
    pipelineObjects: List["PipelineObjectTypeDef"],
    parameterObjects: List["ParameterObjectTypeDef"] = None,
    parameterValues: List["ParameterValueTypeDef"] = None
) -> ValidatePipelineDefinitionOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("datapipeline").get_paginator` method with overloads.

- `client.get_paginator("describe_objects")` -> [DescribeObjectsPaginator](./paginators.md#describeobjectspaginator)
- `client.get_paginator("list_pipelines")` -> [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)
- `client.get_paginator("query_objects")` -> [QueryObjectsPaginator](./paginators.md#queryobjectspaginator)


