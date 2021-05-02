# MediaLiveClient for boto3 MediaLive module

> [Index](../index.md) > [MediaLive](./index.md) > MediaLiveClient

Auto-generated documentation for [MediaLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive)
type annotations stubs module [mypy_boto3_medialive](https://pypi.org/project/mypy-boto3-medialive/).

- [MediaLiveClient for boto3 MediaLive module](#medialiveclient-for-boto3-medialive-module)
  - [MediaLiveClient](#medialiveclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_input_device_transfer](#accept_input_device_transfer)
    - [batch_delete](#batch_delete)
    - [batch_start](#batch_start)
    - [batch_stop](#batch_stop)
    - [batch_update_schedule](#batch_update_schedule)
    - [can_paginate](#can_paginate)
    - [cancel_input_device_transfer](#cancel_input_device_transfer)
    - [create_channel](#create_channel)
    - [create_input](#create_input)
    - [create_input_security_group](#create_input_security_group)
    - [create_multiplex](#create_multiplex)
    - [create_multiplex_program](#create_multiplex_program)
    - [create_partner_input](#create_partner_input)
    - [create_tags](#create_tags)
    - [delete_channel](#delete_channel)
    - [delete_input](#delete_input)
    - [delete_input_security_group](#delete_input_security_group)
    - [delete_multiplex](#delete_multiplex)
    - [delete_multiplex_program](#delete_multiplex_program)
    - [delete_reservation](#delete_reservation)
    - [delete_schedule](#delete_schedule)
    - [delete_tags](#delete_tags)
    - [describe_channel](#describe_channel)
    - [describe_input](#describe_input)
    - [describe_input_device](#describe_input_device)
    - [describe_input_device_thumbnail](#describe_input_device_thumbnail)
    - [describe_input_security_group](#describe_input_security_group)
    - [describe_multiplex](#describe_multiplex)
    - [describe_multiplex_program](#describe_multiplex_program)
    - [describe_offering](#describe_offering)
    - [describe_reservation](#describe_reservation)
    - [describe_schedule](#describe_schedule)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_channels](#list_channels)
    - [list_input_device_transfers](#list_input_device_transfers)
    - [list_input_devices](#list_input_devices)
    - [list_input_security_groups](#list_input_security_groups)
    - [list_inputs](#list_inputs)
    - [list_multiplex_programs](#list_multiplex_programs)
    - [list_multiplexes](#list_multiplexes)
    - [list_offerings](#list_offerings)
    - [list_reservations](#list_reservations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [purchase_offering](#purchase_offering)
    - [reject_input_device_transfer](#reject_input_device_transfer)
    - [start_channel](#start_channel)
    - [start_multiplex](#start_multiplex)
    - [stop_channel](#stop_channel)
    - [stop_multiplex](#stop_multiplex)
    - [transfer_input_device](#transfer_input_device)
    - [update_channel](#update_channel)
    - [update_channel_class](#update_channel_class)
    - [update_input](#update_input)
    - [update_input_device](#update_input_device)
    - [update_input_security_group](#update_input_security_group)
    - [update_multiplex](#update_multiplex)
    - [update_multiplex_program](#update_multiplex_program)
    - [update_reservation](#update_reservation)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)
    - [get_waiter](#get_waiter-4)
    - [get_waiter](#get_waiter-5)
    - [get_waiter](#get_waiter-6)
    - [get_waiter](#get_waiter-7)
    - [get_waiter](#get_waiter-8)
    - [get_waiter](#get_waiter-9)
    - [get_waiter](#get_waiter-10)

## MediaLiveClient

Type annotations for `boto3.client("medialive")`

Can be used directly:

```python
from mypy_boto3_medialive.client import MediaLiveClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_medialive.client import Exceptions

def handle_error(exc: Exceptions.BadGatewayException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadGatewayException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.GatewayTimeoutException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnprocessableEntityException`


## Methods


### accept_input_device_transfer

Type annotations for `boto3.client("medialive").accept_input_device_transfer` method.

[Client.accept_input_device_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.accept_input_device_transfer)

```python
def accept_input_device_transfer(
    self,
    InputDeviceId: str
) -> Dict[str, Any]:
    pass
```

### batch_delete

Type annotations for `boto3.client("medialive").batch_delete` method.

[Client.batch_delete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_delete)

```python
def batch_delete(
    self,
    ChannelIds: List[str] = None,
    InputIds: List[str] = None,
    InputSecurityGroupIds: List[str] = None,
    MultiplexIds: List[str] = None
) -> BatchDeleteResponseTypeDef:
    pass
```

### batch_start

Type annotations for `boto3.client("medialive").batch_start` method.

[Client.batch_start documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_start)

```python
def batch_start(
    self,
    ChannelIds: List[str] = None,
    MultiplexIds: List[str] = None
) -> BatchStartResponseTypeDef:
    pass
```

### batch_stop

Type annotations for `boto3.client("medialive").batch_stop` method.

[Client.batch_stop documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_stop)

```python
def batch_stop(
    self,
    ChannelIds: List[str] = None,
    MultiplexIds: List[str] = None
) -> BatchStopResponseTypeDef:
    pass
```

### batch_update_schedule

Type annotations for `boto3.client("medialive").batch_update_schedule` method.

[Client.batch_update_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.batch_update_schedule)

```python
def batch_update_schedule(
    self,
    ChannelId: str,
    Creates: BatchScheduleActionCreateRequestTypeDef = None,
    Deletes: BatchScheduleActionDeleteRequestTypeDef = None
) -> BatchUpdateScheduleResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("medialive").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_input_device_transfer

Type annotations for `boto3.client("medialive").cancel_input_device_transfer` method.

[Client.cancel_input_device_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.cancel_input_device_transfer)

```python
def cancel_input_device_transfer(
    self,
    InputDeviceId: str
) -> Dict[str, Any]:
    pass
```

### create_channel

Type annotations for `boto3.client("medialive").create_channel` method.

[Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_channel)

```python
def create_channel(
    self,
    CdiInputSpecification: "CdiInputSpecificationTypeDef" = None,
    ChannelClass: ChannelClass = None,
    Destinations: List["OutputDestinationTypeDef"] = None,
    EncoderSettings: "EncoderSettingsTypeDef" = None,
    InputAttachments: List["InputAttachmentTypeDef"] = None,
    InputSpecification: "InputSpecificationTypeDef" = None,
    LogLevel: LogLevel = None,
    Name: str = None,
    RequestId: str = None,
    Reserved: str = None,
    RoleArn: str = None,
    Tags: Dict[str, str] = None,
    Vpc: VpcOutputSettingsTypeDef = None
) -> CreateChannelResponseTypeDef:
    pass
```

### create_input

Type annotations for `boto3.client("medialive").create_input` method.

[Client.create_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_input)

```python
def create_input(
    self,
    Destinations: List[InputDestinationRequestTypeDef] = None,
    InputDevices: List["InputDeviceSettingsTypeDef"] = None,
    InputSecurityGroups: List[str] = None,
    MediaConnectFlows: List[MediaConnectFlowRequestTypeDef] = None,
    Name: str = None,
    RequestId: str = None,
    RoleArn: str = None,
    Sources: List[InputSourceRequestTypeDef] = None,
    Tags: Dict[str, str] = None,
    Type: InputType = None,
    Vpc: InputVpcRequestTypeDef = None
) -> CreateInputResponseTypeDef:
    pass
```

### create_input_security_group

Type annotations for `boto3.client("medialive").create_input_security_group` method.

[Client.create_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_input_security_group)

```python
def create_input_security_group(
    self,
    Tags: Dict[str, str] = None,
    WhitelistRules: List[InputWhitelistRuleCidrTypeDef] = None
) -> CreateInputSecurityGroupResponseTypeDef:
    pass
```

### create_multiplex

Type annotations for `boto3.client("medialive").create_multiplex` method.

[Client.create_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_multiplex)

```python
def create_multiplex(
    self,
    AvailabilityZones: List[str],
    MultiplexSettings: "MultiplexSettingsTypeDef",
    Name: str,
    RequestId: str,
    Tags: Dict[str, str] = None
) -> CreateMultiplexResponseTypeDef:
    pass
```

### create_multiplex_program

Type annotations for `boto3.client("medialive").create_multiplex_program` method.

[Client.create_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_multiplex_program)

```python
def create_multiplex_program(
    self,
    MultiplexId: str,
    MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef",
    ProgramName: str,
    RequestId: str
) -> CreateMultiplexProgramResponseTypeDef:
    pass
```

### create_partner_input

Type annotations for `boto3.client("medialive").create_partner_input` method.

[Client.create_partner_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_partner_input)

```python
def create_partner_input(
    self,
    InputId: str,
    RequestId: str = None,
    Tags: Dict[str, str] = None
) -> CreatePartnerInputResponseTypeDef:
    pass
```

### create_tags

Type annotations for `boto3.client("medialive").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.create_tags)

```python
def create_tags(
    self,
    ResourceArn: str,
    Tags: Dict[str, str] = None
) -> None:
    pass
```

### delete_channel

Type annotations for `boto3.client("medialive").delete_channel` method.

[Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_channel)

```python
def delete_channel(
    self,
    ChannelId: str
) -> DeleteChannelResponseTypeDef:
    pass
```

### delete_input

Type annotations for `boto3.client("medialive").delete_input` method.

[Client.delete_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_input)

```python
def delete_input(
    self,
    InputId: str
) -> Dict[str, Any]:
    pass
```

### delete_input_security_group

Type annotations for `boto3.client("medialive").delete_input_security_group` method.

[Client.delete_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_input_security_group)

```python
def delete_input_security_group(
    self,
    InputSecurityGroupId: str
) -> Dict[str, Any]:
    pass
```

### delete_multiplex

Type annotations for `boto3.client("medialive").delete_multiplex` method.

[Client.delete_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_multiplex)

```python
def delete_multiplex(
    self,
    MultiplexId: str
) -> DeleteMultiplexResponseTypeDef:
    pass
```

### delete_multiplex_program

Type annotations for `boto3.client("medialive").delete_multiplex_program` method.

[Client.delete_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_multiplex_program)

```python
def delete_multiplex_program(
    self,
    MultiplexId: str,
    ProgramName: str
) -> DeleteMultiplexProgramResponseTypeDef:
    pass
```

### delete_reservation

Type annotations for `boto3.client("medialive").delete_reservation` method.

[Client.delete_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_reservation)

```python
def delete_reservation(
    self,
    ReservationId: str
) -> DeleteReservationResponseTypeDef:
    pass
```

### delete_schedule

Type annotations for `boto3.client("medialive").delete_schedule` method.

[Client.delete_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_schedule)

```python
def delete_schedule(
    self,
    ChannelId: str
) -> Dict[str, Any]:
    pass
```

### delete_tags

Type annotations for `boto3.client("medialive").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.delete_tags)

```python
def delete_tags(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### describe_channel

Type annotations for `boto3.client("medialive").describe_channel` method.

[Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_channel)

```python
def describe_channel(
    self,
    ChannelId: str
) -> DescribeChannelResponseTypeDef:
    pass
```

### describe_input

Type annotations for `boto3.client("medialive").describe_input` method.

[Client.describe_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input)

```python
def describe_input(
    self,
    InputId: str
) -> DescribeInputResponseTypeDef:
    pass
```

### describe_input_device

Type annotations for `boto3.client("medialive").describe_input_device` method.

[Client.describe_input_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input_device)

```python
def describe_input_device(
    self,
    InputDeviceId: str
) -> DescribeInputDeviceResponseTypeDef:
    pass
```

### describe_input_device_thumbnail

Type annotations for `boto3.client("medialive").describe_input_device_thumbnail` method.

[Client.describe_input_device_thumbnail documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input_device_thumbnail)

```python
def describe_input_device_thumbnail(
    self,
    InputDeviceId: str,
    Accept: AcceptHeader
) -> DescribeInputDeviceThumbnailResponseTypeDef:
    pass
```

### describe_input_security_group

Type annotations for `boto3.client("medialive").describe_input_security_group` method.

[Client.describe_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_input_security_group)

```python
def describe_input_security_group(
    self,
    InputSecurityGroupId: str
) -> DescribeInputSecurityGroupResponseTypeDef:
    pass
```

### describe_multiplex

Type annotations for `boto3.client("medialive").describe_multiplex` method.

[Client.describe_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_multiplex)

```python
def describe_multiplex(
    self,
    MultiplexId: str
) -> DescribeMultiplexResponseTypeDef:
    pass
```

### describe_multiplex_program

Type annotations for `boto3.client("medialive").describe_multiplex_program` method.

[Client.describe_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_multiplex_program)

```python
def describe_multiplex_program(
    self,
    MultiplexId: str,
    ProgramName: str
) -> DescribeMultiplexProgramResponseTypeDef:
    pass
```

### describe_offering

Type annotations for `boto3.client("medialive").describe_offering` method.

[Client.describe_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_offering)

```python
def describe_offering(
    self,
    OfferingId: str
) -> DescribeOfferingResponseTypeDef:
    pass
```

### describe_reservation

Type annotations for `boto3.client("medialive").describe_reservation` method.

[Client.describe_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_reservation)

```python
def describe_reservation(
    self,
    ReservationId: str
) -> DescribeReservationResponseTypeDef:
    pass
```

### describe_schedule

Type annotations for `boto3.client("medialive").describe_schedule` method.

[Client.describe_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.describe_schedule)

```python
def describe_schedule(
    self,
    ChannelId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeScheduleResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("medialive").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.generate_presigned_url)

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

### list_channels

Type annotations for `boto3.client("medialive").list_channels` method.

[Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_channels)

```python
def list_channels(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListChannelsResponseTypeDef:
    pass
```

### list_input_device_transfers

Type annotations for `boto3.client("medialive").list_input_device_transfers` method.

[Client.list_input_device_transfers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_input_device_transfers)

```python
def list_input_device_transfers(
    self,
    TransferType: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInputDeviceTransfersResponseTypeDef:
    pass
```

### list_input_devices

Type annotations for `boto3.client("medialive").list_input_devices` method.

[Client.list_input_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_input_devices)

```python
def list_input_devices(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInputDevicesResponseTypeDef:
    pass
```

### list_input_security_groups

Type annotations for `boto3.client("medialive").list_input_security_groups` method.

[Client.list_input_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_input_security_groups)

```python
def list_input_security_groups(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInputSecurityGroupsResponseTypeDef:
    pass
```

### list_inputs

Type annotations for `boto3.client("medialive").list_inputs` method.

[Client.list_inputs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_inputs)

```python
def list_inputs(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListInputsResponseTypeDef:
    pass
```

### list_multiplex_programs

Type annotations for `boto3.client("medialive").list_multiplex_programs` method.

[Client.list_multiplex_programs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_multiplex_programs)

```python
def list_multiplex_programs(
    self,
    MultiplexId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListMultiplexProgramsResponseTypeDef:
    pass
```

### list_multiplexes

Type annotations for `boto3.client("medialive").list_multiplexes` method.

[Client.list_multiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_multiplexes)

```python
def list_multiplexes(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListMultiplexesResponseTypeDef:
    pass
```

### list_offerings

Type annotations for `boto3.client("medialive").list_offerings` method.

[Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_offerings)

```python
def list_offerings(
    self,
    ChannelClass: str = None,
    ChannelConfiguration: str = None,
    Codec: str = None,
    Duration: str = None,
    MaxResults: int = None,
    MaximumBitrate: str = None,
    MaximumFramerate: str = None,
    NextToken: str = None,
    Resolution: str = None,
    ResourceType: str = None,
    SpecialFeature: str = None,
    VideoQuality: str = None
) -> ListOfferingsResponseTypeDef:
    pass
```

### list_reservations

Type annotations for `boto3.client("medialive").list_reservations` method.

[Client.list_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_reservations)

```python
def list_reservations(
    self,
    ChannelClass: str = None,
    Codec: str = None,
    MaxResults: int = None,
    MaximumBitrate: str = None,
    MaximumFramerate: str = None,
    NextToken: str = None,
    Resolution: str = None,
    ResourceType: str = None,
    SpecialFeature: str = None,
    VideoQuality: str = None
) -> ListReservationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("medialive").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### purchase_offering

Type annotations for `boto3.client("medialive").purchase_offering` method.

[Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.purchase_offering)

```python
def purchase_offering(
    self,
    Count: int,
    OfferingId: str,
    Name: str = None,
    RequestId: str = None,
    Start: str = None,
    Tags: Dict[str, str] = None
) -> PurchaseOfferingResponseTypeDef:
    pass
```

### reject_input_device_transfer

Type annotations for `boto3.client("medialive").reject_input_device_transfer` method.

[Client.reject_input_device_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.reject_input_device_transfer)

```python
def reject_input_device_transfer(
    self,
    InputDeviceId: str
) -> Dict[str, Any]:
    pass
```

### start_channel

Type annotations for `boto3.client("medialive").start_channel` method.

[Client.start_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.start_channel)

```python
def start_channel(
    self,
    ChannelId: str
) -> StartChannelResponseTypeDef:
    pass
```

### start_multiplex

Type annotations for `boto3.client("medialive").start_multiplex` method.

[Client.start_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.start_multiplex)

```python
def start_multiplex(
    self,
    MultiplexId: str
) -> StartMultiplexResponseTypeDef:
    pass
```

### stop_channel

Type annotations for `boto3.client("medialive").stop_channel` method.

[Client.stop_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.stop_channel)

```python
def stop_channel(
    self,
    ChannelId: str
) -> StopChannelResponseTypeDef:
    pass
```

### stop_multiplex

Type annotations for `boto3.client("medialive").stop_multiplex` method.

[Client.stop_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.stop_multiplex)

```python
def stop_multiplex(
    self,
    MultiplexId: str
) -> StopMultiplexResponseTypeDef:
    pass
```

### transfer_input_device

Type annotations for `boto3.client("medialive").transfer_input_device` method.

[Client.transfer_input_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.transfer_input_device)

```python
def transfer_input_device(
    self,
    InputDeviceId: str,
    TargetCustomerId: str = None,
    TargetRegion: str = None,
    TransferMessage: str = None
) -> Dict[str, Any]:
    pass
```

### update_channel

Type annotations for `boto3.client("medialive").update_channel` method.

[Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_channel)

```python
def update_channel(
    self,
    ChannelId: str,
    CdiInputSpecification: "CdiInputSpecificationTypeDef" = None,
    Destinations: List["OutputDestinationTypeDef"] = None,
    EncoderSettings: "EncoderSettingsTypeDef" = None,
    InputAttachments: List["InputAttachmentTypeDef"] = None,
    InputSpecification: "InputSpecificationTypeDef" = None,
    LogLevel: LogLevel = None,
    Name: str = None,
    RoleArn: str = None
) -> UpdateChannelResponseTypeDef:
    pass
```

### update_channel_class

Type annotations for `boto3.client("medialive").update_channel_class` method.

[Client.update_channel_class documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_channel_class)

```python
def update_channel_class(
    self,
    ChannelClass: ChannelClass,
    ChannelId: str,
    Destinations: List["OutputDestinationTypeDef"] = None
) -> UpdateChannelClassResponseTypeDef:
    pass
```

### update_input

Type annotations for `boto3.client("medialive").update_input` method.

[Client.update_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_input)

```python
def update_input(
    self,
    InputId: str,
    Destinations: List[InputDestinationRequestTypeDef] = None,
    InputDevices: List[InputDeviceRequestTypeDef] = None,
    InputSecurityGroups: List[str] = None,
    MediaConnectFlows: List[MediaConnectFlowRequestTypeDef] = None,
    Name: str = None,
    RoleArn: str = None,
    Sources: List[InputSourceRequestTypeDef] = None
) -> UpdateInputResponseTypeDef:
    pass
```

### update_input_device

Type annotations for `boto3.client("medialive").update_input_device` method.

[Client.update_input_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_input_device)

```python
def update_input_device(
    self,
    InputDeviceId: str,
    HdDeviceSettings: InputDeviceConfigurableSettingsTypeDef = None,
    Name: str = None,
    UhdDeviceSettings: InputDeviceConfigurableSettingsTypeDef = None
) -> UpdateInputDeviceResponseTypeDef:
    pass
```

### update_input_security_group

Type annotations for `boto3.client("medialive").update_input_security_group` method.

[Client.update_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_input_security_group)

```python
def update_input_security_group(
    self,
    InputSecurityGroupId: str,
    Tags: Dict[str, str] = None,
    WhitelistRules: List[InputWhitelistRuleCidrTypeDef] = None
) -> UpdateInputSecurityGroupResponseTypeDef:
    pass
```

### update_multiplex

Type annotations for `boto3.client("medialive").update_multiplex` method.

[Client.update_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_multiplex)

```python
def update_multiplex(
    self,
    MultiplexId: str,
    MultiplexSettings: "MultiplexSettingsTypeDef" = None,
    Name: str = None
) -> UpdateMultiplexResponseTypeDef:
    pass
```

### update_multiplex_program

Type annotations for `boto3.client("medialive").update_multiplex_program` method.

[Client.update_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_multiplex_program)

```python
def update_multiplex_program(
    self,
    MultiplexId: str,
    ProgramName: str,
    MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef" = None
) -> UpdateMultiplexProgramResponseTypeDef:
    pass
```

### update_reservation

Type annotations for `boto3.client("medialive").update_reservation` method.

[Client.update_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Client.update_reservation)

```python
def update_reservation(
    self,
    ReservationId: str,
    Name: str = None
) -> UpdateReservationResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeSchedulePaginatorName
) -> DescribeSchedulePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListChannels)

```python
@overload
def get_paginator(
    self,
    operation_name: ListChannelsPaginatorName
) -> ListChannelsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListInputDeviceTransfers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputDeviceTransfers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInputDeviceTransfersPaginatorName
) -> ListInputDeviceTransfersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListInputDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputDevices)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInputDevicesPaginatorName
) -> ListInputDevicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInputSecurityGroupsPaginatorName
) -> ListInputSecurityGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListInputs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInputsPaginatorName
) -> ListInputsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMultiplexProgramsPaginatorName
) -> ListMultiplexProgramsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListMultiplexesPaginatorName
) -> ListMultiplexesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)

```python
@overload
def get_paginator(
    self,
    operation_name: ListOfferingsPaginatorName
) -> ListOfferingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("medialive").get_paginator` method.

[Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Paginator.ListReservations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListReservationsPaginatorName
) -> ListReservationsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.ChannelCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)

```python
@overload
def get_waiter(
    self,
    waiter_name: ChannelCreatedWaiterName
) -> ChannelCreatedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.ChannelDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: ChannelDeletedWaiterName
) -> ChannelDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.ChannelRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)

```python
@overload
def get_waiter(
    self,
    waiter_name: ChannelRunningWaiterName
) -> ChannelRunningWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.ChannelStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)

```python
@overload
def get_waiter(
    self,
    waiter_name: ChannelStoppedWaiterName
) -> ChannelStoppedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.InputAttached documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.InputAttached)

```python
@overload
def get_waiter(
    self,
    waiter_name: InputAttachedWaiterName
) -> InputAttachedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.InputDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.InputDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: InputDeletedWaiterName
) -> InputDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.InputDetached documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.InputDetached)

```python
@overload
def get_waiter(
    self,
    waiter_name: InputDetachedWaiterName
) -> InputDetachedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.MultiplexCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)

```python
@overload
def get_waiter(
    self,
    waiter_name: MultiplexCreatedWaiterName
) -> MultiplexCreatedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.MultiplexDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: MultiplexDeletedWaiterName
) -> MultiplexDeletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.MultiplexRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)

```python
@overload
def get_waiter(
    self,
    waiter_name: MultiplexRunningWaiterName
) -> MultiplexRunningWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("medialive").get_waiter` method.

[Waiter.MultiplexStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)

```python
@overload
def get_waiter(
    self,
    waiter_name: MultiplexStoppedWaiterName
) -> MultiplexStoppedWaiter:
    pass
```