# Waiters for boto3 EMR module

> [Index](../index.md) > [EMR](./index.md) > Waiters

Auto-generated documentation for [EMR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR)
type annotations stubs module [mypy_boto3_emr](https://pypi.org/project/mypy-boto3-emr/).

- [Waiters for boto3 EMR module](#waiters-for-boto3-emr-module)
  - [ClusterRunningWaiter](#clusterrunningwaiter)
  - [ClusterTerminatedWaiter](#clusterterminatedwaiter)
  - [StepCompleteWaiter](#stepcompletewaiter)

## ClusterRunningWaiter

Type annotations for `boto3.client("emr").get_waiter("cluster_running")`.

Can be used directly:

```python
from mypy_boto3_emr.waiters import ClusterRunningWaiter

def get_cluster_running_waiter() -> ClusterRunningWaiter:
    return boto3.client("emr").get_waiter("cluster_running")
```

[Waiter.ClusterRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Waiter.ClusterRunning)

```python
class ClusterRunningWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ClusterTerminatedWaiter

Type annotations for `boto3.client("emr").get_waiter("cluster_terminated")`.

Can be used directly:

```python
from mypy_boto3_emr.waiters import ClusterTerminatedWaiter

def get_cluster_terminated_waiter() -> ClusterTerminatedWaiter:
    return boto3.client("emr").get_waiter("cluster_terminated")
```

[Waiter.ClusterTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Waiter.ClusterTerminated)

```python
class ClusterTerminatedWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## StepCompleteWaiter

Type annotations for `boto3.client("emr").get_waiter("step_complete")`.

Can be used directly:

```python
from mypy_boto3_emr.waiters import StepCompleteWaiter

def get_step_complete_waiter() -> StepCompleteWaiter:
    return boto3.client("emr").get_waiter("step_complete")
```

[Waiter.StepComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Waiter.StepComplete)

```python
class StepCompleteWaiter(Boto3Waiter):
    def wait(
        self,
        ClusterId: str,
        StepId: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```