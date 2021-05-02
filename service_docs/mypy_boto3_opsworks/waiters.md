# Waiters for boto3 OpsWorks module

> [Index](../index.md) > [OpsWorks](./index.md) > Waiters

Auto-generated documentation for [OpsWorks](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks)
type annotations stubs module [mypy_boto3_opsworks](https://pypi.org/project/mypy-boto3-opsworks/).

- [Waiters for boto3 OpsWorks module](#waiters-for-boto3-opsworks-module)
  - [AppExistsWaiter](#appexistswaiter)
  - [DeploymentSuccessfulWaiter](#deploymentsuccessfulwaiter)
  - [InstanceOnlineWaiter](#instanceonlinewaiter)
  - [InstanceRegisteredWaiter](#instanceregisteredwaiter)
  - [InstanceStoppedWaiter](#instancestoppedwaiter)
  - [InstanceTerminatedWaiter](#instanceterminatedwaiter)

## AppExistsWaiter

Type annotations for `boto3.client("opsworks").get_waiter("app_exists")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import AppExistsWaiter

def get_app_exists_waiter() -> AppExistsWaiter:
    return boto3.client("opsworks").get_waiter("app_exists")
```

[Waiter.AppExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.AppExists)

```python
class AppExistsWaiter(Boto3Waiter):
    def wait(
        self,
        StackId: str = None,
        AppIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DeploymentSuccessfulWaiter

Type annotations for `boto3.client("opsworks").get_waiter("deployment_successful")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import DeploymentSuccessfulWaiter

def get_deployment_successful_waiter() -> DeploymentSuccessfulWaiter:
    return boto3.client("opsworks").get_waiter("deployment_successful")
```

[Waiter.DeploymentSuccessful documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessful)

```python
class DeploymentSuccessfulWaiter(Boto3Waiter):
    def wait(
        self,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InstanceOnlineWaiter

Type annotations for `boto3.client("opsworks").get_waiter("instance_online")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import InstanceOnlineWaiter

def get_instance_online_waiter() -> InstanceOnlineWaiter:
    return boto3.client("opsworks").get_waiter("instance_online")
```

[Waiter.InstanceOnline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnline)

```python
class InstanceOnlineWaiter(Boto3Waiter):
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InstanceRegisteredWaiter

Type annotations for `boto3.client("opsworks").get_waiter("instance_registered")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import InstanceRegisteredWaiter

def get_instance_registered_waiter() -> InstanceRegisteredWaiter:
    return boto3.client("opsworks").get_waiter("instance_registered")
```

[Waiter.InstanceRegistered documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegistered)

```python
class InstanceRegisteredWaiter(Boto3Waiter):
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InstanceStoppedWaiter

Type annotations for `boto3.client("opsworks").get_waiter("instance_stopped")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import InstanceStoppedWaiter

def get_instance_stopped_waiter() -> InstanceStoppedWaiter:
    return boto3.client("opsworks").get_waiter("instance_stopped")
```

[Waiter.InstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStopped)

```python
class InstanceStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## InstanceTerminatedWaiter

Type annotations for `boto3.client("opsworks").get_waiter("instance_terminated")`.

Can be used directly:

```python
from mypy_boto3_opsworks.waiters import InstanceTerminatedWaiter

def get_instance_terminated_waiter() -> InstanceTerminatedWaiter:
    return boto3.client("opsworks").get_waiter("instance_terminated")
```

[Waiter.InstanceTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminated)

```python
class InstanceTerminatedWaiter(Boto3Waiter):
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```