# PIClient for boto3 PI module

> [Index](../index.md) > [PI](./index.md) > PIClient

Auto-generated documentation for [PI](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI)
type annotations stubs module [mypy_boto3_pi](https://pypi.org/project/mypy-boto3-pi/).

- [PIClient for boto3 PI module](#piclient-for-boto3-pi-module)
  - [PIClient](#piclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [describe_dimension_keys](#describe_dimension_keys)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_resource_metrics](#get_resource_metrics)

## PIClient

Type annotations for `boto3.client("pi")`

Can be used directly:

```python
from mypy_boto3_pi.client import PIClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_pi.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServiceError`
- `Exceptions.InvalidArgumentException`
- `Exceptions.NotAuthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("pi").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### describe_dimension_keys

Type annotations for `boto3.client("pi").describe_dimension_keys` method.

[Client.describe_dimension_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI.Client.describe_dimension_keys)

```python
def describe_dimension_keys(
    self,
    ServiceType: Literal['RDS'],
    Identifier: str,
    StartTime: datetime,
    EndTime: datetime,
    Metric: str,
    GroupBy: "DimensionGroupTypeDef",
    PeriodInSeconds: int = None,
    PartitionBy: "DimensionGroupTypeDef" = None,
    Filter: Dict[str, str] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeDimensionKeysResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("pi").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI.Client.generate_presigned_url)

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

### get_resource_metrics

Type annotations for `boto3.client("pi").get_resource_metrics` method.

[Client.get_resource_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI.Client.get_resource_metrics)

```python
def get_resource_metrics(
    self,
    ServiceType: Literal['RDS'],
    Identifier: str,
    MetricQueries: List[MetricQueryTypeDef],
    StartTime: datetime,
    EndTime: datetime,
    PeriodInSeconds: int = None,
    MaxResults: int = None,
    NextToken: str = None
) -> GetResourceMetricsResponseTypeDef:
    pass
```



