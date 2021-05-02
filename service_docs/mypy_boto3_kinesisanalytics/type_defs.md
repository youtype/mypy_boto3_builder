# Structures for boto3 KinesisAnalytics module

> [Index](../index.md) > [KinesisAnalytics](./index.md) > Structures

Auto-generated documentation for [KinesisAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics)
type annotations stubs module [mypy_boto3_kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics/).

- [Structures for boto3 KinesisAnalytics module](#structures-for-boto3-kinesisanalytics-module)
  - [ApplicationDetailTypeDef](#applicationdetailtypedef)
  - [ApplicationSummaryTypeDef](#applicationsummarytypedef)
  - [CSVMappingParametersTypeDef](#csvmappingparameterstypedef)
  - [CloudWatchLoggingOptionDescriptionTypeDef](#cloudwatchloggingoptiondescriptiontypedef)
  - [CloudWatchLoggingOptionUpdateTypeDef](#cloudwatchloggingoptionupdatetypedef)
  - [DestinationSchemaTypeDef](#destinationschematypedef)
  - [InputDescriptionTypeDef](#inputdescriptiontypedef)
  - [InputLambdaProcessorDescriptionTypeDef](#inputlambdaprocessordescriptiontypedef)
  - [InputLambdaProcessorTypeDef](#inputlambdaprocessortypedef)
  - [InputLambdaProcessorUpdateTypeDef](#inputlambdaprocessorupdatetypedef)
  - [InputParallelismTypeDef](#inputparallelismtypedef)
  - [InputParallelismUpdateTypeDef](#inputparallelismupdatetypedef)
  - [InputProcessingConfigurationDescriptionTypeDef](#inputprocessingconfigurationdescriptiontypedef)
  - [InputProcessingConfigurationTypeDef](#inputprocessingconfigurationtypedef)
  - [InputProcessingConfigurationUpdateTypeDef](#inputprocessingconfigurationupdatetypedef)
  - [InputSchemaUpdateTypeDef](#inputschemaupdatetypedef)
  - [InputStartingPositionConfigurationTypeDef](#inputstartingpositionconfigurationtypedef)
  - [InputUpdateTypeDef](#inputupdatetypedef)
  - [JSONMappingParametersTypeDef](#jsonmappingparameterstypedef)
  - [KinesisFirehoseInputDescriptionTypeDef](#kinesisfirehoseinputdescriptiontypedef)
  - [KinesisFirehoseInputTypeDef](#kinesisfirehoseinputtypedef)
  - [KinesisFirehoseInputUpdateTypeDef](#kinesisfirehoseinputupdatetypedef)
  - [KinesisFirehoseOutputDescriptionTypeDef](#kinesisfirehoseoutputdescriptiontypedef)
  - [KinesisFirehoseOutputTypeDef](#kinesisfirehoseoutputtypedef)
  - [KinesisFirehoseOutputUpdateTypeDef](#kinesisfirehoseoutputupdatetypedef)
  - [KinesisStreamsInputDescriptionTypeDef](#kinesisstreamsinputdescriptiontypedef)
  - [KinesisStreamsInputTypeDef](#kinesisstreamsinputtypedef)
  - [KinesisStreamsInputUpdateTypeDef](#kinesisstreamsinputupdatetypedef)
  - [KinesisStreamsOutputDescriptionTypeDef](#kinesisstreamsoutputdescriptiontypedef)
  - [KinesisStreamsOutputTypeDef](#kinesisstreamsoutputtypedef)
  - [KinesisStreamsOutputUpdateTypeDef](#kinesisstreamsoutputupdatetypedef)
  - [LambdaOutputDescriptionTypeDef](#lambdaoutputdescriptiontypedef)
  - [LambdaOutputTypeDef](#lambdaoutputtypedef)
  - [LambdaOutputUpdateTypeDef](#lambdaoutputupdatetypedef)
  - [MappingParametersTypeDef](#mappingparameterstypedef)
  - [OutputDescriptionTypeDef](#outputdescriptiontypedef)
  - [OutputUpdateTypeDef](#outputupdatetypedef)
  - [RecordColumnTypeDef](#recordcolumntypedef)
  - [RecordFormatTypeDef](#recordformattypedef)
  - [ReferenceDataSourceDescriptionTypeDef](#referencedatasourcedescriptiontypedef)
  - [ReferenceDataSourceUpdateTypeDef](#referencedatasourceupdatetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3ReferenceDataSourceDescriptionTypeDef](#s3referencedatasourcedescriptiontypedef)
  - [S3ReferenceDataSourceTypeDef](#s3referencedatasourcetypedef)
  - [S3ReferenceDataSourceUpdateTypeDef](#s3referencedatasourceupdatetypedef)
  - [SourceSchemaTypeDef](#sourceschematypedef)
  - [TagTypeDef](#tagtypedef)
  - [ApplicationUpdateTypeDef](#applicationupdatetypedef)
  - [CloudWatchLoggingOptionTypeDef](#cloudwatchloggingoptiontypedef)
  - [CreateApplicationResponseTypeDef](#createapplicationresponsetypedef)
  - [DescribeApplicationResponseTypeDef](#describeapplicationresponsetypedef)
  - [DiscoverInputSchemaResponseTypeDef](#discoverinputschemaresponsetypedef)
  - [InputConfigurationTypeDef](#inputconfigurationtypedef)
  - [InputTypeDef](#inputtypedef)
  - [ListApplicationsResponseTypeDef](#listapplicationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [OutputTypeDef](#outputtypedef)
  - [ReferenceDataSourceTypeDef](#referencedatasourcetypedef)
  - [S3ConfigurationTypeDef](#s3configurationtypedef)

## ApplicationDetailTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ApplicationDetailTypeDef
```


Required fields:
- `ApplicationName`: `str`
- `ApplicationARN`: `str`
- `ApplicationStatus`: `ApplicationStatus`
- `ApplicationVersionId`: `int`



Optional fields:
- `ApplicationDescription`: `str`
- `CreateTimestamp`: `datetime`
- `LastUpdateTimestamp`: `datetime`
- `InputDescriptions`: `List["InputDescriptionTypeDef"]`
- `OutputDescriptions`: `List["OutputDescriptionTypeDef"]`
- `ReferenceDataSourceDescriptions`: `List["ReferenceDataSourceDescriptionTypeDef"]`
- `CloudWatchLoggingOptionDescriptions`: `List["CloudWatchLoggingOptionDescriptionTypeDef"]`
- `ApplicationCode`: `str`


## ApplicationSummaryTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ApplicationSummaryTypeDef
```


Required fields:
- `ApplicationName`: `str`
- `ApplicationARN`: `str`
- `ApplicationStatus`: `ApplicationStatus`




## CSVMappingParametersTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import CSVMappingParametersTypeDef
```


Required fields:
- `RecordRowDelimiter`: `str`
- `RecordColumnDelimiter`: `str`




## CloudWatchLoggingOptionDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import CloudWatchLoggingOptionDescriptionTypeDef
```


Required fields:
- `LogStreamARN`: `str`
- `RoleARN`: `str`



Optional fields:
- `CloudWatchLoggingOptionId`: `str`


## CloudWatchLoggingOptionUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import CloudWatchLoggingOptionUpdateTypeDef
```


Required fields:
- `CloudWatchLoggingOptionId`: `str`



Optional fields:
- `LogStreamARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## DestinationSchemaTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import DestinationSchemaTypeDef
```


Required fields:
- `RecordFormatType`: `RecordFormatType`




## InputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputDescriptionTypeDef
```




Optional fields:
- `InputId`: `str`
- `NamePrefix`: `str`
- `InAppStreamNames`: `List[str]`
- `InputProcessingConfigurationDescription`: `"InputProcessingConfigurationDescriptionTypeDef"`
- `KinesisStreamsInputDescription`: `"KinesisStreamsInputDescriptionTypeDef"`
- `KinesisFirehoseInputDescription`: `"KinesisFirehoseInputDescriptionTypeDef"`
- `InputSchema`: `"SourceSchemaTypeDef"`
- `InputParallelism`: `"InputParallelismTypeDef"`
- `InputStartingPositionConfiguration`: `"InputStartingPositionConfigurationTypeDef"`


## InputLambdaProcessorDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputLambdaProcessorDescriptionTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`


## InputLambdaProcessorTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputLambdaProcessorTypeDef
```


Required fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`




## InputLambdaProcessorUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputLambdaProcessorUpdateTypeDef
```




Optional fields:
- `ResourceARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## InputParallelismTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputParallelismTypeDef
```




Optional fields:
- `Count`: `int`


## InputParallelismUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputParallelismUpdateTypeDef
```




Optional fields:
- `CountUpdate`: `int`


## InputProcessingConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputProcessingConfigurationDescriptionTypeDef
```




Optional fields:
- `InputLambdaProcessorDescription`: `"InputLambdaProcessorDescriptionTypeDef"`


## InputProcessingConfigurationTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputProcessingConfigurationTypeDef
```


Required fields:
- `InputLambdaProcessor`: `"InputLambdaProcessorTypeDef"`




## InputProcessingConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputProcessingConfigurationUpdateTypeDef
```


Required fields:
- `InputLambdaProcessorUpdate`: `"InputLambdaProcessorUpdateTypeDef"`




## InputSchemaUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputSchemaUpdateTypeDef
```




Optional fields:
- `RecordFormatUpdate`: `"RecordFormatTypeDef"`
- `RecordEncodingUpdate`: `str`
- `RecordColumnUpdates`: `List["RecordColumnTypeDef"]`


## InputStartingPositionConfigurationTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputStartingPositionConfigurationTypeDef
```




Optional fields:
- `InputStartingPosition`: `InputStartingPosition`


## InputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputUpdateTypeDef
```


Required fields:
- `InputId`: `str`



Optional fields:
- `NamePrefixUpdate`: `str`
- `InputProcessingConfigurationUpdate`: `"InputProcessingConfigurationUpdateTypeDef"`
- `KinesisStreamsInputUpdate`: `"KinesisStreamsInputUpdateTypeDef"`
- `KinesisFirehoseInputUpdate`: `"KinesisFirehoseInputUpdateTypeDef"`
- `InputSchemaUpdate`: `"InputSchemaUpdateTypeDef"`
- `InputParallelismUpdate`: `"InputParallelismUpdateTypeDef"`


## JSONMappingParametersTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import JSONMappingParametersTypeDef
```


Required fields:
- `RecordRowPath`: `str`




## KinesisFirehoseInputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisFirehoseInputDescriptionTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`


## KinesisFirehoseInputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisFirehoseInputTypeDef
```


Required fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`




## KinesisFirehoseInputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisFirehoseInputUpdateTypeDef
```




Optional fields:
- `ResourceARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## KinesisFirehoseOutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisFirehoseOutputDescriptionTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`


## KinesisFirehoseOutputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisFirehoseOutputTypeDef
```


Required fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## KinesisFirehoseOutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisFirehoseOutputUpdateTypeDef
```




Optional fields:
- `ResourceARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## KinesisStreamsInputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisStreamsInputDescriptionTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`


## KinesisStreamsInputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisStreamsInputTypeDef
```


Required fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`




## KinesisStreamsInputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisStreamsInputUpdateTypeDef
```




Optional fields:
- `ResourceARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## KinesisStreamsOutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisStreamsOutputDescriptionTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`


## KinesisStreamsOutputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisStreamsOutputTypeDef
```


Required fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## KinesisStreamsOutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import KinesisStreamsOutputUpdateTypeDef
```




Optional fields:
- `ResourceARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## LambdaOutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import LambdaOutputDescriptionTypeDef
```




Optional fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`


## LambdaOutputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import LambdaOutputTypeDef
```


Required fields:
- `ResourceARN`: `str`
- `RoleARN`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## LambdaOutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import LambdaOutputUpdateTypeDef
```




Optional fields:
- `ResourceARNUpdate`: `str`
- `RoleARNUpdate`: `str`


## MappingParametersTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import MappingParametersTypeDef
```




Optional fields:
- `JSONMappingParameters`: `"JSONMappingParametersTypeDef"`
- `CSVMappingParameters`: `"CSVMappingParametersTypeDef"`


## OutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import OutputDescriptionTypeDef
```




Optional fields:
- `OutputId`: `str`
- `Name`: `str`
- `KinesisStreamsOutputDescription`: `"KinesisStreamsOutputDescriptionTypeDef"`
- `KinesisFirehoseOutputDescription`: `"KinesisFirehoseOutputDescriptionTypeDef"`
- `LambdaOutputDescription`: `"LambdaOutputDescriptionTypeDef"`
- `DestinationSchema`: `"DestinationSchemaTypeDef"`


## OutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import OutputUpdateTypeDef
```


Required fields:
- `OutputId`: `str`



Optional fields:
- `NameUpdate`: `str`
- `KinesisStreamsOutputUpdate`: `"KinesisStreamsOutputUpdateTypeDef"`
- `KinesisFirehoseOutputUpdate`: `"KinesisFirehoseOutputUpdateTypeDef"`
- `LambdaOutputUpdate`: `"LambdaOutputUpdateTypeDef"`
- `DestinationSchemaUpdate`: `"DestinationSchemaTypeDef"`


## RecordColumnTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import RecordColumnTypeDef
```


Required fields:
- `Name`: `str`
- `SqlType`: `str`



Optional fields:
- `Mapping`: `str`


## RecordFormatTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import RecordFormatTypeDef
```


Required fields:
- `RecordFormatType`: `RecordFormatType`



Optional fields:
- `MappingParameters`: `"MappingParametersTypeDef"`


## ReferenceDataSourceDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ReferenceDataSourceDescriptionTypeDef
```


Required fields:
- `ReferenceId`: `str`
- `TableName`: `str`
- `S3ReferenceDataSourceDescription`: `"S3ReferenceDataSourceDescriptionTypeDef"`



Optional fields:
- `ReferenceSchema`: `"SourceSchemaTypeDef"`


## ReferenceDataSourceUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ReferenceDataSourceUpdateTypeDef
```


Required fields:
- `ReferenceId`: `str`



Optional fields:
- `TableNameUpdate`: `str`
- `S3ReferenceDataSourceUpdate`: `"S3ReferenceDataSourceUpdateTypeDef"`
- `ReferenceSchemaUpdate`: `"SourceSchemaTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_kinesisanalytics.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3ReferenceDataSourceDescriptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import S3ReferenceDataSourceDescriptionTypeDef
```


Required fields:
- `BucketARN`: `str`
- `FileKey`: `str`
- `ReferenceRoleARN`: `str`




## S3ReferenceDataSourceTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import S3ReferenceDataSourceTypeDef
```


Required fields:
- `BucketARN`: `str`
- `FileKey`: `str`
- `ReferenceRoleARN`: `str`




## S3ReferenceDataSourceUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import S3ReferenceDataSourceUpdateTypeDef
```




Optional fields:
- `BucketARNUpdate`: `str`
- `FileKeyUpdate`: `str`
- `ReferenceRoleARNUpdate`: `str`


## SourceSchemaTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import SourceSchemaTypeDef
```


Required fields:
- `RecordFormat`: `"RecordFormatTypeDef"`
- `RecordColumns`: `List["RecordColumnTypeDef"]`



Optional fields:
- `RecordEncoding`: `str`


## TagTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## ApplicationUpdateTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ApplicationUpdateTypeDef
```




Optional fields:
- `InputUpdates`: `List["InputUpdateTypeDef"]`
- `ApplicationCodeUpdate`: `str`
- `OutputUpdates`: `List["OutputUpdateTypeDef"]`
- `ReferenceDataSourceUpdates`: `List["ReferenceDataSourceUpdateTypeDef"]`
- `CloudWatchLoggingOptionUpdates`: `List["CloudWatchLoggingOptionUpdateTypeDef"]`


## CloudWatchLoggingOptionTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import CloudWatchLoggingOptionTypeDef
```


Required fields:
- `LogStreamARN`: `str`
- `RoleARN`: `str`




## CreateApplicationResponseTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import CreateApplicationResponseTypeDef
```


Required fields:
- `ApplicationSummary`: `"ApplicationSummaryTypeDef"`




## DescribeApplicationResponseTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import DescribeApplicationResponseTypeDef
```


Required fields:
- `ApplicationDetail`: `"ApplicationDetailTypeDef"`




## DiscoverInputSchemaResponseTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import DiscoverInputSchemaResponseTypeDef
```




Optional fields:
- `InputSchema`: `"SourceSchemaTypeDef"`
- `ParsedInputRecords`: `List[List[str]]`
- `ProcessedInputRecords`: `List[str]`
- `RawInputRecords`: `List[str]`


## InputConfigurationTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputConfigurationTypeDef
```


Required fields:
- `Id`: `str`
- `InputStartingPositionConfiguration`: `"InputStartingPositionConfigurationTypeDef"`




## InputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import InputTypeDef
```


Required fields:
- `NamePrefix`: `str`
- `InputSchema`: `"SourceSchemaTypeDef"`



Optional fields:
- `InputProcessingConfiguration`: `"InputProcessingConfigurationTypeDef"`
- `KinesisStreamsInput`: `"KinesisStreamsInputTypeDef"`
- `KinesisFirehoseInput`: `"KinesisFirehoseInputTypeDef"`
- `InputParallelism`: `"InputParallelismTypeDef"`


## ListApplicationsResponseTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ListApplicationsResponseTypeDef
```


Required fields:
- `ApplicationSummaries`: `List["ApplicationSummaryTypeDef"]`
- `HasMoreApplications`: `bool`




## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## OutputTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import OutputTypeDef
```


Required fields:
- `Name`: `str`
- `DestinationSchema`: `"DestinationSchemaTypeDef"`



Optional fields:
- `KinesisStreamsOutput`: `"KinesisStreamsOutputTypeDef"`
- `KinesisFirehoseOutput`: `"KinesisFirehoseOutputTypeDef"`
- `LambdaOutput`: `"LambdaOutputTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ReferenceDataSourceTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import ReferenceDataSourceTypeDef
```


Required fields:
- `TableName`: `str`
- `ReferenceSchema`: `"SourceSchemaTypeDef"`



Optional fields:
- `S3ReferenceDataSource`: `"S3ReferenceDataSourceTypeDef"`


## S3ConfigurationTypeDef

```python
from mypy_boto3_kinesisanalytics.type_defs import S3ConfigurationTypeDef
```


Required fields:
- `RoleARN`: `str`
- `BucketARN`: `str`
- `FileKey`: `str`



