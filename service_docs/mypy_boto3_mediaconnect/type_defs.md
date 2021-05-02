# Structures for boto3 MediaConnect module

> [Index](../index.md) > [MediaConnect](./index.md) > Structures

Auto-generated documentation for [MediaConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect)
type annotations stubs module [mypy_boto3_mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/).

- [Structures for boto3 MediaConnect module](#structures-for-boto3-mediaconnect-module)
  - [AddFlowOutputsResponseTypeDef](#addflowoutputsresponsetypedef)
  - [AddFlowSourcesResponseTypeDef](#addflowsourcesresponsetypedef)
  - [AddFlowVpcInterfacesResponseTypeDef](#addflowvpcinterfacesresponsetypedef)
  - [AddOutputRequestTypeDef](#addoutputrequesttypedef)
  - [CreateFlowResponseTypeDef](#createflowresponsetypedef)
  - [DeleteFlowResponseTypeDef](#deleteflowresponsetypedef)
  - [DescribeFlowResponseTypeDef](#describeflowresponsetypedef)
  - [DescribeOfferingResponseTypeDef](#describeofferingresponsetypedef)
  - [DescribeReservationResponseTypeDef](#describereservationresponsetypedef)
  - [EncryptionTypeDef](#encryptiontypedef)
  - [EntitlementTypeDef](#entitlementtypedef)
  - [FailoverConfigTypeDef](#failoverconfigtypedef)
  - [FlowTypeDef](#flowtypedef)
  - [GrantEntitlementRequestTypeDef](#grantentitlementrequesttypedef)
  - [GrantFlowEntitlementsResponseTypeDef](#grantflowentitlementsresponsetypedef)
  - [ListEntitlementsResponseTypeDef](#listentitlementsresponsetypedef)
  - [ListFlowsResponseTypeDef](#listflowsresponsetypedef)
  - [ListOfferingsResponseTypeDef](#listofferingsresponsetypedef)
  - [ListReservationsResponseTypeDef](#listreservationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListedEntitlementTypeDef](#listedentitlementtypedef)
  - [ListedFlowTypeDef](#listedflowtypedef)
  - [MessagesTypeDef](#messagestypedef)
  - [OfferingTypeDef](#offeringtypedef)
  - [OutputTypeDef](#outputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PurchaseOfferingResponseTypeDef](#purchaseofferingresponsetypedef)
  - [RemoveFlowOutputResponseTypeDef](#removeflowoutputresponsetypedef)
  - [RemoveFlowSourceResponseTypeDef](#removeflowsourceresponsetypedef)
  - [RemoveFlowVpcInterfaceResponseTypeDef](#removeflowvpcinterfaceresponsetypedef)
  - [ReservationTypeDef](#reservationtypedef)
  - [ResourceSpecificationTypeDef](#resourcespecificationtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RevokeFlowEntitlementResponseTypeDef](#revokeflowentitlementresponsetypedef)
  - [SetSourceRequestTypeDef](#setsourcerequesttypedef)
  - [SourceTypeDef](#sourcetypedef)
  - [StartFlowResponseTypeDef](#startflowresponsetypedef)
  - [StopFlowResponseTypeDef](#stopflowresponsetypedef)
  - [TransportTypeDef](#transporttypedef)
  - [UpdateEncryptionTypeDef](#updateencryptiontypedef)
  - [UpdateFailoverConfigTypeDef](#updatefailoverconfigtypedef)
  - [UpdateFlowEntitlementResponseTypeDef](#updateflowentitlementresponsetypedef)
  - [UpdateFlowOutputResponseTypeDef](#updateflowoutputresponsetypedef)
  - [UpdateFlowResponseTypeDef](#updateflowresponsetypedef)
  - [UpdateFlowSourceResponseTypeDef](#updateflowsourceresponsetypedef)
  - [VpcInterfaceAttachmentTypeDef](#vpcinterfaceattachmenttypedef)
  - [VpcInterfaceRequestTypeDef](#vpcinterfacerequesttypedef)
  - [VpcInterfaceTypeDef](#vpcinterfacetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AddFlowOutputsResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import AddFlowOutputsResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Outputs`: `List["OutputTypeDef"]`


## AddFlowSourcesResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import AddFlowSourcesResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Sources`: `List["SourceTypeDef"]`


## AddFlowVpcInterfacesResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import AddFlowVpcInterfacesResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `VpcInterfaces`: `List["VpcInterfaceTypeDef"]`


## AddOutputRequestTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import AddOutputRequestTypeDef
```


Required fields:
- `Protocol`: `ProtocolType`



Optional fields:
- `CidrAllowList`: `List[str]`
- `Description`: `str`
- `Destination`: `str`
- `Encryption`: `"EncryptionTypeDef"`
- `MaxLatency`: `int`
- `MinLatency`: `int`
- `Name`: `str`
- `Port`: `int`
- `RemoteId`: `str`
- `SmoothingLatency`: `int`
- `StreamId`: `str`
- `VpcInterfaceAttachment`: `"VpcInterfaceAttachmentTypeDef"`


## CreateFlowResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import CreateFlowResponseTypeDef
```




Optional fields:
- `Flow`: `"FlowTypeDef"`


## DeleteFlowResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import DeleteFlowResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Status`: `Status`


## DescribeFlowResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import DescribeFlowResponseTypeDef
```




Optional fields:
- `Flow`: `"FlowTypeDef"`
- `Messages`: `"MessagesTypeDef"`


## DescribeOfferingResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import DescribeOfferingResponseTypeDef
```




Optional fields:
- `Offering`: `"OfferingTypeDef"`


## DescribeReservationResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import DescribeReservationResponseTypeDef
```




Optional fields:
- `Reservation`: `"ReservationTypeDef"`


## EncryptionTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import EncryptionTypeDef
```


Required fields:
- `RoleArn`: `str`



Optional fields:
- `Algorithm`: `Algorithm`
- `ConstantInitializationVector`: `str`
- `DeviceId`: `str`
- `KeyType`: `KeyType`
- `Region`: `str`
- `ResourceId`: `str`
- `SecretArn`: `str`
- `Url`: `str`


## EntitlementTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import EntitlementTypeDef
```


Required fields:
- `EntitlementArn`: `str`
- `Name`: `str`
- `Subscribers`: `List[str]`



Optional fields:
- `DataTransferSubscriberFeePercent`: `int`
- `Description`: `str`
- `Encryption`: `"EncryptionTypeDef"`
- `EntitlementStatus`: `EntitlementStatus`


## FailoverConfigTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import FailoverConfigTypeDef
```




Optional fields:
- `RecoveryWindow`: `int`
- `State`: `State`


## FlowTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import FlowTypeDef
```


Required fields:
- `AvailabilityZone`: `str`
- `Entitlements`: `List["EntitlementTypeDef"]`
- `FlowArn`: `str`
- `Name`: `str`
- `Outputs`: `List["OutputTypeDef"]`
- `Source`: `"SourceTypeDef"`
- `Status`: `Status`



Optional fields:
- `Description`: `str`
- `EgressIp`: `str`
- `SourceFailoverConfig`: `"FailoverConfigTypeDef"`
- `Sources`: `List["SourceTypeDef"]`
- `VpcInterfaces`: `List["VpcInterfaceTypeDef"]`


## GrantEntitlementRequestTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import GrantEntitlementRequestTypeDef
```


Required fields:
- `Subscribers`: `List[str]`



Optional fields:
- `DataTransferSubscriberFeePercent`: `int`
- `Description`: `str`
- `Encryption`: `"EncryptionTypeDef"`
- `EntitlementStatus`: `EntitlementStatus`
- `Name`: `str`


## GrantFlowEntitlementsResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import GrantFlowEntitlementsResponseTypeDef
```




Optional fields:
- `Entitlements`: `List["EntitlementTypeDef"]`
- `FlowArn`: `str`


## ListEntitlementsResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListEntitlementsResponseTypeDef
```




Optional fields:
- `Entitlements`: `List["ListedEntitlementTypeDef"]`
- `NextToken`: `str`


## ListFlowsResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListFlowsResponseTypeDef
```




Optional fields:
- `Flows`: `List["ListedFlowTypeDef"]`
- `NextToken`: `str`


## ListOfferingsResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListOfferingsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Offerings`: `List["OfferingTypeDef"]`


## ListReservationsResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListReservationsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `Reservations`: `List["ReservationTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListedEntitlementTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListedEntitlementTypeDef
```


Required fields:
- `EntitlementArn`: `str`
- `EntitlementName`: `str`



Optional fields:
- `DataTransferSubscriberFeePercent`: `int`


## ListedFlowTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ListedFlowTypeDef
```


Required fields:
- `AvailabilityZone`: `str`
- `Description`: `str`
- `FlowArn`: `str`
- `Name`: `str`
- `SourceType`: `SourceType`
- `Status`: `Status`




## MessagesTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import MessagesTypeDef
```


Required fields:
- `Errors`: `List[str]`




## OfferingTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import OfferingTypeDef
```


Required fields:
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `Literal['MONTHS']`
- `OfferingArn`: `str`
- `OfferingDescription`: `str`
- `PricePerUnit`: `str`
- `PriceUnits`: `Literal['HOURLY']`
- `ResourceSpecification`: `"ResourceSpecificationTypeDef"`




## OutputTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import OutputTypeDef
```


Required fields:
- `Name`: `str`
- `OutputArn`: `str`



Optional fields:
- `DataTransferSubscriberFeePercent`: `int`
- `Description`: `str`
- `Destination`: `str`
- `Encryption`: `"EncryptionTypeDef"`
- `EntitlementArn`: `str`
- `ListenerAddress`: `str`
- `MediaLiveInputArn`: `str`
- `Port`: `int`
- `Transport`: `"TransportTypeDef"`
- `VpcInterfaceAttachment`: `"VpcInterfaceAttachmentTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PurchaseOfferingResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import PurchaseOfferingResponseTypeDef
```




Optional fields:
- `Reservation`: `"ReservationTypeDef"`


## RemoveFlowOutputResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import RemoveFlowOutputResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `OutputArn`: `str`


## RemoveFlowSourceResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import RemoveFlowSourceResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `SourceArn`: `str`


## RemoveFlowVpcInterfaceResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import RemoveFlowVpcInterfaceResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `NonDeletedNetworkInterfaceIds`: `List[str]`
- `VpcInterfaceName`: `str`


## ReservationTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ReservationTypeDef
```


Required fields:
- `CurrencyCode`: `str`
- `Duration`: `int`
- `DurationUnits`: `Literal['MONTHS']`
- `End`: `str`
- `OfferingArn`: `str`
- `OfferingDescription`: `str`
- `PricePerUnit`: `str`
- `PriceUnits`: `Literal['HOURLY']`
- `ReservationArn`: `str`
- `ReservationName`: `str`
- `ReservationState`: `ReservationState`
- `ResourceSpecification`: `"ResourceSpecificationTypeDef"`
- `Start`: `str`




## ResourceSpecificationTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import ResourceSpecificationTypeDef
```


Required fields:
- `ResourceType`: `Literal['Mbps_Outbound_Bandwidth']`



Optional fields:
- `ReservedBitrate`: `int`


## ResponseMetadata

```python
from mypy_boto3_mediaconnect.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RevokeFlowEntitlementResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import RevokeFlowEntitlementResponseTypeDef
```




Optional fields:
- `EntitlementArn`: `str`
- `FlowArn`: `str`


## SetSourceRequestTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import SetSourceRequestTypeDef
```




Optional fields:
- `Decryption`: `"EncryptionTypeDef"`
- `Description`: `str`
- `EntitlementArn`: `str`
- `IngestPort`: `int`
- `MaxBitrate`: `int`
- `MaxLatency`: `int`
- `MinLatency`: `int`
- `Name`: `str`
- `Protocol`: `ProtocolType`
- `StreamId`: `str`
- `VpcInterfaceName`: `str`
- `WhitelistCidr`: `str`


## SourceTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import SourceTypeDef
```


Required fields:
- `Name`: `str`
- `SourceArn`: `str`



Optional fields:
- `DataTransferSubscriberFeePercent`: `int`
- `Decryption`: `"EncryptionTypeDef"`
- `Description`: `str`
- `EntitlementArn`: `str`
- `IngestIp`: `str`
- `IngestPort`: `int`
- `Transport`: `"TransportTypeDef"`
- `VpcInterfaceName`: `str`
- `WhitelistCidr`: `str`


## StartFlowResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import StartFlowResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Status`: `Status`


## StopFlowResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import StopFlowResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Status`: `Status`


## TransportTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import TransportTypeDef
```


Required fields:
- `Protocol`: `ProtocolType`



Optional fields:
- `CidrAllowList`: `List[str]`
- `MaxBitrate`: `int`
- `MaxLatency`: `int`
- `MinLatency`: `int`
- `RemoteId`: `str`
- `SmoothingLatency`: `int`
- `StreamId`: `str`


## UpdateEncryptionTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import UpdateEncryptionTypeDef
```




Optional fields:
- `Algorithm`: `Algorithm`
- `ConstantInitializationVector`: `str`
- `DeviceId`: `str`
- `KeyType`: `KeyType`
- `Region`: `str`
- `ResourceId`: `str`
- `RoleArn`: `str`
- `SecretArn`: `str`
- `Url`: `str`


## UpdateFailoverConfigTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import UpdateFailoverConfigTypeDef
```




Optional fields:
- `RecoveryWindow`: `int`
- `State`: `State`


## UpdateFlowEntitlementResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import UpdateFlowEntitlementResponseTypeDef
```




Optional fields:
- `Entitlement`: `"EntitlementTypeDef"`
- `FlowArn`: `str`


## UpdateFlowOutputResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import UpdateFlowOutputResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Output`: `"OutputTypeDef"`


## UpdateFlowResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import UpdateFlowResponseTypeDef
```




Optional fields:
- `Flow`: `"FlowTypeDef"`


## UpdateFlowSourceResponseTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import UpdateFlowSourceResponseTypeDef
```




Optional fields:
- `FlowArn`: `str`
- `Source`: `"SourceTypeDef"`


## VpcInterfaceAttachmentTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import VpcInterfaceAttachmentTypeDef
```




Optional fields:
- `VpcInterfaceName`: `str`


## VpcInterfaceRequestTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import VpcInterfaceRequestTypeDef
```


Required fields:
- `Name`: `str`
- `RoleArn`: `str`
- `SecurityGroupIds`: `List[str]`
- `SubnetId`: `str`




## VpcInterfaceTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import VpcInterfaceTypeDef
```


Required fields:
- `Name`: `str`
- `NetworkInterfaceIds`: `List[str]`
- `RoleArn`: `str`
- `SecurityGroupIds`: `List[str]`
- `SubnetId`: `str`




## WaiterConfigTypeDef

```python
from mypy_boto3_mediaconnect.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

