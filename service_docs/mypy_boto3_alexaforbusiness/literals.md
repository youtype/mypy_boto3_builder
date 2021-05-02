# Literals for boto3 AlexaForBusiness module

> [Index](../index.md) > [AlexaForBusiness](./index.md) > Literals

Auto-generated documentation for [AlexaForBusiness](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness)
type annotations stubs module [mypy_boto3_alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/).

- [Literals for boto3 AlexaForBusiness module](#literals-for-boto3-alexaforbusiness-module)
  - [BusinessReportFailureCode](#businessreportfailurecode)
  - [BusinessReportFormat](#businessreportformat)
  - [BusinessReportInterval](#businessreportinterval)
  - [BusinessReportStatus](#businessreportstatus)
  - [CommsProtocol](#commsprotocol)
  - [ConferenceProviderType](#conferenceprovidertype)
  - [ConnectionStatus](#connectionstatus)
  - [DeviceEventType](#deviceeventtype)
  - [DeviceStatus](#devicestatus)
  - [DeviceStatusDetailCode](#devicestatusdetailcode)
  - [DeviceUsageType](#deviceusagetype)
  - [DistanceUnit](#distanceunit)
  - [EnablementType](#enablementtype)
  - [EnablementTypeFilter](#enablementtypefilter)
  - [EndOfMeetingReminderType](#endofmeetingremindertype)
  - [EnrollmentStatus](#enrollmentstatus)
  - [Feature](#feature)
  - [ListBusinessReportSchedulesPaginatorName](#listbusinessreportschedulespaginatorname)
  - [ListConferenceProvidersPaginatorName](#listconferenceproviderspaginatorname)
  - [ListDeviceEventsPaginatorName](#listdeviceeventspaginatorname)
  - [ListSkillsPaginatorName](#listskillspaginatorname)
  - [ListSkillsStoreCategoriesPaginatorName](#listskillsstorecategoriespaginatorname)
  - [ListSkillsStoreSkillsByCategoryPaginatorName](#listskillsstoreskillsbycategorypaginatorname)
  - [ListSmartHomeAppliancesPaginatorName](#listsmarthomeappliancespaginatorname)
  - [ListTagsPaginatorName](#listtagspaginatorname)
  - [Locale](#locale)
  - [NetworkEapMethod](#networkeapmethod)
  - [NetworkSecurityType](#networksecuritytype)
  - [PhoneNumberType](#phonenumbertype)
  - [RequirePin](#requirepin)
  - [SearchDevicesPaginatorName](#searchdevicespaginatorname)
  - [SearchProfilesPaginatorName](#searchprofilespaginatorname)
  - [SearchRoomsPaginatorName](#searchroomspaginatorname)
  - [SearchSkillGroupsPaginatorName](#searchskillgroupspaginatorname)
  - [SearchUsersPaginatorName](#searchuserspaginatorname)
  - [SipType](#siptype)
  - [SkillType](#skilltype)
  - [SkillTypeFilter](#skilltypefilter)
  - [SortValue](#sortvalue)
  - [TemperatureUnit](#temperatureunit)
  - [WakeWord](#wakeword)

## BusinessReportFailureCode

```python
from mypy_boto3_alexaforbusiness.literals import BusinessReportFailureCode
```

Values:

- `ACCESS_DENIED`
- `INTERNAL_FAILURE`
- `NO_SUCH_BUCKET`

## BusinessReportFormat

```python
from mypy_boto3_alexaforbusiness.literals import BusinessReportFormat
```

Values:

- `CSV`
- `CSV_ZIP`

## BusinessReportInterval

```python
from mypy_boto3_alexaforbusiness.literals import BusinessReportInterval
```

Values:

- `ONE_DAY`
- `ONE_WEEK`
- `THIRTY_DAYS`

## BusinessReportStatus

```python
from mypy_boto3_alexaforbusiness.literals import BusinessReportStatus
```

Values:

- `FAILED`
- `RUNNING`
- `SUCCEEDED`

## CommsProtocol

```python
from mypy_boto3_alexaforbusiness.literals import CommsProtocol
```

Values:

- `H323`
- `SIP`
- `SIPS`

## ConferenceProviderType

```python
from mypy_boto3_alexaforbusiness.literals import ConferenceProviderType
```

Values:

- `BLUEJEANS`
- `CHIME`
- `CUSTOM`
- `FUZE`
- `GOOGLE_HANGOUTS`
- `POLYCOM`
- `RINGCENTRAL`
- `SKYPE_FOR_BUSINESS`
- `WEBEX`
- `ZOOM`

## ConnectionStatus

```python
from mypy_boto3_alexaforbusiness.literals import ConnectionStatus
```

Values:

- `OFFLINE`
- `ONLINE`

## DeviceEventType

```python
from mypy_boto3_alexaforbusiness.literals import DeviceEventType
```

Values:

- `CONNECTION_STATUS`
- `DEVICE_STATUS`

## DeviceStatus

```python
from mypy_boto3_alexaforbusiness.literals import DeviceStatus
```

Values:

- `DEREGISTERED`
- `FAILED`
- `PENDING`
- `READY`
- `WAS_OFFLINE`

## DeviceStatusDetailCode

```python
from mypy_boto3_alexaforbusiness.literals import DeviceStatusDetailCode
```

Values:

- `ASSOCIATION_REJECTION`
- `AUTHENTICATION_FAILURE`
- `CERTIFICATE_AUTHORITY_ACCESS_DENIED`
- `CERTIFICATE_ISSUING_LIMIT_EXCEEDED`
- `CREDENTIALS_ACCESS_FAILURE`
- `DEVICE_SOFTWARE_UPDATE_NEEDED`
- `DEVICE_WAS_OFFLINE`
- `DHCP_FAILURE`
- `DNS_FAILURE`
- `INTERNET_UNAVAILABLE`
- `INVALID_CERTIFICATE_AUTHORITY`
- `INVALID_PASSWORD_STATE`
- `NETWORK_PROFILE_NOT_FOUND`
- `PASSWORD_MANAGER_ACCESS_DENIED`
- `PASSWORD_NOT_FOUND`
- `TLS_VERSION_MISMATCH`
- `UNKNOWN_FAILURE`

## DeviceUsageType

```python
from mypy_boto3_alexaforbusiness.literals import DeviceUsageType
```

Values:

- `VOICE`

## DistanceUnit

```python
from mypy_boto3_alexaforbusiness.literals import DistanceUnit
```

Values:

- `IMPERIAL`
- `METRIC`

## EnablementType

```python
from mypy_boto3_alexaforbusiness.literals import EnablementType
```

Values:

- `ENABLED`
- `PENDING`

## EnablementTypeFilter

```python
from mypy_boto3_alexaforbusiness.literals import EnablementTypeFilter
```

Values:

- `ENABLED`
- `PENDING`

## EndOfMeetingReminderType

```python
from mypy_boto3_alexaforbusiness.literals import EndOfMeetingReminderType
```

Values:

- `ANNOUNCEMENT_TIME_CHECK`
- `ANNOUNCEMENT_VARIABLE_TIME_LEFT`
- `CHIME`
- `KNOCK`

## EnrollmentStatus

```python
from mypy_boto3_alexaforbusiness.literals import EnrollmentStatus
```

Values:

- `DEREGISTERING`
- `DISASSOCIATING`
- `INITIALIZED`
- `PENDING`
- `REGISTERED`

## Feature

```python
from mypy_boto3_alexaforbusiness.literals import Feature
```

Values:

- `ALL`
- `BLUETOOTH`
- `LISTS`
- `NETWORK_PROFILE`
- `NOTIFICATIONS`
- `SETTINGS`
- `SKILLS`
- `VOLUME`

## ListBusinessReportSchedulesPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListBusinessReportSchedulesPaginatorName
```

Values:

- `list_business_report_schedules`

## ListConferenceProvidersPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListConferenceProvidersPaginatorName
```

Values:

- `list_conference_providers`

## ListDeviceEventsPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListDeviceEventsPaginatorName
```

Values:

- `list_device_events`

## ListSkillsPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListSkillsPaginatorName
```

Values:

- `list_skills`

## ListSkillsStoreCategoriesPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListSkillsStoreCategoriesPaginatorName
```

Values:

- `list_skills_store_categories`

## ListSkillsStoreSkillsByCategoryPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListSkillsStoreSkillsByCategoryPaginatorName
```

Values:

- `list_skills_store_skills_by_category`

## ListSmartHomeAppliancesPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListSmartHomeAppliancesPaginatorName
```

Values:

- `list_smart_home_appliances`

## ListTagsPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import ListTagsPaginatorName
```

Values:

- `list_tags`

## Locale

```python
from mypy_boto3_alexaforbusiness.literals import Locale
```

Values:

- `en-US`

## NetworkEapMethod

```python
from mypy_boto3_alexaforbusiness.literals import NetworkEapMethod
```

Values:

- `EAP_TLS`

## NetworkSecurityType

```python
from mypy_boto3_alexaforbusiness.literals import NetworkSecurityType
```

Values:

- `OPEN`
- `WEP`
- `WPA2_ENTERPRISE`
- `WPA2_PSK`
- `WPA_PSK`

## PhoneNumberType

```python
from mypy_boto3_alexaforbusiness.literals import PhoneNumberType
```

Values:

- `HOME`
- `MOBILE`
- `WORK`

## RequirePin

```python
from mypy_boto3_alexaforbusiness.literals import RequirePin
```

Values:

- `NO`
- `OPTIONAL`
- `YES`

## SearchDevicesPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import SearchDevicesPaginatorName
```

Values:

- `search_devices`

## SearchProfilesPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import SearchProfilesPaginatorName
```

Values:

- `search_profiles`

## SearchRoomsPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import SearchRoomsPaginatorName
```

Values:

- `search_rooms`

## SearchSkillGroupsPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import SearchSkillGroupsPaginatorName
```

Values:

- `search_skill_groups`

## SearchUsersPaginatorName

```python
from mypy_boto3_alexaforbusiness.literals import SearchUsersPaginatorName
```

Values:

- `search_users`

## SipType

```python
from mypy_boto3_alexaforbusiness.literals import SipType
```

Values:

- `WORK`

## SkillType

```python
from mypy_boto3_alexaforbusiness.literals import SkillType
```

Values:

- `PRIVATE`
- `PUBLIC`

## SkillTypeFilter

```python
from mypy_boto3_alexaforbusiness.literals import SkillTypeFilter
```

Values:

- `ALL`
- `PRIVATE`
- `PUBLIC`

## SortValue

```python
from mypy_boto3_alexaforbusiness.literals import SortValue
```

Values:

- `ASC`
- `DESC`

## TemperatureUnit

```python
from mypy_boto3_alexaforbusiness.literals import TemperatureUnit
```

Values:

- `CELSIUS`
- `FAHRENHEIT`

## WakeWord

```python
from mypy_boto3_alexaforbusiness.literals import WakeWord
```

Values:

- `ALEXA`
- `AMAZON`
- `COMPUTER`
- `ECHO`
