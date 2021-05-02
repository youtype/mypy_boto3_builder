# Literals for boto3 FraudDetector module

> [Index](../index.md) > [FraudDetector](./index.md) > Literals

Auto-generated documentation for [FraudDetector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html#FraudDetector)
type annotations stubs module [mypy_boto3_frauddetector](https://pypi.org/project/mypy-boto3-frauddetector/).

- [Literals for boto3 FraudDetector module](#literals-for-boto3-frauddetector-module)
  - [AsyncJobStatus](#asyncjobstatus)
  - [DataSource](#datasource)
  - [DataType](#datatype)
  - [DetectorVersionStatus](#detectorversionstatus)
  - [Language](#language)
  - [ModelEndpointStatus](#modelendpointstatus)
  - [ModelInputDataFormat](#modelinputdataformat)
  - [ModelOutputDataFormat](#modeloutputdataformat)
  - [ModelSource](#modelsource)
  - [ModelTypeEnum](#modeltypeenum)
  - [ModelVersionStatus](#modelversionstatus)
  - [RuleExecutionMode](#ruleexecutionmode)
  - [TrainingDataSourceEnum](#trainingdatasourceenum)

## AsyncJobStatus

```python
from mypy_boto3_frauddetector.literals import AsyncJobStatus
```

Values:

- `CANCEL_IN_PROGRESS`
- `CANCELED`
- `COMPLETE`
- `FAILED`
- `IN_PROGRESS`
- `IN_PROGRESS_INITIALIZING`

## DataSource

```python
from mypy_boto3_frauddetector.literals import DataSource
```

Values:

- `EVENT`
- `EXTERNAL_MODEL_SCORE`
- `MODEL_SCORE`

## DataType

```python
from mypy_boto3_frauddetector.literals import DataType
```

Values:

- `BOOLEAN`
- `FLOAT`
- `INTEGER`
- `STRING`

## DetectorVersionStatus

```python
from mypy_boto3_frauddetector.literals import DetectorVersionStatus
```

Values:

- `ACTIVE`
- `DRAFT`
- `INACTIVE`

## Language

```python
from mypy_boto3_frauddetector.literals import Language
```

Values:

- `DETECTORPL`

## ModelEndpointStatus

```python
from mypy_boto3_frauddetector.literals import ModelEndpointStatus
```

Values:

- `ASSOCIATED`
- `DISSOCIATED`

## ModelInputDataFormat

```python
from mypy_boto3_frauddetector.literals import ModelInputDataFormat
```

Values:

- `APPLICATION_JSON`
- `TEXT_CSV`

## ModelOutputDataFormat

```python
from mypy_boto3_frauddetector.literals import ModelOutputDataFormat
```

Values:

- `APPLICATION_JSONLINES`
- `TEXT_CSV`

## ModelSource

```python
from mypy_boto3_frauddetector.literals import ModelSource
```

Values:

- `SAGEMAKER`

## ModelTypeEnum

```python
from mypy_boto3_frauddetector.literals import ModelTypeEnum
```

Values:

- `ONLINE_FRAUD_INSIGHTS`

## ModelVersionStatus

```python
from mypy_boto3_frauddetector.literals import ModelVersionStatus
```

Values:

- `ACTIVE`
- `INACTIVE`
- `TRAINING_CANCELLED`

## RuleExecutionMode

```python
from mypy_boto3_frauddetector.literals import RuleExecutionMode
```

Values:

- `ALL_MATCHED`
- `FIRST_MATCHED`

## TrainingDataSourceEnum

```python
from mypy_boto3_frauddetector.literals import TrainingDataSourceEnum
```

Values:

- `EXTERNAL_EVENTS`
