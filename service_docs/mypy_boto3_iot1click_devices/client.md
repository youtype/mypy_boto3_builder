# IoT1ClickDevicesServiceClient for boto3 IoT1ClickDevicesService module

> [Index](../index.md) > [IoT1ClickDevicesService](./index.md) > IoT1ClickDevicesServiceClient

Auto-generated documentation for [IoT1ClickDevicesService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService)
type annotations stubs module [mypy_boto3_iot1click_devices](https://pypi.org/project/mypy-boto3-iot1click-devices/).

- [IoT1ClickDevicesServiceClient for boto3 IoT1ClickDevicesService module](#iot1clickdevicesserviceclient-for-boto3-iot1clickdevicesservice-module)
  - [IoT1ClickDevicesServiceClient](#iot1clickdevicesserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [claim_devices_by_claim_code](#claim_devices_by_claim_code)
    - [describe_device](#describe_device)
    - [finalize_device_claim](#finalize_device_claim)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_device_methods](#get_device_methods)
    - [initiate_device_claim](#initiate_device_claim)
    - [invoke_device_method](#invoke_device_method)
    - [list_device_events](#list_device_events)
    - [list_devices](#list_devices)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [unclaim_device](#unclaim_device)
    - [untag_resource](#untag_resource)
    - [update_device_state](#update_device_state)
    - [get_paginator](#get_paginator)

## IoT1ClickDevicesServiceClient

Type annotations for `boto3.client("iot1click-devices")`

Can be used directly:

```python
from mypy_boto3_iot1click_devices.client import IoT1ClickDevicesServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iot1click_devices.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.PreconditionFailedException`
- `Exceptions.RangeNotSatisfiableException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("iot1click-devices").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### claim_devices_by_claim_code

Type annotations for `boto3.client("iot1click-devices").claim_devices_by_claim_code` method.

[Client.claim_devices_by_claim_code documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.claim_devices_by_claim_code)

```python
def claim_devices_by_claim_code(
    self,
    ClaimCode: str
) -> ClaimDevicesByClaimCodeResponseTypeDef:
    pass
```

### describe_device

Type annotations for `boto3.client("iot1click-devices").describe_device` method.

[Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.describe_device)

```python
def describe_device(
    self,
    DeviceId: str
) -> DescribeDeviceResponseTypeDef:
    pass
```

### finalize_device_claim

Type annotations for `boto3.client("iot1click-devices").finalize_device_claim` method.

[Client.finalize_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.finalize_device_claim)

```python
def finalize_device_claim(
    self,
    DeviceId: str,
    Tags: Dict[str, str] = None
) -> FinalizeDeviceClaimResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iot1click-devices").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.generate_presigned_url)

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

### get_device_methods

Type annotations for `boto3.client("iot1click-devices").get_device_methods` method.

[Client.get_device_methods documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.get_device_methods)

```python
def get_device_methods(
    self,
    DeviceId: str
) -> GetDeviceMethodsResponseTypeDef:
    pass
```

### initiate_device_claim

Type annotations for `boto3.client("iot1click-devices").initiate_device_claim` method.

[Client.initiate_device_claim documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.initiate_device_claim)

```python
def initiate_device_claim(
    self,
    DeviceId: str
) -> InitiateDeviceClaimResponseTypeDef:
    pass
```

### invoke_device_method

Type annotations for `boto3.client("iot1click-devices").invoke_device_method` method.

[Client.invoke_device_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.invoke_device_method)

```python
def invoke_device_method(
    self,
    DeviceId: str,
    DeviceMethod: "DeviceMethodTypeDef" = None,
    DeviceMethodParameters: str = None
) -> InvokeDeviceMethodResponseTypeDef:
    pass
```

### list_device_events

Type annotations for `boto3.client("iot1click-devices").list_device_events` method.

[Client.list_device_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_device_events)

```python
def list_device_events(
    self,
    DeviceId: str,
    FromTimeStamp: datetime,
    ToTimeStamp: datetime,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDeviceEventsResponseTypeDef:
    pass
```

### list_devices

Type annotations for `boto3.client("iot1click-devices").list_devices` method.

[Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_devices)

```python
def list_devices(
    self,
    DeviceType: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDevicesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iot1click-devices").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iot1click-devices").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### unclaim_device

Type annotations for `boto3.client("iot1click-devices").unclaim_device` method.

[Client.unclaim_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.unclaim_device)

```python
def unclaim_device(
    self,
    DeviceId: str
) -> UnclaimDeviceResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("iot1click-devices").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_device_state

Type annotations for `boto3.client("iot1click-devices").update_device_state` method.

[Client.update_device_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html#IoT1ClickDevicesService.Client.update_device_state)

```python
def update_device_state(
    self,
    DeviceId: str,
    Enabled: bool = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("iot1click-devices").get_paginator` method with overloads.

- `client.get_paginator("list_device_events")` -> [ListDeviceEventsPaginator](./paginators.md#listdeviceeventspaginator)
- `client.get_paginator("list_devices")` -> [ListDevicesPaginator](./paginators.md#listdevicespaginator)


