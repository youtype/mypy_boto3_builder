# Waiters for boto3 Rekognition module

> [Index](../index.md) > [Rekognition](./index.md) > Waiters

Auto-generated documentation for [Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition)
type annotations stubs module [mypy_boto3_rekognition](https://pypi.org/project/mypy-boto3-rekognition/).

- [Waiters for boto3 Rekognition module](#waiters-for-boto3-rekognition-module)
  - [ProjectVersionRunningWaiter](#projectversionrunningwaiter)
  - [ProjectVersionTrainingCompletedWaiter](#projectversiontrainingcompletedwaiter)

## ProjectVersionRunningWaiter

Type annotations for `boto3.client("rekognition").get_waiter("project_version_running")`.

Can be used directly:

```python
from mypy_boto3_rekognition.waiters import ProjectVersionRunningWaiter

def get_project_version_running_waiter() -> ProjectVersionRunningWaiter:
    return boto3.client("rekognition").get_waiter("project_version_running")
```

[Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)

```python
class ProjectVersionRunningWaiter(Boto3Waiter):
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ProjectVersionTrainingCompletedWaiter

Type annotations for `boto3.client("rekognition").get_waiter("project_version_training_completed")`.

Can be used directly:

```python
from mypy_boto3_rekognition.waiters import ProjectVersionTrainingCompletedWaiter

def get_project_version_training_completed_waiter() -> ProjectVersionTrainingCompletedWaiter:
    return boto3.client("rekognition").get_waiter("project_version_training_completed")
```

[Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)

```python
class ProjectVersionTrainingCompletedWaiter(Boto3Waiter):
    def wait(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```