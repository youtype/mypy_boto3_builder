# IdentityStoreClient for boto3 IdentityStore module

> [Index](../index.md) > [IdentityStore](./index.md) > IdentityStoreClient

Auto-generated documentation for [IdentityStore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore)
type annotations stubs module [mypy_boto3_identitystore](https://pypi.org/project/mypy-boto3-identitystore/).

- [IdentityStoreClient for boto3 IdentityStore module](#identitystoreclient-for-boto3-identitystore-module)
  - [IdentityStoreClient](#identitystoreclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_group](#describe_group)
    - [describe_user](#describe_user)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_groups](#list_groups)
    - [list_users](#list_users)

## IdentityStoreClient

Type annotations for `boto3.client("identitystore")`

Can be used directly:

```python
from mypy_boto3_identitystore.client import IdentityStoreClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_identitystore.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("identitystore").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_group

Type annotations for `boto3.client("identitystore").describe_group` method.

[Client.describe_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Client.describe_group)

```python
def describe_group(
    self,
    IdentityStoreId: str,
    GroupId: str
) -> DescribeGroupResponseTypeDef:
    pass
```

### describe_user

Type annotations for `boto3.client("identitystore").describe_user` method.

[Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Client.describe_user)

```python
def describe_user(
    self,
    IdentityStoreId: str,
    UserId: str
) -> DescribeUserResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("identitystore").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Client.generate_presigned_url)

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

### list_groups

Type annotations for `boto3.client("identitystore").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Client.list_groups)

```python
def list_groups(
    self,
    IdentityStoreId: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListGroupsResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("identitystore").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html#IdentityStore.Client.list_users)

```python
def list_users(
    self,
    IdentityStoreId: str,
    MaxResults: int = None,
    NextToken: str = None,
    Filters: List[FilterTypeDef] = None
) -> ListUsersResponseTypeDef:
    pass
```



