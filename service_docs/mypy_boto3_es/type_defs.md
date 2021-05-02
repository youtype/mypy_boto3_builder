# Structures for boto3 ElasticsearchService module

> [Index](../index.md) > [ElasticsearchService](./index.md) > Structures

Auto-generated documentation for [ElasticsearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService)
type annotations stubs module [mypy_boto3_es](https://pypi.org/project/mypy-boto3-es/).

- [Structures for boto3 ElasticsearchService module](#structures-for-boto3-elasticsearchservice-module)
  - [AccessPoliciesStatusTypeDef](#accesspoliciesstatustypedef)
  - [AdditionalLimitTypeDef](#additionallimittypedef)
  - [AdvancedOptionsStatusTypeDef](#advancedoptionsstatustypedef)
  - [AdvancedSecurityOptionsStatusTypeDef](#advancedsecurityoptionsstatustypedef)
  - [AdvancedSecurityOptionsTypeDef](#advancedsecurityoptionstypedef)
  - [AutoTuneDetailsTypeDef](#autotunedetailstypedef)
  - [AutoTuneMaintenanceScheduleTypeDef](#autotunemaintenancescheduletypedef)
  - [AutoTuneOptionsOutputTypeDef](#autotuneoptionsoutputtypedef)
  - [AutoTuneOptionsStatusTypeDef](#autotuneoptionsstatustypedef)
  - [AutoTuneOptionsTypeDef](#autotuneoptionstypedef)
  - [AutoTuneStatusTypeDef](#autotunestatustypedef)
  - [AutoTuneTypeDef](#autotunetypedef)
  - [CognitoOptionsStatusTypeDef](#cognitooptionsstatustypedef)
  - [CognitoOptionsTypeDef](#cognitooptionstypedef)
  - [CompatibleVersionsMapTypeDef](#compatibleversionsmaptypedef)
  - [DomainEndpointOptionsStatusTypeDef](#domainendpointoptionsstatustypedef)
  - [DomainEndpointOptionsTypeDef](#domainendpointoptionstypedef)
  - [DomainInfoTypeDef](#domaininfotypedef)
  - [DomainInformationTypeDef](#domaininformationtypedef)
  - [DomainPackageDetailsTypeDef](#domainpackagedetailstypedef)
  - [DurationTypeDef](#durationtypedef)
  - [EBSOptionsStatusTypeDef](#ebsoptionsstatustypedef)
  - [EBSOptionsTypeDef](#ebsoptionstypedef)
  - [ElasticsearchClusterConfigStatusTypeDef](#elasticsearchclusterconfigstatustypedef)
  - [ElasticsearchClusterConfigTypeDef](#elasticsearchclusterconfigtypedef)
  - [ElasticsearchDomainConfigTypeDef](#elasticsearchdomainconfigtypedef)
  - [ElasticsearchDomainStatusTypeDef](#elasticsearchdomainstatustypedef)
  - [ElasticsearchVersionStatusTypeDef](#elasticsearchversionstatustypedef)
  - [EncryptionAtRestOptionsStatusTypeDef](#encryptionatrestoptionsstatustypedef)
  - [EncryptionAtRestOptionsTypeDef](#encryptionatrestoptionstypedef)
  - [ErrorDetailsTypeDef](#errordetailstypedef)
  - [InboundCrossClusterSearchConnectionStatusTypeDef](#inboundcrossclustersearchconnectionstatustypedef)
  - [InboundCrossClusterSearchConnectionTypeDef](#inboundcrossclustersearchconnectiontypedef)
  - [InstanceCountLimitsTypeDef](#instancecountlimitstypedef)
  - [InstanceLimitsTypeDef](#instancelimitstypedef)
  - [LimitsTypeDef](#limitstypedef)
  - [LogPublishingOptionTypeDef](#logpublishingoptiontypedef)
  - [LogPublishingOptionsStatusTypeDef](#logpublishingoptionsstatustypedef)
  - [MasterUserOptionsTypeDef](#masteruseroptionstypedef)
  - [NodeToNodeEncryptionOptionsStatusTypeDef](#nodetonodeencryptionoptionsstatustypedef)
  - [NodeToNodeEncryptionOptionsTypeDef](#nodetonodeencryptionoptionstypedef)
  - [OptionStatusTypeDef](#optionstatustypedef)
  - [OutboundCrossClusterSearchConnectionStatusTypeDef](#outboundcrossclustersearchconnectionstatustypedef)
  - [OutboundCrossClusterSearchConnectionTypeDef](#outboundcrossclustersearchconnectiontypedef)
  - [PackageDetailsTypeDef](#packagedetailstypedef)
  - [PackageVersionHistoryTypeDef](#packageversionhistorytypedef)
  - [RecurringChargeTypeDef](#recurringchargetypedef)
  - [ReservedElasticsearchInstanceOfferingTypeDef](#reservedelasticsearchinstanceofferingtypedef)
  - [ReservedElasticsearchInstanceTypeDef](#reservedelasticsearchinstancetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SAMLIdpTypeDef](#samlidptypedef)
  - [SAMLOptionsInputTypeDef](#samloptionsinputtypedef)
  - [SAMLOptionsOutputTypeDef](#samloptionsoutputtypedef)
  - [ScheduledAutoTuneDetailsTypeDef](#scheduledautotunedetailstypedef)
  - [ServiceSoftwareOptionsTypeDef](#servicesoftwareoptionstypedef)
  - [SnapshotOptionsStatusTypeDef](#snapshotoptionsstatustypedef)
  - [SnapshotOptionsTypeDef](#snapshotoptionstypedef)
  - [StorageTypeLimitTypeDef](#storagetypelimittypedef)
  - [StorageTypeTypeDef](#storagetypetypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpgradeHistoryTypeDef](#upgradehistorytypedef)
  - [UpgradeStepItemTypeDef](#upgradestepitemtypedef)
  - [VPCDerivedInfoStatusTypeDef](#vpcderivedinfostatustypedef)
  - [VPCDerivedInfoTypeDef](#vpcderivedinfotypedef)
  - [ZoneAwarenessConfigTypeDef](#zoneawarenessconfigtypedef)
  - [AcceptInboundCrossClusterSearchConnectionResponseTypeDef](#acceptinboundcrossclustersearchconnectionresponsetypedef)
  - [AdvancedSecurityOptionsInputTypeDef](#advancedsecurityoptionsinputtypedef)
  - [AssociatePackageResponseTypeDef](#associatepackageresponsetypedef)
  - [AutoTuneOptionsInputTypeDef](#autotuneoptionsinputtypedef)
  - [CancelElasticsearchServiceSoftwareUpdateResponseTypeDef](#cancelelasticsearchservicesoftwareupdateresponsetypedef)
  - [CreateElasticsearchDomainResponseTypeDef](#createelasticsearchdomainresponsetypedef)
  - [CreateOutboundCrossClusterSearchConnectionResponseTypeDef](#createoutboundcrossclustersearchconnectionresponsetypedef)
  - [CreatePackageResponseTypeDef](#createpackageresponsetypedef)
  - [DeleteElasticsearchDomainResponseTypeDef](#deleteelasticsearchdomainresponsetypedef)
  - [DeleteInboundCrossClusterSearchConnectionResponseTypeDef](#deleteinboundcrossclustersearchconnectionresponsetypedef)
  - [DeleteOutboundCrossClusterSearchConnectionResponseTypeDef](#deleteoutboundcrossclustersearchconnectionresponsetypedef)
  - [DeletePackageResponseTypeDef](#deletepackageresponsetypedef)
  - [DescribeDomainAutoTunesResponseTypeDef](#describedomainautotunesresponsetypedef)
  - [DescribeElasticsearchDomainConfigResponseTypeDef](#describeelasticsearchdomainconfigresponsetypedef)
  - [DescribeElasticsearchDomainResponseTypeDef](#describeelasticsearchdomainresponsetypedef)
  - [DescribeElasticsearchDomainsResponseTypeDef](#describeelasticsearchdomainsresponsetypedef)
  - [DescribeElasticsearchInstanceTypeLimitsResponseTypeDef](#describeelasticsearchinstancetypelimitsresponsetypedef)
  - [DescribeInboundCrossClusterSearchConnectionsResponseTypeDef](#describeinboundcrossclustersearchconnectionsresponsetypedef)
  - [DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef](#describeoutboundcrossclustersearchconnectionsresponsetypedef)
  - [DescribePackagesFilterTypeDef](#describepackagesfiltertypedef)
  - [DescribePackagesResponseTypeDef](#describepackagesresponsetypedef)
  - [DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef](#describereservedelasticsearchinstanceofferingsresponsetypedef)
  - [DescribeReservedElasticsearchInstancesResponseTypeDef](#describereservedelasticsearchinstancesresponsetypedef)
  - [DissociatePackageResponseTypeDef](#dissociatepackageresponsetypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetCompatibleElasticsearchVersionsResponseTypeDef](#getcompatibleelasticsearchversionsresponsetypedef)
  - [GetPackageVersionHistoryResponseTypeDef](#getpackageversionhistoryresponsetypedef)
  - [GetUpgradeHistoryResponseTypeDef](#getupgradehistoryresponsetypedef)
  - [GetUpgradeStatusResponseTypeDef](#getupgradestatusresponsetypedef)
  - [ListDomainNamesResponseTypeDef](#listdomainnamesresponsetypedef)
  - [ListDomainsForPackageResponseTypeDef](#listdomainsforpackageresponsetypedef)
  - [ListElasticsearchInstanceTypesResponseTypeDef](#listelasticsearchinstancetypesresponsetypedef)
  - [ListElasticsearchVersionsResponseTypeDef](#listelasticsearchversionsresponsetypedef)
  - [ListPackagesForDomainResponseTypeDef](#listpackagesfordomainresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [PackageSourceTypeDef](#packagesourcetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef](#purchasereservedelasticsearchinstanceofferingresponsetypedef)
  - [RejectInboundCrossClusterSearchConnectionResponseTypeDef](#rejectinboundcrossclustersearchconnectionresponsetypedef)
  - [StartElasticsearchServiceSoftwareUpdateResponseTypeDef](#startelasticsearchservicesoftwareupdateresponsetypedef)
  - [UpdateElasticsearchDomainConfigResponseTypeDef](#updateelasticsearchdomainconfigresponsetypedef)
  - [UpdatePackageResponseTypeDef](#updatepackageresponsetypedef)
  - [UpgradeElasticsearchDomainResponseTypeDef](#upgradeelasticsearchdomainresponsetypedef)
  - [VPCOptionsTypeDef](#vpcoptionstypedef)

## AccessPoliciesStatusTypeDef

```python
from mypy_boto3_es.type_defs import AccessPoliciesStatusTypeDef
```


Required fields:
- `Options`: `str`
- `Status`: `"OptionStatusTypeDef"`




## AdditionalLimitTypeDef

```python
from mypy_boto3_es.type_defs import AdditionalLimitTypeDef
```




Optional fields:
- `LimitName`: `str`
- `LimitValues`: `List[str]`


## AdvancedOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import AdvancedOptionsStatusTypeDef
```


Required fields:
- `Options`: `Dict[str, str]`
- `Status`: `"OptionStatusTypeDef"`




## AdvancedSecurityOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import AdvancedSecurityOptionsStatusTypeDef
```


Required fields:
- `Options`: `"AdvancedSecurityOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## AdvancedSecurityOptionsTypeDef

```python
from mypy_boto3_es.type_defs import AdvancedSecurityOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `InternalUserDatabaseEnabled`: `bool`
- `SAMLOptions`: `"SAMLOptionsOutputTypeDef"`


## AutoTuneDetailsTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneDetailsTypeDef
```




Optional fields:
- `ScheduledAutoTuneDetails`: `"ScheduledAutoTuneDetailsTypeDef"`


## AutoTuneMaintenanceScheduleTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneMaintenanceScheduleTypeDef
```




Optional fields:
- `StartAt`: `datetime`
- `Duration`: `"DurationTypeDef"`
- `CronExpressionForRecurrence`: `str`


## AutoTuneOptionsOutputTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneOptionsOutputTypeDef
```




Optional fields:
- `State`: `AutoTuneState`
- `ErrorMessage`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## AutoTuneOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneOptionsStatusTypeDef
```




Optional fields:
- `Options`: `"AutoTuneOptionsTypeDef"`
- `Status`: `"AutoTuneStatusTypeDef"`


## AutoTuneOptionsTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneOptionsTypeDef
```




Optional fields:
- `DesiredState`: `AutoTuneDesiredState`
- `RollbackOnDisable`: `RollbackOnDisable`
- `MaintenanceSchedules`: `List["AutoTuneMaintenanceScheduleTypeDef"]`


## AutoTuneStatusTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneStatusTypeDef
```


Required fields:
- `CreationDate`: `datetime`
- `UpdateDate`: `datetime`
- `State`: `AutoTuneState`



Optional fields:
- `UpdateVersion`: `int`
- `ErrorMessage`: `str`
- `PendingDeletion`: `bool`


## AutoTuneTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneTypeDef
```




Optional fields:
- `AutoTuneType`: `AutoTuneType`
- `AutoTuneDetails`: `"AutoTuneDetailsTypeDef"`


## CognitoOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import CognitoOptionsStatusTypeDef
```


Required fields:
- `Options`: `"CognitoOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## CognitoOptionsTypeDef

```python
from mypy_boto3_es.type_defs import CognitoOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `UserPoolId`: `str`
- `IdentityPoolId`: `str`
- `RoleArn`: `str`


## CompatibleVersionsMapTypeDef

```python
from mypy_boto3_es.type_defs import CompatibleVersionsMapTypeDef
```




Optional fields:
- `SourceVersion`: `str`
- `TargetVersions`: `List[str]`


## DomainEndpointOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import DomainEndpointOptionsStatusTypeDef
```


Required fields:
- `Options`: `"DomainEndpointOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## DomainEndpointOptionsTypeDef

```python
from mypy_boto3_es.type_defs import DomainEndpointOptionsTypeDef
```




Optional fields:
- `EnforceHTTPS`: `bool`
- `TLSSecurityPolicy`: `TLSSecurityPolicy`
- `CustomEndpointEnabled`: `bool`
- `CustomEndpoint`: `str`
- `CustomEndpointCertificateArn`: `str`


## DomainInfoTypeDef

```python
from mypy_boto3_es.type_defs import DomainInfoTypeDef
```




Optional fields:
- `DomainName`: `str`


## DomainInformationTypeDef

```python
from mypy_boto3_es.type_defs import DomainInformationTypeDef
```


Required fields:
- `DomainName`: `str`



Optional fields:
- `OwnerId`: `str`
- `Region`: `str`


## DomainPackageDetailsTypeDef

```python
from mypy_boto3_es.type_defs import DomainPackageDetailsTypeDef
```




Optional fields:
- `PackageID`: `str`
- `PackageName`: `str`
- `PackageType`: `PackageType`
- `LastUpdated`: `datetime`
- `DomainName`: `str`
- `DomainPackageStatus`: `DomainPackageStatus`
- `PackageVersion`: `str`
- `ReferencePath`: `str`
- `ErrorDetails`: `"ErrorDetailsTypeDef"`


## DurationTypeDef

```python
from mypy_boto3_es.type_defs import DurationTypeDef
```




Optional fields:
- `Value`: `int`
- `Unit`: `TimeUnit`


## EBSOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import EBSOptionsStatusTypeDef
```


Required fields:
- `Options`: `"EBSOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## EBSOptionsTypeDef

```python
from mypy_boto3_es.type_defs import EBSOptionsTypeDef
```




Optional fields:
- `EBSEnabled`: `bool`
- `VolumeType`: `VolumeType`
- `VolumeSize`: `int`
- `Iops`: `int`


## ElasticsearchClusterConfigStatusTypeDef

```python
from mypy_boto3_es.type_defs import ElasticsearchClusterConfigStatusTypeDef
```


Required fields:
- `Options`: `"ElasticsearchClusterConfigTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## ElasticsearchClusterConfigTypeDef

```python
from mypy_boto3_es.type_defs import ElasticsearchClusterConfigTypeDef
```




Optional fields:
- `InstanceType`: `ESPartitionInstanceType`
- `InstanceCount`: `int`
- `DedicatedMasterEnabled`: `bool`
- `ZoneAwarenessEnabled`: `bool`
- `ZoneAwarenessConfig`: `"ZoneAwarenessConfigTypeDef"`
- `DedicatedMasterType`: `ESPartitionInstanceType`
- `DedicatedMasterCount`: `int`
- `WarmEnabled`: `bool`
- `WarmType`: `ESWarmPartitionInstanceType`
- `WarmCount`: `int`


## ElasticsearchDomainConfigTypeDef

```python
from mypy_boto3_es.type_defs import ElasticsearchDomainConfigTypeDef
```




Optional fields:
- `ElasticsearchVersion`: `"ElasticsearchVersionStatusTypeDef"`
- `ElasticsearchClusterConfig`: `"ElasticsearchClusterConfigStatusTypeDef"`
- `EBSOptions`: `"EBSOptionsStatusTypeDef"`
- `AccessPolicies`: `"AccessPoliciesStatusTypeDef"`
- `SnapshotOptions`: `"SnapshotOptionsStatusTypeDef"`
- `VPCOptions`: `"VPCDerivedInfoStatusTypeDef"`
- `CognitoOptions`: `"CognitoOptionsStatusTypeDef"`
- `EncryptionAtRestOptions`: `"EncryptionAtRestOptionsStatusTypeDef"`
- `NodeToNodeEncryptionOptions`: `"NodeToNodeEncryptionOptionsStatusTypeDef"`
- `AdvancedOptions`: `"AdvancedOptionsStatusTypeDef"`
- `LogPublishingOptions`: `"LogPublishingOptionsStatusTypeDef"`
- `DomainEndpointOptions`: `"DomainEndpointOptionsStatusTypeDef"`
- `AdvancedSecurityOptions`: `"AdvancedSecurityOptionsStatusTypeDef"`
- `AutoTuneOptions`: `"AutoTuneOptionsStatusTypeDef"`


## ElasticsearchDomainStatusTypeDef

```python
from mypy_boto3_es.type_defs import ElasticsearchDomainStatusTypeDef
```


Required fields:
- `DomainId`: `str`
- `DomainName`: `str`
- `ARN`: `str`
- `ElasticsearchClusterConfig`: `"ElasticsearchClusterConfigTypeDef"`



Optional fields:
- `Created`: `bool`
- `Deleted`: `bool`
- `Endpoint`: `str`
- `Endpoints`: `Dict[str, str]`
- `Processing`: `bool`
- `UpgradeProcessing`: `bool`
- `ElasticsearchVersion`: `str`
- `EBSOptions`: `"EBSOptionsTypeDef"`
- `AccessPolicies`: `str`
- `SnapshotOptions`: `"SnapshotOptionsTypeDef"`
- `VPCOptions`: `"VPCDerivedInfoTypeDef"`
- `CognitoOptions`: `"CognitoOptionsTypeDef"`
- `EncryptionAtRestOptions`: `"EncryptionAtRestOptionsTypeDef"`
- `NodeToNodeEncryptionOptions`: `"NodeToNodeEncryptionOptionsTypeDef"`
- `AdvancedOptions`: `Dict[str, str]`
- `LogPublishingOptions`: `Dict[LogType, "LogPublishingOptionTypeDef"]`
- `ServiceSoftwareOptions`: `"ServiceSoftwareOptionsTypeDef"`
- `DomainEndpointOptions`: `"DomainEndpointOptionsTypeDef"`
- `AdvancedSecurityOptions`: `"AdvancedSecurityOptionsTypeDef"`
- `AutoTuneOptions`: `"AutoTuneOptionsOutputTypeDef"`


## ElasticsearchVersionStatusTypeDef

```python
from mypy_boto3_es.type_defs import ElasticsearchVersionStatusTypeDef
```


Required fields:
- `Options`: `str`
- `Status`: `"OptionStatusTypeDef"`




## EncryptionAtRestOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import EncryptionAtRestOptionsStatusTypeDef
```


Required fields:
- `Options`: `"EncryptionAtRestOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## EncryptionAtRestOptionsTypeDef

```python
from mypy_boto3_es.type_defs import EncryptionAtRestOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `KmsKeyId`: `str`


## ErrorDetailsTypeDef

```python
from mypy_boto3_es.type_defs import ErrorDetailsTypeDef
```




Optional fields:
- `ErrorType`: `str`
- `ErrorMessage`: `str`


## InboundCrossClusterSearchConnectionStatusTypeDef

```python
from mypy_boto3_es.type_defs import InboundCrossClusterSearchConnectionStatusTypeDef
```




Optional fields:
- `StatusCode`: `InboundCrossClusterSearchConnectionStatusCode`
- `Message`: `str`


## InboundCrossClusterSearchConnectionTypeDef

```python
from mypy_boto3_es.type_defs import InboundCrossClusterSearchConnectionTypeDef
```




Optional fields:
- `SourceDomainInfo`: `"DomainInformationTypeDef"`
- `DestinationDomainInfo`: `"DomainInformationTypeDef"`
- `CrossClusterSearchConnectionId`: `str`
- `ConnectionStatus`: `"InboundCrossClusterSearchConnectionStatusTypeDef"`


## InstanceCountLimitsTypeDef

```python
from mypy_boto3_es.type_defs import InstanceCountLimitsTypeDef
```




Optional fields:
- `MinimumInstanceCount`: `int`
- `MaximumInstanceCount`: `int`


## InstanceLimitsTypeDef

```python
from mypy_boto3_es.type_defs import InstanceLimitsTypeDef
```




Optional fields:
- `InstanceCountLimits`: `"InstanceCountLimitsTypeDef"`


## LimitsTypeDef

```python
from mypy_boto3_es.type_defs import LimitsTypeDef
```




Optional fields:
- `StorageTypes`: `List["StorageTypeTypeDef"]`
- `InstanceLimits`: `"InstanceLimitsTypeDef"`
- `AdditionalLimits`: `List["AdditionalLimitTypeDef"]`


## LogPublishingOptionTypeDef

```python
from mypy_boto3_es.type_defs import LogPublishingOptionTypeDef
```




Optional fields:
- `CloudWatchLogsLogGroupArn`: `str`
- `Enabled`: `bool`


## LogPublishingOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import LogPublishingOptionsStatusTypeDef
```




Optional fields:
- `Options`: `Dict[LogType, "LogPublishingOptionTypeDef"]`
- `Status`: `"OptionStatusTypeDef"`


## MasterUserOptionsTypeDef

```python
from mypy_boto3_es.type_defs import MasterUserOptionsTypeDef
```




Optional fields:
- `MasterUserARN`: `str`
- `MasterUserName`: `str`
- `MasterUserPassword`: `str`


## NodeToNodeEncryptionOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import NodeToNodeEncryptionOptionsStatusTypeDef
```


Required fields:
- `Options`: `"NodeToNodeEncryptionOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## NodeToNodeEncryptionOptionsTypeDef

```python
from mypy_boto3_es.type_defs import NodeToNodeEncryptionOptionsTypeDef
```




Optional fields:
- `Enabled`: `bool`


## OptionStatusTypeDef

```python
from mypy_boto3_es.type_defs import OptionStatusTypeDef
```


Required fields:
- `CreationDate`: `datetime`
- `UpdateDate`: `datetime`
- `State`: `OptionState`



Optional fields:
- `UpdateVersion`: `int`
- `PendingDeletion`: `bool`


## OutboundCrossClusterSearchConnectionStatusTypeDef

```python
from mypy_boto3_es.type_defs import OutboundCrossClusterSearchConnectionStatusTypeDef
```




Optional fields:
- `StatusCode`: `OutboundCrossClusterSearchConnectionStatusCode`
- `Message`: `str`


## OutboundCrossClusterSearchConnectionTypeDef

```python
from mypy_boto3_es.type_defs import OutboundCrossClusterSearchConnectionTypeDef
```




Optional fields:
- `SourceDomainInfo`: `"DomainInformationTypeDef"`
- `DestinationDomainInfo`: `"DomainInformationTypeDef"`
- `CrossClusterSearchConnectionId`: `str`
- `ConnectionAlias`: `str`
- `ConnectionStatus`: `"OutboundCrossClusterSearchConnectionStatusTypeDef"`


## PackageDetailsTypeDef

```python
from mypy_boto3_es.type_defs import PackageDetailsTypeDef
```




Optional fields:
- `PackageID`: `str`
- `PackageName`: `str`
- `PackageType`: `PackageType`
- `PackageDescription`: `str`
- `PackageStatus`: `PackageStatus`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `AvailablePackageVersion`: `str`
- `ErrorDetails`: `"ErrorDetailsTypeDef"`


## PackageVersionHistoryTypeDef

```python
from mypy_boto3_es.type_defs import PackageVersionHistoryTypeDef
```




Optional fields:
- `PackageVersion`: `str`
- `CommitMessage`: `str`
- `CreatedAt`: `datetime`


## RecurringChargeTypeDef

```python
from mypy_boto3_es.type_defs import RecurringChargeTypeDef
```




Optional fields:
- `RecurringChargeAmount`: `float`
- `RecurringChargeFrequency`: `str`


## ReservedElasticsearchInstanceOfferingTypeDef

```python
from mypy_boto3_es.type_defs import ReservedElasticsearchInstanceOfferingTypeDef
```




Optional fields:
- `ReservedElasticsearchInstanceOfferingId`: `str`
- `ElasticsearchInstanceType`: `ESPartitionInstanceType`
- `Duration`: `int`
- `FixedPrice`: `float`
- `UsagePrice`: `float`
- `CurrencyCode`: `str`
- `PaymentOption`: `ReservedElasticsearchInstancePaymentOption`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`


## ReservedElasticsearchInstanceTypeDef

```python
from mypy_boto3_es.type_defs import ReservedElasticsearchInstanceTypeDef
```




Optional fields:
- `ReservationName`: `str`
- `ReservedElasticsearchInstanceId`: `str`
- `ReservedElasticsearchInstanceOfferingId`: `str`
- `ElasticsearchInstanceType`: `ESPartitionInstanceType`
- `StartTime`: `datetime`
- `Duration`: `int`
- `FixedPrice`: `float`
- `UsagePrice`: `float`
- `CurrencyCode`: `str`
- `ElasticsearchInstanceCount`: `int`
- `State`: `str`
- `PaymentOption`: `ReservedElasticsearchInstancePaymentOption`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`


## ResponseMetadata

```python
from mypy_boto3_es.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SAMLIdpTypeDef

```python
from mypy_boto3_es.type_defs import SAMLIdpTypeDef
```


Required fields:
- `MetadataContent`: `str`
- `EntityId`: `str`




## SAMLOptionsInputTypeDef

```python
from mypy_boto3_es.type_defs import SAMLOptionsInputTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `Idp`: `"SAMLIdpTypeDef"`
- `MasterUserName`: `str`
- `MasterBackendRole`: `str`
- `SubjectKey`: `str`
- `RolesKey`: `str`
- `SessionTimeoutMinutes`: `int`


## SAMLOptionsOutputTypeDef

```python
from mypy_boto3_es.type_defs import SAMLOptionsOutputTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `Idp`: `"SAMLIdpTypeDef"`
- `SubjectKey`: `str`
- `RolesKey`: `str`
- `SessionTimeoutMinutes`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## ScheduledAutoTuneDetailsTypeDef

```python
from mypy_boto3_es.type_defs import ScheduledAutoTuneDetailsTypeDef
```




Optional fields:
- `Date`: `datetime`
- `ActionType`: `ScheduledAutoTuneActionType`
- `Action`: `str`
- `Severity`: `ScheduledAutoTuneSeverityType`


## ServiceSoftwareOptionsTypeDef

```python
from mypy_boto3_es.type_defs import ServiceSoftwareOptionsTypeDef
```




Optional fields:
- `CurrentVersion`: `str`
- `NewVersion`: `str`
- `UpdateAvailable`: `bool`
- `Cancellable`: `bool`
- `UpdateStatus`: `DeploymentStatus`
- `Description`: `str`
- `AutomatedUpdateDate`: `datetime`
- `OptionalDeployment`: `bool`


## SnapshotOptionsStatusTypeDef

```python
from mypy_boto3_es.type_defs import SnapshotOptionsStatusTypeDef
```


Required fields:
- `Options`: `"SnapshotOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## SnapshotOptionsTypeDef

```python
from mypy_boto3_es.type_defs import SnapshotOptionsTypeDef
```




Optional fields:
- `AutomatedSnapshotStartHour`: `int`


## StorageTypeLimitTypeDef

```python
from mypy_boto3_es.type_defs import StorageTypeLimitTypeDef
```




Optional fields:
- `LimitName`: `str`
- `LimitValues`: `List[str]`


## StorageTypeTypeDef

```python
from mypy_boto3_es.type_defs import StorageTypeTypeDef
```




Optional fields:
- `StorageTypeName`: `str`
- `StorageSubTypeName`: `str`
- `StorageTypeLimits`: `List["StorageTypeLimitTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_es.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UpgradeHistoryTypeDef

```python
from mypy_boto3_es.type_defs import UpgradeHistoryTypeDef
```




Optional fields:
- `UpgradeName`: `str`
- `StartTimestamp`: `datetime`
- `UpgradeStatus`: `UpgradeStatus`
- `StepsList`: `List["UpgradeStepItemTypeDef"]`


## UpgradeStepItemTypeDef

```python
from mypy_boto3_es.type_defs import UpgradeStepItemTypeDef
```




Optional fields:
- `UpgradeStep`: `UpgradeStep`
- `UpgradeStepStatus`: `UpgradeStatus`
- `Issues`: `List[str]`
- `ProgressPercent`: `float`


## VPCDerivedInfoStatusTypeDef

```python
from mypy_boto3_es.type_defs import VPCDerivedInfoStatusTypeDef
```


Required fields:
- `Options`: `"VPCDerivedInfoTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## VPCDerivedInfoTypeDef

```python
from mypy_boto3_es.type_defs import VPCDerivedInfoTypeDef
```




Optional fields:
- `VPCId`: `str`
- `SubnetIds`: `List[str]`
- `AvailabilityZones`: `List[str]`
- `SecurityGroupIds`: `List[str]`


## ZoneAwarenessConfigTypeDef

```python
from mypy_boto3_es.type_defs import ZoneAwarenessConfigTypeDef
```




Optional fields:
- `AvailabilityZoneCount`: `int`


## AcceptInboundCrossClusterSearchConnectionResponseTypeDef

```python
from mypy_boto3_es.type_defs import AcceptInboundCrossClusterSearchConnectionResponseTypeDef
```




Optional fields:
- `CrossClusterSearchConnection`: `"InboundCrossClusterSearchConnectionTypeDef"`


## AdvancedSecurityOptionsInputTypeDef

```python
from mypy_boto3_es.type_defs import AdvancedSecurityOptionsInputTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `InternalUserDatabaseEnabled`: `bool`
- `MasterUserOptions`: `"MasterUserOptionsTypeDef"`
- `SAMLOptions`: `"SAMLOptionsInputTypeDef"`


## AssociatePackageResponseTypeDef

```python
from mypy_boto3_es.type_defs import AssociatePackageResponseTypeDef
```




Optional fields:
- `DomainPackageDetails`: `"DomainPackageDetailsTypeDef"`


## AutoTuneOptionsInputTypeDef

```python
from mypy_boto3_es.type_defs import AutoTuneOptionsInputTypeDef
```




Optional fields:
- `DesiredState`: `AutoTuneDesiredState`
- `MaintenanceSchedules`: `List["AutoTuneMaintenanceScheduleTypeDef"]`


## CancelElasticsearchServiceSoftwareUpdateResponseTypeDef

```python
from mypy_boto3_es.type_defs import CancelElasticsearchServiceSoftwareUpdateResponseTypeDef
```




Optional fields:
- `ServiceSoftwareOptions`: `"ServiceSoftwareOptionsTypeDef"`


## CreateElasticsearchDomainResponseTypeDef

```python
from mypy_boto3_es.type_defs import CreateElasticsearchDomainResponseTypeDef
```




Optional fields:
- `DomainStatus`: `"ElasticsearchDomainStatusTypeDef"`


## CreateOutboundCrossClusterSearchConnectionResponseTypeDef

```python
from mypy_boto3_es.type_defs import CreateOutboundCrossClusterSearchConnectionResponseTypeDef
```




Optional fields:
- `SourceDomainInfo`: `"DomainInformationTypeDef"`
- `DestinationDomainInfo`: `"DomainInformationTypeDef"`
- `ConnectionAlias`: `str`
- `ConnectionStatus`: `"OutboundCrossClusterSearchConnectionStatusTypeDef"`
- `CrossClusterSearchConnectionId`: `str`


## CreatePackageResponseTypeDef

```python
from mypy_boto3_es.type_defs import CreatePackageResponseTypeDef
```




Optional fields:
- `PackageDetails`: `"PackageDetailsTypeDef"`


## DeleteElasticsearchDomainResponseTypeDef

```python
from mypy_boto3_es.type_defs import DeleteElasticsearchDomainResponseTypeDef
```




Optional fields:
- `DomainStatus`: `"ElasticsearchDomainStatusTypeDef"`


## DeleteInboundCrossClusterSearchConnectionResponseTypeDef

```python
from mypy_boto3_es.type_defs import DeleteInboundCrossClusterSearchConnectionResponseTypeDef
```




Optional fields:
- `CrossClusterSearchConnection`: `"InboundCrossClusterSearchConnectionTypeDef"`


## DeleteOutboundCrossClusterSearchConnectionResponseTypeDef

```python
from mypy_boto3_es.type_defs import DeleteOutboundCrossClusterSearchConnectionResponseTypeDef
```




Optional fields:
- `CrossClusterSearchConnection`: `"OutboundCrossClusterSearchConnectionTypeDef"`


## DeletePackageResponseTypeDef

```python
from mypy_boto3_es.type_defs import DeletePackageResponseTypeDef
```




Optional fields:
- `PackageDetails`: `"PackageDetailsTypeDef"`


## DescribeDomainAutoTunesResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeDomainAutoTunesResponseTypeDef
```




Optional fields:
- `AutoTunes`: `List["AutoTuneTypeDef"]`
- `NextToken`: `str`


## DescribeElasticsearchDomainConfigResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeElasticsearchDomainConfigResponseTypeDef
```


Required fields:
- `DomainConfig`: `"ElasticsearchDomainConfigTypeDef"`




## DescribeElasticsearchDomainResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeElasticsearchDomainResponseTypeDef
```


Required fields:
- `DomainStatus`: `"ElasticsearchDomainStatusTypeDef"`




## DescribeElasticsearchDomainsResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeElasticsearchDomainsResponseTypeDef
```


Required fields:
- `DomainStatusList`: `List["ElasticsearchDomainStatusTypeDef"]`




## DescribeElasticsearchInstanceTypeLimitsResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeElasticsearchInstanceTypeLimitsResponseTypeDef
```




Optional fields:
- `LimitsByRole`: `Dict[str, "LimitsTypeDef"]`


## DescribeInboundCrossClusterSearchConnectionsResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeInboundCrossClusterSearchConnectionsResponseTypeDef
```




Optional fields:
- `CrossClusterSearchConnections`: `List["InboundCrossClusterSearchConnectionTypeDef"]`
- `NextToken`: `str`


## DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef
```




Optional fields:
- `CrossClusterSearchConnections`: `List["OutboundCrossClusterSearchConnectionTypeDef"]`
- `NextToken`: `str`


## DescribePackagesFilterTypeDef

```python
from mypy_boto3_es.type_defs import DescribePackagesFilterTypeDef
```




Optional fields:
- `Name`: `DescribePackagesFilterName`
- `Value`: `List[str]`


## DescribePackagesResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribePackagesResponseTypeDef
```




Optional fields:
- `PackageDetailsList`: `List["PackageDetailsTypeDef"]`
- `NextToken`: `str`


## DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ReservedElasticsearchInstanceOfferings`: `List["ReservedElasticsearchInstanceOfferingTypeDef"]`


## DescribeReservedElasticsearchInstancesResponseTypeDef

```python
from mypy_boto3_es.type_defs import DescribeReservedElasticsearchInstancesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ReservedElasticsearchInstances`: `List["ReservedElasticsearchInstanceTypeDef"]`


## DissociatePackageResponseTypeDef

```python
from mypy_boto3_es.type_defs import DissociatePackageResponseTypeDef
```




Optional fields:
- `DomainPackageDetails`: `"DomainPackageDetailsTypeDef"`


## FilterTypeDef

```python
from mypy_boto3_es.type_defs import FilterTypeDef
```




Optional fields:
- `Name`: `str`
- `Values`: `List[str]`


## GetCompatibleElasticsearchVersionsResponseTypeDef

```python
from mypy_boto3_es.type_defs import GetCompatibleElasticsearchVersionsResponseTypeDef
```




Optional fields:
- `CompatibleElasticsearchVersions`: `List["CompatibleVersionsMapTypeDef"]`


## GetPackageVersionHistoryResponseTypeDef

```python
from mypy_boto3_es.type_defs import GetPackageVersionHistoryResponseTypeDef
```




Optional fields:
- `PackageID`: `str`
- `PackageVersionHistoryList`: `List["PackageVersionHistoryTypeDef"]`
- `NextToken`: `str`


## GetUpgradeHistoryResponseTypeDef

```python
from mypy_boto3_es.type_defs import GetUpgradeHistoryResponseTypeDef
```




Optional fields:
- `UpgradeHistories`: `List["UpgradeHistoryTypeDef"]`
- `NextToken`: `str`


## GetUpgradeStatusResponseTypeDef

```python
from mypy_boto3_es.type_defs import GetUpgradeStatusResponseTypeDef
```




Optional fields:
- `UpgradeStep`: `UpgradeStep`
- `StepStatus`: `UpgradeStatus`
- `UpgradeName`: `str`


## ListDomainNamesResponseTypeDef

```python
from mypy_boto3_es.type_defs import ListDomainNamesResponseTypeDef
```




Optional fields:
- `DomainNames`: `List["DomainInfoTypeDef"]`


## ListDomainsForPackageResponseTypeDef

```python
from mypy_boto3_es.type_defs import ListDomainsForPackageResponseTypeDef
```




Optional fields:
- `DomainPackageDetailsList`: `List["DomainPackageDetailsTypeDef"]`
- `NextToken`: `str`


## ListElasticsearchInstanceTypesResponseTypeDef

```python
from mypy_boto3_es.type_defs import ListElasticsearchInstanceTypesResponseTypeDef
```




Optional fields:
- `ElasticsearchInstanceTypes`: `List[ESPartitionInstanceType]`
- `NextToken`: `str`


## ListElasticsearchVersionsResponseTypeDef

```python
from mypy_boto3_es.type_defs import ListElasticsearchVersionsResponseTypeDef
```




Optional fields:
- `ElasticsearchVersions`: `List[str]`
- `NextToken`: `str`


## ListPackagesForDomainResponseTypeDef

```python
from mypy_boto3_es.type_defs import ListPackagesForDomainResponseTypeDef
```




Optional fields:
- `DomainPackageDetailsList`: `List["DomainPackageDetailsTypeDef"]`
- `NextToken`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_es.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `TagList`: `List["TagTypeDef"]`


## PackageSourceTypeDef

```python
from mypy_boto3_es.type_defs import PackageSourceTypeDef
```




Optional fields:
- `S3BucketName`: `str`
- `S3Key`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_es.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef

```python
from mypy_boto3_es.type_defs import PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef
```




Optional fields:
- `ReservedElasticsearchInstanceId`: `str`
- `ReservationName`: `str`


## RejectInboundCrossClusterSearchConnectionResponseTypeDef

```python
from mypy_boto3_es.type_defs import RejectInboundCrossClusterSearchConnectionResponseTypeDef
```




Optional fields:
- `CrossClusterSearchConnection`: `"InboundCrossClusterSearchConnectionTypeDef"`


## StartElasticsearchServiceSoftwareUpdateResponseTypeDef

```python
from mypy_boto3_es.type_defs import StartElasticsearchServiceSoftwareUpdateResponseTypeDef
```




Optional fields:
- `ServiceSoftwareOptions`: `"ServiceSoftwareOptionsTypeDef"`


## UpdateElasticsearchDomainConfigResponseTypeDef

```python
from mypy_boto3_es.type_defs import UpdateElasticsearchDomainConfigResponseTypeDef
```


Required fields:
- `DomainConfig`: `"ElasticsearchDomainConfigTypeDef"`




## UpdatePackageResponseTypeDef

```python
from mypy_boto3_es.type_defs import UpdatePackageResponseTypeDef
```




Optional fields:
- `PackageDetails`: `"PackageDetailsTypeDef"`


## UpgradeElasticsearchDomainResponseTypeDef

```python
from mypy_boto3_es.type_defs import UpgradeElasticsearchDomainResponseTypeDef
```




Optional fields:
- `DomainName`: `str`
- `TargetVersion`: `str`
- `PerformCheckOnly`: `bool`


## VPCOptionsTypeDef

```python
from mypy_boto3_es.type_defs import VPCOptionsTypeDef
```




Optional fields:
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`

