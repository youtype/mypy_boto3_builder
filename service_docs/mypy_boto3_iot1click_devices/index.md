# Type annotations for boto3 IoT1ClickDevicesService module

> [Index](../index.md) > IoT1ClickDevicesService

Auto-generated documentation for [IoT1ClickDevicesService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService)
type annotations stubs module [mypy_boto3_iot1click_devices](https://pypi.org/project/mypy-boto3-iot1click-devices/).

```bash
pip install mypy-boto3-iot1click-devices
```

- [Type annotations for boto3 IoT1ClickDevicesService module](#type-annotations-for-boto3-iot1clickdevicesservice-module)
  - [IoT1ClickDevicesServiceClient](#iot1clickdevicesserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## IoT1ClickDevicesServiceClient

Type annotations for  `boto3.client("iot1click-devices")` as [IoT1ClickDevicesServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iot1click_devices.client import IoT1ClickDevicesServiceClient
```


IoT1ClickDevicesServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [claim_devices_by_claim_code](./client.md#claim-devices-by-claim-code)
- [describe_device](./client.md#describe-device)
- [finalize_device_claim](./client.md#finalize-device-claim)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_device_methods](./client.md#get-device-methods)
- [get_paginator](./client.md#get-paginator)
- [initiate_device_claim](./client.md#initiate-device-claim)
- [invoke_device_method](./client.md#invoke-device-method)
- [list_device_events](./client.md#list-device-events)
- [list_devices](./client.md#list-devices)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [unclaim_device](./client.md#unclaim-device)
- [untag_resource](./client.md#untag-resource)
- [update_device_state](./client.md#update-device-state)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [PreconditionFailedException](./client.md#preconditionfailedexception)
- [RangeNotSatisfiableException](./client.md#rangenotsatisfiableexception)
- [ResourceConflictException](./client.md#resourceconflictexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iot1click-devices").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iot1click_devices.paginators import ListDeviceEventsPaginator, ...
```

- [ListDeviceEventsPaginator](./paginators.md#listdeviceeventspaginator)
- [ListDevicesPaginator](./paginators.md#listdevicespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot1click_devices.literals import ListDeviceEventsPaginatorName, ...
```

- [ListDeviceEventsPaginatorName](./literals.md#listdeviceeventspaginatorname)
- [ListDevicesPaginatorName](./literals.md#listdevicespaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot1click_devices.type_defs import DeviceDescriptionTypeDef, ...
```

- [DeviceDescriptionTypeDef](./type_defs.md#devicedescriptiontypedef)
- [DeviceEventTypeDef](./type_defs.md#deviceeventtypedef)
- [DeviceMethodTypeDef](./type_defs.md#devicemethodtypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [ClaimDevicesByClaimCodeResponseTypeDef](./type_defs.md#claimdevicesbyclaimcoderesponsetypedef)
- [DescribeDeviceResponseTypeDef](./type_defs.md#describedeviceresponsetypedef)
- [FinalizeDeviceClaimResponseTypeDef](./type_defs.md#finalizedeviceclaimresponsetypedef)
- [GetDeviceMethodsResponseTypeDef](./type_defs.md#getdevicemethodsresponsetypedef)
- [InitiateDeviceClaimResponseTypeDef](./type_defs.md#initiatedeviceclaimresponsetypedef)
- [InvokeDeviceMethodResponseTypeDef](./type_defs.md#invokedevicemethodresponsetypedef)
- [ListDeviceEventsResponseTypeDef](./type_defs.md#listdeviceeventsresponsetypedef)
- [ListDevicesResponseTypeDef](./type_defs.md#listdevicesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UnclaimDeviceResponseTypeDef](./type_defs.md#unclaimdeviceresponsetypedef)
