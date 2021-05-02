# SageMakerRuntimeClient for boto3 SageMakerRuntime module

> [Index](../index.md) > [SageMakerRuntime](./index.md) > SageMakerRuntimeClient

Auto-generated documentation for [SageMakerRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime)
type annotations stubs module [mypy_boto3_sagemaker_runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime/).

- [SageMakerRuntimeClient for boto3 SageMakerRuntime module](#sagemakerruntimeclient-for-boto3-sagemakerruntime-module)
  - [SageMakerRuntimeClient](#sagemakerruntimeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [invoke_endpoint](#invoke_endpoint)

## SageMakerRuntimeClient

Type annotations for `boto3.client("sagemaker-runtime")`

Can be used directly:

```python
from mypy_boto3_sagemaker_runtime.client import SageMakerRuntimeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sagemaker_runtime.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalFailure`
- `Exceptions.ModelError`
- `Exceptions.ServiceUnavailable`
- `Exceptions.ValidationError`


## Methods


### can_paginate

Type annotations for `boto3.client("sagemaker-runtime").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sagemaker-runtime").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.generate_presigned_url)

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

### invoke_endpoint

Type annotations for `boto3.client("sagemaker-runtime").invoke_endpoint` method.

[Client.invoke_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client.invoke_endpoint)

```python
def invoke_endpoint(
    self,
    EndpointName: str,
    Body: Union[bytes, IO[bytes]],
    ContentType: str = None,
    Accept: str = None,
    CustomAttributes: str = None,
    TargetModel: str = None,
    TargetVariant: str = None,
    TargetContainerHostname: str = None,
    InferenceId: str = None
) -> InvokeEndpointOutputTypeDef:
    pass
```



