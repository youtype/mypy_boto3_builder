# Structures for boto3 SageMakerRuntime module

> [Index](../index.md) > [SageMakerRuntime](./index.md) > Structures

Auto-generated documentation for [SageMakerRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime)
type annotations stubs module [mypy_boto3_sagemaker_runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime/).

- [Structures for boto3 SageMakerRuntime module](#structures-for-boto3-sagemakerruntime-module)
  - [InvokeEndpointOutputTypeDef](#invokeendpointoutputtypedef)
  - [ResponseMetadata](#responsemetadata)

## InvokeEndpointOutputTypeDef

```python
from mypy_boto3_sagemaker_runtime.type_defs import InvokeEndpointOutputTypeDef
```


Required fields:
- `Body`: `Union[bytes, IO[bytes]]`



Optional fields:
- `ContentType`: `str`
- `InvokedProductionVariant`: `str`
- `CustomAttributes`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResponseMetadata

```python
from mypy_boto3_sagemaker_runtime.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`



