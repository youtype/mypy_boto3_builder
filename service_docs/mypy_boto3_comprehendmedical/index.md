# Type annotations for boto3 ComprehendMedical module

> [Index](../index.md) > ComprehendMedical

Auto-generated documentation for [ComprehendMedical](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical)
type annotations stubs module [mypy_boto3_comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/).

```bash
pip install mypy-boto3-comprehendmedical
```

- [Type annotations for boto3 ComprehendMedical module](#type-annotations-for-boto3-comprehendmedical-module)
  - [ComprehendMedicalClient](#comprehendmedicalclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## ComprehendMedicalClient

Type annotations for  `boto3.client("comprehendmedical")` as [ComprehendMedicalClient](./client.md)

Can be used directly:

```python
from mypy_boto3_comprehendmedical.client import ComprehendMedicalClient
```


ComprehendMedicalClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [describe_entities_detection_v2_job](./client.md#describe-entities-detection-v2-job)
- [describe_icd10_cm_inference_job](./client.md#describe-icd10-cm-inference-job)
- [describe_phi_detection_job](./client.md#describe-phi-detection-job)
- [describe_rx_norm_inference_job](./client.md#describe-rx-norm-inference-job)
- [detect_entities](./client.md#detect-entities)
- [detect_entities_v2](./client.md#detect-entities-v2)
- [detect_phi](./client.md#detect-phi)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [infer_icd10_cm](./client.md#infer-icd10-cm)
- [infer_rx_norm](./client.md#infer-rx-norm)
- [list_entities_detection_v2_jobs](./client.md#list-entities-detection-v2-jobs)
- [list_icd10_cm_inference_jobs](./client.md#list-icd10-cm-inference-jobs)
- [list_phi_detection_jobs](./client.md#list-phi-detection-jobs)
- [list_rx_norm_inference_jobs](./client.md#list-rx-norm-inference-jobs)
- [start_entities_detection_v2_job](./client.md#start-entities-detection-v2-job)
- [start_icd10_cm_inference_job](./client.md#start-icd10-cm-inference-job)
- [start_phi_detection_job](./client.md#start-phi-detection-job)
- [start_rx_norm_inference_job](./client.md#start-rx-norm-inference-job)
- [stop_entities_detection_v2_job](./client.md#stop-entities-detection-v2-job)
- [stop_icd10_cm_inference_job](./client.md#stop-icd10-cm-inference-job)
- [stop_phi_detection_job](./client.md#stop-phi-detection-job)
- [stop_rx_norm_inference_job](./client.md#stop-rx-norm-inference-job)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [InvalidEncodingException](./client.md#invalidencodingexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TextSizeLimitExceededException](./client.md#textsizelimitexceededexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_comprehendmedical.literals import AttributeName, ...
```

- [AttributeName](./literals.md#attributename)
- [EntitySubType](./literals.md#entitysubtype)
- [EntityType](./literals.md#entitytype)
- [ICD10CMAttributeType](./literals.md#icd10cmattributetype)
- [ICD10CMEntityCategory](./literals.md#icd10cmentitycategory)
- [ICD10CMEntityType](./literals.md#icd10cmentitytype)
- [ICD10CMRelationshipType](./literals.md#icd10cmrelationshiptype)
- [ICD10CMTraitName](./literals.md#icd10cmtraitname)
- [JobStatus](./literals.md#jobstatus)
- [LanguageCode](./literals.md#languagecode)
- [RelationshipType](./literals.md#relationshiptype)
- [RxNormAttributeType](./literals.md#rxnormattributetype)
- [RxNormEntityCategory](./literals.md#rxnormentitycategory)
- [RxNormEntityType](./literals.md#rxnormentitytype)
- [RxNormTraitName](./literals.md#rxnormtraitname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_comprehendmedical.type_defs import AttributeTypeDef, ...
```

- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [ComprehendMedicalAsyncJobPropertiesTypeDef](./type_defs.md#comprehendmedicalasyncjobpropertiestypedef)
- [EntityTypeDef](./type_defs.md#entitytypedef)
- [ICD10CMAttributeTypeDef](./type_defs.md#icd10cmattributetypedef)
- [ICD10CMConceptTypeDef](./type_defs.md#icd10cmconcepttypedef)
- [ICD10CMEntityTypeDef](./type_defs.md#icd10cmentitytypedef)
- [ICD10CMTraitTypeDef](./type_defs.md#icd10cmtraittypedef)
- [InputDataConfigTypeDef](./type_defs.md#inputdataconfigtypedef)
- [OutputDataConfigTypeDef](./type_defs.md#outputdataconfigtypedef)
- [RxNormAttributeTypeDef](./type_defs.md#rxnormattributetypedef)
- [RxNormConceptTypeDef](./type_defs.md#rxnormconcepttypedef)
- [RxNormEntityTypeDef](./type_defs.md#rxnormentitytypedef)
- [RxNormTraitTypeDef](./type_defs.md#rxnormtraittypedef)
- [TraitTypeDef](./type_defs.md#traittypedef)
- [UnmappedAttributeTypeDef](./type_defs.md#unmappedattributetypedef)
- [ComprehendMedicalAsyncJobFilterTypeDef](./type_defs.md#comprehendmedicalasyncjobfiltertypedef)
- [DescribeEntitiesDetectionV2JobResponseTypeDef](./type_defs.md#describeentitiesdetectionv2jobresponsetypedef)
- [DescribeICD10CMInferenceJobResponseTypeDef](./type_defs.md#describeicd10cminferencejobresponsetypedef)
- [DescribePHIDetectionJobResponseTypeDef](./type_defs.md#describephidetectionjobresponsetypedef)
- [DescribeRxNormInferenceJobResponseTypeDef](./type_defs.md#describerxnorminferencejobresponsetypedef)
- [DetectEntitiesResponseTypeDef](./type_defs.md#detectentitiesresponsetypedef)
- [DetectEntitiesV2ResponseTypeDef](./type_defs.md#detectentitiesv2responsetypedef)
- [DetectPHIResponseTypeDef](./type_defs.md#detectphiresponsetypedef)
- [InferICD10CMResponseTypeDef](./type_defs.md#infericd10cmresponsetypedef)
- [InferRxNormResponseTypeDef](./type_defs.md#inferrxnormresponsetypedef)
- [ListEntitiesDetectionV2JobsResponseTypeDef](./type_defs.md#listentitiesdetectionv2jobsresponsetypedef)
- [ListICD10CMInferenceJobsResponseTypeDef](./type_defs.md#listicd10cminferencejobsresponsetypedef)
- [ListPHIDetectionJobsResponseTypeDef](./type_defs.md#listphidetectionjobsresponsetypedef)
- [ListRxNormInferenceJobsResponseTypeDef](./type_defs.md#listrxnorminferencejobsresponsetypedef)
- [StartEntitiesDetectionV2JobResponseTypeDef](./type_defs.md#startentitiesdetectionv2jobresponsetypedef)
- [StartICD10CMInferenceJobResponseTypeDef](./type_defs.md#starticd10cminferencejobresponsetypedef)
- [StartPHIDetectionJobResponseTypeDef](./type_defs.md#startphidetectionjobresponsetypedef)
- [StartRxNormInferenceJobResponseTypeDef](./type_defs.md#startrxnorminferencejobresponsetypedef)
- [StopEntitiesDetectionV2JobResponseTypeDef](./type_defs.md#stopentitiesdetectionv2jobresponsetypedef)
- [StopICD10CMInferenceJobResponseTypeDef](./type_defs.md#stopicd10cminferencejobresponsetypedef)
- [StopPHIDetectionJobResponseTypeDef](./type_defs.md#stopphidetectionjobresponsetypedef)
- [StopRxNormInferenceJobResponseTypeDef](./type_defs.md#stoprxnorminferencejobresponsetypedef)
