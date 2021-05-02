# Paginators for boto3 NetworkManager module

> [Index](../index.md) > [NetworkManager](./index.md) > Paginators

Auto-generated documentation for [NetworkManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager)
type annotations stubs module [mypy_boto3_networkmanager](https://pypi.org/project/mypy-boto3-networkmanager/).

- [Paginators for boto3 NetworkManager module](#paginators-for-boto3-networkmanager-module)
  - [DescribeGlobalNetworksPaginator](#describeglobalnetworkspaginator)
  - [GetConnectionsPaginator](#getconnectionspaginator)
  - [GetCustomerGatewayAssociationsPaginator](#getcustomergatewayassociationspaginator)
  - [GetDevicesPaginator](#getdevicespaginator)
  - [GetLinkAssociationsPaginator](#getlinkassociationspaginator)
  - [GetLinksPaginator](#getlinkspaginator)
  - [GetSitesPaginator](#getsitespaginator)
  - [GetTransitGatewayConnectPeerAssociationsPaginator](#gettransitgatewayconnectpeerassociationspaginator)
  - [GetTransitGatewayRegistrationsPaginator](#gettransitgatewayregistrationspaginator)

## DescribeGlobalNetworksPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("describe_global_networks")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import DescribeGlobalNetworksPaginator

def get_describe_global_networks_paginator() -> DescribeGlobalNetworksPaginator:
    return boto3.client("networkmanager").get_paginator("describe_global_networks")
```

[Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)

```python
class DescribeGlobalNetworksPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGlobalNetworksResponseTypeDef]:
        pass
```
## GetConnectionsPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_connections")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetConnectionsPaginator

def get_get_connections_paginator() -> GetConnectionsPaginator:
    return boto3.client("networkmanager").get_paginator("get_connections")
```

[Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections)

```python
class GetConnectionsPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        ConnectionIds: List[str] = None,
        DeviceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectionsResponseTypeDef]:
        pass
```
## GetCustomerGatewayAssociationsPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_customer_gateway_associations")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetCustomerGatewayAssociationsPaginator

def get_get_customer_gateway_associations_paginator() -> GetCustomerGatewayAssociationsPaginator:
    return boto3.client("networkmanager").get_paginator("get_customer_gateway_associations")
```

[Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)

```python
class GetCustomerGatewayAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCustomerGatewayAssociationsResponseTypeDef]:
        pass
```
## GetDevicesPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_devices")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetDevicesPaginator

def get_get_devices_paginator() -> GetDevicesPaginator:
    return boto3.client("networkmanager").get_paginator("get_devices")
```

[Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)

```python
class GetDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetDevicesResponseTypeDef]:
        pass
```
## GetLinkAssociationsPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_link_associations")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetLinkAssociationsPaginator

def get_get_link_associations_paginator() -> GetLinkAssociationsPaginator:
    return boto3.client("networkmanager").get_paginator("get_link_associations")
```

[Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)

```python
class GetLinkAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLinkAssociationsResponseTypeDef]:
        pass
```
## GetLinksPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_links")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetLinksPaginator

def get_get_links_paginator() -> GetLinksPaginator:
    return boto3.client("networkmanager").get_paginator("get_links")
```

[Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)

```python
class GetLinksPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetLinksResponseTypeDef]:
        pass
```
## GetSitesPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_sites")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetSitesPaginator

def get_get_sites_paginator() -> GetSitesPaginator:
    return boto3.client("networkmanager").get_paginator("get_sites")
```

[Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)

```python
class GetSitesPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSitesResponseTypeDef]:
        pass
```
## GetTransitGatewayConnectPeerAssociationsPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_transit_gateway_connect_peer_associations")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetTransitGatewayConnectPeerAssociationsPaginator

def get_get_transit_gateway_connect_peer_associations_paginator() -> GetTransitGatewayConnectPeerAssociationsPaginator:
    return boto3.client("networkmanager").get_paginator("get_transit_gateway_connect_peer_associations")
```

[Paginator.GetTransitGatewayConnectPeerAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)

```python
class GetTransitGatewayConnectPeerAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayConnectPeerAssociationsResponseTypeDef]:
        pass
```
## GetTransitGatewayRegistrationsPaginator

Type annotations for `boto3.client("networkmanager").get_paginator("get_transit_gateway_registrations")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import GetTransitGatewayRegistrationsPaginator

def get_get_transit_gateway_registrations_paginator() -> GetTransitGatewayRegistrationsPaginator:
    return boto3.client("networkmanager").get_paginator("get_transit_gateway_registrations")
```

[Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)

```python
class GetTransitGatewayRegistrationsPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayRegistrationsResponseTypeDef]:
        pass
```