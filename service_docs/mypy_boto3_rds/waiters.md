# Waiters for boto3 RDS module

> [Index](../index.md) > [RDS](./index.md) > Waiters

Auto-generated documentation for [RDS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS)
type annotations stubs module [mypy_boto3_rds](https://pypi.org/project/mypy-boto3-rds/).

- [Waiters for boto3 RDS module](#waiters-for-boto3-rds-module)
  - [DBClusterSnapshotAvailableWaiter](#dbclustersnapshotavailablewaiter)
  - [DBClusterSnapshotDeletedWaiter](#dbclustersnapshotdeletedwaiter)
  - [DBInstanceAvailableWaiter](#dbinstanceavailablewaiter)
  - [DBInstanceDeletedWaiter](#dbinstancedeletedwaiter)
  - [DBSnapshotAvailableWaiter](#dbsnapshotavailablewaiter)
  - [DBSnapshotCompletedWaiter](#dbsnapshotcompletedwaiter)
  - [DBSnapshotDeletedWaiter](#dbsnapshotdeletedwaiter)

## DBClusterSnapshotAvailableWaiter

Type annotations for `boto3.client("rds").get_waiter("db_cluster_snapshot_available")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBClusterSnapshotAvailableWaiter

def get_db_cluster_snapshot_available_waiter() -> DBClusterSnapshotAvailableWaiter:
    return boto3.client("rds").get_waiter("db_cluster_snapshot_available")
```

[Waiter.DBClusterSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotAvailable)

```python
class DBClusterSnapshotAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DBClusterSnapshotDeletedWaiter

Type annotations for `boto3.client("rds").get_waiter("db_cluster_snapshot_deleted")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBClusterSnapshotDeletedWaiter

def get_db_cluster_snapshot_deleted_waiter() -> DBClusterSnapshotDeletedWaiter:
    return boto3.client("rds").get_waiter("db_cluster_snapshot_deleted")
```

[Waiter.DBClusterSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotDeleted)

```python
class DBClusterSnapshotDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DBInstanceAvailableWaiter

Type annotations for `boto3.client("rds").get_waiter("db_instance_available")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBInstanceAvailableWaiter

def get_db_instance_available_waiter() -> DBInstanceAvailableWaiter:
    return boto3.client("rds").get_waiter("db_instance_available")
```

[Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBInstanceAvailable)

```python
class DBInstanceAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DBInstanceDeletedWaiter

Type annotations for `boto3.client("rds").get_waiter("db_instance_deleted")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBInstanceDeletedWaiter

def get_db_instance_deleted_waiter() -> DBInstanceDeletedWaiter:
    return boto3.client("rds").get_waiter("db_instance_deleted")
```

[Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBInstanceDeleted)

```python
class DBInstanceDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DBSnapshotAvailableWaiter

Type annotations for `boto3.client("rds").get_waiter("db_snapshot_available")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBSnapshotAvailableWaiter

def get_db_snapshot_available_waiter() -> DBSnapshotAvailableWaiter:
    return boto3.client("rds").get_waiter("db_snapshot_available")
```

[Waiter.DBSnapshotAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBSnapshotAvailable)

```python
class DBSnapshotAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DBSnapshotCompletedWaiter

Type annotations for `boto3.client("rds").get_waiter("db_snapshot_completed")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBSnapshotCompletedWaiter

def get_db_snapshot_completed_waiter() -> DBSnapshotCompletedWaiter:
    return boto3.client("rds").get_waiter("db_snapshot_completed")
```

[Waiter.DBSnapshotCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBSnapshotCompleted)

```python
class DBSnapshotCompletedWaiter(Boto3Waiter):
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DBSnapshotDeletedWaiter

Type annotations for `boto3.client("rds").get_waiter("db_snapshot_deleted")`.

Can be used directly:

```python
from mypy_boto3_rds.waiters import DBSnapshotDeletedWaiter

def get_db_snapshot_deleted_waiter() -> DBSnapshotDeletedWaiter:
    return boto3.client("rds").get_waiter("db_snapshot_deleted")
```

[Waiter.DBSnapshotDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Waiter.DBSnapshotDeleted)

```python
class DBSnapshotDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```