# DirectConnectClient for boto3 DirectConnect module

> [Index](../index.md) > [DirectConnect](./index.md) > DirectConnectClient

Auto-generated documentation for [DirectConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect)
type annotations stubs module [mypy_boto3_directconnect](https://pypi.org/project/mypy-boto3-directconnect/).

- [DirectConnectClient for boto3 DirectConnect module](#directconnectclient-for-boto3-directconnect-module)
  - [DirectConnectClient](#directconnectclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_direct_connect_gateway_association_proposal](#accept_direct_connect_gateway_association_proposal)
    - [allocate_connection_on_interconnect](#allocate_connection_on_interconnect)
    - [allocate_hosted_connection](#allocate_hosted_connection)
    - [allocate_private_virtual_interface](#allocate_private_virtual_interface)
    - [allocate_public_virtual_interface](#allocate_public_virtual_interface)
    - [allocate_transit_virtual_interface](#allocate_transit_virtual_interface)
    - [associate_connection_with_lag](#associate_connection_with_lag)
    - [associate_hosted_connection](#associate_hosted_connection)
    - [associate_mac_sec_key](#associate_mac_sec_key)
    - [associate_virtual_interface](#associate_virtual_interface)
    - [can_paginate](#can_paginate)
    - [confirm_connection](#confirm_connection)
    - [confirm_private_virtual_interface](#confirm_private_virtual_interface)
    - [confirm_public_virtual_interface](#confirm_public_virtual_interface)
    - [confirm_transit_virtual_interface](#confirm_transit_virtual_interface)
    - [create_bgp_peer](#create_bgp_peer)
    - [create_connection](#create_connection)
    - [create_direct_connect_gateway](#create_direct_connect_gateway)
    - [create_direct_connect_gateway_association](#create_direct_connect_gateway_association)
    - [create_direct_connect_gateway_association_proposal](#create_direct_connect_gateway_association_proposal)
    - [create_interconnect](#create_interconnect)
    - [create_lag](#create_lag)
    - [create_private_virtual_interface](#create_private_virtual_interface)
    - [create_public_virtual_interface](#create_public_virtual_interface)
    - [create_transit_virtual_interface](#create_transit_virtual_interface)
    - [delete_bgp_peer](#delete_bgp_peer)
    - [delete_connection](#delete_connection)
    - [delete_direct_connect_gateway](#delete_direct_connect_gateway)
    - [delete_direct_connect_gateway_association](#delete_direct_connect_gateway_association)
    - [delete_direct_connect_gateway_association_proposal](#delete_direct_connect_gateway_association_proposal)
    - [delete_interconnect](#delete_interconnect)
    - [delete_lag](#delete_lag)
    - [delete_virtual_interface](#delete_virtual_interface)
    - [describe_connection_loa](#describe_connection_loa)
    - [describe_connections](#describe_connections)
    - [describe_connections_on_interconnect](#describe_connections_on_interconnect)
    - [describe_direct_connect_gateway_association_proposals](#describe_direct_connect_gateway_association_proposals)
    - [describe_direct_connect_gateway_associations](#describe_direct_connect_gateway_associations)
    - [describe_direct_connect_gateway_attachments](#describe_direct_connect_gateway_attachments)
    - [describe_direct_connect_gateways](#describe_direct_connect_gateways)
    - [describe_hosted_connections](#describe_hosted_connections)
    - [describe_interconnect_loa](#describe_interconnect_loa)
    - [describe_interconnects](#describe_interconnects)
    - [describe_lags](#describe_lags)
    - [describe_loa](#describe_loa)
    - [describe_locations](#describe_locations)
    - [describe_tags](#describe_tags)
    - [describe_virtual_gateways](#describe_virtual_gateways)
    - [describe_virtual_interfaces](#describe_virtual_interfaces)
    - [disassociate_connection_from_lag](#disassociate_connection_from_lag)
    - [disassociate_mac_sec_key](#disassociate_mac_sec_key)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_virtual_interface_test_history](#list_virtual_interface_test_history)
    - [start_bgp_failover_test](#start_bgp_failover_test)
    - [stop_bgp_failover_test](#stop_bgp_failover_test)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_connection](#update_connection)
    - [update_direct_connect_gateway_association](#update_direct_connect_gateway_association)
    - [update_lag](#update_lag)
    - [update_virtual_interface_attributes](#update_virtual_interface_attributes)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)

## DirectConnectClient

Type annotations for `boto3.client("directconnect")`

Can be used directly:

```python
from mypy_boto3_directconnect.client import DirectConnectClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_directconnect.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DirectConnectClientException`
- `Exceptions.DirectConnectServerException`
- `Exceptions.DuplicateTagKeysException`
- `Exceptions.TooManyTagsException`


## Methods


### accept_direct_connect_gateway_association_proposal

Type annotations for `boto3.client("directconnect").accept_direct_connect_gateway_association_proposal` method.

[Client.accept_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.accept_direct_connect_gateway_association_proposal)

```python
def accept_direct_connect_gateway_association_proposal(
    self,
    directConnectGatewayId: str,
    proposalId: str,
    associatedGatewayOwnerAccount: str,
    overrideAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None
) -> AcceptDirectConnectGatewayAssociationProposalResultTypeDef:
    pass
```

### allocate_connection_on_interconnect

Type annotations for `boto3.client("directconnect").allocate_connection_on_interconnect` method.

[Client.allocate_connection_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.allocate_connection_on_interconnect)

```python
def allocate_connection_on_interconnect(
    self,
    bandwidth: str,
    connectionName: str,
    ownerAccount: str,
    interconnectId: str,
    vlan: int
) -> "ConnectionTypeDef":
    pass
```

### allocate_hosted_connection

Type annotations for `boto3.client("directconnect").allocate_hosted_connection` method.

[Client.allocate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.allocate_hosted_connection)

```python
def allocate_hosted_connection(
    self,
    connectionId: str,
    ownerAccount: str,
    bandwidth: str,
    connectionName: str,
    vlan: int,
    tags: List["TagTypeDef"] = None
) -> "ConnectionTypeDef":
    pass
```

### allocate_private_virtual_interface

Type annotations for `boto3.client("directconnect").allocate_private_virtual_interface` method.

[Client.allocate_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.allocate_private_virtual_interface)

```python
def allocate_private_virtual_interface(
    self,
    connectionId: str,
    ownerAccount: str,
    newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef
) -> "VirtualInterfaceTypeDef":
    pass
```

### allocate_public_virtual_interface

Type annotations for `boto3.client("directconnect").allocate_public_virtual_interface` method.

[Client.allocate_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.allocate_public_virtual_interface)

```python
def allocate_public_virtual_interface(
    self,
    connectionId: str,
    ownerAccount: str,
    newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef
) -> "VirtualInterfaceTypeDef":
    pass
```

### allocate_transit_virtual_interface

Type annotations for `boto3.client("directconnect").allocate_transit_virtual_interface` method.

[Client.allocate_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.allocate_transit_virtual_interface)

```python
def allocate_transit_virtual_interface(
    self,
    connectionId: str,
    ownerAccount: str,
    newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef
) -> AllocateTransitVirtualInterfaceResultTypeDef:
    pass
```

### associate_connection_with_lag

Type annotations for `boto3.client("directconnect").associate_connection_with_lag` method.

[Client.associate_connection_with_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.associate_connection_with_lag)

```python
def associate_connection_with_lag(
    self,
    connectionId: str,
    lagId: str
) -> "ConnectionTypeDef":
    pass
```

### associate_hosted_connection

Type annotations for `boto3.client("directconnect").associate_hosted_connection` method.

[Client.associate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.associate_hosted_connection)

```python
def associate_hosted_connection(
    self,
    connectionId: str,
    parentConnectionId: str
) -> "ConnectionTypeDef":
    pass
```

### associate_mac_sec_key

Type annotations for `boto3.client("directconnect").associate_mac_sec_key` method.

[Client.associate_mac_sec_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.associate_mac_sec_key)

```python
def associate_mac_sec_key(
    self,
    connectionId: str,
    secretARN: str = None,
    ckn: str = None,
    cak: str = None
) -> AssociateMacSecKeyResponseTypeDef:
    pass
```

### associate_virtual_interface

Type annotations for `boto3.client("directconnect").associate_virtual_interface` method.

[Client.associate_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.associate_virtual_interface)

```python
def associate_virtual_interface(
    self,
    virtualInterfaceId: str,
    connectionId: str
) -> "VirtualInterfaceTypeDef":
    pass
```

### can_paginate

Type annotations for `boto3.client("directconnect").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### confirm_connection

Type annotations for `boto3.client("directconnect").confirm_connection` method.

[Client.confirm_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.confirm_connection)

```python
def confirm_connection(
    self,
    connectionId: str
) -> ConfirmConnectionResponseTypeDef:
    pass
```

### confirm_private_virtual_interface

Type annotations for `boto3.client("directconnect").confirm_private_virtual_interface` method.

[Client.confirm_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.confirm_private_virtual_interface)

```python
def confirm_private_virtual_interface(
    self,
    virtualInterfaceId: str,
    virtualGatewayId: str = None,
    directConnectGatewayId: str = None
) -> ConfirmPrivateVirtualInterfaceResponseTypeDef:
    pass
```

### confirm_public_virtual_interface

Type annotations for `boto3.client("directconnect").confirm_public_virtual_interface` method.

[Client.confirm_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.confirm_public_virtual_interface)

```python
def confirm_public_virtual_interface(
    self,
    virtualInterfaceId: str
) -> ConfirmPublicVirtualInterfaceResponseTypeDef:
    pass
```

### confirm_transit_virtual_interface

Type annotations for `boto3.client("directconnect").confirm_transit_virtual_interface` method.

[Client.confirm_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.confirm_transit_virtual_interface)

```python
def confirm_transit_virtual_interface(
    self,
    virtualInterfaceId: str,
    directConnectGatewayId: str
) -> ConfirmTransitVirtualInterfaceResponseTypeDef:
    pass
```

### create_bgp_peer

Type annotations for `boto3.client("directconnect").create_bgp_peer` method.

[Client.create_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_bgp_peer)

```python
def create_bgp_peer(
    self,
    virtualInterfaceId: str = None,
    newBGPPeer: NewBGPPeerTypeDef = None
) -> CreateBGPPeerResponseTypeDef:
    pass
```

### create_connection

Type annotations for `boto3.client("directconnect").create_connection` method.

[Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_connection)

```python
def create_connection(
    self,
    location: str,
    bandwidth: str,
    connectionName: str,
    lagId: str = None,
    tags: List["TagTypeDef"] = None,
    providerName: str = None,
    requestMACSec: bool = None
) -> "ConnectionTypeDef":
    pass
```

### create_direct_connect_gateway

Type annotations for `boto3.client("directconnect").create_direct_connect_gateway` method.

[Client.create_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway)

```python
def create_direct_connect_gateway(
    self,
    directConnectGatewayName: str,
    amazonSideAsn: int = None
) -> CreateDirectConnectGatewayResultTypeDef:
    pass
```

### create_direct_connect_gateway_association

Type annotations for `boto3.client("directconnect").create_direct_connect_gateway_association` method.

[Client.create_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association)

```python
def create_direct_connect_gateway_association(
    self,
    directConnectGatewayId: str,
    gatewayId: str = None,
    addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
    virtualGatewayId: str = None
) -> CreateDirectConnectGatewayAssociationResultTypeDef:
    pass
```

### create_direct_connect_gateway_association_proposal

Type annotations for `boto3.client("directconnect").create_direct_connect_gateway_association_proposal` method.

[Client.create_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association_proposal)

```python
def create_direct_connect_gateway_association_proposal(
    self,
    directConnectGatewayId: str,
    directConnectGatewayOwnerAccount: str,
    gatewayId: str,
    addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
    removeAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None
) -> CreateDirectConnectGatewayAssociationProposalResultTypeDef:
    pass
```

### create_interconnect

Type annotations for `boto3.client("directconnect").create_interconnect` method.

[Client.create_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_interconnect)

```python
def create_interconnect(
    self,
    interconnectName: str,
    bandwidth: str,
    location: str,
    lagId: str = None,
    tags: List["TagTypeDef"] = None,
    providerName: str = None
) -> "InterconnectTypeDef":
    pass
```

### create_lag

Type annotations for `boto3.client("directconnect").create_lag` method.

[Client.create_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_lag)

```python
def create_lag(
    self,
    numberOfConnections: int,
    location: str,
    connectionsBandwidth: str,
    lagName: str,
    connectionId: str = None,
    tags: List["TagTypeDef"] = None,
    childConnectionTags: List["TagTypeDef"] = None,
    providerName: str = None,
    requestMACSec: bool = None
) -> "LagTypeDef":
    pass
```

### create_private_virtual_interface

Type annotations for `boto3.client("directconnect").create_private_virtual_interface` method.

[Client.create_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_private_virtual_interface)

```python
def create_private_virtual_interface(
    self,
    connectionId: str,
    newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef
) -> "VirtualInterfaceTypeDef":
    pass
```

### create_public_virtual_interface

Type annotations for `boto3.client("directconnect").create_public_virtual_interface` method.

[Client.create_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_public_virtual_interface)

```python
def create_public_virtual_interface(
    self,
    connectionId: str,
    newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef
) -> "VirtualInterfaceTypeDef":
    pass
```

### create_transit_virtual_interface

Type annotations for `boto3.client("directconnect").create_transit_virtual_interface` method.

[Client.create_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.create_transit_virtual_interface)

```python
def create_transit_virtual_interface(
    self,
    connectionId: str,
    newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef
) -> CreateTransitVirtualInterfaceResultTypeDef:
    pass
```

### delete_bgp_peer

Type annotations for `boto3.client("directconnect").delete_bgp_peer` method.

[Client.delete_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_bgp_peer)

```python
def delete_bgp_peer(
    self,
    virtualInterfaceId: str = None,
    asn: int = None,
    customerAddress: str = None,
    bgpPeerId: str = None
) -> DeleteBGPPeerResponseTypeDef:
    pass
```

### delete_connection

Type annotations for `boto3.client("directconnect").delete_connection` method.

[Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_connection)

```python
def delete_connection(
    self,
    connectionId: str
) -> "ConnectionTypeDef":
    pass
```

### delete_direct_connect_gateway

Type annotations for `boto3.client("directconnect").delete_direct_connect_gateway` method.

[Client.delete_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway)

```python
def delete_direct_connect_gateway(
    self,
    directConnectGatewayId: str
) -> DeleteDirectConnectGatewayResultTypeDef:
    pass
```

### delete_direct_connect_gateway_association

Type annotations for `boto3.client("directconnect").delete_direct_connect_gateway_association` method.

[Client.delete_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association)

```python
def delete_direct_connect_gateway_association(
    self,
    associationId: str = None,
    directConnectGatewayId: str = None,
    virtualGatewayId: str = None
) -> DeleteDirectConnectGatewayAssociationResultTypeDef:
    pass
```

### delete_direct_connect_gateway_association_proposal

Type annotations for `boto3.client("directconnect").delete_direct_connect_gateway_association_proposal` method.

[Client.delete_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association_proposal)

```python
def delete_direct_connect_gateway_association_proposal(
    self,
    proposalId: str
) -> DeleteDirectConnectGatewayAssociationProposalResultTypeDef:
    pass
```

### delete_interconnect

Type annotations for `boto3.client("directconnect").delete_interconnect` method.

[Client.delete_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_interconnect)

```python
def delete_interconnect(
    self,
    interconnectId: str
) -> DeleteInterconnectResponseTypeDef:
    pass
```

### delete_lag

Type annotations for `boto3.client("directconnect").delete_lag` method.

[Client.delete_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_lag)

```python
def delete_lag(
    self,
    lagId: str
) -> "LagTypeDef":
    pass
```

### delete_virtual_interface

Type annotations for `boto3.client("directconnect").delete_virtual_interface` method.

[Client.delete_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.delete_virtual_interface)

```python
def delete_virtual_interface(
    self,
    virtualInterfaceId: str
) -> DeleteVirtualInterfaceResponseTypeDef:
    pass
```

### describe_connection_loa

Type annotations for `boto3.client("directconnect").describe_connection_loa` method.

[Client.describe_connection_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_connection_loa)

```python
def describe_connection_loa(
    self,
    connectionId: str,
    providerName: str = None,
    loaContentType: LoaContentType = None
) -> DescribeConnectionLoaResponseTypeDef:
    pass
```

### describe_connections

Type annotations for `boto3.client("directconnect").describe_connections` method.

[Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_connections)

```python
def describe_connections(
    self,
    connectionId: str = None
) -> ConnectionsTypeDef:
    pass
```

### describe_connections_on_interconnect

Type annotations for `boto3.client("directconnect").describe_connections_on_interconnect` method.

[Client.describe_connections_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_connections_on_interconnect)

```python
def describe_connections_on_interconnect(
    self,
    interconnectId: str
) -> ConnectionsTypeDef:
    pass
```

### describe_direct_connect_gateway_association_proposals

Type annotations for `boto3.client("directconnect").describe_direct_connect_gateway_association_proposals` method.

[Client.describe_direct_connect_gateway_association_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_association_proposals)

```python
def describe_direct_connect_gateway_association_proposals(
    self,
    directConnectGatewayId: str = None,
    proposalId: str = None,
    associatedGatewayId: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeDirectConnectGatewayAssociationProposalsResultTypeDef:
    pass
```

### describe_direct_connect_gateway_associations

Type annotations for `boto3.client("directconnect").describe_direct_connect_gateway_associations` method.

[Client.describe_direct_connect_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_associations)

```python
def describe_direct_connect_gateway_associations(
    self,
    associationId: str = None,
    associatedGatewayId: str = None,
    directConnectGatewayId: str = None,
    maxResults: int = None,
    nextToken: str = None,
    virtualGatewayId: str = None
) -> DescribeDirectConnectGatewayAssociationsResultTypeDef:
    pass
```

### describe_direct_connect_gateway_attachments

Type annotations for `boto3.client("directconnect").describe_direct_connect_gateway_attachments` method.

[Client.describe_direct_connect_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_attachments)

```python
def describe_direct_connect_gateway_attachments(
    self,
    directConnectGatewayId: str = None,
    virtualInterfaceId: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeDirectConnectGatewayAttachmentsResultTypeDef:
    pass
```

### describe_direct_connect_gateways

Type annotations for `boto3.client("directconnect").describe_direct_connect_gateways` method.

[Client.describe_direct_connect_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateways)

```python
def describe_direct_connect_gateways(
    self,
    directConnectGatewayId: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeDirectConnectGatewaysResultTypeDef:
    pass
```

### describe_hosted_connections

Type annotations for `boto3.client("directconnect").describe_hosted_connections` method.

[Client.describe_hosted_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_hosted_connections)

```python
def describe_hosted_connections(
    self,
    connectionId: str
) -> ConnectionsTypeDef:
    pass
```

### describe_interconnect_loa

Type annotations for `boto3.client("directconnect").describe_interconnect_loa` method.

[Client.describe_interconnect_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_interconnect_loa)

```python
def describe_interconnect_loa(
    self,
    interconnectId: str,
    providerName: str = None,
    loaContentType: LoaContentType = None
) -> DescribeInterconnectLoaResponseTypeDef:
    pass
```

### describe_interconnects

Type annotations for `boto3.client("directconnect").describe_interconnects` method.

[Client.describe_interconnects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_interconnects)

```python
def describe_interconnects(
    self,
    interconnectId: str = None
) -> InterconnectsTypeDef:
    pass
```

### describe_lags

Type annotations for `boto3.client("directconnect").describe_lags` method.

[Client.describe_lags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_lags)

```python
def describe_lags(
    self,
    lagId: str = None
) -> LagsTypeDef:
    pass
```

### describe_loa

Type annotations for `boto3.client("directconnect").describe_loa` method.

[Client.describe_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_loa)

```python
def describe_loa(
    self,
    connectionId: str,
    providerName: str = None,
    loaContentType: LoaContentType = None
) -> "LoaTypeDef":
    pass
```

### describe_locations

Type annotations for `boto3.client("directconnect").describe_locations` method.

[Client.describe_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_locations)

```python
def describe_locations(
    self
) -> LocationsTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("directconnect").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_tags)

```python
def describe_tags(
    self,
    resourceArns: List[str]
) -> DescribeTagsResponseTypeDef:
    pass
```

### describe_virtual_gateways

Type annotations for `boto3.client("directconnect").describe_virtual_gateways` method.

[Client.describe_virtual_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_gateways)

```python
def describe_virtual_gateways(
    self
) -> VirtualGatewaysTypeDef:
    pass
```

### describe_virtual_interfaces

Type annotations for `boto3.client("directconnect").describe_virtual_interfaces` method.

[Client.describe_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_interfaces)

```python
def describe_virtual_interfaces(
    self,
    connectionId: str = None,
    virtualInterfaceId: str = None
) -> VirtualInterfacesTypeDef:
    pass
```

### disassociate_connection_from_lag

Type annotations for `boto3.client("directconnect").disassociate_connection_from_lag` method.

[Client.disassociate_connection_from_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.disassociate_connection_from_lag)

```python
def disassociate_connection_from_lag(
    self,
    connectionId: str,
    lagId: str
) -> "ConnectionTypeDef":
    pass
```

### disassociate_mac_sec_key

Type annotations for `boto3.client("directconnect").disassociate_mac_sec_key` method.

[Client.disassociate_mac_sec_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.disassociate_mac_sec_key)

```python
def disassociate_mac_sec_key(
    self,
    connectionId: str,
    secretARN: str
) -> DisassociateMacSecKeyResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("directconnect").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.generate_presigned_url)

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

### list_virtual_interface_test_history

Type annotations for `boto3.client("directconnect").list_virtual_interface_test_history` method.

[Client.list_virtual_interface_test_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.list_virtual_interface_test_history)

```python
def list_virtual_interface_test_history(
    self,
    testId: str = None,
    virtualInterfaceId: str = None,
    bgpPeers: List[str] = None,
    status: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListVirtualInterfaceTestHistoryResponseTypeDef:
    pass
```

### start_bgp_failover_test

Type annotations for `boto3.client("directconnect").start_bgp_failover_test` method.

[Client.start_bgp_failover_test documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.start_bgp_failover_test)

```python
def start_bgp_failover_test(
    self,
    virtualInterfaceId: str,
    bgpPeers: List[str] = None,
    testDurationInMinutes: int = None
) -> StartBgpFailoverTestResponseTypeDef:
    pass
```

### stop_bgp_failover_test

Type annotations for `boto3.client("directconnect").stop_bgp_failover_test` method.

[Client.stop_bgp_failover_test documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.stop_bgp_failover_test)

```python
def stop_bgp_failover_test(
    self,
    virtualInterfaceId: str
) -> StopBgpFailoverTestResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("directconnect").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("directconnect").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_connection

Type annotations for `boto3.client("directconnect").update_connection` method.

[Client.update_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.update_connection)

```python
def update_connection(
    self,
    connectionId: str,
    connectionName: str = None,
    encryptionMode: str = None
) -> "ConnectionTypeDef":
    pass
```

### update_direct_connect_gateway_association

Type annotations for `boto3.client("directconnect").update_direct_connect_gateway_association` method.

[Client.update_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.update_direct_connect_gateway_association)

```python
def update_direct_connect_gateway_association(
    self,
    associationId: str = None,
    addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
    removeAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None
) -> UpdateDirectConnectGatewayAssociationResultTypeDef:
    pass
```

### update_lag

Type annotations for `boto3.client("directconnect").update_lag` method.

[Client.update_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.update_lag)

```python
def update_lag(
    self,
    lagId: str,
    lagName: str = None,
    minimumLinks: int = None,
    encryptionMode: str = None
) -> "LagTypeDef":
    pass
```

### update_virtual_interface_attributes

Type annotations for `boto3.client("directconnect").update_virtual_interface_attributes` method.

[Client.update_virtual_interface_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Client.update_virtual_interface_attributes)

```python
def update_virtual_interface_attributes(
    self,
    virtualInterfaceId: str,
    mtu: int = None
) -> "VirtualInterfaceTypeDef":
    pass
```

### get_paginator

Type annotations for `boto3.client("directconnect").get_paginator` method.

[Paginator.DescribeDirectConnectGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDirectConnectGatewayAssociationsPaginatorName
) -> DescribeDirectConnectGatewayAssociationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("directconnect").get_paginator` method.

[Paginator.DescribeDirectConnectGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDirectConnectGatewayAttachmentsPaginatorName
) -> DescribeDirectConnectGatewayAttachmentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("directconnect").get_paginator` method.

[Paginator.DescribeDirectConnectGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDirectConnectGatewaysPaginatorName
) -> DescribeDirectConnectGatewaysPaginator:
    pass
```