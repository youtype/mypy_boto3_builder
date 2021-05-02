# Type annotations for boto3 MarketplaceEntitlementService module

> [Index](../index.md) > MarketplaceEntitlementService

Auto-generated documentation for [MarketplaceEntitlementService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService)
type annotations stubs module [mypy_boto3_marketplace_entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/).

```bash
pip install mypy-boto3-marketplace-entitlement
```

- [Type annotations for boto3 MarketplaceEntitlementService module](#type-annotations-for-boto3-marketplaceentitlementservice-module)
  - [MarketplaceEntitlementServiceClient](#marketplaceentitlementserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MarketplaceEntitlementServiceClient

Type annotations for  `boto3.client("marketplace-entitlement")` as [MarketplaceEntitlementServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_marketplace_entitlement.client import MarketplaceEntitlementServiceClient
```


MarketplaceEntitlementServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_entitlements](./client.md#get-entitlements)
- [get_paginator](./client.md#get-paginator)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [ThrottlingException](./client.md#throttlingexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("marketplace-entitlement").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_marketplace_entitlement.paginators import GetEntitlementsPaginator, ...
```

- [GetEntitlementsPaginator](./paginators.md#getentitlementspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_marketplace_entitlement.literals import GetEntitlementFilterName, ...
```

- [GetEntitlementFilterName](./literals.md#getentitlementfiltername)
- [GetEntitlementsPaginatorName](./literals.md#getentitlementspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_marketplace_entitlement.type_defs import EntitlementTypeDef, ...
```

- [EntitlementTypeDef](./type_defs.md#entitlementtypedef)
- [EntitlementValueTypeDef](./type_defs.md#entitlementvaluetypedef)
- [GetEntitlementsResultTypeDef](./type_defs.md#getentitlementsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
