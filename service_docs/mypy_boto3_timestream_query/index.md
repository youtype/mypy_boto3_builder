# Type annotations for boto3 TimestreamQuery module

> [Index](../index.md) > TimestreamQuery

Auto-generated documentation for [TimestreamQuery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html#TimestreamQuery)
type annotations stubs module [mypy_boto3_timestream_query](https://pypi.org/project/mypy-boto3-timestream-query/).

```bash
pip install mypy-boto3-timestream-query
```

- [Type annotations for boto3 TimestreamQuery module](#type-annotations-for-boto3-timestreamquery-module)
  - [TimestreamQueryClient](#timestreamqueryclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## TimestreamQueryClient

Type annotations for  `boto3.client("timestream-query")` as [TimestreamQueryClient](./client.md)

Can be used directly:

```python
from mypy_boto3_timestream_query.client import TimestreamQueryClient
```


TimestreamQueryClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_query](./client.md#cancel-query)
- [describe_endpoints](./client.md#describe-endpoints)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [query](./client.md#query)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidEndpointException](./client.md#invalidendpointexception)
- [QueryExecutionException](./client.md#queryexecutionexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("timestream-query").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_timestream_query.paginators import QueryPaginator, ...
```

- [QueryPaginator](./paginators.md#querypaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_timestream_query.literals import QueryPaginatorName, ...
```

- [QueryPaginatorName](./literals.md#querypaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_timestream_query.type_defs import CancelQueryResponseTypeDef, ...
```

- [CancelQueryResponseTypeDef](./type_defs.md#cancelqueryresponsetypedef)
- [ColumnInfoTypeDef](./type_defs.md#columninfotypedef)
- [DatumTypeDef](./type_defs.md#datumtypedef)
- [DescribeEndpointsResponseTypeDef](./type_defs.md#describeendpointsresponsetypedef)
- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [QueryResponseTypeDef](./type_defs.md#queryresponsetypedef)
- [QueryStatusTypeDef](./type_defs.md#querystatustypedef)
- [RowTypeDef](./type_defs.md#rowtypedef)
- [TimeSeriesDataPointTypeDef](./type_defs.md#timeseriesdatapointtypedef)
- [TypeTypeDef](./type_defs.md#typetypedef)
