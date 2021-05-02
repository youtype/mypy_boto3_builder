# Structures for boto3 SagemakerEdgeManager module

> [Index](../index.md) > [SagemakerEdgeManager](./index.md) > Structures

Auto-generated documentation for [SagemakerEdgeManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager)
type annotations stubs module [mypy_boto3_sagemaker_edge](https://pypi.org/project/mypy-boto3-sagemaker-edge/).

- [Structures for boto3 SagemakerEdgeManager module](#structures-for-boto3-sagemakeredgemanager-module)
  - [EdgeMetricTypeDef](#edgemetrictypedef)
  - [GetDeviceRegistrationResultTypeDef](#getdeviceregistrationresulttypedef)
  - [ModelTypeDef](#modeltypedef)

## EdgeMetricTypeDef

```python
from mypy_boto3_sagemaker_edge.type_defs import EdgeMetricTypeDef
```




Optional fields:
- `Dimension`: `str`
- `MetricName`: `str`
- `Value`: `float`
- `Timestamp`: `datetime`


## GetDeviceRegistrationResultTypeDef

```python
from mypy_boto3_sagemaker_edge.type_defs import GetDeviceRegistrationResultTypeDef
```




Optional fields:
- `DeviceRegistration`: `str`
- `CacheTTL`: `str`


## ModelTypeDef

```python
from mypy_boto3_sagemaker_edge.type_defs import ModelTypeDef
```




Optional fields:
- `ModelName`: `str`
- `ModelVersion`: `str`
- `LatestSampleTime`: `datetime`
- `LatestInference`: `datetime`
- `ModelMetrics`: `List["EdgeMetricTypeDef"]`

