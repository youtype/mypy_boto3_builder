# Structures for boto3 ComprehendMedical module

> [Index](../index.md) > [ComprehendMedical](./index.md) > Structures

Auto-generated documentation for [ComprehendMedical](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical)
type annotations stubs module [mypy_boto3_comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/).

- [Structures for boto3 ComprehendMedical module](#structures-for-boto3-comprehendmedical-module)
  - [AttributeTypeDef](#attributetypedef)
  - [ComprehendMedicalAsyncJobFilterTypeDef](#comprehendmedicalasyncjobfiltertypedef)
  - [ComprehendMedicalAsyncJobPropertiesTypeDef](#comprehendmedicalasyncjobpropertiestypedef)
  - [DescribeEntitiesDetectionV2JobResponseTypeDef](#describeentitiesdetectionv2jobresponsetypedef)
  - [DescribeICD10CMInferenceJobResponseTypeDef](#describeicd10cminferencejobresponsetypedef)
  - [DescribePHIDetectionJobResponseTypeDef](#describephidetectionjobresponsetypedef)
  - [DescribeRxNormInferenceJobResponseTypeDef](#describerxnorminferencejobresponsetypedef)
  - [DetectEntitiesResponseTypeDef](#detectentitiesresponsetypedef)
  - [DetectEntitiesV2ResponseTypeDef](#detectentitiesv2responsetypedef)
  - [DetectPHIResponseTypeDef](#detectphiresponsetypedef)
  - [EntityTypeDef](#entitytypedef)
  - [ICD10CMAttributeTypeDef](#icd10cmattributetypedef)
  - [ICD10CMConceptTypeDef](#icd10cmconcepttypedef)
  - [ICD10CMEntityTypeDef](#icd10cmentitytypedef)
  - [ICD10CMTraitTypeDef](#icd10cmtraittypedef)
  - [InferICD10CMResponseTypeDef](#infericd10cmresponsetypedef)
  - [InferRxNormResponseTypeDef](#inferrxnormresponsetypedef)
  - [InputDataConfigTypeDef](#inputdataconfigtypedef)
  - [ListEntitiesDetectionV2JobsResponseTypeDef](#listentitiesdetectionv2jobsresponsetypedef)
  - [ListICD10CMInferenceJobsResponseTypeDef](#listicd10cminferencejobsresponsetypedef)
  - [ListPHIDetectionJobsResponseTypeDef](#listphidetectionjobsresponsetypedef)
  - [ListRxNormInferenceJobsResponseTypeDef](#listrxnorminferencejobsresponsetypedef)
  - [OutputDataConfigTypeDef](#outputdataconfigtypedef)
  - [RxNormAttributeTypeDef](#rxnormattributetypedef)
  - [RxNormConceptTypeDef](#rxnormconcepttypedef)
  - [RxNormEntityTypeDef](#rxnormentitytypedef)
  - [RxNormTraitTypeDef](#rxnormtraittypedef)
  - [StartEntitiesDetectionV2JobResponseTypeDef](#startentitiesdetectionv2jobresponsetypedef)
  - [StartICD10CMInferenceJobResponseTypeDef](#starticd10cminferencejobresponsetypedef)
  - [StartPHIDetectionJobResponseTypeDef](#startphidetectionjobresponsetypedef)
  - [StartRxNormInferenceJobResponseTypeDef](#startrxnorminferencejobresponsetypedef)
  - [StopEntitiesDetectionV2JobResponseTypeDef](#stopentitiesdetectionv2jobresponsetypedef)
  - [StopICD10CMInferenceJobResponseTypeDef](#stopicd10cminferencejobresponsetypedef)
  - [StopPHIDetectionJobResponseTypeDef](#stopphidetectionjobresponsetypedef)
  - [StopRxNormInferenceJobResponseTypeDef](#stoprxnorminferencejobresponsetypedef)
  - [TraitTypeDef](#traittypedef)
  - [UnmappedAttributeTypeDef](#unmappedattributetypedef)

## AttributeTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import AttributeTypeDef
```




Optional fields:
- `Type`: `EntitySubType`
- `Score`: `float`
- `RelationshipScore`: `float`
- `RelationshipType`: `RelationshipType`
- `Id`: `int`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `Text`: `str`
- `Category`: `EntityType`
- `Traits`: `List["TraitTypeDef"]`


## ComprehendMedicalAsyncJobFilterTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ComprehendMedicalAsyncJobFilterTypeDef
```




Optional fields:
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `SubmitTimeBefore`: `datetime`
- `SubmitTimeAfter`: `datetime`


## ComprehendMedicalAsyncJobPropertiesTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ComprehendMedicalAsyncJobPropertiesTypeDef
```




Optional fields:
- `JobId`: `str`
- `JobName`: `str`
- `JobStatus`: `JobStatus`
- `Message`: `str`
- `SubmitTime`: `datetime`
- `EndTime`: `datetime`
- `ExpirationTime`: `datetime`
- `InputDataConfig`: `"InputDataConfigTypeDef"`
- `OutputDataConfig`: `"OutputDataConfigTypeDef"`
- `LanguageCode`: `Literal['en']`
- `DataAccessRoleArn`: `str`
- `ManifestFilePath`: `str`
- `KMSKey`: `str`
- `ModelVersion`: `str`


## DescribeEntitiesDetectionV2JobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DescribeEntitiesDetectionV2JobResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobProperties`: `"ComprehendMedicalAsyncJobPropertiesTypeDef"`


## DescribeICD10CMInferenceJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DescribeICD10CMInferenceJobResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobProperties`: `"ComprehendMedicalAsyncJobPropertiesTypeDef"`


## DescribePHIDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DescribePHIDetectionJobResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobProperties`: `"ComprehendMedicalAsyncJobPropertiesTypeDef"`


## DescribeRxNormInferenceJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DescribeRxNormInferenceJobResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobProperties`: `"ComprehendMedicalAsyncJobPropertiesTypeDef"`


## DetectEntitiesResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DetectEntitiesResponseTypeDef
```


Required fields:
- `Entities`: `List["EntityTypeDef"]`
- `ModelVersion`: `str`



Optional fields:
- `UnmappedAttributes`: `List["UnmappedAttributeTypeDef"]`
- `PaginationToken`: `str`


## DetectEntitiesV2ResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DetectEntitiesV2ResponseTypeDef
```


Required fields:
- `Entities`: `List["EntityTypeDef"]`
- `ModelVersion`: `str`



Optional fields:
- `UnmappedAttributes`: `List["UnmappedAttributeTypeDef"]`
- `PaginationToken`: `str`


## DetectPHIResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import DetectPHIResponseTypeDef
```


Required fields:
- `Entities`: `List["EntityTypeDef"]`
- `ModelVersion`: `str`



Optional fields:
- `PaginationToken`: `str`


## EntityTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import EntityTypeDef
```




Optional fields:
- `Id`: `int`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `Score`: `float`
- `Text`: `str`
- `Category`: `EntityType`
- `Type`: `EntitySubType`
- `Traits`: `List["TraitTypeDef"]`
- `Attributes`: `List["AttributeTypeDef"]`


## ICD10CMAttributeTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ICD10CMAttributeTypeDef
```




Optional fields:
- `Type`: `ICD10CMAttributeType`
- `Score`: `float`
- `RelationshipScore`: `float`
- `Id`: `int`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `Text`: `str`
- `Traits`: `List["ICD10CMTraitTypeDef"]`
- `Category`: `ICD10CMEntityType`
- `RelationshipType`: `ICD10CMRelationshipType`


## ICD10CMConceptTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ICD10CMConceptTypeDef
```




Optional fields:
- `Description`: `str`
- `Code`: `str`
- `Score`: `float`


## ICD10CMEntityTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ICD10CMEntityTypeDef
```




Optional fields:
- `Id`: `int`
- `Text`: `str`
- `Category`: `Literal['MEDICAL_CONDITION']`
- `Type`: `ICD10CMEntityType`
- `Score`: `float`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `Attributes`: `List["ICD10CMAttributeTypeDef"]`
- `Traits`: `List["ICD10CMTraitTypeDef"]`
- `ICD10CMConcepts`: `List["ICD10CMConceptTypeDef"]`


## ICD10CMTraitTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ICD10CMTraitTypeDef
```




Optional fields:
- `Name`: `ICD10CMTraitName`
- `Score`: `float`


## InferICD10CMResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import InferICD10CMResponseTypeDef
```


Required fields:
- `Entities`: `List["ICD10CMEntityTypeDef"]`



Optional fields:
- `PaginationToken`: `str`
- `ModelVersion`: `str`


## InferRxNormResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import InferRxNormResponseTypeDef
```


Required fields:
- `Entities`: `List["RxNormEntityTypeDef"]`



Optional fields:
- `PaginationToken`: `str`
- `ModelVersion`: `str`


## InputDataConfigTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import InputDataConfigTypeDef
```


Required fields:
- `S3Bucket`: `str`



Optional fields:
- `S3Key`: `str`


## ListEntitiesDetectionV2JobsResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ListEntitiesDetectionV2JobsResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobPropertiesList`: `List["ComprehendMedicalAsyncJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListICD10CMInferenceJobsResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ListICD10CMInferenceJobsResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobPropertiesList`: `List["ComprehendMedicalAsyncJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListPHIDetectionJobsResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ListPHIDetectionJobsResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobPropertiesList`: `List["ComprehendMedicalAsyncJobPropertiesTypeDef"]`
- `NextToken`: `str`


## ListRxNormInferenceJobsResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import ListRxNormInferenceJobsResponseTypeDef
```




Optional fields:
- `ComprehendMedicalAsyncJobPropertiesList`: `List["ComprehendMedicalAsyncJobPropertiesTypeDef"]`
- `NextToken`: `str`


## OutputDataConfigTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import OutputDataConfigTypeDef
```


Required fields:
- `S3Bucket`: `str`



Optional fields:
- `S3Key`: `str`


## RxNormAttributeTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import RxNormAttributeTypeDef
```




Optional fields:
- `Type`: `RxNormAttributeType`
- `Score`: `float`
- `RelationshipScore`: `float`
- `Id`: `int`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `Text`: `str`
- `Traits`: `List["RxNormTraitTypeDef"]`


## RxNormConceptTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import RxNormConceptTypeDef
```




Optional fields:
- `Description`: `str`
- `Code`: `str`
- `Score`: `float`


## RxNormEntityTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import RxNormEntityTypeDef
```




Optional fields:
- `Id`: `int`
- `Text`: `str`
- `Category`: `Literal['MEDICATION']`
- `Type`: `RxNormEntityType`
- `Score`: `float`
- `BeginOffset`: `int`
- `EndOffset`: `int`
- `Attributes`: `List["RxNormAttributeTypeDef"]`
- `Traits`: `List["RxNormTraitTypeDef"]`
- `RxNormConcepts`: `List["RxNormConceptTypeDef"]`


## RxNormTraitTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import RxNormTraitTypeDef
```




Optional fields:
- `Name`: `Literal['NEGATION']`
- `Score`: `float`


## StartEntitiesDetectionV2JobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StartEntitiesDetectionV2JobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartICD10CMInferenceJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StartICD10CMInferenceJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartPHIDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StartPHIDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StartRxNormInferenceJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StartRxNormInferenceJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StopEntitiesDetectionV2JobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StopEntitiesDetectionV2JobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StopICD10CMInferenceJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StopICD10CMInferenceJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StopPHIDetectionJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StopPHIDetectionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## StopRxNormInferenceJobResponseTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import StopRxNormInferenceJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`


## TraitTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import TraitTypeDef
```




Optional fields:
- `Name`: `AttributeName`
- `Score`: `float`


## UnmappedAttributeTypeDef

```python
from mypy_boto3_comprehendmedical.type_defs import UnmappedAttributeTypeDef
```




Optional fields:
- `Type`: `EntityType`
- `Attribute`: `"AttributeTypeDef"`

