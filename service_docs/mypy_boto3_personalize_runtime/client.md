# PersonalizeRuntimeClient for boto3 PersonalizeRuntime module

> [Index](../index.md) > [PersonalizeRuntime](./index.md) > PersonalizeRuntimeClient

Auto-generated documentation for [PersonalizeRuntime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime)
type annotations stubs module [mypy_boto3_personalize_runtime](https://pypi.org/project/mypy-boto3-personalize-runtime/).

- [PersonalizeRuntimeClient for boto3 PersonalizeRuntime module](#personalizeruntimeclient-for-boto3-personalizeruntime-module)
  - [PersonalizeRuntimeClient](#personalizeruntimeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_personalized_ranking](#get_personalized_ranking)
    - [get_recommendations](#get_recommendations)

## PersonalizeRuntimeClient

Type annotations for `boto3.client("personalize-runtime")`

Can be used directly:

```python
from mypy_boto3_personalize_runtime.client import PersonalizeRuntimeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_personalize_runtime.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("personalize-runtime").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("personalize-runtime").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.generate_presigned_url)

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

### get_personalized_ranking

Type annotations for `boto3.client("personalize-runtime").get_personalized_ranking` method.

[Client.get_personalized_ranking documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_personalized_ranking)

```python
def get_personalized_ranking(
    self,
    campaignArn: str,
    inputList: List[str],
    userId: str,
    context: Dict[str, str] = None,
    filterArn: str = None,
    filterValues: Dict[str, str] = None
) -> GetPersonalizedRankingResponseTypeDef:
    pass
```

### get_recommendations

Type annotations for `boto3.client("personalize-runtime").get_recommendations` method.

[Client.get_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html#PersonalizeRuntime.Client.get_recommendations)

```python
def get_recommendations(
    self,
    campaignArn: str,
    itemId: str = None,
    userId: str = None,
    numResults: int = None,
    context: Dict[str, str] = None,
    filterArn: str = None,
    filterValues: Dict[str, str] = None
) -> GetRecommendationsResponseTypeDef:
    pass
```