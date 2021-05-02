# Literals for boto3 ElastiCache module

> [Index](../index.md) > [ElastiCache](./index.md) > Literals

Auto-generated documentation for [ElastiCache](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache)
type annotations stubs module [mypy_boto3_elasticache](https://pypi.org/project/mypy-boto3-elasticache/).

- [Literals for boto3 ElastiCache module](#literals-for-boto3-elasticache-module)
  - [AZMode](#azmode)
  - [AuthTokenUpdateStatus](#authtokenupdatestatus)
  - [AuthTokenUpdateStrategyType](#authtokenupdatestrategytype)
  - [AuthenticationType](#authenticationtype)
  - [AutomaticFailoverStatus](#automaticfailoverstatus)
  - [CacheClusterAvailableWaiterName](#cacheclusteravailablewaitername)
  - [CacheClusterDeletedWaiterName](#cacheclusterdeletedwaitername)
  - [ChangeType](#changetype)
  - [DescribeCacheClustersPaginatorName](#describecacheclusterspaginatorname)
  - [DescribeCacheEngineVersionsPaginatorName](#describecacheengineversionspaginatorname)
  - [DescribeCacheParameterGroupsPaginatorName](#describecacheparametergroupspaginatorname)
  - [DescribeCacheParametersPaginatorName](#describecacheparameterspaginatorname)
  - [DescribeCacheSecurityGroupsPaginatorName](#describecachesecuritygroupspaginatorname)
  - [DescribeCacheSubnetGroupsPaginatorName](#describecachesubnetgroupspaginatorname)
  - [DescribeEngineDefaultParametersPaginatorName](#describeenginedefaultparameterspaginatorname)
  - [DescribeEventsPaginatorName](#describeeventspaginatorname)
  - [DescribeGlobalReplicationGroupsPaginatorName](#describeglobalreplicationgroupspaginatorname)
  - [DescribeReplicationGroupsPaginatorName](#describereplicationgroupspaginatorname)
  - [DescribeReservedCacheNodesOfferingsPaginatorName](#describereservedcachenodesofferingspaginatorname)
  - [DescribeReservedCacheNodesPaginatorName](#describereservedcachenodespaginatorname)
  - [DescribeServiceUpdatesPaginatorName](#describeserviceupdatespaginatorname)
  - [DescribeSnapshotsPaginatorName](#describesnapshotspaginatorname)
  - [DescribeUpdateActionsPaginatorName](#describeupdateactionspaginatorname)
  - [DescribeUserGroupsPaginatorName](#describeusergroupspaginatorname)
  - [DescribeUsersPaginatorName](#describeuserspaginatorname)
  - [DestinationType](#destinationtype)
  - [LogDeliveryConfigurationStatus](#logdeliveryconfigurationstatus)
  - [LogFormat](#logformat)
  - [LogType](#logtype)
  - [MultiAZStatus](#multiazstatus)
  - [NodeUpdateInitiatedBy](#nodeupdateinitiatedby)
  - [NodeUpdateStatus](#nodeupdatestatus)
  - [OutpostMode](#outpostmode)
  - [PendingAutomaticFailoverStatus](#pendingautomaticfailoverstatus)
  - [ReplicationGroupAvailableWaiterName](#replicationgroupavailablewaitername)
  - [ReplicationGroupDeletedWaiterName](#replicationgroupdeletedwaitername)
  - [ServiceUpdateSeverity](#serviceupdateseverity)
  - [ServiceUpdateStatus](#serviceupdatestatus)
  - [ServiceUpdateType](#serviceupdatetype)
  - [SlaMet](#slamet)
  - [SourceType](#sourcetype)
  - [UpdateActionStatus](#updateactionstatus)

## AZMode

```python
from mypy_boto3_elasticache.literals import AZMode
```

Values:

- `cross-az`
- `single-az`

## AuthTokenUpdateStatus

```python
from mypy_boto3_elasticache.literals import AuthTokenUpdateStatus
```

Values:

- `ROTATING`
- `SETTING`

## AuthTokenUpdateStrategyType

```python
from mypy_boto3_elasticache.literals import AuthTokenUpdateStrategyType
```

Values:

- `DELETE`
- `ROTATE`
- `SET`

## AuthenticationType

```python
from mypy_boto3_elasticache.literals import AuthenticationType
```

Values:

- `no-password`
- `password`

## AutomaticFailoverStatus

```python
from mypy_boto3_elasticache.literals import AutomaticFailoverStatus
```

Values:

- `disabled`
- `disabling`
- `enabled`
- `enabling`

## CacheClusterAvailableWaiterName

```python
from mypy_boto3_elasticache.literals import CacheClusterAvailableWaiterName
```

Values:

- `cache_cluster_available`

## CacheClusterDeletedWaiterName

```python
from mypy_boto3_elasticache.literals import CacheClusterDeletedWaiterName
```

Values:

- `cache_cluster_deleted`

## ChangeType

```python
from mypy_boto3_elasticache.literals import ChangeType
```

Values:

- `immediate`
- `requires-reboot`

## DescribeCacheClustersPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeCacheClustersPaginatorName
```

Values:

- `describe_cache_clusters`

## DescribeCacheEngineVersionsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeCacheEngineVersionsPaginatorName
```

Values:

- `describe_cache_engine_versions`

## DescribeCacheParameterGroupsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeCacheParameterGroupsPaginatorName
```

Values:

- `describe_cache_parameter_groups`

## DescribeCacheParametersPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeCacheParametersPaginatorName
```

Values:

- `describe_cache_parameters`

## DescribeCacheSecurityGroupsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeCacheSecurityGroupsPaginatorName
```

Values:

- `describe_cache_security_groups`

## DescribeCacheSubnetGroupsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeCacheSubnetGroupsPaginatorName
```

Values:

- `describe_cache_subnet_groups`

## DescribeEngineDefaultParametersPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeEngineDefaultParametersPaginatorName
```

Values:

- `describe_engine_default_parameters`

## DescribeEventsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeEventsPaginatorName
```

Values:

- `describe_events`

## DescribeGlobalReplicationGroupsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeGlobalReplicationGroupsPaginatorName
```

Values:

- `describe_global_replication_groups`

## DescribeReplicationGroupsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeReplicationGroupsPaginatorName
```

Values:

- `describe_replication_groups`

## DescribeReservedCacheNodesOfferingsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeReservedCacheNodesOfferingsPaginatorName
```

Values:

- `describe_reserved_cache_nodes_offerings`

## DescribeReservedCacheNodesPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeReservedCacheNodesPaginatorName
```

Values:

- `describe_reserved_cache_nodes`

## DescribeServiceUpdatesPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeServiceUpdatesPaginatorName
```

Values:

- `describe_service_updates`

## DescribeSnapshotsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeSnapshotsPaginatorName
```

Values:

- `describe_snapshots`

## DescribeUpdateActionsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeUpdateActionsPaginatorName
```

Values:

- `describe_update_actions`

## DescribeUserGroupsPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeUserGroupsPaginatorName
```

Values:

- `describe_user_groups`

## DescribeUsersPaginatorName

```python
from mypy_boto3_elasticache.literals import DescribeUsersPaginatorName
```

Values:

- `describe_users`

## DestinationType

```python
from mypy_boto3_elasticache.literals import DestinationType
```

Values:

- `cloudwatch-logs`
- `kinesis-firehose`

## LogDeliveryConfigurationStatus

```python
from mypy_boto3_elasticache.literals import LogDeliveryConfigurationStatus
```

Values:

- `active`
- `disabling`
- `enabling`
- `error`
- `modifying`

## LogFormat

```python
from mypy_boto3_elasticache.literals import LogFormat
```

Values:

- `json`
- `text`

## LogType

```python
from mypy_boto3_elasticache.literals import LogType
```

Values:

- `slow-log`

## MultiAZStatus

```python
from mypy_boto3_elasticache.literals import MultiAZStatus
```

Values:

- `disabled`
- `enabled`

## NodeUpdateInitiatedBy

```python
from mypy_boto3_elasticache.literals import NodeUpdateInitiatedBy
```

Values:

- `customer`
- `system`

## NodeUpdateStatus

```python
from mypy_boto3_elasticache.literals import NodeUpdateStatus
```

Values:

- `complete`
- `in-progress`
- `not-applied`
- `stopped`
- `stopping`
- `waiting-to-start`

## OutpostMode

```python
from mypy_boto3_elasticache.literals import OutpostMode
```

Values:

- `cross-outpost`
- `single-outpost`

## PendingAutomaticFailoverStatus

```python
from mypy_boto3_elasticache.literals import PendingAutomaticFailoverStatus
```

Values:

- `disabled`
- `enabled`

## ReplicationGroupAvailableWaiterName

```python
from mypy_boto3_elasticache.literals import ReplicationGroupAvailableWaiterName
```

Values:

- `replication_group_available`

## ReplicationGroupDeletedWaiterName

```python
from mypy_boto3_elasticache.literals import ReplicationGroupDeletedWaiterName
```

Values:

- `replication_group_deleted`

## ServiceUpdateSeverity

```python
from mypy_boto3_elasticache.literals import ServiceUpdateSeverity
```

Values:

- `critical`
- `important`
- `low`
- `medium`

## ServiceUpdateStatus

```python
from mypy_boto3_elasticache.literals import ServiceUpdateStatus
```

Values:

- `available`
- `cancelled`
- `expired`

## ServiceUpdateType

```python
from mypy_boto3_elasticache.literals import ServiceUpdateType
```

Values:

- `security-update`

## SlaMet

```python
from mypy_boto3_elasticache.literals import SlaMet
```

Values:

- `n/a`
- `no`
- `yes`

## SourceType

```python
from mypy_boto3_elasticache.literals import SourceType
```

Values:

- `cache-cluster`
- `cache-parameter-group`
- `cache-security-group`
- `cache-subnet-group`
- `replication-group`
- `user`
- `user-group`

## UpdateActionStatus

```python
from mypy_boto3_elasticache.literals import UpdateActionStatus
```

Values:

- `complete`
- `in-progress`
- `not-applicable`
- `not-applied`
- `scheduled`
- `scheduling`
- `stopped`
- `stopping`
- `waiting-to-start`
