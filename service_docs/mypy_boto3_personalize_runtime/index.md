# Type annotations for boto3 PersonalizeRuntime module

> [Index](../index.md) > PersonalizeRuntime

Auto-generated documentation for [PersonalizeRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime)
type annotations stubs module [mypy_boto3_personalize_runtime](https://pypi.org/project/mypy-boto3-personalize-runtime/).

```bash
pip install mypy-boto3-personalize-runtime
```

- [Type annotations for boto3 PersonalizeRuntime module](#type-annotations-for-boto3-personalizeruntime-module)
  - [PersonalizeRuntimeClient](#personalizeruntimeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## PersonalizeRuntimeClient

Type annotations for  `boto3.client("personalize-runtime")` as [PersonalizeRuntimeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_personalize_runtime.client import PersonalizeRuntimeClient
```


PersonalizeRuntimeClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_personalized_ranking](./client.md#get-personalized-ranking)
- [get_recommendations](./client.md#get-recommendations)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidInputException](./client.md#invalidinputexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_personalize_runtime.type_defs import GetPersonalizedRankingResponseTypeDef, ...
```

- [GetPersonalizedRankingResponseTypeDef](./type_defs.md#getpersonalizedrankingresponsetypedef)
- [GetRecommendationsResponseTypeDef](./type_defs.md#getrecommendationsresponsetypedef)
- [PredictedItemTypeDef](./type_defs.md#predicteditemtypedef)
