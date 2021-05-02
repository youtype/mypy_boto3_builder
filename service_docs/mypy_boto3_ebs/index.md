# Type annotations for boto3 EBS module

> [Index](../index.md) > EBS

Auto-generated documentation for [EBS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS)
type annotations stubs module [mypy_boto3_ebs](https://pypi.org/project/mypy-boto3-ebs/).

```bash
pip install mypy-boto3-ebs
```

- [Type annotations for boto3 EBS module](#type-annotations-for-boto3-ebs-module)
  - [EBSClient](#ebsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## EBSClient

Type annotations for  `boto3.client("ebs")` as [EBSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ebs.client import EBSClient
```


EBSClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [complete_snapshot](./client.md#complete-snapshot)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_snapshot_block](./client.md#get-snapshot-block)
- [list_changed_blocks](./client.md#list-changed-blocks)
- [list_snapshot_blocks](./client.md#list-snapshot-blocks)
- [put_snapshot_block](./client.md#put-snapshot-block)
- [start_snapshot](./client.md#start-snapshot)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentLimitExceededException](./client.md#concurrentlimitexceededexception)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [RequestThrottledException](./client.md#requestthrottledexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ebs.literals import ChecksumAggregationMethod, ...
```

- [ChecksumAggregationMethod](./literals.md#checksumaggregationmethod)
- [ChecksumAlgorithm](./literals.md#checksumalgorithm)
- [Status](./literals.md#status)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ebs.type_defs import BlockTypeDef, ...
```

- [BlockTypeDef](./type_defs.md#blocktypedef)
- [ChangedBlockTypeDef](./type_defs.md#changedblocktypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CompleteSnapshotResponseTypeDef](./type_defs.md#completesnapshotresponsetypedef)
- [GetSnapshotBlockResponseTypeDef](./type_defs.md#getsnapshotblockresponsetypedef)
- [ListChangedBlocksResponseTypeDef](./type_defs.md#listchangedblocksresponsetypedef)
- [ListSnapshotBlocksResponseTypeDef](./type_defs.md#listsnapshotblocksresponsetypedef)
- [PutSnapshotBlockResponseTypeDef](./type_defs.md#putsnapshotblockresponsetypedef)
- [StartSnapshotResponseTypeDef](./type_defs.md#startsnapshotresponsetypedef)
