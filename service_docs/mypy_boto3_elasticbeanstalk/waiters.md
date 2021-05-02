# Waiters for boto3 ElasticBeanstalk module

> [Index](../index.md) > [ElasticBeanstalk](./index.md) > Waiters

Auto-generated documentation for [ElasticBeanstalk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk)
type annotations stubs module [mypy_boto3_elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/).

- [Waiters for boto3 ElasticBeanstalk module](#waiters-for-boto3-elasticbeanstalk-module)
  - [EnvironmentExistsWaiter](#environmentexistswaiter)
  - [EnvironmentTerminatedWaiter](#environmentterminatedwaiter)
  - [EnvironmentUpdatedWaiter](#environmentupdatedwaiter)

## EnvironmentExistsWaiter

Type annotations for `boto3.client("elasticbeanstalk").get_waiter("environment_exists")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.waiters import EnvironmentExistsWaiter

def get_environment_exists_waiter() -> EnvironmentExistsWaiter:
    return boto3.client("elasticbeanstalk").get_waiter("environment_exists")
```

[Waiter.EnvironmentExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists)

```python
class EnvironmentExistsWaiter(Boto3Waiter):
    def wait(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## EnvironmentTerminatedWaiter

Type annotations for `boto3.client("elasticbeanstalk").get_waiter("environment_terminated")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.waiters import EnvironmentTerminatedWaiter

def get_environment_terminated_waiter() -> EnvironmentTerminatedWaiter:
    return boto3.client("elasticbeanstalk").get_waiter("environment_terminated")
```

[Waiter.EnvironmentTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated)

```python
class EnvironmentTerminatedWaiter(Boto3Waiter):
    def wait(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## EnvironmentUpdatedWaiter

Type annotations for `boto3.client("elasticbeanstalk").get_waiter("environment_updated")`.

Can be used directly:

```python
from mypy_boto3_elasticbeanstalk.waiters import EnvironmentUpdatedWaiter

def get_environment_updated_waiter() -> EnvironmentUpdatedWaiter:
    return boto3.client("elasticbeanstalk").get_waiter("environment_updated")
```

[Waiter.EnvironmentUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated)

```python
class EnvironmentUpdatedWaiter(Boto3Waiter):
    def wait(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```