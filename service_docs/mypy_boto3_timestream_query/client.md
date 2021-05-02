# TimestreamQueryClient for boto3 TimestreamQuery module

> [Index](../index.md) > [TimestreamQuery](./index.md) > TimestreamQueryClient

Auto-generated documentation for [TimestreamQuery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery)
type annotations stubs module [mypy_boto3_timestream_query](https://pypi.org/project/mypy-boto3-timestream-query/).

- [TimestreamQueryClient for boto3 TimestreamQuery module](#timestreamqueryclient-for-boto3-timestreamquery-module)
  - [TimestreamQueryClient](#timestreamqueryclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_query](#cancel_query)
    - [describe_endpoints](#describe_endpoints)
    - [generate_presigned_url](#generate_presigned_url)
    - [query](#query)
    - [get_paginator](#get_paginator)

## TimestreamQueryClient

Type annotations for `boto3.client("timestream-query")`

Can be used directly:

```python
from mypy_boto3_timestream_query.client import TimestreamQueryClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_timestream_query.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidEndpointException`
- `Exceptions.QueryExecutionException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("timestream-query").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_query

Type annotations for `boto3.client("timestream-query").cancel_query` method.

[Client.cancel_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery.Client.cancel_query)

```python
def cancel_query(
    self,
    QueryId: str
) -> CancelQueryResponseTypeDef:
    pass
```

### describe_endpoints

Type annotations for `boto3.client("timestream-query").describe_endpoints` method.

[Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery.Client.describe_endpoints)

```python
def describe_endpoints(
    self
) -> DescribeEndpointsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("timestream-query").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery.Client.generate_presigned_url)

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

### query

Type annotations for `boto3.client("timestream-query").query` method.

[Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery.Client.query)

```python
def query(
    self,
    QueryString: str,
    ClientToken: str = None,
    NextToken: str = None,
    MaxRows: int = None
) -> QueryResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("timestream-query").get_paginator` method with overloads.

- `client.get_paginator("query")` -> [QueryPaginator](./paginators.md#querypaginator)


