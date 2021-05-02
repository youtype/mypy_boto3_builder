# Structures for boto3 SES module

> [Index](../index.md) > [SES](./index.md) > Structures

Auto-generated documentation for [SES](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES)
type annotations stubs module [mypy_boto3_ses](https://pypi.org/project/mypy-boto3-ses/).

- [Structures for boto3 SES module](#structures-for-boto3-ses-module)
  - [AddHeaderActionTypeDef](#addheaderactiontypedef)
  - [BodyTypeDef](#bodytypedef)
  - [BounceActionTypeDef](#bounceactiontypedef)
  - [BouncedRecipientInfoTypeDef](#bouncedrecipientinfotypedef)
  - [BulkEmailDestinationStatusTypeDef](#bulkemaildestinationstatustypedef)
  - [BulkEmailDestinationTypeDef](#bulkemaildestinationtypedef)
  - [CloudWatchDestinationTypeDef](#cloudwatchdestinationtypedef)
  - [CloudWatchDimensionConfigurationTypeDef](#cloudwatchdimensionconfigurationtypedef)
  - [ConfigurationSetTypeDef](#configurationsettypedef)
  - [ContentTypeDef](#contenttypedef)
  - [CustomVerificationEmailTemplateTypeDef](#customverificationemailtemplatetypedef)
  - [DeliveryOptionsTypeDef](#deliveryoptionstypedef)
  - [DescribeActiveReceiptRuleSetResponseTypeDef](#describeactivereceiptrulesetresponsetypedef)
  - [DescribeConfigurationSetResponseTypeDef](#describeconfigurationsetresponsetypedef)
  - [DescribeReceiptRuleResponseTypeDef](#describereceiptruleresponsetypedef)
  - [DescribeReceiptRuleSetResponseTypeDef](#describereceiptrulesetresponsetypedef)
  - [DestinationTypeDef](#destinationtypedef)
  - [EventDestinationTypeDef](#eventdestinationtypedef)
  - [ExtensionFieldTypeDef](#extensionfieldtypedef)
  - [GetAccountSendingEnabledResponseTypeDef](#getaccountsendingenabledresponsetypedef)
  - [GetCustomVerificationEmailTemplateResponseTypeDef](#getcustomverificationemailtemplateresponsetypedef)
  - [GetIdentityDkimAttributesResponseTypeDef](#getidentitydkimattributesresponsetypedef)
  - [GetIdentityMailFromDomainAttributesResponseTypeDef](#getidentitymailfromdomainattributesresponsetypedef)
  - [GetIdentityNotificationAttributesResponseTypeDef](#getidentitynotificationattributesresponsetypedef)
  - [GetIdentityPoliciesResponseTypeDef](#getidentitypoliciesresponsetypedef)
  - [GetIdentityVerificationAttributesResponseTypeDef](#getidentityverificationattributesresponsetypedef)
  - [GetSendQuotaResponseTypeDef](#getsendquotaresponsetypedef)
  - [GetSendStatisticsResponseTypeDef](#getsendstatisticsresponsetypedef)
  - [GetTemplateResponseTypeDef](#gettemplateresponsetypedef)
  - [IdentityDkimAttributesTypeDef](#identitydkimattributestypedef)
  - [IdentityMailFromDomainAttributesTypeDef](#identitymailfromdomainattributestypedef)
  - [IdentityNotificationAttributesTypeDef](#identitynotificationattributestypedef)
  - [IdentityVerificationAttributesTypeDef](#identityverificationattributestypedef)
  - [KinesisFirehoseDestinationTypeDef](#kinesisfirehosedestinationtypedef)
  - [LambdaActionTypeDef](#lambdaactiontypedef)
  - [ListConfigurationSetsResponseTypeDef](#listconfigurationsetsresponsetypedef)
  - [ListCustomVerificationEmailTemplatesResponseTypeDef](#listcustomverificationemailtemplatesresponsetypedef)
  - [ListIdentitiesResponseTypeDef](#listidentitiesresponsetypedef)
  - [ListIdentityPoliciesResponseTypeDef](#listidentitypoliciesresponsetypedef)
  - [ListReceiptFiltersResponseTypeDef](#listreceiptfiltersresponsetypedef)
  - [ListReceiptRuleSetsResponseTypeDef](#listreceiptrulesetsresponsetypedef)
  - [ListTemplatesResponseTypeDef](#listtemplatesresponsetypedef)
  - [ListVerifiedEmailAddressesResponseTypeDef](#listverifiedemailaddressesresponsetypedef)
  - [MessageDsnTypeDef](#messagedsntypedef)
  - [MessageTagTypeDef](#messagetagtypedef)
  - [MessageTypeDef](#messagetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [RawMessageTypeDef](#rawmessagetypedef)
  - [ReceiptActionTypeDef](#receiptactiontypedef)
  - [ReceiptFilterTypeDef](#receiptfiltertypedef)
  - [ReceiptIpFilterTypeDef](#receiptipfiltertypedef)
  - [ReceiptRuleSetMetadataTypeDef](#receiptrulesetmetadatatypedef)
  - [ReceiptRuleTypeDef](#receiptruletypedef)
  - [RecipientDsnFieldsTypeDef](#recipientdsnfieldstypedef)
  - [ReputationOptionsTypeDef](#reputationoptionstypedef)
  - [S3ActionTypeDef](#s3actiontypedef)
  - [SNSActionTypeDef](#snsactiontypedef)
  - [SNSDestinationTypeDef](#snsdestinationtypedef)
  - [SendBounceResponseTypeDef](#sendbounceresponsetypedef)
  - [SendBulkTemplatedEmailResponseTypeDef](#sendbulktemplatedemailresponsetypedef)
  - [SendCustomVerificationEmailResponseTypeDef](#sendcustomverificationemailresponsetypedef)
  - [SendDataPointTypeDef](#senddatapointtypedef)
  - [SendEmailResponseTypeDef](#sendemailresponsetypedef)
  - [SendRawEmailResponseTypeDef](#sendrawemailresponsetypedef)
  - [SendTemplatedEmailResponseTypeDef](#sendtemplatedemailresponsetypedef)
  - [StopActionTypeDef](#stopactiontypedef)
  - [TemplateMetadataTypeDef](#templatemetadatatypedef)
  - [TemplateTypeDef](#templatetypedef)
  - [TestRenderTemplateResponseTypeDef](#testrendertemplateresponsetypedef)
  - [TrackingOptionsTypeDef](#trackingoptionstypedef)
  - [VerifyDomainDkimResponseTypeDef](#verifydomaindkimresponsetypedef)
  - [VerifyDomainIdentityResponseTypeDef](#verifydomainidentityresponsetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)
  - [WorkmailActionTypeDef](#workmailactiontypedef)

## AddHeaderActionTypeDef

```python
from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef
```


Required fields:
- `HeaderName`: `str`
- `HeaderValue`: `str`




## BodyTypeDef

```python
from mypy_boto3_ses.type_defs import BodyTypeDef
```




Optional fields:
- `Text`: `"ContentTypeDef"`
- `Html`: `"ContentTypeDef"`


## BounceActionTypeDef

```python
from mypy_boto3_ses.type_defs import BounceActionTypeDef
```


Required fields:
- `SmtpReplyCode`: `str`
- `Message`: `str`
- `Sender`: `str`



Optional fields:
- `TopicArn`: `str`
- `StatusCode`: `str`


## BouncedRecipientInfoTypeDef

```python
from mypy_boto3_ses.type_defs import BouncedRecipientInfoTypeDef
```


Required fields:
- `Recipient`: `str`



Optional fields:
- `RecipientArn`: `str`
- `BounceType`: `BounceType`
- `RecipientDsnFields`: `"RecipientDsnFieldsTypeDef"`


## BulkEmailDestinationStatusTypeDef

```python
from mypy_boto3_ses.type_defs import BulkEmailDestinationStatusTypeDef
```




Optional fields:
- `Status`: `BulkEmailStatus`
- `Error`: `str`
- `MessageId`: `str`


## BulkEmailDestinationTypeDef

```python
from mypy_boto3_ses.type_defs import BulkEmailDestinationTypeDef
```


Required fields:
- `Destination`: `"DestinationTypeDef"`



Optional fields:
- `ReplacementTags`: `List["MessageTagTypeDef"]`
- `ReplacementTemplateData`: `str`


## CloudWatchDestinationTypeDef

```python
from mypy_boto3_ses.type_defs import CloudWatchDestinationTypeDef
```


Required fields:
- `DimensionConfigurations`: `List["CloudWatchDimensionConfigurationTypeDef"]`




## CloudWatchDimensionConfigurationTypeDef

```python
from mypy_boto3_ses.type_defs import CloudWatchDimensionConfigurationTypeDef
```


Required fields:
- `DimensionName`: `str`
- `DimensionValueSource`: `DimensionValueSource`
- `DefaultDimensionValue`: `str`




## ConfigurationSetTypeDef

```python
from mypy_boto3_ses.type_defs import ConfigurationSetTypeDef
```


Required fields:
- `Name`: `str`




## ContentTypeDef

```python
from mypy_boto3_ses.type_defs import ContentTypeDef
```


Required fields:
- `Data`: `str`



Optional fields:
- `Charset`: `str`


## CustomVerificationEmailTemplateTypeDef

```python
from mypy_boto3_ses.type_defs import CustomVerificationEmailTemplateTypeDef
```




Optional fields:
- `TemplateName`: `str`
- `FromEmailAddress`: `str`
- `TemplateSubject`: `str`
- `SuccessRedirectionURL`: `str`
- `FailureRedirectionURL`: `str`


## DeliveryOptionsTypeDef

```python
from mypy_boto3_ses.type_defs import DeliveryOptionsTypeDef
```




Optional fields:
- `TlsPolicy`: `TlsPolicy`


## DescribeActiveReceiptRuleSetResponseTypeDef

```python
from mypy_boto3_ses.type_defs import DescribeActiveReceiptRuleSetResponseTypeDef
```




Optional fields:
- `Metadata`: `"ReceiptRuleSetMetadataTypeDef"`
- `Rules`: `List["ReceiptRuleTypeDef"]`


## DescribeConfigurationSetResponseTypeDef

```python
from mypy_boto3_ses.type_defs import DescribeConfigurationSetResponseTypeDef
```




Optional fields:
- `ConfigurationSet`: `"ConfigurationSetTypeDef"`
- `EventDestinations`: `List["EventDestinationTypeDef"]`
- `TrackingOptions`: `"TrackingOptionsTypeDef"`
- `DeliveryOptions`: `"DeliveryOptionsTypeDef"`
- `ReputationOptions`: `"ReputationOptionsTypeDef"`


## DescribeReceiptRuleResponseTypeDef

```python
from mypy_boto3_ses.type_defs import DescribeReceiptRuleResponseTypeDef
```




Optional fields:
- `Rule`: `"ReceiptRuleTypeDef"`


## DescribeReceiptRuleSetResponseTypeDef

```python
from mypy_boto3_ses.type_defs import DescribeReceiptRuleSetResponseTypeDef
```




Optional fields:
- `Metadata`: `"ReceiptRuleSetMetadataTypeDef"`
- `Rules`: `List["ReceiptRuleTypeDef"]`


## DestinationTypeDef

```python
from mypy_boto3_ses.type_defs import DestinationTypeDef
```




Optional fields:
- `ToAddresses`: `List[str]`
- `CcAddresses`: `List[str]`
- `BccAddresses`: `List[str]`


## EventDestinationTypeDef

```python
from mypy_boto3_ses.type_defs import EventDestinationTypeDef
```


Required fields:
- `Name`: `str`
- `MatchingEventTypes`: `List[EventType]`



Optional fields:
- `Enabled`: `bool`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `CloudWatchDestination`: `"CloudWatchDestinationTypeDef"`
- `SNSDestination`: `"SNSDestinationTypeDef"`


## ExtensionFieldTypeDef

```python
from mypy_boto3_ses.type_defs import ExtensionFieldTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## GetAccountSendingEnabledResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetAccountSendingEnabledResponseTypeDef
```




Optional fields:
- `Enabled`: `bool`


## GetCustomVerificationEmailTemplateResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetCustomVerificationEmailTemplateResponseTypeDef
```




Optional fields:
- `TemplateName`: `str`
- `FromEmailAddress`: `str`
- `TemplateSubject`: `str`
- `TemplateContent`: `str`
- `SuccessRedirectionURL`: `str`
- `FailureRedirectionURL`: `str`


## GetIdentityDkimAttributesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetIdentityDkimAttributesResponseTypeDef
```


Required fields:
- `DkimAttributes`: `Dict[str, "IdentityDkimAttributesTypeDef"]`




## GetIdentityMailFromDomainAttributesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetIdentityMailFromDomainAttributesResponseTypeDef
```


Required fields:
- `MailFromDomainAttributes`: `Dict[str, "IdentityMailFromDomainAttributesTypeDef"]`




## GetIdentityNotificationAttributesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetIdentityNotificationAttributesResponseTypeDef
```


Required fields:
- `NotificationAttributes`: `Dict[str, "IdentityNotificationAttributesTypeDef"]`




## GetIdentityPoliciesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetIdentityPoliciesResponseTypeDef
```


Required fields:
- `Policies`: `Dict[str, str]`




## GetIdentityVerificationAttributesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetIdentityVerificationAttributesResponseTypeDef
```


Required fields:
- `VerificationAttributes`: `Dict[str, "IdentityVerificationAttributesTypeDef"]`




## GetSendQuotaResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetSendQuotaResponseTypeDef
```




Optional fields:
- `Max24HourSend`: `float`
- `MaxSendRate`: `float`
- `SentLast24Hours`: `float`


## GetSendStatisticsResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetSendStatisticsResponseTypeDef
```




Optional fields:
- `SendDataPoints`: `List["SendDataPointTypeDef"]`


## GetTemplateResponseTypeDef

```python
from mypy_boto3_ses.type_defs import GetTemplateResponseTypeDef
```




Optional fields:
- `Template`: `"TemplateTypeDef"`


## IdentityDkimAttributesTypeDef

```python
from mypy_boto3_ses.type_defs import IdentityDkimAttributesTypeDef
```


Required fields:
- `DkimEnabled`: `bool`
- `DkimVerificationStatus`: `VerificationStatus`



Optional fields:
- `DkimTokens`: `List[str]`


## IdentityMailFromDomainAttributesTypeDef

```python
from mypy_boto3_ses.type_defs import IdentityMailFromDomainAttributesTypeDef
```


Required fields:
- `MailFromDomain`: `str`
- `MailFromDomainStatus`: `CustomMailFromStatus`
- `BehaviorOnMXFailure`: `BehaviorOnMXFailure`




## IdentityNotificationAttributesTypeDef

```python
from mypy_boto3_ses.type_defs import IdentityNotificationAttributesTypeDef
```


Required fields:
- `BounceTopic`: `str`
- `ComplaintTopic`: `str`
- `DeliveryTopic`: `str`
- `ForwardingEnabled`: `bool`



Optional fields:
- `HeadersInBounceNotificationsEnabled`: `bool`
- `HeadersInComplaintNotificationsEnabled`: `bool`
- `HeadersInDeliveryNotificationsEnabled`: `bool`


## IdentityVerificationAttributesTypeDef

```python
from mypy_boto3_ses.type_defs import IdentityVerificationAttributesTypeDef
```


Required fields:
- `VerificationStatus`: `VerificationStatus`



Optional fields:
- `VerificationToken`: `str`


## KinesisFirehoseDestinationTypeDef

```python
from mypy_boto3_ses.type_defs import KinesisFirehoseDestinationTypeDef
```


Required fields:
- `IAMRoleARN`: `str`
- `DeliveryStreamARN`: `str`




## LambdaActionTypeDef

```python
from mypy_boto3_ses.type_defs import LambdaActionTypeDef
```


Required fields:
- `FunctionArn`: `str`



Optional fields:
- `TopicArn`: `str`
- `InvocationType`: `InvocationType`


## ListConfigurationSetsResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListConfigurationSetsResponseTypeDef
```




Optional fields:
- `ConfigurationSets`: `List["ConfigurationSetTypeDef"]`
- `NextToken`: `str`


## ListCustomVerificationEmailTemplatesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListCustomVerificationEmailTemplatesResponseTypeDef
```




Optional fields:
- `CustomVerificationEmailTemplates`: `List["CustomVerificationEmailTemplateTypeDef"]`
- `NextToken`: `str`


## ListIdentitiesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListIdentitiesResponseTypeDef
```


Required fields:
- `Identities`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListIdentityPoliciesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListIdentityPoliciesResponseTypeDef
```


Required fields:
- `PolicyNames`: `List[str]`




## ListReceiptFiltersResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListReceiptFiltersResponseTypeDef
```




Optional fields:
- `Filters`: `List["ReceiptFilterTypeDef"]`


## ListReceiptRuleSetsResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListReceiptRuleSetsResponseTypeDef
```




Optional fields:
- `RuleSets`: `List["ReceiptRuleSetMetadataTypeDef"]`
- `NextToken`: `str`


## ListTemplatesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListTemplatesResponseTypeDef
```




Optional fields:
- `TemplatesMetadata`: `List["TemplateMetadataTypeDef"]`
- `NextToken`: `str`


## ListVerifiedEmailAddressesResponseTypeDef

```python
from mypy_boto3_ses.type_defs import ListVerifiedEmailAddressesResponseTypeDef
```




Optional fields:
- `VerifiedEmailAddresses`: `List[str]`


## MessageDsnTypeDef

```python
from mypy_boto3_ses.type_defs import MessageDsnTypeDef
```


Required fields:
- `ReportingMta`: `str`



Optional fields:
- `ArrivalDate`: `datetime`
- `ExtensionFields`: `List["ExtensionFieldTypeDef"]`


## MessageTagTypeDef

```python
from mypy_boto3_ses.type_defs import MessageTagTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## MessageTypeDef

```python
from mypy_boto3_ses.type_defs import MessageTypeDef
```


Required fields:
- `Subject`: `"ContentTypeDef"`
- `Body`: `"BodyTypeDef"`




## PaginatorConfigTypeDef

```python
from mypy_boto3_ses.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## RawMessageTypeDef

```python
from mypy_boto3_ses.type_defs import RawMessageTypeDef
```


Required fields:
- `Data`: `Union[bytes, IO[bytes]]`




## ReceiptActionTypeDef

```python
from mypy_boto3_ses.type_defs import ReceiptActionTypeDef
```




Optional fields:
- `S3Action`: `"S3ActionTypeDef"`
- `BounceAction`: `"BounceActionTypeDef"`
- `WorkmailAction`: `"WorkmailActionTypeDef"`
- `LambdaAction`: `"LambdaActionTypeDef"`
- `StopAction`: `"StopActionTypeDef"`
- `AddHeaderAction`: `"AddHeaderActionTypeDef"`
- `SNSAction`: `"SNSActionTypeDef"`


## ReceiptFilterTypeDef

```python
from mypy_boto3_ses.type_defs import ReceiptFilterTypeDef
```


Required fields:
- `Name`: `str`
- `IpFilter`: `"ReceiptIpFilterTypeDef"`




## ReceiptIpFilterTypeDef

```python
from mypy_boto3_ses.type_defs import ReceiptIpFilterTypeDef
```


Required fields:
- `Policy`: `ReceiptFilterPolicy`
- `Cidr`: `str`




## ReceiptRuleSetMetadataTypeDef

```python
from mypy_boto3_ses.type_defs import ReceiptRuleSetMetadataTypeDef
```




Optional fields:
- `Name`: `str`
- `CreatedTimestamp`: `datetime`


## ReceiptRuleTypeDef

```python
from mypy_boto3_ses.type_defs import ReceiptRuleTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `Enabled`: `bool`
- `TlsPolicy`: `TlsPolicy`
- `Recipients`: `List[str]`
- `Actions`: `List["ReceiptActionTypeDef"]`
- `ScanEnabled`: `bool`


## RecipientDsnFieldsTypeDef

```python
from mypy_boto3_ses.type_defs import RecipientDsnFieldsTypeDef
```


Required fields:
- `Action`: `DsnAction`
- `Status`: `str`



Optional fields:
- `FinalRecipient`: `str`
- `RemoteMta`: `str`
- `DiagnosticCode`: `str`
- `LastAttemptDate`: `datetime`
- `ExtensionFields`: `List["ExtensionFieldTypeDef"]`


## ReputationOptionsTypeDef

```python
from mypy_boto3_ses.type_defs import ReputationOptionsTypeDef
```




Optional fields:
- `SendingEnabled`: `bool`
- `ReputationMetricsEnabled`: `bool`
- `LastFreshStart`: `datetime`


## S3ActionTypeDef

```python
from mypy_boto3_ses.type_defs import S3ActionTypeDef
```


Required fields:
- `BucketName`: `str`



Optional fields:
- `TopicArn`: `str`
- `ObjectKeyPrefix`: `str`
- `KmsKeyArn`: `str`


## SNSActionTypeDef

```python
from mypy_boto3_ses.type_defs import SNSActionTypeDef
```


Required fields:
- `TopicArn`: `str`



Optional fields:
- `Encoding`: `SNSActionEncoding`


## SNSDestinationTypeDef

```python
from mypy_boto3_ses.type_defs import SNSDestinationTypeDef
```


Required fields:
- `TopicARN`: `str`




## SendBounceResponseTypeDef

```python
from mypy_boto3_ses.type_defs import SendBounceResponseTypeDef
```




Optional fields:
- `MessageId`: `str`


## SendBulkTemplatedEmailResponseTypeDef

```python
from mypy_boto3_ses.type_defs import SendBulkTemplatedEmailResponseTypeDef
```


Required fields:
- `Status`: `List["BulkEmailDestinationStatusTypeDef"]`




## SendCustomVerificationEmailResponseTypeDef

```python
from mypy_boto3_ses.type_defs import SendCustomVerificationEmailResponseTypeDef
```




Optional fields:
- `MessageId`: `str`


## SendDataPointTypeDef

```python
from mypy_boto3_ses.type_defs import SendDataPointTypeDef
```




Optional fields:
- `Timestamp`: `datetime`
- `DeliveryAttempts`: `int`
- `Bounces`: `int`
- `Complaints`: `int`
- `Rejects`: `int`


## SendEmailResponseTypeDef

```python
from mypy_boto3_ses.type_defs import SendEmailResponseTypeDef
```


Required fields:
- `MessageId`: `str`




## SendRawEmailResponseTypeDef

```python
from mypy_boto3_ses.type_defs import SendRawEmailResponseTypeDef
```


Required fields:
- `MessageId`: `str`




## SendTemplatedEmailResponseTypeDef

```python
from mypy_boto3_ses.type_defs import SendTemplatedEmailResponseTypeDef
```


Required fields:
- `MessageId`: `str`




## StopActionTypeDef

```python
from mypy_boto3_ses.type_defs import StopActionTypeDef
```


Required fields:
- `Scope`: `Literal['RuleSet']`



Optional fields:
- `TopicArn`: `str`


## TemplateMetadataTypeDef

```python
from mypy_boto3_ses.type_defs import TemplateMetadataTypeDef
```




Optional fields:
- `Name`: `str`
- `CreatedTimestamp`: `datetime`


## TemplateTypeDef

```python
from mypy_boto3_ses.type_defs import TemplateTypeDef
```


Required fields:
- `TemplateName`: `str`



Optional fields:
- `SubjectPart`: `str`
- `TextPart`: `str`
- `HtmlPart`: `str`


## TestRenderTemplateResponseTypeDef

```python
from mypy_boto3_ses.type_defs import TestRenderTemplateResponseTypeDef
```




Optional fields:
- `RenderedTemplate`: `str`


## TrackingOptionsTypeDef

```python
from mypy_boto3_ses.type_defs import TrackingOptionsTypeDef
```




Optional fields:
- `CustomRedirectDomain`: `str`


## VerifyDomainDkimResponseTypeDef

```python
from mypy_boto3_ses.type_defs import VerifyDomainDkimResponseTypeDef
```


Required fields:
- `DkimTokens`: `List[str]`




## VerifyDomainIdentityResponseTypeDef

```python
from mypy_boto3_ses.type_defs import VerifyDomainIdentityResponseTypeDef
```


Required fields:
- `VerificationToken`: `str`




## WaiterConfigTypeDef

```python
from mypy_boto3_ses.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`


## WorkmailActionTypeDef

```python
from mypy_boto3_ses.type_defs import WorkmailActionTypeDef
```


Required fields:
- `OrganizationArn`: `str`



Optional fields:
- `TopicArn`: `str`

