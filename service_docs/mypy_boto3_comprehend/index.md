# Type annotations for boto3 Comprehend module

> [Index](../index.md) > Comprehend

Auto-generated documentation for [Comprehend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend)
type annotations stubs module [mypy_boto3_comprehend](https://pypi.org/project/mypy-boto3-comprehend/).

```bash
pip install mypy-boto3-comprehend
```

- [Type annotations for boto3 Comprehend module](#type-annotations-for-boto3-comprehend-module)
  - [ComprehendClient](#comprehendclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ComprehendClient

Type annotations for  `boto3.client("comprehend")` as [ComprehendClient](./client.md)

Can be used directly:

```python
from mypy_boto3_comprehend.client import ComprehendClient
```


ComprehendClient [exceptions](./client.md#exceptions)



### Methods
- [batch_detect_dominant_language](./client.md#batch-detect-dominant-language)
- [batch_detect_entities](./client.md#batch-detect-entities)
- [batch_detect_key_phrases](./client.md#batch-detect-key-phrases)
- [batch_detect_sentiment](./client.md#batch-detect-sentiment)
- [batch_detect_syntax](./client.md#batch-detect-syntax)
- [can_paginate](./client.md#can-paginate)
- [classify_document](./client.md#classify-document)
- [contains_pii_entities](./client.md#contains-pii-entities)
- [create_document_classifier](./client.md#create-document-classifier)
- [create_endpoint](./client.md#create-endpoint)
- [create_entity_recognizer](./client.md#create-entity-recognizer)
- [delete_document_classifier](./client.md#delete-document-classifier)
- [delete_endpoint](./client.md#delete-endpoint)
- [delete_entity_recognizer](./client.md#delete-entity-recognizer)
- [describe_document_classification_job](./client.md#describe-document-classification-job)
- [describe_document_classifier](./client.md#describe-document-classifier)
- [describe_dominant_language_detection_job](./client.md#describe-dominant-language-detection-job)
- [describe_endpoint](./client.md#describe-endpoint)
- [describe_entities_detection_job](./client.md#describe-entities-detection-job)
- [describe_entity_recognizer](./client.md#describe-entity-recognizer)
- [describe_events_detection_job](./client.md#describe-events-detection-job)
- [describe_key_phrases_detection_job](./client.md#describe-key-phrases-detection-job)
- [describe_pii_entities_detection_job](./client.md#describe-pii-entities-detection-job)
- [describe_sentiment_detection_job](./client.md#describe-sentiment-detection-job)
- [describe_topics_detection_job](./client.md#describe-topics-detection-job)
- [detect_dominant_language](./client.md#detect-dominant-language)
- [detect_entities](./client.md#detect-entities)
- [detect_key_phrases](./client.md#detect-key-phrases)
- [detect_pii_entities](./client.md#detect-pii-entities)
- [detect_sentiment](./client.md#detect-sentiment)
- [detect_syntax](./client.md#detect-syntax)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_document_classification_jobs](./client.md#list-document-classification-jobs)
- [list_document_classifiers](./client.md#list-document-classifiers)
- [list_dominant_language_detection_jobs](./client.md#list-dominant-language-detection-jobs)
- [list_endpoints](./client.md#list-endpoints)
- [list_entities_detection_jobs](./client.md#list-entities-detection-jobs)
- [list_entity_recognizers](./client.md#list-entity-recognizers)
- [list_events_detection_jobs](./client.md#list-events-detection-jobs)
- [list_key_phrases_detection_jobs](./client.md#list-key-phrases-detection-jobs)
- [list_pii_entities_detection_jobs](./client.md#list-pii-entities-detection-jobs)
- [list_sentiment_detection_jobs](./client.md#list-sentiment-detection-jobs)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_topics_detection_jobs](./client.md#list-topics-detection-jobs)
- [start_document_classification_job](./client.md#start-document-classification-job)
- [start_dominant_language_detection_job](./client.md#start-dominant-language-detection-job)
- [start_entities_detection_job](./client.md#start-entities-detection-job)
- [start_events_detection_job](./client.md#start-events-detection-job)
- [start_key_phrases_detection_job](./client.md#start-key-phrases-detection-job)
- [start_pii_entities_detection_job](./client.md#start-pii-entities-detection-job)
- [start_sentiment_detection_job](./client.md#start-sentiment-detection-job)
- [start_topics_detection_job](./client.md#start-topics-detection-job)
- [stop_dominant_language_detection_job](./client.md#stop-dominant-language-detection-job)
- [stop_entities_detection_job](./client.md#stop-entities-detection-job)
- [stop_events_detection_job](./client.md#stop-events-detection-job)
- [stop_key_phrases_detection_job](./client.md#stop-key-phrases-detection-job)
- [stop_pii_entities_detection_job](./client.md#stop-pii-entities-detection-job)
- [stop_sentiment_detection_job](./client.md#stop-sentiment-detection-job)
- [stop_training_document_classifier](./client.md#stop-training-document-classifier)
- [stop_training_entity_recognizer](./client.md#stop-training-entity-recognizer)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_endpoint](./client.md#update-endpoint)




### Exceptions
- [BatchSizeLimitExceededException](./client.md#batchsizelimitexceededexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidFilterException](./client.md#invalidfilterexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [JobNotFoundException](./client.md#jobnotfoundexception)
- [KmsKeyValidationException](./client.md#kmskeyvalidationexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceLimitExceededException](./client.md#resourcelimitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceUnavailableException](./client.md#resourceunavailableexception)
- [TextSizeLimitExceededException](./client.md#textsizelimitexceededexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [TooManyTagKeysException](./client.md#toomanytagkeysexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnsupportedLanguageException](./client.md#unsupportedlanguageexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("comprehend").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_comprehend.paginators import ListDocumentClassificationJobsPaginator, ...
```

- [ListDocumentClassificationJobsPaginator](./paginators.md#listdocumentclassificationjobspaginator)
- [ListDocumentClassifiersPaginator](./paginators.md#listdocumentclassifierspaginator)
- [ListDominantLanguageDetectionJobsPaginator](./paginators.md#listdominantlanguagedetectionjobspaginator)
- [ListEntitiesDetectionJobsPaginator](./paginators.md#listentitiesdetectionjobspaginator)
- [ListEntityRecognizersPaginator](./paginators.md#listentityrecognizerspaginator)
- [ListKeyPhrasesDetectionJobsPaginator](./paginators.md#listkeyphrasesdetectionjobspaginator)
- [ListSentimentDetectionJobsPaginator](./paginators.md#listsentimentdetectionjobspaginator)
- [ListTopicsDetectionJobsPaginator](./paginators.md#listtopicsdetectionjobspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_comprehend.literals import DocumentClassifierDataFormat, ...
```

- [DocumentClassifierDataFormat](./literals.md#documentclassifierdataformat)
- [DocumentClassifierMode](./literals.md#documentclassifiermode)
- [EndpointStatus](./literals.md#endpointstatus)
- [EntityRecognizerDataFormat](./literals.md#entityrecognizerdataformat)
- [EntityType](./literals.md#entitytype)
- [InputFormat](./literals.md#inputformat)
- [JobStatus](./literals.md#jobstatus)
- [LanguageCode](./literals.md#languagecode)
- [ListDocumentClassificationJobsPaginatorName](./literals.md#listdocumentclassificationjobspaginatorname)
- [ListDocumentClassifiersPaginatorName](./literals.md#listdocumentclassifierspaginatorname)
- [ListDominantLanguageDetectionJobsPaginatorName](./literals.md#listdominantlanguagedetectionjobspaginatorname)
- [ListEntitiesDetectionJobsPaginatorName](./literals.md#listentitiesdetectionjobspaginatorname)
- [ListEntityRecognizersPaginatorName](./literals.md#listentityrecognizerspaginatorname)
- [ListKeyPhrasesDetectionJobsPaginatorName](./literals.md#listkeyphrasesdetectionjobspaginatorname)
- [ListSentimentDetectionJobsPaginatorName](./literals.md#listsentimentdetectionjobspaginatorname)
- [ListTopicsDetectionJobsPaginatorName](./literals.md#listtopicsdetectionjobspaginatorname)
- [ModelStatus](./literals.md#modelstatus)
- [PartOfSpeechTagType](./literals.md#partofspeechtagtype)
- [PiiEntitiesDetectionMaskMode](./literals.md#piientitiesdetectionmaskmode)
- [PiiEntitiesDetectionMode](./literals.md#piientitiesdetectionmode)
- [PiiEntityType](./literals.md#piientitytype)
- [SentimentType](./literals.md#sentimenttype)
- [SyntaxLanguageCode](./literals.md#syntaxlanguagecode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_comprehend.type_defs import AugmentedManifestsListItemTypeDef, ...
```

- [AugmentedManifestsListItemTypeDef](./type_defs.md#augmentedmanifestslistitemtypedef)
- [BatchDetectDominantLanguageItemResultTypeDef](./type_defs.md#batchdetectdominantlanguageitemresulttypedef)
- [BatchDetectDominantLanguageResponseTypeDef](./type_defs.md#batchdetectdominantlanguageresponsetypedef)
- [BatchDetectEntitiesItemResultTypeDef](./type_defs.md#batchdetectentitiesitemresulttypedef)
- [BatchDetectEntitiesResponseTypeDef](./type_defs.md#batchdetectentitiesresponsetypedef)
- [BatchDetectKeyPhrasesItemResultTypeDef](./type_defs.md#batchdetectkeyphrasesitemresulttypedef)
- [BatchDetectKeyPhrasesResponseTypeDef](./type_defs.md#batchdetectkeyphrasesresponsetypedef)
- [BatchDetectSentimentItemResultTypeDef](./type_defs.md#batchdetectsentimentitemresulttypedef)
- [BatchDetectSentimentResponseTypeDef](./type_defs.md#batchdetectsentimentresponsetypedef)
- [BatchDetectSyntaxItemResultTypeDef](./type_defs.md#batchdetectsyntaxitemresulttypedef)
- [BatchDetectSyntaxResponseTypeDef](./type_defs.md#batchdetectsyntaxresponsetypedef)
- [BatchItemErrorTypeDef](./type_defs.md#batchitemerrortypedef)
- [ClassifierEvaluationMetricsTypeDef](./type_defs.md#classifierevaluationmetricstypedef)
- [ClassifierMetadataTypeDef](./type_defs.md#classifiermetadatatypedef)
- [ClassifyDocumentResponseTypeDef](./type_defs.md#classifydocumentresponsetypedef)
- [ContainsPiiEntitiesResponseTypeDef](./type_defs.md#containspiientitiesresponsetypedef)
- [CreateDocumentClassifierResponseTypeDef](./type_defs.md#createdocumentclassifierresponsetypedef)
- [CreateEndpointResponseTypeDef](./type_defs.md#createendpointresponsetypedef)
- [CreateEntityRecognizerResponseTypeDef](./type_defs.md#createentityrecognizerresponsetypedef)
- [DescribeDocumentClassificationJobResponseTypeDef](./type_defs.md#describedocumentclassificationjobresponsetypedef)
- [DescribeDocumentClassifierResponseTypeDef](./type_defs.md#describedocumentclassifierresponsetypedef)
- [DescribeDominantLanguageDetectionJobResponseTypeDef](./type_defs.md#describedominantlanguagedetectionjobresponsetypedef)
- [DescribeEndpointResponseTypeDef](./type_defs.md#describeendpointresponsetypedef)
- [DescribeEntitiesDetectionJobResponseTypeDef](./type_defs.md#describeentitiesdetectionjobresponsetypedef)
- [DescribeEntityRecognizerResponseTypeDef](./type_defs.md#describeentityrecognizerresponsetypedef)
- [DescribeEventsDetectionJobResponseTypeDef](./type_defs.md#describeeventsdetectionjobresponsetypedef)
- [DescribeKeyPhrasesDetectionJobResponseTypeDef](./type_defs.md#describekeyphrasesdetectionjobresponsetypedef)
- [DescribePiiEntitiesDetectionJobResponseTypeDef](./type_defs.md#describepiientitiesdetectionjobresponsetypedef)
- [DescribeSentimentDetectionJobResponseTypeDef](./type_defs.md#describesentimentdetectionjobresponsetypedef)
- [DescribeTopicsDetectionJobResponseTypeDef](./type_defs.md#describetopicsdetectionjobresponsetypedef)
- [DetectDominantLanguageResponseTypeDef](./type_defs.md#detectdominantlanguageresponsetypedef)
- [DetectEntitiesResponseTypeDef](./type_defs.md#detectentitiesresponsetypedef)
- [DetectKeyPhrasesResponseTypeDef](./type_defs.md#detectkeyphrasesresponsetypedef)
- [DetectPiiEntitiesResponseTypeDef](./type_defs.md#detectpiientitiesresponsetypedef)
- [DetectSentimentResponseTypeDef](./type_defs.md#detectsentimentresponsetypedef)
- [DetectSyntaxResponseTypeDef](./type_defs.md#detectsyntaxresponsetypedef)
- [DocumentClassTypeDef](./type_defs.md#documentclasstypedef)
- [DocumentClassificationJobFilterTypeDef](./type_defs.md#documentclassificationjobfiltertypedef)
- [DocumentClassificationJobPropertiesTypeDef](./type_defs.md#documentclassificationjobpropertiestypedef)
- [DocumentClassifierFilterTypeDef](./type_defs.md#documentclassifierfiltertypedef)
- [DocumentClassifierInputDataConfigTypeDef](./type_defs.md#documentclassifierinputdataconfigtypedef)
- [DocumentClassifierOutputDataConfigTypeDef](./type_defs.md#documentclassifieroutputdataconfigtypedef)
- [DocumentClassifierPropertiesTypeDef](./type_defs.md#documentclassifierpropertiestypedef)
- [DocumentLabelTypeDef](./type_defs.md#documentlabeltypedef)
- [DominantLanguageDetectionJobFilterTypeDef](./type_defs.md#dominantlanguagedetectionjobfiltertypedef)
- [DominantLanguageDetectionJobPropertiesTypeDef](./type_defs.md#dominantlanguagedetectionjobpropertiestypedef)
- [DominantLanguageTypeDef](./type_defs.md#dominantlanguagetypedef)
- [EndpointFilterTypeDef](./type_defs.md#endpointfiltertypedef)
- [EndpointPropertiesTypeDef](./type_defs.md#endpointpropertiestypedef)
- [EntitiesDetectionJobFilterTypeDef](./type_defs.md#entitiesdetectionjobfiltertypedef)
- [EntitiesDetectionJobPropertiesTypeDef](./type_defs.md#entitiesdetectionjobpropertiestypedef)
- [EntityLabelTypeDef](./type_defs.md#entitylabeltypedef)
- [EntityRecognizerAnnotationsTypeDef](./type_defs.md#entityrecognizerannotationstypedef)
- [EntityRecognizerDocumentsTypeDef](./type_defs.md#entityrecognizerdocumentstypedef)
- [EntityRecognizerEntityListTypeDef](./type_defs.md#entityrecognizerentitylisttypedef)
- [EntityRecognizerEvaluationMetricsTypeDef](./type_defs.md#entityrecognizerevaluationmetricstypedef)
- [EntityRecognizerFilterTypeDef](./type_defs.md#entityrecognizerfiltertypedef)
- [EntityRecognizerInputDataConfigTypeDef](./type_defs.md#entityrecognizerinputdataconfigtypedef)
- [EntityRecognizerMetadataEntityTypesListItemTypeDef](./type_defs.md#entityrecognizermetadataentitytypeslistitemtypedef)
- [EntityRecognizerMetadataTypeDef](./type_defs.md#entityrecognizermetadatatypedef)
- [EntityRecognizerPropertiesTypeDef](./type_defs.md#entityrecognizerpropertiestypedef)
- [EntityTypeDef](./type_defs.md#entitytypedef)
- [EntityTypesEvaluationMetricsTypeDef](./type_defs.md#entitytypesevaluationmetricstypedef)
- [EntityTypesListItemTypeDef](./type_defs.md#entitytypeslistitemtypedef)
- [EventsDetectionJobFilterTypeDef](./type_defs.md#eventsdetectionjobfiltertypedef)
- [EventsDetectionJobPropertiesTypeDef](./type_defs.md#eventsdetectionjobpropertiestypedef)
- [InputDataConfigTypeDef](./type_defs.md#inputdataconfigtypedef)
- [KeyPhraseTypeDef](./type_defs.md#keyphrasetypedef)
- [KeyPhrasesDetectionJobFilterTypeDef](./type_defs.md#keyphrasesdetectionjobfiltertypedef)
- [KeyPhrasesDetectionJobPropertiesTypeDef](./type_defs.md#keyphrasesdetectionjobpropertiestypedef)
- [ListDocumentClassificationJobsResponseTypeDef](./type_defs.md#listdocumentclassificationjobsresponsetypedef)
- [ListDocumentClassifiersResponseTypeDef](./type_defs.md#listdocumentclassifiersresponsetypedef)
- [ListDominantLanguageDetectionJobsResponseTypeDef](./type_defs.md#listdominantlanguagedetectionjobsresponsetypedef)
- [ListEndpointsResponseTypeDef](./type_defs.md#listendpointsresponsetypedef)
- [ListEntitiesDetectionJobsResponseTypeDef](./type_defs.md#listentitiesdetectionjobsresponsetypedef)
- [ListEntityRecognizersResponseTypeDef](./type_defs.md#listentityrecognizersresponsetypedef)
- [ListEventsDetectionJobsResponseTypeDef](./type_defs.md#listeventsdetectionjobsresponsetypedef)
- [ListKeyPhrasesDetectionJobsResponseTypeDef](./type_defs.md#listkeyphrasesdetectionjobsresponsetypedef)
- [ListPiiEntitiesDetectionJobsResponseTypeDef](./type_defs.md#listpiientitiesdetectionjobsresponsetypedef)
- [ListSentimentDetectionJobsResponseTypeDef](./type_defs.md#listsentimentdetectionjobsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTopicsDetectionJobsResponseTypeDef](./type_defs.md#listtopicsdetectionjobsresponsetypedef)
- [OutputDataConfigTypeDef](./type_defs.md#outputdataconfigtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PartOfSpeechTagTypeDef](./type_defs.md#partofspeechtagtypedef)
- [PiiEntitiesDetectionJobFilterTypeDef](./type_defs.md#piientitiesdetectionjobfiltertypedef)
- [PiiEntitiesDetectionJobPropertiesTypeDef](./type_defs.md#piientitiesdetectionjobpropertiestypedef)
- [PiiEntityTypeDef](./type_defs.md#piientitytypedef)
- [PiiOutputDataConfigTypeDef](./type_defs.md#piioutputdataconfigtypedef)
- [RedactionConfigTypeDef](./type_defs.md#redactionconfigtypedef)
- [SentimentDetectionJobFilterTypeDef](./type_defs.md#sentimentdetectionjobfiltertypedef)
- [SentimentDetectionJobPropertiesTypeDef](./type_defs.md#sentimentdetectionjobpropertiestypedef)
- [SentimentScoreTypeDef](./type_defs.md#sentimentscoretypedef)
- [StartDocumentClassificationJobResponseTypeDef](./type_defs.md#startdocumentclassificationjobresponsetypedef)
- [StartDominantLanguageDetectionJobResponseTypeDef](./type_defs.md#startdominantlanguagedetectionjobresponsetypedef)
- [StartEntitiesDetectionJobResponseTypeDef](./type_defs.md#startentitiesdetectionjobresponsetypedef)
- [StartEventsDetectionJobResponseTypeDef](./type_defs.md#starteventsdetectionjobresponsetypedef)
- [StartKeyPhrasesDetectionJobResponseTypeDef](./type_defs.md#startkeyphrasesdetectionjobresponsetypedef)
- [StartPiiEntitiesDetectionJobResponseTypeDef](./type_defs.md#startpiientitiesdetectionjobresponsetypedef)
- [StartSentimentDetectionJobResponseTypeDef](./type_defs.md#startsentimentdetectionjobresponsetypedef)
- [StartTopicsDetectionJobResponseTypeDef](./type_defs.md#starttopicsdetectionjobresponsetypedef)
- [StopDominantLanguageDetectionJobResponseTypeDef](./type_defs.md#stopdominantlanguagedetectionjobresponsetypedef)
- [StopEntitiesDetectionJobResponseTypeDef](./type_defs.md#stopentitiesdetectionjobresponsetypedef)
- [StopEventsDetectionJobResponseTypeDef](./type_defs.md#stopeventsdetectionjobresponsetypedef)
- [StopKeyPhrasesDetectionJobResponseTypeDef](./type_defs.md#stopkeyphrasesdetectionjobresponsetypedef)
- [StopPiiEntitiesDetectionJobResponseTypeDef](./type_defs.md#stoppiientitiesdetectionjobresponsetypedef)
- [StopSentimentDetectionJobResponseTypeDef](./type_defs.md#stopsentimentdetectionjobresponsetypedef)
- [SyntaxTokenTypeDef](./type_defs.md#syntaxtokentypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TopicsDetectionJobFilterTypeDef](./type_defs.md#topicsdetectionjobfiltertypedef)
- [TopicsDetectionJobPropertiesTypeDef](./type_defs.md#topicsdetectionjobpropertiestypedef)
- [VpcConfigTypeDef](./type_defs.md#vpcconfigtypedef)
