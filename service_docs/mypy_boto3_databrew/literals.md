# Literals for boto3 GlueDataBrew module

> [Index](../index.md) > [GlueDataBrew](./index.md) > Literals

Auto-generated documentation for [GlueDataBrew](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew)
type annotations stubs module [mypy_boto3_databrew](https://pypi.org/project/mypy-boto3-databrew/).

- [Literals for boto3 GlueDataBrew module](#literals-for-boto3-gluedatabrew-module)
  - [CompressionFormat](#compressionformat)
  - [EncryptionMode](#encryptionmode)
  - [InputFormat](#inputformat)
  - [JobRunState](#jobrunstate)
  - [JobType](#jobtype)
  - [ListDatasetsPaginatorName](#listdatasetspaginatorname)
  - [ListJobRunsPaginatorName](#listjobrunspaginatorname)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [ListProjectsPaginatorName](#listprojectspaginatorname)
  - [ListRecipeVersionsPaginatorName](#listrecipeversionspaginatorname)
  - [ListRecipesPaginatorName](#listrecipespaginatorname)
  - [ListSchedulesPaginatorName](#listschedulespaginatorname)
  - [LogSubscription](#logsubscription)
  - [Order](#order)
  - [OrderedBy](#orderedby)
  - [OutputFormat](#outputformat)
  - [ParameterType](#parametertype)
  - [SampleMode](#samplemode)
  - [SampleType](#sampletype)
  - [SessionStatus](#sessionstatus)
  - [Source](#source)

## CompressionFormat

```python
from mypy_boto3_databrew.literals import CompressionFormat
```

Values:

- `BROTLI`
- `BZIP2`
- `DEFLATE`
- `GZIP`
- `LZ4`
- `LZO`
- `SNAPPY`
- `ZLIB`
- `ZSTD`

## EncryptionMode

```python
from mypy_boto3_databrew.literals import EncryptionMode
```

Values:

- `SSE-KMS`
- `SSE-S3`

## InputFormat

```python
from mypy_boto3_databrew.literals import InputFormat
```

Values:

- `CSV`
- `EXCEL`
- `JSON`
- `PARQUET`

## JobRunState

```python
from mypy_boto3_databrew.literals import JobRunState
```

Values:

- `FAILED`
- `RUNNING`
- `STARTING`
- `STOPPED`
- `STOPPING`
- `SUCCEEDED`
- `TIMEOUT`

## JobType

```python
from mypy_boto3_databrew.literals import JobType
```

Values:

- `PROFILE`
- `RECIPE`

## ListDatasetsPaginatorName

```python
from mypy_boto3_databrew.literals import ListDatasetsPaginatorName
```

Values:

- `list_datasets`

## ListJobRunsPaginatorName

```python
from mypy_boto3_databrew.literals import ListJobRunsPaginatorName
```

Values:

- `list_job_runs`

## ListJobsPaginatorName

```python
from mypy_boto3_databrew.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## ListProjectsPaginatorName

```python
from mypy_boto3_databrew.literals import ListProjectsPaginatorName
```

Values:

- `list_projects`

## ListRecipeVersionsPaginatorName

```python
from mypy_boto3_databrew.literals import ListRecipeVersionsPaginatorName
```

Values:

- `list_recipe_versions`

## ListRecipesPaginatorName

```python
from mypy_boto3_databrew.literals import ListRecipesPaginatorName
```

Values:

- `list_recipes`

## ListSchedulesPaginatorName

```python
from mypy_boto3_databrew.literals import ListSchedulesPaginatorName
```

Values:

- `list_schedules`

## LogSubscription

```python
from mypy_boto3_databrew.literals import LogSubscription
```

Values:

- `DISABLE`
- `ENABLE`

## Order

```python
from mypy_boto3_databrew.literals import Order
```

Values:

- `ASCENDING`
- `DESCENDING`

## OrderedBy

```python
from mypy_boto3_databrew.literals import OrderedBy
```

Values:

- `LAST_MODIFIED_DATE`

## OutputFormat

```python
from mypy_boto3_databrew.literals import OutputFormat
```

Values:

- `AVRO`
- `CSV`
- `GLUEPARQUET`
- `JSON`
- `ORC`
- `PARQUET`
- `XML`

## ParameterType

```python
from mypy_boto3_databrew.literals import ParameterType
```

Values:

- `Datetime`
- `Number`
- `String`

## SampleMode

```python
from mypy_boto3_databrew.literals import SampleMode
```

Values:

- `CUSTOM_ROWS`
- `FULL_DATASET`

## SampleType

```python
from mypy_boto3_databrew.literals import SampleType
```

Values:

- `FIRST_N`
- `LAST_N`
- `RANDOM`

## SessionStatus

```python
from mypy_boto3_databrew.literals import SessionStatus
```

Values:

- `ASSIGNED`
- `FAILED`
- `INITIALIZING`
- `PROVISIONING`
- `READY`
- `RECYCLING`
- `ROTATING`
- `TERMINATED`
- `TERMINATING`
- `UPDATING`

## Source

```python
from mypy_boto3_databrew.literals import Source
```

Values:

- `DATA-CATALOG`
- `DATABASE`
- `S3`
