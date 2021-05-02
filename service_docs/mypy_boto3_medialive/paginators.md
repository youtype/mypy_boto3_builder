# Paginators for boto3 MediaLive module

> [Index](../index.md) > [MediaLive](./index.md) > Paginators

Auto-generated documentation for [MediaLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive)
type annotations stubs module [mypy_boto3_medialive](https://pypi.org/project/mypy-boto3-medialive/).

- [Paginators for boto3 MediaLive module](#paginators-for-boto3-medialive-module)
  - [DescribeSchedulePaginator](#describeschedulepaginator)
  - [ListChannelsPaginator](#listchannelspaginator)
  - [ListInputDeviceTransfersPaginator](#listinputdevicetransferspaginator)
  - [ListInputDevicesPaginator](#listinputdevicespaginator)
  - [ListInputSecurityGroupsPaginator](#listinputsecuritygroupspaginator)
  - [ListInputsPaginator](#listinputspaginator)
  - [ListMultiplexProgramsPaginator](#listmultiplexprogramspaginator)
  - [ListMultiplexesPaginator](#listmultiplexespaginator)
  - [ListOfferingsPaginator](#listofferingspaginator)
  - [ListReservationsPaginator](#listreservationspaginator)

## DescribeSchedulePaginator

Type annotations for `boto3.client("medialive").get_paginator("describe_schedule")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import DescribeSchedulePaginator

def get_describe_schedule_paginator() -> DescribeSchedulePaginator:
    return boto3.client("medialive").get_paginator("describe_schedule")
```

[Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)

```python
class DescribeSchedulePaginator(Boto3Paginator):
    def paginate(
        self,
        ChannelId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduleResponseTypeDef]:
        pass
```
## ListChannelsPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_channels")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListChannelsPaginator

def get_list_channels_paginator() -> ListChannelsPaginator:
    return boto3.client("medialive").get_paginator("list_channels")
```

[Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListChannels)

```python
class ListChannelsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        pass
```
## ListInputDeviceTransfersPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_input_device_transfers")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListInputDeviceTransfersPaginator

def get_list_input_device_transfers_paginator() -> ListInputDeviceTransfersPaginator:
    return boto3.client("medialive").get_paginator("list_input_device_transfers")
```

[Paginator.ListInputDeviceTransfers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputDeviceTransfers)

```python
class ListInputDeviceTransfersPaginator(Boto3Paginator):
    def paginate(
        self,
        TransferType: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputDeviceTransfersResponseTypeDef]:
        pass
```
## ListInputDevicesPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_input_devices")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListInputDevicesPaginator

def get_list_input_devices_paginator() -> ListInputDevicesPaginator:
    return boto3.client("medialive").get_paginator("list_input_devices")
```

[Paginator.ListInputDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputDevices)

```python
class ListInputDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputDevicesResponseTypeDef]:
        pass
```
## ListInputSecurityGroupsPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_input_security_groups")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListInputSecurityGroupsPaginator

def get_list_input_security_groups_paginator() -> ListInputSecurityGroupsPaginator:
    return boto3.client("medialive").get_paginator("list_input_security_groups")
```

[Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)

```python
class ListInputSecurityGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputSecurityGroupsResponseTypeDef]:
        pass
```
## ListInputsPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_inputs")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListInputsPaginator

def get_list_inputs_paginator() -> ListInputsPaginator:
    return boto3.client("medialive").get_paginator("list_inputs")
```

[Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputs)

```python
class ListInputsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputsResponseTypeDef]:
        pass
```
## ListMultiplexProgramsPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_multiplex_programs")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListMultiplexProgramsPaginator

def get_list_multiplex_programs_paginator() -> ListMultiplexProgramsPaginator:
    return boto3.client("medialive").get_paginator("list_multiplex_programs")
```

[Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)

```python
class ListMultiplexProgramsPaginator(Boto3Paginator):
    def paginate(
        self,
        MultiplexId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultiplexProgramsResponseTypeDef]:
        pass
```
## ListMultiplexesPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_multiplexes")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListMultiplexesPaginator

def get_list_multiplexes_paginator() -> ListMultiplexesPaginator:
    return boto3.client("medialive").get_paginator("list_multiplexes")
```

[Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)

```python
class ListMultiplexesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultiplexesResponseTypeDef]:
        pass
```
## ListOfferingsPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_offerings")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListOfferingsPaginator

def get_list_offerings_paginator() -> ListOfferingsPaginator:
    return boto3.client("medialive").get_paginator("list_offerings")
```

[Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)

```python
class ListOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingsResponseTypeDef]:
        pass
```
## ListReservationsPaginator

Type annotations for `boto3.client("medialive").get_paginator("list_reservations")`.

Can be used directly:

```python
from mypy_boto3_medialive.paginators import ListReservationsPaginator

def get_list_reservations_paginator() -> ListReservationsPaginator:
    return boto3.client("medialive").get_paginator("list_reservations")
```

[Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListReservations)

```python
class ListReservationsPaginator(Boto3Paginator):
    def paginate(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListReservationsResponseTypeDef]:
        pass
```