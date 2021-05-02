# Type annotations for boto3 AlexaForBusiness module

> [Index](../index.md) > AlexaForBusiness

Auto-generated documentation for [AlexaForBusiness](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html#AlexaForBusiness)
type annotations stubs module [mypy_boto3_alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/).

```bash
pip install mypy-boto3-alexaforbusiness
```

- [Type annotations for boto3 AlexaForBusiness module](#type-annotations-for-boto3-alexaforbusiness-module)
  - [AlexaForBusinessClient](#alexaforbusinessclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AlexaForBusinessClient

Type annotations for  `boto3.client("alexaforbusiness")` as [AlexaForBusinessClient](./client.md)

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.client import AlexaForBusinessClient
```


AlexaForBusinessClient [exceptions](./client.md#exceptions)



### Methods
- [approve_skill](./client.md#approve-skill)
- [associate_contact_with_address_book](./client.md#associate-contact-with-address-book)
- [associate_device_with_network_profile](./client.md#associate-device-with-network-profile)
- [associate_device_with_room](./client.md#associate-device-with-room)
- [associate_skill_group_with_room](./client.md#associate-skill-group-with-room)
- [associate_skill_with_skill_group](./client.md#associate-skill-with-skill-group)
- [associate_skill_with_users](./client.md#associate-skill-with-users)
- [can_paginate](./client.md#can-paginate)
- [create_address_book](./client.md#create-address-book)
- [create_business_report_schedule](./client.md#create-business-report-schedule)
- [create_conference_provider](./client.md#create-conference-provider)
- [create_contact](./client.md#create-contact)
- [create_gateway_group](./client.md#create-gateway-group)
- [create_network_profile](./client.md#create-network-profile)
- [create_profile](./client.md#create-profile)
- [create_room](./client.md#create-room)
- [create_skill_group](./client.md#create-skill-group)
- [create_user](./client.md#create-user)
- [delete_address_book](./client.md#delete-address-book)
- [delete_business_report_schedule](./client.md#delete-business-report-schedule)
- [delete_conference_provider](./client.md#delete-conference-provider)
- [delete_contact](./client.md#delete-contact)
- [delete_device](./client.md#delete-device)
- [delete_device_usage_data](./client.md#delete-device-usage-data)
- [delete_gateway_group](./client.md#delete-gateway-group)
- [delete_network_profile](./client.md#delete-network-profile)
- [delete_profile](./client.md#delete-profile)
- [delete_room](./client.md#delete-room)
- [delete_room_skill_parameter](./client.md#delete-room-skill-parameter)
- [delete_skill_authorization](./client.md#delete-skill-authorization)
- [delete_skill_group](./client.md#delete-skill-group)
- [delete_user](./client.md#delete-user)
- [disassociate_contact_from_address_book](./client.md#disassociate-contact-from-address-book)
- [disassociate_device_from_room](./client.md#disassociate-device-from-room)
- [disassociate_skill_from_skill_group](./client.md#disassociate-skill-from-skill-group)
- [disassociate_skill_from_users](./client.md#disassociate-skill-from-users)
- [disassociate_skill_group_from_room](./client.md#disassociate-skill-group-from-room)
- [forget_smart_home_appliances](./client.md#forget-smart-home-appliances)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_address_book](./client.md#get-address-book)
- [get_conference_preference](./client.md#get-conference-preference)
- [get_conference_provider](./client.md#get-conference-provider)
- [get_contact](./client.md#get-contact)
- [get_device](./client.md#get-device)
- [get_gateway](./client.md#get-gateway)
- [get_gateway_group](./client.md#get-gateway-group)
- [get_invitation_configuration](./client.md#get-invitation-configuration)
- [get_network_profile](./client.md#get-network-profile)
- [get_paginator](./client.md#get-paginator)
- [get_profile](./client.md#get-profile)
- [get_room](./client.md#get-room)
- [get_room_skill_parameter](./client.md#get-room-skill-parameter)
- [get_skill_group](./client.md#get-skill-group)
- [list_business_report_schedules](./client.md#list-business-report-schedules)
- [list_conference_providers](./client.md#list-conference-providers)
- [list_device_events](./client.md#list-device-events)
- [list_gateway_groups](./client.md#list-gateway-groups)
- [list_gateways](./client.md#list-gateways)
- [list_skills](./client.md#list-skills)
- [list_skills_store_categories](./client.md#list-skills-store-categories)
- [list_skills_store_skills_by_category](./client.md#list-skills-store-skills-by-category)
- [list_smart_home_appliances](./client.md#list-smart-home-appliances)
- [list_tags](./client.md#list-tags)
- [put_conference_preference](./client.md#put-conference-preference)
- [put_invitation_configuration](./client.md#put-invitation-configuration)
- [put_room_skill_parameter](./client.md#put-room-skill-parameter)
- [put_skill_authorization](./client.md#put-skill-authorization)
- [register_avs_device](./client.md#register-avs-device)
- [reject_skill](./client.md#reject-skill)
- [resolve_room](./client.md#resolve-room)
- [revoke_invitation](./client.md#revoke-invitation)
- [search_address_books](./client.md#search-address-books)
- [search_contacts](./client.md#search-contacts)
- [search_devices](./client.md#search-devices)
- [search_network_profiles](./client.md#search-network-profiles)
- [search_profiles](./client.md#search-profiles)
- [search_rooms](./client.md#search-rooms)
- [search_skill_groups](./client.md#search-skill-groups)
- [search_users](./client.md#search-users)
- [send_announcement](./client.md#send-announcement)
- [send_invitation](./client.md#send-invitation)
- [start_device_sync](./client.md#start-device-sync)
- [start_smart_home_appliance_discovery](./client.md#start-smart-home-appliance-discovery)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_address_book](./client.md#update-address-book)
- [update_business_report_schedule](./client.md#update-business-report-schedule)
- [update_conference_provider](./client.md#update-conference-provider)
- [update_contact](./client.md#update-contact)
- [update_device](./client.md#update-device)
- [update_gateway](./client.md#update-gateway)
- [update_gateway_group](./client.md#update-gateway-group)
- [update_network_profile](./client.md#update-network-profile)
- [update_profile](./client.md#update-profile)
- [update_room](./client.md#update-room)
- [update_skill_group](./client.md#update-skill-group)




### Exceptions
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [DeviceNotRegisteredException](./client.md#devicenotregisteredexception)
- [InvalidCertificateAuthorityException](./client.md#invalidcertificateauthorityexception)
- [InvalidDeviceException](./client.md#invaliddeviceexception)
- [InvalidSecretsManagerResourceException](./client.md#invalidsecretsmanagerresourceexception)
- [InvalidServiceLinkedRoleStateException](./client.md#invalidservicelinkedrolestateexception)
- [InvalidUserStatusException](./client.md#invaliduserstatusexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NameInUseException](./client.md#nameinuseexception)
- [NotFoundException](./client.md#notfoundexception)
- [ResourceAssociatedException](./client.md#resourceassociatedexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [SkillNotLinkedException](./client.md#skillnotlinkedexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("alexaforbusiness").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.paginators import ListBusinessReportSchedulesPaginator, ...
```

- [ListBusinessReportSchedulesPaginator](./paginators.md#listbusinessreportschedulespaginator)
- [ListConferenceProvidersPaginator](./paginators.md#listconferenceproviderspaginator)
- [ListDeviceEventsPaginator](./paginators.md#listdeviceeventspaginator)
- [ListSkillsPaginator](./paginators.md#listskillspaginator)
- [ListSkillsStoreCategoriesPaginator](./paginators.md#listskillsstorecategoriespaginator)
- [ListSkillsStoreSkillsByCategoryPaginator](./paginators.md#listskillsstoreskillsbycategorypaginator)
- [ListSmartHomeAppliancesPaginator](./paginators.md#listsmarthomeappliancespaginator)
- [ListTagsPaginator](./paginators.md#listtagspaginator)
- [SearchDevicesPaginator](./paginators.md#searchdevicespaginator)
- [SearchProfilesPaginator](./paginators.md#searchprofilespaginator)
- [SearchRoomsPaginator](./paginators.md#searchroomspaginator)
- [SearchSkillGroupsPaginator](./paginators.md#searchskillgroupspaginator)
- [SearchUsersPaginator](./paginators.md#searchuserspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.literals import BusinessReportFailureCode, ...
```

- [BusinessReportFailureCode](./literals.md#businessreportfailurecode)
- [BusinessReportFormat](./literals.md#businessreportformat)
- [BusinessReportInterval](./literals.md#businessreportinterval)
- [BusinessReportStatus](./literals.md#businessreportstatus)
- [CommsProtocol](./literals.md#commsprotocol)
- [ConferenceProviderType](./literals.md#conferenceprovidertype)
- [ConnectionStatus](./literals.md#connectionstatus)
- [DeviceEventType](./literals.md#deviceeventtype)
- [DeviceStatus](./literals.md#devicestatus)
- [DeviceStatusDetailCode](./literals.md#devicestatusdetailcode)
- [DeviceUsageType](./literals.md#deviceusagetype)
- [DistanceUnit](./literals.md#distanceunit)
- [EnablementType](./literals.md#enablementtype)
- [EnablementTypeFilter](./literals.md#enablementtypefilter)
- [EndOfMeetingReminderType](./literals.md#endofmeetingremindertype)
- [EnrollmentStatus](./literals.md#enrollmentstatus)
- [Feature](./literals.md#feature)
- [ListBusinessReportSchedulesPaginatorName](./literals.md#listbusinessreportschedulespaginatorname)
- [ListConferenceProvidersPaginatorName](./literals.md#listconferenceproviderspaginatorname)
- [ListDeviceEventsPaginatorName](./literals.md#listdeviceeventspaginatorname)
- [ListSkillsPaginatorName](./literals.md#listskillspaginatorname)
- [ListSkillsStoreCategoriesPaginatorName](./literals.md#listskillsstorecategoriespaginatorname)
- [ListSkillsStoreSkillsByCategoryPaginatorName](./literals.md#listskillsstoreskillsbycategorypaginatorname)
- [ListSmartHomeAppliancesPaginatorName](./literals.md#listsmarthomeappliancespaginatorname)
- [ListTagsPaginatorName](./literals.md#listtagspaginatorname)
- [Locale](./literals.md#locale)
- [NetworkEapMethod](./literals.md#networkeapmethod)
- [NetworkSecurityType](./literals.md#networksecuritytype)
- [PhoneNumberType](./literals.md#phonenumbertype)
- [RequirePin](./literals.md#requirepin)
- [SearchDevicesPaginatorName](./literals.md#searchdevicespaginatorname)
- [SearchProfilesPaginatorName](./literals.md#searchprofilespaginatorname)
- [SearchRoomsPaginatorName](./literals.md#searchroomspaginatorname)
- [SearchSkillGroupsPaginatorName](./literals.md#searchskillgroupspaginatorname)
- [SearchUsersPaginatorName](./literals.md#searchuserspaginatorname)
- [SipType](./literals.md#siptype)
- [SkillType](./literals.md#skilltype)
- [SkillTypeFilter](./literals.md#skilltypefilter)
- [SortValue](./literals.md#sortvalue)
- [TemperatureUnit](./literals.md#temperatureunit)
- [WakeWord](./literals.md#wakeword)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_alexaforbusiness.type_defs import AddressBookDataTypeDef, ...
```

- [AddressBookDataTypeDef](./type_defs.md#addressbookdatatypedef)
- [AddressBookTypeDef](./type_defs.md#addressbooktypedef)
- [AudioTypeDef](./type_defs.md#audiotypedef)
- [BusinessReportContentRangeTypeDef](./type_defs.md#businessreportcontentrangetypedef)
- [BusinessReportRecurrenceTypeDef](./type_defs.md#businessreportrecurrencetypedef)
- [BusinessReportS3LocationTypeDef](./type_defs.md#businessreports3locationtypedef)
- [BusinessReportScheduleTypeDef](./type_defs.md#businessreportscheduletypedef)
- [BusinessReportTypeDef](./type_defs.md#businessreporttypedef)
- [CategoryTypeDef](./type_defs.md#categorytypedef)
- [ConferencePreferenceTypeDef](./type_defs.md#conferencepreferencetypedef)
- [ConferenceProviderTypeDef](./type_defs.md#conferenceprovidertypedef)
- [ContactDataTypeDef](./type_defs.md#contactdatatypedef)
- [ContactTypeDef](./type_defs.md#contacttypedef)
- [CreateEndOfMeetingReminderTypeDef](./type_defs.md#createendofmeetingremindertypedef)
- [CreateInstantBookingTypeDef](./type_defs.md#createinstantbookingtypedef)
- [CreateRequireCheckInTypeDef](./type_defs.md#createrequirecheckintypedef)
- [DeveloperInfoTypeDef](./type_defs.md#developerinfotypedef)
- [DeviceDataTypeDef](./type_defs.md#devicedatatypedef)
- [DeviceEventTypeDef](./type_defs.md#deviceeventtypedef)
- [DeviceNetworkProfileInfoTypeDef](./type_defs.md#devicenetworkprofileinfotypedef)
- [DeviceStatusDetailTypeDef](./type_defs.md#devicestatusdetailtypedef)
- [DeviceStatusInfoTypeDef](./type_defs.md#devicestatusinfotypedef)
- [DeviceTypeDef](./type_defs.md#devicetypedef)
- [EndOfMeetingReminderTypeDef](./type_defs.md#endofmeetingremindertypedef)
- [GatewayGroupSummaryTypeDef](./type_defs.md#gatewaygroupsummarytypedef)
- [GatewayGroupTypeDef](./type_defs.md#gatewaygrouptypedef)
- [GatewaySummaryTypeDef](./type_defs.md#gatewaysummarytypedef)
- [GatewayTypeDef](./type_defs.md#gatewaytypedef)
- [IPDialInTypeDef](./type_defs.md#ipdialintypedef)
- [InstantBookingTypeDef](./type_defs.md#instantbookingtypedef)
- [MeetingRoomConfigurationTypeDef](./type_defs.md#meetingroomconfigurationtypedef)
- [MeetingSettingTypeDef](./type_defs.md#meetingsettingtypedef)
- [NetworkProfileDataTypeDef](./type_defs.md#networkprofiledatatypedef)
- [NetworkProfileTypeDef](./type_defs.md#networkprofiletypedef)
- [PSTNDialInTypeDef](./type_defs.md#pstndialintypedef)
- [PhoneNumberTypeDef](./type_defs.md#phonenumbertypedef)
- [ProfileDataTypeDef](./type_defs.md#profiledatatypedef)
- [ProfileTypeDef](./type_defs.md#profiletypedef)
- [RequireCheckInTypeDef](./type_defs.md#requirecheckintypedef)
- [RoomDataTypeDef](./type_defs.md#roomdatatypedef)
- [RoomSkillParameterTypeDef](./type_defs.md#roomskillparametertypedef)
- [RoomTypeDef](./type_defs.md#roomtypedef)
- [SipAddressTypeDef](./type_defs.md#sipaddresstypedef)
- [SkillDetailsTypeDef](./type_defs.md#skilldetailstypedef)
- [SkillGroupDataTypeDef](./type_defs.md#skillgroupdatatypedef)
- [SkillGroupTypeDef](./type_defs.md#skillgrouptypedef)
- [SkillSummaryTypeDef](./type_defs.md#skillsummarytypedef)
- [SkillsStoreSkillTypeDef](./type_defs.md#skillsstoreskilltypedef)
- [SmartHomeApplianceTypeDef](./type_defs.md#smarthomeappliancetypedef)
- [SsmlTypeDef](./type_defs.md#ssmltypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TextTypeDef](./type_defs.md#texttypedef)
- [UpdateEndOfMeetingReminderTypeDef](./type_defs.md#updateendofmeetingremindertypedef)
- [UpdateInstantBookingTypeDef](./type_defs.md#updateinstantbookingtypedef)
- [UpdateRequireCheckInTypeDef](./type_defs.md#updaterequirecheckintypedef)
- [UserDataTypeDef](./type_defs.md#userdatatypedef)
- [ContentTypeDef](./type_defs.md#contenttypedef)
- [CreateAddressBookResponseTypeDef](./type_defs.md#createaddressbookresponsetypedef)
- [CreateBusinessReportScheduleResponseTypeDef](./type_defs.md#createbusinessreportscheduleresponsetypedef)
- [CreateConferenceProviderResponseTypeDef](./type_defs.md#createconferenceproviderresponsetypedef)
- [CreateContactResponseTypeDef](./type_defs.md#createcontactresponsetypedef)
- [CreateGatewayGroupResponseTypeDef](./type_defs.md#creategatewaygroupresponsetypedef)
- [CreateMeetingRoomConfigurationTypeDef](./type_defs.md#createmeetingroomconfigurationtypedef)
- [CreateNetworkProfileResponseTypeDef](./type_defs.md#createnetworkprofileresponsetypedef)
- [CreateProfileResponseTypeDef](./type_defs.md#createprofileresponsetypedef)
- [CreateRoomResponseTypeDef](./type_defs.md#createroomresponsetypedef)
- [CreateSkillGroupResponseTypeDef](./type_defs.md#createskillgroupresponsetypedef)
- [CreateUserResponseTypeDef](./type_defs.md#createuserresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetAddressBookResponseTypeDef](./type_defs.md#getaddressbookresponsetypedef)
- [GetConferencePreferenceResponseTypeDef](./type_defs.md#getconferencepreferenceresponsetypedef)
- [GetConferenceProviderResponseTypeDef](./type_defs.md#getconferenceproviderresponsetypedef)
- [GetContactResponseTypeDef](./type_defs.md#getcontactresponsetypedef)
- [GetDeviceResponseTypeDef](./type_defs.md#getdeviceresponsetypedef)
- [GetGatewayGroupResponseTypeDef](./type_defs.md#getgatewaygroupresponsetypedef)
- [GetGatewayResponseTypeDef](./type_defs.md#getgatewayresponsetypedef)
- [GetInvitationConfigurationResponseTypeDef](./type_defs.md#getinvitationconfigurationresponsetypedef)
- [GetNetworkProfileResponseTypeDef](./type_defs.md#getnetworkprofileresponsetypedef)
- [GetProfileResponseTypeDef](./type_defs.md#getprofileresponsetypedef)
- [GetRoomResponseTypeDef](./type_defs.md#getroomresponsetypedef)
- [GetRoomSkillParameterResponseTypeDef](./type_defs.md#getroomskillparameterresponsetypedef)
- [GetSkillGroupResponseTypeDef](./type_defs.md#getskillgroupresponsetypedef)
- [ListBusinessReportSchedulesResponseTypeDef](./type_defs.md#listbusinessreportschedulesresponsetypedef)
- [ListConferenceProvidersResponseTypeDef](./type_defs.md#listconferenceprovidersresponsetypedef)
- [ListDeviceEventsResponseTypeDef](./type_defs.md#listdeviceeventsresponsetypedef)
- [ListGatewayGroupsResponseTypeDef](./type_defs.md#listgatewaygroupsresponsetypedef)
- [ListGatewaysResponseTypeDef](./type_defs.md#listgatewaysresponsetypedef)
- [ListSkillsResponseTypeDef](./type_defs.md#listskillsresponsetypedef)
- [ListSkillsStoreCategoriesResponseTypeDef](./type_defs.md#listskillsstorecategoriesresponsetypedef)
- [ListSkillsStoreSkillsByCategoryResponseTypeDef](./type_defs.md#listskillsstoreskillsbycategoryresponsetypedef)
- [ListSmartHomeAppliancesResponseTypeDef](./type_defs.md#listsmarthomeappliancesresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RegisterAVSDeviceResponseTypeDef](./type_defs.md#registeravsdeviceresponsetypedef)
- [ResolveRoomResponseTypeDef](./type_defs.md#resolveroomresponsetypedef)
- [SearchAddressBooksResponseTypeDef](./type_defs.md#searchaddressbooksresponsetypedef)
- [SearchContactsResponseTypeDef](./type_defs.md#searchcontactsresponsetypedef)
- [SearchDevicesResponseTypeDef](./type_defs.md#searchdevicesresponsetypedef)
- [SearchNetworkProfilesResponseTypeDef](./type_defs.md#searchnetworkprofilesresponsetypedef)
- [SearchProfilesResponseTypeDef](./type_defs.md#searchprofilesresponsetypedef)
- [SearchRoomsResponseTypeDef](./type_defs.md#searchroomsresponsetypedef)
- [SearchSkillGroupsResponseTypeDef](./type_defs.md#searchskillgroupsresponsetypedef)
- [SearchUsersResponseTypeDef](./type_defs.md#searchusersresponsetypedef)
- [SendAnnouncementResponseTypeDef](./type_defs.md#sendannouncementresponsetypedef)
- [SortTypeDef](./type_defs.md#sorttypedef)
- [UpdateMeetingRoomConfigurationTypeDef](./type_defs.md#updatemeetingroomconfigurationtypedef)
