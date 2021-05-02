# Paginators for boto3 Route53Domains module

> [Index](../index.md) > [Route53Domains](./index.md) > Paginators

Auto-generated documentation for [Route53Domains](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains)
type annotations stubs module [mypy_boto3_route53domains](https://pypi.org/project/mypy-boto3-route53domains/).

- [Paginators for boto3 Route53Domains module](#paginators-for-boto3-route53domains-module)
  - [ListDomainsPaginator](#listdomainspaginator)
  - [ListOperationsPaginator](#listoperationspaginator)
  - [ViewBillingPaginator](#viewbillingpaginator)

## ListDomainsPaginator

Type annotations for `boto3.client("route53domains").get_paginator("list_domains")`.

Can be used directly:

```python
from mypy_boto3_route53domains.paginators import ListDomainsPaginator

def get_list_domains_paginator() -> ListDomainsPaginator:
    return boto3.client("route53domains").get_paginator("list_domains")
```

[Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Paginator.ListDomains)

```python
class ListDomainsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        pass
```
## ListOperationsPaginator

Type annotations for `boto3.client("route53domains").get_paginator("list_operations")`.

Can be used directly:

```python
from mypy_boto3_route53domains.paginators import ListOperationsPaginator

def get_list_operations_paginator() -> ListOperationsPaginator:
    return boto3.client("route53domains").get_paginator("list_operations")
```

[Paginator.ListOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Paginator.ListOperations)

```python
class ListOperationsPaginator(Boto3Paginator):
    def paginate(
        self,
        SubmittedSince: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOperationsResponseTypeDef]:
        pass
```
## ViewBillingPaginator

Type annotations for `boto3.client("route53domains").get_paginator("view_billing")`.

Can be used directly:

```python
from mypy_boto3_route53domains.paginators import ViewBillingPaginator

def get_view_billing_paginator() -> ViewBillingPaginator:
    return boto3.client("route53domains").get_paginator("view_billing")
```

[Paginator.ViewBilling documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html#Route53Domains.Paginator.ViewBilling)

```python
class ViewBillingPaginator(Boto3Paginator):
    def paginate(
        self,
        Start: datetime = None,
        End: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ViewBillingResponseTypeDef]:
        pass
```