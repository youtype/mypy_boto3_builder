# Structures for boto3 Pinpoint module

> [Index](../index.md) > [Pinpoint](./index.md) > Structures

Auto-generated documentation for [Pinpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint)
type annotations stubs module [mypy_boto3_pinpoint](https://pypi.org/project/mypy-boto3-pinpoint/).

- [Structures for boto3 Pinpoint module](#structures-for-boto3-pinpoint-module)
  - [ADMChannelResponseTypeDef](#admchannelresponsetypedef)
  - [ADMMessageTypeDef](#admmessagetypedef)
  - [APNSChannelResponseTypeDef](#apnschannelresponsetypedef)
  - [APNSMessageTypeDef](#apnsmessagetypedef)
  - [APNSPushNotificationTemplateTypeDef](#apnspushnotificationtemplatetypedef)
  - [APNSSandboxChannelResponseTypeDef](#apnssandboxchannelresponsetypedef)
  - [APNSVoipChannelResponseTypeDef](#apnsvoipchannelresponsetypedef)
  - [APNSVoipSandboxChannelResponseTypeDef](#apnsvoipsandboxchannelresponsetypedef)
  - [ActivitiesResponseTypeDef](#activitiesresponsetypedef)
  - [ActivityResponseTypeDef](#activityresponsetypedef)
  - [ActivityTypeDef](#activitytypedef)
  - [AddressConfigurationTypeDef](#addressconfigurationtypedef)
  - [AndroidPushNotificationTemplateTypeDef](#androidpushnotificationtemplatetypedef)
  - [ApplicationDateRangeKpiResponseTypeDef](#applicationdaterangekpiresponsetypedef)
  - [ApplicationResponseTypeDef](#applicationresponsetypedef)
  - [ApplicationSettingsResourceTypeDef](#applicationsettingsresourcetypedef)
  - [ApplicationsResponseTypeDef](#applicationsresponsetypedef)
  - [AttributeDimensionTypeDef](#attributedimensiontypedef)
  - [AttributesResourceTypeDef](#attributesresourcetypedef)
  - [BaiduChannelResponseTypeDef](#baiduchannelresponsetypedef)
  - [BaiduMessageTypeDef](#baidumessagetypedef)
  - [BaseKpiResultTypeDef](#basekpiresulttypedef)
  - [CampaignCustomMessageTypeDef](#campaigncustommessagetypedef)
  - [CampaignDateRangeKpiResponseTypeDef](#campaigndaterangekpiresponsetypedef)
  - [CampaignEmailMessageTypeDef](#campaignemailmessagetypedef)
  - [CampaignEventFilterTypeDef](#campaigneventfiltertypedef)
  - [CampaignHookTypeDef](#campaignhooktypedef)
  - [CampaignLimitsTypeDef](#campaignlimitstypedef)
  - [CampaignResponseTypeDef](#campaignresponsetypedef)
  - [CampaignSmsMessageTypeDef](#campaignsmsmessagetypedef)
  - [CampaignStateTypeDef](#campaignstatetypedef)
  - [CampaignsResponseTypeDef](#campaignsresponsetypedef)
  - [ChannelResponseTypeDef](#channelresponsetypedef)
  - [ChannelsResponseTypeDef](#channelsresponsetypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [ConditionalSplitActivityTypeDef](#conditionalsplitactivitytypedef)
  - [CreateTemplateMessageBodyTypeDef](#createtemplatemessagebodytypedef)
  - [CustomDeliveryConfigurationTypeDef](#customdeliveryconfigurationtypedef)
  - [CustomMessageActivityTypeDef](#custommessageactivitytypedef)
  - [DefaultMessageTypeDef](#defaultmessagetypedef)
  - [DefaultPushNotificationMessageTypeDef](#defaultpushnotificationmessagetypedef)
  - [DefaultPushNotificationTemplateTypeDef](#defaultpushnotificationtemplatetypedef)
  - [DirectMessageConfigurationTypeDef](#directmessageconfigurationtypedef)
  - [EmailChannelResponseTypeDef](#emailchannelresponsetypedef)
  - [EmailMessageActivityTypeDef](#emailmessageactivitytypedef)
  - [EmailMessageTypeDef](#emailmessagetypedef)
  - [EmailTemplateResponseTypeDef](#emailtemplateresponsetypedef)
  - [EndpointBatchItemTypeDef](#endpointbatchitemtypedef)
  - [EndpointDemographicTypeDef](#endpointdemographictypedef)
  - [EndpointItemResponseTypeDef](#endpointitemresponsetypedef)
  - [EndpointLocationTypeDef](#endpointlocationtypedef)
  - [EndpointMessageResultTypeDef](#endpointmessageresulttypedef)
  - [EndpointResponseTypeDef](#endpointresponsetypedef)
  - [EndpointSendConfigurationTypeDef](#endpointsendconfigurationtypedef)
  - [EndpointUserTypeDef](#endpointusertypedef)
  - [EndpointsResponseTypeDef](#endpointsresponsetypedef)
  - [EventConditionTypeDef](#eventconditiontypedef)
  - [EventDimensionsTypeDef](#eventdimensionstypedef)
  - [EventFilterTypeDef](#eventfiltertypedef)
  - [EventItemResponseTypeDef](#eventitemresponsetypedef)
  - [EventStartConditionTypeDef](#eventstartconditiontypedef)
  - [EventStreamTypeDef](#eventstreamtypedef)
  - [EventTypeDef](#eventtypedef)
  - [EventsBatchTypeDef](#eventsbatchtypedef)
  - [EventsResponseTypeDef](#eventsresponsetypedef)
  - [ExportJobResourceTypeDef](#exportjobresourcetypedef)
  - [ExportJobResponseTypeDef](#exportjobresponsetypedef)
  - [ExportJobsResponseTypeDef](#exportjobsresponsetypedef)
  - [GCMChannelResponseTypeDef](#gcmchannelresponsetypedef)
  - [GCMMessageTypeDef](#gcmmessagetypedef)
  - [GPSCoordinatesTypeDef](#gpscoordinatestypedef)
  - [GPSPointDimensionTypeDef](#gpspointdimensiontypedef)
  - [HoldoutActivityTypeDef](#holdoutactivitytypedef)
  - [ImportJobResourceTypeDef](#importjobresourcetypedef)
  - [ImportJobResponseTypeDef](#importjobresponsetypedef)
  - [ImportJobsResponseTypeDef](#importjobsresponsetypedef)
  - [ItemResponseTypeDef](#itemresponsetypedef)
  - [JourneyCustomMessageTypeDef](#journeycustommessagetypedef)
  - [JourneyDateRangeKpiResponseTypeDef](#journeydaterangekpiresponsetypedef)
  - [JourneyEmailMessageTypeDef](#journeyemailmessagetypedef)
  - [JourneyExecutionActivityMetricsResponseTypeDef](#journeyexecutionactivitymetricsresponsetypedef)
  - [JourneyExecutionMetricsResponseTypeDef](#journeyexecutionmetricsresponsetypedef)
  - [JourneyLimitsTypeDef](#journeylimitstypedef)
  - [JourneyPushMessageTypeDef](#journeypushmessagetypedef)
  - [JourneyResponseTypeDef](#journeyresponsetypedef)
  - [JourneySMSMessageTypeDef](#journeysmsmessagetypedef)
  - [JourneyScheduleTypeDef](#journeyscheduletypedef)
  - [JourneysResponseTypeDef](#journeysresponsetypedef)
  - [ListRecommenderConfigurationsResponseTypeDef](#listrecommenderconfigurationsresponsetypedef)
  - [MessageBodyTypeDef](#messagebodytypedef)
  - [MessageConfigurationTypeDef](#messageconfigurationtypedef)
  - [MessageResponseTypeDef](#messageresponsetypedef)
  - [MessageResultTypeDef](#messageresulttypedef)
  - [MessageTypeDef](#messagetypedef)
  - [MetricDimensionTypeDef](#metricdimensiontypedef)
  - [MultiConditionalBranchTypeDef](#multiconditionalbranchtypedef)
  - [MultiConditionalSplitActivityTypeDef](#multiconditionalsplitactivitytypedef)
  - [NumberValidateResponseTypeDef](#numbervalidateresponsetypedef)
  - [PublicEndpointTypeDef](#publicendpointtypedef)
  - [PushMessageActivityTypeDef](#pushmessageactivitytypedef)
  - [PushNotificationTemplateResponseTypeDef](#pushnotificationtemplateresponsetypedef)
  - [QuietTimeTypeDef](#quiettimetypedef)
  - [RandomSplitActivityTypeDef](#randomsplitactivitytypedef)
  - [RandomSplitEntryTypeDef](#randomsplitentrytypedef)
  - [RawEmailTypeDef](#rawemailtypedef)
  - [RecencyDimensionTypeDef](#recencydimensiontypedef)
  - [RecommenderConfigurationResponseTypeDef](#recommenderconfigurationresponsetypedef)
  - [ResultRowTypeDef](#resultrowtypedef)
  - [ResultRowValueTypeDef](#resultrowvaluetypedef)
  - [SMSChannelResponseTypeDef](#smschannelresponsetypedef)
  - [SMSMessageActivityTypeDef](#smsmessageactivitytypedef)
  - [SMSMessageTypeDef](#smsmessagetypedef)
  - [SMSTemplateResponseTypeDef](#smstemplateresponsetypedef)
  - [ScheduleTypeDef](#scheduletypedef)
  - [SegmentBehaviorsTypeDef](#segmentbehaviorstypedef)
  - [SegmentConditionTypeDef](#segmentconditiontypedef)
  - [SegmentDemographicsTypeDef](#segmentdemographicstypedef)
  - [SegmentDimensionsTypeDef](#segmentdimensionstypedef)
  - [SegmentGroupListTypeDef](#segmentgrouplisttypedef)
  - [SegmentGroupTypeDef](#segmentgrouptypedef)
  - [SegmentImportResourceTypeDef](#segmentimportresourcetypedef)
  - [SegmentLocationTypeDef](#segmentlocationtypedef)
  - [SegmentReferenceTypeDef](#segmentreferencetypedef)
  - [SegmentResponseTypeDef](#segmentresponsetypedef)
  - [SegmentsResponseTypeDef](#segmentsresponsetypedef)
  - [SendUsersMessageResponseTypeDef](#sendusersmessageresponsetypedef)
  - [SessionTypeDef](#sessiontypedef)
  - [SetDimensionTypeDef](#setdimensiontypedef)
  - [SimpleConditionTypeDef](#simpleconditiontypedef)
  - [SimpleEmailPartTypeDef](#simpleemailparttypedef)
  - [SimpleEmailTypeDef](#simpleemailtypedef)
  - [StartConditionTypeDef](#startconditiontypedef)
  - [TagsModelTypeDef](#tagsmodeltypedef)
  - [TemplateConfigurationTypeDef](#templateconfigurationtypedef)
  - [TemplateResponseTypeDef](#templateresponsetypedef)
  - [TemplateTypeDef](#templatetypedef)
  - [TemplateVersionResponseTypeDef](#templateversionresponsetypedef)
  - [TemplateVersionsResponseTypeDef](#templateversionsresponsetypedef)
  - [TemplatesResponseTypeDef](#templatesresponsetypedef)
  - [TreatmentResourceTypeDef](#treatmentresourcetypedef)
  - [VoiceChannelResponseTypeDef](#voicechannelresponsetypedef)
  - [VoiceMessageTypeDef](#voicemessagetypedef)
  - [VoiceTemplateResponseTypeDef](#voicetemplateresponsetypedef)
  - [WaitActivityTypeDef](#waitactivitytypedef)
  - [WaitTimeTypeDef](#waittimetypedef)
  - [WriteTreatmentResourceTypeDef](#writetreatmentresourcetypedef)
  - [ADMChannelRequestTypeDef](#admchannelrequesttypedef)
  - [APNSChannelRequestTypeDef](#apnschannelrequesttypedef)
  - [APNSSandboxChannelRequestTypeDef](#apnssandboxchannelrequesttypedef)
  - [APNSVoipChannelRequestTypeDef](#apnsvoipchannelrequesttypedef)
  - [APNSVoipSandboxChannelRequestTypeDef](#apnsvoipsandboxchannelrequesttypedef)
  - [BaiduChannelRequestTypeDef](#baiduchannelrequesttypedef)
  - [CreateAppResponseTypeDef](#createappresponsetypedef)
  - [CreateApplicationRequestTypeDef](#createapplicationrequesttypedef)
  - [CreateCampaignResponseTypeDef](#createcampaignresponsetypedef)
  - [CreateEmailTemplateResponseTypeDef](#createemailtemplateresponsetypedef)
  - [CreateExportJobResponseTypeDef](#createexportjobresponsetypedef)
  - [CreateImportJobResponseTypeDef](#createimportjobresponsetypedef)
  - [CreateJourneyResponseTypeDef](#createjourneyresponsetypedef)
  - [CreatePushTemplateResponseTypeDef](#createpushtemplateresponsetypedef)
  - [CreateRecommenderConfigurationResponseTypeDef](#createrecommenderconfigurationresponsetypedef)
  - [CreateRecommenderConfigurationTypeDef](#createrecommenderconfigurationtypedef)
  - [CreateSegmentResponseTypeDef](#createsegmentresponsetypedef)
  - [CreateSmsTemplateResponseTypeDef](#createsmstemplateresponsetypedef)
  - [CreateVoiceTemplateResponseTypeDef](#createvoicetemplateresponsetypedef)
  - [DeleteAdmChannelResponseTypeDef](#deleteadmchannelresponsetypedef)
  - [DeleteApnsChannelResponseTypeDef](#deleteapnschannelresponsetypedef)
  - [DeleteApnsSandboxChannelResponseTypeDef](#deleteapnssandboxchannelresponsetypedef)
  - [DeleteApnsVoipChannelResponseTypeDef](#deleteapnsvoipchannelresponsetypedef)
  - [DeleteApnsVoipSandboxChannelResponseTypeDef](#deleteapnsvoipsandboxchannelresponsetypedef)
  - [DeleteAppResponseTypeDef](#deleteappresponsetypedef)
  - [DeleteBaiduChannelResponseTypeDef](#deletebaiduchannelresponsetypedef)
  - [DeleteCampaignResponseTypeDef](#deletecampaignresponsetypedef)
  - [DeleteEmailChannelResponseTypeDef](#deleteemailchannelresponsetypedef)
  - [DeleteEmailTemplateResponseTypeDef](#deleteemailtemplateresponsetypedef)
  - [DeleteEndpointResponseTypeDef](#deleteendpointresponsetypedef)
  - [DeleteEventStreamResponseTypeDef](#deleteeventstreamresponsetypedef)
  - [DeleteGcmChannelResponseTypeDef](#deletegcmchannelresponsetypedef)
  - [DeleteJourneyResponseTypeDef](#deletejourneyresponsetypedef)
  - [DeletePushTemplateResponseTypeDef](#deletepushtemplateresponsetypedef)
  - [DeleteRecommenderConfigurationResponseTypeDef](#deleterecommenderconfigurationresponsetypedef)
  - [DeleteSegmentResponseTypeDef](#deletesegmentresponsetypedef)
  - [DeleteSmsChannelResponseTypeDef](#deletesmschannelresponsetypedef)
  - [DeleteSmsTemplateResponseTypeDef](#deletesmstemplateresponsetypedef)
  - [DeleteUserEndpointsResponseTypeDef](#deleteuserendpointsresponsetypedef)
  - [DeleteVoiceChannelResponseTypeDef](#deletevoicechannelresponsetypedef)
  - [DeleteVoiceTemplateResponseTypeDef](#deletevoicetemplateresponsetypedef)
  - [EmailChannelRequestTypeDef](#emailchannelrequesttypedef)
  - [EmailTemplateRequestTypeDef](#emailtemplaterequesttypedef)
  - [EndpointBatchRequestTypeDef](#endpointbatchrequesttypedef)
  - [EndpointRequestTypeDef](#endpointrequesttypedef)
  - [EventsRequestTypeDef](#eventsrequesttypedef)
  - [ExportJobRequestTypeDef](#exportjobrequesttypedef)
  - [GCMChannelRequestTypeDef](#gcmchannelrequesttypedef)
  - [GetAdmChannelResponseTypeDef](#getadmchannelresponsetypedef)
  - [GetApnsChannelResponseTypeDef](#getapnschannelresponsetypedef)
  - [GetApnsSandboxChannelResponseTypeDef](#getapnssandboxchannelresponsetypedef)
  - [GetApnsVoipChannelResponseTypeDef](#getapnsvoipchannelresponsetypedef)
  - [GetApnsVoipSandboxChannelResponseTypeDef](#getapnsvoipsandboxchannelresponsetypedef)
  - [GetAppResponseTypeDef](#getappresponsetypedef)
  - [GetApplicationDateRangeKpiResponseTypeDef](#getapplicationdaterangekpiresponsetypedef)
  - [GetApplicationSettingsResponseTypeDef](#getapplicationsettingsresponsetypedef)
  - [GetAppsResponseTypeDef](#getappsresponsetypedef)
  - [GetBaiduChannelResponseTypeDef](#getbaiduchannelresponsetypedef)
  - [GetCampaignActivitiesResponseTypeDef](#getcampaignactivitiesresponsetypedef)
  - [GetCampaignDateRangeKpiResponseTypeDef](#getcampaigndaterangekpiresponsetypedef)
  - [GetCampaignResponseTypeDef](#getcampaignresponsetypedef)
  - [GetCampaignVersionResponseTypeDef](#getcampaignversionresponsetypedef)
  - [GetCampaignVersionsResponseTypeDef](#getcampaignversionsresponsetypedef)
  - [GetCampaignsResponseTypeDef](#getcampaignsresponsetypedef)
  - [GetChannelsResponseTypeDef](#getchannelsresponsetypedef)
  - [GetEmailChannelResponseTypeDef](#getemailchannelresponsetypedef)
  - [GetEmailTemplateResponseTypeDef](#getemailtemplateresponsetypedef)
  - [GetEndpointResponseTypeDef](#getendpointresponsetypedef)
  - [GetEventStreamResponseTypeDef](#geteventstreamresponsetypedef)
  - [GetExportJobResponseTypeDef](#getexportjobresponsetypedef)
  - [GetExportJobsResponseTypeDef](#getexportjobsresponsetypedef)
  - [GetGcmChannelResponseTypeDef](#getgcmchannelresponsetypedef)
  - [GetImportJobResponseTypeDef](#getimportjobresponsetypedef)
  - [GetImportJobsResponseTypeDef](#getimportjobsresponsetypedef)
  - [GetJourneyDateRangeKpiResponseTypeDef](#getjourneydaterangekpiresponsetypedef)
  - [GetJourneyExecutionActivityMetricsResponseTypeDef](#getjourneyexecutionactivitymetricsresponsetypedef)
  - [GetJourneyExecutionMetricsResponseTypeDef](#getjourneyexecutionmetricsresponsetypedef)
  - [GetJourneyResponseTypeDef](#getjourneyresponsetypedef)
  - [GetPushTemplateResponseTypeDef](#getpushtemplateresponsetypedef)
  - [GetRecommenderConfigurationResponseTypeDef](#getrecommenderconfigurationresponsetypedef)
  - [GetRecommenderConfigurationsResponseTypeDef](#getrecommenderconfigurationsresponsetypedef)
  - [GetSegmentExportJobsResponseTypeDef](#getsegmentexportjobsresponsetypedef)
  - [GetSegmentImportJobsResponseTypeDef](#getsegmentimportjobsresponsetypedef)
  - [GetSegmentResponseTypeDef](#getsegmentresponsetypedef)
  - [GetSegmentVersionResponseTypeDef](#getsegmentversionresponsetypedef)
  - [GetSegmentVersionsResponseTypeDef](#getsegmentversionsresponsetypedef)
  - [GetSegmentsResponseTypeDef](#getsegmentsresponsetypedef)
  - [GetSmsChannelResponseTypeDef](#getsmschannelresponsetypedef)
  - [GetSmsTemplateResponseTypeDef](#getsmstemplateresponsetypedef)
  - [GetUserEndpointsResponseTypeDef](#getuserendpointsresponsetypedef)
  - [GetVoiceChannelResponseTypeDef](#getvoicechannelresponsetypedef)
  - [GetVoiceTemplateResponseTypeDef](#getvoicetemplateresponsetypedef)
  - [ImportJobRequestTypeDef](#importjobrequesttypedef)
  - [JourneyStateRequestTypeDef](#journeystaterequesttypedef)
  - [ListJourneysResponseTypeDef](#listjourneysresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTemplateVersionsResponseTypeDef](#listtemplateversionsresponsetypedef)
  - [ListTemplatesResponseTypeDef](#listtemplatesresponsetypedef)
  - [MessageRequestTypeDef](#messagerequesttypedef)
  - [NumberValidateRequestTypeDef](#numbervalidaterequesttypedef)
  - [PhoneNumberValidateResponseTypeDef](#phonenumbervalidateresponsetypedef)
  - [PushNotificationTemplateRequestTypeDef](#pushnotificationtemplaterequesttypedef)
  - [PutEventStreamResponseTypeDef](#puteventstreamresponsetypedef)
  - [PutEventsResponseTypeDef](#puteventsresponsetypedef)
  - [RemoveAttributesResponseTypeDef](#removeattributesresponsetypedef)
  - [SMSChannelRequestTypeDef](#smschannelrequesttypedef)
  - [SMSTemplateRequestTypeDef](#smstemplaterequesttypedef)
  - [SendMessagesResponseTypeDef](#sendmessagesresponsetypedef)
  - [SendUsersMessageRequestTypeDef](#sendusersmessagerequesttypedef)
  - [SendUsersMessagesResponseTypeDef](#sendusersmessagesresponsetypedef)
  - [TemplateActiveVersionRequestTypeDef](#templateactiveversionrequesttypedef)
  - [UpdateAdmChannelResponseTypeDef](#updateadmchannelresponsetypedef)
  - [UpdateApnsChannelResponseTypeDef](#updateapnschannelresponsetypedef)
  - [UpdateApnsSandboxChannelResponseTypeDef](#updateapnssandboxchannelresponsetypedef)
  - [UpdateApnsVoipChannelResponseTypeDef](#updateapnsvoipchannelresponsetypedef)
  - [UpdateApnsVoipSandboxChannelResponseTypeDef](#updateapnsvoipsandboxchannelresponsetypedef)
  - [UpdateApplicationSettingsResponseTypeDef](#updateapplicationsettingsresponsetypedef)
  - [UpdateAttributesRequestTypeDef](#updateattributesrequesttypedef)
  - [UpdateBaiduChannelResponseTypeDef](#updatebaiduchannelresponsetypedef)
  - [UpdateCampaignResponseTypeDef](#updatecampaignresponsetypedef)
  - [UpdateEmailChannelResponseTypeDef](#updateemailchannelresponsetypedef)
  - [UpdateEmailTemplateResponseTypeDef](#updateemailtemplateresponsetypedef)
  - [UpdateEndpointResponseTypeDef](#updateendpointresponsetypedef)
  - [UpdateEndpointsBatchResponseTypeDef](#updateendpointsbatchresponsetypedef)
  - [UpdateGcmChannelResponseTypeDef](#updategcmchannelresponsetypedef)
  - [UpdateJourneyResponseTypeDef](#updatejourneyresponsetypedef)
  - [UpdateJourneyStateResponseTypeDef](#updatejourneystateresponsetypedef)
  - [UpdatePushTemplateResponseTypeDef](#updatepushtemplateresponsetypedef)
  - [UpdateRecommenderConfigurationResponseTypeDef](#updaterecommenderconfigurationresponsetypedef)
  - [UpdateRecommenderConfigurationTypeDef](#updaterecommenderconfigurationtypedef)
  - [UpdateSegmentResponseTypeDef](#updatesegmentresponsetypedef)
  - [UpdateSmsChannelResponseTypeDef](#updatesmschannelresponsetypedef)
  - [UpdateSmsTemplateResponseTypeDef](#updatesmstemplateresponsetypedef)
  - [UpdateTemplateActiveVersionResponseTypeDef](#updatetemplateactiveversionresponsetypedef)
  - [UpdateVoiceChannelResponseTypeDef](#updatevoicechannelresponsetypedef)
  - [UpdateVoiceTemplateResponseTypeDef](#updatevoicetemplateresponsetypedef)
  - [VoiceChannelRequestTypeDef](#voicechannelrequesttypedef)
  - [VoiceTemplateRequestTypeDef](#voicetemplaterequesttypedef)
  - [WriteApplicationSettingsRequestTypeDef](#writeapplicationsettingsrequesttypedef)
  - [WriteCampaignRequestTypeDef](#writecampaignrequesttypedef)
  - [WriteEventStreamTypeDef](#writeeventstreamtypedef)
  - [WriteJourneyRequestTypeDef](#writejourneyrequesttypedef)
  - [WriteSegmentRequestTypeDef](#writesegmentrequesttypedef)

## ADMChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ADMChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## ADMMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ADMMessageTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `ConsolidationKey`: `str`
- `Data`: `Dict[str, str]`
- `ExpiresAfter`: `str`
- `IconReference`: `str`
- `ImageIconUrl`: `str`
- `ImageUrl`: `str`
- `MD5`: `str`
- `RawContent`: `str`
- `SilentPush`: `bool`
- `SmallImageIconUrl`: `str`
- `Sound`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `Title`: `str`
- `Url`: `str`


## APNSChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `HasTokenKey`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## APNSMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSMessageTypeDef
```




Optional fields:
- `APNSPushType`: `str`
- `Action`: `Action`
- `Badge`: `int`
- `Body`: `str`
- `Category`: `str`
- `CollapseId`: `str`
- `Data`: `Dict[str, str]`
- `MediaUrl`: `str`
- `PreferredAuthenticationMethod`: `str`
- `Priority`: `str`
- `RawContent`: `str`
- `SilentPush`: `bool`
- `Sound`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `ThreadId`: `str`
- `TimeToLive`: `int`
- `Title`: `str`
- `Url`: `str`


## APNSPushNotificationTemplateTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSPushNotificationTemplateTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `MediaUrl`: `str`
- `RawContent`: `str`
- `Sound`: `str`
- `Title`: `str`
- `Url`: `str`


## APNSSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSSandboxChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `HasTokenKey`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## APNSVoipChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSVoipChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `HasTokenKey`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## APNSVoipSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSVoipSandboxChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `HasTokenKey`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## ActivitiesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ActivitiesResponseTypeDef
```


Required fields:
- `Item`: `List["ActivityResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ActivityResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ActivityResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `CampaignId`: `str`
- `Id`: `str`



Optional fields:
- `End`: `str`
- `Result`: `str`
- `ScheduledStart`: `str`
- `Start`: `str`
- `State`: `str`
- `SuccessfulEndpointCount`: `int`
- `TimezonesCompletedCount`: `int`
- `TimezonesTotalCount`: `int`
- `TotalEndpointCount`: `int`
- `TreatmentId`: `str`


## ActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ActivityTypeDef
```




Optional fields:
- `CUSTOM`: `"CustomMessageActivityTypeDef"`
- `ConditionalSplit`: `"ConditionalSplitActivityTypeDef"`
- `Description`: `str`
- `EMAIL`: `"EmailMessageActivityTypeDef"`
- `Holdout`: `"HoldoutActivityTypeDef"`
- `MultiCondition`: `"MultiConditionalSplitActivityTypeDef"`
- `PUSH`: `"PushMessageActivityTypeDef"`
- `RandomSplit`: `"RandomSplitActivityTypeDef"`
- `SMS`: `"SMSMessageActivityTypeDef"`
- `Wait`: `"WaitActivityTypeDef"`


## AddressConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import AddressConfigurationTypeDef
```




Optional fields:
- `BodyOverride`: `str`
- `ChannelType`: `ChannelType`
- `Context`: `Dict[str, str]`
- `RawContent`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `TitleOverride`: `str`


## AndroidPushNotificationTemplateTypeDef

```python
from mypy_boto3_pinpoint.type_defs import AndroidPushNotificationTemplateTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `ImageIconUrl`: `str`
- `ImageUrl`: `str`
- `RawContent`: `str`
- `SmallImageIconUrl`: `str`
- `Sound`: `str`
- `Title`: `str`
- `Url`: `str`


## ApplicationDateRangeKpiResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ApplicationDateRangeKpiResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `EndTime`: `datetime`
- `KpiName`: `str`
- `KpiResult`: `"BaseKpiResultTypeDef"`
- `StartTime`: `datetime`



Optional fields:
- `NextToken`: `str`


## ApplicationResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ApplicationResponseTypeDef
```


Required fields:
- `Arn`: `str`
- `Id`: `str`
- `Name`: `str`



Optional fields:
- `tags`: `Dict[str, str]`


## ApplicationSettingsResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ApplicationSettingsResourceTypeDef
```


Required fields:
- `ApplicationId`: `str`



Optional fields:
- `CampaignHook`: `"CampaignHookTypeDef"`
- `LastModifiedDate`: `str`
- `Limits`: `"CampaignLimitsTypeDef"`
- `QuietTime`: `"QuietTimeTypeDef"`


## ApplicationsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ApplicationsResponseTypeDef
```




Optional fields:
- `Item`: `List["ApplicationResponseTypeDef"]`
- `NextToken`: `str`


## AttributeDimensionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import AttributeDimensionTypeDef
```


Required fields:
- `Values`: `List[str]`



Optional fields:
- `AttributeType`: `AttributeType`


## AttributesResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import AttributesResourceTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `AttributeType`: `str`



Optional fields:
- `Attributes`: `List[str]`


## BaiduChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import BaiduChannelResponseTypeDef
```


Required fields:
- `Credential`: `str`
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## BaiduMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import BaiduMessageTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `Data`: `Dict[str, str]`
- `IconReference`: `str`
- `ImageIconUrl`: `str`
- `ImageUrl`: `str`
- `RawContent`: `str`
- `SilentPush`: `bool`
- `SmallImageIconUrl`: `str`
- `Sound`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `TimeToLive`: `int`
- `Title`: `str`
- `Url`: `str`


## BaseKpiResultTypeDef

```python
from mypy_boto3_pinpoint.type_defs import BaseKpiResultTypeDef
```


Required fields:
- `Rows`: `List["ResultRowTypeDef"]`




## CampaignCustomMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignCustomMessageTypeDef
```




Optional fields:
- `Data`: `str`


## CampaignDateRangeKpiResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignDateRangeKpiResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `CampaignId`: `str`
- `EndTime`: `datetime`
- `KpiName`: `str`
- `KpiResult`: `"BaseKpiResultTypeDef"`
- `StartTime`: `datetime`



Optional fields:
- `NextToken`: `str`


## CampaignEmailMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignEmailMessageTypeDef
```




Optional fields:
- `Body`: `str`
- `FromAddress`: `str`
- `HtmlBody`: `str`
- `Title`: `str`


## CampaignEventFilterTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignEventFilterTypeDef
```


Required fields:
- `Dimensions`: `"EventDimensionsTypeDef"`
- `FilterType`: `FilterType`




## CampaignHookTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignHookTypeDef
```




Optional fields:
- `LambdaFunctionName`: `str`
- `Mode`: `Mode`
- `WebUrl`: `str`


## CampaignLimitsTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignLimitsTypeDef
```




Optional fields:
- `Daily`: `int`
- `MaximumDuration`: `int`
- `MessagesPerSecond`: `int`
- `Total`: `int`


## CampaignResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `Arn`: `str`
- `CreationDate`: `str`
- `Id`: `str`
- `LastModifiedDate`: `str`
- `SegmentId`: `str`
- `SegmentVersion`: `int`



Optional fields:
- `AdditionalTreatments`: `List["TreatmentResourceTypeDef"]`
- `CustomDeliveryConfiguration`: `"CustomDeliveryConfigurationTypeDef"`
- `DefaultState`: `"CampaignStateTypeDef"`
- `Description`: `str`
- `HoldoutPercent`: `int`
- `Hook`: `"CampaignHookTypeDef"`
- `IsPaused`: `bool`
- `Limits`: `"CampaignLimitsTypeDef"`
- `MessageConfiguration`: `"MessageConfigurationTypeDef"`
- `Name`: `str`
- `Schedule`: `"ScheduleTypeDef"`
- `State`: `"CampaignStateTypeDef"`
- `tags`: `Dict[str, str]`
- `TemplateConfiguration`: `"TemplateConfigurationTypeDef"`
- `TreatmentDescription`: `str`
- `TreatmentName`: `str`
- `Version`: `int`


## CampaignSmsMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignSmsMessageTypeDef
```




Optional fields:
- `Body`: `str`
- `MessageType`: `MessageType`
- `OriginationNumber`: `str`
- `SenderId`: `str`
- `EntityId`: `str`
- `TemplateId`: `str`


## CampaignStateTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignStateTypeDef
```




Optional fields:
- `CampaignStatus`: `CampaignStatus`


## CampaignsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CampaignsResponseTypeDef
```


Required fields:
- `Item`: `List["CampaignResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ChannelResponseTypeDef
```




Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## ChannelsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ChannelsResponseTypeDef
```


Required fields:
- `Channels`: `Dict[str, "ChannelResponseTypeDef"]`




## ConditionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ConditionTypeDef
```




Optional fields:
- `Conditions`: `List["SimpleConditionTypeDef"]`
- `Operator`: `Operator`


## ConditionalSplitActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ConditionalSplitActivityTypeDef
```




Optional fields:
- `Condition`: `"ConditionTypeDef"`
- `EvaluationWaitTime`: `"WaitTimeTypeDef"`
- `FalseActivity`: `str`
- `TrueActivity`: `str`


## CreateTemplateMessageBodyTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateTemplateMessageBodyTypeDef
```




Optional fields:
- `Arn`: `str`
- `Message`: `str`
- `RequestID`: `str`


## CustomDeliveryConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CustomDeliveryConfigurationTypeDef
```


Required fields:
- `DeliveryUri`: `str`



Optional fields:
- `EndpointTypes`: `List[__EndpointTypesElement]`


## CustomMessageActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CustomMessageActivityTypeDef
```




Optional fields:
- `DeliveryUri`: `str`
- `EndpointTypes`: `List[__EndpointTypesElement]`
- `MessageConfig`: `"JourneyCustomMessageTypeDef"`
- `NextActivity`: `str`
- `TemplateName`: `str`
- `TemplateVersion`: `str`


## DefaultMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DefaultMessageTypeDef
```




Optional fields:
- `Body`: `str`
- `Substitutions`: `Dict[str, List[str]]`


## DefaultPushNotificationMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DefaultPushNotificationMessageTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `Data`: `Dict[str, str]`
- `SilentPush`: `bool`
- `Substitutions`: `Dict[str, List[str]]`
- `Title`: `str`
- `Url`: `str`


## DefaultPushNotificationTemplateTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DefaultPushNotificationTemplateTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `Sound`: `str`
- `Title`: `str`
- `Url`: `str`


## DirectMessageConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DirectMessageConfigurationTypeDef
```




Optional fields:
- `ADMMessage`: `"ADMMessageTypeDef"`
- `APNSMessage`: `"APNSMessageTypeDef"`
- `BaiduMessage`: `"BaiduMessageTypeDef"`
- `DefaultMessage`: `"DefaultMessageTypeDef"`
- `DefaultPushNotificationMessage`: `"DefaultPushNotificationMessageTypeDef"`
- `EmailMessage`: `"EmailMessageTypeDef"`
- `GCMMessage`: `"GCMMessageTypeDef"`
- `SMSMessage`: `"SMSMessageTypeDef"`
- `VoiceMessage`: `"VoiceMessageTypeDef"`


## EmailChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EmailChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `ConfigurationSet`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `FromAddress`: `str`
- `HasCredential`: `bool`
- `Id`: `str`
- `Identity`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `MessagesPerSecond`: `int`
- `RoleArn`: `str`
- `Version`: `int`


## EmailMessageActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EmailMessageActivityTypeDef
```




Optional fields:
- `MessageConfig`: `"JourneyEmailMessageTypeDef"`
- `NextActivity`: `str`
- `TemplateName`: `str`
- `TemplateVersion`: `str`


## EmailMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EmailMessageTypeDef
```




Optional fields:
- `Body`: `str`
- `FeedbackForwardingAddress`: `str`
- `FromAddress`: `str`
- `RawEmail`: `"RawEmailTypeDef"`
- `ReplyToAddresses`: `List[str]`
- `SimpleEmail`: `"SimpleEmailTypeDef"`
- `Substitutions`: `Dict[str, List[str]]`


## EmailTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EmailTemplateResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `TemplateName`: `str`
- `TemplateType`: `TemplateType`



Optional fields:
- `Arn`: `str`
- `DefaultSubstitutions`: `str`
- `HtmlPart`: `str`
- `RecommenderId`: `str`
- `Subject`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `TextPart`: `str`
- `Version`: `str`


## EndpointBatchItemTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointBatchItemTypeDef
```




Optional fields:
- `Address`: `str`
- `Attributes`: `Dict[str, List[str]]`
- `ChannelType`: `ChannelType`
- `Demographic`: `"EndpointDemographicTypeDef"`
- `EffectiveDate`: `str`
- `EndpointStatus`: `str`
- `Id`: `str`
- `Location`: `"EndpointLocationTypeDef"`
- `Metrics`: `Dict[str, float]`
- `OptOut`: `str`
- `RequestId`: `str`
- `User`: `"EndpointUserTypeDef"`


## EndpointDemographicTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointDemographicTypeDef
```




Optional fields:
- `AppVersion`: `str`
- `Locale`: `str`
- `Make`: `str`
- `Model`: `str`
- `ModelVersion`: `str`
- `Platform`: `str`
- `PlatformVersion`: `str`
- `Timezone`: `str`


## EndpointItemResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointItemResponseTypeDef
```




Optional fields:
- `Message`: `str`
- `StatusCode`: `int`


## EndpointLocationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointLocationTypeDef
```




Optional fields:
- `City`: `str`
- `Country`: `str`
- `Latitude`: `float`
- `Longitude`: `float`
- `PostalCode`: `str`
- `Region`: `str`


## EndpointMessageResultTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointMessageResultTypeDef
```


Required fields:
- `DeliveryStatus`: `DeliveryStatus`
- `StatusCode`: `int`



Optional fields:
- `Address`: `str`
- `MessageId`: `str`
- `StatusMessage`: `str`
- `UpdatedToken`: `str`


## EndpointResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointResponseTypeDef
```




Optional fields:
- `Address`: `str`
- `ApplicationId`: `str`
- `Attributes`: `Dict[str, List[str]]`
- `ChannelType`: `ChannelType`
- `CohortId`: `str`
- `CreationDate`: `str`
- `Demographic`: `"EndpointDemographicTypeDef"`
- `EffectiveDate`: `str`
- `EndpointStatus`: `str`
- `Id`: `str`
- `Location`: `"EndpointLocationTypeDef"`
- `Metrics`: `Dict[str, float]`
- `OptOut`: `str`
- `RequestId`: `str`
- `User`: `"EndpointUserTypeDef"`


## EndpointSendConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointSendConfigurationTypeDef
```




Optional fields:
- `BodyOverride`: `str`
- `Context`: `Dict[str, str]`
- `RawContent`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `TitleOverride`: `str`


## EndpointUserTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointUserTypeDef
```




Optional fields:
- `UserAttributes`: `Dict[str, List[str]]`
- `UserId`: `str`


## EndpointsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointsResponseTypeDef
```


Required fields:
- `Item`: `List["EndpointResponseTypeDef"]`




## EventConditionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventConditionTypeDef
```




Optional fields:
- `Dimensions`: `"EventDimensionsTypeDef"`
- `MessageActivity`: `str`


## EventDimensionsTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventDimensionsTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, "AttributeDimensionTypeDef"]`
- `EventType`: `"SetDimensionTypeDef"`
- `Metrics`: `Dict[str, "MetricDimensionTypeDef"]`


## EventFilterTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventFilterTypeDef
```


Required fields:
- `Dimensions`: `"EventDimensionsTypeDef"`
- `FilterType`: `FilterType`




## EventItemResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventItemResponseTypeDef
```




Optional fields:
- `Message`: `str`
- `StatusCode`: `int`


## EventStartConditionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventStartConditionTypeDef
```




Optional fields:
- `EventFilter`: `"EventFilterTypeDef"`
- `SegmentId`: `str`


## EventStreamTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventStreamTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `DestinationStreamArn`: `str`
- `RoleArn`: `str`



Optional fields:
- `ExternalId`: `str`
- `LastModifiedDate`: `str`
- `LastUpdatedBy`: `str`


## EventTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventTypeDef
```


Required fields:
- `EventType`: `str`
- `Timestamp`: `str`



Optional fields:
- `AppPackageName`: `str`
- `AppTitle`: `str`
- `AppVersionCode`: `str`
- `Attributes`: `Dict[str, str]`
- `ClientSdkVersion`: `str`
- `Metrics`: `Dict[str, float]`
- `SdkName`: `str`
- `Session`: `"SessionTypeDef"`


## EventsBatchTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventsBatchTypeDef
```


Required fields:
- `Endpoint`: `"PublicEndpointTypeDef"`
- `Events`: `Dict[str, "EventTypeDef"]`




## EventsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventsResponseTypeDef
```




Optional fields:
- `Results`: `Dict[str, "ItemResponseTypeDef"]`


## ExportJobResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ExportJobResourceTypeDef
```


Required fields:
- `RoleArn`: `str`
- `S3UrlPrefix`: `str`



Optional fields:
- `SegmentId`: `str`
- `SegmentVersion`: `int`


## ExportJobResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ExportJobResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Definition`: `"ExportJobResourceTypeDef"`
- `Id`: `str`
- `JobStatus`: `JobStatus`
- `Type`: `str`



Optional fields:
- `CompletedPieces`: `int`
- `CompletionDate`: `str`
- `FailedPieces`: `int`
- `Failures`: `List[str]`
- `TotalFailures`: `int`
- `TotalPieces`: `int`
- `TotalProcessed`: `int`


## ExportJobsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ExportJobsResponseTypeDef
```


Required fields:
- `Item`: `List["ExportJobResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## GCMChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GCMChannelResponseTypeDef
```


Required fields:
- `Credential`: `str`
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## GCMMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GCMMessageTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `CollapseKey`: `str`
- `Data`: `Dict[str, str]`
- `IconReference`: `str`
- `ImageIconUrl`: `str`
- `ImageUrl`: `str`
- `Priority`: `str`
- `RawContent`: `str`
- `RestrictedPackageName`: `str`
- `SilentPush`: `bool`
- `SmallImageIconUrl`: `str`
- `Sound`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `TimeToLive`: `int`
- `Title`: `str`
- `Url`: `str`


## GPSCoordinatesTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GPSCoordinatesTypeDef
```


Required fields:
- `Latitude`: `float`
- `Longitude`: `float`




## GPSPointDimensionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GPSPointDimensionTypeDef
```


Required fields:
- `Coordinates`: `"GPSCoordinatesTypeDef"`



Optional fields:
- `RangeInKilometers`: `float`


## HoldoutActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import HoldoutActivityTypeDef
```


Required fields:
- `Percentage`: `int`



Optional fields:
- `NextActivity`: `str`


## ImportJobResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ImportJobResourceTypeDef
```


Required fields:
- `Format`: `Format`
- `RoleArn`: `str`
- `S3Url`: `str`



Optional fields:
- `DefineSegment`: `bool`
- `ExternalId`: `str`
- `RegisterEndpoints`: `bool`
- `SegmentId`: `str`
- `SegmentName`: `str`


## ImportJobResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ImportJobResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Definition`: `"ImportJobResourceTypeDef"`
- `Id`: `str`
- `JobStatus`: `JobStatus`
- `Type`: `str`



Optional fields:
- `CompletedPieces`: `int`
- `CompletionDate`: `str`
- `FailedPieces`: `int`
- `Failures`: `List[str]`
- `TotalFailures`: `int`
- `TotalPieces`: `int`
- `TotalProcessed`: `int`


## ImportJobsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ImportJobsResponseTypeDef
```


Required fields:
- `Item`: `List["ImportJobResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ItemResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ItemResponseTypeDef
```




Optional fields:
- `EndpointItemResponse`: `"EndpointItemResponseTypeDef"`
- `EventsItemResponse`: `Dict[str, "EventItemResponseTypeDef"]`


## JourneyCustomMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyCustomMessageTypeDef
```




Optional fields:
- `Data`: `str`


## JourneyDateRangeKpiResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyDateRangeKpiResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `EndTime`: `datetime`
- `JourneyId`: `str`
- `KpiName`: `str`
- `KpiResult`: `"BaseKpiResultTypeDef"`
- `StartTime`: `datetime`



Optional fields:
- `NextToken`: `str`


## JourneyEmailMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyEmailMessageTypeDef
```




Optional fields:
- `FromAddress`: `str`


## JourneyExecutionActivityMetricsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyExecutionActivityMetricsResponseTypeDef
```


Required fields:
- `ActivityType`: `str`
- `ApplicationId`: `str`
- `JourneyActivityId`: `str`
- `JourneyId`: `str`
- `LastEvaluatedTime`: `str`
- `Metrics`: `Dict[str, str]`




## JourneyExecutionMetricsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyExecutionMetricsResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `JourneyId`: `str`
- `LastEvaluatedTime`: `str`
- `Metrics`: `Dict[str, str]`




## JourneyLimitsTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyLimitsTypeDef
```




Optional fields:
- `DailyCap`: `int`
- `EndpointReentryCap`: `int`
- `MessagesPerSecond`: `int`
- `EndpointReentryInterval`: `str`


## JourneyPushMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyPushMessageTypeDef
```




Optional fields:
- `TimeToLive`: `str`


## JourneyResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `Id`: `str`
- `Name`: `str`



Optional fields:
- `Activities`: `Dict[str, "ActivityTypeDef"]`
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `Limits`: `"JourneyLimitsTypeDef"`
- `LocalTime`: `bool`
- `QuietTime`: `"QuietTimeTypeDef"`
- `RefreshFrequency`: `str`
- `Schedule`: `"JourneyScheduleTypeDef"`
- `StartActivity`: `str`
- `StartCondition`: `"StartConditionTypeDef"`
- `State`: `State`
- `tags`: `Dict[str, str]`
- `WaitForQuietTime`: `bool`
- `RefreshOnSegmentUpdate`: `bool`


## JourneySMSMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneySMSMessageTypeDef
```




Optional fields:
- `MessageType`: `MessageType`
- `OriginationNumber`: `str`
- `SenderId`: `str`
- `EntityId`: `str`
- `TemplateId`: `str`


## JourneyScheduleTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyScheduleTypeDef
```




Optional fields:
- `EndTime`: `datetime`
- `StartTime`: `datetime`
- `Timezone`: `str`


## JourneysResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneysResponseTypeDef
```


Required fields:
- `Item`: `List["JourneyResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListRecommenderConfigurationsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ListRecommenderConfigurationsResponseTypeDef
```


Required fields:
- `Item`: `List["RecommenderConfigurationResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## MessageBodyTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MessageBodyTypeDef
```




Optional fields:
- `Message`: `str`
- `RequestID`: `str`


## MessageConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MessageConfigurationTypeDef
```




Optional fields:
- `ADMMessage`: `"MessageTypeDef"`
- `APNSMessage`: `"MessageTypeDef"`
- `BaiduMessage`: `"MessageTypeDef"`
- `CustomMessage`: `"CampaignCustomMessageTypeDef"`
- `DefaultMessage`: `"MessageTypeDef"`
- `EmailMessage`: `"CampaignEmailMessageTypeDef"`
- `GCMMessage`: `"MessageTypeDef"`
- `SMSMessage`: `"CampaignSmsMessageTypeDef"`


## MessageResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MessageResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`



Optional fields:
- `EndpointResult`: `Dict[str, "EndpointMessageResultTypeDef"]`
- `RequestId`: `str`
- `Result`: `Dict[str, "MessageResultTypeDef"]`


## MessageResultTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MessageResultTypeDef
```


Required fields:
- `DeliveryStatus`: `DeliveryStatus`
- `StatusCode`: `int`



Optional fields:
- `MessageId`: `str`
- `StatusMessage`: `str`
- `UpdatedToken`: `str`


## MessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MessageTypeDef
```




Optional fields:
- `Action`: `Action`
- `Body`: `str`
- `ImageIconUrl`: `str`
- `ImageSmallIconUrl`: `str`
- `ImageUrl`: `str`
- `JsonBody`: `str`
- `MediaUrl`: `str`
- `RawContent`: `str`
- `SilentPush`: `bool`
- `TimeToLive`: `int`
- `Title`: `str`
- `Url`: `str`


## MetricDimensionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MetricDimensionTypeDef
```


Required fields:
- `ComparisonOperator`: `str`
- `Value`: `float`




## MultiConditionalBranchTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MultiConditionalBranchTypeDef
```




Optional fields:
- `Condition`: `"SimpleConditionTypeDef"`
- `NextActivity`: `str`


## MultiConditionalSplitActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MultiConditionalSplitActivityTypeDef
```




Optional fields:
- `Branches`: `List["MultiConditionalBranchTypeDef"]`
- `DefaultActivity`: `str`
- `EvaluationWaitTime`: `"WaitTimeTypeDef"`


## NumberValidateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import NumberValidateResponseTypeDef
```




Optional fields:
- `Carrier`: `str`
- `City`: `str`
- `CleansedPhoneNumberE164`: `str`
- `CleansedPhoneNumberNational`: `str`
- `Country`: `str`
- `CountryCodeIso2`: `str`
- `CountryCodeNumeric`: `str`
- `County`: `str`
- `OriginalCountryCodeIso2`: `str`
- `OriginalPhoneNumber`: `str`
- `PhoneType`: `str`
- `PhoneTypeCode`: `int`
- `Timezone`: `str`
- `ZipCode`: `str`


## PublicEndpointTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PublicEndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Attributes`: `Dict[str, List[str]]`
- `ChannelType`: `ChannelType`
- `Demographic`: `"EndpointDemographicTypeDef"`
- `EffectiveDate`: `str`
- `EndpointStatus`: `str`
- `Location`: `"EndpointLocationTypeDef"`
- `Metrics`: `Dict[str, float]`
- `OptOut`: `str`
- `RequestId`: `str`
- `User`: `"EndpointUserTypeDef"`


## PushMessageActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PushMessageActivityTypeDef
```




Optional fields:
- `MessageConfig`: `"JourneyPushMessageTypeDef"`
- `NextActivity`: `str`
- `TemplateName`: `str`
- `TemplateVersion`: `str`


## PushNotificationTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PushNotificationTemplateResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `TemplateName`: `str`
- `TemplateType`: `TemplateType`



Optional fields:
- `ADM`: `"AndroidPushNotificationTemplateTypeDef"`
- `APNS`: `"APNSPushNotificationTemplateTypeDef"`
- `Arn`: `str`
- `Baidu`: `"AndroidPushNotificationTemplateTypeDef"`
- `Default`: `"DefaultPushNotificationTemplateTypeDef"`
- `DefaultSubstitutions`: `str`
- `GCM`: `"AndroidPushNotificationTemplateTypeDef"`
- `RecommenderId`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `Version`: `str`


## QuietTimeTypeDef

```python
from mypy_boto3_pinpoint.type_defs import QuietTimeTypeDef
```




Optional fields:
- `End`: `str`
- `Start`: `str`


## RandomSplitActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import RandomSplitActivityTypeDef
```




Optional fields:
- `Branches`: `List["RandomSplitEntryTypeDef"]`


## RandomSplitEntryTypeDef

```python
from mypy_boto3_pinpoint.type_defs import RandomSplitEntryTypeDef
```




Optional fields:
- `NextActivity`: `str`
- `Percentage`: `int`


## RawEmailTypeDef

```python
from mypy_boto3_pinpoint.type_defs import RawEmailTypeDef
```




Optional fields:
- `Data`: `Union[bytes, IO[bytes]]`


## RecencyDimensionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import RecencyDimensionTypeDef
```


Required fields:
- `Duration`: `Duration`
- `RecencyType`: `RecencyType`




## RecommenderConfigurationResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import RecommenderConfigurationResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `Id`: `str`
- `LastModifiedDate`: `str`
- `RecommendationProviderRoleArn`: `str`
- `RecommendationProviderUri`: `str`



Optional fields:
- `Attributes`: `Dict[str, str]`
- `Description`: `str`
- `Name`: `str`
- `RecommendationProviderIdType`: `str`
- `RecommendationTransformerUri`: `str`
- `RecommendationsDisplayName`: `str`
- `RecommendationsPerMessage`: `int`


## ResultRowTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ResultRowTypeDef
```


Required fields:
- `GroupedBys`: `List["ResultRowValueTypeDef"]`
- `Values`: `List["ResultRowValueTypeDef"]`




## ResultRowValueTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ResultRowValueTypeDef
```


Required fields:
- `Key`: `str`
- `Type`: `str`
- `Value`: `str`




## SMSChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SMSChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `PromotionalMessagesPerSecond`: `int`
- `SenderId`: `str`
- `ShortCode`: `str`
- `TransactionalMessagesPerSecond`: `int`
- `Version`: `int`


## SMSMessageActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SMSMessageActivityTypeDef
```




Optional fields:
- `MessageConfig`: `"JourneySMSMessageTypeDef"`
- `NextActivity`: `str`
- `TemplateName`: `str`
- `TemplateVersion`: `str`


## SMSMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SMSMessageTypeDef
```




Optional fields:
- `Body`: `str`
- `Keyword`: `str`
- `MediaUrl`: `str`
- `MessageType`: `MessageType`
- `OriginationNumber`: `str`
- `SenderId`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `EntityId`: `str`
- `TemplateId`: `str`


## SMSTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SMSTemplateResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `TemplateName`: `str`
- `TemplateType`: `TemplateType`



Optional fields:
- `Arn`: `str`
- `Body`: `str`
- `DefaultSubstitutions`: `str`
- `RecommenderId`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `Version`: `str`


## ScheduleTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ScheduleTypeDef
```


Required fields:
- `StartTime`: `str`



Optional fields:
- `EndTime`: `str`
- `EventFilter`: `"CampaignEventFilterTypeDef"`
- `Frequency`: `Frequency`
- `IsLocalTime`: `bool`
- `QuietTime`: `"QuietTimeTypeDef"`
- `Timezone`: `str`


## SegmentBehaviorsTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentBehaviorsTypeDef
```




Optional fields:
- `Recency`: `"RecencyDimensionTypeDef"`


## SegmentConditionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentConditionTypeDef
```


Required fields:
- `SegmentId`: `str`




## SegmentDemographicsTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentDemographicsTypeDef
```




Optional fields:
- `AppVersion`: `"SetDimensionTypeDef"`
- `Channel`: `"SetDimensionTypeDef"`
- `DeviceType`: `"SetDimensionTypeDef"`
- `Make`: `"SetDimensionTypeDef"`
- `Model`: `"SetDimensionTypeDef"`
- `Platform`: `"SetDimensionTypeDef"`


## SegmentDimensionsTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentDimensionsTypeDef
```




Optional fields:
- `Attributes`: `Dict[str, "AttributeDimensionTypeDef"]`
- `Behavior`: `"SegmentBehaviorsTypeDef"`
- `Demographic`: `"SegmentDemographicsTypeDef"`
- `Location`: `"SegmentLocationTypeDef"`
- `Metrics`: `Dict[str, "MetricDimensionTypeDef"]`
- `UserAttributes`: `Dict[str, "AttributeDimensionTypeDef"]`


## SegmentGroupListTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentGroupListTypeDef
```




Optional fields:
- `Groups`: `List["SegmentGroupTypeDef"]`
- `Include`: `Include`


## SegmentGroupTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentGroupTypeDef
```




Optional fields:
- `Dimensions`: `List["SegmentDimensionsTypeDef"]`
- `SourceSegments`: `List["SegmentReferenceTypeDef"]`
- `SourceType`: `SourceType`
- `Type`: `TypeType`


## SegmentImportResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentImportResourceTypeDef
```


Required fields:
- `ExternalId`: `str`
- `Format`: `Format`
- `RoleArn`: `str`
- `S3Url`: `str`
- `Size`: `int`



Optional fields:
- `ChannelCounts`: `Dict[str, int]`


## SegmentLocationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentLocationTypeDef
```




Optional fields:
- `Country`: `"SetDimensionTypeDef"`
- `GPSPoint`: `"GPSPointDimensionTypeDef"`


## SegmentReferenceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentReferenceTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `Version`: `int`


## SegmentResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`
- `Arn`: `str`
- `CreationDate`: `str`
- `Id`: `str`
- `SegmentType`: `SegmentType`



Optional fields:
- `Dimensions`: `"SegmentDimensionsTypeDef"`
- `ImportDefinition`: `"SegmentImportResourceTypeDef"`
- `LastModifiedDate`: `str`
- `Name`: `str`
- `SegmentGroups`: `"SegmentGroupListTypeDef"`
- `tags`: `Dict[str, str]`
- `Version`: `int`


## SegmentsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SegmentsResponseTypeDef
```


Required fields:
- `Item`: `List["SegmentResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## SendUsersMessageResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SendUsersMessageResponseTypeDef
```


Required fields:
- `ApplicationId`: `str`



Optional fields:
- `RequestId`: `str`
- `Result`: `Dict[str, Dict[str, "EndpointMessageResultTypeDef"]]`


## SessionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SessionTypeDef
```


Required fields:
- `Id`: `str`
- `StartTimestamp`: `str`



Optional fields:
- `Duration`: `int`
- `StopTimestamp`: `str`


## SetDimensionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SetDimensionTypeDef
```


Required fields:
- `Values`: `List[str]`



Optional fields:
- `DimensionType`: `DimensionType`


## SimpleConditionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SimpleConditionTypeDef
```




Optional fields:
- `EventCondition`: `"EventConditionTypeDef"`
- `SegmentCondition`: `"SegmentConditionTypeDef"`
- `SegmentDimensions`: `"SegmentDimensionsTypeDef"`


## SimpleEmailPartTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SimpleEmailPartTypeDef
```




Optional fields:
- `Charset`: `str`
- `Data`: `str`


## SimpleEmailTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SimpleEmailTypeDef
```




Optional fields:
- `HtmlPart`: `"SimpleEmailPartTypeDef"`
- `Subject`: `"SimpleEmailPartTypeDef"`
- `TextPart`: `"SimpleEmailPartTypeDef"`


## StartConditionTypeDef

```python
from mypy_boto3_pinpoint.type_defs import StartConditionTypeDef
```




Optional fields:
- `Description`: `str`
- `EventStartCondition`: `"EventStartConditionTypeDef"`
- `SegmentStartCondition`: `"SegmentConditionTypeDef"`


## TagsModelTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TagsModelTypeDef
```


Required fields:
- `tags`: `Dict[str, str]`




## TemplateConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplateConfigurationTypeDef
```




Optional fields:
- `EmailTemplate`: `"TemplateTypeDef"`
- `PushTemplate`: `"TemplateTypeDef"`
- `SMSTemplate`: `"TemplateTypeDef"`
- `VoiceTemplate`: `"TemplateTypeDef"`


## TemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplateResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `TemplateName`: `str`
- `TemplateType`: `TemplateType`



Optional fields:
- `Arn`: `str`
- `DefaultSubstitutions`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `Version`: `str`


## TemplateTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplateTypeDef
```




Optional fields:
- `Name`: `str`
- `Version`: `str`


## TemplateVersionResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplateVersionResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `TemplateName`: `str`
- `TemplateType`: `str`



Optional fields:
- `DefaultSubstitutions`: `str`
- `TemplateDescription`: `str`
- `Version`: `str`


## TemplateVersionsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplateVersionsResponseTypeDef
```


Required fields:
- `Item`: `List["TemplateVersionResponseTypeDef"]`



Optional fields:
- `Message`: `str`
- `NextToken`: `str`
- `RequestID`: `str`


## TemplatesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplatesResponseTypeDef
```


Required fields:
- `Item`: `List["TemplateResponseTypeDef"]`



Optional fields:
- `NextToken`: `str`


## TreatmentResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TreatmentResourceTypeDef
```


Required fields:
- `Id`: `str`
- `SizePercent`: `int`



Optional fields:
- `CustomDeliveryConfiguration`: `"CustomDeliveryConfigurationTypeDef"`
- `MessageConfiguration`: `"MessageConfigurationTypeDef"`
- `Schedule`: `"ScheduleTypeDef"`
- `State`: `"CampaignStateTypeDef"`
- `TemplateConfiguration`: `"TemplateConfigurationTypeDef"`
- `TreatmentDescription`: `str`
- `TreatmentName`: `str`


## VoiceChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import VoiceChannelResponseTypeDef
```


Required fields:
- `Platform`: `str`



Optional fields:
- `ApplicationId`: `str`
- `CreationDate`: `str`
- `Enabled`: `bool`
- `HasCredential`: `bool`
- `Id`: `str`
- `IsArchived`: `bool`
- `LastModifiedBy`: `str`
- `LastModifiedDate`: `str`
- `Version`: `int`


## VoiceMessageTypeDef

```python
from mypy_boto3_pinpoint.type_defs import VoiceMessageTypeDef
```




Optional fields:
- `Body`: `str`
- `LanguageCode`: `str`
- `OriginationNumber`: `str`
- `Substitutions`: `Dict[str, List[str]]`
- `VoiceId`: `str`


## VoiceTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import VoiceTemplateResponseTypeDef
```


Required fields:
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `TemplateName`: `str`
- `TemplateType`: `TemplateType`



Optional fields:
- `Arn`: `str`
- `Body`: `str`
- `DefaultSubstitutions`: `str`
- `LanguageCode`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `Version`: `str`
- `VoiceId`: `str`


## WaitActivityTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WaitActivityTypeDef
```




Optional fields:
- `NextActivity`: `str`
- `WaitTime`: `"WaitTimeTypeDef"`


## WaitTimeTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WaitTimeTypeDef
```




Optional fields:
- `WaitFor`: `str`
- `WaitUntil`: `str`


## WriteTreatmentResourceTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WriteTreatmentResourceTypeDef
```


Required fields:
- `SizePercent`: `int`



Optional fields:
- `CustomDeliveryConfiguration`: `"CustomDeliveryConfigurationTypeDef"`
- `MessageConfiguration`: `"MessageConfigurationTypeDef"`
- `Schedule`: `"ScheduleTypeDef"`
- `TemplateConfiguration`: `"TemplateConfigurationTypeDef"`
- `TreatmentDescription`: `str`
- `TreatmentName`: `str`


## ADMChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ADMChannelRequestTypeDef
```


Required fields:
- `ClientId`: `str`
- `ClientSecret`: `str`



Optional fields:
- `Enabled`: `bool`


## APNSChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSChannelRequestTypeDef
```




Optional fields:
- `BundleId`: `str`
- `Certificate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `PrivateKey`: `str`
- `TeamId`: `str`
- `TokenKey`: `str`
- `TokenKeyId`: `str`


## APNSSandboxChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSSandboxChannelRequestTypeDef
```




Optional fields:
- `BundleId`: `str`
- `Certificate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `PrivateKey`: `str`
- `TeamId`: `str`
- `TokenKey`: `str`
- `TokenKeyId`: `str`


## APNSVoipChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSVoipChannelRequestTypeDef
```




Optional fields:
- `BundleId`: `str`
- `Certificate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `PrivateKey`: `str`
- `TeamId`: `str`
- `TokenKey`: `str`
- `TokenKeyId`: `str`


## APNSVoipSandboxChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import APNSVoipSandboxChannelRequestTypeDef
```




Optional fields:
- `BundleId`: `str`
- `Certificate`: `str`
- `DefaultAuthenticationMethod`: `str`
- `Enabled`: `bool`
- `PrivateKey`: `str`
- `TeamId`: `str`
- `TokenKey`: `str`
- `TokenKeyId`: `str`


## BaiduChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import BaiduChannelRequestTypeDef
```


Required fields:
- `ApiKey`: `str`
- `SecretKey`: `str`



Optional fields:
- `Enabled`: `bool`


## CreateAppResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateAppResponseTypeDef
```


Required fields:
- `ApplicationResponse`: `"ApplicationResponseTypeDef"`




## CreateApplicationRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateApplicationRequestTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `tags`: `Dict[str, str]`


## CreateCampaignResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateCampaignResponseTypeDef
```


Required fields:
- `CampaignResponse`: `"CampaignResponseTypeDef"`




## CreateEmailTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateEmailTemplateResponseTypeDef
```


Required fields:
- `CreateTemplateMessageBody`: `"CreateTemplateMessageBodyTypeDef"`




## CreateExportJobResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateExportJobResponseTypeDef
```


Required fields:
- `ExportJobResponse`: `"ExportJobResponseTypeDef"`




## CreateImportJobResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateImportJobResponseTypeDef
```


Required fields:
- `ImportJobResponse`: `"ImportJobResponseTypeDef"`




## CreateJourneyResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateJourneyResponseTypeDef
```


Required fields:
- `JourneyResponse`: `"JourneyResponseTypeDef"`




## CreatePushTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreatePushTemplateResponseTypeDef
```


Required fields:
- `CreateTemplateMessageBody`: `"CreateTemplateMessageBodyTypeDef"`




## CreateRecommenderConfigurationResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateRecommenderConfigurationResponseTypeDef
```


Required fields:
- `RecommenderConfigurationResponse`: `"RecommenderConfigurationResponseTypeDef"`




## CreateRecommenderConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateRecommenderConfigurationTypeDef
```


Required fields:
- `RecommendationProviderRoleArn`: `str`
- `RecommendationProviderUri`: `str`



Optional fields:
- `Attributes`: `Dict[str, str]`
- `Description`: `str`
- `Name`: `str`
- `RecommendationProviderIdType`: `str`
- `RecommendationTransformerUri`: `str`
- `RecommendationsDisplayName`: `str`
- `RecommendationsPerMessage`: `int`


## CreateSegmentResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateSegmentResponseTypeDef
```


Required fields:
- `SegmentResponse`: `"SegmentResponseTypeDef"`




## CreateSmsTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateSmsTemplateResponseTypeDef
```


Required fields:
- `CreateTemplateMessageBody`: `"CreateTemplateMessageBodyTypeDef"`




## CreateVoiceTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import CreateVoiceTemplateResponseTypeDef
```


Required fields:
- `CreateTemplateMessageBody`: `"CreateTemplateMessageBodyTypeDef"`




## DeleteAdmChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteAdmChannelResponseTypeDef
```


Required fields:
- `ADMChannelResponse`: `"ADMChannelResponseTypeDef"`




## DeleteApnsChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteApnsChannelResponseTypeDef
```


Required fields:
- `APNSChannelResponse`: `"APNSChannelResponseTypeDef"`




## DeleteApnsSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteApnsSandboxChannelResponseTypeDef
```


Required fields:
- `APNSSandboxChannelResponse`: `"APNSSandboxChannelResponseTypeDef"`




## DeleteApnsVoipChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteApnsVoipChannelResponseTypeDef
```


Required fields:
- `APNSVoipChannelResponse`: `"APNSVoipChannelResponseTypeDef"`




## DeleteApnsVoipSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteApnsVoipSandboxChannelResponseTypeDef
```


Required fields:
- `APNSVoipSandboxChannelResponse`: `"APNSVoipSandboxChannelResponseTypeDef"`




## DeleteAppResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteAppResponseTypeDef
```


Required fields:
- `ApplicationResponse`: `"ApplicationResponseTypeDef"`




## DeleteBaiduChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteBaiduChannelResponseTypeDef
```


Required fields:
- `BaiduChannelResponse`: `"BaiduChannelResponseTypeDef"`




## DeleteCampaignResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteCampaignResponseTypeDef
```


Required fields:
- `CampaignResponse`: `"CampaignResponseTypeDef"`




## DeleteEmailChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteEmailChannelResponseTypeDef
```


Required fields:
- `EmailChannelResponse`: `"EmailChannelResponseTypeDef"`




## DeleteEmailTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteEmailTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## DeleteEndpointResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteEndpointResponseTypeDef
```


Required fields:
- `EndpointResponse`: `"EndpointResponseTypeDef"`




## DeleteEventStreamResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteEventStreamResponseTypeDef
```


Required fields:
- `EventStream`: `"EventStreamTypeDef"`




## DeleteGcmChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteGcmChannelResponseTypeDef
```


Required fields:
- `GCMChannelResponse`: `"GCMChannelResponseTypeDef"`




## DeleteJourneyResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteJourneyResponseTypeDef
```


Required fields:
- `JourneyResponse`: `"JourneyResponseTypeDef"`




## DeletePushTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeletePushTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## DeleteRecommenderConfigurationResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteRecommenderConfigurationResponseTypeDef
```


Required fields:
- `RecommenderConfigurationResponse`: `"RecommenderConfigurationResponseTypeDef"`




## DeleteSegmentResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteSegmentResponseTypeDef
```


Required fields:
- `SegmentResponse`: `"SegmentResponseTypeDef"`




## DeleteSmsChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteSmsChannelResponseTypeDef
```


Required fields:
- `SMSChannelResponse`: `"SMSChannelResponseTypeDef"`




## DeleteSmsTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteSmsTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## DeleteUserEndpointsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteUserEndpointsResponseTypeDef
```


Required fields:
- `EndpointsResponse`: `"EndpointsResponseTypeDef"`




## DeleteVoiceChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteVoiceChannelResponseTypeDef
```


Required fields:
- `VoiceChannelResponse`: `"VoiceChannelResponseTypeDef"`




## DeleteVoiceTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import DeleteVoiceTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## EmailChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EmailChannelRequestTypeDef
```


Required fields:
- `FromAddress`: `str`
- `Identity`: `str`



Optional fields:
- `ConfigurationSet`: `str`
- `Enabled`: `bool`
- `RoleArn`: `str`


## EmailTemplateRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EmailTemplateRequestTypeDef
```




Optional fields:
- `DefaultSubstitutions`: `str`
- `HtmlPart`: `str`
- `RecommenderId`: `str`
- `Subject`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `TextPart`: `str`


## EndpointBatchRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointBatchRequestTypeDef
```


Required fields:
- `Item`: `List["EndpointBatchItemTypeDef"]`




## EndpointRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EndpointRequestTypeDef
```




Optional fields:
- `Address`: `str`
- `Attributes`: `Dict[str, List[str]]`
- `ChannelType`: `ChannelType`
- `Demographic`: `"EndpointDemographicTypeDef"`
- `EffectiveDate`: `str`
- `EndpointStatus`: `str`
- `Location`: `"EndpointLocationTypeDef"`
- `Metrics`: `Dict[str, float]`
- `OptOut`: `str`
- `RequestId`: `str`
- `User`: `"EndpointUserTypeDef"`


## EventsRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import EventsRequestTypeDef
```


Required fields:
- `BatchItem`: `Dict[str, "EventsBatchTypeDef"]`




## ExportJobRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ExportJobRequestTypeDef
```


Required fields:
- `RoleArn`: `str`
- `S3UrlPrefix`: `str`



Optional fields:
- `SegmentId`: `str`
- `SegmentVersion`: `int`


## GCMChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GCMChannelRequestTypeDef
```


Required fields:
- `ApiKey`: `str`



Optional fields:
- `Enabled`: `bool`


## GetAdmChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetAdmChannelResponseTypeDef
```


Required fields:
- `ADMChannelResponse`: `"ADMChannelResponseTypeDef"`




## GetApnsChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetApnsChannelResponseTypeDef
```


Required fields:
- `APNSChannelResponse`: `"APNSChannelResponseTypeDef"`




## GetApnsSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetApnsSandboxChannelResponseTypeDef
```


Required fields:
- `APNSSandboxChannelResponse`: `"APNSSandboxChannelResponseTypeDef"`




## GetApnsVoipChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetApnsVoipChannelResponseTypeDef
```


Required fields:
- `APNSVoipChannelResponse`: `"APNSVoipChannelResponseTypeDef"`




## GetApnsVoipSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetApnsVoipSandboxChannelResponseTypeDef
```


Required fields:
- `APNSVoipSandboxChannelResponse`: `"APNSVoipSandboxChannelResponseTypeDef"`




## GetAppResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetAppResponseTypeDef
```


Required fields:
- `ApplicationResponse`: `"ApplicationResponseTypeDef"`




## GetApplicationDateRangeKpiResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetApplicationDateRangeKpiResponseTypeDef
```


Required fields:
- `ApplicationDateRangeKpiResponse`: `"ApplicationDateRangeKpiResponseTypeDef"`




## GetApplicationSettingsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetApplicationSettingsResponseTypeDef
```


Required fields:
- `ApplicationSettingsResource`: `"ApplicationSettingsResourceTypeDef"`




## GetAppsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetAppsResponseTypeDef
```


Required fields:
- `ApplicationsResponse`: `"ApplicationsResponseTypeDef"`




## GetBaiduChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetBaiduChannelResponseTypeDef
```


Required fields:
- `BaiduChannelResponse`: `"BaiduChannelResponseTypeDef"`




## GetCampaignActivitiesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetCampaignActivitiesResponseTypeDef
```


Required fields:
- `ActivitiesResponse`: `"ActivitiesResponseTypeDef"`




## GetCampaignDateRangeKpiResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetCampaignDateRangeKpiResponseTypeDef
```


Required fields:
- `CampaignDateRangeKpiResponse`: `"CampaignDateRangeKpiResponseTypeDef"`




## GetCampaignResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetCampaignResponseTypeDef
```


Required fields:
- `CampaignResponse`: `"CampaignResponseTypeDef"`




## GetCampaignVersionResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetCampaignVersionResponseTypeDef
```


Required fields:
- `CampaignResponse`: `"CampaignResponseTypeDef"`




## GetCampaignVersionsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetCampaignVersionsResponseTypeDef
```


Required fields:
- `CampaignsResponse`: `"CampaignsResponseTypeDef"`




## GetCampaignsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetCampaignsResponseTypeDef
```


Required fields:
- `CampaignsResponse`: `"CampaignsResponseTypeDef"`




## GetChannelsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetChannelsResponseTypeDef
```


Required fields:
- `ChannelsResponse`: `"ChannelsResponseTypeDef"`




## GetEmailChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetEmailChannelResponseTypeDef
```


Required fields:
- `EmailChannelResponse`: `"EmailChannelResponseTypeDef"`




## GetEmailTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetEmailTemplateResponseTypeDef
```


Required fields:
- `EmailTemplateResponse`: `"EmailTemplateResponseTypeDef"`




## GetEndpointResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetEndpointResponseTypeDef
```


Required fields:
- `EndpointResponse`: `"EndpointResponseTypeDef"`




## GetEventStreamResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetEventStreamResponseTypeDef
```


Required fields:
- `EventStream`: `"EventStreamTypeDef"`




## GetExportJobResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetExportJobResponseTypeDef
```


Required fields:
- `ExportJobResponse`: `"ExportJobResponseTypeDef"`




## GetExportJobsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetExportJobsResponseTypeDef
```


Required fields:
- `ExportJobsResponse`: `"ExportJobsResponseTypeDef"`




## GetGcmChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetGcmChannelResponseTypeDef
```


Required fields:
- `GCMChannelResponse`: `"GCMChannelResponseTypeDef"`




## GetImportJobResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetImportJobResponseTypeDef
```


Required fields:
- `ImportJobResponse`: `"ImportJobResponseTypeDef"`




## GetImportJobsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetImportJobsResponseTypeDef
```


Required fields:
- `ImportJobsResponse`: `"ImportJobsResponseTypeDef"`




## GetJourneyDateRangeKpiResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetJourneyDateRangeKpiResponseTypeDef
```


Required fields:
- `JourneyDateRangeKpiResponse`: `"JourneyDateRangeKpiResponseTypeDef"`




## GetJourneyExecutionActivityMetricsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetJourneyExecutionActivityMetricsResponseTypeDef
```


Required fields:
- `JourneyExecutionActivityMetricsResponse`: `"JourneyExecutionActivityMetricsResponseTypeDef"`




## GetJourneyExecutionMetricsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetJourneyExecutionMetricsResponseTypeDef
```


Required fields:
- `JourneyExecutionMetricsResponse`: `"JourneyExecutionMetricsResponseTypeDef"`




## GetJourneyResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetJourneyResponseTypeDef
```


Required fields:
- `JourneyResponse`: `"JourneyResponseTypeDef"`




## GetPushTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetPushTemplateResponseTypeDef
```


Required fields:
- `PushNotificationTemplateResponse`: `"PushNotificationTemplateResponseTypeDef"`




## GetRecommenderConfigurationResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetRecommenderConfigurationResponseTypeDef
```


Required fields:
- `RecommenderConfigurationResponse`: `"RecommenderConfigurationResponseTypeDef"`




## GetRecommenderConfigurationsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetRecommenderConfigurationsResponseTypeDef
```


Required fields:
- `ListRecommenderConfigurationsResponse`: `"ListRecommenderConfigurationsResponseTypeDef"`




## GetSegmentExportJobsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSegmentExportJobsResponseTypeDef
```


Required fields:
- `ExportJobsResponse`: `"ExportJobsResponseTypeDef"`




## GetSegmentImportJobsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSegmentImportJobsResponseTypeDef
```


Required fields:
- `ImportJobsResponse`: `"ImportJobsResponseTypeDef"`




## GetSegmentResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSegmentResponseTypeDef
```


Required fields:
- `SegmentResponse`: `"SegmentResponseTypeDef"`




## GetSegmentVersionResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSegmentVersionResponseTypeDef
```


Required fields:
- `SegmentResponse`: `"SegmentResponseTypeDef"`




## GetSegmentVersionsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSegmentVersionsResponseTypeDef
```


Required fields:
- `SegmentsResponse`: `"SegmentsResponseTypeDef"`




## GetSegmentsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSegmentsResponseTypeDef
```


Required fields:
- `SegmentsResponse`: `"SegmentsResponseTypeDef"`




## GetSmsChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSmsChannelResponseTypeDef
```


Required fields:
- `SMSChannelResponse`: `"SMSChannelResponseTypeDef"`




## GetSmsTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetSmsTemplateResponseTypeDef
```


Required fields:
- `SMSTemplateResponse`: `"SMSTemplateResponseTypeDef"`




## GetUserEndpointsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetUserEndpointsResponseTypeDef
```


Required fields:
- `EndpointsResponse`: `"EndpointsResponseTypeDef"`




## GetVoiceChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetVoiceChannelResponseTypeDef
```


Required fields:
- `VoiceChannelResponse`: `"VoiceChannelResponseTypeDef"`




## GetVoiceTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import GetVoiceTemplateResponseTypeDef
```


Required fields:
- `VoiceTemplateResponse`: `"VoiceTemplateResponseTypeDef"`




## ImportJobRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ImportJobRequestTypeDef
```


Required fields:
- `Format`: `Format`
- `RoleArn`: `str`
- `S3Url`: `str`



Optional fields:
- `DefineSegment`: `bool`
- `ExternalId`: `str`
- `RegisterEndpoints`: `bool`
- `SegmentId`: `str`
- `SegmentName`: `str`


## JourneyStateRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import JourneyStateRequestTypeDef
```




Optional fields:
- `State`: `State`


## ListJourneysResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ListJourneysResponseTypeDef
```


Required fields:
- `JourneysResponse`: `"JourneysResponseTypeDef"`




## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ListTagsForResourceResponseTypeDef
```


Required fields:
- `TagsModel`: `"TagsModelTypeDef"`




## ListTemplateVersionsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ListTemplateVersionsResponseTypeDef
```


Required fields:
- `TemplateVersionsResponse`: `"TemplateVersionsResponseTypeDef"`




## ListTemplatesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import ListTemplatesResponseTypeDef
```


Required fields:
- `TemplatesResponse`: `"TemplatesResponseTypeDef"`




## MessageRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import MessageRequestTypeDef
```


Required fields:
- `MessageConfiguration`: `"DirectMessageConfigurationTypeDef"`



Optional fields:
- `Addresses`: `Dict[str, "AddressConfigurationTypeDef"]`
- `Context`: `Dict[str, str]`
- `Endpoints`: `Dict[str, "EndpointSendConfigurationTypeDef"]`
- `TemplateConfiguration`: `"TemplateConfigurationTypeDef"`
- `TraceId`: `str`


## NumberValidateRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import NumberValidateRequestTypeDef
```




Optional fields:
- `IsoCountryCode`: `str`
- `PhoneNumber`: `str`


## PhoneNumberValidateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PhoneNumberValidateResponseTypeDef
```


Required fields:
- `NumberValidateResponse`: `"NumberValidateResponseTypeDef"`




## PushNotificationTemplateRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PushNotificationTemplateRequestTypeDef
```




Optional fields:
- `ADM`: `"AndroidPushNotificationTemplateTypeDef"`
- `APNS`: `"APNSPushNotificationTemplateTypeDef"`
- `Baidu`: `"AndroidPushNotificationTemplateTypeDef"`
- `Default`: `"DefaultPushNotificationTemplateTypeDef"`
- `DefaultSubstitutions`: `str`
- `GCM`: `"AndroidPushNotificationTemplateTypeDef"`
- `RecommenderId`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`


## PutEventStreamResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PutEventStreamResponseTypeDef
```


Required fields:
- `EventStream`: `"EventStreamTypeDef"`




## PutEventsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import PutEventsResponseTypeDef
```


Required fields:
- `EventsResponse`: `"EventsResponseTypeDef"`




## RemoveAttributesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import RemoveAttributesResponseTypeDef
```


Required fields:
- `AttributesResource`: `"AttributesResourceTypeDef"`




## SMSChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SMSChannelRequestTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `SenderId`: `str`
- `ShortCode`: `str`


## SMSTemplateRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SMSTemplateRequestTypeDef
```




Optional fields:
- `Body`: `str`
- `DefaultSubstitutions`: `str`
- `RecommenderId`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`


## SendMessagesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SendMessagesResponseTypeDef
```


Required fields:
- `MessageResponse`: `"MessageResponseTypeDef"`




## SendUsersMessageRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SendUsersMessageRequestTypeDef
```


Required fields:
- `MessageConfiguration`: `"DirectMessageConfigurationTypeDef"`
- `Users`: `Dict[str, "EndpointSendConfigurationTypeDef"]`



Optional fields:
- `Context`: `Dict[str, str]`
- `TemplateConfiguration`: `"TemplateConfigurationTypeDef"`
- `TraceId`: `str`


## SendUsersMessagesResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import SendUsersMessagesResponseTypeDef
```


Required fields:
- `SendUsersMessageResponse`: `"SendUsersMessageResponseTypeDef"`




## TemplateActiveVersionRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import TemplateActiveVersionRequestTypeDef
```




Optional fields:
- `Version`: `str`


## UpdateAdmChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateAdmChannelResponseTypeDef
```


Required fields:
- `ADMChannelResponse`: `"ADMChannelResponseTypeDef"`




## UpdateApnsChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateApnsChannelResponseTypeDef
```


Required fields:
- `APNSChannelResponse`: `"APNSChannelResponseTypeDef"`




## UpdateApnsSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateApnsSandboxChannelResponseTypeDef
```


Required fields:
- `APNSSandboxChannelResponse`: `"APNSSandboxChannelResponseTypeDef"`




## UpdateApnsVoipChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateApnsVoipChannelResponseTypeDef
```


Required fields:
- `APNSVoipChannelResponse`: `"APNSVoipChannelResponseTypeDef"`




## UpdateApnsVoipSandboxChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateApnsVoipSandboxChannelResponseTypeDef
```


Required fields:
- `APNSVoipSandboxChannelResponse`: `"APNSVoipSandboxChannelResponseTypeDef"`




## UpdateApplicationSettingsResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateApplicationSettingsResponseTypeDef
```


Required fields:
- `ApplicationSettingsResource`: `"ApplicationSettingsResourceTypeDef"`




## UpdateAttributesRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateAttributesRequestTypeDef
```




Optional fields:
- `Blacklist`: `List[str]`


## UpdateBaiduChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateBaiduChannelResponseTypeDef
```


Required fields:
- `BaiduChannelResponse`: `"BaiduChannelResponseTypeDef"`




## UpdateCampaignResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateCampaignResponseTypeDef
```


Required fields:
- `CampaignResponse`: `"CampaignResponseTypeDef"`




## UpdateEmailChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateEmailChannelResponseTypeDef
```


Required fields:
- `EmailChannelResponse`: `"EmailChannelResponseTypeDef"`




## UpdateEmailTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateEmailTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## UpdateEndpointResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateEndpointResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## UpdateEndpointsBatchResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateEndpointsBatchResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## UpdateGcmChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateGcmChannelResponseTypeDef
```


Required fields:
- `GCMChannelResponse`: `"GCMChannelResponseTypeDef"`




## UpdateJourneyResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateJourneyResponseTypeDef
```


Required fields:
- `JourneyResponse`: `"JourneyResponseTypeDef"`




## UpdateJourneyStateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateJourneyStateResponseTypeDef
```


Required fields:
- `JourneyResponse`: `"JourneyResponseTypeDef"`




## UpdatePushTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdatePushTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## UpdateRecommenderConfigurationResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateRecommenderConfigurationResponseTypeDef
```


Required fields:
- `RecommenderConfigurationResponse`: `"RecommenderConfigurationResponseTypeDef"`




## UpdateRecommenderConfigurationTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateRecommenderConfigurationTypeDef
```


Required fields:
- `RecommendationProviderRoleArn`: `str`
- `RecommendationProviderUri`: `str`



Optional fields:
- `Attributes`: `Dict[str, str]`
- `Description`: `str`
- `Name`: `str`
- `RecommendationProviderIdType`: `str`
- `RecommendationTransformerUri`: `str`
- `RecommendationsDisplayName`: `str`
- `RecommendationsPerMessage`: `int`


## UpdateSegmentResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateSegmentResponseTypeDef
```


Required fields:
- `SegmentResponse`: `"SegmentResponseTypeDef"`




## UpdateSmsChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateSmsChannelResponseTypeDef
```


Required fields:
- `SMSChannelResponse`: `"SMSChannelResponseTypeDef"`




## UpdateSmsTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateSmsTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## UpdateTemplateActiveVersionResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateTemplateActiveVersionResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## UpdateVoiceChannelResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateVoiceChannelResponseTypeDef
```


Required fields:
- `VoiceChannelResponse`: `"VoiceChannelResponseTypeDef"`




## UpdateVoiceTemplateResponseTypeDef

```python
from mypy_boto3_pinpoint.type_defs import UpdateVoiceTemplateResponseTypeDef
```


Required fields:
- `MessageBody`: `"MessageBodyTypeDef"`




## VoiceChannelRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import VoiceChannelRequestTypeDef
```




Optional fields:
- `Enabled`: `bool`


## VoiceTemplateRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import VoiceTemplateRequestTypeDef
```




Optional fields:
- `Body`: `str`
- `DefaultSubstitutions`: `str`
- `LanguageCode`: `str`
- `tags`: `Dict[str, str]`
- `TemplateDescription`: `str`
- `VoiceId`: `str`


## WriteApplicationSettingsRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WriteApplicationSettingsRequestTypeDef
```




Optional fields:
- `CampaignHook`: `"CampaignHookTypeDef"`
- `CloudWatchMetricsEnabled`: `bool`
- `EventTaggingEnabled`: `bool`
- `Limits`: `"CampaignLimitsTypeDef"`
- `QuietTime`: `"QuietTimeTypeDef"`


## WriteCampaignRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WriteCampaignRequestTypeDef
```




Optional fields:
- `AdditionalTreatments`: `List["WriteTreatmentResourceTypeDef"]`
- `CustomDeliveryConfiguration`: `"CustomDeliveryConfigurationTypeDef"`
- `Description`: `str`
- `HoldoutPercent`: `int`
- `Hook`: `"CampaignHookTypeDef"`
- `IsPaused`: `bool`
- `Limits`: `"CampaignLimitsTypeDef"`
- `MessageConfiguration`: `"MessageConfigurationTypeDef"`
- `Name`: `str`
- `Schedule`: `"ScheduleTypeDef"`
- `SegmentId`: `str`
- `SegmentVersion`: `int`
- `tags`: `Dict[str, str]`
- `TemplateConfiguration`: `"TemplateConfigurationTypeDef"`
- `TreatmentDescription`: `str`
- `TreatmentName`: `str`


## WriteEventStreamTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WriteEventStreamTypeDef
```


Required fields:
- `DestinationStreamArn`: `str`
- `RoleArn`: `str`




## WriteJourneyRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WriteJourneyRequestTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Activities`: `Dict[str, "ActivityTypeDef"]`
- `CreationDate`: `str`
- `LastModifiedDate`: `str`
- `Limits`: `"JourneyLimitsTypeDef"`
- `LocalTime`: `bool`
- `QuietTime`: `"QuietTimeTypeDef"`
- `RefreshFrequency`: `str`
- `Schedule`: `"JourneyScheduleTypeDef"`
- `StartActivity`: `str`
- `StartCondition`: `"StartConditionTypeDef"`
- `State`: `State`
- `WaitForQuietTime`: `bool`
- `RefreshOnSegmentUpdate`: `bool`


## WriteSegmentRequestTypeDef

```python
from mypy_boto3_pinpoint.type_defs import WriteSegmentRequestTypeDef
```




Optional fields:
- `Dimensions`: `"SegmentDimensionsTypeDef"`
- `Name`: `str`
- `SegmentGroups`: `"SegmentGroupListTypeDef"`
- `tags`: `Dict[str, str]`

