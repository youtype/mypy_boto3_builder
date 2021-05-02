# Paginators for boto3 Comprehend module

> [Index](../index.md) > [Comprehend](./index.md) > Paginators

Auto-generated documentation for [Comprehend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend)
type annotations stubs module [mypy_boto3_comprehend](https://pypi.org/project/mypy-boto3-comprehend/).

- [Paginators for boto3 Comprehend module](#paginators-for-boto3-comprehend-module)
  - [ListDocumentClassificationJobsPaginator](#listdocumentclassificationjobspaginator)
  - [ListDocumentClassifiersPaginator](#listdocumentclassifierspaginator)
  - [ListDominantLanguageDetectionJobsPaginator](#listdominantlanguagedetectionjobspaginator)
  - [ListEntitiesDetectionJobsPaginator](#listentitiesdetectionjobspaginator)
  - [ListEntityRecognizersPaginator](#listentityrecognizerspaginator)
  - [ListKeyPhrasesDetectionJobsPaginator](#listkeyphrasesdetectionjobspaginator)
  - [ListSentimentDetectionJobsPaginator](#listsentimentdetectionjobspaginator)
  - [ListTopicsDetectionJobsPaginator](#listtopicsdetectionjobspaginator)

## ListDocumentClassificationJobsPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_document_classification_jobs")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListDocumentClassificationJobsPaginator

def get_list_document_classification_jobs_paginator() -> ListDocumentClassificationJobsPaginator:
    return boto3.client("comprehend").get_paginator("list_document_classification_jobs")
```

[Paginator.ListDocumentClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)

```python
class ListDocumentClassificationJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: DocumentClassificationJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentClassificationJobsResponseTypeDef]:
        pass
```
## ListDocumentClassifiersPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_document_classifiers")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListDocumentClassifiersPaginator

def get_list_document_classifiers_paginator() -> ListDocumentClassifiersPaginator:
    return boto3.client("comprehend").get_paginator("list_document_classifiers")
```

[Paginator.ListDocumentClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)

```python
class ListDocumentClassifiersPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: DocumentClassifierFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentClassifiersResponseTypeDef]:
        pass
```
## ListDominantLanguageDetectionJobsPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_dominant_language_detection_jobs")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListDominantLanguageDetectionJobsPaginator

def get_list_dominant_language_detection_jobs_paginator() -> ListDominantLanguageDetectionJobsPaginator:
    return boto3.client("comprehend").get_paginator("list_dominant_language_detection_jobs")
```

[Paginator.ListDominantLanguageDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)

```python
class ListDominantLanguageDetectionJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: DominantLanguageDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDominantLanguageDetectionJobsResponseTypeDef]:
        pass
```
## ListEntitiesDetectionJobsPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_entities_detection_jobs")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListEntitiesDetectionJobsPaginator

def get_list_entities_detection_jobs_paginator() -> ListEntitiesDetectionJobsPaginator:
    return boto3.client("comprehend").get_paginator("list_entities_detection_jobs")
```

[Paginator.ListEntitiesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)

```python
class ListEntitiesDetectionJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: EntitiesDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntitiesDetectionJobsResponseTypeDef]:
        pass
```
## ListEntityRecognizersPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_entity_recognizers")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListEntityRecognizersPaginator

def get_list_entity_recognizers_paginator() -> ListEntityRecognizersPaginator:
    return boto3.client("comprehend").get_paginator("list_entity_recognizers")
```

[Paginator.ListEntityRecognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)

```python
class ListEntityRecognizersPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: EntityRecognizerFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntityRecognizersResponseTypeDef]:
        pass
```
## ListKeyPhrasesDetectionJobsPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_key_phrases_detection_jobs")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListKeyPhrasesDetectionJobsPaginator

def get_list_key_phrases_detection_jobs_paginator() -> ListKeyPhrasesDetectionJobsPaginator:
    return boto3.client("comprehend").get_paginator("list_key_phrases_detection_jobs")
```

[Paginator.ListKeyPhrasesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)

```python
class ListKeyPhrasesDetectionJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeyPhrasesDetectionJobsResponseTypeDef]:
        pass
```
## ListSentimentDetectionJobsPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_sentiment_detection_jobs")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListSentimentDetectionJobsPaginator

def get_list_sentiment_detection_jobs_paginator() -> ListSentimentDetectionJobsPaginator:
    return boto3.client("comprehend").get_paginator("list_sentiment_detection_jobs")
```

[Paginator.ListSentimentDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)

```python
class ListSentimentDetectionJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: SentimentDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSentimentDetectionJobsResponseTypeDef]:
        pass
```
## ListTopicsDetectionJobsPaginator

Type annotations for `boto3.client("comprehend").get_paginator("list_topics_detection_jobs")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListTopicsDetectionJobsPaginator

def get_list_topics_detection_jobs_paginator() -> ListTopicsDetectionJobsPaginator:
    return boto3.client("comprehend").get_paginator("list_topics_detection_jobs")
```

[Paginator.ListTopicsDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)

```python
class ListTopicsDetectionJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filter: TopicsDetectionJobFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicsDetectionJobsResponseTypeDef]:
        pass
```