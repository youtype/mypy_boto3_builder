# Paginators for boto3 ElastiCache module

> [Index](../index.md) > [ElastiCache](./index.md) > Paginators

Auto-generated documentation for [ElastiCache](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache)
type annotations stubs module [mypy_boto3_elasticache](https://pypi.org/project/mypy-boto3-elasticache/).

- [Paginators for boto3 ElastiCache module](#paginators-for-boto3-elasticache-module)
  - [DescribeCacheClustersPaginator](#describecacheclusterspaginator)
  - [DescribeCacheEngineVersionsPaginator](#describecacheengineversionspaginator)
  - [DescribeCacheParameterGroupsPaginator](#describecacheparametergroupspaginator)
  - [DescribeCacheParametersPaginator](#describecacheparameterspaginator)
  - [DescribeCacheSecurityGroupsPaginator](#describecachesecuritygroupspaginator)
  - [DescribeCacheSubnetGroupsPaginator](#describecachesubnetgroupspaginator)
  - [DescribeEngineDefaultParametersPaginator](#describeenginedefaultparameterspaginator)
  - [DescribeEventsPaginator](#describeeventspaginator)
  - [DescribeGlobalReplicationGroupsPaginator](#describeglobalreplicationgroupspaginator)
  - [DescribeReplicationGroupsPaginator](#describereplicationgroupspaginator)
  - [DescribeReservedCacheNodesPaginator](#describereservedcachenodespaginator)
  - [DescribeReservedCacheNodesOfferingsPaginator](#describereservedcachenodesofferingspaginator)
  - [DescribeServiceUpdatesPaginator](#describeserviceupdatespaginator)
  - [DescribeSnapshotsPaginator](#describesnapshotspaginator)
  - [DescribeUpdateActionsPaginator](#describeupdateactionspaginator)
  - [DescribeUserGroupsPaginator](#describeusergroupspaginator)
  - [DescribeUsersPaginator](#describeuserspaginator)

## DescribeCacheClustersPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_cache_clusters")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheClustersPaginator

def get_describe_cache_clusters_paginator() -> DescribeCacheClustersPaginator:
    return boto3.client("elasticache").get_paginator("describe_cache_clusters")
```

[Paginator.DescribeCacheClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheClusters)

```python
class DescribeCacheClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        CacheClusterId: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheClusterMessageTypeDef]:
        pass
```
## DescribeCacheEngineVersionsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_cache_engine_versions")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheEngineVersionsPaginator

def get_describe_cache_engine_versions_paginator() -> DescribeCacheEngineVersionsPaginator:
    return boto3.client("elasticache").get_paginator("describe_cache_engine_versions")
```

[Paginator.DescribeCacheEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheEngineVersions)

```python
class DescribeCacheEngineVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        CacheParameterGroupFamily: str = None,
        DefaultOnly: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheEngineVersionMessageTypeDef]:
        pass
```
## DescribeCacheParameterGroupsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_cache_parameter_groups")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheParameterGroupsPaginator

def get_describe_cache_parameter_groups_paginator() -> DescribeCacheParameterGroupsPaginator:
    return boto3.client("elasticache").get_paginator("describe_cache_parameter_groups")
```

[Paginator.DescribeCacheParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameterGroups)

```python
class DescribeCacheParameterGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        CacheParameterGroupName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheParameterGroupsMessageTypeDef]:
        pass
```
## DescribeCacheParametersPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_cache_parameters")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheParametersPaginator

def get_describe_cache_parameters_paginator() -> DescribeCacheParametersPaginator:
    return boto3.client("elasticache").get_paginator("describe_cache_parameters")
```

[Paginator.DescribeCacheParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheParameters)

```python
class DescribeCacheParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        CacheParameterGroupName: str,
        Source: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheParameterGroupDetailsTypeDef]:
        pass
```
## DescribeCacheSecurityGroupsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_cache_security_groups")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheSecurityGroupsPaginator

def get_describe_cache_security_groups_paginator() -> DescribeCacheSecurityGroupsPaginator:
    return boto3.client("elasticache").get_paginator("describe_cache_security_groups")
```

[Paginator.DescribeCacheSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSecurityGroups)

```python
class DescribeCacheSecurityGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        CacheSecurityGroupName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheSecurityGroupMessageTypeDef]:
        pass
```
## DescribeCacheSubnetGroupsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_cache_subnet_groups")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeCacheSubnetGroupsPaginator

def get_describe_cache_subnet_groups_paginator() -> DescribeCacheSubnetGroupsPaginator:
    return boto3.client("elasticache").get_paginator("describe_cache_subnet_groups")
```

[Paginator.DescribeCacheSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeCacheSubnetGroups)

```python
class DescribeCacheSubnetGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        CacheSubnetGroupName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[CacheSubnetGroupMessageTypeDef]:
        pass
```
## DescribeEngineDefaultParametersPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_engine_default_parameters")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeEngineDefaultParametersPaginator

def get_describe_engine_default_parameters_paginator() -> DescribeEngineDefaultParametersPaginator:
    return boto3.client("elasticache").get_paginator("describe_engine_default_parameters")
```

[Paginator.DescribeEngineDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEngineDefaultParameters)

```python
class DescribeEngineDefaultParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        CacheParameterGroupFamily: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEngineDefaultParametersResultTypeDef]:
        pass
```
## DescribeEventsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_events")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeEventsPaginator

def get_describe_events_paginator() -> DescribeEventsPaginator:
    return boto3.client("elasticache").get_paginator("describe_events")
```

[Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeEvents)

```python
class DescribeEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: SourceType = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[EventsMessageTypeDef]:
        pass
```
## DescribeGlobalReplicationGroupsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_global_replication_groups")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeGlobalReplicationGroupsPaginator

def get_describe_global_replication_groups_paginator() -> DescribeGlobalReplicationGroupsPaginator:
    return boto3.client("elasticache").get_paginator("describe_global_replication_groups")
```

[Paginator.DescribeGlobalReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeGlobalReplicationGroups)

```python
class DescribeGlobalReplicationGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        GlobalReplicationGroupId: str = None,
        ShowMemberInfo: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGlobalReplicationGroupsResultTypeDef]:
        pass
```
## DescribeReplicationGroupsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_replication_groups")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeReplicationGroupsPaginator

def get_describe_replication_groups_paginator() -> DescribeReplicationGroupsPaginator:
    return boto3.client("elasticache").get_paginator("describe_replication_groups")
```

[Paginator.DescribeReplicationGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReplicationGroups)

```python
class DescribeReplicationGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReplicationGroupId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReplicationGroupMessageTypeDef]:
        pass
```
## DescribeReservedCacheNodesPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_reserved_cache_nodes")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeReservedCacheNodesPaginator

def get_describe_reserved_cache_nodes_paginator() -> DescribeReservedCacheNodesPaginator:
    return boto3.client("elasticache").get_paginator("describe_reserved_cache_nodes")
```

[Paginator.DescribeReservedCacheNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodes)

```python
class DescribeReservedCacheNodesPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedCacheNodeId: str = None,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedCacheNodeMessageTypeDef]:
        pass
```
## DescribeReservedCacheNodesOfferingsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_reserved_cache_nodes_offerings")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeReservedCacheNodesOfferingsPaginator

def get_describe_reserved_cache_nodes_offerings_paginator() -> DescribeReservedCacheNodesOfferingsPaginator:
    return boto3.client("elasticache").get_paginator("describe_reserved_cache_nodes_offerings")
```

[Paginator.DescribeReservedCacheNodesOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeReservedCacheNodesOfferings)

```python
class DescribeReservedCacheNodesOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedCacheNodesOfferingId: str = None,
        CacheNodeType: str = None,
        Duration: str = None,
        ProductDescription: str = None,
        OfferingType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ReservedCacheNodesOfferingMessageTypeDef]:
        pass
```
## DescribeServiceUpdatesPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_service_updates")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeServiceUpdatesPaginator

def get_describe_service_updates_paginator() -> DescribeServiceUpdatesPaginator:
    return boto3.client("elasticache").get_paginator("describe_service_updates")
```

[Paginator.DescribeServiceUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeServiceUpdates)

```python
class DescribeServiceUpdatesPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ServiceUpdateStatus: List[ServiceUpdateStatus] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ServiceUpdatesMessageTypeDef]:
        pass
```
## DescribeSnapshotsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_snapshots")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeSnapshotsPaginator

def get_describe_snapshots_paginator() -> DescribeSnapshotsPaginator:
    return boto3.client("elasticache").get_paginator("describe_snapshots")
```

[Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeSnapshots)

```python
class DescribeSnapshotsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReplicationGroupId: str = None,
        CacheClusterId: str = None,
        SnapshotName: str = None,
        SnapshotSource: str = None,
        ShowNodeGroupConfig: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotsListMessageTypeDef]:
        pass
```
## DescribeUpdateActionsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_update_actions")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeUpdateActionsPaginator

def get_describe_update_actions_paginator() -> DescribeUpdateActionsPaginator:
    return boto3.client("elasticache").get_paginator("describe_update_actions")
```

[Paginator.DescribeUpdateActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUpdateActions)

```python
class DescribeUpdateActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ServiceUpdateName: str = None,
        ReplicationGroupIds: List[str] = None,
        CacheClusterIds: List[str] = None,
        Engine: str = None,
        ServiceUpdateStatus: List[ServiceUpdateStatus] = None,
        ServiceUpdateTimeRange: TimeRangeFilterTypeDef = None,
        UpdateActionStatus: List[UpdateActionStatus] = None,
        ShowNodeLevelUpdateStatus: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[UpdateActionsMessageTypeDef]:
        pass
```
## DescribeUserGroupsPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_user_groups")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeUserGroupsPaginator

def get_describe_user_groups_paginator() -> DescribeUserGroupsPaginator:
    return boto3.client("elasticache").get_paginator("describe_user_groups")
```

[Paginator.DescribeUserGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUserGroups)

```python
class DescribeUserGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        UserGroupId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUserGroupsResultTypeDef]:
        pass
```
## DescribeUsersPaginator

Type annotations for `boto3.client("elasticache").get_paginator("describe_users")`.

Can be used directly:

```python
from mypy_boto3_elasticache.paginators import DescribeUsersPaginator

def get_describe_users_paginator() -> DescribeUsersPaginator:
    return boto3.client("elasticache").get_paginator("describe_users")
```

[Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Paginator.DescribeUsers)

```python
class DescribeUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        Engine: str = None,
        UserId: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUsersResultTypeDef]:
        pass
```