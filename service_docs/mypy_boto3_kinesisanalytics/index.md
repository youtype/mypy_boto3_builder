# Type annotations for boto3 KinesisAnalytics module

> [Index](../index.md) > KinesisAnalytics

Auto-generated documentation for [KinesisAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics)
type annotations stubs module [mypy_boto3_kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics/).

```bash
pip install mypy-boto3-kinesisanalytics
```

- [Type annotations for boto3 KinesisAnalytics module](#type-annotations-for-boto3-kinesisanalytics-module)
  - [KinesisAnalyticsClient](#kinesisanalyticsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## KinesisAnalyticsClient

Type annotations for  `boto3.client("kinesisanalytics")` as [KinesisAnalyticsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kinesisanalytics.client import KinesisAnalyticsClient
```


KinesisAnalyticsClient [exceptions](./client.md#exceptions)



### Methods
- [add_application_cloud_watch_logging_option](./client.md#add-application-cloud-watch-logging-option)
- [add_application_input](./client.md#add-application-input)
- [add_application_input_processing_configuration](./client.md#add-application-input-processing-configuration)
- [add_application_output](./client.md#add-application-output)
- [add_application_reference_data_source](./client.md#add-application-reference-data-source)
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [delete_application](./client.md#delete-application)
- [delete_application_cloud_watch_logging_option](./client.md#delete-application-cloud-watch-logging-option)
- [delete_application_input_processing_configuration](./client.md#delete-application-input-processing-configuration)
- [delete_application_output](./client.md#delete-application-output)
- [delete_application_reference_data_source](./client.md#delete-application-reference-data-source)
- [describe_application](./client.md#describe-application)
- [discover_input_schema](./client.md#discover-input-schema)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_applications](./client.md#list-applications)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_application](./client.md#start-application)
- [stop_application](./client.md#stop-application)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CodeValidationException](./client.md#codevalidationexception)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [InvalidApplicationConfigurationException](./client.md#invalidapplicationconfigurationexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceProvisionedThroughputExceededException](./client.md#resourceprovisionedthroughputexceededexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnableToDetectSchemaException](./client.md#unabletodetectschemaexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesisanalytics.literals import ApplicationStatus, ...
```

- [ApplicationStatus](./literals.md#applicationstatus)
- [InputStartingPosition](./literals.md#inputstartingposition)
- [RecordFormatType](./literals.md#recordformattype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kinesisanalytics.type_defs import ApplicationDetailTypeDef, ...
```

- [ApplicationDetailTypeDef](./type_defs.md#applicationdetailtypedef)
- [ApplicationSummaryTypeDef](./type_defs.md#applicationsummarytypedef)
- [ApplicationUpdateTypeDef](./type_defs.md#applicationupdatetypedef)
- [CSVMappingParametersTypeDef](./type_defs.md#csvmappingparameterstypedef)
- [CloudWatchLoggingOptionDescriptionTypeDef](./type_defs.md#cloudwatchloggingoptiondescriptiontypedef)
- [CloudWatchLoggingOptionTypeDef](./type_defs.md#cloudwatchloggingoptiontypedef)
- [CloudWatchLoggingOptionUpdateTypeDef](./type_defs.md#cloudwatchloggingoptionupdatetypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [DescribeApplicationResponseTypeDef](./type_defs.md#describeapplicationresponsetypedef)
- [DestinationSchemaTypeDef](./type_defs.md#destinationschematypedef)
- [DiscoverInputSchemaResponseTypeDef](./type_defs.md#discoverinputschemaresponsetypedef)
- [InputConfigurationTypeDef](./type_defs.md#inputconfigurationtypedef)
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
- [ListApplicationsResponseTypeDef](./type_defs.md#listapplicationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MappingParametersTypeDef](./type_defs.md#mappingparameterstypedef)
- [OutputDescriptionTypeDef](./type_defs.md#outputdescriptiontypedef)
- [OutputTypeDef](./type_defs.md#outputtypedef)
- [OutputUpdateTypeDef](./type_defs.md#outputupdatetypedef)
- [RecordColumnTypeDef](./type_defs.md#recordcolumntypedef)
- [RecordFormatTypeDef](./type_defs.md#recordformattypedef)
- [ReferenceDataSourceDescriptionTypeDef](./type_defs.md#referencedatasourcedescriptiontypedef)
- [ReferenceDataSourceTypeDef](./type_defs.md#referencedatasourcetypedef)
- [ReferenceDataSourceUpdateTypeDef](./type_defs.md#referencedatasourceupdatetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3ConfigurationTypeDef](./type_defs.md#s3configurationtypedef)
- [S3ReferenceDataSourceDescriptionTypeDef](./type_defs.md#s3referencedatasourcedescriptiontypedef)
- [S3ReferenceDataSourceTypeDef](./type_defs.md#s3referencedatasourcetypedef)
- [S3ReferenceDataSourceUpdateTypeDef](./type_defs.md#s3referencedatasourceupdatetypedef)
- [SourceSchemaTypeDef](./type_defs.md#sourceschematypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
