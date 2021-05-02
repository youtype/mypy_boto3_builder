# QLDBClient for boto3 QLDB module

> [Index](../index.md) > [QLDB](./index.md) > QLDBClient

Auto-generated documentation for [QLDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB)
type annotations stubs module [mypy_boto3_qldb](https://pypi.org/project/mypy-boto3-qldb/).

- [QLDBClient for boto3 QLDB module](#qldbclient-for-boto3-qldb-module)
  - [QLDBClient](#qldbclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_journal_kinesis_stream](#cancel_journal_kinesis_stream)
    - [create_ledger](#create_ledger)
    - [delete_ledger](#delete_ledger)
    - [describe_journal_kinesis_stream](#describe_journal_kinesis_stream)
    - [describe_journal_s3_export](#describe_journal_s3_export)
    - [describe_ledger](#describe_ledger)
    - [export_journal_to_s3](#export_journal_to_s3)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_block](#get_block)
    - [get_digest](#get_digest)
    - [get_revision](#get_revision)
    - [list_journal_kinesis_streams_for_ledger](#list_journal_kinesis_streams_for_ledger)
    - [list_journal_s3_exports](#list_journal_s3_exports)
    - [list_journal_s3_exports_for_ledger](#list_journal_s3_exports_for_ledger)
    - [list_ledgers](#list_ledgers)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [stream_journal_to_kinesis](#stream_journal_to_kinesis)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_ledger](#update_ledger)

## QLDBClient

Type annotations for `boto3.client("qldb")`

Can be used directly:

```python
from mypy_boto3_qldb.client import QLDBClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_qldb.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidParameterException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourcePreconditionNotMetException`


## Methods


### can_paginate

Type annotations for `boto3.client("qldb").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_journal_kinesis_stream

Type annotations for `boto3.client("qldb").cancel_journal_kinesis_stream` method.

[Client.cancel_journal_kinesis_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.cancel_journal_kinesis_stream)

```python
def cancel_journal_kinesis_stream(
    self,
    LedgerName: str,
    StreamId: str
) -> CancelJournalKinesisStreamResponseTypeDef:
    pass
```

### create_ledger

Type annotations for `boto3.client("qldb").create_ledger` method.

[Client.create_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.create_ledger)

```python
def create_ledger(
    self,
    Name: str,
    PermissionsMode: PermissionsMode,
    Tags: Dict[str, str] = None,
    DeletionProtection: bool = None
) -> CreateLedgerResponseTypeDef:
    pass
```

### delete_ledger

Type annotations for `boto3.client("qldb").delete_ledger` method.

[Client.delete_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.delete_ledger)

```python
def delete_ledger(
    self,
    Name: str
) -> None:
    pass
```

### describe_journal_kinesis_stream

Type annotations for `boto3.client("qldb").describe_journal_kinesis_stream` method.

[Client.describe_journal_kinesis_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.describe_journal_kinesis_stream)

```python
def describe_journal_kinesis_stream(
    self,
    LedgerName: str,
    StreamId: str
) -> DescribeJournalKinesisStreamResponseTypeDef:
    pass
```

### describe_journal_s3_export

Type annotations for `boto3.client("qldb").describe_journal_s3_export` method.

[Client.describe_journal_s3_export documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.describe_journal_s3_export)

```python
def describe_journal_s3_export(
    self,
    Name: str,
    ExportId: str
) -> DescribeJournalS3ExportResponseTypeDef:
    pass
```

### describe_ledger

Type annotations for `boto3.client("qldb").describe_ledger` method.

[Client.describe_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.describe_ledger)

```python
def describe_ledger(
    self,
    Name: str
) -> DescribeLedgerResponseTypeDef:
    pass
```

### export_journal_to_s3

Type annotations for `boto3.client("qldb").export_journal_to_s3` method.

[Client.export_journal_to_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.export_journal_to_s3)

```python
def export_journal_to_s3(
    self,
    Name: str,
    InclusiveStartTime: datetime,
    ExclusiveEndTime: datetime,
    S3ExportConfiguration: "S3ExportConfigurationTypeDef",
    RoleArn: str
) -> ExportJournalToS3ResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("qldb").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.generate_presigned_url)

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

### get_block

Type annotations for `boto3.client("qldb").get_block` method.

[Client.get_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.get_block)

```python
def get_block(
    self,
    Name: str,
    BlockAddress: "ValueHolderTypeDef",
    DigestTipAddress: "ValueHolderTypeDef" = None
) -> GetBlockResponseTypeDef:
    pass
```

### get_digest

Type annotations for `boto3.client("qldb").get_digest` method.

[Client.get_digest documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.get_digest)

```python
def get_digest(
    self,
    Name: str
) -> GetDigestResponseTypeDef:
    pass
```

### get_revision

Type annotations for `boto3.client("qldb").get_revision` method.

[Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.get_revision)

```python
def get_revision(
    self,
    Name: str,
    BlockAddress: "ValueHolderTypeDef",
    DocumentId: str,
    DigestTipAddress: "ValueHolderTypeDef" = None
) -> GetRevisionResponseTypeDef:
    pass
```

### list_journal_kinesis_streams_for_ledger

Type annotations for `boto3.client("qldb").list_journal_kinesis_streams_for_ledger` method.

[Client.list_journal_kinesis_streams_for_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.list_journal_kinesis_streams_for_ledger)

```python
def list_journal_kinesis_streams_for_ledger(
    self,
    LedgerName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListJournalKinesisStreamsForLedgerResponseTypeDef:
    pass
```

### list_journal_s3_exports

Type annotations for `boto3.client("qldb").list_journal_s3_exports` method.

[Client.list_journal_s3_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports)

```python
def list_journal_s3_exports(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListJournalS3ExportsResponseTypeDef:
    pass
```

### list_journal_s3_exports_for_ledger

Type annotations for `boto3.client("qldb").list_journal_s3_exports_for_ledger` method.

[Client.list_journal_s3_exports_for_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.list_journal_s3_exports_for_ledger)

```python
def list_journal_s3_exports_for_ledger(
    self,
    Name: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListJournalS3ExportsForLedgerResponseTypeDef:
    pass
```

### list_ledgers

Type annotations for `boto3.client("qldb").list_ledgers` method.

[Client.list_ledgers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.list_ledgers)

```python
def list_ledgers(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListLedgersResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("qldb").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### stream_journal_to_kinesis

Type annotations for `boto3.client("qldb").stream_journal_to_kinesis` method.

[Client.stream_journal_to_kinesis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.stream_journal_to_kinesis)

```python
def stream_journal_to_kinesis(
    self,
    LedgerName: str,
    RoleArn: str,
    InclusiveStartTime: datetime,
    KinesisConfiguration: "KinesisConfigurationTypeDef",
    StreamName: str,
    Tags: Dict[str, str] = None,
    ExclusiveEndTime: datetime = None
) -> StreamJournalToKinesisResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("qldb").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("qldb").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_ledger

Type annotations for `boto3.client("qldb").update_ledger` method.

[Client.update_ledger documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html#QLDB.Client.update_ledger)

```python
def update_ledger(
    self,
    Name: str,
    DeletionProtection: bool = None
) -> UpdateLedgerResponseTypeDef:
    pass
```