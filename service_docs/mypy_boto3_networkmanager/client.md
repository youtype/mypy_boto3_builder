# NetworkManagerClient for boto3 NetworkManager module

> [Index](../index.md) > [NetworkManager](./index.md) > NetworkManagerClient

Auto-generated documentation for [NetworkManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager)
type annotations stubs module [mypy_boto3_networkmanager](https://pypi.org/project/mypy-boto3-networkmanager/).

- [NetworkManagerClient for boto3 NetworkManager module](#networkmanagerclient-for-boto3-networkmanager-module)
  - [NetworkManagerClient](#networkmanagerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_customer_gateway](#associate_customer_gateway)
    - [associate_link](#associate_link)
    - [associate_transit_gateway_connect_peer](#associate_transit_gateway_connect_peer)
    - [can_paginate](#can_paginate)
    - [create_connection](#create_connection)
    - [create_device](#create_device)
    - [create_global_network](#create_global_network)
    - [create_link](#create_link)
    - [create_site](#create_site)
    - [delete_connection](#delete_connection)
    - [delete_device](#delete_device)
    - [delete_global_network](#delete_global_network)
    - [delete_link](#delete_link)
    - [delete_site](#delete_site)
    - [deregister_transit_gateway](#deregister_transit_gateway)
    - [describe_global_networks](#describe_global_networks)
    - [disassociate_customer_gateway](#disassociate_customer_gateway)
    - [disassociate_link](#disassociate_link)
    - [disassociate_transit_gateway_connect_peer](#disassociate_transit_gateway_connect_peer)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_connections](#get_connections)
    - [get_customer_gateway_associations](#get_customer_gateway_associations)
    - [get_devices](#get_devices)
    - [get_link_associations](#get_link_associations)
    - [get_links](#get_links)
    - [get_sites](#get_sites)
    - [get_transit_gateway_connect_peer_associations](#get_transit_gateway_connect_peer_associations)
    - [get_transit_gateway_registrations](#get_transit_gateway_registrations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [register_transit_gateway](#register_transit_gateway)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_connection](#update_connection)
    - [update_device](#update_device)
    - [update_global_network](#update_global_network)
    - [update_link](#update_link)
    - [update_site](#update_site)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)

## NetworkManagerClient

Type annotations for `boto3.client("networkmanager")`

Can be used directly:

```python
from mypy_boto3_networkmanager.client import NetworkManagerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_networkmanager.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### associate_customer_gateway

Type annotations for `boto3.client("networkmanager").associate_customer_gateway` method.

[Client.associate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.associate_customer_gateway)

```python
def associate_customer_gateway(
    self,
    CustomerGatewayArn: str,
    GlobalNetworkId: str,
    DeviceId: str,
    LinkId: str = None
) -> AssociateCustomerGatewayResponseTypeDef:
    pass
```

### associate_link

Type annotations for `boto3.client("networkmanager").associate_link` method.

[Client.associate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.associate_link)

```python
def associate_link(
    self,
    GlobalNetworkId: str,
    DeviceId: str,
    LinkId: str
) -> AssociateLinkResponseTypeDef:
    pass
```

### associate_transit_gateway_connect_peer

Type annotations for `boto3.client("networkmanager").associate_transit_gateway_connect_peer` method.

[Client.associate_transit_gateway_connect_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.associate_transit_gateway_connect_peer)

```python
def associate_transit_gateway_connect_peer(
    self,
    GlobalNetworkId: str,
    TransitGatewayConnectPeerArn: str,
    DeviceId: str,
    LinkId: str = None
) -> AssociateTransitGatewayConnectPeerResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("networkmanager").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_connection

Type annotations for `boto3.client("networkmanager").create_connection` method.

[Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.create_connection)

```python
def create_connection(
    self,
    GlobalNetworkId: str,
    DeviceId: str,
    ConnectedDeviceId: str,
    LinkId: str = None,
    ConnectedLinkId: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateConnectionResponseTypeDef:
    pass
```

### create_device

Type annotations for `boto3.client("networkmanager").create_device` method.

[Client.create_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.create_device)

```python
def create_device(
    self,
    GlobalNetworkId: str,
    AWSLocation: "AWSLocationTypeDef" = None,
    Description: str = None,
    Type: str = None,
    Vendor: str = None,
    Model: str = None,
    SerialNumber: str = None,
    Location: "LocationTypeDef" = None,
    SiteId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDeviceResponseTypeDef:
    pass
```

### create_global_network

Type annotations for `boto3.client("networkmanager").create_global_network` method.

[Client.create_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.create_global_network)

```python
def create_global_network(
    self,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateGlobalNetworkResponseTypeDef:
    pass
```

### create_link

Type annotations for `boto3.client("networkmanager").create_link` method.

[Client.create_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.create_link)

```python
def create_link(
    self,
    GlobalNetworkId: str,
    Bandwidth: "BandwidthTypeDef",
    SiteId: str,
    Description: str = None,
    Type: str = None,
    Provider: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateLinkResponseTypeDef:
    pass
```

### create_site

Type annotations for `boto3.client("networkmanager").create_site` method.

[Client.create_site documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.create_site)

```python
def create_site(
    self,
    GlobalNetworkId: str,
    Description: str = None,
    Location: "LocationTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateSiteResponseTypeDef:
    pass
```

### delete_connection

Type annotations for `boto3.client("networkmanager").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.delete_connection)

```python
def delete_connection(
    self,
    GlobalNetworkId: str,
    ConnectionId: str
) -> DeleteConnectionResponseTypeDef:
    pass
```

### delete_device

Type annotations for `boto3.client("networkmanager").delete_device` method.

[Client.delete_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.delete_device)

```python
def delete_device(
    self,
    GlobalNetworkId: str,
    DeviceId: str
) -> DeleteDeviceResponseTypeDef:
    pass
```

### delete_global_network

Type annotations for `boto3.client("networkmanager").delete_global_network` method.

[Client.delete_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.delete_global_network)

```python
def delete_global_network(
    self,
    GlobalNetworkId: str
) -> DeleteGlobalNetworkResponseTypeDef:
    pass
```

### delete_link

Type annotations for `boto3.client("networkmanager").delete_link` method.

[Client.delete_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.delete_link)

```python
def delete_link(
    self,
    GlobalNetworkId: str,
    LinkId: str
) -> DeleteLinkResponseTypeDef:
    pass
```

### delete_site

Type annotations for `boto3.client("networkmanager").delete_site` method.

[Client.delete_site documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.delete_site)

```python
def delete_site(
    self,
    GlobalNetworkId: str,
    SiteId: str
) -> DeleteSiteResponseTypeDef:
    pass
```

### deregister_transit_gateway

Type annotations for `boto3.client("networkmanager").deregister_transit_gateway` method.

[Client.deregister_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.deregister_transit_gateway)

```python
def deregister_transit_gateway(
    self,
    GlobalNetworkId: str,
    TransitGatewayArn: str
) -> DeregisterTransitGatewayResponseTypeDef:
    pass
```

### describe_global_networks

Type annotations for `boto3.client("networkmanager").describe_global_networks` method.

[Client.describe_global_networks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.describe_global_networks)

```python
def describe_global_networks(
    self,
    GlobalNetworkIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeGlobalNetworksResponseTypeDef:
    pass
```

### disassociate_customer_gateway

Type annotations for `boto3.client("networkmanager").disassociate_customer_gateway` method.

[Client.disassociate_customer_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.disassociate_customer_gateway)

```python
def disassociate_customer_gateway(
    self,
    GlobalNetworkId: str,
    CustomerGatewayArn: str
) -> DisassociateCustomerGatewayResponseTypeDef:
    pass
```

### disassociate_link

Type annotations for `boto3.client("networkmanager").disassociate_link` method.

[Client.disassociate_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.disassociate_link)

```python
def disassociate_link(
    self,
    GlobalNetworkId: str,
    DeviceId: str,
    LinkId: str
) -> DisassociateLinkResponseTypeDef:
    pass
```

### disassociate_transit_gateway_connect_peer

Type annotations for `boto3.client("networkmanager").disassociate_transit_gateway_connect_peer` method.

[Client.disassociate_transit_gateway_connect_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.disassociate_transit_gateway_connect_peer)

```python
def disassociate_transit_gateway_connect_peer(
    self,
    GlobalNetworkId: str,
    TransitGatewayConnectPeerArn: str
) -> DisassociateTransitGatewayConnectPeerResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("networkmanager").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.generate_presigned_url)

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

### get_connections

Type annotations for `boto3.client("networkmanager").get_connections` method.

[Client.get_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_connections)

```python
def get_connections(
    self,
    GlobalNetworkId: str,
    ConnectionIds: List[str] = None,
    DeviceId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetConnectionsResponseTypeDef:
    pass
```

### get_customer_gateway_associations

Type annotations for `boto3.client("networkmanager").get_customer_gateway_associations` method.

[Client.get_customer_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_customer_gateway_associations)

```python
def get_customer_gateway_associations(
    self,
    GlobalNetworkId: str,
    CustomerGatewayArns: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetCustomerGatewayAssociationsResponseTypeDef:
    pass
```

### get_devices

Type annotations for `boto3.client("networkmanager").get_devices` method.

[Client.get_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_devices)

```python
def get_devices(
    self,
    GlobalNetworkId: str,
    DeviceIds: List[str] = None,
    SiteId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetDevicesResponseTypeDef:
    pass
```

### get_link_associations

Type annotations for `boto3.client("networkmanager").get_link_associations` method.

[Client.get_link_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_link_associations)

```python
def get_link_associations(
    self,
    GlobalNetworkId: str,
    DeviceId: str = None,
    LinkId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetLinkAssociationsResponseTypeDef:
    pass
```

### get_links

Type annotations for `boto3.client("networkmanager").get_links` method.

[Client.get_links documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_links)

```python
def get_links(
    self,
    GlobalNetworkId: str,
    LinkIds: List[str] = None,
    SiteId: str = None,
    Type: str = None,
    Provider: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetLinksResponseTypeDef:
    pass
```

### get_sites

Type annotations for `boto3.client("networkmanager").get_sites` method.

[Client.get_sites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_sites)

```python
def get_sites(
    self,
    GlobalNetworkId: str,
    SiteIds: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetSitesResponseTypeDef:
    pass
```

### get_transit_gateway_connect_peer_associations

Type annotations for `boto3.client("networkmanager").get_transit_gateway_connect_peer_associations` method.

[Client.get_transit_gateway_connect_peer_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_connect_peer_associations)

```python
def get_transit_gateway_connect_peer_associations(
    self,
    GlobalNetworkId: str,
    TransitGatewayConnectPeerArns: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetTransitGatewayConnectPeerAssociationsResponseTypeDef:
    pass
```

### get_transit_gateway_registrations

Type annotations for `boto3.client("networkmanager").get_transit_gateway_registrations` method.

[Client.get_transit_gateway_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_registrations)

```python
def get_transit_gateway_registrations(
    self,
    GlobalNetworkId: str,
    TransitGatewayArns: List[str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetTransitGatewayRegistrationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("networkmanager").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### register_transit_gateway

Type annotations for `boto3.client("networkmanager").register_transit_gateway` method.

[Client.register_transit_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.register_transit_gateway)

```python
def register_transit_gateway(
    self,
    GlobalNetworkId: str,
    TransitGatewayArn: str
) -> RegisterTransitGatewayResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("networkmanager").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("networkmanager").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_connection

Type annotations for `boto3.client("networkmanager").update_connection` method.

[Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.update_connection)

```python
def update_connection(
    self,
    GlobalNetworkId: str,
    ConnectionId: str,
    LinkId: str = None,
    ConnectedLinkId: str = None,
    Description: str = None
) -> UpdateConnectionResponseTypeDef:
    pass
```

### update_device

Type annotations for `boto3.client("networkmanager").update_device` method.

[Client.update_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.update_device)

```python
def update_device(
    self,
    GlobalNetworkId: str,
    DeviceId: str,
    AWSLocation: "AWSLocationTypeDef" = None,
    Description: str = None,
    Type: str = None,
    Vendor: str = None,
    Model: str = None,
    SerialNumber: str = None,
    Location: "LocationTypeDef" = None,
    SiteId: str = None
) -> UpdateDeviceResponseTypeDef:
    pass
```

### update_global_network

Type annotations for `boto3.client("networkmanager").update_global_network` method.

[Client.update_global_network documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.update_global_network)

```python
def update_global_network(
    self,
    GlobalNetworkId: str,
    Description: str = None
) -> UpdateGlobalNetworkResponseTypeDef:
    pass
```

### update_link

Type annotations for `boto3.client("networkmanager").update_link` method.

[Client.update_link documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.update_link)

```python
def update_link(
    self,
    GlobalNetworkId: str,
    LinkId: str,
    Description: str = None,
    Type: str = None,
    Bandwidth: "BandwidthTypeDef" = None,
    Provider: str = None
) -> UpdateLinkResponseTypeDef:
    pass
```

### update_site

Type annotations for `boto3.client("networkmanager").update_site` method.

[Client.update_site documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Client.update_site)

```python
def update_site(
    self,
    GlobalNetworkId: str,
    SiteId: str,
    Description: str = None,
    Location: "LocationTypeDef" = None
) -> UpdateSiteResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.DescribeGlobalNetworks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeGlobalNetworksPaginatorName
) -> DescribeGlobalNetworksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections)

```python
@overload
def get_paginator(
    self,
    operation_name: GetConnectionsPaginatorName
) -> GetConnectionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetCustomerGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetCustomerGatewayAssociationsPaginatorName
) -> GetCustomerGatewayAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDevicesPaginatorName
) -> GetDevicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetLinkAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetLinkAssociationsPaginatorName
) -> GetLinkAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)

```python
@overload
def get_paginator(
    self,
    operation_name: GetLinksPaginatorName
) -> GetLinksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetSites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)

```python
@overload
def get_paginator(
    self,
    operation_name: GetSitesPaginatorName
) -> GetSitesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetTransitGatewayConnectPeerAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTransitGatewayConnectPeerAssociationsPaginatorName
) -> GetTransitGatewayConnectPeerAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("networkmanager").get_paginator` method.

[Paginator.GetTransitGatewayRegistrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetTransitGatewayRegistrationsPaginatorName
) -> GetTransitGatewayRegistrationsPaginator:
    pass
```