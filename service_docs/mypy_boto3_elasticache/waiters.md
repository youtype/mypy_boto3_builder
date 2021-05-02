# Waiters for boto3 ElastiCache module

> [Index](../index.md) > [ElastiCache](./index.md) > Waiters

Auto-generated documentation for [ElastiCache](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache)
type annotations stubs module [mypy_boto3_elasticache](https://pypi.org/project/mypy-boto3-elasticache/).

- [Waiters for boto3 ElastiCache module](#waiters-for-boto3-elasticache-module)
  - [CacheClusterAvailableWaiter](#cacheclusteravailablewaiter)
  - [CacheClusterDeletedWaiter](#cacheclusterdeletedwaiter)
  - [ReplicationGroupAvailableWaiter](#replicationgroupavailablewaiter)
  - [ReplicationGroupDeletedWaiter](#replicationgroupdeletedwaiter)

## CacheClusterAvailableWaiter

Type annotations for `boto3.client("elasticache").get_waiter("cache_cluster_available")`.

Can be used directly:

```python
from mypy_boto3_elasticache.waiters import CacheClusterAvailableWaiter

def get_cache_cluster_available_waiter() -> CacheClusterAvailableWaiter:
    return boto3.client("elasticache").get_waiter("cache_cluster_available")
```

[Waiter.CacheClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterAvailable)

```python
class CacheClusterAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## CacheClusterDeletedWaiter

Type annotations for `boto3.client("elasticache").get_waiter("cache_cluster_deleted")`.

Can be used directly:

```python
from mypy_boto3_elasticache.waiters import CacheClusterDeletedWaiter

def get_cache_cluster_deleted_waiter() -> CacheClusterDeletedWaiter:
    return boto3.client("elasticache").get_waiter("cache_cluster_deleted")
```

[Waiter.CacheClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Waiter.CacheClusterDeleted)

```python
class CacheClusterDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationGroupAvailableWaiter

Type annotations for `boto3.client("elasticache").get_waiter("replication_group_available")`.

Can be used directly:

```python
from mypy_boto3_elasticache.waiters import ReplicationGroupAvailableWaiter

def get_replication_group_available_waiter() -> ReplicationGroupAvailableWaiter:
    return boto3.client("elasticache").get_waiter("replication_group_available")
```

[Waiter.ReplicationGroupAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupAvailable)

```python
class ReplicationGroupAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationGroupDeletedWaiter

Type annotations for `boto3.client("elasticache").get_waiter("replication_group_deleted")`.

Can be used directly:

```python
from mypy_boto3_elasticache.waiters import ReplicationGroupDeletedWaiter

def get_replication_group_deleted_waiter() -> ReplicationGroupDeletedWaiter:
    return boto3.client("elasticache").get_waiter("replication_group_deleted")
```

[Waiter.ReplicationGroupDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Waiter.ReplicationGroupDeleted)

```python
class ReplicationGroupDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```