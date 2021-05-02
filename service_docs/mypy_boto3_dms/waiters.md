# Waiters for boto3 DatabaseMigrationService module

> [Index](../index.md) > [DatabaseMigrationService](./index.md) > Waiters

Auto-generated documentation for [DatabaseMigrationService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService)
type annotations stubs module [mypy_boto3_dms](https://pypi.org/project/mypy-boto3-dms/).

- [Waiters for boto3 DatabaseMigrationService module](#waiters-for-boto3-databasemigrationservice-module)
  - [EndpointDeletedWaiter](#endpointdeletedwaiter)
  - [ReplicationInstanceAvailableWaiter](#replicationinstanceavailablewaiter)
  - [ReplicationInstanceDeletedWaiter](#replicationinstancedeletedwaiter)
  - [ReplicationTaskDeletedWaiter](#replicationtaskdeletedwaiter)
  - [ReplicationTaskReadyWaiter](#replicationtaskreadywaiter)
  - [ReplicationTaskRunningWaiter](#replicationtaskrunningwaiter)
  - [ReplicationTaskStoppedWaiter](#replicationtaskstoppedwaiter)
  - [TestConnectionSucceedsWaiter](#testconnectionsucceedswaiter)

## EndpointDeletedWaiter

Type annotations for `boto3.client("dms").get_waiter("endpoint_deleted")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import EndpointDeletedWaiter

def get_endpoint_deleted_waiter() -> EndpointDeletedWaiter:
    return boto3.client("dms").get_waiter("endpoint_deleted")
```

[Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)

```python
class EndpointDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationInstanceAvailableWaiter

Type annotations for `boto3.client("dms").get_waiter("replication_instance_available")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import ReplicationInstanceAvailableWaiter

def get_replication_instance_available_waiter() -> ReplicationInstanceAvailableWaiter:
    return boto3.client("dms").get_waiter("replication_instance_available")
```

[Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)

```python
class ReplicationInstanceAvailableWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationInstanceDeletedWaiter

Type annotations for `boto3.client("dms").get_waiter("replication_instance_deleted")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import ReplicationInstanceDeletedWaiter

def get_replication_instance_deleted_waiter() -> ReplicationInstanceDeletedWaiter:
    return boto3.client("dms").get_waiter("replication_instance_deleted")
```

[Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)

```python
class ReplicationInstanceDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationTaskDeletedWaiter

Type annotations for `boto3.client("dms").get_waiter("replication_task_deleted")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import ReplicationTaskDeletedWaiter

def get_replication_task_deleted_waiter() -> ReplicationTaskDeletedWaiter:
    return boto3.client("dms").get_waiter("replication_task_deleted")
```

[Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)

```python
class ReplicationTaskDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationTaskReadyWaiter

Type annotations for `boto3.client("dms").get_waiter("replication_task_ready")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import ReplicationTaskReadyWaiter

def get_replication_task_ready_waiter() -> ReplicationTaskReadyWaiter:
    return boto3.client("dms").get_waiter("replication_task_ready")
```

[Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)

```python
class ReplicationTaskReadyWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationTaskRunningWaiter

Type annotations for `boto3.client("dms").get_waiter("replication_task_running")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import ReplicationTaskRunningWaiter

def get_replication_task_running_waiter() -> ReplicationTaskRunningWaiter:
    return boto3.client("dms").get_waiter("replication_task_running")
```

[Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)

```python
class ReplicationTaskRunningWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ReplicationTaskStoppedWaiter

Type annotations for `boto3.client("dms").get_waiter("replication_task_stopped")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import ReplicationTaskStoppedWaiter

def get_replication_task_stopped_waiter() -> ReplicationTaskStoppedWaiter:
    return boto3.client("dms").get_waiter("replication_task_stopped")
```

[Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)

```python
class ReplicationTaskStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## TestConnectionSucceedsWaiter

Type annotations for `boto3.client("dms").get_waiter("test_connection_succeeds")`.

Can be used directly:

```python
from mypy_boto3_dms.waiters import TestConnectionSucceedsWaiter

def get_test_connection_succeeds_waiter() -> TestConnectionSucceedsWaiter:
    return boto3.client("dms").get_waiter("test_connection_succeeds")
```

[Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)

```python
class TestConnectionSucceedsWaiter(Boto3Waiter):
    def wait(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```