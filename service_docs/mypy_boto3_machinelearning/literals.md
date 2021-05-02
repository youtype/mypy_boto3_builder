# Literals for boto3 MachineLearning module

> [Index](../index.md) > [MachineLearning](./index.md) > Literals

Auto-generated documentation for [MachineLearning](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning)
type annotations stubs module [mypy_boto3_machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/).

- [Literals for boto3 MachineLearning module](#literals-for-boto3-machinelearning-module)
  - [Algorithm](#algorithm)
  - [BatchPredictionAvailableWaiterName](#batchpredictionavailablewaitername)
  - [BatchPredictionFilterVariable](#batchpredictionfiltervariable)
  - [DataSourceAvailableWaiterName](#datasourceavailablewaitername)
  - [DataSourceFilterVariable](#datasourcefiltervariable)
  - [DescribeBatchPredictionsPaginatorName](#describebatchpredictionspaginatorname)
  - [DescribeDataSourcesPaginatorName](#describedatasourcespaginatorname)
  - [DescribeEvaluationsPaginatorName](#describeevaluationspaginatorname)
  - [DescribeMLModelsPaginatorName](#describemlmodelspaginatorname)
  - [DetailsAttributes](#detailsattributes)
  - [EntityStatus](#entitystatus)
  - [EvaluationAvailableWaiterName](#evaluationavailablewaitername)
  - [EvaluationFilterVariable](#evaluationfiltervariable)
  - [MLModelAvailableWaiterName](#mlmodelavailablewaitername)
  - [MLModelFilterVariable](#mlmodelfiltervariable)
  - [MLModelType](#mlmodeltype)
  - [RealtimeEndpointStatus](#realtimeendpointstatus)
  - [SortOrder](#sortorder)
  - [TaggableResourceType](#taggableresourcetype)

## Algorithm

```python
from mypy_boto3_machinelearning.literals import Algorithm
```

Values:

- `sgd`

## BatchPredictionAvailableWaiterName

```python
from mypy_boto3_machinelearning.literals import BatchPredictionAvailableWaiterName
```

Values:

- `batch_prediction_available`

## BatchPredictionFilterVariable

```python
from mypy_boto3_machinelearning.literals import BatchPredictionFilterVariable
```

Values:

- `CreatedAt`
- `DataSourceId`
- `DataURI`
- `IAMUser`
- `LastUpdatedAt`
- `MLModelId`
- `Name`
- `Status`

## DataSourceAvailableWaiterName

```python
from mypy_boto3_machinelearning.literals import DataSourceAvailableWaiterName
```

Values:

- `data_source_available`

## DataSourceFilterVariable

```python
from mypy_boto3_machinelearning.literals import DataSourceFilterVariable
```

Values:

- `CreatedAt`
- `DataLocationS3`
- `IAMUser`
- `LastUpdatedAt`
- `Name`
- `Status`

## DescribeBatchPredictionsPaginatorName

```python
from mypy_boto3_machinelearning.literals import DescribeBatchPredictionsPaginatorName
```

Values:

- `describe_batch_predictions`

## DescribeDataSourcesPaginatorName

```python
from mypy_boto3_machinelearning.literals import DescribeDataSourcesPaginatorName
```

Values:

- `describe_data_sources`

## DescribeEvaluationsPaginatorName

```python
from mypy_boto3_machinelearning.literals import DescribeEvaluationsPaginatorName
```

Values:

- `describe_evaluations`

## DescribeMLModelsPaginatorName

```python
from mypy_boto3_machinelearning.literals import DescribeMLModelsPaginatorName
```

Values:

- `describe_ml_models`

## DetailsAttributes

```python
from mypy_boto3_machinelearning.literals import DetailsAttributes
```

Values:

- `Algorithm`
- `PredictiveModelType`

## EntityStatus

```python
from mypy_boto3_machinelearning.literals import EntityStatus
```

Values:

- `COMPLETED`
- `DELETED`
- `FAILED`
- `INPROGRESS`
- `PENDING`

## EvaluationAvailableWaiterName

```python
from mypy_boto3_machinelearning.literals import EvaluationAvailableWaiterName
```

Values:

- `evaluation_available`

## EvaluationFilterVariable

```python
from mypy_boto3_machinelearning.literals import EvaluationFilterVariable
```

Values:

- `CreatedAt`
- `DataSourceId`
- `DataURI`
- `IAMUser`
- `LastUpdatedAt`
- `MLModelId`
- `Name`
- `Status`

## MLModelAvailableWaiterName

```python
from mypy_boto3_machinelearning.literals import MLModelAvailableWaiterName
```

Values:

- `ml_model_available`

## MLModelFilterVariable

```python
from mypy_boto3_machinelearning.literals import MLModelFilterVariable
```

Values:

- `Algorithm`
- `CreatedAt`
- `IAMUser`
- `LastUpdatedAt`
- `MLModelType`
- `Name`
- `RealtimeEndpointStatus`
- `Status`
- `TrainingDataSourceId`
- `TrainingDataURI`

## MLModelType

```python
from mypy_boto3_machinelearning.literals import MLModelType
```

Values:

- `BINARY`
- `MULTICLASS`
- `REGRESSION`

## RealtimeEndpointStatus

```python
from mypy_boto3_machinelearning.literals import RealtimeEndpointStatus
```

Values:

- `FAILED`
- `NONE`
- `READY`
- `UPDATING`

## SortOrder

```python
from mypy_boto3_machinelearning.literals import SortOrder
```

Values:

- `asc`
- `dsc`

## TaggableResourceType

```python
from mypy_boto3_machinelearning.literals import TaggableResourceType
```

Values:

- `BatchPrediction`
- `DataSource`
- `Evaluation`
- `MLModel`
