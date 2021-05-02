# Structures for boto3 Neptune module

> [Index](../index.md) > [Neptune](./index.md) > Structures

Auto-generated documentation for [Neptune](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html#Neptune)
type annotations stubs module [mypy_boto3_neptune](https://pypi.org/project/mypy-boto3-neptune/).

- [Structures for boto3 Neptune module](#structures-for-boto3-neptune-module)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [CharacterSetTypeDef](#charactersettypedef)
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
  - [DBInstanceStatusInfoTypeDef](#dbinstancestatusinfotypedef)
  - [DBInstanceTypeDef](#dbinstancetypedef)
  - [DBParameterGroupStatusTypeDef](#dbparametergroupstatustypedef)
  - [DBParameterGroupTypeDef](#dbparametergrouptypedef)
  - [DBSecurityGroupMembershipTypeDef](#dbsecuritygroupmembershiptypedef)
  - [DBSubnetGroupTypeDef](#dbsubnetgrouptypedef)
  - [DomainMembershipTypeDef](#domainmembershiptypedef)
  - [DoubleRangeTypeDef](#doublerangetypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [EngineDefaultsTypeDef](#enginedefaultstypedef)
  - [EventCategoriesMapTypeDef](#eventcategoriesmaptypedef)
  - [EventSubscriptionTypeDef](#eventsubscriptiontypedef)
  - [EventTypeDef](#eventtypedef)
  - [OptionGroupMembershipTypeDef](#optiongroupmembershiptypedef)
  - [OrderableDBInstanceOptionTypeDef](#orderabledbinstanceoptiontypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [PendingCloudwatchLogsExportsTypeDef](#pendingcloudwatchlogsexportstypedef)
  - [PendingMaintenanceActionTypeDef](#pendingmaintenanceactiontypedef)
  - [PendingModifiedValuesTypeDef](#pendingmodifiedvaluestypedef)
  - [RangeTypeDef](#rangetypedef)
  - [ResourcePendingMaintenanceActionsTypeDef](#resourcependingmaintenanceactionstypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SubnetTypeDef](#subnettypedef)
  - [TagTypeDef](#tagtypedef)
  - [TimezoneTypeDef](#timezonetypedef)
  - [UpgradeTargetTypeDef](#upgradetargettypedef)
  - [ValidDBInstanceModificationsMessageTypeDef](#validdbinstancemodificationsmessagetypedef)
  - [ValidStorageOptionsTypeDef](#validstorageoptionstypedef)
  - [VpcSecurityGroupMembershipTypeDef](#vpcsecuritygroupmembershiptypedef)
  - [AddSourceIdentifierToSubscriptionResultTypeDef](#addsourceidentifiertosubscriptionresulttypedef)
  - [ApplyPendingMaintenanceActionResultTypeDef](#applypendingmaintenanceactionresulttypedef)
  - [CloudwatchLogsExportConfigurationTypeDef](#cloudwatchlogsexportconfigurationtypedef)
  - [CopyDBClusterParameterGroupResultTypeDef](#copydbclusterparametergroupresulttypedef)
  - [CopyDBClusterSnapshotResultTypeDef](#copydbclustersnapshotresulttypedef)
  - [CopyDBParameterGroupResultTypeDef](#copydbparametergroupresulttypedef)
  - [CreateDBClusterEndpointOutputTypeDef](#createdbclusterendpointoutputtypedef)
  - [CreateDBClusterParameterGroupResultTypeDef](#createdbclusterparametergroupresulttypedef)
  - [CreateDBClusterResultTypeDef](#createdbclusterresulttypedef)
  - [CreateDBClusterSnapshotResultTypeDef](#createdbclustersnapshotresulttypedef)
  - [CreateDBInstanceResultTypeDef](#createdbinstanceresulttypedef)
  - [CreateDBParameterGroupResultTypeDef](#createdbparametergroupresulttypedef)
  - [CreateDBSubnetGroupResultTypeDef](#createdbsubnetgroupresulttypedef)
  - [CreateEventSubscriptionResultTypeDef](#createeventsubscriptionresulttypedef)
  - [DBClusterEndpointMessageTypeDef](#dbclusterendpointmessagetypedef)
  - [DBClusterMessageTypeDef](#dbclustermessagetypedef)
  - [DBClusterParameterGroupDetailsTypeDef](#dbclusterparametergroupdetailstypedef)
  - [DBClusterParameterGroupNameMessageTypeDef](#dbclusterparametergroupnamemessagetypedef)
  - [DBClusterParameterGroupsMessageTypeDef](#dbclusterparametergroupsmessagetypedef)
  - [DBClusterSnapshotMessageTypeDef](#dbclustersnapshotmessagetypedef)
  - [DBEngineVersionMessageTypeDef](#dbengineversionmessagetypedef)
  - [DBInstanceMessageTypeDef](#dbinstancemessagetypedef)
  - [DBParameterGroupDetailsTypeDef](#dbparametergroupdetailstypedef)
  - [DBParameterGroupNameMessageTypeDef](#dbparametergroupnamemessagetypedef)
  - [DBParameterGroupsMessageTypeDef](#dbparametergroupsmessagetypedef)
  - [DBSubnetGroupMessageTypeDef](#dbsubnetgroupmessagetypedef)
  - [DeleteDBClusterEndpointOutputTypeDef](#deletedbclusterendpointoutputtypedef)
  - [DeleteDBClusterResultTypeDef](#deletedbclusterresulttypedef)
  - [DeleteDBClusterSnapshotResultTypeDef](#deletedbclustersnapshotresulttypedef)
  - [DeleteDBInstanceResultTypeDef](#deletedbinstanceresulttypedef)
  - [DeleteEventSubscriptionResultTypeDef](#deleteeventsubscriptionresulttypedef)
  - [DescribeDBClusterSnapshotAttributesResultTypeDef](#describedbclustersnapshotattributesresulttypedef)
  - [DescribeEngineDefaultClusterParametersResultTypeDef](#describeenginedefaultclusterparametersresulttypedef)
  - [DescribeEngineDefaultParametersResultTypeDef](#describeenginedefaultparametersresulttypedef)
  - [DescribeValidDBInstanceModificationsResultTypeDef](#describevaliddbinstancemodificationsresulttypedef)
  - [EventCategoriesMessageTypeDef](#eventcategoriesmessagetypedef)
  - [EventSubscriptionsMessageTypeDef](#eventsubscriptionsmessagetypedef)
  - [EventsMessageTypeDef](#eventsmessagetypedef)
  - [FailoverDBClusterResultTypeDef](#failoverdbclusterresulttypedef)
  - [FilterTypeDef](#filtertypedef)
  - [ModifyDBClusterEndpointOutputTypeDef](#modifydbclusterendpointoutputtypedef)
  - [ModifyDBClusterResultTypeDef](#modifydbclusterresulttypedef)
  - [ModifyDBClusterSnapshotAttributeResultTypeDef](#modifydbclustersnapshotattributeresulttypedef)
  - [ModifyDBInstanceResultTypeDef](#modifydbinstanceresulttypedef)
  - [ModifyDBSubnetGroupResultTypeDef](#modifydbsubnetgroupresulttypedef)
  - [ModifyEventSubscriptionResultTypeDef](#modifyeventsubscriptionresulttypedef)
  - [OrderableDBInstanceOptionsMessageTypeDef](#orderabledbinstanceoptionsmessagetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PendingMaintenanceActionsMessageTypeDef](#pendingmaintenanceactionsmessagetypedef)
  - [PromoteReadReplicaDBClusterResultTypeDef](#promotereadreplicadbclusterresulttypedef)
  - [RebootDBInstanceResultTypeDef](#rebootdbinstanceresulttypedef)
  - [RemoveSourceIdentifierFromSubscriptionResultTypeDef](#removesourceidentifierfromsubscriptionresulttypedef)
  - [RestoreDBClusterFromSnapshotResultTypeDef](#restoredbclusterfromsnapshotresulttypedef)
  - [RestoreDBClusterToPointInTimeResultTypeDef](#restoredbclustertopointintimeresulttypedef)
  - [StartDBClusterResultTypeDef](#startdbclusterresulttypedef)
  - [StopDBClusterResultTypeDef](#stopdbclusterresulttypedef)
  - [TagListMessageTypeDef](#taglistmessagetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AvailabilityZoneTypeDef

```python
from mypy_boto3_neptune.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `Name`: `str`


## CharacterSetTypeDef

```python
from mypy_boto3_neptune.type_defs import CharacterSetTypeDef
```




Optional fields:
- `CharacterSetName`: `str`
- `CharacterSetDescription`: `str`


## DBClusterEndpointTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterEndpointTypeDef
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
from mypy_boto3_neptune.type_defs import DBClusterMemberTypeDef
```




Optional fields:
- `DBInstanceIdentifier`: `str`
- `IsClusterWriter`: `bool`
- `DBClusterParameterGroupStatus`: `str`
- `PromotionTier`: `int`


## DBClusterOptionGroupStatusTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterOptionGroupStatusTypeDef
```




Optional fields:
- `DBClusterOptionGroupName`: `str`
- `Status`: `str`


## DBClusterParameterGroupTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterParameterGroupTypeDef
```




Optional fields:
- `DBClusterParameterGroupName`: `str`
- `DBParameterGroupFamily`: `str`
- `Description`: `str`
- `DBClusterParameterGroupArn`: `str`


## DBClusterRoleTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterRoleTypeDef
```




Optional fields:
- `RoleArn`: `str`
- `Status`: `str`
- `FeatureName`: `str`


## DBClusterSnapshotAttributeTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterSnapshotAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValues`: `List[str]`


## DBClusterSnapshotAttributesResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterSnapshotAttributesResultTypeDef
```




Optional fields:
- `DBClusterSnapshotIdentifier`: `str`
- `DBClusterSnapshotAttributes`: `List["DBClusterSnapshotAttributeTypeDef"]`


## DBClusterSnapshotTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterSnapshotTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `DBClusterSnapshotIdentifier`: `str`
- `DBClusterIdentifier`: `str`
- `SnapshotCreateTime`: `datetime`
- `Engine`: `str`
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


## DBClusterTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterTypeDef
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
- `EnabledCloudwatchLogsExports`: `List[str]`
- `DeletionProtection`: `bool`


## DBEngineVersionTypeDef

```python
from mypy_boto3_neptune.type_defs import DBEngineVersionTypeDef
```




Optional fields:
- `Engine`: `str`
- `EngineVersion`: `str`
- `DBParameterGroupFamily`: `str`
- `DBEngineDescription`: `str`
- `DBEngineVersionDescription`: `str`
- `DefaultCharacterSet`: `"CharacterSetTypeDef"`
- `SupportedCharacterSets`: `List["CharacterSetTypeDef"]`
- `ValidUpgradeTarget`: `List["UpgradeTargetTypeDef"]`
- `SupportedTimezones`: `List["TimezoneTypeDef"]`
- `ExportableLogTypes`: `List[str]`
- `SupportsLogExportsToCloudwatchLogs`: `bool`
- `SupportsReadReplica`: `bool`


## DBInstanceStatusInfoTypeDef

```python
from mypy_boto3_neptune.type_defs import DBInstanceStatusInfoTypeDef
```




Optional fields:
- `StatusType`: `str`
- `Normal`: `bool`
- `Status`: `str`
- `Message`: `str`


## DBInstanceTypeDef

```python
from mypy_boto3_neptune.type_defs import DBInstanceTypeDef
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
- `LicenseModel`: `str`
- `Iops`: `int`
- `OptionGroupMemberships`: `List["OptionGroupMembershipTypeDef"]`
- `CharacterSetName`: `str`
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
- `EnabledCloudwatchLogsExports`: `List[str]`
- `DeletionProtection`: `bool`


## DBParameterGroupStatusTypeDef

```python
from mypy_boto3_neptune.type_defs import DBParameterGroupStatusTypeDef
```




Optional fields:
- `DBParameterGroupName`: `str`
- `ParameterApplyStatus`: `str`


## DBParameterGroupTypeDef

```python
from mypy_boto3_neptune.type_defs import DBParameterGroupTypeDef
```




Optional fields:
- `DBParameterGroupName`: `str`
- `DBParameterGroupFamily`: `str`
- `Description`: `str`
- `DBParameterGroupArn`: `str`


## DBSecurityGroupMembershipTypeDef

```python
from mypy_boto3_neptune.type_defs import DBSecurityGroupMembershipTypeDef
```




Optional fields:
- `DBSecurityGroupName`: `str`
- `Status`: `str`


## DBSubnetGroupTypeDef

```python
from mypy_boto3_neptune.type_defs import DBSubnetGroupTypeDef
```




Optional fields:
- `DBSubnetGroupName`: `str`
- `DBSubnetGroupDescription`: `str`
- `VpcId`: `str`
- `SubnetGroupStatus`: `str`
- `Subnets`: `List["SubnetTypeDef"]`
- `DBSubnetGroupArn`: `str`


## DomainMembershipTypeDef

```python
from mypy_boto3_neptune.type_defs import DomainMembershipTypeDef
```




Optional fields:
- `Domain`: `str`
- `Status`: `str`
- `FQDN`: `str`
- `IAMRoleName`: `str`


## DoubleRangeTypeDef

```python
from mypy_boto3_neptune.type_defs import DoubleRangeTypeDef
```




Optional fields:
- `From`: `float`
- `To`: `float`


## EndpointTypeDef

```python
from mypy_boto3_neptune.type_defs import EndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Port`: `int`
- `HostedZoneId`: `str`


## EngineDefaultsTypeDef

```python
from mypy_boto3_neptune.type_defs import EngineDefaultsTypeDef
```




Optional fields:
- `DBParameterGroupFamily`: `str`
- `Marker`: `str`
- `Parameters`: `List["ParameterTypeDef"]`


## EventCategoriesMapTypeDef

```python
from mypy_boto3_neptune.type_defs import EventCategoriesMapTypeDef
```




Optional fields:
- `SourceType`: `str`
- `EventCategories`: `List[str]`


## EventSubscriptionTypeDef

```python
from mypy_boto3_neptune.type_defs import EventSubscriptionTypeDef
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
from mypy_boto3_neptune.type_defs import EventTypeDef
```




Optional fields:
- `SourceIdentifier`: `str`
- `SourceType`: `SourceType`
- `Message`: `str`
- `EventCategories`: `List[str]`
- `Date`: `datetime`
- `SourceArn`: `str`


## OptionGroupMembershipTypeDef

```python
from mypy_boto3_neptune.type_defs import OptionGroupMembershipTypeDef
```




Optional fields:
- `OptionGroupName`: `str`
- `Status`: `str`


## OrderableDBInstanceOptionTypeDef

```python
from mypy_boto3_neptune.type_defs import OrderableDBInstanceOptionTypeDef
```




Optional fields:
- `Engine`: `str`
- `EngineVersion`: `str`
- `DBInstanceClass`: `str`
- `LicenseModel`: `str`
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


## ParameterTypeDef

```python
from mypy_boto3_neptune.type_defs import ParameterTypeDef
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


## PendingCloudwatchLogsExportsTypeDef

```python
from mypy_boto3_neptune.type_defs import PendingCloudwatchLogsExportsTypeDef
```




Optional fields:
- `LogTypesToEnable`: `List[str]`
- `LogTypesToDisable`: `List[str]`


## PendingMaintenanceActionTypeDef

```python
from mypy_boto3_neptune.type_defs import PendingMaintenanceActionTypeDef
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
from mypy_boto3_neptune.type_defs import PendingModifiedValuesTypeDef
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


## RangeTypeDef

```python
from mypy_boto3_neptune.type_defs import RangeTypeDef
```




Optional fields:
- `From`: `int`
- `To`: `int`
- `Step`: `int`


## ResourcePendingMaintenanceActionsTypeDef

```python
from mypy_boto3_neptune.type_defs import ResourcePendingMaintenanceActionsTypeDef
```




Optional fields:
- `ResourceIdentifier`: `str`
- `PendingMaintenanceActionDetails`: `List["PendingMaintenanceActionTypeDef"]`


## ResponseMetadata

```python
from mypy_boto3_neptune.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SubnetTypeDef

```python
from mypy_boto3_neptune.type_defs import SubnetTypeDef
```




Optional fields:
- `SubnetIdentifier`: `str`
- `SubnetAvailabilityZone`: `"AvailabilityZoneTypeDef"`
- `SubnetStatus`: `str`


## TagTypeDef

```python
from mypy_boto3_neptune.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TimezoneTypeDef

```python
from mypy_boto3_neptune.type_defs import TimezoneTypeDef
```




Optional fields:
- `TimezoneName`: `str`


## UpgradeTargetTypeDef

```python
from mypy_boto3_neptune.type_defs import UpgradeTargetTypeDef
```




Optional fields:
- `Engine`: `str`
- `EngineVersion`: `str`
- `Description`: `str`
- `AutoUpgrade`: `bool`
- `IsMajorVersionUpgrade`: `bool`


## ValidDBInstanceModificationsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import ValidDBInstanceModificationsMessageTypeDef
```




Optional fields:
- `Storage`: `List["ValidStorageOptionsTypeDef"]`


## ValidStorageOptionsTypeDef

```python
from mypy_boto3_neptune.type_defs import ValidStorageOptionsTypeDef
```




Optional fields:
- `StorageType`: `str`
- `StorageSize`: `List["RangeTypeDef"]`
- `ProvisionedIops`: `List["RangeTypeDef"]`
- `IopsToStorageRatio`: `List["DoubleRangeTypeDef"]`


## VpcSecurityGroupMembershipTypeDef

```python
from mypy_boto3_neptune.type_defs import VpcSecurityGroupMembershipTypeDef
```




Optional fields:
- `VpcSecurityGroupId`: `str`
- `Status`: `str`


## AddSourceIdentifierToSubscriptionResultTypeDef

```python
from mypy_boto3_neptune.type_defs import AddSourceIdentifierToSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## ApplyPendingMaintenanceActionResultTypeDef

```python
from mypy_boto3_neptune.type_defs import ApplyPendingMaintenanceActionResultTypeDef
```




Optional fields:
- `ResourcePendingMaintenanceActions`: `"ResourcePendingMaintenanceActionsTypeDef"`


## CloudwatchLogsExportConfigurationTypeDef

```python
from mypy_boto3_neptune.type_defs import CloudwatchLogsExportConfigurationTypeDef
```




Optional fields:
- `EnableLogTypes`: `List[str]`
- `DisableLogTypes`: `List[str]`


## CopyDBClusterParameterGroupResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CopyDBClusterParameterGroupResultTypeDef
```




Optional fields:
- `DBClusterParameterGroup`: `"DBClusterParameterGroupTypeDef"`


## CopyDBClusterSnapshotResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CopyDBClusterSnapshotResultTypeDef
```




Optional fields:
- `DBClusterSnapshot`: `"DBClusterSnapshotTypeDef"`


## CopyDBParameterGroupResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CopyDBParameterGroupResultTypeDef
```




Optional fields:
- `DBParameterGroup`: `"DBParameterGroupTypeDef"`


## CreateDBClusterEndpointOutputTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBClusterEndpointOutputTypeDef
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
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateDBClusterParameterGroupResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBClusterParameterGroupResultTypeDef
```




Optional fields:
- `DBClusterParameterGroup`: `"DBClusterParameterGroupTypeDef"`


## CreateDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## CreateDBClusterSnapshotResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBClusterSnapshotResultTypeDef
```




Optional fields:
- `DBClusterSnapshot`: `"DBClusterSnapshotTypeDef"`


## CreateDBInstanceResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## CreateDBParameterGroupResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBParameterGroupResultTypeDef
```




Optional fields:
- `DBParameterGroup`: `"DBParameterGroupTypeDef"`


## CreateDBSubnetGroupResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateDBSubnetGroupResultTypeDef
```




Optional fields:
- `DBSubnetGroup`: `"DBSubnetGroupTypeDef"`


## CreateEventSubscriptionResultTypeDef

```python
from mypy_boto3_neptune.type_defs import CreateEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## DBClusterEndpointMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterEndpointMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterEndpoints`: `List["DBClusterEndpointTypeDef"]`


## DBClusterMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusters`: `List["DBClusterTypeDef"]`


## DBClusterParameterGroupDetailsTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterParameterGroupDetailsTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `Marker`: `str`


## DBClusterParameterGroupNameMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterParameterGroupNameMessageTypeDef
```




Optional fields:
- `DBClusterParameterGroupName`: `str`


## DBClusterParameterGroupsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterParameterGroupsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterParameterGroups`: `List["DBClusterParameterGroupTypeDef"]`


## DBClusterSnapshotMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBClusterSnapshotMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBClusterSnapshots`: `List["DBClusterSnapshotTypeDef"]`


## DBEngineVersionMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBEngineVersionMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBEngineVersions`: `List["DBEngineVersionTypeDef"]`


## DBInstanceMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBInstanceMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBInstances`: `List["DBInstanceTypeDef"]`


## DBParameterGroupDetailsTypeDef

```python
from mypy_boto3_neptune.type_defs import DBParameterGroupDetailsTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `Marker`: `str`


## DBParameterGroupNameMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBParameterGroupNameMessageTypeDef
```




Optional fields:
- `DBParameterGroupName`: `str`


## DBParameterGroupsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBParameterGroupsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBParameterGroups`: `List["DBParameterGroupTypeDef"]`


## DBSubnetGroupMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import DBSubnetGroupMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `DBSubnetGroups`: `List["DBSubnetGroupTypeDef"]`


## DeleteDBClusterEndpointOutputTypeDef

```python
from mypy_boto3_neptune.type_defs import DeleteDBClusterEndpointOutputTypeDef
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
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DeleteDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## DeleteDBClusterSnapshotResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DeleteDBClusterSnapshotResultTypeDef
```




Optional fields:
- `DBClusterSnapshot`: `"DBClusterSnapshotTypeDef"`


## DeleteDBInstanceResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DeleteDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## DeleteEventSubscriptionResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DeleteEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## DescribeDBClusterSnapshotAttributesResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DescribeDBClusterSnapshotAttributesResultTypeDef
```




Optional fields:
- `DBClusterSnapshotAttributesResult`: `"DBClusterSnapshotAttributesResultTypeDef"`


## DescribeEngineDefaultClusterParametersResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DescribeEngineDefaultClusterParametersResultTypeDef
```




Optional fields:
- `EngineDefaults`: `"EngineDefaultsTypeDef"`


## DescribeEngineDefaultParametersResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DescribeEngineDefaultParametersResultTypeDef
```




Optional fields:
- `EngineDefaults`: `"EngineDefaultsTypeDef"`


## DescribeValidDBInstanceModificationsResultTypeDef

```python
from mypy_boto3_neptune.type_defs import DescribeValidDBInstanceModificationsResultTypeDef
```




Optional fields:
- `ValidDBInstanceModificationsMessage`: `"ValidDBInstanceModificationsMessageTypeDef"`


## EventCategoriesMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import EventCategoriesMessageTypeDef
```




Optional fields:
- `EventCategoriesMapList`: `List["EventCategoriesMapTypeDef"]`


## EventSubscriptionsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import EventSubscriptionsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `EventSubscriptionsList`: `List["EventSubscriptionTypeDef"]`


## EventsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import EventsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `Events`: `List["EventTypeDef"]`


## FailoverDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import FailoverDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## FilterTypeDef

```python
from mypy_boto3_neptune.type_defs import FilterTypeDef
```


Required fields:
- `Name`: `str`
- `Values`: `List[str]`




## ModifyDBClusterEndpointOutputTypeDef

```python
from mypy_boto3_neptune.type_defs import ModifyDBClusterEndpointOutputTypeDef
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
- `ResponseMetadata`: `"ResponseMetadata"`


## ModifyDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import ModifyDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## ModifyDBClusterSnapshotAttributeResultTypeDef

```python
from mypy_boto3_neptune.type_defs import ModifyDBClusterSnapshotAttributeResultTypeDef
```




Optional fields:
- `DBClusterSnapshotAttributesResult`: `"DBClusterSnapshotAttributesResultTypeDef"`


## ModifyDBInstanceResultTypeDef

```python
from mypy_boto3_neptune.type_defs import ModifyDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## ModifyDBSubnetGroupResultTypeDef

```python
from mypy_boto3_neptune.type_defs import ModifyDBSubnetGroupResultTypeDef
```




Optional fields:
- `DBSubnetGroup`: `"DBSubnetGroupTypeDef"`


## ModifyEventSubscriptionResultTypeDef

```python
from mypy_boto3_neptune.type_defs import ModifyEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## OrderableDBInstanceOptionsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import OrderableDBInstanceOptionsMessageTypeDef
```




Optional fields:
- `OrderableDBInstanceOptions`: `List["OrderableDBInstanceOptionTypeDef"]`
- `Marker`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_neptune.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PendingMaintenanceActionsMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import PendingMaintenanceActionsMessageTypeDef
```




Optional fields:
- `PendingMaintenanceActions`: `List["ResourcePendingMaintenanceActionsTypeDef"]`
- `Marker`: `str`


## PromoteReadReplicaDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import PromoteReadReplicaDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## RebootDBInstanceResultTypeDef

```python
from mypy_boto3_neptune.type_defs import RebootDBInstanceResultTypeDef
```




Optional fields:
- `DBInstance`: `"DBInstanceTypeDef"`


## RemoveSourceIdentifierFromSubscriptionResultTypeDef

```python
from mypy_boto3_neptune.type_defs import RemoveSourceIdentifierFromSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## RestoreDBClusterFromSnapshotResultTypeDef

```python
from mypy_boto3_neptune.type_defs import RestoreDBClusterFromSnapshotResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## RestoreDBClusterToPointInTimeResultTypeDef

```python
from mypy_boto3_neptune.type_defs import RestoreDBClusterToPointInTimeResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## StartDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import StartDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## StopDBClusterResultTypeDef

```python
from mypy_boto3_neptune.type_defs import StopDBClusterResultTypeDef
```




Optional fields:
- `DBCluster`: `"DBClusterTypeDef"`


## TagListMessageTypeDef

```python
from mypy_boto3_neptune.type_defs import TagListMessageTypeDef
```




Optional fields:
- `TagList`: `List["TagTypeDef"]`


## WaiterConfigTypeDef

```python
from mypy_boto3_neptune.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

