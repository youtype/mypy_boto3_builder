# SagemakerEdgeManagerClient for boto3 SagemakerEdgeManager module

> [Index](../index.md) > [SagemakerEdgeManager](./index.md) > SagemakerEdgeManagerClient

Auto-generated documentation for [SagemakerEdgeManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager)
type annotations stubs module [mypy_boto3_sagemaker_edge](https://pypi.org/project/mypy-boto3-sagemaker-edge/).

- [SagemakerEdgeManagerClient for boto3 SagemakerEdgeManager module](#sagemakeredgemanagerclient-for-boto3-sagemakeredgemanager-module)
  - [SagemakerEdgeManagerClient](#sagemakeredgemanagerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_device_registration](#get_device_registration)
    - [send_heartbeat](#send_heartbeat)

## SagemakerEdgeManagerClient

Type annotations for `boto3.client("sagemaker-edge")`

Can be used directly:

```python
from mypy_boto3_sagemaker_edge.client import SagemakerEdgeManagerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sagemaker_edge.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServiceException`


## Methods


### can_paginate

Type annotations for `boto3.client("sagemaker-edge").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sagemaker-edge").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.generate_presigned_url)

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

### get_device_registration

Type annotations for `boto3.client("sagemaker-edge").get_device_registration` method.

[Client.get_device_registration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.get_device_registration)

```python
def get_device_registration(
    self,
    DeviceName: str,
    DeviceFleetName: str
) -> GetDeviceRegistrationResultTypeDef:
    pass
```

### send_heartbeat

Type annotations for `boto3.client("sagemaker-edge").send_heartbeat` method.

[Client.send_heartbeat documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.send_heartbeat)

```python
def send_heartbeat(
    self,
    AgentVersion: str,
    DeviceName: str,
    DeviceFleetName: str,
    AgentMetrics: List["EdgeMetricTypeDef"] = None,
    Models: List[ModelTypeDef] = None
) -> None:
    pass
```