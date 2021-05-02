# Structures for boto3 ConnectParticipant module

> [Index](../index.md) > [ConnectParticipant](./index.md) > Structures

Auto-generated documentation for [ConnectParticipant](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html#ConnectParticipant)
type annotations stubs module [mypy_boto3_connectparticipant](https://pypi.org/project/mypy-boto3-connectparticipant/).

- [Structures for boto3 ConnectParticipant module](#structures-for-boto3-connectparticipant-module)
  - [AttachmentItemTypeDef](#attachmentitemtypedef)
  - [ConnectionCredentialsTypeDef](#connectioncredentialstypedef)
  - [ItemTypeDef](#itemtypedef)
  - [UploadMetadataTypeDef](#uploadmetadatatypedef)
  - [WebsocketTypeDef](#websockettypedef)
  - [CreateParticipantConnectionResponseTypeDef](#createparticipantconnectionresponsetypedef)
  - [GetAttachmentResponseTypeDef](#getattachmentresponsetypedef)
  - [GetTranscriptResponseTypeDef](#gettranscriptresponsetypedef)
  - [SendEventResponseTypeDef](#sendeventresponsetypedef)
  - [SendMessageResponseTypeDef](#sendmessageresponsetypedef)
  - [StartAttachmentUploadResponseTypeDef](#startattachmentuploadresponsetypedef)
  - [StartPositionTypeDef](#startpositiontypedef)

## AttachmentItemTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef
```




Optional fields:
- `ContentType`: `str`
- `AttachmentId`: `str`
- `AttachmentName`: `str`
- `Status`: `ArtifactStatus`


## ConnectionCredentialsTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import ConnectionCredentialsTypeDef
```




Optional fields:
- `ConnectionToken`: `str`
- `Expiry`: `str`


## ItemTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import ItemTypeDef
```




Optional fields:
- `AbsoluteTime`: `str`
- `Content`: `str`
- `ContentType`: `str`
- `Id`: `str`
- `Type`: `ChatItemType`
- `ParticipantId`: `str`
- `DisplayName`: `str`
- `ParticipantRole`: `ParticipantRole`
- `Attachments`: `List["AttachmentItemTypeDef"]`


## UploadMetadataTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import UploadMetadataTypeDef
```




Optional fields:
- `Url`: `str`
- `UrlExpiry`: `str`
- `HeadersToInclude`: `Dict[str, str]`


## WebsocketTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import WebsocketTypeDef
```




Optional fields:
- `Url`: `str`
- `ConnectionExpiry`: `str`


## CreateParticipantConnectionResponseTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import CreateParticipantConnectionResponseTypeDef
```




Optional fields:
- `Websocket`: `"WebsocketTypeDef"`
- `ConnectionCredentials`: `"ConnectionCredentialsTypeDef"`


## GetAttachmentResponseTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import GetAttachmentResponseTypeDef
```




Optional fields:
- `Url`: `str`
- `UrlExpiry`: `str`


## GetTranscriptResponseTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import GetTranscriptResponseTypeDef
```




Optional fields:
- `InitialContactId`: `str`
- `Transcript`: `List["ItemTypeDef"]`
- `NextToken`: `str`


## SendEventResponseTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import SendEventResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `AbsoluteTime`: `str`


## SendMessageResponseTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import SendMessageResponseTypeDef
```




Optional fields:
- `Id`: `str`
- `AbsoluteTime`: `str`


## StartAttachmentUploadResponseTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import StartAttachmentUploadResponseTypeDef
```




Optional fields:
- `AttachmentId`: `str`
- `UploadMetadata`: `"UploadMetadataTypeDef"`


## StartPositionTypeDef

```python
from mypy_boto3_connectparticipant.type_defs import StartPositionTypeDef
```




Optional fields:
- `Id`: `str`
- `AbsoluteTime`: `str`
- `MostRecent`: `int`

