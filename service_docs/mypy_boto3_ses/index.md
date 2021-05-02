# Type annotations for boto3 SES module

> [Index](../index.md) > SES

Auto-generated documentation for [SES](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES)
type annotations stubs module [mypy_boto3_ses](https://pypi.org/project/mypy-boto3-ses/).

```bash
pip install mypy-boto3-ses
```

- [Type annotations for boto3 SES module](#type-annotations-for-boto3-ses-module)
  - [SESClient](#sesclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## SESClient

Type annotations for  `boto3.client("ses")` as [SESClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ses.client import SESClient
```


SESClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [clone_receipt_rule_set](./client.md#clone-receipt-rule-set)
- [create_configuration_set](./client.md#create-configuration-set)
- [create_configuration_set_event_destination](./client.md#create-configuration-set-event-destination)
- [create_configuration_set_tracking_options](./client.md#create-configuration-set-tracking-options)
- [create_custom_verification_email_template](./client.md#create-custom-verification-email-template)
- [create_receipt_filter](./client.md#create-receipt-filter)
- [create_receipt_rule](./client.md#create-receipt-rule)
- [create_receipt_rule_set](./client.md#create-receipt-rule-set)
- [create_template](./client.md#create-template)
- [delete_configuration_set](./client.md#delete-configuration-set)
- [delete_configuration_set_event_destination](./client.md#delete-configuration-set-event-destination)
- [delete_configuration_set_tracking_options](./client.md#delete-configuration-set-tracking-options)
- [delete_custom_verification_email_template](./client.md#delete-custom-verification-email-template)
- [delete_identity](./client.md#delete-identity)
- [delete_identity_policy](./client.md#delete-identity-policy)
- [delete_receipt_filter](./client.md#delete-receipt-filter)
- [delete_receipt_rule](./client.md#delete-receipt-rule)
- [delete_receipt_rule_set](./client.md#delete-receipt-rule-set)
- [delete_template](./client.md#delete-template)
- [delete_verified_email_address](./client.md#delete-verified-email-address)
- [describe_active_receipt_rule_set](./client.md#describe-active-receipt-rule-set)
- [describe_configuration_set](./client.md#describe-configuration-set)
- [describe_receipt_rule](./client.md#describe-receipt-rule)
- [describe_receipt_rule_set](./client.md#describe-receipt-rule-set)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account_sending_enabled](./client.md#get-account-sending-enabled)
- [get_custom_verification_email_template](./client.md#get-custom-verification-email-template)
- [get_identity_dkim_attributes](./client.md#get-identity-dkim-attributes)
- [get_identity_mail_from_domain_attributes](./client.md#get-identity-mail-from-domain-attributes)
- [get_identity_notification_attributes](./client.md#get-identity-notification-attributes)
- [get_identity_policies](./client.md#get-identity-policies)
- [get_identity_verification_attributes](./client.md#get-identity-verification-attributes)
- [get_paginator](./client.md#get-paginator)
- [get_send_quota](./client.md#get-send-quota)
- [get_send_statistics](./client.md#get-send-statistics)
- [get_template](./client.md#get-template)
- [get_waiter](./client.md#get-waiter)
- [list_configuration_sets](./client.md#list-configuration-sets)
- [list_custom_verification_email_templates](./client.md#list-custom-verification-email-templates)
- [list_identities](./client.md#list-identities)
- [list_identity_policies](./client.md#list-identity-policies)
- [list_receipt_filters](./client.md#list-receipt-filters)
- [list_receipt_rule_sets](./client.md#list-receipt-rule-sets)
- [list_templates](./client.md#list-templates)
- [list_verified_email_addresses](./client.md#list-verified-email-addresses)
- [put_configuration_set_delivery_options](./client.md#put-configuration-set-delivery-options)
- [put_identity_policy](./client.md#put-identity-policy)
- [reorder_receipt_rule_set](./client.md#reorder-receipt-rule-set)
- [send_bounce](./client.md#send-bounce)
- [send_bulk_templated_email](./client.md#send-bulk-templated-email)
- [send_custom_verification_email](./client.md#send-custom-verification-email)
- [send_email](./client.md#send-email)
- [send_raw_email](./client.md#send-raw-email)
- [send_templated_email](./client.md#send-templated-email)
- [set_active_receipt_rule_set](./client.md#set-active-receipt-rule-set)
- [set_identity_dkim_enabled](./client.md#set-identity-dkim-enabled)
- [set_identity_feedback_forwarding_enabled](./client.md#set-identity-feedback-forwarding-enabled)
- [set_identity_headers_in_notifications_enabled](./client.md#set-identity-headers-in-notifications-enabled)
- [set_identity_mail_from_domain](./client.md#set-identity-mail-from-domain)
- [set_identity_notification_topic](./client.md#set-identity-notification-topic)
- [set_receipt_rule_position](./client.md#set-receipt-rule-position)
- [test_render_template](./client.md#test-render-template)
- [update_account_sending_enabled](./client.md#update-account-sending-enabled)
- [update_configuration_set_event_destination](./client.md#update-configuration-set-event-destination)
- [update_configuration_set_reputation_metrics_enabled](./client.md#update-configuration-set-reputation-metrics-enabled)
- [update_configuration_set_sending_enabled](./client.md#update-configuration-set-sending-enabled)
- [update_configuration_set_tracking_options](./client.md#update-configuration-set-tracking-options)
- [update_custom_verification_email_template](./client.md#update-custom-verification-email-template)
- [update_receipt_rule](./client.md#update-receipt-rule)
- [update_template](./client.md#update-template)
- [verify_domain_dkim](./client.md#verify-domain-dkim)
- [verify_domain_identity](./client.md#verify-domain-identity)
- [verify_email_address](./client.md#verify-email-address)
- [verify_email_identity](./client.md#verify-email-identity)




### Exceptions
- [AccountSendingPausedException](./client.md#accountsendingpausedexception)
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [CannotDeleteException](./client.md#cannotdeleteexception)
- [ClientError](./client.md#clienterror)
- [ConfigurationSetAlreadyExistsException](./client.md#configurationsetalreadyexistsexception)
- [ConfigurationSetDoesNotExistException](./client.md#configurationsetdoesnotexistexception)
- [ConfigurationSetSendingPausedException](./client.md#configurationsetsendingpausedexception)
- [CustomVerificationEmailInvalidContentException](./client.md#customverificationemailinvalidcontentexception)
- [CustomVerificationEmailTemplateAlreadyExistsException](./client.md#customverificationemailtemplatealreadyexistsexception)
- [CustomVerificationEmailTemplateDoesNotExistException](./client.md#customverificationemailtemplatedoesnotexistexception)
- [EventDestinationAlreadyExistsException](./client.md#eventdestinationalreadyexistsexception)
- [EventDestinationDoesNotExistException](./client.md#eventdestinationdoesnotexistexception)
- [FromEmailAddressNotVerifiedException](./client.md#fromemailaddressnotverifiedexception)
- [InvalidCloudWatchDestinationException](./client.md#invalidcloudwatchdestinationexception)
- [InvalidConfigurationSetException](./client.md#invalidconfigurationsetexception)
- [InvalidDeliveryOptionsException](./client.md#invaliddeliveryoptionsexception)
- [InvalidFirehoseDestinationException](./client.md#invalidfirehosedestinationexception)
- [InvalidLambdaFunctionException](./client.md#invalidlambdafunctionexception)
- [InvalidPolicyException](./client.md#invalidpolicyexception)
- [InvalidRenderingParameterException](./client.md#invalidrenderingparameterexception)
- [InvalidS3ConfigurationException](./client.md#invalids3configurationexception)
- [InvalidSNSDestinationException](./client.md#invalidsnsdestinationexception)
- [InvalidSnsTopicException](./client.md#invalidsnstopicexception)
- [InvalidTemplateException](./client.md#invalidtemplateexception)
- [InvalidTrackingOptionsException](./client.md#invalidtrackingoptionsexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MailFromDomainNotVerifiedException](./client.md#mailfromdomainnotverifiedexception)
- [MessageRejected](./client.md#messagerejected)
- [MissingRenderingAttributeException](./client.md#missingrenderingattributeexception)
- [ProductionAccessNotGrantedException](./client.md#productionaccessnotgrantedexception)
- [RuleDoesNotExistException](./client.md#ruledoesnotexistexception)
- [RuleSetDoesNotExistException](./client.md#rulesetdoesnotexistexception)
- [TemplateDoesNotExistException](./client.md#templatedoesnotexistexception)
- [TrackingOptionsAlreadyExistsException](./client.md#trackingoptionsalreadyexistsexception)
- [TrackingOptionsDoesNotExistException](./client.md#trackingoptionsdoesnotexistexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("ses").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_ses.paginators import ListConfigurationSetsPaginator, ...
```

- [ListConfigurationSetsPaginator](./paginators.md#listconfigurationsetspaginator)
- [ListCustomVerificationEmailTemplatesPaginator](./paginators.md#listcustomverificationemailtemplatespaginator)
- [ListIdentitiesPaginator](./paginators.md#listidentitiespaginator)
- [ListReceiptRuleSetsPaginator](./paginators.md#listreceiptrulesetspaginator)
- [ListTemplatesPaginator](./paginators.md#listtemplatespaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("ses").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_ses.waiters import IdentityExistsWaiter, ...
```

- [IdentityExistsWaiter](./waiters.md#identityexistswaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ses.literals import BehaviorOnMXFailure, ...
```

- [BehaviorOnMXFailure](./literals.md#behavioronmxfailure)
- [BounceType](./literals.md#bouncetype)
- [BulkEmailStatus](./literals.md#bulkemailstatus)
- [ConfigurationSetAttribute](./literals.md#configurationsetattribute)
- [CustomMailFromStatus](./literals.md#custommailfromstatus)
- [DimensionValueSource](./literals.md#dimensionvaluesource)
- [DsnAction](./literals.md#dsnaction)
- [EventType](./literals.md#eventtype)
- [IdentityExistsWaiterName](./literals.md#identityexistswaitername)
- [IdentityType](./literals.md#identitytype)
- [InvocationType](./literals.md#invocationtype)
- [ListConfigurationSetsPaginatorName](./literals.md#listconfigurationsetspaginatorname)
- [ListCustomVerificationEmailTemplatesPaginatorName](./literals.md#listcustomverificationemailtemplatespaginatorname)
- [ListIdentitiesPaginatorName](./literals.md#listidentitiespaginatorname)
- [ListReceiptRuleSetsPaginatorName](./literals.md#listreceiptrulesetspaginatorname)
- [ListTemplatesPaginatorName](./literals.md#listtemplatespaginatorname)
- [NotificationType](./literals.md#notificationtype)
- [ReceiptFilterPolicy](./literals.md#receiptfilterpolicy)
- [SNSActionEncoding](./literals.md#snsactionencoding)
- [StopScope](./literals.md#stopscope)
- [TlsPolicy](./literals.md#tlspolicy)
- [VerificationStatus](./literals.md#verificationstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef, ...
```

- [AddHeaderActionTypeDef](./type_defs.md#addheaderactiontypedef)
- [BodyTypeDef](./type_defs.md#bodytypedef)
- [BounceActionTypeDef](./type_defs.md#bounceactiontypedef)
- [BulkEmailDestinationStatusTypeDef](./type_defs.md#bulkemaildestinationstatustypedef)
- [CloudWatchDestinationTypeDef](./type_defs.md#cloudwatchdestinationtypedef)
- [CloudWatchDimensionConfigurationTypeDef](./type_defs.md#cloudwatchdimensionconfigurationtypedef)
- [ConfigurationSetTypeDef](./type_defs.md#configurationsettypedef)
- [ContentTypeDef](./type_defs.md#contenttypedef)
- [CustomVerificationEmailTemplateTypeDef](./type_defs.md#customverificationemailtemplatetypedef)
- [DeliveryOptionsTypeDef](./type_defs.md#deliveryoptionstypedef)
- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [EventDestinationTypeDef](./type_defs.md#eventdestinationtypedef)
- [ExtensionFieldTypeDef](./type_defs.md#extensionfieldtypedef)
- [IdentityDkimAttributesTypeDef](./type_defs.md#identitydkimattributestypedef)
- [IdentityMailFromDomainAttributesTypeDef](./type_defs.md#identitymailfromdomainattributestypedef)
- [IdentityNotificationAttributesTypeDef](./type_defs.md#identitynotificationattributestypedef)
- [IdentityVerificationAttributesTypeDef](./type_defs.md#identityverificationattributestypedef)
- [KinesisFirehoseDestinationTypeDef](./type_defs.md#kinesisfirehosedestinationtypedef)
- [LambdaActionTypeDef](./type_defs.md#lambdaactiontypedef)
- [MessageTagTypeDef](./type_defs.md#messagetagtypedef)
- [ReceiptActionTypeDef](./type_defs.md#receiptactiontypedef)
- [ReceiptFilterTypeDef](./type_defs.md#receiptfiltertypedef)
- [ReceiptIpFilterTypeDef](./type_defs.md#receiptipfiltertypedef)
- [ReceiptRuleSetMetadataTypeDef](./type_defs.md#receiptrulesetmetadatatypedef)
- [ReceiptRuleTypeDef](./type_defs.md#receiptruletypedef)
- [RecipientDsnFieldsTypeDef](./type_defs.md#recipientdsnfieldstypedef)
- [ReputationOptionsTypeDef](./type_defs.md#reputationoptionstypedef)
- [S3ActionTypeDef](./type_defs.md#s3actiontypedef)
- [SNSActionTypeDef](./type_defs.md#snsactiontypedef)
- [SNSDestinationTypeDef](./type_defs.md#snsdestinationtypedef)
- [SendDataPointTypeDef](./type_defs.md#senddatapointtypedef)
- [StopActionTypeDef](./type_defs.md#stopactiontypedef)
- [TemplateMetadataTypeDef](./type_defs.md#templatemetadatatypedef)
- [TemplateTypeDef](./type_defs.md#templatetypedef)
- [TrackingOptionsTypeDef](./type_defs.md#trackingoptionstypedef)
- [WorkmailActionTypeDef](./type_defs.md#workmailactiontypedef)
- [BouncedRecipientInfoTypeDef](./type_defs.md#bouncedrecipientinfotypedef)
- [BulkEmailDestinationTypeDef](./type_defs.md#bulkemaildestinationtypedef)
- [DescribeActiveReceiptRuleSetResponseTypeDef](./type_defs.md#describeactivereceiptrulesetresponsetypedef)
- [DescribeConfigurationSetResponseTypeDef](./type_defs.md#describeconfigurationsetresponsetypedef)
- [DescribeReceiptRuleResponseTypeDef](./type_defs.md#describereceiptruleresponsetypedef)
- [DescribeReceiptRuleSetResponseTypeDef](./type_defs.md#describereceiptrulesetresponsetypedef)
- [GetAccountSendingEnabledResponseTypeDef](./type_defs.md#getaccountsendingenabledresponsetypedef)
- [GetCustomVerificationEmailTemplateResponseTypeDef](./type_defs.md#getcustomverificationemailtemplateresponsetypedef)
- [GetIdentityDkimAttributesResponseTypeDef](./type_defs.md#getidentitydkimattributesresponsetypedef)
- [GetIdentityMailFromDomainAttributesResponseTypeDef](./type_defs.md#getidentitymailfromdomainattributesresponsetypedef)
- [GetIdentityNotificationAttributesResponseTypeDef](./type_defs.md#getidentitynotificationattributesresponsetypedef)
- [GetIdentityPoliciesResponseTypeDef](./type_defs.md#getidentitypoliciesresponsetypedef)
- [GetIdentityVerificationAttributesResponseTypeDef](./type_defs.md#getidentityverificationattributesresponsetypedef)
- [GetSendQuotaResponseTypeDef](./type_defs.md#getsendquotaresponsetypedef)
- [GetSendStatisticsResponseTypeDef](./type_defs.md#getsendstatisticsresponsetypedef)
- [GetTemplateResponseTypeDef](./type_defs.md#gettemplateresponsetypedef)
- [ListConfigurationSetsResponseTypeDef](./type_defs.md#listconfigurationsetsresponsetypedef)
- [ListCustomVerificationEmailTemplatesResponseTypeDef](./type_defs.md#listcustomverificationemailtemplatesresponsetypedef)
- [ListIdentitiesResponseTypeDef](./type_defs.md#listidentitiesresponsetypedef)
- [ListIdentityPoliciesResponseTypeDef](./type_defs.md#listidentitypoliciesresponsetypedef)
- [ListReceiptFiltersResponseTypeDef](./type_defs.md#listreceiptfiltersresponsetypedef)
- [ListReceiptRuleSetsResponseTypeDef](./type_defs.md#listreceiptrulesetsresponsetypedef)
- [ListTemplatesResponseTypeDef](./type_defs.md#listtemplatesresponsetypedef)
- [ListVerifiedEmailAddressesResponseTypeDef](./type_defs.md#listverifiedemailaddressesresponsetypedef)
- [MessageDsnTypeDef](./type_defs.md#messagedsntypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RawMessageTypeDef](./type_defs.md#rawmessagetypedef)
- [SendBounceResponseTypeDef](./type_defs.md#sendbounceresponsetypedef)
- [SendBulkTemplatedEmailResponseTypeDef](./type_defs.md#sendbulktemplatedemailresponsetypedef)
- [SendCustomVerificationEmailResponseTypeDef](./type_defs.md#sendcustomverificationemailresponsetypedef)
- [SendEmailResponseTypeDef](./type_defs.md#sendemailresponsetypedef)
- [SendRawEmailResponseTypeDef](./type_defs.md#sendrawemailresponsetypedef)
- [SendTemplatedEmailResponseTypeDef](./type_defs.md#sendtemplatedemailresponsetypedef)
- [TestRenderTemplateResponseTypeDef](./type_defs.md#testrendertemplateresponsetypedef)
- [VerifyDomainDkimResponseTypeDef](./type_defs.md#verifydomaindkimresponsetypedef)
- [VerifyDomainIdentityResponseTypeDef](./type_defs.md#verifydomainidentityresponsetypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
