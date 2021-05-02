# Structures for boto3 Comprehend module

> [Index](../index.md) > [Comprehend](./index.md) > Structures

Auto-generated documentation for [Comprehend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend)
type annotations stubs module [mypy_boto3_comprehend](https://pypi.org/project/mypy-boto3-comprehend/).

- [Structures for boto3 Comprehend module](#structures-for-boto3-comprehend-module)
  - [AugmentedManifestsListItemTypeDef](#augmentedmanifestslistitemtypedef)
  - [BatchDetectDominantLanguageItemResultTypeDef](#batchdetectdominantlanguageitemresulttypedef)
  - [BatchDetectEntitiesItemResultTypeDef](#batchdetectentitiesitemresulttypedef)
  - [BatchDetectKeyPhrasesItemResultTypeDef](#batchdetectkeyphrasesitemresulttypedef)
  - [BatchDetectSentimentItemResultTypeDef](#batchdetectsentimentitemresulttypedef)
  - [BatchDetectSyntaxItemResultTypeDef](#batchdetectsyntaxitemresulttypedef)
  - [BatchItemErrorTypeDef](#batchitemerrortypedef)
  - [ClassifierEvaluationMetricsTypeDef](#classifierevaluationmetricstypedef)
  - [ClassifierMetadataTypeDef](#classifiermetadatatypedef)
  - [DocumentClassTypeDef](#documentclasstypedef)
  - [DocumentClassificationJobPropertiesTypeDef](#documentclassificationjobpropertiestypedef)
  - [DocumentClassifierInputDataConfigTypeDef](#documentclassifierinputdataconfigtypedef)
  - [DocumentClassifierOutputDataConfigTypeDef](#documentclassifieroutputdataconfigtypedef)
  - [DocumentClassifierPropertiesTypeDef](#documentclassifierpropertiestypedef)
  - [DocumentLabelTypeDef](#documentlabeltypedef)
  - [DominantLanguageDetectionJobPropertiesTypeDef](#dominantlanguagedetectionjobpropertiestypedef)
  - [DominantLanguageTypeDef](#dominantlanguagetypedef)
  - [EndpointPropertiesTypeDef](#endpointpropertiestypedef)
  - [EntitiesDetectionJobPropertiesTypeDef](#entitiesdetectionjobpropertiestypedef)
  - [EntityLabelTypeDef](#entitylabeltypedef)
  - [EntityRecognizerAnnotationsTypeDef](#entityrecognizerannotationstypedef)
  - [EntityRecognizerDocumentsTypeDef](#entityrecognizerdocumentstypedef)
  - [EntityRecognizerEntityListTypeDef](#entityrecognizerentitylisttypedef)
  - [EntityRecognizerEvaluationMetricsTypeDef](#entityrecognizerevaluationmetricstypedef)
  - [EntityRecognizerInputDataConfigTypeDef](#entityrecognizerinputdataconfigtypedef)
  - [EntityRecognizerMetadataEntityTypesListItemTypeDef](#entityrecognizermetadataentitytypeslistitemtypedef)
  - [EntityRecognizerMetadataTypeDef](#entityrecognizermetadatatypedef)
  - [EntityRecognizerPropertiesTypeDef](#entityrecognizerpropertiestypedef)
  - [EntityTypeDef](#entitytypedef)
  - [EntityTypesEvaluationMetricsTypeDef](#entitytypesevaluationmetricstypedef)
  - [EntityTypesListItemTypeDef](#entitytypeslistitemtypedef)
  - [EventsDetectionJobPropertiesTypeDef](#eventsdetectionjobpropertiestypedef)
  - [InputDataConfigTypeDef](#inputdataconfigtypedef)
  - [KeyPhraseTypeDef](#keyphrasetypedef)
  - [KeyPhrasesDetectionJobPropertiesTypeDef](#keyphrasesdetectionjobpropertiestypedef)
  - [OutputDataConfigTypeDef](#outputdataconfigtypedef)
  - [PartOfSpeechTagTypeDef](#partofspeechtagtypedef)
  - [PiiEntitiesDetectionJobPropertiesTypeDef](#piientitiesdetectionjobpropertiestypedef)
  - [PiiEntityTypeDef](#piientitytypedef)
  - [PiiOutputDataConfigTypeDef](#piioutputdataconfigtypedef)
  - [RedactionConfigTypeDef](#redactionconfigtypedef)
  - [SentimentDetectionJobPropertiesTypeDef](#sentimentdetectionjobpropertiestypedef)
  - [SentimentScoreTypeDef](#sentimentscoretypedef)
  - [SyntaxTokenTypeDef](#syntaxtokentypedef)
  - [TagTypeDef](#tagtypedef)
  - [TopicsDetectionJobPropertiesTypeDef](#topicsdetectionjobpropertiestypedef)
  - [VpcConfigTypeDef](#vpcconfigtypedef)
  - [BatchDetectDominantLanguageResponseTypeDef](#batchdetectdominantlanguageresponsetypedef)
  - [BatchDetectEntitiesResponseTypeDef](#batchdetectentitiesresponsetypedef)
  - [BatchDetectKeyPhrasesResponseTypeDef](#batchdetectkeyphrasesresponsetypedef)
  - [BatchDetectSentimentResponseTypeDef](#batchdetectsentimentresponsetypedef)
  - [BatchDetectSyntaxResponseTypeDef](#batchdetectsyntaxresponsetypedef)
  - [ClassifyDocumentResponseTypeDef](#classifydocumentresponsetypedef)
  - [ContainsPiiEntitiesResponseTypeDef](#containspiientitiesresponsetypedef)
  - [CreateDocumentClassifierResponseTypeDef](#createdocumentclassifierresponsetypedef)
  - [CreateEndpointResponseTypeDef](#createendpointresponsetypedef)
  - [CreateEntityRecognizerResponseTypeDef](#createentityrecognizerresponsetypedef)
  - [DescribeDocumentClassificationJobResponseTypeDef](#describedocumentclassificationjobresponsetypedef)
  - [DescribeDocumentClassifierResponseTypeDef](#describedocumentclassifierresponsetypedef)
  - [DescribeDominantLanguageDetectionJobResponseTypeDef](#describedominantlanguagedetectionjobresponsetypedef)
  - [DescribeEndpointResponseTypeDef](#describeendpointresponsetypedef)
  - [DescribeEntitiesDetectionJobResponseTypeDef](#describeentitiesdetectionjobresponsetypedef)
  - [DescribeEntityRecognizerResponseTypeDef](#describeentityrecognizerresponsetypedef)
  - [DescribeEventsDetectionJobResponseTypeDef](#describeeventsdetectionjobresponsetypedef)
  - [DescribeKeyPhrasesDetectionJobResponseTypeDef](#describekeyphrasesdetectionjobresponsetypedef)
  - [DescribePiiEntitiesDetectionJobResponseTypeDef](#describepiientitiesdetectionjobresponsetypedef)
  - [DescribeSentimentDetectionJobResponseTypeDef](#describesentimentdetectionjobresponsetypedef)
  - [DescribeTopicsDetectionJobResponseTypeDef](#describetopicsdetectionjobresponsetypedef)
  - [DetectDominantLanguageResponseTypeDef](#detectdominantlanguageresponsetypedef)
  - [DetectEntitiesResponseTypeDef](#detectentitiesresponsetypedef)
  - [DetectKeyPhrasesResponseTypeDef](#detectkeyphrasesresponsetypedef)
  - [DetectPiiEntitiesResponseTypeDef](#detectpiientitiesresponsetypedef)
  - [DetectSentimentResponseTypeDef](#detectsentimentresponsetypedef)
  - [DetectSyntaxResponseTypeDef](#detectsyntaxresponsetypedef)
  - [DocumentClassificationJobFilterTypeDef](#documentclassificationjobfiltertypedef)
  - [DocumentClassifierFilterTypeDef](#documentclassifierfiltertypedef)
  - [DominantLanguageDetectionJobFilterTypeDef](#dominantlanguagedetectionjobfiltertypedef)
  - [EndpointFilterTypeDef](#endpointfiltertypedef)
  - [EntitiesDetectionJobFilterTypeDef](#entitiesdetectionjobfiltertypedef)
  - [EntityRecognizerFilterTypeDef](#entityrecognizerfiltertypedef)
  - [EventsDetectionJobFilterTypeDef](#eventsdetectionjobfiltertypedef)
  - [KeyPhrasesDetectionJobFilterTypeDef](#keyphrasesdetectionjobfiltertypedef)
  - [ListDocumentClassificationJobsResponseTypeDef](#listdocumentclassificationjobsresponsetypedef)
  - [ListDocumentClassifiersResponseTypeDef](#listdocumentclassifiersresponsetypedef)
  - [ListDominantLanguageDetectionJobsResponseTypeDef](#listdominantlanguagedetectionjobsresponsetypedef)
  - [ListEndpointsResponseTypeDef](#listendpointsresponsetypedef)
  - [ListEntitiesDetectionJobsResponseTypeDef](#listentitiesdetectionjobsresponsetypedef)
  - [ListEntityRecognizersResponseTypeDef](#listentityrecognizersresponsetypedef)
  - [ListEventsDetectionJobsResponseTypeDef](#listeventsdetectionjobsresponsetypedef)
  - [ListKeyPhrasesDetectionJobsResponseTypeDef](#listkeyphrasesdetectionjobsresponsetypedef)
  - [ListPiiEntitiesDetectionJobsResponseTypeDef](#listpiientitiesdetectionjobsresponsetypedef)
  - [ListSentimentDetectionJobsResponseTypeDef](#listsentimentdetectionjobsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTopicsDetectionJobsResponseTypeDef](#listtopicsdetectionjobsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PiiEntitiesDetectionJobFilterTypeDef](#piientitiesdetectionjobfiltertypedef)
  - [SentimentDetectionJobFilterTypeDef](#sentimentdetectionjobfiltertypedef)
  - [StartDocumentClassificationJobResponseTypeDef](#startdocumentclassificationjobresponsetypedef)
  - [StartDominantLanguageDetectionJobResponseTypeDef](#startdominantlanguagedetectionjobresponsetypedef)
  - [StartEntitiesDetectionJobResponseTypeDef](#startentitiesdetectionjobresponsetypedef)
  - [StartEventsDetectionJobResponseTypeDef](#starteventsdetectionjobresponsetypedef)
  - [StartKeyPhrasesDetectionJobResponseTypeDef](#startkeyphrasesdetectionjobresponsetypedef)
  - [StartPiiEntitiesDetectionJobResponseTypeDef](#startpiientitiesdetectionjobresponsetypedef)
  - [StartSentimentDetectionJobResponseTypeDef](#startsentimentdetectionjobresponsetypedef)
  - [StartTopicsDetectionJobResponseTypeDef](#starttopicsdetectionjobresponsetypedef)
  - [StopDominantLanguageDetectionJobResponseTypeDef](#stopdominantlanguagedetectionjobresponsetypedef)
  - [StopEntitiesDetectionJobResponseTypeDef](#stopentitiesdetectionjobresponsetypedef)
  - [StopEventsDetectionJobResponseTypeDef](#stopeventsdetectionjobresponsetypedef)
  - [StopKeyPhrasesDetectionJobResponseTypeDef](#stopkeyphrasesdetectionjobresponsetypedef)
  - [StopPiiEntitiesDetectionJobResponseTypeDef](#stoppiientitiesdetectionjobresponsetypedef)
  - [StopSentimentDetectionJobResponseTypeDef](#stopsentimentdetectionjobresponsetypedef)
  - [TopicsDetectionJobFilterTypeDef](#topicsdetectionjobfiltertypedef)

## AugmentedManifestsListItemTypeDef

```python
from mypy_boto3_comprehend.type_defs import AugmentedManifestsListItemTypeDef
```


Required fields:
- `S3Uri`: `str`
- `AttributeNames`: `List[str]`




## BatchDetectDominantLanguageItemResultTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectDominantLanguageItemResultTypeDef
```




Optional fields:
- `Index`: `int`
- `Languages`: `List["DominantLanguageTypeDef"]`


## BatchDetectEntitiesItemResultTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectEntitiesItemResultTypeDef
```




Optional fields:
- `Index`: `int`
- `Entities`: `List["EntityTypeDef"]`


## BatchDetectKeyPhrasesItemResultTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectKeyPhrasesItemResultTypeDef
```




Optional fields:
- `Index`: `int`
- `KeyPhrases`: `List["KeyPhraseTypeDef"]`


## BatchDetectSentimentItemResultTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectSentimentItemResultTypeDef
```




Optional fields:
- `Index`: `int`
- `Sentiment`: `SentimentType`
- `SentimentScore`: `"SentimentScoreTypeDef"`


## BatchDetectSyntaxItemResultTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectSyntaxItemResultTypeDef
```




Optional fields:
- `Index`: `int`
- `SyntaxTokens`: `List["SyntaxTokenTypeDef"]`


## BatchItemErrorTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchItemErrorTypeDef
```




Optional fields:
- `Index`: `int`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## ClassifierEvaluationMetricsTypeDef

```python
from mypy_boto3_comprehend.type_defs import ClassifierEvaluationMetricsTypeDef
```




Optional fields:
- `Accuracy`: `float`
- `Precision`: `float`
- `Recall`: `float`
- `F1Score`: `float`
- `MicroPrecision`: `float`
- `MicroRecall`: `float`
- `MicroF1Score`: `float`
- `HammingLoss`: `float`


## ClassifierMetadataTypeDef

```python
from mypy_boto3_comprehend.type_defs import ClassifierMetadataTypeDef
```




Optional fields:
- `NumberOfLabels`: `int`
- `NumberOfTrainedDocuments`: `int`
- `NumberOfTestDocuments`: `int`
- `EvaluationMetrics`: `"ClassifierEvaluationMetricsTypeDef"`


## DocumentClassTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassTypeDef
```




Optional fields:
- `Name`: `str`
- `Score`: `float`


## DocumentClassificationJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassificationJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `DocumentClassifierArn`: `str`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`


## DocumentClassifierInputDataConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassifierInputDataConfigTypeDef
```




Optional fields:
- `DataFormat`: `DocumentClassifierDataFormat`
- `S3Uri`: `str`
- `LabelDelimiter`: `str`
- `AugmentedManifests`: `List["AugmentedManifestsListItemTypeDef"]`


## DocumentClassifierOutputDataConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassifierOutputDataConfigTypeDef
```




Optional fields:
- `S3Uri`: `str`
- `KmsKeyId`: `str`


## DocumentClassifierPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassifierPropertiesTypeDef
```




Optional fields:
- `DocumentClassifierArn`: `str`
- `LanguageCode`: `LanguageCode`
- `Status`: `ModelStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `TrainingStartTime`: `datetime`
- `TrainingEndTime`: `datetime`
- `InputDataConfig`: `"DocumentClassifierInputDataConfigTypeDef"`
- `OutputDataConfig`: `"DocumentClassifierOutputDataConfigTypeDef"`
- `ClassifierMetadata`: `"ClassifierMetadataTypeDef"`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `Mode`: `DocumentClassifierMode`
- `ModelKmsKeyId`: `str`


## DocumentLabelTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentLabelTypeDef
```




Optional fields:
- `Name`: `str`
- `Score`: `float`


## DominantLanguageDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import DominantLanguageDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`


## DominantLanguageTypeDef

```python
from mypy_boto3_comprehend.type_defs import DominantLanguageTypeDef
```




Optional fields:
- `LanguageCode`: `str`
- `Score`: `float`


## EndpointPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import EndpointPropertiesTypeDef
```




Optional fields:
- `EndpointArn`: `str`
- `Status`: `EndpointStatus`
- `Message`: `str`
- `ModelArn`: `str`
- `DesiredInferenceUnits`: `int`
- `CurrentInferenceUnits`: `int`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `DataAccessRoleArn`: `str`


## EntitiesDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntitiesDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `EntityRecognizerArn`: `str`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `LanguageCode`: `LanguageCode`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`


## EntityLabelTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityLabelTypeDef
```




Optional fields:
- `Name`: `PiiEntityType`
- `Score`: `float`


## EntityRecognizerAnnotationsTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerAnnotationsTypeDef
```


Required fields:
- `S3Uri`: `str`




## EntityRecognizerDocumentsTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerDocumentsTypeDef
```


Required fields:
- `S3Uri`: `str`




## EntityRecognizerEntityListTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerEntityListTypeDef
```


Required fields:
- `S3Uri`: `str`




## EntityRecognizerEvaluationMetricsTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerEvaluationMetricsTypeDef
```




Optional fields:
- `Precision`: `float`
- `Recall`: `float`
- `F1Score`: `float`


## EntityRecognizerInputDataConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerInputDataConfigTypeDef
```


Required fields:
- `EntityTypes`: `List["EntityTypesListItemTypeDef"]`



Optional fields:
- `DataFormat`: `EntityRecognizerDataFormat`
- `Documents`: `"EntityRecognizerDocumentsTypeDef"`
- `Annotations`: `"EntityRecognizerAnnotationsTypeDef"`
- `EntityList`: `"EntityRecognizerEntityListTypeDef"`
- `AugmentedManifests`: `List["AugmentedManifestsListItemTypeDef"]`


## EntityRecognizerMetadataEntityTypesListItemTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerMetadataEntityTypesListItemTypeDef
```




Optional fields:
- `Type`: `str`
- `EvaluationMetrics`: `"EntityTypesEvaluationMetricsTypeDef"`
- `NumberOfTrainMentions`: `int`


## EntityRecognizerMetadataTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerMetadataTypeDef
```




Optional fields:
- `NumberOfTrainedDocuments`: `int`
- `NumberOfTestDocuments`: `int`
- `EvaluationMetrics`: `"EntityRecognizerEvaluationMetricsTypeDef"`
- `EntityTypes`: `List["EntityRecognizerMetadataEntityTypesListItemTypeDef"]`


## EntityRecognizerPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerPropertiesTypeDef
```




Optional fields:
- `EntityRecognizerArn`: `str`
- `LanguageCode`: `LanguageCode`
- `Status`: `ModelStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `TrainingStartTime`: `datetime`
- `TrainingEndTime`: `datetime`
- `InputDataConfig`: `"EntityRecognizerInputDataConfigTypeDef"`
- `RecognizerMetadata`: `"EntityRecognizerMetadataTypeDef"`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`
- `ModelKmsKeyId`: `str`


## EntityTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityTypeDef
```




Optional fields:
- `Score`: `float`
- `Type`: `EntityType`
- `Text`: `str`
- `BeginOffset`: `int`
- `EndOffset`: `int`


## EntityTypesEvaluationMetricsTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityTypesEvaluationMetricsTypeDef
```




Optional fields:
- `Precision`: `float`
- `Recall`: `float`
- `F1Score`: `float`


## EntityTypesListItemTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityTypesListItemTypeDef
```


Required fields:
- `Type`: `str`




## EventsDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import EventsDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `LanguageCode`: `LanguageCode`
- `DataAccessRoleArn`: `str`
- `TargetEventTypes`: `List[str]`


## InputDataConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import InputDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`



Optional fields:
- `InputFormat`: `InputFormat`


## KeyPhraseTypeDef

```python
from mypy_boto3_comprehend.type_defs import KeyPhraseTypeDef
```




Optional fields:
- `Score`: `float`
- `Text`: `str`
- `BeginOffset`: `int`
- `EndOffset`: `int`


## KeyPhrasesDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import KeyPhrasesDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `LanguageCode`: `LanguageCode`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`


## OutputDataConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import OutputDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`



Optional fields:
- `KmsKeyId`: `str`


## PartOfSpeechTagTypeDef

```python
from mypy_boto3_comprehend.type_defs import PartOfSpeechTagTypeDef
```




Optional fields:
- `Tag`: `PartOfSpeechTagType`
- `Score`: `float`


## PiiEntitiesDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import PiiEntitiesDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"PiiOutputDataConfigTypeDef"`
- `RedactionConfig`: `"RedactionConfigTypeDef"`
- `LanguageCode`: `LanguageCode`
- `DataAccessRoleArn`: `str`
- `Mode`: `PiiEntitiesDetectionMode`


## PiiEntityTypeDef

```python
from mypy_boto3_comprehend.type_defs import PiiEntityTypeDef
```




Optional fields:
- `Score`: `float`
- `Type`: `PiiEntityType`
- `BeginOffset`: `int`
- `EndOffset`: `int`


## PiiOutputDataConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import PiiOutputDataConfigTypeDef
```


Required fields:
- `S3Uri`: `str`



Optional fields:
- `KmsKeyId`: `str`


## RedactionConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import RedactionConfigTypeDef
```




Optional fields:
- `PiiEntityTypes`: `List[PiiEntityType]`
- `MaskMode`: `PiiEntitiesDetectionMaskMode`
- `MaskCharacter`: `str`


## SentimentDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import SentimentDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `LanguageCode`: `LanguageCode`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`


## SentimentScoreTypeDef

```python
from mypy_boto3_comprehend.type_defs import SentimentScoreTypeDef
```




Optional fields:
- `Positive`: `float`
- `Negative`: `float`
- `Neutral`: `float`
- `Mixed`: `float`


## SyntaxTokenTypeDef

```python
from mypy_boto3_comprehend.type_defs import SyntaxTokenTypeDef
```




Optional fields:
- `TokenId`: `int`
- `Text`: `str`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `PartOfSpeech`: `"PartOfSpeechTagTypeDef"`


## TagTypeDef

```python
from mypy_boto3_comprehend.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## TopicsDetectionJobPropertiesTypeDef

```python
from mypy_boto3_comprehend.type_defs import TopicsDetectionJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `NumberOfTopics`: `int`
- `DataAccessRoleArn`: `str`
- `VolumeKmsKeyId`: `str`
- `VpcConfig`: `"VpcConfigTypeDef"`


## VpcConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import VpcConfigTypeDef
```


Required fields:
- `SecurityGroupIds`: `List[str]`
- `Subnets`: `List[str]`




## BatchDetectDominantLanguageResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectDominantLanguageResponseTypeDef
```


Required fields:
- `ResultList`: `List["BatchDetectDominantLanguageItemResultTypeDef"]`
- `ErrorList`: `List["BatchItemErrorTypeDef"]`




## BatchDetectEntitiesResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectEntitiesResponseTypeDef
```


Required fields:
- `ResultList`: `List["BatchDetectEntitiesItemResultTypeDef"]`
- `ErrorList`: `List["BatchItemErrorTypeDef"]`




## BatchDetectKeyPhrasesResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectKeyPhrasesResponseTypeDef
```


Required fields:
- `ResultList`: `List["BatchDetectKeyPhrasesItemResultTypeDef"]`
- `ErrorList`: `List["BatchItemErrorTypeDef"]`




## BatchDetectSentimentResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectSentimentResponseTypeDef
```


Required fields:
- `ResultList`: `List["BatchDetectSentimentItemResultTypeDef"]`
- `ErrorList`: `List["BatchItemErrorTypeDef"]`




## BatchDetectSyntaxResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import BatchDetectSyntaxResponseTypeDef
```


Required fields:
- `ResultList`: `List["BatchDetectSyntaxItemResultTypeDef"]`
- `ErrorList`: `List["BatchItemErrorTypeDef"]`




## ClassifyDocumentResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ClassifyDocumentResponseTypeDef
```




Optional fields:
- `Classes`: `List["DocumentClassTypeDef"]`
- `Labels`: `List["DocumentLabelTypeDef"]`


## ContainsPiiEntitiesResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ContainsPiiEntitiesResponseTypeDef
```




Optional fields:
- `Labels`: `List["EntityLabelTypeDef"]`


## CreateDocumentClassifierResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import CreateDocumentClassifierResponseTypeDef
```




Optional fields:
- `DocumentClassifierArn`: `str`


## CreateEndpointResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import CreateEndpointResponseTypeDef
```




Optional fields:
- `EndpointArn`: `str`


## CreateEntityRecognizerResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import CreateEntityRecognizerResponseTypeDef
```




Optional fields:
- `EntityRecognizerArn`: `str`


## DescribeDocumentClassificationJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeDocumentClassificationJobResponseTypeDef
```




Optional fields:
- `DocumentClassificationJobProperties`: `"DocumentClassificationJobPropertiesTypeDef"`


## DescribeDocumentClassifierResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeDocumentClassifierResponseTypeDef
```




Optional fields:
- `DocumentClassifierProperties`: `"DocumentClassifierPropertiesTypeDef"`


## DescribeDominantLanguageDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeDominantLanguageDetectionJobResponseTypeDef
```




Optional fields:
- `DominantLanguageDetectionJobProperties`: `"DominantLanguageDetectionJobPropertiesTypeDef"`


## DescribeEndpointResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeEndpointResponseTypeDef
```




Optional fields:
- `EndpointProperties`: `"EndpointPropertiesTypeDef"`


## DescribeEntitiesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeEntitiesDetectionJobResponseTypeDef
```




Optional fields:
- `EntitiesDetectionJobProperties`: `"EntitiesDetectionJobPropertiesTypeDef"`


## DescribeEntityRecognizerResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeEntityRecognizerResponseTypeDef
```




Optional fields:
- `EntityRecognizerProperties`: `"EntityRecognizerPropertiesTypeDef"`


## DescribeEventsDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeEventsDetectionJobResponseTypeDef
```




Optional fields:
- `EventsDetectionJobProperties`: `"EventsDetectionJobPropertiesTypeDef"`


## DescribeKeyPhrasesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeKeyPhrasesDetectionJobResponseTypeDef
```




Optional fields:
- `KeyPhrasesDetectionJobProperties`: `"KeyPhrasesDetectionJobPropertiesTypeDef"`


## DescribePiiEntitiesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribePiiEntitiesDetectionJobResponseTypeDef
```




Optional fields:
- `PiiEntitiesDetectionJobProperties`: `"PiiEntitiesDetectionJobPropertiesTypeDef"`


## DescribeSentimentDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeSentimentDetectionJobResponseTypeDef
```




Optional fields:
- `SentimentDetectionJobProperties`: `"SentimentDetectionJobPropertiesTypeDef"`


## DescribeTopicsDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DescribeTopicsDetectionJobResponseTypeDef
```




Optional fields:
- `TopicsDetectionJobProperties`: `"TopicsDetectionJobPropertiesTypeDef"`


## DetectDominantLanguageResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DetectDominantLanguageResponseTypeDef
```




Optional fields:
- `Languages`: `List["DominantLanguageTypeDef"]`


## DetectEntitiesResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DetectEntitiesResponseTypeDef
```




Optional fields:
- `Entities`: `List["EntityTypeDef"]`


## DetectKeyPhrasesResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DetectKeyPhrasesResponseTypeDef
```




Optional fields:
- `KeyPhrases`: `List["KeyPhraseTypeDef"]`


## DetectPiiEntitiesResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DetectPiiEntitiesResponseTypeDef
```




Optional fields:
- `Entities`: `List["PiiEntityTypeDef"]`


## DetectSentimentResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DetectSentimentResponseTypeDef
```




Optional fields:
- `Sentiment`: `SentimentType`
- `SentimentScore`: `"SentimentScoreTypeDef"`


## DetectSyntaxResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import DetectSyntaxResponseTypeDef
```




Optional fields:
- `SyntaxTokens`: `List["SyntaxTokenTypeDef"]`


## DocumentClassificationJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassificationJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## DocumentClassifierFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import DocumentClassifierFilterTypeDef
```




Optional fields:
- `Status`: `ModelStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## DominantLanguageDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import DominantLanguageDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## EndpointFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import EndpointFilterTypeDef
```




Optional fields:
- `ModelArn`: `str`
- `Status`: `EndpointStatus`
- `CreationTimeBefore`: `datetime`
- `CreationTimeAfter`: `datetime`


## EntitiesDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntitiesDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## EntityRecognizerFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import EntityRecognizerFilterTypeDef
```




Optional fields:
- `Status`: `ModelStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## EventsDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import EventsDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## KeyPhrasesDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import KeyPhrasesDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## ListDocumentClassificationJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListDocumentClassificationJobsResponseTypeDef
```




Optional fields:
- `DocumentClassificationJobPropertiesList`: `List["DocumentClassificationJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListDocumentClassifiersResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListDocumentClassifiersResponseTypeDef
```




Optional fields:
- `DocumentClassifierPropertiesList`: `List["DocumentClassifierPropertiesTypeDef"]`
- `NextToken`: `str`


## ListDominantLanguageDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListDominantLanguageDetectionJobsResponseTypeDef
```




Optional fields:
- `DominantLanguageDetectionJobPropertiesList`: `List["DominantLanguageDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListEndpointsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListEndpointsResponseTypeDef
```




Optional fields:
- `EndpointPropertiesList`: `List["EndpointPropertiesTypeDef"]`
- `NextToken`: `str`


## ListEntitiesDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListEntitiesDetectionJobsResponseTypeDef
```




Optional fields:
- `EntitiesDetectionJobPropertiesList`: `List["EntitiesDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListEntityRecognizersResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListEntityRecognizersResponseTypeDef
```




Optional fields:
- `EntityRecognizerPropertiesList`: `List["EntityRecognizerPropertiesTypeDef"]`
- `NextToken`: `str`


## ListEventsDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListEventsDetectionJobsResponseTypeDef
```




Optional fields:
- `EventsDetectionJobPropertiesList`: `List["EventsDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListKeyPhrasesDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListKeyPhrasesDetectionJobsResponseTypeDef
```




Optional fields:
- `KeyPhrasesDetectionJobPropertiesList`: `List["KeyPhrasesDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListPiiEntitiesDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListPiiEntitiesDetectionJobsResponseTypeDef
```




Optional fields:
- `PiiEntitiesDetectionJobPropertiesList`: `List["PiiEntitiesDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListSentimentDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListSentimentDetectionJobsResponseTypeDef
```




Optional fields:
- `SentimentDetectionJobPropertiesList`: `List["SentimentDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `Tags`: `List["TagTypeDef"]`


## ListTopicsDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import ListTopicsDetectionJobsResponseTypeDef
```




Optional fields:
- `TopicsDetectionJobPropertiesList`: `List["TopicsDetectionJobPropertiesTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_comprehend.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PiiEntitiesDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import PiiEntitiesDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## SentimentDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import SentimentDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## StartDocumentClassificationJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartDocumentClassificationJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartDominantLanguageDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartDominantLanguageDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartEntitiesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartEntitiesDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartEventsDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartEventsDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartKeyPhrasesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartKeyPhrasesDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartPiiEntitiesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartPiiEntitiesDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartSentimentDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartSentimentDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StartTopicsDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StartTopicsDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopDominantLanguageDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StopDominantLanguageDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopEntitiesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StopEntitiesDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopEventsDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StopEventsDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopKeyPhrasesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StopKeyPhrasesDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopPiiEntitiesDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StopPiiEntitiesDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## StopSentimentDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehend.type_defs import StopSentimentDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobStatus`: `JobStatus`


## TopicsDetectionJobFilterTypeDef

```python
from mypy_boto3_comprehend.type_defs import TopicsDetectionJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`

