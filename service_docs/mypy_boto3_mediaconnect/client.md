# MediaConnectClient for boto3 MediaConnect module

> [Index](../index.md) > [MediaConnect](./index.md) > MediaConnectClient

Auto-generated documentation for [MediaConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect)
type annotations stubs module [mypy_boto3_mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/).

- [MediaConnectClient for boto3 MediaConnect module](#mediaconnectclient-for-boto3-mediaconnect-module)
  - [MediaConnectClient](#mediaconnectclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_flow_outputs](#add_flow_outputs)
    - [add_flow_sources](#add_flow_sources)
    - [add_flow_vpc_interfaces](#add_flow_vpc_interfaces)
    - [can_paginate](#can_paginate)
    - [create_flow](#create_flow)
    - [delete_flow](#delete_flow)
    - [describe_flow](#describe_flow)
    - [describe_offering](#describe_offering)
    - [describe_reservation](#describe_reservation)
    - [generate_presigned_url](#generate_presigned_url)
    - [grant_flow_entitlements](#grant_flow_entitlements)
    - [list_entitlements](#list_entitlements)
    - [list_flows](#list_flows)
    - [list_offerings](#list_offerings)
    - [list_reservations](#list_reservations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [purchase_offering](#purchase_offering)
    - [remove_flow_output](#remove_flow_output)
    - [remove_flow_source](#remove_flow_source)
    - [remove_flow_vpc_interface](#remove_flow_vpc_interface)
    - [revoke_flow_entitlement](#revoke_flow_entitlement)
    - [start_flow](#start_flow)
    - [stop_flow](#stop_flow)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_flow](#update_flow)
    - [update_flow_entitlement](#update_flow_entitlement)
    - [update_flow_output](#update_flow_output)
    - [update_flow_source](#update_flow_source)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## MediaConnectClient

Type annotations for `boto3.client("mediaconnect")`

Can be used directly:

```python
from mypy_boto3_mediaconnect.client import MediaConnectClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mediaconnect.client import Exceptions

def handle_error(exc: Exceptions.AddFlowOutputs420Exception) -> None:
    ...
```


Exceptions:

- `Exceptions.AddFlowOutputs420Exception`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.CreateFlow420Exception`
- `Exceptions.ForbiddenException`
- `Exceptions.GrantFlowEntitlements420Exception`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`


## Methods


### add_flow_outputs

Type annotations for `boto3.client("mediaconnect").add_flow_outputs` method.

[Client.add_flow_outputs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_outputs)

```python
def add_flow_outputs(
    self,
    FlowArn: str,
    Outputs: List[AddOutputRequestTypeDef]
) -> AddFlowOutputsResponseTypeDef:
    pass
```

### add_flow_sources

Type annotations for `boto3.client("mediaconnect").add_flow_sources` method.

[Client.add_flow_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_sources)

```python
def add_flow_sources(
    self,
    FlowArn: str,
    Sources: List[SetSourceRequestTypeDef]
) -> AddFlowSourcesResponseTypeDef:
    pass
```

### add_flow_vpc_interfaces

Type annotations for `boto3.client("mediaconnect").add_flow_vpc_interfaces` method.

[Client.add_flow_vpc_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.add_flow_vpc_interfaces)

```python
def add_flow_vpc_interfaces(
    self,
    FlowArn: str,
    VpcInterfaces: List[VpcInterfaceRequestTypeDef]
) -> AddFlowVpcInterfacesResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("mediaconnect").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_flow

Type annotations for `boto3.client("mediaconnect").create_flow` method.

[Client.create_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.create_flow)

```python
def create_flow(
    self,
    Name: str,
    AvailabilityZone: str = None,
    Entitlements: List[GrantEntitlementRequestTypeDef] = None,
    Outputs: List[AddOutputRequestTypeDef] = None,
    Source: SetSourceRequestTypeDef = None,
    SourceFailoverConfig: "FailoverConfigTypeDef" = None,
    Sources: List[SetSourceRequestTypeDef] = None,
    VpcInterfaces: List[VpcInterfaceRequestTypeDef] = None
) -> CreateFlowResponseTypeDef:
    pass
```

### delete_flow

Type annotations for `boto3.client("mediaconnect").delete_flow` method.

[Client.delete_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.delete_flow)

```python
def delete_flow(
    self,
    FlowArn: str
) -> DeleteFlowResponseTypeDef:
    pass
```

### describe_flow

Type annotations for `boto3.client("mediaconnect").describe_flow` method.

[Client.describe_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_flow)

```python
def describe_flow(
    self,
    FlowArn: str
) -> DescribeFlowResponseTypeDef:
    pass
```

### describe_offering

Type annotations for `boto3.client("mediaconnect").describe_offering` method.

[Client.describe_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_offering)

```python
def describe_offering(
    self,
    OfferingArn: str
) -> DescribeOfferingResponseTypeDef:
    pass
```

### describe_reservation

Type annotations for `boto3.client("mediaconnect").describe_reservation` method.

[Client.describe_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.describe_reservation)

```python
def describe_reservation(
    self,
    ReservationArn: str
) -> DescribeReservationResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mediaconnect").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.generate_presigned_url)

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

### grant_flow_entitlements

Type annotations for `boto3.client("mediaconnect").grant_flow_entitlements` method.

[Client.grant_flow_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.grant_flow_entitlements)

```python
def grant_flow_entitlements(
    self,
    Entitlements: List[GrantEntitlementRequestTypeDef],
    FlowArn: str
) -> GrantFlowEntitlementsResponseTypeDef:
    pass
```

### list_entitlements

Type annotations for `boto3.client("mediaconnect").list_entitlements` method.

[Client.list_entitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_entitlements)

```python
def list_entitlements(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListEntitlementsResponseTypeDef:
    pass
```

### list_flows

Type annotations for `boto3.client("mediaconnect").list_flows` method.

[Client.list_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_flows)

```python
def list_flows(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListFlowsResponseTypeDef:
    pass
```

### list_offerings

Type annotations for `boto3.client("mediaconnect").list_offerings` method.

[Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_offerings)

```python
def list_offerings(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListOfferingsResponseTypeDef:
    pass
```

### list_reservations

Type annotations for `boto3.client("mediaconnect").list_reservations` method.

[Client.list_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_reservations)

```python
def list_reservations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListReservationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mediaconnect").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### purchase_offering

Type annotations for `boto3.client("mediaconnect").purchase_offering` method.

[Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.purchase_offering)

```python
def purchase_offering(
    self,
    OfferingArn: str,
    ReservationName: str,
    Start: str
) -> PurchaseOfferingResponseTypeDef:
    pass
```

### remove_flow_output

Type annotations for `boto3.client("mediaconnect").remove_flow_output` method.

[Client.remove_flow_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_output)

```python
def remove_flow_output(
    self,
    FlowArn: str,
    OutputArn: str
) -> RemoveFlowOutputResponseTypeDef:
    pass
```

### remove_flow_source

Type annotations for `boto3.client("mediaconnect").remove_flow_source` method.

[Client.remove_flow_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_source)

```python
def remove_flow_source(
    self,
    FlowArn: str,
    SourceArn: str
) -> RemoveFlowSourceResponseTypeDef:
    pass
```

### remove_flow_vpc_interface

Type annotations for `boto3.client("mediaconnect").remove_flow_vpc_interface` method.

[Client.remove_flow_vpc_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.remove_flow_vpc_interface)

```python
def remove_flow_vpc_interface(
    self,
    FlowArn: str,
    VpcInterfaceName: str
) -> RemoveFlowVpcInterfaceResponseTypeDef:
    pass
```

### revoke_flow_entitlement

Type annotations for `boto3.client("mediaconnect").revoke_flow_entitlement` method.

[Client.revoke_flow_entitlement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.revoke_flow_entitlement)

```python
def revoke_flow_entitlement(
    self,
    EntitlementArn: str,
    FlowArn: str
) -> RevokeFlowEntitlementResponseTypeDef:
    pass
```

### start_flow

Type annotations for `boto3.client("mediaconnect").start_flow` method.

[Client.start_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.start_flow)

```python
def start_flow(
    self,
    FlowArn: str
) -> StartFlowResponseTypeDef:
    pass
```

### stop_flow

Type annotations for `boto3.client("mediaconnect").stop_flow` method.

[Client.stop_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.stop_flow)

```python
def stop_flow(
    self,
    FlowArn: str
) -> StopFlowResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("mediaconnect").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("mediaconnect").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_flow

Type annotations for `boto3.client("mediaconnect").update_flow` method.

[Client.update_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow)

```python
def update_flow(
    self,
    FlowArn: str,
    SourceFailoverConfig: UpdateFailoverConfigTypeDef = None
) -> UpdateFlowResponseTypeDef:
    pass
```

### update_flow_entitlement

Type annotations for `boto3.client("mediaconnect").update_flow_entitlement` method.

[Client.update_flow_entitlement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_entitlement)

```python
def update_flow_entitlement(
    self,
    EntitlementArn: str,
    FlowArn: str,
    Description: str = None,
    Encryption: UpdateEncryptionTypeDef = None,
    EntitlementStatus: EntitlementStatus = None,
    Subscribers: List[str] = None
) -> UpdateFlowEntitlementResponseTypeDef:
    pass
```

### update_flow_output

Type annotations for `boto3.client("mediaconnect").update_flow_output` method.

[Client.update_flow_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_output)

```python
def update_flow_output(
    self,
    FlowArn: str,
    OutputArn: str,
    CidrAllowList: List[str] = None,
    Description: str = None,
    Destination: str = None,
    Encryption: UpdateEncryptionTypeDef = None,
    MaxLatency: int = None,
    MinLatency: int = None,
    Port: int = None,
    Protocol: ProtocolType = None,
    RemoteId: str = None,
    SmoothingLatency: int = None,
    StreamId: str = None,
    VpcInterfaceAttachment: "VpcInterfaceAttachmentTypeDef" = None
) -> UpdateFlowOutputResponseTypeDef:
    pass
```

### update_flow_source

Type annotations for `boto3.client("mediaconnect").update_flow_source` method.

[Client.update_flow_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect.Client.update_flow_source)

```python
def update_flow_source(
    self,
    FlowArn: str,
    SourceArn: str,
    Decryption: UpdateEncryptionTypeDef = None,
    Description: str = None,
    EntitlementArn: str = None,
    IngestPort: int = None,
    MaxBitrate: int = None,
    MaxLatency: int = None,
    MinLatency: int = None,
    Protocol: ProtocolType = None,
    StreamId: str = None,
    VpcInterfaceName: str = None,
    WhitelistCidr: str = None
) -> UpdateFlowSourceResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("mediaconnect").get_paginator` method with overloads.

- `client.get_paginator("list_entitlements")` -> [ListEntitlementsPaginator](./paginators.md#listentitlementspaginator)
- `client.get_paginator("list_flows")` -> [ListFlowsPaginator](./paginators.md#listflowspaginator)
- `client.get_paginator("list_offerings")` -> [ListOfferingsPaginator](./paginators.md#listofferingspaginator)
- `client.get_paginator("list_reservations")` -> [ListReservationsPaginator](./paginators.md#listreservationspaginator)




### get_waiter

Type annotations for `boto3.client("mediaconnect").get_waiter` method with overloads.

- `client.get_waiter("flow_active")` -> [FlowActiveWaiter](./waiters.md#flowactivewaiter)
- `client.get_waiter("flow_deleted")` -> [FlowDeletedWaiter](./waiters.md#flowdeletedwaiter)
- `client.get_waiter("flow_standby")` -> [FlowStandbyWaiter](./waiters.md#flowstandbywaiter)
