# GlobalAcceleratorClient for boto3 GlobalAccelerator module

> [Index](../index.md) > [GlobalAccelerator](./index.md) > GlobalAcceleratorClient

Auto-generated documentation for [GlobalAccelerator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator)
type annotations stubs module [mypy_boto3_globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/).

- [GlobalAcceleratorClient for boto3 GlobalAccelerator module](#globalacceleratorclient-for-boto3-globalaccelerator-module)
  - [GlobalAcceleratorClient](#globalacceleratorclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_custom_routing_endpoints](#add_custom_routing_endpoints)
    - [advertise_byoip_cidr](#advertise_byoip_cidr)
    - [allow_custom_routing_traffic](#allow_custom_routing_traffic)
    - [can_paginate](#can_paginate)
    - [create_accelerator](#create_accelerator)
    - [create_custom_routing_accelerator](#create_custom_routing_accelerator)
    - [create_custom_routing_endpoint_group](#create_custom_routing_endpoint_group)
    - [create_custom_routing_listener](#create_custom_routing_listener)
    - [create_endpoint_group](#create_endpoint_group)
    - [create_listener](#create_listener)
    - [delete_accelerator](#delete_accelerator)
    - [delete_custom_routing_accelerator](#delete_custom_routing_accelerator)
    - [delete_custom_routing_endpoint_group](#delete_custom_routing_endpoint_group)
    - [delete_custom_routing_listener](#delete_custom_routing_listener)
    - [delete_endpoint_group](#delete_endpoint_group)
    - [delete_listener](#delete_listener)
    - [deny_custom_routing_traffic](#deny_custom_routing_traffic)
    - [deprovision_byoip_cidr](#deprovision_byoip_cidr)
    - [describe_accelerator](#describe_accelerator)
    - [describe_accelerator_attributes](#describe_accelerator_attributes)
    - [describe_custom_routing_accelerator](#describe_custom_routing_accelerator)
    - [describe_custom_routing_accelerator_attributes](#describe_custom_routing_accelerator_attributes)
    - [describe_custom_routing_endpoint_group](#describe_custom_routing_endpoint_group)
    - [describe_custom_routing_listener](#describe_custom_routing_listener)
    - [describe_endpoint_group](#describe_endpoint_group)
    - [describe_listener](#describe_listener)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_accelerators](#list_accelerators)
    - [list_byoip_cidrs](#list_byoip_cidrs)
    - [list_custom_routing_accelerators](#list_custom_routing_accelerators)
    - [list_custom_routing_endpoint_groups](#list_custom_routing_endpoint_groups)
    - [list_custom_routing_listeners](#list_custom_routing_listeners)
    - [list_custom_routing_port_mappings](#list_custom_routing_port_mappings)
    - [list_custom_routing_port_mappings_by_destination](#list_custom_routing_port_mappings_by_destination)
    - [list_endpoint_groups](#list_endpoint_groups)
    - [list_listeners](#list_listeners)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [provision_byoip_cidr](#provision_byoip_cidr)
    - [remove_custom_routing_endpoints](#remove_custom_routing_endpoints)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_accelerator](#update_accelerator)
    - [update_accelerator_attributes](#update_accelerator_attributes)
    - [update_custom_routing_accelerator](#update_custom_routing_accelerator)
    - [update_custom_routing_accelerator_attributes](#update_custom_routing_accelerator_attributes)
    - [update_custom_routing_listener](#update_custom_routing_listener)
    - [update_endpoint_group](#update_endpoint_group)
    - [update_listener](#update_listener)
    - [withdraw_byoip_cidr](#withdraw_byoip_cidr)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)

## GlobalAcceleratorClient

Type annotations for `boto3.client("globalaccelerator")`

Can be used directly:

```python
from mypy_boto3_globalaccelerator.client import GlobalAcceleratorClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_globalaccelerator.client import Exceptions

def handle_error(exc: Exceptions.AcceleratorNotDisabledException) -> None:
    ...
```


Exceptions:

- `Exceptions.AcceleratorNotDisabledException`
- `Exceptions.AcceleratorNotFoundException`
- `Exceptions.AccessDeniedException`
- `Exceptions.AssociatedEndpointGroupFoundException`
- `Exceptions.AssociatedListenerFoundException`
- `Exceptions.ByoipCidrNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.EndpointAlreadyExistsException`
- `Exceptions.EndpointGroupAlreadyExistsException`
- `Exceptions.EndpointGroupNotFoundException`
- `Exceptions.EndpointNotFoundException`
- `Exceptions.IncorrectCidrStateException`
- `Exceptions.InternalServiceErrorException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidPortRangeException`
- `Exceptions.LimitExceededException`
- `Exceptions.ListenerNotFoundException`


## Methods


### add_custom_routing_endpoints

Type annotations for `boto3.client("globalaccelerator").add_custom_routing_endpoints` method.

[Client.add_custom_routing_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.add_custom_routing_endpoints)

```python
def add_custom_routing_endpoints(
    self,
    EndpointConfigurations: List[CustomRoutingEndpointConfigurationTypeDef],
    EndpointGroupArn: str
) -> AddCustomRoutingEndpointsResponseTypeDef:
    pass
```

### advertise_byoip_cidr

Type annotations for `boto3.client("globalaccelerator").advertise_byoip_cidr` method.

[Client.advertise_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.advertise_byoip_cidr)

```python
def advertise_byoip_cidr(
    self,
    Cidr: str
) -> AdvertiseByoipCidrResponseTypeDef:
    pass
```

### allow_custom_routing_traffic

Type annotations for `boto3.client("globalaccelerator").allow_custom_routing_traffic` method.

[Client.allow_custom_routing_traffic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.allow_custom_routing_traffic)

```python
def allow_custom_routing_traffic(
    self,
    EndpointGroupArn: str,
    EndpointId: str,
    DestinationAddresses: List[str] = None,
    DestinationPorts: List[int] = None,
    AllowAllTrafficToEndpoint: bool = None
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("globalaccelerator").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_accelerator

Type annotations for `boto3.client("globalaccelerator").create_accelerator` method.

[Client.create_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_accelerator)

```python
def create_accelerator(
    self,
    Name: str,
    IdempotencyToken: str,
    IpAddressType: IpAddressType = None,
    IpAddresses: List[str] = None,
    Enabled: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAcceleratorResponseTypeDef:
    pass
```

### create_custom_routing_accelerator

Type annotations for `boto3.client("globalaccelerator").create_custom_routing_accelerator` method.

[Client.create_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_accelerator)

```python
def create_custom_routing_accelerator(
    self,
    Name: str,
    IdempotencyToken: str,
    IpAddressType: IpAddressType = None,
    IpAddresses: List[str] = None,
    Enabled: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateCustomRoutingAcceleratorResponseTypeDef:
    pass
```

### create_custom_routing_endpoint_group

Type annotations for `boto3.client("globalaccelerator").create_custom_routing_endpoint_group` method.

[Client.create_custom_routing_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_endpoint_group)

```python
def create_custom_routing_endpoint_group(
    self,
    ListenerArn: str,
    EndpointGroupRegion: str,
    DestinationConfigurations: List[CustomRoutingDestinationConfigurationTypeDef],
    IdempotencyToken: str
) -> CreateCustomRoutingEndpointGroupResponseTypeDef:
    pass
```

### create_custom_routing_listener

Type annotations for `boto3.client("globalaccelerator").create_custom_routing_listener` method.

[Client.create_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_custom_routing_listener)

```python
def create_custom_routing_listener(
    self,
    AcceleratorArn: str,
    PortRanges: List["PortRangeTypeDef"],
    IdempotencyToken: str
) -> CreateCustomRoutingListenerResponseTypeDef:
    pass
```

### create_endpoint_group

Type annotations for `boto3.client("globalaccelerator").create_endpoint_group` method.

[Client.create_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_endpoint_group)

```python
def create_endpoint_group(
    self,
    ListenerArn: str,
    EndpointGroupRegion: str,
    IdempotencyToken: str,
    EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
    TrafficDialPercentage: float = None,
    HealthCheckPort: int = None,
    HealthCheckProtocol: HealthCheckProtocol = None,
    HealthCheckPath: str = None,
    HealthCheckIntervalSeconds: int = None,
    ThresholdCount: int = None,
    PortOverrides: List["PortOverrideTypeDef"] = None
) -> CreateEndpointGroupResponseTypeDef:
    pass
```

### create_listener

Type annotations for `boto3.client("globalaccelerator").create_listener` method.

[Client.create_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.create_listener)

```python
def create_listener(
    self,
    AcceleratorArn: str,
    PortRanges: List["PortRangeTypeDef"],
    Protocol: ProtocolType,
    IdempotencyToken: str,
    ClientAffinity: ClientAffinity = None
) -> CreateListenerResponseTypeDef:
    pass
```

### delete_accelerator

Type annotations for `boto3.client("globalaccelerator").delete_accelerator` method.

[Client.delete_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_accelerator)

```python
def delete_accelerator(
    self,
    AcceleratorArn: str
) -> None:
    pass
```

### delete_custom_routing_accelerator

Type annotations for `boto3.client("globalaccelerator").delete_custom_routing_accelerator` method.

[Client.delete_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_accelerator)

```python
def delete_custom_routing_accelerator(
    self,
    AcceleratorArn: str
) -> None:
    pass
```

### delete_custom_routing_endpoint_group

Type annotations for `boto3.client("globalaccelerator").delete_custom_routing_endpoint_group` method.

[Client.delete_custom_routing_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_endpoint_group)

```python
def delete_custom_routing_endpoint_group(
    self,
    EndpointGroupArn: str
) -> None:
    pass
```

### delete_custom_routing_listener

Type annotations for `boto3.client("globalaccelerator").delete_custom_routing_listener` method.

[Client.delete_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_custom_routing_listener)

```python
def delete_custom_routing_listener(
    self,
    ListenerArn: str
) -> None:
    pass
```

### delete_endpoint_group

Type annotations for `boto3.client("globalaccelerator").delete_endpoint_group` method.

[Client.delete_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_endpoint_group)

```python
def delete_endpoint_group(
    self,
    EndpointGroupArn: str
) -> None:
    pass
```

### delete_listener

Type annotations for `boto3.client("globalaccelerator").delete_listener` method.

[Client.delete_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.delete_listener)

```python
def delete_listener(
    self,
    ListenerArn: str
) -> None:
    pass
```

### deny_custom_routing_traffic

Type annotations for `boto3.client("globalaccelerator").deny_custom_routing_traffic` method.

[Client.deny_custom_routing_traffic documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deny_custom_routing_traffic)

```python
def deny_custom_routing_traffic(
    self,
    EndpointGroupArn: str,
    EndpointId: str,
    DestinationAddresses: List[str] = None,
    DestinationPorts: List[int] = None,
    DenyAllTrafficToEndpoint: bool = None
) -> None:
    pass
```

### deprovision_byoip_cidr

Type annotations for `boto3.client("globalaccelerator").deprovision_byoip_cidr` method.

[Client.deprovision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.deprovision_byoip_cidr)

```python
def deprovision_byoip_cidr(
    self,
    Cidr: str
) -> DeprovisionByoipCidrResponseTypeDef:
    pass
```

### describe_accelerator

Type annotations for `boto3.client("globalaccelerator").describe_accelerator` method.

[Client.describe_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator)

```python
def describe_accelerator(
    self,
    AcceleratorArn: str
) -> DescribeAcceleratorResponseTypeDef:
    pass
```

### describe_accelerator_attributes

Type annotations for `boto3.client("globalaccelerator").describe_accelerator_attributes` method.

[Client.describe_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_accelerator_attributes)

```python
def describe_accelerator_attributes(
    self,
    AcceleratorArn: str
) -> DescribeAcceleratorAttributesResponseTypeDef:
    pass
```

### describe_custom_routing_accelerator

Type annotations for `boto3.client("globalaccelerator").describe_custom_routing_accelerator` method.

[Client.describe_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator)

```python
def describe_custom_routing_accelerator(
    self,
    AcceleratorArn: str
) -> DescribeCustomRoutingAcceleratorResponseTypeDef:
    pass
```

### describe_custom_routing_accelerator_attributes

Type annotations for `boto3.client("globalaccelerator").describe_custom_routing_accelerator_attributes` method.

[Client.describe_custom_routing_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_accelerator_attributes)

```python
def describe_custom_routing_accelerator_attributes(
    self,
    AcceleratorArn: str
) -> DescribeCustomRoutingAcceleratorAttributesResponseTypeDef:
    pass
```

### describe_custom_routing_endpoint_group

Type annotations for `boto3.client("globalaccelerator").describe_custom_routing_endpoint_group` method.

[Client.describe_custom_routing_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_endpoint_group)

```python
def describe_custom_routing_endpoint_group(
    self,
    EndpointGroupArn: str
) -> DescribeCustomRoutingEndpointGroupResponseTypeDef:
    pass
```

### describe_custom_routing_listener

Type annotations for `boto3.client("globalaccelerator").describe_custom_routing_listener` method.

[Client.describe_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_custom_routing_listener)

```python
def describe_custom_routing_listener(
    self,
    ListenerArn: str
) -> DescribeCustomRoutingListenerResponseTypeDef:
    pass
```

### describe_endpoint_group

Type annotations for `boto3.client("globalaccelerator").describe_endpoint_group` method.

[Client.describe_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_endpoint_group)

```python
def describe_endpoint_group(
    self,
    EndpointGroupArn: str
) -> DescribeEndpointGroupResponseTypeDef:
    pass
```

### describe_listener

Type annotations for `boto3.client("globalaccelerator").describe_listener` method.

[Client.describe_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.describe_listener)

```python
def describe_listener(
    self,
    ListenerArn: str
) -> DescribeListenerResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("globalaccelerator").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.generate_presigned_url)

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

### list_accelerators

Type annotations for `boto3.client("globalaccelerator").list_accelerators` method.

[Client.list_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_accelerators)

```python
def list_accelerators(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAcceleratorsResponseTypeDef:
    pass
```

### list_byoip_cidrs

Type annotations for `boto3.client("globalaccelerator").list_byoip_cidrs` method.

[Client.list_byoip_cidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_byoip_cidrs)

```python
def list_byoip_cidrs(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListByoipCidrsResponseTypeDef:
    pass
```

### list_custom_routing_accelerators

Type annotations for `boto3.client("globalaccelerator").list_custom_routing_accelerators` method.

[Client.list_custom_routing_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_accelerators)

```python
def list_custom_routing_accelerators(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCustomRoutingAcceleratorsResponseTypeDef:
    pass
```

### list_custom_routing_endpoint_groups

Type annotations for `boto3.client("globalaccelerator").list_custom_routing_endpoint_groups` method.

[Client.list_custom_routing_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_endpoint_groups)

```python
def list_custom_routing_endpoint_groups(
    self,
    ListenerArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCustomRoutingEndpointGroupsResponseTypeDef:
    pass
```

### list_custom_routing_listeners

Type annotations for `boto3.client("globalaccelerator").list_custom_routing_listeners` method.

[Client.list_custom_routing_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_listeners)

```python
def list_custom_routing_listeners(
    self,
    AcceleratorArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCustomRoutingListenersResponseTypeDef:
    pass
```

### list_custom_routing_port_mappings

Type annotations for `boto3.client("globalaccelerator").list_custom_routing_port_mappings` method.

[Client.list_custom_routing_port_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings)

```python
def list_custom_routing_port_mappings(
    self,
    AcceleratorArn: str,
    EndpointGroupArn: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCustomRoutingPortMappingsResponseTypeDef:
    pass
```

### list_custom_routing_port_mappings_by_destination

Type annotations for `boto3.client("globalaccelerator").list_custom_routing_port_mappings_by_destination` method.

[Client.list_custom_routing_port_mappings_by_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_custom_routing_port_mappings_by_destination)

```python
def list_custom_routing_port_mappings_by_destination(
    self,
    EndpointId: str,
    DestinationAddress: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListCustomRoutingPortMappingsByDestinationResponseTypeDef:
    pass
```

### list_endpoint_groups

Type annotations for `boto3.client("globalaccelerator").list_endpoint_groups` method.

[Client.list_endpoint_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_endpoint_groups)

```python
def list_endpoint_groups(
    self,
    ListenerArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListEndpointGroupsResponseTypeDef:
    pass
```

### list_listeners

Type annotations for `boto3.client("globalaccelerator").list_listeners` method.

[Client.list_listeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_listeners)

```python
def list_listeners(
    self,
    AcceleratorArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListListenersResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("globalaccelerator").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### provision_byoip_cidr

Type annotations for `boto3.client("globalaccelerator").provision_byoip_cidr` method.

[Client.provision_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.provision_byoip_cidr)

```python
def provision_byoip_cidr(
    self,
    Cidr: str,
    CidrAuthorizationContext: CidrAuthorizationContextTypeDef
) -> ProvisionByoipCidrResponseTypeDef:
    pass
```

### remove_custom_routing_endpoints

Type annotations for `boto3.client("globalaccelerator").remove_custom_routing_endpoints` method.

[Client.remove_custom_routing_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.remove_custom_routing_endpoints)

```python
def remove_custom_routing_endpoints(
    self,
    EndpointIds: List[str],
    EndpointGroupArn: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("globalaccelerator").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("globalaccelerator").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_accelerator

Type annotations for `boto3.client("globalaccelerator").update_accelerator` method.

[Client.update_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator)

```python
def update_accelerator(
    self,
    AcceleratorArn: str,
    Name: str = None,
    IpAddressType: IpAddressType = None,
    Enabled: bool = None
) -> UpdateAcceleratorResponseTypeDef:
    pass
```

### update_accelerator_attributes

Type annotations for `boto3.client("globalaccelerator").update_accelerator_attributes` method.

[Client.update_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_accelerator_attributes)

```python
def update_accelerator_attributes(
    self,
    AcceleratorArn: str,
    FlowLogsEnabled: bool = None,
    FlowLogsS3Bucket: str = None,
    FlowLogsS3Prefix: str = None
) -> UpdateAcceleratorAttributesResponseTypeDef:
    pass
```

### update_custom_routing_accelerator

Type annotations for `boto3.client("globalaccelerator").update_custom_routing_accelerator` method.

[Client.update_custom_routing_accelerator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator)

```python
def update_custom_routing_accelerator(
    self,
    AcceleratorArn: str,
    Name: str = None,
    IpAddressType: IpAddressType = None,
    Enabled: bool = None
) -> UpdateCustomRoutingAcceleratorResponseTypeDef:
    pass
```

### update_custom_routing_accelerator_attributes

Type annotations for `boto3.client("globalaccelerator").update_custom_routing_accelerator_attributes` method.

[Client.update_custom_routing_accelerator_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_accelerator_attributes)

```python
def update_custom_routing_accelerator_attributes(
    self,
    AcceleratorArn: str,
    FlowLogsEnabled: bool = None,
    FlowLogsS3Bucket: str = None,
    FlowLogsS3Prefix: str = None
) -> UpdateCustomRoutingAcceleratorAttributesResponseTypeDef:
    pass
```

### update_custom_routing_listener

Type annotations for `boto3.client("globalaccelerator").update_custom_routing_listener` method.

[Client.update_custom_routing_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_custom_routing_listener)

```python
def update_custom_routing_listener(
    self,
    ListenerArn: str,
    PortRanges: List["PortRangeTypeDef"]
) -> UpdateCustomRoutingListenerResponseTypeDef:
    pass
```

### update_endpoint_group

Type annotations for `boto3.client("globalaccelerator").update_endpoint_group` method.

[Client.update_endpoint_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_endpoint_group)

```python
def update_endpoint_group(
    self,
    EndpointGroupArn: str,
    EndpointConfigurations: List[EndpointConfigurationTypeDef] = None,
    TrafficDialPercentage: float = None,
    HealthCheckPort: int = None,
    HealthCheckProtocol: HealthCheckProtocol = None,
    HealthCheckPath: str = None,
    HealthCheckIntervalSeconds: int = None,
    ThresholdCount: int = None,
    PortOverrides: List["PortOverrideTypeDef"] = None
) -> UpdateEndpointGroupResponseTypeDef:
    pass
```

### update_listener

Type annotations for `boto3.client("globalaccelerator").update_listener` method.

[Client.update_listener documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.update_listener)

```python
def update_listener(
    self,
    ListenerArn: str,
    PortRanges: List["PortRangeTypeDef"] = None,
    Protocol: ProtocolType = None,
    ClientAffinity: ClientAffinity = None
) -> UpdateListenerResponseTypeDef:
    pass
```

### withdraw_byoip_cidr

Type annotations for `boto3.client("globalaccelerator").withdraw_byoip_cidr` method.

[Client.withdraw_byoip_cidr documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Client.withdraw_byoip_cidr)

```python
def withdraw_byoip_cidr(
    self,
    Cidr: str
) -> WithdrawByoipCidrResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListAccelerators)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAcceleratorsPaginatorName
) -> ListAcceleratorsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListByoipCidrs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListByoipCidrs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListByoipCidrsPaginatorName
) -> ListByoipCidrsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListCustomRoutingAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingAccelerators)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCustomRoutingAcceleratorsPaginatorName
) -> ListCustomRoutingAcceleratorsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListCustomRoutingListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingListeners)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCustomRoutingListenersPaginatorName
) -> ListCustomRoutingListenersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListCustomRoutingPortMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappings)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCustomRoutingPortMappingsPaginatorName
) -> ListCustomRoutingPortMappingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListCustomRoutingPortMappingsByDestination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListCustomRoutingPortMappingsByDestination)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCustomRoutingPortMappingsByDestinationPaginatorName
) -> ListCustomRoutingPortMappingsByDestinationPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListEndpointGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListEndpointGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListEndpointGroupsPaginatorName
) -> ListEndpointGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("globalaccelerator").get_paginator` method.

[Paginator.ListListeners documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator.Paginator.ListListeners)

```python
@overload
def get_paginator(
    self,
    operation_name: ListListenersPaginatorName
) -> ListListenersPaginator:
    pass
```