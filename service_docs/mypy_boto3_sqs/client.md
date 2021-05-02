# SQSClient for boto3 SQS module

> [Index](../index.md) > [SQS](./index.md) > SQSClient

Auto-generated documentation for [SQS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS)
type annotations stubs module [mypy_boto3_sqs](https://pypi.org/project/mypy-boto3-sqs/).

- [SQSClient for boto3 SQS module](#sqsclient-for-boto3-sqs-module)
  - [SQSClient](#sqsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_permission](#add_permission)
    - [can_paginate](#can_paginate)
    - [change_message_visibility](#change_message_visibility)
    - [change_message_visibility_batch](#change_message_visibility_batch)
    - [create_queue](#create_queue)
    - [delete_message](#delete_message)
    - [delete_message_batch](#delete_message_batch)
    - [delete_queue](#delete_queue)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_queue_attributes](#get_queue_attributes)
    - [get_queue_url](#get_queue_url)
    - [list_dead_letter_source_queues](#list_dead_letter_source_queues)
    - [list_queue_tags](#list_queue_tags)
    - [list_queues](#list_queues)
    - [purge_queue](#purge_queue)
    - [receive_message](#receive_message)
    - [remove_permission](#remove_permission)
    - [send_message](#send_message)
    - [send_message_batch](#send_message_batch)
    - [set_queue_attributes](#set_queue_attributes)
    - [tag_queue](#tag_queue)
    - [untag_queue](#untag_queue)
    - [get_paginator](#get_paginator)

## SQSClient

Type annotations for `boto3.client("sqs")`

Can be used directly:

```python
from mypy_boto3_sqs.client import SQSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sqs.client import Exceptions

def handle_error(exc: Exceptions.BatchEntryIdsNotDistinct) -> None:
    ...
```


Exceptions:

- `Exceptions.BatchEntryIdsNotDistinct`
- `Exceptions.BatchRequestTooLong`
- `Exceptions.ClientError`
- `Exceptions.EmptyBatchRequest`
- `Exceptions.InvalidAttributeName`
- `Exceptions.InvalidBatchEntryId`
- `Exceptions.InvalidIdFormat`
- `Exceptions.InvalidMessageContents`
- `Exceptions.MessageNotInflight`
- `Exceptions.OverLimit`
- `Exceptions.PurgeQueueInProgress`
- `Exceptions.QueueDeletedRecently`
- `Exceptions.QueueDoesNotExist`
- `Exceptions.QueueNameExists`
- `Exceptions.ReceiptHandleIsInvalid`
- `Exceptions.TooManyEntriesInBatchRequest`
- `Exceptions.UnsupportedOperation`


## Methods


### add_permission

Type annotations for `boto3.client("sqs").add_permission` method.

[Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.add_permission)

```python
def add_permission(
    self,
    QueueUrl: str,
    Label: str,
    AWSAccountIds: List[str],
    Actions: List[str]
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("sqs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### change_message_visibility

Type annotations for `boto3.client("sqs").change_message_visibility` method.

[Client.change_message_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.change_message_visibility)

```python
def change_message_visibility(
    self,
    QueueUrl: str,
    ReceiptHandle: str,
    VisibilityTimeout: int
) -> None:
    pass
```

### change_message_visibility_batch

Type annotations for `boto3.client("sqs").change_message_visibility_batch` method.

[Client.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)

```python
def change_message_visibility_batch(
    self,
    QueueUrl: str,
    Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
) -> ChangeMessageVisibilityBatchResultTypeDef:
    pass
```

### create_queue

Type annotations for `boto3.client("sqs").create_queue` method.

[Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue)

```python
def create_queue(
    self,
    QueueName: str,
    Attributes: Dict[QueueAttributeName, str] = None,
    tags: Dict[str, str] = None
) -> CreateQueueResultTypeDef:
    pass
```

### delete_message

Type annotations for `boto3.client("sqs").delete_message` method.

[Client.delete_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message)

```python
def delete_message(
    self,
    QueueUrl: str,
    ReceiptHandle: str
) -> None:
    pass
```

### delete_message_batch

Type annotations for `boto3.client("sqs").delete_message_batch` method.

[Client.delete_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message_batch)

```python
def delete_message_batch(
    self,
    QueueUrl: str,
    Entries: List[DeleteMessageBatchRequestEntryTypeDef]
) -> DeleteMessageBatchResultTypeDef:
    pass
```

### delete_queue

Type annotations for `boto3.client("sqs").delete_queue` method.

[Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_queue)

```python
def delete_queue(
    self,
    QueueUrl: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sqs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.generate_presigned_url)

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

### get_queue_attributes

Type annotations for `boto3.client("sqs").get_queue_attributes` method.

[Client.get_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_queue_attributes)

```python
def get_queue_attributes(
    self,
    QueueUrl: str,
    AttributeNames: List[QueueAttributeName] = None
) -> GetQueueAttributesResultTypeDef:
    pass
```

### get_queue_url

Type annotations for `boto3.client("sqs").get_queue_url` method.

[Client.get_queue_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_queue_url)

```python
def get_queue_url(
    self,
    QueueName: str,
    QueueOwnerAWSAccountId: str = None
) -> GetQueueUrlResultTypeDef:
    pass
```

### list_dead_letter_source_queues

Type annotations for `boto3.client("sqs").list_dead_letter_source_queues` method.

[Client.list_dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)

```python
def list_dead_letter_source_queues(
    self,
    QueueUrl: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDeadLetterSourceQueuesResultTypeDef:
    pass
```

### list_queue_tags

Type annotations for `boto3.client("sqs").list_queue_tags` method.

[Client.list_queue_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queue_tags)

```python
def list_queue_tags(
    self,
    QueueUrl: str
) -> ListQueueTagsResultTypeDef:
    pass
```

### list_queues

Type annotations for `boto3.client("sqs").list_queues` method.

[Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queues)

```python
def list_queues(
    self,
    QueueNamePrefix: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListQueuesResultTypeDef:
    pass
```

### purge_queue

Type annotations for `boto3.client("sqs").purge_queue` method.

[Client.purge_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.purge_queue)

```python
def purge_queue(
    self,
    QueueUrl: str
) -> None:
    pass
```

### receive_message

Type annotations for `boto3.client("sqs").receive_message` method.

[Client.receive_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message)

```python
def receive_message(
    self,
    QueueUrl: str,
    AttributeNames: List[QueueAttributeName] = None,
    MessageAttributeNames: List[str] = None,
    MaxNumberOfMessages: int = None,
    VisibilityTimeout: int = None,
    WaitTimeSeconds: int = None,
    ReceiveRequestAttemptId: str = None
) -> ReceiveMessageResultTypeDef:
    pass
```

### remove_permission

Type annotations for `boto3.client("sqs").remove_permission` method.

[Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.remove_permission)

```python
def remove_permission(
    self,
    QueueUrl: str,
    Label: str
) -> None:
    pass
```

### send_message

Type annotations for `boto3.client("sqs").send_message` method.

[Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message)

```python
def send_message(
    self,
    QueueUrl: str,
    MessageBody: str,
    DelaySeconds: int = None,
    MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"] = None,
    MessageSystemAttributes: Dict[Literal['AWSTraceHeader'], "MessageSystemAttributeValueTypeDef"] = None,
    MessageDeduplicationId: str = None,
    MessageGroupId: str = None
) -> SendMessageResultTypeDef:
    pass
```

### send_message_batch

Type annotations for `boto3.client("sqs").send_message_batch` method.

[Client.send_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message_batch)

```python
def send_message_batch(
    self,
    QueueUrl: str,
    Entries: List[SendMessageBatchRequestEntryTypeDef]
) -> SendMessageBatchResultTypeDef:
    pass
```

### set_queue_attributes

Type annotations for `boto3.client("sqs").set_queue_attributes` method.

[Client.set_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes)

```python
def set_queue_attributes(
    self,
    QueueUrl: str,
    Attributes: Dict[QueueAttributeName, str]
) -> None:
    pass
```

### tag_queue

Type annotations for `boto3.client("sqs").tag_queue` method.

[Client.tag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.tag_queue)

```python
def tag_queue(
    self,
    QueueUrl: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_queue

Type annotations for `boto3.client("sqs").untag_queue` method.

[Client.untag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.untag_queue)

```python
def untag_queue(
    self,
    QueueUrl: str,
    TagKeys: List[str]
) -> None:
    pass
```



### get_paginator

Type annotations for `boto3.client("sqs").get_paginator` method with overloads.

- `client.get_paginator("list_dead_letter_source_queues")` -> [ListDeadLetterSourceQueuesPaginator](./paginators.md#listdeadlettersourcequeuespaginator)
- `client.get_paginator("list_queues")` -> [ListQueuesPaginator](./paginators.md#listqueuespaginator)


