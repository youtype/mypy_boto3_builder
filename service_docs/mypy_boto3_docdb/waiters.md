# Waiters for boto3 DocDB module

> [Index](../index.md) > [DocDB](./index.md) > Waiters

Auto-generated documentation for [DocDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB)
type annotations stubs module [mypy_boto3_docdb](https://pypi.org/project/mypy-boto3-docdb/).

- [Waiters for boto3 DocDB module](#waiters-for-boto3-docdb-module)
  - [DBInstanceAvailableWaiter](#dbinstanceavailablewaiter)
  - [DBInstanceDeletedWaiter](#dbinstancedeletedwaiter)

## DBInstanceAvailableWaiter

Type annotations for `boto3.client("docdb").get_waiter("db_instance_available")`.

Can be used directly:

```python
from mypy_boto3_docdb.waiters import DBInstanceAvailableWaiter

def get_db_instance_available_waiter() -> DBInstanceAvailableWaiter:
    return boto3.client("docdb").get_waiter("db_instance_available")
```

[Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)

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

Type annotations for `boto3.client("docdb").get_waiter("db_instance_deleted")`.

Can be used directly:

```python
from mypy_boto3_docdb.waiters import DBInstanceDeletedWaiter

def get_db_instance_deleted_waiter() -> DBInstanceDeletedWaiter:
    return boto3.client("docdb").get_waiter("db_instance_deleted")
```

[Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)

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