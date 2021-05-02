# MachineLearningClient for boto3 MachineLearning module

> [Index](../index.md) > [MachineLearning](./index.md) > MachineLearningClient

Auto-generated documentation for [MachineLearning](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning)
type annotations stubs module [mypy_boto3_machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/).

- [MachineLearningClient for boto3 MachineLearning module](#machinelearningclient-for-boto3-machinelearning-module)
  - [MachineLearningClient](#machinelearningclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags](#add_tags)
    - [can_paginate](#can_paginate)
    - [create_batch_prediction](#create_batch_prediction)
    - [create_data_source_from_rds](#create_data_source_from_rds)
    - [create_data_source_from_redshift](#create_data_source_from_redshift)
    - [create_data_source_from_s3](#create_data_source_from_s3)
    - [create_evaluation](#create_evaluation)
    - [create_ml_model](#create_ml_model)
    - [create_realtime_endpoint](#create_realtime_endpoint)
    - [delete_batch_prediction](#delete_batch_prediction)
    - [delete_data_source](#delete_data_source)
    - [delete_evaluation](#delete_evaluation)
    - [delete_ml_model](#delete_ml_model)
    - [delete_realtime_endpoint](#delete_realtime_endpoint)
    - [delete_tags](#delete_tags)
    - [describe_batch_predictions](#describe_batch_predictions)
    - [describe_data_sources](#describe_data_sources)
    - [describe_evaluations](#describe_evaluations)
    - [describe_ml_models](#describe_ml_models)
    - [describe_tags](#describe_tags)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_batch_prediction](#get_batch_prediction)
    - [get_data_source](#get_data_source)
    - [get_evaluation](#get_evaluation)
    - [get_ml_model](#get_ml_model)
    - [predict](#predict)
    - [update_batch_prediction](#update_batch_prediction)
    - [update_data_source](#update_data_source)
    - [update_evaluation](#update_evaluation)
    - [update_ml_model](#update_ml_model)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)

## MachineLearningClient

Type annotations for `boto3.client("machinelearning")`

Can be used directly:

```python
from mypy_boto3_machinelearning.client import MachineLearningClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_machinelearning.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidTagException`
- `Exceptions.LimitExceededException`
- `Exceptions.PredictorNotMountedException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TagLimitExceededException`


## Methods


### add_tags

Type annotations for `boto3.client("machinelearning").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.add_tags)

```python
def add_tags(
    self,
    Tags: List["TagTypeDef"],
    ResourceId: str,
    ResourceType: TaggableResourceType
) -> AddTagsOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("machinelearning").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_batch_prediction

Type annotations for `boto3.client("machinelearning").create_batch_prediction` method.

[Client.create_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_batch_prediction)

```python
def create_batch_prediction(
    self,
    BatchPredictionId: str,
    MLModelId: str,
    BatchPredictionDataSourceId: str,
    OutputUri: str,
    BatchPredictionName: str = None
) -> CreateBatchPredictionOutputTypeDef:
    pass
```

### create_data_source_from_rds

Type annotations for `boto3.client("machinelearning").create_data_source_from_rds` method.

[Client.create_data_source_from_rds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_rds)

```python
def create_data_source_from_rds(
    self,
    DataSourceId: str,
    RDSData: RDSDataSpecTypeDef,
    RoleARN: str,
    DataSourceName: str = None,
    ComputeStatistics: bool = None
) -> CreateDataSourceFromRDSOutputTypeDef:
    pass
```

### create_data_source_from_redshift

Type annotations for `boto3.client("machinelearning").create_data_source_from_redshift` method.

[Client.create_data_source_from_redshift documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_redshift)

```python
def create_data_source_from_redshift(
    self,
    DataSourceId: str,
    DataSpec: RedshiftDataSpecTypeDef,
    RoleARN: str,
    DataSourceName: str = None,
    ComputeStatistics: bool = None
) -> CreateDataSourceFromRedshiftOutputTypeDef:
    pass
```

### create_data_source_from_s3

Type annotations for `boto3.client("machinelearning").create_data_source_from_s3` method.

[Client.create_data_source_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_s3)

```python
def create_data_source_from_s3(
    self,
    DataSourceId: str,
    DataSpec: S3DataSpecTypeDef,
    DataSourceName: str = None,
    ComputeStatistics: bool = None
) -> CreateDataSourceFromS3OutputTypeDef:
    pass
```

### create_evaluation

Type annotations for `boto3.client("machinelearning").create_evaluation` method.

[Client.create_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_evaluation)

```python
def create_evaluation(
    self,
    EvaluationId: str,
    MLModelId: str,
    EvaluationDataSourceId: str,
    EvaluationName: str = None
) -> CreateEvaluationOutputTypeDef:
    pass
```

### create_ml_model

Type annotations for `boto3.client("machinelearning").create_ml_model` method.

[Client.create_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_ml_model)

```python
def create_ml_model(
    self,
    MLModelId: str,
    MLModelType: MLModelType,
    TrainingDataSourceId: str,
    MLModelName: str = None,
    Parameters: Dict[str, str] = None,
    Recipe: str = None,
    RecipeUri: str = None
) -> CreateMLModelOutputTypeDef:
    pass
```

### create_realtime_endpoint

Type annotations for `boto3.client("machinelearning").create_realtime_endpoint` method.

[Client.create_realtime_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_realtime_endpoint)

```python
def create_realtime_endpoint(
    self,
    MLModelId: str
) -> CreateRealtimeEndpointOutputTypeDef:
    pass
```

### delete_batch_prediction

Type annotations for `boto3.client("machinelearning").delete_batch_prediction` method.

[Client.delete_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_batch_prediction)

```python
def delete_batch_prediction(
    self,
    BatchPredictionId: str
) -> DeleteBatchPredictionOutputTypeDef:
    pass
```

### delete_data_source

Type annotations for `boto3.client("machinelearning").delete_data_source` method.

[Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_data_source)

```python
def delete_data_source(
    self,
    DataSourceId: str
) -> DeleteDataSourceOutputTypeDef:
    pass
```

### delete_evaluation

Type annotations for `boto3.client("machinelearning").delete_evaluation` method.

[Client.delete_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_evaluation)

```python
def delete_evaluation(
    self,
    EvaluationId: str
) -> DeleteEvaluationOutputTypeDef:
    pass
```

### delete_ml_model

Type annotations for `boto3.client("machinelearning").delete_ml_model` method.

[Client.delete_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_ml_model)

```python
def delete_ml_model(
    self,
    MLModelId: str
) -> DeleteMLModelOutputTypeDef:
    pass
```

### delete_realtime_endpoint

Type annotations for `boto3.client("machinelearning").delete_realtime_endpoint` method.

[Client.delete_realtime_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_realtime_endpoint)

```python
def delete_realtime_endpoint(
    self,
    MLModelId: str
) -> DeleteRealtimeEndpointOutputTypeDef:
    pass
```

### delete_tags

Type annotations for `boto3.client("machinelearning").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_tags)

```python
def delete_tags(
    self,
    TagKeys: List[str],
    ResourceId: str,
    ResourceType: TaggableResourceType
) -> DeleteTagsOutputTypeDef:
    pass
```

### describe_batch_predictions

Type annotations for `boto3.client("machinelearning").describe_batch_predictions` method.

[Client.describe_batch_predictions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_batch_predictions)

```python
def describe_batch_predictions(
    self,
    FilterVariable: BatchPredictionFilterVariable = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeBatchPredictionsOutputTypeDef:
    pass
```

### describe_data_sources

Type annotations for `boto3.client("machinelearning").describe_data_sources` method.

[Client.describe_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_data_sources)

```python
def describe_data_sources(
    self,
    FilterVariable: DataSourceFilterVariable = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeDataSourcesOutputTypeDef:
    pass
```

### describe_evaluations

Type annotations for `boto3.client("machinelearning").describe_evaluations` method.

[Client.describe_evaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_evaluations)

```python
def describe_evaluations(
    self,
    FilterVariable: EvaluationFilterVariable = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeEvaluationsOutputTypeDef:
    pass
```

### describe_ml_models

Type annotations for `boto3.client("machinelearning").describe_ml_models` method.

[Client.describe_ml_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_ml_models)

```python
def describe_ml_models(
    self,
    FilterVariable: MLModelFilterVariable = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: SortOrder = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeMLModelsOutputTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("machinelearning").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_tags)

```python
def describe_tags(
    self,
    ResourceId: str,
    ResourceType: TaggableResourceType
) -> DescribeTagsOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("machinelearning").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.generate_presigned_url)

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

### get_batch_prediction

Type annotations for `boto3.client("machinelearning").get_batch_prediction` method.

[Client.get_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_batch_prediction)

```python
def get_batch_prediction(
    self,
    BatchPredictionId: str
) -> GetBatchPredictionOutputTypeDef:
    pass
```

### get_data_source

Type annotations for `boto3.client("machinelearning").get_data_source` method.

[Client.get_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_data_source)

```python
def get_data_source(
    self,
    DataSourceId: str,
    Verbose: bool = None
) -> GetDataSourceOutputTypeDef:
    pass
```

### get_evaluation

Type annotations for `boto3.client("machinelearning").get_evaluation` method.

[Client.get_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_evaluation)

```python
def get_evaluation(
    self,
    EvaluationId: str
) -> GetEvaluationOutputTypeDef:
    pass
```

### get_ml_model

Type annotations for `boto3.client("machinelearning").get_ml_model` method.

[Client.get_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_ml_model)

```python
def get_ml_model(
    self,
    MLModelId: str,
    Verbose: bool = None
) -> GetMLModelOutputTypeDef:
    pass
```

### predict

Type annotations for `boto3.client("machinelearning").predict` method.

[Client.predict documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.predict)

```python
def predict(
    self,
    MLModelId: str,
    Record: Dict[str, str],
    PredictEndpoint: str
) -> PredictOutputTypeDef:
    pass
```

### update_batch_prediction

Type annotations for `boto3.client("machinelearning").update_batch_prediction` method.

[Client.update_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_batch_prediction)

```python
def update_batch_prediction(
    self,
    BatchPredictionId: str,
    BatchPredictionName: str
) -> UpdateBatchPredictionOutputTypeDef:
    pass
```

### update_data_source

Type annotations for `boto3.client("machinelearning").update_data_source` method.

[Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_data_source)

```python
def update_data_source(
    self,
    DataSourceId: str,
    DataSourceName: str
) -> UpdateDataSourceOutputTypeDef:
    pass
```

### update_evaluation

Type annotations for `boto3.client("machinelearning").update_evaluation` method.

[Client.update_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_evaluation)

```python
def update_evaluation(
    self,
    EvaluationId: str,
    EvaluationName: str
) -> UpdateEvaluationOutputTypeDef:
    pass
```

### update_ml_model

Type annotations for `boto3.client("machinelearning").update_ml_model` method.

[Client.update_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_ml_model)

```python
def update_ml_model(
    self,
    MLModelId: str,
    MLModelName: str = None,
    ScoreThreshold: float = None
) -> UpdateMLModelOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("machinelearning").get_paginator` method.

[Paginator.DescribeBatchPredictions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeBatchPredictionsPaginatorName
) -> DescribeBatchPredictionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("machinelearning").get_paginator` method.

[Paginator.DescribeDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDataSourcesPaginatorName
) -> DescribeDataSourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("machinelearning").get_paginator` method.

[Paginator.DescribeEvaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEvaluationsPaginatorName
) -> DescribeEvaluationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("machinelearning").get_paginator` method.

[Paginator.DescribeMLModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeMLModelsPaginatorName
) -> DescribeMLModelsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("machinelearning").get_waiter` method.

[Waiter.BatchPredictionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: BatchPredictionAvailableWaiterName
) -> BatchPredictionAvailableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("machinelearning").get_waiter` method.

[Waiter.DataSourceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: DataSourceAvailableWaiterName
) -> DataSourceAvailableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("machinelearning").get_waiter` method.

[Waiter.EvaluationAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: EvaluationAvailableWaiterName
) -> EvaluationAvailableWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("machinelearning").get_waiter` method.

[Waiter.MLModelAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)

```python
@overload
def get_waiter(
    self,
    waiter_name: MLModelAvailableWaiterName
) -> MLModelAvailableWaiter:
    pass
```