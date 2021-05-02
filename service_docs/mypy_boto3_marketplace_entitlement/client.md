# MarketplaceEntitlementServiceClient for boto3 MarketplaceEntitlementService module

> [Index](../index.md) > [MarketplaceEntitlementService](./index.md) > MarketplaceEntitlementServiceClient

Auto-generated documentation for [MarketplaceEntitlementService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService)
type annotations stubs module [mypy_boto3_marketplace_entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/).

- [MarketplaceEntitlementServiceClient for boto3 MarketplaceEntitlementService module](#marketplaceentitlementserviceclient-for-boto3-marketplaceentitlementservice-module)
  - [MarketplaceEntitlementServiceClient](#marketplaceentitlementserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_entitlements](#get_entitlements)
    - [get_paginator](#get_paginator)

## MarketplaceEntitlementServiceClient

Type annotations for `boto3.client("marketplace-entitlement")`

Can be used directly:

```python
from mypy_boto3_marketplace_entitlement.client import MarketplaceEntitlementServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_marketplace_entitlement.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.InvalidParameterException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("marketplace-entitlement").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("marketplace-entitlement").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.generate_presigned_url)

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

### get_entitlements

Type annotations for `boto3.client("marketplace-entitlement").get_entitlements` method.

[Client.get_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.get_entitlements)

```python
def get_entitlements(
    self,
    ProductCode: str,
    Filter: Dict[GetEntitlementFilterName, List[str]] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> GetEntitlementsResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("marketplace-entitlement").get_paginator` method.

[Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)

```python
def get_paginator(
    self,
    operation_name: GetEntitlementsPaginatorName
) -> GetEntitlementsPaginator:
    pass
```