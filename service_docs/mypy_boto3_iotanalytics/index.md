# Type annotations for boto3 IoTAnalytics module

> [Index](../index.md) > IoTAnalytics

Auto-generated documentation for [IoTAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics)
type annotations stubs module [mypy_boto3_iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics/).

```bash
pip install mypy-boto3-iotanalytics
```

- [Type annotations for boto3 IoTAnalytics module](#type-annotations-for-boto3-iotanalytics-module)
  - [IoTAnalyticsClient](#iotanalyticsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTAnalyticsClient

Type annotations for  `boto3.client("iotanalytics")` as [IoTAnalyticsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotanalytics.client import IoTAnalyticsClient
```


IoTAnalyticsClient [exceptions](./client.md#exceptions)



### Methods
- [batch_put_message](./client.md#batch-put-message)
- [can_paginate](./client.md#can-paginate)
- [cancel_pipeline_reprocessing](./client.md#cancel-pipeline-reprocessing)
- [create_channel](./client.md#create-channel)
- [create_dataset](./client.md#create-dataset)
- [create_dataset_content](./client.md#create-dataset-content)
- [create_datastore](./client.md#create-datastore)
- [create_pipeline](./client.md#create-pipeline)
- [delete_channel](./client.md#delete-channel)
- [delete_dataset](./client.md#delete-dataset)
- [delete_dataset_content](./client.md#delete-dataset-content)
- [delete_datastore](./client.md#delete-datastore)
- [delete_pipeline](./client.md#delete-pipeline)
- [describe_channel](./client.md#describe-channel)
- [describe_dataset](./client.md#describe-dataset)
- [describe_datastore](./client.md#describe-datastore)
- [describe_logging_options](./client.md#describe-logging-options)
- [describe_pipeline](./client.md#describe-pipeline)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_dataset_content](./client.md#get-dataset-content)
- [get_paginator](./client.md#get-paginator)
- [list_channels](./client.md#list-channels)
- [list_dataset_contents](./client.md#list-dataset-contents)
- [list_datasets](./client.md#list-datasets)
- [list_datastores](./client.md#list-datastores)
- [list_pipelines](./client.md#list-pipelines)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_logging_options](./client.md#put-logging-options)
- [run_pipeline_activity](./client.md#run-pipeline-activity)
- [sample_channel_data](./client.md#sample-channel-data)
- [start_pipeline_reprocessing](./client.md#start-pipeline-reprocessing)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_channel](./client.md#update-channel)
- [update_dataset](./client.md#update-dataset)
- [update_datastore](./client.md#update-datastore)
- [update_pipeline](./client.md#update-pipeline)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [ThrottlingException](./client.md#throttlingexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iotanalytics").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iotanalytics.paginators import ListChannelsPaginator, ...
```

- [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- [ListDatasetContentsPaginator](./paginators.md#listdatasetcontentspaginator)
- [ListDatasetsPaginator](./paginators.md#listdatasetspaginator)
- [ListDatastoresPaginator](./paginators.md#listdatastorespaginator)
- [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotanalytics.literals import ChannelStatus, ...
```

- [ChannelStatus](./literals.md#channelstatus)
- [ComputeType](./literals.md#computetype)
- [DatasetActionType](./literals.md#datasetactiontype)
- [DatasetContentState](./literals.md#datasetcontentstate)
- [DatasetStatus](./literals.md#datasetstatus)
- [DatastoreStatus](./literals.md#datastorestatus)
- [FileFormatType](./literals.md#fileformattype)
- [ListChannelsPaginatorName](./literals.md#listchannelspaginatorname)
- [ListDatasetContentsPaginatorName](./literals.md#listdatasetcontentspaginatorname)
- [ListDatasetsPaginatorName](./literals.md#listdatasetspaginatorname)
- [ListDatastoresPaginatorName](./literals.md#listdatastorespaginatorname)
- [ListPipelinesPaginatorName](./literals.md#listpipelinespaginatorname)
- [LoggingLevel](./literals.md#logginglevel)
- [ReprocessingStatus](./literals.md#reprocessingstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityTypeDef, ...
```

- [AddAttributesActivityTypeDef](./type_defs.md#addattributesactivitytypedef)
- [BatchPutMessageErrorEntryTypeDef](./type_defs.md#batchputmessageerrorentrytypedef)
- [BatchPutMessageResponseTypeDef](./type_defs.md#batchputmessageresponsetypedef)
- [ChannelActivityTypeDef](./type_defs.md#channelactivitytypedef)
- [ChannelMessagesTypeDef](./type_defs.md#channelmessagestypedef)
- [ChannelStatisticsTypeDef](./type_defs.md#channelstatisticstypedef)
- [ChannelStorageSummaryTypeDef](./type_defs.md#channelstoragesummarytypedef)
- [ChannelStorageTypeDef](./type_defs.md#channelstoragetypedef)
- [ChannelSummaryTypeDef](./type_defs.md#channelsummarytypedef)
- [ChannelTypeDef](./type_defs.md#channeltypedef)
- [ColumnTypeDef](./type_defs.md#columntypedef)
- [ContainerDatasetActionTypeDef](./type_defs.md#containerdatasetactiontypedef)
- [CreateChannelResponseTypeDef](./type_defs.md#createchannelresponsetypedef)
- [CreateDatasetContentResponseTypeDef](./type_defs.md#createdatasetcontentresponsetypedef)
- [CreateDatasetResponseTypeDef](./type_defs.md#createdatasetresponsetypedef)
- [CreateDatastoreResponseTypeDef](./type_defs.md#createdatastoreresponsetypedef)
- [CreatePipelineResponseTypeDef](./type_defs.md#createpipelineresponsetypedef)
- [CustomerManagedChannelS3StorageSummaryTypeDef](./type_defs.md#customermanagedchannels3storagesummarytypedef)
- [CustomerManagedChannelS3StorageTypeDef](./type_defs.md#customermanagedchannels3storagetypedef)
- [CustomerManagedDatastoreS3StorageSummaryTypeDef](./type_defs.md#customermanageddatastores3storagesummarytypedef)
- [CustomerManagedDatastoreS3StorageTypeDef](./type_defs.md#customermanageddatastores3storagetypedef)
- [DatasetActionSummaryTypeDef](./type_defs.md#datasetactionsummarytypedef)
- [DatasetActionTypeDef](./type_defs.md#datasetactiontypedef)
- [DatasetContentDeliveryDestinationTypeDef](./type_defs.md#datasetcontentdeliverydestinationtypedef)
- [DatasetContentDeliveryRuleTypeDef](./type_defs.md#datasetcontentdeliveryruletypedef)
- [DatasetContentStatusTypeDef](./type_defs.md#datasetcontentstatustypedef)
- [DatasetContentSummaryTypeDef](./type_defs.md#datasetcontentsummarytypedef)
- [DatasetContentVersionValueTypeDef](./type_defs.md#datasetcontentversionvaluetypedef)
- [DatasetEntryTypeDef](./type_defs.md#datasetentrytypedef)
- [DatasetSummaryTypeDef](./type_defs.md#datasetsummarytypedef)
- [DatasetTriggerTypeDef](./type_defs.md#datasettriggertypedef)
- [DatasetTypeDef](./type_defs.md#datasettypedef)
- [DatastoreActivityTypeDef](./type_defs.md#datastoreactivitytypedef)
- [DatastoreStatisticsTypeDef](./type_defs.md#datastorestatisticstypedef)
- [DatastoreStorageSummaryTypeDef](./type_defs.md#datastorestoragesummarytypedef)
- [DatastoreStorageTypeDef](./type_defs.md#datastorestoragetypedef)
- [DatastoreSummaryTypeDef](./type_defs.md#datastoresummarytypedef)
- [DatastoreTypeDef](./type_defs.md#datastoretypedef)
- [DeltaTimeSessionWindowConfigurationTypeDef](./type_defs.md#deltatimesessionwindowconfigurationtypedef)
- [DeltaTimeTypeDef](./type_defs.md#deltatimetypedef)
- [DescribeChannelResponseTypeDef](./type_defs.md#describechannelresponsetypedef)
- [DescribeDatasetResponseTypeDef](./type_defs.md#describedatasetresponsetypedef)
- [DescribeDatastoreResponseTypeDef](./type_defs.md#describedatastoreresponsetypedef)
- [DescribeLoggingOptionsResponseTypeDef](./type_defs.md#describeloggingoptionsresponsetypedef)
- [DescribePipelineResponseTypeDef](./type_defs.md#describepipelineresponsetypedef)
- [DeviceRegistryEnrichActivityTypeDef](./type_defs.md#deviceregistryenrichactivitytypedef)
- [DeviceShadowEnrichActivityTypeDef](./type_defs.md#deviceshadowenrichactivitytypedef)
- [EstimatedResourceSizeTypeDef](./type_defs.md#estimatedresourcesizetypedef)
- [FileFormatConfigurationTypeDef](./type_defs.md#fileformatconfigurationtypedef)
- [FilterActivityTypeDef](./type_defs.md#filteractivitytypedef)
- [GetDatasetContentResponseTypeDef](./type_defs.md#getdatasetcontentresponsetypedef)
- [GlueConfigurationTypeDef](./type_defs.md#glueconfigurationtypedef)
- [IotEventsDestinationConfigurationTypeDef](./type_defs.md#ioteventsdestinationconfigurationtypedef)
- [LambdaActivityTypeDef](./type_defs.md#lambdaactivitytypedef)
- [LateDataRuleConfigurationTypeDef](./type_defs.md#latedataruleconfigurationtypedef)
- [LateDataRuleTypeDef](./type_defs.md#latedataruletypedef)
- [ListChannelsResponseTypeDef](./type_defs.md#listchannelsresponsetypedef)
- [ListDatasetContentsResponseTypeDef](./type_defs.md#listdatasetcontentsresponsetypedef)
- [ListDatasetsResponseTypeDef](./type_defs.md#listdatasetsresponsetypedef)
- [ListDatastoresResponseTypeDef](./type_defs.md#listdatastoresresponsetypedef)
- [ListPipelinesResponseTypeDef](./type_defs.md#listpipelinesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [LoggingOptionsTypeDef](./type_defs.md#loggingoptionstypedef)
- [MathActivityTypeDef](./type_defs.md#mathactivitytypedef)
- [MessageTypeDef](./type_defs.md#messagetypedef)
- [OutputFileUriValueTypeDef](./type_defs.md#outputfileurivaluetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParquetConfigurationTypeDef](./type_defs.md#parquetconfigurationtypedef)
- [PipelineActivityTypeDef](./type_defs.md#pipelineactivitytypedef)
- [PipelineSummaryTypeDef](./type_defs.md#pipelinesummarytypedef)
- [PipelineTypeDef](./type_defs.md#pipelinetypedef)
- [QueryFilterTypeDef](./type_defs.md#queryfiltertypedef)
- [RemoveAttributesActivityTypeDef](./type_defs.md#removeattributesactivitytypedef)
- [ReprocessingSummaryTypeDef](./type_defs.md#reprocessingsummarytypedef)
- [ResourceConfigurationTypeDef](./type_defs.md#resourceconfigurationtypedef)
- [RetentionPeriodTypeDef](./type_defs.md#retentionperiodtypedef)
- [RunPipelineActivityResponseTypeDef](./type_defs.md#runpipelineactivityresponsetypedef)
- [S3DestinationConfigurationTypeDef](./type_defs.md#s3destinationconfigurationtypedef)
- [SampleChannelDataResponseTypeDef](./type_defs.md#samplechanneldataresponsetypedef)
- [ScheduleTypeDef](./type_defs.md#scheduletypedef)
- [SchemaDefinitionTypeDef](./type_defs.md#schemadefinitiontypedef)
- [SelectAttributesActivityTypeDef](./type_defs.md#selectattributesactivitytypedef)
- [SqlQueryDatasetActionTypeDef](./type_defs.md#sqlquerydatasetactiontypedef)
- [StartPipelineReprocessingResponseTypeDef](./type_defs.md#startpipelinereprocessingresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TriggeringDatasetTypeDef](./type_defs.md#triggeringdatasettypedef)
- [VariableTypeDef](./type_defs.md#variabletypedef)
- [VersioningConfigurationTypeDef](./type_defs.md#versioningconfigurationtypedef)
