# Type annotations for boto3 ConnectContactLens module

> [Index](../index.md) > ConnectContactLens

Auto-generated documentation for [ConnectContactLens](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html#ConnectContactLens)
type annotations stubs module [mypy_boto3_connect_contact_lens](https://pypi.org/project/mypy-boto3-connect-contact-lens/).

```bash
pip install mypy-boto3-connect-contact-lens
```

- [Type annotations for boto3 ConnectContactLens module](#type-annotations-for-boto3-connectcontactlens-module)
  - [ConnectContactLensClient](#connectcontactlensclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## ConnectContactLensClient

Type annotations for  `boto3.client("connect-contact-lens")` as [ConnectContactLensClient](./client.md)

Can be used directly:

```python
from mypy_boto3_connect_contact_lens.client import ConnectContactLensClient
```


ConnectContactLensClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_realtime_contact_analysis_segments](./client.md#list-realtime-contact-analysis-segments)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServiceException](./client.md#internalserviceexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_connect_contact_lens.literals import SentimentValue, ...
```

- [SentimentValue](./literals.md#sentimentvalue)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_connect_contact_lens.type_defs import CategoriesTypeDef, ...
```

- [CategoriesTypeDef](./type_defs.md#categoriestypedef)
- [CategoryDetailsTypeDef](./type_defs.md#categorydetailstypedef)
- [CharacterOffsetsTypeDef](./type_defs.md#characteroffsetstypedef)
- [IssueDetectedTypeDef](./type_defs.md#issuedetectedtypedef)
- [ListRealtimeContactAnalysisSegmentsResponseTypeDef](./type_defs.md#listrealtimecontactanalysissegmentsresponsetypedef)
- [PointOfInterestTypeDef](./type_defs.md#pointofinteresttypedef)
- [RealtimeContactAnalysisSegmentTypeDef](./type_defs.md#realtimecontactanalysissegmenttypedef)
- [TranscriptTypeDef](./type_defs.md#transcripttypedef)
