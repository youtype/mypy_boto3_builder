# Type annotations for boto3 MediaConnect module

> [Index](../index.md) > MediaConnect

Auto-generated documentation for [MediaConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect)
type annotations stubs module [mypy_boto3_mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/).

```bash
pip install mypy-boto3-mediaconnect
```

- [Type annotations for boto3 MediaConnect module](#type-annotations-for-boto3-mediaconnect-module)
  - [MediaConnectClient](#mediaconnectclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## MediaConnectClient

Type annotations for  `boto3.client("mediaconnect")` as [MediaConnectClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mediaconnect.client import MediaConnectClient
```


MediaConnectClient [exceptions](./client.md#exceptions)



### Methods
- [add_flow_outputs](./client.md#add-flow-outputs)
- [add_flow_sources](./client.md#add-flow-sources)
- [add_flow_vpc_interfaces](./client.md#add-flow-vpc-interfaces)
- [can_paginate](./client.md#can-paginate)
- [create_flow](./client.md#create-flow)
- [delete_flow](./client.md#delete-flow)
- [describe_flow](./client.md#describe-flow)
- [describe_offering](./client.md#describe-offering)
- [describe_reservation](./client.md#describe-reservation)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [grant_flow_entitlements](./client.md#grant-flow-entitlements)
- [list_entitlements](./client.md#list-entitlements)
- [list_flows](./client.md#list-flows)
- [list_offerings](./client.md#list-offerings)
- [list_reservations](./client.md#list-reservations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [purchase_offering](./client.md#purchase-offering)
- [remove_flow_output](./client.md#remove-flow-output)
- [remove_flow_source](./client.md#remove-flow-source)
- [remove_flow_vpc_interface](./client.md#remove-flow-vpc-interface)
- [revoke_flow_entitlement](./client.md#revoke-flow-entitlement)
- [start_flow](./client.md#start-flow)
- [stop_flow](./client.md#stop-flow)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_flow](./client.md#update-flow)
- [update_flow_entitlement](./client.md#update-flow-entitlement)
- [update_flow_output](./client.md#update-flow-output)
- [update_flow_source](./client.md#update-flow-source)




### Exceptions
- [AddFlowOutputs420Exception](./client.md#addflowoutputs420exception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [CreateFlow420Exception](./client.md#createflow420exception)
- [ForbiddenException](./client.md#forbiddenexception)
- [GrantFlowEntitlements420Exception](./client.md#grantflowentitlements420exception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mediaconnect").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mediaconnect.paginators import ListEntitlementsPaginator, ...
```

- [ListEntitlementsPaginator](./paginators.md#listentitlementspaginator)
- [ListFlowsPaginator](./paginators.md#listflowspaginator)
- [ListOfferingsPaginator](./paginators.md#listofferingspaginator)
- [ListReservationsPaginator](./paginators.md#listreservationspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("mediaconnect").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_mediaconnect.waiters import FlowActiveWaiter, ...
```

- [FlowActiveWaiter](./waiters.md#flowactivewaiter)
- [FlowDeletedWaiter](./waiters.md#flowdeletedwaiter)
- [FlowStandbyWaiter](./waiters.md#flowstandbywaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediaconnect.literals import Algorithm, ...
```

- [Algorithm](./literals.md#algorithm)
- [DurationUnits](./literals.md#durationunits)
- [EntitlementStatus](./literals.md#entitlementstatus)
- [FlowActiveWaiterName](./literals.md#flowactivewaitername)
- [FlowDeletedWaiterName](./literals.md#flowdeletedwaitername)
- [FlowStandbyWaiterName](./literals.md#flowstandbywaitername)
- [KeyType](./literals.md#keytype)
- [ListEntitlementsPaginatorName](./literals.md#listentitlementspaginatorname)
- [ListFlowsPaginatorName](./literals.md#listflowspaginatorname)
- [ListOfferingsPaginatorName](./literals.md#listofferingspaginatorname)
- [ListReservationsPaginatorName](./literals.md#listreservationspaginatorname)
- [PriceUnits](./literals.md#priceunits)
- [ProtocolType](./literals.md#protocoltype)
- [ReservationState](./literals.md#reservationstate)
- [ResourceType](./literals.md#resourcetype)
- [SourceType](./literals.md#sourcetype)
- [State](./literals.md#state)
- [Status](./literals.md#status)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediaconnect.type_defs import EncryptionTypeDef, ...
```

- [EncryptionTypeDef](./type_defs.md#encryptiontypedef)
- [EntitlementTypeDef](./type_defs.md#entitlementtypedef)
- [FailoverConfigTypeDef](./type_defs.md#failoverconfigtypedef)
- [FlowTypeDef](./type_defs.md#flowtypedef)
- [ListedEntitlementTypeDef](./type_defs.md#listedentitlementtypedef)
- [ListedFlowTypeDef](./type_defs.md#listedflowtypedef)
- [MessagesTypeDef](./type_defs.md#messagestypedef)
- [OfferingTypeDef](./type_defs.md#offeringtypedef)
- [OutputTypeDef](./type_defs.md#outputtypedef)
- [ReservationTypeDef](./type_defs.md#reservationtypedef)
- [ResourceSpecificationTypeDef](./type_defs.md#resourcespecificationtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SourceTypeDef](./type_defs.md#sourcetypedef)
- [TransportTypeDef](./type_defs.md#transporttypedef)
- [VpcInterfaceAttachmentTypeDef](./type_defs.md#vpcinterfaceattachmenttypedef)
- [VpcInterfaceTypeDef](./type_defs.md#vpcinterfacetypedef)
- [AddFlowOutputsResponseTypeDef](./type_defs.md#addflowoutputsresponsetypedef)
- [AddFlowSourcesResponseTypeDef](./type_defs.md#addflowsourcesresponsetypedef)
- [AddFlowVpcInterfacesResponseTypeDef](./type_defs.md#addflowvpcinterfacesresponsetypedef)
- [AddOutputRequestTypeDef](./type_defs.md#addoutputrequesttypedef)
- [CreateFlowResponseTypeDef](./type_defs.md#createflowresponsetypedef)
- [DeleteFlowResponseTypeDef](./type_defs.md#deleteflowresponsetypedef)
- [DescribeFlowResponseTypeDef](./type_defs.md#describeflowresponsetypedef)
- [DescribeOfferingResponseTypeDef](./type_defs.md#describeofferingresponsetypedef)
- [DescribeReservationResponseTypeDef](./type_defs.md#describereservationresponsetypedef)
- [GrantEntitlementRequestTypeDef](./type_defs.md#grantentitlementrequesttypedef)
- [GrantFlowEntitlementsResponseTypeDef](./type_defs.md#grantflowentitlementsresponsetypedef)
- [ListEntitlementsResponseTypeDef](./type_defs.md#listentitlementsresponsetypedef)
- [ListFlowsResponseTypeDef](./type_defs.md#listflowsresponsetypedef)
- [ListOfferingsResponseTypeDef](./type_defs.md#listofferingsresponsetypedef)
- [ListReservationsResponseTypeDef](./type_defs.md#listreservationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PurchaseOfferingResponseTypeDef](./type_defs.md#purchaseofferingresponsetypedef)
- [RemoveFlowOutputResponseTypeDef](./type_defs.md#removeflowoutputresponsetypedef)
- [RemoveFlowSourceResponseTypeDef](./type_defs.md#removeflowsourceresponsetypedef)
- [RemoveFlowVpcInterfaceResponseTypeDef](./type_defs.md#removeflowvpcinterfaceresponsetypedef)
- [RevokeFlowEntitlementResponseTypeDef](./type_defs.md#revokeflowentitlementresponsetypedef)
- [SetSourceRequestTypeDef](./type_defs.md#setsourcerequesttypedef)
- [StartFlowResponseTypeDef](./type_defs.md#startflowresponsetypedef)
- [StopFlowResponseTypeDef](./type_defs.md#stopflowresponsetypedef)
- [UpdateEncryptionTypeDef](./type_defs.md#updateencryptiontypedef)
- [UpdateFailoverConfigTypeDef](./type_defs.md#updatefailoverconfigtypedef)
- [UpdateFlowEntitlementResponseTypeDef](./type_defs.md#updateflowentitlementresponsetypedef)
- [UpdateFlowOutputResponseTypeDef](./type_defs.md#updateflowoutputresponsetypedef)
- [UpdateFlowResponseTypeDef](./type_defs.md#updateflowresponsetypedef)
- [UpdateFlowSourceResponseTypeDef](./type_defs.md#updateflowsourceresponsetypedef)
- [VpcInterfaceRequestTypeDef](./type_defs.md#vpcinterfacerequesttypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
