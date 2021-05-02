# IoTJobsDataPlaneClient for boto3 IoTJobsDataPlane module

> [Index](../index.md) > [IoTJobsDataPlane](./index.md) > IoTJobsDataPlaneClient

Auto-generated documentation for [IoTJobsDataPlane](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane)
type annotations stubs module [mypy_boto3_iot_jobs_data](https://pypi.org/project/mypy-boto3-iot-jobs-data/).

- [IoTJobsDataPlaneClient for boto3 IoTJobsDataPlane module](#iotjobsdataplaneclient-for-boto3-iotjobsdataplane-module)
  - [IoTJobsDataPlaneClient](#iotjobsdataplaneclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_job_execution](#describe_job_execution)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_pending_job_executions](#get_pending_job_executions)
    - [start_next_pending_job_execution](#start_next_pending_job_execution)
    - [update_job_execution](#update_job_execution)

## IoTJobsDataPlaneClient

Type annotations for `boto3.client("iot-jobs-data")`

Can be used directly:

```python
from mypy_boto3_iot_jobs_data.client import IoTJobsDataPlaneClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iot_jobs_data.client import Exceptions

def handle_error(exc: Exceptions.CertificateValidationException) -> None:
    ...
```


Exceptions:

- `Exceptions.CertificateValidationException`
- `Exceptions.ClientError`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidStateTransitionException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TerminalStateException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("iot-jobs-data").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_job_execution

Type annotations for `boto3.client("iot-jobs-data").describe_job_execution` method.

[Client.describe_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.describe_job_execution)

```python
def describe_job_execution(
    self,
    jobId: str,
    thingName: str,
    includeJobDocument: bool = None,
    executionNumber: int = None
) -> DescribeJobExecutionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iot-jobs-data").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_pending_job_executions

Type annotations for `boto3.client("iot-jobs-data").get_pending_job_executions` method.

[Client.get_pending_job_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.get_pending_job_executions)

```python
def get_pending_job_executions(
    self,
    thingName: str
) -> GetPendingJobExecutionsResponseTypeDef:
    pass
```

### start_next_pending_job_execution

Type annotations for `boto3.client("iot-jobs-data").start_next_pending_job_execution` method.

[Client.start_next_pending_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.start_next_pending_job_execution)

```python
def start_next_pending_job_execution(
    self,
    thingName: str,
    statusDetails: Dict[str, str] = None,
    stepTimeoutInMinutes: int = None
) -> StartNextPendingJobExecutionResponseTypeDef:
    pass
```

### update_job_execution

Type annotations for `boto3.client("iot-jobs-data").update_job_execution` method.

[Client.update_job_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html#IoTJobsDataPlane.Client.update_job_execution)

```python
def update_job_execution(
    self,
    jobId: str,
    thingName: str,
    status: JobExecutionStatus,
    statusDetails: Dict[str, str] = None,
    stepTimeoutInMinutes: int = None,
    expectedVersion: int = None,
    includeJobExecutionState: bool = None,
    includeJobDocument: bool = None,
    executionNumber: int = None
) -> UpdateJobExecutionResponseTypeDef:
    pass
```