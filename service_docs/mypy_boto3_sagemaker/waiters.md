# Waiters for boto3 SageMaker module

> [Index](../index.md) > [SageMaker](./index.md) > Waiters

Auto-generated documentation for [SageMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker)
type annotations stubs module [mypy_boto3_sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/).

- [Waiters for boto3 SageMaker module](#waiters-for-boto3-sagemaker-module)
  - [EndpointDeletedWaiter](#endpointdeletedwaiter)
  - [EndpointInServiceWaiter](#endpointinservicewaiter)
  - [NotebookInstanceDeletedWaiter](#notebookinstancedeletedwaiter)
  - [NotebookInstanceInServiceWaiter](#notebookinstanceinservicewaiter)
  - [NotebookInstanceStoppedWaiter](#notebookinstancestoppedwaiter)
  - [ProcessingJobCompletedOrStoppedWaiter](#processingjobcompletedorstoppedwaiter)
  - [TrainingJobCompletedOrStoppedWaiter](#trainingjobcompletedorstoppedwaiter)
  - [TransformJobCompletedOrStoppedWaiter](#transformjobcompletedorstoppedwaiter)

## EndpointDeletedWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("endpoint_deleted")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import EndpointDeletedWaiter

def get_endpoint_deleted_waiter() -> EndpointDeletedWaiter:
    return boto3.client("sagemaker").get_waiter("endpoint_deleted")
```

[Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted)

```python
class EndpointDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        EndpointName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## EndpointInServiceWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("endpoint_in_service")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import EndpointInServiceWaiter

def get_endpoint_in_service_waiter() -> EndpointInServiceWaiter:
    return boto3.client("sagemaker").get_waiter("endpoint_in_service")
```

[Waiter.EndpointInService documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService)

```python
class EndpointInServiceWaiter(Boto3Waiter):
    def wait(
        self,
        EndpointName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## NotebookInstanceDeletedWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("notebook_instance_deleted")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import NotebookInstanceDeletedWaiter

def get_notebook_instance_deleted_waiter() -> NotebookInstanceDeletedWaiter:
    return boto3.client("sagemaker").get_waiter("notebook_instance_deleted")
```

[Waiter.NotebookInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted)

```python
class NotebookInstanceDeletedWaiter(Boto3Waiter):
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## NotebookInstanceInServiceWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("notebook_instance_in_service")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import NotebookInstanceInServiceWaiter

def get_notebook_instance_in_service_waiter() -> NotebookInstanceInServiceWaiter:
    return boto3.client("sagemaker").get_waiter("notebook_instance_in_service")
```

[Waiter.NotebookInstanceInService documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService)

```python
class NotebookInstanceInServiceWaiter(Boto3Waiter):
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## NotebookInstanceStoppedWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("notebook_instance_stopped")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import NotebookInstanceStoppedWaiter

def get_notebook_instance_stopped_waiter() -> NotebookInstanceStoppedWaiter:
    return boto3.client("sagemaker").get_waiter("notebook_instance_stopped")
```

[Waiter.NotebookInstanceStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped)

```python
class NotebookInstanceStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## ProcessingJobCompletedOrStoppedWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("processing_job_completed_or_stopped")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import ProcessingJobCompletedOrStoppedWaiter

def get_processing_job_completed_or_stopped_waiter() -> ProcessingJobCompletedOrStoppedWaiter:
    return boto3.client("sagemaker").get_waiter("processing_job_completed_or_stopped")
```

[Waiter.ProcessingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped)

```python
class ProcessingJobCompletedOrStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        ProcessingJobName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## TrainingJobCompletedOrStoppedWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("training_job_completed_or_stopped")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import TrainingJobCompletedOrStoppedWaiter

def get_training_job_completed_or_stopped_waiter() -> TrainingJobCompletedOrStoppedWaiter:
    return boto3.client("sagemaker").get_waiter("training_job_completed_or_stopped")
```

[Waiter.TrainingJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped)

```python
class TrainingJobCompletedOrStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        TrainingJobName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## TransformJobCompletedOrStoppedWaiter

Type annotations for `boto3.client("sagemaker").get_waiter("transform_job_completed_or_stopped")`.

Can be used directly:

```python
from mypy_boto3_sagemaker.waiters import TransformJobCompletedOrStoppedWaiter

def get_transform_job_completed_or_stopped_waiter() -> TransformJobCompletedOrStoppedWaiter:
    return boto3.client("sagemaker").get_waiter("transform_job_completed_or_stopped")
```

[Waiter.TransformJobCompletedOrStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped)

```python
class TransformJobCompletedOrStoppedWaiter(Boto3Waiter):
    def wait(
        self,
        TransformJobName: str,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```