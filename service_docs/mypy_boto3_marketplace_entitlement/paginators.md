# Paginators for boto3 MarketplaceEntitlementService module

> [Index](../index.md) > [MarketplaceEntitlementService](./index.md) > Paginators

Auto-generated documentation for [MarketplaceEntitlementService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService)
type annotations stubs module [mypy_boto3_marketplace_entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/).

- [Paginators for boto3 MarketplaceEntitlementService module](#paginators-for-boto3-marketplaceentitlementservice-module)
  - [GetEntitlementsPaginator](#getentitlementspaginator)

## GetEntitlementsPaginator

Type annotations for `boto3.client("marketplace-entitlement").get_paginator("get_entitlements")`.

Can be used directly:

```python
from mypy_boto3_marketplace_entitlement.paginators import GetEntitlementsPaginator

def get_get_entitlements_paginator() -> GetEntitlementsPaginator:
    return boto3.client("marketplace-entitlement").get_paginator("get_entitlements")
```

[Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)

```python
class GetEntitlementsPaginator(Boto3Paginator):
    def paginate(
        self,
        ProductCode: str,
        Filter: Dict[GetEntitlementFilterName, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetEntitlementsResultTypeDef]:
        pass
```