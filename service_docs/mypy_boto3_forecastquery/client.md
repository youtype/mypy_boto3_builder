# ForecastQueryServiceClient for boto3 ForecastQueryService module

> [Index](../index.md) > [ForecastQueryService](./index.md) > ForecastQueryServiceClient

Auto-generated documentation for [ForecastQueryService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html#ForecastQueryService)
type annotations stubs module [mypy_boto3_forecastquery](https://pypi.org/project/mypy-boto3-forecastquery/).

- [ForecastQueryServiceClient for boto3 ForecastQueryService module](#forecastqueryserviceclient-for-boto3-forecastqueryservice-module)
  - [ForecastQueryServiceClient](#forecastqueryserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [query_forecast](#query_forecast)

## ForecastQueryServiceClient

Type annotations for `boto3.client("forecastquery")`

Can be used directly:

```python
from mypy_boto3_forecastquery.client import ForecastQueryServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_forecastquery.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("forecastquery").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html#ForecastQueryService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("forecastquery").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html#ForecastQueryService.Client.generate_presigned_url)

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

### query_forecast

Type annotations for `boto3.client("forecastquery").query_forecast` method.

[Client.query_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html#ForecastQueryService.Client.query_forecast)

```python
def query_forecast(
    self,
    ForecastArn: str,
    Filters: Dict[str, str],
    StartDate: str = None,
    EndDate: str = None,
    NextToken: str = None
) -> QueryForecastResponseTypeDef:
    pass
```



