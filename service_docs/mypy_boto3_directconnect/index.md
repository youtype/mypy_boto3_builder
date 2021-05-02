# Type annotations for boto3 DirectConnect module

> [Index](../index.md) > DirectConnect

Auto-generated documentation for [DirectConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect)
type annotations stubs module [mypy_boto3_directconnect](https://pypi.org/project/mypy-boto3-directconnect/).

```bash
pip install mypy-boto3-directconnect
```

- [Type annotations for boto3 DirectConnect module](#type-annotations-for-boto3-directconnect-module)
  - [DirectConnectClient](#directconnectclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## DirectConnectClient

Type annotations for  `boto3.client("directconnect")` as [DirectConnectClient](./client.md)

Can be used directly:

```python
from mypy_boto3_directconnect.client import DirectConnectClient
```


DirectConnectClient [exceptions](./client.md#exceptions)



### Methods
- [accept_direct_connect_gateway_association_proposal](./client.md#accept-direct-connect-gateway-association-proposal)
- [allocate_connection_on_interconnect](./client.md#allocate-connection-on-interconnect)
- [allocate_hosted_connection](./client.md#allocate-hosted-connection)
- [allocate_private_virtual_interface](./client.md#allocate-private-virtual-interface)
- [allocate_public_virtual_interface](./client.md#allocate-public-virtual-interface)
- [allocate_transit_virtual_interface](./client.md#allocate-transit-virtual-interface)
- [associate_connection_with_lag](./client.md#associate-connection-with-lag)
- [associate_hosted_connection](./client.md#associate-hosted-connection)
- [associate_mac_sec_key](./client.md#associate-mac-sec-key)
- [associate_virtual_interface](./client.md#associate-virtual-interface)
- [can_paginate](./client.md#can-paginate)
- [confirm_connection](./client.md#confirm-connection)
- [confirm_private_virtual_interface](./client.md#confirm-private-virtual-interface)
- [confirm_public_virtual_interface](./client.md#confirm-public-virtual-interface)
- [confirm_transit_virtual_interface](./client.md#confirm-transit-virtual-interface)
- [create_bgp_peer](./client.md#create-bgp-peer)
- [create_connection](./client.md#create-connection)
- [create_direct_connect_gateway](./client.md#create-direct-connect-gateway)
- [create_direct_connect_gateway_association](./client.md#create-direct-connect-gateway-association)
- [create_direct_connect_gateway_association_proposal](./client.md#create-direct-connect-gateway-association-proposal)
- [create_interconnect](./client.md#create-interconnect)
- [create_lag](./client.md#create-lag)
- [create_private_virtual_interface](./client.md#create-private-virtual-interface)
- [create_public_virtual_interface](./client.md#create-public-virtual-interface)
- [create_transit_virtual_interface](./client.md#create-transit-virtual-interface)
- [delete_bgp_peer](./client.md#delete-bgp-peer)
- [delete_connection](./client.md#delete-connection)
- [delete_direct_connect_gateway](./client.md#delete-direct-connect-gateway)
- [delete_direct_connect_gateway_association](./client.md#delete-direct-connect-gateway-association)
- [delete_direct_connect_gateway_association_proposal](./client.md#delete-direct-connect-gateway-association-proposal)
- [delete_interconnect](./client.md#delete-interconnect)
- [delete_lag](./client.md#delete-lag)
- [delete_virtual_interface](./client.md#delete-virtual-interface)
- [describe_connection_loa](./client.md#describe-connection-loa)
- [describe_connections](./client.md#describe-connections)
- [describe_connections_on_interconnect](./client.md#describe-connections-on-interconnect)
- [describe_direct_connect_gateway_association_proposals](./client.md#describe-direct-connect-gateway-association-proposals)
- [describe_direct_connect_gateway_associations](./client.md#describe-direct-connect-gateway-associations)
- [describe_direct_connect_gateway_attachments](./client.md#describe-direct-connect-gateway-attachments)
- [describe_direct_connect_gateways](./client.md#describe-direct-connect-gateways)
- [describe_hosted_connections](./client.md#describe-hosted-connections)
- [describe_interconnect_loa](./client.md#describe-interconnect-loa)
- [describe_interconnects](./client.md#describe-interconnects)
- [describe_lags](./client.md#describe-lags)
- [describe_loa](./client.md#describe-loa)
- [describe_locations](./client.md#describe-locations)
- [describe_tags](./client.md#describe-tags)
- [describe_virtual_gateways](./client.md#describe-virtual-gateways)
- [describe_virtual_interfaces](./client.md#describe-virtual-interfaces)
- [disassociate_connection_from_lag](./client.md#disassociate-connection-from-lag)
- [disassociate_mac_sec_key](./client.md#disassociate-mac-sec-key)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_virtual_interface_test_history](./client.md#list-virtual-interface-test-history)
- [start_bgp_failover_test](./client.md#start-bgp-failover-test)
- [stop_bgp_failover_test](./client.md#stop-bgp-failover-test)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_connection](./client.md#update-connection)
- [update_direct_connect_gateway_association](./client.md#update-direct-connect-gateway-association)
- [update_lag](./client.md#update-lag)
- [update_virtual_interface_attributes](./client.md#update-virtual-interface-attributes)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DirectConnectClientException](./client.md#directconnectclientexception)
- [DirectConnectServerException](./client.md#directconnectserverexception)
- [DuplicateTagKeysException](./client.md#duplicatetagkeysexception)
- [TooManyTagsException](./client.md#toomanytagsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("directconnect").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_directconnect.paginators import DescribeDirectConnectGatewayAssociationsPaginator, ...
```

- [DescribeDirectConnectGatewayAssociationsPaginator](./paginators.md#describedirectconnectgatewayassociationspaginator)
- [DescribeDirectConnectGatewayAttachmentsPaginator](./paginators.md#describedirectconnectgatewayattachmentspaginator)
- [DescribeDirectConnectGatewaysPaginator](./paginators.md#describedirectconnectgatewayspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_directconnect.literals import AddressFamily, ...
```

- [AddressFamily](./literals.md#addressfamily)
- [BGPPeerState](./literals.md#bgppeerstate)
- [BGPStatus](./literals.md#bgpstatus)
- [ConnectionState](./literals.md#connectionstate)
- [DescribeDirectConnectGatewayAssociationsPaginatorName](./literals.md#describedirectconnectgatewayassociationspaginatorname)
- [DescribeDirectConnectGatewayAttachmentsPaginatorName](./literals.md#describedirectconnectgatewayattachmentspaginatorname)
- [DescribeDirectConnectGatewaysPaginatorName](./literals.md#describedirectconnectgatewayspaginatorname)
- [DirectConnectGatewayAssociationProposalState](./literals.md#directconnectgatewayassociationproposalstate)
- [DirectConnectGatewayAssociationState](./literals.md#directconnectgatewayassociationstate)
- [DirectConnectGatewayAttachmentState](./literals.md#directconnectgatewayattachmentstate)
- [DirectConnectGatewayAttachmentType](./literals.md#directconnectgatewayattachmenttype)
- [DirectConnectGatewayState](./literals.md#directconnectgatewaystate)
- [GatewayType](./literals.md#gatewaytype)
- [HasLogicalRedundancy](./literals.md#haslogicalredundancy)
- [InterconnectState](./literals.md#interconnectstate)
- [LagState](./literals.md#lagstate)
- [LoaContentType](./literals.md#loacontenttype)
- [VirtualInterfaceState](./literals.md#virtualinterfacestate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_directconnect.type_defs import AssociatedGatewayTypeDef, ...
```

- [AssociatedGatewayTypeDef](./type_defs.md#associatedgatewaytypedef)
- [BGPPeerTypeDef](./type_defs.md#bgppeertypedef)
- [ConnectionTypeDef](./type_defs.md#connectiontypedef)
- [DirectConnectGatewayAssociationProposalTypeDef](./type_defs.md#directconnectgatewayassociationproposaltypedef)
- [DirectConnectGatewayAssociationTypeDef](./type_defs.md#directconnectgatewayassociationtypedef)
- [DirectConnectGatewayAttachmentTypeDef](./type_defs.md#directconnectgatewayattachmenttypedef)
- [DirectConnectGatewayTypeDef](./type_defs.md#directconnectgatewaytypedef)
- [InterconnectTypeDef](./type_defs.md#interconnecttypedef)
- [LagTypeDef](./type_defs.md#lagtypedef)
- [LoaTypeDef](./type_defs.md#loatypedef)
- [LocationTypeDef](./type_defs.md#locationtypedef)
- [MacSecKeyTypeDef](./type_defs.md#macseckeytypedef)
- [ResourceTagTypeDef](./type_defs.md#resourcetagtypedef)
- [RouteFilterPrefixTypeDef](./type_defs.md#routefilterprefixtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [VirtualGatewayTypeDef](./type_defs.md#virtualgatewaytypedef)
- [VirtualInterfaceTestHistoryTypeDef](./type_defs.md#virtualinterfacetesthistorytypedef)
- [VirtualInterfaceTypeDef](./type_defs.md#virtualinterfacetypedef)
- [AcceptDirectConnectGatewayAssociationProposalResultTypeDef](./type_defs.md#acceptdirectconnectgatewayassociationproposalresulttypedef)
- [AllocateTransitVirtualInterfaceResultTypeDef](./type_defs.md#allocatetransitvirtualinterfaceresulttypedef)
- [AssociateMacSecKeyResponseTypeDef](./type_defs.md#associatemacseckeyresponsetypedef)
- [ConfirmConnectionResponseTypeDef](./type_defs.md#confirmconnectionresponsetypedef)
- [ConfirmPrivateVirtualInterfaceResponseTypeDef](./type_defs.md#confirmprivatevirtualinterfaceresponsetypedef)
- [ConfirmPublicVirtualInterfaceResponseTypeDef](./type_defs.md#confirmpublicvirtualinterfaceresponsetypedef)
- [ConfirmTransitVirtualInterfaceResponseTypeDef](./type_defs.md#confirmtransitvirtualinterfaceresponsetypedef)
- [ConnectionsTypeDef](./type_defs.md#connectionstypedef)
- [CreateBGPPeerResponseTypeDef](./type_defs.md#createbgppeerresponsetypedef)
- [CreateDirectConnectGatewayAssociationProposalResultTypeDef](./type_defs.md#createdirectconnectgatewayassociationproposalresulttypedef)
- [CreateDirectConnectGatewayAssociationResultTypeDef](./type_defs.md#createdirectconnectgatewayassociationresulttypedef)
- [CreateDirectConnectGatewayResultTypeDef](./type_defs.md#createdirectconnectgatewayresulttypedef)
- [CreateTransitVirtualInterfaceResultTypeDef](./type_defs.md#createtransitvirtualinterfaceresulttypedef)
- [DeleteBGPPeerResponseTypeDef](./type_defs.md#deletebgppeerresponsetypedef)
- [DeleteDirectConnectGatewayAssociationProposalResultTypeDef](./type_defs.md#deletedirectconnectgatewayassociationproposalresulttypedef)
- [DeleteDirectConnectGatewayAssociationResultTypeDef](./type_defs.md#deletedirectconnectgatewayassociationresulttypedef)
- [DeleteDirectConnectGatewayResultTypeDef](./type_defs.md#deletedirectconnectgatewayresulttypedef)
- [DeleteInterconnectResponseTypeDef](./type_defs.md#deleteinterconnectresponsetypedef)
- [DeleteVirtualInterfaceResponseTypeDef](./type_defs.md#deletevirtualinterfaceresponsetypedef)
- [DescribeConnectionLoaResponseTypeDef](./type_defs.md#describeconnectionloaresponsetypedef)
- [DescribeDirectConnectGatewayAssociationProposalsResultTypeDef](./type_defs.md#describedirectconnectgatewayassociationproposalsresulttypedef)
- [DescribeDirectConnectGatewayAssociationsResultTypeDef](./type_defs.md#describedirectconnectgatewayassociationsresulttypedef)
- [DescribeDirectConnectGatewayAttachmentsResultTypeDef](./type_defs.md#describedirectconnectgatewayattachmentsresulttypedef)
- [DescribeDirectConnectGatewaysResultTypeDef](./type_defs.md#describedirectconnectgatewaysresulttypedef)
- [DescribeInterconnectLoaResponseTypeDef](./type_defs.md#describeinterconnectloaresponsetypedef)
- [DescribeTagsResponseTypeDef](./type_defs.md#describetagsresponsetypedef)
- [DisassociateMacSecKeyResponseTypeDef](./type_defs.md#disassociatemacseckeyresponsetypedef)
- [InterconnectsTypeDef](./type_defs.md#interconnectstypedef)
- [LagsTypeDef](./type_defs.md#lagstypedef)
- [ListVirtualInterfaceTestHistoryResponseTypeDef](./type_defs.md#listvirtualinterfacetesthistoryresponsetypedef)
- [LocationsTypeDef](./type_defs.md#locationstypedef)
- [NewBGPPeerTypeDef](./type_defs.md#newbgppeertypedef)
- [NewPrivateVirtualInterfaceAllocationTypeDef](./type_defs.md#newprivatevirtualinterfaceallocationtypedef)
- [NewPrivateVirtualInterfaceTypeDef](./type_defs.md#newprivatevirtualinterfacetypedef)
- [NewPublicVirtualInterfaceAllocationTypeDef](./type_defs.md#newpublicvirtualinterfaceallocationtypedef)
- [NewPublicVirtualInterfaceTypeDef](./type_defs.md#newpublicvirtualinterfacetypedef)
- [NewTransitVirtualInterfaceAllocationTypeDef](./type_defs.md#newtransitvirtualinterfaceallocationtypedef)
- [NewTransitVirtualInterfaceTypeDef](./type_defs.md#newtransitvirtualinterfacetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartBgpFailoverTestResponseTypeDef](./type_defs.md#startbgpfailovertestresponsetypedef)
- [StopBgpFailoverTestResponseTypeDef](./type_defs.md#stopbgpfailovertestresponsetypedef)
- [UpdateDirectConnectGatewayAssociationResultTypeDef](./type_defs.md#updatedirectconnectgatewayassociationresulttypedef)
- [VirtualGatewaysTypeDef](./type_defs.md#virtualgatewaystypedef)
- [VirtualInterfacesTypeDef](./type_defs.md#virtualinterfacestypedef)
