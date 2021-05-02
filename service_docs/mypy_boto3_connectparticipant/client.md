# ConnectParticipantClient for boto3 ConnectParticipant module

> [Index](../index.md) > [ConnectParticipant](./index.md) > ConnectParticipantClient

Auto-generated documentation for [ConnectParticipant](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant)
type annotations stubs module [mypy_boto3_connectparticipant](https://pypi.org/project/mypy-boto3-connectparticipant/).

- [ConnectParticipantClient for boto3 ConnectParticipant module](#connectparticipantclient-for-boto3-connectparticipant-module)
  - [ConnectParticipantClient](#connectparticipantclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [complete_attachment_upload](#complete_attachment_upload)
    - [create_participant_connection](#create_participant_connection)
    - [disconnect_participant](#disconnect_participant)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_attachment](#get_attachment)
    - [get_transcript](#get_transcript)
    - [send_event](#send_event)
    - [send_message](#send_message)
    - [start_attachment_upload](#start_attachment_upload)

## ConnectParticipantClient

Type annotations for `boto3.client("connectparticipant")`

Can be used directly:

```python
from mypy_boto3_connectparticipant.client import ConnectParticipantClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_connectparticipant.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("connectparticipant").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### complete_attachment_upload

Type annotations for `boto3.client("connectparticipant").complete_attachment_upload` method.

[Client.complete_attachment_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.complete_attachment_upload)

```python
def complete_attachment_upload(
    self,
    AttachmentIds: List[str],
    ClientToken: str,
    ConnectionToken: str
) -> Dict[str, Any]:
    pass
```

### create_participant_connection

Type annotations for `boto3.client("connectparticipant").create_participant_connection` method.

[Client.create_participant_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.create_participant_connection)

```python
def create_participant_connection(
    self,
    Type: List[ConnectionType],
    ParticipantToken: str
) -> CreateParticipantConnectionResponseTypeDef:
    pass
```

### disconnect_participant

Type annotations for `boto3.client("connectparticipant").disconnect_participant` method.

[Client.disconnect_participant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.disconnect_participant)

```python
def disconnect_participant(
    self,
    ConnectionToken: str,
    ClientToken: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("connectparticipant").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.generate_presigned_url)

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

### get_attachment

Type annotations for `boto3.client("connectparticipant").get_attachment` method.

[Client.get_attachment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.get_attachment)

```python
def get_attachment(
    self,
    AttachmentId: str,
    ConnectionToken: str
) -> GetAttachmentResponseTypeDef:
    pass
```

### get_transcript

Type annotations for `boto3.client("connectparticipant").get_transcript` method.

[Client.get_transcript documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.get_transcript)

```python
def get_transcript(
    self,
    ConnectionToken: str,
    ContactId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    ScanDirection: ScanDirection = None,
    SortOrder: SortKey = None,
    StartPosition: StartPositionTypeDef = None
) -> GetTranscriptResponseTypeDef:
    pass
```

### send_event

Type annotations for `boto3.client("connectparticipant").send_event` method.

[Client.send_event documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.send_event)

```python
def send_event(
    self,
    ContentType: str,
    ConnectionToken: str,
    Content: str = None,
    ClientToken: str = None
) -> SendEventResponseTypeDef:
    pass
```

### send_message

Type annotations for `boto3.client("connectparticipant").send_message` method.

[Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.send_message)

```python
def send_message(
    self,
    ContentType: str,
    Content: str,
    ConnectionToken: str,
    ClientToken: str = None
) -> SendMessageResponseTypeDef:
    pass
```

### start_attachment_upload

Type annotations for `boto3.client("connectparticipant").start_attachment_upload` method.

[Client.start_attachment_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant.Client.start_attachment_upload)

```python
def start_attachment_upload(
    self,
    ContentType: str,
    AttachmentSizeInBytes: int,
    AttachmentName: str,
    ClientToken: str,
    ConnectionToken: str
) -> StartAttachmentUploadResponseTypeDef:
    pass
```



