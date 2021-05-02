# LexRuntimeServiceClient for boto3 LexRuntimeService module

> [Index](../index.md) > [LexRuntimeService](./index.md) > LexRuntimeServiceClient

Auto-generated documentation for [LexRuntimeService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService)
type annotations stubs module [mypy_boto3_lex_runtime](https://pypi.org/project/mypy-boto3-lex-runtime/).

- [LexRuntimeServiceClient for boto3 LexRuntimeService module](#lexruntimeserviceclient-for-boto3-lexruntimeservice-module)
  - [LexRuntimeServiceClient](#lexruntimeserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [delete_session](#delete_session)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_session](#get_session)
    - [post_content](#post_content)
    - [post_text](#post_text)
    - [put_session](#put_session)

## LexRuntimeServiceClient

Type annotations for `boto3.client("lex-runtime")`

Can be used directly:

```python
from mypy_boto3_lex_runtime.client import LexRuntimeServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lex_runtime.client import Exceptions

def handle_error(exc: Exceptions.BadGatewayException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadGatewayException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.DependencyFailedException`
- `Exceptions.InternalFailureException`
- `Exceptions.LimitExceededException`
- `Exceptions.LoopDetectedException`
- `Exceptions.NotAcceptableException`
- `Exceptions.NotFoundException`
- `Exceptions.RequestTimeoutException`
- `Exceptions.UnsupportedMediaTypeException`


## Methods


### can_paginate

Type annotations for `boto3.client("lex-runtime").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_session

Type annotations for `boto3.client("lex-runtime").delete_session` method.

[Client.delete_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.delete_session)

```python
def delete_session(
    self,
    botName: str,
    botAlias: str,
    userId: str
) -> DeleteSessionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lex-runtime").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.generate_presigned_url)

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

Type annotations for `boto3.client("lex-runtime").get_session` method.

[Client.get_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.get_session)

```python
def get_session(
    self,
    botName: str,
    botAlias: str,
    userId: str,
    checkpointLabelFilter: str = None
) -> GetSessionResponseTypeDef:
    pass
```

### post_content

Type annotations for `boto3.client("lex-runtime").post_content` method.

[Client.post_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.post_content)

```python
def post_content(
    self,
    botName: str,
    botAlias: str,
    userId: str,
    contentType: str,
    inputStream: Union[bytes, IO[bytes]],
    sessionAttributes: str = None,
    requestAttributes: str = None,
    accept: str = None,
    activeContexts: str = None
) -> PostContentResponseTypeDef:
    pass
```

### post_text

Type annotations for `boto3.client("lex-runtime").post_text` method.

[Client.post_text documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.post_text)

```python
def post_text(
    self,
    botName: str,
    botAlias: str,
    userId: str,
    inputText: str,
    sessionAttributes: Dict[str, str] = None,
    requestAttributes: Dict[str, str] = None,
    activeContexts: List["ActiveContextTypeDef"] = None
) -> PostTextResponseTypeDef:
    pass
```

### put_session

Type annotations for `boto3.client("lex-runtime").put_session` method.

[Client.put_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html#LexRuntimeService.Client.put_session)

```python
def put_session(
    self,
    botName: str,
    botAlias: str,
    userId: str,
    sessionAttributes: Dict[str, str] = None,
    dialogAction: "DialogActionTypeDef" = None,
    recentIntentSummaryView: List["IntentSummaryTypeDef"] = None,
    accept: str = None,
    activeContexts: List["ActiveContextTypeDef"] = None
) -> PutSessionResponseTypeDef:
    pass
```



