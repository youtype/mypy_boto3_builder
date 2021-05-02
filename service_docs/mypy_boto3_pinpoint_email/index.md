# Type annotations for boto3 PinpointEmail module

> [Index](../index.md) > PinpointEmail

Auto-generated documentation for [PinpointEmail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail)
type annotations stubs module [mypy_boto3_pinpoint_email](https://pypi.org/project/mypy-boto3-pinpoint-email/).

```bash
pip install mypy-boto3-pinpoint-email
```

- [Type annotations for boto3 PinpointEmail module](#type-annotations-for-boto3-pinpointemail-module)
  - [PinpointEmailClient](#pinpointemailclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## PinpointEmailClient

Type annotations for  `boto3.client("pinpoint-email")` as [PinpointEmailClient](./client.md)

Can be used directly:

```python
from mypy_boto3_pinpoint_email.client import PinpointEmailClient
```


PinpointEmailClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_configuration_set](./client.md#create-configuration-set)
- [create_configuration_set_event_destination](./client.md#create-configuration-set-event-destination)
- [create_dedicated_ip_pool](./client.md#create-dedicated-ip-pool)
- [create_deliverability_test_report](./client.md#create-deliverability-test-report)
- [create_email_identity](./client.md#create-email-identity)
- [delete_configuration_set](./client.md#delete-configuration-set)
- [delete_configuration_set_event_destination](./client.md#delete-configuration-set-event-destination)
- [delete_dedicated_ip_pool](./client.md#delete-dedicated-ip-pool)
- [delete_email_identity](./client.md#delete-email-identity)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account](./client.md#get-account)
- [get_blacklist_reports](./client.md#get-blacklist-reports)
- [get_configuration_set](./client.md#get-configuration-set)
- [get_configuration_set_event_destinations](./client.md#get-configuration-set-event-destinations)
- [get_dedicated_ip](./client.md#get-dedicated-ip)
- [get_dedicated_ips](./client.md#get-dedicated-ips)
- [get_deliverability_dashboard_options](./client.md#get-deliverability-dashboard-options)
- [get_deliverability_test_report](./client.md#get-deliverability-test-report)
- [get_domain_deliverability_campaign](./client.md#get-domain-deliverability-campaign)
- [get_domain_statistics_report](./client.md#get-domain-statistics-report)
- [get_email_identity](./client.md#get-email-identity)
- [get_paginator](./client.md#get-paginator)
- [list_configuration_sets](./client.md#list-configuration-sets)
- [list_dedicated_ip_pools](./client.md#list-dedicated-ip-pools)
- [list_deliverability_test_reports](./client.md#list-deliverability-test-reports)
- [list_domain_deliverability_campaigns](./client.md#list-domain-deliverability-campaigns)
- [list_email_identities](./client.md#list-email-identities)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_account_dedicated_ip_warmup_attributes](./client.md#put-account-dedicated-ip-warmup-attributes)
- [put_account_sending_attributes](./client.md#put-account-sending-attributes)
- [put_configuration_set_delivery_options](./client.md#put-configuration-set-delivery-options)
- [put_configuration_set_reputation_options](./client.md#put-configuration-set-reputation-options)
- [put_configuration_set_sending_options](./client.md#put-configuration-set-sending-options)
- [put_configuration_set_tracking_options](./client.md#put-configuration-set-tracking-options)
- [put_dedicated_ip_in_pool](./client.md#put-dedicated-ip-in-pool)
- [put_dedicated_ip_warmup_attributes](./client.md#put-dedicated-ip-warmup-attributes)
- [put_deliverability_dashboard_option](./client.md#put-deliverability-dashboard-option)
- [put_email_identity_dkim_attributes](./client.md#put-email-identity-dkim-attributes)
- [put_email_identity_feedback_attributes](./client.md#put-email-identity-feedback-attributes)
- [put_email_identity_mail_from_attributes](./client.md#put-email-identity-mail-from-attributes)
- [send_email](./client.md#send-email)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_configuration_set_event_destination](./client.md#update-configuration-set-event-destination)




### Exceptions
- [AccountSuspendedException](./client.md#accountsuspendedexception)
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MailFromDomainNotVerifiedException](./client.md#mailfromdomainnotverifiedexception)
- [MessageRejected](./client.md#messagerejected)
- [NotFoundException](./client.md#notfoundexception)
- [SendingPausedException](./client.md#sendingpausedexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("pinpoint-email").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.paginators import GetDedicatedIpsPaginator, ...
```

- [GetDedicatedIpsPaginator](./paginators.md#getdedicatedipspaginator)
- [ListConfigurationSetsPaginator](./paginators.md#listconfigurationsetspaginator)
- [ListDedicatedIpPoolsPaginator](./paginators.md#listdedicatedippoolspaginator)
- [ListDeliverabilityTestReportsPaginator](./paginators.md#listdeliverabilitytestreportspaginator)
- [ListEmailIdentitiesPaginator](./paginators.md#listemailidentitiespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.literals import BehaviorOnMxFailure, ...
```

- [BehaviorOnMxFailure](./literals.md#behavioronmxfailure)
- [DeliverabilityDashboardAccountStatus](./literals.md#deliverabilitydashboardaccountstatus)
- [DeliverabilityTestStatus](./literals.md#deliverabilityteststatus)
- [DimensionValueSource](./literals.md#dimensionvaluesource)
- [DkimStatus](./literals.md#dkimstatus)
- [EventType](./literals.md#eventtype)
- [GetDedicatedIpsPaginatorName](./literals.md#getdedicatedipspaginatorname)
- [IdentityType](./literals.md#identitytype)
- [ListConfigurationSetsPaginatorName](./literals.md#listconfigurationsetspaginatorname)
- [ListDedicatedIpPoolsPaginatorName](./literals.md#listdedicatedippoolspaginatorname)
- [ListDeliverabilityTestReportsPaginatorName](./literals.md#listdeliverabilitytestreportspaginatorname)
- [ListEmailIdentitiesPaginatorName](./literals.md#listemailidentitiespaginatorname)
- [MailFromDomainStatus](./literals.md#mailfromdomainstatus)
- [TlsPolicy](./literals.md#tlspolicy)
- [WarmupStatus](./literals.md#warmupstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef, ...
```

- [BlacklistEntryTypeDef](./type_defs.md#blacklistentrytypedef)
- [BodyTypeDef](./type_defs.md#bodytypedef)
- [CloudWatchDestinationTypeDef](./type_defs.md#cloudwatchdestinationtypedef)
- [CloudWatchDimensionConfigurationTypeDef](./type_defs.md#cloudwatchdimensionconfigurationtypedef)
- [ContentTypeDef](./type_defs.md#contenttypedef)
- [CreateDeliverabilityTestReportResponseTypeDef](./type_defs.md#createdeliverabilitytestreportresponsetypedef)
- [CreateEmailIdentityResponseTypeDef](./type_defs.md#createemailidentityresponsetypedef)
- [DailyVolumeTypeDef](./type_defs.md#dailyvolumetypedef)
- [DedicatedIpTypeDef](./type_defs.md#dedicatediptypedef)
- [DeliverabilityTestReportTypeDef](./type_defs.md#deliverabilitytestreporttypedef)
- [DeliveryOptionsTypeDef](./type_defs.md#deliveryoptionstypedef)
- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [DkimAttributesTypeDef](./type_defs.md#dkimattributestypedef)
- [DomainDeliverabilityCampaignTypeDef](./type_defs.md#domaindeliverabilitycampaigntypedef)
- [DomainDeliverabilityTrackingOptionTypeDef](./type_defs.md#domaindeliverabilitytrackingoptiontypedef)
- [DomainIspPlacementTypeDef](./type_defs.md#domainispplacementtypedef)
- [EmailContentTypeDef](./type_defs.md#emailcontenttypedef)
- [EventDestinationDefinitionTypeDef](./type_defs.md#eventdestinationdefinitiontypedef)
- [EventDestinationTypeDef](./type_defs.md#eventdestinationtypedef)
- [GetAccountResponseTypeDef](./type_defs.md#getaccountresponsetypedef)
- [GetBlacklistReportsResponseTypeDef](./type_defs.md#getblacklistreportsresponsetypedef)
- [GetConfigurationSetEventDestinationsResponseTypeDef](./type_defs.md#getconfigurationseteventdestinationsresponsetypedef)
- [GetConfigurationSetResponseTypeDef](./type_defs.md#getconfigurationsetresponsetypedef)
- [GetDedicatedIpResponseTypeDef](./type_defs.md#getdedicatedipresponsetypedef)
- [GetDedicatedIpsResponseTypeDef](./type_defs.md#getdedicatedipsresponsetypedef)
- [GetDeliverabilityDashboardOptionsResponseTypeDef](./type_defs.md#getdeliverabilitydashboardoptionsresponsetypedef)
- [GetDeliverabilityTestReportResponseTypeDef](./type_defs.md#getdeliverabilitytestreportresponsetypedef)
- [GetDomainDeliverabilityCampaignResponseTypeDef](./type_defs.md#getdomaindeliverabilitycampaignresponsetypedef)
- [GetDomainStatisticsReportResponseTypeDef](./type_defs.md#getdomainstatisticsreportresponsetypedef)
- [GetEmailIdentityResponseTypeDef](./type_defs.md#getemailidentityresponsetypedef)
- [IdentityInfoTypeDef](./type_defs.md#identityinfotypedef)
- [InboxPlacementTrackingOptionTypeDef](./type_defs.md#inboxplacementtrackingoptiontypedef)
- [IspPlacementTypeDef](./type_defs.md#ispplacementtypedef)
- [KinesisFirehoseDestinationTypeDef](./type_defs.md#kinesisfirehosedestinationtypedef)
- [ListConfigurationSetsResponseTypeDef](./type_defs.md#listconfigurationsetsresponsetypedef)
- [ListDedicatedIpPoolsResponseTypeDef](./type_defs.md#listdedicatedippoolsresponsetypedef)
- [ListDeliverabilityTestReportsResponseTypeDef](./type_defs.md#listdeliverabilitytestreportsresponsetypedef)
- [ListDomainDeliverabilityCampaignsResponseTypeDef](./type_defs.md#listdomaindeliverabilitycampaignsresponsetypedef)
- [ListEmailIdentitiesResponseTypeDef](./type_defs.md#listemailidentitiesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MailFromAttributesTypeDef](./type_defs.md#mailfromattributestypedef)
- [MessageTagTypeDef](./type_defs.md#messagetagtypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [OverallVolumeTypeDef](./type_defs.md#overallvolumetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PinpointDestinationTypeDef](./type_defs.md#pinpointdestinationtypedef)
- [PlacementStatisticsTypeDef](./type_defs.md#placementstatisticstypedef)
- [RawMessageTypeDef](./type_defs.md#rawmessagetypedef)
- [ReputationOptionsTypeDef](./type_defs.md#reputationoptionstypedef)
- [SendEmailResponseTypeDef](./type_defs.md#sendemailresponsetypedef)
- [SendQuotaTypeDef](./type_defs.md#sendquotatypedef)
- [SendingOptionsTypeDef](./type_defs.md#sendingoptionstypedef)
- [SnsDestinationTypeDef](./type_defs.md#snsdestinationtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TemplateTypeDef](./type_defs.md#templatetypedef)
- [TrackingOptionsTypeDef](./type_defs.md#trackingoptionstypedef)
- [VolumeStatisticsTypeDef](./type_defs.md#volumestatisticstypedef)
