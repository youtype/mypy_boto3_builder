# LookoutEquipmentClient for boto3 LookoutEquipment module

> [Index](../index.md) > [LookoutEquipment](./index.md) > LookoutEquipmentClient

Auto-generated documentation for [LookoutEquipment](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment)
type annotations stubs module [mypy_boto3_lookoutequipment](https://pypi.org/project/mypy-boto3-lookoutequipment/).

- [LookoutEquipmentClient for boto3 LookoutEquipment module](#lookoutequipmentclient-for-boto3-lookoutequipment-module)
  - [LookoutEquipmentClient](#lookoutequipmentclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_dataset](#create_dataset)
    - [create_inference_scheduler](#create_inference_scheduler)
    - [create_model](#create_model)
    - [delete_dataset](#delete_dataset)
    - [delete_inference_scheduler](#delete_inference_scheduler)
    - [delete_model](#delete_model)
    - [describe_data_ingestion_job](#describe_data_ingestion_job)
    - [describe_dataset](#describe_dataset)
    - [describe_inference_scheduler](#describe_inference_scheduler)
    - [describe_model](#describe_model)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_data_ingestion_jobs](#list_data_ingestion_jobs)
    - [list_datasets](#list_datasets)
    - [list_inference_executions](#list_inference_executions)
    - [list_inference_schedulers](#list_inference_schedulers)
    - [list_models](#list_models)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_data_ingestion_job](#start_data_ingestion_job)
    - [start_inference_scheduler](#start_inference_scheduler)
    - [stop_inference_scheduler](#stop_inference_scheduler)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_inference_scheduler](#update_inference_scheduler)

## LookoutEquipmentClient

Type annotations for `boto3.client("lookoutequipment")`

Can be used directly:

```python
from mypy_boto3_lookoutequipment.client import LookoutEquipmentClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lookoutequipment.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("lookoutequipment").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_dataset

Type annotations for `boto3.client("lookoutequipment").create_dataset` method.

[Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_dataset)

```python
def create_dataset(
    self,
    DatasetName: str,
    DatasetSchema: DatasetSchemaTypeDef,
    ClientToken: str,
    ServerSideKmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDatasetResponseTypeDef:
    pass
```

### create_inference_scheduler

Type annotations for `boto3.client("lookoutequipment").create_inference_scheduler` method.

[Client.create_inference_scheduler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_inference_scheduler)

```python
def create_inference_scheduler(
    self,
    ModelName: str,
    InferenceSchedulerName: str,
    DataUploadFrequency: DataUploadFrequency,
    DataInputConfiguration: "InferenceInputConfigurationTypeDef",
    DataOutputConfiguration: "InferenceOutputConfigurationTypeDef",
    RoleArn: str,
    ClientToken: str,
    DataDelayOffsetInMinutes: int = None,
    ServerSideKmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateInferenceSchedulerResponseTypeDef:
    pass
```

### create_model

Type annotations for `boto3.client("lookoutequipment").create_model` method.

[Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_model)

```python
def create_model(
    self,
    ModelName: str,
    DatasetName: str,
    ClientToken: str,
    DatasetSchema: DatasetSchemaTypeDef = None,
    LabelsInputConfiguration: "LabelsInputConfigurationTypeDef" = None,
    TrainingDataStartTime: datetime = None,
    TrainingDataEndTime: datetime = None,
    EvaluationDataStartTime: datetime = None,
    EvaluationDataEndTime: datetime = None,
    RoleArn: str = None,
    DataPreProcessingConfiguration: "DataPreProcessingConfigurationTypeDef" = None,
    ServerSideKmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateModelResponseTypeDef:
    pass
```

### delete_dataset

Type annotations for `boto3.client("lookoutequipment").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_dataset)

```python
def delete_dataset(
    self,
    DatasetName: str
) -> None:
    pass
```

### delete_inference_scheduler

Type annotations for `boto3.client("lookoutequipment").delete_inference_scheduler` method.

[Client.delete_inference_scheduler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_inference_scheduler)

```python
def delete_inference_scheduler(
    self,
    InferenceSchedulerName: str
) -> None:
    pass
```

### delete_model

Type annotations for `boto3.client("lookoutequipment").delete_model` method.

[Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_model)

```python
def delete_model(
    self,
    ModelName: str
) -> None:
    pass
```

### describe_data_ingestion_job

Type annotations for `boto3.client("lookoutequipment").describe_data_ingestion_job` method.

[Client.describe_data_ingestion_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_data_ingestion_job)

```python
def describe_data_ingestion_job(
    self,
    JobId: str
) -> DescribeDataIngestionJobResponseTypeDef:
    pass
```

### describe_dataset

Type annotations for `boto3.client("lookoutequipment").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_dataset)

```python
def describe_dataset(
    self,
    DatasetName: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_inference_scheduler

Type annotations for `boto3.client("lookoutequipment").describe_inference_scheduler` method.

[Client.describe_inference_scheduler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_inference_scheduler)

```python
def describe_inference_scheduler(
    self,
    InferenceSchedulerName: str
) -> DescribeInferenceSchedulerResponseTypeDef:
    pass
```

### describe_model

Type annotations for `boto3.client("lookoutequipment").describe_model` method.

[Client.describe_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_model)

```python
def describe_model(
    self,
    ModelName: str
) -> DescribeModelResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lookoutequipment").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.generate_presigned_url)

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

### list_data_ingestion_jobs

Type annotations for `boto3.client("lookoutequipment").list_data_ingestion_jobs` method.

[Client.list_data_ingestion_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_data_ingestion_jobs)

```python
def list_data_ingestion_jobs(
    self,
    DatasetName: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    Status: IngestionJobStatus = None
) -> ListDataIngestionJobsResponseTypeDef:
    pass
```

### list_datasets

Type annotations for `boto3.client("lookoutequipment").list_datasets` method.

[Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_datasets)

```python
def list_datasets(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    DatasetNameBeginsWith: str = None
) -> ListDatasetsResponseTypeDef:
    pass
```

### list_inference_executions

Type annotations for `boto3.client("lookoutequipment").list_inference_executions` method.

[Client.list_inference_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_executions)

```python
def list_inference_executions(
    self,
    InferenceSchedulerName: str,
    NextToken: str = None,
    MaxResults: int = None,
    DataStartTimeAfter: datetime = None,
    DataEndTimeBefore: datetime = None,
    Status: InferenceExecutionStatus = None
) -> ListInferenceExecutionsResponseTypeDef:
    pass
```

### list_inference_schedulers

Type annotations for `boto3.client("lookoutequipment").list_inference_schedulers` method.

[Client.list_inference_schedulers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_schedulers)

```python
def list_inference_schedulers(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    InferenceSchedulerNameBeginsWith: str = None,
    ModelName: str = None
) -> ListInferenceSchedulersResponseTypeDef:
    pass
```

### list_models

Type annotations for `boto3.client("lookoutequipment").list_models` method.

[Client.list_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_models)

```python
def list_models(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Status: ModelStatus = None,
    ModelNameBeginsWith: str = None,
    DatasetNameBeginsWith: str = None
) -> ListModelsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("lookoutequipment").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_data_ingestion_job

Type annotations for `boto3.client("lookoutequipment").start_data_ingestion_job` method.

[Client.start_data_ingestion_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_data_ingestion_job)

```python
def start_data_ingestion_job(
    self,
    DatasetName: str,
    IngestionInputConfiguration: "IngestionInputConfigurationTypeDef",
    RoleArn: str,
    ClientToken: str
) -> StartDataIngestionJobResponseTypeDef:
    pass
```

### start_inference_scheduler

Type annotations for `boto3.client("lookoutequipment").start_inference_scheduler` method.

[Client.start_inference_scheduler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_inference_scheduler)

```python
def start_inference_scheduler(
    self,
    InferenceSchedulerName: str
) -> StartInferenceSchedulerResponseTypeDef:
    pass
```

### stop_inference_scheduler

Type annotations for `boto3.client("lookoutequipment").stop_inference_scheduler` method.

[Client.stop_inference_scheduler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.stop_inference_scheduler)

```python
def stop_inference_scheduler(
    self,
    InferenceSchedulerName: str
) -> StopInferenceSchedulerResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("lookoutequipment").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("lookoutequipment").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_inference_scheduler

Type annotations for `boto3.client("lookoutequipment").update_inference_scheduler` method.

[Client.update_inference_scheduler documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_inference_scheduler)

```python
def update_inference_scheduler(
    self,
    InferenceSchedulerName: str,
    DataDelayOffsetInMinutes: int = None,
    DataUploadFrequency: DataUploadFrequency = None,
    DataInputConfiguration: "InferenceInputConfigurationTypeDef" = None,
    DataOutputConfiguration: "InferenceOutputConfigurationTypeDef" = None,
    RoleArn: str = None
) -> None:
    pass
```