# Type annotations for boto3 KinesisAnalyticsV2 module

> [Index](../index.md) > KinesisAnalyticsV2

Auto-generated documentation for [KinesisAnalyticsV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2)
type annotations stubs module [mypy_boto3_kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/).

```bash
pip install mypy-boto3-kinesisanalyticsv2
```

- [Type annotations for boto3 KinesisAnalyticsV2 module](#type-annotations-for-boto3-kinesisanalyticsv2-module)
  - [KinesisAnalyticsV2Client](#kinesisanalyticsv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisAnalyticsV2Client

Type annotations for  `boto3.client("kinesisanalyticsv2")` as [KinesisAnalyticsV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesisanalyticsv2.client import KinesisAnalyticsV2Client
```


KinesisAnalyticsV2Client [exceptions](./client.md#exceptions)



### Methods
- [add_application_cloud_watch_logging_option](./client.md#add-application-cloud-watch-logging-option)
- [add_application_input](./client.md#add-application-input)
- [add_application_input_processing_configuration](./client.md#add-application-input-processing-configuration)
- [add_application_output](./client.md#add-application-output)
- [add_application_reference_data_source](./client.md#add-application-reference-data-source)
- [add_application_vpc_configuration](./client.md#add-application-vpc-configuration)
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [create_application_presigned_url](./client.md#create-application-presigned-url)
- [create_application_snapshot](./client.md#create-application-snapshot)
- [delete_application](./client.md#delete-application)
- [delete_application_cloud_watch_logging_option](./client.md#delete-application-cloud-watch-logging-option)
- [delete_application_input_processing_configuration](./client.md#delete-application-input-processing-configuration)
- [delete_application_output](./client.md#delete-application-output)
- [delete_application_reference_data_source](./client.md#delete-application-reference-data-source)
- [delete_application_snapshot](./client.md#delete-application-snapshot)
- [delete_application_vpc_configuration](./client.md#delete-application-vpc-configuration)
- [describe_application](./client.md#describe-application)
- [describe_application_snapshot](./client.md#describe-application-snapshot)
- [discover_input_schema](./client.md#discover-input-schema)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_application_snapshots](./client.md#list-application-snapshots)
- [list_applications](./client.md#list-applications)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_application](./client.md#start-application)
- [stop_application](./client.md#stop-application)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)
- [update_application_maintenance_configuration](./client.md#update-application-maintenance-configuration)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CodeValidationException](./client.md#codevalidationexception)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InvalidApplicationConfigurationException](./client.md#invalidapplicationconfigurationexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceProvisionedThroughputExceededException](./client.md#resourceprovisionedthroughputexceededexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnableToDetectSchemaException](./client.md#unabletodetectschemaexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("kinesisanalyticsv2").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_kinesisanalyticsv2.paginators import ListApplicationSnapshotsPaginator, ...
```

- [ListApplicationSnapshotsPaginator](./paginators.md#listapplicationsnapshotspaginator)
- [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesisanalyticsv2.literals import ApplicationRestoreType, ...
```

- [ApplicationRestoreType](./literals.md#applicationrestoretype)
- [ApplicationStatus](./literals.md#applicationstatus)
- [CodeContentType](./literals.md#codecontenttype)
- [ConfigurationType](./literals.md#configurationtype)
- [InputStartingPosition](./literals.md#inputstartingposition)
- [ListApplicationSnapshotsPaginatorName](./literals.md#listapplicationsnapshotspaginatorname)
- [ListApplicationsPaginatorName](./literals.md#listapplicationspaginatorname)
- [LogLevel](./literals.md#loglevel)
- [MetricsLevel](./literals.md#metricslevel)
- [RecordFormatType](./literals.md#recordformattype)
- [RuntimeEnvironment](./literals.md#runtimeenvironment)
- [SnapshotStatus](./literals.md#snapshotstatus)
- [UrlType](./literals.md#urltype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesisanalyticsv2.type_defs import ApplicationCodeConfigurationDescriptionTypeDef, ...
```

- [ApplicationCodeConfigurationDescriptionTypeDef](./type_defs.md#applicationcodeconfigurationdescriptiontypedef)
- [ApplicationCodeConfigurationTypeDef](./type_defs.md#applicationcodeconfigurationtypedef)
- [ApplicationCodeConfigurationUpdateTypeDef](./type_defs.md#applicationcodeconfigurationupdatetypedef)
- [ApplicationConfigurationDescriptionTypeDef](./type_defs.md#applicationconfigurationdescriptiontypedef)
- [ApplicationDetailTypeDef](./type_defs.md#applicationdetailtypedef)
- [ApplicationMaintenanceConfigurationDescriptionTypeDef](./type_defs.md#applicationmaintenanceconfigurationdescriptiontypedef)
- [ApplicationRestoreConfigurationTypeDef](./type_defs.md#applicationrestoreconfigurationtypedef)
- [ApplicationSnapshotConfigurationDescriptionTypeDef](./type_defs.md#applicationsnapshotconfigurationdescriptiontypedef)
- [ApplicationSnapshotConfigurationTypeDef](./type_defs.md#applicationsnapshotconfigurationtypedef)
- [ApplicationSnapshotConfigurationUpdateTypeDef](./type_defs.md#applicationsnapshotconfigurationupdatetypedef)
- [ApplicationSummaryTypeDef](./type_defs.md#applicationsummarytypedef)
- [CSVMappingParametersTypeDef](./type_defs.md#csvmappingparameterstypedef)
- [CheckpointConfigurationDescriptionTypeDef](./type_defs.md#checkpointconfigurationdescriptiontypedef)
- [CheckpointConfigurationTypeDef](./type_defs.md#checkpointconfigurationtypedef)
- [CheckpointConfigurationUpdateTypeDef](./type_defs.md#checkpointconfigurationupdatetypedef)
- [CloudWatchLoggingOptionDescriptionTypeDef](./type_defs.md#cloudwatchloggingoptiondescriptiontypedef)
- [CodeContentDescriptionTypeDef](./type_defs.md#codecontentdescriptiontypedef)
- [CodeContentTypeDef](./type_defs.md#codecontenttypedef)
- [CodeContentUpdateTypeDef](./type_defs.md#codecontentupdatetypedef)
- [DestinationSchemaTypeDef](./type_defs.md#destinationschematypedef)
- [EnvironmentPropertiesTypeDef](./type_defs.md#environmentpropertiestypedef)
- [EnvironmentPropertyDescriptionsTypeDef](./type_defs.md#environmentpropertydescriptionstypedef)
- [EnvironmentPropertyUpdatesTypeDef](./type_defs.md#environmentpropertyupdatestypedef)
- [FlinkApplicationConfigurationDescriptionTypeDef](./type_defs.md#flinkapplicationconfigurationdescriptiontypedef)
- [FlinkApplicationConfigurationTypeDef](./type_defs.md#flinkapplicationconfigurationtypedef)
- [FlinkApplicationConfigurationUpdateTypeDef](./type_defs.md#flinkapplicationconfigurationupdatetypedef)
- [FlinkRunConfigurationTypeDef](./type_defs.md#flinkrunconfigurationtypedef)
- [InputDescriptionTypeDef](./type_defs.md#inputdescriptiontypedef)
- [InputLambdaProcessorDescriptionTypeDef](./type_defs.md#inputlambdaprocessordescriptiontypedef)
- [InputLambdaProcessorTypeDef](./type_defs.md#inputlambdaprocessortypedef)
- [InputLambdaProcessorUpdateTypeDef](./type_defs.md#inputlambdaprocessorupdatetypedef)
- [InputParallelismTypeDef](./type_defs.md#inputparallelismtypedef)
- [InputParallelismUpdateTypeDef](./type_defs.md#inputparallelismupdatetypedef)
- [InputProcessingConfigurationDescriptionTypeDef](./type_defs.md#inputprocessingconfigurationdescriptiontypedef)
- [InputProcessingConfigurationTypeDef](./type_defs.md#inputprocessingconfigurationtypedef)
- [InputProcessingConfigurationUpdateTypeDef](./type_defs.md#inputprocessingconfigurationupdatetypedef)
- [InputSchemaUpdateTypeDef](./type_defs.md#inputschemaupdatetypedef)
- [InputStartingPositionConfigurationTypeDef](./type_defs.md#inputstartingpositionconfigurationtypedef)
- [InputTypeDef](./type_defs.md#inputtypedef)
- [InputUpdateTypeDef](./type_defs.md#inputupdatetypedef)
- [JSONMappingParametersTypeDef](./type_defs.md#jsonmappingparameterstypedef)
- [KinesisFirehoseInputDescriptionTypeDef](./type_defs.md#kinesisfirehoseinputdescriptiontypedef)
- [KinesisFirehoseInputTypeDef](./type_defs.md#kinesisfirehoseinputtypedef)
- [KinesisFirehoseInputUpdateTypeDef](./type_defs.md#kinesisfirehoseinputupdatetypedef)
- [KinesisFirehoseOutputDescriptionTypeDef](./type_defs.md#kinesisfirehoseoutputdescriptiontypedef)
- [KinesisFirehoseOutputTypeDef](./type_defs.md#kinesisfirehoseoutputtypedef)
- [KinesisFirehoseOutputUpdateTypeDef](./type_defs.md#kinesisfirehoseoutputupdatetypedef)
- [KinesisStreamsInputDescriptionTypeDef](./type_defs.md#kinesisstreamsinputdescriptiontypedef)
- [KinesisStreamsInputTypeDef](./type_defs.md#kinesisstreamsinputtypedef)
- [KinesisStreamsInputUpdateTypeDef](./type_defs.md#kinesisstreamsinputupdatetypedef)
- [KinesisStreamsOutputDescriptionTypeDef](./type_defs.md#kinesisstreamsoutputdescriptiontypedef)
- [KinesisStreamsOutputTypeDef](./type_defs.md#kinesisstreamsoutputtypedef)
- [KinesisStreamsOutputUpdateTypeDef](./type_defs.md#kinesisstreamsoutputupdatetypedef)
- [LambdaOutputDescriptionTypeDef](./type_defs.md#lambdaoutputdescriptiontypedef)
- [LambdaOutputTypeDef](./type_defs.md#lambdaoutputtypedef)
- [LambdaOutputUpdateTypeDef](./type_defs.md#lambdaoutputupdatetypedef)
- [MappingParametersTypeDef](./type_defs.md#mappingparameterstypedef)
- [MonitoringConfigurationDescriptionTypeDef](./type_defs.md#monitoringconfigurationdescriptiontypedef)
- [MonitoringConfigurationTypeDef](./type_defs.md#monitoringconfigurationtypedef)
- [MonitoringConfigurationUpdateTypeDef](./type_defs.md#monitoringconfigurationupdatetypedef)
- [OutputDescriptionTypeDef](./type_defs.md#outputdescriptiontypedef)
- [OutputTypeDef](./type_defs.md#outputtypedef)
- [OutputUpdateTypeDef](./type_defs.md#outputupdatetypedef)
- [ParallelismConfigurationDescriptionTypeDef](./type_defs.md#parallelismconfigurationdescriptiontypedef)
- [ParallelismConfigurationTypeDef](./type_defs.md#parallelismconfigurationtypedef)
- [ParallelismConfigurationUpdateTypeDef](./type_defs.md#parallelismconfigurationupdatetypedef)
- [PropertyGroupTypeDef](./type_defs.md#propertygrouptypedef)
- [RecordColumnTypeDef](./type_defs.md#recordcolumntypedef)
- [RecordFormatTypeDef](./type_defs.md#recordformattypedef)
- [ReferenceDataSourceDescriptionTypeDef](./type_defs.md#referencedatasourcedescriptiontypedef)
- [ReferenceDataSourceTypeDef](./type_defs.md#referencedatasourcetypedef)
- [ReferenceDataSourceUpdateTypeDef](./type_defs.md#referencedatasourceupdatetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RunConfigurationDescriptionTypeDef](./type_defs.md#runconfigurationdescriptiontypedef)
- [S3ApplicationCodeLocationDescriptionTypeDef](./type_defs.md#s3applicationcodelocationdescriptiontypedef)
- [S3ContentLocationTypeDef](./type_defs.md#s3contentlocationtypedef)
- [S3ContentLocationUpdateTypeDef](./type_defs.md#s3contentlocationupdatetypedef)
- [S3ReferenceDataSourceDescriptionTypeDef](./type_defs.md#s3referencedatasourcedescriptiontypedef)
- [S3ReferenceDataSourceTypeDef](./type_defs.md#s3referencedatasourcetypedef)
- [S3ReferenceDataSourceUpdateTypeDef](./type_defs.md#s3referencedatasourceupdatetypedef)
- [SnapshotDetailsTypeDef](./type_defs.md#snapshotdetailstypedef)
- [SourceSchemaTypeDef](./type_defs.md#sourceschematypedef)
- [SqlApplicationConfigurationDescriptionTypeDef](./type_defs.md#sqlapplicationconfigurationdescriptiontypedef)
- [SqlApplicationConfigurationTypeDef](./type_defs.md#sqlapplicationconfigurationtypedef)
- [SqlApplicationConfigurationUpdateTypeDef](./type_defs.md#sqlapplicationconfigurationupdatetypedef)
- [SqlRunConfigurationTypeDef](./type_defs.md#sqlrunconfigurationtypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [VpcConfigurationDescriptionTypeDef](./type_defs.md#vpcconfigurationdescriptiontypedef)
- [VpcConfigurationTypeDef](./type_defs.md#vpcconfigurationtypedef)
- [VpcConfigurationUpdateTypeDef](./type_defs.md#vpcconfigurationupdatetypedef)
- [AddApplicationCloudWatchLoggingOptionResponseTypeDef](./type_defs.md#addapplicationcloudwatchloggingoptionresponsetypedef)
- [AddApplicationInputProcessingConfigurationResponseTypeDef](./type_defs.md#addapplicationinputprocessingconfigurationresponsetypedef)
- [AddApplicationInputResponseTypeDef](./type_defs.md#addapplicationinputresponsetypedef)
- [AddApplicationOutputResponseTypeDef](./type_defs.md#addapplicationoutputresponsetypedef)
- [AddApplicationReferenceDataSourceResponseTypeDef](./type_defs.md#addapplicationreferencedatasourceresponsetypedef)
- [AddApplicationVpcConfigurationResponseTypeDef](./type_defs.md#addapplicationvpcconfigurationresponsetypedef)
- [ApplicationConfigurationTypeDef](./type_defs.md#applicationconfigurationtypedef)
- [ApplicationConfigurationUpdateTypeDef](./type_defs.md#applicationconfigurationupdatetypedef)
- [ApplicationMaintenanceConfigurationUpdateTypeDef](./type_defs.md#applicationmaintenanceconfigurationupdatetypedef)
- [CloudWatchLoggingOptionTypeDef](./type_defs.md#cloudwatchloggingoptiontypedef)
- [CloudWatchLoggingOptionUpdateTypeDef](./type_defs.md#cloudwatchloggingoptionupdatetypedef)
- [CreateApplicationPresignedUrlResponseTypeDef](./type_defs.md#createapplicationpresignedurlresponsetypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [DeleteApplicationCloudWatchLoggingOptionResponseTypeDef](./type_defs.md#deleteapplicationcloudwatchloggingoptionresponsetypedef)
- [DeleteApplicationInputProcessingConfigurationResponseTypeDef](./type_defs.md#deleteapplicationinputprocessingconfigurationresponsetypedef)
- [DeleteApplicationOutputResponseTypeDef](./type_defs.md#deleteapplicationoutputresponsetypedef)
- [DeleteApplicationReferenceDataSourceResponseTypeDef](./type_defs.md#deleteapplicationreferencedatasourceresponsetypedef)
- [DeleteApplicationVpcConfigurationResponseTypeDef](./type_defs.md#deleteapplicationvpcconfigurationresponsetypedef)
- [DescribeApplicationResponseTypeDef](./type_defs.md#describeapplicationresponsetypedef)
- [DescribeApplicationSnapshotResponseTypeDef](./type_defs.md#describeapplicationsnapshotresponsetypedef)
- [DiscoverInputSchemaResponseTypeDef](./type_defs.md#discoverinputschemaresponsetypedef)
- [ListApplicationSnapshotsResponseTypeDef](./type_defs.md#listapplicationsnapshotsresponsetypedef)
- [ListApplicationsResponseTypeDef](./type_defs.md#listapplicationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RunConfigurationTypeDef](./type_defs.md#runconfigurationtypedef)
- [RunConfigurationUpdateTypeDef](./type_defs.md#runconfigurationupdatetypedef)
- [S3ConfigurationTypeDef](./type_defs.md#s3configurationtypedef)
- [UpdateApplicationMaintenanceConfigurationResponseTypeDef](./type_defs.md#updateapplicationmaintenanceconfigurationresponsetypedef)
- [UpdateApplicationResponseTypeDef](./type_defs.md#updateapplicationresponsetypedef)
