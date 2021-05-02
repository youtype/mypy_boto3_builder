# Structures for boto3 DirectConnect module

> [Index](../index.md) > [DirectConnect](./index.md) > Structures

Auto-generated documentation for [DirectConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect)
type annotations stubs module [mypy_boto3_directconnect](https://pypi.org/project/mypy-boto3-directconnect/).

- [Structures for boto3 DirectConnect module](#structures-for-boto3-directconnect-module)
  - [AcceptDirectConnectGatewayAssociationProposalResultTypeDef](#acceptdirectconnectgatewayassociationproposalresulttypedef)
  - [AllocateTransitVirtualInterfaceResultTypeDef](#allocatetransitvirtualinterfaceresulttypedef)
  - [AssociateMacSecKeyResponseTypeDef](#associatemacseckeyresponsetypedef)
  - [AssociatedGatewayTypeDef](#associatedgatewaytypedef)
  - [BGPPeerTypeDef](#bgppeertypedef)
  - [ConfirmConnectionResponseTypeDef](#confirmconnectionresponsetypedef)
  - [ConfirmPrivateVirtualInterfaceResponseTypeDef](#confirmprivatevirtualinterfaceresponsetypedef)
  - [ConfirmPublicVirtualInterfaceResponseTypeDef](#confirmpublicvirtualinterfaceresponsetypedef)
  - [ConfirmTransitVirtualInterfaceResponseTypeDef](#confirmtransitvirtualinterfaceresponsetypedef)
  - [ConnectionTypeDef](#connectiontypedef)
  - [ConnectionsTypeDef](#connectionstypedef)
  - [CreateBGPPeerResponseTypeDef](#createbgppeerresponsetypedef)
  - [CreateDirectConnectGatewayAssociationProposalResultTypeDef](#createdirectconnectgatewayassociationproposalresulttypedef)
  - [CreateDirectConnectGatewayAssociationResultTypeDef](#createdirectconnectgatewayassociationresulttypedef)
  - [CreateDirectConnectGatewayResultTypeDef](#createdirectconnectgatewayresulttypedef)
  - [CreateTransitVirtualInterfaceResultTypeDef](#createtransitvirtualinterfaceresulttypedef)
  - [DeleteBGPPeerResponseTypeDef](#deletebgppeerresponsetypedef)
  - [DeleteDirectConnectGatewayAssociationProposalResultTypeDef](#deletedirectconnectgatewayassociationproposalresulttypedef)
  - [DeleteDirectConnectGatewayAssociationResultTypeDef](#deletedirectconnectgatewayassociationresulttypedef)
  - [DeleteDirectConnectGatewayResultTypeDef](#deletedirectconnectgatewayresulttypedef)
  - [DeleteInterconnectResponseTypeDef](#deleteinterconnectresponsetypedef)
  - [DeleteVirtualInterfaceResponseTypeDef](#deletevirtualinterfaceresponsetypedef)
  - [DescribeConnectionLoaResponseTypeDef](#describeconnectionloaresponsetypedef)
  - [DescribeDirectConnectGatewayAssociationProposalsResultTypeDef](#describedirectconnectgatewayassociationproposalsresulttypedef)
  - [DescribeDirectConnectGatewayAssociationsResultTypeDef](#describedirectconnectgatewayassociationsresulttypedef)
  - [DescribeDirectConnectGatewayAttachmentsResultTypeDef](#describedirectconnectgatewayattachmentsresulttypedef)
  - [DescribeDirectConnectGatewaysResultTypeDef](#describedirectconnectgatewaysresulttypedef)
  - [DescribeInterconnectLoaResponseTypeDef](#describeinterconnectloaresponsetypedef)
  - [DescribeTagsResponseTypeDef](#describetagsresponsetypedef)
  - [DirectConnectGatewayAssociationProposalTypeDef](#directconnectgatewayassociationproposaltypedef)
  - [DirectConnectGatewayAssociationTypeDef](#directconnectgatewayassociationtypedef)
  - [DirectConnectGatewayAttachmentTypeDef](#directconnectgatewayattachmenttypedef)
  - [DirectConnectGatewayTypeDef](#directconnectgatewaytypedef)
  - [DisassociateMacSecKeyResponseTypeDef](#disassociatemacseckeyresponsetypedef)
  - [InterconnectTypeDef](#interconnecttypedef)
  - [InterconnectsTypeDef](#interconnectstypedef)
  - [LagTypeDef](#lagtypedef)
  - [LagsTypeDef](#lagstypedef)
  - [ListVirtualInterfaceTestHistoryResponseTypeDef](#listvirtualinterfacetesthistoryresponsetypedef)
  - [LoaTypeDef](#loatypedef)
  - [LocationTypeDef](#locationtypedef)
  - [LocationsTypeDef](#locationstypedef)
  - [MacSecKeyTypeDef](#macseckeytypedef)
  - [NewBGPPeerTypeDef](#newbgppeertypedef)
  - [NewPrivateVirtualInterfaceAllocationTypeDef](#newprivatevirtualinterfaceallocationtypedef)
  - [NewPrivateVirtualInterfaceTypeDef](#newprivatevirtualinterfacetypedef)
  - [NewPublicVirtualInterfaceAllocationTypeDef](#newpublicvirtualinterfaceallocationtypedef)
  - [NewPublicVirtualInterfaceTypeDef](#newpublicvirtualinterfacetypedef)
  - [NewTransitVirtualInterfaceAllocationTypeDef](#newtransitvirtualinterfaceallocationtypedef)
  - [NewTransitVirtualInterfaceTypeDef](#newtransitvirtualinterfacetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResourceTagTypeDef](#resourcetagtypedef)
  - [RouteFilterPrefixTypeDef](#routefilterprefixtypedef)
  - [StartBgpFailoverTestResponseTypeDef](#startbgpfailovertestresponsetypedef)
  - [StopBgpFailoverTestResponseTypeDef](#stopbgpfailovertestresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateDirectConnectGatewayAssociationResultTypeDef](#updatedirectconnectgatewayassociationresulttypedef)
  - [VirtualGatewayTypeDef](#virtualgatewaytypedef)
  - [VirtualGatewaysTypeDef](#virtualgatewaystypedef)
  - [VirtualInterfaceTestHistoryTypeDef](#virtualinterfacetesthistorytypedef)
  - [VirtualInterfaceTypeDef](#virtualinterfacetypedef)
  - [VirtualInterfacesTypeDef](#virtualinterfacestypedef)

## AcceptDirectConnectGatewayAssociationProposalResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import AcceptDirectConnectGatewayAssociationProposalResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociation`: `"DirectConnectGatewayAssociationTypeDef"`


## AllocateTransitVirtualInterfaceResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import AllocateTransitVirtualInterfaceResultTypeDef
```




Optional fields:
- `virtualInterface`: `"VirtualInterfaceTypeDef"`


## AssociateMacSecKeyResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import AssociateMacSecKeyResponseTypeDef
```




Optional fields:
- `connectionId`: `str`
- `macSecKeys`: `List["MacSecKeyTypeDef"]`


## AssociatedGatewayTypeDef

```python
from mypy_boto3_directconnect.type_defs import AssociatedGatewayTypeDef
```




Optional fields:
- `id`: `str`
- `type`: `GatewayType`
- `ownerAccount`: `str`
- `region`: `str`


## BGPPeerTypeDef

```python
from mypy_boto3_directconnect.type_defs import BGPPeerTypeDef
```




Optional fields:
- `bgpPeerId`: `str`
- `asn`: `int`
- `authKey`: `str`
- `addressFamily`: `AddressFamily`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `bgpPeerState`: `BGPPeerState`
- `bgpStatus`: `BGPStatus`
- `awsDeviceV2`: `str`


## ConfirmConnectionResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import ConfirmConnectionResponseTypeDef
```




Optional fields:
- `connectionState`: `ConnectionState`


## ConfirmPrivateVirtualInterfaceResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import ConfirmPrivateVirtualInterfaceResponseTypeDef
```




Optional fields:
- `virtualInterfaceState`: `VirtualInterfaceState`


## ConfirmPublicVirtualInterfaceResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import ConfirmPublicVirtualInterfaceResponseTypeDef
```




Optional fields:
- `virtualInterfaceState`: `VirtualInterfaceState`


## ConfirmTransitVirtualInterfaceResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import ConfirmTransitVirtualInterfaceResponseTypeDef
```




Optional fields:
- `virtualInterfaceState`: `VirtualInterfaceState`


## ConnectionTypeDef

```python
from mypy_boto3_directconnect.type_defs import ConnectionTypeDef
```




Optional fields:
- `ownerAccount`: `str`
- `connectionId`: `str`
- `connectionName`: `str`
- `connectionState`: `ConnectionState`
- `region`: `str`
- `location`: `str`
- `bandwidth`: `str`
- `vlan`: `int`
- `partnerName`: `str`
- `loaIssueTime`: `datetime`
- `lagId`: `str`
- `awsDevice`: `str`
- `jumboFrameCapable`: `bool`
- `awsDeviceV2`: `str`
- `hasLogicalRedundancy`: `HasLogicalRedundancy`
- `tags`: `List["TagTypeDef"]`
- `providerName`: `str`
- `macSecCapable`: `bool`
- `portEncryptionStatus`: `str`
- `encryptionMode`: `str`
- `macSecKeys`: `List["MacSecKeyTypeDef"]`


## ConnectionsTypeDef

```python
from mypy_boto3_directconnect.type_defs import ConnectionsTypeDef
```




Optional fields:
- `connections`: `List["ConnectionTypeDef"]`


## CreateBGPPeerResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import CreateBGPPeerResponseTypeDef
```




Optional fields:
- `virtualInterface`: `"VirtualInterfaceTypeDef"`


## CreateDirectConnectGatewayAssociationProposalResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import CreateDirectConnectGatewayAssociationProposalResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociationProposal`: `"DirectConnectGatewayAssociationProposalTypeDef"`


## CreateDirectConnectGatewayAssociationResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import CreateDirectConnectGatewayAssociationResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociation`: `"DirectConnectGatewayAssociationTypeDef"`


## CreateDirectConnectGatewayResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import CreateDirectConnectGatewayResultTypeDef
```




Optional fields:
- `directConnectGateway`: `"DirectConnectGatewayTypeDef"`


## CreateTransitVirtualInterfaceResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import CreateTransitVirtualInterfaceResultTypeDef
```




Optional fields:
- `virtualInterface`: `"VirtualInterfaceTypeDef"`


## DeleteBGPPeerResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DeleteBGPPeerResponseTypeDef
```




Optional fields:
- `virtualInterface`: `"VirtualInterfaceTypeDef"`


## DeleteDirectConnectGatewayAssociationProposalResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DeleteDirectConnectGatewayAssociationProposalResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociationProposal`: `"DirectConnectGatewayAssociationProposalTypeDef"`


## DeleteDirectConnectGatewayAssociationResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DeleteDirectConnectGatewayAssociationResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociation`: `"DirectConnectGatewayAssociationTypeDef"`


## DeleteDirectConnectGatewayResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DeleteDirectConnectGatewayResultTypeDef
```




Optional fields:
- `directConnectGateway`: `"DirectConnectGatewayTypeDef"`


## DeleteInterconnectResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DeleteInterconnectResponseTypeDef
```




Optional fields:
- `interconnectState`: `InterconnectState`


## DeleteVirtualInterfaceResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DeleteVirtualInterfaceResponseTypeDef
```




Optional fields:
- `virtualInterfaceState`: `VirtualInterfaceState`


## DescribeConnectionLoaResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeConnectionLoaResponseTypeDef
```




Optional fields:
- `loa`: `"LoaTypeDef"`


## DescribeDirectConnectGatewayAssociationProposalsResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeDirectConnectGatewayAssociationProposalsResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociationProposals`: `List["DirectConnectGatewayAssociationProposalTypeDef"]`
- `nextToken`: `str`


## DescribeDirectConnectGatewayAssociationsResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeDirectConnectGatewayAssociationsResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociations`: `List["DirectConnectGatewayAssociationTypeDef"]`
- `nextToken`: `str`


## DescribeDirectConnectGatewayAttachmentsResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeDirectConnectGatewayAttachmentsResultTypeDef
```




Optional fields:
- `directConnectGatewayAttachments`: `List["DirectConnectGatewayAttachmentTypeDef"]`
- `nextToken`: `str`


## DescribeDirectConnectGatewaysResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeDirectConnectGatewaysResultTypeDef
```




Optional fields:
- `directConnectGateways`: `List["DirectConnectGatewayTypeDef"]`
- `nextToken`: `str`


## DescribeInterconnectLoaResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeInterconnectLoaResponseTypeDef
```




Optional fields:
- `loa`: `"LoaTypeDef"`


## DescribeTagsResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DescribeTagsResponseTypeDef
```




Optional fields:
- `resourceTags`: `List["ResourceTagTypeDef"]`


## DirectConnectGatewayAssociationProposalTypeDef

```python
from mypy_boto3_directconnect.type_defs import DirectConnectGatewayAssociationProposalTypeDef
```




Optional fields:
- `proposalId`: `str`
- `directConnectGatewayId`: `str`
- `directConnectGatewayOwnerAccount`: `str`
- `proposalState`: `DirectConnectGatewayAssociationProposalState`
- `associatedGateway`: `"AssociatedGatewayTypeDef"`
- `existingAllowedPrefixesToDirectConnectGateway`: `List["RouteFilterPrefixTypeDef"]`
- `requestedAllowedPrefixesToDirectConnectGateway`: `List["RouteFilterPrefixTypeDef"]`


## DirectConnectGatewayAssociationTypeDef

```python
from mypy_boto3_directconnect.type_defs import DirectConnectGatewayAssociationTypeDef
```




Optional fields:
- `directConnectGatewayId`: `str`
- `directConnectGatewayOwnerAccount`: `str`
- `associationState`: `DirectConnectGatewayAssociationState`
- `stateChangeError`: `str`
- `associatedGateway`: `"AssociatedGatewayTypeDef"`
- `associationId`: `str`
- `allowedPrefixesToDirectConnectGateway`: `List["RouteFilterPrefixTypeDef"]`
- `virtualGatewayId`: `str`
- `virtualGatewayRegion`: `str`
- `virtualGatewayOwnerAccount`: `str`


## DirectConnectGatewayAttachmentTypeDef

```python
from mypy_boto3_directconnect.type_defs import DirectConnectGatewayAttachmentTypeDef
```




Optional fields:
- `directConnectGatewayId`: `str`
- `virtualInterfaceId`: `str`
- `virtualInterfaceRegion`: `str`
- `virtualInterfaceOwnerAccount`: `str`
- `attachmentState`: `DirectConnectGatewayAttachmentState`
- `attachmentType`: `DirectConnectGatewayAttachmentType`
- `stateChangeError`: `str`


## DirectConnectGatewayTypeDef

```python
from mypy_boto3_directconnect.type_defs import DirectConnectGatewayTypeDef
```




Optional fields:
- `directConnectGatewayId`: `str`
- `directConnectGatewayName`: `str`
- `amazonSideAsn`: `int`
- `ownerAccount`: `str`
- `directConnectGatewayState`: `DirectConnectGatewayState`
- `stateChangeError`: `str`


## DisassociateMacSecKeyResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import DisassociateMacSecKeyResponseTypeDef
```




Optional fields:
- `connectionId`: `str`
- `macSecKeys`: `List["MacSecKeyTypeDef"]`


## InterconnectTypeDef

```python
from mypy_boto3_directconnect.type_defs import InterconnectTypeDef
```




Optional fields:
- `interconnectId`: `str`
- `interconnectName`: `str`
- `interconnectState`: `InterconnectState`
- `region`: `str`
- `location`: `str`
- `bandwidth`: `str`
- `loaIssueTime`: `datetime`
- `lagId`: `str`
- `awsDevice`: `str`
- `jumboFrameCapable`: `bool`
- `awsDeviceV2`: `str`
- `hasLogicalRedundancy`: `HasLogicalRedundancy`
- `tags`: `List["TagTypeDef"]`
- `providerName`: `str`


## InterconnectsTypeDef

```python
from mypy_boto3_directconnect.type_defs import InterconnectsTypeDef
```




Optional fields:
- `interconnects`: `List["InterconnectTypeDef"]`


## LagTypeDef

```python
from mypy_boto3_directconnect.type_defs import LagTypeDef
```




Optional fields:
- `connectionsBandwidth`: `str`
- `numberOfConnections`: `int`
- `lagId`: `str`
- `ownerAccount`: `str`
- `lagName`: `str`
- `lagState`: `LagState`
- `location`: `str`
- `region`: `str`
- `minimumLinks`: `int`
- `awsDevice`: `str`
- `awsDeviceV2`: `str`
- `connections`: `List["ConnectionTypeDef"]`
- `allowsHostedConnections`: `bool`
- `jumboFrameCapable`: `bool`
- `hasLogicalRedundancy`: `HasLogicalRedundancy`
- `tags`: `List["TagTypeDef"]`
- `providerName`: `str`
- `macSecCapable`: `bool`
- `encryptionMode`: `str`
- `macSecKeys`: `List["MacSecKeyTypeDef"]`


## LagsTypeDef

```python
from mypy_boto3_directconnect.type_defs import LagsTypeDef
```




Optional fields:
- `lags`: `List["LagTypeDef"]`


## ListVirtualInterfaceTestHistoryResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import ListVirtualInterfaceTestHistoryResponseTypeDef
```




Optional fields:
- `virtualInterfaceTestHistory`: `List["VirtualInterfaceTestHistoryTypeDef"]`
- `nextToken`: `str`


## LoaTypeDef

```python
from mypy_boto3_directconnect.type_defs import LoaTypeDef
```




Optional fields:
- `loaContent`: `Union[bytes, IO[bytes]]`
- `loaContentType`: `Literal['application/pdf']`


## LocationTypeDef

```python
from mypy_boto3_directconnect.type_defs import LocationTypeDef
```




Optional fields:
- `locationCode`: `str`
- `locationName`: `str`
- `region`: `str`
- `availablePortSpeeds`: `List[str]`
- `availableProviders`: `List[str]`
- `availableMacSecPortSpeeds`: `List[str]`


## LocationsTypeDef

```python
from mypy_boto3_directconnect.type_defs import LocationsTypeDef
```




Optional fields:
- `locations`: `List["LocationTypeDef"]`


## MacSecKeyTypeDef

```python
from mypy_boto3_directconnect.type_defs import MacSecKeyTypeDef
```




Optional fields:
- `secretARN`: `str`
- `ckn`: `str`
- `state`: `str`
- `startOn`: `str`


## NewBGPPeerTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewBGPPeerTypeDef
```




Optional fields:
- `asn`: `int`
- `authKey`: `str`
- `addressFamily`: `AddressFamily`
- `amazonAddress`: `str`
- `customerAddress`: `str`


## NewPrivateVirtualInterfaceAllocationTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewPrivateVirtualInterfaceAllocationTypeDef
```


Required fields:
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`



Optional fields:
- `mtu`: `int`
- `authKey`: `str`
- `amazonAddress`: `str`
- `addressFamily`: `AddressFamily`
- `customerAddress`: `str`
- `tags`: `List["TagTypeDef"]`


## NewPrivateVirtualInterfaceTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewPrivateVirtualInterfaceTypeDef
```


Required fields:
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`



Optional fields:
- `mtu`: `int`
- `authKey`: `str`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `addressFamily`: `AddressFamily`
- `virtualGatewayId`: `str`
- `directConnectGatewayId`: `str`
- `tags`: `List["TagTypeDef"]`


## NewPublicVirtualInterfaceAllocationTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewPublicVirtualInterfaceAllocationTypeDef
```


Required fields:
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`



Optional fields:
- `authKey`: `str`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `addressFamily`: `AddressFamily`
- `routeFilterPrefixes`: `List["RouteFilterPrefixTypeDef"]`
- `tags`: `List["TagTypeDef"]`


## NewPublicVirtualInterfaceTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewPublicVirtualInterfaceTypeDef
```


Required fields:
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`



Optional fields:
- `authKey`: `str`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `addressFamily`: `AddressFamily`
- `routeFilterPrefixes`: `List["RouteFilterPrefixTypeDef"]`
- `tags`: `List["TagTypeDef"]`


## NewTransitVirtualInterfaceAllocationTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewTransitVirtualInterfaceAllocationTypeDef
```




Optional fields:
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`
- `mtu`: `int`
- `authKey`: `str`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `addressFamily`: `AddressFamily`
- `tags`: `List["TagTypeDef"]`


## NewTransitVirtualInterfaceTypeDef

```python
from mypy_boto3_directconnect.type_defs import NewTransitVirtualInterfaceTypeDef
```




Optional fields:
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`
- `mtu`: `int`
- `authKey`: `str`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `addressFamily`: `AddressFamily`
- `directConnectGatewayId`: `str`
- `tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_directconnect.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResourceTagTypeDef

```python
from mypy_boto3_directconnect.type_defs import ResourceTagTypeDef
```




Optional fields:
- `resourceArn`: `str`
- `tags`: `List["TagTypeDef"]`


## RouteFilterPrefixTypeDef

```python
from mypy_boto3_directconnect.type_defs import RouteFilterPrefixTypeDef
```




Optional fields:
- `cidr`: `str`


## StartBgpFailoverTestResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import StartBgpFailoverTestResponseTypeDef
```




Optional fields:
- `virtualInterfaceTest`: `"VirtualInterfaceTestHistoryTypeDef"`


## StopBgpFailoverTestResponseTypeDef

```python
from mypy_boto3_directconnect.type_defs import StopBgpFailoverTestResponseTypeDef
```




Optional fields:
- `virtualInterfaceTest`: `"VirtualInterfaceTestHistoryTypeDef"`


## TagTypeDef

```python
from mypy_boto3_directconnect.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `value`: `str`


## UpdateDirectConnectGatewayAssociationResultTypeDef

```python
from mypy_boto3_directconnect.type_defs import UpdateDirectConnectGatewayAssociationResultTypeDef
```




Optional fields:
- `directConnectGatewayAssociation`: `"DirectConnectGatewayAssociationTypeDef"`


## VirtualGatewayTypeDef

```python
from mypy_boto3_directconnect.type_defs import VirtualGatewayTypeDef
```




Optional fields:
- `virtualGatewayId`: `str`
- `virtualGatewayState`: `str`


## VirtualGatewaysTypeDef

```python
from mypy_boto3_directconnect.type_defs import VirtualGatewaysTypeDef
```




Optional fields:
- `virtualGateways`: `List["VirtualGatewayTypeDef"]`


## VirtualInterfaceTestHistoryTypeDef

```python
from mypy_boto3_directconnect.type_defs import VirtualInterfaceTestHistoryTypeDef
```




Optional fields:
- `testId`: `str`
- `virtualInterfaceId`: `str`
- `bgpPeers`: `List[str]`
- `status`: `str`
- `ownerAccount`: `str`
- `testDurationInMinutes`: `int`
- `startTime`: `datetime`
- `endTime`: `datetime`


## VirtualInterfaceTypeDef

```python
from mypy_boto3_directconnect.type_defs import VirtualInterfaceTypeDef
```




Optional fields:
- `ownerAccount`: `str`
- `virtualInterfaceId`: `str`
- `location`: `str`
- `connectionId`: `str`
- `virtualInterfaceType`: `str`
- `virtualInterfaceName`: `str`
- `vlan`: `int`
- `asn`: `int`
- `amazonSideAsn`: `int`
- `authKey`: `str`
- `amazonAddress`: `str`
- `customerAddress`: `str`
- `addressFamily`: `AddressFamily`
- `virtualInterfaceState`: `VirtualInterfaceState`
- `customerRouterConfig`: `str`
- `mtu`: `int`
- `jumboFrameCapable`: `bool`
- `virtualGatewayId`: `str`
- `directConnectGatewayId`: `str`
- `routeFilterPrefixes`: `List["RouteFilterPrefixTypeDef"]`
- `bgpPeers`: `List["BGPPeerTypeDef"]`
- `region`: `str`
- `awsDeviceV2`: `str`
- `tags`: `List["TagTypeDef"]`


## VirtualInterfacesTypeDef

```python
from mypy_boto3_directconnect.type_defs import VirtualInterfacesTypeDef
```




Optional fields:
- `virtualInterfaces`: `List["VirtualInterfaceTypeDef"]`

