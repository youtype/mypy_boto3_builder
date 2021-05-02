# MobileClient for boto3 Mobile module

> [Index](../index.md) > [Mobile](./index.md) > MobileClient

Auto-generated documentation for [Mobile](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile)
type annotations stubs module [mypy_boto3_mobile](https://pypi.org/project/mypy-boto3-mobile/).

- [MobileClient for boto3 Mobile module](#mobileclient-for-boto3-mobile-module)
  - [MobileClient](#mobileclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_project](#create_project)
    - [delete_project](#delete_project)
    - [describe_bundle](#describe_bundle)
    - [describe_project](#describe_project)
    - [export_bundle](#export_bundle)
    - [export_project](#export_project)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_bundles](#list_bundles)
    - [list_projects](#list_projects)
    - [update_project](#update_project)
    - [get_paginator](#get_paginator)

## MobileClient

Type annotations for `boto3.client("mobile")`

Can be used directly:

```python
from mypy_boto3_mobile.client import MobileClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mobile.client import Exceptions

def handle_error(exc: Exceptions.AccountActionRequiredException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccountActionRequiredException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalFailureException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("mobile").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_project

Type annotations for `boto3.client("mobile").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.create_project)

```python
def create_project(
    self,
    name: str = None,
    region: str = None,
    contents: Union[bytes, IO[bytes]] = None,
    snapshotId: str = None
) -> CreateProjectResultTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("mobile").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.delete_project)

```python
def delete_project(
    self,
    projectId: str
) -> DeleteProjectResultTypeDef:
    pass
```

### describe_bundle

Type annotations for `boto3.client("mobile").describe_bundle` method.

[Client.describe_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.describe_bundle)

```python
def describe_bundle(
    self,
    bundleId: str
) -> DescribeBundleResultTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("mobile").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.describe_project)

```python
def describe_project(
    self,
    projectId: str,
    syncFromResources: bool = None
) -> DescribeProjectResultTypeDef:
    pass
```

### export_bundle

Type annotations for `boto3.client("mobile").export_bundle` method.

[Client.export_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.export_bundle)

```python
def export_bundle(
    self,
    bundleId: str,
    projectId: str = None,
    platform: Platform = None
) -> ExportBundleResultTypeDef:
    pass
```

### export_project

Type annotations for `boto3.client("mobile").export_project` method.

[Client.export_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.export_project)

```python
def export_project(
    self,
    projectId: str
) -> ExportProjectResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mobile").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.generate_presigned_url)

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

### list_bundles

Type annotations for `boto3.client("mobile").list_bundles` method.

[Client.list_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.list_bundles)

```python
def list_bundles(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListBundlesResultTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("mobile").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.list_projects)

```python
def list_projects(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListProjectsResultTypeDef:
    pass
```

### update_project

Type annotations for `boto3.client("mobile").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile.Client.update_project)

```python
def update_project(
    self,
    projectId: str,
    contents: Union[bytes, IO[bytes]] = None
) -> UpdateProjectResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mobile").get_paginator` method with overloads.

- `client.get_paginator("list_bundles")` -> [ListBundlesPaginator](./paginators.md#listbundlespaginator)
- `client.get_paginator("list_projects")` -> [ListProjectsPaginator](./paginators.md#listprojectspaginator)


