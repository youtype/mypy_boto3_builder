# PrometheusServiceClient for boto3 PrometheusService module

> [Index](../index.md) > [PrometheusService](./index.md) > PrometheusServiceClient

Auto-generated documentation for [PrometheusService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService)
type annotations stubs module [mypy_boto3_amp](https://pypi.org/project/mypy-boto3-amp/).

- [PrometheusServiceClient for boto3 PrometheusService module](#prometheusserviceclient-for-boto3-prometheusservice-module)
  - [PrometheusServiceClient](#prometheusserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_workspace](#create_workspace)
    - [delete_workspace](#delete_workspace)
    - [describe_workspace](#describe_workspace)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_workspaces](#list_workspaces)
    - [update_workspace_alias](#update_workspace_alias)
    - [get_paginator](#get_paginator)

## PrometheusServiceClient

Type annotations for `boto3.client("amp")`

Can be used directly:

```python
from mypy_boto3_amp.client import PrometheusServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_amp.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("amp").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_workspace

Type annotations for `boto3.client("amp").create_workspace` method.

[Client.create_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.create_workspace)

```python
def create_workspace(
    self,
    alias: str = None,
    clientToken: str = None
) -> CreateWorkspaceResponseTypeDef:
    pass
```

### delete_workspace

Type annotations for `boto3.client("amp").delete_workspace` method.

[Client.delete_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.delete_workspace)

```python
def delete_workspace(
    self,
    workspaceId: str,
    clientToken: str = None
) -> None:
    pass
```

### describe_workspace

Type annotations for `boto3.client("amp").describe_workspace` method.

[Client.describe_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.describe_workspace)

```python
def describe_workspace(
    self,
    workspaceId: str
) -> DescribeWorkspaceResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("amp").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.generate_presigned_url)

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

### list_workspaces

Type annotations for `boto3.client("amp").list_workspaces` method.

[Client.list_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.list_workspaces)

```python
def list_workspaces(
    self,
    alias: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListWorkspacesResponseTypeDef:
    pass
```

### update_workspace_alias

Type annotations for `boto3.client("amp").update_workspace_alias` method.

[Client.update_workspace_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Client.update_workspace_alias)

```python
def update_workspace_alias(
    self,
    workspaceId: str,
    alias: str = None,
    clientToken: str = None
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("amp").get_paginator` method.

[Paginator.ListWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)

```python
def get_paginator(
    self,
    operation_name: ListWorkspacesPaginatorName
) -> ListWorkspacesPaginator:
    pass
```