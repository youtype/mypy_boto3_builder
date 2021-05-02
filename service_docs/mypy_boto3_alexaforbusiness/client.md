# AlexaForBusinessClient for boto3 AlexaForBusiness module

> [Index](../index.md) > [AlexaForBusiness](./index.md) > AlexaForBusinessClient

Auto-generated documentation for [AlexaForBusiness](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness)
type annotations stubs module [mypy_boto3_alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/).

- [AlexaForBusinessClient for boto3 AlexaForBusiness module](#alexaforbusinessclient-for-boto3-alexaforbusiness-module)
  - [AlexaForBusinessClient](#alexaforbusinessclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [approve_skill](#approve_skill)
    - [associate_contact_with_address_book](#associate_contact_with_address_book)
    - [associate_device_with_network_profile](#associate_device_with_network_profile)
    - [associate_device_with_room](#associate_device_with_room)
    - [associate_skill_group_with_room](#associate_skill_group_with_room)
    - [associate_skill_with_skill_group](#associate_skill_with_skill_group)
    - [associate_skill_with_users](#associate_skill_with_users)
    - [can_paginate](#can_paginate)
    - [create_address_book](#create_address_book)
    - [create_business_report_schedule](#create_business_report_schedule)
    - [create_conference_provider](#create_conference_provider)
    - [create_contact](#create_contact)
    - [create_gateway_group](#create_gateway_group)
    - [create_network_profile](#create_network_profile)
    - [create_profile](#create_profile)
    - [create_room](#create_room)
    - [create_skill_group](#create_skill_group)
    - [create_user](#create_user)
    - [delete_address_book](#delete_address_book)
    - [delete_business_report_schedule](#delete_business_report_schedule)
    - [delete_conference_provider](#delete_conference_provider)
    - [delete_contact](#delete_contact)
    - [delete_device](#delete_device)
    - [delete_device_usage_data](#delete_device_usage_data)
    - [delete_gateway_group](#delete_gateway_group)
    - [delete_network_profile](#delete_network_profile)
    - [delete_profile](#delete_profile)
    - [delete_room](#delete_room)
    - [delete_room_skill_parameter](#delete_room_skill_parameter)
    - [delete_skill_authorization](#delete_skill_authorization)
    - [delete_skill_group](#delete_skill_group)
    - [delete_user](#delete_user)
    - [disassociate_contact_from_address_book](#disassociate_contact_from_address_book)
    - [disassociate_device_from_room](#disassociate_device_from_room)
    - [disassociate_skill_from_skill_group](#disassociate_skill_from_skill_group)
    - [disassociate_skill_from_users](#disassociate_skill_from_users)
    - [disassociate_skill_group_from_room](#disassociate_skill_group_from_room)
    - [forget_smart_home_appliances](#forget_smart_home_appliances)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_address_book](#get_address_book)
    - [get_conference_preference](#get_conference_preference)
    - [get_conference_provider](#get_conference_provider)
    - [get_contact](#get_contact)
    - [get_device](#get_device)
    - [get_gateway](#get_gateway)
    - [get_gateway_group](#get_gateway_group)
    - [get_invitation_configuration](#get_invitation_configuration)
    - [get_network_profile](#get_network_profile)
    - [get_profile](#get_profile)
    - [get_room](#get_room)
    - [get_room_skill_parameter](#get_room_skill_parameter)
    - [get_skill_group](#get_skill_group)
    - [list_business_report_schedules](#list_business_report_schedules)
    - [list_conference_providers](#list_conference_providers)
    - [list_device_events](#list_device_events)
    - [list_gateway_groups](#list_gateway_groups)
    - [list_gateways](#list_gateways)
    - [list_skills](#list_skills)
    - [list_skills_store_categories](#list_skills_store_categories)
    - [list_skills_store_skills_by_category](#list_skills_store_skills_by_category)
    - [list_smart_home_appliances](#list_smart_home_appliances)
    - [list_tags](#list_tags)
    - [put_conference_preference](#put_conference_preference)
    - [put_invitation_configuration](#put_invitation_configuration)
    - [put_room_skill_parameter](#put_room_skill_parameter)
    - [put_skill_authorization](#put_skill_authorization)
    - [register_avs_device](#register_avs_device)
    - [reject_skill](#reject_skill)
    - [resolve_room](#resolve_room)
    - [revoke_invitation](#revoke_invitation)
    - [search_address_books](#search_address_books)
    - [search_contacts](#search_contacts)
    - [search_devices](#search_devices)
    - [search_network_profiles](#search_network_profiles)
    - [search_profiles](#search_profiles)
    - [search_rooms](#search_rooms)
    - [search_skill_groups](#search_skill_groups)
    - [search_users](#search_users)
    - [send_announcement](#send_announcement)
    - [send_invitation](#send_invitation)
    - [start_device_sync](#start_device_sync)
    - [start_smart_home_appliance_discovery](#start_smart_home_appliance_discovery)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_address_book](#update_address_book)
    - [update_business_report_schedule](#update_business_report_schedule)
    - [update_conference_provider](#update_conference_provider)
    - [update_contact](#update_contact)
    - [update_device](#update_device)
    - [update_gateway](#update_gateway)
    - [update_gateway_group](#update_gateway_group)
    - [update_network_profile](#update_network_profile)
    - [update_profile](#update_profile)
    - [update_room](#update_room)
    - [update_skill_group](#update_skill_group)
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
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)

## AlexaForBusinessClient

Type annotations for `boto3.client("alexaforbusiness")`

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.client import AlexaForBusinessClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_alexaforbusiness.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.DeviceNotRegisteredException`
- `Exceptions.InvalidCertificateAuthorityException`
- `Exceptions.InvalidDeviceException`
- `Exceptions.InvalidSecretsManagerResourceException`
- `Exceptions.InvalidServiceLinkedRoleStateException`
- `Exceptions.InvalidUserStatusException`
- `Exceptions.LimitExceededException`
- `Exceptions.NameInUseException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceAssociatedException`
- `Exceptions.ResourceInUseException`
- `Exceptions.SkillNotLinkedException`
- `Exceptions.UnauthorizedException`


## Methods


### approve_skill

Type annotations for `boto3.client("alexaforbusiness").approve_skill` method.

[Client.approve_skill documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.approve_skill)

```python
def approve_skill(
    self,
    SkillId: str
) -> Dict[str, Any]:
    pass
```

### associate_contact_with_address_book

Type annotations for `boto3.client("alexaforbusiness").associate_contact_with_address_book` method.

[Client.associate_contact_with_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_contact_with_address_book)

```python
def associate_contact_with_address_book(
    self,
    ContactArn: str,
    AddressBookArn: str
) -> Dict[str, Any]:
    pass
```

### associate_device_with_network_profile

Type annotations for `boto3.client("alexaforbusiness").associate_device_with_network_profile` method.

[Client.associate_device_with_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_device_with_network_profile)

```python
def associate_device_with_network_profile(
    self,
    DeviceArn: str,
    NetworkProfileArn: str
) -> Dict[str, Any]:
    pass
```

### associate_device_with_room

Type annotations for `boto3.client("alexaforbusiness").associate_device_with_room` method.

[Client.associate_device_with_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_device_with_room)

```python
def associate_device_with_room(
    self,
    DeviceArn: str = None,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### associate_skill_group_with_room

Type annotations for `boto3.client("alexaforbusiness").associate_skill_group_with_room` method.

[Client.associate_skill_group_with_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_group_with_room)

```python
def associate_skill_group_with_room(
    self,
    SkillGroupArn: str = None,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### associate_skill_with_skill_group

Type annotations for `boto3.client("alexaforbusiness").associate_skill_with_skill_group` method.

[Client.associate_skill_with_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_with_skill_group)

```python
def associate_skill_with_skill_group(
    self,
    SkillId: str,
    SkillGroupArn: str = None
) -> Dict[str, Any]:
    pass
```

### associate_skill_with_users

Type annotations for `boto3.client("alexaforbusiness").associate_skill_with_users` method.

[Client.associate_skill_with_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.associate_skill_with_users)

```python
def associate_skill_with_users(
    self,
    SkillId: str
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("alexaforbusiness").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_address_book

Type annotations for `boto3.client("alexaforbusiness").create_address_book` method.

[Client.create_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_address_book)

```python
def create_address_book(
    self,
    Name: str,
    Description: str = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAddressBookResponseTypeDef:
    pass
```

### create_business_report_schedule

Type annotations for `boto3.client("alexaforbusiness").create_business_report_schedule` method.

[Client.create_business_report_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_business_report_schedule)

```python
def create_business_report_schedule(
    self,
    Format: BusinessReportFormat,
    ContentRange: "BusinessReportContentRangeTypeDef",
    ScheduleName: str = None,
    S3BucketName: str = None,
    S3KeyPrefix: str = None,
    Recurrence: "BusinessReportRecurrenceTypeDef" = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateBusinessReportScheduleResponseTypeDef:
    pass
```

### create_conference_provider

Type annotations for `boto3.client("alexaforbusiness").create_conference_provider` method.

[Client.create_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_conference_provider)

```python
def create_conference_provider(
    self,
    ConferenceProviderName: str,
    ConferenceProviderType: ConferenceProviderType,
    MeetingSetting: "MeetingSettingTypeDef",
    IPDialIn: "IPDialInTypeDef" = None,
    PSTNDialIn: "PSTNDialInTypeDef" = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateConferenceProviderResponseTypeDef:
    pass
```

### create_contact

Type annotations for `boto3.client("alexaforbusiness").create_contact` method.

[Client.create_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_contact)

```python
def create_contact(
    self,
    FirstName: str,
    DisplayName: str = None,
    LastName: str = None,
    PhoneNumber: str = None,
    PhoneNumbers: List["PhoneNumberTypeDef"] = None,
    SipAddresses: List["SipAddressTypeDef"] = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateContactResponseTypeDef:
    pass
```

### create_gateway_group

Type annotations for `boto3.client("alexaforbusiness").create_gateway_group` method.

[Client.create_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_gateway_group)

```python
def create_gateway_group(
    self,
    Name: str,
    ClientRequestToken: str,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateGatewayGroupResponseTypeDef:
    pass
```

### create_network_profile

Type annotations for `boto3.client("alexaforbusiness").create_network_profile` method.

[Client.create_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_network_profile)

```python
def create_network_profile(
    self,
    NetworkProfileName: str,
    Ssid: str,
    SecurityType: NetworkSecurityType,
    ClientRequestToken: str,
    Description: str = None,
    EapMethod: NetworkEapMethod = None,
    CurrentPassword: str = None,
    NextPassword: str = None,
    CertificateAuthorityArn: str = None,
    TrustAnchors: List[str] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateNetworkProfileResponseTypeDef:
    pass
```

### create_profile

Type annotations for `boto3.client("alexaforbusiness").create_profile` method.

[Client.create_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_profile)

```python
def create_profile(
    self,
    ProfileName: str,
    Timezone: str,
    Address: str,
    DistanceUnit: DistanceUnit,
    TemperatureUnit: TemperatureUnit,
    WakeWord: WakeWord,
    Locale: str = None,
    ClientRequestToken: str = None,
    SetupModeDisabled: bool = None,
    MaxVolumeLimit: int = None,
    PSTNEnabled: bool = None,
    DataRetentionOptIn: bool = None,
    MeetingRoomConfiguration: CreateMeetingRoomConfigurationTypeDef = None,
    Tags: List["TagTypeDef"] = None
) -> CreateProfileResponseTypeDef:
    pass
```

### create_room

Type annotations for `boto3.client("alexaforbusiness").create_room` method.

[Client.create_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_room)

```python
def create_room(
    self,
    RoomName: str,
    Description: str = None,
    ProfileArn: str = None,
    ProviderCalendarId: str = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateRoomResponseTypeDef:
    pass
```

### create_skill_group

Type annotations for `boto3.client("alexaforbusiness").create_skill_group` method.

[Client.create_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_skill_group)

```python
def create_skill_group(
    self,
    SkillGroupName: str,
    Description: str = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateSkillGroupResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("alexaforbusiness").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.create_user)

```python
def create_user(
    self,
    UserId: str,
    FirstName: str = None,
    LastName: str = None,
    Email: str = None,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateUserResponseTypeDef:
    pass
```

### delete_address_book

Type annotations for `boto3.client("alexaforbusiness").delete_address_book` method.

[Client.delete_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_address_book)

```python
def delete_address_book(
    self,
    AddressBookArn: str
) -> Dict[str, Any]:
    pass
```

### delete_business_report_schedule

Type annotations for `boto3.client("alexaforbusiness").delete_business_report_schedule` method.

[Client.delete_business_report_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_business_report_schedule)

```python
def delete_business_report_schedule(
    self,
    ScheduleArn: str
) -> Dict[str, Any]:
    pass
```

### delete_conference_provider

Type annotations for `boto3.client("alexaforbusiness").delete_conference_provider` method.

[Client.delete_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_conference_provider)

```python
def delete_conference_provider(
    self,
    ConferenceProviderArn: str
) -> Dict[str, Any]:
    pass
```

### delete_contact

Type annotations for `boto3.client("alexaforbusiness").delete_contact` method.

[Client.delete_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_contact)

```python
def delete_contact(
    self,
    ContactArn: str
) -> Dict[str, Any]:
    pass
```

### delete_device

Type annotations for `boto3.client("alexaforbusiness").delete_device` method.

[Client.delete_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_device)

```python
def delete_device(
    self,
    DeviceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_device_usage_data

Type annotations for `boto3.client("alexaforbusiness").delete_device_usage_data` method.

[Client.delete_device_usage_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_device_usage_data)

```python
def delete_device_usage_data(
    self,
    DeviceArn: str,
    DeviceUsageType: DeviceUsageType
) -> Dict[str, Any]:
    pass
```

### delete_gateway_group

Type annotations for `boto3.client("alexaforbusiness").delete_gateway_group` method.

[Client.delete_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_gateway_group)

```python
def delete_gateway_group(
    self,
    GatewayGroupArn: str
) -> Dict[str, Any]:
    pass
```

### delete_network_profile

Type annotations for `boto3.client("alexaforbusiness").delete_network_profile` method.

[Client.delete_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_network_profile)

```python
def delete_network_profile(
    self,
    NetworkProfileArn: str
) -> Dict[str, Any]:
    pass
```

### delete_profile

Type annotations for `boto3.client("alexaforbusiness").delete_profile` method.

[Client.delete_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_profile)

```python
def delete_profile(
    self,
    ProfileArn: str = None
) -> Dict[str, Any]:
    pass
```

### delete_room

Type annotations for `boto3.client("alexaforbusiness").delete_room` method.

[Client.delete_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_room)

```python
def delete_room(
    self,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### delete_room_skill_parameter

Type annotations for `boto3.client("alexaforbusiness").delete_room_skill_parameter` method.

[Client.delete_room_skill_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_room_skill_parameter)

```python
def delete_room_skill_parameter(
    self,
    SkillId: str,
    ParameterKey: str,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### delete_skill_authorization

Type annotations for `boto3.client("alexaforbusiness").delete_skill_authorization` method.

[Client.delete_skill_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_skill_authorization)

```python
def delete_skill_authorization(
    self,
    SkillId: str,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### delete_skill_group

Type annotations for `boto3.client("alexaforbusiness").delete_skill_group` method.

[Client.delete_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_skill_group)

```python
def delete_skill_group(
    self,
    SkillGroupArn: str = None
) -> Dict[str, Any]:
    pass
```

### delete_user

Type annotations for `boto3.client("alexaforbusiness").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.delete_user)

```python
def delete_user(
    self,
    EnrollmentId: str,
    UserArn: str = None
) -> Dict[str, Any]:
    pass
```

### disassociate_contact_from_address_book

Type annotations for `boto3.client("alexaforbusiness").disassociate_contact_from_address_book` method.

[Client.disassociate_contact_from_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_contact_from_address_book)

```python
def disassociate_contact_from_address_book(
    self,
    ContactArn: str,
    AddressBookArn: str
) -> Dict[str, Any]:
    pass
```

### disassociate_device_from_room

Type annotations for `boto3.client("alexaforbusiness").disassociate_device_from_room` method.

[Client.disassociate_device_from_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_device_from_room)

```python
def disassociate_device_from_room(
    self,
    DeviceArn: str = None
) -> Dict[str, Any]:
    pass
```

### disassociate_skill_from_skill_group

Type annotations for `boto3.client("alexaforbusiness").disassociate_skill_from_skill_group` method.

[Client.disassociate_skill_from_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_from_skill_group)

```python
def disassociate_skill_from_skill_group(
    self,
    SkillId: str,
    SkillGroupArn: str = None
) -> Dict[str, Any]:
    pass
```

### disassociate_skill_from_users

Type annotations for `boto3.client("alexaforbusiness").disassociate_skill_from_users` method.

[Client.disassociate_skill_from_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_from_users)

```python
def disassociate_skill_from_users(
    self,
    SkillId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_skill_group_from_room

Type annotations for `boto3.client("alexaforbusiness").disassociate_skill_group_from_room` method.

[Client.disassociate_skill_group_from_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.disassociate_skill_group_from_room)

```python
def disassociate_skill_group_from_room(
    self,
    SkillGroupArn: str = None,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### forget_smart_home_appliances

Type annotations for `boto3.client("alexaforbusiness").forget_smart_home_appliances` method.

[Client.forget_smart_home_appliances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.forget_smart_home_appliances)

```python
def forget_smart_home_appliances(
    self,
    RoomArn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("alexaforbusiness").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.generate_presigned_url)

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

### get_address_book

Type annotations for `boto3.client("alexaforbusiness").get_address_book` method.

[Client.get_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_address_book)

```python
def get_address_book(
    self,
    AddressBookArn: str
) -> GetAddressBookResponseTypeDef:
    pass
```

### get_conference_preference

Type annotations for `boto3.client("alexaforbusiness").get_conference_preference` method.

[Client.get_conference_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_conference_preference)

```python
def get_conference_preference(
    self
) -> GetConferencePreferenceResponseTypeDef:
    pass
```

### get_conference_provider

Type annotations for `boto3.client("alexaforbusiness").get_conference_provider` method.

[Client.get_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_conference_provider)

```python
def get_conference_provider(
    self,
    ConferenceProviderArn: str
) -> GetConferenceProviderResponseTypeDef:
    pass
```

### get_contact

Type annotations for `boto3.client("alexaforbusiness").get_contact` method.

[Client.get_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_contact)

```python
def get_contact(
    self,
    ContactArn: str
) -> GetContactResponseTypeDef:
    pass
```

### get_device

Type annotations for `boto3.client("alexaforbusiness").get_device` method.

[Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_device)

```python
def get_device(
    self,
    DeviceArn: str = None
) -> GetDeviceResponseTypeDef:
    pass
```

### get_gateway

Type annotations for `boto3.client("alexaforbusiness").get_gateway` method.

[Client.get_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_gateway)

```python
def get_gateway(
    self,
    GatewayArn: str
) -> GetGatewayResponseTypeDef:
    pass
```

### get_gateway_group

Type annotations for `boto3.client("alexaforbusiness").get_gateway_group` method.

[Client.get_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_gateway_group)

```python
def get_gateway_group(
    self,
    GatewayGroupArn: str
) -> GetGatewayGroupResponseTypeDef:
    pass
```

### get_invitation_configuration

Type annotations for `boto3.client("alexaforbusiness").get_invitation_configuration` method.

[Client.get_invitation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_invitation_configuration)

```python
def get_invitation_configuration(
    self
) -> GetInvitationConfigurationResponseTypeDef:
    pass
```

### get_network_profile

Type annotations for `boto3.client("alexaforbusiness").get_network_profile` method.

[Client.get_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_network_profile)

```python
def get_network_profile(
    self,
    NetworkProfileArn: str
) -> GetNetworkProfileResponseTypeDef:
    pass
```

### get_profile

Type annotations for `boto3.client("alexaforbusiness").get_profile` method.

[Client.get_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_profile)

```python
def get_profile(
    self,
    ProfileArn: str = None
) -> GetProfileResponseTypeDef:
    pass
```

### get_room

Type annotations for `boto3.client("alexaforbusiness").get_room` method.

[Client.get_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_room)

```python
def get_room(
    self,
    RoomArn: str = None
) -> GetRoomResponseTypeDef:
    pass
```

### get_room_skill_parameter

Type annotations for `boto3.client("alexaforbusiness").get_room_skill_parameter` method.

[Client.get_room_skill_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_room_skill_parameter)

```python
def get_room_skill_parameter(
    self,
    SkillId: str,
    ParameterKey: str,
    RoomArn: str = None
) -> GetRoomSkillParameterResponseTypeDef:
    pass
```

### get_skill_group

Type annotations for `boto3.client("alexaforbusiness").get_skill_group` method.

[Client.get_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.get_skill_group)

```python
def get_skill_group(
    self,
    SkillGroupArn: str = None
) -> GetSkillGroupResponseTypeDef:
    pass
```

### list_business_report_schedules

Type annotations for `boto3.client("alexaforbusiness").list_business_report_schedules` method.

[Client.list_business_report_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_business_report_schedules)

```python
def list_business_report_schedules(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListBusinessReportSchedulesResponseTypeDef:
    pass
```

### list_conference_providers

Type annotations for `boto3.client("alexaforbusiness").list_conference_providers` method.

[Client.list_conference_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_conference_providers)

```python
def list_conference_providers(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListConferenceProvidersResponseTypeDef:
    pass
```

### list_device_events

Type annotations for `boto3.client("alexaforbusiness").list_device_events` method.

[Client.list_device_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_device_events)

```python
def list_device_events(
    self,
    DeviceArn: str,
    EventType: DeviceEventType = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDeviceEventsResponseTypeDef:
    pass
```

### list_gateway_groups

Type annotations for `boto3.client("alexaforbusiness").list_gateway_groups` method.

[Client.list_gateway_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_gateway_groups)

```python
def list_gateway_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListGatewayGroupsResponseTypeDef:
    pass
```

### list_gateways

Type annotations for `boto3.client("alexaforbusiness").list_gateways` method.

[Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_gateways)

```python
def list_gateways(
    self,
    GatewayGroupArn: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListGatewaysResponseTypeDef:
    pass
```

### list_skills

Type annotations for `boto3.client("alexaforbusiness").list_skills` method.

[Client.list_skills documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills)

```python
def list_skills(
    self,
    SkillGroupArn: str = None,
    EnablementType: EnablementTypeFilter = None,
    SkillType: SkillTypeFilter = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSkillsResponseTypeDef:
    pass
```

### list_skills_store_categories

Type annotations for `boto3.client("alexaforbusiness").list_skills_store_categories` method.

[Client.list_skills_store_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills_store_categories)

```python
def list_skills_store_categories(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSkillsStoreCategoriesResponseTypeDef:
    pass
```

### list_skills_store_skills_by_category

Type annotations for `boto3.client("alexaforbusiness").list_skills_store_skills_by_category` method.

[Client.list_skills_store_skills_by_category documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_skills_store_skills_by_category)

```python
def list_skills_store_skills_by_category(
    self,
    CategoryId: int,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSkillsStoreSkillsByCategoryResponseTypeDef:
    pass
```

### list_smart_home_appliances

Type annotations for `boto3.client("alexaforbusiness").list_smart_home_appliances` method.

[Client.list_smart_home_appliances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_smart_home_appliances)

```python
def list_smart_home_appliances(
    self,
    RoomArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSmartHomeAppliancesResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("alexaforbusiness").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.list_tags)

```python
def list_tags(
    self,
    Arn: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTagsResponseTypeDef:
    pass
```

### put_conference_preference

Type annotations for `boto3.client("alexaforbusiness").put_conference_preference` method.

[Client.put_conference_preference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_conference_preference)

```python
def put_conference_preference(
    self,
    ConferencePreference: "ConferencePreferenceTypeDef"
) -> Dict[str, Any]:
    pass
```

### put_invitation_configuration

Type annotations for `boto3.client("alexaforbusiness").put_invitation_configuration` method.

[Client.put_invitation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_invitation_configuration)

```python
def put_invitation_configuration(
    self,
    OrganizationName: str,
    ContactEmail: str = None,
    PrivateSkillIds: List[str] = None
) -> Dict[str, Any]:
    pass
```

### put_room_skill_parameter

Type annotations for `boto3.client("alexaforbusiness").put_room_skill_parameter` method.

[Client.put_room_skill_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_room_skill_parameter)

```python
def put_room_skill_parameter(
    self,
    SkillId: str,
    RoomSkillParameter: "RoomSkillParameterTypeDef",
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### put_skill_authorization

Type annotations for `boto3.client("alexaforbusiness").put_skill_authorization` method.

[Client.put_skill_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.put_skill_authorization)

```python
def put_skill_authorization(
    self,
    AuthorizationResult: Dict[str, str],
    SkillId: str,
    RoomArn: str = None
) -> Dict[str, Any]:
    pass
```

### register_avs_device

Type annotations for `boto3.client("alexaforbusiness").register_avs_device` method.

[Client.register_avs_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.register_avs_device)

```python
def register_avs_device(
    self,
    ClientId: str,
    UserCode: str,
    ProductId: str,
    AmazonId: str,
    DeviceSerialNumber: str = None,
    RoomArn: str = None,
    Tags: List["TagTypeDef"] = None
) -> RegisterAVSDeviceResponseTypeDef:
    pass
```

### reject_skill

Type annotations for `boto3.client("alexaforbusiness").reject_skill` method.

[Client.reject_skill documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.reject_skill)

```python
def reject_skill(
    self,
    SkillId: str
) -> Dict[str, Any]:
    pass
```

### resolve_room

Type annotations for `boto3.client("alexaforbusiness").resolve_room` method.

[Client.resolve_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.resolve_room)

```python
def resolve_room(
    self,
    UserId: str,
    SkillId: str
) -> ResolveRoomResponseTypeDef:
    pass
```

### revoke_invitation

Type annotations for `boto3.client("alexaforbusiness").revoke_invitation` method.

[Client.revoke_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.revoke_invitation)

```python
def revoke_invitation(
    self,
    UserArn: str = None,
    EnrollmentId: str = None
) -> Dict[str, Any]:
    pass
```

### search_address_books

Type annotations for `boto3.client("alexaforbusiness").search_address_books` method.

[Client.search_address_books documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_address_books)

```python
def search_address_books(
    self,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> SearchAddressBooksResponseTypeDef:
    pass
```

### search_contacts

Type annotations for `boto3.client("alexaforbusiness").search_contacts` method.

[Client.search_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_contacts)

```python
def search_contacts(
    self,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> SearchContactsResponseTypeDef:
    pass
```

### search_devices

Type annotations for `boto3.client("alexaforbusiness").search_devices` method.

[Client.search_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_devices)

```python
def search_devices(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None
) -> SearchDevicesResponseTypeDef:
    pass
```

### search_network_profiles

Type annotations for `boto3.client("alexaforbusiness").search_network_profiles` method.

[Client.search_network_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_network_profiles)

```python
def search_network_profiles(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None
) -> SearchNetworkProfilesResponseTypeDef:
    pass
```

### search_profiles

Type annotations for `boto3.client("alexaforbusiness").search_profiles` method.

[Client.search_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_profiles)

```python
def search_profiles(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None
) -> SearchProfilesResponseTypeDef:
    pass
```

### search_rooms

Type annotations for `boto3.client("alexaforbusiness").search_rooms` method.

[Client.search_rooms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_rooms)

```python
def search_rooms(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None
) -> SearchRoomsResponseTypeDef:
    pass
```

### search_skill_groups

Type annotations for `boto3.client("alexaforbusiness").search_skill_groups` method.

[Client.search_skill_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_skill_groups)

```python
def search_skill_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None
) -> SearchSkillGroupsResponseTypeDef:
    pass
```

### search_users

Type annotations for `boto3.client("alexaforbusiness").search_users` method.

[Client.search_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.search_users)

```python
def search_users(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[FilterTypeDef] = None,
    SortCriteria: List[SortTypeDef] = None
) -> SearchUsersResponseTypeDef:
    pass
```

### send_announcement

Type annotations for `boto3.client("alexaforbusiness").send_announcement` method.

[Client.send_announcement documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.send_announcement)

```python
def send_announcement(
    self,
    RoomFilters: List[FilterTypeDef],
    Content: ContentTypeDef,
    ClientRequestToken: str,
    TimeToLiveInSeconds: int = None
) -> SendAnnouncementResponseTypeDef:
    pass
```

### send_invitation

Type annotations for `boto3.client("alexaforbusiness").send_invitation` method.

[Client.send_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.send_invitation)

```python
def send_invitation(
    self,
    UserArn: str = None
) -> Dict[str, Any]:
    pass
```

### start_device_sync

Type annotations for `boto3.client("alexaforbusiness").start_device_sync` method.

[Client.start_device_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.start_device_sync)

```python
def start_device_sync(
    self,
    Features: List[Feature],
    RoomArn: str = None,
    DeviceArn: str = None
) -> Dict[str, Any]:
    pass
```

### start_smart_home_appliance_discovery

Type annotations for `boto3.client("alexaforbusiness").start_smart_home_appliance_discovery` method.

[Client.start_smart_home_appliance_discovery documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.start_smart_home_appliance_discovery)

```python
def start_smart_home_appliance_discovery(
    self,
    RoomArn: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("alexaforbusiness").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.tag_resource)

```python
def tag_resource(
    self,
    Arn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("alexaforbusiness").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.untag_resource)

```python
def untag_resource(
    self,
    Arn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_address_book

Type annotations for `boto3.client("alexaforbusiness").update_address_book` method.

[Client.update_address_book documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_address_book)

```python
def update_address_book(
    self,
    AddressBookArn: str,
    Name: str = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### update_business_report_schedule

Type annotations for `boto3.client("alexaforbusiness").update_business_report_schedule` method.

[Client.update_business_report_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_business_report_schedule)

```python
def update_business_report_schedule(
    self,
    ScheduleArn: str,
    S3BucketName: str = None,
    S3KeyPrefix: str = None,
    Format: BusinessReportFormat = None,
    ScheduleName: str = None,
    Recurrence: "BusinessReportRecurrenceTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_conference_provider

Type annotations for `boto3.client("alexaforbusiness").update_conference_provider` method.

[Client.update_conference_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_conference_provider)

```python
def update_conference_provider(
    self,
    ConferenceProviderArn: str,
    ConferenceProviderType: ConferenceProviderType,
    MeetingSetting: "MeetingSettingTypeDef",
    IPDialIn: "IPDialInTypeDef" = None,
    PSTNDialIn: "PSTNDialInTypeDef" = None
) -> Dict[str, Any]:
    pass
```

### update_contact

Type annotations for `boto3.client("alexaforbusiness").update_contact` method.

[Client.update_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_contact)

```python
def update_contact(
    self,
    ContactArn: str,
    DisplayName: str = None,
    FirstName: str = None,
    LastName: str = None,
    PhoneNumber: str = None,
    PhoneNumbers: List["PhoneNumberTypeDef"] = None,
    SipAddresses: List["SipAddressTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### update_device

Type annotations for `boto3.client("alexaforbusiness").update_device` method.

[Client.update_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_device)

```python
def update_device(
    self,
    DeviceArn: str = None,
    DeviceName: str = None
) -> Dict[str, Any]:
    pass
```

### update_gateway

Type annotations for `boto3.client("alexaforbusiness").update_gateway` method.

[Client.update_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_gateway)

```python
def update_gateway(
    self,
    GatewayArn: str,
    Name: str = None,
    Description: str = None,
    SoftwareVersion: str = None
) -> Dict[str, Any]:
    pass
```

### update_gateway_group

Type annotations for `boto3.client("alexaforbusiness").update_gateway_group` method.

[Client.update_gateway_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_gateway_group)

```python
def update_gateway_group(
    self,
    GatewayGroupArn: str,
    Name: str = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### update_network_profile

Type annotations for `boto3.client("alexaforbusiness").update_network_profile` method.

[Client.update_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_network_profile)

```python
def update_network_profile(
    self,
    NetworkProfileArn: str,
    NetworkProfileName: str = None,
    Description: str = None,
    CurrentPassword: str = None,
    NextPassword: str = None,
    CertificateAuthorityArn: str = None,
    TrustAnchors: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_profile

Type annotations for `boto3.client("alexaforbusiness").update_profile` method.

[Client.update_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_profile)

```python
def update_profile(
    self,
    ProfileArn: str = None,
    ProfileName: str = None,
    IsDefault: bool = None,
    Timezone: str = None,
    Address: str = None,
    DistanceUnit: DistanceUnit = None,
    TemperatureUnit: TemperatureUnit = None,
    WakeWord: WakeWord = None,
    Locale: str = None,
    SetupModeDisabled: bool = None,
    MaxVolumeLimit: int = None,
    PSTNEnabled: bool = None,
    DataRetentionOptIn: bool = None,
    MeetingRoomConfiguration: UpdateMeetingRoomConfigurationTypeDef = None
) -> Dict[str, Any]:
    pass
```

### update_room

Type annotations for `boto3.client("alexaforbusiness").update_room` method.

[Client.update_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_room)

```python
def update_room(
    self,
    RoomArn: str = None,
    RoomName: str = None,
    Description: str = None,
    ProviderCalendarId: str = None,
    ProfileArn: str = None
) -> Dict[str, Any]:
    pass
```

### update_skill_group

Type annotations for `boto3.client("alexaforbusiness").update_skill_group` method.

[Client.update_skill_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Client.update_skill_group)

```python
def update_skill_group(
    self,
    SkillGroupArn: str = None,
    SkillGroupName: str = None,
    Description: str = None
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListBusinessReportSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListBusinessReportSchedules)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBusinessReportSchedulesPaginatorName
) -> ListBusinessReportSchedulesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListConferenceProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListConferenceProviders)

```python
@overload
def get_paginator(
    self,
    operation_name: ListConferenceProvidersPaginatorName
) -> ListConferenceProvidersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListDeviceEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListDeviceEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDeviceEventsPaginatorName
) -> ListDeviceEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListSkills documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkills)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSkillsPaginatorName
) -> ListSkillsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListSkillsStoreCategories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreCategories)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSkillsStoreCategoriesPaginatorName
) -> ListSkillsStoreCategoriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListSkillsStoreSkillsByCategory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSkillsStoreSkillsByCategory)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSkillsStoreSkillsByCategoryPaginatorName
) -> ListSkillsStoreSkillsByCategoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListSmartHomeAppliances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListSmartHomeAppliances)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSmartHomeAppliancesPaginatorName
) -> ListSmartHomeAppliancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.ListTags)

```python
@overload
def get_paginator(
    self,
    operation_name: ListTagsPaginatorName
) -> ListTagsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.SearchDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchDevices)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchDevicesPaginatorName
) -> SearchDevicesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.SearchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchProfiles)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchProfilesPaginatorName
) -> SearchProfilesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.SearchRooms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchRooms)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchRoomsPaginatorName
) -> SearchRoomsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.SearchSkillGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchSkillGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchSkillGroupsPaginatorName
) -> SearchSkillGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("alexaforbusiness").get_paginator` method.

[Paginator.SearchUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness.Paginator.SearchUsers)

```python
@overload
def get_paginator(
    self,
    operation_name: SearchUsersPaginatorName
) -> SearchUsersPaginator:
    pass
```