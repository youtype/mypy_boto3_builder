# Literals for boto3 LexRuntimeService module

> [Index](../index.md) > [LexRuntimeService](./index.md) > Literals

Auto-generated documentation for [LexRuntimeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService)
type annotations stubs module [mypy_boto3_lex_runtime](https://pypi.org/project/mypy-boto3-lex-runtime/).

- [Literals for boto3 LexRuntimeService module](#literals-for-boto3-lexruntimeservice-module)
  - [ConfirmationStatus](#confirmationstatus)
  - [ContentType](#contenttype)
  - [DialogActionType](#dialogactiontype)
  - [DialogState](#dialogstate)
  - [FulfillmentState](#fulfillmentstate)
  - [MessageFormatType](#messageformattype)

## ConfirmationStatus

```python
from mypy_boto3_lex_runtime.literals import ConfirmationStatus
```

Values:

- `Confirmed`
- `Denied`
- `None`

## ContentType

```python
from mypy_boto3_lex_runtime.literals import ContentType
```

Values:

- `application/vnd.amazonaws.card.generic`

## DialogActionType

```python
from mypy_boto3_lex_runtime.literals import DialogActionType
```

Values:

- `Close`
- `ConfirmIntent`
- `Delegate`
- `ElicitIntent`
- `ElicitSlot`

## DialogState

```python
from mypy_boto3_lex_runtime.literals import DialogState
```

Values:

- `ConfirmIntent`
- `ElicitIntent`
- `ElicitSlot`
- `Failed`
- `Fulfilled`
- `ReadyForFulfillment`

## FulfillmentState

```python
from mypy_boto3_lex_runtime.literals import FulfillmentState
```

Values:

- `Failed`
- `Fulfilled`
- `ReadyForFulfillment`

## MessageFormatType

```python
from mypy_boto3_lex_runtime.literals import MessageFormatType
```

Values:

- `Composite`
- `CustomPayload`
- `PlainText`
- `SSML`
