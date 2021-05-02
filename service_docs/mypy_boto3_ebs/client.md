# EBSClient for boto3 EBS module

> [Index](../index.md) > [EBS](./index.md) > EBSClient

Auto-generated documentation for [EBS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS)
type annotations stubs module [mypy_boto3_ebs](https://pypi.org/project/mypy-boto3-ebs/).

- [EBSClient for boto3 EBS module](#ebsclient-for-boto3-ebs-module)
  - [EBSClient](#ebsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [complete_snapshot](#complete_snapshot)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_snapshot_block](#get_snapshot_block)
    - [list_changed_blocks](#list_changed_blocks)
    - [list_snapshot_blocks](#list_snapshot_blocks)
    - [put_snapshot_block](#put_snapshot_block)
    - [start_snapshot](#start_snapshot)

## EBSClient

Type annotations for `boto3.client("ebs")`

Can be used directly:

```python
from mypy_boto3_ebs.client import EBSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ebs.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentLimitExceededException`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.RequestThrottledException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("ebs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_snapshot

Type annotations for `boto3.client("ebs").complete_snapshot` method.

[Client.complete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.complete_snapshot)

```python
def complete_snapshot(
    self,
    SnapshotId: str,
    ChangedBlocksCount: int,
    Checksum: str = None,
    ChecksumAlgorithm: Literal['SHA256'] = None,
    ChecksumAggregationMethod: Literal['LINEAR'] = None
) -> CompleteSnapshotResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ebs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.generate_presigned_url)

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

### get_snapshot_block

Type annotations for `boto3.client("ebs").get_snapshot_block` method.

[Client.get_snapshot_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.get_snapshot_block)

```python
def get_snapshot_block(
    self,
    SnapshotId: str,
    BlockIndex: int,
    BlockToken: str
) -> GetSnapshotBlockResponseTypeDef:
    pass
```

### list_changed_blocks

Type annotations for `boto3.client("ebs").list_changed_blocks` method.

[Client.list_changed_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.list_changed_blocks)

```python
def list_changed_blocks(
    self,
    SecondSnapshotId: str,
    FirstSnapshotId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    StartingBlockIndex: int = None
) -> ListChangedBlocksResponseTypeDef:
    pass
```

### list_snapshot_blocks

Type annotations for `boto3.client("ebs").list_snapshot_blocks` method.

[Client.list_snapshot_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.list_snapshot_blocks)

```python
def list_snapshot_blocks(
    self,
    SnapshotId: str,
    NextToken: str = None,
    MaxResults: int = None,
    StartingBlockIndex: int = None
) -> ListSnapshotBlocksResponseTypeDef:
    pass
```

### put_snapshot_block

Type annotations for `boto3.client("ebs").put_snapshot_block` method.

[Client.put_snapshot_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.put_snapshot_block)

```python
def put_snapshot_block(
    self,
    SnapshotId: str,
    BlockIndex: int,
    BlockData: Union[bytes, IO[bytes]],
    DataLength: int,
    Checksum: str,
    ChecksumAlgorithm: Literal['SHA256'],
    Progress: int = None
) -> PutSnapshotBlockResponseTypeDef:
    pass
```

### start_snapshot

Type annotations for `boto3.client("ebs").start_snapshot` method.

[Client.start_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client.start_snapshot)

```python
def start_snapshot(
    self,
    VolumeSize: int,
    ParentSnapshotId: str = None,
    Tags: List["TagTypeDef"] = None,
    Description: str = None,
    ClientToken: str = None,
    Encrypted: bool = None,
    KmsKeyArn: str = None,
    Timeout: int = None
) -> StartSnapshotResponseTypeDef:
    pass
```



