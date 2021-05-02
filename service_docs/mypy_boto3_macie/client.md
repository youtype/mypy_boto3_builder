# MacieClient for boto3 Macie module

> [Index](../index.md) > [Macie](./index.md) > MacieClient

Auto-generated documentation for [Macie](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie)
type annotations stubs module [mypy_boto3_macie](https://pypi.org/project/mypy-boto3-macie/).

- [MacieClient for boto3 Macie module](#macieclient-for-boto3-macie-module)
  - [MacieClient](#macieclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_member_account](#associate_member_account)
    - [associate_s3_resources](#associate_s3_resources)
    - [can_paginate](#can_paginate)
    - [disassociate_member_account](#disassociate_member_account)
    - [disassociate_s3_resources](#disassociate_s3_resources)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_member_accounts](#list_member_accounts)
    - [list_s3_resources](#list_s3_resources)
    - [update_s3_resources](#update_s3_resources)
    - [get_paginator](#get_paginator)

## MacieClient

Type annotations for `boto3.client("macie")`

Can be used directly:

```python
from mypy_boto3_macie.client import MacieClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_macie.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalException`
- `Exceptions.InvalidInputException`
- `Exceptions.LimitExceededException`


## Methods


### associate_member_account

Type annotations for `boto3.client("macie").associate_member_account` method.

[Client.associate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.associate_member_account)

```python
def associate_member_account(
    self,
    memberAccountId: str
) -> None:
    pass
```

### associate_s3_resources

Type annotations for `boto3.client("macie").associate_s3_resources` method.

[Client.associate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.associate_s3_resources)

```python
def associate_s3_resources(
    self,
    s3Resources: List["S3ResourceClassificationTypeDef"],
    memberAccountId: str = None
) -> AssociateS3ResourcesResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("macie").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### disassociate_member_account

Type annotations for `boto3.client("macie").disassociate_member_account` method.

[Client.disassociate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.disassociate_member_account)

```python
def disassociate_member_account(
    self,
    memberAccountId: str
) -> None:
    pass
```

### disassociate_s3_resources

Type annotations for `boto3.client("macie").disassociate_s3_resources` method.

[Client.disassociate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.disassociate_s3_resources)

```python
def disassociate_s3_resources(
    self,
    associatedS3Resources: List["S3ResourceTypeDef"],
    memberAccountId: str = None
) -> DisassociateS3ResourcesResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("macie").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.generate_presigned_url)

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

### list_member_accounts

Type annotations for `boto3.client("macie").list_member_accounts` method.

[Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.list_member_accounts)

```python
def list_member_accounts(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListMemberAccountsResultTypeDef:
    pass
```

### list_s3_resources

Type annotations for `boto3.client("macie").list_s3_resources` method.

[Client.list_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.list_s3_resources)

```python
def list_s3_resources(
    self,
    memberAccountId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListS3ResourcesResultTypeDef:
    pass
```

### update_s3_resources

Type annotations for `boto3.client("macie").update_s3_resources` method.

[Client.update_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html#Macie.Client.update_s3_resources)

```python
def update_s3_resources(
    self,
    s3ResourcesUpdate: List[S3ResourceClassificationUpdateTypeDef],
    memberAccountId: str = None
) -> UpdateS3ResourcesResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("macie").get_paginator` method with overloads.

- `client.get_paginator("list_member_accounts")` -> [ListMemberAccountsPaginator](./paginators.md#listmemberaccountspaginator)
- `client.get_paginator("list_s3_resources")` -> [ListS3ResourcesPaginator](./paginators.md#lists3resourcespaginator)


