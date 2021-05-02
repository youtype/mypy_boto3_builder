# Structures for boto3 IoTEvents module

> [Index](../index.md) > [IoTEvents](./index.md) > Structures

Auto-generated documentation for [IoTEvents](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents)
type annotations stubs module [mypy_boto3_iotevents](https://pypi.org/project/mypy-boto3-iotevents/).

- [Structures for boto3 IoTEvents module](#structures-for-boto3-iotevents-module)
  - [ActionTypeDef](#actiontypedef)
  - [AnalysisResultLocationTypeDef](#analysisresultlocationtypedef)
  - [AnalysisResultTypeDef](#analysisresulttypedef)
  - [AssetPropertyTimestampTypeDef](#assetpropertytimestamptypedef)
  - [AssetPropertyValueTypeDef](#assetpropertyvaluetypedef)
  - [AssetPropertyVariantTypeDef](#assetpropertyvarianttypedef)
  - [AttributeTypeDef](#attributetypedef)
  - [ClearTimerActionTypeDef](#cleartimeractiontypedef)
  - [DetectorDebugOptionTypeDef](#detectordebugoptiontypedef)
  - [DetectorModelConfigurationTypeDef](#detectormodelconfigurationtypedef)
  - [DetectorModelDefinitionTypeDef](#detectormodeldefinitiontypedef)
  - [DetectorModelSummaryTypeDef](#detectormodelsummarytypedef)
  - [DetectorModelTypeDef](#detectormodeltypedef)
  - [DetectorModelVersionSummaryTypeDef](#detectormodelversionsummarytypedef)
  - [DynamoDBActionTypeDef](#dynamodbactiontypedef)
  - [DynamoDBv2ActionTypeDef](#dynamodbv2actiontypedef)
  - [EventTypeDef](#eventtypedef)
  - [FirehoseActionTypeDef](#firehoseactiontypedef)
  - [InputConfigurationTypeDef](#inputconfigurationtypedef)
  - [InputDefinitionTypeDef](#inputdefinitiontypedef)
  - [InputSummaryTypeDef](#inputsummarytypedef)
  - [InputTypeDef](#inputtypedef)
  - [IotEventsActionTypeDef](#ioteventsactiontypedef)
  - [IotSiteWiseActionTypeDef](#iotsitewiseactiontypedef)
  - [IotTopicPublishActionTypeDef](#iottopicpublishactiontypedef)
  - [LambdaActionTypeDef](#lambdaactiontypedef)
  - [LoggingOptionsTypeDef](#loggingoptionstypedef)
  - [OnEnterLifecycleTypeDef](#onenterlifecycletypedef)
  - [OnExitLifecycleTypeDef](#onexitlifecycletypedef)
  - [OnInputLifecycleTypeDef](#oninputlifecycletypedef)
  - [PayloadTypeDef](#payloadtypedef)
  - [ResetTimerActionTypeDef](#resettimeractiontypedef)
  - [SNSTopicPublishActionTypeDef](#snstopicpublishactiontypedef)
  - [SetTimerActionTypeDef](#settimeractiontypedef)
  - [SetVariableActionTypeDef](#setvariableactiontypedef)
  - [SqsActionTypeDef](#sqsactiontypedef)
  - [StateTypeDef](#statetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TransitionEventTypeDef](#transitioneventtypedef)
  - [CreateDetectorModelResponseTypeDef](#createdetectormodelresponsetypedef)
  - [CreateInputResponseTypeDef](#createinputresponsetypedef)
  - [DescribeDetectorModelAnalysisResponseTypeDef](#describedetectormodelanalysisresponsetypedef)
  - [DescribeDetectorModelResponseTypeDef](#describedetectormodelresponsetypedef)
  - [DescribeInputResponseTypeDef](#describeinputresponsetypedef)
  - [DescribeLoggingOptionsResponseTypeDef](#describeloggingoptionsresponsetypedef)
  - [GetDetectorModelAnalysisResultsResponseTypeDef](#getdetectormodelanalysisresultsresponsetypedef)
  - [ListDetectorModelVersionsResponseTypeDef](#listdetectormodelversionsresponsetypedef)
  - [ListDetectorModelsResponseTypeDef](#listdetectormodelsresponsetypedef)
  - [ListInputsResponseTypeDef](#listinputsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [StartDetectorModelAnalysisResponseTypeDef](#startdetectormodelanalysisresponsetypedef)
  - [UpdateDetectorModelResponseTypeDef](#updatedetectormodelresponsetypedef)
  - [UpdateInputResponseTypeDef](#updateinputresponsetypedef)

## ActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import ActionTypeDef
```




Optional fields:
- `setVariable`: `"SetVariableActionTypeDef"`
- `sns`: `"SNSTopicPublishActionTypeDef"`
- `iotTopicPublish`: `"IotTopicPublishActionTypeDef"`
- `setTimer`: `"SetTimerActionTypeDef"`
- `clearTimer`: `"ClearTimerActionTypeDef"`
- `resetTimer`: `"ResetTimerActionTypeDef"`
- `lambda`: `"LambdaActionTypeDef"`
- `iotEvents`: `"IotEventsActionTypeDef"`
- `sqs`: `"SqsActionTypeDef"`
- `firehose`: `"FirehoseActionTypeDef"`
- `dynamoDB`: `"DynamoDBActionTypeDef"`
- `dynamoDBv2`: `"DynamoDBv2ActionTypeDef"`
- `iotSiteWise`: `"IotSiteWiseActionTypeDef"`


## AnalysisResultLocationTypeDef

```python
from mypy_boto3_iotevents.type_defs import AnalysisResultLocationTypeDef
```




Optional fields:
- `path`: `str`


## AnalysisResultTypeDef

```python
from mypy_boto3_iotevents.type_defs import AnalysisResultTypeDef
```




Optional fields:
- `type`: `str`
- `level`: `AnalysisResultLevel`
- `message`: `str`
- `locations`: `List["AnalysisResultLocationTypeDef"]`


## AssetPropertyTimestampTypeDef

```python
from mypy_boto3_iotevents.type_defs import AssetPropertyTimestampTypeDef
```


Required fields:
- `timeInSeconds`: `str`



Optional fields:
- `offsetInNanos`: `str`


## AssetPropertyValueTypeDef

```python
from mypy_boto3_iotevents.type_defs import AssetPropertyValueTypeDef
```


Required fields:
- `value`: `"AssetPropertyVariantTypeDef"`



Optional fields:
- `timestamp`: `"AssetPropertyTimestampTypeDef"`
- `quality`: `str`


## AssetPropertyVariantTypeDef

```python
from mypy_boto3_iotevents.type_defs import AssetPropertyVariantTypeDef
```




Optional fields:
- `stringValue`: `str`
- `integerValue`: `str`
- `doubleValue`: `str`
- `booleanValue`: `str`


## AttributeTypeDef

```python
from mypy_boto3_iotevents.type_defs import AttributeTypeDef
```


Required fields:
- `jsonPath`: `str`




## ClearTimerActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import ClearTimerActionTypeDef
```


Required fields:
- `timerName`: `str`




## DetectorDebugOptionTypeDef

```python
from mypy_boto3_iotevents.type_defs import DetectorDebugOptionTypeDef
```


Required fields:
- `detectorModelName`: `str`



Optional fields:
- `keyValue`: `str`


## DetectorModelConfigurationTypeDef

```python
from mypy_boto3_iotevents.type_defs import DetectorModelConfigurationTypeDef
```




Optional fields:
- `detectorModelName`: `str`
- `detectorModelVersion`: `str`
- `detectorModelDescription`: `str`
- `detectorModelArn`: `str`
- `roleArn`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `status`: `DetectorModelVersionStatus`
- `key`: `str`
- `evaluationMethod`: `EvaluationMethod`


## DetectorModelDefinitionTypeDef

```python
from mypy_boto3_iotevents.type_defs import DetectorModelDefinitionTypeDef
```


Required fields:
- `states`: `List["StateTypeDef"]`
- `initialStateName`: `str`




## DetectorModelSummaryTypeDef

```python
from mypy_boto3_iotevents.type_defs import DetectorModelSummaryTypeDef
```




Optional fields:
- `detectorModelName`: `str`
- `detectorModelDescription`: `str`
- `creationTime`: `datetime`


## DetectorModelTypeDef

```python
from mypy_boto3_iotevents.type_defs import DetectorModelTypeDef
```




Optional fields:
- `detectorModelDefinition`: `"DetectorModelDefinitionTypeDef"`
- `detectorModelConfiguration`: `"DetectorModelConfigurationTypeDef"`


## DetectorModelVersionSummaryTypeDef

```python
from mypy_boto3_iotevents.type_defs import DetectorModelVersionSummaryTypeDef
```




Optional fields:
- `detectorModelName`: `str`
- `detectorModelVersion`: `str`
- `detectorModelArn`: `str`
- `roleArn`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `status`: `DetectorModelVersionStatus`
- `evaluationMethod`: `EvaluationMethod`


## DynamoDBActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import DynamoDBActionTypeDef
```


Required fields:
- `hashKeyField`: `str`
- `hashKeyValue`: `str`
- `tableName`: `str`



Optional fields:
- `hashKeyType`: `str`
- `rangeKeyType`: `str`
- `rangeKeyField`: `str`
- `rangeKeyValue`: `str`
- `operation`: `str`
- `payloadField`: `str`
- `payload`: `"PayloadTypeDef"`


## DynamoDBv2ActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import DynamoDBv2ActionTypeDef
```


Required fields:
- `tableName`: `str`



Optional fields:
- `payload`: `"PayloadTypeDef"`


## EventTypeDef

```python
from mypy_boto3_iotevents.type_defs import EventTypeDef
```


Required fields:
- `eventName`: `str`



Optional fields:
- `condition`: `str`
- `actions`: `List["ActionTypeDef"]`


## FirehoseActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import FirehoseActionTypeDef
```


Required fields:
- `deliveryStreamName`: `str`



Optional fields:
- `separator`: `str`
- `payload`: `"PayloadTypeDef"`


## InputConfigurationTypeDef

```python
from mypy_boto3_iotevents.type_defs import InputConfigurationTypeDef
```


Required fields:
- `inputName`: `str`
- `inputArn`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `status`: `InputStatus`



Optional fields:
- `inputDescription`: `str`


## InputDefinitionTypeDef

```python
from mypy_boto3_iotevents.type_defs import InputDefinitionTypeDef
```


Required fields:
- `attributes`: `List["AttributeTypeDef"]`




## InputSummaryTypeDef

```python
from mypy_boto3_iotevents.type_defs import InputSummaryTypeDef
```




Optional fields:
- `inputName`: `str`
- `inputDescription`: `str`
- `inputArn`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `status`: `InputStatus`


## InputTypeDef

```python
from mypy_boto3_iotevents.type_defs import InputTypeDef
```




Optional fields:
- `inputConfiguration`: `"InputConfigurationTypeDef"`
- `inputDefinition`: `"InputDefinitionTypeDef"`


## IotEventsActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import IotEventsActionTypeDef
```


Required fields:
- `inputName`: `str`



Optional fields:
- `payload`: `"PayloadTypeDef"`


## IotSiteWiseActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import IotSiteWiseActionTypeDef
```


Required fields:
- `propertyValue`: `"AssetPropertyValueTypeDef"`



Optional fields:
- `entryId`: `str`
- `assetId`: `str`
- `propertyId`: `str`
- `propertyAlias`: `str`


## IotTopicPublishActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import IotTopicPublishActionTypeDef
```


Required fields:
- `mqttTopic`: `str`



Optional fields:
- `payload`: `"PayloadTypeDef"`


## LambdaActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import LambdaActionTypeDef
```


Required fields:
- `functionArn`: `str`



Optional fields:
- `payload`: `"PayloadTypeDef"`


## LoggingOptionsTypeDef

```python
from mypy_boto3_iotevents.type_defs import LoggingOptionsTypeDef
```


Required fields:
- `roleArn`: `str`
- `level`: `LoggingLevel`
- `enabled`: `bool`



Optional fields:
- `detectorDebugOptions`: `List["DetectorDebugOptionTypeDef"]`


## OnEnterLifecycleTypeDef

```python
from mypy_boto3_iotevents.type_defs import OnEnterLifecycleTypeDef
```




Optional fields:
- `events`: `List["EventTypeDef"]`


## OnExitLifecycleTypeDef

```python
from mypy_boto3_iotevents.type_defs import OnExitLifecycleTypeDef
```




Optional fields:
- `events`: `List["EventTypeDef"]`


## OnInputLifecycleTypeDef

```python
from mypy_boto3_iotevents.type_defs import OnInputLifecycleTypeDef
```




Optional fields:
- `events`: `List["EventTypeDef"]`
- `transitionEvents`: `List["TransitionEventTypeDef"]`


## PayloadTypeDef

```python
from mypy_boto3_iotevents.type_defs import PayloadTypeDef
```


Required fields:
- `contentExpression`: `str`
- `type`: `PayloadType`




## ResetTimerActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import ResetTimerActionTypeDef
```


Required fields:
- `timerName`: `str`




## SNSTopicPublishActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import SNSTopicPublishActionTypeDef
```


Required fields:
- `targetArn`: `str`



Optional fields:
- `payload`: `"PayloadTypeDef"`


## SetTimerActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import SetTimerActionTypeDef
```


Required fields:
- `timerName`: `str`



Optional fields:
- `seconds`: `int`
- `durationExpression`: `str`


## SetVariableActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import SetVariableActionTypeDef
```


Required fields:
- `variableName`: `str`
- `value`: `str`




## SqsActionTypeDef

```python
from mypy_boto3_iotevents.type_defs import SqsActionTypeDef
```


Required fields:
- `queueUrl`: `str`



Optional fields:
- `useBase64`: `bool`
- `payload`: `"PayloadTypeDef"`


## StateTypeDef

```python
from mypy_boto3_iotevents.type_defs import StateTypeDef
```


Required fields:
- `stateName`: `str`



Optional fields:
- `onInput`: `"OnInputLifecycleTypeDef"`
- `onEnter`: `"OnEnterLifecycleTypeDef"`
- `onExit`: `"OnExitLifecycleTypeDef"`


## TagTypeDef

```python
from mypy_boto3_iotevents.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## TransitionEventTypeDef

```python
from mypy_boto3_iotevents.type_defs import TransitionEventTypeDef
```


Required fields:
- `eventName`: `str`
- `condition`: `str`
- `nextState`: `str`



Optional fields:
- `actions`: `List["ActionTypeDef"]`


## CreateDetectorModelResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import CreateDetectorModelResponseTypeDef
```




Optional fields:
- `detectorModelConfiguration`: `"DetectorModelConfigurationTypeDef"`


## CreateInputResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import CreateInputResponseTypeDef
```




Optional fields:
- `inputConfiguration`: `"InputConfigurationTypeDef"`


## DescribeDetectorModelAnalysisResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import DescribeDetectorModelAnalysisResponseTypeDef
```




Optional fields:
- `status`: `AnalysisStatus`


## DescribeDetectorModelResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import DescribeDetectorModelResponseTypeDef
```




Optional fields:
- `detectorModel`: `"DetectorModelTypeDef"`


## DescribeInputResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import DescribeInputResponseTypeDef
```




Optional fields:
- `input`: `"InputTypeDef"`


## DescribeLoggingOptionsResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import DescribeLoggingOptionsResponseTypeDef
```




Optional fields:
- `loggingOptions`: `"LoggingOptionsTypeDef"`


## GetDetectorModelAnalysisResultsResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import GetDetectorModelAnalysisResultsResponseTypeDef
```




Optional fields:
- `analysisResults`: `List["AnalysisResultTypeDef"]`
- `nextToken`: `str`


## ListDetectorModelVersionsResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import ListDetectorModelVersionsResponseTypeDef
```




Optional fields:
- `detectorModelVersionSummaries`: `List["DetectorModelVersionSummaryTypeDef"]`
- `nextToken`: `str`


## ListDetectorModelsResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import ListDetectorModelsResponseTypeDef
```




Optional fields:
- `detectorModelSummaries`: `List["DetectorModelSummaryTypeDef"]`
- `nextToken`: `str`


## ListInputsResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import ListInputsResponseTypeDef
```




Optional fields:
- `inputSummaries`: `List["InputSummaryTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`


## StartDetectorModelAnalysisResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import StartDetectorModelAnalysisResponseTypeDef
```




Optional fields:
- `analysisId`: `str`


## UpdateDetectorModelResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import UpdateDetectorModelResponseTypeDef
```




Optional fields:
- `detectorModelConfiguration`: `"DetectorModelConfigurationTypeDef"`


## UpdateInputResponseTypeDef

```python
from mypy_boto3_iotevents.type_defs import UpdateInputResponseTypeDef
```




Optional fields:
- `inputConfiguration`: `"InputConfigurationTypeDef"`

