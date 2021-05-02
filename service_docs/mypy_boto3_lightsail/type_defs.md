# Structures for boto3 Lightsail module

> [Index](../index.md) > [Lightsail](./index.md) > Structures

Auto-generated documentation for [Lightsail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail)
type annotations stubs module [mypy_boto3_lightsail](https://pypi.org/project/mypy-boto3-lightsail/).

- [Structures for boto3 Lightsail module](#structures-for-boto3-lightsail-module)
  - [AddOnRequestTypeDef](#addonrequesttypedef)
  - [AddOnTypeDef](#addontypedef)
  - [AlarmTypeDef](#alarmtypedef)
  - [AllocateStaticIpResultTypeDef](#allocatestaticipresulttypedef)
  - [AttachCertificateToDistributionResultTypeDef](#attachcertificatetodistributionresulttypedef)
  - [AttachDiskResultTypeDef](#attachdiskresulttypedef)
  - [AttachInstancesToLoadBalancerResultTypeDef](#attachinstancestoloadbalancerresulttypedef)
  - [AttachLoadBalancerTlsCertificateResultTypeDef](#attachloadbalancertlscertificateresulttypedef)
  - [AttachStaticIpResultTypeDef](#attachstaticipresulttypedef)
  - [AttachedDiskTypeDef](#attacheddisktypedef)
  - [AutoSnapshotAddOnRequestTypeDef](#autosnapshotaddonrequesttypedef)
  - [AutoSnapshotDetailsTypeDef](#autosnapshotdetailstypedef)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [BlueprintTypeDef](#blueprinttypedef)
  - [BundleTypeDef](#bundletypedef)
  - [CacheBehaviorPerPathTypeDef](#cachebehaviorperpathtypedef)
  - [CacheBehaviorTypeDef](#cachebehaviortypedef)
  - [CacheSettingsTypeDef](#cachesettingstypedef)
  - [CertificateSummaryTypeDef](#certificatesummarytypedef)
  - [CertificateTypeDef](#certificatetypedef)
  - [CloseInstancePublicPortsResultTypeDef](#closeinstancepublicportsresulttypedef)
  - [CloudFormationStackRecordSourceInfoTypeDef](#cloudformationstackrecordsourceinfotypedef)
  - [CloudFormationStackRecordTypeDef](#cloudformationstackrecordtypedef)
  - [ContactMethodTypeDef](#contactmethodtypedef)
  - [ContainerImageTypeDef](#containerimagetypedef)
  - [ContainerServiceDeploymentRequestTypeDef](#containerservicedeploymentrequesttypedef)
  - [ContainerServiceDeploymentTypeDef](#containerservicedeploymenttypedef)
  - [ContainerServiceEndpointTypeDef](#containerserviceendpointtypedef)
  - [ContainerServiceHealthCheckConfigTypeDef](#containerservicehealthcheckconfigtypedef)
  - [ContainerServiceLogEventTypeDef](#containerservicelogeventtypedef)
  - [ContainerServicePowerTypeDef](#containerservicepowertypedef)
  - [ContainerServiceRegistryLoginTypeDef](#containerserviceregistrylogintypedef)
  - [ContainerServiceStateDetailTypeDef](#containerservicestatedetailtypedef)
  - [ContainerServiceTypeDef](#containerservicetypedef)
  - [ContainerServicesListResultTypeDef](#containerserviceslistresulttypedef)
  - [ContainerTypeDef](#containertypedef)
  - [CookieObjectTypeDef](#cookieobjecttypedef)
  - [CopySnapshotResultTypeDef](#copysnapshotresulttypedef)
  - [CreateCertificateResultTypeDef](#createcertificateresulttypedef)
  - [CreateCloudFormationStackResultTypeDef](#createcloudformationstackresulttypedef)
  - [CreateContactMethodResultTypeDef](#createcontactmethodresulttypedef)
  - [CreateContainerServiceDeploymentResultTypeDef](#createcontainerservicedeploymentresulttypedef)
  - [CreateContainerServiceRegistryLoginResultTypeDef](#createcontainerserviceregistryloginresulttypedef)
  - [CreateContainerServiceResultTypeDef](#createcontainerserviceresulttypedef)
  - [CreateDiskFromSnapshotResultTypeDef](#creatediskfromsnapshotresulttypedef)
  - [CreateDiskResultTypeDef](#creatediskresulttypedef)
  - [CreateDiskSnapshotResultTypeDef](#createdisksnapshotresulttypedef)
  - [CreateDistributionResultTypeDef](#createdistributionresulttypedef)
  - [CreateDomainEntryResultTypeDef](#createdomainentryresulttypedef)
  - [CreateDomainResultTypeDef](#createdomainresulttypedef)
  - [CreateInstanceSnapshotResultTypeDef](#createinstancesnapshotresulttypedef)
  - [CreateInstancesFromSnapshotResultTypeDef](#createinstancesfromsnapshotresulttypedef)
  - [CreateInstancesResultTypeDef](#createinstancesresulttypedef)
  - [CreateKeyPairResultTypeDef](#createkeypairresulttypedef)
  - [CreateLoadBalancerResultTypeDef](#createloadbalancerresulttypedef)
  - [CreateLoadBalancerTlsCertificateResultTypeDef](#createloadbalancertlscertificateresulttypedef)
  - [CreateRelationalDatabaseFromSnapshotResultTypeDef](#createrelationaldatabasefromsnapshotresulttypedef)
  - [CreateRelationalDatabaseResultTypeDef](#createrelationaldatabaseresulttypedef)
  - [CreateRelationalDatabaseSnapshotResultTypeDef](#createrelationaldatabasesnapshotresulttypedef)
  - [DeleteAlarmResultTypeDef](#deletealarmresulttypedef)
  - [DeleteAutoSnapshotResultTypeDef](#deleteautosnapshotresulttypedef)
  - [DeleteCertificateResultTypeDef](#deletecertificateresulttypedef)
  - [DeleteContactMethodResultTypeDef](#deletecontactmethodresulttypedef)
  - [DeleteDiskResultTypeDef](#deletediskresulttypedef)
  - [DeleteDiskSnapshotResultTypeDef](#deletedisksnapshotresulttypedef)
  - [DeleteDistributionResultTypeDef](#deletedistributionresulttypedef)
  - [DeleteDomainEntryResultTypeDef](#deletedomainentryresulttypedef)
  - [DeleteDomainResultTypeDef](#deletedomainresulttypedef)
  - [DeleteInstanceResultTypeDef](#deleteinstanceresulttypedef)
  - [DeleteInstanceSnapshotResultTypeDef](#deleteinstancesnapshotresulttypedef)
  - [DeleteKeyPairResultTypeDef](#deletekeypairresulttypedef)
  - [DeleteKnownHostKeysResultTypeDef](#deleteknownhostkeysresulttypedef)
  - [DeleteLoadBalancerResultTypeDef](#deleteloadbalancerresulttypedef)
  - [DeleteLoadBalancerTlsCertificateResultTypeDef](#deleteloadbalancertlscertificateresulttypedef)
  - [DeleteRelationalDatabaseResultTypeDef](#deleterelationaldatabaseresulttypedef)
  - [DeleteRelationalDatabaseSnapshotResultTypeDef](#deleterelationaldatabasesnapshotresulttypedef)
  - [DestinationInfoTypeDef](#destinationinfotypedef)
  - [DetachCertificateFromDistributionResultTypeDef](#detachcertificatefromdistributionresulttypedef)
  - [DetachDiskResultTypeDef](#detachdiskresulttypedef)
  - [DetachInstancesFromLoadBalancerResultTypeDef](#detachinstancesfromloadbalancerresulttypedef)
  - [DetachStaticIpResultTypeDef](#detachstaticipresulttypedef)
  - [DisableAddOnResultTypeDef](#disableaddonresulttypedef)
  - [DiskInfoTypeDef](#diskinfotypedef)
  - [DiskMapTypeDef](#diskmaptypedef)
  - [DiskSnapshotInfoTypeDef](#disksnapshotinfotypedef)
  - [DiskSnapshotTypeDef](#disksnapshottypedef)
  - [DiskTypeDef](#disktypedef)
  - [DistributionBundleTypeDef](#distributionbundletypedef)
  - [DomainEntryTypeDef](#domainentrytypedef)
  - [DomainTypeDef](#domaintypedef)
  - [DomainValidationRecordTypeDef](#domainvalidationrecordtypedef)
  - [DownloadDefaultKeyPairResultTypeDef](#downloaddefaultkeypairresulttypedef)
  - [EnableAddOnResultTypeDef](#enableaddonresulttypedef)
  - [EndpointRequestTypeDef](#endpointrequesttypedef)
  - [ExportSnapshotRecordSourceInfoTypeDef](#exportsnapshotrecordsourceinfotypedef)
  - [ExportSnapshotRecordTypeDef](#exportsnapshotrecordtypedef)
  - [ExportSnapshotResultTypeDef](#exportsnapshotresulttypedef)
  - [GetActiveNamesResultTypeDef](#getactivenamesresulttypedef)
  - [GetAlarmsResultTypeDef](#getalarmsresulttypedef)
  - [GetAutoSnapshotsResultTypeDef](#getautosnapshotsresulttypedef)
  - [GetBlueprintsResultTypeDef](#getblueprintsresulttypedef)
  - [GetBundlesResultTypeDef](#getbundlesresulttypedef)
  - [GetCertificatesResultTypeDef](#getcertificatesresulttypedef)
  - [GetCloudFormationStackRecordsResultTypeDef](#getcloudformationstackrecordsresulttypedef)
  - [GetContactMethodsResultTypeDef](#getcontactmethodsresulttypedef)
  - [GetContainerAPIMetadataResultTypeDef](#getcontainerapimetadataresulttypedef)
  - [GetContainerImagesResultTypeDef](#getcontainerimagesresulttypedef)
  - [GetContainerLogResultTypeDef](#getcontainerlogresulttypedef)
  - [GetContainerServiceDeploymentsResultTypeDef](#getcontainerservicedeploymentsresulttypedef)
  - [GetContainerServiceMetricDataResultTypeDef](#getcontainerservicemetricdataresulttypedef)
  - [GetContainerServicePowersResultTypeDef](#getcontainerservicepowersresulttypedef)
  - [GetDiskResultTypeDef](#getdiskresulttypedef)
  - [GetDiskSnapshotResultTypeDef](#getdisksnapshotresulttypedef)
  - [GetDiskSnapshotsResultTypeDef](#getdisksnapshotsresulttypedef)
  - [GetDisksResultTypeDef](#getdisksresulttypedef)
  - [GetDistributionBundlesResultTypeDef](#getdistributionbundlesresulttypedef)
  - [GetDistributionLatestCacheResetResultTypeDef](#getdistributionlatestcacheresetresulttypedef)
  - [GetDistributionMetricDataResultTypeDef](#getdistributionmetricdataresulttypedef)
  - [GetDistributionsResultTypeDef](#getdistributionsresulttypedef)
  - [GetDomainResultTypeDef](#getdomainresulttypedef)
  - [GetDomainsResultTypeDef](#getdomainsresulttypedef)
  - [GetExportSnapshotRecordsResultTypeDef](#getexportsnapshotrecordsresulttypedef)
  - [GetInstanceAccessDetailsResultTypeDef](#getinstanceaccessdetailsresulttypedef)
  - [GetInstanceMetricDataResultTypeDef](#getinstancemetricdataresulttypedef)
  - [GetInstancePortStatesResultTypeDef](#getinstanceportstatesresulttypedef)
  - [GetInstanceResultTypeDef](#getinstanceresulttypedef)
  - [GetInstanceSnapshotResultTypeDef](#getinstancesnapshotresulttypedef)
  - [GetInstanceSnapshotsResultTypeDef](#getinstancesnapshotsresulttypedef)
  - [GetInstanceStateResultTypeDef](#getinstancestateresulttypedef)
  - [GetInstancesResultTypeDef](#getinstancesresulttypedef)
  - [GetKeyPairResultTypeDef](#getkeypairresulttypedef)
  - [GetKeyPairsResultTypeDef](#getkeypairsresulttypedef)
  - [GetLoadBalancerMetricDataResultTypeDef](#getloadbalancermetricdataresulttypedef)
  - [GetLoadBalancerResultTypeDef](#getloadbalancerresulttypedef)
  - [GetLoadBalancerTlsCertificatesResultTypeDef](#getloadbalancertlscertificatesresulttypedef)
  - [GetLoadBalancersResultTypeDef](#getloadbalancersresulttypedef)
  - [GetOperationResultTypeDef](#getoperationresulttypedef)
  - [GetOperationsForResourceResultTypeDef](#getoperationsforresourceresulttypedef)
  - [GetOperationsResultTypeDef](#getoperationsresulttypedef)
  - [GetRegionsResultTypeDef](#getregionsresulttypedef)
  - [GetRelationalDatabaseBlueprintsResultTypeDef](#getrelationaldatabaseblueprintsresulttypedef)
  - [GetRelationalDatabaseBundlesResultTypeDef](#getrelationaldatabasebundlesresulttypedef)
  - [GetRelationalDatabaseEventsResultTypeDef](#getrelationaldatabaseeventsresulttypedef)
  - [GetRelationalDatabaseLogEventsResultTypeDef](#getrelationaldatabaselogeventsresulttypedef)
  - [GetRelationalDatabaseLogStreamsResultTypeDef](#getrelationaldatabaselogstreamsresulttypedef)
  - [GetRelationalDatabaseMasterUserPasswordResultTypeDef](#getrelationaldatabasemasteruserpasswordresulttypedef)
  - [GetRelationalDatabaseMetricDataResultTypeDef](#getrelationaldatabasemetricdataresulttypedef)
  - [GetRelationalDatabaseParametersResultTypeDef](#getrelationaldatabaseparametersresulttypedef)
  - [GetRelationalDatabaseResultTypeDef](#getrelationaldatabaseresulttypedef)
  - [GetRelationalDatabaseSnapshotResultTypeDef](#getrelationaldatabasesnapshotresulttypedef)
  - [GetRelationalDatabaseSnapshotsResultTypeDef](#getrelationaldatabasesnapshotsresulttypedef)
  - [GetRelationalDatabasesResultTypeDef](#getrelationaldatabasesresulttypedef)
  - [GetStaticIpResultTypeDef](#getstaticipresulttypedef)
  - [GetStaticIpsResultTypeDef](#getstaticipsresulttypedef)
  - [HeaderObjectTypeDef](#headerobjecttypedef)
  - [HostKeyAttributesTypeDef](#hostkeyattributestypedef)
  - [ImportKeyPairResultTypeDef](#importkeypairresulttypedef)
  - [InputOriginTypeDef](#inputorigintypedef)
  - [InstanceAccessDetailsTypeDef](#instanceaccessdetailstypedef)
  - [InstanceEntryTypeDef](#instanceentrytypedef)
  - [InstanceHardwareTypeDef](#instancehardwaretypedef)
  - [InstanceHealthSummaryTypeDef](#instancehealthsummarytypedef)
  - [InstanceNetworkingTypeDef](#instancenetworkingtypedef)
  - [InstancePortInfoTypeDef](#instanceportinfotypedef)
  - [InstancePortStateTypeDef](#instanceportstatetypedef)
  - [InstanceSnapshotInfoTypeDef](#instancesnapshotinfotypedef)
  - [InstanceSnapshotTypeDef](#instancesnapshottypedef)
  - [InstanceStateTypeDef](#instancestatetypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [IsVpcPeeredResultTypeDef](#isvpcpeeredresulttypedef)
  - [KeyPairTypeDef](#keypairtypedef)
  - [LightsailDistributionTypeDef](#lightsaildistributiontypedef)
  - [LoadBalancerTlsCertificateDomainValidationOptionTypeDef](#loadbalancertlscertificatedomainvalidationoptiontypedef)
  - [LoadBalancerTlsCertificateDomainValidationRecordTypeDef](#loadbalancertlscertificatedomainvalidationrecordtypedef)
  - [LoadBalancerTlsCertificateRenewalSummaryTypeDef](#loadbalancertlscertificaterenewalsummarytypedef)
  - [LoadBalancerTlsCertificateSummaryTypeDef](#loadbalancertlscertificatesummarytypedef)
  - [LoadBalancerTlsCertificateTypeDef](#loadbalancertlscertificatetypedef)
  - [LoadBalancerTypeDef](#loadbalancertypedef)
  - [LogEventTypeDef](#logeventtypedef)
  - [MetricDatapointTypeDef](#metricdatapointtypedef)
  - [MonitoredResourceInfoTypeDef](#monitoredresourceinfotypedef)
  - [MonthlyTransferTypeDef](#monthlytransfertypedef)
  - [OpenInstancePublicPortsResultTypeDef](#openinstancepublicportsresulttypedef)
  - [OperationTypeDef](#operationtypedef)
  - [OriginTypeDef](#origintypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PasswordDataTypeDef](#passworddatatypedef)
  - [PeerVpcResultTypeDef](#peervpcresulttypedef)
  - [PendingMaintenanceActionTypeDef](#pendingmaintenanceactiontypedef)
  - [PendingModifiedRelationalDatabaseValuesTypeDef](#pendingmodifiedrelationaldatabasevaluestypedef)
  - [PortInfoTypeDef](#portinfotypedef)
  - [PutAlarmResultTypeDef](#putalarmresulttypedef)
  - [PutInstancePublicPortsResultTypeDef](#putinstancepublicportsresulttypedef)
  - [QueryStringObjectTypeDef](#querystringobjecttypedef)
  - [RebootInstanceResultTypeDef](#rebootinstanceresulttypedef)
  - [RebootRelationalDatabaseResultTypeDef](#rebootrelationaldatabaseresulttypedef)
  - [RegionTypeDef](#regiontypedef)
  - [RegisterContainerImageResultTypeDef](#registercontainerimageresulttypedef)
  - [RelationalDatabaseBlueprintTypeDef](#relationaldatabaseblueprinttypedef)
  - [RelationalDatabaseBundleTypeDef](#relationaldatabasebundletypedef)
  - [RelationalDatabaseEndpointTypeDef](#relationaldatabaseendpointtypedef)
  - [RelationalDatabaseEventTypeDef](#relationaldatabaseeventtypedef)
  - [RelationalDatabaseHardwareTypeDef](#relationaldatabasehardwaretypedef)
  - [RelationalDatabaseParameterTypeDef](#relationaldatabaseparametertypedef)
  - [RelationalDatabaseSnapshotTypeDef](#relationaldatabasesnapshottypedef)
  - [RelationalDatabaseTypeDef](#relationaldatabasetypedef)
  - [ReleaseStaticIpResultTypeDef](#releasestaticipresulttypedef)
  - [RenewalSummaryTypeDef](#renewalsummarytypedef)
  - [ResetDistributionCacheResultTypeDef](#resetdistributioncacheresulttypedef)
  - [ResourceLocationTypeDef](#resourcelocationtypedef)
  - [ResourceRecordTypeDef](#resourcerecordtypedef)
  - [SendContactMethodVerificationResultTypeDef](#sendcontactmethodverificationresulttypedef)
  - [SetIpAddressTypeResultTypeDef](#setipaddresstyperesulttypedef)
  - [StartInstanceResultTypeDef](#startinstanceresulttypedef)
  - [StartRelationalDatabaseResultTypeDef](#startrelationaldatabaseresulttypedef)
  - [StaticIpTypeDef](#staticiptypedef)
  - [StopInstanceResultTypeDef](#stopinstanceresulttypedef)
  - [StopRelationalDatabaseResultTypeDef](#stoprelationaldatabaseresulttypedef)
  - [TagResourceResultTypeDef](#tagresourceresulttypedef)
  - [TagTypeDef](#tagtypedef)
  - [TestAlarmResultTypeDef](#testalarmresulttypedef)
  - [UnpeerVpcResultTypeDef](#unpeervpcresulttypedef)
  - [UntagResourceResultTypeDef](#untagresourceresulttypedef)
  - [UpdateContainerServiceResultTypeDef](#updatecontainerserviceresulttypedef)
  - [UpdateDistributionBundleResultTypeDef](#updatedistributionbundleresulttypedef)
  - [UpdateDistributionResultTypeDef](#updatedistributionresulttypedef)
  - [UpdateDomainEntryResultTypeDef](#updatedomainentryresulttypedef)
  - [UpdateLoadBalancerAttributeResultTypeDef](#updateloadbalancerattributeresulttypedef)
  - [UpdateRelationalDatabaseParametersResultTypeDef](#updaterelationaldatabaseparametersresulttypedef)
  - [UpdateRelationalDatabaseResultTypeDef](#updaterelationaldatabaseresulttypedef)

## AddOnRequestTypeDef

```python
from mypy_boto3_lightsail.type_defs import AddOnRequestTypeDef
```


Required fields:
- `addOnType`: `Literal['AutoSnapshot']`



Optional fields:
- `autoSnapshotAddOnRequest`: `"AutoSnapshotAddOnRequestTypeDef"`


## AddOnTypeDef

```python
from mypy_boto3_lightsail.type_defs import AddOnTypeDef
```




Optional fields:
- `name`: `str`
- `status`: `str`
- `snapshotTimeOfDay`: `str`
- `nextSnapshotTimeOfDay`: `str`


## AlarmTypeDef

```python
from mypy_boto3_lightsail.type_defs import AlarmTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `supportCode`: `str`
- `monitoredResourceInfo`: `"MonitoredResourceInfoTypeDef"`
- `comparisonOperator`: `ComparisonOperator`
- `evaluationPeriods`: `int`
- `period`: `int`
- `threshold`: `float`
- `datapointsToAlarm`: `int`
- `treatMissingData`: `TreatMissingData`
- `statistic`: `MetricStatistic`
- `metricName`: `MetricName`
- `state`: `AlarmState`
- `unit`: `MetricUnit`
- `contactProtocols`: `List[ContactProtocol]`
- `notificationTriggers`: `List[AlarmState]`
- `notificationEnabled`: `bool`


## AllocateStaticIpResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import AllocateStaticIpResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## AttachCertificateToDistributionResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import AttachCertificateToDistributionResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## AttachDiskResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import AttachDiskResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## AttachInstancesToLoadBalancerResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import AttachInstancesToLoadBalancerResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## AttachLoadBalancerTlsCertificateResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import AttachLoadBalancerTlsCertificateResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## AttachStaticIpResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import AttachStaticIpResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## AttachedDiskTypeDef

```python
from mypy_boto3_lightsail.type_defs import AttachedDiskTypeDef
```




Optional fields:
- `path`: `str`
- `sizeInGb`: `int`


## AutoSnapshotAddOnRequestTypeDef

```python
from mypy_boto3_lightsail.type_defs import AutoSnapshotAddOnRequestTypeDef
```




Optional fields:
- `snapshotTimeOfDay`: `str`


## AutoSnapshotDetailsTypeDef

```python
from mypy_boto3_lightsail.type_defs import AutoSnapshotDetailsTypeDef
```




Optional fields:
- `date`: `str`
- `createdAt`: `datetime`
- `status`: `AutoSnapshotStatus`
- `fromAttachedDisks`: `List["AttachedDiskTypeDef"]`


## AvailabilityZoneTypeDef

```python
from mypy_boto3_lightsail.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `zoneName`: `str`
- `state`: `str`


## BlueprintTypeDef

```python
from mypy_boto3_lightsail.type_defs import BlueprintTypeDef
```




Optional fields:
- `blueprintId`: `str`
- `name`: `str`
- `group`: `str`
- `type`: `BlueprintType`
- `description`: `str`
- `isActive`: `bool`
- `minPower`: `int`
- `version`: `str`
- `versionCode`: `str`
- `productUrl`: `str`
- `licenseUrl`: `str`
- `platform`: `InstancePlatform`


## BundleTypeDef

```python
from mypy_boto3_lightsail.type_defs import BundleTypeDef
```




Optional fields:
- `price`: `float`
- `cpuCount`: `int`
- `diskSizeInGb`: `int`
- `bundleId`: `str`
- `instanceType`: `str`
- `isActive`: `bool`
- `name`: `str`
- `power`: `int`
- `ramSizeInGb`: `float`
- `transferPerMonthInGb`: `int`
- `supportedPlatforms`: `List[InstancePlatform]`


## CacheBehaviorPerPathTypeDef

```python
from mypy_boto3_lightsail.type_defs import CacheBehaviorPerPathTypeDef
```




Optional fields:
- `path`: `str`
- `behavior`: `BehaviorEnum`


## CacheBehaviorTypeDef

```python
from mypy_boto3_lightsail.type_defs import CacheBehaviorTypeDef
```




Optional fields:
- `behavior`: `BehaviorEnum`


## CacheSettingsTypeDef

```python
from mypy_boto3_lightsail.type_defs import CacheSettingsTypeDef
```




Optional fields:
- `defaultTTL`: `int`
- `minimumTTL`: `int`
- `maximumTTL`: `int`
- `allowedHTTPMethods`: `str`
- `cachedHTTPMethods`: `str`
- `forwardedCookies`: `"CookieObjectTypeDef"`
- `forwardedHeaders`: `"HeaderObjectTypeDef"`
- `forwardedQueryStrings`: `"QueryStringObjectTypeDef"`


## CertificateSummaryTypeDef

```python
from mypy_boto3_lightsail.type_defs import CertificateSummaryTypeDef
```




Optional fields:
- `certificateArn`: `str`
- `certificateName`: `str`
- `domainName`: `str`
- `certificateDetail`: `"CertificateTypeDef"`
- `tags`: `List["TagTypeDef"]`


## CertificateTypeDef

```python
from mypy_boto3_lightsail.type_defs import CertificateTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `domainName`: `str`
- `status`: `CertificateStatus`
- `serialNumber`: `str`
- `subjectAlternativeNames`: `List[str]`
- `domainValidationRecords`: `List["DomainValidationRecordTypeDef"]`
- `requestFailureReason`: `str`
- `inUseResourceCount`: `int`
- `keyAlgorithm`: `str`
- `createdAt`: `datetime`
- `issuedAt`: `datetime`
- `issuerCA`: `str`
- `notBefore`: `datetime`
- `notAfter`: `datetime`
- `eligibleToRenew`: `str`
- `renewalSummary`: `"RenewalSummaryTypeDef"`
- `revokedAt`: `datetime`
- `revocationReason`: `str`
- `tags`: `List["TagTypeDef"]`
- `supportCode`: `str`


## CloseInstancePublicPortsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CloseInstancePublicPortsResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## CloudFormationStackRecordSourceInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import CloudFormationStackRecordSourceInfoTypeDef
```




Optional fields:
- `resourceType`: `Literal['ExportSnapshotRecord']`
- `name`: `str`
- `arn`: `str`


## CloudFormationStackRecordTypeDef

```python
from mypy_boto3_lightsail.type_defs import CloudFormationStackRecordTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `state`: `RecordState`
- `sourceInfo`: `List["CloudFormationStackRecordSourceInfoTypeDef"]`
- `destinationInfo`: `"DestinationInfoTypeDef"`


## ContactMethodTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContactMethodTypeDef
```




Optional fields:
- `contactEndpoint`: `str`
- `status`: `ContactMethodStatus`
- `protocol`: `ContactProtocol`
- `name`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `supportCode`: `str`


## ContainerImageTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerImageTypeDef
```




Optional fields:
- `image`: `str`
- `digest`: `str`
- `createdAt`: `datetime`


## ContainerServiceDeploymentRequestTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceDeploymentRequestTypeDef
```




Optional fields:
- `containers`: `Dict[str, "ContainerTypeDef"]`
- `publicEndpoint`: `"EndpointRequestTypeDef"`


## ContainerServiceDeploymentTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceDeploymentTypeDef
```




Optional fields:
- `version`: `int`
- `state`: `ContainerServiceDeploymentState`
- `containers`: `Dict[str, "ContainerTypeDef"]`
- `publicEndpoint`: `"ContainerServiceEndpointTypeDef"`
- `createdAt`: `datetime`


## ContainerServiceEndpointTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceEndpointTypeDef
```




Optional fields:
- `containerName`: `str`
- `containerPort`: `int`
- `healthCheck`: `"ContainerServiceHealthCheckConfigTypeDef"`


## ContainerServiceHealthCheckConfigTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceHealthCheckConfigTypeDef
```




Optional fields:
- `healthyThreshold`: `int`
- `unhealthyThreshold`: `int`
- `timeoutSeconds`: `int`
- `intervalSeconds`: `int`
- `path`: `str`
- `successCodes`: `str`


## ContainerServiceLogEventTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceLogEventTypeDef
```




Optional fields:
- `createdAt`: `datetime`
- `message`: `str`


## ContainerServicePowerTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServicePowerTypeDef
```




Optional fields:
- `powerId`: `str`
- `price`: `float`
- `cpuCount`: `float`
- `ramSizeInGb`: `float`
- `name`: `str`
- `isActive`: `bool`


## ContainerServiceRegistryLoginTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceRegistryLoginTypeDef
```




Optional fields:
- `username`: `str`
- `password`: `str`
- `expiresAt`: `datetime`
- `registry`: `str`


## ContainerServiceStateDetailTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceStateDetailTypeDef
```




Optional fields:
- `code`: `ContainerServiceStateDetailCode`
- `message`: `str`


## ContainerServiceTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServiceTypeDef
```




Optional fields:
- `containerServiceName`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `power`: `ContainerServicePowerName`
- `powerId`: `str`
- `state`: `ContainerServiceState`
- `stateDetail`: `"ContainerServiceStateDetailTypeDef"`
- `scale`: `int`
- `currentDeployment`: `"ContainerServiceDeploymentTypeDef"`
- `nextDeployment`: `"ContainerServiceDeploymentTypeDef"`
- `isDisabled`: `bool`
- `principalArn`: `str`
- `privateDomainName`: `str`
- `publicDomainNames`: `Dict[str, List[str]]`
- `url`: `str`


## ContainerServicesListResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerServicesListResultTypeDef
```




Optional fields:
- `containerServices`: `List["ContainerServiceTypeDef"]`


## ContainerTypeDef

```python
from mypy_boto3_lightsail.type_defs import ContainerTypeDef
```




Optional fields:
- `image`: `str`
- `command`: `List[str]`
- `environment`: `Dict[str, str]`
- `ports`: `Dict[str, ContainerServiceProtocol]`


## CookieObjectTypeDef

```python
from mypy_boto3_lightsail.type_defs import CookieObjectTypeDef
```




Optional fields:
- `option`: `ForwardValues`
- `cookiesAllowList`: `List[str]`


## CopySnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CopySnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateCertificateResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateCertificateResultTypeDef
```




Optional fields:
- `certificate`: `"CertificateSummaryTypeDef"`
- `operations`: `List["OperationTypeDef"]`


## CreateCloudFormationStackResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateCloudFormationStackResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateContactMethodResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateContactMethodResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateContainerServiceDeploymentResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateContainerServiceDeploymentResultTypeDef
```




Optional fields:
- `containerService`: `"ContainerServiceTypeDef"`


## CreateContainerServiceRegistryLoginResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateContainerServiceRegistryLoginResultTypeDef
```




Optional fields:
- `registryLogin`: `"ContainerServiceRegistryLoginTypeDef"`


## CreateContainerServiceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateContainerServiceResultTypeDef
```




Optional fields:
- `containerService`: `"ContainerServiceTypeDef"`


## CreateDiskFromSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateDiskFromSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateDiskResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateDiskResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateDiskSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateDiskSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateDistributionResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateDistributionResultTypeDef
```




Optional fields:
- `distribution`: `"LightsailDistributionTypeDef"`
- `operation`: `"OperationTypeDef"`


## CreateDomainEntryResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateDomainEntryResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## CreateDomainResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateDomainResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## CreateInstanceSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateInstanceSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateInstancesFromSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateInstancesFromSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateInstancesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateInstancesResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateKeyPairResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateKeyPairResultTypeDef
```




Optional fields:
- `keyPair`: `"KeyPairTypeDef"`
- `publicKeyBase64`: `str`
- `privateKeyBase64`: `str`
- `operation`: `"OperationTypeDef"`


## CreateLoadBalancerResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateLoadBalancerResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateLoadBalancerTlsCertificateResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateLoadBalancerTlsCertificateResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateRelationalDatabaseFromSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateRelationalDatabaseFromSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateRelationalDatabaseResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## CreateRelationalDatabaseSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import CreateRelationalDatabaseSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteAlarmResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteAlarmResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteAutoSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteAutoSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteCertificateResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteCertificateResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteContactMethodResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteContactMethodResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteDiskResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteDiskResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteDiskSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteDiskSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteDistributionResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteDistributionResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## DeleteDomainEntryResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteDomainEntryResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## DeleteDomainResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteDomainResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## DeleteInstanceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteInstanceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteInstanceSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteInstanceSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteKeyPairResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteKeyPairResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## DeleteKnownHostKeysResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteKnownHostKeysResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteLoadBalancerResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteLoadBalancerResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteLoadBalancerTlsCertificateResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteLoadBalancerTlsCertificateResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteRelationalDatabaseResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DeleteRelationalDatabaseSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DeleteRelationalDatabaseSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DestinationInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import DestinationInfoTypeDef
```




Optional fields:
- `id`: `str`
- `service`: `str`


## DetachCertificateFromDistributionResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DetachCertificateFromDistributionResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## DetachDiskResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DetachDiskResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DetachInstancesFromLoadBalancerResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DetachInstancesFromLoadBalancerResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DetachStaticIpResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DetachStaticIpResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DisableAddOnResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DisableAddOnResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## DiskInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import DiskInfoTypeDef
```




Optional fields:
- `name`: `str`
- `path`: `str`
- `sizeInGb`: `int`
- `isSystemDisk`: `bool`


## DiskMapTypeDef

```python
from mypy_boto3_lightsail.type_defs import DiskMapTypeDef
```




Optional fields:
- `originalDiskPath`: `str`
- `newDiskName`: `str`


## DiskSnapshotInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import DiskSnapshotInfoTypeDef
```




Optional fields:
- `sizeInGb`: `int`


## DiskSnapshotTypeDef

```python
from mypy_boto3_lightsail.type_defs import DiskSnapshotTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `sizeInGb`: `int`
- `state`: `DiskSnapshotState`
- `progress`: `str`
- `fromDiskName`: `str`
- `fromDiskArn`: `str`
- `fromInstanceName`: `str`
- `fromInstanceArn`: `str`
- `isFromAutoSnapshot`: `bool`


## DiskTypeDef

```python
from mypy_boto3_lightsail.type_defs import DiskTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `addOns`: `List["AddOnTypeDef"]`
- `sizeInGb`: `int`
- `isSystemDisk`: `bool`
- `iops`: `int`
- `path`: `str`
- `state`: `DiskState`
- `attachedTo`: `str`
- `isAttached`: `bool`
- `attachmentState`: `str`
- `gbInUse`: `int`


## DistributionBundleTypeDef

```python
from mypy_boto3_lightsail.type_defs import DistributionBundleTypeDef
```




Optional fields:
- `bundleId`: `str`
- `name`: `str`
- `price`: `float`
- `transferPerMonthInGb`: `int`
- `isActive`: `bool`


## DomainEntryTypeDef

```python
from mypy_boto3_lightsail.type_defs import DomainEntryTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `target`: `str`
- `isAlias`: `bool`
- `type`: `str`
- `options`: `Dict[str, str]`


## DomainTypeDef

```python
from mypy_boto3_lightsail.type_defs import DomainTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `domainEntries`: `List["DomainEntryTypeDef"]`


## DomainValidationRecordTypeDef

```python
from mypy_boto3_lightsail.type_defs import DomainValidationRecordTypeDef
```




Optional fields:
- `domainName`: `str`
- `resourceRecord`: `"ResourceRecordTypeDef"`


## DownloadDefaultKeyPairResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import DownloadDefaultKeyPairResultTypeDef
```




Optional fields:
- `publicKeyBase64`: `str`
- `privateKeyBase64`: `str`


## EnableAddOnResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import EnableAddOnResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## EndpointRequestTypeDef

```python
from mypy_boto3_lightsail.type_defs import EndpointRequestTypeDef
```


Required fields:
- `containerName`: `str`
- `containerPort`: `int`



Optional fields:
- `healthCheck`: `"ContainerServiceHealthCheckConfigTypeDef"`


## ExportSnapshotRecordSourceInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import ExportSnapshotRecordSourceInfoTypeDef
```




Optional fields:
- `resourceType`: `ExportSnapshotRecordSourceType`
- `createdAt`: `datetime`
- `name`: `str`
- `arn`: `str`
- `fromResourceName`: `str`
- `fromResourceArn`: `str`
- `instanceSnapshotInfo`: `"InstanceSnapshotInfoTypeDef"`
- `diskSnapshotInfo`: `"DiskSnapshotInfoTypeDef"`


## ExportSnapshotRecordTypeDef

```python
from mypy_boto3_lightsail.type_defs import ExportSnapshotRecordTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `state`: `RecordState`
- `sourceInfo`: `"ExportSnapshotRecordSourceInfoTypeDef"`
- `destinationInfo`: `"DestinationInfoTypeDef"`


## ExportSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import ExportSnapshotResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## GetActiveNamesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetActiveNamesResultTypeDef
```




Optional fields:
- `activeNames`: `List[str]`
- `nextPageToken`: `str`


## GetAlarmsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetAlarmsResultTypeDef
```




Optional fields:
- `alarms`: `List["AlarmTypeDef"]`
- `nextPageToken`: `str`


## GetAutoSnapshotsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetAutoSnapshotsResultTypeDef
```




Optional fields:
- `resourceName`: `str`
- `resourceType`: `ResourceType`
- `autoSnapshots`: `List["AutoSnapshotDetailsTypeDef"]`


## GetBlueprintsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetBlueprintsResultTypeDef
```




Optional fields:
- `blueprints`: `List["BlueprintTypeDef"]`
- `nextPageToken`: `str`


## GetBundlesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetBundlesResultTypeDef
```




Optional fields:
- `bundles`: `List["BundleTypeDef"]`
- `nextPageToken`: `str`


## GetCertificatesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetCertificatesResultTypeDef
```




Optional fields:
- `certificates`: `List["CertificateSummaryTypeDef"]`


## GetCloudFormationStackRecordsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetCloudFormationStackRecordsResultTypeDef
```




Optional fields:
- `cloudFormationStackRecords`: `List["CloudFormationStackRecordTypeDef"]`
- `nextPageToken`: `str`


## GetContactMethodsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContactMethodsResultTypeDef
```




Optional fields:
- `contactMethods`: `List["ContactMethodTypeDef"]`


## GetContainerAPIMetadataResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContainerAPIMetadataResultTypeDef
```




Optional fields:
- `metadata`: `List[Dict[str, str]]`


## GetContainerImagesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContainerImagesResultTypeDef
```




Optional fields:
- `containerImages`: `List["ContainerImageTypeDef"]`


## GetContainerLogResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContainerLogResultTypeDef
```




Optional fields:
- `logEvents`: `List["ContainerServiceLogEventTypeDef"]`
- `nextPageToken`: `str`


## GetContainerServiceDeploymentsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContainerServiceDeploymentsResultTypeDef
```




Optional fields:
- `deployments`: `List["ContainerServiceDeploymentTypeDef"]`


## GetContainerServiceMetricDataResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContainerServiceMetricDataResultTypeDef
```




Optional fields:
- `metricName`: `ContainerServiceMetricName`
- `metricData`: `List["MetricDatapointTypeDef"]`


## GetContainerServicePowersResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetContainerServicePowersResultTypeDef
```




Optional fields:
- `powers`: `List["ContainerServicePowerTypeDef"]`


## GetDiskResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDiskResultTypeDef
```




Optional fields:
- `disk`: `"DiskTypeDef"`


## GetDiskSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDiskSnapshotResultTypeDef
```




Optional fields:
- `diskSnapshot`: `"DiskSnapshotTypeDef"`


## GetDiskSnapshotsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDiskSnapshotsResultTypeDef
```




Optional fields:
- `diskSnapshots`: `List["DiskSnapshotTypeDef"]`
- `nextPageToken`: `str`


## GetDisksResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDisksResultTypeDef
```




Optional fields:
- `disks`: `List["DiskTypeDef"]`
- `nextPageToken`: `str`


## GetDistributionBundlesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDistributionBundlesResultTypeDef
```




Optional fields:
- `bundles`: `List["DistributionBundleTypeDef"]`


## GetDistributionLatestCacheResetResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDistributionLatestCacheResetResultTypeDef
```




Optional fields:
- `status`: `str`
- `createTime`: `datetime`


## GetDistributionMetricDataResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDistributionMetricDataResultTypeDef
```




Optional fields:
- `metricName`: `DistributionMetricName`
- `metricData`: `List["MetricDatapointTypeDef"]`


## GetDistributionsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDistributionsResultTypeDef
```




Optional fields:
- `distributions`: `List["LightsailDistributionTypeDef"]`
- `nextPageToken`: `str`


## GetDomainResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDomainResultTypeDef
```




Optional fields:
- `domain`: `"DomainTypeDef"`


## GetDomainsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetDomainsResultTypeDef
```




Optional fields:
- `domains`: `List["DomainTypeDef"]`
- `nextPageToken`: `str`


## GetExportSnapshotRecordsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetExportSnapshotRecordsResultTypeDef
```




Optional fields:
- `exportSnapshotRecords`: `List["ExportSnapshotRecordTypeDef"]`
- `nextPageToken`: `str`


## GetInstanceAccessDetailsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstanceAccessDetailsResultTypeDef
```




Optional fields:
- `accessDetails`: `"InstanceAccessDetailsTypeDef"`


## GetInstanceMetricDataResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstanceMetricDataResultTypeDef
```




Optional fields:
- `metricName`: `InstanceMetricName`
- `metricData`: `List["MetricDatapointTypeDef"]`


## GetInstancePortStatesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstancePortStatesResultTypeDef
```




Optional fields:
- `portStates`: `List["InstancePortStateTypeDef"]`


## GetInstanceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstanceResultTypeDef
```




Optional fields:
- `instance`: `"InstanceTypeDef"`


## GetInstanceSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstanceSnapshotResultTypeDef
```




Optional fields:
- `instanceSnapshot`: `"InstanceSnapshotTypeDef"`


## GetInstanceSnapshotsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstanceSnapshotsResultTypeDef
```




Optional fields:
- `instanceSnapshots`: `List["InstanceSnapshotTypeDef"]`
- `nextPageToken`: `str`


## GetInstanceStateResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstanceStateResultTypeDef
```




Optional fields:
- `state`: `"InstanceStateTypeDef"`


## GetInstancesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetInstancesResultTypeDef
```




Optional fields:
- `instances`: `List["InstanceTypeDef"]`
- `nextPageToken`: `str`


## GetKeyPairResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetKeyPairResultTypeDef
```




Optional fields:
- `keyPair`: `"KeyPairTypeDef"`


## GetKeyPairsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetKeyPairsResultTypeDef
```




Optional fields:
- `keyPairs`: `List["KeyPairTypeDef"]`
- `nextPageToken`: `str`


## GetLoadBalancerMetricDataResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetLoadBalancerMetricDataResultTypeDef
```




Optional fields:
- `metricName`: `LoadBalancerMetricName`
- `metricData`: `List["MetricDatapointTypeDef"]`


## GetLoadBalancerResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetLoadBalancerResultTypeDef
```




Optional fields:
- `loadBalancer`: `"LoadBalancerTypeDef"`


## GetLoadBalancerTlsCertificatesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetLoadBalancerTlsCertificatesResultTypeDef
```




Optional fields:
- `tlsCertificates`: `List["LoadBalancerTlsCertificateTypeDef"]`


## GetLoadBalancersResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetLoadBalancersResultTypeDef
```




Optional fields:
- `loadBalancers`: `List["LoadBalancerTypeDef"]`
- `nextPageToken`: `str`


## GetOperationResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetOperationResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## GetOperationsForResourceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetOperationsForResourceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`
- `nextPageCount`: `str`
- `nextPageToken`: `str`


## GetOperationsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetOperationsResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`
- `nextPageToken`: `str`


## GetRegionsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRegionsResultTypeDef
```




Optional fields:
- `regions`: `List["RegionTypeDef"]`


## GetRelationalDatabaseBlueprintsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseBlueprintsResultTypeDef
```




Optional fields:
- `blueprints`: `List["RelationalDatabaseBlueprintTypeDef"]`
- `nextPageToken`: `str`


## GetRelationalDatabaseBundlesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseBundlesResultTypeDef
```




Optional fields:
- `bundles`: `List["RelationalDatabaseBundleTypeDef"]`
- `nextPageToken`: `str`


## GetRelationalDatabaseEventsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseEventsResultTypeDef
```




Optional fields:
- `relationalDatabaseEvents`: `List["RelationalDatabaseEventTypeDef"]`
- `nextPageToken`: `str`


## GetRelationalDatabaseLogEventsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseLogEventsResultTypeDef
```




Optional fields:
- `resourceLogEvents`: `List["LogEventTypeDef"]`
- `nextBackwardToken`: `str`
- `nextForwardToken`: `str`


## GetRelationalDatabaseLogStreamsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseLogStreamsResultTypeDef
```




Optional fields:
- `logStreams`: `List[str]`


## GetRelationalDatabaseMasterUserPasswordResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseMasterUserPasswordResultTypeDef
```




Optional fields:
- `masterUserPassword`: `str`
- `createdAt`: `datetime`


## GetRelationalDatabaseMetricDataResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseMetricDataResultTypeDef
```




Optional fields:
- `metricName`: `RelationalDatabaseMetricName`
- `metricData`: `List["MetricDatapointTypeDef"]`


## GetRelationalDatabaseParametersResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseParametersResultTypeDef
```




Optional fields:
- `parameters`: `List["RelationalDatabaseParameterTypeDef"]`
- `nextPageToken`: `str`


## GetRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseResultTypeDef
```




Optional fields:
- `relationalDatabase`: `"RelationalDatabaseTypeDef"`


## GetRelationalDatabaseSnapshotResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseSnapshotResultTypeDef
```




Optional fields:
- `relationalDatabaseSnapshot`: `"RelationalDatabaseSnapshotTypeDef"`


## GetRelationalDatabaseSnapshotsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabaseSnapshotsResultTypeDef
```




Optional fields:
- `relationalDatabaseSnapshots`: `List["RelationalDatabaseSnapshotTypeDef"]`
- `nextPageToken`: `str`


## GetRelationalDatabasesResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetRelationalDatabasesResultTypeDef
```




Optional fields:
- `relationalDatabases`: `List["RelationalDatabaseTypeDef"]`
- `nextPageToken`: `str`


## GetStaticIpResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetStaticIpResultTypeDef
```




Optional fields:
- `staticIp`: `"StaticIpTypeDef"`


## GetStaticIpsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import GetStaticIpsResultTypeDef
```




Optional fields:
- `staticIps`: `List["StaticIpTypeDef"]`
- `nextPageToken`: `str`


## HeaderObjectTypeDef

```python
from mypy_boto3_lightsail.type_defs import HeaderObjectTypeDef
```




Optional fields:
- `option`: `ForwardValues`
- `headersAllowList`: `List[HeaderEnum]`


## HostKeyAttributesTypeDef

```python
from mypy_boto3_lightsail.type_defs import HostKeyAttributesTypeDef
```




Optional fields:
- `algorithm`: `str`
- `publicKey`: `str`
- `witnessedAt`: `datetime`
- `fingerprintSHA1`: `str`
- `fingerprintSHA256`: `str`
- `notValidBefore`: `datetime`
- `notValidAfter`: `datetime`


## ImportKeyPairResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import ImportKeyPairResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## InputOriginTypeDef

```python
from mypy_boto3_lightsail.type_defs import InputOriginTypeDef
```




Optional fields:
- `name`: `str`
- `regionName`: `RegionName`
- `protocolPolicy`: `OriginProtocolPolicyEnum`


## InstanceAccessDetailsTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceAccessDetailsTypeDef
```




Optional fields:
- `certKey`: `str`
- `expiresAt`: `datetime`
- `ipAddress`: `str`
- `password`: `str`
- `passwordData`: `"PasswordDataTypeDef"`
- `privateKey`: `str`
- `protocol`: `InstanceAccessProtocol`
- `instanceName`: `str`
- `username`: `str`
- `hostKeys`: `List["HostKeyAttributesTypeDef"]`


## InstanceEntryTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceEntryTypeDef
```


Required fields:
- `sourceName`: `str`
- `instanceType`: `str`
- `portInfoSource`: `PortInfoSourceType`
- `availabilityZone`: `str`



Optional fields:
- `userData`: `str`


## InstanceHardwareTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceHardwareTypeDef
```




Optional fields:
- `cpuCount`: `int`
- `disks`: `List["DiskTypeDef"]`
- `ramSizeInGb`: `float`


## InstanceHealthSummaryTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceHealthSummaryTypeDef
```




Optional fields:
- `instanceName`: `str`
- `instanceHealth`: `InstanceHealthState`
- `instanceHealthReason`: `InstanceHealthReason`


## InstanceNetworkingTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceNetworkingTypeDef
```




Optional fields:
- `monthlyTransfer`: `"MonthlyTransferTypeDef"`
- `ports`: `List["InstancePortInfoTypeDef"]`


## InstancePortInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstancePortInfoTypeDef
```




Optional fields:
- `fromPort`: `int`
- `toPort`: `int`
- `protocol`: `NetworkProtocol`
- `accessFrom`: `str`
- `accessType`: `PortAccessType`
- `commonName`: `str`
- `accessDirection`: `AccessDirection`
- `cidrs`: `List[str]`
- `ipv6Cidrs`: `List[str]`
- `cidrListAliases`: `List[str]`


## InstancePortStateTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstancePortStateTypeDef
```




Optional fields:
- `fromPort`: `int`
- `toPort`: `int`
- `protocol`: `NetworkProtocol`
- `state`: `PortState`
- `cidrs`: `List[str]`
- `ipv6Cidrs`: `List[str]`
- `cidrListAliases`: `List[str]`


## InstanceSnapshotInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceSnapshotInfoTypeDef
```




Optional fields:
- `fromBundleId`: `str`
- `fromBlueprintId`: `str`
- `fromDiskInfo`: `List["DiskInfoTypeDef"]`


## InstanceSnapshotTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceSnapshotTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `state`: `InstanceSnapshotState`
- `progress`: `str`
- `fromAttachedDisks`: `List["DiskTypeDef"]`
- `fromInstanceName`: `str`
- `fromInstanceArn`: `str`
- `fromBlueprintId`: `str`
- `fromBundleId`: `str`
- `isFromAutoSnapshot`: `bool`
- `sizeInGb`: `int`


## InstanceStateTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceStateTypeDef
```




Optional fields:
- `code`: `int`
- `name`: `str`


## InstanceTypeDef

```python
from mypy_boto3_lightsail.type_defs import InstanceTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `blueprintId`: `str`
- `blueprintName`: `str`
- `bundleId`: `str`
- `addOns`: `List["AddOnTypeDef"]`
- `isStaticIp`: `bool`
- `privateIpAddress`: `str`
- `publicIpAddress`: `str`
- `ipv6Addresses`: `List[str]`
- `ipAddressType`: `IpAddressType`
- `hardware`: `"InstanceHardwareTypeDef"`
- `networking`: `"InstanceNetworkingTypeDef"`
- `state`: `"InstanceStateTypeDef"`
- `username`: `str`
- `sshKeyName`: `str`


## IsVpcPeeredResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import IsVpcPeeredResultTypeDef
```




Optional fields:
- `isPeered`: `bool`


## KeyPairTypeDef

```python
from mypy_boto3_lightsail.type_defs import KeyPairTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `fingerprint`: `str`


## LightsailDistributionTypeDef

```python
from mypy_boto3_lightsail.type_defs import LightsailDistributionTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `alternativeDomainNames`: `List[str]`
- `status`: `str`
- `isEnabled`: `bool`
- `domainName`: `str`
- `bundleId`: `str`
- `certificateName`: `str`
- `origin`: `"OriginTypeDef"`
- `originPublicDNS`: `str`
- `defaultCacheBehavior`: `"CacheBehaviorTypeDef"`
- `cacheBehaviorSettings`: `"CacheSettingsTypeDef"`
- `cacheBehaviors`: `List["CacheBehaviorPerPathTypeDef"]`
- `ableToUpdateBundle`: `bool`
- `ipAddressType`: `IpAddressType`
- `tags`: `List["TagTypeDef"]`


## LoadBalancerTlsCertificateDomainValidationOptionTypeDef

```python
from mypy_boto3_lightsail.type_defs import LoadBalancerTlsCertificateDomainValidationOptionTypeDef
```




Optional fields:
- `domainName`: `str`
- `validationStatus`: `LoadBalancerTlsCertificateDomainStatus`


## LoadBalancerTlsCertificateDomainValidationRecordTypeDef

```python
from mypy_boto3_lightsail.type_defs import LoadBalancerTlsCertificateDomainValidationRecordTypeDef
```




Optional fields:
- `name`: `str`
- `type`: `str`
- `value`: `str`
- `validationStatus`: `LoadBalancerTlsCertificateDomainStatus`
- `domainName`: `str`


## LoadBalancerTlsCertificateRenewalSummaryTypeDef

```python
from mypy_boto3_lightsail.type_defs import LoadBalancerTlsCertificateRenewalSummaryTypeDef
```




Optional fields:
- `renewalStatus`: `LoadBalancerTlsCertificateRenewalStatus`
- `domainValidationOptions`: `List["LoadBalancerTlsCertificateDomainValidationOptionTypeDef"]`


## LoadBalancerTlsCertificateSummaryTypeDef

```python
from mypy_boto3_lightsail.type_defs import LoadBalancerTlsCertificateSummaryTypeDef
```




Optional fields:
- `name`: `str`
- `isAttached`: `bool`


## LoadBalancerTlsCertificateTypeDef

```python
from mypy_boto3_lightsail.type_defs import LoadBalancerTlsCertificateTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `loadBalancerName`: `str`
- `isAttached`: `bool`
- `status`: `LoadBalancerTlsCertificateStatus`
- `domainName`: `str`
- `domainValidationRecords`: `List["LoadBalancerTlsCertificateDomainValidationRecordTypeDef"]`
- `failureReason`: `LoadBalancerTlsCertificateFailureReason`
- `issuedAt`: `datetime`
- `issuer`: `str`
- `keyAlgorithm`: `str`
- `notAfter`: `datetime`
- `notBefore`: `datetime`
- `renewalSummary`: `"LoadBalancerTlsCertificateRenewalSummaryTypeDef"`
- `revocationReason`: `LoadBalancerTlsCertificateRevocationReason`
- `revokedAt`: `datetime`
- `serial`: `str`
- `signatureAlgorithm`: `str`
- `subject`: `str`
- `subjectAlternativeNames`: `List[str]`


## LoadBalancerTypeDef

```python
from mypy_boto3_lightsail.type_defs import LoadBalancerTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `dnsName`: `str`
- `state`: `LoadBalancerState`
- `protocol`: `LoadBalancerProtocol`
- `publicPorts`: `List[int]`
- `healthCheckPath`: `str`
- `instancePort`: `int`
- `instanceHealthSummary`: `List["InstanceHealthSummaryTypeDef"]`
- `tlsCertificateSummaries`: `List["LoadBalancerTlsCertificateSummaryTypeDef"]`
- `configurationOptions`: `Dict[LoadBalancerAttributeName, str]`
- `ipAddressType`: `IpAddressType`


## LogEventTypeDef

```python
from mypy_boto3_lightsail.type_defs import LogEventTypeDef
```




Optional fields:
- `createdAt`: `datetime`
- `message`: `str`


## MetricDatapointTypeDef

```python
from mypy_boto3_lightsail.type_defs import MetricDatapointTypeDef
```




Optional fields:
- `average`: `float`
- `maximum`: `float`
- `minimum`: `float`
- `sampleCount`: `float`
- `sum`: `float`
- `timestamp`: `datetime`
- `unit`: `MetricUnit`


## MonitoredResourceInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import MonitoredResourceInfoTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `resourceType`: `ResourceType`


## MonthlyTransferTypeDef

```python
from mypy_boto3_lightsail.type_defs import MonthlyTransferTypeDef
```




Optional fields:
- `gbPerMonthAllocated`: `int`


## OpenInstancePublicPortsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import OpenInstancePublicPortsResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## OperationTypeDef

```python
from mypy_boto3_lightsail.type_defs import OperationTypeDef
```




Optional fields:
- `id`: `str`
- `resourceName`: `str`
- `resourceType`: `ResourceType`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `isTerminal`: `bool`
- `operationDetails`: `str`
- `operationType`: `OperationType`
- `status`: `OperationStatus`
- `statusChangedAt`: `datetime`
- `errorCode`: `str`
- `errorDetails`: `str`


## OriginTypeDef

```python
from mypy_boto3_lightsail.type_defs import OriginTypeDef
```




Optional fields:
- `name`: `str`
- `resourceType`: `ResourceType`
- `regionName`: `RegionName`
- `protocolPolicy`: `OriginProtocolPolicyEnum`


## PaginatorConfigTypeDef

```python
from mypy_boto3_lightsail.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PasswordDataTypeDef

```python
from mypy_boto3_lightsail.type_defs import PasswordDataTypeDef
```




Optional fields:
- `ciphertext`: `str`
- `keyPairName`: `str`


## PeerVpcResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import PeerVpcResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## PendingMaintenanceActionTypeDef

```python
from mypy_boto3_lightsail.type_defs import PendingMaintenanceActionTypeDef
```




Optional fields:
- `action`: `str`
- `description`: `str`
- `currentApplyDate`: `datetime`


## PendingModifiedRelationalDatabaseValuesTypeDef

```python
from mypy_boto3_lightsail.type_defs import PendingModifiedRelationalDatabaseValuesTypeDef
```




Optional fields:
- `masterUserPassword`: `str`
- `engineVersion`: `str`
- `backupRetentionEnabled`: `bool`


## PortInfoTypeDef

```python
from mypy_boto3_lightsail.type_defs import PortInfoTypeDef
```




Optional fields:
- `fromPort`: `int`
- `toPort`: `int`
- `protocol`: `NetworkProtocol`
- `cidrs`: `List[str]`
- `ipv6Cidrs`: `List[str]`
- `cidrListAliases`: `List[str]`


## PutAlarmResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import PutAlarmResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## PutInstancePublicPortsResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import PutInstancePublicPortsResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## QueryStringObjectTypeDef

```python
from mypy_boto3_lightsail.type_defs import QueryStringObjectTypeDef
```




Optional fields:
- `option`: `bool`
- `queryStringsAllowList`: `List[str]`


## RebootInstanceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import RebootInstanceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## RebootRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import RebootRelationalDatabaseResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## RegionTypeDef

```python
from mypy_boto3_lightsail.type_defs import RegionTypeDef
```




Optional fields:
- `continentCode`: `str`
- `description`: `str`
- `displayName`: `str`
- `name`: `RegionName`
- `availabilityZones`: `List["AvailabilityZoneTypeDef"]`
- `relationalDatabaseAvailabilityZones`: `List["AvailabilityZoneTypeDef"]`


## RegisterContainerImageResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import RegisterContainerImageResultTypeDef
```




Optional fields:
- `containerImage`: `"ContainerImageTypeDef"`


## RelationalDatabaseBlueprintTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseBlueprintTypeDef
```




Optional fields:
- `blueprintId`: `str`
- `engine`: `Literal['mysql']`
- `engineVersion`: `str`
- `engineDescription`: `str`
- `engineVersionDescription`: `str`
- `isEngineDefault`: `bool`


## RelationalDatabaseBundleTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseBundleTypeDef
```




Optional fields:
- `bundleId`: `str`
- `name`: `str`
- `price`: `float`
- `ramSizeInGb`: `float`
- `diskSizeInGb`: `int`
- `transferPerMonthInGb`: `int`
- `cpuCount`: `int`
- `isEncrypted`: `bool`
- `isActive`: `bool`


## RelationalDatabaseEndpointTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseEndpointTypeDef
```




Optional fields:
- `port`: `int`
- `address`: `str`


## RelationalDatabaseEventTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseEventTypeDef
```




Optional fields:
- `resource`: `str`
- `createdAt`: `datetime`
- `message`: `str`
- `eventCategories`: `List[str]`


## RelationalDatabaseHardwareTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseHardwareTypeDef
```




Optional fields:
- `cpuCount`: `int`
- `diskSizeInGb`: `int`
- `ramSizeInGb`: `float`


## RelationalDatabaseParameterTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseParameterTypeDef
```




Optional fields:
- `allowedValues`: `str`
- `applyMethod`: `str`
- `applyType`: `str`
- `dataType`: `str`
- `description`: `str`
- `isModifiable`: `bool`
- `parameterName`: `str`
- `parameterValue`: `str`


## RelationalDatabaseSnapshotTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseSnapshotTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `engine`: `str`
- `engineVersion`: `str`
- `sizeInGb`: `int`
- `state`: `str`
- `fromRelationalDatabaseName`: `str`
- `fromRelationalDatabaseArn`: `str`
- `fromRelationalDatabaseBundleId`: `str`
- `fromRelationalDatabaseBlueprintId`: `str`


## RelationalDatabaseTypeDef

```python
from mypy_boto3_lightsail.type_defs import RelationalDatabaseTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `tags`: `List["TagTypeDef"]`
- `relationalDatabaseBlueprintId`: `str`
- `relationalDatabaseBundleId`: `str`
- `masterDatabaseName`: `str`
- `hardware`: `"RelationalDatabaseHardwareTypeDef"`
- `state`: `str`
- `secondaryAvailabilityZone`: `str`
- `backupRetentionEnabled`: `bool`
- `pendingModifiedValues`: `"PendingModifiedRelationalDatabaseValuesTypeDef"`
- `engine`: `str`
- `engineVersion`: `str`
- `latestRestorableTime`: `datetime`
- `masterUsername`: `str`
- `parameterApplyStatus`: `str`
- `preferredBackupWindow`: `str`
- `preferredMaintenanceWindow`: `str`
- `publiclyAccessible`: `bool`
- `masterEndpoint`: `"RelationalDatabaseEndpointTypeDef"`
- `pendingMaintenanceActions`: `List["PendingMaintenanceActionTypeDef"]`
- `caCertificateIdentifier`: `str`


## ReleaseStaticIpResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import ReleaseStaticIpResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## RenewalSummaryTypeDef

```python
from mypy_boto3_lightsail.type_defs import RenewalSummaryTypeDef
```




Optional fields:
- `domainValidationRecords`: `List["DomainValidationRecordTypeDef"]`
- `renewalStatus`: `RenewalStatus`
- `renewalStatusReason`: `str`
- `updatedAt`: `datetime`


## ResetDistributionCacheResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import ResetDistributionCacheResultTypeDef
```




Optional fields:
- `status`: `str`
- `createTime`: `datetime`
- `operation`: `"OperationTypeDef"`


## ResourceLocationTypeDef

```python
from mypy_boto3_lightsail.type_defs import ResourceLocationTypeDef
```




Optional fields:
- `availabilityZone`: `str`
- `regionName`: `RegionName`


## ResourceRecordTypeDef

```python
from mypy_boto3_lightsail.type_defs import ResourceRecordTypeDef
```




Optional fields:
- `name`: `str`
- `type`: `str`
- `value`: `str`


## SendContactMethodVerificationResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import SendContactMethodVerificationResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## SetIpAddressTypeResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import SetIpAddressTypeResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## StartInstanceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import StartInstanceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## StartRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import StartRelationalDatabaseResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## StaticIpTypeDef

```python
from mypy_boto3_lightsail.type_defs import StaticIpTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `supportCode`: `str`
- `createdAt`: `datetime`
- `location`: `"ResourceLocationTypeDef"`
- `resourceType`: `ResourceType`
- `ipAddress`: `str`
- `attachedTo`: `str`
- `isAttached`: `bool`


## StopInstanceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import StopInstanceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## StopRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import StopRelationalDatabaseResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## TagResourceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import TagResourceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_lightsail.type_defs import TagTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## TestAlarmResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import TestAlarmResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## UnpeerVpcResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UnpeerVpcResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## UntagResourceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UntagResourceResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## UpdateContainerServiceResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateContainerServiceResultTypeDef
```




Optional fields:
- `containerService`: `"ContainerServiceTypeDef"`


## UpdateDistributionBundleResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateDistributionBundleResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## UpdateDistributionResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateDistributionResultTypeDef
```




Optional fields:
- `operation`: `"OperationTypeDef"`


## UpdateDomainEntryResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateDomainEntryResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## UpdateLoadBalancerAttributeResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateLoadBalancerAttributeResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## UpdateRelationalDatabaseParametersResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateRelationalDatabaseParametersResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`


## UpdateRelationalDatabaseResultTypeDef

```python
from mypy_boto3_lightsail.type_defs import UpdateRelationalDatabaseResultTypeDef
```




Optional fields:
- `operations`: `List["OperationTypeDef"]`

