# Type annotations for boto3 SQS module

> [Index](../index.md) > SQS

Auto-generated documentation for [SQS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS)
type annotations stubs module [mypy_boto3_sqs](https://pypi.org/project/mypy-boto3-sqs/).

```bash
pip install mypy-boto3-sqs
```

- [Type annotations for boto3 SQS module](#type-annotations-for-boto3-sqs-module)
  - [SQSClient](#sqsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [SQSServiceResource](#sqsserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SQSClient

Type annotations for  `boto3.client("sqs")` as [SQSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_sqs.client import SQSClient
```


SQSClient [exceptions](./client.md#exceptions)



### Methods
- [add_permission](./client.md#add-permission)
- [can_paginate](./client.md#can-paginate)
- [change_message_visibility](./client.md#change-message-visibility)
- [change_message_visibility_batch](./client.md#change-message-visibility-batch)
- [create_queue](./client.md#create-queue)
- [delete_message](./client.md#delete-message)
- [delete_message_batch](./client.md#delete-message-batch)
- [delete_queue](./client.md#delete-queue)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_queue_attributes](./client.md#get-queue-attributes)
- [get_queue_url](./client.md#get-queue-url)
- [list_dead_letter_source_queues](./client.md#list-dead-letter-source-queues)
- [list_queue_tags](./client.md#list-queue-tags)
- [list_queues](./client.md#list-queues)
- [purge_queue](./client.md#purge-queue)
- [receive_message](./client.md#receive-message)
- [remove_permission](./client.md#remove-permission)
- [send_message](./client.md#send-message)
- [send_message_batch](./client.md#send-message-batch)
- [set_queue_attributes](./client.md#set-queue-attributes)
- [tag_queue](./client.md#tag-queue)
- [untag_queue](./client.md#untag-queue)




### Exceptions
- [BatchEntryIdsNotDistinct](./client.md#batchentryidsnotdistinct)
- [BatchRequestTooLong](./client.md#batchrequesttoolong)
- [ClientError](./client.md#clienterror)
- [EmptyBatchRequest](./client.md#emptybatchrequest)
- [InvalidAttributeName](./client.md#invalidattributename)
- [InvalidBatchEntryId](./client.md#invalidbatchentryid)
- [InvalidIdFormat](./client.md#invalididformat)
- [InvalidMessageContents](./client.md#invalidmessagecontents)
- [MessageNotInflight](./client.md#messagenotinflight)
- [OverLimit](./client.md#overlimit)
- [PurgeQueueInProgress](./client.md#purgequeueinprogress)
- [QueueDeletedRecently](./client.md#queuedeletedrecently)
- [QueueDoesNotExist](./client.md#queuedoesnotexist)
- [QueueNameExists](./client.md#queuenameexists)
- [ReceiptHandleIsInvalid](./client.md#receipthandleisinvalid)
- [TooManyEntriesInBatchRequest](./client.md#toomanyentriesinbatchrequest)
- [UnsupportedOperation](./client.md#unsupportedoperation)




## SQSServiceResource

Type annotations for  `boto3.resource("sqs")` as [SQSServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_sqs.service_resource import SQSServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("sqs").*`.

Can be used directly:

```python
from mypy_boto3_sqs.service_resource import ServiceResourceQueuesCollection, ...
```

- [ServiceResourceQueuesCollection](./service_resource.md#sqsserviceresource.queues)




### Resources

Type annotations for additional resources from `boto3.resource("sqs").*`.

Can be used directly:

```python
from mypy_boto3_sqs.service_resource import Message, ...
```

- [Message](./service_resource.md#message)
- [Queue](./service_resource.md#queue)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("sqs").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_sqs.paginators import ListDeadLetterSourceQueuesPaginator, ...
```

- [ListDeadLetterSourceQueuesPaginator](./paginators.md#listdeadlettersourcequeuespaginator)
- [ListQueuesPaginator](./paginators.md#listqueuespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sqs.literals import ListDeadLetterSourceQueuesPaginatorName, ...
```

- [ListDeadLetterSourceQueuesPaginatorName](./literals.md#listdeadlettersourcequeuespaginatorname)
- [ListQueuesPaginatorName](./literals.md#listqueuespaginatorname)
- [MessageSystemAttributeName](./literals.md#messagesystemattributename)
- [MessageSystemAttributeNameForSends](./literals.md#messagesystemattributenameforsends)
- [QueueAttributeName](./literals.md#queueattributename)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_sqs.type_defs import BatchResultErrorEntryTypeDef, ...
```

- [BatchResultErrorEntryTypeDef](./type_defs.md#batchresulterrorentrytypedef)
- [ChangeMessageVisibilityBatchResultEntryTypeDef](./type_defs.md#changemessagevisibilitybatchresultentrytypedef)
- [DeleteMessageBatchResultEntryTypeDef](./type_defs.md#deletemessagebatchresultentrytypedef)
- [MessageAttributeValueTypeDef](./type_defs.md#messageattributevaluetypedef)
- [MessageSystemAttributeValueTypeDef](./type_defs.md#messagesystemattributevaluetypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [SendMessageBatchResultEntryTypeDef](./type_defs.md#sendmessagebatchresultentrytypedef)
- [ChangeMessageVisibilityBatchRequestEntryTypeDef](./type_defs.md#changemessagevisibilitybatchrequestentrytypedef)
- [ChangeMessageVisibilityBatchResultTypeDef](./type_defs.md#changemessagevisibilitybatchresulttypedef)
- [CreateQueueResultTypeDef](./type_defs.md#createqueueresulttypedef)
- [DeleteMessageBatchRequestEntryTypeDef](./type_defs.md#deletemessagebatchrequestentrytypedef)
- [DeleteMessageBatchResultTypeDef](./type_defs.md#deletemessagebatchresulttypedef)
- [GetQueueAttributesResultTypeDef](./type_defs.md#getqueueattributesresulttypedef)
- [GetQueueUrlResultTypeDef](./type_defs.md#getqueueurlresulttypedef)
- [ListDeadLetterSourceQueuesResultTypeDef](./type_defs.md#listdeadlettersourcequeuesresulttypedef)
- [ListQueueTagsResultTypeDef](./type_defs.md#listqueuetagsresulttypedef)
- [ListQueuesResultTypeDef](./type_defs.md#listqueuesresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ReceiveMessageResultTypeDef](./type_defs.md#receivemessageresulttypedef)
- [SendMessageBatchRequestEntryTypeDef](./type_defs.md#sendmessagebatchrequestentrytypedef)
- [SendMessageBatchResultTypeDef](./type_defs.md#sendmessagebatchresulttypedef)
- [SendMessageResultTypeDef](./type_defs.md#sendmessageresulttypedef)
