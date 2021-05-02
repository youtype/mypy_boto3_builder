# Paginators for boto3 IoT1ClickDevicesService module

> [Index](../index.md) > [IoT1ClickDevicesService](./index.md) > Paginators

Auto-generated documentation for [IoT1ClickDevicesService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService)
type annotations stubs module [mypy_boto3_iot1click_devices](https://pypi.org/project/mypy-boto3-iot1click-devices/).

- [Paginators for boto3 IoT1ClickDevicesService module](#paginators-for-boto3-iot1clickdevicesservice-module)
  - [ListDeviceEventsPaginator](#listdeviceeventspaginator)
  - [ListDevicesPaginator](#listdevicespaginator)

## ListDeviceEventsPaginator

Type annotations for `boto3.client("iot1click-devices").get_paginator("list_device_events")`.

Can be used directly:

```python
from mypy_boto3_iot1click_devices.paginators import ListDeviceEventsPaginator

def get_list_device_events_paginator() -> ListDeviceEventsPaginator:
    return boto3.client("iot1click-devices").get_paginator("list_device_events")
```

[Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDeviceEvents)

```python
class ListDeviceEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        DeviceId: str,
        FromTimeStamp: datetime,
        ToTimeStamp: datetime,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceEventsResponseTypeDef]:
        pass
```
## ListDevicesPaginator

Type annotations for `boto3.client("iot1click-devices").get_paginator("list_devices")`.

Can be used directly:

```python
from mypy_boto3_iot1click_devices.paginators import ListDevicesPaginator

def get_list_devices_paginator() -> ListDevicesPaginator:
    return boto3.client("iot1click-devices").get_paginator("list_devices")
```

[Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Paginator.ListDevices)

```python
class ListDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        DeviceType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicesResponseTypeDef]:
        pass
```