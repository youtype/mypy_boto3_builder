# Type annotations for boto3 SagemakerFeatureStoreRuntime module

> [Index](../index.md) > SagemakerFeatureStoreRuntime

Auto-generated documentation for [SagemakerFeatureStoreRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime)
type annotations stubs module [mypy_boto3_sagemaker_featurestore_runtime](https://pypi.org/project/mypy-boto3-sagemaker-featurestore-runtime/).

```bash
pip install mypy-boto3-sagemaker-featurestore-runtime
```

- [Type annotations for boto3 SagemakerFeatureStoreRuntime module](#type-annotations-for-boto3-sagemakerfeaturestoreruntime-module)
  - [SagemakerFeatureStoreRuntimeClient](#sagemakerfeaturestoreruntimeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## SagemakerFeatureStoreRuntimeClient

Type annotations for  `boto3.client("sagemaker-featurestore-runtime")` as [SagemakerFeatureStoreRuntimeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sagemaker_featurestore_runtime.client import SagemakerFeatureStoreRuntimeClient
```


SagemakerFeatureStoreRuntimeClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [delete_record](./client.md#delete-record)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_record](./client.md#get-record)
- [put_record](./client.md#put-record)




### Exceptions
- [AccessForbidden](./client.md#accessforbidden)
- [ClientError](./client.md#clienterror)
- [InternalFailure](./client.md#internalfailure)
- [ResourceNotFound](./client.md#resourcenotfound)
- [ServiceUnavailable](./client.md#serviceunavailable)
- [ValidationError](./client.md#validationerror)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sagemaker_featurestore_runtime.type_defs import FeatureValueTypeDef, ...
```

- [FeatureValueTypeDef](./type_defs.md#featurevaluetypedef)
- [GetRecordResponseTypeDef](./type_defs.md#getrecordresponsetypedef)
