# Literals for boto3 SQS module

> [Index](../index.md) > [SQS](./index.md) > Literals

Auto-generated documentation for [SQS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS)
type annotations stubs module [mypy_boto3_sqs](https://pypi.org/project/mypy-boto3-sqs/).

- [Literals for boto3 SQS module](#literals-for-boto3-sqs-module)
  - [ListDeadLetterSourceQueuesPaginatorName](#listdeadlettersourcequeuespaginatorname)
  - [ListQueuesPaginatorName](#listqueuespaginatorname)
  - [MessageSystemAttributeName](#messagesystemattributename)
  - [MessageSystemAttributeNameForSends](#messagesystemattributenameforsends)
  - [QueueAttributeName](#queueattributename)

## ListDeadLetterSourceQueuesPaginatorName

```python
from mypy_boto3_sqs.literals import ListDeadLetterSourceQueuesPaginatorName
```

Values:

- `list_dead_letter_source_queues`

## ListQueuesPaginatorName

```python
from mypy_boto3_sqs.literals import ListQueuesPaginatorName
```

Values:

- `list_queues`

## MessageSystemAttributeName

```python
from mypy_boto3_sqs.literals import MessageSystemAttributeName
```

Values:

- `ApproximateFirstReceiveTimestamp`
- `ApproximateReceiveCount`
- `AWSTraceHeader`
- `MessageDeduplicationId`
- `MessageGroupId`
- `SenderId`
- `SentTimestamp`
- `SequenceNumber`

## MessageSystemAttributeNameForSends

```python
from mypy_boto3_sqs.literals import MessageSystemAttributeNameForSends
```

Values:

- `AWSTraceHeader`

## QueueAttributeName

```python
from mypy_boto3_sqs.literals import QueueAttributeName
```

Values:

- `All`
- `ApproximateNumberOfMessages`
- `ApproximateNumberOfMessagesDelayed`
- `ApproximateNumberOfMessagesNotVisible`
- `ContentBasedDeduplication`
- `CreatedTimestamp`
- `DeduplicationScope`
- `DelaySeconds`
- `FifoQueue`
- `FifoThroughputLimit`
- `KmsDataKeyReusePeriodSeconds`
- `KmsMasterKeyId`
- `LastModifiedTimestamp`
- `MaximumMessageSize`
- `MessageRetentionPeriod`
- `Policy`
- `QueueArn`
- `ReceiveMessageWaitTimeSeconds`
- `RedrivePolicy`
- `VisibilityTimeout`
