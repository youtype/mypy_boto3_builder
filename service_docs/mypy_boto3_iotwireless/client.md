# IoTWirelessClient for boto3 IoTWireless module

> [Index](../index.md) > [IoTWireless](./index.md) > IoTWirelessClient

Auto-generated documentation for [IoTWireless](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless)
type annotations stubs module [mypy_boto3_iotwireless](https://pypi.org/project/mypy-boto3-iotwireless/).

- [IoTWirelessClient for boto3 IoTWireless module](#iotwirelessclient-for-boto3-iotwireless-module)
  - [IoTWirelessClient](#iotwirelessclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_aws_account_with_partner_account](#associate_aws_account_with_partner_account)
    - [associate_wireless_device_with_thing](#associate_wireless_device_with_thing)
    - [associate_wireless_gateway_with_certificate](#associate_wireless_gateway_with_certificate)
    - [associate_wireless_gateway_with_thing](#associate_wireless_gateway_with_thing)
    - [can_paginate](#can_paginate)
    - [create_destination](#create_destination)
    - [create_device_profile](#create_device_profile)
    - [create_service_profile](#create_service_profile)
    - [create_wireless_device](#create_wireless_device)
    - [create_wireless_gateway](#create_wireless_gateway)
    - [create_wireless_gateway_task](#create_wireless_gateway_task)
    - [create_wireless_gateway_task_definition](#create_wireless_gateway_task_definition)
    - [delete_destination](#delete_destination)
    - [delete_device_profile](#delete_device_profile)
    - [delete_service_profile](#delete_service_profile)
    - [delete_wireless_device](#delete_wireless_device)
    - [delete_wireless_gateway](#delete_wireless_gateway)
    - [delete_wireless_gateway_task](#delete_wireless_gateway_task)
    - [delete_wireless_gateway_task_definition](#delete_wireless_gateway_task_definition)
    - [disassociate_aws_account_from_partner_account](#disassociate_aws_account_from_partner_account)
    - [disassociate_wireless_device_from_thing](#disassociate_wireless_device_from_thing)
    - [disassociate_wireless_gateway_from_certificate](#disassociate_wireless_gateway_from_certificate)
    - [disassociate_wireless_gateway_from_thing](#disassociate_wireless_gateway_from_thing)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_destination](#get_destination)
    - [get_device_profile](#get_device_profile)
    - [get_partner_account](#get_partner_account)
    - [get_service_endpoint](#get_service_endpoint)
    - [get_service_profile](#get_service_profile)
    - [get_wireless_device](#get_wireless_device)
    - [get_wireless_device_statistics](#get_wireless_device_statistics)
    - [get_wireless_gateway](#get_wireless_gateway)
    - [get_wireless_gateway_certificate](#get_wireless_gateway_certificate)
    - [get_wireless_gateway_firmware_information](#get_wireless_gateway_firmware_information)
    - [get_wireless_gateway_statistics](#get_wireless_gateway_statistics)
    - [get_wireless_gateway_task](#get_wireless_gateway_task)
    - [get_wireless_gateway_task_definition](#get_wireless_gateway_task_definition)
    - [list_destinations](#list_destinations)
    - [list_device_profiles](#list_device_profiles)
    - [list_partner_accounts](#list_partner_accounts)
    - [list_service_profiles](#list_service_profiles)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_wireless_devices](#list_wireless_devices)
    - [list_wireless_gateway_task_definitions](#list_wireless_gateway_task_definitions)
    - [list_wireless_gateways](#list_wireless_gateways)
    - [send_data_to_wireless_device](#send_data_to_wireless_device)
    - [tag_resource](#tag_resource)
    - [test_wireless_device](#test_wireless_device)
    - [untag_resource](#untag_resource)
    - [update_destination](#update_destination)
    - [update_partner_account](#update_partner_account)
    - [update_wireless_device](#update_wireless_device)
    - [update_wireless_gateway](#update_wireless_gateway)

## IoTWirelessClient

Type annotations for `boto3.client("iotwireless")`

Can be used directly:

```python
from mypy_boto3_iotwireless.client import IoTWirelessClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotwireless.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.TooManyTagsException`
- `Exceptions.ValidationException`


## Methods


### associate_aws_account_with_partner_account

Type annotations for `boto3.client("iotwireless").associate_aws_account_with_partner_account` method.

[Client.associate_aws_account_with_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.associate_aws_account_with_partner_account)

```python
def associate_aws_account_with_partner_account(
    self,
    Sidewalk: "SidewalkAccountInfoTypeDef",
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> AssociateAwsAccountWithPartnerAccountResponseTypeDef:
    pass
```

### associate_wireless_device_with_thing

Type annotations for `boto3.client("iotwireless").associate_wireless_device_with_thing` method.

[Client.associate_wireless_device_with_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_device_with_thing)

```python
def associate_wireless_device_with_thing(
    self,
    Id: str,
    ThingArn: str
) -> Dict[str, Any]:
    pass
```

### associate_wireless_gateway_with_certificate

Type annotations for `boto3.client("iotwireless").associate_wireless_gateway_with_certificate` method.

[Client.associate_wireless_gateway_with_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_certificate)

```python
def associate_wireless_gateway_with_certificate(
    self,
    Id: str,
    IotCertificateId: str
) -> AssociateWirelessGatewayWithCertificateResponseTypeDef:
    pass
```

### associate_wireless_gateway_with_thing

Type annotations for `boto3.client("iotwireless").associate_wireless_gateway_with_thing` method.

[Client.associate_wireless_gateway_with_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.associate_wireless_gateway_with_thing)

```python
def associate_wireless_gateway_with_thing(
    self,
    Id: str,
    ThingArn: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("iotwireless").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_destination

Type annotations for `boto3.client("iotwireless").create_destination` method.

[Client.create_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_destination)

```python
def create_destination(
    self,
    Name: str,
    ExpressionType: ExpressionType,
    Expression: str,
    RoleArn: str,
    Description: str = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None
) -> CreateDestinationResponseTypeDef:
    pass
```

### create_device_profile

Type annotations for `boto3.client("iotwireless").create_device_profile` method.

[Client.create_device_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_device_profile)

```python
def create_device_profile(
    self,
    Name: str = None,
    LoRaWAN: "LoRaWANDeviceProfileTypeDef" = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None
) -> CreateDeviceProfileResponseTypeDef:
    pass
```

### create_service_profile

Type annotations for `boto3.client("iotwireless").create_service_profile` method.

[Client.create_service_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_service_profile)

```python
def create_service_profile(
    self,
    Name: str = None,
    LoRaWAN: LoRaWANServiceProfileTypeDef = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None
) -> CreateServiceProfileResponseTypeDef:
    pass
```

### create_wireless_device

Type annotations for `boto3.client("iotwireless").create_wireless_device` method.

[Client.create_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_device)

```python
def create_wireless_device(
    self,
    Type: WirelessDeviceType,
    DestinationName: str,
    Name: str = None,
    Description: str = None,
    ClientRequestToken: str = None,
    LoRaWAN: "LoRaWANDeviceTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateWirelessDeviceResponseTypeDef:
    pass
```

### create_wireless_gateway

Type annotations for `boto3.client("iotwireless").create_wireless_gateway` method.

[Client.create_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway)

```python
def create_wireless_gateway(
    self,
    LoRaWAN: "LoRaWANGatewayTypeDef",
    Name: str = None,
    Description: str = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None
) -> CreateWirelessGatewayResponseTypeDef:
    pass
```

### create_wireless_gateway_task

Type annotations for `boto3.client("iotwireless").create_wireless_gateway_task` method.

[Client.create_wireless_gateway_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task)

```python
def create_wireless_gateway_task(
    self,
    Id: str,
    WirelessGatewayTaskDefinitionId: str
) -> CreateWirelessGatewayTaskResponseTypeDef:
    pass
```

### create_wireless_gateway_task_definition

Type annotations for `boto3.client("iotwireless").create_wireless_gateway_task_definition` method.

[Client.create_wireless_gateway_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.create_wireless_gateway_task_definition)

```python
def create_wireless_gateway_task_definition(
    self,
    AutoCreateTasks: bool,
    Name: str = None,
    Update: "UpdateWirelessGatewayTaskCreateTypeDef" = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateWirelessGatewayTaskDefinitionResponseTypeDef:
    pass
```

### delete_destination

Type annotations for `boto3.client("iotwireless").delete_destination` method.

[Client.delete_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_destination)

```python
def delete_destination(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_device_profile

Type annotations for `boto3.client("iotwireless").delete_device_profile` method.

[Client.delete_device_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_device_profile)

```python
def delete_device_profile(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_service_profile

Type annotations for `boto3.client("iotwireless").delete_service_profile` method.

[Client.delete_service_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_service_profile)

```python
def delete_service_profile(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_wireless_device

Type annotations for `boto3.client("iotwireless").delete_wireless_device` method.

[Client.delete_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_device)

```python
def delete_wireless_device(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_wireless_gateway

Type annotations for `boto3.client("iotwireless").delete_wireless_gateway` method.

[Client.delete_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway)

```python
def delete_wireless_gateway(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_wireless_gateway_task

Type annotations for `boto3.client("iotwireless").delete_wireless_gateway_task` method.

[Client.delete_wireless_gateway_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task)

```python
def delete_wireless_gateway_task(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_wireless_gateway_task_definition

Type annotations for `boto3.client("iotwireless").delete_wireless_gateway_task_definition` method.

[Client.delete_wireless_gateway_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.delete_wireless_gateway_task_definition)

```python
def delete_wireless_gateway_task_definition(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### disassociate_aws_account_from_partner_account

Type annotations for `boto3.client("iotwireless").disassociate_aws_account_from_partner_account` method.

[Client.disassociate_aws_account_from_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.disassociate_aws_account_from_partner_account)

```python
def disassociate_aws_account_from_partner_account(
    self,
    PartnerAccountId: str,
    PartnerType: Literal['Sidewalk']
) -> Dict[str, Any]:
    pass
```

### disassociate_wireless_device_from_thing

Type annotations for `boto3.client("iotwireless").disassociate_wireless_device_from_thing` method.

[Client.disassociate_wireless_device_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_device_from_thing)

```python
def disassociate_wireless_device_from_thing(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### disassociate_wireless_gateway_from_certificate

Type annotations for `boto3.client("iotwireless").disassociate_wireless_gateway_from_certificate` method.

[Client.disassociate_wireless_gateway_from_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_certificate)

```python
def disassociate_wireless_gateway_from_certificate(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### disassociate_wireless_gateway_from_thing

Type annotations for `boto3.client("iotwireless").disassociate_wireless_gateway_from_thing` method.

[Client.disassociate_wireless_gateway_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.disassociate_wireless_gateway_from_thing)

```python
def disassociate_wireless_gateway_from_thing(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotwireless").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.generate_presigned_url)

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

### get_destination

Type annotations for `boto3.client("iotwireless").get_destination` method.

[Client.get_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_destination)

```python
def get_destination(
    self,
    Name: str
) -> GetDestinationResponseTypeDef:
    pass
```

### get_device_profile

Type annotations for `boto3.client("iotwireless").get_device_profile` method.

[Client.get_device_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_device_profile)

```python
def get_device_profile(
    self,
    Id: str
) -> GetDeviceProfileResponseTypeDef:
    pass
```

### get_partner_account

Type annotations for `boto3.client("iotwireless").get_partner_account` method.

[Client.get_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_partner_account)

```python
def get_partner_account(
    self,
    PartnerAccountId: str,
    PartnerType: Literal['Sidewalk']
) -> GetPartnerAccountResponseTypeDef:
    pass
```

### get_service_endpoint

Type annotations for `boto3.client("iotwireless").get_service_endpoint` method.

[Client.get_service_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_service_endpoint)

```python
def get_service_endpoint(
    self,
    ServiceType: WirelessGatewayServiceType = None
) -> GetServiceEndpointResponseTypeDef:
    pass
```

### get_service_profile

Type annotations for `boto3.client("iotwireless").get_service_profile` method.

[Client.get_service_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_service_profile)

```python
def get_service_profile(
    self,
    Id: str
) -> GetServiceProfileResponseTypeDef:
    pass
```

### get_wireless_device

Type annotations for `boto3.client("iotwireless").get_wireless_device` method.

[Client.get_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device)

```python
def get_wireless_device(
    self,
    Identifier: str,
    IdentifierType: WirelessDeviceIdType
) -> GetWirelessDeviceResponseTypeDef:
    pass
```

### get_wireless_device_statistics

Type annotations for `boto3.client("iotwireless").get_wireless_device_statistics` method.

[Client.get_wireless_device_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_device_statistics)

```python
def get_wireless_device_statistics(
    self,
    WirelessDeviceId: str
) -> GetWirelessDeviceStatisticsResponseTypeDef:
    pass
```

### get_wireless_gateway

Type annotations for `boto3.client("iotwireless").get_wireless_gateway` method.

[Client.get_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway)

```python
def get_wireless_gateway(
    self,
    Identifier: str,
    IdentifierType: WirelessGatewayIdType
) -> GetWirelessGatewayResponseTypeDef:
    pass
```

### get_wireless_gateway_certificate

Type annotations for `boto3.client("iotwireless").get_wireless_gateway_certificate` method.

[Client.get_wireless_gateway_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_certificate)

```python
def get_wireless_gateway_certificate(
    self,
    Id: str
) -> GetWirelessGatewayCertificateResponseTypeDef:
    pass
```

### get_wireless_gateway_firmware_information

Type annotations for `boto3.client("iotwireless").get_wireless_gateway_firmware_information` method.

[Client.get_wireless_gateway_firmware_information documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_firmware_information)

```python
def get_wireless_gateway_firmware_information(
    self,
    Id: str
) -> GetWirelessGatewayFirmwareInformationResponseTypeDef:
    pass
```

### get_wireless_gateway_statistics

Type annotations for `boto3.client("iotwireless").get_wireless_gateway_statistics` method.

[Client.get_wireless_gateway_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_statistics)

```python
def get_wireless_gateway_statistics(
    self,
    WirelessGatewayId: str
) -> GetWirelessGatewayStatisticsResponseTypeDef:
    pass
```

### get_wireless_gateway_task

Type annotations for `boto3.client("iotwireless").get_wireless_gateway_task` method.

[Client.get_wireless_gateway_task documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task)

```python
def get_wireless_gateway_task(
    self,
    Id: str
) -> GetWirelessGatewayTaskResponseTypeDef:
    pass
```

### get_wireless_gateway_task_definition

Type annotations for `boto3.client("iotwireless").get_wireless_gateway_task_definition` method.

[Client.get_wireless_gateway_task_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.get_wireless_gateway_task_definition)

```python
def get_wireless_gateway_task_definition(
    self,
    Id: str
) -> GetWirelessGatewayTaskDefinitionResponseTypeDef:
    pass
```

### list_destinations

Type annotations for `boto3.client("iotwireless").list_destinations` method.

[Client.list_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_destinations)

```python
def list_destinations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDestinationsResponseTypeDef:
    pass
```

### list_device_profiles

Type annotations for `boto3.client("iotwireless").list_device_profiles` method.

[Client.list_device_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_device_profiles)

```python
def list_device_profiles(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDeviceProfilesResponseTypeDef:
    pass
```

### list_partner_accounts

Type annotations for `boto3.client("iotwireless").list_partner_accounts` method.

[Client.list_partner_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_partner_accounts)

```python
def list_partner_accounts(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPartnerAccountsResponseTypeDef:
    pass
```

### list_service_profiles

Type annotations for `boto3.client("iotwireless").list_service_profiles` method.

[Client.list_service_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_service_profiles)

```python
def list_service_profiles(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListServiceProfilesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotwireless").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_wireless_devices

Type annotations for `boto3.client("iotwireless").list_wireless_devices` method.

[Client.list_wireless_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_devices)

```python
def list_wireless_devices(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    DestinationName: str = None,
    DeviceProfileId: str = None,
    ServiceProfileId: str = None,
    WirelessDeviceType: WirelessDeviceType = None
) -> ListWirelessDevicesResponseTypeDef:
    pass
```

### list_wireless_gateway_task_definitions

Type annotations for `boto3.client("iotwireless").list_wireless_gateway_task_definitions` method.

[Client.list_wireless_gateway_task_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateway_task_definitions)

```python
def list_wireless_gateway_task_definitions(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    TaskDefinitionType: Literal['UPDATE'] = None
) -> ListWirelessGatewayTaskDefinitionsResponseTypeDef:
    pass
```

### list_wireless_gateways

Type annotations for `boto3.client("iotwireless").list_wireless_gateways` method.

[Client.list_wireless_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.list_wireless_gateways)

```python
def list_wireless_gateways(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWirelessGatewaysResponseTypeDef:
    pass
```

### send_data_to_wireless_device

Type annotations for `boto3.client("iotwireless").send_data_to_wireless_device` method.

[Client.send_data_to_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.send_data_to_wireless_device)

```python
def send_data_to_wireless_device(
    self,
    Id: str,
    TransmitMode: int,
    PayloadData: str,
    WirelessMetadata: WirelessMetadataTypeDef = None
) -> SendDataToWirelessDeviceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotwireless").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### test_wireless_device

Type annotations for `boto3.client("iotwireless").test_wireless_device` method.

[Client.test_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.test_wireless_device)

```python
def test_wireless_device(
    self,
    Id: str
) -> TestWirelessDeviceResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotwireless").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_destination

Type annotations for `boto3.client("iotwireless").update_destination` method.

[Client.update_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.update_destination)

```python
def update_destination(
    self,
    Name: str,
    ExpressionType: ExpressionType = None,
    Expression: str = None,
    Description: str = None,
    RoleArn: str = None
) -> Dict[str, Any]:
    pass
```

### update_partner_account

Type annotations for `boto3.client("iotwireless").update_partner_account` method.

[Client.update_partner_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.update_partner_account)

```python
def update_partner_account(
    self,
    Sidewalk: SidewalkUpdateAccountTypeDef,
    PartnerAccountId: str,
    PartnerType: Literal['Sidewalk']
) -> Dict[str, Any]:
    pass
```

### update_wireless_device

Type annotations for `boto3.client("iotwireless").update_wireless_device` method.

[Client.update_wireless_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_device)

```python
def update_wireless_device(
    self,
    Id: str,
    DestinationName: str = None,
    Name: str = None,
    Description: str = None,
    LoRaWAN: LoRaWANUpdateDeviceTypeDef = None
) -> Dict[str, Any]:
    pass
```

### update_wireless_gateway

Type annotations for `boto3.client("iotwireless").update_wireless_gateway` method.

[Client.update_wireless_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.update_wireless_gateway)

```python
def update_wireless_gateway(
    self,
    Id: str,
    Name: str = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```



