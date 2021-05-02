# Structures for boto3 PersonalizeRuntime module

> [Index](../index.md) > [PersonalizeRuntime](./index.md) > Structures

Auto-generated documentation for [PersonalizeRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime)
type annotations stubs module [mypy_boto3_personalize_runtime](https://pypi.org/project/mypy-boto3-personalize-runtime/).

- [Structures for boto3 PersonalizeRuntime module](#structures-for-boto3-personalizeruntime-module)
  - [PredictedItemTypeDef](#predicteditemtypedef)
  - [GetPersonalizedRankingResponseTypeDef](#getpersonalizedrankingresponsetypedef)
  - [GetRecommendationsResponseTypeDef](#getrecommendationsresponsetypedef)

## PredictedItemTypeDef

```python
from mypy_boto3_personalize_runtime.type_defs import PredictedItemTypeDef
```




Optional fields:
- `itemId`: `str`
- `score`: `float`


## GetPersonalizedRankingResponseTypeDef

```python
from mypy_boto3_personalize_runtime.type_defs import GetPersonalizedRankingResponseTypeDef
```




Optional fields:
- `personalizedRanking`: `List["PredictedItemTypeDef"]`
- `recommendationId`: `str`


## GetRecommendationsResponseTypeDef

```python
from mypy_boto3_personalize_runtime.type_defs import GetRecommendationsResponseTypeDef
```




Optional fields:
- `itemList`: `List["PredictedItemTypeDef"]`
- `recommendationId`: `str`

