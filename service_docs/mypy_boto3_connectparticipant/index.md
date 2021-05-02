# Type annotations for boto3 ConnectParticipant module

> [Index](../index.md) > ConnectParticipant

Auto-generated documentation for [ConnectParticipant](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant)
type annotations stubs module [mypy_boto3_connectparticipant](https://pypi.org/project/mypy-boto3-connectparticipant/).

```bash
pip install mypy-boto3-connectparticipant
```

- [Type annotations for boto3 ConnectParticipant module](#type-annotations-for-boto3-connectparticipant-module)
  - [ConnectParticipantClient](#connectparticipantclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## ConnectParticipantClient

Type annotations for  `boto3.client("connectparticipant")` as [ConnectParticipantClient](./client.md)

Can be used directly:

```python
from mypy_boto3_connectparticipant.client import ConnectParticipantClient
```


ConnectParticipantClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [complete_attachment_upload](./client.md#complete-attachment-upload)
- [create_participant_connection](./client.md#create-participant-connection)
- [disconnect_participant](./client.md#disconnect-participant)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_attachment](./client.md#get-attachment)
- [get_transcript](./client.md#get-transcript)
- [send_event](./client.md#send-event)
- [send_message](./client.md#send-message)
- [start_attachment_upload](./client.md#start-attachment-upload)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_connectparticipant.literals import ArtifactStatus, ...
```

- [ArtifactStatus](./literals.md#artifactstatus)
- [ChatItemType](./literals.md#chatitemtype)
- [ConnectionType](./literals.md#connectiontype)
- [ParticipantRole](./literals.md#participantrole)
- [ScanDirection](./literals.md#scandirection)
- [SortKey](./literals.md#sortkey)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef, ...
```

- [AttachmentItemTypeDef](./type_defs.md#attachmentitemtypedef)
- [ConnectionCredentialsTypeDef](./type_defs.md#connectioncredentialstypedef)
- [CreateParticipantConnectionResponseTypeDef](./type_defs.md#createparticipantconnectionresponsetypedef)
- [GetAttachmentResponseTypeDef](./type_defs.md#getattachmentresponsetypedef)
- [GetTranscriptResponseTypeDef](./type_defs.md#gettranscriptresponsetypedef)
- [ItemTypeDef](./type_defs.md#itemtypedef)
- [SendEventResponseTypeDef](./type_defs.md#sendeventresponsetypedef)
- [SendMessageResponseTypeDef](./type_defs.md#sendmessageresponsetypedef)
- [StartAttachmentUploadResponseTypeDef](./type_defs.md#startattachmentuploadresponsetypedef)
- [StartPositionTypeDef](./type_defs.md#startpositiontypedef)
- [UploadMetadataTypeDef](./type_defs.md#uploadmetadatatypedef)
- [WebsocketTypeDef](./type_defs.md#websockettypedef)
