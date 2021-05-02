# TimestreamWriteClient for boto3 TimestreamWrite module

> [Index](../index.md) > [TimestreamWrite](./index.md) > TimestreamWriteClient

Auto-generated documentation for [TimestreamWrite](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite)
type annotations stubs module [mypy_boto3_timestream_write](https://pypi.org/project/mypy-boto3-timestream-write/).

- [TimestreamWriteClient for boto3 TimestreamWrite module](#timestreamwriteclient-for-boto3-timestreamwrite-module)
  - [TimestreamWriteClient](#timestreamwriteclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_database](#create_database)
    - [create_table](#create_table)
    - [delete_database](#delete_database)
    - [delete_table](#delete_table)
    - [describe_database](#describe_database)
    - [describe_endpoints](#describe_endpoints)
    - [describe_table](#describe_table)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_databases](#list_databases)
    - [list_tables](#list_tables)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_database](#update_database)
    - [update_table](#update_table)
    - [write_records](#write_records)

## TimestreamWriteClient

Type annotations for `boto3.client("timestream-write")`

Can be used directly:

```python
from mypy_boto3_timestream_write.client import TimestreamWriteClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_timestream_write.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidEndpointException`
- `Exceptions.RejectedRecordsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("timestream-write").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_database

Type annotations for `boto3.client("timestream-write").create_database` method.

[Client.create_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.create_database)

```python
def create_database(
    self,
    DatabaseName: str,
    KmsKeyId: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateDatabaseResponseTypeDef:
    pass
```

### create_table

Type annotations for `boto3.client("timestream-write").create_table` method.

[Client.create_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.create_table)

```python
def create_table(
    self,
    DatabaseName: str,
    TableName: str,
    RetentionProperties: "RetentionPropertiesTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateTableResponseTypeDef:
    pass
```

### delete_database

Type annotations for `boto3.client("timestream-write").delete_database` method.

[Client.delete_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.delete_database)

```python
def delete_database(
    self,
    DatabaseName: str
) -> None:
    pass
```

### delete_table

Type annotations for `boto3.client("timestream-write").delete_table` method.

[Client.delete_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.delete_table)

```python
def delete_table(
    self,
    DatabaseName: str,
    TableName: str
) -> None:
    pass
```

### describe_database

Type annotations for `boto3.client("timestream-write").describe_database` method.

[Client.describe_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.describe_database)

```python
def describe_database(
    self,
    DatabaseName: str
) -> DescribeDatabaseResponseTypeDef:
    pass
```

### describe_endpoints

Type annotations for `boto3.client("timestream-write").describe_endpoints` method.

[Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.describe_endpoints)

```python
def describe_endpoints(
    self
) -> DescribeEndpointsResponseTypeDef:
    pass
```

### describe_table

Type annotations for `boto3.client("timestream-write").describe_table` method.

[Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.describe_table)

```python
def describe_table(
    self,
    DatabaseName: str,
    TableName: str
) -> DescribeTableResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("timestream-write").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.generate_presigned_url)

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

### list_databases

Type annotations for `boto3.client("timestream-write").list_databases` method.

[Client.list_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.list_databases)

```python
def list_databases(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDatabasesResponseTypeDef:
    pass
```

### list_tables

Type annotations for `boto3.client("timestream-write").list_tables` method.

[Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.list_tables)

```python
def list_tables(
    self,
    DatabaseName: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTablesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("timestream-write").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("timestream-write").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("timestream-write").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_database

Type annotations for `boto3.client("timestream-write").update_database` method.

[Client.update_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.update_database)

```python
def update_database(
    self,
    DatabaseName: str,
    KmsKeyId: str
) -> UpdateDatabaseResponseTypeDef:
    pass
```

### update_table

Type annotations for `boto3.client("timestream-write").update_table` method.

[Client.update_table documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.update_table)

```python
def update_table(
    self,
    DatabaseName: str,
    TableName: str,
    RetentionProperties: "RetentionPropertiesTypeDef"
) -> UpdateTableResponseTypeDef:
    pass
```

### write_records

Type annotations for `boto3.client("timestream-write").write_records` method.

[Client.write_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html#TimestreamWrite.Client.write_records)

```python
def write_records(
    self,
    DatabaseName: str,
    TableName: str,
    Records: List[RecordTypeDef],
    CommonAttributes: RecordTypeDef = None
) -> None:
    pass
```



