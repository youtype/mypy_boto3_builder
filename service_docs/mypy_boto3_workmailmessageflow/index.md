# Type annotations for boto3 WorkMailMessageFlow module

> [Index](../index.md) > WorkMailMessageFlow

Auto-generated documentation for [WorkMailMessageFlow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow)
type annotations stubs module [mypy_boto3_workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow/).

```bash
pip install mypy-boto3-workmailmessageflow
```

- [Type annotations for boto3 WorkMailMessageFlow module](#type-annotations-for-boto3-workmailmessageflow-module)
  - [WorkMailMessageFlowClient](#workmailmessageflowclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## WorkMailMessageFlowClient

Type annotations for  `boto3.client("workmailmessageflow")` as [WorkMailMessageFlowClient](./client.md)

Can be used directly:

```python
from mypy_boto3_workmailmessageflow.client import WorkMailMessageFlowClient
```


WorkMailMessageFlowClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_raw_message_content](./client.md#get-raw-message-content)
- [put_raw_message_content](./client.md#put-raw-message-content)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidContentLocation](./client.md#invalidcontentlocation)
- [MessageFrozen](./client.md#messagefrozen)
- [MessageRejected](./client.md#messagerejected)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentResponseTypeDef, ...
```

- [GetRawMessageContentResponseTypeDef](./type_defs.md#getrawmessagecontentresponsetypedef)
- [RawMessageContentTypeDef](./type_defs.md#rawmessagecontenttypedef)
- [S3ReferenceTypeDef](./type_defs.md#s3referencetypedef)
