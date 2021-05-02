# Structures for boto3 PinpointEmail module

> [Index](../index.md) > [PinpointEmail](./index.md) > Structures

Auto-generated documentation for [PinpointEmail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail)
type annotations stubs module [mypy_boto3_pinpoint_email](https://pypi.org/project/mypy-boto3-pinpoint-email/).

- [Structures for boto3 PinpointEmail module](#structures-for-boto3-pinpointemail-module)
  - [BlacklistEntryTypeDef](#blacklistentrytypedef)
  - [BodyTypeDef](#bodytypedef)
  - [CloudWatchDestinationTypeDef](#cloudwatchdestinationtypedef)
  - [CloudWatchDimensionConfigurationTypeDef](#cloudwatchdimensionconfigurationtypedef)
  - [ContentTypeDef](#contenttypedef)
  - [DailyVolumeTypeDef](#dailyvolumetypedef)
  - [DedicatedIpTypeDef](#dedicatediptypedef)
  - [DeliverabilityTestReportTypeDef](#deliverabilitytestreporttypedef)
  - [DeliveryOptionsTypeDef](#deliveryoptionstypedef)
  - [DkimAttributesTypeDef](#dkimattributestypedef)
  - [DomainDeliverabilityCampaignTypeDef](#domaindeliverabilitycampaigntypedef)
  - [DomainDeliverabilityTrackingOptionTypeDef](#domaindeliverabilitytrackingoptiontypedef)
  - [DomainIspPlacementTypeDef](#domainispplacementtypedef)
  - [EventDestinationTypeDef](#eventdestinationtypedef)
  - [IdentityInfoTypeDef](#identityinfotypedef)
  - [InboxPlacementTrackingOptionTypeDef](#inboxplacementtrackingoptiontypedef)
  - [IspPlacementTypeDef](#ispplacementtypedef)
  - [KinesisFirehoseDestinationTypeDef](#kinesisfirehosedestinationtypedef)
  - [MailFromAttributesTypeDef](#mailfromattributestypedef)
  - [MessageTypeDef](#messagetypedef)
  - [OverallVolumeTypeDef](#overallvolumetypedef)
  - [PinpointDestinationTypeDef](#pinpointdestinationtypedef)
  - [PlacementStatisticsTypeDef](#placementstatisticstypedef)
  - [RawMessageTypeDef](#rawmessagetypedef)
  - [ReputationOptionsTypeDef](#reputationoptionstypedef)
  - [SendQuotaTypeDef](#sendquotatypedef)
  - [SendingOptionsTypeDef](#sendingoptionstypedef)
  - [SnsDestinationTypeDef](#snsdestinationtypedef)
  - [TagTypeDef](#tagtypedef)
  - [TemplateTypeDef](#templatetypedef)
  - [TrackingOptionsTypeDef](#trackingoptionstypedef)
  - [VolumeStatisticsTypeDef](#volumestatisticstypedef)
  - [CreateDeliverabilityTestReportResponseTypeDef](#createdeliverabilitytestreportresponsetypedef)
  - [CreateEmailIdentityResponseTypeDef](#createemailidentityresponsetypedef)
  - [DestinationTypeDef](#destinationtypedef)
  - [EmailContentTypeDef](#emailcontenttypedef)
  - [EventDestinationDefinitionTypeDef](#eventdestinationdefinitiontypedef)
  - [GetAccountResponseTypeDef](#getaccountresponsetypedef)
  - [GetBlacklistReportsResponseTypeDef](#getblacklistreportsresponsetypedef)
  - [GetConfigurationSetEventDestinationsResponseTypeDef](#getconfigurationseteventdestinationsresponsetypedef)
  - [GetConfigurationSetResponseTypeDef](#getconfigurationsetresponsetypedef)
  - [GetDedicatedIpResponseTypeDef](#getdedicatedipresponsetypedef)
  - [GetDedicatedIpsResponseTypeDef](#getdedicatedipsresponsetypedef)
  - [GetDeliverabilityDashboardOptionsResponseTypeDef](#getdeliverabilitydashboardoptionsresponsetypedef)
  - [GetDeliverabilityTestReportResponseTypeDef](#getdeliverabilitytestreportresponsetypedef)
  - [GetDomainDeliverabilityCampaignResponseTypeDef](#getdomaindeliverabilitycampaignresponsetypedef)
  - [GetDomainStatisticsReportResponseTypeDef](#getdomainstatisticsreportresponsetypedef)
  - [GetEmailIdentityResponseTypeDef](#getemailidentityresponsetypedef)
  - [ListConfigurationSetsResponseTypeDef](#listconfigurationsetsresponsetypedef)
  - [ListDedicatedIpPoolsResponseTypeDef](#listdedicatedippoolsresponsetypedef)
  - [ListDeliverabilityTestReportsResponseTypeDef](#listdeliverabilitytestreportsresponsetypedef)
  - [ListDomainDeliverabilityCampaignsResponseTypeDef](#listdomaindeliverabilitycampaignsresponsetypedef)
  - [ListEmailIdentitiesResponseTypeDef](#listemailidentitiesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MessageTagTypeDef](#messagetagtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [SendEmailResponseTypeDef](#sendemailresponsetypedef)

## BlacklistEntryTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef
```




Optional fields:
- `RblName`: `str`
- `ListingTime`: `datetime`
- `Description`: `str`


## BodyTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import BodyTypeDef
```




Optional fields:
- `Text`: `"ContentTypeDef"`
- `Html`: `"ContentTypeDef"`


## CloudWatchDestinationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import CloudWatchDestinationTypeDef
```


Required fields:
- `DimensionConfigurations`: `List["CloudWatchDimensionConfigurationTypeDef"]`




## CloudWatchDimensionConfigurationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import CloudWatchDimensionConfigurationTypeDef
```


Required fields:
- `DimensionName`: `str`
- `DimensionValueSource`: `DimensionValueSource`
- `DefaultDimensionValue`: `str`




## ContentTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ContentTypeDef
```


Required fields:
- `Data`: `str`



Optional fields:
- `Charset`: `str`


## DailyVolumeTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DailyVolumeTypeDef
```




Optional fields:
- `StartDate`: `datetime`
- `VolumeStatistics`: `"VolumeStatisticsTypeDef"`
- `DomainIspPlacements`: `List["DomainIspPlacementTypeDef"]`


## DedicatedIpTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DedicatedIpTypeDef
```


Required fields:
- `Ip`: `str`
- `WarmupStatus`: `WarmupStatus`
- `WarmupPercentage`: `int`



Optional fields:
- `PoolName`: `str`


## DeliverabilityTestReportTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DeliverabilityTestReportTypeDef
```




Optional fields:
- `ReportId`: `str`
- `ReportName`: `str`
- `Subject`: `str`
- `FromEmailAddress`: `str`
- `CreateDate`: `datetime`
- `DeliverabilityTestStatus`: `DeliverabilityTestStatus`


## DeliveryOptionsTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DeliveryOptionsTypeDef
```




Optional fields:
- `TlsPolicy`: `TlsPolicy`
- `SendingPoolName`: `str`


## DkimAttributesTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DkimAttributesTypeDef
```




Optional fields:
- `SigningEnabled`: `bool`
- `Status`: `DkimStatus`
- `Tokens`: `List[str]`


## DomainDeliverabilityCampaignTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DomainDeliverabilityCampaignTypeDef
```




Optional fields:
- `CampaignId`: `str`
- `ImageUrl`: `str`
- `Subject`: `str`
- `FromAddress`: `str`
- `SendingIps`: `List[str]`
- `FirstSeenDateTime`: `datetime`
- `LastSeenDateTime`: `datetime`
- `InboxCount`: `int`
- `SpamCount`: `int`
- `ReadRate`: `float`
- `DeleteRate`: `float`
- `ReadDeleteRate`: `float`
- `ProjectedVolume`: `int`
- `Esps`: `List[str]`


## DomainDeliverabilityTrackingOptionTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DomainDeliverabilityTrackingOptionTypeDef
```




Optional fields:
- `Domain`: `str`
- `SubscriptionStartDate`: `datetime`
- `InboxPlacementTrackingOption`: `"InboxPlacementTrackingOptionTypeDef"`


## DomainIspPlacementTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DomainIspPlacementTypeDef
```




Optional fields:
- `IspName`: `str`
- `InboxRawCount`: `int`
- `SpamRawCount`: `int`
- `InboxPercentage`: `float`
- `SpamPercentage`: `float`


## EventDestinationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import EventDestinationTypeDef
```


Required fields:
- `Name`: `str`
- `MatchingEventTypes`: `List[EventType]`



Optional fields:
- `Enabled`: `bool`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `CloudWatchDestination`: `"CloudWatchDestinationTypeDef"`
- `SnsDestination`: `"SnsDestinationTypeDef"`
- `PinpointDestination`: `"PinpointDestinationTypeDef"`


## IdentityInfoTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import IdentityInfoTypeDef
```




Optional fields:
- `IdentityType`: `IdentityType`
- `IdentityName`: `str`
- `SendingEnabled`: `bool`


## InboxPlacementTrackingOptionTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import InboxPlacementTrackingOptionTypeDef
```




Optional fields:
- `Global`: `bool`
- `TrackedIsps`: `List[str]`


## IspPlacementTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import IspPlacementTypeDef
```




Optional fields:
- `IspName`: `str`
- `PlacementStatistics`: `"PlacementStatisticsTypeDef"`


## KinesisFirehoseDestinationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import KinesisFirehoseDestinationTypeDef
```


Required fields:
- `IamRoleArn`: `str`
- `DeliveryStreamArn`: `str`




## MailFromAttributesTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import MailFromAttributesTypeDef
```


Required fields:
- `MailFromDomain`: `str`
- `MailFromDomainStatus`: `MailFromDomainStatus`
- `BehaviorOnMxFailure`: `BehaviorOnMxFailure`




## MessageTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import MessageTypeDef
```


Required fields:
- `Subject`: `"ContentTypeDef"`
- `Body`: `"BodyTypeDef"`




## OverallVolumeTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import OverallVolumeTypeDef
```




Optional fields:
- `VolumeStatistics`: `"VolumeStatisticsTypeDef"`
- `ReadRatePercent`: `float`
- `DomainIspPlacements`: `List["DomainIspPlacementTypeDef"]`


## PinpointDestinationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import PinpointDestinationTypeDef
```




Optional fields:
- `ApplicationArn`: `str`


## PlacementStatisticsTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import PlacementStatisticsTypeDef
```




Optional fields:
- `InboxPercentage`: `float`
- `SpamPercentage`: `float`
- `MissingPercentage`: `float`
- `SpfPercentage`: `float`
- `DkimPercentage`: `float`


## RawMessageTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import RawMessageTypeDef
```


Required fields:
- `Data`: `Union[bytes, IO[bytes]]`




## ReputationOptionsTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ReputationOptionsTypeDef
```




Optional fields:
- `ReputationMetricsEnabled`: `bool`
- `LastFreshStart`: `datetime`


## SendQuotaTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import SendQuotaTypeDef
```




Optional fields:
- `Max24HourSend`: `float`
- `MaxSendRate`: `float`
- `SentLast24Hours`: `float`


## SendingOptionsTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import SendingOptionsTypeDef
```




Optional fields:
- `SendingEnabled`: `bool`


## SnsDestinationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import SnsDestinationTypeDef
```


Required fields:
- `TopicArn`: `str`




## TagTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TemplateTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import TemplateTypeDef
```




Optional fields:
- `TemplateArn`: `str`
- `TemplateData`: `str`


## TrackingOptionsTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import TrackingOptionsTypeDef
```


Required fields:
- `CustomRedirectDomain`: `str`




## VolumeStatisticsTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import VolumeStatisticsTypeDef
```




Optional fields:
- `InboxRawCount`: `int`
- `SpamRawCount`: `int`
- `ProjectedInbox`: `int`
- `ProjectedSpam`: `int`


## CreateDeliverabilityTestReportResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import CreateDeliverabilityTestReportResponseTypeDef
```


Required fields:
- `ReportId`: `str`
- `DeliverabilityTestStatus`: `DeliverabilityTestStatus`




## CreateEmailIdentityResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import CreateEmailIdentityResponseTypeDef
```




Optional fields:
- `IdentityType`: `IdentityType`
- `VerifiedForSendingStatus`: `bool`
- `DkimAttributes`: `"DkimAttributesTypeDef"`


## DestinationTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import DestinationTypeDef
```




Optional fields:
- `ToAddresses`: `List[str]`
- `CcAddresses`: `List[str]`
- `BccAddresses`: `List[str]`


## EmailContentTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import EmailContentTypeDef
```




Optional fields:
- `Simple`: `"MessageTypeDef"`
- `Raw`: `"RawMessageTypeDef"`
- `Template`: `"TemplateTypeDef"`


## EventDestinationDefinitionTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import EventDestinationDefinitionTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `MatchingEventTypes`: `List[EventType]`
- `KinesisFirehoseDestination`: `"KinesisFirehoseDestinationTypeDef"`
- `CloudWatchDestination`: `"CloudWatchDestinationTypeDef"`
- `SnsDestination`: `"SnsDestinationTypeDef"`
- `PinpointDestination`: `"PinpointDestinationTypeDef"`


## GetAccountResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetAccountResponseTypeDef
```




Optional fields:
- `SendQuota`: `"SendQuotaTypeDef"`
- `SendingEnabled`: `bool`
- `DedicatedIpAutoWarmupEnabled`: `bool`
- `EnforcementStatus`: `str`
- `ProductionAccessEnabled`: `bool`


## GetBlacklistReportsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetBlacklistReportsResponseTypeDef
```


Required fields:
- `BlacklistReport`: `Dict[str, List["BlacklistEntryTypeDef"]]`




## GetConfigurationSetEventDestinationsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetConfigurationSetEventDestinationsResponseTypeDef
```




Optional fields:
- `EventDestinations`: `List["EventDestinationTypeDef"]`


## GetConfigurationSetResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetConfigurationSetResponseTypeDef
```




Optional fields:
- `ConfigurationSetName`: `str`
- `TrackingOptions`: `"TrackingOptionsTypeDef"`
- `DeliveryOptions`: `"DeliveryOptionsTypeDef"`
- `ReputationOptions`: `"ReputationOptionsTypeDef"`
- `SendingOptions`: `"SendingOptionsTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## GetDedicatedIpResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetDedicatedIpResponseTypeDef
```




Optional fields:
- `DedicatedIp`: `"DedicatedIpTypeDef"`


## GetDedicatedIpsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetDedicatedIpsResponseTypeDef
```




Optional fields:
- `DedicatedIps`: `List["DedicatedIpTypeDef"]`
- `NextToken`: `str`


## GetDeliverabilityDashboardOptionsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetDeliverabilityDashboardOptionsResponseTypeDef
```


Required fields:
- `DashboardEnabled`: `bool`



Optional fields:
- `SubscriptionExpiryDate`: `datetime`
- `AccountStatus`: `DeliverabilityDashboardAccountStatus`
- `ActiveSubscribedDomains`: `List["DomainDeliverabilityTrackingOptionTypeDef"]`
- `PendingExpirationSubscribedDomains`: `List["DomainDeliverabilityTrackingOptionTypeDef"]`


## GetDeliverabilityTestReportResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetDeliverabilityTestReportResponseTypeDef
```


Required fields:
- `DeliverabilityTestReport`: `"DeliverabilityTestReportTypeDef"`
- `OverallPlacement`: `"PlacementStatisticsTypeDef"`
- `IspPlacements`: `List["IspPlacementTypeDef"]`



Optional fields:
- `Message`: `str`
- `Tags`: `List["TagTypeDef"]`


## GetDomainDeliverabilityCampaignResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetDomainDeliverabilityCampaignResponseTypeDef
```


Required fields:
- `DomainDeliverabilityCampaign`: `"DomainDeliverabilityCampaignTypeDef"`




## GetDomainStatisticsReportResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetDomainStatisticsReportResponseTypeDef
```


Required fields:
- `OverallVolume`: `"OverallVolumeTypeDef"`
- `DailyVolumes`: `List["DailyVolumeTypeDef"]`




## GetEmailIdentityResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import GetEmailIdentityResponseTypeDef
```




Optional fields:
- `IdentityType`: `IdentityType`
- `FeedbackForwardingStatus`: `bool`
- `VerifiedForSendingStatus`: `bool`
- `DkimAttributes`: `"DkimAttributesTypeDef"`
- `MailFromAttributes`: `"MailFromAttributesTypeDef"`
- `Tags`: `List["TagTypeDef"]`


## ListConfigurationSetsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ListConfigurationSetsResponseTypeDef
```




Optional fields:
- `ConfigurationSets`: `List[str]`
- `NextToken`: `str`


## ListDedicatedIpPoolsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ListDedicatedIpPoolsResponseTypeDef
```




Optional fields:
- `DedicatedIpPools`: `List[str]`
- `NextToken`: `str`


## ListDeliverabilityTestReportsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ListDeliverabilityTestReportsResponseTypeDef
```


Required fields:
- `DeliverabilityTestReports`: `List["DeliverabilityTestReportTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListDomainDeliverabilityCampaignsResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ListDomainDeliverabilityCampaignsResponseTypeDef
```


Required fields:
- `DomainDeliverabilityCampaigns`: `List["DomainDeliverabilityCampaignTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListEmailIdentitiesResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ListEmailIdentitiesResponseTypeDef
```




Optional fields:
- `EmailIdentities`: `List["IdentityInfoTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import ListTagsForResourceResponseTypeDef
```


Required fields:
- `Tags`: `List["TagTypeDef"]`




## MessageTagTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import MessageTagTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## SendEmailResponseTypeDef

```python
from mypy_boto3_pinpoint_email.type_defs import SendEmailResponseTypeDef
```




Optional fields:
- `MessageId`: `str`

