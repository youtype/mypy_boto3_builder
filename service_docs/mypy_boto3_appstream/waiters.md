# Waiters for boto3 AppStream module

> [Index](../index.md) > [AppStream](./index.md) > Waiters

Auto-generated documentation for [AppStream](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream)
type annotations stubs module [mypy_boto3_appstream](https://pypi.org/project/mypy-boto3-appstream/).

- [Waiters for boto3 AppStream module](#waiters-for-boto3-appstream-module)
  - [FleetStartedWaiter](#fleetstartedwaiter)
  - [FleetStoppedWaiter](#fleetstoppedwaiter)

## FleetStartedWaiter

Type annotations for `boto3.client("appstream").get_waiter("fleet_started")`.

Can be used directly:

```python
from mypy_boto3_appstream.waiters import FleetStartedWaiter

def get_fleet_started_waiter() -> FleetStartedWaiter:
    return boto3.client("appstream").get_waiter("fleet_started")
```

[Waiter.FleetStarted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Waiter.FleetStarted)

```python
class FleetStartedWaiter(Boto3Waiter):
    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## FleetStoppedWaiter

Type annotations for `boto3.client("appstream").get_waiter("fleet_stopped")`.

Can be used directly:

```python
from mypy_boto3_appstream.waiters import FleetStoppedWaiter

def get_fleet_stopped_waiter() -> FleetStoppedWaiter:
    return boto3.client("appstream").get_waiter("fleet_stopped")
```

[Waiter.FleetStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Waiter.FleetStopped)

```python
class FleetStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        Names: List[str] = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```