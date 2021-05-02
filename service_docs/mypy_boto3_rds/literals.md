# Literals for boto3 RDS module

> [Index](../index.md) > [RDS](./index.md) > Literals

Auto-generated documentation for [RDS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
type annotations stubs module [mypy_boto3_rds](https://pypi.org/project/mypy-boto3-rds/).

- [Literals for boto3 RDS module](#literals-for-boto3-rds-module)
  - [ActivityStreamMode](#activitystreammode)
  - [ActivityStreamStatus](#activitystreamstatus)
  - [ApplyMethod](#applymethod)
  - [AuthScheme](#authscheme)
  - [DBClusterSnapshotAvailableWaiterName](#dbclustersnapshotavailablewaitername)
  - [DBClusterSnapshotDeletedWaiterName](#dbclustersnapshotdeletedwaitername)
  - [DBInstanceAvailableWaiterName](#dbinstanceavailablewaitername)
  - [DBInstanceDeletedWaiterName](#dbinstancedeletedwaitername)
  - [DBProxyEndpointStatus](#dbproxyendpointstatus)
  - [DBProxyEndpointTargetRole](#dbproxyendpointtargetrole)
  - [DBProxyStatus](#dbproxystatus)
  - [DBSnapshotAvailableWaiterName](#dbsnapshotavailablewaitername)
  - [DBSnapshotCompletedWaiterName](#dbsnapshotcompletedwaitername)
  - [DBSnapshotDeletedWaiterName](#dbsnapshotdeletedwaitername)
  - [DescribeCertificatesPaginatorName](#describecertificatespaginatorname)
  - [DescribeCustomAvailabilityZonesPaginatorName](#describecustomavailabilityzonespaginatorname)
  - [DescribeDBClusterBacktracksPaginatorName](#describedbclusterbacktrackspaginatorname)
  - [DescribeDBClusterEndpointsPaginatorName](#describedbclusterendpointspaginatorname)
  - [DescribeDBClusterParameterGroupsPaginatorName](#describedbclusterparametergroupspaginatorname)
  - [DescribeDBClusterParametersPaginatorName](#describedbclusterparameterspaginatorname)
  - [DescribeDBClusterSnapshotsPaginatorName](#describedbclustersnapshotspaginatorname)
  - [DescribeDBClustersPaginatorName](#describedbclusterspaginatorname)
  - [DescribeDBEngineVersionsPaginatorName](#describedbengineversionspaginatorname)
  - [DescribeDBInstanceAutomatedBackupsPaginatorName](#describedbinstanceautomatedbackupspaginatorname)
  - [DescribeDBInstancesPaginatorName](#describedbinstancespaginatorname)
  - [DescribeDBLogFilesPaginatorName](#describedblogfilespaginatorname)
  - [DescribeDBParameterGroupsPaginatorName](#describedbparametergroupspaginatorname)
  - [DescribeDBParametersPaginatorName](#describedbparameterspaginatorname)
  - [DescribeDBProxiesPaginatorName](#describedbproxiespaginatorname)
  - [DescribeDBProxyEndpointsPaginatorName](#describedbproxyendpointspaginatorname)
  - [DescribeDBProxyTargetGroupsPaginatorName](#describedbproxytargetgroupspaginatorname)
  - [DescribeDBProxyTargetsPaginatorName](#describedbproxytargetspaginatorname)
  - [DescribeDBSecurityGroupsPaginatorName](#describedbsecuritygroupspaginatorname)
  - [DescribeDBSnapshotsPaginatorName](#describedbsnapshotspaginatorname)
  - [DescribeDBSubnetGroupsPaginatorName](#describedbsubnetgroupspaginatorname)
  - [DescribeEngineDefaultClusterParametersPaginatorName](#describeenginedefaultclusterparameterspaginatorname)
  - [DescribeEngineDefaultParametersPaginatorName](#describeenginedefaultparameterspaginatorname)
  - [DescribeEventSubscriptionsPaginatorName](#describeeventsubscriptionspaginatorname)
  - [DescribeEventsPaginatorName](#describeeventspaginatorname)
  - [DescribeExportTasksPaginatorName](#describeexporttaskspaginatorname)
  - [DescribeGlobalClustersPaginatorName](#describeglobalclusterspaginatorname)
  - [DescribeInstallationMediaPaginatorName](#describeinstallationmediapaginatorname)
  - [DescribeOptionGroupOptionsPaginatorName](#describeoptiongroupoptionspaginatorname)
  - [DescribeOptionGroupsPaginatorName](#describeoptiongroupspaginatorname)
  - [DescribeOrderableDBInstanceOptionsPaginatorName](#describeorderabledbinstanceoptionspaginatorname)
  - [DescribePendingMaintenanceActionsPaginatorName](#describependingmaintenanceactionspaginatorname)
  - [DescribeReservedDBInstancesOfferingsPaginatorName](#describereserveddbinstancesofferingspaginatorname)
  - [DescribeReservedDBInstancesPaginatorName](#describereserveddbinstancespaginatorname)
  - [DescribeSourceRegionsPaginatorName](#describesourceregionspaginatorname)
  - [DownloadDBLogFilePortionPaginatorName](#downloaddblogfileportionpaginatorname)
  - [EngineFamily](#enginefamily)
  - [FailoverStatus](#failoverstatus)
  - [IAMAuthMode](#iamauthmode)
  - [ReplicaMode](#replicamode)
  - [SourceType](#sourcetype)
  - [TargetHealthReason](#targethealthreason)
  - [TargetRole](#targetrole)
  - [TargetState](#targetstate)
  - [TargetType](#targettype)
  - [WriteForwardingStatus](#writeforwardingstatus)

## ActivityStreamMode

```python
from mypy_boto3_rds.literals import ActivityStreamMode
```

Values:

- `async`
- `sync`

## ActivityStreamStatus

```python
from mypy_boto3_rds.literals import ActivityStreamStatus
```

Values:

- `started`
- `starting`
- `stopped`
- `stopping`

## ApplyMethod

```python
from mypy_boto3_rds.literals import ApplyMethod
```

Values:

- `immediate`
- `pending-reboot`

## AuthScheme

```python
from mypy_boto3_rds.literals import AuthScheme
```

Values:

- `SECRETS`

## DBClusterSnapshotAvailableWaiterName

```python
from mypy_boto3_rds.literals import DBClusterSnapshotAvailableWaiterName
```

Values:

- `db_cluster_snapshot_available`

## DBClusterSnapshotDeletedWaiterName

```python
from mypy_boto3_rds.literals import DBClusterSnapshotDeletedWaiterName
```

Values:

- `db_cluster_snapshot_deleted`

## DBInstanceAvailableWaiterName

```python
from mypy_boto3_rds.literals import DBInstanceAvailableWaiterName
```

Values:

- `db_instance_available`

## DBInstanceDeletedWaiterName

```python
from mypy_boto3_rds.literals import DBInstanceDeletedWaiterName
```

Values:

- `db_instance_deleted`

## DBProxyEndpointStatus

```python
from mypy_boto3_rds.literals import DBProxyEndpointStatus
```

Values:

- `available`
- `creating`
- `deleting`
- `incompatible-network`
- `insufficient-resource-limits`
- `modifying`

## DBProxyEndpointTargetRole

```python
from mypy_boto3_rds.literals import DBProxyEndpointTargetRole
```

Values:

- `READ_ONLY`
- `READ_WRITE`

## DBProxyStatus

```python
from mypy_boto3_rds.literals import DBProxyStatus
```

Values:

- `available`
- `creating`
- `deleting`
- `incompatible-network`
- `insufficient-resource-limits`
- `modifying`
- `reactivating`
- `suspended`
- `suspending`

## DBSnapshotAvailableWaiterName

```python
from mypy_boto3_rds.literals import DBSnapshotAvailableWaiterName
```

Values:

- `db_snapshot_available`

## DBSnapshotCompletedWaiterName

```python
from mypy_boto3_rds.literals import DBSnapshotCompletedWaiterName
```

Values:

- `db_snapshot_completed`

## DBSnapshotDeletedWaiterName

```python
from mypy_boto3_rds.literals import DBSnapshotDeletedWaiterName
```

Values:

- `db_snapshot_deleted`

## DescribeCertificatesPaginatorName

```python
from mypy_boto3_rds.literals import DescribeCertificatesPaginatorName
```

Values:

- `describe_certificates`

## DescribeCustomAvailabilityZonesPaginatorName

```python
from mypy_boto3_rds.literals import DescribeCustomAvailabilityZonesPaginatorName
```

Values:

- `describe_custom_availability_zones`

## DescribeDBClusterBacktracksPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBClusterBacktracksPaginatorName
```

Values:

- `describe_db_cluster_backtracks`

## DescribeDBClusterEndpointsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBClusterEndpointsPaginatorName
```

Values:

- `describe_db_cluster_endpoints`

## DescribeDBClusterParameterGroupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBClusterParameterGroupsPaginatorName
```

Values:

- `describe_db_cluster_parameter_groups`

## DescribeDBClusterParametersPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBClusterParametersPaginatorName
```

Values:

- `describe_db_cluster_parameters`

## DescribeDBClusterSnapshotsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBClusterSnapshotsPaginatorName
```

Values:

- `describe_db_cluster_snapshots`

## DescribeDBClustersPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBClustersPaginatorName
```

Values:

- `describe_db_clusters`

## DescribeDBEngineVersionsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBEngineVersionsPaginatorName
```

Values:

- `describe_db_engine_versions`

## DescribeDBInstanceAutomatedBackupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBInstanceAutomatedBackupsPaginatorName
```

Values:

- `describe_db_instance_automated_backups`

## DescribeDBInstancesPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBInstancesPaginatorName
```

Values:

- `describe_db_instances`

## DescribeDBLogFilesPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBLogFilesPaginatorName
```

Values:

- `describe_db_log_files`

## DescribeDBParameterGroupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBParameterGroupsPaginatorName
```

Values:

- `describe_db_parameter_groups`

## DescribeDBParametersPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBParametersPaginatorName
```

Values:

- `describe_db_parameters`

## DescribeDBProxiesPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBProxiesPaginatorName
```

Values:

- `describe_db_proxies`

## DescribeDBProxyEndpointsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBProxyEndpointsPaginatorName
```

Values:

- `describe_db_proxy_endpoints`

## DescribeDBProxyTargetGroupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBProxyTargetGroupsPaginatorName
```

Values:

- `describe_db_proxy_target_groups`

## DescribeDBProxyTargetsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBProxyTargetsPaginatorName
```

Values:

- `describe_db_proxy_targets`

## DescribeDBSecurityGroupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBSecurityGroupsPaginatorName
```

Values:

- `describe_db_security_groups`

## DescribeDBSnapshotsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBSnapshotsPaginatorName
```

Values:

- `describe_db_snapshots`

## DescribeDBSubnetGroupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeDBSubnetGroupsPaginatorName
```

Values:

- `describe_db_subnet_groups`

## DescribeEngineDefaultClusterParametersPaginatorName

```python
from mypy_boto3_rds.literals import DescribeEngineDefaultClusterParametersPaginatorName
```

Values:

- `describe_engine_default_cluster_parameters`

## DescribeEngineDefaultParametersPaginatorName

```python
from mypy_boto3_rds.literals import DescribeEngineDefaultParametersPaginatorName
```

Values:

- `describe_engine_default_parameters`

## DescribeEventSubscriptionsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeEventSubscriptionsPaginatorName
```

Values:

- `describe_event_subscriptions`

## DescribeEventsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeEventsPaginatorName
```

Values:

- `describe_events`

## DescribeExportTasksPaginatorName

```python
from mypy_boto3_rds.literals import DescribeExportTasksPaginatorName
```

Values:

- `describe_export_tasks`

## DescribeGlobalClustersPaginatorName

```python
from mypy_boto3_rds.literals import DescribeGlobalClustersPaginatorName
```

Values:

- `describe_global_clusters`

## DescribeInstallationMediaPaginatorName

```python
from mypy_boto3_rds.literals import DescribeInstallationMediaPaginatorName
```

Values:

- `describe_installation_media`

## DescribeOptionGroupOptionsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeOptionGroupOptionsPaginatorName
```

Values:

- `describe_option_group_options`

## DescribeOptionGroupsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeOptionGroupsPaginatorName
```

Values:

- `describe_option_groups`

## DescribeOrderableDBInstanceOptionsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeOrderableDBInstanceOptionsPaginatorName
```

Values:

- `describe_orderable_db_instance_options`

## DescribePendingMaintenanceActionsPaginatorName

```python
from mypy_boto3_rds.literals import DescribePendingMaintenanceActionsPaginatorName
```

Values:

- `describe_pending_maintenance_actions`

## DescribeReservedDBInstancesOfferingsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeReservedDBInstancesOfferingsPaginatorName
```

Values:

- `describe_reserved_db_instances_offerings`

## DescribeReservedDBInstancesPaginatorName

```python
from mypy_boto3_rds.literals import DescribeReservedDBInstancesPaginatorName
```

Values:

- `describe_reserved_db_instances`

## DescribeSourceRegionsPaginatorName

```python
from mypy_boto3_rds.literals import DescribeSourceRegionsPaginatorName
```

Values:

- `describe_source_regions`

## DownloadDBLogFilePortionPaginatorName

```python
from mypy_boto3_rds.literals import DownloadDBLogFilePortionPaginatorName
```

Values:

- `download_db_log_file_portion`

## EngineFamily

```python
from mypy_boto3_rds.literals import EngineFamily
```

Values:

- `MYSQL`
- `POSTGRESQL`

## FailoverStatus

```python
from mypy_boto3_rds.literals import FailoverStatus
```

Values:

- `cancelling`
- `failing-over`
- `pending`

## IAMAuthMode

```python
from mypy_boto3_rds.literals import IAMAuthMode
```

Values:

- `DISABLED`
- `REQUIRED`

## ReplicaMode

```python
from mypy_boto3_rds.literals import ReplicaMode
```

Values:

- `mounted`
- `open-read-only`

## SourceType

```python
from mypy_boto3_rds.literals import SourceType
```

Values:

- `db-cluster`
- `db-cluster-snapshot`
- `db-instance`
- `db-parameter-group`
- `db-security-group`
- `db-snapshot`

## TargetHealthReason

```python
from mypy_boto3_rds.literals import TargetHealthReason
```

Values:

- `AUTH_FAILURE`
- `CONNECTION_FAILED`
- `INVALID_REPLICATION_STATE`
- `PENDING_PROXY_CAPACITY`
- `UNREACHABLE`

## TargetRole

```python
from mypy_boto3_rds.literals import TargetRole
```

Values:

- `READ_ONLY`
- `READ_WRITE`
- `UNKNOWN`

## TargetState

```python
from mypy_boto3_rds.literals import TargetState
```

Values:

- `AVAILABLE`
- `REGISTERING`
- `UNAVAILABLE`

## TargetType

```python
from mypy_boto3_rds.literals import TargetType
```

Values:

- `RDS_INSTANCE`
- `RDS_SERVERLESS_ENDPOINT`
- `TRACKED_CLUSTER`

## WriteForwardingStatus

```python
from mypy_boto3_rds.literals import WriteForwardingStatus
```

Values:

- `disabled`
- `disabling`
- `enabled`
- `enabling`
- `unknown`
