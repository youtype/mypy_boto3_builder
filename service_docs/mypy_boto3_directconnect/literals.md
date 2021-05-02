# Literals for boto3 DirectConnect module

> [Index](../index.md) > [DirectConnect](./index.md) > Literals

Auto-generated documentation for [DirectConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect)
type annotations stubs module [mypy_boto3_directconnect](https://pypi.org/project/mypy-boto3-directconnect/).

- [Literals for boto3 DirectConnect module](#literals-for-boto3-directconnect-module)
  - [AddressFamily](#addressfamily)
  - [BGPPeerState](#bgppeerstate)
  - [BGPStatus](#bgpstatus)
  - [ConnectionState](#connectionstate)
  - [DescribeDirectConnectGatewayAssociationsPaginatorName](#describedirectconnectgatewayassociationspaginatorname)
  - [DescribeDirectConnectGatewayAttachmentsPaginatorName](#describedirectconnectgatewayattachmentspaginatorname)
  - [DescribeDirectConnectGatewaysPaginatorName](#describedirectconnectgatewayspaginatorname)
  - [DirectConnectGatewayAssociationProposalState](#directconnectgatewayassociationproposalstate)
  - [DirectConnectGatewayAssociationState](#directconnectgatewayassociationstate)
  - [DirectConnectGatewayAttachmentState](#directconnectgatewayattachmentstate)
  - [DirectConnectGatewayAttachmentType](#directconnectgatewayattachmenttype)
  - [DirectConnectGatewayState](#directconnectgatewaystate)
  - [GatewayType](#gatewaytype)
  - [HasLogicalRedundancy](#haslogicalredundancy)
  - [InterconnectState](#interconnectstate)
  - [LagState](#lagstate)
  - [LoaContentType](#loacontenttype)
  - [VirtualInterfaceState](#virtualinterfacestate)

## AddressFamily

```python
from mypy_boto3_directconnect.literals import AddressFamily
```

Values:

- `ipv4`
- `ipv6`

## BGPPeerState

```python
from mypy_boto3_directconnect.literals import BGPPeerState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`
- `verifying`

## BGPStatus

```python
from mypy_boto3_directconnect.literals import BGPStatus
```

Values:

- `down`
- `unknown`
- `up`

## ConnectionState

```python
from mypy_boto3_directconnect.literals import ConnectionState
```

Values:

- `available`
- `deleted`
- `deleting`
- `down`
- `ordering`
- `pending`
- `rejected`
- `requested`
- `unknown`

## DescribeDirectConnectGatewayAssociationsPaginatorName

```python
from mypy_boto3_directconnect.literals import DescribeDirectConnectGatewayAssociationsPaginatorName
```

Values:

- `describe_direct_connect_gateway_associations`

## DescribeDirectConnectGatewayAttachmentsPaginatorName

```python
from mypy_boto3_directconnect.literals import DescribeDirectConnectGatewayAttachmentsPaginatorName
```

Values:

- `describe_direct_connect_gateway_attachments`

## DescribeDirectConnectGatewaysPaginatorName

```python
from mypy_boto3_directconnect.literals import DescribeDirectConnectGatewaysPaginatorName
```

Values:

- `describe_direct_connect_gateways`

## DirectConnectGatewayAssociationProposalState

```python
from mypy_boto3_directconnect.literals import DirectConnectGatewayAssociationProposalState
```

Values:

- `accepted`
- `deleted`
- `requested`

## DirectConnectGatewayAssociationState

```python
from mypy_boto3_directconnect.literals import DirectConnectGatewayAssociationState
```

Values:

- `associated`
- `associating`
- `disassociated`
- `disassociating`
- `updating`

## DirectConnectGatewayAttachmentState

```python
from mypy_boto3_directconnect.literals import DirectConnectGatewayAttachmentState
```

Values:

- `attached`
- `attaching`
- `detached`
- `detaching`

## DirectConnectGatewayAttachmentType

```python
from mypy_boto3_directconnect.literals import DirectConnectGatewayAttachmentType
```

Values:

- `PrivateVirtualInterface`
- `TransitVirtualInterface`

## DirectConnectGatewayState

```python
from mypy_boto3_directconnect.literals import DirectConnectGatewayState
```

Values:

- `available`
- `deleted`
- `deleting`
- `pending`

## GatewayType

```python
from mypy_boto3_directconnect.literals import GatewayType
```

Values:

- `transitGateway`
- `virtualPrivateGateway`

## HasLogicalRedundancy

```python
from mypy_boto3_directconnect.literals import HasLogicalRedundancy
```

Values:

- `no`
- `unknown`
- `yes`

## InterconnectState

```python
from mypy_boto3_directconnect.literals import InterconnectState
```

Values:

- `available`
- `deleted`
- `deleting`
- `down`
- `pending`
- `requested`
- `unknown`

## LagState

```python
from mypy_boto3_directconnect.literals import LagState
```

Values:

- `available`
- `deleted`
- `deleting`
- `down`
- `pending`
- `requested`
- `unknown`

## LoaContentType

```python
from mypy_boto3_directconnect.literals import LoaContentType
```

Values:

- `application/pdf`

## VirtualInterfaceState

```python
from mypy_boto3_directconnect.literals import VirtualInterfaceState
```

Values:

- `available`
- `confirming`
- `deleted`
- `deleting`
- `down`
- `pending`
- `rejected`
- `unknown`
- `verifying`
