# BraketClient for boto3 Braket module

> [Index](../index.md) > [Braket](./index.md) > BraketClient

Auto-generated documentation for [Braket](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket)
type annotations stubs module [mypy_boto3_braket](https://pypi.org/project/mypy-boto3-braket/).

- [BraketClient for boto3 Braket module](#braketclient-for-boto3-braket-module)
  - [BraketClient](#braketclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_quantum_task](#cancel_quantum_task)
    - [create_quantum_task](#create_quantum_task)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_device](#get_device)
    - [get_quantum_task](#get_quantum_task)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [search_devices](#search_devices)
    - [search_quantum_tasks](#search_quantum_tasks)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)

## BraketClient

Type annotations for `boto3.client("braket")`

Can be used directly:

```python
from mypy_boto3_braket.client import BraketClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_braket.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.DeviceOfflineException`
- `Exceptions.InternalServiceException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("braket").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_quantum_task

Type annotations for `boto3.client("braket").cancel_quantum_task` method.

[Client.cancel_quantum_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.cancel_quantum_task)

```python
def cancel_quantum_task(
    self,
    clientToken: str,
    quantumTaskArn: str
) -> CancelQuantumTaskResponseTypeDef:
    pass
```

### create_quantum_task

Type annotations for `boto3.client("braket").create_quantum_task` method.

[Client.create_quantum_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.create_quantum_task)

```python
def create_quantum_task(
    self,
    action: str,
    clientToken: str,
    deviceArn: str,
    outputS3Bucket: str,
    outputS3KeyPrefix: str,
    shots: int,
    deviceParameters: str = None,
    tags: Dict[str, str] = None
) -> CreateQuantumTaskResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("braket").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.generate_presigned_url)

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

### get_device

Type annotations for `boto3.client("braket").get_device` method.

[Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_device)

```python
def get_device(
    self,
    deviceArn: str
) -> GetDeviceResponseTypeDef:
    pass
```

### get_quantum_task

Type annotations for `boto3.client("braket").get_quantum_task` method.

[Client.get_quantum_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_quantum_task)

```python
def get_quantum_task(
    self,
    quantumTaskArn: str
) -> GetQuantumTaskResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("braket").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### search_devices

Type annotations for `boto3.client("braket").search_devices` method.

[Client.search_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.search_devices)

```python
def search_devices(
    self,
    filters: List[SearchDevicesFilterTypeDef],
    maxResults: int = None,
    nextToken: str = None
) -> SearchDevicesResponseTypeDef:
    pass
```

### search_quantum_tasks

Type annotations for `boto3.client("braket").search_quantum_tasks` method.

[Client.search_quantum_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.search_quantum_tasks)

```python
def search_quantum_tasks(
    self,
    filters: List[SearchQuantumTasksFilterTypeDef],
    maxResults: int = None,
    nextToken: str = None
) -> SearchQuantumTasksResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("braket").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("braket").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("braket").get_paginator` method.

[Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Paginator.SearchDevices)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchDevicesPaginatorName
) -> SearchDevicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("braket").get_paginator` method.

[Paginator.SearchQuantumTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Paginator.SearchQuantumTasks)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchQuantumTasksPaginatorName
) -> SearchQuantumTasksPaginator:
    pass
```