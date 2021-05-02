# Structures for boto3 WorkMailMessageFlow module

> [Index](../index.md) > [WorkMailMessageFlow](./index.md) > Structures

Auto-generated documentation for [WorkMailMessageFlow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow)
type annotations stubs module [mypy_boto3_workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow/).

- [Structures for boto3 WorkMailMessageFlow module](#structures-for-boto3-workmailmessageflow-module)
  - [S3ReferenceTypeDef](#s3referencetypedef)
  - [GetRawMessageContentResponseTypeDef](#getrawmessagecontentresponsetypedef)
  - [RawMessageContentTypeDef](#rawmessagecontenttypedef)

## S3ReferenceTypeDef

```python
from mypy_boto3_workmailmessageflow.type_defs import S3ReferenceTypeDef
```


Required fields:
- `bucket`: `str`
- `key`: `str`



Optional fields:
- `objectVersion`: `str`


## GetRawMessageContentResponseTypeDef

```python
from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentResponseTypeDef
```


Required fields:
- `messageContent`: `StreamingBody`




## RawMessageContentTypeDef

```python
from mypy_boto3_workmailmessageflow.type_defs import RawMessageContentTypeDef
```


Required fields:
- `s3Reference`: `"S3ReferenceTypeDef"`



