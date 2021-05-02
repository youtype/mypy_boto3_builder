# Paginators for boto3 SecretsManager module

> [Index](../index.md) > [SecretsManager](./index.md) > Paginators

Auto-generated documentation for [SecretsManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager)
type annotations stubs module [mypy_boto3_secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/).

- [Paginators for boto3 SecretsManager module](#paginators-for-boto3-secretsmanager-module)
  - [ListSecretsPaginator](#listsecretspaginator)

## ListSecretsPaginator

Type annotations for `boto3.client("secretsmanager").get_paginator("list_secrets")`.

Can be used directly:

```python
from mypy_boto3_secretsmanager.paginators import ListSecretsPaginator

def get_list_secrets_paginator() -> ListSecretsPaginator:
    return boto3.client("secretsmanager").get_paginator("list_secrets")
```

[Paginator.ListSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)

```python
class ListSecretsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecretsResponseTypeDef]:
        pass
```