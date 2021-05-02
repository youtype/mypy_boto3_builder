# Waiters for boto3 CloudWatch module

> [Index](../index.md) > [CloudWatch](./index.md) > Waiters

Auto-generated documentation for [CloudWatch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch)
type annotations stubs module [mypy_boto3_cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/).

- [Waiters for boto3 CloudWatch module](#waiters-for-boto3-cloudwatch-module)
  - [AlarmExistsWaiter](#alarmexistswaiter)
  - [CompositeAlarmExistsWaiter](#compositealarmexistswaiter)

## AlarmExistsWaiter

Type annotations for `boto3.client("cloudwatch").get_waiter("alarm_exists")`.

Can be used directly:

```python
from mypy_boto3_cloudwatch.waiters import AlarmExistsWaiter

def get_alarm_exists_waiter() -> AlarmExistsWaiter:
    return boto3.client("cloudwatch").get_waiter("alarm_exists")
```

[Waiter.AlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Waiter.AlarmExists)

```python
class AlarmExistsWaiter(Boto3Waiter):
    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValue = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## CompositeAlarmExistsWaiter

Type annotations for `boto3.client("cloudwatch").get_waiter("composite_alarm_exists")`.

Can be used directly:

```python
from mypy_boto3_cloudwatch.waiters import CompositeAlarmExistsWaiter

def get_composite_alarm_exists_waiter() -> CompositeAlarmExistsWaiter:
    return boto3.client("cloudwatch").get_waiter("composite_alarm_exists")
```

[Waiter.CompositeAlarmExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Waiter.CompositeAlarmExists)

```python
class CompositeAlarmExistsWaiter(Boto3Waiter):
    def wait(
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValue = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```