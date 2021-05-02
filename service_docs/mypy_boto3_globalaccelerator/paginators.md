# Paginators for boto3 GlobalAccelerator module

> [Index](../index.md) > [GlobalAccelerator](./index.md) > Paginators

Auto-generated documentation for [GlobalAccelerator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator)
type annotations stubs module [mypy_boto3_globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/).

- [Paginators for boto3 GlobalAccelerator module](#paginators-for-boto3-globalaccelerator-module)
  - [ListAcceleratorsPaginator](#listacceleratorspaginator)
  - [ListByoipCidrsPaginator](#listbyoipcidrspaginator)
  - [ListCustomRoutingAcceleratorsPaginator](#listcustomroutingacceleratorspaginator)
  - [ListCustomRoutingListenersPaginator](#listcustomroutinglistenerspaginator)
  - [ListCustomRoutingPortMappingsPaginator](#listcustomroutingportmappingspaginator)
  - [ListCustomRoutingPortMappingsByDestinationPaginator](#listcustomroutingportmappingsbydestinationpaginator)
  - [ListEndpointGroupsPaginator](#listendpointgroupspaginator)
  - [ListListenersPaginator](#listlistenerspaginator)

## ListAcceleratorsPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_accelerators")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListAcceleratorsPaginator

def get_list_accelerators_paginator() -> ListAcceleratorsPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_accelerators")
```

[Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)

```python
class ListAcceleratorsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAcceleratorsResponseTypeDef]:
        pass
```
## ListByoipCidrsPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_byoip_cidrs")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListByoipCidrsPaginator

def get_list_byoip_cidrs_paginator() -> ListByoipCidrsPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_byoip_cidrs")
```

[Paginator.ListByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs)

```python
class ListByoipCidrsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListByoipCidrsResponseTypeDef]:
        pass
```
## ListCustomRoutingAcceleratorsPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_custom_routing_accelerators")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListCustomRoutingAcceleratorsPaginator

def get_list_custom_routing_accelerators_paginator() -> ListCustomRoutingAcceleratorsPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_custom_routing_accelerators")
```

[Paginator.ListCustomRoutingAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)

```python
class ListCustomRoutingAcceleratorsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomRoutingAcceleratorsResponseTypeDef]:
        pass
```
## ListCustomRoutingListenersPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_custom_routing_listeners")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListCustomRoutingListenersPaginator

def get_list_custom_routing_listeners_paginator() -> ListCustomRoutingListenersPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_custom_routing_listeners")
```

[Paginator.ListCustomRoutingListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)

```python
class ListCustomRoutingListenersPaginator(Boto3Paginator):
    def paginate(
        self,
        AcceleratorArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomRoutingListenersResponseTypeDef]:
        pass
```
## ListCustomRoutingPortMappingsPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_custom_routing_port_mappings")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListCustomRoutingPortMappingsPaginator

def get_list_custom_routing_port_mappings_paginator() -> ListCustomRoutingPortMappingsPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_custom_routing_port_mappings")
```

[Paginator.ListCustomRoutingPortMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)

```python
class ListCustomRoutingPortMappingsPaginator(Boto3Paginator):
    def paginate(
        self,
        AcceleratorArn: str,
        EndpointGroupArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomRoutingPortMappingsResponseTypeDef]:
        pass
```
## ListCustomRoutingPortMappingsByDestinationPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_custom_routing_port_mappings_by_destination")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListCustomRoutingPortMappingsByDestinationPaginator

def get_list_custom_routing_port_mappings_by_destination_paginator() -> ListCustomRoutingPortMappingsByDestinationPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_custom_routing_port_mappings_by_destination")
```

[Paginator.ListCustomRoutingPortMappingsByDestination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)

```python
class ListCustomRoutingPortMappingsByDestinationPaginator(Boto3Paginator):
    def paginate(
        self,
        EndpointId: str,
        DestinationAddress: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomRoutingPortMappingsByDestinationResponseTypeDef]:
        pass
```
## ListEndpointGroupsPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_endpoint_groups")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListEndpointGroupsPaginator

def get_list_endpoint_groups_paginator() -> ListEndpointGroupsPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_endpoint_groups")
```

[Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)

```python
class ListEndpointGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ListenerArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEndpointGroupsResponseTypeDef]:
        pass
```
## ListListenersPaginator

Type annotations for `boto3.client("globalaccelerator").get_paginator("list_listeners")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListListenersPaginator

def get_list_listeners_paginator() -> ListListenersPaginator:
    return boto3.client("globalaccelerator").get_paginator("list_listeners")
```

[Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)

```python
class ListListenersPaginator(Boto3Paginator):
    def paginate(
        self,
        AcceleratorArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListListenersResponseTypeDef]:
        pass
```