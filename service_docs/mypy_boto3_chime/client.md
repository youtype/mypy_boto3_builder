# ChimeClient for boto3 Chime module

> [Index](../index.md) > [Chime](./index.md) > ChimeClient

Auto-generated documentation for [Chime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime)
type annotations stubs module [mypy_boto3_chime](https://pypi.org/project/mypy-boto3-chime/).

- [ChimeClient for boto3 Chime module](#chimeclient-for-boto3-chime-module)
  - [ChimeClient](#chimeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_phone_number_with_user](#associate_phone_number_with_user)
    - [associate_phone_numbers_with_voice_connector](#associate_phone_numbers_with_voice_connector)
    - [associate_phone_numbers_with_voice_connector_group](#associate_phone_numbers_with_voice_connector_group)
    - [associate_signin_delegate_groups_with_account](#associate_signin_delegate_groups_with_account)
    - [batch_create_attendee](#batch_create_attendee)
    - [batch_create_room_membership](#batch_create_room_membership)
    - [batch_delete_phone_number](#batch_delete_phone_number)
    - [batch_suspend_user](#batch_suspend_user)
    - [batch_unsuspend_user](#batch_unsuspend_user)
    - [batch_update_phone_number](#batch_update_phone_number)
    - [batch_update_user](#batch_update_user)
    - [can_paginate](#can_paginate)
    - [create_account](#create_account)
    - [create_app_instance](#create_app_instance)
    - [create_app_instance_admin](#create_app_instance_admin)
    - [create_app_instance_user](#create_app_instance_user)
    - [create_attendee](#create_attendee)
    - [create_bot](#create_bot)
    - [create_channel](#create_channel)
    - [create_channel_ban](#create_channel_ban)
    - [create_channel_membership](#create_channel_membership)
    - [create_channel_moderator](#create_channel_moderator)
    - [create_meeting](#create_meeting)
    - [create_meeting_dial_out](#create_meeting_dial_out)
    - [create_meeting_with_attendees](#create_meeting_with_attendees)
    - [create_phone_number_order](#create_phone_number_order)
    - [create_proxy_session](#create_proxy_session)
    - [create_room](#create_room)
    - [create_room_membership](#create_room_membership)
    - [create_sip_media_application](#create_sip_media_application)
    - [create_sip_media_application_call](#create_sip_media_application_call)
    - [create_sip_rule](#create_sip_rule)
    - [create_user](#create_user)
    - [create_voice_connector](#create_voice_connector)
    - [create_voice_connector_group](#create_voice_connector_group)
    - [delete_account](#delete_account)
    - [delete_app_instance](#delete_app_instance)
    - [delete_app_instance_admin](#delete_app_instance_admin)
    - [delete_app_instance_streaming_configurations](#delete_app_instance_streaming_configurations)
    - [delete_app_instance_user](#delete_app_instance_user)
    - [delete_attendee](#delete_attendee)
    - [delete_channel](#delete_channel)
    - [delete_channel_ban](#delete_channel_ban)
    - [delete_channel_membership](#delete_channel_membership)
    - [delete_channel_message](#delete_channel_message)
    - [delete_channel_moderator](#delete_channel_moderator)
    - [delete_events_configuration](#delete_events_configuration)
    - [delete_meeting](#delete_meeting)
    - [delete_phone_number](#delete_phone_number)
    - [delete_proxy_session](#delete_proxy_session)
    - [delete_room](#delete_room)
    - [delete_room_membership](#delete_room_membership)
    - [delete_sip_media_application](#delete_sip_media_application)
    - [delete_sip_rule](#delete_sip_rule)
    - [delete_voice_connector](#delete_voice_connector)
    - [delete_voice_connector_emergency_calling_configuration](#delete_voice_connector_emergency_calling_configuration)
    - [delete_voice_connector_group](#delete_voice_connector_group)
    - [delete_voice_connector_origination](#delete_voice_connector_origination)
    - [delete_voice_connector_proxy](#delete_voice_connector_proxy)
    - [delete_voice_connector_streaming_configuration](#delete_voice_connector_streaming_configuration)
    - [delete_voice_connector_termination](#delete_voice_connector_termination)
    - [delete_voice_connector_termination_credentials](#delete_voice_connector_termination_credentials)
    - [describe_app_instance](#describe_app_instance)
    - [describe_app_instance_admin](#describe_app_instance_admin)
    - [describe_app_instance_user](#describe_app_instance_user)
    - [describe_channel](#describe_channel)
    - [describe_channel_ban](#describe_channel_ban)
    - [describe_channel_membership](#describe_channel_membership)
    - [describe_channel_membership_for_app_instance_user](#describe_channel_membership_for_app_instance_user)
    - [describe_channel_moderated_by_app_instance_user](#describe_channel_moderated_by_app_instance_user)
    - [describe_channel_moderator](#describe_channel_moderator)
    - [disassociate_phone_number_from_user](#disassociate_phone_number_from_user)
    - [disassociate_phone_numbers_from_voice_connector](#disassociate_phone_numbers_from_voice_connector)
    - [disassociate_phone_numbers_from_voice_connector_group](#disassociate_phone_numbers_from_voice_connector_group)
    - [disassociate_signin_delegate_groups_from_account](#disassociate_signin_delegate_groups_from_account)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account](#get_account)
    - [get_account_settings](#get_account_settings)
    - [get_app_instance_retention_settings](#get_app_instance_retention_settings)
    - [get_app_instance_streaming_configurations](#get_app_instance_streaming_configurations)
    - [get_attendee](#get_attendee)
    - [get_bot](#get_bot)
    - [get_channel_message](#get_channel_message)
    - [get_events_configuration](#get_events_configuration)
    - [get_global_settings](#get_global_settings)
    - [get_meeting](#get_meeting)
    - [get_messaging_session_endpoint](#get_messaging_session_endpoint)
    - [get_phone_number](#get_phone_number)
    - [get_phone_number_order](#get_phone_number_order)
    - [get_phone_number_settings](#get_phone_number_settings)
    - [get_proxy_session](#get_proxy_session)
    - [get_retention_settings](#get_retention_settings)
    - [get_room](#get_room)
    - [get_sip_media_application](#get_sip_media_application)
    - [get_sip_media_application_logging_configuration](#get_sip_media_application_logging_configuration)
    - [get_sip_rule](#get_sip_rule)
    - [get_user](#get_user)
    - [get_user_settings](#get_user_settings)
    - [get_voice_connector](#get_voice_connector)
    - [get_voice_connector_emergency_calling_configuration](#get_voice_connector_emergency_calling_configuration)
    - [get_voice_connector_group](#get_voice_connector_group)
    - [get_voice_connector_logging_configuration](#get_voice_connector_logging_configuration)
    - [get_voice_connector_origination](#get_voice_connector_origination)
    - [get_voice_connector_proxy](#get_voice_connector_proxy)
    - [get_voice_connector_streaming_configuration](#get_voice_connector_streaming_configuration)
    - [get_voice_connector_termination](#get_voice_connector_termination)
    - [get_voice_connector_termination_health](#get_voice_connector_termination_health)
    - [invite_users](#invite_users)
    - [list_accounts](#list_accounts)
    - [list_app_instance_admins](#list_app_instance_admins)
    - [list_app_instance_users](#list_app_instance_users)
    - [list_app_instances](#list_app_instances)
    - [list_attendee_tags](#list_attendee_tags)
    - [list_attendees](#list_attendees)
    - [list_bots](#list_bots)
    - [list_channel_bans](#list_channel_bans)
    - [list_channel_memberships](#list_channel_memberships)
    - [list_channel_memberships_for_app_instance_user](#list_channel_memberships_for_app_instance_user)
    - [list_channel_messages](#list_channel_messages)
    - [list_channel_moderators](#list_channel_moderators)
    - [list_channels](#list_channels)
    - [list_channels_moderated_by_app_instance_user](#list_channels_moderated_by_app_instance_user)
    - [list_meeting_tags](#list_meeting_tags)
    - [list_meetings](#list_meetings)
    - [list_phone_number_orders](#list_phone_number_orders)
    - [list_phone_numbers](#list_phone_numbers)
    - [list_proxy_sessions](#list_proxy_sessions)
    - [list_room_memberships](#list_room_memberships)
    - [list_rooms](#list_rooms)
    - [list_sip_media_applications](#list_sip_media_applications)
    - [list_sip_rules](#list_sip_rules)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_users](#list_users)
    - [list_voice_connector_groups](#list_voice_connector_groups)
    - [list_voice_connector_termination_credentials](#list_voice_connector_termination_credentials)
    - [list_voice_connectors](#list_voice_connectors)
    - [logout_user](#logout_user)
    - [put_app_instance_retention_settings](#put_app_instance_retention_settings)
    - [put_app_instance_streaming_configurations](#put_app_instance_streaming_configurations)
    - [put_events_configuration](#put_events_configuration)
    - [put_retention_settings](#put_retention_settings)
    - [put_sip_media_application_logging_configuration](#put_sip_media_application_logging_configuration)
    - [put_voice_connector_emergency_calling_configuration](#put_voice_connector_emergency_calling_configuration)
    - [put_voice_connector_logging_configuration](#put_voice_connector_logging_configuration)
    - [put_voice_connector_origination](#put_voice_connector_origination)
    - [put_voice_connector_proxy](#put_voice_connector_proxy)
    - [put_voice_connector_streaming_configuration](#put_voice_connector_streaming_configuration)
    - [put_voice_connector_termination](#put_voice_connector_termination)
    - [put_voice_connector_termination_credentials](#put_voice_connector_termination_credentials)
    - [redact_channel_message](#redact_channel_message)
    - [redact_conversation_message](#redact_conversation_message)
    - [redact_room_message](#redact_room_message)
    - [regenerate_security_token](#regenerate_security_token)
    - [reset_personal_pin](#reset_personal_pin)
    - [restore_phone_number](#restore_phone_number)
    - [search_available_phone_numbers](#search_available_phone_numbers)
    - [send_channel_message](#send_channel_message)
    - [tag_attendee](#tag_attendee)
    - [tag_meeting](#tag_meeting)
    - [tag_resource](#tag_resource)
    - [untag_attendee](#untag_attendee)
    - [untag_meeting](#untag_meeting)
    - [untag_resource](#untag_resource)
    - [update_account](#update_account)
    - [update_account_settings](#update_account_settings)
    - [update_app_instance](#update_app_instance)
    - [update_app_instance_user](#update_app_instance_user)
    - [update_bot](#update_bot)
    - [update_channel](#update_channel)
    - [update_channel_message](#update_channel_message)
    - [update_channel_read_marker](#update_channel_read_marker)
    - [update_global_settings](#update_global_settings)
    - [update_phone_number](#update_phone_number)
    - [update_phone_number_settings](#update_phone_number_settings)
    - [update_proxy_session](#update_proxy_session)
    - [update_room](#update_room)
    - [update_room_membership](#update_room_membership)
    - [update_sip_media_application](#update_sip_media_application)
    - [update_sip_rule](#update_sip_rule)
    - [update_user](#update_user)
    - [update_user_settings](#update_user_settings)
    - [update_voice_connector](#update_voice_connector)
    - [update_voice_connector_group](#update_voice_connector_group)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)

## ChimeClient

Type annotations for `boto3.client("chime")`

Can be used directly:

```python
from mypy_boto3_chime.client import ChimeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_chime.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ServiceFailureException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottledClientException`
- `Exceptions.UnauthorizedClientException`
- `Exceptions.UnprocessableEntityException`


## Methods


### associate_phone_number_with_user

Type annotations for `boto3.client("chime").associate_phone_number_with_user` method.

[Client.associate_phone_number_with_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.associate_phone_number_with_user)

```python
def associate_phone_number_with_user(
    self,
    AccountId: str,
    UserId: str,
    E164PhoneNumber: str
) -> Dict[str, Any]:
    pass
```

### associate_phone_numbers_with_voice_connector

Type annotations for `boto3.client("chime").associate_phone_numbers_with_voice_connector` method.

[Client.associate_phone_numbers_with_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector)

```python
def associate_phone_numbers_with_voice_connector(
    self,
    VoiceConnectorId: str,
    E164PhoneNumbers: List[str],
    ForceAssociate: bool = None
) -> AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef:
    pass
```

### associate_phone_numbers_with_voice_connector_group

Type annotations for `boto3.client("chime").associate_phone_numbers_with_voice_connector_group` method.

[Client.associate_phone_numbers_with_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.associate_phone_numbers_with_voice_connector_group)

```python
def associate_phone_numbers_with_voice_connector_group(
    self,
    VoiceConnectorGroupId: str,
    E164PhoneNumbers: List[str],
    ForceAssociate: bool = None
) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef:
    pass
```

### associate_signin_delegate_groups_with_account

Type annotations for `boto3.client("chime").associate_signin_delegate_groups_with_account` method.

[Client.associate_signin_delegate_groups_with_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.associate_signin_delegate_groups_with_account)

```python
def associate_signin_delegate_groups_with_account(
    self,
    AccountId: str,
    SigninDelegateGroups: List["SigninDelegateGroupTypeDef"]
) -> Dict[str, Any]:
    pass
```

### batch_create_attendee

Type annotations for `boto3.client("chime").batch_create_attendee` method.

[Client.batch_create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_create_attendee)

```python
def batch_create_attendee(
    self,
    MeetingId: str,
    Attendees: List[CreateAttendeeRequestItemTypeDef]
) -> BatchCreateAttendeeResponseTypeDef:
    pass
```

### batch_create_room_membership

Type annotations for `boto3.client("chime").batch_create_room_membership` method.

[Client.batch_create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_create_room_membership)

```python
def batch_create_room_membership(
    self,
    AccountId: str,
    RoomId: str,
    MembershipItemList: List[MembershipItemTypeDef]
) -> BatchCreateRoomMembershipResponseTypeDef:
    pass
```

### batch_delete_phone_number

Type annotations for `boto3.client("chime").batch_delete_phone_number` method.

[Client.batch_delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_delete_phone_number)

```python
def batch_delete_phone_number(
    self,
    PhoneNumberIds: List[str]
) -> BatchDeletePhoneNumberResponseTypeDef:
    pass
```

### batch_suspend_user

Type annotations for `boto3.client("chime").batch_suspend_user` method.

[Client.batch_suspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_suspend_user)

```python
def batch_suspend_user(
    self,
    AccountId: str,
    UserIdList: List[str]
) -> BatchSuspendUserResponseTypeDef:
    pass
```

### batch_unsuspend_user

Type annotations for `boto3.client("chime").batch_unsuspend_user` method.

[Client.batch_unsuspend_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_unsuspend_user)

```python
def batch_unsuspend_user(
    self,
    AccountId: str,
    UserIdList: List[str]
) -> BatchUnsuspendUserResponseTypeDef:
    pass
```

### batch_update_phone_number

Type annotations for `boto3.client("chime").batch_update_phone_number` method.

[Client.batch_update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_update_phone_number)

```python
def batch_update_phone_number(
    self,
    UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItemTypeDef]
) -> BatchUpdatePhoneNumberResponseTypeDef:
    pass
```

### batch_update_user

Type annotations for `boto3.client("chime").batch_update_user` method.

[Client.batch_update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.batch_update_user)

```python
def batch_update_user(
    self,
    AccountId: str,
    UpdateUserRequestItems: List[UpdateUserRequestItemTypeDef]
) -> BatchUpdateUserResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("chime").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_account

Type annotations for `boto3.client("chime").create_account` method.

[Client.create_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_account)

```python
def create_account(
    self,
    Name: str
) -> CreateAccountResponseTypeDef:
    pass
```

### create_app_instance

Type annotations for `boto3.client("chime").create_app_instance` method.

[Client.create_app_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_app_instance)

```python
def create_app_instance(
    self,
    Name: str,
    ClientRequestToken: str,
    Metadata: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAppInstanceResponseTypeDef:
    pass
```

### create_app_instance_admin

Type annotations for `boto3.client("chime").create_app_instance_admin` method.

[Client.create_app_instance_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_app_instance_admin)

```python
def create_app_instance_admin(
    self,
    AppInstanceAdminArn: str,
    AppInstanceArn: str
) -> CreateAppInstanceAdminResponseTypeDef:
    pass
```

### create_app_instance_user

Type annotations for `boto3.client("chime").create_app_instance_user` method.

[Client.create_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_app_instance_user)

```python
def create_app_instance_user(
    self,
    AppInstanceArn: str,
    AppInstanceUserId: str,
    Name: str,
    ClientRequestToken: str,
    Metadata: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateAppInstanceUserResponseTypeDef:
    pass
```

### create_attendee

Type annotations for `boto3.client("chime").create_attendee` method.

[Client.create_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_attendee)

```python
def create_attendee(
    self,
    MeetingId: str,
    ExternalUserId: str,
    Tags: List["TagTypeDef"] = None
) -> CreateAttendeeResponseTypeDef:
    pass
```

### create_bot

Type annotations for `boto3.client("chime").create_bot` method.

[Client.create_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_bot)

```python
def create_bot(
    self,
    AccountId: str,
    DisplayName: str,
    Domain: str = None
) -> CreateBotResponseTypeDef:
    pass
```

### create_channel

Type annotations for `boto3.client("chime").create_channel` method.

[Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_channel)

```python
def create_channel(
    self,
    AppInstanceArn: str,
    Name: str,
    ClientRequestToken: str,
    Mode: ChannelMode = None,
    Privacy: ChannelPrivacy = None,
    Metadata: str = None,
    Tags: List["TagTypeDef"] = None,
    ChimeBearer: str = None
) -> CreateChannelResponseTypeDef:
    pass
```

### create_channel_ban

Type annotations for `boto3.client("chime").create_channel_ban` method.

[Client.create_channel_ban documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_channel_ban)

```python
def create_channel_ban(
    self,
    ChannelArn: str,
    MemberArn: str,
    ChimeBearer: str = None
) -> CreateChannelBanResponseTypeDef:
    pass
```

### create_channel_membership

Type annotations for `boto3.client("chime").create_channel_membership` method.

[Client.create_channel_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_channel_membership)

```python
def create_channel_membership(
    self,
    ChannelArn: str,
    MemberArn: str,
    Type: ChannelMembershipType,
    ChimeBearer: str = None
) -> CreateChannelMembershipResponseTypeDef:
    pass
```

### create_channel_moderator

Type annotations for `boto3.client("chime").create_channel_moderator` method.

[Client.create_channel_moderator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_channel_moderator)

```python
def create_channel_moderator(
    self,
    ChannelArn: str,
    ChannelModeratorArn: str,
    ChimeBearer: str = None
) -> CreateChannelModeratorResponseTypeDef:
    pass
```

### create_meeting

Type annotations for `boto3.client("chime").create_meeting` method.

[Client.create_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_meeting)

```python
def create_meeting(
    self,
    ClientRequestToken: str,
    ExternalMeetingId: str = None,
    MeetingHostId: str = None,
    MediaRegion: str = None,
    Tags: List["TagTypeDef"] = None,
    NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None
) -> CreateMeetingResponseTypeDef:
    pass
```

### create_meeting_dial_out

Type annotations for `boto3.client("chime").create_meeting_dial_out` method.

[Client.create_meeting_dial_out documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_meeting_dial_out)

```python
def create_meeting_dial_out(
    self,
    MeetingId: str,
    FromPhoneNumber: str,
    ToPhoneNumber: str,
    JoinToken: str
) -> CreateMeetingDialOutResponseTypeDef:
    pass
```

### create_meeting_with_attendees

Type annotations for `boto3.client("chime").create_meeting_with_attendees` method.

[Client.create_meeting_with_attendees documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_meeting_with_attendees)

```python
def create_meeting_with_attendees(
    self,
    ClientRequestToken: str,
    ExternalMeetingId: str = None,
    MeetingHostId: str = None,
    MediaRegion: str = None,
    Tags: List["TagTypeDef"] = None,
    NotificationsConfiguration: MeetingNotificationConfigurationTypeDef = None,
    Attendees: List[CreateAttendeeRequestItemTypeDef] = None
) -> CreateMeetingWithAttendeesResponseTypeDef:
    pass
```

### create_phone_number_order

Type annotations for `boto3.client("chime").create_phone_number_order` method.

[Client.create_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_phone_number_order)

```python
def create_phone_number_order(
    self,
    ProductType: PhoneNumberProductType,
    E164PhoneNumbers: List[str]
) -> CreatePhoneNumberOrderResponseTypeDef:
    pass
```

### create_proxy_session

Type annotations for `boto3.client("chime").create_proxy_session` method.

[Client.create_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_proxy_session)

```python
def create_proxy_session(
    self,
    VoiceConnectorId: str,
    ParticipantPhoneNumbers: List[str],
    Capabilities: List[Capability],
    Name: str = None,
    ExpiryMinutes: int = None,
    NumberSelectionBehavior: NumberSelectionBehavior = None,
    GeoMatchLevel: GeoMatchLevel = None,
    GeoMatchParams: "GeoMatchParamsTypeDef" = None
) -> CreateProxySessionResponseTypeDef:
    pass
```

### create_room

Type annotations for `boto3.client("chime").create_room` method.

[Client.create_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_room)

```python
def create_room(
    self,
    AccountId: str,
    Name: str,
    ClientRequestToken: str = None
) -> CreateRoomResponseTypeDef:
    pass
```

### create_room_membership

Type annotations for `boto3.client("chime").create_room_membership` method.

[Client.create_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_room_membership)

```python
def create_room_membership(
    self,
    AccountId: str,
    RoomId: str,
    MemberId: str,
    Role: RoomMembershipRole = None
) -> CreateRoomMembershipResponseTypeDef:
    pass
```

### create_sip_media_application

Type annotations for `boto3.client("chime").create_sip_media_application` method.

[Client.create_sip_media_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_sip_media_application)

```python
def create_sip_media_application(
    self,
    AwsRegion: str,
    Name: str,
    Endpoints: List["SipMediaApplicationEndpointTypeDef"]
) -> CreateSipMediaApplicationResponseTypeDef:
    pass
```

### create_sip_media_application_call

Type annotations for `boto3.client("chime").create_sip_media_application_call` method.

[Client.create_sip_media_application_call documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_sip_media_application_call)

```python
def create_sip_media_application_call(
    self,
    FromPhoneNumber: str,
    ToPhoneNumber: str,
    SipMediaApplicationId: str
) -> CreateSipMediaApplicationCallResponseTypeDef:
    pass
```

### create_sip_rule

Type annotations for `boto3.client("chime").create_sip_rule` method.

[Client.create_sip_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_sip_rule)

```python
def create_sip_rule(
    self,
    Name: str,
    TriggerType: SipRuleTriggerType,
    TriggerValue: str,
    TargetApplications: List["SipRuleTargetApplicationTypeDef"],
    Disabled: bool = None
) -> CreateSipRuleResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("chime").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_user)

```python
def create_user(
    self,
    AccountId: str,
    Username: str = None,
    Email: str = None,
    UserType: UserType = None
) -> CreateUserResponseTypeDef:
    pass
```

### create_voice_connector

Type annotations for `boto3.client("chime").create_voice_connector` method.

[Client.create_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_voice_connector)

```python
def create_voice_connector(
    self,
    Name: str,
    RequireEncryption: bool,
    AwsRegion: VoiceConnectorAwsRegion = None
) -> CreateVoiceConnectorResponseTypeDef:
    pass
```

### create_voice_connector_group

Type annotations for `boto3.client("chime").create_voice_connector_group` method.

[Client.create_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.create_voice_connector_group)

```python
def create_voice_connector_group(
    self,
    Name: str,
    VoiceConnectorItems: List["VoiceConnectorItemTypeDef"] = None
) -> CreateVoiceConnectorGroupResponseTypeDef:
    pass
```

### delete_account

Type annotations for `boto3.client("chime").delete_account` method.

[Client.delete_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_account)

```python
def delete_account(
    self,
    AccountId: str
) -> Dict[str, Any]:
    pass
```

### delete_app_instance

Type annotations for `boto3.client("chime").delete_app_instance` method.

[Client.delete_app_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_app_instance)

```python
def delete_app_instance(
    self,
    AppInstanceArn: str
) -> None:
    pass
```

### delete_app_instance_admin

Type annotations for `boto3.client("chime").delete_app_instance_admin` method.

[Client.delete_app_instance_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_app_instance_admin)

```python
def delete_app_instance_admin(
    self,
    AppInstanceAdminArn: str,
    AppInstanceArn: str
) -> None:
    pass
```

### delete_app_instance_streaming_configurations

Type annotations for `boto3.client("chime").delete_app_instance_streaming_configurations` method.

[Client.delete_app_instance_streaming_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_app_instance_streaming_configurations)

```python
def delete_app_instance_streaming_configurations(
    self,
    AppInstanceArn: str
) -> None:
    pass
```

### delete_app_instance_user

Type annotations for `boto3.client("chime").delete_app_instance_user` method.

[Client.delete_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_app_instance_user)

```python
def delete_app_instance_user(
    self,
    AppInstanceUserArn: str
) -> None:
    pass
```

### delete_attendee

Type annotations for `boto3.client("chime").delete_attendee` method.

[Client.delete_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_attendee)

```python
def delete_attendee(
    self,
    MeetingId: str,
    AttendeeId: str
) -> None:
    pass
```

### delete_channel

Type annotations for `boto3.client("chime").delete_channel` method.

[Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_channel)

```python
def delete_channel(
    self,
    ChannelArn: str,
    ChimeBearer: str = None
) -> None:
    pass
```

### delete_channel_ban

Type annotations for `boto3.client("chime").delete_channel_ban` method.

[Client.delete_channel_ban documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_channel_ban)

```python
def delete_channel_ban(
    self,
    ChannelArn: str,
    MemberArn: str,
    ChimeBearer: str = None
) -> None:
    pass
```

### delete_channel_membership

Type annotations for `boto3.client("chime").delete_channel_membership` method.

[Client.delete_channel_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_channel_membership)

```python
def delete_channel_membership(
    self,
    ChannelArn: str,
    MemberArn: str,
    ChimeBearer: str = None
) -> None:
    pass
```

### delete_channel_message

Type annotations for `boto3.client("chime").delete_channel_message` method.

[Client.delete_channel_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_channel_message)

```python
def delete_channel_message(
    self,
    ChannelArn: str,
    MessageId: str,
    ChimeBearer: str = None
) -> None:
    pass
```

### delete_channel_moderator

Type annotations for `boto3.client("chime").delete_channel_moderator` method.

[Client.delete_channel_moderator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_channel_moderator)

```python
def delete_channel_moderator(
    self,
    ChannelArn: str,
    ChannelModeratorArn: str,
    ChimeBearer: str = None
) -> None:
    pass
```

### delete_events_configuration

Type annotations for `boto3.client("chime").delete_events_configuration` method.

[Client.delete_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_events_configuration)

```python
def delete_events_configuration(
    self,
    AccountId: str,
    BotId: str
) -> None:
    pass
```

### delete_meeting

Type annotations for `boto3.client("chime").delete_meeting` method.

[Client.delete_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_meeting)

```python
def delete_meeting(
    self,
    MeetingId: str
) -> None:
    pass
```

### delete_phone_number

Type annotations for `boto3.client("chime").delete_phone_number` method.

[Client.delete_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_phone_number)

```python
def delete_phone_number(
    self,
    PhoneNumberId: str
) -> None:
    pass
```

### delete_proxy_session

Type annotations for `boto3.client("chime").delete_proxy_session` method.

[Client.delete_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_proxy_session)

```python
def delete_proxy_session(
    self,
    VoiceConnectorId: str,
    ProxySessionId: str
) -> None:
    pass
```

### delete_room

Type annotations for `boto3.client("chime").delete_room` method.

[Client.delete_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_room)

```python
def delete_room(
    self,
    AccountId: str,
    RoomId: str
) -> None:
    pass
```

### delete_room_membership

Type annotations for `boto3.client("chime").delete_room_membership` method.

[Client.delete_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_room_membership)

```python
def delete_room_membership(
    self,
    AccountId: str,
    RoomId: str,
    MemberId: str
) -> None:
    pass
```

### delete_sip_media_application

Type annotations for `boto3.client("chime").delete_sip_media_application` method.

[Client.delete_sip_media_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_sip_media_application)

```python
def delete_sip_media_application(
    self,
    SipMediaApplicationId: str
) -> None:
    pass
```

### delete_sip_rule

Type annotations for `boto3.client("chime").delete_sip_rule` method.

[Client.delete_sip_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_sip_rule)

```python
def delete_sip_rule(
    self,
    SipRuleId: str
) -> None:
    pass
```

### delete_voice_connector

Type annotations for `boto3.client("chime").delete_voice_connector` method.

[Client.delete_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector)

```python
def delete_voice_connector(
    self,
    VoiceConnectorId: str
) -> None:
    pass
```

### delete_voice_connector_emergency_calling_configuration

Type annotations for `boto3.client("chime").delete_voice_connector_emergency_calling_configuration` method.

[Client.delete_voice_connector_emergency_calling_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_emergency_calling_configuration)

```python
def delete_voice_connector_emergency_calling_configuration(
    self,
    VoiceConnectorId: str
) -> None:
    pass
```

### delete_voice_connector_group

Type annotations for `boto3.client("chime").delete_voice_connector_group` method.

[Client.delete_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_group)

```python
def delete_voice_connector_group(
    self,
    VoiceConnectorGroupId: str
) -> None:
    pass
```

### delete_voice_connector_origination

Type annotations for `boto3.client("chime").delete_voice_connector_origination` method.

[Client.delete_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_origination)

```python
def delete_voice_connector_origination(
    self,
    VoiceConnectorId: str
) -> None:
    pass
```

### delete_voice_connector_proxy

Type annotations for `boto3.client("chime").delete_voice_connector_proxy` method.

[Client.delete_voice_connector_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_proxy)

```python
def delete_voice_connector_proxy(
    self,
    VoiceConnectorId: str
) -> None:
    pass
```

### delete_voice_connector_streaming_configuration

Type annotations for `boto3.client("chime").delete_voice_connector_streaming_configuration` method.

[Client.delete_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_streaming_configuration)

```python
def delete_voice_connector_streaming_configuration(
    self,
    VoiceConnectorId: str
) -> None:
    pass
```

### delete_voice_connector_termination

Type annotations for `boto3.client("chime").delete_voice_connector_termination` method.

[Client.delete_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_termination)

```python
def delete_voice_connector_termination(
    self,
    VoiceConnectorId: str
) -> None:
    pass
```

### delete_voice_connector_termination_credentials

Type annotations for `boto3.client("chime").delete_voice_connector_termination_credentials` method.

[Client.delete_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.delete_voice_connector_termination_credentials)

```python
def delete_voice_connector_termination_credentials(
    self,
    VoiceConnectorId: str,
    Usernames: List[str]
) -> None:
    pass
```

### describe_app_instance

Type annotations for `boto3.client("chime").describe_app_instance` method.

[Client.describe_app_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_app_instance)

```python
def describe_app_instance(
    self,
    AppInstanceArn: str
) -> DescribeAppInstanceResponseTypeDef:
    pass
```

### describe_app_instance_admin

Type annotations for `boto3.client("chime").describe_app_instance_admin` method.

[Client.describe_app_instance_admin documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_app_instance_admin)

```python
def describe_app_instance_admin(
    self,
    AppInstanceAdminArn: str,
    AppInstanceArn: str
) -> DescribeAppInstanceAdminResponseTypeDef:
    pass
```

### describe_app_instance_user

Type annotations for `boto3.client("chime").describe_app_instance_user` method.

[Client.describe_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_app_instance_user)

```python
def describe_app_instance_user(
    self,
    AppInstanceUserArn: str
) -> DescribeAppInstanceUserResponseTypeDef:
    pass
```

### describe_channel

Type annotations for `boto3.client("chime").describe_channel` method.

[Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_channel)

```python
def describe_channel(
    self,
    ChannelArn: str,
    ChimeBearer: str = None
) -> DescribeChannelResponseTypeDef:
    pass
```

### describe_channel_ban

Type annotations for `boto3.client("chime").describe_channel_ban` method.

[Client.describe_channel_ban documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_channel_ban)

```python
def describe_channel_ban(
    self,
    ChannelArn: str,
    MemberArn: str,
    ChimeBearer: str = None
) -> DescribeChannelBanResponseTypeDef:
    pass
```

### describe_channel_membership

Type annotations for `boto3.client("chime").describe_channel_membership` method.

[Client.describe_channel_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_channel_membership)

```python
def describe_channel_membership(
    self,
    ChannelArn: str,
    MemberArn: str,
    ChimeBearer: str = None
) -> DescribeChannelMembershipResponseTypeDef:
    pass
```

### describe_channel_membership_for_app_instance_user

Type annotations for `boto3.client("chime").describe_channel_membership_for_app_instance_user` method.

[Client.describe_channel_membership_for_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_channel_membership_for_app_instance_user)

```python
def describe_channel_membership_for_app_instance_user(
    self,
    ChannelArn: str,
    AppInstanceUserArn: str,
    ChimeBearer: str = None
) -> DescribeChannelMembershipForAppInstanceUserResponseTypeDef:
    pass
```

### describe_channel_moderated_by_app_instance_user

Type annotations for `boto3.client("chime").describe_channel_moderated_by_app_instance_user` method.

[Client.describe_channel_moderated_by_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_channel_moderated_by_app_instance_user)

```python
def describe_channel_moderated_by_app_instance_user(
    self,
    ChannelArn: str,
    AppInstanceUserArn: str,
    ChimeBearer: str = None
) -> DescribeChannelModeratedByAppInstanceUserResponseTypeDef:
    pass
```

### describe_channel_moderator

Type annotations for `boto3.client("chime").describe_channel_moderator` method.

[Client.describe_channel_moderator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.describe_channel_moderator)

```python
def describe_channel_moderator(
    self,
    ChannelArn: str,
    ChannelModeratorArn: str,
    ChimeBearer: str = None
) -> DescribeChannelModeratorResponseTypeDef:
    pass
```

### disassociate_phone_number_from_user

Type annotations for `boto3.client("chime").disassociate_phone_number_from_user` method.

[Client.disassociate_phone_number_from_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.disassociate_phone_number_from_user)

```python
def disassociate_phone_number_from_user(
    self,
    AccountId: str,
    UserId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_phone_numbers_from_voice_connector

Type annotations for `boto3.client("chime").disassociate_phone_numbers_from_voice_connector` method.

[Client.disassociate_phone_numbers_from_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector)

```python
def disassociate_phone_numbers_from_voice_connector(
    self,
    VoiceConnectorId: str,
    E164PhoneNumbers: List[str]
) -> DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef:
    pass
```

### disassociate_phone_numbers_from_voice_connector_group

Type annotations for `boto3.client("chime").disassociate_phone_numbers_from_voice_connector_group` method.

[Client.disassociate_phone_numbers_from_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.disassociate_phone_numbers_from_voice_connector_group)

```python
def disassociate_phone_numbers_from_voice_connector_group(
    self,
    VoiceConnectorGroupId: str,
    E164PhoneNumbers: List[str]
) -> DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef:
    pass
```

### disassociate_signin_delegate_groups_from_account

Type annotations for `boto3.client("chime").disassociate_signin_delegate_groups_from_account` method.

[Client.disassociate_signin_delegate_groups_from_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.disassociate_signin_delegate_groups_from_account)

```python
def disassociate_signin_delegate_groups_from_account(
    self,
    AccountId: str,
    GroupNames: List[str]
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("chime").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.generate_presigned_url)

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

### get_account

Type annotations for `boto3.client("chime").get_account` method.

[Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_account)

```python
def get_account(
    self,
    AccountId: str
) -> GetAccountResponseTypeDef:
    pass
```

### get_account_settings

Type annotations for `boto3.client("chime").get_account_settings` method.

[Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_account_settings)

```python
def get_account_settings(
    self,
    AccountId: str
) -> GetAccountSettingsResponseTypeDef:
    pass
```

### get_app_instance_retention_settings

Type annotations for `boto3.client("chime").get_app_instance_retention_settings` method.

[Client.get_app_instance_retention_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_app_instance_retention_settings)

```python
def get_app_instance_retention_settings(
    self,
    AppInstanceArn: str
) -> GetAppInstanceRetentionSettingsResponseTypeDef:
    pass
```

### get_app_instance_streaming_configurations

Type annotations for `boto3.client("chime").get_app_instance_streaming_configurations` method.

[Client.get_app_instance_streaming_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_app_instance_streaming_configurations)

```python
def get_app_instance_streaming_configurations(
    self,
    AppInstanceArn: str
) -> GetAppInstanceStreamingConfigurationsResponseTypeDef:
    pass
```

### get_attendee

Type annotations for `boto3.client("chime").get_attendee` method.

[Client.get_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_attendee)

```python
def get_attendee(
    self,
    MeetingId: str,
    AttendeeId: str
) -> GetAttendeeResponseTypeDef:
    pass
```

### get_bot

Type annotations for `boto3.client("chime").get_bot` method.

[Client.get_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_bot)

```python
def get_bot(
    self,
    AccountId: str,
    BotId: str
) -> GetBotResponseTypeDef:
    pass
```

### get_channel_message

Type annotations for `boto3.client("chime").get_channel_message` method.

[Client.get_channel_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_channel_message)

```python
def get_channel_message(
    self,
    ChannelArn: str,
    MessageId: str,
    ChimeBearer: str = None
) -> GetChannelMessageResponseTypeDef:
    pass
```

### get_events_configuration

Type annotations for `boto3.client("chime").get_events_configuration` method.

[Client.get_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_events_configuration)

```python
def get_events_configuration(
    self,
    AccountId: str,
    BotId: str
) -> GetEventsConfigurationResponseTypeDef:
    pass
```

### get_global_settings

Type annotations for `boto3.client("chime").get_global_settings` method.

[Client.get_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_global_settings)

```python
def get_global_settings(
    self
) -> GetGlobalSettingsResponseTypeDef:
    pass
```

### get_meeting

Type annotations for `boto3.client("chime").get_meeting` method.

[Client.get_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_meeting)

```python
def get_meeting(
    self,
    MeetingId: str
) -> GetMeetingResponseTypeDef:
    pass
```

### get_messaging_session_endpoint

Type annotations for `boto3.client("chime").get_messaging_session_endpoint` method.

[Client.get_messaging_session_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_messaging_session_endpoint)

```python
def get_messaging_session_endpoint(
    self
) -> GetMessagingSessionEndpointResponseTypeDef:
    pass
```

### get_phone_number

Type annotations for `boto3.client("chime").get_phone_number` method.

[Client.get_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_phone_number)

```python
def get_phone_number(
    self,
    PhoneNumberId: str
) -> GetPhoneNumberResponseTypeDef:
    pass
```

### get_phone_number_order

Type annotations for `boto3.client("chime").get_phone_number_order` method.

[Client.get_phone_number_order documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_phone_number_order)

```python
def get_phone_number_order(
    self,
    PhoneNumberOrderId: str
) -> GetPhoneNumberOrderResponseTypeDef:
    pass
```

### get_phone_number_settings

Type annotations for `boto3.client("chime").get_phone_number_settings` method.

[Client.get_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_phone_number_settings)

```python
def get_phone_number_settings(
    self
) -> GetPhoneNumberSettingsResponseTypeDef:
    pass
```

### get_proxy_session

Type annotations for `boto3.client("chime").get_proxy_session` method.

[Client.get_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_proxy_session)

```python
def get_proxy_session(
    self,
    VoiceConnectorId: str,
    ProxySessionId: str
) -> GetProxySessionResponseTypeDef:
    pass
```

### get_retention_settings

Type annotations for `boto3.client("chime").get_retention_settings` method.

[Client.get_retention_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_retention_settings)

```python
def get_retention_settings(
    self,
    AccountId: str
) -> GetRetentionSettingsResponseTypeDef:
    pass
```

### get_room

Type annotations for `boto3.client("chime").get_room` method.

[Client.get_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_room)

```python
def get_room(
    self,
    AccountId: str,
    RoomId: str
) -> GetRoomResponseTypeDef:
    pass
```

### get_sip_media_application

Type annotations for `boto3.client("chime").get_sip_media_application` method.

[Client.get_sip_media_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_sip_media_application)

```python
def get_sip_media_application(
    self,
    SipMediaApplicationId: str
) -> GetSipMediaApplicationResponseTypeDef:
    pass
```

### get_sip_media_application_logging_configuration

Type annotations for `boto3.client("chime").get_sip_media_application_logging_configuration` method.

[Client.get_sip_media_application_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_sip_media_application_logging_configuration)

```python
def get_sip_media_application_logging_configuration(
    self,
    SipMediaApplicationId: str
) -> GetSipMediaApplicationLoggingConfigurationResponseTypeDef:
    pass
```

### get_sip_rule

Type annotations for `boto3.client("chime").get_sip_rule` method.

[Client.get_sip_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_sip_rule)

```python
def get_sip_rule(
    self,
    SipRuleId: str
) -> GetSipRuleResponseTypeDef:
    pass
```

### get_user

Type annotations for `boto3.client("chime").get_user` method.

[Client.get_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_user)

```python
def get_user(
    self,
    AccountId: str,
    UserId: str
) -> GetUserResponseTypeDef:
    pass
```

### get_user_settings

Type annotations for `boto3.client("chime").get_user_settings` method.

[Client.get_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_user_settings)

```python
def get_user_settings(
    self,
    AccountId: str,
    UserId: str
) -> GetUserSettingsResponseTypeDef:
    pass
```

### get_voice_connector

Type annotations for `boto3.client("chime").get_voice_connector` method.

[Client.get_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector)

```python
def get_voice_connector(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorResponseTypeDef:
    pass
```

### get_voice_connector_emergency_calling_configuration

Type annotations for `boto3.client("chime").get_voice_connector_emergency_calling_configuration` method.

[Client.get_voice_connector_emergency_calling_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_emergency_calling_configuration)

```python
def get_voice_connector_emergency_calling_configuration(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
    pass
```

### get_voice_connector_group

Type annotations for `boto3.client("chime").get_voice_connector_group` method.

[Client.get_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_group)

```python
def get_voice_connector_group(
    self,
    VoiceConnectorGroupId: str
) -> GetVoiceConnectorGroupResponseTypeDef:
    pass
```

### get_voice_connector_logging_configuration

Type annotations for `boto3.client("chime").get_voice_connector_logging_configuration` method.

[Client.get_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_logging_configuration)

```python
def get_voice_connector_logging_configuration(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorLoggingConfigurationResponseTypeDef:
    pass
```

### get_voice_connector_origination

Type annotations for `boto3.client("chime").get_voice_connector_origination` method.

[Client.get_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_origination)

```python
def get_voice_connector_origination(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorOriginationResponseTypeDef:
    pass
```

### get_voice_connector_proxy

Type annotations for `boto3.client("chime").get_voice_connector_proxy` method.

[Client.get_voice_connector_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_proxy)

```python
def get_voice_connector_proxy(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorProxyResponseTypeDef:
    pass
```

### get_voice_connector_streaming_configuration

Type annotations for `boto3.client("chime").get_voice_connector_streaming_configuration` method.

[Client.get_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_streaming_configuration)

```python
def get_voice_connector_streaming_configuration(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorStreamingConfigurationResponseTypeDef:
    pass
```

### get_voice_connector_termination

Type annotations for `boto3.client("chime").get_voice_connector_termination` method.

[Client.get_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_termination)

```python
def get_voice_connector_termination(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorTerminationResponseTypeDef:
    pass
```

### get_voice_connector_termination_health

Type annotations for `boto3.client("chime").get_voice_connector_termination_health` method.

[Client.get_voice_connector_termination_health documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.get_voice_connector_termination_health)

```python
def get_voice_connector_termination_health(
    self,
    VoiceConnectorId: str
) -> GetVoiceConnectorTerminationHealthResponseTypeDef:
    pass
```

### invite_users

Type annotations for `boto3.client("chime").invite_users` method.

[Client.invite_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.invite_users)

```python
def invite_users(
    self,
    AccountId: str,
    UserEmailList: List[str],
    UserType: UserType = None
) -> InviteUsersResponseTypeDef:
    pass
```

### list_accounts

Type annotations for `boto3.client("chime").list_accounts` method.

[Client.list_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_accounts)

```python
def list_accounts(
    self,
    Name: str = None,
    UserEmail: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAccountsResponseTypeDef:
    pass
```

### list_app_instance_admins

Type annotations for `boto3.client("chime").list_app_instance_admins` method.

[Client.list_app_instance_admins documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_app_instance_admins)

```python
def list_app_instance_admins(
    self,
    AppInstanceArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAppInstanceAdminsResponseTypeDef:
    pass
```

### list_app_instance_users

Type annotations for `boto3.client("chime").list_app_instance_users` method.

[Client.list_app_instance_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_app_instance_users)

```python
def list_app_instance_users(
    self,
    AppInstanceArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAppInstanceUsersResponseTypeDef:
    pass
```

### list_app_instances

Type annotations for `boto3.client("chime").list_app_instances` method.

[Client.list_app_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_app_instances)

```python
def list_app_instances(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAppInstancesResponseTypeDef:
    pass
```

### list_attendee_tags

Type annotations for `boto3.client("chime").list_attendee_tags` method.

[Client.list_attendee_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_attendee_tags)

```python
def list_attendee_tags(
    self,
    MeetingId: str,
    AttendeeId: str
) -> ListAttendeeTagsResponseTypeDef:
    pass
```

### list_attendees

Type annotations for `boto3.client("chime").list_attendees` method.

[Client.list_attendees documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_attendees)

```python
def list_attendees(
    self,
    MeetingId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAttendeesResponseTypeDef:
    pass
```

### list_bots

Type annotations for `boto3.client("chime").list_bots` method.

[Client.list_bots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_bots)

```python
def list_bots(
    self,
    AccountId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListBotsResponseTypeDef:
    pass
```

### list_channel_bans

Type annotations for `boto3.client("chime").list_channel_bans` method.

[Client.list_channel_bans documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channel_bans)

```python
def list_channel_bans(
    self,
    ChannelArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelBansResponseTypeDef:
    pass
```

### list_channel_memberships

Type annotations for `boto3.client("chime").list_channel_memberships` method.

[Client.list_channel_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channel_memberships)

```python
def list_channel_memberships(
    self,
    ChannelArn: str,
    Type: ChannelMembershipType = None,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelMembershipsResponseTypeDef:
    pass
```

### list_channel_memberships_for_app_instance_user

Type annotations for `boto3.client("chime").list_channel_memberships_for_app_instance_user` method.

[Client.list_channel_memberships_for_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channel_memberships_for_app_instance_user)

```python
def list_channel_memberships_for_app_instance_user(
    self,
    AppInstanceUserArn: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelMembershipsForAppInstanceUserResponseTypeDef:
    pass
```

### list_channel_messages

Type annotations for `boto3.client("chime").list_channel_messages` method.

[Client.list_channel_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channel_messages)

```python
def list_channel_messages(
    self,
    ChannelArn: str,
    SortOrder: SortOrder = None,
    NotBefore: datetime = None,
    NotAfter: datetime = None,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelMessagesResponseTypeDef:
    pass
```

### list_channel_moderators

Type annotations for `boto3.client("chime").list_channel_moderators` method.

[Client.list_channel_moderators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channel_moderators)

```python
def list_channel_moderators(
    self,
    ChannelArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelModeratorsResponseTypeDef:
    pass
```

### list_channels

Type annotations for `boto3.client("chime").list_channels` method.

[Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channels)

```python
def list_channels(
    self,
    AppInstanceArn: str,
    Privacy: ChannelPrivacy = None,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelsResponseTypeDef:
    pass
```

### list_channels_moderated_by_app_instance_user

Type annotations for `boto3.client("chime").list_channels_moderated_by_app_instance_user` method.

[Client.list_channels_moderated_by_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_channels_moderated_by_app_instance_user)

```python
def list_channels_moderated_by_app_instance_user(
    self,
    AppInstanceUserArn: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    ChimeBearer: str = None
) -> ListChannelsModeratedByAppInstanceUserResponseTypeDef:
    pass
```

### list_meeting_tags

Type annotations for `boto3.client("chime").list_meeting_tags` method.

[Client.list_meeting_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_meeting_tags)

```python
def list_meeting_tags(
    self,
    MeetingId: str
) -> ListMeetingTagsResponseTypeDef:
    pass
```

### list_meetings

Type annotations for `boto3.client("chime").list_meetings` method.

[Client.list_meetings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_meetings)

```python
def list_meetings(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMeetingsResponseTypeDef:
    pass
```

### list_phone_number_orders

Type annotations for `boto3.client("chime").list_phone_number_orders` method.

[Client.list_phone_number_orders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_phone_number_orders)

```python
def list_phone_number_orders(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPhoneNumberOrdersResponseTypeDef:
    pass
```

### list_phone_numbers

Type annotations for `boto3.client("chime").list_phone_numbers` method.

[Client.list_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_phone_numbers)

```python
def list_phone_numbers(
    self,
    Status: PhoneNumberStatus = None,
    ProductType: PhoneNumberProductType = None,
    FilterName: PhoneNumberAssociationName = None,
    FilterValue: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPhoneNumbersResponseTypeDef:
    pass
```

### list_proxy_sessions

Type annotations for `boto3.client("chime").list_proxy_sessions` method.

[Client.list_proxy_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_proxy_sessions)

```python
def list_proxy_sessions(
    self,
    VoiceConnectorId: str,
    Status: ProxySessionStatus = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProxySessionsResponseTypeDef:
    pass
```

### list_room_memberships

Type annotations for `boto3.client("chime").list_room_memberships` method.

[Client.list_room_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_room_memberships)

```python
def list_room_memberships(
    self,
    AccountId: str,
    RoomId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRoomMembershipsResponseTypeDef:
    pass
```

### list_rooms

Type annotations for `boto3.client("chime").list_rooms` method.

[Client.list_rooms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_rooms)

```python
def list_rooms(
    self,
    AccountId: str,
    MemberId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRoomsResponseTypeDef:
    pass
```

### list_sip_media_applications

Type annotations for `boto3.client("chime").list_sip_media_applications` method.

[Client.list_sip_media_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_sip_media_applications)

```python
def list_sip_media_applications(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSipMediaApplicationsResponseTypeDef:
    pass
```

### list_sip_rules

Type annotations for `boto3.client("chime").list_sip_rules` method.

[Client.list_sip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_sip_rules)

```python
def list_sip_rules(
    self,
    SipMediaApplicationId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSipRulesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("chime").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("chime").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_users)

```python
def list_users(
    self,
    AccountId: str,
    UserEmail: str = None,
    UserType: UserType = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListUsersResponseTypeDef:
    pass
```

### list_voice_connector_groups

Type annotations for `boto3.client("chime").list_voice_connector_groups` method.

[Client.list_voice_connector_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_voice_connector_groups)

```python
def list_voice_connector_groups(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListVoiceConnectorGroupsResponseTypeDef:
    pass
```

### list_voice_connector_termination_credentials

Type annotations for `boto3.client("chime").list_voice_connector_termination_credentials` method.

[Client.list_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_voice_connector_termination_credentials)

```python
def list_voice_connector_termination_credentials(
    self,
    VoiceConnectorId: str
) -> ListVoiceConnectorTerminationCredentialsResponseTypeDef:
    pass
```

### list_voice_connectors

Type annotations for `boto3.client("chime").list_voice_connectors` method.

[Client.list_voice_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.list_voice_connectors)

```python
def list_voice_connectors(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListVoiceConnectorsResponseTypeDef:
    pass
```

### logout_user

Type annotations for `boto3.client("chime").logout_user` method.

[Client.logout_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.logout_user)

```python
def logout_user(
    self,
    AccountId: str,
    UserId: str
) -> Dict[str, Any]:
    pass
```

### put_app_instance_retention_settings

Type annotations for `boto3.client("chime").put_app_instance_retention_settings` method.

[Client.put_app_instance_retention_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_app_instance_retention_settings)

```python
def put_app_instance_retention_settings(
    self,
    AppInstanceArn: str,
    AppInstanceRetentionSettings: "AppInstanceRetentionSettingsTypeDef"
) -> PutAppInstanceRetentionSettingsResponseTypeDef:
    pass
```

### put_app_instance_streaming_configurations

Type annotations for `boto3.client("chime").put_app_instance_streaming_configurations` method.

[Client.put_app_instance_streaming_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_app_instance_streaming_configurations)

```python
def put_app_instance_streaming_configurations(
    self,
    AppInstanceArn: str,
    AppInstanceStreamingConfigurations: List["AppInstanceStreamingConfigurationTypeDef"]
) -> PutAppInstanceStreamingConfigurationsResponseTypeDef:
    pass
```

### put_events_configuration

Type annotations for `boto3.client("chime").put_events_configuration` method.

[Client.put_events_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_events_configuration)

```python
def put_events_configuration(
    self,
    AccountId: str,
    BotId: str,
    OutboundEventsHTTPSEndpoint: str = None,
    LambdaFunctionArn: str = None
) -> PutEventsConfigurationResponseTypeDef:
    pass
```

### put_retention_settings

Type annotations for `boto3.client("chime").put_retention_settings` method.

[Client.put_retention_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_retention_settings)

```python
def put_retention_settings(
    self,
    AccountId: str,
    RetentionSettings: "RetentionSettingsTypeDef"
) -> PutRetentionSettingsResponseTypeDef:
    pass
```

### put_sip_media_application_logging_configuration

Type annotations for `boto3.client("chime").put_sip_media_application_logging_configuration` method.

[Client.put_sip_media_application_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_sip_media_application_logging_configuration)

```python
def put_sip_media_application_logging_configuration(
    self,
    SipMediaApplicationId: str,
    SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef" = None
) -> PutSipMediaApplicationLoggingConfigurationResponseTypeDef:
    pass
```

### put_voice_connector_emergency_calling_configuration

Type annotations for `boto3.client("chime").put_voice_connector_emergency_calling_configuration` method.

[Client.put_voice_connector_emergency_calling_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_emergency_calling_configuration)

```python
def put_voice_connector_emergency_calling_configuration(
    self,
    VoiceConnectorId: str,
    EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"
) -> PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef:
    pass
```

### put_voice_connector_logging_configuration

Type annotations for `boto3.client("chime").put_voice_connector_logging_configuration` method.

[Client.put_voice_connector_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_logging_configuration)

```python
def put_voice_connector_logging_configuration(
    self,
    VoiceConnectorId: str,
    LoggingConfiguration: "LoggingConfigurationTypeDef"
) -> PutVoiceConnectorLoggingConfigurationResponseTypeDef:
    pass
```

### put_voice_connector_origination

Type annotations for `boto3.client("chime").put_voice_connector_origination` method.

[Client.put_voice_connector_origination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_origination)

```python
def put_voice_connector_origination(
    self,
    VoiceConnectorId: str,
    Origination: "OriginationTypeDef"
) -> PutVoiceConnectorOriginationResponseTypeDef:
    pass
```

### put_voice_connector_proxy

Type annotations for `boto3.client("chime").put_voice_connector_proxy` method.

[Client.put_voice_connector_proxy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_proxy)

```python
def put_voice_connector_proxy(
    self,
    VoiceConnectorId: str,
    DefaultSessionExpiryMinutes: int,
    PhoneNumberPoolCountries: List[str],
    FallBackPhoneNumber: str = None,
    Disabled: bool = None
) -> PutVoiceConnectorProxyResponseTypeDef:
    pass
```

### put_voice_connector_streaming_configuration

Type annotations for `boto3.client("chime").put_voice_connector_streaming_configuration` method.

[Client.put_voice_connector_streaming_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_streaming_configuration)

```python
def put_voice_connector_streaming_configuration(
    self,
    VoiceConnectorId: str,
    StreamingConfiguration: "StreamingConfigurationTypeDef"
) -> PutVoiceConnectorStreamingConfigurationResponseTypeDef:
    pass
```

### put_voice_connector_termination

Type annotations for `boto3.client("chime").put_voice_connector_termination` method.

[Client.put_voice_connector_termination documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_termination)

```python
def put_voice_connector_termination(
    self,
    VoiceConnectorId: str,
    Termination: "TerminationTypeDef"
) -> PutVoiceConnectorTerminationResponseTypeDef:
    pass
```

### put_voice_connector_termination_credentials

Type annotations for `boto3.client("chime").put_voice_connector_termination_credentials` method.

[Client.put_voice_connector_termination_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.put_voice_connector_termination_credentials)

```python
def put_voice_connector_termination_credentials(
    self,
    VoiceConnectorId: str,
    Credentials: List[CredentialTypeDef] = None
) -> None:
    pass
```

### redact_channel_message

Type annotations for `boto3.client("chime").redact_channel_message` method.

[Client.redact_channel_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.redact_channel_message)

```python
def redact_channel_message(
    self,
    ChannelArn: str,
    MessageId: str,
    ChimeBearer: str = None
) -> RedactChannelMessageResponseTypeDef:
    pass
```

### redact_conversation_message

Type annotations for `boto3.client("chime").redact_conversation_message` method.

[Client.redact_conversation_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.redact_conversation_message)

```python
def redact_conversation_message(
    self,
    AccountId: str,
    ConversationId: str,
    MessageId: str
) -> Dict[str, Any]:
    pass
```

### redact_room_message

Type annotations for `boto3.client("chime").redact_room_message` method.

[Client.redact_room_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.redact_room_message)

```python
def redact_room_message(
    self,
    AccountId: str,
    RoomId: str,
    MessageId: str
) -> Dict[str, Any]:
    pass
```

### regenerate_security_token

Type annotations for `boto3.client("chime").regenerate_security_token` method.

[Client.regenerate_security_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.regenerate_security_token)

```python
def regenerate_security_token(
    self,
    AccountId: str,
    BotId: str
) -> RegenerateSecurityTokenResponseTypeDef:
    pass
```

### reset_personal_pin

Type annotations for `boto3.client("chime").reset_personal_pin` method.

[Client.reset_personal_pin documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.reset_personal_pin)

```python
def reset_personal_pin(
    self,
    AccountId: str,
    UserId: str
) -> ResetPersonalPINResponseTypeDef:
    pass
```

### restore_phone_number

Type annotations for `boto3.client("chime").restore_phone_number` method.

[Client.restore_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.restore_phone_number)

```python
def restore_phone_number(
    self,
    PhoneNumberId: str
) -> RestorePhoneNumberResponseTypeDef:
    pass
```

### search_available_phone_numbers

Type annotations for `boto3.client("chime").search_available_phone_numbers` method.

[Client.search_available_phone_numbers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.search_available_phone_numbers)

```python
def search_available_phone_numbers(
    self,
    AreaCode: str = None,
    City: str = None,
    Country: str = None,
    State: str = None,
    TollFreePrefix: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> SearchAvailablePhoneNumbersResponseTypeDef:
    pass
```

### send_channel_message

Type annotations for `boto3.client("chime").send_channel_message` method.

[Client.send_channel_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.send_channel_message)

```python
def send_channel_message(
    self,
    ChannelArn: str,
    Content: str,
    Type: ChannelMessageType,
    Persistence: ChannelMessagePersistenceType,
    ClientRequestToken: str,
    Metadata: str = None,
    ChimeBearer: str = None
) -> SendChannelMessageResponseTypeDef:
    pass
```

### tag_attendee

Type annotations for `boto3.client("chime").tag_attendee` method.

[Client.tag_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.tag_attendee)

```python
def tag_attendee(
    self,
    MeetingId: str,
    AttendeeId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_meeting

Type annotations for `boto3.client("chime").tag_meeting` method.

[Client.tag_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.tag_meeting)

```python
def tag_meeting(
    self,
    MeetingId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("chime").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_attendee

Type annotations for `boto3.client("chime").untag_attendee` method.

[Client.untag_attendee documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.untag_attendee)

```python
def untag_attendee(
    self,
    MeetingId: str,
    AttendeeId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_meeting

Type annotations for `boto3.client("chime").untag_meeting` method.

[Client.untag_meeting documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.untag_meeting)

```python
def untag_meeting(
    self,
    MeetingId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("chime").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_account

Type annotations for `boto3.client("chime").update_account` method.

[Client.update_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_account)

```python
def update_account(
    self,
    AccountId: str,
    Name: str = None
) -> UpdateAccountResponseTypeDef:
    pass
```

### update_account_settings

Type annotations for `boto3.client("chime").update_account_settings` method.

[Client.update_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_account_settings)

```python
def update_account_settings(
    self,
    AccountId: str,
    AccountSettings: "AccountSettingsTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_app_instance

Type annotations for `boto3.client("chime").update_app_instance` method.

[Client.update_app_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_app_instance)

```python
def update_app_instance(
    self,
    AppInstanceArn: str,
    Name: str,
    Metadata: str = None
) -> UpdateAppInstanceResponseTypeDef:
    pass
```

### update_app_instance_user

Type annotations for `boto3.client("chime").update_app_instance_user` method.

[Client.update_app_instance_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_app_instance_user)

```python
def update_app_instance_user(
    self,
    AppInstanceUserArn: str,
    Name: str,
    Metadata: str = None
) -> UpdateAppInstanceUserResponseTypeDef:
    pass
```

### update_bot

Type annotations for `boto3.client("chime").update_bot` method.

[Client.update_bot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_bot)

```python
def update_bot(
    self,
    AccountId: str,
    BotId: str,
    Disabled: bool = None
) -> UpdateBotResponseTypeDef:
    pass
```

### update_channel

Type annotations for `boto3.client("chime").update_channel` method.

[Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_channel)

```python
def update_channel(
    self,
    ChannelArn: str,
    Name: str,
    Mode: ChannelMode,
    Metadata: str = None,
    ChimeBearer: str = None
) -> UpdateChannelResponseTypeDef:
    pass
```

### update_channel_message

Type annotations for `boto3.client("chime").update_channel_message` method.

[Client.update_channel_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_channel_message)

```python
def update_channel_message(
    self,
    ChannelArn: str,
    MessageId: str,
    Content: str = None,
    Metadata: str = None,
    ChimeBearer: str = None
) -> UpdateChannelMessageResponseTypeDef:
    pass
```

### update_channel_read_marker

Type annotations for `boto3.client("chime").update_channel_read_marker` method.

[Client.update_channel_read_marker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_channel_read_marker)

```python
def update_channel_read_marker(
    self,
    ChannelArn: str,
    ChimeBearer: str = None
) -> UpdateChannelReadMarkerResponseTypeDef:
    pass
```

### update_global_settings

Type annotations for `boto3.client("chime").update_global_settings` method.

[Client.update_global_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_global_settings)

```python
def update_global_settings(
    self,
    BusinessCalling: "BusinessCallingSettingsTypeDef",
    VoiceConnector: "VoiceConnectorSettingsTypeDef"
) -> None:
    pass
```

### update_phone_number

Type annotations for `boto3.client("chime").update_phone_number` method.

[Client.update_phone_number documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_phone_number)

```python
def update_phone_number(
    self,
    PhoneNumberId: str,
    ProductType: PhoneNumberProductType = None,
    CallingName: str = None
) -> UpdatePhoneNumberResponseTypeDef:
    pass
```

### update_phone_number_settings

Type annotations for `boto3.client("chime").update_phone_number_settings` method.

[Client.update_phone_number_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_phone_number_settings)

```python
def update_phone_number_settings(
    self,
    CallingName: str
) -> None:
    pass
```

### update_proxy_session

Type annotations for `boto3.client("chime").update_proxy_session` method.

[Client.update_proxy_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_proxy_session)

```python
def update_proxy_session(
    self,
    VoiceConnectorId: str,
    ProxySessionId: str,
    Capabilities: List[Capability],
    ExpiryMinutes: int = None
) -> UpdateProxySessionResponseTypeDef:
    pass
```

### update_room

Type annotations for `boto3.client("chime").update_room` method.

[Client.update_room documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_room)

```python
def update_room(
    self,
    AccountId: str,
    RoomId: str,
    Name: str = None
) -> UpdateRoomResponseTypeDef:
    pass
```

### update_room_membership

Type annotations for `boto3.client("chime").update_room_membership` method.

[Client.update_room_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_room_membership)

```python
def update_room_membership(
    self,
    AccountId: str,
    RoomId: str,
    MemberId: str,
    Role: RoomMembershipRole = None
) -> UpdateRoomMembershipResponseTypeDef:
    pass
```

### update_sip_media_application

Type annotations for `boto3.client("chime").update_sip_media_application` method.

[Client.update_sip_media_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_sip_media_application)

```python
def update_sip_media_application(
    self,
    SipMediaApplicationId: str,
    Name: str = None,
    Endpoints: List["SipMediaApplicationEndpointTypeDef"] = None
) -> UpdateSipMediaApplicationResponseTypeDef:
    pass
```

### update_sip_rule

Type annotations for `boto3.client("chime").update_sip_rule` method.

[Client.update_sip_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_sip_rule)

```python
def update_sip_rule(
    self,
    SipRuleId: str,
    Name: str,
    Disabled: bool = None,
    TargetApplications: List["SipRuleTargetApplicationTypeDef"] = None
) -> UpdateSipRuleResponseTypeDef:
    pass
```

### update_user

Type annotations for `boto3.client("chime").update_user` method.

[Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_user)

```python
def update_user(
    self,
    AccountId: str,
    UserId: str,
    LicenseType: License = None,
    UserType: UserType = None,
    AlexaForBusinessMetadata: "AlexaForBusinessMetadataTypeDef" = None
) -> UpdateUserResponseTypeDef:
    pass
```

### update_user_settings

Type annotations for `boto3.client("chime").update_user_settings` method.

[Client.update_user_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_user_settings)

```python
def update_user_settings(
    self,
    AccountId: str,
    UserId: str,
    UserSettings: "UserSettingsTypeDef"
) -> None:
    pass
```

### update_voice_connector

Type annotations for `boto3.client("chime").update_voice_connector` method.

[Client.update_voice_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_voice_connector)

```python
def update_voice_connector(
    self,
    VoiceConnectorId: str,
    Name: str,
    RequireEncryption: bool
) -> UpdateVoiceConnectorResponseTypeDef:
    pass
```

### update_voice_connector_group

Type annotations for `boto3.client("chime").update_voice_connector_group` method.

[Client.update_voice_connector_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Client.update_voice_connector_group)

```python
def update_voice_connector_group(
    self,
    VoiceConnectorGroupId: str,
    Name: str,
    VoiceConnectorItems: List["VoiceConnectorItemTypeDef"]
) -> UpdateVoiceConnectorGroupResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("chime").get_paginator` method.

[Paginator.ListAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Paginator.ListAccounts)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAccountsPaginatorName
) -> ListAccountsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("chime").get_paginator` method.

[Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html#Chime.Paginator.ListUsers)

```python
@overload
def get_paginator(
    self,
    operation_name: ListUsersPaginatorName
) -> ListUsersPaginator:
    pass
```