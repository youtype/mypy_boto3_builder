# Type annotations for boto3 NetworkManager module

> [Index](../index.md) > NetworkManager

Auto-generated documentation for [NetworkManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager)
type annotations stubs module [mypy_boto3_networkmanager](https://pypi.org/project/mypy-boto3-networkmanager/).

```bash
pip install mypy-boto3-networkmanager
```

- [Type annotations for boto3 NetworkManager module](#type-annotations-for-boto3-networkmanager-module)
  - [NetworkManagerClient](#networkmanagerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## NetworkManagerClient

Type annotations for  `boto3.client("networkmanager")` as [NetworkManagerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_networkmanager.client import NetworkManagerClient
```


NetworkManagerClient [exceptions](./client.md#exceptions)



### Methods
- [associate_customer_gateway](./client.md#associate-customer-gateway)
- [associate_link](./client.md#associate-link)
- [associate_transit_gateway_connect_peer](./client.md#associate-transit-gateway-connect-peer)
- [can_paginate](./client.md#can-paginate)
- [create_connection](./client.md#create-connection)
- [create_device](./client.md#create-device)
- [create_global_network](./client.md#create-global-network)
- [create_link](./client.md#create-link)
- [create_site](./client.md#create-site)
- [delete_connection](./client.md#delete-connection)
- [delete_device](./client.md#delete-device)
- [delete_global_network](./client.md#delete-global-network)
- [delete_link](./client.md#delete-link)
- [delete_site](./client.md#delete-site)
- [deregister_transit_gateway](./client.md#deregister-transit-gateway)
- [describe_global_networks](./client.md#describe-global-networks)
- [disassociate_customer_gateway](./client.md#disassociate-customer-gateway)
- [disassociate_link](./client.md#disassociate-link)
- [disassociate_transit_gateway_connect_peer](./client.md#disassociate-transit-gateway-connect-peer)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_connections](./client.md#get-connections)
- [get_customer_gateway_associations](./client.md#get-customer-gateway-associations)
- [get_devices](./client.md#get-devices)
- [get_link_associations](./client.md#get-link-associations)
- [get_links](./client.md#get-links)
- [get_paginator](./client.md#get-paginator)
- [get_sites](./client.md#get-sites)
- [get_transit_gateway_connect_peer_associations](./client.md#get-transit-gateway-connect-peer-associations)
- [get_transit_gateway_registrations](./client.md#get-transit-gateway-registrations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [register_transit_gateway](./client.md#register-transit-gateway)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_connection](./client.md#update-connection)
- [update_device](./client.md#update-device)
- [update_global_network](./client.md#update-global-network)
- [update_link](./client.md#update-link)
- [update_site](./client.md#update-site)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("networkmanager").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_networkmanager.paginators import DescribeGlobalNetworksPaginator, ...
```

- [DescribeGlobalNetworksPaginator](./paginators.md#describeglobalnetworkspaginator)
- [GetConnectionsPaginator](./paginators.md#getconnectionspaginator)
- [GetCustomerGatewayAssociationsPaginator](./paginators.md#getcustomergatewayassociationspaginator)
- [GetDevicesPaginator](./paginators.md#getdevicespaginator)
- [GetLinkAssociationsPaginator](./paginators.md#getlinkassociationspaginator)
- [GetLinksPaginator](./paginators.md#getlinkspaginator)
- [GetSitesPaginator](./paginators.md#getsitespaginator)
- [GetTransitGatewayConnectPeerAssociationsPaginator](./paginators.md#gettransitgatewayconnectpeerassociationspaginator)
- [GetTransitGatewayRegistrationsPaginator](./paginators.md#gettransitgatewayregistrationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_networkmanager.literals import ConnectionState, ...
```

- [ConnectionState](./literals.md#connectionstate)
- [CustomerGatewayAssociationState](./literals.md#customergatewayassociationstate)
- [DescribeGlobalNetworksPaginatorName](./literals.md#describeglobalnetworkspaginatorname)
- [DeviceState](./literals.md#devicestate)
- [GetConnectionsPaginatorName](./literals.md#getconnectionspaginatorname)
- [GetCustomerGatewayAssociationsPaginatorName](./literals.md#getcustomergatewayassociationspaginatorname)
- [GetDevicesPaginatorName](./literals.md#getdevicespaginatorname)
- [GetLinkAssociationsPaginatorName](./literals.md#getlinkassociationspaginatorname)
- [GetLinksPaginatorName](./literals.md#getlinkspaginatorname)
- [GetSitesPaginatorName](./literals.md#getsitespaginatorname)
- [GetTransitGatewayConnectPeerAssociationsPaginatorName](./literals.md#gettransitgatewayconnectpeerassociationspaginatorname)
- [GetTransitGatewayRegistrationsPaginatorName](./literals.md#gettransitgatewayregistrationspaginatorname)
- [GlobalNetworkState](./literals.md#globalnetworkstate)
- [LinkAssociationState](./literals.md#linkassociationstate)
- [LinkState](./literals.md#linkstate)
- [SiteState](./literals.md#sitestate)
- [TransitGatewayConnectPeerAssociationState](./literals.md#transitgatewayconnectpeerassociationstate)
- [TransitGatewayRegistrationState](./literals.md#transitgatewayregistrationstate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef, ...
```

- [AWSLocationTypeDef](./type_defs.md#awslocationtypedef)
- [BandwidthTypeDef](./type_defs.md#bandwidthtypedef)
- [ConnectionTypeDef](./type_defs.md#connectiontypedef)
- [CustomerGatewayAssociationTypeDef](./type_defs.md#customergatewayassociationtypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [GlobalNetworkTypeDef](./type_defs.md#globalnetworktypedef)
- [LinkAssociationTypeDef](./type_defs.md#linkassociationtypedef)
- [LinkTypeDef](./type_defs.md#linktypedef)
- [LocationTypeDef](./type_defs.md#locationtypedef)
- [SiteTypeDef](./type_defs.md#sitetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TransitGatewayConnectPeerAssociationTypeDef](./type_defs.md#transitgatewayconnectpeerassociationtypedef)
- [TransitGatewayRegistrationStateReasonTypeDef](./type_defs.md#transitgatewayregistrationstatereasontypedef)
- [TransitGatewayRegistrationTypeDef](./type_defs.md#transitgatewayregistrationtypedef)
- [AssociateCustomerGatewayResponseTypeDef](./type_defs.md#associatecustomergatewayresponsetypedef)
- [AssociateLinkResponseTypeDef](./type_defs.md#associatelinkresponsetypedef)
- [AssociateTransitGatewayConnectPeerResponseTypeDef](./type_defs.md#associatetransitgatewayconnectpeerresponsetypedef)
- [CreateConnectionResponseTypeDef](./type_defs.md#createconnectionresponsetypedef)
- [CreateDeviceResponseTypeDef](./type_defs.md#createdeviceresponsetypedef)
- [CreateGlobalNetworkResponseTypeDef](./type_defs.md#createglobalnetworkresponsetypedef)
- [CreateLinkResponseTypeDef](./type_defs.md#createlinkresponsetypedef)
- [CreateSiteResponseTypeDef](./type_defs.md#createsiteresponsetypedef)
- [DeleteConnectionResponseTypeDef](./type_defs.md#deleteconnectionresponsetypedef)
- [DeleteDeviceResponseTypeDef](./type_defs.md#deletedeviceresponsetypedef)
- [DeleteGlobalNetworkResponseTypeDef](./type_defs.md#deleteglobalnetworkresponsetypedef)
- [DeleteLinkResponseTypeDef](./type_defs.md#deletelinkresponsetypedef)
- [DeleteSiteResponseTypeDef](./type_defs.md#deletesiteresponsetypedef)
- [DeregisterTransitGatewayResponseTypeDef](./type_defs.md#deregistertransitgatewayresponsetypedef)
- [DescribeGlobalNetworksResponseTypeDef](./type_defs.md#describeglobalnetworksresponsetypedef)
- [DisassociateCustomerGatewayResponseTypeDef](./type_defs.md#disassociatecustomergatewayresponsetypedef)
- [DisassociateLinkResponseTypeDef](./type_defs.md#disassociatelinkresponsetypedef)
- [DisassociateTransitGatewayConnectPeerResponseTypeDef](./type_defs.md#disassociatetransitgatewayconnectpeerresponsetypedef)
- [GetConnectionsResponseTypeDef](./type_defs.md#getconnectionsresponsetypedef)
- [GetCustomerGatewayAssociationsResponseTypeDef](./type_defs.md#getcustomergatewayassociationsresponsetypedef)
- [GetDevicesResponseTypeDef](./type_defs.md#getdevicesresponsetypedef)
- [GetLinkAssociationsResponseTypeDef](./type_defs.md#getlinkassociationsresponsetypedef)
- [GetLinksResponseTypeDef](./type_defs.md#getlinksresponsetypedef)
- [GetSitesResponseTypeDef](./type_defs.md#getsitesresponsetypedef)
- [GetTransitGatewayConnectPeerAssociationsResponseTypeDef](./type_defs.md#gettransitgatewayconnectpeerassociationsresponsetypedef)
- [GetTransitGatewayRegistrationsResponseTypeDef](./type_defs.md#gettransitgatewayregistrationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RegisterTransitGatewayResponseTypeDef](./type_defs.md#registertransitgatewayresponsetypedef)
- [UpdateConnectionResponseTypeDef](./type_defs.md#updateconnectionresponsetypedef)
- [UpdateDeviceResponseTypeDef](./type_defs.md#updatedeviceresponsetypedef)
- [UpdateGlobalNetworkResponseTypeDef](./type_defs.md#updateglobalnetworkresponsetypedef)
- [UpdateLinkResponseTypeDef](./type_defs.md#updatelinkresponsetypedef)
- [UpdateSiteResponseTypeDef](./type_defs.md#updatesiteresponsetypedef)
