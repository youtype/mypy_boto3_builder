# Structures for boto3 NetworkManager module

> [Index](../index.md) > [NetworkManager](./index.md) > Structures

Auto-generated documentation for [NetworkManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html#NetworkManager)
type annotations stubs module [mypy_boto3_networkmanager](https://pypi.org/project/mypy-boto3-networkmanager/).

- [Structures for boto3 NetworkManager module](#structures-for-boto3-networkmanager-module)
  - [AWSLocationTypeDef](#awslocationtypedef)
  - [BandwidthTypeDef](#bandwidthtypedef)
  - [ConnectionTypeDef](#connectiontypedef)
  - [CustomerGatewayAssociationTypeDef](#customergatewayassociationtypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [GlobalNetworkTypeDef](#globalnetworktypedef)
  - [LinkAssociationTypeDef](#linkassociationtypedef)
  - [LinkTypeDef](#linktypedef)
  - [LocationTypeDef](#locationtypedef)
  - [SiteTypeDef](#sitetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TransitGatewayConnectPeerAssociationTypeDef](#transitgatewayconnectpeerassociationtypedef)
  - [TransitGatewayRegistrationStateReasonTypeDef](#transitgatewayregistrationstatereasontypedef)
  - [TransitGatewayRegistrationTypeDef](#transitgatewayregistrationtypedef)
  - [AssociateCustomerGatewayResponseTypeDef](#associatecustomergatewayresponsetypedef)
  - [AssociateLinkResponseTypeDef](#associatelinkresponsetypedef)
  - [AssociateTransitGatewayConnectPeerResponseTypeDef](#associatetransitgatewayconnectpeerresponsetypedef)
  - [CreateConnectionResponseTypeDef](#createconnectionresponsetypedef)
  - [CreateDeviceResponseTypeDef](#createdeviceresponsetypedef)
  - [CreateGlobalNetworkResponseTypeDef](#createglobalnetworkresponsetypedef)
  - [CreateLinkResponseTypeDef](#createlinkresponsetypedef)
  - [CreateSiteResponseTypeDef](#createsiteresponsetypedef)
  - [DeleteConnectionResponseTypeDef](#deleteconnectionresponsetypedef)
  - [DeleteDeviceResponseTypeDef](#deletedeviceresponsetypedef)
  - [DeleteGlobalNetworkResponseTypeDef](#deleteglobalnetworkresponsetypedef)
  - [DeleteLinkResponseTypeDef](#deletelinkresponsetypedef)
  - [DeleteSiteResponseTypeDef](#deletesiteresponsetypedef)
  - [DeregisterTransitGatewayResponseTypeDef](#deregistertransitgatewayresponsetypedef)
  - [DescribeGlobalNetworksResponseTypeDef](#describeglobalnetworksresponsetypedef)
  - [DisassociateCustomerGatewayResponseTypeDef](#disassociatecustomergatewayresponsetypedef)
  - [DisassociateLinkResponseTypeDef](#disassociatelinkresponsetypedef)
  - [DisassociateTransitGatewayConnectPeerResponseTypeDef](#disassociatetransitgatewayconnectpeerresponsetypedef)
  - [GetConnectionsResponseTypeDef](#getconnectionsresponsetypedef)
  - [GetCustomerGatewayAssociationsResponseTypeDef](#getcustomergatewayassociationsresponsetypedef)
  - [GetDevicesResponseTypeDef](#getdevicesresponsetypedef)
  - [GetLinkAssociationsResponseTypeDef](#getlinkassociationsresponsetypedef)
  - [GetLinksResponseTypeDef](#getlinksresponsetypedef)
  - [GetSitesResponseTypeDef](#getsitesresponsetypedef)
  - [GetTransitGatewayConnectPeerAssociationsResponseTypeDef](#gettransitgatewayconnectpeerassociationsresponsetypedef)
  - [GetTransitGatewayRegistrationsResponseTypeDef](#gettransitgatewayregistrationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RegisterTransitGatewayResponseTypeDef](#registertransitgatewayresponsetypedef)
  - [UpdateConnectionResponseTypeDef](#updateconnectionresponsetypedef)
  - [UpdateDeviceResponseTypeDef](#updatedeviceresponsetypedef)
  - [UpdateGlobalNetworkResponseTypeDef](#updateglobalnetworkresponsetypedef)
  - [UpdateLinkResponseTypeDef](#updatelinkresponsetypedef)
  - [UpdateSiteResponseTypeDef](#updatesiteresponsetypedef)

## AWSLocationTypeDef

```python
from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef
```




Optional fields:
- `Zone`: `str`
- `SubnetArn`: `str`


## BandwidthTypeDef

```python
from mypy_boto3_networkmanager.type_defs import BandwidthTypeDef
```




Optional fields:
- `UploadSpeed`: `int`
- `DownloadSpeed`: `int`


## ConnectionTypeDef

```python
from mypy_boto3_networkmanager.type_defs import ConnectionTypeDef
```




Optional fields:
- `ConnectionId`: `str`
- `ConnectionArn`: `str`
- `GlobalNetworkId`: `str`
- `DeviceId`: `str`
- `ConnectedDeviceId`: `str`
- `LinkId`: `str`
- `ConnectedLinkId`: `str`
- `Description`: `str`
- `CreatedAt`: `datetime`
- `State`: `ConnectionState`
- `Tags`: `List["TagTypeDef"]`


## CustomerGatewayAssociationTypeDef

```python
from mypy_boto3_networkmanager.type_defs import CustomerGatewayAssociationTypeDef
```




Optional fields:
- `CustomerGatewayArn`: `str`
- `GlobalNetworkId`: `str`
- `DeviceId`: `str`
- `LinkId`: `str`
- `State`: `CustomerGatewayAssociationState`


## DeviceTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeviceTypeDef
```




Optional fields:
- `DeviceId`: `str`
- `DeviceArn`: `str`
- `GlobalNetworkId`: `str`
- `AWSLocation`: `"AWSLocationTypeDef"`
- `Description`: `str`
- `Type`: `str`
- `Vendor`: `str`
- `Model`: `str`
- `SerialNumber`: `str`
- `Location`: `"LocationTypeDef"`
- `SiteId`: `str`
- `CreatedAt`: `datetime`
- `State`: `DeviceState`
- `Tags`: `List["TagTypeDef"]`


## GlobalNetworkTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GlobalNetworkTypeDef
```




Optional fields:
- `GlobalNetworkId`: `str`
- `GlobalNetworkArn`: `str`
- `Description`: `str`
- `CreatedAt`: `datetime`
- `State`: `GlobalNetworkState`
- `Tags`: `List["TagTypeDef"]`


## LinkAssociationTypeDef

```python
from mypy_boto3_networkmanager.type_defs import LinkAssociationTypeDef
```




Optional fields:
- `GlobalNetworkId`: `str`
- `DeviceId`: `str`
- `LinkId`: `str`
- `LinkAssociationState`: `LinkAssociationState`


## LinkTypeDef

```python
from mypy_boto3_networkmanager.type_defs import LinkTypeDef
```




Optional fields:
- `LinkId`: `str`
- `LinkArn`: `str`
- `GlobalNetworkId`: `str`
- `SiteId`: `str`
- `Description`: `str`
- `Type`: `str`
- `Bandwidth`: `"BandwidthTypeDef"`
- `Provider`: `str`
- `CreatedAt`: `datetime`
- `State`: `LinkState`
- `Tags`: `List["TagTypeDef"]`


## LocationTypeDef

```python
from mypy_boto3_networkmanager.type_defs import LocationTypeDef
```




Optional fields:
- `Address`: `str`
- `Latitude`: `str`
- `Longitude`: `str`


## SiteTypeDef

```python
from mypy_boto3_networkmanager.type_defs import SiteTypeDef
```




Optional fields:
- `SiteId`: `str`
- `SiteArn`: `str`
- `GlobalNetworkId`: `str`
- `Description`: `str`
- `Location`: `"LocationTypeDef"`
- `CreatedAt`: `datetime`
- `State`: `SiteState`
- `Tags`: `List["TagTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_networkmanager.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TransitGatewayConnectPeerAssociationTypeDef

```python
from mypy_boto3_networkmanager.type_defs import TransitGatewayConnectPeerAssociationTypeDef
```




Optional fields:
- `TransitGatewayConnectPeerArn`: `str`
- `GlobalNetworkId`: `str`
- `DeviceId`: `str`
- `LinkId`: `str`
- `State`: `TransitGatewayConnectPeerAssociationState`


## TransitGatewayRegistrationStateReasonTypeDef

```python
from mypy_boto3_networkmanager.type_defs import TransitGatewayRegistrationStateReasonTypeDef
```




Optional fields:
- `Code`: `TransitGatewayRegistrationState`
- `Message`: `str`


## TransitGatewayRegistrationTypeDef

```python
from mypy_boto3_networkmanager.type_defs import TransitGatewayRegistrationTypeDef
```




Optional fields:
- `GlobalNetworkId`: `str`
- `TransitGatewayArn`: `str`
- `State`: `"TransitGatewayRegistrationStateReasonTypeDef"`


## AssociateCustomerGatewayResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import AssociateCustomerGatewayResponseTypeDef
```




Optional fields:
- `CustomerGatewayAssociation`: `"CustomerGatewayAssociationTypeDef"`


## AssociateLinkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import AssociateLinkResponseTypeDef
```




Optional fields:
- `LinkAssociation`: `"LinkAssociationTypeDef"`


## AssociateTransitGatewayConnectPeerResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import AssociateTransitGatewayConnectPeerResponseTypeDef
```




Optional fields:
- `TransitGatewayConnectPeerAssociation`: `"TransitGatewayConnectPeerAssociationTypeDef"`


## CreateConnectionResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import CreateConnectionResponseTypeDef
```




Optional fields:
- `Connection`: `"ConnectionTypeDef"`


## CreateDeviceResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import CreateDeviceResponseTypeDef
```




Optional fields:
- `Device`: `"DeviceTypeDef"`


## CreateGlobalNetworkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import CreateGlobalNetworkResponseTypeDef
```




Optional fields:
- `GlobalNetwork`: `"GlobalNetworkTypeDef"`


## CreateLinkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import CreateLinkResponseTypeDef
```




Optional fields:
- `Link`: `"LinkTypeDef"`


## CreateSiteResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import CreateSiteResponseTypeDef
```




Optional fields:
- `Site`: `"SiteTypeDef"`


## DeleteConnectionResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeleteConnectionResponseTypeDef
```




Optional fields:
- `Connection`: `"ConnectionTypeDef"`


## DeleteDeviceResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeleteDeviceResponseTypeDef
```




Optional fields:
- `Device`: `"DeviceTypeDef"`


## DeleteGlobalNetworkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeleteGlobalNetworkResponseTypeDef
```




Optional fields:
- `GlobalNetwork`: `"GlobalNetworkTypeDef"`


## DeleteLinkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeleteLinkResponseTypeDef
```




Optional fields:
- `Link`: `"LinkTypeDef"`


## DeleteSiteResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeleteSiteResponseTypeDef
```




Optional fields:
- `Site`: `"SiteTypeDef"`


## DeregisterTransitGatewayResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DeregisterTransitGatewayResponseTypeDef
```




Optional fields:
- `TransitGatewayRegistration`: `"TransitGatewayRegistrationTypeDef"`


## DescribeGlobalNetworksResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DescribeGlobalNetworksResponseTypeDef
```




Optional fields:
- `GlobalNetworks`: `List["GlobalNetworkTypeDef"]`
- `NextToken`: `str`


## DisassociateCustomerGatewayResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DisassociateCustomerGatewayResponseTypeDef
```




Optional fields:
- `CustomerGatewayAssociation`: `"CustomerGatewayAssociationTypeDef"`


## DisassociateLinkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DisassociateLinkResponseTypeDef
```




Optional fields:
- `LinkAssociation`: `"LinkAssociationTypeDef"`


## DisassociateTransitGatewayConnectPeerResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import DisassociateTransitGatewayConnectPeerResponseTypeDef
```




Optional fields:
- `TransitGatewayConnectPeerAssociation`: `"TransitGatewayConnectPeerAssociationTypeDef"`


## GetConnectionsResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetConnectionsResponseTypeDef
```




Optional fields:
- `Connections`: `List["ConnectionTypeDef"]`
- `NextToken`: `str`


## GetCustomerGatewayAssociationsResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetCustomerGatewayAssociationsResponseTypeDef
```




Optional fields:
- `CustomerGatewayAssociations`: `List["CustomerGatewayAssociationTypeDef"]`
- `NextToken`: `str`


## GetDevicesResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetDevicesResponseTypeDef
```




Optional fields:
- `Devices`: `List["DeviceTypeDef"]`
- `NextToken`: `str`


## GetLinkAssociationsResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetLinkAssociationsResponseTypeDef
```




Optional fields:
- `LinkAssociations`: `List["LinkAssociationTypeDef"]`
- `NextToken`: `str`


## GetLinksResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetLinksResponseTypeDef
```




Optional fields:
- `Links`: `List["LinkTypeDef"]`
- `NextToken`: `str`


## GetSitesResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetSitesResponseTypeDef
```




Optional fields:
- `Sites`: `List["SiteTypeDef"]`
- `NextToken`: `str`


## GetTransitGatewayConnectPeerAssociationsResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetTransitGatewayConnectPeerAssociationsResponseTypeDef
```




Optional fields:
- `TransitGatewayConnectPeerAssociations`: `List["TransitGatewayConnectPeerAssociationTypeDef"]`
- `NextToken`: `str`


## GetTransitGatewayRegistrationsResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import GetTransitGatewayRegistrationsResponseTypeDef
```




Optional fields:
- `TransitGatewayRegistrations`: `List["TransitGatewayRegistrationTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `TagList`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_networkmanager.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RegisterTransitGatewayResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import RegisterTransitGatewayResponseTypeDef
```




Optional fields:
- `TransitGatewayRegistration`: `"TransitGatewayRegistrationTypeDef"`


## UpdateConnectionResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import UpdateConnectionResponseTypeDef
```




Optional fields:
- `Connection`: `"ConnectionTypeDef"`


## UpdateDeviceResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import UpdateDeviceResponseTypeDef
```




Optional fields:
- `Device`: `"DeviceTypeDef"`


## UpdateGlobalNetworkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import UpdateGlobalNetworkResponseTypeDef
```




Optional fields:
- `GlobalNetwork`: `"GlobalNetworkTypeDef"`


## UpdateLinkResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import UpdateLinkResponseTypeDef
```




Optional fields:
- `Link`: `"LinkTypeDef"`


## UpdateSiteResponseTypeDef

```python
from mypy_boto3_networkmanager.type_defs import UpdateSiteResponseTypeDef
```




Optional fields:
- `Site`: `"SiteTypeDef"`

