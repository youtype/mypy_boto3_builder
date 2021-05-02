# Type annotations for boto3 SageMakerRuntime module

> [Index](../index.md) > SageMakerRuntime

Auto-generated documentation for [SageMakerRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime)
type annotations stubs module [mypy_boto3_sagemaker_runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime/).

```bash
pip install mypy-boto3-sagemaker-runtime
```

- [Type annotations for boto3 SageMakerRuntime module](#type-annotations-for-boto3-sagemakerruntime-module)
  - [SageMakerRuntimeClient](#sagemakerruntimeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## SageMakerRuntimeClient

Type annotations for  `boto3.client("sagemaker-runtime")` as [SageMakerRuntimeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sagemaker_runtime.client import SageMakerRuntimeClient
```


SageMakerRuntimeClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [invoke_endpoint](./client.md#invoke-endpoint)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalFailure](./client.md#internalfailure)
- [ModelError](./client.md#modelerror)
- [ServiceUnavailable](./client.md#serviceunavailable)
- [ValidationError](./client.md#validationerror)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sagemaker_runtime.type_defs import InvokeEndpointOutputTypeDef, ...
```

- [InvokeEndpointOutputTypeDef](./type_defs.md#invokeendpointoutputtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
