# TextractClient for boto3 Textract module

> [Index](../index.md) > [Textract](./index.md) > TextractClient

Auto-generated documentation for [Textract](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract)
type annotations stubs module [mypy_boto3_textract](https://pypi.org/project/mypy-boto3-textract/).

- [TextractClient for boto3 Textract module](#textractclient-for-boto3-textract-module)
  - [TextractClient](#textractclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [analyze_document](#analyze_document)
    - [can_paginate](#can_paginate)
    - [detect_document_text](#detect_document_text)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_document_analysis](#get_document_analysis)
    - [get_document_text_detection](#get_document_text_detection)
    - [start_document_analysis](#start_document_analysis)
    - [start_document_text_detection](#start_document_text_detection)

## TextractClient

Type annotations for `boto3.client("textract")`

Can be used directly:

```python
from mypy_boto3_textract.client import TextractClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_textract.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadDocumentException`
- `Exceptions.ClientError`
- `Exceptions.DocumentTooLargeException`
- `Exceptions.HumanLoopQuotaExceededException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.InternalServerError`
- `Exceptions.InvalidJobIdException`
- `Exceptions.InvalidKMSKeyException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidS3ObjectException`
- `Exceptions.LimitExceededException`
- `Exceptions.ProvisionedThroughputExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnsupportedDocumentException`


## Methods


### analyze_document

Type annotations for `boto3.client("textract").analyze_document` method.

[Client.analyze_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.analyze_document)

```python
def analyze_document(
    self,
    Document: DocumentTypeDef,
    FeatureTypes: List[FeatureType],
    HumanLoopConfig: HumanLoopConfigTypeDef = None
) -> AnalyzeDocumentResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("textract").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### detect_document_text

Type annotations for `boto3.client("textract").detect_document_text` method.

[Client.detect_document_text documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.detect_document_text)

```python
def detect_document_text(
    self,
    Document: DocumentTypeDef
) -> DetectDocumentTextResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("textract").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.generate_presigned_url)

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

### get_document_analysis

Type annotations for `boto3.client("textract").get_document_analysis` method.

[Client.get_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.get_document_analysis)

```python
def get_document_analysis(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetDocumentAnalysisResponseTypeDef:
    pass
```

### get_document_text_detection

Type annotations for `boto3.client("textract").get_document_text_detection` method.

[Client.get_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.get_document_text_detection)

```python
def get_document_text_detection(
    self,
    JobId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetDocumentTextDetectionResponseTypeDef:
    pass
```

### start_document_analysis

Type annotations for `boto3.client("textract").start_document_analysis` method.

[Client.start_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.start_document_analysis)

```python
def start_document_analysis(
    self,
    DocumentLocation: DocumentLocationTypeDef,
    FeatureTypes: List[FeatureType],
    ClientRequestToken: str = None,
    JobTag: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    OutputConfig: OutputConfigTypeDef = None,
    KMSKeyId: str = None
) -> StartDocumentAnalysisResponseTypeDef:
    pass
```

### start_document_text_detection

Type annotations for `boto3.client("textract").start_document_text_detection` method.

[Client.start_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.start_document_text_detection)

```python
def start_document_text_detection(
    self,
    DocumentLocation: DocumentLocationTypeDef,
    ClientRequestToken: str = None,
    JobTag: str = None,
    NotificationChannel: NotificationChannelTypeDef = None,
    OutputConfig: OutputConfigTypeDef = None,
    KMSKeyId: str = None
) -> StartDocumentTextDetectionResponseTypeDef:
    pass
```



