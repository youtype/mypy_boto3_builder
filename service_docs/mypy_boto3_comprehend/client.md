# ComprehendClient for boto3 Comprehend module

> [Index](../index.md) > [Comprehend](./index.md) > ComprehendClient

Auto-generated documentation for [Comprehend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend)
type annotations stubs module [mypy_boto3_comprehend](https://pypi.org/project/mypy-boto3-comprehend/).

- [ComprehendClient for boto3 Comprehend module](#comprehendclient-for-boto3-comprehend-module)
  - [ComprehendClient](#comprehendclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_detect_dominant_language](#batch_detect_dominant_language)
    - [batch_detect_entities](#batch_detect_entities)
    - [batch_detect_key_phrases](#batch_detect_key_phrases)
    - [batch_detect_sentiment](#batch_detect_sentiment)
    - [batch_detect_syntax](#batch_detect_syntax)
    - [can_paginate](#can_paginate)
    - [classify_document](#classify_document)
    - [contains_pii_entities](#contains_pii_entities)
    - [create_document_classifier](#create_document_classifier)
    - [create_endpoint](#create_endpoint)
    - [create_entity_recognizer](#create_entity_recognizer)
    - [delete_document_classifier](#delete_document_classifier)
    - [delete_endpoint](#delete_endpoint)
    - [delete_entity_recognizer](#delete_entity_recognizer)
    - [describe_document_classification_job](#describe_document_classification_job)
    - [describe_document_classifier](#describe_document_classifier)
    - [describe_dominant_language_detection_job](#describe_dominant_language_detection_job)
    - [describe_endpoint](#describe_endpoint)
    - [describe_entities_detection_job](#describe_entities_detection_job)
    - [describe_entity_recognizer](#describe_entity_recognizer)
    - [describe_events_detection_job](#describe_events_detection_job)
    - [describe_key_phrases_detection_job](#describe_key_phrases_detection_job)
    - [describe_pii_entities_detection_job](#describe_pii_entities_detection_job)
    - [describe_sentiment_detection_job](#describe_sentiment_detection_job)
    - [describe_topics_detection_job](#describe_topics_detection_job)
    - [detect_dominant_language](#detect_dominant_language)
    - [detect_entities](#detect_entities)
    - [detect_key_phrases](#detect_key_phrases)
    - [detect_pii_entities](#detect_pii_entities)
    - [detect_sentiment](#detect_sentiment)
    - [detect_syntax](#detect_syntax)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_document_classification_jobs](#list_document_classification_jobs)
    - [list_document_classifiers](#list_document_classifiers)
    - [list_dominant_language_detection_jobs](#list_dominant_language_detection_jobs)
    - [list_endpoints](#list_endpoints)
    - [list_entities_detection_jobs](#list_entities_detection_jobs)
    - [list_entity_recognizers](#list_entity_recognizers)
    - [list_events_detection_jobs](#list_events_detection_jobs)
    - [list_key_phrases_detection_jobs](#list_key_phrases_detection_jobs)
    - [list_pii_entities_detection_jobs](#list_pii_entities_detection_jobs)
    - [list_sentiment_detection_jobs](#list_sentiment_detection_jobs)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_topics_detection_jobs](#list_topics_detection_jobs)
    - [start_document_classification_job](#start_document_classification_job)
    - [start_dominant_language_detection_job](#start_dominant_language_detection_job)
    - [start_entities_detection_job](#start_entities_detection_job)
    - [start_events_detection_job](#start_events_detection_job)
    - [start_key_phrases_detection_job](#start_key_phrases_detection_job)
    - [start_pii_entities_detection_job](#start_pii_entities_detection_job)
    - [start_sentiment_detection_job](#start_sentiment_detection_job)
    - [start_topics_detection_job](#start_topics_detection_job)
    - [stop_dominant_language_detection_job](#stop_dominant_language_detection_job)
    - [stop_entities_detection_job](#stop_entities_detection_job)
    - [stop_events_detection_job](#stop_events_detection_job)
    - [stop_key_phrases_detection_job](#stop_key_phrases_detection_job)
    - [stop_pii_entities_detection_job](#stop_pii_entities_detection_job)
    - [stop_sentiment_detection_job](#stop_sentiment_detection_job)
    - [stop_training_document_classifier](#stop_training_document_classifier)
    - [stop_training_entity_recognizer](#stop_training_entity_recognizer)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_endpoint](#update_endpoint)
    - [get_paginator](#get_paginator)

## ComprehendClient

Type annotations for `boto3.client("comprehend")`

Can be used directly:

```python
from mypy_boto3_comprehend.client import ComprehendClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_comprehend.client import Exceptions

def handle_error(exc: Exceptions.BatchSizeLimitExceededException) -> None:
    ...
```


Exceptions:

- `Exceptions.BatchSizeLimitExceededException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidFilterException`
- `Exceptions.InvalidRequestException`
- `Exceptions.JobNotFoundException`
- `Exceptions.KmsKeyValidationException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceUnavailableException`
- `Exceptions.TextSizeLimitExceededException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.TooManyTagKeysException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnsupportedLanguageException`


## Methods


### batch_detect_dominant_language

Type annotations for `boto3.client("comprehend").batch_detect_dominant_language` method.

[Client.batch_detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.batch_detect_dominant_language)

```python
def batch_detect_dominant_language(
    self,
    TextList: List[str]
) -> BatchDetectDominantLanguageResponseTypeDef:
    pass
```

### batch_detect_entities

Type annotations for `boto3.client("comprehend").batch_detect_entities` method.

[Client.batch_detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.batch_detect_entities)

```python
def batch_detect_entities(
    self,
    TextList: List[str],
    LanguageCode: LanguageCode
) -> BatchDetectEntitiesResponseTypeDef:
    pass
```

### batch_detect_key_phrases

Type annotations for `boto3.client("comprehend").batch_detect_key_phrases` method.

[Client.batch_detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.batch_detect_key_phrases)

```python
def batch_detect_key_phrases(
    self,
    TextList: List[str],
    LanguageCode: LanguageCode
) -> BatchDetectKeyPhrasesResponseTypeDef:
    pass
```

### batch_detect_sentiment

Type annotations for `boto3.client("comprehend").batch_detect_sentiment` method.

[Client.batch_detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.batch_detect_sentiment)

```python
def batch_detect_sentiment(
    self,
    TextList: List[str],
    LanguageCode: LanguageCode
) -> BatchDetectSentimentResponseTypeDef:
    pass
```

### batch_detect_syntax

Type annotations for `boto3.client("comprehend").batch_detect_syntax` method.

[Client.batch_detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.batch_detect_syntax)

```python
def batch_detect_syntax(
    self,
    TextList: List[str],
    LanguageCode: SyntaxLanguageCode
) -> BatchDetectSyntaxResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("comprehend").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### classify_document

Type annotations for `boto3.client("comprehend").classify_document` method.

[Client.classify_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.classify_document)

```python
def classify_document(
    self,
    Text: str,
    EndpointArn: str
) -> ClassifyDocumentResponseTypeDef:
    pass
```

### contains_pii_entities

Type annotations for `boto3.client("comprehend").contains_pii_entities` method.

[Client.contains_pii_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.contains_pii_entities)

```python
def contains_pii_entities(
    self,
    Text: str,
    LanguageCode: LanguageCode
) -> ContainsPiiEntitiesResponseTypeDef:
    pass
```

### create_document_classifier

Type annotations for `boto3.client("comprehend").create_document_classifier` method.

[Client.create_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.create_document_classifier)

```python
def create_document_classifier(
    self,
    DocumentClassifierName: str,
    DataAccessRoleArn: str,
    InputDataConfig: "DocumentClassifierInputDataConfigTypeDef",
    LanguageCode: LanguageCode,
    Tags: List["TagTypeDef"] = None,
    OutputDataConfig: "DocumentClassifierOutputDataConfigTypeDef" = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    Mode: DocumentClassifierMode = None,
    ModelKmsKeyId: str = None
) -> CreateDocumentClassifierResponseTypeDef:
    pass
```

### create_endpoint

Type annotations for `boto3.client("comprehend").create_endpoint` method.

[Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.create_endpoint)

```python
def create_endpoint(
    self,
    EndpointName: str,
    ModelArn: str,
    DesiredInferenceUnits: int,
    ClientRequestToken: str = None,
    Tags: List["TagTypeDef"] = None,
    DataAccessRoleArn: str = None
) -> CreateEndpointResponseTypeDef:
    pass
```

### create_entity_recognizer

Type annotations for `boto3.client("comprehend").create_entity_recognizer` method.

[Client.create_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.create_entity_recognizer)

```python
def create_entity_recognizer(
    self,
    RecognizerName: str,
    DataAccessRoleArn: str,
    InputDataConfig: "EntityRecognizerInputDataConfigTypeDef",
    LanguageCode: LanguageCode,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None,
    ModelKmsKeyId: str = None
) -> CreateEntityRecognizerResponseTypeDef:
    pass
```

### delete_document_classifier

Type annotations for `boto3.client("comprehend").delete_document_classifier` method.

[Client.delete_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.delete_document_classifier)

```python
def delete_document_classifier(
    self,
    DocumentClassifierArn: str
) -> Dict[str, Any]:
    pass
```

### delete_endpoint

Type annotations for `boto3.client("comprehend").delete_endpoint` method.

[Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.delete_endpoint)

```python
def delete_endpoint(
    self,
    EndpointArn: str
) -> Dict[str, Any]:
    pass
```

### delete_entity_recognizer

Type annotations for `boto3.client("comprehend").delete_entity_recognizer` method.

[Client.delete_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.delete_entity_recognizer)

```python
def delete_entity_recognizer(
    self,
    EntityRecognizerArn: str
) -> Dict[str, Any]:
    pass
```

### describe_document_classification_job

Type annotations for `boto3.client("comprehend").describe_document_classification_job` method.

[Client.describe_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_document_classification_job)

```python
def describe_document_classification_job(
    self,
    JobId: str
) -> DescribeDocumentClassificationJobResponseTypeDef:
    pass
```

### describe_document_classifier

Type annotations for `boto3.client("comprehend").describe_document_classifier` method.

[Client.describe_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier)

```python
def describe_document_classifier(
    self,
    DocumentClassifierArn: str
) -> DescribeDocumentClassifierResponseTypeDef:
    pass
```

### describe_dominant_language_detection_job

Type annotations for `boto3.client("comprehend").describe_dominant_language_detection_job` method.

[Client.describe_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_dominant_language_detection_job)

```python
def describe_dominant_language_detection_job(
    self,
    JobId: str
) -> DescribeDominantLanguageDetectionJobResponseTypeDef:
    pass
```

### describe_endpoint

Type annotations for `boto3.client("comprehend").describe_endpoint` method.

[Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_endpoint)

```python
def describe_endpoint(
    self,
    EndpointArn: str
) -> DescribeEndpointResponseTypeDef:
    pass
```

### describe_entities_detection_job

Type annotations for `boto3.client("comprehend").describe_entities_detection_job` method.

[Client.describe_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_entities_detection_job)

```python
def describe_entities_detection_job(
    self,
    JobId: str
) -> DescribeEntitiesDetectionJobResponseTypeDef:
    pass
```

### describe_entity_recognizer

Type annotations for `boto3.client("comprehend").describe_entity_recognizer` method.

[Client.describe_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer)

```python
def describe_entity_recognizer(
    self,
    EntityRecognizerArn: str
) -> DescribeEntityRecognizerResponseTypeDef:
    pass
```

### describe_events_detection_job

Type annotations for `boto3.client("comprehend").describe_events_detection_job` method.

[Client.describe_events_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_events_detection_job)

```python
def describe_events_detection_job(
    self,
    JobId: str
) -> DescribeEventsDetectionJobResponseTypeDef:
    pass
```

### describe_key_phrases_detection_job

Type annotations for `boto3.client("comprehend").describe_key_phrases_detection_job` method.

[Client.describe_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_key_phrases_detection_job)

```python
def describe_key_phrases_detection_job(
    self,
    JobId: str
) -> DescribeKeyPhrasesDetectionJobResponseTypeDef:
    pass
```

### describe_pii_entities_detection_job

Type annotations for `boto3.client("comprehend").describe_pii_entities_detection_job` method.

[Client.describe_pii_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_pii_entities_detection_job)

```python
def describe_pii_entities_detection_job(
    self,
    JobId: str
) -> DescribePiiEntitiesDetectionJobResponseTypeDef:
    pass
```

### describe_sentiment_detection_job

Type annotations for `boto3.client("comprehend").describe_sentiment_detection_job` method.

[Client.describe_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_sentiment_detection_job)

```python
def describe_sentiment_detection_job(
    self,
    JobId: str
) -> DescribeSentimentDetectionJobResponseTypeDef:
    pass
```

### describe_topics_detection_job

Type annotations for `boto3.client("comprehend").describe_topics_detection_job` method.

[Client.describe_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.describe_topics_detection_job)

```python
def describe_topics_detection_job(
    self,
    JobId: str
) -> DescribeTopicsDetectionJobResponseTypeDef:
    pass
```

### detect_dominant_language

Type annotations for `boto3.client("comprehend").detect_dominant_language` method.

[Client.detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language)

```python
def detect_dominant_language(
    self,
    Text: str
) -> DetectDominantLanguageResponseTypeDef:
    pass
```

### detect_entities

Type annotations for `boto3.client("comprehend").detect_entities` method.

[Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_entities)

```python
def detect_entities(
    self,
    Text: str,
    LanguageCode: LanguageCode = None,
    EndpointArn: str = None
) -> DetectEntitiesResponseTypeDef:
    pass
```

### detect_key_phrases

Type annotations for `boto3.client("comprehend").detect_key_phrases` method.

[Client.detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_key_phrases)

```python
def detect_key_phrases(
    self,
    Text: str,
    LanguageCode: LanguageCode
) -> DetectKeyPhrasesResponseTypeDef:
    pass
```

### detect_pii_entities

Type annotations for `boto3.client("comprehend").detect_pii_entities` method.

[Client.detect_pii_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_pii_entities)

```python
def detect_pii_entities(
    self,
    Text: str,
    LanguageCode: LanguageCode
) -> DetectPiiEntitiesResponseTypeDef:
    pass
```

### detect_sentiment

Type annotations for `boto3.client("comprehend").detect_sentiment` method.

[Client.detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_sentiment)

```python
def detect_sentiment(
    self,
    Text: str,
    LanguageCode: LanguageCode
) -> DetectSentimentResponseTypeDef:
    pass
```

### detect_syntax

Type annotations for `boto3.client("comprehend").detect_syntax` method.

[Client.detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_syntax)

```python
def detect_syntax(
    self,
    Text: str,
    LanguageCode: SyntaxLanguageCode
) -> DetectSyntaxResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("comprehend").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.generate_presigned_url)

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

### list_document_classification_jobs

Type annotations for `boto3.client("comprehend").list_document_classification_jobs` method.

[Client.list_document_classification_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_document_classification_jobs)

```python
def list_document_classification_jobs(
    self,
    Filter: DocumentClassificationJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDocumentClassificationJobsResponseTypeDef:
    pass
```

### list_document_classifiers

Type annotations for `boto3.client("comprehend").list_document_classifiers` method.

[Client.list_document_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_document_classifiers)

```python
def list_document_classifiers(
    self,
    Filter: DocumentClassifierFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDocumentClassifiersResponseTypeDef:
    pass
```

### list_dominant_language_detection_jobs

Type annotations for `boto3.client("comprehend").list_dominant_language_detection_jobs` method.

[Client.list_dominant_language_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_dominant_language_detection_jobs)

```python
def list_dominant_language_detection_jobs(
    self,
    Filter: DominantLanguageDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListDominantLanguageDetectionJobsResponseTypeDef:
    pass
```

### list_endpoints

Type annotations for `boto3.client("comprehend").list_endpoints` method.

[Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_endpoints)

```python
def list_endpoints(
    self,
    Filter: EndpointFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEndpointsResponseTypeDef:
    pass
```

### list_entities_detection_jobs

Type annotations for `boto3.client("comprehend").list_entities_detection_jobs` method.

[Client.list_entities_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_entities_detection_jobs)

```python
def list_entities_detection_jobs(
    self,
    Filter: EntitiesDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEntitiesDetectionJobsResponseTypeDef:
    pass
```

### list_entity_recognizers

Type annotations for `boto3.client("comprehend").list_entity_recognizers` method.

[Client.list_entity_recognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizers)

```python
def list_entity_recognizers(
    self,
    Filter: EntityRecognizerFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEntityRecognizersResponseTypeDef:
    pass
```

### list_events_detection_jobs

Type annotations for `boto3.client("comprehend").list_events_detection_jobs` method.

[Client.list_events_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_events_detection_jobs)

```python
def list_events_detection_jobs(
    self,
    Filter: EventsDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListEventsDetectionJobsResponseTypeDef:
    pass
```

### list_key_phrases_detection_jobs

Type annotations for `boto3.client("comprehend").list_key_phrases_detection_jobs` method.

[Client.list_key_phrases_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_key_phrases_detection_jobs)

```python
def list_key_phrases_detection_jobs(
    self,
    Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListKeyPhrasesDetectionJobsResponseTypeDef:
    pass
```

### list_pii_entities_detection_jobs

Type annotations for `boto3.client("comprehend").list_pii_entities_detection_jobs` method.

[Client.list_pii_entities_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_pii_entities_detection_jobs)

```python
def list_pii_entities_detection_jobs(
    self,
    Filter: PiiEntitiesDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListPiiEntitiesDetectionJobsResponseTypeDef:
    pass
```

### list_sentiment_detection_jobs

Type annotations for `boto3.client("comprehend").list_sentiment_detection_jobs` method.

[Client.list_sentiment_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_sentiment_detection_jobs)

```python
def list_sentiment_detection_jobs(
    self,
    Filter: SentimentDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListSentimentDetectionJobsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("comprehend").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_topics_detection_jobs

Type annotations for `boto3.client("comprehend").list_topics_detection_jobs` method.

[Client.list_topics_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.list_topics_detection_jobs)

```python
def list_topics_detection_jobs(
    self,
    Filter: TopicsDetectionJobFilterTypeDef = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListTopicsDetectionJobsResponseTypeDef:
    pass
```

### start_document_classification_job

Type annotations for `boto3.client("comprehend").start_document_classification_job` method.

[Client.start_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_document_classification_job)

```python
def start_document_classification_job(
    self,
    DocumentClassifierArn: str,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None
) -> StartDocumentClassificationJobResponseTypeDef:
    pass
```

### start_dominant_language_detection_job

Type annotations for `boto3.client("comprehend").start_dominant_language_detection_job` method.

[Client.start_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_dominant_language_detection_job)

```python
def start_dominant_language_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None
) -> StartDominantLanguageDetectionJobResponseTypeDef:
    pass
```

### start_entities_detection_job

Type annotations for `boto3.client("comprehend").start_entities_detection_job` method.

[Client.start_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_entities_detection_job)

```python
def start_entities_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: LanguageCode,
    JobName: str = None,
    EntityRecognizerArn: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None
) -> StartEntitiesDetectionJobResponseTypeDef:
    pass
```

### start_events_detection_job

Type annotations for `boto3.client("comprehend").start_events_detection_job` method.

[Client.start_events_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_events_detection_job)

```python
def start_events_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: LanguageCode,
    TargetEventTypes: List[str],
    JobName: str = None,
    ClientRequestToken: str = None
) -> StartEventsDetectionJobResponseTypeDef:
    pass
```

### start_key_phrases_detection_job

Type annotations for `boto3.client("comprehend").start_key_phrases_detection_job` method.

[Client.start_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_key_phrases_detection_job)

```python
def start_key_phrases_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: LanguageCode,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None
) -> StartKeyPhrasesDetectionJobResponseTypeDef:
    pass
```

### start_pii_entities_detection_job

Type annotations for `boto3.client("comprehend").start_pii_entities_detection_job` method.

[Client.start_pii_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_pii_entities_detection_job)

```python
def start_pii_entities_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    Mode: PiiEntitiesDetectionMode,
    DataAccessRoleArn: str,
    LanguageCode: LanguageCode,
    RedactionConfig: "RedactionConfigTypeDef" = None,
    JobName: str = None,
    ClientRequestToken: str = None
) -> StartPiiEntitiesDetectionJobResponseTypeDef:
    pass
```

### start_sentiment_detection_job

Type annotations for `boto3.client("comprehend").start_sentiment_detection_job` method.

[Client.start_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_sentiment_detection_job)

```python
def start_sentiment_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    LanguageCode: LanguageCode,
    JobName: str = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None
) -> StartSentimentDetectionJobResponseTypeDef:
    pass
```

### start_topics_detection_job

Type annotations for `boto3.client("comprehend").start_topics_detection_job` method.

[Client.start_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.start_topics_detection_job)

```python
def start_topics_detection_job(
    self,
    InputDataConfig: "InputDataConfigTypeDef",
    OutputDataConfig: "OutputDataConfigTypeDef",
    DataAccessRoleArn: str,
    JobName: str = None,
    NumberOfTopics: int = None,
    ClientRequestToken: str = None,
    VolumeKmsKeyId: str = None,
    VpcConfig: "VpcConfigTypeDef" = None
) -> StartTopicsDetectionJobResponseTypeDef:
    pass
```

### stop_dominant_language_detection_job

Type annotations for `boto3.client("comprehend").stop_dominant_language_detection_job` method.

[Client.stop_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_dominant_language_detection_job)

```python
def stop_dominant_language_detection_job(
    self,
    JobId: str
) -> StopDominantLanguageDetectionJobResponseTypeDef:
    pass
```

### stop_entities_detection_job

Type annotations for `boto3.client("comprehend").stop_entities_detection_job` method.

[Client.stop_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_entities_detection_job)

```python
def stop_entities_detection_job(
    self,
    JobId: str
) -> StopEntitiesDetectionJobResponseTypeDef:
    pass
```

### stop_events_detection_job

Type annotations for `boto3.client("comprehend").stop_events_detection_job` method.

[Client.stop_events_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_events_detection_job)

```python
def stop_events_detection_job(
    self,
    JobId: str
) -> StopEventsDetectionJobResponseTypeDef:
    pass
```

### stop_key_phrases_detection_job

Type annotations for `boto3.client("comprehend").stop_key_phrases_detection_job` method.

[Client.stop_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_key_phrases_detection_job)

```python
def stop_key_phrases_detection_job(
    self,
    JobId: str
) -> StopKeyPhrasesDetectionJobResponseTypeDef:
    pass
```

### stop_pii_entities_detection_job

Type annotations for `boto3.client("comprehend").stop_pii_entities_detection_job` method.

[Client.stop_pii_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_pii_entities_detection_job)

```python
def stop_pii_entities_detection_job(
    self,
    JobId: str
) -> StopPiiEntitiesDetectionJobResponseTypeDef:
    pass
```

### stop_sentiment_detection_job

Type annotations for `boto3.client("comprehend").stop_sentiment_detection_job` method.

[Client.stop_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_sentiment_detection_job)

```python
def stop_sentiment_detection_job(
    self,
    JobId: str
) -> StopSentimentDetectionJobResponseTypeDef:
    pass
```

### stop_training_document_classifier

Type annotations for `boto3.client("comprehend").stop_training_document_classifier` method.

[Client.stop_training_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_training_document_classifier)

```python
def stop_training_document_classifier(
    self,
    DocumentClassifierArn: str
) -> Dict[str, Any]:
    pass
```

### stop_training_entity_recognizer

Type annotations for `boto3.client("comprehend").stop_training_entity_recognizer` method.

[Client.stop_training_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.stop_training_entity_recognizer)

```python
def stop_training_entity_recognizer(
    self,
    EntityRecognizerArn: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("comprehend").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("comprehend").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_endpoint

Type annotations for `boto3.client("comprehend").update_endpoint` method.

[Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.update_endpoint)

```python
def update_endpoint(
    self,
    EndpointArn: str,
    DesiredInferenceUnits: int
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("comprehend").get_paginator` method with overloads.

- `client.get_paginator("list_document_classification_jobs")` -> [ListDocumentClassificationJobsPaginator](./paginators.md#listdocumentclassificationjobspaginator)
- `client.get_paginator("list_document_classifiers")` -> [ListDocumentClassifiersPaginator](./paginators.md#listdocumentclassifierspaginator)
- `client.get_paginator("list_dominant_language_detection_jobs")` -> [ListDominantLanguageDetectionJobsPaginator](./paginators.md#listdominantlanguagedetectionjobspaginator)
- `client.get_paginator("list_entities_detection_jobs")` -> [ListEntitiesDetectionJobsPaginator](./paginators.md#listentitiesdetectionjobspaginator)
- `client.get_paginator("list_entity_recognizers")` -> [ListEntityRecognizersPaginator](./paginators.md#listentityrecognizerspaginator)
- `client.get_paginator("list_key_phrases_detection_jobs")` -> [ListKeyPhrasesDetectionJobsPaginator](./paginators.md#listkeyphrasesdetectionjobspaginator)
- `client.get_paginator("list_sentiment_detection_jobs")` -> [ListSentimentDetectionJobsPaginator](./paginators.md#listsentimentdetectionjobspaginator)
- `client.get_paginator("list_topics_detection_jobs")` -> [ListTopicsDetectionJobsPaginator](./paginators.md#listtopicsdetectionjobspaginator)


