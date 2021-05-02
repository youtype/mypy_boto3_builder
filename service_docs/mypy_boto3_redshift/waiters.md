# Waiters for boto3 Redshift module

> [Index](../index.md) > [Redshift](./index.md) > Waiters

Auto-generated documentation for [Redshift](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift)
type annotations stubs module [mypy_boto3_redshift](https://pypi.org/project/mypy-boto3-redshift/).

- [Waiters for boto3 Redshift module](#waiters-for-boto3-redshift-module)
  - [ClusterAvailableWaiter](#clusteravailablewaiter)
  - [ClusterDeletedWaiter](#clusterdeletedwaiter)
  - [ClusterRestoredWaiter](#clusterrestoredwaiter)
  - [SnapshotAvailableWaiter](#snapshotavailablewaiter)

## ClusterAvailableWaiter

Type annotations for `boto3.client("redshift").get_waiter("cluster_available")`.

Can be used directly:

```python
from mypy_boto3_redshift.waiters import ClusterAvailableWaiter

def get_cluster_available_waiter() -> ClusterAvailableWaiter:
    return boto3.client("redshift").get_waiter("cluster_available")
```

[Waiter.ClusterAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.ClusterAvailable)

```python
class ClusterAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ClusterDeletedWaiter

Type annotations for `boto3.client("redshift").get_waiter("cluster_deleted")`.

Can be used directly:

```python
from mypy_boto3_redshift.waiters import ClusterDeletedWaiter

def get_cluster_deleted_waiter() -> ClusterDeletedWaiter:
    return boto3.client("redshift").get_waiter("cluster_deleted")
```

[Waiter.ClusterDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.ClusterDeleted)

```python
class ClusterDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ClusterRestoredWaiter

Type annotations for `boto3.client("redshift").get_waiter("cluster_restored")`.

Can be used directly:

```python
from mypy_boto3_redshift.waiters import ClusterRestoredWaiter

def get_cluster_restored_waiter() -> ClusterRestoredWaiter:
    return boto3.client("redshift").get_waiter("cluster_restored")
```

[Waiter.ClusterRestored documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.ClusterRestored)

```python
class ClusterRestoredWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterIdentifier: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## SnapshotAvailableWaiter

Type annotations for `boto3.client("redshift").get_waiter("snapshot_available")`.

Can be used directly:

```python
from mypy_boto3_redshift.waiters import SnapshotAvailableWaiter

def get_snapshot_available_waiter() -> SnapshotAvailableWaiter:
    return boto3.client("redshift").get_waiter("snapshot_available")
```

[Waiter.SnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Waiter.SnapshotAvailable)

```python
class SnapshotAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterIdentifier: str = None,
        SnapshotIdentifier: str = None,
        SnapshotType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        Marker: str = None,
        OwnerAccount: str = None,
        TagKeys: List[str] = None,
        TagValues: List[str] = None,
        ClusterExists: bool = None,
        SortingEntities: List[SnapshotSortingEntityTypeDef] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```