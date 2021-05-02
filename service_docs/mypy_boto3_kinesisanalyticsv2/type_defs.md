# Structures for boto3 KinesisAnalyticsV2 module

> [Index](../index.md) > [KinesisAnalyticsV2](./index.md) > Structures

Auto-generated documentation for [KinesisAnalyticsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2)
type annotations stubs module [mypy_boto3_kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/).

- [Structures for boto3 KinesisAnalyticsV2 module](#structures-for-boto3-kinesisanalyticsv2-module)
  - [AddApplicationCloudWatchLoggingOptionResponseTypeDef](#addapplicationcloudwatchloggingoptionresponsetypedef)
  - [AddApplicationInputProcessingConfigurationResponseTypeDef](#addapplicationinputprocessingconfigurationresponsetypedef)
  - [AddApplicationInputResponseTypeDef](#addapplicationinputresponsetypedef)
  - [AddApplicationOutputResponseTypeDef](#addapplicationoutputresponsetypedef)
  - [AddApplicationReferenceDataSourceResponseTypeDef](#addapplicationreferencedatasourceresponsetypedef)
  - [AddApplicationVpcConfigurationResponseTypeDef](#addapplicationvpcconfigurationresponsetypedef)
  - [ApplicationCodeConfigurationDescriptionTypeDef](#applicationcodeconfigurationdescriptiontypedef)
  - [ApplicationCodeConfigurationTypeDef](#applicationcodeconfigurationtypedef)
  - [ApplicationCodeConfigurationUpdateTypeDef](#applicationcodeconfigurationupdatetypedef)
  - [ApplicationConfigurationDescriptionTypeDef](#applicationconfigurationdescriptiontypedef)
  - [ApplicationConfigurationTypeDef](#applicationconfigurationtypedef)
  - [ApplicationConfigurationUpdateTypeDef](#applicationconfigurationupdatetypedef)
  - [ApplicationDetailTypeDef](#applicationdetailtypedef)
  - [ApplicationMaintenanceConfigurationDescriptionTypeDef](#applicationmaintenanceconfigurationdescriptiontypedef)
  - [ApplicationMaintenanceConfigurationUpdateTypeDef](#applicationmaintenanceconfigurationupdatetypedef)
  - [ApplicationRestoreConfigurationTypeDef](#applicationrestoreconfigurationtypedef)
  - [ApplicationSnapshotConfigurationDescriptionTypeDef](#applicationsnapshotconfigurationdescriptiontypedef)
  - [ApplicationSnapshotConfigurationTypeDef](#applicationsnapshotconfigurationtypedef)
  - [ApplicationSnapshotConfigurationUpdateTypeDef](#applicationsnapshotconfigurationupdatetypedef)
  - [ApplicationSummaryTypeDef](#applicationsummarytypedef)
  - [CSVMappingParametersTypeDef](#csvmappingparameterstypedef)
  - [CheckpointConfigurationDescriptionTypeDef](#checkpointconfigurationdescriptiontypedef)
  - [CheckpointConfigurationTypeDef](#checkpointconfigurationtypedef)
  - [CheckpointConfigurationUpdateTypeDef](#checkpointconfigurationupdatetypedef)
  - [CloudWatchLoggingOptionDescriptionTypeDef](#cloudwatchloggingoptiondescriptiontypedef)
  - [CloudWatchLoggingOptionTypeDef](#cloudwatchloggingoptiontypedef)
  - [CloudWatchLoggingOptionUpdateTypeDef](#cloudwatchloggingoptionupdatetypedef)
  - [CodeContentDescriptionTypeDef](#codecontentdescriptiontypedef)
  - [CodeContentTypeDef](#codecontenttypedef)
  - [CodeContentUpdateTypeDef](#codecontentupdatetypedef)
  - [CreateApplicationPresignedUrlResponseTypeDef](#createapplicationpresignedurlresponsetypedef)
  - [CreateApplicationResponseTypeDef](#createapplicationresponsetypedef)
  - [DeleteApplicationCloudWatchLoggingOptionResponseTypeDef](#deleteapplicationcloudwatchloggingoptionresponsetypedef)
  - [DeleteApplicationInputProcessingConfigurationResponseTypeDef](#deleteapplicationinputprocessingconfigurationresponsetypedef)
  - [DeleteApplicationOutputResponseTypeDef](#deleteapplicationoutputresponsetypedef)
  - [DeleteApplicationReferenceDataSourceResponseTypeDef](#deleteapplicationreferencedatasourceresponsetypedef)
  - [DeleteApplicationVpcConfigurationResponseTypeDef](#deleteapplicationvpcconfigurationresponsetypedef)
  - [DescribeApplicationResponseTypeDef](#describeapplicationresponsetypedef)
  - [DescribeApplicationSnapshotResponseTypeDef](#describeapplicationsnapshotresponsetypedef)
  - [DestinationSchemaTypeDef](#destinationschematypedef)
  - [DiscoverInputSchemaResponseTypeDef](#discoverinputschemaresponsetypedef)
  - [EnvironmentPropertiesTypeDef](#environmentpropertiestypedef)
  - [EnvironmentPropertyDescriptionsTypeDef](#environmentpropertydescriptionstypedef)
  - [EnvironmentPropertyUpdatesTypeDef](#environmentpropertyupdatestypedef)
  - [FlinkApplicationConfigurationDescriptionTypeDef](#flinkapplicationconfigurationdescriptiontypedef)
  - [FlinkApplicationConfigurationTypeDef](#flinkapplicationconfigurationtypedef)
  - [FlinkApplicationConfigurationUpdateTypeDef](#flinkapplicationconfigurationupdatetypedef)
  - [FlinkRunConfigurationTypeDef](#flinkrunconfigurationtypedef)
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
  - [InputTypeDef](#inputtypedef)
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
  - [ListApplicationSnapshotsResponseTypeDef](#listapplicationsnapshotsresponsetypedef)
  - [ListApplicationsResponseTypeDef](#listapplicationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MappingParametersTypeDef](#mappingparameterstypedef)
  - [MonitoringConfigurationDescriptionTypeDef](#monitoringconfigurationdescriptiontypedef)
  - [MonitoringConfigurationTypeDef](#monitoringconfigurationtypedef)
  - [MonitoringConfigurationUpdateTypeDef](#monitoringconfigurationupdatetypedef)
  - [OutputDescriptionTypeDef](#outputdescriptiontypedef)
  - [OutputTypeDef](#outputtypedef)
  - [OutputUpdateTypeDef](#outputupdatetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParallelismConfigurationDescriptionTypeDef](#parallelismconfigurationdescriptiontypedef)
  - [ParallelismConfigurationTypeDef](#parallelismconfigurationtypedef)
  - [ParallelismConfigurationUpdateTypeDef](#parallelismconfigurationupdatetypedef)
  - [PropertyGroupTypeDef](#propertygrouptypedef)
  - [RecordColumnTypeDef](#recordcolumntypedef)
  - [RecordFormatTypeDef](#recordformattypedef)
  - [ReferenceDataSourceDescriptionTypeDef](#referencedatasourcedescriptiontypedef)
  - [ReferenceDataSourceTypeDef](#referencedatasourcetypedef)
  - [ReferenceDataSourceUpdateTypeDef](#referencedatasourceupdatetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RunConfigurationDescriptionTypeDef](#runconfigurationdescriptiontypedef)
  - [RunConfigurationTypeDef](#runconfigurationtypedef)
  - [RunConfigurationUpdateTypeDef](#runconfigurationupdatetypedef)
  - [S3ApplicationCodeLocationDescriptionTypeDef](#s3applicationcodelocationdescriptiontypedef)
  - [S3ConfigurationTypeDef](#s3configurationtypedef)
  - [S3ContentLocationTypeDef](#s3contentlocationtypedef)
  - [S3ContentLocationUpdateTypeDef](#s3contentlocationupdatetypedef)
  - [S3ReferenceDataSourceDescriptionTypeDef](#s3referencedatasourcedescriptiontypedef)
  - [S3ReferenceDataSourceTypeDef](#s3referencedatasourcetypedef)
  - [S3ReferenceDataSourceUpdateTypeDef](#s3referencedatasourceupdatetypedef)
  - [SnapshotDetailsTypeDef](#snapshotdetailstypedef)
  - [SourceSchemaTypeDef](#sourceschematypedef)
  - [SqlApplicationConfigurationDescriptionTypeDef](#sqlapplicationconfigurationdescriptiontypedef)
  - [SqlApplicationConfigurationTypeDef](#sqlapplicationconfigurationtypedef)
  - [SqlApplicationConfigurationUpdateTypeDef](#sqlapplicationconfigurationupdatetypedef)
  - [SqlRunConfigurationTypeDef](#sqlrunconfigurationtypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateApplicationMaintenanceConfigurationResponseTypeDef](#updateapplicationmaintenanceconfigurationresponsetypedef)
  - [UpdateApplicationResponseTypeDef](#updateapplicationresponsetypedef)
  - [VpcConfigurationDescriptionTypeDef](#vpcconfigurationdescriptiontypedef)
  - [VpcConfigurationTypeDef](#vpcconfigurationtypedef)
  - [VpcConfigurationUpdateTypeDef](#vpcconfigurationupdatetypedef)

## AddApplicationCloudWatchLoggingOptionResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationCloudWatchLoggingOptionResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `CloudWatchLoggingOptionDescriptions`: `List["CloudWatchLoggingOptionDescriptionTypeDef"]`


## AddApplicationInputProcessingConfigurationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationInputProcessingConfigurationResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `InputId`: `str`
- `InputProcessingConfigurationDescription`: `"InputProcessingConfigurationDescriptionTypeDef"`


## AddApplicationInputResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationInputResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `InputDescriptions`: `List["InputDescriptionTypeDef"]`


## AddApplicationOutputResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationOutputResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `OutputDescriptions`: `List["OutputDescriptionTypeDef"]`


## AddApplicationReferenceDataSourceResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationReferenceDataSourceResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `ReferenceDataSourceDescriptions`: `List["ReferenceDataSourceDescriptionTypeDef"]`


## AddApplicationVpcConfigurationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationVpcConfigurationResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `VpcConfigurationDescription`: `"VpcConfigurationDescriptionTypeDef"`


## ApplicationCodeConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationCodeConfigurationDescriptionTypeDef
```


Required fields:
- `CodeContentType`: `CodeContentType`



Optional fields:
- `CodeContentDescription`: `"CodeContentDescriptionTypeDef"`


## ApplicationCodeConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationCodeConfigurationTypeDef
```


Required fields:
- `CodeContentType`: `CodeContentType`



Optional fields:
- `CodeContent`: `"CodeContentTypeDef"`


## ApplicationCodeConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationCodeConfigurationUpdateTypeDef
```




Optional fields:
- `CodeContentTypeUpdate`: `CodeContentType`
- `CodeContentUpdate`: `"CodeContentUpdateTypeDef"`


## ApplicationConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationConfigurationDescriptionTypeDef
```




Optional fields:
- `SqlApplicationConfigurationDescription`: `"SqlApplicationConfigurationDescriptionTypeDef"`
- `ApplicationCodeConfigurationDescription`: `"ApplicationCodeConfigurationDescriptionTypeDef"`
- `RunConfigurationDescription`: `"RunConfigurationDescriptionTypeDef"`
- `FlinkApplicationConfigurationDescription`: `"FlinkApplicationConfigurationDescriptionTypeDef"`
- `EnvironmentPropertyDescriptions`: `"EnvironmentPropertyDescriptionsTypeDef"`
- `ApplicationSnapshotConfigurationDescription`: `"ApplicationSnapshotConfigurationDescriptionTypeDef"`
- `VpcConfigurationDescriptions`: `List["VpcConfigurationDescriptionTypeDef"]`


## ApplicationConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationConfigurationTypeDef
```


Required fields:
- `ApplicationCodeConfiguration`: `"ApplicationCodeConfigurationTypeDef"`



Optional fields:
- `SqlApplicationConfiguration`: `"SqlApplicationConfigurationTypeDef"`
- `FlinkApplicationConfiguration`: `"FlinkApplicationConfigurationTypeDef"`
- `EnvironmentProperties`: `"EnvironmentPropertiesTypeDef"`
- `ApplicationSnapshotConfiguration`: `"ApplicationSnapshotConfigurationTypeDef"`
- `VpcConfigurations`: `List["VpcConfigurationTypeDef"]`


## ApplicationConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationConfigurationUpdateTypeDef
```




Optional fields:
- `SqlApplicationConfigurationUpdate`: `"SqlApplicationConfigurationUpdateTypeDef"`
- `ApplicationCodeConfigurationUpdate`: `"ApplicationCodeConfigurationUpdateTypeDef"`
- `FlinkApplicationConfigurationUpdate`: `"FlinkApplicationConfigurationUpdateTypeDef"`
- `EnvironmentPropertyUpdates`: `"EnvironmentPropertyUpdatesTypeDef"`
- `ApplicationSnapshotConfigurationUpdate`: `"ApplicationSnapshotConfigurationUpdateTypeDef"`
- `VpcConfigurationUpdates`: `List["VpcConfigurationUpdateTypeDef"]`


## ApplicationDetailTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationDetailTypeDef
```


Required fields:
- `ApplicationARN`: `str`
- `ApplicationName`: `str`
- `RuntimeEnvironment`: `RuntimeEnvironment`
- `ApplicationStatus`: `ApplicationStatus`
- `ApplicationVersionId`: `int`



Optional fields:
- `ApplicationDescription`: `str`
- `ServiceExecutionRole`: `str`
- `CreateTimestamp`: `datetime`
- `LastUpdateTimestamp`: `datetime`
- `ApplicationConfigurationDescription`: `"ApplicationConfigurationDescriptionTypeDef"`
- `CloudWatchLoggingOptionDescriptions`: `List["CloudWatchLoggingOptionDescriptionTypeDef"]`
- `ApplicationMaintenanceConfigurationDescription`: `"ApplicationMaintenanceConfigurationDescriptionTypeDef"`


## ApplicationMaintenanceConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationMaintenanceConfigurationDescriptionTypeDef
```


Required fields:
- `ApplicationMaintenanceWindowStartTime`: `str`
- `ApplicationMaintenanceWindowEndTime`: `str`




## ApplicationMaintenanceConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationMaintenanceConfigurationUpdateTypeDef
```


Required fields:
- `ApplicationMaintenanceWindowStartTimeUpdate`: `str`




## ApplicationRestoreConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationRestoreConfigurationTypeDef
```


Required fields:
- `ApplicationRestoreType`: `ApplicationRestoreType`



Optional fields:
- `SnapshotName`: `str`


## ApplicationSnapshotConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationSnapshotConfigurationDescriptionTypeDef
```


Required fields:
- `SnapshotsEnabled`: `bool`




## ApplicationSnapshotConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationSnapshotConfigurationTypeDef
```


Required fields:
- `SnapshotsEnabled`: `bool`




## ApplicationSnapshotConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationSnapshotConfigurationUpdateTypeDef
```


Required fields:
- `SnapshotsEnabledUpdate`: `bool`




## ApplicationSummaryTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationSummaryTypeDef
```


Required fields:
- `ApplicationName`: `str`
- `ApplicationARN`: `str`
- `ApplicationStatus`: `ApplicationStatus`
- `ApplicationVersionId`: `int`
- `RuntimeEnvironment`: `RuntimeEnvironment`




## CSVMappingParametersTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CSVMappingParametersTypeDef
```


Required fields:
- `RecordRowDelimiter`: `str`
- `RecordColumnDelimiter`: `str`




## CheckpointConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CheckpointConfigurationDescriptionTypeDef
```




Optional fields:
- `ConfigurationType`: `ConfigurationType`
- `CheckpointingEnabled`: `bool`
- `CheckpointInterval`: `int`
- `MinPauseBetweenCheckpoints`: `int`


## CheckpointConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CheckpointConfigurationTypeDef
```


Required fields:
- `ConfigurationType`: `ConfigurationType`



Optional fields:
- `CheckpointingEnabled`: `bool`
- `CheckpointInterval`: `int`
- `MinPauseBetweenCheckpoints`: `int`


## CheckpointConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CheckpointConfigurationUpdateTypeDef
```




Optional fields:
- `ConfigurationTypeUpdate`: `ConfigurationType`
- `CheckpointingEnabledUpdate`: `bool`
- `CheckpointIntervalUpdate`: `int`
- `MinPauseBetweenCheckpointsUpdate`: `int`


## CloudWatchLoggingOptionDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CloudWatchLoggingOptionDescriptionTypeDef
```


Required fields:
- `LogStreamARN`: `str`



Optional fields:
- `CloudWatchLoggingOptionId`: `str`
- `RoleARN`: `str`


## CloudWatchLoggingOptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CloudWatchLoggingOptionTypeDef
```


Required fields:
- `LogStreamARN`: `str`




## CloudWatchLoggingOptionUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CloudWatchLoggingOptionUpdateTypeDef
```


Required fields:
- `CloudWatchLoggingOptionId`: `str`



Optional fields:
- `LogStreamARNUpdate`: `str`


## CodeContentDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CodeContentDescriptionTypeDef
```




Optional fields:
- `TextContent`: `str`
- `CodeMD5`: `str`
- `CodeSize`: `int`
- `S3ApplicationCodeLocationDescription`: `"S3ApplicationCodeLocationDescriptionTypeDef"`


## CodeContentTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CodeContentTypeDef
```




Optional fields:
- `TextContent`: `str`
- `ZipFileContent`: `Union[bytes, IO[bytes]]`
- `S3ContentLocation`: `"S3ContentLocationTypeDef"`


## CodeContentUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CodeContentUpdateTypeDef
```




Optional fields:
- `TextContentUpdate`: `str`
- `ZipFileContentUpdate`: `Union[bytes, IO[bytes]]`
- `S3ContentLocationUpdate`: `"S3ContentLocationUpdateTypeDef"`


## CreateApplicationPresignedUrlResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CreateApplicationPresignedUrlResponseTypeDef
```




Optional fields:
- `AuthorizedUrl`: `str`


## CreateApplicationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import CreateApplicationResponseTypeDef
```


Required fields:
- `ApplicationDetail`: `"ApplicationDetailTypeDef"`




## DeleteApplicationCloudWatchLoggingOptionResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DeleteApplicationCloudWatchLoggingOptionResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`
- `CloudWatchLoggingOptionDescriptions`: `List["CloudWatchLoggingOptionDescriptionTypeDef"]`


## DeleteApplicationInputProcessingConfigurationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DeleteApplicationInputProcessingConfigurationResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`


## DeleteApplicationOutputResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DeleteApplicationOutputResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`


## DeleteApplicationReferenceDataSourceResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DeleteApplicationReferenceDataSourceResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`


## DeleteApplicationVpcConfigurationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DeleteApplicationVpcConfigurationResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationVersionId`: `int`


## DescribeApplicationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DescribeApplicationResponseTypeDef
```


Required fields:
- `ApplicationDetail`: `"ApplicationDetailTypeDef"`




## DescribeApplicationSnapshotResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DescribeApplicationSnapshotResponseTypeDef
```


Required fields:
- `SnapshotDetails`: `"SnapshotDetailsTypeDef"`




## DestinationSchemaTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DestinationSchemaTypeDef
```


Required fields:
- `RecordFormatType`: `RecordFormatType`




## DiscoverInputSchemaResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import DiscoverInputSchemaResponseTypeDef
```




Optional fields:
- `InputSchema`: `"SourceSchemaTypeDef"`
- `ParsedInputRecords`: `List[List[str]]`
- `ProcessedInputRecords`: `List[str]`
- `RawInputRecords`: `List[str]`


## EnvironmentPropertiesTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import EnvironmentPropertiesTypeDef
```


Required fields:
- `PropertyGroups`: `List["PropertyGroupTypeDef"]`




## EnvironmentPropertyDescriptionsTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import EnvironmentPropertyDescriptionsTypeDef
```




Optional fields:
- `PropertyGroupDescriptions`: `List["PropertyGroupTypeDef"]`


## EnvironmentPropertyUpdatesTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import EnvironmentPropertyUpdatesTypeDef
```


Required fields:
- `PropertyGroups`: `List["PropertyGroupTypeDef"]`




## FlinkApplicationConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import FlinkApplicationConfigurationDescriptionTypeDef
```




Optional fields:
- `CheckpointConfigurationDescription`: `"CheckpointConfigurationDescriptionTypeDef"`
- `MonitoringConfigurationDescription`: `"MonitoringConfigurationDescriptionTypeDef"`
- `ParallelismConfigurationDescription`: `"ParallelismConfigurationDescriptionTypeDef"`
- `JobPlanDescription`: `str`


## FlinkApplicationConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import FlinkApplicationConfigurationTypeDef
```




Optional fields:
- `CheckpointConfiguration`: `"CheckpointConfigurationTypeDef"`
- `MonitoringConfiguration`: `"MonitoringConfigurationTypeDef"`
- `ParallelismConfiguration`: `"ParallelismConfigurationTypeDef"`


## FlinkApplicationConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import FlinkApplicationConfigurationUpdateTypeDef
```




Optional fields:
- `CheckpointConfigurationUpdate`: `"CheckpointConfigurationUpdateTypeDef"`
- `MonitoringConfigurationUpdate`: `"MonitoringConfigurationUpdateTypeDef"`
- `ParallelismConfigurationUpdate`: `"ParallelismConfigurationUpdateTypeDef"`


## FlinkRunConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import FlinkRunConfigurationTypeDef
```




Optional fields:
- `AllowNonRestoredState`: `bool`


## InputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputDescriptionTypeDef
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
from mypy_boto3_kinesisanalyticsv2.type_defs import InputLambdaProcessorDescriptionTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `RoleARN`: `str`


## InputLambdaProcessorTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputLambdaProcessorTypeDef
```


Required fields:
- `ResourceARN`: `str`




## InputLambdaProcessorUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputLambdaProcessorUpdateTypeDef
```


Required fields:
- `ResourceARNUpdate`: `str`




## InputParallelismTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputParallelismTypeDef
```




Optional fields:
- `Count`: `int`


## InputParallelismUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputParallelismUpdateTypeDef
```


Required fields:
- `CountUpdate`: `int`




## InputProcessingConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputProcessingConfigurationDescriptionTypeDef
```




Optional fields:
- `InputLambdaProcessorDescription`: `"InputLambdaProcessorDescriptionTypeDef"`


## InputProcessingConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputProcessingConfigurationTypeDef
```


Required fields:
- `InputLambdaProcessor`: `"InputLambdaProcessorTypeDef"`




## InputProcessingConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputProcessingConfigurationUpdateTypeDef
```


Required fields:
- `InputLambdaProcessorUpdate`: `"InputLambdaProcessorUpdateTypeDef"`




## InputSchemaUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputSchemaUpdateTypeDef
```




Optional fields:
- `RecordFormatUpdate`: `"RecordFormatTypeDef"`
- `RecordEncodingUpdate`: `str`
- `RecordColumnUpdates`: `List["RecordColumnTypeDef"]`


## InputStartingPositionConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputStartingPositionConfigurationTypeDef
```




Optional fields:
- `InputStartingPosition`: `InputStartingPosition`


## InputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputTypeDef
```


Required fields:
- `NamePrefix`: `str`
- `InputSchema`: `"SourceSchemaTypeDef"`



Optional fields:
- `InputProcessingConfiguration`: `"InputProcessingConfigurationTypeDef"`
- `KinesisStreamsInput`: `"KinesisStreamsInputTypeDef"`
- `KinesisFirehoseInput`: `"KinesisFirehoseInputTypeDef"`
- `InputParallelism`: `"InputParallelismTypeDef"`


## InputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import InputUpdateTypeDef
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
from mypy_boto3_kinesisanalyticsv2.type_defs import JSONMappingParametersTypeDef
```


Required fields:
- `RecordRowPath`: `str`




## KinesisFirehoseInputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisFirehoseInputDescriptionTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `RoleARN`: `str`


## KinesisFirehoseInputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisFirehoseInputTypeDef
```


Required fields:
- `ResourceARN`: `str`




## KinesisFirehoseInputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisFirehoseInputUpdateTypeDef
```


Required fields:
- `ResourceARNUpdate`: `str`




## KinesisFirehoseOutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisFirehoseOutputDescriptionTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `RoleARN`: `str`


## KinesisFirehoseOutputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisFirehoseOutputTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## KinesisFirehoseOutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisFirehoseOutputUpdateTypeDef
```


Required fields:
- `ResourceARNUpdate`: `str`




## KinesisStreamsInputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisStreamsInputDescriptionTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `RoleARN`: `str`


## KinesisStreamsInputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisStreamsInputTypeDef
```


Required fields:
- `ResourceARN`: `str`




## KinesisStreamsInputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisStreamsInputUpdateTypeDef
```


Required fields:
- `ResourceARNUpdate`: `str`




## KinesisStreamsOutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisStreamsOutputDescriptionTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `RoleARN`: `str`


## KinesisStreamsOutputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisStreamsOutputTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## KinesisStreamsOutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import KinesisStreamsOutputUpdateTypeDef
```


Required fields:
- `ResourceARNUpdate`: `str`




## LambdaOutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import LambdaOutputDescriptionTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `RoleARN`: `str`


## LambdaOutputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import LambdaOutputTypeDef
```


Required fields:
- `ResourceARN`: `str`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## LambdaOutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import LambdaOutputUpdateTypeDef
```


Required fields:
- `ResourceARNUpdate`: `str`




## ListApplicationSnapshotsResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ListApplicationSnapshotsResponseTypeDef
```




Optional fields:
- `SnapshotSummaries`: `List["SnapshotDetailsTypeDef"]`
- `NextToken`: `str`


## ListApplicationsResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ListApplicationsResponseTypeDef
```


Required fields:
- `ApplicationSummaries`: `List["ApplicationSummaryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## MappingParametersTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import MappingParametersTypeDef
```




Optional fields:
- `JSONMappingParameters`: `"JSONMappingParametersTypeDef"`
- `CSVMappingParameters`: `"CSVMappingParametersTypeDef"`


## MonitoringConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import MonitoringConfigurationDescriptionTypeDef
```




Optional fields:
- `ConfigurationType`: `ConfigurationType`
- `MetricsLevel`: `MetricsLevel`
- `LogLevel`: `LogLevel`


## MonitoringConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import MonitoringConfigurationTypeDef
```


Required fields:
- `ConfigurationType`: `ConfigurationType`



Optional fields:
- `MetricsLevel`: `MetricsLevel`
- `LogLevel`: `LogLevel`


## MonitoringConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import MonitoringConfigurationUpdateTypeDef
```




Optional fields:
- `ConfigurationTypeUpdate`: `ConfigurationType`
- `MetricsLevelUpdate`: `MetricsLevel`
- `LogLevelUpdate`: `LogLevel`


## OutputDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import OutputDescriptionTypeDef
```




Optional fields:
- `OutputId`: `str`
- `Name`: `str`
- `KinesisStreamsOutputDescription`: `"KinesisStreamsOutputDescriptionTypeDef"`
- `KinesisFirehoseOutputDescription`: `"KinesisFirehoseOutputDescriptionTypeDef"`
- `LambdaOutputDescription`: `"LambdaOutputDescriptionTypeDef"`
- `DestinationSchema`: `"DestinationSchemaTypeDef"`


## OutputTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import OutputTypeDef
```


Required fields:
- `Name`: `str`
- `DestinationSchema`: `"DestinationSchemaTypeDef"`



Optional fields:
- `KinesisStreamsOutput`: `"KinesisStreamsOutputTypeDef"`
- `KinesisFirehoseOutput`: `"KinesisFirehoseOutputTypeDef"`
- `LambdaOutput`: `"LambdaOutputTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## OutputUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import OutputUpdateTypeDef
```


Required fields:
- `OutputId`: `str`



Optional fields:
- `NameUpdate`: `str`
- `KinesisStreamsOutputUpdate`: `"KinesisStreamsOutputUpdateTypeDef"`
- `KinesisFirehoseOutputUpdate`: `"KinesisFirehoseOutputUpdateTypeDef"`
- `LambdaOutputUpdate`: `"LambdaOutputUpdateTypeDef"`
- `DestinationSchemaUpdate`: `"DestinationSchemaTypeDef"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParallelismConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ParallelismConfigurationDescriptionTypeDef
```




Optional fields:
- `ConfigurationType`: `ConfigurationType`
- `Parallelism`: `int`
- `ParallelismPerKPU`: `int`
- `CurrentParallelism`: `int`
- `AutoScalingEnabled`: `bool`


## ParallelismConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ParallelismConfigurationTypeDef
```


Required fields:
- `ConfigurationType`: `ConfigurationType`



Optional fields:
- `Parallelism`: `int`
- `ParallelismPerKPU`: `int`
- `AutoScalingEnabled`: `bool`


## ParallelismConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ParallelismConfigurationUpdateTypeDef
```




Optional fields:
- `ConfigurationTypeUpdate`: `ConfigurationType`
- `ParallelismUpdate`: `int`
- `ParallelismPerKPUUpdate`: `int`
- `AutoScalingEnabledUpdate`: `bool`


## PropertyGroupTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import PropertyGroupTypeDef
```


Required fields:
- `PropertyGroupId`: `str`
- `PropertyMap`: `Dict[str, str]`




## RecordColumnTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import RecordColumnTypeDef
```


Required fields:
- `Name`: `str`
- `SqlType`: `str`



Optional fields:
- `Mapping`: `str`


## RecordFormatTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import RecordFormatTypeDef
```


Required fields:
- `RecordFormatType`: `RecordFormatType`



Optional fields:
- `MappingParameters`: `"MappingParametersTypeDef"`


## ReferenceDataSourceDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ReferenceDataSourceDescriptionTypeDef
```


Required fields:
- `ReferenceId`: `str`
- `TableName`: `str`
- `S3ReferenceDataSourceDescription`: `"S3ReferenceDataSourceDescriptionTypeDef"`



Optional fields:
- `ReferenceSchema`: `"SourceSchemaTypeDef"`


## ReferenceDataSourceTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ReferenceDataSourceTypeDef
```


Required fields:
- `TableName`: `str`
- `ReferenceSchema`: `"SourceSchemaTypeDef"`



Optional fields:
- `S3ReferenceDataSource`: `"S3ReferenceDataSourceTypeDef"`


## ReferenceDataSourceUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ReferenceDataSourceUpdateTypeDef
```


Required fields:
- `ReferenceId`: `str`



Optional fields:
- `TableNameUpdate`: `str`
- `S3ReferenceDataSourceUpdate`: `"S3ReferenceDataSourceUpdateTypeDef"`
- `ReferenceSchemaUpdate`: `"SourceSchemaTypeDef"`


## ResponseMetadata

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RunConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import RunConfigurationDescriptionTypeDef
```




Optional fields:
- `ApplicationRestoreConfigurationDescription`: `"ApplicationRestoreConfigurationTypeDef"`
- `FlinkRunConfigurationDescription`: `"FlinkRunConfigurationTypeDef"`


## RunConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import RunConfigurationTypeDef
```




Optional fields:
- `FlinkRunConfiguration`: `"FlinkRunConfigurationTypeDef"`
- `SqlRunConfigurations`: `List["SqlRunConfigurationTypeDef"]`
- `ApplicationRestoreConfiguration`: `"ApplicationRestoreConfigurationTypeDef"`


## RunConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import RunConfigurationUpdateTypeDef
```




Optional fields:
- `FlinkRunConfiguration`: `"FlinkRunConfigurationTypeDef"`
- `ApplicationRestoreConfiguration`: `"ApplicationRestoreConfigurationTypeDef"`


## S3ApplicationCodeLocationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ApplicationCodeLocationDescriptionTypeDef
```


Required fields:
- `BucketARN`: `str`
- `FileKey`: `str`



Optional fields:
- `ObjectVersion`: `str`


## S3ConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ConfigurationTypeDef
```


Required fields:
- `BucketARN`: `str`
- `FileKey`: `str`




## S3ContentLocationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ContentLocationTypeDef
```


Required fields:
- `BucketARN`: `str`
- `FileKey`: `str`



Optional fields:
- `ObjectVersion`: `str`


## S3ContentLocationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ContentLocationUpdateTypeDef
```




Optional fields:
- `BucketARNUpdate`: `str`
- `FileKeyUpdate`: `str`
- `ObjectVersionUpdate`: `str`


## S3ReferenceDataSourceDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ReferenceDataSourceDescriptionTypeDef
```


Required fields:
- `BucketARN`: `str`
- `FileKey`: `str`



Optional fields:
- `ReferenceRoleARN`: `str`


## S3ReferenceDataSourceTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ReferenceDataSourceTypeDef
```




Optional fields:
- `BucketARN`: `str`
- `FileKey`: `str`


## S3ReferenceDataSourceUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import S3ReferenceDataSourceUpdateTypeDef
```




Optional fields:
- `BucketARNUpdate`: `str`
- `FileKeyUpdate`: `str`


## SnapshotDetailsTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import SnapshotDetailsTypeDef
```


Required fields:
- `SnapshotName`: `str`
- `SnapshotStatus`: `SnapshotStatus`
- `ApplicationVersionId`: `int`



Optional fields:
- `SnapshotCreationTimestamp`: `datetime`


## SourceSchemaTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import SourceSchemaTypeDef
```


Required fields:
- `RecordFormat`: `"RecordFormatTypeDef"`
- `RecordColumns`: `List["RecordColumnTypeDef"]`



Optional fields:
- `RecordEncoding`: `str`


## SqlApplicationConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import SqlApplicationConfigurationDescriptionTypeDef
```




Optional fields:
- `InputDescriptions`: `List["InputDescriptionTypeDef"]`
- `OutputDescriptions`: `List["OutputDescriptionTypeDef"]`
- `ReferenceDataSourceDescriptions`: `List["ReferenceDataSourceDescriptionTypeDef"]`


## SqlApplicationConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import SqlApplicationConfigurationTypeDef
```




Optional fields:
- `Inputs`: `List["InputTypeDef"]`
- `Outputs`: `List["OutputTypeDef"]`
- `ReferenceDataSources`: `List["ReferenceDataSourceTypeDef"]`


## SqlApplicationConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import SqlApplicationConfigurationUpdateTypeDef
```




Optional fields:
- `InputUpdates`: `List["InputUpdateTypeDef"]`
- `OutputUpdates`: `List["OutputUpdateTypeDef"]`
- `ReferenceDataSourceUpdates`: `List["ReferenceDataSourceUpdateTypeDef"]`


## SqlRunConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import SqlRunConfigurationTypeDef
```


Required fields:
- `InputId`: `str`
- `InputStartingPositionConfiguration`: `"InputStartingPositionConfigurationTypeDef"`




## TagTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## UpdateApplicationMaintenanceConfigurationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import UpdateApplicationMaintenanceConfigurationResponseTypeDef
```




Optional fields:
- `ApplicationARN`: `str`
- `ApplicationMaintenanceConfigurationDescription`: `"ApplicationMaintenanceConfigurationDescriptionTypeDef"`


## UpdateApplicationResponseTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import UpdateApplicationResponseTypeDef
```


Required fields:
- `ApplicationDetail`: `"ApplicationDetailTypeDef"`




## VpcConfigurationDescriptionTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import VpcConfigurationDescriptionTypeDef
```


Required fields:
- `VpcConfigurationId`: `str`
- `VpcId`: `str`
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`




## VpcConfigurationTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import VpcConfigurationTypeDef
```


Required fields:
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`




## VpcConfigurationUpdateTypeDef

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import VpcConfigurationUpdateTypeDef
```


Required fields:
- `VpcConfigurationId`: `str`



Optional fields:
- `SubnetIdUpdates`: `List[str]`
- `SecurityGroupIdUpdates`: `List[str]`

