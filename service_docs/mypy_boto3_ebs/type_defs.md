# Structures for boto3 EBS module

> [Index](../index.md) > [EBS](./index.md) > Structures

Auto-generated documentation for [EBS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS)
type annotations stubs module [mypy_boto3_ebs](https://pypi.org/project/mypy-boto3-ebs/).

- [Structures for boto3 EBS module](#structures-for-boto3-ebs-module)
  - [BlockTypeDef](#blocktypedef)
  - [ChangedBlockTypeDef](#changedblocktypedef)
  - [CompleteSnapshotResponseTypeDef](#completesnapshotresponsetypedef)
  - [GetSnapshotBlockResponseTypeDef](#getsnapshotblockresponsetypedef)
  - [ListChangedBlocksResponseTypeDef](#listchangedblocksresponsetypedef)
  - [ListSnapshotBlocksResponseTypeDef](#listsnapshotblocksresponsetypedef)
  - [PutSnapshotBlockResponseTypeDef](#putsnapshotblockresponsetypedef)
  - [StartSnapshotResponseTypeDef](#startsnapshotresponsetypedef)
  - [TagTypeDef](#tagtypedef)

## BlockTypeDef

```python
from mypy_boto3_ebs.type_defs import BlockTypeDef
```




Optional fields:
- `BlockIndex`: `int`
- `BlockToken`: `str`


## ChangedBlockTypeDef

```python
from mypy_boto3_ebs.type_defs import ChangedBlockTypeDef
```




Optional fields:
- `BlockIndex`: `int`
- `FirstBlockToken`: `str`
- `SecondBlockToken`: `str`


## CompleteSnapshotResponseTypeDef

```python
from mypy_boto3_ebs.type_defs import CompleteSnapshotResponseTypeDef
```




Optional fields:
- `Status`: `Status`


## GetSnapshotBlockResponseTypeDef

```python
from mypy_boto3_ebs.type_defs import GetSnapshotBlockResponseTypeDef
```




Optional fields:
- `DataLength`: `int`
- `BlockData`: `StreamingBody`
- `Checksum`: `str`
- `ChecksumAlgorithm`: `Literal['SHA256']`


## ListChangedBlocksResponseTypeDef

```python
from mypy_boto3_ebs.type_defs import ListChangedBlocksResponseTypeDef
```




Optional fields:
- `ChangedBlocks`: `List["ChangedBlockTypeDef"]`
- `ExpiryTime`: `datetime`
- `VolumeSize`: `int`
- `BlockSize`: `int`
- `NextToken`: `str`


## ListSnapshotBlocksResponseTypeDef

```python
from mypy_boto3_ebs.type_defs import ListSnapshotBlocksResponseTypeDef
```




Optional fields:
- `Blocks`: `List["BlockTypeDef"]`
- `ExpiryTime`: `datetime`
- `VolumeSize`: `int`
- `BlockSize`: `int`
- `NextToken`: `str`


## PutSnapshotBlockResponseTypeDef

```python
from mypy_boto3_ebs.type_defs import PutSnapshotBlockResponseTypeDef
```




Optional fields:
- `Checksum`: `str`
- `ChecksumAlgorithm`: `Literal['SHA256']`


## StartSnapshotResponseTypeDef

```python
from mypy_boto3_ebs.type_defs import StartSnapshotResponseTypeDef
```




Optional fields:
- `Description`: `str`
- `SnapshotId`: `str`
- `OwnerId`: `str`
- `Status`: `Status`
- `StartTime`: `datetime`
- `VolumeSize`: `int`
- `BlockSize`: `int`
- `Tags`: `List["TagTypeDef"]`
- `ParentSnapshotId`: `str`
- `KmsKeyArn`: `str`


## TagTypeDef

```python
from mypy_boto3_ebs.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`

