# Paginators for boto3 MediaConnect module

> [Index](../index.md) > [MediaConnect](./index.md) > Paginators

Auto-generated documentation for [MediaConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect)
type annotations stubs module [mypy_boto3_mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/).

- [Paginators for boto3 MediaConnect module](#paginators-for-boto3-mediaconnect-module)
  - [ListEntitlementsPaginator](#listentitlementspaginator)
  - [ListFlowsPaginator](#listflowspaginator)
  - [ListOfferingsPaginator](#listofferingspaginator)
  - [ListReservationsPaginator](#listreservationspaginator)

## ListEntitlementsPaginator

Type annotations for `boto3.client("mediaconnect").get_paginator("list_entitlements")`.

Can be used directly:

```python
from mypy_boto3_mediaconnect.paginators import ListEntitlementsPaginator

def get_list_entitlements_paginator() -> ListEntitlementsPaginator:
    return boto3.client("mediaconnect").get_paginator("list_entitlements")
```

[Paginator.ListEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements)

```python
class ListEntitlementsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntitlementsResponseTypeDef]:
        pass
```
## ListFlowsPaginator

Type annotations for `boto3.client("mediaconnect").get_paginator("list_flows")`.

Can be used directly:

```python
from mypy_boto3_mediaconnect.paginators import ListFlowsPaginator

def get_list_flows_paginator() -> ListFlowsPaginator:
    return boto3.client("mediaconnect").get_paginator("list_flows")
```

[Paginator.ListFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows)

```python
class ListFlowsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFlowsResponseTypeDef]:
        pass
```
## ListOfferingsPaginator

Type annotations for `boto3.client("mediaconnect").get_paginator("list_offerings")`.

Can be used directly:

```python
from mypy_boto3_mediaconnect.paginators import ListOfferingsPaginator

def get_list_offerings_paginator() -> ListOfferingsPaginator:
    return boto3.client("mediaconnect").get_paginator("list_offerings")
```

[Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Paginator.ListOfferings)

```python
class ListOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingsResponseTypeDef]:
        pass
```
## ListReservationsPaginator

Type annotations for `boto3.client("mediaconnect").get_paginator("list_reservations")`.

Can be used directly:

```python
from mypy_boto3_mediaconnect.paginators import ListReservationsPaginator

def get_list_reservations_paginator() -> ListReservationsPaginator:
    return boto3.client("mediaconnect").get_paginator("list_reservations")
```

[Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Paginator.ListReservations)

```python
class ListReservationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReservationsResponseTypeDef]:
        pass
```