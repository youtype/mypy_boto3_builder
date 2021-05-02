# Structures for boto3 LookoutEquipment module

> [Index](../index.md) > [LookoutEquipment](./index.md) > Structures

Auto-generated documentation for [LookoutEquipment](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment)
type annotations stubs module [mypy_boto3_lookoutequipment](https://pypi.org/project/mypy-boto3-lookoutequipment/).

- [Structures for boto3 LookoutEquipment module](#structures-for-boto3-lookoutequipment-module)
  - [CreateDatasetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateInferenceSchedulerResponseTypeDef](#createinferenceschedulerresponsetypedef)
  - [CreateModelResponseTypeDef](#createmodelresponsetypedef)
  - [DataIngestionJobSummaryTypeDef](#dataingestionjobsummarytypedef)
  - [DataPreProcessingConfigurationTypeDef](#datapreprocessingconfigurationtypedef)
  - [DatasetSchemaTypeDef](#datasetschematypedef)
  - [DatasetSummaryTypeDef](#datasetsummarytypedef)
  - [DescribeDataIngestionJobResponseTypeDef](#describedataingestionjobresponsetypedef)
  - [DescribeDatasetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeInferenceSchedulerResponseTypeDef](#describeinferenceschedulerresponsetypedef)
  - [DescribeModelResponseTypeDef](#describemodelresponsetypedef)
  - [InferenceExecutionSummaryTypeDef](#inferenceexecutionsummarytypedef)
  - [InferenceInputConfigurationTypeDef](#inferenceinputconfigurationtypedef)
  - [InferenceInputNameConfigurationTypeDef](#inferenceinputnameconfigurationtypedef)
  - [InferenceOutputConfigurationTypeDef](#inferenceoutputconfigurationtypedef)
  - [InferenceS3InputConfigurationTypeDef](#inferences3inputconfigurationtypedef)
  - [InferenceS3OutputConfigurationTypeDef](#inferences3outputconfigurationtypedef)
  - [InferenceSchedulerSummaryTypeDef](#inferenceschedulersummarytypedef)
  - [IngestionInputConfigurationTypeDef](#ingestioninputconfigurationtypedef)
  - [IngestionS3InputConfigurationTypeDef](#ingestions3inputconfigurationtypedef)
  - [LabelsInputConfigurationTypeDef](#labelsinputconfigurationtypedef)
  - [LabelsS3InputConfigurationTypeDef](#labelss3inputconfigurationtypedef)
  - [ListDataIngestionJobsResponseTypeDef](#listdataingestionjobsresponsetypedef)
  - [ListDatasetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListInferenceExecutionsResponseTypeDef](#listinferenceexecutionsresponsetypedef)
  - [ListInferenceSchedulersResponseTypeDef](#listinferenceschedulersresponsetypedef)
  - [ListModelsResponseTypeDef](#listmodelsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ModelSummaryTypeDef](#modelsummarytypedef)
  - [S3ObjectTypeDef](#s3objecttypedef)
  - [StartDataIngestionJobResponseTypeDef](#startdataingestionjobresponsetypedef)
  - [StartInferenceSchedulerResponseTypeDef](#startinferenceschedulerresponsetypedef)
  - [StopInferenceSchedulerResponseTypeDef](#stopinferenceschedulerresponsetypedef)
  - [TagTypeDef](#tagtypedef)

## CreateDatasetResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import CreateDatasetResponseTypeDef
```




Optional fields:
- `DatasetName`: `str`
- `DatasetArn`: `str`
- `Status`: `DatasetStatus`


## CreateInferenceSchedulerResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import CreateInferenceSchedulerResponseTypeDef
```




Optional fields:
- `InferenceSchedulerArn`: `str`
- `InferenceSchedulerName`: `str`
- `Status`: `InferenceSchedulerStatus`


## CreateModelResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import CreateModelResponseTypeDef
```




Optional fields:
- `ModelArn`: `str`
- `Status`: `ModelStatus`


## DataIngestionJobSummaryTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DataIngestionJobSummaryTypeDef
```




Optional fields:
- `JobId`: `str`
- `DatasetName`: `str`
- `DatasetArn`: `str`
- `IngestionInputConfiguration`: `"IngestionInputConfigurationTypeDef"`
- `Status`: `IngestionJobStatus`


## DataPreProcessingConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DataPreProcessingConfigurationTypeDef
```




Optional fields:
- `TargetSamplingRate`: `TargetSamplingRate`


## DatasetSchemaTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DatasetSchemaTypeDef
```




Optional fields:
- `InlineDataSchema`: `str`


## DatasetSummaryTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DatasetSummaryTypeDef
```




Optional fields:
- `DatasetName`: `str`
- `DatasetArn`: `str`
- `Status`: `DatasetStatus`
- `CreatedAt`: `datetime`


## DescribeDataIngestionJobResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DescribeDataIngestionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `DatasetArn`: `str`
- `IngestionInputConfiguration`: `"IngestionInputConfigurationTypeDef"`
- `RoleArn`: `str`
- `CreatedAt`: `datetime`
- `Status`: `IngestionJobStatus`
- `FailedReason`: `str`


## DescribeDatasetResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DescribeDatasetResponseTypeDef
```




Optional fields:
- `DatasetName`: `str`
- `DatasetArn`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Status`: `DatasetStatus`
- `Schema`: `str`
- `ServerSideKmsKeyId`: `str`
- `IngestionInputConfiguration`: `"IngestionInputConfigurationTypeDef"`


## DescribeInferenceSchedulerResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DescribeInferenceSchedulerResponseTypeDef
```




Optional fields:
- `ModelArn`: `str`
- `ModelName`: `str`
- `InferenceSchedulerName`: `str`
- `InferenceSchedulerArn`: `str`
- `Status`: `InferenceSchedulerStatus`
- `DataDelayOffsetInMinutes`: `int`
- `DataUploadFrequency`: `DataUploadFrequency`
- `CreatedAt`: `datetime`
- `UpdatedAt`: `datetime`
- `DataInputConfiguration`: `"InferenceInputConfigurationTypeDef"`
- `DataOutputConfiguration`: `"InferenceOutputConfigurationTypeDef"`
- `RoleArn`: `str`
- `ServerSideKmsKeyId`: `str`


## DescribeModelResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import DescribeModelResponseTypeDef
```




Optional fields:
- `ModelName`: `str`
- `ModelArn`: `str`
- `DatasetName`: `str`
- `DatasetArn`: `str`
- `Schema`: `str`
- `LabelsInputConfiguration`: `"LabelsInputConfigurationTypeDef"`
- `TrainingDataStartTime`: `datetime`
- `TrainingDataEndTime`: `datetime`
- `EvaluationDataStartTime`: `datetime`
- `EvaluationDataEndTime`: `datetime`
- `RoleArn`: `str`
- `DataPreProcessingConfiguration`: `"DataPreProcessingConfigurationTypeDef"`
- `Status`: `ModelStatus`
- `TrainingExecutionStartTime`: `datetime`
- `TrainingExecutionEndTime`: `datetime`
- `FailedReason`: `str`
- `ModelMetrics`: `str`
- `LastUpdatedTime`: `datetime`
- `CreatedAt`: `datetime`
- `ServerSideKmsKeyId`: `str`


## InferenceExecutionSummaryTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceExecutionSummaryTypeDef
```




Optional fields:
- `ModelName`: `str`
- `ModelArn`: `str`
- `InferenceSchedulerName`: `str`
- `InferenceSchedulerArn`: `str`
- `ScheduledStartTime`: `datetime`
- `DataStartTime`: `datetime`
- `DataEndTime`: `datetime`
- `DataInputConfiguration`: `"InferenceInputConfigurationTypeDef"`
- `DataOutputConfiguration`: `"InferenceOutputConfigurationTypeDef"`
- `CustomerResultObject`: `"S3ObjectTypeDef"`
- `Status`: `InferenceExecutionStatus`
- `FailedReason`: `str`


## InferenceInputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceInputConfigurationTypeDef
```




Optional fields:
- `S3InputConfiguration`: `"InferenceS3InputConfigurationTypeDef"`
- `InputTimeZoneOffset`: `str`
- `InferenceInputNameConfiguration`: `"InferenceInputNameConfigurationTypeDef"`


## InferenceInputNameConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceInputNameConfigurationTypeDef
```




Optional fields:
- `TimestampFormat`: `str`
- `ComponentTimestampDelimiter`: `str`


## InferenceOutputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceOutputConfigurationTypeDef
```


Required fields:
- `S3OutputConfiguration`: `"InferenceS3OutputConfigurationTypeDef"`



Optional fields:
- `KmsKeyId`: `str`


## InferenceS3InputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceS3InputConfigurationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Prefix`: `str`


## InferenceS3OutputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceS3OutputConfigurationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Prefix`: `str`


## InferenceSchedulerSummaryTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import InferenceSchedulerSummaryTypeDef
```




Optional fields:
- `ModelName`: `str`
- `ModelArn`: `str`
- `InferenceSchedulerName`: `str`
- `InferenceSchedulerArn`: `str`
- `Status`: `InferenceSchedulerStatus`
- `DataDelayOffsetInMinutes`: `int`
- `DataUploadFrequency`: `DataUploadFrequency`


## IngestionInputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import IngestionInputConfigurationTypeDef
```


Required fields:
- `S3InputConfiguration`: `"IngestionS3InputConfigurationTypeDef"`




## IngestionS3InputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import IngestionS3InputConfigurationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Prefix`: `str`


## LabelsInputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import LabelsInputConfigurationTypeDef
```


Required fields:
- `S3InputConfiguration`: `"LabelsS3InputConfigurationTypeDef"`




## LabelsS3InputConfigurationTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import LabelsS3InputConfigurationTypeDef
```


Required fields:
- `Bucket`: `str`



Optional fields:
- `Prefix`: `str`


## ListDataIngestionJobsResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ListDataIngestionJobsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `DataIngestionJobSummaries`: `List["DataIngestionJobSummaryTypeDef"]`


## ListDatasetsResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ListDatasetsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `DatasetSummaries`: `List["DatasetSummaryTypeDef"]`


## ListInferenceExecutionsResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ListInferenceExecutionsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `InferenceExecutionSummaries`: `List["InferenceExecutionSummaryTypeDef"]`


## ListInferenceSchedulersResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ListInferenceSchedulersResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `InferenceSchedulerSummaries`: `List["InferenceSchedulerSummaryTypeDef"]`


## ListModelsResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ListModelsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `ModelSummaries`: `List["ModelSummaryTypeDef"]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ModelSummaryTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import ModelSummaryTypeDef
```




Optional fields:
- `ModelName`: `str`
- `ModelArn`: `str`
- `DatasetName`: `str`
- `DatasetArn`: `str`
- `Status`: `ModelStatus`
- `CreatedAt`: `datetime`


## S3ObjectTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import S3ObjectTypeDef
```


Required fields:
- `Bucket`: `str`
- `Key`: `str`




## StartDataIngestionJobResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import StartDataIngestionJobResponseTypeDef
```




Optional fields:
- `JobId`: `str`
- `Status`: `IngestionJobStatus`


## StartInferenceSchedulerResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import StartInferenceSchedulerResponseTypeDef
```




Optional fields:
- `ModelArn`: `str`
- `ModelName`: `str`
- `InferenceSchedulerName`: `str`
- `InferenceSchedulerArn`: `str`
- `Status`: `InferenceSchedulerStatus`


## StopInferenceSchedulerResponseTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import StopInferenceSchedulerResponseTypeDef
```




Optional fields:
- `ModelArn`: `str`
- `ModelName`: `str`
- `InferenceSchedulerName`: `str`
- `InferenceSchedulerArn`: `str`
- `Status`: `InferenceSchedulerStatus`


## TagTypeDef

```python
from mypy_boto3_lookoutequipment.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`



