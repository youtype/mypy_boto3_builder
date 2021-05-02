# Structures for boto3 FraudDetector module

> [Index](../index.md) > [FraudDetector](./index.md) > Structures

Auto-generated documentation for [FraudDetector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector)
type annotations stubs module [mypy_boto3_frauddetector](https://pypi.org/project/mypy-boto3-frauddetector/).

- [Structures for boto3 FraudDetector module](#structures-for-boto3-frauddetector-module)
  - [BatchCreateVariableErrorTypeDef](#batchcreatevariableerrortypedef)
  - [BatchCreateVariableResultTypeDef](#batchcreatevariableresulttypedef)
  - [BatchGetVariableErrorTypeDef](#batchgetvariableerrortypedef)
  - [BatchGetVariableResultTypeDef](#batchgetvariableresulttypedef)
  - [BatchPredictionTypeDef](#batchpredictiontypedef)
  - [CreateDetectorVersionResultTypeDef](#createdetectorversionresulttypedef)
  - [CreateModelVersionResultTypeDef](#createmodelversionresulttypedef)
  - [CreateRuleResultTypeDef](#createruleresulttypedef)
  - [DataValidationMetricsTypeDef](#datavalidationmetricstypedef)
  - [DescribeDetectorResultTypeDef](#describedetectorresulttypedef)
  - [DescribeModelVersionsResultTypeDef](#describemodelversionsresulttypedef)
  - [DetectorTypeDef](#detectortypedef)
  - [DetectorVersionSummaryTypeDef](#detectorversionsummarytypedef)
  - [EntityTypeDef](#entitytypedef)
  - [EntityTypeTypeDef](#entitytypetypedef)
  - [EventTypeTypeDef](#eventtypetypedef)
  - [ExternalEventsDetailTypeDef](#externaleventsdetailtypedef)
  - [ExternalModelTypeDef](#externalmodeltypedef)
  - [FieldValidationMessageTypeDef](#fieldvalidationmessagetypedef)
  - [FileValidationMessageTypeDef](#filevalidationmessagetypedef)
  - [GetBatchPredictionJobsResultTypeDef](#getbatchpredictionjobsresulttypedef)
  - [GetDetectorVersionResultTypeDef](#getdetectorversionresulttypedef)
  - [GetDetectorsResultTypeDef](#getdetectorsresulttypedef)
  - [GetEntityTypesResultTypeDef](#getentitytypesresulttypedef)
  - [GetEventPredictionResultTypeDef](#geteventpredictionresulttypedef)
  - [GetEventTypesResultTypeDef](#geteventtypesresulttypedef)
  - [GetExternalModelsResultTypeDef](#getexternalmodelsresulttypedef)
  - [GetKMSEncryptionKeyResultTypeDef](#getkmsencryptionkeyresulttypedef)
  - [GetLabelsResultTypeDef](#getlabelsresulttypedef)
  - [GetModelVersionResultTypeDef](#getmodelversionresulttypedef)
  - [GetModelsResultTypeDef](#getmodelsresulttypedef)
  - [GetOutcomesResultTypeDef](#getoutcomesresulttypedef)
  - [GetRulesResultTypeDef](#getrulesresulttypedef)
  - [GetVariablesResultTypeDef](#getvariablesresulttypedef)
  - [KMSKeyTypeDef](#kmskeytypedef)
  - [LabelSchemaTypeDef](#labelschematypedef)
  - [LabelTypeDef](#labeltypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [MetricDataPointTypeDef](#metricdatapointtypedef)
  - [ModelEndpointDataBlobTypeDef](#modelendpointdatablobtypedef)
  - [ModelInputConfigurationTypeDef](#modelinputconfigurationtypedef)
  - [ModelOutputConfigurationTypeDef](#modeloutputconfigurationtypedef)
  - [ModelScoresTypeDef](#modelscorestypedef)
  - [ModelTypeDef](#modeltypedef)
  - [ModelVersionDetailTypeDef](#modelversiondetailtypedef)
  - [ModelVersionTypeDef](#modelversiontypedef)
  - [OutcomeTypeDef](#outcometypedef)
  - [RuleDetailTypeDef](#ruledetailtypedef)
  - [RuleResultTypeDef](#ruleresulttypedef)
  - [RuleTypeDef](#ruletypedef)
  - [TagTypeDef](#tagtypedef)
  - [TrainingDataSchemaTypeDef](#trainingdataschematypedef)
  - [TrainingMetricsTypeDef](#trainingmetricstypedef)
  - [TrainingResultTypeDef](#trainingresulttypedef)
  - [UpdateModelVersionResultTypeDef](#updatemodelversionresulttypedef)
  - [UpdateRuleVersionResultTypeDef](#updateruleversionresulttypedef)
  - [VariableEntryTypeDef](#variableentrytypedef)
  - [VariableTypeDef](#variabletypedef)

## BatchCreateVariableErrorTypeDef

```python
from mypy_boto3_frauddetector.type_defs import BatchCreateVariableErrorTypeDef
```




Optional fields:
- `name`: `str`
- `code`: `int`
- `message`: `str`


## BatchCreateVariableResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import BatchCreateVariableResultTypeDef
```




Optional fields:
- `errors`: `List["BatchCreateVariableErrorTypeDef"]`


## BatchGetVariableErrorTypeDef

```python
from mypy_boto3_frauddetector.type_defs import BatchGetVariableErrorTypeDef
```




Optional fields:
- `name`: `str`
- `code`: `int`
- `message`: `str`


## BatchGetVariableResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import BatchGetVariableResultTypeDef
```




Optional fields:
- `variables`: `List["VariableTypeDef"]`
- `errors`: `List["BatchGetVariableErrorTypeDef"]`


## BatchPredictionTypeDef

```python
from mypy_boto3_frauddetector.type_defs import BatchPredictionTypeDef
```




Optional fields:
- `jobId`: `str`
- `status`: `AsyncJobStatus`
- `failureReason`: `str`
- `startTime`: `str`
- `completionTime`: `str`
- `lastHeartbeatTime`: `str`
- `inputPath`: `str`
- `outputPath`: `str`
- `eventTypeName`: `str`
- `detectorName`: `str`
- `detectorVersion`: `str`
- `iamRoleArn`: `str`
- `arn`: `str`
- `processedRecordsCount`: `int`
- `totalRecordsCount`: `int`


## CreateDetectorVersionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import CreateDetectorVersionResultTypeDef
```




Optional fields:
- `detectorId`: `str`
- `detectorVersionId`: `str`
- `status`: `DetectorVersionStatus`


## CreateModelVersionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import CreateModelVersionResultTypeDef
```




Optional fields:
- `modelId`: `str`
- `modelType`: `Literal['ONLINE_FRAUD_INSIGHTS']`
- `modelVersionNumber`: `str`
- `status`: `str`


## CreateRuleResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import CreateRuleResultTypeDef
```




Optional fields:
- `rule`: `"RuleTypeDef"`


## DataValidationMetricsTypeDef

```python
from mypy_boto3_frauddetector.type_defs import DataValidationMetricsTypeDef
```




Optional fields:
- `fileLevelMessages`: `List["FileValidationMessageTypeDef"]`
- `fieldLevelMessages`: `List["FieldValidationMessageTypeDef"]`


## DescribeDetectorResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import DescribeDetectorResultTypeDef
```




Optional fields:
- `detectorId`: `str`
- `detectorVersionSummaries`: `List["DetectorVersionSummaryTypeDef"]`
- `nextToken`: `str`
- `arn`: `str`


## DescribeModelVersionsResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import DescribeModelVersionsResultTypeDef
```




Optional fields:
- `modelVersionDetails`: `List["ModelVersionDetailTypeDef"]`
- `nextToken`: `str`


## DetectorTypeDef

```python
from mypy_boto3_frauddetector.type_defs import DetectorTypeDef
```




Optional fields:
- `detectorId`: `str`
- `description`: `str`
- `eventTypeName`: `str`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## DetectorVersionSummaryTypeDef

```python
from mypy_boto3_frauddetector.type_defs import DetectorVersionSummaryTypeDef
```




Optional fields:
- `detectorVersionId`: `str`
- `status`: `DetectorVersionStatus`
- `description`: `str`
- `lastUpdatedTime`: `str`


## EntityTypeDef

```python
from mypy_boto3_frauddetector.type_defs import EntityTypeDef
```


Required fields:
- `entityType`: `str`
- `entityId`: `str`




## EntityTypeTypeDef

```python
from mypy_boto3_frauddetector.type_defs import EntityTypeTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## EventTypeTypeDef

```python
from mypy_boto3_frauddetector.type_defs import EventTypeTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `eventVariables`: `List[str]`
- `labels`: `List[str]`
- `entityTypes`: `List[str]`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## ExternalEventsDetailTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ExternalEventsDetailTypeDef
```


Required fields:
- `dataLocation`: `str`
- `dataAccessRoleArn`: `str`




## ExternalModelTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ExternalModelTypeDef
```




Optional fields:
- `modelEndpoint`: `str`
- `modelSource`: `Literal['SAGEMAKER']`
- `invokeModelEndpointRoleArn`: `str`
- `inputConfiguration`: `"ModelInputConfigurationTypeDef"`
- `outputConfiguration`: `"ModelOutputConfigurationTypeDef"`
- `modelEndpointStatus`: `ModelEndpointStatus`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## FieldValidationMessageTypeDef

```python
from mypy_boto3_frauddetector.type_defs import FieldValidationMessageTypeDef
```




Optional fields:
- `fieldName`: `str`
- `identifier`: `str`
- `title`: `str`
- `content`: `str`
- `type`: `str`


## FileValidationMessageTypeDef

```python
from mypy_boto3_frauddetector.type_defs import FileValidationMessageTypeDef
```




Optional fields:
- `title`: `str`
- `content`: `str`
- `type`: `str`


## GetBatchPredictionJobsResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetBatchPredictionJobsResultTypeDef
```




Optional fields:
- `batchPredictions`: `List["BatchPredictionTypeDef"]`
- `nextToken`: `str`


## GetDetectorVersionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetDetectorVersionResultTypeDef
```




Optional fields:
- `detectorId`: `str`
- `detectorVersionId`: `str`
- `description`: `str`
- `externalModelEndpoints`: `List[str]`
- `modelVersions`: `List["ModelVersionTypeDef"]`
- `rules`: `List["RuleTypeDef"]`
- `status`: `DetectorVersionStatus`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `ruleExecutionMode`: `RuleExecutionMode`
- `arn`: `str`


## GetDetectorsResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetDetectorsResultTypeDef
```




Optional fields:
- `detectors`: `List["DetectorTypeDef"]`
- `nextToken`: `str`


## GetEntityTypesResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetEntityTypesResultTypeDef
```




Optional fields:
- `entityTypes`: `List["EntityTypeTypeDef"]`
- `nextToken`: `str`


## GetEventPredictionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetEventPredictionResultTypeDef
```




Optional fields:
- `modelScores`: `List["ModelScoresTypeDef"]`
- `ruleResults`: `List["RuleResultTypeDef"]`


## GetEventTypesResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetEventTypesResultTypeDef
```




Optional fields:
- `eventTypes`: `List["EventTypeTypeDef"]`
- `nextToken`: `str`


## GetExternalModelsResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetExternalModelsResultTypeDef
```




Optional fields:
- `externalModels`: `List["ExternalModelTypeDef"]`
- `nextToken`: `str`


## GetKMSEncryptionKeyResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetKMSEncryptionKeyResultTypeDef
```




Optional fields:
- `kmsKey`: `"KMSKeyTypeDef"`


## GetLabelsResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetLabelsResultTypeDef
```




Optional fields:
- `labels`: `List["LabelTypeDef"]`
- `nextToken`: `str`


## GetModelVersionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetModelVersionResultTypeDef
```




Optional fields:
- `modelId`: `str`
- `modelType`: `Literal['ONLINE_FRAUD_INSIGHTS']`
- `modelVersionNumber`: `str`
- `trainingDataSource`: `Literal['EXTERNAL_EVENTS']`
- `trainingDataSchema`: `"TrainingDataSchemaTypeDef"`
- `externalEventsDetail`: `"ExternalEventsDetailTypeDef"`
- `status`: `str`
- `arn`: `str`


## GetModelsResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetModelsResultTypeDef
```




Optional fields:
- `nextToken`: `str`
- `models`: `List["ModelTypeDef"]`


## GetOutcomesResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetOutcomesResultTypeDef
```




Optional fields:
- `outcomes`: `List["OutcomeTypeDef"]`
- `nextToken`: `str`


## GetRulesResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetRulesResultTypeDef
```




Optional fields:
- `ruleDetails`: `List["RuleDetailTypeDef"]`
- `nextToken`: `str`


## GetVariablesResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import GetVariablesResultTypeDef
```




Optional fields:
- `variables`: `List["VariableTypeDef"]`
- `nextToken`: `str`


## KMSKeyTypeDef

```python
from mypy_boto3_frauddetector.type_defs import KMSKeyTypeDef
```




Optional fields:
- `kmsEncryptionKeyArn`: `str`


## LabelSchemaTypeDef

```python
from mypy_boto3_frauddetector.type_defs import LabelSchemaTypeDef
```


Required fields:
- `labelMapper`: `Dict[str, List[str]]`




## LabelTypeDef

```python
from mypy_boto3_frauddetector.type_defs import LabelTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ListTagsForResourceResultTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`
- `nextToken`: `str`


## MetricDataPointTypeDef

```python
from mypy_boto3_frauddetector.type_defs import MetricDataPointTypeDef
```




Optional fields:
- `fpr`: `float`
- `precision`: `float`
- `tpr`: `float`
- `threshold`: `float`


## ModelEndpointDataBlobTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelEndpointDataBlobTypeDef
```




Optional fields:
- `byteBuffer`: `Union[bytes, IO[bytes]]`
- `contentType`: `str`


## ModelInputConfigurationTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelInputConfigurationTypeDef
```


Required fields:
- `useEventVariables`: `bool`



Optional fields:
- `eventTypeName`: `str`
- `format`: `ModelInputDataFormat`
- `jsonInputTemplate`: `str`
- `csvInputTemplate`: `str`


## ModelOutputConfigurationTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelOutputConfigurationTypeDef
```


Required fields:
- `format`: `ModelOutputDataFormat`



Optional fields:
- `jsonKeyToVariableMap`: `Dict[str, str]`
- `csvIndexToVariableMap`: `Dict[str, str]`


## ModelScoresTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelScoresTypeDef
```




Optional fields:
- `modelVersion`: `"ModelVersionTypeDef"`
- `scores`: `Dict[str, float]`


## ModelTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelTypeDef
```




Optional fields:
- `modelId`: `str`
- `modelType`: `Literal['ONLINE_FRAUD_INSIGHTS']`
- `description`: `str`
- `eventTypeName`: `str`
- `createdTime`: `str`
- `lastUpdatedTime`: `str`
- `arn`: `str`


## ModelVersionDetailTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelVersionDetailTypeDef
```




Optional fields:
- `modelId`: `str`
- `modelType`: `Literal['ONLINE_FRAUD_INSIGHTS']`
- `modelVersionNumber`: `str`
- `status`: `str`
- `trainingDataSource`: `Literal['EXTERNAL_EVENTS']`
- `trainingDataSchema`: `"TrainingDataSchemaTypeDef"`
- `externalEventsDetail`: `"ExternalEventsDetailTypeDef"`
- `trainingResult`: `"TrainingResultTypeDef"`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## ModelVersionTypeDef

```python
from mypy_boto3_frauddetector.type_defs import ModelVersionTypeDef
```


Required fields:
- `modelId`: `str`
- `modelType`: `Literal['ONLINE_FRAUD_INSIGHTS']`
- `modelVersionNumber`: `str`



Optional fields:
- `arn`: `str`


## OutcomeTypeDef

```python
from mypy_boto3_frauddetector.type_defs import OutcomeTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## RuleDetailTypeDef

```python
from mypy_boto3_frauddetector.type_defs import RuleDetailTypeDef
```




Optional fields:
- `ruleId`: `str`
- `description`: `str`
- `detectorId`: `str`
- `ruleVersion`: `str`
- `expression`: `str`
- `language`: `Literal['DETECTORPL']`
- `outcomes`: `List[str]`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`


## RuleResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import RuleResultTypeDef
```




Optional fields:
- `ruleId`: `str`
- `outcomes`: `List[str]`


## RuleTypeDef

```python
from mypy_boto3_frauddetector.type_defs import RuleTypeDef
```


Required fields:
- `detectorId`: `str`
- `ruleId`: `str`
- `ruleVersion`: `str`




## TagTypeDef

```python
from mypy_boto3_frauddetector.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## TrainingDataSchemaTypeDef

```python
from mypy_boto3_frauddetector.type_defs import TrainingDataSchemaTypeDef
```


Required fields:
- `modelVariables`: `List[str]`
- `labelSchema`: `"LabelSchemaTypeDef"`




## TrainingMetricsTypeDef

```python
from mypy_boto3_frauddetector.type_defs import TrainingMetricsTypeDef
```




Optional fields:
- `auc`: `float`
- `metricDataPoints`: `List["MetricDataPointTypeDef"]`


## TrainingResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import TrainingResultTypeDef
```




Optional fields:
- `dataValidationMetrics`: `"DataValidationMetricsTypeDef"`
- `trainingMetrics`: `"TrainingMetricsTypeDef"`


## UpdateModelVersionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import UpdateModelVersionResultTypeDef
```




Optional fields:
- `modelId`: `str`
- `modelType`: `Literal['ONLINE_FRAUD_INSIGHTS']`
- `modelVersionNumber`: `str`
- `status`: `str`


## UpdateRuleVersionResultTypeDef

```python
from mypy_boto3_frauddetector.type_defs import UpdateRuleVersionResultTypeDef
```




Optional fields:
- `rule`: `"RuleTypeDef"`


## VariableEntryTypeDef

```python
from mypy_boto3_frauddetector.type_defs import VariableEntryTypeDef
```




Optional fields:
- `name`: `str`
- `dataType`: `str`
- `dataSource`: `str`
- `defaultValue`: `str`
- `description`: `str`
- `variableType`: `str`


## VariableTypeDef

```python
from mypy_boto3_frauddetector.type_defs import VariableTypeDef
```




Optional fields:
- `name`: `str`
- `dataType`: `DataType`
- `dataSource`: `DataSource`
- `defaultValue`: `str`
- `description`: `str`
- `variableType`: `str`
- `lastUpdatedTime`: `str`
- `createdTime`: `str`
- `arn`: `str`

