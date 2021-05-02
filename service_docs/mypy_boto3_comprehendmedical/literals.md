# Literals for boto3 ComprehendMedical module

> [Index](../index.md) > [ComprehendMedical](./index.md) > Literals

Auto-generated documentation for [ComprehendMedical](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html#ComprehendMedical)
type annotations stubs module [mypy_boto3_comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/).

- [Literals for boto3 ComprehendMedical module](#literals-for-boto3-comprehendmedical-module)
  - [AttributeName](#attributename)
  - [EntitySubType](#entitysubtype)
  - [EntityType](#entitytype)
  - [ICD10CMAttributeType](#icd10cmattributetype)
  - [ICD10CMEntityCategory](#icd10cmentitycategory)
  - [ICD10CMEntityType](#icd10cmentitytype)
  - [ICD10CMRelationshipType](#icd10cmrelationshiptype)
  - [ICD10CMTraitName](#icd10cmtraitname)
  - [JobStatus](#jobstatus)
  - [LanguageCode](#languagecode)
  - [RelationshipType](#relationshiptype)
  - [RxNormAttributeType](#rxnormattributetype)
  - [RxNormEntityCategory](#rxnormentitycategory)
  - [RxNormEntityType](#rxnormentitytype)
  - [RxNormTraitName](#rxnormtraitname)

## AttributeName

```python
from mypy_boto3_comprehendmedical.literals import AttributeName
```

Values:

- `DIAGNOSIS`
- `NEGATION`
- `SIGN`
- `SYMPTOM`

## EntitySubType

```python
from mypy_boto3_comprehendmedical.literals import EntitySubType
```

Values:

- `ACUITY`
- `ADDRESS`
- `AGE`
- `BRAND_NAME`
- `CONTACT_POINT`
- `DATE`
- `DIRECTION`
- `DOSAGE`
- `DURATION`
- `EMAIL`
- `FORM`
- `FREQUENCY`
- `GENERIC_NAME`
- `IDENTIFIER`
- `NAME`
- `PROCEDURE_NAME`
- `PROFESSION`
- `QUALITY`
- `QUANTITY`
- `RATE`
- `ROUTE_OR_MODE`
- `STRENGTH`
- `SYSTEM_ORGAN_SITE`
- `TEST_NAME`
- `TEST_UNITS`
- `TEST_VALUE`
- `TIME_EXPRESSION`
- `TIME_TO_DX_NAME`
- `TIME_TO_MEDICATION_NAME`
- `TIME_TO_PROCEDURE_NAME`
- `TIME_TO_TEST_NAME`
- `TIME_TO_TREATMENT_NAME`
- `TREATMENT_NAME`
- `URL`

## EntityType

```python
from mypy_boto3_comprehendmedical.literals import EntityType
```

Values:

- `ANATOMY`
- `MEDICAL_CONDITION`
- `MEDICATION`
- `PROTECTED_HEALTH_INFORMATION`
- `TEST_TREATMENT_PROCEDURE`
- `TIME_EXPRESSION`

## ICD10CMAttributeType

```python
from mypy_boto3_comprehendmedical.literals import ICD10CMAttributeType
```

Values:

- `ACUITY`
- `DIRECTION`
- `QUALITY`
- `QUANTITY`
- `SYSTEM_ORGAN_SITE`
- `TIME_EXPRESSION`
- `TIME_TO_DX_NAME`

## ICD10CMEntityCategory

```python
from mypy_boto3_comprehendmedical.literals import ICD10CMEntityCategory
```

Values:

- `MEDICAL_CONDITION`

## ICD10CMEntityType

```python
from mypy_boto3_comprehendmedical.literals import ICD10CMEntityType
```

Values:

- `DX_NAME`
- `TIME_EXPRESSION`

## ICD10CMRelationshipType

```python
from mypy_boto3_comprehendmedical.literals import ICD10CMRelationshipType
```

Values:

- `OVERLAP`
- `SYSTEM_ORGAN_SITE`

## ICD10CMTraitName

```python
from mypy_boto3_comprehendmedical.literals import ICD10CMTraitName
```

Values:

- `DIAGNOSIS`
- `NEGATION`
- `SIGN`
- `SYMPTOM`

## JobStatus

```python
from mypy_boto3_comprehendmedical.literals import JobStatus
```

Values:

- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`
- `PARTIAL_SUCCESS`
- `STOP_REQUESTED`
- `STOPPED`
- `SUBMITTED`

## LanguageCode

```python
from mypy_boto3_comprehendmedical.literals import LanguageCode
```

Values:

- `en`

## RelationshipType

```python
from mypy_boto3_comprehendmedical.literals import RelationshipType
```

Values:

- `ACUITY`
- `ADMINISTERED_VIA`
- `DIRECTION`
- `DOSAGE`
- `DURATION`
- `EVERY`
- `FOR`
- `FORM`
- `FREQUENCY`
- `NEGATIVE`
- `OVERLAP`
- `RATE`
- `ROUTE_OR_MODE`
- `STRENGTH`
- `SYSTEM_ORGAN_SITE`
- `TEST_UNITS`
- `TEST_VALUE`
- `WITH_DOSAGE`

## RxNormAttributeType

```python
from mypy_boto3_comprehendmedical.literals import RxNormAttributeType
```

Values:

- `DOSAGE`
- `DURATION`
- `FORM`
- `FREQUENCY`
- `RATE`
- `ROUTE_OR_MODE`
- `STRENGTH`

## RxNormEntityCategory

```python
from mypy_boto3_comprehendmedical.literals import RxNormEntityCategory
```

Values:

- `MEDICATION`

## RxNormEntityType

```python
from mypy_boto3_comprehendmedical.literals import RxNormEntityType
```

Values:

- `BRAND_NAME`
- `GENERIC_NAME`

## RxNormTraitName

```python
from mypy_boto3_comprehendmedical.literals import RxNormTraitName
```

Values:

- `NEGATION`
