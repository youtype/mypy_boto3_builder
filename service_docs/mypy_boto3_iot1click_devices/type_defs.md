# Structures for boto3 IoT1ClickDevicesService module

> [Index](../index.md) > [IoT1ClickDevicesService](./index.md) > Structures

Auto-generated documentation for [IoT1ClickDevicesService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService)
type annotations stubs module [mypy_boto3_iot1click_devices](https://pypi.org/project/mypy-boto3-iot1click-devices/).

- [Structures for boto3 IoT1ClickDevicesService module](#structures-for-boto3-iot1clickdevicesservice-module)
  - [ClaimDevicesByClaimCodeResponseTypeDef](#claimdevicesbyclaimcoderesponsetypedef)
  - [DescribeDeviceResponseTypeDef](#describedeviceresponsetypedef)
  - [DeviceDescriptionTypeDef](#devicedescriptiontypedef)
  - [DeviceEventTypeDef](#deviceeventtypedef)
  - [DeviceMethodTypeDef](#devicemethodtypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [FinalizeDeviceClaimResponseTypeDef](#finalizedeviceclaimresponsetypedef)
  - [GetDeviceMethodsResponseTypeDef](#getdevicemethodsresponsetypedef)
  - [InitiateDeviceClaimResponseTypeDef](#initiatedeviceclaimresponsetypedef)
  - [InvokeDeviceMethodResponseTypeDef](#invokedevicemethodresponsetypedef)
  - [ListDeviceEventsResponseTypeDef](#listdeviceeventsresponsetypedef)
  - [ListDevicesResponseTypeDef](#listdevicesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UnclaimDeviceResponseTypeDef](#unclaimdeviceresponsetypedef)

## ClaimDevicesByClaimCodeResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import ClaimDevicesByClaimCodeResponseTypeDef
```




Optional fields:
- `ClaimCode`: `str`
- `Total`: `int`


## DescribeDeviceResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import DescribeDeviceResponseTypeDef
```




Optional fields:
- `DeviceDescription`: `"DeviceDescriptionTypeDef"`


## DeviceDescriptionTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import DeviceDescriptionTypeDef
```




Optional fields:
- `Arn`: `str`
- `Attributes`: `Dict[str, str]`
- `DeviceId`: `str`
- `Enabled`: `bool`
- `RemainingLife`: `float`
- `Type`: `str`
- `Tags`: `Dict[str, str]`


## DeviceEventTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import DeviceEventTypeDef
```




Optional fields:
- `Device`: `"DeviceTypeDef"`
- `StdEvent`: `str`


## DeviceMethodTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import DeviceMethodTypeDef
```




Optional fields:
- `DeviceType`: `str`
- `MethodName`: `str`


## DeviceTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import DeviceTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, Any]`
- `DeviceId`: `str`
- `Type`: `str`


## FinalizeDeviceClaimResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import FinalizeDeviceClaimResponseTypeDef
```




Optional fields:
- `State`: `str`


## GetDeviceMethodsResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import GetDeviceMethodsResponseTypeDef
```




Optional fields:
- `DeviceMethods`: `List["DeviceMethodTypeDef"]`


## InitiateDeviceClaimResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import InitiateDeviceClaimResponseTypeDef
```




Optional fields:
- `State`: `str`


## InvokeDeviceMethodResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import InvokeDeviceMethodResponseTypeDef
```




Optional fields:
- `DeviceMethodResponse`: `str`


## ListDeviceEventsResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import ListDeviceEventsResponseTypeDef
```




Optional fields:
- `Events`: `List["DeviceEventTypeDef"]`
- `NextToken`: `str`


## ListDevicesResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import ListDevicesResponseTypeDef
```




Optional fields:
- `Devices`: `List["DeviceDescriptionTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UnclaimDeviceResponseTypeDef

```python
from mypy_boto3_iot1click_devices.type_defs import UnclaimDeviceResponseTypeDef
```




Optional fields:
- `State`: `str`

