# Type annotations for boto3 FraudDetector module

> [Index](../index.md) > FraudDetector

Auto-generated documentation for [FraudDetector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector)
type annotations stubs module [mypy_boto3_frauddetector](https://pypi.org/project/mypy-boto3-frauddetector/).

```bash
pip install mypy-boto3-frauddetector
```

- [Type annotations for boto3 FraudDetector module](#type-annotations-for-boto3-frauddetector-module)
  - [FraudDetectorClient](#frauddetectorclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## FraudDetectorClient

Type annotations for  `boto3.client("frauddetector")` as [FraudDetectorClient](./client.md)

Can be used directly:

```python
from mypy_boto3_frauddetector.client import FraudDetectorClient
```


FraudDetectorClient [exceptions](./client.md#exceptions)



### Methods
- [batch_create_variable](./client.md#batch-create-variable)
- [batch_get_variable](./client.md#batch-get-variable)
- [can_paginate](./client.md#can-paginate)
- [cancel_batch_prediction_job](./client.md#cancel-batch-prediction-job)
- [create_batch_prediction_job](./client.md#create-batch-prediction-job)
- [create_detector_version](./client.md#create-detector-version)
- [create_model](./client.md#create-model)
- [create_model_version](./client.md#create-model-version)
- [create_rule](./client.md#create-rule)
- [create_variable](./client.md#create-variable)
- [delete_batch_prediction_job](./client.md#delete-batch-prediction-job)
- [delete_detector](./client.md#delete-detector)
- [delete_detector_version](./client.md#delete-detector-version)
- [delete_entity_type](./client.md#delete-entity-type)
- [delete_event](./client.md#delete-event)
- [delete_event_type](./client.md#delete-event-type)
- [delete_external_model](./client.md#delete-external-model)
- [delete_label](./client.md#delete-label)
- [delete_model](./client.md#delete-model)
- [delete_model_version](./client.md#delete-model-version)
- [delete_outcome](./client.md#delete-outcome)
- [delete_rule](./client.md#delete-rule)
- [delete_variable](./client.md#delete-variable)
- [describe_detector](./client.md#describe-detector)
- [describe_model_versions](./client.md#describe-model-versions)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_batch_prediction_jobs](./client.md#get-batch-prediction-jobs)
- [get_detector_version](./client.md#get-detector-version)
- [get_detectors](./client.md#get-detectors)
- [get_entity_types](./client.md#get-entity-types)
- [get_event_prediction](./client.md#get-event-prediction)
- [get_event_types](./client.md#get-event-types)
- [get_external_models](./client.md#get-external-models)
- [get_kms_encryption_key](./client.md#get-kms-encryption-key)
- [get_labels](./client.md#get-labels)
- [get_model_version](./client.md#get-model-version)
- [get_models](./client.md#get-models)
- [get_outcomes](./client.md#get-outcomes)
- [get_rules](./client.md#get-rules)
- [get_variables](./client.md#get-variables)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_detector](./client.md#put-detector)
- [put_entity_type](./client.md#put-entity-type)
- [put_event_type](./client.md#put-event-type)
- [put_external_model](./client.md#put-external-model)
- [put_kms_encryption_key](./client.md#put-kms-encryption-key)
- [put_label](./client.md#put-label)
- [put_outcome](./client.md#put-outcome)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_detector_version](./client.md#update-detector-version)
- [update_detector_version_metadata](./client.md#update-detector-version-metadata)
- [update_detector_version_status](./client.md#update-detector-version-status)
- [update_model](./client.md#update-model)
- [update_model_version](./client.md#update-model-version)
- [update_model_version_status](./client.md#update-model-version-status)
- [update_rule_metadata](./client.md#update-rule-metadata)
- [update_rule_version](./client.md#update-rule-version)
- [update_variable](./client.md#update-variable)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_frauddetector.literals import AsyncJobStatus, ...
```

- [AsyncJobStatus](./literals.md#asyncjobstatus)
- [DataSource](./literals.md#datasource)
- [DataType](./literals.md#datatype)
- [DetectorVersionStatus](./literals.md#detectorversionstatus)
- [Language](./literals.md#language)
- [ModelEndpointStatus](./literals.md#modelendpointstatus)
- [ModelInputDataFormat](./literals.md#modelinputdataformat)
- [ModelOutputDataFormat](./literals.md#modeloutputdataformat)
- [ModelSource](./literals.md#modelsource)
- [ModelTypeEnum](./literals.md#modeltypeenum)
- [ModelVersionStatus](./literals.md#modelversionstatus)
- [RuleExecutionMode](./literals.md#ruleexecutionmode)
- [TrainingDataSourceEnum](./literals.md#trainingdatasourceenum)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_frauddetector.type_defs import BatchCreateVariableErrorTypeDef, ...
```

- [BatchCreateVariableErrorTypeDef](./type_defs.md#batchcreatevariableerrortypedef)
- [BatchGetVariableErrorTypeDef](./type_defs.md#batchgetvariableerrortypedef)
- [BatchPredictionTypeDef](./type_defs.md#batchpredictiontypedef)
- [DataValidationMetricsTypeDef](./type_defs.md#datavalidationmetricstypedef)
- [DetectorTypeDef](./type_defs.md#detectortypedef)
- [DetectorVersionSummaryTypeDef](./type_defs.md#detectorversionsummarytypedef)
- [EntityTypeTypeDef](./type_defs.md#entitytypetypedef)
- [EventTypeTypeDef](./type_defs.md#eventtypetypedef)
- [ExternalEventsDetailTypeDef](./type_defs.md#externaleventsdetailtypedef)
- [ExternalModelTypeDef](./type_defs.md#externalmodeltypedef)
- [FieldValidationMessageTypeDef](./type_defs.md#fieldvalidationmessagetypedef)
- [FileValidationMessageTypeDef](./type_defs.md#filevalidationmessagetypedef)
- [KMSKeyTypeDef](./type_defs.md#kmskeytypedef)
- [LabelSchemaTypeDef](./type_defs.md#labelschematypedef)
- [LabelTypeDef](./type_defs.md#labeltypedef)
- [MetricDataPointTypeDef](./type_defs.md#metricdatapointtypedef)
- [ModelInputConfigurationTypeDef](./type_defs.md#modelinputconfigurationtypedef)
- [ModelOutputConfigurationTypeDef](./type_defs.md#modeloutputconfigurationtypedef)
- [ModelScoresTypeDef](./type_defs.md#modelscorestypedef)
- [ModelTypeDef](./type_defs.md#modeltypedef)
- [ModelVersionDetailTypeDef](./type_defs.md#modelversiondetailtypedef)
- [ModelVersionTypeDef](./type_defs.md#modelversiontypedef)
- [OutcomeTypeDef](./type_defs.md#outcometypedef)
- [RuleDetailTypeDef](./type_defs.md#ruledetailtypedef)
- [RuleResultTypeDef](./type_defs.md#ruleresulttypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TrainingDataSchemaTypeDef](./type_defs.md#trainingdataschematypedef)
- [TrainingMetricsTypeDef](./type_defs.md#trainingmetricstypedef)
- [TrainingResultTypeDef](./type_defs.md#trainingresulttypedef)
- [VariableTypeDef](./type_defs.md#variabletypedef)
- [BatchCreateVariableResultTypeDef](./type_defs.md#batchcreatevariableresulttypedef)
- [BatchGetVariableResultTypeDef](./type_defs.md#batchgetvariableresulttypedef)
- [CreateDetectorVersionResultTypeDef](./type_defs.md#createdetectorversionresulttypedef)
- [CreateModelVersionResultTypeDef](./type_defs.md#createmodelversionresulttypedef)
- [CreateRuleResultTypeDef](./type_defs.md#createruleresulttypedef)
- [DescribeDetectorResultTypeDef](./type_defs.md#describedetectorresulttypedef)
- [DescribeModelVersionsResultTypeDef](./type_defs.md#describemodelversionsresulttypedef)
- [EntityTypeDef](./type_defs.md#entitytypedef)
- [GetBatchPredictionJobsResultTypeDef](./type_defs.md#getbatchpredictionjobsresulttypedef)
- [GetDetectorVersionResultTypeDef](./type_defs.md#getdetectorversionresulttypedef)
- [GetDetectorsResultTypeDef](./type_defs.md#getdetectorsresulttypedef)
- [GetEntityTypesResultTypeDef](./type_defs.md#getentitytypesresulttypedef)
- [GetEventPredictionResultTypeDef](./type_defs.md#geteventpredictionresulttypedef)
- [GetEventTypesResultTypeDef](./type_defs.md#geteventtypesresulttypedef)
- [GetExternalModelsResultTypeDef](./type_defs.md#getexternalmodelsresulttypedef)
- [GetKMSEncryptionKeyResultTypeDef](./type_defs.md#getkmsencryptionkeyresulttypedef)
- [GetLabelsResultTypeDef](./type_defs.md#getlabelsresulttypedef)
- [GetModelVersionResultTypeDef](./type_defs.md#getmodelversionresulttypedef)
- [GetModelsResultTypeDef](./type_defs.md#getmodelsresulttypedef)
- [GetOutcomesResultTypeDef](./type_defs.md#getoutcomesresulttypedef)
- [GetRulesResultTypeDef](./type_defs.md#getrulesresulttypedef)
- [GetVariablesResultTypeDef](./type_defs.md#getvariablesresulttypedef)
- [ListTagsForResourceResultTypeDef](./type_defs.md#listtagsforresourceresulttypedef)
- [ModelEndpointDataBlobTypeDef](./type_defs.md#modelendpointdatablobtypedef)
- [UpdateModelVersionResultTypeDef](./type_defs.md#updatemodelversionresulttypedef)
- [UpdateRuleVersionResultTypeDef](./type_defs.md#updateruleversionresulttypedef)
- [VariableEntryTypeDef](./type_defs.md#variableentrytypedef)
