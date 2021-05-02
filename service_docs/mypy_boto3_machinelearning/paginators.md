# Paginators for boto3 MachineLearning module

> [Index](../index.md) > [MachineLearning](./index.md) > Paginators

Auto-generated documentation for [MachineLearning](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning)
type annotations stubs module [mypy_boto3_machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/).

- [Paginators for boto3 MachineLearning module](#paginators-for-boto3-machinelearning-module)
  - [DescribeBatchPredictionsPaginator](#describebatchpredictionspaginator)
  - [DescribeDataSourcesPaginator](#describedatasourcespaginator)
  - [DescribeEvaluationsPaginator](#describeevaluationspaginator)
  - [DescribeMLModelsPaginator](#describemlmodelspaginator)

## DescribeBatchPredictionsPaginator

Type annotations for `boto3.client("machinelearning").get_paginator("describe_batch_predictions")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.paginators import DescribeBatchPredictionsPaginator

def get_describe_batch_predictions_paginator() -> DescribeBatchPredictionsPaginator:
    return boto3.client("machinelearning").get_paginator("describe_batch_predictions")
```

[Paginator.DescribeBatchPredictions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)

```python
class DescribeBatchPredictionsPaginator(Boto3Paginator):
    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBatchPredictionsOutputTypeDef]:
        pass
```
## DescribeDataSourcesPaginator

Type annotations for `boto3.client("machinelearning").get_paginator("describe_data_sources")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.paginators import DescribeDataSourcesPaginator

def get_describe_data_sources_paginator() -> DescribeDataSourcesPaginator:
    return boto3.client("machinelearning").get_paginator("describe_data_sources")
```

[Paginator.DescribeDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)

```python
class DescribeDataSourcesPaginator(Boto3Paginator):
    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDataSourcesOutputTypeDef]:
        pass
```
## DescribeEvaluationsPaginator

Type annotations for `boto3.client("machinelearning").get_paginator("describe_evaluations")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.paginators import DescribeEvaluationsPaginator

def get_describe_evaluations_paginator() -> DescribeEvaluationsPaginator:
    return boto3.client("machinelearning").get_paginator("describe_evaluations")
```

[Paginator.DescribeEvaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)

```python
class DescribeEvaluationsPaginator(Boto3Paginator):
    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEvaluationsOutputTypeDef]:
        pass
```
## DescribeMLModelsPaginator

Type annotations for `boto3.client("machinelearning").get_paginator("describe_ml_models")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.paginators import DescribeMLModelsPaginator

def get_describe_ml_models_paginator() -> DescribeMLModelsPaginator:
    return boto3.client("machinelearning").get_paginator("describe_ml_models")
```

[Paginator.DescribeMLModels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)

```python
class DescribeMLModelsPaginator(Boto3Paginator):
    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMLModelsOutputTypeDef]:
        pass
```