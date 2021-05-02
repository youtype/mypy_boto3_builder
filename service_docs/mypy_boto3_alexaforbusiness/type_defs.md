# Structures for boto3 AlexaForBusiness module

> [Index](../index.md) > [AlexaForBusiness](./index.md) > Structures

Auto-generated documentation for [AlexaForBusiness](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness)
type annotations stubs module [mypy_boto3_alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/).

- [Structures for boto3 AlexaForBusiness module](#structures-for-boto3-alexaforbusiness-module)
  - [AddressBookDataTypeDef](#addressbookdatatypedef)
  - [AddressBookTypeDef](#addressbooktypedef)
  - [AudioTypeDef](#audiotypedef)
  - [BusinessReportContentRangeTypeDef](#businessreportcontentrangetypedef)
  - [BusinessReportRecurrenceTypeDef](#businessreportrecurrencetypedef)
  - [BusinessReportS3LocationTypeDef](#businessreports3locationtypedef)
  - [BusinessReportScheduleTypeDef](#businessreportscheduletypedef)
  - [BusinessReportTypeDef](#businessreporttypedef)
  - [CategoryTypeDef](#categorytypedef)
  - [ConferencePreferenceTypeDef](#conferencepreferencetypedef)
  - [ConferenceProviderTypeDef](#conferenceprovidertypedef)
  - [ContactDataTypeDef](#contactdatatypedef)
  - [ContactTypeDef](#contacttypedef)
  - [CreateEndOfMeetingReminderTypeDef](#createendofmeetingremindertypedef)
  - [CreateInstantBookingTypeDef](#createinstantbookingtypedef)
  - [CreateRequireCheckInTypeDef](#createrequirecheckintypedef)
  - [DeveloperInfoTypeDef](#developerinfotypedef)
  - [DeviceDataTypeDef](#devicedatatypedef)
  - [DeviceEventTypeDef](#deviceeventtypedef)
  - [DeviceNetworkProfileInfoTypeDef](#devicenetworkprofileinfotypedef)
  - [DeviceStatusDetailTypeDef](#devicestatusdetailtypedef)
  - [DeviceStatusInfoTypeDef](#devicestatusinfotypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [EndOfMeetingReminderTypeDef](#endofmeetingremindertypedef)
  - [GatewayGroupSummaryTypeDef](#gatewaygroupsummarytypedef)
  - [GatewayGroupTypeDef](#gatewaygrouptypedef)
  - [GatewaySummaryTypeDef](#gatewaysummarytypedef)
  - [GatewayTypeDef](#gatewaytypedef)
  - [IPDialInTypeDef](#ipdialintypedef)
  - [InstantBookingTypeDef](#instantbookingtypedef)
  - [MeetingRoomConfigurationTypeDef](#meetingroomconfigurationtypedef)
  - [MeetingSettingTypeDef](#meetingsettingtypedef)
  - [NetworkProfileDataTypeDef](#networkprofiledatatypedef)
  - [NetworkProfileTypeDef](#networkprofiletypedef)
  - [PSTNDialInTypeDef](#pstndialintypedef)
  - [PhoneNumberTypeDef](#phonenumbertypedef)
  - [ProfileDataTypeDef](#profiledatatypedef)
  - [ProfileTypeDef](#profiletypedef)
  - [RequireCheckInTypeDef](#requirecheckintypedef)
  - [RoomDataTypeDef](#roomdatatypedef)
  - [RoomSkillParameterTypeDef](#roomskillparametertypedef)
  - [RoomTypeDef](#roomtypedef)
  - [SipAddressTypeDef](#sipaddresstypedef)
  - [SkillDetailsTypeDef](#skilldetailstypedef)
  - [SkillGroupDataTypeDef](#skillgroupdatatypedef)
  - [SkillGroupTypeDef](#skillgrouptypedef)
  - [SkillSummaryTypeDef](#skillsummarytypedef)
  - [SkillsStoreSkillTypeDef](#skillsstoreskilltypedef)
  - [SmartHomeApplianceTypeDef](#smarthomeappliancetypedef)
  - [SsmlTypeDef](#ssmltypedef)
  - [TagTypeDef](#tagtypedef)
  - [TextTypeDef](#texttypedef)
  - [UpdateEndOfMeetingReminderTypeDef](#updateendofmeetingremindertypedef)
  - [UpdateInstantBookingTypeDef](#updateinstantbookingtypedef)
  - [UpdateRequireCheckInTypeDef](#updaterequirecheckintypedef)
  - [UserDataTypeDef](#userdatatypedef)
  - [ContentTypeDef](#contenttypedef)
  - [CreateAddressBookResponseTypeDef](#createaddressbookresponsetypedef)
  - [CreateBusinessReportScheduleResponseTypeDef](#createbusinessreportscheduleresponsetypedef)
  - [CreateConferenceProviderResponseTypeDef](#createconferenceproviderresponsetypedef)
  - [CreateContactResponseTypeDef](#createcontactresponsetypedef)
  - [CreateGatewayGroupResponseTypeDef](#creategatewaygroupresponsetypedef)
  - [CreateMeetingRoomConfigurationTypeDef](#createmeetingroomconfigurationtypedef)
  - [CreateNetworkProfileResponseTypeDef](#createnetworkprofileresponsetypedef)
  - [CreateProfileResponseTypeDef](#createprofileresponsetypedef)
  - [CreateRoomResponseTypeDef](#createroomresponsetypedef)
  - [CreateSkillGroupResponseTypeDef](#createskillgroupresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetAddressBookResponseTypeDef](#getaddressbookresponsetypedef)
  - [GetConferencePreferenceResponseTypeDef](#getconferencepreferenceresponsetypedef)
  - [GetConferenceProviderResponseTypeDef](#getconferenceproviderresponsetypedef)
  - [GetContactResponseTypeDef](#getcontactresponsetypedef)
  - [GetDeviceResponseTypeDef](#getdeviceresponsetypedef)
  - [GetGatewayGroupResponseTypeDef](#getgatewaygroupresponsetypedef)
  - [GetGatewayResponseTypeDef](#getgatewayresponsetypedef)
  - [GetInvitationConfigurationResponseTypeDef](#getinvitationconfigurationresponsetypedef)
  - [GetNetworkProfileResponseTypeDef](#getnetworkprofileresponsetypedef)
  - [GetProfileResponseTypeDef](#getprofileresponsetypedef)
  - [GetRoomResponseTypeDef](#getroomresponsetypedef)
  - [GetRoomSkillParameterResponseTypeDef](#getroomskillparameterresponsetypedef)
  - [GetSkillGroupResponseTypeDef](#getskillgroupresponsetypedef)
  - [ListBusinessReportSchedulesResponseTypeDef](#listbusinessreportschedulesresponsetypedef)
  - [ListConferenceProvidersResponseTypeDef](#listconferenceprovidersresponsetypedef)
  - [ListDeviceEventsResponseTypeDef](#listdeviceeventsresponsetypedef)
  - [ListGatewayGroupsResponseTypeDef](#listgatewaygroupsresponsetypedef)
  - [ListGatewaysResponseTypeDef](#listgatewaysresponsetypedef)
  - [ListSkillsResponseTypeDef](#listskillsresponsetypedef)
  - [ListSkillsStoreCategoriesResponseTypeDef](#listskillsstorecategoriesresponsetypedef)
  - [ListSkillsStoreSkillsByCategoryResponseTypeDef](#listskillsstoreskillsbycategoryresponsetypedef)
  - [ListSmartHomeAppliancesResponseTypeDef](#listsmarthomeappliancesresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RegisterAVSDeviceResponseTypeDef](#registeravsdeviceresponsetypedef)
  - [ResolveRoomResponseTypeDef](#resolveroomresponsetypedef)
  - [SearchAddressBooksResponseTypeDef](#searchaddressbooksresponsetypedef)
  - [SearchContactsResponseTypeDef](#searchcontactsresponsetypedef)
  - [SearchDevicesResponseTypeDef](#searchdevicesresponsetypedef)
  - [SearchNetworkProfilesResponseTypeDef](#searchnetworkprofilesresponsetypedef)
  - [SearchProfilesResponseTypeDef](#searchprofilesresponsetypedef)
  - [SearchRoomsResponseTypeDef](#searchroomsresponsetypedef)
  - [SearchSkillGroupsResponseTypeDef](#searchskillgroupsresponsetypedef)
  - [SearchUsersResponseTypeDef](#searchusersresponsetypedef)
  - [SendAnnouncementResponseTypeDef](#sendannouncementresponsetypedef)
  - [SortTypeDef](#sorttypedef)
  - [UpdateMeetingRoomConfigurationTypeDef](#updatemeetingroomconfigurationtypedef)

## AddressBookDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import AddressBookDataTypeDef
```




Optional fields:
- `AddressBookArn`: `str`
- `Name`: `str`
- `Description`: `str`


## AddressBookTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import AddressBookTypeDef
```




Optional fields:
- `AddressBookArn`: `str`
- `Name`: `str`
- `Description`: `str`


## AudioTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import AudioTypeDef
```


Required fields:
- `Locale`: `Locale`
- `Location`: `str`




## BusinessReportContentRangeTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import BusinessReportContentRangeTypeDef
```


Required fields:
- `Interval`: `BusinessReportInterval`




## BusinessReportRecurrenceTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import BusinessReportRecurrenceTypeDef
```




Optional fields:
- `StartDate`: `str`


## BusinessReportS3LocationTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import BusinessReportS3LocationTypeDef
```




Optional fields:
- `Path`: `str`
- `BucketName`: `str`


## BusinessReportScheduleTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import BusinessReportScheduleTypeDef
```




Optional fields:
- `ScheduleArn`: `str`
- `ScheduleName`: `str`
- `S3BucketName`: `str`
- `S3KeyPrefix`: `str`
- `Format`: `BusinessReportFormat`
- `ContentRange`: `"BusinessReportContentRangeTypeDef"`
- `Recurrence`: `"BusinessReportRecurrenceTypeDef"`
- `LastBusinessReport`: `"BusinessReportTypeDef"`


## BusinessReportTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import BusinessReportTypeDef
```




Optional fields:
- `Status`: `BusinessReportStatus`
- `FailureCode`: `BusinessReportFailureCode`
- `S3Location`: `"BusinessReportS3LocationTypeDef"`
- `DeliveryTime`: `datetime`
- `DownloadUrl`: `str`


## CategoryTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CategoryTypeDef
```




Optional fields:
- `CategoryId`: `int`
- `CategoryName`: `str`


## ConferencePreferenceTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ConferencePreferenceTypeDef
```




Optional fields:
- `DefaultConferenceProviderArn`: `str`


## ConferenceProviderTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ConferenceProviderTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Type`: `ConferenceProviderType`
- `IPDialIn`: `"IPDialInTypeDef"`
- `PSTNDialIn`: `"PSTNDialInTypeDef"`
- `MeetingSetting`: `"MeetingSettingTypeDef"`


## ContactDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ContactDataTypeDef
```




Optional fields:
- `ContactArn`: `str`
- `DisplayName`: `str`
- `FirstName`: `str`
- `LastName`: `str`
- `PhoneNumber`: `str`
- `PhoneNumbers`: `List["PhoneNumberTypeDef"]`
- `SipAddresses`: `List["SipAddressTypeDef"]`


## ContactTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ContactTypeDef
```




Optional fields:
- `ContactArn`: `str`
- `DisplayName`: `str`
- `FirstName`: `str`
- `LastName`: `str`
- `PhoneNumber`: `str`
- `PhoneNumbers`: `List["PhoneNumberTypeDef"]`
- `SipAddresses`: `List["SipAddressTypeDef"]`


## CreateEndOfMeetingReminderTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateEndOfMeetingReminderTypeDef
```


Required fields:
- `ReminderAtMinutes`: `List[int]`
- `ReminderType`: `EndOfMeetingReminderType`
- `Enabled`: `bool`




## CreateInstantBookingTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateInstantBookingTypeDef
```


Required fields:
- `DurationInMinutes`: `int`
- `Enabled`: `bool`




## CreateRequireCheckInTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateRequireCheckInTypeDef
```


Required fields:
- `ReleaseAfterMinutes`: `int`
- `Enabled`: `bool`




## DeveloperInfoTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeveloperInfoTypeDef
```




Optional fields:
- `DeveloperName`: `str`
- `PrivacyPolicy`: `str`
- `Email`: `str`
- `Url`: `str`


## DeviceDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeviceDataTypeDef
```




Optional fields:
- `DeviceArn`: `str`
- `DeviceSerialNumber`: `str`
- `DeviceType`: `str`
- `DeviceName`: `str`
- `SoftwareVersion`: `str`
- `MacAddress`: `str`
- `DeviceStatus`: `DeviceStatus`
- `NetworkProfileArn`: `str`
- `NetworkProfileName`: `str`
- `RoomArn`: `str`
- `RoomName`: `str`
- `DeviceStatusInfo`: `"DeviceStatusInfoTypeDef"`
- `CreatedTime`: `datetime`


## DeviceEventTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeviceEventTypeDef
```




Optional fields:
- `Type`: `DeviceEventType`
- `Value`: `str`
- `Timestamp`: `datetime`


## DeviceNetworkProfileInfoTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeviceNetworkProfileInfoTypeDef
```




Optional fields:
- `NetworkProfileArn`: `str`
- `CertificateArn`: `str`
- `CertificateExpirationTime`: `datetime`


## DeviceStatusDetailTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeviceStatusDetailTypeDef
```




Optional fields:
- `Feature`: `Feature`
- `Code`: `DeviceStatusDetailCode`


## DeviceStatusInfoTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeviceStatusInfoTypeDef
```




Optional fields:
- `DeviceStatusDetails`: `List["DeviceStatusDetailTypeDef"]`
- `ConnectionStatus`: `ConnectionStatus`
- `ConnectionStatusUpdatedTime`: `datetime`


## DeviceTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import DeviceTypeDef
```




Optional fields:
- `DeviceArn`: `str`
- `DeviceSerialNumber`: `str`
- `DeviceType`: `str`
- `DeviceName`: `str`
- `SoftwareVersion`: `str`
- `MacAddress`: `str`
- `RoomArn`: `str`
- `DeviceStatus`: `DeviceStatus`
- `DeviceStatusInfo`: `"DeviceStatusInfoTypeDef"`
- `NetworkProfileInfo`: `"DeviceNetworkProfileInfoTypeDef"`


## EndOfMeetingReminderTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import EndOfMeetingReminderTypeDef
```




Optional fields:
- `ReminderAtMinutes`: `List[int]`
- `ReminderType`: `EndOfMeetingReminderType`
- `Enabled`: `bool`


## GatewayGroupSummaryTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GatewayGroupSummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Description`: `str`


## GatewayGroupTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GatewayGroupTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Description`: `str`


## GatewaySummaryTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GatewaySummaryTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Description`: `str`
- `GatewayGroupArn`: `str`
- `SoftwareVersion`: `str`


## GatewayTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GatewayTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`
- `Description`: `str`
- `GatewayGroupArn`: `str`
- `SoftwareVersion`: `str`


## IPDialInTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import IPDialInTypeDef
```


Required fields:
- `Endpoint`: `str`
- `CommsProtocol`: `CommsProtocol`




## InstantBookingTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import InstantBookingTypeDef
```




Optional fields:
- `DurationInMinutes`: `int`
- `Enabled`: `bool`


## MeetingRoomConfigurationTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import MeetingRoomConfigurationTypeDef
```




Optional fields:
- `RoomUtilizationMetricsEnabled`: `bool`
- `EndOfMeetingReminder`: `"EndOfMeetingReminderTypeDef"`
- `InstantBooking`: `"InstantBookingTypeDef"`
- `RequireCheckIn`: `"RequireCheckInTypeDef"`


## MeetingSettingTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import MeetingSettingTypeDef
```


Required fields:
- `RequirePin`: `RequirePin`




## NetworkProfileDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import NetworkProfileDataTypeDef
```




Optional fields:
- `NetworkProfileArn`: `str`
- `NetworkProfileName`: `str`
- `Description`: `str`
- `Ssid`: `str`
- `SecurityType`: `NetworkSecurityType`
- `EapMethod`: `NetworkEapMethod`
- `CertificateAuthorityArn`: `str`


## NetworkProfileTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import NetworkProfileTypeDef
```




Optional fields:
- `NetworkProfileArn`: `str`
- `NetworkProfileName`: `str`
- `Description`: `str`
- `Ssid`: `str`
- `SecurityType`: `NetworkSecurityType`
- `EapMethod`: `NetworkEapMethod`
- `CurrentPassword`: `str`
- `NextPassword`: `str`
- `CertificateAuthorityArn`: `str`
- `TrustAnchors`: `List[str]`


## PSTNDialInTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import PSTNDialInTypeDef
```


Required fields:
- `CountryCode`: `str`
- `PhoneNumber`: `str`
- `OneClickIdDelay`: `str`
- `OneClickPinDelay`: `str`




## PhoneNumberTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import PhoneNumberTypeDef
```


Required fields:
- `Number`: `str`
- `Type`: `PhoneNumberType`




## ProfileDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ProfileDataTypeDef
```




Optional fields:
- `ProfileArn`: `str`
- `ProfileName`: `str`
- `IsDefault`: `bool`
- `Address`: `str`
- `Timezone`: `str`
- `DistanceUnit`: `DistanceUnit`
- `TemperatureUnit`: `TemperatureUnit`
- `WakeWord`: `WakeWord`
- `Locale`: `str`


## ProfileTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ProfileTypeDef
```




Optional fields:
- `ProfileArn`: `str`
- `ProfileName`: `str`
- `IsDefault`: `bool`
- `Address`: `str`
- `Timezone`: `str`
- `DistanceUnit`: `DistanceUnit`
- `TemperatureUnit`: `TemperatureUnit`
- `WakeWord`: `WakeWord`
- `Locale`: `str`
- `SetupModeDisabled`: `bool`
- `MaxVolumeLimit`: `int`
- `PSTNEnabled`: `bool`
- `DataRetentionOptIn`: `bool`
- `AddressBookArn`: `str`
- `MeetingRoomConfiguration`: `"MeetingRoomConfigurationTypeDef"`


## RequireCheckInTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import RequireCheckInTypeDef
```




Optional fields:
- `ReleaseAfterMinutes`: `int`
- `Enabled`: `bool`


## RoomDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import RoomDataTypeDef
```




Optional fields:
- `RoomArn`: `str`
- `RoomName`: `str`
- `Description`: `str`
- `ProviderCalendarId`: `str`
- `ProfileArn`: `str`
- `ProfileName`: `str`


## RoomSkillParameterTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import RoomSkillParameterTypeDef
```


Required fields:
- `ParameterKey`: `str`
- `ParameterValue`: `str`




## RoomTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import RoomTypeDef
```




Optional fields:
- `RoomArn`: `str`
- `RoomName`: `str`
- `Description`: `str`
- `ProviderCalendarId`: `str`
- `ProfileArn`: `str`


## SipAddressTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SipAddressTypeDef
```


Required fields:
- `Uri`: `str`
- `Type`: `SipType`




## SkillDetailsTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SkillDetailsTypeDef
```




Optional fields:
- `ProductDescription`: `str`
- `InvocationPhrase`: `str`
- `ReleaseDate`: `str`
- `EndUserLicenseAgreement`: `str`
- `GenericKeywords`: `List[str]`
- `BulletPoints`: `List[str]`
- `NewInThisVersionBulletPoints`: `List[str]`
- `SkillTypes`: `List[str]`
- `Reviews`: `Dict[str, str]`
- `DeveloperInfo`: `"DeveloperInfoTypeDef"`


## SkillGroupDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SkillGroupDataTypeDef
```




Optional fields:
- `SkillGroupArn`: `str`
- `SkillGroupName`: `str`
- `Description`: `str`


## SkillGroupTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SkillGroupTypeDef
```




Optional fields:
- `SkillGroupArn`: `str`
- `SkillGroupName`: `str`
- `Description`: `str`


## SkillSummaryTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SkillSummaryTypeDef
```




Optional fields:
- `SkillId`: `str`
- `SkillName`: `str`
- `SupportsLinking`: `bool`
- `EnablementType`: `EnablementType`
- `SkillType`: `SkillType`


## SkillsStoreSkillTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SkillsStoreSkillTypeDef
```




Optional fields:
- `SkillId`: `str`
- `SkillName`: `str`
- `ShortDescription`: `str`
- `IconUrl`: `str`
- `SampleUtterances`: `List[str]`
- `SkillDetails`: `"SkillDetailsTypeDef"`
- `SupportsLinking`: `bool`


## SmartHomeApplianceTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SmartHomeApplianceTypeDef
```




Optional fields:
- `FriendlyName`: `str`
- `Description`: `str`
- `ManufacturerName`: `str`


## SsmlTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SsmlTypeDef
```


Required fields:
- `Locale`: `Locale`
- `Value`: `str`




## TagTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TextTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import TextTypeDef
```


Required fields:
- `Locale`: `Locale`
- `Value`: `str`




## UpdateEndOfMeetingReminderTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import UpdateEndOfMeetingReminderTypeDef
```




Optional fields:
- `ReminderAtMinutes`: `List[int]`
- `ReminderType`: `EndOfMeetingReminderType`
- `Enabled`: `bool`


## UpdateInstantBookingTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import UpdateInstantBookingTypeDef
```




Optional fields:
- `DurationInMinutes`: `int`
- `Enabled`: `bool`


## UpdateRequireCheckInTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import UpdateRequireCheckInTypeDef
```




Optional fields:
- `ReleaseAfterMinutes`: `int`
- `Enabled`: `bool`


## UserDataTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import UserDataTypeDef
```




Optional fields:
- `UserArn`: `str`
- `FirstName`: `str`
- `LastName`: `str`
- `Email`: `str`
- `EnrollmentStatus`: `EnrollmentStatus`
- `EnrollmentId`: `str`


## ContentTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ContentTypeDef
```




Optional fields:
- `TextList`: `List["TextTypeDef"]`
- `SsmlList`: `List["SsmlTypeDef"]`
- `AudioList`: `List["AudioTypeDef"]`


## CreateAddressBookResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateAddressBookResponseTypeDef
```




Optional fields:
- `AddressBookArn`: `str`


## CreateBusinessReportScheduleResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateBusinessReportScheduleResponseTypeDef
```




Optional fields:
- `ScheduleArn`: `str`


## CreateConferenceProviderResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateConferenceProviderResponseTypeDef
```




Optional fields:
- `ConferenceProviderArn`: `str`


## CreateContactResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateContactResponseTypeDef
```




Optional fields:
- `ContactArn`: `str`


## CreateGatewayGroupResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateGatewayGroupResponseTypeDef
```




Optional fields:
- `GatewayGroupArn`: `str`


## CreateMeetingRoomConfigurationTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateMeetingRoomConfigurationTypeDef
```




Optional fields:
- `RoomUtilizationMetricsEnabled`: `bool`
- `EndOfMeetingReminder`: `"CreateEndOfMeetingReminderTypeDef"`
- `InstantBooking`: `"CreateInstantBookingTypeDef"`
- `RequireCheckIn`: `"CreateRequireCheckInTypeDef"`


## CreateNetworkProfileResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateNetworkProfileResponseTypeDef
```




Optional fields:
- `NetworkProfileArn`: `str`


## CreateProfileResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateProfileResponseTypeDef
```




Optional fields:
- `ProfileArn`: `str`


## CreateRoomResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateRoomResponseTypeDef
```




Optional fields:
- `RoomArn`: `str`


## CreateSkillGroupResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateSkillGroupResponseTypeDef
```




Optional fields:
- `SkillGroupArn`: `str`


## CreateUserResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import CreateUserResponseTypeDef
```




Optional fields:
- `UserArn`: `str`


## FilterTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import FilterTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`




## GetAddressBookResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetAddressBookResponseTypeDef
```




Optional fields:
- `AddressBook`: `"AddressBookTypeDef"`


## GetConferencePreferenceResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetConferencePreferenceResponseTypeDef
```




Optional fields:
- `Preference`: `"ConferencePreferenceTypeDef"`


## GetConferenceProviderResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetConferenceProviderResponseTypeDef
```




Optional fields:
- `ConferenceProvider`: `"ConferenceProviderTypeDef"`


## GetContactResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetContactResponseTypeDef
```




Optional fields:
- `Contact`: `"ContactTypeDef"`


## GetDeviceResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetDeviceResponseTypeDef
```




Optional fields:
- `Device`: `"DeviceTypeDef"`


## GetGatewayGroupResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetGatewayGroupResponseTypeDef
```




Optional fields:
- `GatewayGroup`: `"GatewayGroupTypeDef"`


## GetGatewayResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetGatewayResponseTypeDef
```




Optional fields:
- `Gateway`: `"GatewayTypeDef"`


## GetInvitationConfigurationResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetInvitationConfigurationResponseTypeDef
```




Optional fields:
- `OrganizationName`: `str`
- `ContactEmail`: `str`
- `PrivateSkillIds`: `List[str]`


## GetNetworkProfileResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetNetworkProfileResponseTypeDef
```




Optional fields:
- `NetworkProfile`: `"NetworkProfileTypeDef"`


## GetProfileResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetProfileResponseTypeDef
```




Optional fields:
- `Profile`: `"ProfileTypeDef"`


## GetRoomResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetRoomResponseTypeDef
```




Optional fields:
- `Room`: `"RoomTypeDef"`


## GetRoomSkillParameterResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetRoomSkillParameterResponseTypeDef
```




Optional fields:
- `RoomSkillParameter`: `"RoomSkillParameterTypeDef"`


## GetSkillGroupResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import GetSkillGroupResponseTypeDef
```




Optional fields:
- `SkillGroup`: `"SkillGroupTypeDef"`


## ListBusinessReportSchedulesResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListBusinessReportSchedulesResponseTypeDef
```




Optional fields:
- `BusinessReportSchedules`: `List["BusinessReportScheduleTypeDef"]`
- `NextToken`: `str`


## ListConferenceProvidersResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListConferenceProvidersResponseTypeDef
```




Optional fields:
- `ConferenceProviders`: `List["ConferenceProviderTypeDef"]`
- `NextToken`: `str`


## ListDeviceEventsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListDeviceEventsResponseTypeDef
```




Optional fields:
- `DeviceEvents`: `List["DeviceEventTypeDef"]`
- `NextToken`: `str`


## ListGatewayGroupsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListGatewayGroupsResponseTypeDef
```




Optional fields:
- `GatewayGroups`: `List["GatewayGroupSummaryTypeDef"]`
- `NextToken`: `str`


## ListGatewaysResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListGatewaysResponseTypeDef
```




Optional fields:
- `Gateways`: `List["GatewaySummaryTypeDef"]`
- `NextToken`: `str`


## ListSkillsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListSkillsResponseTypeDef
```




Optional fields:
- `SkillSummaries`: `List["SkillSummaryTypeDef"]`
- `NextToken`: `str`


## ListSkillsStoreCategoriesResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListSkillsStoreCategoriesResponseTypeDef
```




Optional fields:
- `CategoryList`: `List["CategoryTypeDef"]`
- `NextToken`: `str`


## ListSkillsStoreSkillsByCategoryResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListSkillsStoreSkillsByCategoryResponseTypeDef
```




Optional fields:
- `SkillsStoreSkills`: `List["SkillsStoreSkillTypeDef"]`
- `NextToken`: `str`


## ListSmartHomeAppliancesResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListSmartHomeAppliancesResponseTypeDef
```




Optional fields:
- `SmartHomeAppliances`: `List["SmartHomeApplianceTypeDef"]`
- `NextToken`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RegisterAVSDeviceResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import RegisterAVSDeviceResponseTypeDef
```




Optional fields:
- `DeviceArn`: `str`


## ResolveRoomResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import ResolveRoomResponseTypeDef
```




Optional fields:
- `RoomArn`: `str`
- `RoomName`: `str`
- `RoomSkillParameters`: `List["RoomSkillParameterTypeDef"]`


## SearchAddressBooksResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchAddressBooksResponseTypeDef
```




Optional fields:
- `AddressBooks`: `List["AddressBookDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchContactsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchContactsResponseTypeDef
```




Optional fields:
- `Contacts`: `List["ContactDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchDevicesResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchDevicesResponseTypeDef
```




Optional fields:
- `Devices`: `List["DeviceDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchNetworkProfilesResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchNetworkProfilesResponseTypeDef
```




Optional fields:
- `NetworkProfiles`: `List["NetworkProfileDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchProfilesResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchProfilesResponseTypeDef
```




Optional fields:
- `Profiles`: `List["ProfileDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchRoomsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchRoomsResponseTypeDef
```




Optional fields:
- `Rooms`: `List["RoomDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchSkillGroupsResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchSkillGroupsResponseTypeDef
```




Optional fields:
- `SkillGroups`: `List["SkillGroupDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SearchUsersResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SearchUsersResponseTypeDef
```




Optional fields:
- `Users`: `List["UserDataTypeDef"]`
- `NextToken`: `str`
- `TotalCount`: `int`


## SendAnnouncementResponseTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SendAnnouncementResponseTypeDef
```




Optional fields:
- `AnnouncementArn`: `str`


## SortTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import SortTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `SortValue`




## UpdateMeetingRoomConfigurationTypeDef

```python
from mypy_boto3_alexaforbusiness.type_defs import UpdateMeetingRoomConfigurationTypeDef
```




Optional fields:
- `RoomUtilizationMetricsEnabled`: `bool`
- `EndOfMeetingReminder`: `"UpdateEndOfMeetingReminderTypeDef"`
- `InstantBooking`: `"UpdateInstantBookingTypeDef"`
- `RequireCheckIn`: `"UpdateRequireCheckInTypeDef"`

