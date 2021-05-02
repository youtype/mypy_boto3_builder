# Structures for boto3 SQS module

> [Index](../index.md) > [SQS](./index.md) > Structures

Auto-generated documentation for [SQS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS)
type annotations stubs module [mypy_boto3_sqs](https://pypi.org/project/mypy-boto3-sqs/).

- [Structures for boto3 SQS module](#structures-for-boto3-sqs-module)
  - [BatchResultErrorEntryTypeDef](#batchresulterrorentrytypedef)
  - [ChangeMessageVisibilityBatchResultEntryTypeDef](#changemessagevisibilitybatchresultentrytypedef)
  - [DeleteMessageBatchResultEntryTypeDef](#deletemessagebatchresultentrytypedef)
  - [MessageAttributeValueTypeDef](#messageattributevaluetypedef)
  - [MessageSystemAttributeValueTypeDef](#messagesystemattributevaluetypedef)
  - [MessageTypeDef](#messagetypedef)
  - [SendMessageBatchResultEntryTypeDef](#sendmessagebatchresultentrytypedef)
  - [ChangeMessageVisibilityBatchRequestEntryTypeDef](#changemessagevisibilitybatchrequestentrytypedef)
  - [ChangeMessageVisibilityBatchResultTypeDef](#changemessagevisibilitybatchresulttypedef)
  - [CreateQueueResultTypeDef](#createqueueresulttypedef)
  - [DeleteMessageBatchRequestEntryTypeDef](#deletemessagebatchrequestentrytypedef)
  - [DeleteMessageBatchResultTypeDef](#deletemessagebatchresulttypedef)
  - [GetQueueAttributesResultTypeDef](#getqueueattributesresulttypedef)
  - [GetQueueUrlResultTypeDef](#getqueueurlresulttypedef)
  - [ListDeadLetterSourceQueuesResultTypeDef](#listdeadlettersourcequeuesresulttypedef)
  - [ListQueueTagsResultTypeDef](#listqueuetagsresulttypedef)
  - [ListQueuesResultTypeDef](#listqueuesresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ReceiveMessageResultTypeDef](#receivemessageresulttypedef)
  - [SendMessageBatchRequestEntryTypeDef](#sendmessagebatchrequestentrytypedef)
  - [SendMessageBatchResultTypeDef](#sendmessagebatchresulttypedef)
  - [SendMessageResultTypeDef](#sendmessageresulttypedef)

## BatchResultErrorEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import BatchResultErrorEntryTypeDef
```


Required fields:
- `Id`: `str`
- `SenderFault`: `bool`
- `Code`: `str`



Optional fields:
- `Message`: `str`


## ChangeMessageVisibilityBatchResultEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import ChangeMessageVisibilityBatchResultEntryTypeDef
```


Required fields:
- `Id`: `str`




## DeleteMessageBatchResultEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import DeleteMessageBatchResultEntryTypeDef
```


Required fields:
- `Id`: `str`




## MessageAttributeValueTypeDef

```python
from mypy_boto3_sqs.type_defs import MessageAttributeValueTypeDef
```


Required fields:
- `DataType`: `str`



Optional fields:
- `StringValue`: `str`
- `BinaryValue`: `Union[bytes, IO[bytes]]`
- `StringListValues`: `List[str]`
- `BinaryListValues`: `List[Union[bytes, IO[bytes]]]`


## MessageSystemAttributeValueTypeDef

```python
from mypy_boto3_sqs.type_defs import MessageSystemAttributeValueTypeDef
```


Required fields:
- `DataType`: `str`



Optional fields:
- `StringValue`: `str`
- `BinaryValue`: `Union[bytes, IO[bytes]]`
- `StringListValues`: `List[str]`
- `BinaryListValues`: `List[Union[bytes, IO[bytes]]]`


## MessageTypeDef

```python
from mypy_boto3_sqs.type_defs import MessageTypeDef
```




Optional fields:
- `MessageId`: `str`
- `ReceiptHandle`: `str`
- `MD5OfBody`: `str`
- `Body`: `str`
- `Attributes`: `Dict[MessageSystemAttributeName, str]`
- `MD5OfMessageAttributes`: `str`
- `MessageAttributes`: `Dict[str, "MessageAttributeValueTypeDef"]`


## SendMessageBatchResultEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import SendMessageBatchResultEntryTypeDef
```


Required fields:
- `Id`: `str`
- `MessageId`: `str`
- `MD5OfMessageBody`: `str`



Optional fields:
- `MD5OfMessageAttributes`: `str`
- `MD5OfMessageSystemAttributes`: `str`
- `SequenceNumber`: `str`


## ChangeMessageVisibilityBatchRequestEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import ChangeMessageVisibilityBatchRequestEntryTypeDef
```


Required fields:
- `Id`: `str`
- `ReceiptHandle`: `str`



Optional fields:
- `VisibilityTimeout`: `int`


## ChangeMessageVisibilityBatchResultTypeDef

```python
from mypy_boto3_sqs.type_defs import ChangeMessageVisibilityBatchResultTypeDef
```


Required fields:
- `Successful`: `List["ChangeMessageVisibilityBatchResultEntryTypeDef"]`
- `Failed`: `List["BatchResultErrorEntryTypeDef"]`




## CreateQueueResultTypeDef

```python
from mypy_boto3_sqs.type_defs import CreateQueueResultTypeDef
```




Optional fields:
- `QueueUrl`: `str`


## DeleteMessageBatchRequestEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import DeleteMessageBatchRequestEntryTypeDef
```


Required fields:
- `Id`: `str`
- `ReceiptHandle`: `str`




## DeleteMessageBatchResultTypeDef

```python
from mypy_boto3_sqs.type_defs import DeleteMessageBatchResultTypeDef
```


Required fields:
- `Successful`: `List["DeleteMessageBatchResultEntryTypeDef"]`
- `Failed`: `List["BatchResultErrorEntryTypeDef"]`




## GetQueueAttributesResultTypeDef

```python
from mypy_boto3_sqs.type_defs import GetQueueAttributesResultTypeDef
```




Optional fields:
- `Attributes`: `Dict[QueueAttributeName, str]`


## GetQueueUrlResultTypeDef

```python
from mypy_boto3_sqs.type_defs import GetQueueUrlResultTypeDef
```




Optional fields:
- `QueueUrl`: `str`


## ListDeadLetterSourceQueuesResultTypeDef

```python
from mypy_boto3_sqs.type_defs import ListDeadLetterSourceQueuesResultTypeDef
```


Required fields:
- `queueUrls`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListQueueTagsResultTypeDef

```python
from mypy_boto3_sqs.type_defs import ListQueueTagsResultTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListQueuesResultTypeDef

```python
from mypy_boto3_sqs.type_defs import ListQueuesResultTypeDef
```




Optional fields:
- `QueueUrls`: `List[str]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_sqs.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ReceiveMessageResultTypeDef

```python
from mypy_boto3_sqs.type_defs import ReceiveMessageResultTypeDef
```




Optional fields:
- `Messages`: `List["MessageTypeDef"]`


## SendMessageBatchRequestEntryTypeDef

```python
from mypy_boto3_sqs.type_defs import SendMessageBatchRequestEntryTypeDef
```


Required fields:
- `Id`: `str`
- `MessageBody`: `str`



Optional fields:
- `DelaySeconds`: `int`
- `MessageAttributes`: `Dict[str, "MessageAttributeValueTypeDef"]`
- `MessageSystemAttributes`: `Dict[MessageSystemAttributeNameForSends, "MessageSystemAttributeValueTypeDef"]`
- `MessageDeduplicationId`: `str`
- `MessageGroupId`: `str`


## SendMessageBatchResultTypeDef

```python
from mypy_boto3_sqs.type_defs import SendMessageBatchResultTypeDef
```


Required fields:
- `Successful`: `List["SendMessageBatchResultEntryTypeDef"]`
- `Failed`: `List["BatchResultErrorEntryTypeDef"]`




## SendMessageResultTypeDef

```python
from mypy_boto3_sqs.type_defs import SendMessageResultTypeDef
```




Optional fields:
- `MD5OfMessageBody`: `str`
- `MD5OfMessageAttributes`: `str`
- `MD5OfMessageSystemAttributes`: `str`
- `MessageId`: `str`
- `SequenceNumber`: `str`

