# Paginators for boto3 DirectConnect module

> [Index](../index.md) > [DirectConnect](./index.md) > Paginators

Auto-generated documentation for [DirectConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect)
type annotations stubs module [mypy_boto3_directconnect](https://pypi.org/project/mypy-boto3-directconnect/).

- [Paginators for boto3 DirectConnect module](#paginators-for-boto3-directconnect-module)
  - [DescribeDirectConnectGatewayAssociationsPaginator](#describedirectconnectgatewayassociationspaginator)
  - [DescribeDirectConnectGatewayAttachmentsPaginator](#describedirectconnectgatewayattachmentspaginator)
  - [DescribeDirectConnectGatewaysPaginator](#describedirectconnectgatewayspaginator)

## DescribeDirectConnectGatewayAssociationsPaginator

Type annotations for `boto3.client("directconnect").get_paginator("describe_direct_connect_gateway_associations")`.

Can be used directly:

```python
from mypy_boto3_directconnect.paginators import DescribeDirectConnectGatewayAssociationsPaginator

def get_describe_direct_connect_gateway_associations_paginator() -> DescribeDirectConnectGatewayAssociationsPaginator:
    return boto3.client("directconnect").get_paginator("describe_direct_connect_gateway_associations")
```

[Paginator.DescribeDirectConnectGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)

```python
class DescribeDirectConnectGatewayAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectConnectGatewayAssociationsResultTypeDef]:
        pass
```
## DescribeDirectConnectGatewayAttachmentsPaginator

Type annotations for `boto3.client("directconnect").get_paginator("describe_direct_connect_gateway_attachments")`.

Can be used directly:

```python
from mypy_boto3_directconnect.paginators import DescribeDirectConnectGatewayAttachmentsPaginator

def get_describe_direct_connect_gateway_attachments_paginator() -> DescribeDirectConnectGatewayAttachmentsPaginator:
    return boto3.client("directconnect").get_paginator("describe_direct_connect_gateway_attachments")
```

[Paginator.DescribeDirectConnectGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)

```python
class DescribeDirectConnectGatewayAttachmentsPaginator(Boto3Paginator):
    def paginate(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectConnectGatewayAttachmentsResultTypeDef]:
        pass
```
## DescribeDirectConnectGatewaysPaginator

Type annotations for `boto3.client("directconnect").get_paginator("describe_direct_connect_gateways")`.

Can be used directly:

```python
from mypy_boto3_directconnect.paginators import DescribeDirectConnectGatewaysPaginator

def get_describe_direct_connect_gateways_paginator() -> DescribeDirectConnectGatewaysPaginator:
    return boto3.client("directconnect").get_paginator("describe_direct_connect_gateways")
```

[Paginator.DescribeDirectConnectGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)

```python
class DescribeDirectConnectGatewaysPaginator(Boto3Paginator):
    def paginate(
        self,
        directConnectGatewayId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectConnectGatewaysResultTypeDef]:
        pass
```