# AugmentedAIRuntimeClient for boto3 AugmentedAIRuntime module

> [Index](../index.md) > [AugmentedAIRuntime](./index.md) > AugmentedAIRuntimeClient

Auto-generated documentation for [AugmentedAIRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime)
type annotations stubs module [mypy_boto3_sagemaker_a2i_runtime](https://pypi.org/project/mypy-boto3-sagemaker-a2i-runtime/).

- [AugmentedAIRuntimeClient for boto3 AugmentedAIRuntime module](#augmentedairuntimeclient-for-boto3-augmentedairuntime-module)
  - [AugmentedAIRuntimeClient](#augmentedairuntimeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_human_loop](#delete_human_loop)
    - [describe_human_loop](#describe_human_loop)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_human_loops](#list_human_loops)
    - [start_human_loop](#start_human_loop)
    - [stop_human_loop](#stop_human_loop)
    - [get_paginator](#get_paginator)

## AugmentedAIRuntimeClient

Type annotations for `boto3.client("sagemaker-a2i-runtime")`

Can be used directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sagemaker_a2i_runtime.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("sagemaker-a2i-runtime").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_human_loop

Type annotations for `boto3.client("sagemaker-a2i-runtime").delete_human_loop` method.

[Client.delete_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.delete_human_loop)

```python
def delete_human_loop(
    self,
    HumanLoopName: str
) -> Dict[str, Any]:
    pass
```

### describe_human_loop

Type annotations for `boto3.client("sagemaker-a2i-runtime").describe_human_loop` method.

[Client.describe_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.describe_human_loop)

```python
def describe_human_loop(
    self,
    HumanLoopName: str
) -> DescribeHumanLoopResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sagemaker-a2i-runtime").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.generate_presigned_url)

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

### list_human_loops

Type annotations for `boto3.client("sagemaker-a2i-runtime").list_human_loops` method.

[Client.list_human_loops documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.list_human_loops)

```python
def list_human_loops(
    self,
    FlowDefinitionArn: str,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHumanLoopsResponseTypeDef:
    pass
```

### start_human_loop

Type annotations for `boto3.client("sagemaker-a2i-runtime").start_human_loop` method.

[Client.start_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.start_human_loop)

```python
def start_human_loop(
    self,
    HumanLoopName: str,
    FlowDefinitionArn: str,
    HumanLoopInput: HumanLoopInputTypeDef,
    DataAttributes: HumanLoopDataAttributesTypeDef = None
) -> StartHumanLoopResponseTypeDef:
    pass
```

### stop_human_loop

Type annotations for `boto3.client("sagemaker-a2i-runtime").stop_human_loop` method.

[Client.stop_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.stop_human_loop)

```python
def stop_human_loop(
    self,
    HumanLoopName: str
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("sagemaker-a2i-runtime").get_paginator` method with overloads.

- `client.get_paginator("list_human_loops")` -> [ListHumanLoopsPaginator](./paginators.md#listhumanloopspaginator)


