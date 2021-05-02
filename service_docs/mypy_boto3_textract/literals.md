# Literals for boto3 Textract module

> [Index](../index.md) > [Textract](./index.md) > Literals

Auto-generated documentation for [Textract](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract)
type annotations stubs module [mypy_boto3_textract](https://pypi.org/project/mypy-boto3-textract/).

- [Literals for boto3 Textract module](#literals-for-boto3-textract-module)
  - [BlockType](#blocktype)
  - [ContentClassifier](#contentclassifier)
  - [EntityType](#entitytype)
  - [FeatureType](#featuretype)
  - [JobStatus](#jobstatus)
  - [RelationshipType](#relationshiptype)
  - [SelectionStatus](#selectionstatus)
  - [TextType](#texttype)

## BlockType

```python
from mypy_boto3_textract.literals import BlockType
```

Values:

- `CELL`
- `KEY_VALUE_SET`
- `LINE`
- `PAGE`
- `SELECTION_ELEMENT`
- `TABLE`
- `WORD`

## ContentClassifier

```python
from mypy_boto3_textract.literals import ContentClassifier
```

Values:

- `FreeOfAdultContent`
- `FreeOfPersonallyIdentifiableInformation`

## EntityType

```python
from mypy_boto3_textract.literals import EntityType
```

Values:

- `KEY`
- `VALUE`

## FeatureType

```python
from mypy_boto3_textract.literals import FeatureType
```

Values:

- `FORMS`
- `TABLES`

## JobStatus

```python
from mypy_boto3_textract.literals import JobStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `PARTIAL_SUCCESS`
- `SUCCEEDED`

## RelationshipType

```python
from mypy_boto3_textract.literals import RelationshipType
```

Values:

- `CHILD`
- `COMPLEX_FEATURES`
- `VALUE`

## SelectionStatus

```python
from mypy_boto3_textract.literals import SelectionStatus
```

Values:

- `NOT_SELECTED`
- `SELECTED`

## TextType

```python
from mypy_boto3_textract.literals import TextType
```

Values:

- `HANDWRITING`
- `PRINTED`
