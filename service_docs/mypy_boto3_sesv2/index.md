# Type annotations for boto3 SESV2 module

> [Index](../index.md) > SESV2

Auto-generated documentation for [SESV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2)
type annotations stubs module [mypy_boto3_sesv2](https://pypi.org/project/mypy-boto3-sesv2/).

```bash
pip install mypy-boto3-sesv2
```

- [Type annotations for boto3 SESV2 module](#type-annotations-for-boto3-sesv2-module)
  - [SESV2Client](#sesv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## SESV2Client

Type annotations for  `boto3.client("sesv2")` as [SESV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_sesv2.client import SESV2Client
```


SESV2Client [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_configuration_set](./client.md#create-configuration-set)
- [create_configuration_set_event_destination](./client.md#create-configuration-set-event-destination)
- [create_contact](./client.md#create-contact)
- [create_contact_list](./client.md#create-contact-list)
- [create_custom_verification_email_template](./client.md#create-custom-verification-email-template)
- [create_dedicated_ip_pool](./client.md#create-dedicated-ip-pool)
- [create_deliverability_test_report](./client.md#create-deliverability-test-report)
- [create_email_identity](./client.md#create-email-identity)
- [create_email_identity_policy](./client.md#create-email-identity-policy)
- [create_email_template](./client.md#create-email-template)
- [create_import_job](./client.md#create-import-job)
- [delete_configuration_set](./client.md#delete-configuration-set)
- [delete_configuration_set_event_destination](./client.md#delete-configuration-set-event-destination)
- [delete_contact](./client.md#delete-contact)
- [delete_contact_list](./client.md#delete-contact-list)
- [delete_custom_verification_email_template](./client.md#delete-custom-verification-email-template)
- [delete_dedicated_ip_pool](./client.md#delete-dedicated-ip-pool)
- [delete_email_identity](./client.md#delete-email-identity)
- [delete_email_identity_policy](./client.md#delete-email-identity-policy)
- [delete_email_template](./client.md#delete-email-template)
- [delete_suppressed_destination](./client.md#delete-suppressed-destination)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account](./client.md#get-account)
- [get_blacklist_reports](./client.md#get-blacklist-reports)
- [get_configuration_set](./client.md#get-configuration-set)
- [get_configuration_set_event_destinations](./client.md#get-configuration-set-event-destinations)
- [get_contact](./client.md#get-contact)
- [get_contact_list](./client.md#get-contact-list)
- [get_custom_verification_email_template](./client.md#get-custom-verification-email-template)
- [get_dedicated_ip](./client.md#get-dedicated-ip)
- [get_dedicated_ips](./client.md#get-dedicated-ips)
- [get_deliverability_dashboard_options](./client.md#get-deliverability-dashboard-options)
- [get_deliverability_test_report](./client.md#get-deliverability-test-report)
- [get_domain_deliverability_campaign](./client.md#get-domain-deliverability-campaign)
- [get_domain_statistics_report](./client.md#get-domain-statistics-report)
- [get_email_identity](./client.md#get-email-identity)
- [get_email_identity_policies](./client.md#get-email-identity-policies)
- [get_email_template](./client.md#get-email-template)
- [get_import_job](./client.md#get-import-job)
- [get_suppressed_destination](./client.md#get-suppressed-destination)
- [list_configuration_sets](./client.md#list-configuration-sets)
- [list_contact_lists](./client.md#list-contact-lists)
- [list_contacts](./client.md#list-contacts)
- [list_custom_verification_email_templates](./client.md#list-custom-verification-email-templates)
- [list_dedicated_ip_pools](./client.md#list-dedicated-ip-pools)
- [list_deliverability_test_reports](./client.md#list-deliverability-test-reports)
- [list_domain_deliverability_campaigns](./client.md#list-domain-deliverability-campaigns)
- [list_email_identities](./client.md#list-email-identities)
- [list_email_templates](./client.md#list-email-templates)
- [list_import_jobs](./client.md#list-import-jobs)
- [list_suppressed_destinations](./client.md#list-suppressed-destinations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_account_dedicated_ip_warmup_attributes](./client.md#put-account-dedicated-ip-warmup-attributes)
- [put_account_details](./client.md#put-account-details)
- [put_account_sending_attributes](./client.md#put-account-sending-attributes)
- [put_account_suppression_attributes](./client.md#put-account-suppression-attributes)
- [put_configuration_set_delivery_options](./client.md#put-configuration-set-delivery-options)
- [put_configuration_set_reputation_options](./client.md#put-configuration-set-reputation-options)
- [put_configuration_set_sending_options](./client.md#put-configuration-set-sending-options)
- [put_configuration_set_suppression_options](./client.md#put-configuration-set-suppression-options)
- [put_configuration_set_tracking_options](./client.md#put-configuration-set-tracking-options)
- [put_dedicated_ip_in_pool](./client.md#put-dedicated-ip-in-pool)
- [put_dedicated_ip_warmup_attributes](./client.md#put-dedicated-ip-warmup-attributes)
- [put_deliverability_dashboard_option](./client.md#put-deliverability-dashboard-option)
- [put_email_identity_configuration_set_attributes](./client.md#put-email-identity-configuration-set-attributes)
- [put_email_identity_dkim_attributes](./client.md#put-email-identity-dkim-attributes)
- [put_email_identity_dkim_signing_attributes](./client.md#put-email-identity-dkim-signing-attributes)
- [put_email_identity_feedback_attributes](./client.md#put-email-identity-feedback-attributes)
- [put_email_identity_mail_from_attributes](./client.md#put-email-identity-mail-from-attributes)
- [put_suppressed_destination](./client.md#put-suppressed-destination)
- [send_bulk_email](./client.md#send-bulk-email)
- [send_custom_verification_email](./client.md#send-custom-verification-email)
- [send_email](./client.md#send-email)
- [tag_resource](./client.md#tag-resource)
- [test_render_email_template](./client.md#test-render-email-template)
- [untag_resource](./client.md#untag-resource)
- [update_configuration_set_event_destination](./client.md#update-configuration-set-event-destination)
- [update_contact](./client.md#update-contact)
- [update_contact_list](./client.md#update-contact-list)
- [update_custom_verification_email_template](./client.md#update-custom-verification-email-template)
- [update_email_identity_policy](./client.md#update-email-identity-policy)
- [update_email_template](./client.md#update-email-template)




### Exceptions
- [AccountSuspendedException](./client.md#accountsuspendedexception)
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConflictException](./client.md#conflictexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MailFromDomainNotVerifiedException](./client.md#mailfromdomainnotverifiedexception)
- [MessageRejected](./client.md#messagerejected)
- [NotFoundException](./client.md#notfoundexception)
- [SendingPausedException](./client.md#sendingpausedexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sesv2.literals import BehaviorOnMxFailure, ...
```

- [BehaviorOnMxFailure](./literals.md#behavioronmxfailure)
- [BulkEmailStatus](./literals.md#bulkemailstatus)
- [ContactLanguage](./literals.md#contactlanguage)
- [ContactListImportAction](./literals.md#contactlistimportaction)
- [DataFormat](./literals.md#dataformat)
- [DeliverabilityDashboardAccountStatus](./literals.md#deliverabilitydashboardaccountstatus)
- [DeliverabilityTestStatus](./literals.md#deliverabilityteststatus)
- [DimensionValueSource](./literals.md#dimensionvaluesource)
- [DkimSigningAttributesOrigin](./literals.md#dkimsigningattributesorigin)
- [DkimStatus](./literals.md#dkimstatus)
- [EventType](./literals.md#eventtype)
- [IdentityType](./literals.md#identitytype)
- [ImportDestinationType](./literals.md#importdestinationtype)
- [JobStatus](./literals.md#jobstatus)
- [MailFromDomainStatus](./literals.md#mailfromdomainstatus)
- [MailType](./literals.md#mailtype)
- [ReviewStatus](./literals.md#reviewstatus)
- [SubscriptionStatus](./literals.md#subscriptionstatus)
- [SuppressionListImportAction](./literals.md#suppressionlistimportaction)
- [SuppressionListReason](./literals.md#suppressionlistreason)
- [TlsPolicy](./literals.md#tlspolicy)
- [WarmupStatus](./literals.md#warmupstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sesv2.type_defs import AccountDetailsTypeDef, ...
```

- [AccountDetailsTypeDef](./type_defs.md#accountdetailstypedef)
- [BlacklistEntryTypeDef](./type_defs.md#blacklistentrytypedef)
- [BodyTypeDef](./type_defs.md#bodytypedef)
- [BulkEmailContentTypeDef](./type_defs.md#bulkemailcontenttypedef)
- [BulkEmailEntryResultTypeDef](./type_defs.md#bulkemailentryresulttypedef)
- [BulkEmailEntryTypeDef](./type_defs.md#bulkemailentrytypedef)
- [CloudWatchDestinationTypeDef](./type_defs.md#cloudwatchdestinationtypedef)
- [CloudWatchDimensionConfigurationTypeDef](./type_defs.md#cloudwatchdimensionconfigurationtypedef)
- [ContactListDestinationTypeDef](./type_defs.md#contactlistdestinationtypedef)
- [ContactListTypeDef](./type_defs.md#contactlisttypedef)
- [ContactTypeDef](./type_defs.md#contacttypedef)
- [ContentTypeDef](./type_defs.md#contenttypedef)
- [CreateDeliverabilityTestReportResponseTypeDef](./type_defs.md#createdeliverabilitytestreportresponsetypedef)
- [CreateEmailIdentityResponseTypeDef](./type_defs.md#createemailidentityresponsetypedef)
- [CreateImportJobResponseTypeDef](./type_defs.md#createimportjobresponsetypedef)
- [CustomVerificationEmailTemplateMetadataTypeDef](./type_defs.md#customverificationemailtemplatemetadatatypedef)
- [DailyVolumeTypeDef](./type_defs.md#dailyvolumetypedef)
- [DedicatedIpTypeDef](./type_defs.md#dedicatediptypedef)
- [DeliverabilityTestReportTypeDef](./type_defs.md#deliverabilitytestreporttypedef)
- [DeliveryOptionsTypeDef](./type_defs.md#deliveryoptionstypedef)
- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [DkimAttributesTypeDef](./type_defs.md#dkimattributestypedef)
- [DkimSigningAttributesTypeDef](./type_defs.md#dkimsigningattributestypedef)
- [DomainDeliverabilityCampaignTypeDef](./type_defs.md#domaindeliverabilitycampaigntypedef)
- [DomainDeliverabilityTrackingOptionTypeDef](./type_defs.md#domaindeliverabilitytrackingoptiontypedef)
- [DomainIspPlacementTypeDef](./type_defs.md#domainispplacementtypedef)
- [EmailContentTypeDef](./type_defs.md#emailcontenttypedef)
- [EmailTemplateContentTypeDef](./type_defs.md#emailtemplatecontenttypedef)
- [EmailTemplateMetadataTypeDef](./type_defs.md#emailtemplatemetadatatypedef)
- [EventDestinationDefinitionTypeDef](./type_defs.md#eventdestinationdefinitiontypedef)
- [EventDestinationTypeDef](./type_defs.md#eventdestinationtypedef)
- [FailureInfoTypeDef](./type_defs.md#failureinfotypedef)
- [GetAccountResponseTypeDef](./type_defs.md#getaccountresponsetypedef)
- [GetBlacklistReportsResponseTypeDef](./type_defs.md#getblacklistreportsresponsetypedef)
- [GetConfigurationSetEventDestinationsResponseTypeDef](./type_defs.md#getconfigurationseteventdestinationsresponsetypedef)
- [GetConfigurationSetResponseTypeDef](./type_defs.md#getconfigurationsetresponsetypedef)
- [GetContactListResponseTypeDef](./type_defs.md#getcontactlistresponsetypedef)
- [GetContactResponseTypeDef](./type_defs.md#getcontactresponsetypedef)
- [GetCustomVerificationEmailTemplateResponseTypeDef](./type_defs.md#getcustomverificationemailtemplateresponsetypedef)
- [GetDedicatedIpResponseTypeDef](./type_defs.md#getdedicatedipresponsetypedef)
- [GetDedicatedIpsResponseTypeDef](./type_defs.md#getdedicatedipsresponsetypedef)
- [GetDeliverabilityDashboardOptionsResponseTypeDef](./type_defs.md#getdeliverabilitydashboardoptionsresponsetypedef)
- [GetDeliverabilityTestReportResponseTypeDef](./type_defs.md#getdeliverabilitytestreportresponsetypedef)
- [GetDomainDeliverabilityCampaignResponseTypeDef](./type_defs.md#getdomaindeliverabilitycampaignresponsetypedef)
- [GetDomainStatisticsReportResponseTypeDef](./type_defs.md#getdomainstatisticsreportresponsetypedef)
- [GetEmailIdentityPoliciesResponseTypeDef](./type_defs.md#getemailidentitypoliciesresponsetypedef)
- [GetEmailIdentityResponseTypeDef](./type_defs.md#getemailidentityresponsetypedef)
- [GetEmailTemplateResponseTypeDef](./type_defs.md#getemailtemplateresponsetypedef)
- [GetImportJobResponseTypeDef](./type_defs.md#getimportjobresponsetypedef)
- [GetSuppressedDestinationResponseTypeDef](./type_defs.md#getsuppresseddestinationresponsetypedef)
- [IdentityInfoTypeDef](./type_defs.md#identityinfotypedef)
- [ImportDataSourceTypeDef](./type_defs.md#importdatasourcetypedef)
- [ImportDestinationTypeDef](./type_defs.md#importdestinationtypedef)
- [ImportJobSummaryTypeDef](./type_defs.md#importjobsummarytypedef)
- [InboxPlacementTrackingOptionTypeDef](./type_defs.md#inboxplacementtrackingoptiontypedef)
- [IspPlacementTypeDef](./type_defs.md#ispplacementtypedef)
- [KinesisFirehoseDestinationTypeDef](./type_defs.md#kinesisfirehosedestinationtypedef)
- [ListConfigurationSetsResponseTypeDef](./type_defs.md#listconfigurationsetsresponsetypedef)
- [ListContactListsResponseTypeDef](./type_defs.md#listcontactlistsresponsetypedef)
- [ListContactsFilterTypeDef](./type_defs.md#listcontactsfiltertypedef)
- [ListContactsResponseTypeDef](./type_defs.md#listcontactsresponsetypedef)
- [ListCustomVerificationEmailTemplatesResponseTypeDef](./type_defs.md#listcustomverificationemailtemplatesresponsetypedef)
- [ListDedicatedIpPoolsResponseTypeDef](./type_defs.md#listdedicatedippoolsresponsetypedef)
- [ListDeliverabilityTestReportsResponseTypeDef](./type_defs.md#listdeliverabilitytestreportsresponsetypedef)
- [ListDomainDeliverabilityCampaignsResponseTypeDef](./type_defs.md#listdomaindeliverabilitycampaignsresponsetypedef)
- [ListEmailIdentitiesResponseTypeDef](./type_defs.md#listemailidentitiesresponsetypedef)
- [ListEmailTemplatesResponseTypeDef](./type_defs.md#listemailtemplatesresponsetypedef)
- [ListImportJobsResponseTypeDef](./type_defs.md#listimportjobsresponsetypedef)
- [ListManagementOptionsTypeDef](./type_defs.md#listmanagementoptionstypedef)
- [ListSuppressedDestinationsResponseTypeDef](./type_defs.md#listsuppresseddestinationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MailFromAttributesTypeDef](./type_defs.md#mailfromattributestypedef)
- [MessageTagTypeDef](./type_defs.md#messagetagtypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [OverallVolumeTypeDef](./type_defs.md#overallvolumetypedef)
- [PinpointDestinationTypeDef](./type_defs.md#pinpointdestinationtypedef)
- [PlacementStatisticsTypeDef](./type_defs.md#placementstatisticstypedef)
- [PutEmailIdentityDkimSigningAttributesResponseTypeDef](./type_defs.md#putemailidentitydkimsigningattributesresponsetypedef)
- [RawMessageTypeDef](./type_defs.md#rawmessagetypedef)
- [ReplacementEmailContentTypeDef](./type_defs.md#replacementemailcontenttypedef)
- [ReplacementTemplateTypeDef](./type_defs.md#replacementtemplatetypedef)
- [ReputationOptionsTypeDef](./type_defs.md#reputationoptionstypedef)
- [ReviewDetailsTypeDef](./type_defs.md#reviewdetailstypedef)
- [SendBulkEmailResponseTypeDef](./type_defs.md#sendbulkemailresponsetypedef)
- [SendCustomVerificationEmailResponseTypeDef](./type_defs.md#sendcustomverificationemailresponsetypedef)
- [SendEmailResponseTypeDef](./type_defs.md#sendemailresponsetypedef)
- [SendQuotaTypeDef](./type_defs.md#sendquotatypedef)
- [SendingOptionsTypeDef](./type_defs.md#sendingoptionstypedef)
- [SnsDestinationTypeDef](./type_defs.md#snsdestinationtypedef)
- [SuppressedDestinationAttributesTypeDef](./type_defs.md#suppresseddestinationattributestypedef)
- [SuppressedDestinationSummaryTypeDef](./type_defs.md#suppresseddestinationsummarytypedef)
- [SuppressedDestinationTypeDef](./type_defs.md#suppresseddestinationtypedef)
- [SuppressionAttributesTypeDef](./type_defs.md#suppressionattributestypedef)
- [SuppressionListDestinationTypeDef](./type_defs.md#suppressionlistdestinationtypedef)
- [SuppressionOptionsTypeDef](./type_defs.md#suppressionoptionstypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TemplateTypeDef](./type_defs.md#templatetypedef)
- [TestRenderEmailTemplateResponseTypeDef](./type_defs.md#testrenderemailtemplateresponsetypedef)
- [TopicFilterTypeDef](./type_defs.md#topicfiltertypedef)
- [TopicPreferenceTypeDef](./type_defs.md#topicpreferencetypedef)
- [TopicTypeDef](./type_defs.md#topictypedef)
- [TrackingOptionsTypeDef](./type_defs.md#trackingoptionstypedef)
- [VolumeStatisticsTypeDef](./type_defs.md#volumestatisticstypedef)
