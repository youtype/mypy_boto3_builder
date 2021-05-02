# Structures for boto3 RDS module

> [Index](../index.md) > [RDS](./index.md) > Structures

Auto-generated documentation for [RDS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
type annotations stubs module [mypy_boto3_rds](https://pypi.org/project/mypy-boto3-rds/).

- [Structures for boto3 RDS module](#structures-for-boto3-rds-module)
  - [AccountQuotaTypeDef](#accountquotatypedef)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [AvailableProcessorFeatureTypeDef](#availableprocessorfeaturetypedef)
  - [CertificateTypeDef](#certificatetypedef)
  - [CharacterSetTypeDef](#charactersettypedef)
  - [ClusterPendingModifiedValuesTypeDef](#clusterpendingmodifiedvaluestypedef)
  - [ConnectionPoolConfigurationInfoTypeDef](#connectionpoolconfigurationinfotypedef)
  - [CustomAvailabilityZoneTypeDef](#customavailabilityzonetypedef)
  - [DBClusterBacktrackTypeDef](#dbclusterbacktracktypedef)
  - [DBClusterEndpointTypeDef](#dbclusterendpointtypedef)
  - [DBClusterMemberTypeDef](#dbclustermembertypedef)
  - [DBClusterOptionGroupStatusTypeDef](#dbclusteroptiongroupstatustypedef)
  - [DBClusterParameterGroupTypeDef](#dbclusterparametergrouptypedef)
  - [DBClusterRoleTypeDef](#dbclusterroletypedef)
  - [DBClusterSnapshotAttributeTypeDef](#dbclustersnapshotattributetypedef)
  - [DBClusterSnapshotAttributesResultTypeDef](#dbclustersnapshotattributesresulttypedef)
  - [DBClusterSnapshotTypeDef](#dbclustersnapshottypedef)
  - [DBClusterTypeDef](#dbclustertypedef)
  - [DBEngineVersionTypeDef](#dbengineversiontypedef)
  - [DBInstanceAutomatedBackupTypeDef](#dbinstanceautomatedbackuptypedef)
  - [DBInstanceAutomatedBackupsReplicationTypeDef](#dbinstanceautomatedbackupsreplicationtypedef)
  - [DBInstanceRoleTypeDef](#dbinstanceroletypedef)
  - [DBInstanceStatusInfoTypeDef](#dbinstancestatusinfotypedef)
  - [DBInstanceTypeDef](#dbinstancetypedef)
  - [DBParameterGroupStatusTypeDef](#dbparametergroupstatustypedef)
  - [DBParameterGroupTypeDef](#dbparametergrouptypedef)
  - [DBProxyEndpointTypeDef](#dbproxyendpointtypedef)
  - [DBProxyTargetGroupTypeDef](#dbproxytargetgrouptypedef)
  - [DBProxyTargetTypeDef](#dbproxytargettypedef)
  - [DBProxyTypeDef](#dbproxytypedef)
  - [DBSecurityGroupMembershipTypeDef](#dbsecuritygroupmembershiptypedef)
  - [DBSecurityGroupTypeDef](#dbsecuritygrouptypedef)
  - [DBSnapshotAttributeTypeDef](#dbsnapshotattributetypedef)
  - [DBSnapshotAttributesResultTypeDef](#dbsnapshotattributesresulttypedef)
  - [DBSnapshotTypeDef](#dbsnapshottypedef)
  - [DBSubnetGroupTypeDef](#dbsubnetgrouptypedef)
  - [DescribeDBLogFilesDetailsTypeDef](#describedblogfilesdetailstypedef)
  - [DomainMembershipTypeDef](#domainmembershiptypedef)
  - [DoubleRangeTypeDef](#doublerangetypedef)
  - [EC2SecurityGroupTypeDef](#ec2securitygrouptypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [EngineDefaultsTypeDef](#enginedefaultstypedef)
  - [EventCategoriesMapTypeDef](#eventcategoriesmaptypedef)
  - [EventSubscriptionTypeDef](#eventsubscriptiontypedef)
  - [EventTypeDef](#eventtypedef)
  - [ExportTaskTypeDef](#exporttasktypedef)
  - [FailoverStateTypeDef](#failoverstatetypedef)
  - [GlobalClusterMemberTypeDef](#globalclustermembertypedef)
  - [GlobalClusterTypeDef](#globalclustertypedef)
  - [IPRangeTypeDef](#iprangetypedef)
  - [InstallationMediaFailureCauseTypeDef](#installationmediafailurecausetypedef)
  - [InstallationMediaTypeDef](#installationmediatypedef)
  - [MinimumEngineVersionPerAllowedValueTypeDef](#minimumengineversionperallowedvaluetypedef)
  - [OptionGroupMembershipTypeDef](#optiongroupmembershiptypedef)
  - [OptionGroupOptionSettingTypeDef](#optiongroupoptionsettingtypedef)
  - [OptionGroupOptionTypeDef](#optiongroupoptiontypedef)
  - [OptionGroupTypeDef](#optiongrouptypedef)
  - [OptionSettingTypeDef](#optionsettingtypedef)
  - [OptionTypeDef](#optiontypedef)
  - [OptionVersionTypeDef](#optionversiontypedef)
  - [OrderableDBInstanceOptionTypeDef](#orderabledbinstanceoptiontypedef)
  - [OutpostTypeDef](#outposttypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [PendingCloudwatchLogsExportsTypeDef](#pendingcloudwatchlogsexportstypedef)
  - [PendingMaintenanceActionTypeDef](#pendingmaintenanceactiontypedef)
  - [PendingModifiedValuesTypeDef](#pendingmodifiedvaluestypedef)
  - [ProcessorFeatureTypeDef](#processorfeaturetypedef)
  - [RangeTypeDef](#rangetypedef)
  - [RecurringChargeTypeDef](#recurringchargetypedef)
  - [ReservedDBInstanceTypeDef](#reserveddbinstancetypedef)
  - [ReservedDBInstancesOfferingTypeDef](#reserveddbinstancesofferingtypedef)
  - [ResourcePendingMaintenanceActionsTypeDef](#resourcependingmaintenanceactionstypedef)
  - [RestoreWindowTypeDef](#restorewindowtypedef)
  - [ScalingConfigurationInfoTypeDef](#scalingconfigurationinfotypedef)
  - [SourceRegionTypeDef](#sourceregiontypedef)
  - [SubnetTypeDef](#subnettypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetHealthTypeDef](#targethealthtypedef)
  - [TimezoneTypeDef](#timezonetypedef)
  - [UpgradeTargetTypeDef](#upgradetargettypedef)
  - [UserAuthConfigInfoTypeDef](#userauthconfiginfotypedef)
  - [ValidDBInstanceModificationsMessageTypeDef](#validdbinstancemodificationsmessagetypedef)
  - [ValidStorageOptionsTypeDef](#validstorageoptionstypedef)
  - [VpcSecurityGroupMembershipTypeDef](#vpcsecuritygroupmembershiptypedef)
  - [VpnDetailsTypeDef](#vpndetailstypedef)
  - [AccountAttributesMessageTypeDef](#accountattributesmessagetypedef)
  - [AddSourceIdentifierToSubscriptionResultTypeDef](#addsourceidentifiertosubscriptionresulttypedef)
  - [ApplyPendingMaintenanceActionResultTypeDef](#applypendingmaintenanceactionresulttypedef)
  - [AuthorizeDBSecurityGroupIngressResultTypeDef](#authorizedbsecuritygroupingressresulttypedef)
  - [CertificateMessageTypeDef](#certificatemessagetypedef)
  - [CloudwatchLogsExportConfigurationTypeDef](#cloudwatchlogsexportconfigurationtypedef)
  - [ConnectionPoolConfigurationTypeDef](#connectionpoolconfigurationtypedef)
  - [CopyDBClusterParameterGroupResultTypeDef](#copydbclusterparametergroupresulttypedef)
  - [CopyDBClusterSnapshotResultTypeDef](#copydbclustersnapshotresulttypedef)
  - [CopyDBParameterGroupResultTypeDef](#copydbparametergroupresulttypedef)
  - [CopyDBSnapshotResultTypeDef](#copydbsnapshotresulttypedef)
  - [CopyOptionGroupResultTypeDef](#copyoptiongroupresulttypedef)
  - [CreateCustomAvailabilityZoneResultTypeDef](#createcustomavailabilityzoneresulttypedef)
  - [CreateDBClusterParameterGroupResultTypeDef](#createdbclusterparametergroupresulttypedef)
  - [CreateDBClusterResultTypeDef](#createdbclusterresulttypedef)
  - [CreateDBClusterSnapshotResultTypeDef](#createdbclustersnapshotresulttypedef)
  - [CreateDBInstanceReadReplicaResultTypeDef](#createdbinstancereadreplicaresulttypedef)
  - [CreateDBInstanceResultTypeDef](#createdbinstanceresulttypedef)
  - [CreateDBParameterGroupResultTypeDef](#createdbparametergroupresulttypedef)
  - [CreateDBProxyEndpointResponseTypeDef](#createdbproxyendpointresponsetypedef)
  - [CreateDBProxyResponseTypeDef](#createdbproxyresponsetypedef)
  - [CreateDBSecurityGroupResultTypeDef](#createdbsecuritygroupresulttypedef)
  - [CreateDBSnapshotResultTypeDef](#createdbsnapshotresulttypedef)
  - [CreateDBSubnetGroupResultTypeDef](#createdbsubnetgroupresulttypedef)
  - [CreateEventSubscriptionResultTypeDef](#createeventsubscriptionresulttypedef)
  - [CreateGlobalClusterResultTypeDef](#createglobalclusterresulttypedef)
  - [CreateOptionGroupResultTypeDef](#createoptiongroupresulttypedef)
  - [CustomAvailabilityZoneMessageTypeDef](#customavailabilityzonemessagetypedef)
  - [DBClusterBacktrackMessageTypeDef](#dbclusterbacktrackmessagetypedef)
  - [DBClusterCapacityInfoTypeDef](#dbclustercapacityinfotypedef)
  - [DBClusterEndpointMessageTypeDef](#dbclusterendpointmessagetypedef)
  - [DBClusterMessageTypeDef](#dbclustermessagetypedef)
  - [DBClusterParameterGroupDetailsTypeDef](#dbclusterparametergroupdetailstypedef)
  - [DBClusterParameterGroupNameMessageTypeDef](#dbclusterparametergroupnamemessagetypedef)
  - [DBClusterParameterGroupsMessageTypeDef](#dbclusterparametergroupsmessagetypedef)
  - [DBClusterSnapshotMessageTypeDef](#dbclustersnapshotmessagetypedef)
  - [DBEngineVersionMessageTypeDef](#dbengineversionmessagetypedef)
  - [DBInstanceAutomatedBackupMessageTypeDef](#dbinstanceautomatedbackupmessagetypedef)
  - [DBInstanceMessageTypeDef](#dbinstancemessagetypedef)
  - [DBParameterGroupDetailsTypeDef](#dbparametergroupdetailstypedef)
  - [DBParameterGroupNameMessageTypeDef](#dbparametergroupnamemessagetypedef)
  - [DBParameterGroupsMessageTypeDef](#dbparametergroupsmessagetypedef)
  - [DBSecurityGroupMessageTypeDef](#dbsecuritygroupmessagetypedef)
  - [DBSnapshotMessageTypeDef](#dbsnapshotmessagetypedef)
  - [DBSubnetGroupMessageTypeDef](#dbsubnetgroupmessagetypedef)
  - [DeleteCustomAvailabilityZoneResultTypeDef](#deletecustomavailabilityzoneresulttypedef)
  - [DeleteDBClusterResultTypeDef](#deletedbclusterresulttypedef)
  - [DeleteDBClusterSnapshotResultTypeDef](#deletedbclustersnapshotresulttypedef)
  - [DeleteDBInstanceAutomatedBackupResultTypeDef](#deletedbinstanceautomatedbackupresulttypedef)
  - [DeleteDBInstanceResultTypeDef](#deletedbinstanceresulttypedef)
  - [DeleteDBProxyEndpointResponseTypeDef](#deletedbproxyendpointresponsetypedef)
  - [DeleteDBProxyResponseTypeDef](#deletedbproxyresponsetypedef)
  - [DeleteDBSnapshotResultTypeDef](#deletedbsnapshotresulttypedef)
  - [DeleteEventSubscriptionResultTypeDef](#deleteeventsubscriptionresulttypedef)
  - [DeleteGlobalClusterResultTypeDef](#deleteglobalclusterresulttypedef)
  - [DescribeDBClusterSnapshotAttributesResultTypeDef](#describedbclustersnapshotattributesresulttypedef)
  - [DescribeDBLogFilesResponseTypeDef](#describedblogfilesresponsetypedef)
  - [DescribeDBProxiesResponseTypeDef](#describedbproxiesresponsetypedef)
  - [DescribeDBProxyEndpointsResponseTypeDef](#describedbproxyendpointsresponsetypedef)
  - [DescribeDBProxyTargetGroupsResponseTypeDef](#describedbproxytargetgroupsresponsetypedef)
  - [DescribeDBProxyTargetsResponseTypeDef](#describedbproxytargetsresponsetypedef)
  - [DescribeDBSnapshotAttributesResultTypeDef](#describedbsnapshotattributesresulttypedef)
  - [DescribeEngineDefaultClusterParametersResultTypeDef](#describeenginedefaultclusterparametersresulttypedef)
  - [DescribeEngineDefaultParametersResultTypeDef](#describeenginedefaultparametersresulttypedef)
  - [DescribeValidDBInstanceModificationsResultTypeDef](#describevaliddbinstancemodificationsresulttypedef)
  - [DownloadDBLogFilePortionDetailsTypeDef](#downloaddblogfileportiondetailstypedef)
  - [EventCategoriesMessageTypeDef](#eventcategoriesmessagetypedef)
  - [EventSubscriptionsMessageTypeDef](#eventsubscriptionsmessagetypedef)
  - [EventsMessageTypeDef](#eventsmessagetypedef)
  - [ExportTasksMessageTypeDef](#exporttasksmessagetypedef)
  - [FailoverDBClusterResultTypeDef](#failoverdbclusterresulttypedef)
  - [FailoverGlobalClusterResultTypeDef](#failoverglobalclusterresulttypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GlobalClustersMessageTypeDef](#globalclustersmessagetypedef)
  - [InstallationMediaMessageTypeDef](#installationmediamessagetypedef)
  - [ModifyCertificatesResultTypeDef](#modifycertificatesresulttypedef)
  - [ModifyDBClusterResultTypeDef](#modifydbclusterresulttypedef)
  - [ModifyDBClusterSnapshotAttributeResultTypeDef](#modifydbclustersnapshotattributeresulttypedef)
  - [ModifyDBInstanceResultTypeDef](#modifydbinstanceresulttypedef)
  - [ModifyDBProxyEndpointResponseTypeDef](#modifydbproxyendpointresponsetypedef)
  - [ModifyDBProxyResponseTypeDef](#modifydbproxyresponsetypedef)
  - [ModifyDBProxyTargetGroupResponseTypeDef](#modifydbproxytargetgroupresponsetypedef)
  - [ModifyDBSnapshotAttributeResultTypeDef](#modifydbsnapshotattributeresulttypedef)
  - [ModifyDBSnapshotResultTypeDef](#modifydbsnapshotresulttypedef)
  - [ModifyDBSubnetGroupResultTypeDef](#modifydbsubnetgroupresulttypedef)
  - [ModifyEventSubscriptionResultTypeDef](#modifyeventsubscriptionresulttypedef)
  - [ModifyGlobalClusterResultTypeDef](#modifyglobalclusterresulttypedef)
  - [ModifyOptionGroupResultTypeDef](#modifyoptiongroupresulttypedef)
  - [OptionConfigurationTypeDef](#optionconfigurationtypedef)
  - [OptionGroupOptionsMessageTypeDef](#optiongroupoptionsmessagetypedef)
  - [OptionGroupsTypeDef](#optiongroupstypedef)
  - [OrderableDBInstanceOptionsMessageTypeDef](#orderabledbinstanceoptionsmessagetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PendingMaintenanceActionsMessageTypeDef](#pendingmaintenanceactionsmessagetypedef)
  - [PromoteReadReplicaDBClusterResultTypeDef](#promotereadreplicadbclusterresulttypedef)
  - [PromoteReadReplicaResultTypeDef](#promotereadreplicaresulttypedef)
  - [PurchaseReservedDBInstancesOfferingResultTypeDef](#purchasereserveddbinstancesofferingresulttypedef)
  - [RebootDBInstanceResultTypeDef](#rebootdbinstanceresulttypedef)
  - [RegisterDBProxyTargetsResponseTypeDef](#registerdbproxytargetsresponsetypedef)
  - [RemoveFromGlobalClusterResultTypeDef](#removefromglobalclusterresulttypedef)
  - [RemoveSourceIdentifierFromSubscriptionResultTypeDef](#removesourceidentifierfromsubscriptionresulttypedef)
  - [ReservedDBInstanceMessageTypeDef](#reserveddbinstancemessagetypedef)
  - [ReservedDBInstancesOfferingMessageTypeDef](#reserveddbinstancesofferingmessagetypedef)
  - [RestoreDBClusterFromS3ResultTypeDef](#restoredbclusterfroms3resulttypedef)
  - [RestoreDBClusterFromSnapshotResultTypeDef](#restoredbclusterfromsnapshotresulttypedef)
  - [RestoreDBClusterToPointInTimeResultTypeDef](#restoredbclustertopointintimeresulttypedef)
  - [RestoreDBInstanceFromDBSnapshotResultTypeDef](#restoredbinstancefromdbsnapshotresulttypedef)
  - [RestoreDBInstanceFromS3ResultTypeDef](#restoredbinstancefroms3resulttypedef)
  - [RestoreDBInstanceToPointInTimeResultTypeDef](#restoredbinstancetopointintimeresulttypedef)
  - [RevokeDBSecurityGroupIngressResultTypeDef](#revokedbsecuritygroupingressresulttypedef)
  - [ScalingConfigurationTypeDef](#scalingconfigurationtypedef)
  - [SourceRegionMessageTypeDef](#sourceregionmessagetypedef)
  - [StartActivityStreamResponseTypeDef](#startactivitystreamresponsetypedef)
  - [StartDBClusterResultTypeDef](#startdbclusterresulttypedef)
  - [StartDBInstanceAutomatedBackupsReplicationResultTypeDef](#startdbinstanceautomatedbackupsreplicationresulttypedef)
  - [StartDBInstanceResultTypeDef](#startdbinstanceresulttypedef)
  - [StopActivityStreamResponseTypeDef](#stopactivitystreamresponsetypedef)
  - [StopDBClusterResultTypeDef](#stopdbclusterresulttypedef)
  - [StopDBInstanceAutomatedBackupsReplicationResultTypeDef](#stopdbinstanceautomatedbackupsreplicationresulttypedef)
  - [StopDBInstanceResultTypeDef](#stopdbinstanceresulttypedef)
  - [TagListMessageTypeDef](#taglistmessagetypedef)
  - [UserAuthConfigTypeDef](#userauthconfigtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountQuotaTypeDef

```python
from mypy_boto3_rds.type_defs import AccountQuotaTypeDef
```




Optional fields:
- `AccountQuotaName`: `str`
- `Used`: `int`
- `Max`: `int`


## AvailabilityZoneTypeDef

```python
from mypy_boto3_rds.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `Name`: `str`


## AvailableProcessorFeatureTypeDef

```python
from mypy_boto3_rds.type_defs import AvailableProcessorFeatureTypeDef
```




Optional fields:
- `Name`: `str`
- `DefaultValue`: `str`
- `AllowedValues`: `str`


## CertificateTypeDef

```python
from mypy_boto3_rds.type_defs import CertificateTypeDef
```




Optional fields:
- `CertificateIdentifier`: `str`
- `CertificateType`: `str`
- `Thumbprint`: `str`
- `ValidFrom`: `datetime`
- `ValidTill`: `datetime`
- `CertificateArn`: `str`
- `CustomerOverride`: `bool`
- `CustomerOverrideValidTill`: `datetime`


## CharacterSetTypeDef

```python
from mypy_boto3_rds.type_defs import CharacterSetTypeDef
```




Optional fields:
- `CharacterSetName`: `str`
- `CharacterSetDescription`: `str`


## ClusterPendingModifiedValuesTypeDef

```python
from mypy_boto3_rds.type_defs import ClusterPendingModifiedValuesTypeDef
```




Optional fields:
- `PendingCloudwatchLogsExports`: `"PendingCloudwatchLogsExportsTypeDef"`
- `DBClusterIdentifier`: `str`
- `MasterUserPassword`: `str`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `EngineVersion`: `str`


## ConnectionPoolConfigurationInfoTypeDef

```python
from mypy_boto3_rds.type_defs import ConnectionPoolConfigurationInfoTypeDef
```




Optional fields:
- `MaxConnectionsPercent`: `int`
- `MaxIdleConnectionsPercent`: `int`
- `ConnectionBorrowTimeout`: `int`
- `SessionPinningFilters`: `List[str]`
- `InitQuery`: `str`


## CustomAvailabilityZoneTypeDef

```python
from mypy_boto3_rds.type_defs import CustomAvailabilityZoneTypeDef
```




Optional fields:
- `CustomAvailabilityZoneId`: `str`
- `CustomAvailabilityZoneName`: `str`
- `CustomAvailabilityZoneStatus`: `str`
- `VpnDetails`: `"VpnDetailsTypeDef"`


## DBClusterBacktrackTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterBacktrackTypeDef
```




Optional fields:
- `DBClusterIdentifier`: `str`
- `BacktrackIdentifier`: `str`
- `BacktrackTo`: `datetime`
- `BacktrackedFrom`: `datetime`
- `BacktrackRequestCreationTime`: `datetime`
- `Status`: `str`


## DBClusterEndpointTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterEndpointTypeDef
```




Optional fields:
- `DBClusterEndpointIdentifier`: `str`
- `DBClusterIdentifier`: `str`
- `DBClusterEndpointResourceIdentifier`: `str`
- `Endpoint`: `str`
- `Status`: `str`
- `EndpointType`: `str`
- `CustomEndpointType`: `str`
- `StaticMembers`: `List[str]`
- `ExcludedMembers`: `List[str]`
- `DBClusterEndpointArn`: `str`


## DBClusterMemberTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterMemberTypeDef
```




Optional fields:
- `DBInstanceIdentifier`: `str`
- `IsClusterWriter`: `bool`
- `DBClusterParameterGroupStatus`: `str`
- `PromotionTier`: `int`


## DBClusterOptionGroupStatusTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterOptionGroupStatusTypeDef
```




Optional fields:
- `DBClusterOptionGroupName`: `str`
- `Status`: `str`


## DBClusterParameterGroupTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterParameterGroupTypeDef
```




Optional fields:
- `DBClusterParameterGroupName`: `str`
- `DBParameterGroupFamily`: `str`
- `Description`: `str`
- `DBClusterParameterGroupArn`: `str`


## DBClusterRoleTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterRoleTypeDef
```




Optional fields:
- `RoleArn`: `str`
- `Status`: `str`
- `FeatureName`: `str`


## DBClusterSnapshotAttributeTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterSnapshotAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValues`: `List[str]`


## DBClusterSnapshotAttributesResultTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterSnapshotAttributesResultTypeDef
```




Optional fields:
- `DBClusterSnapshotIdentifier`: `str`
- `DBClusterSnapshotAttributes`: `List["DBClusterSnapshotAttributeTypeDef"]`


## DBClusterSnapshotTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterSnapshotTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `DBClusterSnapshotIdentifier`: `str`
- `DBClusterIdentifier`: `str`
- `SnapshotCreateTime`: `datetime`
- `Engine`: `str`
- `EngineMode`: `str`
- `AllocatedStorage`: `int`
- `Status`: `str`
- `Port`: `int`
- `VpcId`: `str`
- `ClusterCreateTime`: `datetime`
- `MasterUsername`: `str`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `SnapshotType`: `str`
- `PercentProgress`: `int`
- `StorageEncrypted`: `bool`
- `KmsKeyId`: `str`
- `DBClusterSnapshotArn`: `str`
- `SourceDBClusterSnapshotArn`: `str`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `TagList`: `List["TagTypeDef"]`


## DBClusterTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterTypeDef
```




Optional fields:
- `AllocatedStorage`: `int`
- `AvailabilityZones`: `List[str]`
- `BackupRetentionPeriod`: `int`
- `CharacterSetName`: `str`
- `DatabaseName`: `str`
- `DBClusterIdentifier`: `str`
- `DBClusterParameterGroup`: `str`
- `DBSubnetGroup`: `str`
- `Status`: `str`
- `PercentProgress`: `str`
- `EarliestRestorableTime`: `datetime`
- `Endpoint`: `str`
- `ReaderEndpoint`: `str`
- `CustomEndpoints`: `List[str]`
- `MultiAZ`: `bool`
- `Engine`: `str`
- `EngineVersion`: `str`
- `LatestRestorableTime`: `datetime`
- `Port`: `int`
- `MasterUsername`: `str`
- `DBClusterOptionGroupMemberships`: `List["DBClusterOptionGroupStatusTypeDef"]`
- `PreferredBackupWindow`: `str`
- `PreferredMaintenanceWindow`: `str`
- `ReplicationSourceIdentifier`: `str`
- `ReadReplicaIdentifiers`: `List[str]`
- `DBClusterMembers`: `List["DBClusterMemberTypeDef"]`
- `VpcSecurityGroups`: `List["VpcSecurityGroupMembershipTypeDef"]`
- `HostedZoneId`: `str`
- `StorageEncrypted`: `bool`
- `KmsKeyId`: `str`
- `DbClusterResourceId`: `str`
- `DBClusterArn`: `str`
- `AssociatedRoles`: `List["DBClusterRoleTypeDef"]`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `CloneGroupId`: `str`
- `ClusterCreateTime`: `datetime`
- `EarliestBacktrackTime`: `datetime`
- `BacktrackWindow`: `int`
- `BacktrackConsumedChangeRecords`: `int`
- `EnabledCloudwatchLogsExports`: `List[str]`
- `Capacity`: `int`
- `EngineMode`: `str`
- `ScalingConfigurationInfo`: `"ScalingConfigurationInfoTypeDef"`
- `DeletionProtection`: `bool`
- `HttpEndpointEnabled`: `bool`
- `ActivityStreamMode`: `ActivityStreamMode`
- `ActivityStreamStatus`: `ActivityStreamStatus`
- `ActivityStreamKmsKeyId`: `str`
- `ActivityStreamKinesisStreamName`: `str`
- `CopyTagsToSnapshot`: `bool`
- `CrossAccountClone`: `bool`
- `DomainMemberships`: `List["DomainMembershipTypeDef"]`
- `TagList`: `List["TagTypeDef"]`
- `GlobalWriteForwardingStatus`: `WriteForwardingStatus`
- `GlobalWriteForwardingRequested`: `bool`
- `PendingModifiedValues`: `"ClusterPendingModifiedValuesTypeDef"`


## DBEngineVersionTypeDef

```python
from mypy_boto3_rds.type_defs import DBEngineVersionTypeDef
```




Optional fields:
- `Engine`: `str`
- `EngineVersion`: `str`
- `DBParameterGroupFamily`: `str`
- `DBEngineDescription`: `str`
- `DBEngineVersionDescription`: `str`
- `DefaultCharacterSet`: `"CharacterSetTypeDef"`
- `SupportedCharacterSets`: `List["CharacterSetTypeDef"]`
- `SupportedNcharCharacterSets`: `List["CharacterSetTypeDef"]`
- `ValidUpgradeTarget`: `List["UpgradeTargetTypeDef"]`
- `SupportedTimezones`: `List["TimezoneTypeDef"]`
- `ExportableLogTypes`: `List[str]`
- `SupportsLogExportsToCloudwatchLogs`: `bool`
- `SupportsReadReplica`: `bool`
- `SupportedEngineModes`: `List[str]`
- `SupportedFeatureNames`: `List[str]`
- `Status`: `str`
- `SupportsParallelQuery`: `bool`
- `SupportsGlobalDatabases`: `bool`


## DBInstanceAutomatedBackupTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceAutomatedBackupTypeDef
```




Optional fields:
- `DBInstanceArn`: `str`
- `DbiResourceId`: `str`
- `Region`: `str`
- `DBInstanceIdentifier`: `str`
- `RestoreWindow`: `"RestoreWindowTypeDef"`
- `AllocatedStorage`: `int`
- `Status`: `str`
- `Port`: `int`
- `AvailabilityZone`: `str`
- `VpcId`: `str`
- `InstanceCreateTime`: `datetime`
- `MasterUsername`: `str`
- `Engine`: `str`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `Iops`: `int`
- `OptionGroupName`: `str`
- `TdeCredentialArn`: `str`
- `Encrypted`: `bool`
- `StorageType`: `str`
- `KmsKeyId`: `str`
- `Timezone`: `str`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `BackupRetentionPeriod`: `int`
- `DBInstanceAutomatedBackupsArn`: `str`
- `DBInstanceAutomatedBackupsReplications`: `List["DBInstanceAutomatedBackupsReplicationTypeDef"]`


## DBInstanceAutomatedBackupsReplicationTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceAutomatedBackupsReplicationTypeDef
```




Optional fields:
- `DBInstanceAutomatedBackupsArn`: `str`


## DBInstanceRoleTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceRoleTypeDef
```




Optional fields:
- `RoleArn`: `str`
- `FeatureName`: `str`
- `Status`: `str`


## DBInstanceStatusInfoTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceStatusInfoTypeDef
```




Optional fields:
- `StatusType`: `str`
- `Normal`: `bool`
- `Status`: `str`
- `Message`: `str`


## DBInstanceTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceTypeDef
```




Optional fields:
- `DBInstanceIdentifier`: `str`
- `DBInstanceClass`: `str`
- `Engine`: `str`
- `DBInstanceStatus`: `str`
- `MasterUsername`: `str`
- `DBName`: `str`
- `Endpoint`: `"EndpointTypeDef"`
- `AllocatedStorage`: `int`
- `InstanceCreateTime`: `datetime`
- `PreferredBackupWindow`: `str`
- `BackupRetentionPeriod`: `int`
- `DBSecurityGroups`: `List["DBSecurityGroupMembershipTypeDef"]`
- `VpcSecurityGroups`: `List["VpcSecurityGroupMembershipTypeDef"]`
- `DBParameterGroups`: `List["DBParameterGroupStatusTypeDef"]`
- `AvailabilityZone`: `str`
- `DBSubnetGroup`: `"DBSubnetGroupTypeDef"`
- `PreferredMaintenanceWindow`: `str`
- `PendingModifiedValues`: `"PendingModifiedValuesTypeDef"`
- `LatestRestorableTime`: `datetime`
- `MultiAZ`: `bool`
- `EngineVersion`: `str`
- `AutoMinorVersionUpgrade`: `bool`
- `ReadReplicaSourceDBInstanceIdentifier`: `str`
- `ReadReplicaDBInstanceIdentifiers`: `List[str]`
- `ReadReplicaDBClusterIdentifiers`: `List[str]`
- `ReplicaMode`: `ReplicaMode`
- `LicenseModel`: `str`
- `Iops`: `int`
- `OptionGroupMemberships`: `List["OptionGroupMembershipTypeDef"]`
- `CharacterSetName`: `str`
- `NcharCharacterSetName`: `str`
- `SecondaryAvailabilityZone`: `str`
- `PubliclyAccessible`: `bool`
- `StatusInfos`: `List["DBInstanceStatusInfoTypeDef"]`
- `StorageType`: `str`
- `TdeCredentialArn`: `str`
- `DbInstancePort`: `int`
- `DBClusterIdentifier`: `str`
- `StorageEncrypted`: `bool`
- `KmsKeyId`: `str`
- `DbiResourceId`: `str`
- `CACertificateIdentifier`: `str`
- `DomainMemberships`: `List["DomainMembershipTypeDef"]`
- `CopyTagsToSnapshot`: `bool`
- `MonitoringInterval`: `int`
- `EnhancedMonitoringResourceArn`: `str`
- `MonitoringRoleArn`: `str`
- `PromotionTier`: `int`
- `DBInstanceArn`: `str`
- `Timezone`: `str`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `PerformanceInsightsEnabled`: `bool`
- `PerformanceInsightsKMSKeyId`: `str`
- `PerformanceInsightsRetentionPeriod`: `int`
- `EnabledCloudwatchLogsExports`: `List[str]`
- `ProcessorFeatures`: `List["ProcessorFeatureTypeDef"]`
- `DeletionProtection`: `bool`
- `AssociatedRoles`: `List["DBInstanceRoleTypeDef"]`
- `ListenerEndpoint`: `"EndpointTypeDef"`
- `MaxAllocatedStorage`: `int`
- `TagList`: `List["TagTypeDef"]`
- `DBInstanceAutomatedBackupsReplications`: `List["DBInstanceAutomatedBackupsReplicationTypeDef"]`
- `CustomerOwnedIpEnabled`: `bool`
- `AwsBackupRecoveryPointArn`: `str`


## DBParameterGroupStatusTypeDef

```python
from mypy_boto3_rds.type_defs import DBParameterGroupStatusTypeDef
```




Optional fields:
- `DBParameterGroupName`: `str`
- `ParameterApplyStatus`: `str`


## DBParameterGroupTypeDef

```python
from mypy_boto3_rds.type_defs import DBParameterGroupTypeDef
```




Optional fields:
- `DBParameterGroupName`: `str`
- `DBParameterGroupFamily`: `str`
- `Description`: `str`
- `DBParameterGroupArn`: `str`


## DBProxyEndpointTypeDef

```python
from mypy_boto3_rds.type_defs import DBProxyEndpointTypeDef
```




Optional fields:
- `DBProxyEndpointName`: `str`
- `DBProxyEndpointArn`: `str`
- `DBProxyName`: `str`
- `Status`: `DBProxyEndpointStatus`
- `VpcId`: `str`
- `VpcSecurityGroupIds`: `List[str]`
- `VpcSubnetIds`: `List[str]`
- `Endpoint`: `str`
- `CreatedDate`: `datetime`
- `TargetRole`: `DBProxyEndpointTargetRole`
- `IsDefault`: `bool`


## DBProxyTargetGroupTypeDef

```python
from mypy_boto3_rds.type_defs import DBProxyTargetGroupTypeDef
```




Optional fields:
- `DBProxyName`: `str`
- `TargetGroupName`: `str`
- `TargetGroupArn`: `str`
- `IsDefault`: `bool`
- `Status`: `str`
- `ConnectionPoolConfig`: `"ConnectionPoolConfigurationInfoTypeDef"`
- `CreatedDate`: `datetime`
- `UpdatedDate`: `datetime`


## DBProxyTargetTypeDef

```python
from mypy_boto3_rds.type_defs import DBProxyTargetTypeDef
```




Optional fields:
- `TargetArn`: `str`
- `Endpoint`: `str`
- `TrackedClusterId`: `str`
- `RdsResourceId`: `str`
- `Port`: `int`
- `Type`: `TargetType`
- `Role`: `TargetRole`
- `TargetHealth`: `"TargetHealthTypeDef"`


## DBProxyTypeDef

```python
from mypy_boto3_rds.type_defs import DBProxyTypeDef
```




Optional fields:
- `DBProxyName`: `str`
- `DBProxyArn`: `str`
- `Status`: `DBProxyStatus`
- `EngineFamily`: `str`
- `VpcId`: `str`
- `VpcSecurityGroupIds`: `List[str]`
- `VpcSubnetIds`: `List[str]`
- `Auth`: `List["UserAuthConfigInfoTypeDef"]`
- `RoleArn`: `str`
- `Endpoint`: `str`
- `RequireTLS`: `bool`
- `IdleClientTimeout`: `int`
- `DebugLogging`: `bool`
- `CreatedDate`: `datetime`
- `UpdatedDate`: `datetime`


## DBSecurityGroupMembershipTypeDef

```python
from mypy_boto3_rds.type_defs import DBSecurityGroupMembershipTypeDef
```




Optional fields:
- `DBSecurityGroupName`: `str`
- `Status`: `str`


## DBSecurityGroupTypeDef

```python
from mypy_boto3_rds.type_defs import DBSecurityGroupTypeDef
```




Optional fields:
- `OwnerId`: `str`
- `DBSecurityGroupName`: `str`
- `DBSecurityGroupDescription`: `str`
- `VpcId`: `str`
- `EC2SecurityGroups`: `List["EC2SecurityGroupTypeDef"]`
- `IPRanges`: `List["IPRangeTypeDef"]`
- `DBSecurityGroupArn`: `str`


## DBSnapshotAttributeTypeDef

```python
from mypy_boto3_rds.type_defs import DBSnapshotAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValues`: `List[str]`


## DBSnapshotAttributesResultTypeDef

```python
from mypy_boto3_rds.type_defs import DBSnapshotAttributesResultTypeDef
```




Optional fields:
- `DBSnapshotIdentifier`: `str`
- `DBSnapshotAttributes`: `List["DBSnapshotAttributeTypeDef"]`


## DBSnapshotTypeDef

```python
from mypy_boto3_rds.type_defs import DBSnapshotTypeDef
```




Optional fields:
- `DBSnapshotIdentifier`: `str`
- `DBInstanceIdentifier`: `str`
- `SnapshotCreateTime`: `datetime`
- `Engine`: `str`
- `AllocatedStorage`: `int`
- `Status`: `str`
- `Port`: `int`
- `AvailabilityZone`: `str`
- `VpcId`: `str`
- `InstanceCreateTime`: `datetime`
- `MasterUsername`: `str`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `SnapshotType`: `str`
- `Iops`: `int`
- `OptionGroupName`: `str`
- `PercentProgress`: `int`
- `SourceRegion`: `str`
- `SourceDBSnapshotIdentifier`: `str`
- `StorageType`: `str`
- `TdeCredentialArn`: `str`
- `Encrypted`: `bool`
- `KmsKeyId`: `str`
- `DBSnapshotArn`: `str`
- `Timezone`: `str`
- `IAMDatabaseAuthenticationEnabled`: `bool`
- `ProcessorFeatures`: `List["ProcessorFeatureTypeDef"]`
- `DbiResourceId`: `str`
- `TagList`: `List["TagTypeDef"]`


## DBSubnetGroupTypeDef

```python
from mypy_boto3_rds.type_defs import DBSubnetGroupTypeDef
```




Optional fields:
- `DBSubnetGroupName`: `str`
- `DBSubnetGroupDescription`: `str`
- `VpcId`: `str`
- `SubnetGroupStatus`: `str`
- `Subnets`: `List["SubnetTypeDef"]`
- `DBSubnetGroupArn`: `str`


## DescribeDBLogFilesDetailsTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBLogFilesDetailsTypeDef
```




Optional fields:
- `LogFileName`: `str`
- `LastWritten`: `int`
- `Size`: `int`


## DomainMembershipTypeDef

```python
from mypy_boto3_rds.type_defs import DomainMembershipTypeDef
```




Optional fields:
- `Domain`: `str`
- `Status`: `str`
- `FQDN`: `str`
- `IAMRoleName`: `str`


## DoubleRangeTypeDef

```python
from mypy_boto3_rds.type_defs import DoubleRangeTypeDef
```




Optional fields:
- `From`: `float`
- `To`: `float`


## EC2SecurityGroupTypeDef

```python
from mypy_boto3_rds.type_defs import EC2SecurityGroupTypeDef
```




Optional fields:
- `Status`: `str`
- `EC2SecurityGroupName`: `str`
- `EC2SecurityGroupId`: `str`
- `EC2SecurityGroupOwnerId`: `str`


## EndpointTypeDef

```python
from mypy_boto3_rds.type_defs import EndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Port`: `int`
- `HostedZoneId`: `str`


## EngineDefaultsTypeDef

```python
from mypy_boto3_rds.type_defs import EngineDefaultsTypeDef
```




Optional fields:
- `DBParameterGroupFamily`: `str`
- `Marker`: `str`
- `Parameters`: `List["ParameterTypeDef"]`


## EventCategoriesMapTypeDef

```python
from mypy_boto3_rds.type_defs import EventCategoriesMapTypeDef
```




Optional fields:
- `SourceType`: `str`
- `EventCategories`: `List[str]`


## EventSubscriptionTypeDef

```python
from mypy_boto3_rds.type_defs import EventSubscriptionTypeDef
```




Optional fields:
- `CustomerAwsId`: `str`
- `CustSubscriptionId`: `str`
- `SnsTopicArn`: `str`
- `Status`: `str`
- `SubscriptionCreationTime`: `str`
- `SourceType`: `str`
- `SourceIdsList`: `List[str]`
- `EventCategoriesList`: `List[str]`
- `Enabled`: `bool`
- `EventSubscriptionArn`: `str`


## EventTypeDef

```python
from mypy_boto3_rds.type_defs import EventTypeDef
```




Optional fields:
- `SourceIdentifier`: `str`
- `SourceType`: `SourceType`
- `Message`: `str`
- `EventCategories`: `List[str]`
- `Date`: `datetime`
- `SourceArn`: `str`


## ExportTaskTypeDef

```python
from mypy_boto3_rds.type_defs import ExportTaskTypeDef
```




Optional fields:
- `ExportTaskIdentifier`: `str`
- `SourceArn`: `str`
- `ExportOnly`: `List[str]`
- `SnapshotTime`: `datetime`
- `TaskStartTime`: `datetime`
- `TaskEndTime`: `datetime`
- `S3Bucket`: `str`
- `S3Prefix`: `str`
- `IamRoleArn`: `str`
- `KmsKeyId`: `str`
- `Status`: `str`
- `PercentProgress`: `int`
- `TotalExtractedDataInGB`: `int`
- `FailureCause`: `str`
- `WarningMessage`: `str`


## FailoverStateTypeDef

```python
from mypy_boto3_rds.type_defs import FailoverStateTypeDef
```




Optional fields:
- `Status`: `FailoverStatus`
- `FromDbClusterArn`: `str`
- `ToDbClusterArn`: `str`


## GlobalClusterMemberTypeDef

```python
from mypy_boto3_rds.type_defs import GlobalClusterMemberTypeDef
```




Optional fields:
- `DBClusterArn`: `str`
- `Readers`: `List[str]`
- `IsWriter`: `bool`
- `GlobalWriteForwardingStatus`: `WriteForwardingStatus`


## GlobalClusterTypeDef

```python
from mypy_boto3_rds.type_defs import GlobalClusterTypeDef
```




Optional fields:
- `GlobalClusterIdentifier`: `str`
- `GlobalClusterResourceId`: `str`
- `GlobalClusterArn`: `str`
- `Status`: `str`
- `Engine`: `str`
- `EngineVersion`: `str`
- `DatabaseName`: `str`
- `StorageEncrypted`: `bool`
- `DeletionProtection`: `bool`
- `GlobalClusterMembers`: `List["GlobalClusterMemberTypeDef"]`
- `FailoverState`: `"FailoverStateTypeDef"`


## IPRangeTypeDef

```python
from mypy_boto3_rds.type_defs import IPRangeTypeDef
```




Optional fields:
- `Status`: `str`
- `CIDRIP`: `str`


## InstallationMediaFailureCauseTypeDef

```python
from mypy_boto3_rds.type_defs import InstallationMediaFailureCauseTypeDef
```




Optional fields:
- `Message`: `str`


## InstallationMediaTypeDef

```python
from mypy_boto3_rds.type_defs import InstallationMediaTypeDef
```




Optional fields:
- `InstallationMediaId`: `str`
- `CustomAvailabilityZoneId`: `str`
- `Engine`: `str`
- `EngineVersion`: `str`
- `EngineInstallationMediaPath`: `str`
- `OSInstallationMediaPath`: `str`
- `Status`: `str`
- `FailureCause`: `"InstallationMediaFailureCauseTypeDef"`


## MinimumEngineVersionPerAllowedValueTypeDef

```python
from mypy_boto3_rds.type_defs import MinimumEngineVersionPerAllowedValueTypeDef
```




Optional fields:
- `AllowedValue`: `str`
- `MinimumEngineVersion`: `str`


## OptionGroupMembershipTypeDef

```python
from mypy_boto3_rds.type_defs import OptionGroupMembershipTypeDef
```




Optional fields:
- `OptionGroupName`: `str`
- `Status`: `str`


## OptionGroupOptionSettingTypeDef

```python
from mypy_boto3_rds.type_defs import OptionGroupOptionSettingTypeDef
```




Optional fields:
- `SettingName`: `str`
- `SettingDescription`: `str`
- `DefaultValue`: `str`
- `ApplyType`: `str`
- `AllowedValues`: `str`
- `IsModifiable`: `bool`
- `IsRequired`: `bool`
- `MinimumEngineVersionPerAllowedValue`: `List["MinimumEngineVersionPerAllowedValueTypeDef"]`


## OptionGroupOptionTypeDef

```python
from mypy_boto3_rds.type_defs import OptionGroupOptionTypeDef
```




Optional fields:
- `Name`: `str`
- `Description`: `str`
- `EngineName`: `str`
- `MajorEngineVersion`: `str`
- `MinimumRequiredMinorEngineVersion`: `str`
- `PortRequired`: `bool`
- `DefaultPort`: `int`
- `OptionsDependedOn`: `List[str]`
- `OptionsConflictsWith`: `List[str]`
- `Persistent`: `bool`
- `Permanent`: `bool`
- `RequiresAutoMinorEngineVersionUpgrade`: `bool`
- `VpcOnly`: `bool`
- `SupportsOptionVersionDowngrade`: `bool`
- `OptionGroupOptionSettings`: `List["OptionGroupOptionSettingTypeDef"]`
- `OptionGroupOptionVersions`: `List["OptionVersionTypeDef"]`


## OptionGroupTypeDef

```python
from mypy_boto3_rds.type_defs import OptionGroupTypeDef
```




Optional fields:
- `OptionGroupName`: `str`
- `OptionGroupDescription`: `str`
- `EngineName`: `str`
- `MajorEngineVersion`: `str`
- `Options`: `List["OptionTypeDef"]`
- `AllowsVpcAndNonVpcInstanceMemberships`: `bool`
- `VpcId`: `str`
- `OptionGroupArn`: `str`


## OptionSettingTypeDef

```python
from mypy_boto3_rds.type_defs import OptionSettingTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`
- `DefaultValue`: `str`
- `Description`: `str`
- `ApplyType`: `str`
- `DataType`: `str`
- `AllowedValues`: `str`
- `IsModifiable`: `bool`
- `IsCollection`: `bool`


## OptionTypeDef

```python
from mypy_boto3_rds.type_defs import OptionTypeDef
```




Optional fields:
- `OptionName`: `str`
- `OptionDescription`: `str`
- `Persistent`: `bool`
- `Permanent`: `bool`
- `Port`: `int`
- `OptionVersion`: `str`
- `OptionSettings`: `List["OptionSettingTypeDef"]`
- `DBSecurityGroupMemberships`: `List["DBSecurityGroupMembershipTypeDef"]`
- `VpcSecurityGroupMemberships`: `List["VpcSecurityGroupMembershipTypeDef"]`


## OptionVersionTypeDef

```python
from mypy_boto3_rds.type_defs import OptionVersionTypeDef
```




Optional fields:
- `Version`: `str`
- `IsDefault`: `bool`


## OrderableDBInstanceOptionTypeDef

```python
from mypy_boto3_rds.type_defs import OrderableDBInstanceOptionTypeDef
```




Optional fields:
- `Engine`: `str`
- `EngineVersion`: `str`
- `DBInstanceClass`: `str`
- `LicenseModel`: `str`
- `AvailabilityZoneGroup`: `str`
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`
- `MultiAZCapable`: `bool`
- `ReadReplicaCapable`: `bool`
- `Vpc`: `bool`
- `SupportsStorageEncryption`: `bool`
- `StorageType`: `str`
- `SupportsIops`: `bool`
- `SupportsEnhancedMonitoring`: `bool`
- `SupportsIAMDatabaseAuthentication`: `bool`
- `SupportsPerformanceInsights`: `bool`
- `MinStorageSize`: `int`
- `MaxStorageSize`: `int`
- `MinIopsPerDbInstance`: `int`
- `MaxIopsPerDbInstance`: `int`
- `MinIopsPerGib`: `float`
- `MaxIopsPerGib`: `float`
- `AvailableProcessorFeatures`: `List["AvailableProcessorFeatureTypeDef"]`
- `SupportedEngineModes`: `List[str]`
- `SupportsStorageAutoscaling`: `bool`
- `SupportsKerberosAuthentication`: `bool`
- `OutpostCapable`: `bool`
- `SupportsGlobalDatabases`: `bool`


## OutpostTypeDef

```python
from mypy_boto3_rds.type_defs import OutpostTypeDef
```




Optional fields:
- `Arn`: `str`


## ParameterTypeDef

```python
from mypy_boto3_rds.type_defs import ParameterTypeDef
```




Optional fields:
- `ParameterName`: `str`
- `ParameterValue`: `str`
- `Description`: `str`
- `Source`: `str`
- `ApplyType`: `str`
- `DataType`: `str`
- `AllowedValues`: `str`
- `IsModifiable`: `bool`
- `MinimumEngineVersion`: `str`
- `ApplyMethod`: `ApplyMethod`
- `SupportedEngineModes`: `List[str]`


## PendingCloudwatchLogsExportsTypeDef

```python
from mypy_boto3_rds.type_defs import PendingCloudwatchLogsExportsTypeDef
```




Optional fields:
- `LogTypesToEnable`: `List[str]`
- `LogTypesToDisable`: `List[str]`


## PendingMaintenanceActionTypeDef

```python
from mypy_boto3_rds.type_defs import PendingMaintenanceActionTypeDef
```




Optional fields:
- `Action`: `str`
- `AutoAppliedAfterDate`: `datetime`
- `ForcedApplyDate`: `datetime`
- `OptInStatus`: `str`
- `CurrentApplyDate`: `datetime`
- `Description`: `str`


## PendingModifiedValuesTypeDef

```python
from mypy_boto3_rds.type_defs import PendingModifiedValuesTypeDef
```




Optional fields:
- `DBInstanceClass`: `str`
- `AllocatedStorage`: `int`
- `MasterUserPassword`: `str`
- `Port`: `int`
- `BackupRetentionPeriod`: `int`
- `MultiAZ`: `bool`
- `EngineVersion`: `str`
- `LicenseModel`: `str`
- `Iops`: `int`
- `DBInstanceIdentifier`: `str`
- `StorageType`: `str`
- `CACertificateIdentifier`: `str`
- `DBSubnetGroupName`: `str`
- `PendingCloudwatchLogsExports`: `"PendingCloudwatchLogsExportsTypeDef"`
- `ProcessorFeatures`: `List["ProcessorFeatureTypeDef"]`
- `IAMDatabaseAuthenticationEnabled`: `bool`


## ProcessorFeatureTypeDef

```python
from mypy_boto3_rds.type_defs import ProcessorFeatureTypeDef
```




Optional fields:
- `Name`: `str`
- `Value`: `str`


## RangeTypeDef

```python
from mypy_boto3_rds.type_defs import RangeTypeDef
```




Optional fields:
- `From`: `int`
- `To`: `int`
- `Step`: `int`


## RecurringChargeTypeDef

```python
from mypy_boto3_rds.type_defs import RecurringChargeTypeDef
```




Optional fields:
- `RecurringChargeAmount`: `float`
- `RecurringChargeFrequency`: `str`


## ReservedDBInstanceTypeDef

```python
from mypy_boto3_rds.type_defs import ReservedDBInstanceTypeDef
```




Optional fields:
- `ReservedDBInstanceId`: `str`
- `ReservedDBInstancesOfferingId`: `str`
- `DBInstanceClass`: `str`
- `StartTime`: `datetime`
- `Duration`: `int`
- `FixedPrice`: `float`
- `UsagePrice`: `float`
- `CurrencyCode`: `str`
- `DBInstanceCount`: `int`
- `ProductDescription`: `str`
- `OfferingType`: `str`
- `MultiAZ`: `bool`
- `State`: `str`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`
- `ReservedDBInstanceArn`: `str`
- `LeaseId`: `str`


## ReservedDBInstancesOfferingTypeDef

```python
from mypy_boto3_rds.type_defs import ReservedDBInstancesOfferingTypeDef
```




Optional fields:
- `ReservedDBInstancesOfferingId`: `str`
- `DBInstanceClass`: `str`
- `Duration`: `int`
- `FixedPrice`: `float`
- `UsagePrice`: `float`
- `CurrencyCode`: `str`
- `ProductDescription`: `str`
- `OfferingType`: `str`
- `MultiAZ`: `bool`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`


## ResourcePendingMaintenanceActionsTypeDef

```python
from mypy_boto3_rds.type_defs import ResourcePendingMaintenanceActionsTypeDef
```




Optional fields:
- `ResourceIdentifier`: `str`
- `PendingMaintenanceActionDetails`: `List["PendingMaintenanceActionTypeDef"]`


## RestoreWindowTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreWindowTypeDef
```




Optional fields:
- `EarliestTime`: `datetime`
- `LatestTime`: `datetime`


## ScalingConfigurationInfoTypeDef

```python
from mypy_boto3_rds.type_defs import ScalingConfigurationInfoTypeDef
```




Optional fields:
- `MinCapacity`: `int`
- `MaxCapacity`: `int`
- `AutoPause`: `bool`
- `SecondsUntilAutoPause`: `int`
- `TimeoutAction`: `str`


## SourceRegionTypeDef

```python
from mypy_boto3_rds.type_defs import SourceRegionTypeDef
```




Optional fields:
- `RegionName`: `str`
- `Endpoint`: `str`
- `Status`: `str`
- `SupportsDBInstanceAutomatedBackupsReplication`: `bool`


## SubnetTypeDef

```python
from mypy_boto3_rds.type_defs import SubnetTypeDef
```




Optional fields:
- `SubnetIdentifier`: `str`
- `SubnetAvailabilityZone`: `"AvailabilityZoneTypeDef"`
- `SubnetOutpost`: `"OutpostTypeDef"`
- `SubnetStatus`: `str`


## TagTypeDef

```python
from mypy_boto3_rds.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TargetHealthTypeDef

```python
from mypy_boto3_rds.type_defs import TargetHealthTypeDef
```




Optional fields:
- `State`: `TargetState`
- `Reason`: `TargetHealthReason`
- `Description`: `str`


## TimezoneTypeDef

```python
from mypy_boto3_rds.type_defs import TimezoneTypeDef
```




Optional fields:
- `TimezoneName`: `str`


## UpgradeTargetTypeDef

```python
from mypy_boto3_rds.type_defs import UpgradeTargetTypeDef
```




Optional fields:
- `Engine`: `str`
- `EngineVersion`: `str`
- `Description`: `str`
- `AutoUpgrade`: `bool`
- `IsMajorVersionUpgrade`: `bool`
- `SupportedEngineModes`: `List[str]`
- `SupportsParallelQuery`: `bool`
- `SupportsGlobalDatabases`: `bool`


## UserAuthConfigInfoTypeDef

```python
from mypy_boto3_rds.type_defs import UserAuthConfigInfoTypeDef
```




Optional fields:
- `Description`: `str`
- `UserName`: `str`
- `AuthScheme`: `AuthScheme`
- `SecretArn`: `str`
- `IAMAuth`: `IAMAuthMode`


## ValidDBInstanceModificationsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import ValidDBInstanceModificationsMessageTypeDef
```




Optional fields:
- `Storage`: `List["ValidStorageOptionsTypeDef"]`
- `ValidProcessorFeatures`: `List["AvailableProcessorFeatureTypeDef"]`


## ValidStorageOptionsTypeDef

```python
from mypy_boto3_rds.type_defs import ValidStorageOptionsTypeDef
```




Optional fields:
- `StorageType`: `str`
- `StorageSize`: `List["RangeTypeDef"]`
- `ProvisionedIops`: `List["RangeTypeDef"]`
- `IopsToStorageRatio`: `List["DoubleRangeTypeDef"]`
- `SupportsStorageAutoscaling`: `bool`


## VpcSecurityGroupMembershipTypeDef

```python
from mypy_boto3_rds.type_defs import VpcSecurityGroupMembershipTypeDef
```




Optional fields:
- `VpcSecurityGroupId`: `str`
- `Status`: `str`


## VpnDetailsTypeDef

```python
from mypy_boto3_rds.type_defs import VpnDetailsTypeDef
```




Optional fields:
- `VpnId`: `str`
- `VpnTunnelOriginatorIP`: `str`
- `VpnGatewayIp`: `str`
- `VpnPSK`: `str`
- `VpnName`: `str`
- `VpnState`: `str`


## AccountAttributesMessageTypeDef

```python
from mypy_boto3_rds.type_defs import AccountAttributesMessageTypeDef
```




Optional fields:
- `AccountQuotas`: `List["AccountQuotaTypeDef"]`


## AddSourceIdentifierToSubscriptionResultTypeDef

```python
from mypy_boto3_rds.type_defs import AddSourceIdentifierToSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## ApplyPendingMaintenanceActionResultTypeDef

```python
from mypy_boto3_rds.type_defs import ApplyPendingMaintenanceActionResultTypeDef
```




Optional fields:
- `ResourcePendingMaintenanceActions`: `"ResourcePendingMaintenanceActionsTypeDef"`


## AuthorizeDBSecurityGroupIngressResultTypeDef

```python
from mypy_boto3_rds.type_defs import AuthorizeDBSecurityGroupIngressResultTypeDef
```




Optional fields:
- `DBSecurityGroup`: `"DBSecurityGroupTypeDef"`


## CertificateMessageTypeDef

```python
from mypy_boto3_rds.type_defs import CertificateMessageTypeDef
```




Optional fields:
- `Certificates`: `List["CertificateTypeDef"]`
- `Marker`: `str`


## CloudwatchLogsExportConfigurationTypeDef

```python
from mypy_boto3_rds.type_defs import CloudwatchLogsExportConfigurationTypeDef
```




Optional fields:
- `EnableLogTypes`: `List[str]`
- `DisableLogTypes`: `List[str]`


## ConnectionPoolConfigurationTypeDef

```python
from mypy_boto3_rds.type_defs import ConnectionPoolConfigurationTypeDef
```




Optional fields:
- `MaxConnectionsPercent`: `int`
- `MaxIdleConnectionsPercent`: `int`
- `ConnectionBorrowTimeout`: `int`
- `SessionPinningFilters`: `List[str]`
- `InitQuery`: `str`


## CopyDBClusterParameterGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CopyDBClusterParameterGroupResultTypeDef
```




Optional fields:
- `DBClusterParameterGroup`: `"DBClusterParameterGroupTypeDef"`


## CopyDBClusterSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import CopyDBClusterSnapshotResultTypeDef
```




Optional fields:
- `DBClusterSnapshot`: `"DBClusterSnapshotTypeDef"`


## CopyDBParameterGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CopyDBParameterGroupResultTypeDef
```




Optional fields:
- `DBParameterGroup`: `"DBParameterGroupTypeDef"`


## CopyDBSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import CopyDBSnapshotResultTypeDef
```




Optional fields:
- `DBSnapshot`: `"DBSnapshotTypeDef"`


## CopyOptionGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CopyOptionGroupResultTypeDef
```




Optional fields:
- `OptionGroup`: `"OptionGroupTypeDef"`


## CreateCustomAvailabilityZoneResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateCustomAvailabilityZoneResultTypeDef
```




Optional fields:
- `CustomAvailabilityZone`: `"CustomAvailabilityZoneTypeDef"`


## CreateDBClusterParameterGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBClusterParameterGroupResultTypeDef
```




Optional fields:
- `DBClusterParameterGroup`: `"DBClusterParameterGroupTypeDef"`


## CreateDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## CreateDBClusterSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBClusterSnapshotResultTypeDef
```




Optional fields:
- `DBClusterSnapshot`: `"DBClusterSnapshotTypeDef"`


## CreateDBInstanceReadReplicaResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBInstanceReadReplicaResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## CreateDBInstanceResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## CreateDBParameterGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBParameterGroupResultTypeDef
```




Optional fields:
- `DBParameterGroup`: `"DBParameterGroupTypeDef"`


## CreateDBProxyEndpointResponseTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBProxyEndpointResponseTypeDef
```




Optional fields:
- `DBProxyEndpoint`: `"DBProxyEndpointTypeDef"`


## CreateDBProxyResponseTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBProxyResponseTypeDef
```




Optional fields:
- `DBProxy`: `"DBProxyTypeDef"`


## CreateDBSecurityGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBSecurityGroupResultTypeDef
```




Optional fields:
- `DBSecurityGroup`: `"DBSecurityGroupTypeDef"`


## CreateDBSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBSnapshotResultTypeDef
```




Optional fields:
- `DBSnapshot`: `"DBSnapshotTypeDef"`


## CreateDBSubnetGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateDBSubnetGroupResultTypeDef
```




Optional fields:
- `DBSubnetGroup`: `"DBSubnetGroupTypeDef"`


## CreateEventSubscriptionResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## CreateGlobalClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateGlobalClusterResultTypeDef
```




Optional fields:
- `GlobalCluster`: `"GlobalClusterTypeDef"`


## CreateOptionGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import CreateOptionGroupResultTypeDef
```




Optional fields:
- `OptionGroup`: `"OptionGroupTypeDef"`


## CustomAvailabilityZoneMessageTypeDef

```python
from mypy_boto3_rds.type_defs import CustomAvailabilityZoneMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `CustomAvailabilityZones`: `List["CustomAvailabilityZoneTypeDef"]`


## DBClusterBacktrackMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterBacktrackMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterBacktracks`: `List["DBClusterBacktrackTypeDef"]`


## DBClusterCapacityInfoTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterCapacityInfoTypeDef
```




Optional fields:
- `DBClusterIdentifier`: `str`
- `PendingCapacity`: `int`
- `CurrentCapacity`: `int`
- `SecondsBeforeTimeout`: `int`
- `TimeoutAction`: `str`


## DBClusterEndpointMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterEndpointMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterEndpoints`: `List["DBClusterEndpointTypeDef"]`


## DBClusterMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusters`: `List["DBClusterTypeDef"]`


## DBClusterParameterGroupDetailsTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterParameterGroupDetailsTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `Marker`: `str`


## DBClusterParameterGroupNameMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterParameterGroupNameMessageTypeDef
```




Optional fields:
- `DBClusterParameterGroupName`: `str`


## DBClusterParameterGroupsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterParameterGroupsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterParameterGroups`: `List["DBClusterParameterGroupTypeDef"]`


## DBClusterSnapshotMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBClusterSnapshotMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterSnapshots`: `List["DBClusterSnapshotTypeDef"]`


## DBEngineVersionMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBEngineVersionMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBEngineVersions`: `List["DBEngineVersionTypeDef"]`


## DBInstanceAutomatedBackupMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceAutomatedBackupMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBInstanceAutomatedBackups`: `List["DBInstanceAutomatedBackupTypeDef"]`


## DBInstanceMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBInstanceMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBInstances`: `List["DBInstanceTypeDef"]`


## DBParameterGroupDetailsTypeDef

```python
from mypy_boto3_rds.type_defs import DBParameterGroupDetailsTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `Marker`: `str`


## DBParameterGroupNameMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBParameterGroupNameMessageTypeDef
```




Optional fields:
- `DBParameterGroupName`: `str`


## DBParameterGroupsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBParameterGroupsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBParameterGroups`: `List["DBParameterGroupTypeDef"]`


## DBSecurityGroupMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBSecurityGroupMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBSecurityGroups`: `List["DBSecurityGroupTypeDef"]`


## DBSnapshotMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBSnapshotMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBSnapshots`: `List["DBSnapshotTypeDef"]`


## DBSubnetGroupMessageTypeDef

```python
from mypy_boto3_rds.type_defs import DBSubnetGroupMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBSubnetGroups`: `List["DBSubnetGroupTypeDef"]`


## DeleteCustomAvailabilityZoneResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteCustomAvailabilityZoneResultTypeDef
```




Optional fields:
- `CustomAvailabilityZone`: `"CustomAvailabilityZoneTypeDef"`


## DeleteDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## DeleteDBClusterSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBClusterSnapshotResultTypeDef
```




Optional fields:
- `DBClusterSnapshot`: `"DBClusterSnapshotTypeDef"`


## DeleteDBInstanceAutomatedBackupResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBInstanceAutomatedBackupResultTypeDef
```




Optional fields:
- `DBInstanceAutomatedBackup`: `"DBInstanceAutomatedBackupTypeDef"`


## DeleteDBInstanceResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## DeleteDBProxyEndpointResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBProxyEndpointResponseTypeDef
```




Optional fields:
- `DBProxyEndpoint`: `"DBProxyEndpointTypeDef"`


## DeleteDBProxyResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBProxyResponseTypeDef
```




Optional fields:
- `DBProxy`: `"DBProxyTypeDef"`


## DeleteDBSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteDBSnapshotResultTypeDef
```




Optional fields:
- `DBSnapshot`: `"DBSnapshotTypeDef"`


## DeleteEventSubscriptionResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## DeleteGlobalClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import DeleteGlobalClusterResultTypeDef
```




Optional fields:
- `GlobalCluster`: `"GlobalClusterTypeDef"`


## DescribeDBClusterSnapshotAttributesResultTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBClusterSnapshotAttributesResultTypeDef
```




Optional fields:
- `DBClusterSnapshotAttributesResult`: `"DBClusterSnapshotAttributesResultTypeDef"`


## DescribeDBLogFilesResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBLogFilesResponseTypeDef
```




Optional fields:
- `DescribeDBLogFiles`: `List["DescribeDBLogFilesDetailsTypeDef"]`
- `Marker`: `str`


## DescribeDBProxiesResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBProxiesResponseTypeDef
```




Optional fields:
- `DBProxies`: `List["DBProxyTypeDef"]`
- `Marker`: `str`


## DescribeDBProxyEndpointsResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBProxyEndpointsResponseTypeDef
```




Optional fields:
- `DBProxyEndpoints`: `List["DBProxyEndpointTypeDef"]`
- `Marker`: `str`


## DescribeDBProxyTargetGroupsResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBProxyTargetGroupsResponseTypeDef
```




Optional fields:
- `TargetGroups`: `List["DBProxyTargetGroupTypeDef"]`
- `Marker`: `str`


## DescribeDBProxyTargetsResponseTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBProxyTargetsResponseTypeDef
```




Optional fields:
- `Targets`: `List["DBProxyTargetTypeDef"]`
- `Marker`: `str`


## DescribeDBSnapshotAttributesResultTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeDBSnapshotAttributesResultTypeDef
```




Optional fields:
- `DBSnapshotAttributesResult`: `"DBSnapshotAttributesResultTypeDef"`


## DescribeEngineDefaultClusterParametersResultTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeEngineDefaultClusterParametersResultTypeDef
```




Optional fields:
- `EngineDefaults`: `"EngineDefaultsTypeDef"`


## DescribeEngineDefaultParametersResultTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeEngineDefaultParametersResultTypeDef
```




Optional fields:
- `EngineDefaults`: `"EngineDefaultsTypeDef"`


## DescribeValidDBInstanceModificationsResultTypeDef

```python
from mypy_boto3_rds.type_defs import DescribeValidDBInstanceModificationsResultTypeDef
```




Optional fields:
- `ValidDBInstanceModificationsMessage`: `"ValidDBInstanceModificationsMessageTypeDef"`


## DownloadDBLogFilePortionDetailsTypeDef

```python
from mypy_boto3_rds.type_defs import DownloadDBLogFilePortionDetailsTypeDef
```




Optional fields:
- `LogFileData`: `str`
- `Marker`: `str`
- `AdditionalDataPending`: `bool`


## EventCategoriesMessageTypeDef

```python
from mypy_boto3_rds.type_defs import EventCategoriesMessageTypeDef
```




Optional fields:
- `EventCategoriesMapList`: `List["EventCategoriesMapTypeDef"]`


## EventSubscriptionsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import EventSubscriptionsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `EventSubscriptionsList`: `List["EventSubscriptionTypeDef"]`


## EventsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import EventsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `Events`: `List["EventTypeDef"]`


## ExportTasksMessageTypeDef

```python
from mypy_boto3_rds.type_defs import ExportTasksMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ExportTasks`: `List["ExportTaskTypeDef"]`


## FailoverDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import FailoverDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## FailoverGlobalClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import FailoverGlobalClusterResultTypeDef
```




Optional fields:
- `GlobalCluster`: `"GlobalClusterTypeDef"`


## FilterTypeDef

```python
from mypy_boto3_rds.type_defs import FilterTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[str]`




## GlobalClustersMessageTypeDef

```python
from mypy_boto3_rds.type_defs import GlobalClustersMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `GlobalClusters`: `List["GlobalClusterTypeDef"]`


## InstallationMediaMessageTypeDef

```python
from mypy_boto3_rds.type_defs import InstallationMediaMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `InstallationMedia`: `List["InstallationMediaTypeDef"]`


## ModifyCertificatesResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyCertificatesResultTypeDef
```




Optional fields:
- `Certificate`: `"CertificateTypeDef"`


## ModifyDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## ModifyDBClusterSnapshotAttributeResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBClusterSnapshotAttributeResultTypeDef
```




Optional fields:
- `DBClusterSnapshotAttributesResult`: `"DBClusterSnapshotAttributesResultTypeDef"`


## ModifyDBInstanceResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## ModifyDBProxyEndpointResponseTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBProxyEndpointResponseTypeDef
```




Optional fields:
- `DBProxyEndpoint`: `"DBProxyEndpointTypeDef"`


## ModifyDBProxyResponseTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBProxyResponseTypeDef
```




Optional fields:
- `DBProxy`: `"DBProxyTypeDef"`


## ModifyDBProxyTargetGroupResponseTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBProxyTargetGroupResponseTypeDef
```




Optional fields:
- `DBProxyTargetGroup`: `"DBProxyTargetGroupTypeDef"`


## ModifyDBSnapshotAttributeResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBSnapshotAttributeResultTypeDef
```




Optional fields:
- `DBSnapshotAttributesResult`: `"DBSnapshotAttributesResultTypeDef"`


## ModifyDBSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBSnapshotResultTypeDef
```




Optional fields:
- `DBSnapshot`: `"DBSnapshotTypeDef"`


## ModifyDBSubnetGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyDBSubnetGroupResultTypeDef
```




Optional fields:
- `DBSubnetGroup`: `"DBSubnetGroupTypeDef"`


## ModifyEventSubscriptionResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## ModifyGlobalClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyGlobalClusterResultTypeDef
```




Optional fields:
- `GlobalCluster`: `"GlobalClusterTypeDef"`


## ModifyOptionGroupResultTypeDef

```python
from mypy_boto3_rds.type_defs import ModifyOptionGroupResultTypeDef
```




Optional fields:
- `OptionGroup`: `"OptionGroupTypeDef"`


## OptionConfigurationTypeDef

```python
from mypy_boto3_rds.type_defs import OptionConfigurationTypeDef
```


Required fields:
- `OptionName`: `str`



Optional fields:
- `Port`: `int`
- `OptionVersion`: `str`
- `DBSecurityGroupMemberships`: `List[str]`
- `VpcSecurityGroupMemberships`: `List[str]`
- `OptionSettings`: `List["OptionSettingTypeDef"]`


## OptionGroupOptionsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import OptionGroupOptionsMessageTypeDef
```




Optional fields:
- `OptionGroupOptions`: `List["OptionGroupOptionTypeDef"]`
- `Marker`: `str`


## OptionGroupsTypeDef

```python
from mypy_boto3_rds.type_defs import OptionGroupsTypeDef
```




Optional fields:
- `OptionGroupsList`: `List["OptionGroupTypeDef"]`
- `Marker`: `str`


## OrderableDBInstanceOptionsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import OrderableDBInstanceOptionsMessageTypeDef
```




Optional fields:
- `OrderableDBInstanceOptions`: `List["OrderableDBInstanceOptionTypeDef"]`
- `Marker`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_rds.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PendingMaintenanceActionsMessageTypeDef

```python
from mypy_boto3_rds.type_defs import PendingMaintenanceActionsMessageTypeDef
```




Optional fields:
- `PendingMaintenanceActions`: `List["ResourcePendingMaintenanceActionsTypeDef"]`
- `Marker`: `str`


## PromoteReadReplicaDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import PromoteReadReplicaDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## PromoteReadReplicaResultTypeDef

```python
from mypy_boto3_rds.type_defs import PromoteReadReplicaResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## PurchaseReservedDBInstancesOfferingResultTypeDef

```python
from mypy_boto3_rds.type_defs import PurchaseReservedDBInstancesOfferingResultTypeDef
```




Optional fields:
- `ReservedDBInstance`: `"ReservedDBInstanceTypeDef"`


## RebootDBInstanceResultTypeDef

```python
from mypy_boto3_rds.type_defs import RebootDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## RegisterDBProxyTargetsResponseTypeDef

```python
from mypy_boto3_rds.type_defs import RegisterDBProxyTargetsResponseTypeDef
```




Optional fields:
- `DBProxyTargets`: `List["DBProxyTargetTypeDef"]`


## RemoveFromGlobalClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import RemoveFromGlobalClusterResultTypeDef
```




Optional fields:
- `GlobalCluster`: `"GlobalClusterTypeDef"`


## RemoveSourceIdentifierFromSubscriptionResultTypeDef

```python
from mypy_boto3_rds.type_defs import RemoveSourceIdentifierFromSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## ReservedDBInstanceMessageTypeDef

```python
from mypy_boto3_rds.type_defs import ReservedDBInstanceMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ReservedDBInstances`: `List["ReservedDBInstanceTypeDef"]`


## ReservedDBInstancesOfferingMessageTypeDef

```python
from mypy_boto3_rds.type_defs import ReservedDBInstancesOfferingMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ReservedDBInstancesOfferings`: `List["ReservedDBInstancesOfferingTypeDef"]`


## RestoreDBClusterFromS3ResultTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreDBClusterFromS3ResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## RestoreDBClusterFromSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreDBClusterFromSnapshotResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## RestoreDBClusterToPointInTimeResultTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreDBClusterToPointInTimeResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## RestoreDBInstanceFromDBSnapshotResultTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreDBInstanceFromDBSnapshotResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## RestoreDBInstanceFromS3ResultTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreDBInstanceFromS3ResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## RestoreDBInstanceToPointInTimeResultTypeDef

```python
from mypy_boto3_rds.type_defs import RestoreDBInstanceToPointInTimeResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## RevokeDBSecurityGroupIngressResultTypeDef

```python
from mypy_boto3_rds.type_defs import RevokeDBSecurityGroupIngressResultTypeDef
```




Optional fields:
- `DBSecurityGroup`: `"DBSecurityGroupTypeDef"`


## ScalingConfigurationTypeDef

```python
from mypy_boto3_rds.type_defs import ScalingConfigurationTypeDef
```




Optional fields:
- `MinCapacity`: `int`
- `MaxCapacity`: `int`
- `AutoPause`: `bool`
- `SecondsUntilAutoPause`: `int`
- `TimeoutAction`: `str`


## SourceRegionMessageTypeDef

```python
from mypy_boto3_rds.type_defs import SourceRegionMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `SourceRegions`: `List["SourceRegionTypeDef"]`


## StartActivityStreamResponseTypeDef

```python
from mypy_boto3_rds.type_defs import StartActivityStreamResponseTypeDef
```




Optional fields:
- `KmsKeyId`: `str`
- `KinesisStreamName`: `str`
- `Status`: `ActivityStreamStatus`
- `Mode`: `ActivityStreamMode`
- `ApplyImmediately`: `bool`


## StartDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import StartDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## StartDBInstanceAutomatedBackupsReplicationResultTypeDef

```python
from mypy_boto3_rds.type_defs import StartDBInstanceAutomatedBackupsReplicationResultTypeDef
```




Optional fields:
- `DBInstanceAutomatedBackup`: `"DBInstanceAutomatedBackupTypeDef"`


## StartDBInstanceResultTypeDef

```python
from mypy_boto3_rds.type_defs import StartDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## StopActivityStreamResponseTypeDef

```python
from mypy_boto3_rds.type_defs import StopActivityStreamResponseTypeDef
```




Optional fields:
- `KmsKeyId`: `str`
- `KinesisStreamName`: `str`
- `Status`: `ActivityStreamStatus`


## StopDBClusterResultTypeDef

```python
from mypy_boto3_rds.type_defs import StopDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## StopDBInstanceAutomatedBackupsReplicationResultTypeDef

```python
from mypy_boto3_rds.type_defs import StopDBInstanceAutomatedBackupsReplicationResultTypeDef
```




Optional fields:
- `DBInstanceAutomatedBackup`: `"DBInstanceAutomatedBackupTypeDef"`


## StopDBInstanceResultTypeDef

```python
from mypy_boto3_rds.type_defs import StopDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## TagListMessageTypeDef

```python
from mypy_boto3_rds.type_defs import TagListMessageTypeDef
```




Optional fields:
- `TagList`: `List["TagTypeDef"]`


## UserAuthConfigTypeDef

```python
from mypy_boto3_rds.type_defs import UserAuthConfigTypeDef
```




Optional fields:
- `Description`: `str`
- `UserName`: `str`
- `AuthScheme`: `AuthScheme`
- `SecretArn`: `str`
- `IAMAuth`: `IAMAuthMode`


## WaiterConfigTypeDef

```python
from mypy_boto3_rds.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

