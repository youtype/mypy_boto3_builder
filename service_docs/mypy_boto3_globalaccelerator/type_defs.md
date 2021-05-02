# Structures for boto3 GlobalAccelerator module

> [Index](../index.md) > [GlobalAccelerator](./index.md) > Structures

Auto-generated documentation for [GlobalAccelerator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator)
type annotations stubs module [mypy_boto3_globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/).

- [Structures for boto3 GlobalAccelerator module](#structures-for-boto3-globalaccelerator-module)
  - [AcceleratorAttributesTypeDef](#acceleratorattributestypedef)
  - [AcceleratorTypeDef](#acceleratortypedef)
  - [ByoipCidrEventTypeDef](#byoipcidreventtypedef)
  - [ByoipCidrTypeDef](#byoipcidrtypedef)
  - [CustomRoutingAcceleratorAttributesTypeDef](#customroutingacceleratorattributestypedef)
  - [CustomRoutingAcceleratorTypeDef](#customroutingacceleratortypedef)
  - [CustomRoutingDestinationDescriptionTypeDef](#customroutingdestinationdescriptiontypedef)
  - [CustomRoutingEndpointDescriptionTypeDef](#customroutingendpointdescriptiontypedef)
  - [CustomRoutingEndpointGroupTypeDef](#customroutingendpointgrouptypedef)
  - [CustomRoutingListenerTypeDef](#customroutinglistenertypedef)
  - [DestinationPortMappingTypeDef](#destinationportmappingtypedef)
  - [EndpointDescriptionTypeDef](#endpointdescriptiontypedef)
  - [EndpointGroupTypeDef](#endpointgrouptypedef)
  - [IpSetTypeDef](#ipsettypedef)
  - [ListenerTypeDef](#listenertypedef)
  - [PortMappingTypeDef](#portmappingtypedef)
  - [PortOverrideTypeDef](#portoverridetypedef)
  - [PortRangeTypeDef](#portrangetypedef)
  - [SocketAddressTypeDef](#socketaddresstypedef)
  - [TagTypeDef](#tagtypedef)
  - [AddCustomRoutingEndpointsResponseTypeDef](#addcustomroutingendpointsresponsetypedef)
  - [AdvertiseByoipCidrResponseTypeDef](#advertisebyoipcidrresponsetypedef)
  - [CidrAuthorizationContextTypeDef](#cidrauthorizationcontexttypedef)
  - [CreateAcceleratorResponseTypeDef](#createacceleratorresponsetypedef)
  - [CreateCustomRoutingAcceleratorResponseTypeDef](#createcustomroutingacceleratorresponsetypedef)
  - [CreateCustomRoutingEndpointGroupResponseTypeDef](#createcustomroutingendpointgroupresponsetypedef)
  - [CreateCustomRoutingListenerResponseTypeDef](#createcustomroutinglistenerresponsetypedef)
  - [CreateEndpointGroupResponseTypeDef](#createendpointgroupresponsetypedef)
  - [CreateListenerResponseTypeDef](#createlistenerresponsetypedef)
  - [CustomRoutingDestinationConfigurationTypeDef](#customroutingdestinationconfigurationtypedef)
  - [CustomRoutingEndpointConfigurationTypeDef](#customroutingendpointconfigurationtypedef)
  - [DeprovisionByoipCidrResponseTypeDef](#deprovisionbyoipcidrresponsetypedef)
  - [DescribeAcceleratorAttributesResponseTypeDef](#describeacceleratorattributesresponsetypedef)
  - [DescribeAcceleratorResponseTypeDef](#describeacceleratorresponsetypedef)
  - [DescribeCustomRoutingAcceleratorAttributesResponseTypeDef](#describecustomroutingacceleratorattributesresponsetypedef)
  - [DescribeCustomRoutingAcceleratorResponseTypeDef](#describecustomroutingacceleratorresponsetypedef)
  - [DescribeCustomRoutingEndpointGroupResponseTypeDef](#describecustomroutingendpointgroupresponsetypedef)
  - [DescribeCustomRoutingListenerResponseTypeDef](#describecustomroutinglistenerresponsetypedef)
  - [DescribeEndpointGroupResponseTypeDef](#describeendpointgroupresponsetypedef)
  - [DescribeListenerResponseTypeDef](#describelistenerresponsetypedef)
  - [EndpointConfigurationTypeDef](#endpointconfigurationtypedef)
  - [ListAcceleratorsResponseTypeDef](#listacceleratorsresponsetypedef)
  - [ListByoipCidrsResponseTypeDef](#listbyoipcidrsresponsetypedef)
  - [ListCustomRoutingAcceleratorsResponseTypeDef](#listcustomroutingacceleratorsresponsetypedef)
  - [ListCustomRoutingEndpointGroupsResponseTypeDef](#listcustomroutingendpointgroupsresponsetypedef)
  - [ListCustomRoutingListenersResponseTypeDef](#listcustomroutinglistenersresponsetypedef)
  - [ListCustomRoutingPortMappingsByDestinationResponseTypeDef](#listcustomroutingportmappingsbydestinationresponsetypedef)
  - [ListCustomRoutingPortMappingsResponseTypeDef](#listcustomroutingportmappingsresponsetypedef)
  - [ListEndpointGroupsResponseTypeDef](#listendpointgroupsresponsetypedef)
  - [ListListenersResponseTypeDef](#listlistenersresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProvisionByoipCidrResponseTypeDef](#provisionbyoipcidrresponsetypedef)
  - [UpdateAcceleratorAttributesResponseTypeDef](#updateacceleratorattributesresponsetypedef)
  - [UpdateAcceleratorResponseTypeDef](#updateacceleratorresponsetypedef)
  - [UpdateCustomRoutingAcceleratorAttributesResponseTypeDef](#updatecustomroutingacceleratorattributesresponsetypedef)
  - [UpdateCustomRoutingAcceleratorResponseTypeDef](#updatecustomroutingacceleratorresponsetypedef)
  - [UpdateCustomRoutingListenerResponseTypeDef](#updatecustomroutinglistenerresponsetypedef)
  - [UpdateEndpointGroupResponseTypeDef](#updateendpointgroupresponsetypedef)
  - [UpdateListenerResponseTypeDef](#updatelistenerresponsetypedef)
  - [WithdrawByoipCidrResponseTypeDef](#withdrawbyoipcidrresponsetypedef)

## AcceleratorAttributesTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef
```




Optional fields:
- `FlowLogsEnabled`: `bool`
- `FlowLogsS3Bucket`: `str`
- `FlowLogsS3Prefix`: `str`


## AcceleratorTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import AcceleratorTypeDef
```




Optional fields:
- `AcceleratorArn`: `str`
- `Name`: `str`
- `IpAddressType`: `IpAddressType`
- `Enabled`: `bool`
- `IpSets`: `List["IpSetTypeDef"]`
- `DnsName`: `str`
- `Status`: `AcceleratorStatus`
- `CreatedTime`: `datetime`
- `LastModifiedTime`: `datetime`


## ByoipCidrEventTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ByoipCidrEventTypeDef
```




Optional fields:
- `Message`: `str`
- `Timestamp`: `datetime`


## ByoipCidrTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ByoipCidrTypeDef
```




Optional fields:
- `Cidr`: `str`
- `State`: `ByoipCidrState`
- `Events`: `List["ByoipCidrEventTypeDef"]`


## CustomRoutingAcceleratorAttributesTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingAcceleratorAttributesTypeDef
```




Optional fields:
- `FlowLogsEnabled`: `bool`
- `FlowLogsS3Bucket`: `str`
- `FlowLogsS3Prefix`: `str`


## CustomRoutingAcceleratorTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingAcceleratorTypeDef
```




Optional fields:
- `AcceleratorArn`: `str`
- `Name`: `str`
- `IpAddressType`: `IpAddressType`
- `Enabled`: `bool`
- `IpSets`: `List["IpSetTypeDef"]`
- `DnsName`: `str`
- `Status`: `CustomRoutingAcceleratorStatus`
- `CreatedTime`: `datetime`
- `LastModifiedTime`: `datetime`


## CustomRoutingDestinationDescriptionTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingDestinationDescriptionTypeDef
```




Optional fields:
- `FromPort`: `int`
- `ToPort`: `int`
- `Protocols`: `List[ProtocolType]`


## CustomRoutingEndpointDescriptionTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingEndpointDescriptionTypeDef
```




Optional fields:
- `EndpointId`: `str`


## CustomRoutingEndpointGroupTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingEndpointGroupTypeDef
```




Optional fields:
- `EndpointGroupArn`: `str`
- `EndpointGroupRegion`: `str`
- `DestinationDescriptions`: `List["CustomRoutingDestinationDescriptionTypeDef"]`
- `EndpointDescriptions`: `List["CustomRoutingEndpointDescriptionTypeDef"]`


## CustomRoutingListenerTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingListenerTypeDef
```




Optional fields:
- `ListenerArn`: `str`
- `PortRanges`: `List["PortRangeTypeDef"]`


## DestinationPortMappingTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DestinationPortMappingTypeDef
```




Optional fields:
- `AcceleratorArn`: `str`
- `AcceleratorSocketAddresses`: `List["SocketAddressTypeDef"]`
- `EndpointGroupArn`: `str`
- `EndpointId`: `str`
- `EndpointGroupRegion`: `str`
- `DestinationSocketAddress`: `"SocketAddressTypeDef"`
- `IpAddressType`: `IpAddressType`
- `DestinationTrafficState`: `CustomRoutingDestinationTrafficState`


## EndpointDescriptionTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import EndpointDescriptionTypeDef
```




Optional fields:
- `EndpointId`: `str`
- `Weight`: `int`
- `HealthState`: `HealthState`
- `HealthReason`: `str`
- `ClientIPPreservationEnabled`: `bool`


## EndpointGroupTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import EndpointGroupTypeDef
```




Optional fields:
- `EndpointGroupArn`: `str`
- `EndpointGroupRegion`: `str`
- `EndpointDescriptions`: `List["EndpointDescriptionTypeDef"]`
- `TrafficDialPercentage`: `float`
- `HealthCheckPort`: `int`
- `HealthCheckProtocol`: `HealthCheckProtocol`
- `HealthCheckPath`: `str`
- `HealthCheckIntervalSeconds`: `int`
- `ThresholdCount`: `int`
- `PortOverrides`: `List["PortOverrideTypeDef"]`


## IpSetTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import IpSetTypeDef
```




Optional fields:
- `IpFamily`: `str`
- `IpAddresses`: `List[str]`


## ListenerTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListenerTypeDef
```




Optional fields:
- `ListenerArn`: `str`
- `PortRanges`: `List["PortRangeTypeDef"]`
- `Protocol`: `ProtocolType`
- `ClientAffinity`: `ClientAffinity`


## PortMappingTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import PortMappingTypeDef
```




Optional fields:
- `AcceleratorPort`: `int`
- `EndpointGroupArn`: `str`
- `EndpointId`: `str`
- `DestinationSocketAddress`: `"SocketAddressTypeDef"`
- `Protocols`: `List[CustomRoutingProtocol]`
- `DestinationTrafficState`: `CustomRoutingDestinationTrafficState`


## PortOverrideTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import PortOverrideTypeDef
```




Optional fields:
- `ListenerPort`: `int`
- `EndpointPort`: `int`


## PortRangeTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import PortRangeTypeDef
```




Optional fields:
- `FromPort`: `int`
- `ToPort`: `int`


## SocketAddressTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import SocketAddressTypeDef
```




Optional fields:
- `IpAddress`: `str`
- `Port`: `int`


## TagTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## AddCustomRoutingEndpointsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import AddCustomRoutingEndpointsResponseTypeDef
```




Optional fields:
- `EndpointDescriptions`: `List["CustomRoutingEndpointDescriptionTypeDef"]`
- `EndpointGroupArn`: `str`


## AdvertiseByoipCidrResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import AdvertiseByoipCidrResponseTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`


## CidrAuthorizationContextTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CidrAuthorizationContextTypeDef
```


Required fields:
- `Message`: `str`
- `Signature`: `str`




## CreateAcceleratorResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CreateAcceleratorResponseTypeDef
```




Optional fields:
- `Accelerator`: `"AcceleratorTypeDef"`


## CreateCustomRoutingAcceleratorResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CreateCustomRoutingAcceleratorResponseTypeDef
```




Optional fields:
- `Accelerator`: `"CustomRoutingAcceleratorTypeDef"`


## CreateCustomRoutingEndpointGroupResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CreateCustomRoutingEndpointGroupResponseTypeDef
```




Optional fields:
- `EndpointGroup`: `"CustomRoutingEndpointGroupTypeDef"`


## CreateCustomRoutingListenerResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CreateCustomRoutingListenerResponseTypeDef
```




Optional fields:
- `Listener`: `"CustomRoutingListenerTypeDef"`


## CreateEndpointGroupResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CreateEndpointGroupResponseTypeDef
```




Optional fields:
- `EndpointGroup`: `"EndpointGroupTypeDef"`


## CreateListenerResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CreateListenerResponseTypeDef
```




Optional fields:
- `Listener`: `"ListenerTypeDef"`


## CustomRoutingDestinationConfigurationTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingDestinationConfigurationTypeDef
```


Required fields:
- `FromPort`: `int`
- `ToPort`: `int`
- `Protocols`: `List[CustomRoutingProtocol]`




## CustomRoutingEndpointConfigurationTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import CustomRoutingEndpointConfigurationTypeDef
```




Optional fields:
- `EndpointId`: `str`


## DeprovisionByoipCidrResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DeprovisionByoipCidrResponseTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`


## DescribeAcceleratorAttributesResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeAcceleratorAttributesResponseTypeDef
```




Optional fields:
- `AcceleratorAttributes`: `"AcceleratorAttributesTypeDef"`


## DescribeAcceleratorResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeAcceleratorResponseTypeDef
```




Optional fields:
- `Accelerator`: `"AcceleratorTypeDef"`


## DescribeCustomRoutingAcceleratorAttributesResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeCustomRoutingAcceleratorAttributesResponseTypeDef
```




Optional fields:
- `AcceleratorAttributes`: `"CustomRoutingAcceleratorAttributesTypeDef"`


## DescribeCustomRoutingAcceleratorResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeCustomRoutingAcceleratorResponseTypeDef
```




Optional fields:
- `Accelerator`: `"CustomRoutingAcceleratorTypeDef"`


## DescribeCustomRoutingEndpointGroupResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeCustomRoutingEndpointGroupResponseTypeDef
```




Optional fields:
- `EndpointGroup`: `"CustomRoutingEndpointGroupTypeDef"`


## DescribeCustomRoutingListenerResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeCustomRoutingListenerResponseTypeDef
```




Optional fields:
- `Listener`: `"CustomRoutingListenerTypeDef"`


## DescribeEndpointGroupResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeEndpointGroupResponseTypeDef
```




Optional fields:
- `EndpointGroup`: `"EndpointGroupTypeDef"`


## DescribeListenerResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import DescribeListenerResponseTypeDef
```




Optional fields:
- `Listener`: `"ListenerTypeDef"`


## EndpointConfigurationTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import EndpointConfigurationTypeDef
```




Optional fields:
- `EndpointId`: `str`
- `Weight`: `int`
- `ClientIPPreservationEnabled`: `bool`


## ListAcceleratorsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListAcceleratorsResponseTypeDef
```




Optional fields:
- `Accelerators`: `List["AcceleratorTypeDef"]`
- `NextToken`: `str`


## ListByoipCidrsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListByoipCidrsResponseTypeDef
```




Optional fields:
- `ByoipCidrs`: `List["ByoipCidrTypeDef"]`
- `NextToken`: `str`


## ListCustomRoutingAcceleratorsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListCustomRoutingAcceleratorsResponseTypeDef
```




Optional fields:
- `Accelerators`: `List["CustomRoutingAcceleratorTypeDef"]`
- `NextToken`: `str`


## ListCustomRoutingEndpointGroupsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListCustomRoutingEndpointGroupsResponseTypeDef
```




Optional fields:
- `EndpointGroups`: `List["CustomRoutingEndpointGroupTypeDef"]`
- `NextToken`: `str`


## ListCustomRoutingListenersResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListCustomRoutingListenersResponseTypeDef
```




Optional fields:
- `Listeners`: `List["CustomRoutingListenerTypeDef"]`
- `NextToken`: `str`


## ListCustomRoutingPortMappingsByDestinationResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListCustomRoutingPortMappingsByDestinationResponseTypeDef
```




Optional fields:
- `DestinationPortMappings`: `List["DestinationPortMappingTypeDef"]`
- `NextToken`: `str`


## ListCustomRoutingPortMappingsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListCustomRoutingPortMappingsResponseTypeDef
```




Optional fields:
- `PortMappings`: `List["PortMappingTypeDef"]`
- `NextToken`: `str`


## ListEndpointGroupsResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListEndpointGroupsResponseTypeDef
```




Optional fields:
- `EndpointGroups`: `List["EndpointGroupTypeDef"]`
- `NextToken`: `str`


## ListListenersResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListListenersResponseTypeDef
```




Optional fields:
- `Listeners`: `List["ListenerTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProvisionByoipCidrResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import ProvisionByoipCidrResponseTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`


## UpdateAcceleratorAttributesResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateAcceleratorAttributesResponseTypeDef
```




Optional fields:
- `AcceleratorAttributes`: `"AcceleratorAttributesTypeDef"`


## UpdateAcceleratorResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateAcceleratorResponseTypeDef
```




Optional fields:
- `Accelerator`: `"AcceleratorTypeDef"`


## UpdateCustomRoutingAcceleratorAttributesResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateCustomRoutingAcceleratorAttributesResponseTypeDef
```




Optional fields:
- `AcceleratorAttributes`: `"CustomRoutingAcceleratorAttributesTypeDef"`


## UpdateCustomRoutingAcceleratorResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateCustomRoutingAcceleratorResponseTypeDef
```




Optional fields:
- `Accelerator`: `"CustomRoutingAcceleratorTypeDef"`


## UpdateCustomRoutingListenerResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateCustomRoutingListenerResponseTypeDef
```




Optional fields:
- `Listener`: `"CustomRoutingListenerTypeDef"`


## UpdateEndpointGroupResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateEndpointGroupResponseTypeDef
```




Optional fields:
- `EndpointGroup`: `"EndpointGroupTypeDef"`


## UpdateListenerResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import UpdateListenerResponseTypeDef
```




Optional fields:
- `Listener`: `"ListenerTypeDef"`


## WithdrawByoipCidrResponseTypeDef

```python
from mypy_boto3_globalaccelerator.type_defs import WithdrawByoipCidrResponseTypeDef
```




Optional fields:
- `ByoipCidr`: `"ByoipCidrTypeDef"`

