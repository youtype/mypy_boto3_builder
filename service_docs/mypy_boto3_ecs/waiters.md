# Waiters for boto3 ECS module

> [Index](../index.md) > [ECS](./index.md) > Waiters

Auto-generated documentation for [ECS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS)
type annotations stubs module [mypy_boto3_ecs](https://pypi.org/project/mypy-boto3-ecs/).

- [Waiters for boto3 ECS module](#waiters-for-boto3-ecs-module)
  - [ServicesInactiveWaiter](#servicesinactivewaiter)
  - [ServicesStableWaiter](#servicesstablewaiter)
  - [TasksRunningWaiter](#tasksrunningwaiter)
  - [TasksStoppedWaiter](#tasksstoppedwaiter)

## ServicesInactiveWaiter

Type annotations for `boto3.client("ecs").get_waiter("services_inactive")`.

Can be used directly:

```python
from mypy_boto3_ecs.waiters import ServicesInactiveWaiter

def get_services_inactive_waiter() -> ServicesInactiveWaiter:
    return boto3.client("ecs").get_waiter("services_inactive")
```

[Waiter.ServicesInactive documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.ServicesInactive)

```python
class ServicesInactiveWaiter(Boto3Waiter):
    def wait(
        self,
        services: List[str],
        cluster: str = None,
        include: List[Literal['TAGS']] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ServicesStableWaiter

Type annotations for `boto3.client("ecs").get_waiter("services_stable")`.

Can be used directly:

```python
from mypy_boto3_ecs.waiters import ServicesStableWaiter

def get_services_stable_waiter() -> ServicesStableWaiter:
    return boto3.client("ecs").get_waiter("services_stable")
```

[Waiter.ServicesStable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.ServicesStable)

```python
class ServicesStableWaiter(Boto3Waiter):
    def wait(
        self,
        services: List[str],
        cluster: str = None,
        include: List[Literal['TAGS']] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## TasksRunningWaiter

Type annotations for `boto3.client("ecs").get_waiter("tasks_running")`.

Can be used directly:

```python
from mypy_boto3_ecs.waiters import TasksRunningWaiter

def get_tasks_running_waiter() -> TasksRunningWaiter:
    return boto3.client("ecs").get_waiter("tasks_running")
```

[Waiter.TasksRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.TasksRunning)

```python
class TasksRunningWaiter(Boto3Waiter):
    def wait(
        self,
        tasks: List[str],
        cluster: str = None,
        include: List[Literal['TAGS']] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## TasksStoppedWaiter

Type annotations for `boto3.client("ecs").get_waiter("tasks_stopped")`.

Can be used directly:

```python
from mypy_boto3_ecs.waiters import TasksStoppedWaiter

def get_tasks_stopped_waiter() -> TasksStoppedWaiter:
    return boto3.client("ecs").get_waiter("tasks_stopped")
```

[Waiter.TasksStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Waiter.TasksStopped)

```python
class TasksStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        tasks: List[str],
        cluster: str = None,
        include: List[Literal['TAGS']] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```