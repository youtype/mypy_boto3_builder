# Literals for boto3 Redshift module

> [Index](../index.md) > [Redshift](./index.md) > Literals

Auto-generated documentation for [Redshift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift)
type annotations stubs module [mypy_boto3_redshift](https://pypi.org/project/mypy-boto3-redshift/).

- [Literals for boto3 Redshift module](#literals-for-boto3-redshift-module)
  - [ActionType](#actiontype)
  - [AquaConfigurationStatus](#aquaconfigurationstatus)
  - [AquaStatus](#aquastatus)
  - [AuthorizationStatus](#authorizationstatus)
  - [ClusterAvailableWaiterName](#clusteravailablewaitername)
  - [ClusterDeletedWaiterName](#clusterdeletedwaitername)
  - [ClusterRestoredWaiterName](#clusterrestoredwaitername)
  - [DescribeClusterDbRevisionsPaginatorName](#describeclusterdbrevisionspaginatorname)
  - [DescribeClusterParameterGroupsPaginatorName](#describeclusterparametergroupspaginatorname)
  - [DescribeClusterParametersPaginatorName](#describeclusterparameterspaginatorname)
  - [DescribeClusterSecurityGroupsPaginatorName](#describeclustersecuritygroupspaginatorname)
  - [DescribeClusterSnapshotsPaginatorName](#describeclustersnapshotspaginatorname)
  - [DescribeClusterSubnetGroupsPaginatorName](#describeclustersubnetgroupspaginatorname)
  - [DescribeClusterTracksPaginatorName](#describeclustertrackspaginatorname)
  - [DescribeClusterVersionsPaginatorName](#describeclusterversionspaginatorname)
  - [DescribeClustersPaginatorName](#describeclusterspaginatorname)
  - [DescribeDefaultClusterParametersPaginatorName](#describedefaultclusterparameterspaginatorname)
  - [DescribeEndpointAccessPaginatorName](#describeendpointaccesspaginatorname)
  - [DescribeEndpointAuthorizationPaginatorName](#describeendpointauthorizationpaginatorname)
  - [DescribeEventSubscriptionsPaginatorName](#describeeventsubscriptionspaginatorname)
  - [DescribeEventsPaginatorName](#describeeventspaginatorname)
  - [DescribeHsmClientCertificatesPaginatorName](#describehsmclientcertificatespaginatorname)
  - [DescribeHsmConfigurationsPaginatorName](#describehsmconfigurationspaginatorname)
  - [DescribeNodeConfigurationOptionsPaginatorName](#describenodeconfigurationoptionspaginatorname)
  - [DescribeOrderableClusterOptionsPaginatorName](#describeorderableclusteroptionspaginatorname)
  - [DescribeReservedNodeOfferingsPaginatorName](#describereservednodeofferingspaginatorname)
  - [DescribeReservedNodesPaginatorName](#describereservednodespaginatorname)
  - [DescribeScheduledActionsPaginatorName](#describescheduledactionspaginatorname)
  - [DescribeSnapshotCopyGrantsPaginatorName](#describesnapshotcopygrantspaginatorname)
  - [DescribeSnapshotSchedulesPaginatorName](#describesnapshotschedulespaginatorname)
  - [DescribeTableRestoreStatusPaginatorName](#describetablerestorestatuspaginatorname)
  - [DescribeTagsPaginatorName](#describetagspaginatorname)
  - [DescribeUsageLimitsPaginatorName](#describeusagelimitspaginatorname)
  - [GetReservedNodeExchangeOfferingsPaginatorName](#getreservednodeexchangeofferingspaginatorname)
  - [Mode](#mode)
  - [NodeConfigurationOptionsFilterName](#nodeconfigurationoptionsfiltername)
  - [OperatorType](#operatortype)
  - [ParameterApplyType](#parameterapplytype)
  - [PartnerIntegrationStatus](#partnerintegrationstatus)
  - [ReservedNodeOfferingType](#reservednodeofferingtype)
  - [ScheduleState](#schedulestate)
  - [ScheduledActionFilterName](#scheduledactionfiltername)
  - [ScheduledActionState](#scheduledactionstate)
  - [ScheduledActionTypeValues](#scheduledactiontypevalues)
  - [SnapshotAttributeToSortBy](#snapshotattributetosortby)
  - [SnapshotAvailableWaiterName](#snapshotavailablewaitername)
  - [SortByOrder](#sortbyorder)
  - [SourceType](#sourcetype)
  - [TableRestoreStatusType](#tablerestorestatustype)
  - [UsageLimitBreachAction](#usagelimitbreachaction)
  - [UsageLimitFeatureType](#usagelimitfeaturetype)
  - [UsageLimitLimitType](#usagelimitlimittype)
  - [UsageLimitPeriod](#usagelimitperiod)

## ActionType

```python
from mypy_boto3_redshift.literals import ActionType
```

Values:

- `recommend-node-config`
- `resize-cluster`
- `restore-cluster`

## AquaConfigurationStatus

```python
from mypy_boto3_redshift.literals import AquaConfigurationStatus
```

Values:

- `auto`
- `disabled`
- `enabled`

## AquaStatus

```python
from mypy_boto3_redshift.literals import AquaStatus
```

Values:

- `applying`
- `disabled`
- `enabled`

## AuthorizationStatus

```python
from mypy_boto3_redshift.literals import AuthorizationStatus
```

Values:

- `Authorized`
- `Revoking`

## ClusterAvailableWaiterName

```python
from mypy_boto3_redshift.literals import ClusterAvailableWaiterName
```

Values:

- `cluster_available`

## ClusterDeletedWaiterName

```python
from mypy_boto3_redshift.literals import ClusterDeletedWaiterName
```

Values:

- `cluster_deleted`

## ClusterRestoredWaiterName

```python
from mypy_boto3_redshift.literals import ClusterRestoredWaiterName
```

Values:

- `cluster_restored`

## DescribeClusterDbRevisionsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterDbRevisionsPaginatorName
```

Values:

- `describe_cluster_db_revisions`

## DescribeClusterParameterGroupsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterParameterGroupsPaginatorName
```

Values:

- `describe_cluster_parameter_groups`

## DescribeClusterParametersPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterParametersPaginatorName
```

Values:

- `describe_cluster_parameters`

## DescribeClusterSecurityGroupsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterSecurityGroupsPaginatorName
```

Values:

- `describe_cluster_security_groups`

## DescribeClusterSnapshotsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterSnapshotsPaginatorName
```

Values:

- `describe_cluster_snapshots`

## DescribeClusterSubnetGroupsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterSubnetGroupsPaginatorName
```

Values:

- `describe_cluster_subnet_groups`

## DescribeClusterTracksPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterTracksPaginatorName
```

Values:

- `describe_cluster_tracks`

## DescribeClusterVersionsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClusterVersionsPaginatorName
```

Values:

- `describe_cluster_versions`

## DescribeClustersPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeClustersPaginatorName
```

Values:

- `describe_clusters`

## DescribeDefaultClusterParametersPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeDefaultClusterParametersPaginatorName
```

Values:

- `describe_default_cluster_parameters`

## DescribeEndpointAccessPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeEndpointAccessPaginatorName
```

Values:

- `describe_endpoint_access`

## DescribeEndpointAuthorizationPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeEndpointAuthorizationPaginatorName
```

Values:

- `describe_endpoint_authorization`

## DescribeEventSubscriptionsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeEventSubscriptionsPaginatorName
```

Values:

- `describe_event_subscriptions`

## DescribeEventsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeEventsPaginatorName
```

Values:

- `describe_events`

## DescribeHsmClientCertificatesPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeHsmClientCertificatesPaginatorName
```

Values:

- `describe_hsm_client_certificates`

## DescribeHsmConfigurationsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeHsmConfigurationsPaginatorName
```

Values:

- `describe_hsm_configurations`

## DescribeNodeConfigurationOptionsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeNodeConfigurationOptionsPaginatorName
```

Values:

- `describe_node_configuration_options`

## DescribeOrderableClusterOptionsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeOrderableClusterOptionsPaginatorName
```

Values:

- `describe_orderable_cluster_options`

## DescribeReservedNodeOfferingsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeReservedNodeOfferingsPaginatorName
```

Values:

- `describe_reserved_node_offerings`

## DescribeReservedNodesPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeReservedNodesPaginatorName
```

Values:

- `describe_reserved_nodes`

## DescribeScheduledActionsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeScheduledActionsPaginatorName
```

Values:

- `describe_scheduled_actions`

## DescribeSnapshotCopyGrantsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeSnapshotCopyGrantsPaginatorName
```

Values:

- `describe_snapshot_copy_grants`

## DescribeSnapshotSchedulesPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeSnapshotSchedulesPaginatorName
```

Values:

- `describe_snapshot_schedules`

## DescribeTableRestoreStatusPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeTableRestoreStatusPaginatorName
```

Values:

- `describe_table_restore_status`

## DescribeTagsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeTagsPaginatorName
```

Values:

- `describe_tags`

## DescribeUsageLimitsPaginatorName

```python
from mypy_boto3_redshift.literals import DescribeUsageLimitsPaginatorName
```

Values:

- `describe_usage_limits`

## GetReservedNodeExchangeOfferingsPaginatorName

```python
from mypy_boto3_redshift.literals import GetReservedNodeExchangeOfferingsPaginatorName
```

Values:

- `get_reserved_node_exchange_offerings`

## Mode

```python
from mypy_boto3_redshift.literals import Mode
```

Values:

- `high-performance`
- `standard`

## NodeConfigurationOptionsFilterName

```python
from mypy_boto3_redshift.literals import NodeConfigurationOptionsFilterName
```

Values:

- `EstimatedDiskUtilizationPercent`
- `Mode`
- `NodeType`
- `NumberOfNodes`

## OperatorType

```python
from mypy_boto3_redshift.literals import OperatorType
```

Values:

- `between`
- `eq`
- `ge`
- `gt`
- `in`
- `le`
- `lt`

## ParameterApplyType

```python
from mypy_boto3_redshift.literals import ParameterApplyType
```

Values:

- `dynamic`
- `static`

## PartnerIntegrationStatus

```python
from mypy_boto3_redshift.literals import PartnerIntegrationStatus
```

Values:

- `Active`
- `ConnectionFailure`
- `Inactive`
- `RuntimeFailure`

## ReservedNodeOfferingType

```python
from mypy_boto3_redshift.literals import ReservedNodeOfferingType
```

Values:

- `Regular`
- `Upgradable`

## ScheduleState

```python
from mypy_boto3_redshift.literals import ScheduleState
```

Values:

- `ACTIVE`
- `FAILED`
- `MODIFYING`

## ScheduledActionFilterName

```python
from mypy_boto3_redshift.literals import ScheduledActionFilterName
```

Values:

- `cluster-identifier`
- `iam-role`

## ScheduledActionState

```python
from mypy_boto3_redshift.literals import ScheduledActionState
```

Values:

- `ACTIVE`
- `DISABLED`

## ScheduledActionTypeValues

```python
from mypy_boto3_redshift.literals import ScheduledActionTypeValues
```

Values:

- `PauseCluster`
- `ResizeCluster`
- `ResumeCluster`

## SnapshotAttributeToSortBy

```python
from mypy_boto3_redshift.literals import SnapshotAttributeToSortBy
```

Values:

- `CREATE_TIME`
- `SOURCE_TYPE`
- `TOTAL_SIZE`

## SnapshotAvailableWaiterName

```python
from mypy_boto3_redshift.literals import SnapshotAvailableWaiterName
```

Values:

- `snapshot_available`

## SortByOrder

```python
from mypy_boto3_redshift.literals import SortByOrder
```

Values:

- `ASC`
- `DESC`

## SourceType

```python
from mypy_boto3_redshift.literals import SourceType
```

Values:

- `cluster`
- `cluster-parameter-group`
- `cluster-security-group`
- `cluster-snapshot`
- `scheduled-action`

## TableRestoreStatusType

```python
from mypy_boto3_redshift.literals import TableRestoreStatusType
```

Values:

- `CANCELED`
- `FAILED`
- `IN_PROGRESS`
- `PENDING`
- `SUCCEEDED`

## UsageLimitBreachAction

```python
from mypy_boto3_redshift.literals import UsageLimitBreachAction
```

Values:

- `disable`
- `emit-metric`
- `log`

## UsageLimitFeatureType

```python
from mypy_boto3_redshift.literals import UsageLimitFeatureType
```

Values:

- `concurrency-scaling`
- `spectrum`

## UsageLimitLimitType

```python
from mypy_boto3_redshift.literals import UsageLimitLimitType
```

Values:

- `data-scanned`
- `time`

## UsageLimitPeriod

```python
from mypy_boto3_redshift.literals import UsageLimitPeriod
```

Values:

- `daily`
- `monthly`
- `weekly`
