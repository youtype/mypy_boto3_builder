# FraudDetectorClient for boto3 FraudDetector module

> [Index](../index.md) > [FraudDetector](./index.md) > FraudDetectorClient

Auto-generated documentation for [FraudDetector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector)
type annotations stubs module [mypy_boto3_frauddetector](https://pypi.org/project/mypy-boto3-frauddetector/).

- [FraudDetectorClient for boto3 FraudDetector module](#frauddetectorclient-for-boto3-frauddetector-module)
  - [FraudDetectorClient](#frauddetectorclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_create_variable](#batch_create_variable)
    - [batch_get_variable](#batch_get_variable)
    - [can_paginate](#can_paginate)
    - [cancel_batch_prediction_job](#cancel_batch_prediction_job)
    - [create_batch_prediction_job](#create_batch_prediction_job)
    - [create_detector_version](#create_detector_version)
    - [create_model](#create_model)
    - [create_model_version](#create_model_version)
    - [create_rule](#create_rule)
    - [create_variable](#create_variable)
    - [delete_batch_prediction_job](#delete_batch_prediction_job)
    - [delete_detector](#delete_detector)
    - [delete_detector_version](#delete_detector_version)
    - [delete_entity_type](#delete_entity_type)
    - [delete_event](#delete_event)
    - [delete_event_type](#delete_event_type)
    - [delete_external_model](#delete_external_model)
    - [delete_label](#delete_label)
    - [delete_model](#delete_model)
    - [delete_model_version](#delete_model_version)
    - [delete_outcome](#delete_outcome)
    - [delete_rule](#delete_rule)
    - [delete_variable](#delete_variable)
    - [describe_detector](#describe_detector)
    - [describe_model_versions](#describe_model_versions)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_batch_prediction_jobs](#get_batch_prediction_jobs)
    - [get_detector_version](#get_detector_version)
    - [get_detectors](#get_detectors)
    - [get_entity_types](#get_entity_types)
    - [get_event_prediction](#get_event_prediction)
    - [get_event_types](#get_event_types)
    - [get_external_models](#get_external_models)
    - [get_kms_encryption_key](#get_kms_encryption_key)
    - [get_labels](#get_labels)
    - [get_model_version](#get_model_version)
    - [get_models](#get_models)
    - [get_outcomes](#get_outcomes)
    - [get_rules](#get_rules)
    - [get_variables](#get_variables)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_detector](#put_detector)
    - [put_entity_type](#put_entity_type)
    - [put_event_type](#put_event_type)
    - [put_external_model](#put_external_model)
    - [put_kms_encryption_key](#put_kms_encryption_key)
    - [put_label](#put_label)
    - [put_outcome](#put_outcome)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_detector_version](#update_detector_version)
    - [update_detector_version_metadata](#update_detector_version_metadata)
    - [update_detector_version_status](#update_detector_version_status)
    - [update_model](#update_model)
    - [update_model_version](#update_model_version)
    - [update_model_version_status](#update_model_version_status)
    - [update_rule_metadata](#update_rule_metadata)
    - [update_rule_version](#update_rule_version)
    - [update_variable](#update_variable)

## FraudDetectorClient

Type annotations for `boto3.client("frauddetector")`

Can be used directly:

```python
from mypy_boto3_frauddetector.client import FraudDetectorClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_frauddetector.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### batch_create_variable

Type annotations for `boto3.client("frauddetector").batch_create_variable` method.

[Client.batch_create_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.batch_create_variable)

```python
def batch_create_variable(
    self,
    variableEntries: List[VariableEntryTypeDef],
    tags: List["TagTypeDef"] = None
) -> BatchCreateVariableResultTypeDef:
    pass
```

### batch_get_variable

Type annotations for `boto3.client("frauddetector").batch_get_variable` method.

[Client.batch_get_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.batch_get_variable)

```python
def batch_get_variable(
    self,
    names: List[str]
) -> BatchGetVariableResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("frauddetector").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_batch_prediction_job

Type annotations for `boto3.client("frauddetector").cancel_batch_prediction_job` method.

[Client.cancel_batch_prediction_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.cancel_batch_prediction_job)

```python
def cancel_batch_prediction_job(
    self,
    jobId: str
) -> Dict[str, Any]:
    pass
```

### create_batch_prediction_job

Type annotations for `boto3.client("frauddetector").create_batch_prediction_job` method.

[Client.create_batch_prediction_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.create_batch_prediction_job)

```python
def create_batch_prediction_job(
    self,
    jobId: str,
    inputPath: str,
    outputPath: str,
    eventTypeName: str,
    detectorName: str,
    iamRoleArn: str,
    detectorVersion: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### create_detector_version

Type annotations for `boto3.client("frauddetector").create_detector_version` method.

[Client.create_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.create_detector_version)

```python
def create_detector_version(
    self,
    detectorId: str,
    rules: List["RuleTypeDef"],
    description: str = None,
    externalModelEndpoints: List[str] = None,
    modelVersions: List["ModelVersionTypeDef"] = None,
    ruleExecutionMode: RuleExecutionMode = None,
    tags: List["TagTypeDef"] = None
) -> CreateDetectorVersionResultTypeDef:
    pass
```

### create_model

Type annotations for `boto3.client("frauddetector").create_model` method.

[Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.create_model)

```python
def create_model(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    eventTypeName: str,
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### create_model_version

Type annotations for `boto3.client("frauddetector").create_model_version` method.

[Client.create_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.create_model_version)

```python
def create_model_version(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    trainingDataSource: Literal['EXTERNAL_EVENTS'],
    trainingDataSchema: "TrainingDataSchemaTypeDef",
    externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
    tags: List["TagTypeDef"] = None
) -> CreateModelVersionResultTypeDef:
    pass
```

### create_rule

Type annotations for `boto3.client("frauddetector").create_rule` method.

[Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.create_rule)

```python
def create_rule(
    self,
    ruleId: str,
    detectorId: str,
    expression: str,
    language: Literal['DETECTORPL'],
    outcomes: List[str],
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> CreateRuleResultTypeDef:
    pass
```

### create_variable

Type annotations for `boto3.client("frauddetector").create_variable` method.

[Client.create_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.create_variable)

```python
def create_variable(
    self,
    name: str,
    dataType: DataType,
    dataSource: DataSource,
    defaultValue: str,
    description: str = None,
    variableType: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### delete_batch_prediction_job

Type annotations for `boto3.client("frauddetector").delete_batch_prediction_job` method.

[Client.delete_batch_prediction_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_batch_prediction_job)

```python
def delete_batch_prediction_job(
    self,
    jobId: str
) -> Dict[str, Any]:
    pass
```

### delete_detector

Type annotations for `boto3.client("frauddetector").delete_detector` method.

[Client.delete_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_detector)

```python
def delete_detector(
    self,
    detectorId: str
) -> Dict[str, Any]:
    pass
```

### delete_detector_version

Type annotations for `boto3.client("frauddetector").delete_detector_version` method.

[Client.delete_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_detector_version)

```python
def delete_detector_version(
    self,
    detectorId: str,
    detectorVersionId: str
) -> Dict[str, Any]:
    pass
```

### delete_entity_type

Type annotations for `boto3.client("frauddetector").delete_entity_type` method.

[Client.delete_entity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_entity_type)

```python
def delete_entity_type(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### delete_event

Type annotations for `boto3.client("frauddetector").delete_event` method.

[Client.delete_event documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_event)

```python
def delete_event(
    self,
    eventId: str,
    eventTypeName: str
) -> Dict[str, Any]:
    pass
```

### delete_event_type

Type annotations for `boto3.client("frauddetector").delete_event_type` method.

[Client.delete_event_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_event_type)

```python
def delete_event_type(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### delete_external_model

Type annotations for `boto3.client("frauddetector").delete_external_model` method.

[Client.delete_external_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_external_model)

```python
def delete_external_model(
    self,
    modelEndpoint: str
) -> Dict[str, Any]:
    pass
```

### delete_label

Type annotations for `boto3.client("frauddetector").delete_label` method.

[Client.delete_label documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_label)

```python
def delete_label(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### delete_model

Type annotations for `boto3.client("frauddetector").delete_model` method.

[Client.delete_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_model)

```python
def delete_model(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS']
) -> Dict[str, Any]:
    pass
```

### delete_model_version

Type annotations for `boto3.client("frauddetector").delete_model_version` method.

[Client.delete_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_model_version)

```python
def delete_model_version(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    modelVersionNumber: str
) -> Dict[str, Any]:
    pass
```

### delete_outcome

Type annotations for `boto3.client("frauddetector").delete_outcome` method.

[Client.delete_outcome documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_outcome)

```python
def delete_outcome(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### delete_rule

Type annotations for `boto3.client("frauddetector").delete_rule` method.

[Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_rule)

```python
def delete_rule(
    self,
    rule: "RuleTypeDef"
) -> Dict[str, Any]:
    pass
```

### delete_variable

Type annotations for `boto3.client("frauddetector").delete_variable` method.

[Client.delete_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.delete_variable)

```python
def delete_variable(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### describe_detector

Type annotations for `boto3.client("frauddetector").describe_detector` method.

[Client.describe_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.describe_detector)

```python
def describe_detector(
    self,
    detectorId: str,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeDetectorResultTypeDef:
    pass
```

### describe_model_versions

Type annotations for `boto3.client("frauddetector").describe_model_versions` method.

[Client.describe_model_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.describe_model_versions)

```python
def describe_model_versions(
    self,
    modelId: str = None,
    modelVersionNumber: str = None,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeModelVersionsResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("frauddetector").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.generate_presigned_url)

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

### get_batch_prediction_jobs

Type annotations for `boto3.client("frauddetector").get_batch_prediction_jobs` method.

[Client.get_batch_prediction_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_batch_prediction_jobs)

```python
def get_batch_prediction_jobs(
    self,
    jobId: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> GetBatchPredictionJobsResultTypeDef:
    pass
```

### get_detector_version

Type annotations for `boto3.client("frauddetector").get_detector_version` method.

[Client.get_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_detector_version)

```python
def get_detector_version(
    self,
    detectorId: str,
    detectorVersionId: str
) -> GetDetectorVersionResultTypeDef:
    pass
```

### get_detectors

Type annotations for `boto3.client("frauddetector").get_detectors` method.

[Client.get_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_detectors)

```python
def get_detectors(
    self,
    detectorId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetDetectorsResultTypeDef:
    pass
```

### get_entity_types

Type annotations for `boto3.client("frauddetector").get_entity_types` method.

[Client.get_entity_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_entity_types)

```python
def get_entity_types(
    self,
    name: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetEntityTypesResultTypeDef:
    pass
```

### get_event_prediction

Type annotations for `boto3.client("frauddetector").get_event_prediction` method.

[Client.get_event_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_event_prediction)

```python
def get_event_prediction(
    self,
    detectorId: str,
    eventId: str,
    eventTypeName: str,
    entities: List[EntityTypeDef],
    eventTimestamp: str,
    eventVariables: Dict[str, str],
    detectorVersionId: str = None,
    externalModelEndpointDataBlobs: Dict[str, ModelEndpointDataBlobTypeDef] = None
) -> GetEventPredictionResultTypeDef:
    pass
```

### get_event_types

Type annotations for `boto3.client("frauddetector").get_event_types` method.

[Client.get_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_event_types)

```python
def get_event_types(
    self,
    name: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetEventTypesResultTypeDef:
    pass
```

### get_external_models

Type annotations for `boto3.client("frauddetector").get_external_models` method.

[Client.get_external_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_external_models)

```python
def get_external_models(
    self,
    modelEndpoint: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetExternalModelsResultTypeDef:
    pass
```

### get_kms_encryption_key

Type annotations for `boto3.client("frauddetector").get_kms_encryption_key` method.

[Client.get_kms_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_kms_encryption_key)

```python
def get_kms_encryption_key(
    self
) -> GetKMSEncryptionKeyResultTypeDef:
    pass
```

### get_labels

Type annotations for `boto3.client("frauddetector").get_labels` method.

[Client.get_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_labels)

```python
def get_labels(
    self,
    name: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetLabelsResultTypeDef:
    pass
```

### get_model_version

Type annotations for `boto3.client("frauddetector").get_model_version` method.

[Client.get_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_model_version)

```python
def get_model_version(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    modelVersionNumber: str
) -> GetModelVersionResultTypeDef:
    pass
```

### get_models

Type annotations for `boto3.client("frauddetector").get_models` method.

[Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_models)

```python
def get_models(
    self,
    modelId: str = None,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'] = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetModelsResultTypeDef:
    pass
```

### get_outcomes

Type annotations for `boto3.client("frauddetector").get_outcomes` method.

[Client.get_outcomes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_outcomes)

```python
def get_outcomes(
    self,
    name: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetOutcomesResultTypeDef:
    pass
```

### get_rules

Type annotations for `boto3.client("frauddetector").get_rules` method.

[Client.get_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_rules)

```python
def get_rules(
    self,
    detectorId: str,
    ruleId: str = None,
    ruleVersion: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetRulesResultTypeDef:
    pass
```

### get_variables

Type annotations for `boto3.client("frauddetector").get_variables` method.

[Client.get_variables documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.get_variables)

```python
def get_variables(
    self,
    name: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetVariablesResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("frauddetector").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceARN: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListTagsForResourceResultTypeDef:
    pass
```

### put_detector

Type annotations for `boto3.client("frauddetector").put_detector` method.

[Client.put_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_detector)

```python
def put_detector(
    self,
    detectorId: str,
    eventTypeName: str,
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_entity_type

Type annotations for `boto3.client("frauddetector").put_entity_type` method.

[Client.put_entity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_entity_type)

```python
def put_entity_type(
    self,
    name: str,
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_event_type

Type annotations for `boto3.client("frauddetector").put_event_type` method.

[Client.put_event_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_event_type)

```python
def put_event_type(
    self,
    name: str,
    eventVariables: List[str],
    entityTypes: List[str],
    description: str = None,
    labels: List[str] = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_external_model

Type annotations for `boto3.client("frauddetector").put_external_model` method.

[Client.put_external_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_external_model)

```python
def put_external_model(
    self,
    modelEndpoint: str,
    modelSource: Literal['SAGEMAKER'],
    invokeModelEndpointRoleArn: str,
    inputConfiguration: "ModelInputConfigurationTypeDef",
    outputConfiguration: "ModelOutputConfigurationTypeDef",
    modelEndpointStatus: ModelEndpointStatus,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_kms_encryption_key

Type annotations for `boto3.client("frauddetector").put_kms_encryption_key` method.

[Client.put_kms_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_kms_encryption_key)

```python
def put_kms_encryption_key(
    self,
    kmsEncryptionKeyArn: str
) -> Dict[str, Any]:
    pass
```

### put_label

Type annotations for `boto3.client("frauddetector").put_label` method.

[Client.put_label documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_label)

```python
def put_label(
    self,
    name: str,
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_outcome

Type annotations for `boto3.client("frauddetector").put_outcome` method.

[Client.put_outcome documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.put_outcome)

```python
def put_outcome(
    self,
    name: str,
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("frauddetector").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceARN: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("frauddetector").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceARN: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_detector_version

Type annotations for `boto3.client("frauddetector").update_detector_version` method.

[Client.update_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version)

```python
def update_detector_version(
    self,
    detectorId: str,
    detectorVersionId: str,
    externalModelEndpoints: List[str],
    rules: List["RuleTypeDef"],
    description: str = None,
    modelVersions: List["ModelVersionTypeDef"] = None,
    ruleExecutionMode: RuleExecutionMode = None
) -> Dict[str, Any]:
    pass
```

### update_detector_version_metadata

Type annotations for `boto3.client("frauddetector").update_detector_version_metadata` method.

[Client.update_detector_version_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_metadata)

```python
def update_detector_version_metadata(
    self,
    detectorId: str,
    detectorVersionId: str,
    description: str
) -> Dict[str, Any]:
    pass
```

### update_detector_version_status

Type annotations for `boto3.client("frauddetector").update_detector_version_status` method.

[Client.update_detector_version_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_status)

```python
def update_detector_version_status(
    self,
    detectorId: str,
    detectorVersionId: str,
    status: DetectorVersionStatus
) -> Dict[str, Any]:
    pass
```

### update_model

Type annotations for `boto3.client("frauddetector").update_model` method.

[Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_model)

```python
def update_model(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    description: str = None
) -> Dict[str, Any]:
    pass
```

### update_model_version

Type annotations for `boto3.client("frauddetector").update_model_version` method.

[Client.update_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_model_version)

```python
def update_model_version(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    majorVersionNumber: str,
    externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
    tags: List["TagTypeDef"] = None
) -> UpdateModelVersionResultTypeDef:
    pass
```

### update_model_version_status

Type annotations for `boto3.client("frauddetector").update_model_version_status` method.

[Client.update_model_version_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_model_version_status)

```python
def update_model_version_status(
    self,
    modelId: str,
    modelType: Literal['ONLINE_FRAUD_INSIGHTS'],
    modelVersionNumber: str,
    status: ModelVersionStatus
) -> Dict[str, Any]:
    pass
```

### update_rule_metadata

Type annotations for `boto3.client("frauddetector").update_rule_metadata` method.

[Client.update_rule_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_rule_metadata)

```python
def update_rule_metadata(
    self,
    rule: "RuleTypeDef",
    description: str
) -> Dict[str, Any]:
    pass
```

### update_rule_version

Type annotations for `boto3.client("frauddetector").update_rule_version` method.

[Client.update_rule_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_rule_version)

```python
def update_rule_version(
    self,
    rule: "RuleTypeDef",
    expression: str,
    language: Literal['DETECTORPL'],
    outcomes: List[str],
    description: str = None,
    tags: List["TagTypeDef"] = None
) -> UpdateRuleVersionResultTypeDef:
    pass
```

### update_variable

Type annotations for `boto3.client("frauddetector").update_variable` method.

[Client.update_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector.Client.update_variable)

```python
def update_variable(
    self,
    name: str,
    defaultValue: str = None,
    description: str = None,
    variableType: str = None
) -> Dict[str, Any]:
    pass
```



