# Structures for boto3 Chime module

> [Index](../index.md) > [Chime](./index.md) > Structures

Auto-generated documentation for [Chime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime)
type annotations stubs module [mypy_boto3_chime](https://pypi.org/project/mypy-boto3-chime/).

- [Structures for boto3 Chime module](#structures-for-boto3-chime-module)
  - [AccountSettingsTypeDef](#accountsettingstypedef)
  - [AccountTypeDef](#accounttypedef)
  - [AlexaForBusinessMetadataTypeDef](#alexaforbusinessmetadatatypedef)
  - [AppInstanceAdminSummaryTypeDef](#appinstanceadminsummarytypedef)
  - [AppInstanceAdminTypeDef](#appinstanceadmintypedef)
  - [AppInstanceRetentionSettingsTypeDef](#appinstanceretentionsettingstypedef)
  - [AppInstanceStreamingConfigurationTypeDef](#appinstancestreamingconfigurationtypedef)
  - [AppInstanceSummaryTypeDef](#appinstancesummarytypedef)
  - [AppInstanceTypeDef](#appinstancetypedef)
  - [AppInstanceUserMembershipSummaryTypeDef](#appinstanceusermembershipsummarytypedef)
  - [AppInstanceUserSummaryTypeDef](#appinstanceusersummarytypedef)
  - [AppInstanceUserTypeDef](#appinstanceusertypedef)
  - [AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef](#associatephonenumberswithvoiceconnectorgroupresponsetypedef)
  - [AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef](#associatephonenumberswithvoiceconnectorresponsetypedef)
  - [AttendeeTypeDef](#attendeetypedef)
  - [BatchCreateAttendeeResponseTypeDef](#batchcreateattendeeresponsetypedef)
  - [BatchCreateRoomMembershipResponseTypeDef](#batchcreateroommembershipresponsetypedef)
  - [BatchDeletePhoneNumberResponseTypeDef](#batchdeletephonenumberresponsetypedef)
  - [BatchSuspendUserResponseTypeDef](#batchsuspenduserresponsetypedef)
  - [BatchUnsuspendUserResponseTypeDef](#batchunsuspenduserresponsetypedef)
  - [BatchUpdatePhoneNumberResponseTypeDef](#batchupdatephonenumberresponsetypedef)
  - [BatchUpdateUserResponseTypeDef](#batchupdateuserresponsetypedef)
  - [BotTypeDef](#bottypedef)
  - [BusinessCallingSettingsTypeDef](#businesscallingsettingstypedef)
  - [ChannelBanSummaryTypeDef](#channelbansummarytypedef)
  - [ChannelBanTypeDef](#channelbantypedef)
  - [ChannelMembershipForAppInstanceUserSummaryTypeDef](#channelmembershipforappinstanceusersummarytypedef)
  - [ChannelMembershipSummaryTypeDef](#channelmembershipsummarytypedef)
  - [ChannelMembershipTypeDef](#channelmembershiptypedef)
  - [ChannelMessageSummaryTypeDef](#channelmessagesummarytypedef)
  - [ChannelMessageTypeDef](#channelmessagetypedef)
  - [ChannelModeratedByAppInstanceUserSummaryTypeDef](#channelmoderatedbyappinstanceusersummarytypedef)
  - [ChannelModeratorSummaryTypeDef](#channelmoderatorsummarytypedef)
  - [ChannelModeratorTypeDef](#channelmoderatortypedef)
  - [ChannelRetentionSettingsTypeDef](#channelretentionsettingstypedef)
  - [ChannelSummaryTypeDef](#channelsummarytypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [ConversationRetentionSettingsTypeDef](#conversationretentionsettingstypedef)
  - [CreateAccountResponseTypeDef](#createaccountresponsetypedef)
  - [CreateAppInstanceAdminResponseTypeDef](#createappinstanceadminresponsetypedef)
  - [CreateAppInstanceResponseTypeDef](#createappinstanceresponsetypedef)
  - [CreateAppInstanceUserResponseTypeDef](#createappinstanceuserresponsetypedef)
  - [CreateAttendeeErrorTypeDef](#createattendeeerrortypedef)
  - [CreateAttendeeRequestItemTypeDef](#createattendeerequestitemtypedef)
  - [CreateAttendeeResponseTypeDef](#createattendeeresponsetypedef)
  - [CreateBotResponseTypeDef](#createbotresponsetypedef)
  - [CreateChannelBanResponseTypeDef](#createchannelbanresponsetypedef)
  - [CreateChannelMembershipResponseTypeDef](#createchannelmembershipresponsetypedef)
  - [CreateChannelModeratorResponseTypeDef](#createchannelmoderatorresponsetypedef)
  - [CreateChannelResponseTypeDef](#createchannelresponsetypedef)
  - [CreateMeetingDialOutResponseTypeDef](#createmeetingdialoutresponsetypedef)
  - [CreateMeetingResponseTypeDef](#createmeetingresponsetypedef)
  - [CreateMeetingWithAttendeesResponseTypeDef](#createmeetingwithattendeesresponsetypedef)
  - [CreatePhoneNumberOrderResponseTypeDef](#createphonenumberorderresponsetypedef)
  - [CreateProxySessionResponseTypeDef](#createproxysessionresponsetypedef)
  - [CreateRoomMembershipResponseTypeDef](#createroommembershipresponsetypedef)
  - [CreateRoomResponseTypeDef](#createroomresponsetypedef)
  - [CreateSipMediaApplicationCallResponseTypeDef](#createsipmediaapplicationcallresponsetypedef)
  - [CreateSipMediaApplicationResponseTypeDef](#createsipmediaapplicationresponsetypedef)
  - [CreateSipRuleResponseTypeDef](#createsipruleresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [CreateVoiceConnectorGroupResponseTypeDef](#createvoiceconnectorgroupresponsetypedef)
  - [CreateVoiceConnectorResponseTypeDef](#createvoiceconnectorresponsetypedef)
  - [CredentialTypeDef](#credentialtypedef)
  - [DNISEmergencyCallingConfigurationTypeDef](#dnisemergencycallingconfigurationtypedef)
  - [DescribeAppInstanceAdminResponseTypeDef](#describeappinstanceadminresponsetypedef)
  - [DescribeAppInstanceResponseTypeDef](#describeappinstanceresponsetypedef)
  - [DescribeAppInstanceUserResponseTypeDef](#describeappinstanceuserresponsetypedef)
  - [DescribeChannelBanResponseTypeDef](#describechannelbanresponsetypedef)
  - [DescribeChannelMembershipForAppInstanceUserResponseTypeDef](#describechannelmembershipforappinstanceuserresponsetypedef)
  - [DescribeChannelMembershipResponseTypeDef](#describechannelmembershipresponsetypedef)
  - [DescribeChannelModeratedByAppInstanceUserResponseTypeDef](#describechannelmoderatedbyappinstanceuserresponsetypedef)
  - [DescribeChannelModeratorResponseTypeDef](#describechannelmoderatorresponsetypedef)
  - [DescribeChannelResponseTypeDef](#describechannelresponsetypedef)
  - [DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef](#disassociatephonenumbersfromvoiceconnectorgroupresponsetypedef)
  - [DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef](#disassociatephonenumbersfromvoiceconnectorresponsetypedef)
  - [EmergencyCallingConfigurationTypeDef](#emergencycallingconfigurationtypedef)
  - [EventsConfigurationTypeDef](#eventsconfigurationtypedef)
  - [GeoMatchParamsTypeDef](#geomatchparamstypedef)
  - [GetAccountResponseTypeDef](#getaccountresponsetypedef)
  - [GetAccountSettingsResponseTypeDef](#getaccountsettingsresponsetypedef)
  - [GetAppInstanceRetentionSettingsResponseTypeDef](#getappinstanceretentionsettingsresponsetypedef)
  - [GetAppInstanceStreamingConfigurationsResponseTypeDef](#getappinstancestreamingconfigurationsresponsetypedef)
  - [GetAttendeeResponseTypeDef](#getattendeeresponsetypedef)
  - [GetBotResponseTypeDef](#getbotresponsetypedef)
  - [GetChannelMessageResponseTypeDef](#getchannelmessageresponsetypedef)
  - [GetEventsConfigurationResponseTypeDef](#geteventsconfigurationresponsetypedef)
  - [GetGlobalSettingsResponseTypeDef](#getglobalsettingsresponsetypedef)
  - [GetMeetingResponseTypeDef](#getmeetingresponsetypedef)
  - [GetMessagingSessionEndpointResponseTypeDef](#getmessagingsessionendpointresponsetypedef)
  - [GetPhoneNumberOrderResponseTypeDef](#getphonenumberorderresponsetypedef)
  - [GetPhoneNumberResponseTypeDef](#getphonenumberresponsetypedef)
  - [GetPhoneNumberSettingsResponseTypeDef](#getphonenumbersettingsresponsetypedef)
  - [GetProxySessionResponseTypeDef](#getproxysessionresponsetypedef)
  - [GetRetentionSettingsResponseTypeDef](#getretentionsettingsresponsetypedef)
  - [GetRoomResponseTypeDef](#getroomresponsetypedef)
  - [GetSipMediaApplicationLoggingConfigurationResponseTypeDef](#getsipmediaapplicationloggingconfigurationresponsetypedef)
  - [GetSipMediaApplicationResponseTypeDef](#getsipmediaapplicationresponsetypedef)
  - [GetSipRuleResponseTypeDef](#getsipruleresponsetypedef)
  - [GetUserResponseTypeDef](#getuserresponsetypedef)
  - [GetUserSettingsResponseTypeDef](#getusersettingsresponsetypedef)
  - [GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef](#getvoiceconnectoremergencycallingconfigurationresponsetypedef)
  - [GetVoiceConnectorGroupResponseTypeDef](#getvoiceconnectorgroupresponsetypedef)
  - [GetVoiceConnectorLoggingConfigurationResponseTypeDef](#getvoiceconnectorloggingconfigurationresponsetypedef)
  - [GetVoiceConnectorOriginationResponseTypeDef](#getvoiceconnectororiginationresponsetypedef)
  - [GetVoiceConnectorProxyResponseTypeDef](#getvoiceconnectorproxyresponsetypedef)
  - [GetVoiceConnectorResponseTypeDef](#getvoiceconnectorresponsetypedef)
  - [GetVoiceConnectorStreamingConfigurationResponseTypeDef](#getvoiceconnectorstreamingconfigurationresponsetypedef)
  - [GetVoiceConnectorTerminationHealthResponseTypeDef](#getvoiceconnectorterminationhealthresponsetypedef)
  - [GetVoiceConnectorTerminationResponseTypeDef](#getvoiceconnectorterminationresponsetypedef)
  - [IdentityTypeDef](#identitytypedef)
  - [InviteTypeDef](#invitetypedef)
  - [InviteUsersResponseTypeDef](#inviteusersresponsetypedef)
  - [ListAccountsResponseTypeDef](#listaccountsresponsetypedef)
  - [ListAppInstanceAdminsResponseTypeDef](#listappinstanceadminsresponsetypedef)
  - [ListAppInstanceUsersResponseTypeDef](#listappinstanceusersresponsetypedef)
  - [ListAppInstancesResponseTypeDef](#listappinstancesresponsetypedef)
  - [ListAttendeeTagsResponseTypeDef](#listattendeetagsresponsetypedef)
  - [ListAttendeesResponseTypeDef](#listattendeesresponsetypedef)
  - [ListBotsResponseTypeDef](#listbotsresponsetypedef)
  - [ListChannelBansResponseTypeDef](#listchannelbansresponsetypedef)
  - [ListChannelMembershipsForAppInstanceUserResponseTypeDef](#listchannelmembershipsforappinstanceuserresponsetypedef)
  - [ListChannelMembershipsResponseTypeDef](#listchannelmembershipsresponsetypedef)
  - [ListChannelMessagesResponseTypeDef](#listchannelmessagesresponsetypedef)
  - [ListChannelModeratorsResponseTypeDef](#listchannelmoderatorsresponsetypedef)
  - [ListChannelsModeratedByAppInstanceUserResponseTypeDef](#listchannelsmoderatedbyappinstanceuserresponsetypedef)
  - [ListChannelsResponseTypeDef](#listchannelsresponsetypedef)
  - [ListMeetingTagsResponseTypeDef](#listmeetingtagsresponsetypedef)
  - [ListMeetingsResponseTypeDef](#listmeetingsresponsetypedef)
  - [ListPhoneNumberOrdersResponseTypeDef](#listphonenumberordersresponsetypedef)
  - [ListPhoneNumbersResponseTypeDef](#listphonenumbersresponsetypedef)
  - [ListProxySessionsResponseTypeDef](#listproxysessionsresponsetypedef)
  - [ListRoomMembershipsResponseTypeDef](#listroommembershipsresponsetypedef)
  - [ListRoomsResponseTypeDef](#listroomsresponsetypedef)
  - [ListSipMediaApplicationsResponseTypeDef](#listsipmediaapplicationsresponsetypedef)
  - [ListSipRulesResponseTypeDef](#listsiprulesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [ListVoiceConnectorGroupsResponseTypeDef](#listvoiceconnectorgroupsresponsetypedef)
  - [ListVoiceConnectorTerminationCredentialsResponseTypeDef](#listvoiceconnectorterminationcredentialsresponsetypedef)
  - [ListVoiceConnectorsResponseTypeDef](#listvoiceconnectorsresponsetypedef)
  - [LoggingConfigurationTypeDef](#loggingconfigurationtypedef)
  - [MediaPlacementTypeDef](#mediaplacementtypedef)
  - [MeetingNotificationConfigurationTypeDef](#meetingnotificationconfigurationtypedef)
  - [MeetingTypeDef](#meetingtypedef)
  - [MemberErrorTypeDef](#membererrortypedef)
  - [MemberTypeDef](#membertypedef)
  - [MembershipItemTypeDef](#membershipitemtypedef)
  - [MessagingSessionEndpointTypeDef](#messagingsessionendpointtypedef)
  - [OrderedPhoneNumberTypeDef](#orderedphonenumbertypedef)
  - [OriginationRouteTypeDef](#originationroutetypedef)
  - [OriginationTypeDef](#originationtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParticipantTypeDef](#participanttypedef)
  - [PhoneNumberAssociationTypeDef](#phonenumberassociationtypedef)
  - [PhoneNumberCapabilitiesTypeDef](#phonenumbercapabilitiestypedef)
  - [PhoneNumberErrorTypeDef](#phonenumbererrortypedef)
  - [PhoneNumberOrderTypeDef](#phonenumberordertypedef)
  - [PhoneNumberTypeDef](#phonenumbertypedef)
  - [ProxySessionTypeDef](#proxysessiontypedef)
  - [ProxyTypeDef](#proxytypedef)
  - [PutAppInstanceRetentionSettingsResponseTypeDef](#putappinstanceretentionsettingsresponsetypedef)
  - [PutAppInstanceStreamingConfigurationsResponseTypeDef](#putappinstancestreamingconfigurationsresponsetypedef)
  - [PutEventsConfigurationResponseTypeDef](#puteventsconfigurationresponsetypedef)
  - [PutRetentionSettingsResponseTypeDef](#putretentionsettingsresponsetypedef)
  - [PutSipMediaApplicationLoggingConfigurationResponseTypeDef](#putsipmediaapplicationloggingconfigurationresponsetypedef)
  - [PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef](#putvoiceconnectoremergencycallingconfigurationresponsetypedef)
  - [PutVoiceConnectorLoggingConfigurationResponseTypeDef](#putvoiceconnectorloggingconfigurationresponsetypedef)
  - [PutVoiceConnectorOriginationResponseTypeDef](#putvoiceconnectororiginationresponsetypedef)
  - [PutVoiceConnectorProxyResponseTypeDef](#putvoiceconnectorproxyresponsetypedef)
  - [PutVoiceConnectorStreamingConfigurationResponseTypeDef](#putvoiceconnectorstreamingconfigurationresponsetypedef)
  - [PutVoiceConnectorTerminationResponseTypeDef](#putvoiceconnectorterminationresponsetypedef)
  - [RedactChannelMessageResponseTypeDef](#redactchannelmessageresponsetypedef)
  - [RegenerateSecurityTokenResponseTypeDef](#regeneratesecuritytokenresponsetypedef)
  - [ResetPersonalPINResponseTypeDef](#resetpersonalpinresponsetypedef)
  - [RestorePhoneNumberResponseTypeDef](#restorephonenumberresponsetypedef)
  - [RetentionSettingsTypeDef](#retentionsettingstypedef)
  - [RoomMembershipTypeDef](#roommembershiptypedef)
  - [RoomRetentionSettingsTypeDef](#roomretentionsettingstypedef)
  - [RoomTypeDef](#roomtypedef)
  - [SearchAvailablePhoneNumbersResponseTypeDef](#searchavailablephonenumbersresponsetypedef)
  - [SendChannelMessageResponseTypeDef](#sendchannelmessageresponsetypedef)
  - [SigninDelegateGroupTypeDef](#signindelegategrouptypedef)
  - [SipMediaApplicationCallTypeDef](#sipmediaapplicationcalltypedef)
  - [SipMediaApplicationEndpointTypeDef](#sipmediaapplicationendpointtypedef)
  - [SipMediaApplicationLoggingConfigurationTypeDef](#sipmediaapplicationloggingconfigurationtypedef)
  - [SipMediaApplicationTypeDef](#sipmediaapplicationtypedef)
  - [SipRuleTargetApplicationTypeDef](#sipruletargetapplicationtypedef)
  - [SipRuleTypeDef](#sipruletypedef)
  - [StreamingConfigurationTypeDef](#streamingconfigurationtypedef)
  - [StreamingNotificationTargetTypeDef](#streamingnotificationtargettypedef)
  - [TagTypeDef](#tagtypedef)
  - [TelephonySettingsTypeDef](#telephonysettingstypedef)
  - [TerminationHealthTypeDef](#terminationhealthtypedef)
  - [TerminationTypeDef](#terminationtypedef)
  - [UpdateAccountResponseTypeDef](#updateaccountresponsetypedef)
  - [UpdateAppInstanceResponseTypeDef](#updateappinstanceresponsetypedef)
  - [UpdateAppInstanceUserResponseTypeDef](#updateappinstanceuserresponsetypedef)
  - [UpdateBotResponseTypeDef](#updatebotresponsetypedef)
  - [UpdateChannelMessageResponseTypeDef](#updatechannelmessageresponsetypedef)
  - [UpdateChannelReadMarkerResponseTypeDef](#updatechannelreadmarkerresponsetypedef)
  - [UpdateChannelResponseTypeDef](#updatechannelresponsetypedef)
  - [UpdatePhoneNumberRequestItemTypeDef](#updatephonenumberrequestitemtypedef)
  - [UpdatePhoneNumberResponseTypeDef](#updatephonenumberresponsetypedef)
  - [UpdateProxySessionResponseTypeDef](#updateproxysessionresponsetypedef)
  - [UpdateRoomMembershipResponseTypeDef](#updateroommembershipresponsetypedef)
  - [UpdateRoomResponseTypeDef](#updateroomresponsetypedef)
  - [UpdateSipMediaApplicationResponseTypeDef](#updatesipmediaapplicationresponsetypedef)
  - [UpdateSipRuleResponseTypeDef](#updatesipruleresponsetypedef)
  - [UpdateUserRequestItemTypeDef](#updateuserrequestitemtypedef)
  - [UpdateUserResponseTypeDef](#updateuserresponsetypedef)
  - [UpdateVoiceConnectorGroupResponseTypeDef](#updatevoiceconnectorgroupresponsetypedef)
  - [UpdateVoiceConnectorResponseTypeDef](#updatevoiceconnectorresponsetypedef)
  - [UserErrorTypeDef](#usererrortypedef)
  - [UserSettingsTypeDef](#usersettingstypedef)
  - [UserTypeDef](#usertypedef)
  - [VoiceConnectorGroupTypeDef](#voiceconnectorgrouptypedef)
  - [VoiceConnectorItemTypeDef](#voiceconnectoritemtypedef)
  - [VoiceConnectorSettingsTypeDef](#voiceconnectorsettingstypedef)
  - [VoiceConnectorTypeDef](#voiceconnectortypedef)

## AccountSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import AccountSettingsTypeDef
```




Optional fields:
- `DisableRemoteControl`: `bool`
- `EnableDialOut`: `bool`


## AccountTypeDef

```python
from mypy_boto3_chime.type_defs import AccountTypeDef
```


Required fields:
- `AwsAccountId`: `str`
- `AccountId`: `str`
- `Name`: `str`



Optional fields:
- `AccountType`: `AccountType`
- `CreatedTimestamp`: `datetime`
- `DefaultLicense`: `License`
- `SupportedLicenses`: `List[License]`
- `SigninDelegateGroups`: `List["SigninDelegateGroupTypeDef"]`


## AlexaForBusinessMetadataTypeDef

```python
from mypy_boto3_chime.type_defs import AlexaForBusinessMetadataTypeDef
```




Optional fields:
- `IsAlexaForBusinessEnabled`: `bool`
- `AlexaForBusinessRoomArn`: `str`


## AppInstanceAdminSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceAdminSummaryTypeDef
```




Optional fields:
- `Admin`: `"IdentityTypeDef"`


## AppInstanceAdminTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceAdminTypeDef
```




Optional fields:
- `Admin`: `"IdentityTypeDef"`
- `AppInstanceArn`: `str`
- `CreatedTimestamp`: `datetime`


## AppInstanceRetentionSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceRetentionSettingsTypeDef
```




Optional fields:
- `ChannelRetentionSettings`: `"ChannelRetentionSettingsTypeDef"`


## AppInstanceStreamingConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceStreamingConfigurationTypeDef
```


Required fields:
- `AppInstanceDataType`: `AppInstanceDataType`
- `ResourceArn`: `str`




## AppInstanceSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceSummaryTypeDef
```




Optional fields:
- `AppInstanceArn`: `str`
- `Name`: `str`
- `Metadata`: `str`


## AppInstanceTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceTypeDef
```




Optional fields:
- `AppInstanceArn`: `str`
- `Name`: `str`
- `Metadata`: `str`
- `CreatedTimestamp`: `datetime`
- `LastUpdatedTimestamp`: `datetime`


## AppInstanceUserMembershipSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceUserMembershipSummaryTypeDef
```




Optional fields:
- `Type`: `ChannelMembershipType`
- `ReadMarkerTimestamp`: `datetime`


## AppInstanceUserSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceUserSummaryTypeDef
```




Optional fields:
- `AppInstanceUserArn`: `str`
- `Name`: `str`
- `Metadata`: `str`


## AppInstanceUserTypeDef

```python
from mypy_boto3_chime.type_defs import AppInstanceUserTypeDef
```




Optional fields:
- `AppInstanceUserArn`: `str`
- `Name`: `str`
- `CreatedTimestamp`: `datetime`
- `Metadata`: `str`
- `LastUpdatedTimestamp`: `datetime`


## AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef

```python
from mypy_boto3_chime.type_defs import AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef
```




Optional fields:
- `PhoneNumberErrors`: `List["PhoneNumberErrorTypeDef"]`


## AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef
```




Optional fields:
- `PhoneNumberErrors`: `List["PhoneNumberErrorTypeDef"]`


## AttendeeTypeDef

```python
from mypy_boto3_chime.type_defs import AttendeeTypeDef
```




Optional fields:
- `ExternalUserId`: `str`
- `AttendeeId`: `str`
- `JoinToken`: `str`


## BatchCreateAttendeeResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchCreateAttendeeResponseTypeDef
```




Optional fields:
- `Attendees`: `List["AttendeeTypeDef"]`
- `Errors`: `List["CreateAttendeeErrorTypeDef"]`


## BatchCreateRoomMembershipResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchCreateRoomMembershipResponseTypeDef
```




Optional fields:
- `Errors`: `List["MemberErrorTypeDef"]`


## BatchDeletePhoneNumberResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchDeletePhoneNumberResponseTypeDef
```




Optional fields:
- `PhoneNumberErrors`: `List["PhoneNumberErrorTypeDef"]`


## BatchSuspendUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchSuspendUserResponseTypeDef
```




Optional fields:
- `UserErrors`: `List["UserErrorTypeDef"]`


## BatchUnsuspendUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchUnsuspendUserResponseTypeDef
```




Optional fields:
- `UserErrors`: `List["UserErrorTypeDef"]`


## BatchUpdatePhoneNumberResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchUpdatePhoneNumberResponseTypeDef
```




Optional fields:
- `PhoneNumberErrors`: `List["PhoneNumberErrorTypeDef"]`


## BatchUpdateUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import BatchUpdateUserResponseTypeDef
```




Optional fields:
- `UserErrors`: `List["UserErrorTypeDef"]`


## BotTypeDef

```python
from mypy_boto3_chime.type_defs import BotTypeDef
```




Optional fields:
- `BotId`: `str`
- `UserId`: `str`
- `DisplayName`: `str`
- `BotType`: `Literal['ChatBot']`
- `Disabled`: `bool`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`
- `BotEmail`: `str`
- `SecurityToken`: `str`


## BusinessCallingSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import BusinessCallingSettingsTypeDef
```




Optional fields:
- `CdrBucket`: `str`


## ChannelBanSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelBanSummaryTypeDef
```




Optional fields:
- `Member`: `"IdentityTypeDef"`


## ChannelBanTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelBanTypeDef
```




Optional fields:
- `Member`: `"IdentityTypeDef"`
- `ChannelArn`: `str`
- `CreatedTimestamp`: `datetime`
- `CreatedBy`: `"IdentityTypeDef"`


## ChannelMembershipForAppInstanceUserSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelMembershipForAppInstanceUserSummaryTypeDef
```




Optional fields:
- `ChannelSummary`: `"ChannelSummaryTypeDef"`
- `AppInstanceUserMembershipSummary`: `"AppInstanceUserMembershipSummaryTypeDef"`


## ChannelMembershipSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelMembershipSummaryTypeDef
```




Optional fields:
- `Member`: `"IdentityTypeDef"`


## ChannelMembershipTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelMembershipTypeDef
```




Optional fields:
- `InvitedBy`: `"IdentityTypeDef"`
- `Type`: `ChannelMembershipType`
- `Member`: `"IdentityTypeDef"`
- `ChannelArn`: `str`
- `CreatedTimestamp`: `datetime`
- `LastUpdatedTimestamp`: `datetime`


## ChannelMessageSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelMessageSummaryTypeDef
```




Optional fields:
- `MessageId`: `str`
- `Content`: `str`
- `Metadata`: `str`
- `Type`: `ChannelMessageType`
- `CreatedTimestamp`: `datetime`
- `LastUpdatedTimestamp`: `datetime`
- `LastEditedTimestamp`: `datetime`
- `Sender`: `"IdentityTypeDef"`
- `Redacted`: `bool`


## ChannelMessageTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelMessageTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `MessageId`: `str`
- `Content`: `str`
- `Metadata`: `str`
- `Type`: `ChannelMessageType`
- `CreatedTimestamp`: `datetime`
- `LastEditedTimestamp`: `datetime`
- `LastUpdatedTimestamp`: `datetime`
- `Sender`: `"IdentityTypeDef"`
- `Redacted`: `bool`
- `Persistence`: `ChannelMessagePersistenceType`


## ChannelModeratedByAppInstanceUserSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelModeratedByAppInstanceUserSummaryTypeDef
```




Optional fields:
- `ChannelSummary`: `"ChannelSummaryTypeDef"`


## ChannelModeratorSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelModeratorSummaryTypeDef
```




Optional fields:
- `Moderator`: `"IdentityTypeDef"`


## ChannelModeratorTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelModeratorTypeDef
```




Optional fields:
- `Moderator`: `"IdentityTypeDef"`
- `ChannelArn`: `str`
- `CreatedTimestamp`: `datetime`
- `CreatedBy`: `"IdentityTypeDef"`


## ChannelRetentionSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelRetentionSettingsTypeDef
```




Optional fields:
- `RetentionDays`: `int`


## ChannelSummaryTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelSummaryTypeDef
```




Optional fields:
- `Name`: `str`
- `ChannelArn`: `str`
- `Mode`: `ChannelMode`
- `Privacy`: `ChannelPrivacy`
- `Metadata`: `str`
- `LastMessageTimestamp`: `datetime`


## ChannelTypeDef

```python
from mypy_boto3_chime.type_defs import ChannelTypeDef
```




Optional fields:
- `Name`: `str`
- `ChannelArn`: `str`
- `Mode`: `ChannelMode`
- `Privacy`: `ChannelPrivacy`
- `Metadata`: `str`
- `CreatedBy`: `"IdentityTypeDef"`
- `CreatedTimestamp`: `datetime`
- `LastMessageTimestamp`: `datetime`
- `LastUpdatedTimestamp`: `datetime`


## ConversationRetentionSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import ConversationRetentionSettingsTypeDef
```




Optional fields:
- `RetentionDays`: `int`


## CreateAccountResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAccountResponseTypeDef
```




Optional fields:
- `Account`: `"AccountTypeDef"`


## CreateAppInstanceAdminResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAppInstanceAdminResponseTypeDef
```




Optional fields:
- `AppInstanceAdmin`: `"IdentityTypeDef"`
- `AppInstanceArn`: `str`


## CreateAppInstanceResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAppInstanceResponseTypeDef
```




Optional fields:
- `AppInstanceArn`: `str`


## CreateAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAppInstanceUserResponseTypeDef
```




Optional fields:
- `AppInstanceUserArn`: `str`


## CreateAttendeeErrorTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAttendeeErrorTypeDef
```




Optional fields:
- `ExternalUserId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## CreateAttendeeRequestItemTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAttendeeRequestItemTypeDef
```


Required fields:
- `ExternalUserId`: `str`



Optional fields:
- `Tags`: `List["TagTypeDef"]`


## CreateAttendeeResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateAttendeeResponseTypeDef
```




Optional fields:
- `Attendee`: `"AttendeeTypeDef"`


## CreateBotResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateBotResponseTypeDef
```




Optional fields:
- `Bot`: `"BotTypeDef"`


## CreateChannelBanResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateChannelBanResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `Member`: `"IdentityTypeDef"`


## CreateChannelMembershipResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateChannelMembershipResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `Member`: `"IdentityTypeDef"`


## CreateChannelModeratorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateChannelModeratorResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `ChannelModerator`: `"IdentityTypeDef"`


## CreateChannelResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateChannelResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`


## CreateMeetingDialOutResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateMeetingDialOutResponseTypeDef
```




Optional fields:
- `TransactionId`: `str`


## CreateMeetingResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateMeetingResponseTypeDef
```




Optional fields:
- `Meeting`: `"MeetingTypeDef"`


## CreateMeetingWithAttendeesResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateMeetingWithAttendeesResponseTypeDef
```




Optional fields:
- `Meeting`: `"MeetingTypeDef"`
- `Attendees`: `List["AttendeeTypeDef"]`
- `Errors`: `List["CreateAttendeeErrorTypeDef"]`


## CreatePhoneNumberOrderResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreatePhoneNumberOrderResponseTypeDef
```




Optional fields:
- `PhoneNumberOrder`: `"PhoneNumberOrderTypeDef"`


## CreateProxySessionResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateProxySessionResponseTypeDef
```




Optional fields:
- `ProxySession`: `"ProxySessionTypeDef"`


## CreateRoomMembershipResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateRoomMembershipResponseTypeDef
```




Optional fields:
- `RoomMembership`: `"RoomMembershipTypeDef"`


## CreateRoomResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateRoomResponseTypeDef
```




Optional fields:
- `Room`: `"RoomTypeDef"`


## CreateSipMediaApplicationCallResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateSipMediaApplicationCallResponseTypeDef
```




Optional fields:
- `SipMediaApplicationCall`: `"SipMediaApplicationCallTypeDef"`


## CreateSipMediaApplicationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateSipMediaApplicationResponseTypeDef
```




Optional fields:
- `SipMediaApplication`: `"SipMediaApplicationTypeDef"`


## CreateSipRuleResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateSipRuleResponseTypeDef
```




Optional fields:
- `SipRule`: `"SipRuleTypeDef"`


## CreateUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## CreateVoiceConnectorGroupResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateVoiceConnectorGroupResponseTypeDef
```




Optional fields:
- `VoiceConnectorGroup`: `"VoiceConnectorGroupTypeDef"`


## CreateVoiceConnectorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import CreateVoiceConnectorResponseTypeDef
```




Optional fields:
- `VoiceConnector`: `"VoiceConnectorTypeDef"`


## CredentialTypeDef

```python
from mypy_boto3_chime.type_defs import CredentialTypeDef
```




Optional fields:
- `Username`: `str`
- `Password`: `str`


## DNISEmergencyCallingConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import DNISEmergencyCallingConfigurationTypeDef
```


Required fields:
- `EmergencyPhoneNumber`: `str`
- `CallingCountry`: `str`



Optional fields:
- `TestPhoneNumber`: `str`


## DescribeAppInstanceAdminResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeAppInstanceAdminResponseTypeDef
```




Optional fields:
- `AppInstanceAdmin`: `"AppInstanceAdminTypeDef"`


## DescribeAppInstanceResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeAppInstanceResponseTypeDef
```




Optional fields:
- `AppInstance`: `"AppInstanceTypeDef"`


## DescribeAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeAppInstanceUserResponseTypeDef
```




Optional fields:
- `AppInstanceUser`: `"AppInstanceUserTypeDef"`


## DescribeChannelBanResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeChannelBanResponseTypeDef
```




Optional fields:
- `ChannelBan`: `"ChannelBanTypeDef"`


## DescribeChannelMembershipForAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeChannelMembershipForAppInstanceUserResponseTypeDef
```




Optional fields:
- `ChannelMembership`: `"ChannelMembershipForAppInstanceUserSummaryTypeDef"`


## DescribeChannelMembershipResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeChannelMembershipResponseTypeDef
```




Optional fields:
- `ChannelMembership`: `"ChannelMembershipTypeDef"`


## DescribeChannelModeratedByAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeChannelModeratedByAppInstanceUserResponseTypeDef
```




Optional fields:
- `Channel`: `"ChannelModeratedByAppInstanceUserSummaryTypeDef"`


## DescribeChannelModeratorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeChannelModeratorResponseTypeDef
```




Optional fields:
- `ChannelModerator`: `"ChannelModeratorTypeDef"`


## DescribeChannelResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DescribeChannelResponseTypeDef
```




Optional fields:
- `Channel`: `"ChannelTypeDef"`


## DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef
```




Optional fields:
- `PhoneNumberErrors`: `List["PhoneNumberErrorTypeDef"]`


## DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef
```




Optional fields:
- `PhoneNumberErrors`: `List["PhoneNumberErrorTypeDef"]`


## EmergencyCallingConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import EmergencyCallingConfigurationTypeDef
```




Optional fields:
- `DNIS`: `List["DNISEmergencyCallingConfigurationTypeDef"]`


## EventsConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import EventsConfigurationTypeDef
```




Optional fields:
- `BotId`: `str`
- `OutboundEventsHTTPSEndpoint`: `str`
- `LambdaFunctionArn`: `str`


## GeoMatchParamsTypeDef

```python
from mypy_boto3_chime.type_defs import GeoMatchParamsTypeDef
```


Required fields:
- `Country`: `str`
- `AreaCode`: `str`




## GetAccountResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetAccountResponseTypeDef
```




Optional fields:
- `Account`: `"AccountTypeDef"`


## GetAccountSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetAccountSettingsResponseTypeDef
```




Optional fields:
- `AccountSettings`: `"AccountSettingsTypeDef"`


## GetAppInstanceRetentionSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetAppInstanceRetentionSettingsResponseTypeDef
```




Optional fields:
- `AppInstanceRetentionSettings`: `"AppInstanceRetentionSettingsTypeDef"`
- `InitiateDeletionTimestamp`: `datetime`


## GetAppInstanceStreamingConfigurationsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetAppInstanceStreamingConfigurationsResponseTypeDef
```




Optional fields:
- `AppInstanceStreamingConfigurations`: `List["AppInstanceStreamingConfigurationTypeDef"]`


## GetAttendeeResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetAttendeeResponseTypeDef
```




Optional fields:
- `Attendee`: `"AttendeeTypeDef"`


## GetBotResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetBotResponseTypeDef
```




Optional fields:
- `Bot`: `"BotTypeDef"`


## GetChannelMessageResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetChannelMessageResponseTypeDef
```




Optional fields:
- `ChannelMessage`: `"ChannelMessageTypeDef"`


## GetEventsConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetEventsConfigurationResponseTypeDef
```




Optional fields:
- `EventsConfiguration`: `"EventsConfigurationTypeDef"`


## GetGlobalSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetGlobalSettingsResponseTypeDef
```




Optional fields:
- `BusinessCalling`: `"BusinessCallingSettingsTypeDef"`
- `VoiceConnector`: `"VoiceConnectorSettingsTypeDef"`


## GetMeetingResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetMeetingResponseTypeDef
```




Optional fields:
- `Meeting`: `"MeetingTypeDef"`


## GetMessagingSessionEndpointResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetMessagingSessionEndpointResponseTypeDef
```




Optional fields:
- `Endpoint`: `"MessagingSessionEndpointTypeDef"`


## GetPhoneNumberOrderResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetPhoneNumberOrderResponseTypeDef
```




Optional fields:
- `PhoneNumberOrder`: `"PhoneNumberOrderTypeDef"`


## GetPhoneNumberResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetPhoneNumberResponseTypeDef
```




Optional fields:
- `PhoneNumber`: `"PhoneNumberTypeDef"`


## GetPhoneNumberSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetPhoneNumberSettingsResponseTypeDef
```




Optional fields:
- `CallingName`: `str`
- `CallingNameUpdatedTimestamp`: `datetime`


## GetProxySessionResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetProxySessionResponseTypeDef
```




Optional fields:
- `ProxySession`: `"ProxySessionTypeDef"`


## GetRetentionSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetRetentionSettingsResponseTypeDef
```




Optional fields:
- `RetentionSettings`: `"RetentionSettingsTypeDef"`
- `InitiateDeletionTimestamp`: `datetime`


## GetRoomResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetRoomResponseTypeDef
```




Optional fields:
- `Room`: `"RoomTypeDef"`


## GetSipMediaApplicationLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetSipMediaApplicationLoggingConfigurationResponseTypeDef
```




Optional fields:
- `SipMediaApplicationLoggingConfiguration`: `"SipMediaApplicationLoggingConfigurationTypeDef"`


## GetSipMediaApplicationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetSipMediaApplicationResponseTypeDef
```




Optional fields:
- `SipMediaApplication`: `"SipMediaApplicationTypeDef"`


## GetSipRuleResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetSipRuleResponseTypeDef
```




Optional fields:
- `SipRule`: `"SipRuleTypeDef"`


## GetUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## GetUserSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetUserSettingsResponseTypeDef
```




Optional fields:
- `UserSettings`: `"UserSettingsTypeDef"`


## GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef
```




Optional fields:
- `EmergencyCallingConfiguration`: `"EmergencyCallingConfigurationTypeDef"`


## GetVoiceConnectorGroupResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorGroupResponseTypeDef
```




Optional fields:
- `VoiceConnectorGroup`: `"VoiceConnectorGroupTypeDef"`


## GetVoiceConnectorLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorLoggingConfigurationResponseTypeDef
```




Optional fields:
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## GetVoiceConnectorOriginationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorOriginationResponseTypeDef
```




Optional fields:
- `Origination`: `"OriginationTypeDef"`


## GetVoiceConnectorProxyResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorProxyResponseTypeDef
```




Optional fields:
- `Proxy`: `"ProxyTypeDef"`


## GetVoiceConnectorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorResponseTypeDef
```




Optional fields:
- `VoiceConnector`: `"VoiceConnectorTypeDef"`


## GetVoiceConnectorStreamingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorStreamingConfigurationResponseTypeDef
```




Optional fields:
- `StreamingConfiguration`: `"StreamingConfigurationTypeDef"`


## GetVoiceConnectorTerminationHealthResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorTerminationHealthResponseTypeDef
```




Optional fields:
- `TerminationHealth`: `"TerminationHealthTypeDef"`


## GetVoiceConnectorTerminationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import GetVoiceConnectorTerminationResponseTypeDef
```




Optional fields:
- `Termination`: `"TerminationTypeDef"`


## IdentityTypeDef

```python
from mypy_boto3_chime.type_defs import IdentityTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## InviteTypeDef

```python
from mypy_boto3_chime.type_defs import InviteTypeDef
```




Optional fields:
- `InviteId`: `str`
- `Status`: `InviteStatus`
- `EmailAddress`: `str`
- `EmailStatus`: `EmailStatus`


## InviteUsersResponseTypeDef

```python
from mypy_boto3_chime.type_defs import InviteUsersResponseTypeDef
```




Optional fields:
- `Invites`: `List["InviteTypeDef"]`


## ListAccountsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListAccountsResponseTypeDef
```




Optional fields:
- `Accounts`: `List["AccountTypeDef"]`
- `NextToken`: `str`


## ListAppInstanceAdminsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListAppInstanceAdminsResponseTypeDef
```




Optional fields:
- `AppInstanceArn`: `str`
- `AppInstanceAdmins`: `List["AppInstanceAdminSummaryTypeDef"]`
- `NextToken`: `str`


## ListAppInstanceUsersResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListAppInstanceUsersResponseTypeDef
```




Optional fields:
- `AppInstanceArn`: `str`
- `AppInstanceUsers`: `List["AppInstanceUserSummaryTypeDef"]`
- `NextToken`: `str`


## ListAppInstancesResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListAppInstancesResponseTypeDef
```




Optional fields:
- `AppInstances`: `List["AppInstanceSummaryTypeDef"]`
- `NextToken`: `str`


## ListAttendeeTagsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListAttendeeTagsResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListAttendeesResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListAttendeesResponseTypeDef
```




Optional fields:
- `Attendees`: `List["AttendeeTypeDef"]`
- `NextToken`: `str`


## ListBotsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListBotsResponseTypeDef
```




Optional fields:
- `Bots`: `List["BotTypeDef"]`
- `NextToken`: `str`


## ListChannelBansResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelBansResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `NextToken`: `str`
- `ChannelBans`: `List["ChannelBanSummaryTypeDef"]`


## ListChannelMembershipsForAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelMembershipsForAppInstanceUserResponseTypeDef
```




Optional fields:
- `ChannelMemberships`: `List["ChannelMembershipForAppInstanceUserSummaryTypeDef"]`
- `NextToken`: `str`


## ListChannelMembershipsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelMembershipsResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `ChannelMemberships`: `List["ChannelMembershipSummaryTypeDef"]`
- `NextToken`: `str`


## ListChannelMessagesResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelMessagesResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `NextToken`: `str`
- `ChannelMessages`: `List["ChannelMessageSummaryTypeDef"]`


## ListChannelModeratorsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelModeratorsResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `NextToken`: `str`
- `ChannelModerators`: `List["ChannelModeratorSummaryTypeDef"]`


## ListChannelsModeratedByAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelsModeratedByAppInstanceUserResponseTypeDef
```




Optional fields:
- `Channels`: `List["ChannelModeratedByAppInstanceUserSummaryTypeDef"]`
- `NextToken`: `str`


## ListChannelsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListChannelsResponseTypeDef
```




Optional fields:
- `Channels`: `List["ChannelSummaryTypeDef"]`
- `NextToken`: `str`


## ListMeetingTagsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListMeetingTagsResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListMeetingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListMeetingsResponseTypeDef
```




Optional fields:
- `Meetings`: `List["MeetingTypeDef"]`
- `NextToken`: `str`


## ListPhoneNumberOrdersResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListPhoneNumberOrdersResponseTypeDef
```




Optional fields:
- `PhoneNumberOrders`: `List["PhoneNumberOrderTypeDef"]`
- `NextToken`: `str`


## ListPhoneNumbersResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListPhoneNumbersResponseTypeDef
```




Optional fields:
- `PhoneNumbers`: `List["PhoneNumberTypeDef"]`
- `NextToken`: `str`


## ListProxySessionsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListProxySessionsResponseTypeDef
```




Optional fields:
- `ProxySessions`: `List["ProxySessionTypeDef"]`
- `NextToken`: `str`


## ListRoomMembershipsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListRoomMembershipsResponseTypeDef
```




Optional fields:
- `RoomMemberships`: `List["RoomMembershipTypeDef"]`
- `NextToken`: `str`


## ListRoomsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListRoomsResponseTypeDef
```




Optional fields:
- `Rooms`: `List["RoomTypeDef"]`
- `NextToken`: `str`


## ListSipMediaApplicationsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListSipMediaApplicationsResponseTypeDef
```




Optional fields:
- `SipMediaApplications`: `List["SipMediaApplicationTypeDef"]`
- `NextToken`: `str`


## ListSipRulesResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListSipRulesResponseTypeDef
```




Optional fields:
- `SipRules`: `List["SipRuleTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListUsersResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListUsersResponseTypeDef
```




Optional fields:
- `Users`: `List["UserTypeDef"]`
- `NextToken`: `str`


## ListVoiceConnectorGroupsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListVoiceConnectorGroupsResponseTypeDef
```




Optional fields:
- `VoiceConnectorGroups`: `List["VoiceConnectorGroupTypeDef"]`
- `NextToken`: `str`


## ListVoiceConnectorTerminationCredentialsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListVoiceConnectorTerminationCredentialsResponseTypeDef
```




Optional fields:
- `Usernames`: `List[str]`


## ListVoiceConnectorsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ListVoiceConnectorsResponseTypeDef
```




Optional fields:
- `VoiceConnectors`: `List["VoiceConnectorTypeDef"]`
- `NextToken`: `str`


## LoggingConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import LoggingConfigurationTypeDef
```




Optional fields:
- `EnableSIPLogs`: `bool`


## MediaPlacementTypeDef

```python
from mypy_boto3_chime.type_defs import MediaPlacementTypeDef
```




Optional fields:
- `AudioHostUrl`: `str`
- `AudioFallbackUrl`: `str`
- `ScreenDataUrl`: `str`
- `ScreenSharingUrl`: `str`
- `ScreenViewingUrl`: `str`
- `SignalingUrl`: `str`
- `TurnControlUrl`: `str`


## MeetingNotificationConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import MeetingNotificationConfigurationTypeDef
```




Optional fields:
- `SnsTopicArn`: `str`
- `SqsQueueArn`: `str`


## MeetingTypeDef

```python
from mypy_boto3_chime.type_defs import MeetingTypeDef
```




Optional fields:
- `MeetingId`: `str`
- `ExternalMeetingId`: `str`
- `MediaPlacement`: `"MediaPlacementTypeDef"`
- `MediaRegion`: `str`


## MemberErrorTypeDef

```python
from mypy_boto3_chime.type_defs import MemberErrorTypeDef
```




Optional fields:
- `MemberId`: `str`
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## MemberTypeDef

```python
from mypy_boto3_chime.type_defs import MemberTypeDef
```




Optional fields:
- `MemberId`: `str`
- `MemberType`: `MemberType`
- `Email`: `str`
- `FullName`: `str`
- `AccountId`: `str`


## MembershipItemTypeDef

```python
from mypy_boto3_chime.type_defs import MembershipItemTypeDef
```




Optional fields:
- `MemberId`: `str`
- `Role`: `RoomMembershipRole`


## MessagingSessionEndpointTypeDef

```python
from mypy_boto3_chime.type_defs import MessagingSessionEndpointTypeDef
```




Optional fields:
- `Url`: `str`


## OrderedPhoneNumberTypeDef

```python
from mypy_boto3_chime.type_defs import OrderedPhoneNumberTypeDef
```




Optional fields:
- `E164PhoneNumber`: `str`
- `Status`: `OrderedPhoneNumberStatus`


## OriginationRouteTypeDef

```python
from mypy_boto3_chime.type_defs import OriginationRouteTypeDef
```




Optional fields:
- `Host`: `str`
- `Port`: `int`
- `Protocol`: `OriginationRouteProtocol`
- `Priority`: `int`
- `Weight`: `int`


## OriginationTypeDef

```python
from mypy_boto3_chime.type_defs import OriginationTypeDef
```




Optional fields:
- `Routes`: `List["OriginationRouteTypeDef"]`
- `Disabled`: `bool`


## PaginatorConfigTypeDef

```python
from mypy_boto3_chime.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParticipantTypeDef

```python
from mypy_boto3_chime.type_defs import ParticipantTypeDef
```




Optional fields:
- `PhoneNumber`: `str`
- `ProxyPhoneNumber`: `str`


## PhoneNumberAssociationTypeDef

```python
from mypy_boto3_chime.type_defs import PhoneNumberAssociationTypeDef
```




Optional fields:
- `Value`: `str`
- `Name`: `PhoneNumberAssociationName`
- `AssociatedTimestamp`: `datetime`


## PhoneNumberCapabilitiesTypeDef

```python
from mypy_boto3_chime.type_defs import PhoneNumberCapabilitiesTypeDef
```




Optional fields:
- `InboundCall`: `bool`
- `OutboundCall`: `bool`
- `InboundSMS`: `bool`
- `OutboundSMS`: `bool`
- `InboundMMS`: `bool`
- `OutboundMMS`: `bool`


## PhoneNumberErrorTypeDef

```python
from mypy_boto3_chime.type_defs import PhoneNumberErrorTypeDef
```




Optional fields:
- `PhoneNumberId`: `str`
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## PhoneNumberOrderTypeDef

```python
from mypy_boto3_chime.type_defs import PhoneNumberOrderTypeDef
```




Optional fields:
- `PhoneNumberOrderId`: `str`
- `ProductType`: `PhoneNumberProductType`
- `Status`: `PhoneNumberOrderStatus`
- `OrderedPhoneNumbers`: `List["OrderedPhoneNumberTypeDef"]`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`


## PhoneNumberTypeDef

```python
from mypy_boto3_chime.type_defs import PhoneNumberTypeDef
```




Optional fields:
- `PhoneNumberId`: `str`
- `E164PhoneNumber`: `str`
- `Type`: `PhoneNumberType`
- `ProductType`: `PhoneNumberProductType`
- `Status`: `PhoneNumberStatus`
- `Capabilities`: `"PhoneNumberCapabilitiesTypeDef"`
- `Associations`: `List["PhoneNumberAssociationTypeDef"]`
- `CallingName`: `str`
- `CallingNameStatus`: `CallingNameStatus`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`
- `DeletionTimestamp`: `datetime`


## ProxySessionTypeDef

```python
from mypy_boto3_chime.type_defs import ProxySessionTypeDef
```




Optional fields:
- `VoiceConnectorId`: `str`
- `ProxySessionId`: `str`
- `Name`: `str`
- `Status`: `ProxySessionStatus`
- `ExpiryMinutes`: `int`
- `Capabilities`: `List[Capability]`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`
- `EndedTimestamp`: `datetime`
- `Participants`: `List["ParticipantTypeDef"]`
- `NumberSelectionBehavior`: `NumberSelectionBehavior`
- `GeoMatchLevel`: `GeoMatchLevel`
- `GeoMatchParams`: `"GeoMatchParamsTypeDef"`


## ProxyTypeDef

```python
from mypy_boto3_chime.type_defs import ProxyTypeDef
```




Optional fields:
- `DefaultSessionExpiryMinutes`: `int`
- `Disabled`: `bool`
- `FallBackPhoneNumber`: `str`
- `PhoneNumberCountries`: `List[str]`


## PutAppInstanceRetentionSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutAppInstanceRetentionSettingsResponseTypeDef
```




Optional fields:
- `AppInstanceRetentionSettings`: `"AppInstanceRetentionSettingsTypeDef"`
- `InitiateDeletionTimestamp`: `datetime`


## PutAppInstanceStreamingConfigurationsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutAppInstanceStreamingConfigurationsResponseTypeDef
```




Optional fields:
- `AppInstanceStreamingConfigurations`: `List["AppInstanceStreamingConfigurationTypeDef"]`


## PutEventsConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutEventsConfigurationResponseTypeDef
```




Optional fields:
- `EventsConfiguration`: `"EventsConfigurationTypeDef"`


## PutRetentionSettingsResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutRetentionSettingsResponseTypeDef
```




Optional fields:
- `RetentionSettings`: `"RetentionSettingsTypeDef"`
- `InitiateDeletionTimestamp`: `datetime`


## PutSipMediaApplicationLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutSipMediaApplicationLoggingConfigurationResponseTypeDef
```




Optional fields:
- `SipMediaApplicationLoggingConfiguration`: `"SipMediaApplicationLoggingConfigurationTypeDef"`


## PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef
```




Optional fields:
- `EmergencyCallingConfiguration`: `"EmergencyCallingConfigurationTypeDef"`


## PutVoiceConnectorLoggingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutVoiceConnectorLoggingConfigurationResponseTypeDef
```




Optional fields:
- `LoggingConfiguration`: `"LoggingConfigurationTypeDef"`


## PutVoiceConnectorOriginationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutVoiceConnectorOriginationResponseTypeDef
```




Optional fields:
- `Origination`: `"OriginationTypeDef"`


## PutVoiceConnectorProxyResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutVoiceConnectorProxyResponseTypeDef
```




Optional fields:
- `Proxy`: `"ProxyTypeDef"`


## PutVoiceConnectorStreamingConfigurationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutVoiceConnectorStreamingConfigurationResponseTypeDef
```




Optional fields:
- `StreamingConfiguration`: `"StreamingConfigurationTypeDef"`


## PutVoiceConnectorTerminationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import PutVoiceConnectorTerminationResponseTypeDef
```




Optional fields:
- `Termination`: `"TerminationTypeDef"`


## RedactChannelMessageResponseTypeDef

```python
from mypy_boto3_chime.type_defs import RedactChannelMessageResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `MessageId`: `str`


## RegenerateSecurityTokenResponseTypeDef

```python
from mypy_boto3_chime.type_defs import RegenerateSecurityTokenResponseTypeDef
```




Optional fields:
- `Bot`: `"BotTypeDef"`


## ResetPersonalPINResponseTypeDef

```python
from mypy_boto3_chime.type_defs import ResetPersonalPINResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## RestorePhoneNumberResponseTypeDef

```python
from mypy_boto3_chime.type_defs import RestorePhoneNumberResponseTypeDef
```




Optional fields:
- `PhoneNumber`: `"PhoneNumberTypeDef"`


## RetentionSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import RetentionSettingsTypeDef
```




Optional fields:
- `RoomRetentionSettings`: `"RoomRetentionSettingsTypeDef"`
- `ConversationRetentionSettings`: `"ConversationRetentionSettingsTypeDef"`


## RoomMembershipTypeDef

```python
from mypy_boto3_chime.type_defs import RoomMembershipTypeDef
```




Optional fields:
- `RoomId`: `str`
- `Member`: `"MemberTypeDef"`
- `Role`: `RoomMembershipRole`
- `InvitedBy`: `str`
- `UpdatedTimestamp`: `datetime`


## RoomRetentionSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import RoomRetentionSettingsTypeDef
```




Optional fields:
- `RetentionDays`: `int`


## RoomTypeDef

```python
from mypy_boto3_chime.type_defs import RoomTypeDef
```




Optional fields:
- `RoomId`: `str`
- `Name`: `str`
- `AccountId`: `str`
- `CreatedBy`: `str`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`


## SearchAvailablePhoneNumbersResponseTypeDef

```python
from mypy_boto3_chime.type_defs import SearchAvailablePhoneNumbersResponseTypeDef
```




Optional fields:
- `E164PhoneNumbers`: `List[str]`


## SendChannelMessageResponseTypeDef

```python
from mypy_boto3_chime.type_defs import SendChannelMessageResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `MessageId`: `str`


## SigninDelegateGroupTypeDef

```python
from mypy_boto3_chime.type_defs import SigninDelegateGroupTypeDef
```




Optional fields:
- `GroupName`: `str`


## SipMediaApplicationCallTypeDef

```python
from mypy_boto3_chime.type_defs import SipMediaApplicationCallTypeDef
```




Optional fields:
- `TransactionId`: `str`


## SipMediaApplicationEndpointTypeDef

```python
from mypy_boto3_chime.type_defs import SipMediaApplicationEndpointTypeDef
```




Optional fields:
- `LambdaArn`: `str`


## SipMediaApplicationLoggingConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import SipMediaApplicationLoggingConfigurationTypeDef
```




Optional fields:
- `EnableSipMediaApplicationMessageLogs`: `bool`


## SipMediaApplicationTypeDef

```python
from mypy_boto3_chime.type_defs import SipMediaApplicationTypeDef
```




Optional fields:
- `SipMediaApplicationId`: `str`
- `AwsRegion`: `str`
- `Name`: `str`
- `Endpoints`: `List["SipMediaApplicationEndpointTypeDef"]`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`


## SipRuleTargetApplicationTypeDef

```python
from mypy_boto3_chime.type_defs import SipRuleTargetApplicationTypeDef
```




Optional fields:
- `SipMediaApplicationId`: `str`
- `Priority`: `int`
- `AwsRegion`: `str`


## SipRuleTypeDef

```python
from mypy_boto3_chime.type_defs import SipRuleTypeDef
```




Optional fields:
- `SipRuleId`: `str`
- `Name`: `str`
- `Disabled`: `bool`
- `TriggerType`: `SipRuleTriggerType`
- `TriggerValue`: `str`
- `TargetApplications`: `List["SipRuleTargetApplicationTypeDef"]`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`


## StreamingConfigurationTypeDef

```python
from mypy_boto3_chime.type_defs import StreamingConfigurationTypeDef
```


Required fields:
- `DataRetentionInHours`: `int`



Optional fields:
- `Disabled`: `bool`
- `StreamingNotificationTargets`: `List["StreamingNotificationTargetTypeDef"]`


## StreamingNotificationTargetTypeDef

```python
from mypy_boto3_chime.type_defs import StreamingNotificationTargetTypeDef
```


Required fields:
- `NotificationTarget`: `NotificationTarget`




## TagTypeDef

```python
from mypy_boto3_chime.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TelephonySettingsTypeDef

```python
from mypy_boto3_chime.type_defs import TelephonySettingsTypeDef
```


Required fields:
- `InboundCalling`: `bool`
- `OutboundCalling`: `bool`
- `SMS`: `bool`




## TerminationHealthTypeDef

```python
from mypy_boto3_chime.type_defs import TerminationHealthTypeDef
```




Optional fields:
- `Timestamp`: `datetime`
- `Source`: `str`


## TerminationTypeDef

```python
from mypy_boto3_chime.type_defs import TerminationTypeDef
```




Optional fields:
- `CpsLimit`: `int`
- `DefaultPhoneNumber`: `str`
- `CallingRegions`: `List[str]`
- `CidrAllowedList`: `List[str]`
- `Disabled`: `bool`


## UpdateAccountResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateAccountResponseTypeDef
```




Optional fields:
- `Account`: `"AccountTypeDef"`


## UpdateAppInstanceResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateAppInstanceResponseTypeDef
```




Optional fields:
- `AppInstanceArn`: `str`


## UpdateAppInstanceUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateAppInstanceUserResponseTypeDef
```




Optional fields:
- `AppInstanceUserArn`: `str`


## UpdateBotResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateBotResponseTypeDef
```




Optional fields:
- `Bot`: `"BotTypeDef"`


## UpdateChannelMessageResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateChannelMessageResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`
- `MessageId`: `str`


## UpdateChannelReadMarkerResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateChannelReadMarkerResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`


## UpdateChannelResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateChannelResponseTypeDef
```




Optional fields:
- `ChannelArn`: `str`


## UpdatePhoneNumberRequestItemTypeDef

```python
from mypy_boto3_chime.type_defs import UpdatePhoneNumberRequestItemTypeDef
```


Required fields:
- `PhoneNumberId`: `str`



Optional fields:
- `ProductType`: `PhoneNumberProductType`
- `CallingName`: `str`


## UpdatePhoneNumberResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdatePhoneNumberResponseTypeDef
```




Optional fields:
- `PhoneNumber`: `"PhoneNumberTypeDef"`


## UpdateProxySessionResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateProxySessionResponseTypeDef
```




Optional fields:
- `ProxySession`: `"ProxySessionTypeDef"`


## UpdateRoomMembershipResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateRoomMembershipResponseTypeDef
```




Optional fields:
- `RoomMembership`: `"RoomMembershipTypeDef"`


## UpdateRoomResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateRoomResponseTypeDef
```




Optional fields:
- `Room`: `"RoomTypeDef"`


## UpdateSipMediaApplicationResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateSipMediaApplicationResponseTypeDef
```




Optional fields:
- `SipMediaApplication`: `"SipMediaApplicationTypeDef"`


## UpdateSipRuleResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateSipRuleResponseTypeDef
```




Optional fields:
- `SipRule`: `"SipRuleTypeDef"`


## UpdateUserRequestItemTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateUserRequestItemTypeDef
```


Required fields:
- `UserId`: `str`



Optional fields:
- `LicenseType`: `License`
- `UserType`: `UserType`
- `AlexaForBusinessMetadata`: `"AlexaForBusinessMetadataTypeDef"`


## UpdateUserResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## UpdateVoiceConnectorGroupResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateVoiceConnectorGroupResponseTypeDef
```




Optional fields:
- `VoiceConnectorGroup`: `"VoiceConnectorGroupTypeDef"`


## UpdateVoiceConnectorResponseTypeDef

```python
from mypy_boto3_chime.type_defs import UpdateVoiceConnectorResponseTypeDef
```




Optional fields:
- `VoiceConnector`: `"VoiceConnectorTypeDef"`


## UserErrorTypeDef

```python
from mypy_boto3_chime.type_defs import UserErrorTypeDef
```




Optional fields:
- `UserId`: `str`
- `ErrorCode`: `ErrorCode`
- `ErrorMessage`: `str`


## UserSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import UserSettingsTypeDef
```


Required fields:
- `Telephony`: `"TelephonySettingsTypeDef"`




## UserTypeDef

```python
from mypy_boto3_chime.type_defs import UserTypeDef
```


Required fields:
- `UserId`: `str`



Optional fields:
- `AccountId`: `str`
- `PrimaryEmail`: `str`
- `PrimaryProvisionedNumber`: `str`
- `DisplayName`: `str`
- `LicenseType`: `License`
- `UserType`: `UserType`
- `UserRegistrationStatus`: `RegistrationStatus`
- `UserInvitationStatus`: `InviteStatus`
- `RegisteredOn`: `datetime`
- `InvitedOn`: `datetime`
- `AlexaForBusinessMetadata`: `"AlexaForBusinessMetadataTypeDef"`
- `PersonalPIN`: `str`


## VoiceConnectorGroupTypeDef

```python
from mypy_boto3_chime.type_defs import VoiceConnectorGroupTypeDef
```




Optional fields:
- `VoiceConnectorGroupId`: `str`
- `Name`: `str`
- `VoiceConnectorItems`: `List["VoiceConnectorItemTypeDef"]`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`


## VoiceConnectorItemTypeDef

```python
from mypy_boto3_chime.type_defs import VoiceConnectorItemTypeDef
```


Required fields:
- `VoiceConnectorId`: `str`
- `Priority`: `int`




## VoiceConnectorSettingsTypeDef

```python
from mypy_boto3_chime.type_defs import VoiceConnectorSettingsTypeDef
```




Optional fields:
- `CdrBucket`: `str`


## VoiceConnectorTypeDef

```python
from mypy_boto3_chime.type_defs import VoiceConnectorTypeDef
```




Optional fields:
- `VoiceConnectorId`: `str`
- `AwsRegion`: `VoiceConnectorAwsRegion`
- `Name`: `str`
- `OutboundHostName`: `str`
- `RequireEncryption`: `bool`
- `CreatedTimestamp`: `datetime`
- `UpdatedTimestamp`: `datetime`

