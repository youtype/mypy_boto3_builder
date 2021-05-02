# PinpointClient for boto3 Pinpoint module

> [Index](../index.md) > [Pinpoint](./index.md) > PinpointClient

Auto-generated documentation for [Pinpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint)
type annotations stubs module [mypy_boto3_pinpoint](https://pypi.org/project/mypy-boto3-pinpoint/).

- [PinpointClient for boto3 Pinpoint module](#pinpointclient-for-boto3-pinpoint-module)
  - [PinpointClient](#pinpointclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_app](#create_app)
    - [create_campaign](#create_campaign)
    - [create_email_template](#create_email_template)
    - [create_export_job](#create_export_job)
    - [create_import_job](#create_import_job)
    - [create_journey](#create_journey)
    - [create_push_template](#create_push_template)
    - [create_recommender_configuration](#create_recommender_configuration)
    - [create_segment](#create_segment)
    - [create_sms_template](#create_sms_template)
    - [create_voice_template](#create_voice_template)
    - [delete_adm_channel](#delete_adm_channel)
    - [delete_apns_channel](#delete_apns_channel)
    - [delete_apns_sandbox_channel](#delete_apns_sandbox_channel)
    - [delete_apns_voip_channel](#delete_apns_voip_channel)
    - [delete_apns_voip_sandbox_channel](#delete_apns_voip_sandbox_channel)
    - [delete_app](#delete_app)
    - [delete_baidu_channel](#delete_baidu_channel)
    - [delete_campaign](#delete_campaign)
    - [delete_email_channel](#delete_email_channel)
    - [delete_email_template](#delete_email_template)
    - [delete_endpoint](#delete_endpoint)
    - [delete_event_stream](#delete_event_stream)
    - [delete_gcm_channel](#delete_gcm_channel)
    - [delete_journey](#delete_journey)
    - [delete_push_template](#delete_push_template)
    - [delete_recommender_configuration](#delete_recommender_configuration)
    - [delete_segment](#delete_segment)
    - [delete_sms_channel](#delete_sms_channel)
    - [delete_sms_template](#delete_sms_template)
    - [delete_user_endpoints](#delete_user_endpoints)
    - [delete_voice_channel](#delete_voice_channel)
    - [delete_voice_template](#delete_voice_template)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_adm_channel](#get_adm_channel)
    - [get_apns_channel](#get_apns_channel)
    - [get_apns_sandbox_channel](#get_apns_sandbox_channel)
    - [get_apns_voip_channel](#get_apns_voip_channel)
    - [get_apns_voip_sandbox_channel](#get_apns_voip_sandbox_channel)
    - [get_app](#get_app)
    - [get_application_date_range_kpi](#get_application_date_range_kpi)
    - [get_application_settings](#get_application_settings)
    - [get_apps](#get_apps)
    - [get_baidu_channel](#get_baidu_channel)
    - [get_campaign](#get_campaign)
    - [get_campaign_activities](#get_campaign_activities)
    - [get_campaign_date_range_kpi](#get_campaign_date_range_kpi)
    - [get_campaign_version](#get_campaign_version)
    - [get_campaign_versions](#get_campaign_versions)
    - [get_campaigns](#get_campaigns)
    - [get_channels](#get_channels)
    - [get_email_channel](#get_email_channel)
    - [get_email_template](#get_email_template)
    - [get_endpoint](#get_endpoint)
    - [get_event_stream](#get_event_stream)
    - [get_export_job](#get_export_job)
    - [get_export_jobs](#get_export_jobs)
    - [get_gcm_channel](#get_gcm_channel)
    - [get_import_job](#get_import_job)
    - [get_import_jobs](#get_import_jobs)
    - [get_journey](#get_journey)
    - [get_journey_date_range_kpi](#get_journey_date_range_kpi)
    - [get_journey_execution_activity_metrics](#get_journey_execution_activity_metrics)
    - [get_journey_execution_metrics](#get_journey_execution_metrics)
    - [get_push_template](#get_push_template)
    - [get_recommender_configuration](#get_recommender_configuration)
    - [get_recommender_configurations](#get_recommender_configurations)
    - [get_segment](#get_segment)
    - [get_segment_export_jobs](#get_segment_export_jobs)
    - [get_segment_import_jobs](#get_segment_import_jobs)
    - [get_segment_version](#get_segment_version)
    - [get_segment_versions](#get_segment_versions)
    - [get_segments](#get_segments)
    - [get_sms_channel](#get_sms_channel)
    - [get_sms_template](#get_sms_template)
    - [get_user_endpoints](#get_user_endpoints)
    - [get_voice_channel](#get_voice_channel)
    - [get_voice_template](#get_voice_template)
    - [list_journeys](#list_journeys)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_template_versions](#list_template_versions)
    - [list_templates](#list_templates)
    - [phone_number_validate](#phone_number_validate)
    - [put_event_stream](#put_event_stream)
    - [put_events](#put_events)
    - [remove_attributes](#remove_attributes)
    - [send_messages](#send_messages)
    - [send_users_messages](#send_users_messages)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_adm_channel](#update_adm_channel)
    - [update_apns_channel](#update_apns_channel)
    - [update_apns_sandbox_channel](#update_apns_sandbox_channel)
    - [update_apns_voip_channel](#update_apns_voip_channel)
    - [update_apns_voip_sandbox_channel](#update_apns_voip_sandbox_channel)
    - [update_application_settings](#update_application_settings)
    - [update_baidu_channel](#update_baidu_channel)
    - [update_campaign](#update_campaign)
    - [update_email_channel](#update_email_channel)
    - [update_email_template](#update_email_template)
    - [update_endpoint](#update_endpoint)
    - [update_endpoints_batch](#update_endpoints_batch)
    - [update_gcm_channel](#update_gcm_channel)
    - [update_journey](#update_journey)
    - [update_journey_state](#update_journey_state)
    - [update_push_template](#update_push_template)
    - [update_recommender_configuration](#update_recommender_configuration)
    - [update_segment](#update_segment)
    - [update_sms_channel](#update_sms_channel)
    - [update_sms_template](#update_sms_template)
    - [update_template_active_version](#update_template_active_version)
    - [update_voice_channel](#update_voice_channel)
    - [update_voice_template](#update_voice_template)

## PinpointClient

Type annotations for `boto3.client("pinpoint")`

Can be used directly:

```python
from mypy_boto3_pinpoint.client import PinpointClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_pinpoint.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.MethodNotAllowedException`
- `Exceptions.NotFoundException`
- `Exceptions.PayloadTooLargeException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("pinpoint").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_app

Type annotations for `boto3.client("pinpoint").create_app` method.

[Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_app)

```python
def create_app(
    self,
    CreateApplicationRequest: CreateApplicationRequestTypeDef
) -> CreateAppResponseTypeDef:
    pass
```

### create_campaign

Type annotations for `boto3.client("pinpoint").create_campaign` method.

[Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_campaign)

```python
def create_campaign(
    self,
    ApplicationId: str,
    WriteCampaignRequest: WriteCampaignRequestTypeDef
) -> CreateCampaignResponseTypeDef:
    pass
```

### create_email_template

Type annotations for `boto3.client("pinpoint").create_email_template` method.

[Client.create_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_email_template)

```python
def create_email_template(
    self,
    EmailTemplateRequest: EmailTemplateRequestTypeDef,
    TemplateName: str
) -> CreateEmailTemplateResponseTypeDef:
    pass
```

### create_export_job

Type annotations for `boto3.client("pinpoint").create_export_job` method.

[Client.create_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_export_job)

```python
def create_export_job(
    self,
    ApplicationId: str,
    ExportJobRequest: ExportJobRequestTypeDef
) -> CreateExportJobResponseTypeDef:
    pass
```

### create_import_job

Type annotations for `boto3.client("pinpoint").create_import_job` method.

[Client.create_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_import_job)

```python
def create_import_job(
    self,
    ApplicationId: str,
    ImportJobRequest: ImportJobRequestTypeDef
) -> CreateImportJobResponseTypeDef:
    pass
```

### create_journey

Type annotations for `boto3.client("pinpoint").create_journey` method.

[Client.create_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_journey)

```python
def create_journey(
    self,
    ApplicationId: str,
    WriteJourneyRequest: WriteJourneyRequestTypeDef
) -> CreateJourneyResponseTypeDef:
    pass
```

### create_push_template

Type annotations for `boto3.client("pinpoint").create_push_template` method.

[Client.create_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_push_template)

```python
def create_push_template(
    self,
    PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef,
    TemplateName: str
) -> CreatePushTemplateResponseTypeDef:
    pass
```

### create_recommender_configuration

Type annotations for `boto3.client("pinpoint").create_recommender_configuration` method.

[Client.create_recommender_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_recommender_configuration)

```python
def create_recommender_configuration(
    self,
    CreateRecommenderConfiguration: CreateRecommenderConfigurationTypeDef
) -> CreateRecommenderConfigurationResponseTypeDef:
    pass
```

### create_segment

Type annotations for `boto3.client("pinpoint").create_segment` method.

[Client.create_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_segment)

```python
def create_segment(
    self,
    ApplicationId: str,
    WriteSegmentRequest: WriteSegmentRequestTypeDef
) -> CreateSegmentResponseTypeDef:
    pass
```

### create_sms_template

Type annotations for `boto3.client("pinpoint").create_sms_template` method.

[Client.create_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_sms_template)

```python
def create_sms_template(
    self,
    SMSTemplateRequest: SMSTemplateRequestTypeDef,
    TemplateName: str
) -> CreateSmsTemplateResponseTypeDef:
    pass
```

### create_voice_template

Type annotations for `boto3.client("pinpoint").create_voice_template` method.

[Client.create_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.create_voice_template)

```python
def create_voice_template(
    self,
    TemplateName: str,
    VoiceTemplateRequest: VoiceTemplateRequestTypeDef
) -> CreateVoiceTemplateResponseTypeDef:
    pass
```

### delete_adm_channel

Type annotations for `boto3.client("pinpoint").delete_adm_channel` method.

[Client.delete_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_adm_channel)

```python
def delete_adm_channel(
    self,
    ApplicationId: str
) -> DeleteAdmChannelResponseTypeDef:
    pass
```

### delete_apns_channel

Type annotations for `boto3.client("pinpoint").delete_apns_channel` method.

[Client.delete_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_channel)

```python
def delete_apns_channel(
    self,
    ApplicationId: str
) -> DeleteApnsChannelResponseTypeDef:
    pass
```

### delete_apns_sandbox_channel

Type annotations for `boto3.client("pinpoint").delete_apns_sandbox_channel` method.

[Client.delete_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_sandbox_channel)

```python
def delete_apns_sandbox_channel(
    self,
    ApplicationId: str
) -> DeleteApnsSandboxChannelResponseTypeDef:
    pass
```

### delete_apns_voip_channel

Type annotations for `boto3.client("pinpoint").delete_apns_voip_channel` method.

[Client.delete_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_channel)

```python
def delete_apns_voip_channel(
    self,
    ApplicationId: str
) -> DeleteApnsVoipChannelResponseTypeDef:
    pass
```

### delete_apns_voip_sandbox_channel

Type annotations for `boto3.client("pinpoint").delete_apns_voip_sandbox_channel` method.

[Client.delete_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_apns_voip_sandbox_channel)

```python
def delete_apns_voip_sandbox_channel(
    self,
    ApplicationId: str
) -> DeleteApnsVoipSandboxChannelResponseTypeDef:
    pass
```

### delete_app

Type annotations for `boto3.client("pinpoint").delete_app` method.

[Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_app)

```python
def delete_app(
    self,
    ApplicationId: str
) -> DeleteAppResponseTypeDef:
    pass
```

### delete_baidu_channel

Type annotations for `boto3.client("pinpoint").delete_baidu_channel` method.

[Client.delete_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_baidu_channel)

```python
def delete_baidu_channel(
    self,
    ApplicationId: str
) -> DeleteBaiduChannelResponseTypeDef:
    pass
```

### delete_campaign

Type annotations for `boto3.client("pinpoint").delete_campaign` method.

[Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_campaign)

```python
def delete_campaign(
    self,
    ApplicationId: str,
    CampaignId: str
) -> DeleteCampaignResponseTypeDef:
    pass
```

### delete_email_channel

Type annotations for `boto3.client("pinpoint").delete_email_channel` method.

[Client.delete_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_email_channel)

```python
def delete_email_channel(
    self,
    ApplicationId: str
) -> DeleteEmailChannelResponseTypeDef:
    pass
```

### delete_email_template

Type annotations for `boto3.client("pinpoint").delete_email_template` method.

[Client.delete_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_email_template)

```python
def delete_email_template(
    self,
    TemplateName: str,
    Version: str = None
) -> DeleteEmailTemplateResponseTypeDef:
    pass
```

### delete_endpoint

Type annotations for `boto3.client("pinpoint").delete_endpoint` method.

[Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_endpoint)

```python
def delete_endpoint(
    self,
    ApplicationId: str,
    EndpointId: str
) -> DeleteEndpointResponseTypeDef:
    pass
```

### delete_event_stream

Type annotations for `boto3.client("pinpoint").delete_event_stream` method.

[Client.delete_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_event_stream)

```python
def delete_event_stream(
    self,
    ApplicationId: str
) -> DeleteEventStreamResponseTypeDef:
    pass
```

### delete_gcm_channel

Type annotations for `boto3.client("pinpoint").delete_gcm_channel` method.

[Client.delete_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_gcm_channel)

```python
def delete_gcm_channel(
    self,
    ApplicationId: str
) -> DeleteGcmChannelResponseTypeDef:
    pass
```

### delete_journey

Type annotations for `boto3.client("pinpoint").delete_journey` method.

[Client.delete_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_journey)

```python
def delete_journey(
    self,
    ApplicationId: str,
    JourneyId: str
) -> DeleteJourneyResponseTypeDef:
    pass
```

### delete_push_template

Type annotations for `boto3.client("pinpoint").delete_push_template` method.

[Client.delete_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_push_template)

```python
def delete_push_template(
    self,
    TemplateName: str,
    Version: str = None
) -> DeletePushTemplateResponseTypeDef:
    pass
```

### delete_recommender_configuration

Type annotations for `boto3.client("pinpoint").delete_recommender_configuration` method.

[Client.delete_recommender_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_recommender_configuration)

```python
def delete_recommender_configuration(
    self,
    RecommenderId: str
) -> DeleteRecommenderConfigurationResponseTypeDef:
    pass
```

### delete_segment

Type annotations for `boto3.client("pinpoint").delete_segment` method.

[Client.delete_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_segment)

```python
def delete_segment(
    self,
    ApplicationId: str,
    SegmentId: str
) -> DeleteSegmentResponseTypeDef:
    pass
```

### delete_sms_channel

Type annotations for `boto3.client("pinpoint").delete_sms_channel` method.

[Client.delete_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_channel)

```python
def delete_sms_channel(
    self,
    ApplicationId: str
) -> DeleteSmsChannelResponseTypeDef:
    pass
```

### delete_sms_template

Type annotations for `boto3.client("pinpoint").delete_sms_template` method.

[Client.delete_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_sms_template)

```python
def delete_sms_template(
    self,
    TemplateName: str,
    Version: str = None
) -> DeleteSmsTemplateResponseTypeDef:
    pass
```

### delete_user_endpoints

Type annotations for `boto3.client("pinpoint").delete_user_endpoints` method.

[Client.delete_user_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_user_endpoints)

```python
def delete_user_endpoints(
    self,
    ApplicationId: str,
    UserId: str
) -> DeleteUserEndpointsResponseTypeDef:
    pass
```

### delete_voice_channel

Type annotations for `boto3.client("pinpoint").delete_voice_channel` method.

[Client.delete_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_channel)

```python
def delete_voice_channel(
    self,
    ApplicationId: str
) -> DeleteVoiceChannelResponseTypeDef:
    pass
```

### delete_voice_template

Type annotations for `boto3.client("pinpoint").delete_voice_template` method.

[Client.delete_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.delete_voice_template)

```python
def delete_voice_template(
    self,
    TemplateName: str,
    Version: str = None
) -> DeleteVoiceTemplateResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("pinpoint").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.generate_presigned_url)

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

### get_adm_channel

Type annotations for `boto3.client("pinpoint").get_adm_channel` method.

[Client.get_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_adm_channel)

```python
def get_adm_channel(
    self,
    ApplicationId: str
) -> GetAdmChannelResponseTypeDef:
    pass
```

### get_apns_channel

Type annotations for `boto3.client("pinpoint").get_apns_channel` method.

[Client.get_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_apns_channel)

```python
def get_apns_channel(
    self,
    ApplicationId: str
) -> GetApnsChannelResponseTypeDef:
    pass
```

### get_apns_sandbox_channel

Type annotations for `boto3.client("pinpoint").get_apns_sandbox_channel` method.

[Client.get_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_apns_sandbox_channel)

```python
def get_apns_sandbox_channel(
    self,
    ApplicationId: str
) -> GetApnsSandboxChannelResponseTypeDef:
    pass
```

### get_apns_voip_channel

Type annotations for `boto3.client("pinpoint").get_apns_voip_channel` method.

[Client.get_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_channel)

```python
def get_apns_voip_channel(
    self,
    ApplicationId: str
) -> GetApnsVoipChannelResponseTypeDef:
    pass
```

### get_apns_voip_sandbox_channel

Type annotations for `boto3.client("pinpoint").get_apns_voip_sandbox_channel` method.

[Client.get_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_apns_voip_sandbox_channel)

```python
def get_apns_voip_sandbox_channel(
    self,
    ApplicationId: str
) -> GetApnsVoipSandboxChannelResponseTypeDef:
    pass
```

### get_app

Type annotations for `boto3.client("pinpoint").get_app` method.

[Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_app)

```python
def get_app(
    self,
    ApplicationId: str
) -> GetAppResponseTypeDef:
    pass
```

### get_application_date_range_kpi

Type annotations for `boto3.client("pinpoint").get_application_date_range_kpi` method.

[Client.get_application_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_application_date_range_kpi)

```python
def get_application_date_range_kpi(
    self,
    ApplicationId: str,
    KpiName: str,
    EndTime: datetime = None,
    NextToken: str = None,
    PageSize: str = None,
    StartTime: datetime = None
) -> GetApplicationDateRangeKpiResponseTypeDef:
    pass
```

### get_application_settings

Type annotations for `boto3.client("pinpoint").get_application_settings` method.

[Client.get_application_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_application_settings)

```python
def get_application_settings(
    self,
    ApplicationId: str
) -> GetApplicationSettingsResponseTypeDef:
    pass
```

### get_apps

Type annotations for `boto3.client("pinpoint").get_apps` method.

[Client.get_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_apps)

```python
def get_apps(
    self,
    PageSize: str = None,
    Token: str = None
) -> GetAppsResponseTypeDef:
    pass
```

### get_baidu_channel

Type annotations for `boto3.client("pinpoint").get_baidu_channel` method.

[Client.get_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_baidu_channel)

```python
def get_baidu_channel(
    self,
    ApplicationId: str
) -> GetBaiduChannelResponseTypeDef:
    pass
```

### get_campaign

Type annotations for `boto3.client("pinpoint").get_campaign` method.

[Client.get_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaign)

```python
def get_campaign(
    self,
    ApplicationId: str,
    CampaignId: str
) -> GetCampaignResponseTypeDef:
    pass
```

### get_campaign_activities

Type annotations for `boto3.client("pinpoint").get_campaign_activities` method.

[Client.get_campaign_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_activities)

```python
def get_campaign_activities(
    self,
    ApplicationId: str,
    CampaignId: str,
    PageSize: str = None,
    Token: str = None
) -> GetCampaignActivitiesResponseTypeDef:
    pass
```

### get_campaign_date_range_kpi

Type annotations for `boto3.client("pinpoint").get_campaign_date_range_kpi` method.

[Client.get_campaign_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_date_range_kpi)

```python
def get_campaign_date_range_kpi(
    self,
    ApplicationId: str,
    CampaignId: str,
    KpiName: str,
    EndTime: datetime = None,
    NextToken: str = None,
    PageSize: str = None,
    StartTime: datetime = None
) -> GetCampaignDateRangeKpiResponseTypeDef:
    pass
```

### get_campaign_version

Type annotations for `boto3.client("pinpoint").get_campaign_version` method.

[Client.get_campaign_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_version)

```python
def get_campaign_version(
    self,
    ApplicationId: str,
    CampaignId: str,
    Version: str
) -> GetCampaignVersionResponseTypeDef:
    pass
```

### get_campaign_versions

Type annotations for `boto3.client("pinpoint").get_campaign_versions` method.

[Client.get_campaign_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaign_versions)

```python
def get_campaign_versions(
    self,
    ApplicationId: str,
    CampaignId: str,
    PageSize: str = None,
    Token: str = None
) -> GetCampaignVersionsResponseTypeDef:
    pass
```

### get_campaigns

Type annotations for `boto3.client("pinpoint").get_campaigns` method.

[Client.get_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_campaigns)

```python
def get_campaigns(
    self,
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None
) -> GetCampaignsResponseTypeDef:
    pass
```

### get_channels

Type annotations for `boto3.client("pinpoint").get_channels` method.

[Client.get_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_channels)

```python
def get_channels(
    self,
    ApplicationId: str
) -> GetChannelsResponseTypeDef:
    pass
```

### get_email_channel

Type annotations for `boto3.client("pinpoint").get_email_channel` method.

[Client.get_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_email_channel)

```python
def get_email_channel(
    self,
    ApplicationId: str
) -> GetEmailChannelResponseTypeDef:
    pass
```

### get_email_template

Type annotations for `boto3.client("pinpoint").get_email_template` method.

[Client.get_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_email_template)

```python
def get_email_template(
    self,
    TemplateName: str,
    Version: str = None
) -> GetEmailTemplateResponseTypeDef:
    pass
```

### get_endpoint

Type annotations for `boto3.client("pinpoint").get_endpoint` method.

[Client.get_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_endpoint)

```python
def get_endpoint(
    self,
    ApplicationId: str,
    EndpointId: str
) -> GetEndpointResponseTypeDef:
    pass
```

### get_event_stream

Type annotations for `boto3.client("pinpoint").get_event_stream` method.

[Client.get_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_event_stream)

```python
def get_event_stream(
    self,
    ApplicationId: str
) -> GetEventStreamResponseTypeDef:
    pass
```

### get_export_job

Type annotations for `boto3.client("pinpoint").get_export_job` method.

[Client.get_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_export_job)

```python
def get_export_job(
    self,
    ApplicationId: str,
    JobId: str
) -> GetExportJobResponseTypeDef:
    pass
```

### get_export_jobs

Type annotations for `boto3.client("pinpoint").get_export_jobs` method.

[Client.get_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_export_jobs)

```python
def get_export_jobs(
    self,
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None
) -> GetExportJobsResponseTypeDef:
    pass
```

### get_gcm_channel

Type annotations for `boto3.client("pinpoint").get_gcm_channel` method.

[Client.get_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_gcm_channel)

```python
def get_gcm_channel(
    self,
    ApplicationId: str
) -> GetGcmChannelResponseTypeDef:
    pass
```

### get_import_job

Type annotations for `boto3.client("pinpoint").get_import_job` method.

[Client.get_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_import_job)

```python
def get_import_job(
    self,
    ApplicationId: str,
    JobId: str
) -> GetImportJobResponseTypeDef:
    pass
```

### get_import_jobs

Type annotations for `boto3.client("pinpoint").get_import_jobs` method.

[Client.get_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_import_jobs)

```python
def get_import_jobs(
    self,
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None
) -> GetImportJobsResponseTypeDef:
    pass
```

### get_journey

Type annotations for `boto3.client("pinpoint").get_journey` method.

[Client.get_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_journey)

```python
def get_journey(
    self,
    ApplicationId: str,
    JourneyId: str
) -> GetJourneyResponseTypeDef:
    pass
```

### get_journey_date_range_kpi

Type annotations for `boto3.client("pinpoint").get_journey_date_range_kpi` method.

[Client.get_journey_date_range_kpi documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_journey_date_range_kpi)

```python
def get_journey_date_range_kpi(
    self,
    ApplicationId: str,
    JourneyId: str,
    KpiName: str,
    EndTime: datetime = None,
    NextToken: str = None,
    PageSize: str = None,
    StartTime: datetime = None
) -> GetJourneyDateRangeKpiResponseTypeDef:
    pass
```

### get_journey_execution_activity_metrics

Type annotations for `boto3.client("pinpoint").get_journey_execution_activity_metrics` method.

[Client.get_journey_execution_activity_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_activity_metrics)

```python
def get_journey_execution_activity_metrics(
    self,
    ApplicationId: str,
    JourneyActivityId: str,
    JourneyId: str,
    NextToken: str = None,
    PageSize: str = None
) -> GetJourneyExecutionActivityMetricsResponseTypeDef:
    pass
```

### get_journey_execution_metrics

Type annotations for `boto3.client("pinpoint").get_journey_execution_metrics` method.

[Client.get_journey_execution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_journey_execution_metrics)

```python
def get_journey_execution_metrics(
    self,
    ApplicationId: str,
    JourneyId: str,
    NextToken: str = None,
    PageSize: str = None
) -> GetJourneyExecutionMetricsResponseTypeDef:
    pass
```

### get_push_template

Type annotations for `boto3.client("pinpoint").get_push_template` method.

[Client.get_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_push_template)

```python
def get_push_template(
    self,
    TemplateName: str,
    Version: str = None
) -> GetPushTemplateResponseTypeDef:
    pass
```

### get_recommender_configuration

Type annotations for `boto3.client("pinpoint").get_recommender_configuration` method.

[Client.get_recommender_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_recommender_configuration)

```python
def get_recommender_configuration(
    self,
    RecommenderId: str
) -> GetRecommenderConfigurationResponseTypeDef:
    pass
```

### get_recommender_configurations

Type annotations for `boto3.client("pinpoint").get_recommender_configurations` method.

[Client.get_recommender_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_recommender_configurations)

```python
def get_recommender_configurations(
    self,
    PageSize: str = None,
    Token: str = None
) -> GetRecommenderConfigurationsResponseTypeDef:
    pass
```

### get_segment

Type annotations for `boto3.client("pinpoint").get_segment` method.

[Client.get_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment)

```python
def get_segment(
    self,
    ApplicationId: str,
    SegmentId: str
) -> GetSegmentResponseTypeDef:
    pass
```

### get_segment_export_jobs

Type annotations for `boto3.client("pinpoint").get_segment_export_jobs` method.

[Client.get_segment_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment_export_jobs)

```python
def get_segment_export_jobs(
    self,
    ApplicationId: str,
    SegmentId: str,
    PageSize: str = None,
    Token: str = None
) -> GetSegmentExportJobsResponseTypeDef:
    pass
```

### get_segment_import_jobs

Type annotations for `boto3.client("pinpoint").get_segment_import_jobs` method.

[Client.get_segment_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment_import_jobs)

```python
def get_segment_import_jobs(
    self,
    ApplicationId: str,
    SegmentId: str,
    PageSize: str = None,
    Token: str = None
) -> GetSegmentImportJobsResponseTypeDef:
    pass
```

### get_segment_version

Type annotations for `boto3.client("pinpoint").get_segment_version` method.

[Client.get_segment_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment_version)

```python
def get_segment_version(
    self,
    ApplicationId: str,
    SegmentId: str,
    Version: str
) -> GetSegmentVersionResponseTypeDef:
    pass
```

### get_segment_versions

Type annotations for `boto3.client("pinpoint").get_segment_versions` method.

[Client.get_segment_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segment_versions)

```python
def get_segment_versions(
    self,
    ApplicationId: str,
    SegmentId: str,
    PageSize: str = None,
    Token: str = None
) -> GetSegmentVersionsResponseTypeDef:
    pass
```

### get_segments

Type annotations for `boto3.client("pinpoint").get_segments` method.

[Client.get_segments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_segments)

```python
def get_segments(
    self,
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None
) -> GetSegmentsResponseTypeDef:
    pass
```

### get_sms_channel

Type annotations for `boto3.client("pinpoint").get_sms_channel` method.

[Client.get_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_sms_channel)

```python
def get_sms_channel(
    self,
    ApplicationId: str
) -> GetSmsChannelResponseTypeDef:
    pass
```

### get_sms_template

Type annotations for `boto3.client("pinpoint").get_sms_template` method.

[Client.get_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_sms_template)

```python
def get_sms_template(
    self,
    TemplateName: str,
    Version: str = None
) -> GetSmsTemplateResponseTypeDef:
    pass
```

### get_user_endpoints

Type annotations for `boto3.client("pinpoint").get_user_endpoints` method.

[Client.get_user_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_user_endpoints)

```python
def get_user_endpoints(
    self,
    ApplicationId: str,
    UserId: str
) -> GetUserEndpointsResponseTypeDef:
    pass
```

### get_voice_channel

Type annotations for `boto3.client("pinpoint").get_voice_channel` method.

[Client.get_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_voice_channel)

```python
def get_voice_channel(
    self,
    ApplicationId: str
) -> GetVoiceChannelResponseTypeDef:
    pass
```

### get_voice_template

Type annotations for `boto3.client("pinpoint").get_voice_template` method.

[Client.get_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.get_voice_template)

```python
def get_voice_template(
    self,
    TemplateName: str,
    Version: str = None
) -> GetVoiceTemplateResponseTypeDef:
    pass
```

### list_journeys

Type annotations for `boto3.client("pinpoint").list_journeys` method.

[Client.list_journeys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.list_journeys)

```python
def list_journeys(
    self,
    ApplicationId: str,
    PageSize: str = None,
    Token: str = None
) -> ListJourneysResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("pinpoint").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_template_versions

Type annotations for `boto3.client("pinpoint").list_template_versions` method.

[Client.list_template_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.list_template_versions)

```python
def list_template_versions(
    self,
    TemplateName: str,
    TemplateType: str,
    NextToken: str = None,
    PageSize: str = None
) -> ListTemplateVersionsResponseTypeDef:
    pass
```

### list_templates

Type annotations for `boto3.client("pinpoint").list_templates` method.

[Client.list_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.list_templates)

```python
def list_templates(
    self,
    NextToken: str = None,
    PageSize: str = None,
    Prefix: str = None,
    TemplateType: str = None
) -> ListTemplatesResponseTypeDef:
    pass
```

### phone_number_validate

Type annotations for `boto3.client("pinpoint").phone_number_validate` method.

[Client.phone_number_validate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.phone_number_validate)

```python
def phone_number_validate(
    self,
    NumberValidateRequest: NumberValidateRequestTypeDef
) -> PhoneNumberValidateResponseTypeDef:
    pass
```

### put_event_stream

Type annotations for `boto3.client("pinpoint").put_event_stream` method.

[Client.put_event_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.put_event_stream)

```python
def put_event_stream(
    self,
    ApplicationId: str,
    WriteEventStream: WriteEventStreamTypeDef
) -> PutEventStreamResponseTypeDef:
    pass
```

### put_events

Type annotations for `boto3.client("pinpoint").put_events` method.

[Client.put_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.put_events)

```python
def put_events(
    self,
    ApplicationId: str,
    EventsRequest: EventsRequestTypeDef
) -> PutEventsResponseTypeDef:
    pass
```

### remove_attributes

Type annotations for `boto3.client("pinpoint").remove_attributes` method.

[Client.remove_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.remove_attributes)

```python
def remove_attributes(
    self,
    ApplicationId: str,
    AttributeType: str,
    UpdateAttributesRequest: UpdateAttributesRequestTypeDef
) -> RemoveAttributesResponseTypeDef:
    pass
```

### send_messages

Type annotations for `boto3.client("pinpoint").send_messages` method.

[Client.send_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.send_messages)

```python
def send_messages(
    self,
    ApplicationId: str,
    MessageRequest: MessageRequestTypeDef
) -> SendMessagesResponseTypeDef:
    pass
```

### send_users_messages

Type annotations for `boto3.client("pinpoint").send_users_messages` method.

[Client.send_users_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.send_users_messages)

```python
def send_users_messages(
    self,
    ApplicationId: str,
    SendUsersMessageRequest: SendUsersMessageRequestTypeDef
) -> SendUsersMessagesResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("pinpoint").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    TagsModel: "TagsModelTypeDef"
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("pinpoint").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_adm_channel

Type annotations for `boto3.client("pinpoint").update_adm_channel` method.

[Client.update_adm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_adm_channel)

```python
def update_adm_channel(
    self,
    ADMChannelRequest: ADMChannelRequestTypeDef,
    ApplicationId: str
) -> UpdateAdmChannelResponseTypeDef:
    pass
```

### update_apns_channel

Type annotations for `boto3.client("pinpoint").update_apns_channel` method.

[Client.update_apns_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_apns_channel)

```python
def update_apns_channel(
    self,
    APNSChannelRequest: APNSChannelRequestTypeDef,
    ApplicationId: str
) -> UpdateApnsChannelResponseTypeDef:
    pass
```

### update_apns_sandbox_channel

Type annotations for `boto3.client("pinpoint").update_apns_sandbox_channel` method.

[Client.update_apns_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_apns_sandbox_channel)

```python
def update_apns_sandbox_channel(
    self,
    APNSSandboxChannelRequest: APNSSandboxChannelRequestTypeDef,
    ApplicationId: str
) -> UpdateApnsSandboxChannelResponseTypeDef:
    pass
```

### update_apns_voip_channel

Type annotations for `boto3.client("pinpoint").update_apns_voip_channel` method.

[Client.update_apns_voip_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_channel)

```python
def update_apns_voip_channel(
    self,
    APNSVoipChannelRequest: APNSVoipChannelRequestTypeDef,
    ApplicationId: str
) -> UpdateApnsVoipChannelResponseTypeDef:
    pass
```

### update_apns_voip_sandbox_channel

Type annotations for `boto3.client("pinpoint").update_apns_voip_sandbox_channel` method.

[Client.update_apns_voip_sandbox_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_apns_voip_sandbox_channel)

```python
def update_apns_voip_sandbox_channel(
    self,
    APNSVoipSandboxChannelRequest: APNSVoipSandboxChannelRequestTypeDef,
    ApplicationId: str
) -> UpdateApnsVoipSandboxChannelResponseTypeDef:
    pass
```

### update_application_settings

Type annotations for `boto3.client("pinpoint").update_application_settings` method.

[Client.update_application_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_application_settings)

```python
def update_application_settings(
    self,
    ApplicationId: str,
    WriteApplicationSettingsRequest: WriteApplicationSettingsRequestTypeDef
) -> UpdateApplicationSettingsResponseTypeDef:
    pass
```

### update_baidu_channel

Type annotations for `boto3.client("pinpoint").update_baidu_channel` method.

[Client.update_baidu_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_baidu_channel)

```python
def update_baidu_channel(
    self,
    ApplicationId: str,
    BaiduChannelRequest: BaiduChannelRequestTypeDef
) -> UpdateBaiduChannelResponseTypeDef:
    pass
```

### update_campaign

Type annotations for `boto3.client("pinpoint").update_campaign` method.

[Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_campaign)

```python
def update_campaign(
    self,
    ApplicationId: str,
    CampaignId: str,
    WriteCampaignRequest: WriteCampaignRequestTypeDef
) -> UpdateCampaignResponseTypeDef:
    pass
```

### update_email_channel

Type annotations for `boto3.client("pinpoint").update_email_channel` method.

[Client.update_email_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_email_channel)

```python
def update_email_channel(
    self,
    ApplicationId: str,
    EmailChannelRequest: EmailChannelRequestTypeDef
) -> UpdateEmailChannelResponseTypeDef:
    pass
```

### update_email_template

Type annotations for `boto3.client("pinpoint").update_email_template` method.

[Client.update_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_email_template)

```python
def update_email_template(
    self,
    EmailTemplateRequest: EmailTemplateRequestTypeDef,
    TemplateName: str,
    CreateNewVersion: bool = None,
    Version: str = None
) -> UpdateEmailTemplateResponseTypeDef:
    pass
```

### update_endpoint

Type annotations for `boto3.client("pinpoint").update_endpoint` method.

[Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_endpoint)

```python
def update_endpoint(
    self,
    ApplicationId: str,
    EndpointId: str,
    EndpointRequest: EndpointRequestTypeDef
) -> UpdateEndpointResponseTypeDef:
    pass
```

### update_endpoints_batch

Type annotations for `boto3.client("pinpoint").update_endpoints_batch` method.

[Client.update_endpoints_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_endpoints_batch)

```python
def update_endpoints_batch(
    self,
    ApplicationId: str,
    EndpointBatchRequest: EndpointBatchRequestTypeDef
) -> UpdateEndpointsBatchResponseTypeDef:
    pass
```

### update_gcm_channel

Type annotations for `boto3.client("pinpoint").update_gcm_channel` method.

[Client.update_gcm_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_gcm_channel)

```python
def update_gcm_channel(
    self,
    ApplicationId: str,
    GCMChannelRequest: GCMChannelRequestTypeDef
) -> UpdateGcmChannelResponseTypeDef:
    pass
```

### update_journey

Type annotations for `boto3.client("pinpoint").update_journey` method.

[Client.update_journey documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_journey)

```python
def update_journey(
    self,
    ApplicationId: str,
    JourneyId: str,
    WriteJourneyRequest: WriteJourneyRequestTypeDef
) -> UpdateJourneyResponseTypeDef:
    pass
```

### update_journey_state

Type annotations for `boto3.client("pinpoint").update_journey_state` method.

[Client.update_journey_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_journey_state)

```python
def update_journey_state(
    self,
    ApplicationId: str,
    JourneyId: str,
    JourneyStateRequest: JourneyStateRequestTypeDef
) -> UpdateJourneyStateResponseTypeDef:
    pass
```

### update_push_template

Type annotations for `boto3.client("pinpoint").update_push_template` method.

[Client.update_push_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_push_template)

```python
def update_push_template(
    self,
    PushNotificationTemplateRequest: PushNotificationTemplateRequestTypeDef,
    TemplateName: str,
    CreateNewVersion: bool = None,
    Version: str = None
) -> UpdatePushTemplateResponseTypeDef:
    pass
```

### update_recommender_configuration

Type annotations for `boto3.client("pinpoint").update_recommender_configuration` method.

[Client.update_recommender_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_recommender_configuration)

```python
def update_recommender_configuration(
    self,
    RecommenderId: str,
    UpdateRecommenderConfiguration: UpdateRecommenderConfigurationTypeDef
) -> UpdateRecommenderConfigurationResponseTypeDef:
    pass
```

### update_segment

Type annotations for `boto3.client("pinpoint").update_segment` method.

[Client.update_segment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_segment)

```python
def update_segment(
    self,
    ApplicationId: str,
    SegmentId: str,
    WriteSegmentRequest: WriteSegmentRequestTypeDef
) -> UpdateSegmentResponseTypeDef:
    pass
```

### update_sms_channel

Type annotations for `boto3.client("pinpoint").update_sms_channel` method.

[Client.update_sms_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_sms_channel)

```python
def update_sms_channel(
    self,
    ApplicationId: str,
    SMSChannelRequest: SMSChannelRequestTypeDef
) -> UpdateSmsChannelResponseTypeDef:
    pass
```

### update_sms_template

Type annotations for `boto3.client("pinpoint").update_sms_template` method.

[Client.update_sms_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_sms_template)

```python
def update_sms_template(
    self,
    SMSTemplateRequest: SMSTemplateRequestTypeDef,
    TemplateName: str,
    CreateNewVersion: bool = None,
    Version: str = None
) -> UpdateSmsTemplateResponseTypeDef:
    pass
```

### update_template_active_version

Type annotations for `boto3.client("pinpoint").update_template_active_version` method.

[Client.update_template_active_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_template_active_version)

```python
def update_template_active_version(
    self,
    TemplateActiveVersionRequest: TemplateActiveVersionRequestTypeDef,
    TemplateName: str,
    TemplateType: str
) -> UpdateTemplateActiveVersionResponseTypeDef:
    pass
```

### update_voice_channel

Type annotations for `boto3.client("pinpoint").update_voice_channel` method.

[Client.update_voice_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_voice_channel)

```python
def update_voice_channel(
    self,
    ApplicationId: str,
    VoiceChannelRequest: VoiceChannelRequestTypeDef
) -> UpdateVoiceChannelResponseTypeDef:
    pass
```

### update_voice_template

Type annotations for `boto3.client("pinpoint").update_voice_template` method.

[Client.update_voice_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint.Client.update_voice_template)

```python
def update_voice_template(
    self,
    TemplateName: str,
    VoiceTemplateRequest: VoiceTemplateRequestTypeDef,
    CreateNewVersion: bool = None,
    Version: str = None
) -> UpdateVoiceTemplateResponseTypeDef:
    pass
```