# Waiters for boto3 MachineLearning module

> [Index](../index.md) > [MachineLearning](./index.md) > Waiters

Auto-generated documentation for [MachineLearning](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning)
type annotations stubs module [mypy_boto3_machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/).

- [Waiters for boto3 MachineLearning module](#waiters-for-boto3-machinelearning-module)
  - [BatchPredictionAvailableWaiter](#batchpredictionavailablewaiter)
  - [DataSourceAvailableWaiter](#datasourceavailablewaiter)
  - [EvaluationAvailableWaiter](#evaluationavailablewaiter)
  - [MLModelAvailableWaiter](#mlmodelavailablewaiter)

## BatchPredictionAvailableWaiter

Type annotations for `boto3.client("machinelearning").get_waiter("batch_prediction_available")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.waiters import BatchPredictionAvailableWaiter

def get_batch_prediction_available_waiter() -> BatchPredictionAvailableWaiter:
    return boto3.client("machinelearning").get_waiter("batch_prediction_available")
```

[Waiter.BatchPredictionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)

```python
class BatchPredictionAvailableWaiter(Boto3Waiter):
    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## DataSourceAvailableWaiter

Type annotations for `boto3.client("machinelearning").get_waiter("data_source_available")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.waiters import DataSourceAvailableWaiter

def get_data_source_available_waiter() -> DataSourceAvailableWaiter:
    return boto3.client("machinelearning").get_waiter("data_source_available")
```

[Waiter.DataSourceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)

```python
class DataSourceAvailableWaiter(Boto3Waiter):
    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## EvaluationAvailableWaiter

Type annotations for `boto3.client("machinelearning").get_waiter("evaluation_available")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.waiters import EvaluationAvailableWaiter

def get_evaluation_available_waiter() -> EvaluationAvailableWaiter:
    return boto3.client("machinelearning").get_waiter("evaluation_available")
```

[Waiter.EvaluationAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)

```python
class EvaluationAvailableWaiter(Boto3Waiter):
    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```
## MLModelAvailableWaiter

Type annotations for `boto3.client("machinelearning").get_waiter("ml_model_available")`.

Can be used directly:

```python
from mypy_boto3_machinelearning.waiters import MLModelAvailableWaiter

def get_ml_model_available_waiter() -> MLModelAvailableWaiter:
    return boto3.client("machinelearning").get_waiter("ml_model_available")
```

[Waiter.MLModelAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)

```python
class MLModelAvailableWaiter(Boto3Waiter):
    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        pass
```