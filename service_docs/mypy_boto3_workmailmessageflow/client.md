# WorkMailMessageFlowClient for boto3 WorkMailMessageFlow module

> [Index](../index.md) > [WorkMailMessageFlow](./index.md) > WorkMailMessageFlowClient

Auto-generated documentation for [WorkMailMessageFlow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow)
type annotations stubs module [mypy_boto3_workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow/).

- [WorkMailMessageFlowClient for boto3 WorkMailMessageFlow module](#workmailmessageflowclient-for-boto3-workmailmessageflow-module)
  - [WorkMailMessageFlowClient](#workmailmessageflowclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_raw_message_content](#get_raw_message_content)
    - [put_raw_message_content](#put_raw_message_content)

## WorkMailMessageFlowClient

Type annotations for `boto3.client("workmailmessageflow")`

Can be used directly:

```python
from mypy_boto3_workmailmessageflow.client import WorkMailMessageFlowClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_workmailmessageflow.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidContentLocation`
- `Exceptions.MessageFrozen`
- `Exceptions.MessageRejected`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("workmailmessageflow").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("workmailmessageflow").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.generate_presigned_url)

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

### get_raw_message_content

Type annotations for `boto3.client("workmailmessageflow").get_raw_message_content` method.

[Client.get_raw_message_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.get_raw_message_content)

```python
def get_raw_message_content(
    self,
    messageId: str
) -> GetRawMessageContentResponseTypeDef:
    pass
```

### put_raw_message_content

Type annotations for `boto3.client("workmailmessageflow").put_raw_message_content` method.

[Client.put_raw_message_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html#WorkMailMessageFlow.Client.put_raw_message_content)

```python
def put_raw_message_content(
    self,
    messageId: str,
    content: RawMessageContentTypeDef
) -> Dict[str, Any]:
    pass
```