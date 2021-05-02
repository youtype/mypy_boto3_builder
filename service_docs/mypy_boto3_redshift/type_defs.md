# Structures for boto3 Redshift module

> [Index](../index.md) > [Redshift](./index.md) > Structures

Auto-generated documentation for [Redshift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift)
type annotations stubs module [mypy_boto3_redshift](https://pypi.org/project/mypy-boto3-redshift/).

- [Structures for boto3 Redshift module](#structures-for-boto3-redshift-module)
  - [AccountAttributeTypeDef](#accountattributetypedef)
  - [AccountWithRestoreAccessTypeDef](#accountwithrestoreaccesstypedef)
  - [AquaConfigurationTypeDef](#aquaconfigurationtypedef)
  - [AttributeValueTargetTypeDef](#attributevaluetargettypedef)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [ClusterAssociatedToScheduleTypeDef](#clusterassociatedtoscheduletypedef)
  - [ClusterDbRevisionTypeDef](#clusterdbrevisiontypedef)
  - [ClusterIamRoleTypeDef](#clusteriamroletypedef)
  - [ClusterNodeTypeDef](#clusternodetypedef)
  - [ClusterParameterGroupStatusTypeDef](#clusterparametergroupstatustypedef)
  - [ClusterParameterGroupTypeDef](#clusterparametergrouptypedef)
  - [ClusterParameterStatusTypeDef](#clusterparameterstatustypedef)
  - [ClusterSecurityGroupMembershipTypeDef](#clustersecuritygroupmembershiptypedef)
  - [ClusterSecurityGroupTypeDef](#clustersecuritygrouptypedef)
  - [ClusterSnapshotCopyStatusTypeDef](#clustersnapshotcopystatustypedef)
  - [ClusterSubnetGroupTypeDef](#clustersubnetgrouptypedef)
  - [ClusterTypeDef](#clustertypedef)
  - [ClusterVersionTypeDef](#clusterversiontypedef)
  - [DataTransferProgressTypeDef](#datatransferprogresstypedef)
  - [DefaultClusterParametersTypeDef](#defaultclusterparameterstypedef)
  - [DeferredMaintenanceWindowTypeDef](#deferredmaintenancewindowtypedef)
  - [EC2SecurityGroupTypeDef](#ec2securitygrouptypedef)
  - [ElasticIpStatusTypeDef](#elasticipstatustypedef)
  - [EndpointAccessTypeDef](#endpointaccesstypedef)
  - [EndpointAuthorizationTypeDef](#endpointauthorizationtypedef)
  - [EndpointTypeDef](#endpointtypedef)
  - [EventCategoriesMapTypeDef](#eventcategoriesmaptypedef)
  - [EventInfoMapTypeDef](#eventinfomaptypedef)
  - [EventSubscriptionTypeDef](#eventsubscriptiontypedef)
  - [EventTypeDef](#eventtypedef)
  - [HsmClientCertificateTypeDef](#hsmclientcertificatetypedef)
  - [HsmConfigurationTypeDef](#hsmconfigurationtypedef)
  - [HsmStatusTypeDef](#hsmstatustypedef)
  - [IPRangeTypeDef](#iprangetypedef)
  - [MaintenanceTrackTypeDef](#maintenancetracktypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [NodeConfigurationOptionTypeDef](#nodeconfigurationoptiontypedef)
  - [OrderableClusterOptionTypeDef](#orderableclusteroptiontypedef)
  - [ParameterTypeDef](#parametertypedef)
  - [PartnerIntegrationInfoTypeDef](#partnerintegrationinfotypedef)
  - [PauseClusterMessageTypeDef](#pauseclustermessagetypedef)
  - [PendingModifiedValuesTypeDef](#pendingmodifiedvaluestypedef)
  - [RecurringChargeTypeDef](#recurringchargetypedef)
  - [ReservedNodeOfferingTypeDef](#reservednodeofferingtypedef)
  - [ReservedNodeTypeDef](#reservednodetypedef)
  - [ResizeClusterMessageTypeDef](#resizeclustermessagetypedef)
  - [ResizeInfoTypeDef](#resizeinfotypedef)
  - [RestoreStatusTypeDef](#restorestatustypedef)
  - [ResumeClusterMessageTypeDef](#resumeclustermessagetypedef)
  - [RevisionTargetTypeDef](#revisiontargettypedef)
  - [ScheduledActionTypeDef](#scheduledactiontypedef)
  - [ScheduledActionTypeTypeDef](#scheduledactiontypetypedef)
  - [SnapshotCopyGrantTypeDef](#snapshotcopygranttypedef)
  - [SnapshotErrorMessageTypeDef](#snapshoterrormessagetypedef)
  - [SnapshotScheduleTypeDef](#snapshotscheduletypedef)
  - [SnapshotTypeDef](#snapshottypedef)
  - [SubnetTypeDef](#subnettypedef)
  - [SupportedOperationTypeDef](#supportedoperationtypedef)
  - [SupportedPlatformTypeDef](#supportedplatformtypedef)
  - [TableRestoreStatusTypeDef](#tablerestorestatustypedef)
  - [TagTypeDef](#tagtypedef)
  - [TaggedResourceTypeDef](#taggedresourcetypedef)
  - [UpdateTargetTypeDef](#updatetargettypedef)
  - [UsageLimitTypeDef](#usagelimittypedef)
  - [VpcEndpointTypeDef](#vpcendpointtypedef)
  - [VpcSecurityGroupMembershipTypeDef](#vpcsecuritygroupmembershiptypedef)
  - [AcceptReservedNodeExchangeOutputMessageTypeDef](#acceptreservednodeexchangeoutputmessagetypedef)
  - [AccountAttributeListTypeDef](#accountattributelisttypedef)
  - [AuthorizeClusterSecurityGroupIngressResultTypeDef](#authorizeclustersecuritygroupingressresulttypedef)
  - [AuthorizeSnapshotAccessResultTypeDef](#authorizesnapshotaccessresulttypedef)
  - [BatchDeleteClusterSnapshotsResultTypeDef](#batchdeleteclustersnapshotsresulttypedef)
  - [BatchModifyClusterSnapshotsOutputMessageTypeDef](#batchmodifyclustersnapshotsoutputmessagetypedef)
  - [ClusterCredentialsTypeDef](#clustercredentialstypedef)
  - [ClusterDbRevisionsMessageTypeDef](#clusterdbrevisionsmessagetypedef)
  - [ClusterParameterGroupDetailsTypeDef](#clusterparametergroupdetailstypedef)
  - [ClusterParameterGroupNameMessageTypeDef](#clusterparametergroupnamemessagetypedef)
  - [ClusterParameterGroupsMessageTypeDef](#clusterparametergroupsmessagetypedef)
  - [ClusterSecurityGroupMessageTypeDef](#clustersecuritygroupmessagetypedef)
  - [ClusterSubnetGroupMessageTypeDef](#clustersubnetgroupmessagetypedef)
  - [ClusterVersionsMessageTypeDef](#clusterversionsmessagetypedef)
  - [ClustersMessageTypeDef](#clustersmessagetypedef)
  - [CopyClusterSnapshotResultTypeDef](#copyclustersnapshotresulttypedef)
  - [CreateClusterParameterGroupResultTypeDef](#createclusterparametergroupresulttypedef)
  - [CreateClusterResultTypeDef](#createclusterresulttypedef)
  - [CreateClusterSecurityGroupResultTypeDef](#createclustersecuritygroupresulttypedef)
  - [CreateClusterSnapshotResultTypeDef](#createclustersnapshotresulttypedef)
  - [CreateClusterSubnetGroupResultTypeDef](#createclustersubnetgroupresulttypedef)
  - [CreateEventSubscriptionResultTypeDef](#createeventsubscriptionresulttypedef)
  - [CreateHsmClientCertificateResultTypeDef](#createhsmclientcertificateresulttypedef)
  - [CreateHsmConfigurationResultTypeDef](#createhsmconfigurationresulttypedef)
  - [CreateSnapshotCopyGrantResultTypeDef](#createsnapshotcopygrantresulttypedef)
  - [CustomerStorageMessageTypeDef](#customerstoragemessagetypedef)
  - [DeleteClusterResultTypeDef](#deleteclusterresulttypedef)
  - [DeleteClusterSnapshotMessageTypeDef](#deleteclustersnapshotmessagetypedef)
  - [DeleteClusterSnapshotResultTypeDef](#deleteclustersnapshotresulttypedef)
  - [DescribeDefaultClusterParametersResultTypeDef](#describedefaultclusterparametersresulttypedef)
  - [DescribePartnersOutputMessageTypeDef](#describepartnersoutputmessagetypedef)
  - [DescribeSnapshotSchedulesOutputMessageTypeDef](#describesnapshotschedulesoutputmessagetypedef)
  - [DisableSnapshotCopyResultTypeDef](#disablesnapshotcopyresulttypedef)
  - [EnableSnapshotCopyResultTypeDef](#enablesnapshotcopyresulttypedef)
  - [EndpointAccessListTypeDef](#endpointaccesslisttypedef)
  - [EndpointAuthorizationListTypeDef](#endpointauthorizationlisttypedef)
  - [EventCategoriesMessageTypeDef](#eventcategoriesmessagetypedef)
  - [EventSubscriptionsMessageTypeDef](#eventsubscriptionsmessagetypedef)
  - [EventsMessageTypeDef](#eventsmessagetypedef)
  - [GetReservedNodeExchangeOfferingsOutputMessageTypeDef](#getreservednodeexchangeofferingsoutputmessagetypedef)
  - [HsmClientCertificateMessageTypeDef](#hsmclientcertificatemessagetypedef)
  - [HsmConfigurationMessageTypeDef](#hsmconfigurationmessagetypedef)
  - [LoggingStatusTypeDef](#loggingstatustypedef)
  - [ModifyAquaOutputMessageTypeDef](#modifyaquaoutputmessagetypedef)
  - [ModifyClusterDbRevisionResultTypeDef](#modifyclusterdbrevisionresulttypedef)
  - [ModifyClusterIamRolesResultTypeDef](#modifyclusteriamrolesresulttypedef)
  - [ModifyClusterMaintenanceResultTypeDef](#modifyclustermaintenanceresulttypedef)
  - [ModifyClusterResultTypeDef](#modifyclusterresulttypedef)
  - [ModifyClusterSnapshotResultTypeDef](#modifyclustersnapshotresulttypedef)
  - [ModifyClusterSubnetGroupResultTypeDef](#modifyclustersubnetgroupresulttypedef)
  - [ModifyEventSubscriptionResultTypeDef](#modifyeventsubscriptionresulttypedef)
  - [ModifySnapshotCopyRetentionPeriodResultTypeDef](#modifysnapshotcopyretentionperiodresulttypedef)
  - [NodeConfigurationOptionsFilterTypeDef](#nodeconfigurationoptionsfiltertypedef)
  - [NodeConfigurationOptionsMessageTypeDef](#nodeconfigurationoptionsmessagetypedef)
  - [OrderableClusterOptionsMessageTypeDef](#orderableclusteroptionsmessagetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PartnerIntegrationOutputMessageTypeDef](#partnerintegrationoutputmessagetypedef)
  - [PauseClusterResultTypeDef](#pauseclusterresulttypedef)
  - [PurchaseReservedNodeOfferingResultTypeDef](#purchasereservednodeofferingresulttypedef)
  - [RebootClusterResultTypeDef](#rebootclusterresulttypedef)
  - [ReservedNodeOfferingsMessageTypeDef](#reservednodeofferingsmessagetypedef)
  - [ReservedNodesMessageTypeDef](#reservednodesmessagetypedef)
  - [ResizeClusterResultTypeDef](#resizeclusterresulttypedef)
  - [ResizeProgressMessageTypeDef](#resizeprogressmessagetypedef)
  - [RestoreFromClusterSnapshotResultTypeDef](#restorefromclustersnapshotresulttypedef)
  - [RestoreTableFromClusterSnapshotResultTypeDef](#restoretablefromclustersnapshotresulttypedef)
  - [ResumeClusterResultTypeDef](#resumeclusterresulttypedef)
  - [RevokeClusterSecurityGroupIngressResultTypeDef](#revokeclustersecuritygroupingressresulttypedef)
  - [RevokeSnapshotAccessResultTypeDef](#revokesnapshotaccessresulttypedef)
  - [RotateEncryptionKeyResultTypeDef](#rotateencryptionkeyresulttypedef)
  - [ScheduledActionFilterTypeDef](#scheduledactionfiltertypedef)
  - [ScheduledActionsMessageTypeDef](#scheduledactionsmessagetypedef)
  - [SnapshotCopyGrantMessageTypeDef](#snapshotcopygrantmessagetypedef)
  - [SnapshotMessageTypeDef](#snapshotmessagetypedef)
  - [SnapshotSortingEntityTypeDef](#snapshotsortingentitytypedef)
  - [TableRestoreStatusMessageTypeDef](#tablerestorestatusmessagetypedef)
  - [TaggedResourceListMessageTypeDef](#taggedresourcelistmessagetypedef)
  - [TrackListMessageTypeDef](#tracklistmessagetypedef)
  - [UsageLimitListTypeDef](#usagelimitlisttypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountAttributeTypeDef

```python
from mypy_boto3_redshift.type_defs import AccountAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValues`: `List["AttributeValueTargetTypeDef"]`


## AccountWithRestoreAccessTypeDef

```python
from mypy_boto3_redshift.type_defs import AccountWithRestoreAccessTypeDef
```




Optional fields:
- `AccountId`: `str`
- `AccountAlias`: `str`


## AquaConfigurationTypeDef

```python
from mypy_boto3_redshift.type_defs import AquaConfigurationTypeDef
```




Optional fields:
- `AquaStatus`: `AquaStatus`
- `AquaConfigurationStatus`: `AquaConfigurationStatus`


## AttributeValueTargetTypeDef

```python
from mypy_boto3_redshift.type_defs import AttributeValueTargetTypeDef
```




Optional fields:
- `AttributeValue`: `str`


## AvailabilityZoneTypeDef

```python
from mypy_boto3_redshift.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `Name`: `str`
- `SupportedPlatforms`: `List["SupportedPlatformTypeDef"]`


## ClusterAssociatedToScheduleTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterAssociatedToScheduleTypeDef
```




Optional fields:
- `ClusterIdentifier`: `str`
- `ScheduleAssociationState`: `ScheduleState`


## ClusterDbRevisionTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterDbRevisionTypeDef
```




Optional fields:
- `ClusterIdentifier`: `str`
- `CurrentDatabaseRevision`: `str`
- `DatabaseRevisionReleaseDate`: `datetime`
- `RevisionTargets`: `List["RevisionTargetTypeDef"]`


## ClusterIamRoleTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterIamRoleTypeDef
```




Optional fields:
- `IamRoleArn`: `str`
- `ApplyStatus`: `str`


## ClusterNodeTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterNodeTypeDef
```




Optional fields:
- `NodeRole`: `str`
- `PrivateIPAddress`: `str`
- `PublicIPAddress`: `str`


## ClusterParameterGroupStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterParameterGroupStatusTypeDef
```




Optional fields:
- `ParameterGroupName`: `str`
- `ParameterApplyStatus`: `str`
- `ClusterParameterStatusList`: `List["ClusterParameterStatusTypeDef"]`


## ClusterParameterGroupTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterParameterGroupTypeDef
```




Optional fields:
- `ParameterGroupName`: `str`
- `ParameterGroupFamily`: `str`
- `Description`: `str`
- `Tags`: `List["TagTypeDef"]`


## ClusterParameterStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterParameterStatusTypeDef
```




Optional fields:
- `ParameterName`: `str`
- `ParameterApplyStatus`: `str`
- `ParameterApplyErrorDescription`: `str`


## ClusterSecurityGroupMembershipTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterSecurityGroupMembershipTypeDef
```




Optional fields:
- `ClusterSecurityGroupName`: `str`
- `Status`: `str`


## ClusterSecurityGroupTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterSecurityGroupTypeDef
```




Optional fields:
- `ClusterSecurityGroupName`: `str`
- `Description`: `str`
- `EC2SecurityGroups`: `List["EC2SecurityGroupTypeDef"]`
- `IPRanges`: `List["IPRangeTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## ClusterSnapshotCopyStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterSnapshotCopyStatusTypeDef
```




Optional fields:
- `DestinationRegion`: `str`
- `RetentionPeriod`: `int`
- `ManualSnapshotRetentionPeriod`: `int`
- `SnapshotCopyGrantName`: `str`


## ClusterSubnetGroupTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterSubnetGroupTypeDef
```




Optional fields:
- `ClusterSubnetGroupName`: `str`
- `Description`: `str`
- `VpcId`: `str`
- `SubnetGroupStatus`: `str`
- `Subnets`: `List["SubnetTypeDef"]`
- `Tags`: `List["TagTypeDef"]`


## ClusterTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterTypeDef
```




Optional fields:
- `ClusterIdentifier`: `str`
- `NodeType`: `str`
- `ClusterStatus`: `str`
- `ClusterAvailabilityStatus`: `str`
- `ModifyStatus`: `str`
- `MasterUsername`: `str`
- `DBName`: `str`
- `Endpoint`: `"EndpointTypeDef"`
- `ClusterCreateTime`: `datetime`
- `AutomatedSnapshotRetentionPeriod`: `int`
- `ManualSnapshotRetentionPeriod`: `int`
- `ClusterSecurityGroups`: `List["ClusterSecurityGroupMembershipTypeDef"]`
- `VpcSecurityGroups`: `List["VpcSecurityGroupMembershipTypeDef"]`
- `ClusterParameterGroups`: `List["ClusterParameterGroupStatusTypeDef"]`
- `ClusterSubnetGroupName`: `str`
- `VpcId`: `str`
- `AvailabilityZone`: `str`
- `PreferredMaintenanceWindow`: `str`
- `PendingModifiedValues`: `"PendingModifiedValuesTypeDef"`
- `ClusterVersion`: `str`
- `AllowVersionUpgrade`: `bool`
- `NumberOfNodes`: `int`
- `PubliclyAccessible`: `bool`
- `Encrypted`: `bool`
- `RestoreStatus`: `"RestoreStatusTypeDef"`
- `DataTransferProgress`: `"DataTransferProgressTypeDef"`
- `HsmStatus`: `"HsmStatusTypeDef"`
- `ClusterSnapshotCopyStatus`: `"ClusterSnapshotCopyStatusTypeDef"`
- `ClusterPublicKey`: `str`
- `ClusterNodes`: `List["ClusterNodeTypeDef"]`
- `ElasticIpStatus`: `"ElasticIpStatusTypeDef"`
- `ClusterRevisionNumber`: `str`
- `Tags`: `List["TagTypeDef"]`
- `KmsKeyId`: `str`
- `EnhancedVpcRouting`: `bool`
- `IamRoles`: `List["ClusterIamRoleTypeDef"]`
- `PendingActions`: `List[str]`
- `MaintenanceTrackName`: `str`
- `ElasticResizeNumberOfNodeOptions`: `str`
- `DeferredMaintenanceWindows`: `List["DeferredMaintenanceWindowTypeDef"]`
- `SnapshotScheduleIdentifier`: `str`
- `SnapshotScheduleState`: `ScheduleState`
- `ExpectedNextSnapshotScheduleTime`: `datetime`
- `ExpectedNextSnapshotScheduleTimeStatus`: `str`
- `NextMaintenanceWindowStartTime`: `datetime`
- `ResizeInfo`: `"ResizeInfoTypeDef"`
- `AvailabilityZoneRelocationStatus`: `str`
- `ClusterNamespaceArn`: `str`
- `TotalStorageCapacityInMegaBytes`: `int`
- `AquaConfiguration`: `"AquaConfigurationTypeDef"`


## ClusterVersionTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterVersionTypeDef
```




Optional fields:
- `ClusterVersion`: `str`
- `ClusterParameterGroupFamily`: `str`
- `Description`: `str`


## DataTransferProgressTypeDef

```python
from mypy_boto3_redshift.type_defs import DataTransferProgressTypeDef
```




Optional fields:
- `Status`: `str`
- `CurrentRateInMegaBytesPerSecond`: `float`
- `TotalDataInMegaBytes`: `int`
- `DataTransferredInMegaBytes`: `int`
- `EstimatedTimeToCompletionInSeconds`: `int`
- `ElapsedTimeInSeconds`: `int`


## DefaultClusterParametersTypeDef

```python
from mypy_boto3_redshift.type_defs import DefaultClusterParametersTypeDef
```




Optional fields:
- `ParameterGroupFamily`: `str`
- `Marker`: `str`
- `Parameters`: `List["ParameterTypeDef"]`


## DeferredMaintenanceWindowTypeDef

```python
from mypy_boto3_redshift.type_defs import DeferredMaintenanceWindowTypeDef
```




Optional fields:
- `DeferMaintenanceIdentifier`: `str`
- `DeferMaintenanceStartTime`: `datetime`
- `DeferMaintenanceEndTime`: `datetime`


## EC2SecurityGroupTypeDef

```python
from mypy_boto3_redshift.type_defs import EC2SecurityGroupTypeDef
```




Optional fields:
- `Status`: `str`
- `EC2SecurityGroupName`: `str`
- `EC2SecurityGroupOwnerId`: `str`
- `Tags`: `List["TagTypeDef"]`


## ElasticIpStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import ElasticIpStatusTypeDef
```




Optional fields:
- `ElasticIp`: `str`
- `Status`: `str`


## EndpointAccessTypeDef

```python
from mypy_boto3_redshift.type_defs import EndpointAccessTypeDef
```




Optional fields:
- `ClusterIdentifier`: `str`
- `ResourceOwner`: `str`
- `SubnetGroupName`: `str`
- `EndpointStatus`: `str`
- `EndpointName`: `str`
- `EndpointCreateTime`: `datetime`
- `Port`: `int`
- `Address`: `str`
- `VpcSecurityGroups`: `List["VpcSecurityGroupMembershipTypeDef"]`
- `VpcEndpoint`: `"VpcEndpointTypeDef"`


## EndpointAuthorizationTypeDef

```python
from mypy_boto3_redshift.type_defs import EndpointAuthorizationTypeDef
```




Optional fields:
- `Grantor`: `str`
- `Grantee`: `str`
- `ClusterIdentifier`: `str`
- `AuthorizeTime`: `datetime`
- `ClusterStatus`: `str`
- `Status`: `AuthorizationStatus`
- `AllowedAllVPCs`: `bool`
- `AllowedVPCs`: `List[str]`
- `EndpointCount`: `int`


## EndpointTypeDef

```python
from mypy_boto3_redshift.type_defs import EndpointTypeDef
```




Optional fields:
- `Address`: `str`
- `Port`: `int`
- `VpcEndpoints`: `List["VpcEndpointTypeDef"]`


## EventCategoriesMapTypeDef

```python
from mypy_boto3_redshift.type_defs import EventCategoriesMapTypeDef
```




Optional fields:
- `SourceType`: `str`
- `Events`: `List["EventInfoMapTypeDef"]`


## EventInfoMapTypeDef

```python
from mypy_boto3_redshift.type_defs import EventInfoMapTypeDef
```




Optional fields:
- `EventId`: `str`
- `EventCategories`: `List[str]`
- `EventDescription`: `str`
- `Severity`: `str`


## EventSubscriptionTypeDef

```python
from mypy_boto3_redshift.type_defs import EventSubscriptionTypeDef
```




Optional fields:
- `CustomerAwsId`: `str`
- `CustSubscriptionId`: `str`
- `SnsTopicArn`: `str`
- `Status`: `str`
- `SubscriptionCreationTime`: `datetime`
- `SourceType`: `str`
- `SourceIdsList`: `List[str]`
- `EventCategoriesList`: `List[str]`
- `Severity`: `str`
- `Enabled`: `bool`
- `Tags`: `List["TagTypeDef"]`


## EventTypeDef

```python
from mypy_boto3_redshift.type_defs import EventTypeDef
```




Optional fields:
- `SourceIdentifier`: `str`
- `SourceType`: `SourceType`
- `Message`: `str`
- `EventCategories`: `List[str]`
- `Severity`: `str`
- `Date`: `datetime`
- `EventId`: `str`


## HsmClientCertificateTypeDef

```python
from mypy_boto3_redshift.type_defs import HsmClientCertificateTypeDef
```




Optional fields:
- `HsmClientCertificateIdentifier`: `str`
- `HsmClientCertificatePublicKey`: `str`
- `Tags`: `List["TagTypeDef"]`


## HsmConfigurationTypeDef

```python
from mypy_boto3_redshift.type_defs import HsmConfigurationTypeDef
```




Optional fields:
- `HsmConfigurationIdentifier`: `str`
- `Description`: `str`
- `HsmIpAddress`: `str`
- `HsmPartitionName`: `str`
- `Tags`: `List["TagTypeDef"]`


## HsmStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import HsmStatusTypeDef
```




Optional fields:
- `HsmClientCertificateIdentifier`: `str`
- `HsmConfigurationIdentifier`: `str`
- `Status`: `str`


## IPRangeTypeDef

```python
from mypy_boto3_redshift.type_defs import IPRangeTypeDef
```




Optional fields:
- `Status`: `str`
- `CIDRIP`: `str`
- `Tags`: `List["TagTypeDef"]`


## MaintenanceTrackTypeDef

```python
from mypy_boto3_redshift.type_defs import MaintenanceTrackTypeDef
```




Optional fields:
- `MaintenanceTrackName`: `str`
- `DatabaseVersion`: `str`
- `UpdateTargets`: `List["UpdateTargetTypeDef"]`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_redshift.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `NetworkInterfaceId`: `str`
- `SubnetId`: `str`
- `PrivateIpAddress`: `str`
- `AvailabilityZone`: `str`


## NodeConfigurationOptionTypeDef

```python
from mypy_boto3_redshift.type_defs import NodeConfigurationOptionTypeDef
```




Optional fields:
- `NodeType`: `str`
- `NumberOfNodes`: `int`
- `EstimatedDiskUtilizationPercent`: `float`
- `Mode`: `Mode`


## OrderableClusterOptionTypeDef

```python
from mypy_boto3_redshift.type_defs import OrderableClusterOptionTypeDef
```




Optional fields:
- `ClusterVersion`: `str`
- `ClusterType`: `str`
- `NodeType`: `str`
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`


## ParameterTypeDef

```python
from mypy_boto3_redshift.type_defs import ParameterTypeDef
```




Optional fields:
- `ParameterName`: `str`
- `ParameterValue`: `str`
- `Description`: `str`
- `Source`: `str`
- `DataType`: `str`
- `AllowedValues`: `str`
- `ApplyType`: `ParameterApplyType`
- `IsModifiable`: `bool`
- `MinimumEngineVersion`: `str`


## PartnerIntegrationInfoTypeDef

```python
from mypy_boto3_redshift.type_defs import PartnerIntegrationInfoTypeDef
```




Optional fields:
- `DatabaseName`: `str`
- `PartnerName`: `str`
- `Status`: `PartnerIntegrationStatus`
- `StatusMessage`: `str`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`


## PauseClusterMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import PauseClusterMessageTypeDef
```


Required fields:
- `ClusterIdentifier`: `str`




## PendingModifiedValuesTypeDef

```python
from mypy_boto3_redshift.type_defs import PendingModifiedValuesTypeDef
```




Optional fields:
- `MasterUserPassword`: `str`
- `NodeType`: `str`
- `NumberOfNodes`: `int`
- `ClusterType`: `str`
- `ClusterVersion`: `str`
- `AutomatedSnapshotRetentionPeriod`: `int`
- `ClusterIdentifier`: `str`
- `PubliclyAccessible`: `bool`
- `EnhancedVpcRouting`: `bool`
- `MaintenanceTrackName`: `str`
- `EncryptionType`: `str`


## RecurringChargeTypeDef

```python
from mypy_boto3_redshift.type_defs import RecurringChargeTypeDef
```




Optional fields:
- `RecurringChargeAmount`: `float`
- `RecurringChargeFrequency`: `str`


## ReservedNodeOfferingTypeDef

```python
from mypy_boto3_redshift.type_defs import ReservedNodeOfferingTypeDef
```




Optional fields:
- `ReservedNodeOfferingId`: `str`
- `NodeType`: `str`
- `Duration`: `int`
- `FixedPrice`: `float`
- `UsagePrice`: `float`
- `CurrencyCode`: `str`
- `OfferingType`: `str`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`
- `ReservedNodeOfferingType`: `ReservedNodeOfferingType`


## ReservedNodeTypeDef

```python
from mypy_boto3_redshift.type_defs import ReservedNodeTypeDef
```




Optional fields:
- `ReservedNodeId`: `str`
- `ReservedNodeOfferingId`: `str`
- `NodeType`: `str`
- `StartTime`: `datetime`
- `Duration`: `int`
- `FixedPrice`: `float`
- `UsagePrice`: `float`
- `CurrencyCode`: `str`
- `NodeCount`: `int`
- `State`: `str`
- `OfferingType`: `str`
- `RecurringCharges`: `List["RecurringChargeTypeDef"]`
- `ReservedNodeOfferingType`: `ReservedNodeOfferingType`


## ResizeClusterMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ResizeClusterMessageTypeDef
```


Required fields:
- `ClusterIdentifier`: `str`



Optional fields:
- `ClusterType`: `str`
- `NodeType`: `str`
- `NumberOfNodes`: `int`
- `Classic`: `bool`


## ResizeInfoTypeDef

```python
from mypy_boto3_redshift.type_defs import ResizeInfoTypeDef
```




Optional fields:
- `ResizeType`: `str`
- `AllowCancelResize`: `bool`


## RestoreStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import RestoreStatusTypeDef
```




Optional fields:
- `Status`: `str`
- `CurrentRestoreRateInMegaBytesPerSecond`: `float`
- `SnapshotSizeInMegaBytes`: `int`
- `ProgressInMegaBytes`: `int`
- `ElapsedTimeInSeconds`: `int`
- `EstimatedTimeToCompletionInSeconds`: `int`


## ResumeClusterMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ResumeClusterMessageTypeDef
```


Required fields:
- `ClusterIdentifier`: `str`




## RevisionTargetTypeDef

```python
from mypy_boto3_redshift.type_defs import RevisionTargetTypeDef
```




Optional fields:
- `DatabaseRevision`: `str`
- `Description`: `str`
- `DatabaseRevisionReleaseDate`: `datetime`


## ScheduledActionTypeDef

```python
from mypy_boto3_redshift.type_defs import ScheduledActionTypeDef
```




Optional fields:
- `ScheduledActionName`: `str`
- `TargetAction`: `"ScheduledActionTypeTypeDef"`
- `Schedule`: `str`
- `IamRole`: `str`
- `ScheduledActionDescription`: `str`
- `State`: `ScheduledActionState`
- `NextInvocations`: `List[datetime]`
- `StartTime`: `datetime`
- `EndTime`: `datetime`


## ScheduledActionTypeTypeDef

```python
from mypy_boto3_redshift.type_defs import ScheduledActionTypeTypeDef
```




Optional fields:
- `ResizeCluster`: `"ResizeClusterMessageTypeDef"`
- `PauseCluster`: `"PauseClusterMessageTypeDef"`
- `ResumeCluster`: `"ResumeClusterMessageTypeDef"`


## SnapshotCopyGrantTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotCopyGrantTypeDef
```




Optional fields:
- `SnapshotCopyGrantName`: `str`
- `KmsKeyId`: `str`
- `Tags`: `List["TagTypeDef"]`


## SnapshotErrorMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotErrorMessageTypeDef
```




Optional fields:
- `SnapshotIdentifier`: `str`
- `SnapshotClusterIdentifier`: `str`
- `FailureCode`: `str`
- `FailureReason`: `str`


## SnapshotScheduleTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotScheduleTypeDef
```




Optional fields:
- `ScheduleDefinitions`: `List[str]`
- `ScheduleIdentifier`: `str`
- `ScheduleDescription`: `str`
- `Tags`: `List["TagTypeDef"]`
- `NextInvocations`: `List[datetime]`
- `AssociatedClusterCount`: `int`
- `AssociatedClusters`: `List["ClusterAssociatedToScheduleTypeDef"]`


## SnapshotTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotTypeDef
```




Optional fields:
- `SnapshotIdentifier`: `str`
- `ClusterIdentifier`: `str`
- `SnapshotCreateTime`: `datetime`
- `Status`: `str`
- `Port`: `int`
- `AvailabilityZone`: `str`
- `ClusterCreateTime`: `datetime`
- `MasterUsername`: `str`
- `ClusterVersion`: `str`
- `EngineFullVersion`: `str`
- `SnapshotType`: `str`
- `NodeType`: `str`
- `NumberOfNodes`: `int`
- `DBName`: `str`
- `VpcId`: `str`
- `Encrypted`: `bool`
- `KmsKeyId`: `str`
- `EncryptedWithHSM`: `bool`
- `AccountsWithRestoreAccess`: `List["AccountWithRestoreAccessTypeDef"]`
- `OwnerAccount`: `str`
- `TotalBackupSizeInMegaBytes`: `float`
- `ActualIncrementalBackupSizeInMegaBytes`: `float`
- `BackupProgressInMegaBytes`: `float`
- `CurrentBackupRateInMegaBytesPerSecond`: `float`
- `EstimatedSecondsToCompletion`: `int`
- `ElapsedTimeInSeconds`: `int`
- `SourceRegion`: `str`
- `Tags`: `List["TagTypeDef"]`
- `RestorableNodeTypes`: `List[str]`
- `EnhancedVpcRouting`: `bool`
- `MaintenanceTrackName`: `str`
- `ManualSnapshotRetentionPeriod`: `int`
- `ManualSnapshotRemainingDays`: `int`
- `SnapshotRetentionStartTime`: `datetime`


## SubnetTypeDef

```python
from mypy_boto3_redshift.type_defs import SubnetTypeDef
```




Optional fields:
- `SubnetIdentifier`: `str`
- `SubnetAvailabilityZone`: `"AvailabilityZoneTypeDef"`
- `SubnetStatus`: `str`


## SupportedOperationTypeDef

```python
from mypy_boto3_redshift.type_defs import SupportedOperationTypeDef
```




Optional fields:
- `OperationName`: `str`


## SupportedPlatformTypeDef

```python
from mypy_boto3_redshift.type_defs import SupportedPlatformTypeDef
```




Optional fields:
- `Name`: `str`


## TableRestoreStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import TableRestoreStatusTypeDef
```




Optional fields:
- `TableRestoreRequestId`: `str`
- `Status`: `TableRestoreStatusType`
- `Message`: `str`
- `RequestTime`: `datetime`
- `ProgressInMegaBytes`: `int`
- `TotalDataInMegaBytes`: `int`
- `ClusterIdentifier`: `str`
- `SnapshotIdentifier`: `str`
- `SourceDatabaseName`: `str`
- `SourceSchemaName`: `str`
- `SourceTableName`: `str`
- `TargetDatabaseName`: `str`
- `TargetSchemaName`: `str`
- `NewTableName`: `str`


## TagTypeDef

```python
from mypy_boto3_redshift.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TaggedResourceTypeDef

```python
from mypy_boto3_redshift.type_defs import TaggedResourceTypeDef
```




Optional fields:
- `Tag`: `"TagTypeDef"`
- `ResourceName`: `str`
- `ResourceType`: `str`


## UpdateTargetTypeDef

```python
from mypy_boto3_redshift.type_defs import UpdateTargetTypeDef
```




Optional fields:
- `MaintenanceTrackName`: `str`
- `DatabaseVersion`: `str`
- `SupportedOperations`: `List["SupportedOperationTypeDef"]`


## UsageLimitTypeDef

```python
from mypy_boto3_redshift.type_defs import UsageLimitTypeDef
```




Optional fields:
- `UsageLimitId`: `str`
- `ClusterIdentifier`: `str`
- `FeatureType`: `UsageLimitFeatureType`
- `LimitType`: `UsageLimitLimitType`
- `Amount`: `int`
- `Period`: `UsageLimitPeriod`
- `BreachAction`: `UsageLimitBreachAction`
- `Tags`: `List["TagTypeDef"]`


## VpcEndpointTypeDef

```python
from mypy_boto3_redshift.type_defs import VpcEndpointTypeDef
```




Optional fields:
- `VpcEndpointId`: `str`
- `VpcId`: `str`
- `NetworkInterfaces`: `List["NetworkInterfaceTypeDef"]`


## VpcSecurityGroupMembershipTypeDef

```python
from mypy_boto3_redshift.type_defs import VpcSecurityGroupMembershipTypeDef
```




Optional fields:
- `VpcSecurityGroupId`: `str`
- `Status`: `str`


## AcceptReservedNodeExchangeOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeOutputMessageTypeDef
```




Optional fields:
- `ExchangedReservedNode`: `"ReservedNodeTypeDef"`


## AccountAttributeListTypeDef

```python
from mypy_boto3_redshift.type_defs import AccountAttributeListTypeDef
```




Optional fields:
- `AccountAttributes`: `List["AccountAttributeTypeDef"]`


## AuthorizeClusterSecurityGroupIngressResultTypeDef

```python
from mypy_boto3_redshift.type_defs import AuthorizeClusterSecurityGroupIngressResultTypeDef
```




Optional fields:
- `ClusterSecurityGroup`: `"ClusterSecurityGroupTypeDef"`


## AuthorizeSnapshotAccessResultTypeDef

```python
from mypy_boto3_redshift.type_defs import AuthorizeSnapshotAccessResultTypeDef
```




Optional fields:
- `Snapshot`: `"SnapshotTypeDef"`


## BatchDeleteClusterSnapshotsResultTypeDef

```python
from mypy_boto3_redshift.type_defs import BatchDeleteClusterSnapshotsResultTypeDef
```




Optional fields:
- `Resources`: `List[str]`
- `Errors`: `List["SnapshotErrorMessageTypeDef"]`


## BatchModifyClusterSnapshotsOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import BatchModifyClusterSnapshotsOutputMessageTypeDef
```




Optional fields:
- `Resources`: `List[str]`
- `Errors`: `List["SnapshotErrorMessageTypeDef"]`


## ClusterCredentialsTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterCredentialsTypeDef
```




Optional fields:
- `DbUser`: `str`
- `DbPassword`: `str`
- `Expiration`: `datetime`


## ClusterDbRevisionsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterDbRevisionsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ClusterDbRevisions`: `List["ClusterDbRevisionTypeDef"]`


## ClusterParameterGroupDetailsTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterParameterGroupDetailsTypeDef
```




Optional fields:
- `Parameters`: `List["ParameterTypeDef"]`
- `Marker`: `str`


## ClusterParameterGroupNameMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterParameterGroupNameMessageTypeDef
```




Optional fields:
- `ParameterGroupName`: `str`
- `ParameterGroupStatus`: `str`


## ClusterParameterGroupsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterParameterGroupsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ParameterGroups`: `List["ClusterParameterGroupTypeDef"]`


## ClusterSecurityGroupMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterSecurityGroupMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ClusterSecurityGroups`: `List["ClusterSecurityGroupTypeDef"]`


## ClusterSubnetGroupMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterSubnetGroupMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ClusterSubnetGroups`: `List["ClusterSubnetGroupTypeDef"]`


## ClusterVersionsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClusterVersionsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ClusterVersions`: `List["ClusterVersionTypeDef"]`


## ClustersMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ClustersMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `Clusters`: `List["ClusterTypeDef"]`


## CopyClusterSnapshotResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CopyClusterSnapshotResultTypeDef
```




Optional fields:
- `Snapshot`: `"SnapshotTypeDef"`


## CreateClusterParameterGroupResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateClusterParameterGroupResultTypeDef
```




Optional fields:
- `ClusterParameterGroup`: `"ClusterParameterGroupTypeDef"`


## CreateClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## CreateClusterSecurityGroupResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateClusterSecurityGroupResultTypeDef
```




Optional fields:
- `ClusterSecurityGroup`: `"ClusterSecurityGroupTypeDef"`


## CreateClusterSnapshotResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateClusterSnapshotResultTypeDef
```




Optional fields:
- `Snapshot`: `"SnapshotTypeDef"`


## CreateClusterSubnetGroupResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateClusterSubnetGroupResultTypeDef
```




Optional fields:
- `ClusterSubnetGroup`: `"ClusterSubnetGroupTypeDef"`


## CreateEventSubscriptionResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## CreateHsmClientCertificateResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateHsmClientCertificateResultTypeDef
```




Optional fields:
- `HsmClientCertificate`: `"HsmClientCertificateTypeDef"`


## CreateHsmConfigurationResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateHsmConfigurationResultTypeDef
```




Optional fields:
- `HsmConfiguration`: `"HsmConfigurationTypeDef"`


## CreateSnapshotCopyGrantResultTypeDef

```python
from mypy_boto3_redshift.type_defs import CreateSnapshotCopyGrantResultTypeDef
```




Optional fields:
- `SnapshotCopyGrant`: `"SnapshotCopyGrantTypeDef"`


## CustomerStorageMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import CustomerStorageMessageTypeDef
```




Optional fields:
- `TotalBackupSizeInMegaBytes`: `float`
- `TotalProvisionedStorageInMegaBytes`: `float`


## DeleteClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import DeleteClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## DeleteClusterSnapshotMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import DeleteClusterSnapshotMessageTypeDef
```


Required fields:
- `SnapshotIdentifier`: `str`



Optional fields:
- `SnapshotClusterIdentifier`: `str`


## DeleteClusterSnapshotResultTypeDef

```python
from mypy_boto3_redshift.type_defs import DeleteClusterSnapshotResultTypeDef
```




Optional fields:
- `Snapshot`: `"SnapshotTypeDef"`


## DescribeDefaultClusterParametersResultTypeDef

```python
from mypy_boto3_redshift.type_defs import DescribeDefaultClusterParametersResultTypeDef
```




Optional fields:
- `DefaultClusterParameters`: `"DefaultClusterParametersTypeDef"`


## DescribePartnersOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import DescribePartnersOutputMessageTypeDef
```




Optional fields:
- `PartnerIntegrationInfoList`: `List["PartnerIntegrationInfoTypeDef"]`


## DescribeSnapshotSchedulesOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import DescribeSnapshotSchedulesOutputMessageTypeDef
```




Optional fields:
- `SnapshotSchedules`: `List["SnapshotScheduleTypeDef"]`
- `Marker`: `str`


## DisableSnapshotCopyResultTypeDef

```python
from mypy_boto3_redshift.type_defs import DisableSnapshotCopyResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## EnableSnapshotCopyResultTypeDef

```python
from mypy_boto3_redshift.type_defs import EnableSnapshotCopyResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## EndpointAccessListTypeDef

```python
from mypy_boto3_redshift.type_defs import EndpointAccessListTypeDef
```




Optional fields:
- `EndpointAccessList`: `List["EndpointAccessTypeDef"]`
- `Marker`: `str`


## EndpointAuthorizationListTypeDef

```python
from mypy_boto3_redshift.type_defs import EndpointAuthorizationListTypeDef
```




Optional fields:
- `EndpointAuthorizationList`: `List["EndpointAuthorizationTypeDef"]`
- `Marker`: `str`


## EventCategoriesMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import EventCategoriesMessageTypeDef
```




Optional fields:
- `EventCategoriesMapList`: `List["EventCategoriesMapTypeDef"]`


## EventSubscriptionsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import EventSubscriptionsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `EventSubscriptionsList`: `List["EventSubscriptionTypeDef"]`


## EventsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import EventsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `Events`: `List["EventTypeDef"]`


## GetReservedNodeExchangeOfferingsOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import GetReservedNodeExchangeOfferingsOutputMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ReservedNodeOfferings`: `List["ReservedNodeOfferingTypeDef"]`


## HsmClientCertificateMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import HsmClientCertificateMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `HsmClientCertificates`: `List["HsmClientCertificateTypeDef"]`


## HsmConfigurationMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import HsmConfigurationMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `HsmConfigurations`: `List["HsmConfigurationTypeDef"]`


## LoggingStatusTypeDef

```python
from mypy_boto3_redshift.type_defs import LoggingStatusTypeDef
```




Optional fields:
- `LoggingEnabled`: `bool`
- `BucketName`: `str`
- `S3KeyPrefix`: `str`
- `LastSuccessfulDeliveryTime`: `datetime`
- `LastFailureTime`: `datetime`
- `LastFailureMessage`: `str`


## ModifyAquaOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyAquaOutputMessageTypeDef
```




Optional fields:
- `AquaConfiguration`: `"AquaConfigurationTypeDef"`


## ModifyClusterDbRevisionResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyClusterDbRevisionResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ModifyClusterIamRolesResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyClusterIamRolesResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ModifyClusterMaintenanceResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyClusterMaintenanceResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ModifyClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ModifyClusterSnapshotResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyClusterSnapshotResultTypeDef
```




Optional fields:
- `Snapshot`: `"SnapshotTypeDef"`


## ModifyClusterSubnetGroupResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyClusterSubnetGroupResultTypeDef
```




Optional fields:
- `ClusterSubnetGroup`: `"ClusterSubnetGroupTypeDef"`


## ModifyEventSubscriptionResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifyEventSubscriptionResultTypeDef
```




Optional fields:
- `EventSubscription`: `"EventSubscriptionTypeDef"`


## ModifySnapshotCopyRetentionPeriodResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ModifySnapshotCopyRetentionPeriodResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## NodeConfigurationOptionsFilterTypeDef

```python
from mypy_boto3_redshift.type_defs import NodeConfigurationOptionsFilterTypeDef
```




Optional fields:
- `Name`: `NodeConfigurationOptionsFilterName`
- `Operator`: `OperatorType`
- `Values`: `List[str]`


## NodeConfigurationOptionsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import NodeConfigurationOptionsMessageTypeDef
```




Optional fields:
- `NodeConfigurationOptionList`: `List["NodeConfigurationOptionTypeDef"]`
- `Marker`: `str`


## OrderableClusterOptionsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import OrderableClusterOptionsMessageTypeDef
```




Optional fields:
- `OrderableClusterOptions`: `List["OrderableClusterOptionTypeDef"]`
- `Marker`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_redshift.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PartnerIntegrationOutputMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import PartnerIntegrationOutputMessageTypeDef
```




Optional fields:
- `DatabaseName`: `str`
- `PartnerName`: `str`


## PauseClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import PauseClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## PurchaseReservedNodeOfferingResultTypeDef

```python
from mypy_boto3_redshift.type_defs import PurchaseReservedNodeOfferingResultTypeDef
```




Optional fields:
- `ReservedNode`: `"ReservedNodeTypeDef"`


## RebootClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import RebootClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ReservedNodeOfferingsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ReservedNodeOfferingsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ReservedNodeOfferings`: `List["ReservedNodeOfferingTypeDef"]`


## ReservedNodesMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ReservedNodesMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ReservedNodes`: `List["ReservedNodeTypeDef"]`


## ResizeClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ResizeClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ResizeProgressMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ResizeProgressMessageTypeDef
```




Optional fields:
- `TargetNodeType`: `str`
- `TargetNumberOfNodes`: `int`
- `TargetClusterType`: `str`
- `Status`: `str`
- `ImportTablesCompleted`: `List[str]`
- `ImportTablesInProgress`: `List[str]`
- `ImportTablesNotStarted`: `List[str]`
- `AvgResizeRateInMegaBytesPerSecond`: `float`
- `TotalResizeDataInMegaBytes`: `int`
- `ProgressInMegaBytes`: `int`
- `ElapsedTimeInSeconds`: `int`
- `EstimatedTimeToCompletionInSeconds`: `int`
- `ResizeType`: `str`
- `Message`: `str`
- `TargetEncryptionType`: `str`
- `DataTransferProgressPercent`: `float`


## RestoreFromClusterSnapshotResultTypeDef

```python
from mypy_boto3_redshift.type_defs import RestoreFromClusterSnapshotResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## RestoreTableFromClusterSnapshotResultTypeDef

```python
from mypy_boto3_redshift.type_defs import RestoreTableFromClusterSnapshotResultTypeDef
```




Optional fields:
- `TableRestoreStatus`: `"TableRestoreStatusTypeDef"`


## ResumeClusterResultTypeDef

```python
from mypy_boto3_redshift.type_defs import ResumeClusterResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## RevokeClusterSecurityGroupIngressResultTypeDef

```python
from mypy_boto3_redshift.type_defs import RevokeClusterSecurityGroupIngressResultTypeDef
```




Optional fields:
- `ClusterSecurityGroup`: `"ClusterSecurityGroupTypeDef"`


## RevokeSnapshotAccessResultTypeDef

```python
from mypy_boto3_redshift.type_defs import RevokeSnapshotAccessResultTypeDef
```




Optional fields:
- `Snapshot`: `"SnapshotTypeDef"`


## RotateEncryptionKeyResultTypeDef

```python
from mypy_boto3_redshift.type_defs import RotateEncryptionKeyResultTypeDef
```




Optional fields:
- `Cluster`: `"ClusterTypeDef"`


## ScheduledActionFilterTypeDef

```python
from mypy_boto3_redshift.type_defs import ScheduledActionFilterTypeDef
```


Required fields:
- `Name`: `ScheduledActionFilterName`
- `Values`: `List[str]`




## ScheduledActionsMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import ScheduledActionsMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `ScheduledActions`: `List["ScheduledActionTypeDef"]`


## SnapshotCopyGrantMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotCopyGrantMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `SnapshotCopyGrants`: `List["SnapshotCopyGrantTypeDef"]`


## SnapshotMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotMessageTypeDef
```




Optional fields:
- `Marker`: `str`
- `Snapshots`: `List["SnapshotTypeDef"]`


## SnapshotSortingEntityTypeDef

```python
from mypy_boto3_redshift.type_defs import SnapshotSortingEntityTypeDef
```


Required fields:
- `Attribute`: `SnapshotAttributeToSortBy`



Optional fields:
- `SortOrder`: `SortByOrder`


## TableRestoreStatusMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import TableRestoreStatusMessageTypeDef
```




Optional fields:
- `TableRestoreStatusDetails`: `List["TableRestoreStatusTypeDef"]`
- `Marker`: `str`


## TaggedResourceListMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import TaggedResourceListMessageTypeDef
```




Optional fields:
- `TaggedResources`: `List["TaggedResourceTypeDef"]`
- `Marker`: `str`


## TrackListMessageTypeDef

```python
from mypy_boto3_redshift.type_defs import TrackListMessageTypeDef
```




Optional fields:
- `MaintenanceTracks`: `List["MaintenanceTrackTypeDef"]`
- `Marker`: `str`


## UsageLimitListTypeDef

```python
from mypy_boto3_redshift.type_defs import UsageLimitListTypeDef
```




Optional fields:
- `UsageLimits`: `List["UsageLimitTypeDef"]`
- `Marker`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_redshift.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

