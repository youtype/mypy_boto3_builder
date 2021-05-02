# Paginators for boto3 KMS module

> [Index](../index.md) > [KMS](./index.md) > Paginators

Auto-generated documentation for [KMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS)
type annotations stubs module [mypy_boto3_kms](https://pypi.org/project/mypy-boto3-kms/).

- [Paginators for boto3 KMS module](#paginators-for-boto3-kms-module)
  - [ListAliasesPaginator](#listaliasespaginator)
  - [ListGrantsPaginator](#listgrantspaginator)
  - [ListKeyPoliciesPaginator](#listkeypoliciespaginator)
  - [ListKeysPaginator](#listkeyspaginator)

## ListAliasesPaginator

Type annotations for `boto3.client("kms").get_paginator("list_aliases")`.

Can be used directly:

```python
from mypy_boto3_kms.paginators import ListAliasesPaginator

def get_list_aliases_paginator() -> ListAliasesPaginator:
    return boto3.client("kms").get_paginator("list_aliases")
```

[Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Paginator.ListAliases)

```python
class ListAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        KeyId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        pass
```
## ListGrantsPaginator

Type annotations for `boto3.client("kms").get_paginator("list_grants")`.

Can be used directly:

```python
from mypy_boto3_kms.paginators import ListGrantsPaginator

def get_list_grants_paginator() -> ListGrantsPaginator:
    return boto3.client("kms").get_paginator("list_grants")
```

[Paginator.ListGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Paginator.ListGrants)

```python
class ListGrantsPaginator(Boto3Paginator):
    def paginate(
        self,
        KeyId: str,
        GrantId: str = None,
        GranteePrincipal: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGrantsResponseTypeDef]:
        pass
```
## ListKeyPoliciesPaginator

Type annotations for `boto3.client("kms").get_paginator("list_key_policies")`.

Can be used directly:

```python
from mypy_boto3_kms.paginators import ListKeyPoliciesPaginator

def get_list_key_policies_paginator() -> ListKeyPoliciesPaginator:
    return boto3.client("kms").get_paginator("list_key_policies")
```

[Paginator.ListKeyPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)

```python
class ListKeyPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        KeyId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeyPoliciesResponseTypeDef]:
        pass
```
## ListKeysPaginator

Type annotations for `boto3.client("kms").get_paginator("list_keys")`.

Can be used directly:

```python
from mypy_boto3_kms.paginators import ListKeysPaginator

def get_list_keys_paginator() -> ListKeysPaginator:
    return boto3.client("kms").get_paginator("list_keys")
```

[Paginator.ListKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Paginator.ListKeys)

```python
class ListKeysPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysResponseTypeDef]:
        pass
```