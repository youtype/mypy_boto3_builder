# Paginators for boto3 FMS module

> [Index](../index.md) > [FMS](./index.md) > Paginators

Auto-generated documentation for [FMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS)
type annotations stubs module [mypy_boto3_fms](https://pypi.org/project/mypy-boto3-fms/).

- [Paginators for boto3 FMS module](#paginators-for-boto3-fms-module)
  - [ListComplianceStatusPaginator](#listcompliancestatuspaginator)
  - [ListMemberAccountsPaginator](#listmemberaccountspaginator)
  - [ListPoliciesPaginator](#listpoliciespaginator)

## ListComplianceStatusPaginator

Type annotations for `boto3.client("fms").get_paginator("list_compliance_status")`.

Can be used directly:

```python
from mypy_boto3_fms.paginators import ListComplianceStatusPaginator

def get_list_compliance_status_paginator() -> ListComplianceStatusPaginator:
    return boto3.client("fms").get_paginator("list_compliance_status")
```

[Paginator.ListComplianceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)

```python
class ListComplianceStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        PolicyId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComplianceStatusResponseTypeDef]:
        pass
```
## ListMemberAccountsPaginator

Type annotations for `boto3.client("fms").get_paginator("list_member_accounts")`.

Can be used directly:

```python
from mypy_boto3_fms.paginators import ListMemberAccountsPaginator

def get_list_member_accounts_paginator() -> ListMemberAccountsPaginator:
    return boto3.client("fms").get_paginator("list_member_accounts")
```

[Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)

```python
class ListMemberAccountsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMemberAccountsResponseTypeDef]:
        pass
```
## ListPoliciesPaginator

Type annotations for `boto3.client("fms").get_paginator("list_policies")`.

Can be used directly:

```python
from mypy_boto3_fms.paginators import ListPoliciesPaginator

def get_list_policies_paginator() -> ListPoliciesPaginator:
    return boto3.client("fms").get_paginator("list_policies")
```

[Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html#FMS.Paginator.ListPolicies)

```python
class ListPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        pass
```