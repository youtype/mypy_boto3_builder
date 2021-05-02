# S3OutpostsClient for boto3 S3Outposts module

> [Index](../index.md) > [S3Outposts](./index.md) > S3OutpostsClient

Auto-generated documentation for [S3Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts)
type annotations stubs module [mypy_boto3_s3outposts](https://pypi.org/project/mypy-boto3-s3outposts/).

- [S3OutpostsClient for boto3 S3Outposts module](#s3outpostsclient-for-boto3-s3outposts-module)
  - [S3OutpostsClient](#s3outpostsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_endpoint](#create_endpoint)
    - [delete_endpoint](#delete_endpoint)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_endpoints](#list_endpoints)
    - [get_paginator](#get_paginator)

## S3OutpostsClient

Type annotations for `boto3.client("s3outposts")`

Can be used directly:

```python
from mypy_boto3_s3outposts.client import S3OutpostsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_s3outposts.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("s3outposts").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_endpoint

Type annotations for `boto3.client("s3outposts").create_endpoint` method.

[Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client.create_endpoint)

```python
def create_endpoint(
    self,
    OutpostId: str,
    SubnetId: str,
    SecurityGroupId: str
) -> CreateEndpointResultTypeDef:
    pass
```

### delete_endpoint

Type annotations for `boto3.client("s3outposts").delete_endpoint` method.

[Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client.delete_endpoint)

```python
def delete_endpoint(
    self,
    EndpointId: str,
    OutpostId: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("s3outposts").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client.generate_presigned_url)

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

### list_endpoints

Type annotations for `boto3.client("s3outposts").list_endpoints` method.

[Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Client.list_endpoints)

```python
def list_endpoints(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEndpointsResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("s3outposts").get_paginator` method.

[Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts.Paginator.ListEndpoints)

```python
def get_paginator(
    self,
    operation_name: ListEndpointsPaginatorName
) -> ListEndpointsPaginator:
    pass
```