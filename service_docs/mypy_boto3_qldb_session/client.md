# QLDBSessionClient for boto3 QLDBSession module

> [Index](../index.md) > [QLDBSession](./index.md) > QLDBSessionClient

Auto-generated documentation for [QLDBSession](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb-session.html#QLDBSession)
type annotations stubs module [mypy_boto3_qldb_session](https://pypi.org/project/mypy-boto3-qldb-session/).

- [QLDBSessionClient for boto3 QLDBSession module](#qldbsessionclient-for-boto3-qldbsession-module)
  - [QLDBSessionClient](#qldbsessionclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [send_command](#send_command)

## QLDBSessionClient

Type annotations for `boto3.client("qldb-session")`

Can be used directly:

```python
from mypy_boto3_qldb_session.client import QLDBSessionClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_qldb_session.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.CapacityExceededException`
- `Exceptions.ClientError`
- `Exceptions.InvalidSessionException`
- `Exceptions.LimitExceededException`
- `Exceptions.OccConflictException`
- `Exceptions.RateExceededException`


## Methods


### can_paginate

Type annotations for `boto3.client("qldb-session").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb-session.html#QLDBSession.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("qldb-session").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb-session.html#QLDBSession.Client.generate_presigned_url)

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

### send_command

Type annotations for `boto3.client("qldb-session").send_command` method.

[Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb-session.html#QLDBSession.Client.send_command)

```python
def send_command(
    self,
    SessionToken: str = None,
    StartSession: StartSessionRequestTypeDef = None,
    StartTransaction: Dict[str, Any] = None,
    EndSession: Dict[str, Any] = None,
    CommitTransaction: CommitTransactionRequestTypeDef = None,
    AbortTransaction: Dict[str, Any] = None,
    ExecuteStatement: ExecuteStatementRequestTypeDef = None,
    FetchPage: FetchPageRequestTypeDef = None
) -> SendCommandResultTypeDef:
    pass
```



