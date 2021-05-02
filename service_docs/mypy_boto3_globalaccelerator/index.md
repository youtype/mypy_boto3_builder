# Type annotations for boto3 GlobalAccelerator module

> [Index](../index.md) > GlobalAccelerator

Auto-generated documentation for [GlobalAccelerator](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html#GlobalAccelerator)
type annotations stubs module [mypy_boto3_globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/).

```bash
pip install mypy-boto3-globalaccelerator
```

- [Type annotations for boto3 GlobalAccelerator module](#type-annotations-for-boto3-globalaccelerator-module)
  - [GlobalAcceleratorClient](#globalacceleratorclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## GlobalAcceleratorClient

Type annotations for  `boto3.client("globalaccelerator")` as [GlobalAcceleratorClient](./client.md)

Can be used directly:

```python
from mypy_boto3_globalaccelerator.client import GlobalAcceleratorClient
```


GlobalAcceleratorClient [exceptions](./client.md#exceptions)



### Methods
- [add_custom_routing_endpoints](./client.md#add-custom-routing-endpoints)
- [advertise_byoip_cidr](./client.md#advertise-byoip-cidr)
- [allow_custom_routing_traffic](./client.md#allow-custom-routing-traffic)
- [can_paginate](./client.md#can-paginate)
- [create_accelerator](./client.md#create-accelerator)
- [create_custom_routing_accelerator](./client.md#create-custom-routing-accelerator)
- [create_custom_routing_endpoint_group](./client.md#create-custom-routing-endpoint-group)
- [create_custom_routing_listener](./client.md#create-custom-routing-listener)
- [create_endpoint_group](./client.md#create-endpoint-group)
- [create_listener](./client.md#create-listener)
- [delete_accelerator](./client.md#delete-accelerator)
- [delete_custom_routing_accelerator](./client.md#delete-custom-routing-accelerator)
- [delete_custom_routing_endpoint_group](./client.md#delete-custom-routing-endpoint-group)
- [delete_custom_routing_listener](./client.md#delete-custom-routing-listener)
- [delete_endpoint_group](./client.md#delete-endpoint-group)
- [delete_listener](./client.md#delete-listener)
- [deny_custom_routing_traffic](./client.md#deny-custom-routing-traffic)
- [deprovision_byoip_cidr](./client.md#deprovision-byoip-cidr)
- [describe_accelerator](./client.md#describe-accelerator)
- [describe_accelerator_attributes](./client.md#describe-accelerator-attributes)
- [describe_custom_routing_accelerator](./client.md#describe-custom-routing-accelerator)
- [describe_custom_routing_accelerator_attributes](./client.md#describe-custom-routing-accelerator-attributes)
- [describe_custom_routing_endpoint_group](./client.md#describe-custom-routing-endpoint-group)
- [describe_custom_routing_listener](./client.md#describe-custom-routing-listener)
- [describe_endpoint_group](./client.md#describe-endpoint-group)
- [describe_listener](./client.md#describe-listener)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_accelerators](./client.md#list-accelerators)
- [list_byoip_cidrs](./client.md#list-byoip-cidrs)
- [list_custom_routing_accelerators](./client.md#list-custom-routing-accelerators)
- [list_custom_routing_endpoint_groups](./client.md#list-custom-routing-endpoint-groups)
- [list_custom_routing_listeners](./client.md#list-custom-routing-listeners)
- [list_custom_routing_port_mappings](./client.md#list-custom-routing-port-mappings)
- [list_custom_routing_port_mappings_by_destination](./client.md#list-custom-routing-port-mappings-by-destination)
- [list_endpoint_groups](./client.md#list-endpoint-groups)
- [list_listeners](./client.md#list-listeners)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [provision_byoip_cidr](./client.md#provision-byoip-cidr)
- [remove_custom_routing_endpoints](./client.md#remove-custom-routing-endpoints)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_accelerator](./client.md#update-accelerator)
- [update_accelerator_attributes](./client.md#update-accelerator-attributes)
- [update_custom_routing_accelerator](./client.md#update-custom-routing-accelerator)
- [update_custom_routing_accelerator_attributes](./client.md#update-custom-routing-accelerator-attributes)
- [update_custom_routing_listener](./client.md#update-custom-routing-listener)
- [update_endpoint_group](./client.md#update-endpoint-group)
- [update_listener](./client.md#update-listener)
- [withdraw_byoip_cidr](./client.md#withdraw-byoip-cidr)




### Exceptions
- [AcceleratorNotDisabledException](./client.md#acceleratornotdisabledexception)
- [AcceleratorNotFoundException](./client.md#acceleratornotfoundexception)
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AssociatedEndpointGroupFoundException](./client.md#associatedendpointgroupfoundexception)
- [AssociatedListenerFoundException](./client.md#associatedlistenerfoundexception)
- [ByoipCidrNotFoundException](./client.md#byoipcidrnotfoundexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [EndpointAlreadyExistsException](./client.md#endpointalreadyexistsexception)
- [EndpointGroupAlreadyExistsException](./client.md#endpointgroupalreadyexistsexception)
- [EndpointGroupNotFoundException](./client.md#endpointgroupnotfoundexception)
- [EndpointNotFoundException](./client.md#endpointnotfoundexception)
- [IncorrectCidrStateException](./client.md#incorrectcidrstateexception)
- [InternalServiceErrorException](./client.md#internalserviceerrorexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [InvalidPortRangeException](./client.md#invalidportrangeexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ListenerNotFoundException](./client.md#listenernotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("globalaccelerator").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.paginators import ListAcceleratorsPaginator, ...
```

- [ListAcceleratorsPaginator](./paginators.md#listacceleratorspaginator)
- [ListByoipCidrsPaginator](./paginators.md#listbyoipcidrspaginator)
- [ListCustomRoutingAcceleratorsPaginator](./paginators.md#listcustomroutingacceleratorspaginator)
- [ListCustomRoutingListenersPaginator](./paginators.md#listcustomroutinglistenerspaginator)
- [ListCustomRoutingPortMappingsPaginator](./paginators.md#listcustomroutingportmappingspaginator)
- [ListCustomRoutingPortMappingsByDestinationPaginator](./paginators.md#listcustomroutingportmappingsbydestinationpaginator)
- [ListEndpointGroupsPaginator](./paginators.md#listendpointgroupspaginator)
- [ListListenersPaginator](./paginators.md#listlistenerspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.literals import AcceleratorStatus, ...
```

- [AcceleratorStatus](./literals.md#acceleratorstatus)
- [ByoipCidrState](./literals.md#byoipcidrstate)
- [ClientAffinity](./literals.md#clientaffinity)
- [CustomRoutingAcceleratorStatus](./literals.md#customroutingacceleratorstatus)
- [CustomRoutingDestinationTrafficState](./literals.md#customroutingdestinationtrafficstate)
- [CustomRoutingProtocol](./literals.md#customroutingprotocol)
- [HealthCheckProtocol](./literals.md#healthcheckprotocol)
- [HealthState](./literals.md#healthstate)
- [IpAddressType](./literals.md#ipaddresstype)
- [ListAcceleratorsPaginatorName](./literals.md#listacceleratorspaginatorname)
- [ListByoipCidrsPaginatorName](./literals.md#listbyoipcidrspaginatorname)
- [ListCustomRoutingAcceleratorsPaginatorName](./literals.md#listcustomroutingacceleratorspaginatorname)
- [ListCustomRoutingListenersPaginatorName](./literals.md#listcustomroutinglistenerspaginatorname)
- [ListCustomRoutingPortMappingsByDestinationPaginatorName](./literals.md#listcustomroutingportmappingsbydestinationpaginatorname)
- [ListCustomRoutingPortMappingsPaginatorName](./literals.md#listcustomroutingportmappingspaginatorname)
- [ListEndpointGroupsPaginatorName](./literals.md#listendpointgroupspaginatorname)
- [ListListenersPaginatorName](./literals.md#listlistenerspaginatorname)
- [ProtocolType](./literals.md#protocoltype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef, ...
```

- [AcceleratorAttributesTypeDef](./type_defs.md#acceleratorattributestypedef)
- [AcceleratorTypeDef](./type_defs.md#acceleratortypedef)
- [AddCustomRoutingEndpointsResponseTypeDef](./type_defs.md#addcustomroutingendpointsresponsetypedef)
- [AdvertiseByoipCidrResponseTypeDef](./type_defs.md#advertisebyoipcidrresponsetypedef)
- [ByoipCidrEventTypeDef](./type_defs.md#byoipcidreventtypedef)
- [ByoipCidrTypeDef](./type_defs.md#byoipcidrtypedef)
- [CidrAuthorizationContextTypeDef](./type_defs.md#cidrauthorizationcontexttypedef)
- [CreateAcceleratorResponseTypeDef](./type_defs.md#createacceleratorresponsetypedef)
- [CreateCustomRoutingAcceleratorResponseTypeDef](./type_defs.md#createcustomroutingacceleratorresponsetypedef)
- [CreateCustomRoutingEndpointGroupResponseTypeDef](./type_defs.md#createcustomroutingendpointgroupresponsetypedef)
- [CreateCustomRoutingListenerResponseTypeDef](./type_defs.md#createcustomroutinglistenerresponsetypedef)
- [CreateEndpointGroupResponseTypeDef](./type_defs.md#createendpointgroupresponsetypedef)
- [CreateListenerResponseTypeDef](./type_defs.md#createlistenerresponsetypedef)
- [CustomRoutingAcceleratorAttributesTypeDef](./type_defs.md#customroutingacceleratorattributestypedef)
- [CustomRoutingAcceleratorTypeDef](./type_defs.md#customroutingacceleratortypedef)
- [CustomRoutingDestinationConfigurationTypeDef](./type_defs.md#customroutingdestinationconfigurationtypedef)
- [CustomRoutingDestinationDescriptionTypeDef](./type_defs.md#customroutingdestinationdescriptiontypedef)
- [CustomRoutingEndpointConfigurationTypeDef](./type_defs.md#customroutingendpointconfigurationtypedef)
- [CustomRoutingEndpointDescriptionTypeDef](./type_defs.md#customroutingendpointdescriptiontypedef)
- [CustomRoutingEndpointGroupTypeDef](./type_defs.md#customroutingendpointgrouptypedef)
- [CustomRoutingListenerTypeDef](./type_defs.md#customroutinglistenertypedef)
- [DeprovisionByoipCidrResponseTypeDef](./type_defs.md#deprovisionbyoipcidrresponsetypedef)
- [DescribeAcceleratorAttributesResponseTypeDef](./type_defs.md#describeacceleratorattributesresponsetypedef)
- [DescribeAcceleratorResponseTypeDef](./type_defs.md#describeacceleratorresponsetypedef)
- [DescribeCustomRoutingAcceleratorAttributesResponseTypeDef](./type_defs.md#describecustomroutingacceleratorattributesresponsetypedef)
- [DescribeCustomRoutingAcceleratorResponseTypeDef](./type_defs.md#describecustomroutingacceleratorresponsetypedef)
- [DescribeCustomRoutingEndpointGroupResponseTypeDef](./type_defs.md#describecustomroutingendpointgroupresponsetypedef)
- [DescribeCustomRoutingListenerResponseTypeDef](./type_defs.md#describecustomroutinglistenerresponsetypedef)
- [DescribeEndpointGroupResponseTypeDef](./type_defs.md#describeendpointgroupresponsetypedef)
- [DescribeListenerResponseTypeDef](./type_defs.md#describelistenerresponsetypedef)
- [DestinationPortMappingTypeDef](./type_defs.md#destinationportmappingtypedef)
- [EndpointConfigurationTypeDef](./type_defs.md#endpointconfigurationtypedef)
- [EndpointDescriptionTypeDef](./type_defs.md#endpointdescriptiontypedef)
- [EndpointGroupTypeDef](./type_defs.md#endpointgrouptypedef)
- [IpSetTypeDef](./type_defs.md#ipsettypedef)
- [ListAcceleratorsResponseTypeDef](./type_defs.md#listacceleratorsresponsetypedef)
- [ListByoipCidrsResponseTypeDef](./type_defs.md#listbyoipcidrsresponsetypedef)
- [ListCustomRoutingAcceleratorsResponseTypeDef](./type_defs.md#listcustomroutingacceleratorsresponsetypedef)
- [ListCustomRoutingEndpointGroupsResponseTypeDef](./type_defs.md#listcustomroutingendpointgroupsresponsetypedef)
- [ListCustomRoutingListenersResponseTypeDef](./type_defs.md#listcustomroutinglistenersresponsetypedef)
- [ListCustomRoutingPortMappingsByDestinationResponseTypeDef](./type_defs.md#listcustomroutingportmappingsbydestinationresponsetypedef)
- [ListCustomRoutingPortMappingsResponseTypeDef](./type_defs.md#listcustomroutingportmappingsresponsetypedef)
- [ListEndpointGroupsResponseTypeDef](./type_defs.md#listendpointgroupsresponsetypedef)
- [ListListenersResponseTypeDef](./type_defs.md#listlistenersresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListenerTypeDef](./type_defs.md#listenertypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PortMappingTypeDef](./type_defs.md#portmappingtypedef)
- [PortOverrideTypeDef](./type_defs.md#portoverridetypedef)
- [PortRangeTypeDef](./type_defs.md#portrangetypedef)
- [ProvisionByoipCidrResponseTypeDef](./type_defs.md#provisionbyoipcidrresponsetypedef)
- [SocketAddressTypeDef](./type_defs.md#socketaddresstypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateAcceleratorAttributesResponseTypeDef](./type_defs.md#updateacceleratorattributesresponsetypedef)
- [UpdateAcceleratorResponseTypeDef](./type_defs.md#updateacceleratorresponsetypedef)
- [UpdateCustomRoutingAcceleratorAttributesResponseTypeDef](./type_defs.md#updatecustomroutingacceleratorattributesresponsetypedef)
- [UpdateCustomRoutingAcceleratorResponseTypeDef](./type_defs.md#updatecustomroutingacceleratorresponsetypedef)
- [UpdateCustomRoutingListenerResponseTypeDef](./type_defs.md#updatecustomroutinglistenerresponsetypedef)
- [UpdateEndpointGroupResponseTypeDef](./type_defs.md#updateendpointgroupresponsetypedef)
- [UpdateListenerResponseTypeDef](./type_defs.md#updatelistenerresponsetypedef)
- [WithdrawByoipCidrResponseTypeDef](./type_defs.md#withdrawbyoipcidrresponsetypedef)
