# Structures for boto3 AugmentedAIRuntime module

> [Index](../index.md) > [AugmentedAIRuntime](./index.md) > Structures

Auto-generated documentation for [AugmentedAIRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime)
type annotations stubs module [mypy_boto3_sagemaker_a2i_runtime](https://pypi.org/project/mypy-boto3-sagemaker-a2i-runtime/).

- [Structures for boto3 AugmentedAIRuntime module](#structures-for-boto3-augmentedairuntime-module)
  - [HumanLoopOutputTypeDef](#humanloopoutputtypedef)
  - [HumanLoopSummaryTypeDef](#humanloopsummarytypedef)
  - [ResponseMetadata](#responsemetadata)
  - [DescribeHumanLoopResponseTypeDef](#describehumanloopresponsetypedef)
  - [HumanLoopDataAttributesTypeDef](#humanloopdataattributestypedef)
  - [HumanLoopInputTypeDef](#humanloopinputtypedef)
  - [ListHumanLoopsResponseTypeDef](#listhumanloopsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [StartHumanLoopResponseTypeDef](#starthumanloopresponsetypedef)

## HumanLoopOutputTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopOutputTypeDef
```


Required fields:
- `OutputS3Uri`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## HumanLoopSummaryTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopSummaryTypeDef
```




Optional fields:
- `HumanLoopName`: `str`
- `HumanLoopStatus`: `HumanLoopStatus`
- `CreationTime`: `datetime`
- `FailureReason`: `str`
- `FlowDefinitionArn`: `str`


## ResponseMetadata

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## DescribeHumanLoopResponseTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import DescribeHumanLoopResponseTypeDef
```


Required fields:
- `CreationTime`: `datetime`
- `HumanLoopStatus`: `HumanLoopStatus`
- `HumanLoopName`: `str`
- `HumanLoopArn`: `str`
- `FlowDefinitionArn`: `str`



Optional fields:
- `FailureReason`: `str`
- `FailureCode`: `str`
- `HumanLoopOutput`: `"HumanLoopOutputTypeDef"`


## HumanLoopDataAttributesTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopDataAttributesTypeDef
```


Required fields:
- `ContentClassifiers`: `List[ContentClassifier]`




## HumanLoopInputTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopInputTypeDef
```


Required fields:
- `InputContent`: `str`




## ListHumanLoopsResponseTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import ListHumanLoopsResponseTypeDef
```


Required fields:
- `HumanLoopSummaries`: `List["HumanLoopSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## StartHumanLoopResponseTypeDef

```python
from mypy_boto3_sagemaker_a2i_runtime.type_defs import StartHumanLoopResponseTypeDef
```




Optional fields:
- `HumanLoopArn`: `str`

