# Literals for boto3 Chime module

> [Index](../index.md) > [Chime](./index.md) > Literals

Auto-generated documentation for [Chime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime)
type annotations stubs module [mypy_boto3_chime](https://pypi.org/project/mypy-boto3-chime/).

- [Literals for boto3 Chime module](#literals-for-boto3-chime-module)
  - [AccountType](#accounttype)
  - [AppInstanceDataType](#appinstancedatatype)
  - [BotType](#bottype)
  - [CallingNameStatus](#callingnamestatus)
  - [Capability](#capability)
  - [ChannelMembershipType](#channelmembershiptype)
  - [ChannelMessagePersistenceType](#channelmessagepersistencetype)
  - [ChannelMessageType](#channelmessagetype)
  - [ChannelMode](#channelmode)
  - [ChannelPrivacy](#channelprivacy)
  - [EmailStatus](#emailstatus)
  - [ErrorCode](#errorcode)
  - [GeoMatchLevel](#geomatchlevel)
  - [InviteStatus](#invitestatus)
  - [License](#license)
  - [ListAccountsPaginatorName](#listaccountspaginatorname)
  - [ListUsersPaginatorName](#listuserspaginatorname)
  - [MemberType](#membertype)
  - [NotificationTarget](#notificationtarget)
  - [NumberSelectionBehavior](#numberselectionbehavior)
  - [OrderedPhoneNumberStatus](#orderedphonenumberstatus)
  - [OriginationRouteProtocol](#originationrouteprotocol)
  - [PhoneNumberAssociationName](#phonenumberassociationname)
  - [PhoneNumberOrderStatus](#phonenumberorderstatus)
  - [PhoneNumberProductType](#phonenumberproducttype)
  - [PhoneNumberStatus](#phonenumberstatus)
  - [PhoneNumberType](#phonenumbertype)
  - [ProxySessionStatus](#proxysessionstatus)
  - [RegistrationStatus](#registrationstatus)
  - [RoomMembershipRole](#roommembershiprole)
  - [SipRuleTriggerType](#sipruletriggertype)
  - [SortOrder](#sortorder)
  - [UserType](#usertype)
  - [VoiceConnectorAwsRegion](#voiceconnectorawsregion)

## AccountType

```python
from mypy_boto3_chime.literals import AccountType
```

Values:

- `EnterpriseDirectory`
- `EnterpriseLWA`
- `EnterpriseOIDC`
- `Team`

## AppInstanceDataType

```python
from mypy_boto3_chime.literals import AppInstanceDataType
```

Values:

- `Channel`
- `ChannelMessage`

## BotType

```python
from mypy_boto3_chime.literals import BotType
```

Values:

- `ChatBot`

## CallingNameStatus

```python
from mypy_boto3_chime.literals import CallingNameStatus
```

Values:

- `Unassigned`
- `UpdateFailed`
- `UpdateInProgress`
- `UpdateSucceeded`

## Capability

```python
from mypy_boto3_chime.literals import Capability
```

Values:

- `SMS`
- `Voice`

## ChannelMembershipType

```python
from mypy_boto3_chime.literals import ChannelMembershipType
```

Values:

- `DEFAULT`
- `HIDDEN`

## ChannelMessagePersistenceType

```python
from mypy_boto3_chime.literals import ChannelMessagePersistenceType
```

Values:

- `NON_PERSISTENT`
- `PERSISTENT`

## ChannelMessageType

```python
from mypy_boto3_chime.literals import ChannelMessageType
```

Values:

- `CONTROL`
- `STANDARD`

## ChannelMode

```python
from mypy_boto3_chime.literals import ChannelMode
```

Values:

- `RESTRICTED`
- `UNRESTRICTED`

## ChannelPrivacy

```python
from mypy_boto3_chime.literals import ChannelPrivacy
```

Values:

- `PRIVATE`
- `PUBLIC`

## EmailStatus

```python
from mypy_boto3_chime.literals import EmailStatus
```

Values:

- `Failed`
- `NotSent`
- `Sent`

## ErrorCode

```python
from mypy_boto3_chime.literals import ErrorCode
```

Values:

- `AccessDenied`
- `BadRequest`
- `Conflict`
- `Forbidden`
- `NotFound`
- `PhoneNumberAssociationsExist`
- `PreconditionFailed`
- `ResourceLimitExceeded`
- `ServiceFailure`
- `ServiceUnavailable`
- `Throttled`
- `Throttling`
- `Unauthorized`
- `Unprocessable`
- `VoiceConnectorGroupAssociationsExist`

## GeoMatchLevel

```python
from mypy_boto3_chime.literals import GeoMatchLevel
```

Values:

- `AreaCode`
- `Country`

## InviteStatus

```python
from mypy_boto3_chime.literals import InviteStatus
```

Values:

- `Accepted`
- `Failed`
- `Pending`

## License

```python
from mypy_boto3_chime.literals import License
```

Values:

- `Basic`
- `Plus`
- `Pro`
- `ProTrial`

## ListAccountsPaginatorName

```python
from mypy_boto3_chime.literals import ListAccountsPaginatorName
```

Values:

- `list_accounts`

## ListUsersPaginatorName

```python
from mypy_boto3_chime.literals import ListUsersPaginatorName
```

Values:

- `list_users`

## MemberType

```python
from mypy_boto3_chime.literals import MemberType
```

Values:

- `Bot`
- `User`
- `Webhook`

## NotificationTarget

```python
from mypy_boto3_chime.literals import NotificationTarget
```

Values:

- `EventBridge`
- `SNS`
- `SQS`

## NumberSelectionBehavior

```python
from mypy_boto3_chime.literals import NumberSelectionBehavior
```

Values:

- `AvoidSticky`
- `PreferSticky`

## OrderedPhoneNumberStatus

```python
from mypy_boto3_chime.literals import OrderedPhoneNumberStatus
```

Values:

- `Acquired`
- `Failed`
- `Processing`

## OriginationRouteProtocol

```python
from mypy_boto3_chime.literals import OriginationRouteProtocol
```

Values:

- `TCP`
- `UDP`

## PhoneNumberAssociationName

```python
from mypy_boto3_chime.literals import PhoneNumberAssociationName
```

Values:

- `AccountId`
- `SipRuleId`
- `UserId`
- `VoiceConnectorGroupId`
- `VoiceConnectorId`

## PhoneNumberOrderStatus

```python
from mypy_boto3_chime.literals import PhoneNumberOrderStatus
```

Values:

- `Failed`
- `Partial`
- `Processing`
- `Successful`

## PhoneNumberProductType

```python
from mypy_boto3_chime.literals import PhoneNumberProductType
```

Values:

- `BusinessCalling`
- `VoiceConnector`

## PhoneNumberStatus

```python
from mypy_boto3_chime.literals import PhoneNumberStatus
```

Values:

- `AcquireFailed`
- `AcquireInProgress`
- `Assigned`
- `DeleteFailed`
- `DeleteInProgress`
- `ReleaseFailed`
- `ReleaseInProgress`
- `Unassigned`

## PhoneNumberType

```python
from mypy_boto3_chime.literals import PhoneNumberType
```

Values:

- `Local`
- `TollFree`

## ProxySessionStatus

```python
from mypy_boto3_chime.literals import ProxySessionStatus
```

Values:

- `Closed`
- `InProgress`
- `Open`

## RegistrationStatus

```python
from mypy_boto3_chime.literals import RegistrationStatus
```

Values:

- `Registered`
- `Suspended`
- `Unregistered`

## RoomMembershipRole

```python
from mypy_boto3_chime.literals import RoomMembershipRole
```

Values:

- `Administrator`
- `Member`

## SipRuleTriggerType

```python
from mypy_boto3_chime.literals import SipRuleTriggerType
```

Values:

- `RequestUriHostname`
- `ToPhoneNumber`

## SortOrder

```python
from mypy_boto3_chime.literals import SortOrder
```

Values:

- `ASCENDING`
- `DESCENDING`

## UserType

```python
from mypy_boto3_chime.literals import UserType
```

Values:

- `PrivateUser`
- `SharedDevice`

## VoiceConnectorAwsRegion

```python
from mypy_boto3_chime.literals import VoiceConnectorAwsRegion
```

Values:

- `us-east-1`
- `us-west-2`
