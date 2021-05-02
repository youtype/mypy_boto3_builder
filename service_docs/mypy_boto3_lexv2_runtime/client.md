# LexRuntimeV2Client for boto3 LexRuntimeV2 module

> [Index](../index.md) > [LexRuntimeV2](./index.md) > LexRuntimeV2Client

Auto-generated documentation for [LexRuntimeV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2)
type annotations stubs module [mypy_boto3_lexv2_runtime](https://pypi.org/project/mypy-boto3-lexv2-runtime/).

- [LexRuntimeV2Client for boto3 LexRuntimeV2 module](#lexruntimev2client-for-boto3-lexruntimev2-module)
  - [LexRuntimeV2Client](#lexruntimev2client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_session](#delete_session)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_session](#get_session)
    - [put_session](#put_session)
    - [recognize_text](#recognize_text)
    - [recognize_utterance](#recognize_utterance)

## LexRuntimeV2Client

Type annotations for `boto3.client("lexv2-runtime")`

Can be used directly:

```python
from mypy_boto3_lexv2_runtime.client import LexRuntimeV2Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lexv2_runtime.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadGatewayException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.DependencyFailedException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("lexv2-runtime").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_session

Type annotations for `boto3.client("lexv2-runtime").delete_session` method.

[Client.delete_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.delete_session)

```python
def delete_session(
    self,
    botId: str,
    botAliasId: str,
    localeId: str,
    sessionId: str
) -> DeleteSessionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lexv2-runtime").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.generate_presigned_url)

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

### get_session

Type annotations for `boto3.client("lexv2-runtime").get_session` method.

[Client.get_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.get_session)

```python
def get_session(
    self,
    botId: str,
    botAliasId: str,
    localeId: str,
    sessionId: str
) -> GetSessionResponseTypeDef:
    pass
```

### put_session

Type annotations for `boto3.client("lexv2-runtime").put_session` method.

[Client.put_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.put_session)

```python
def put_session(
    self,
    botId: str,
    botAliasId: str,
    localeId: str,
    sessionId: str,
    sessionState: "SessionStateTypeDef",
    messages: List["MessageTypeDef"] = None,
    requestAttributes: Dict[str, str] = None,
    responseContentType: str = None
) -> PutSessionResponseTypeDef:
    pass
```

### recognize_text

Type annotations for `boto3.client("lexv2-runtime").recognize_text` method.

[Client.recognize_text documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.recognize_text)

```python
def recognize_text(
    self,
    botId: str,
    botAliasId: str,
    localeId: str,
    sessionId: str,
    text: str,
    sessionState: "SessionStateTypeDef" = None,
    requestAttributes: Dict[str, str] = None
) -> RecognizeTextResponseTypeDef:
    pass
```

### recognize_utterance

Type annotations for `boto3.client("lexv2-runtime").recognize_utterance` method.

[Client.recognize_utterance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.recognize_utterance)

```python
def recognize_utterance(
    self,
    botId: str,
    botAliasId: str,
    localeId: str,
    sessionId: str,
    requestContentType: str,
    sessionState: str = None,
    requestAttributes: str = None,
    responseContentType: str = None,
    inputStream: Union[bytes, IO[bytes]] = None
) -> RecognizeUtteranceResponseTypeDef:
    pass
```