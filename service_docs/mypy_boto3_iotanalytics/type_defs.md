# Structures for boto3 IoTAnalytics module

> [Index](../index.md) > [IoTAnalytics](./index.md) > Structures

Auto-generated documentation for [IoTAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics)
type annotations stubs module [mypy_boto3_iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics/).

- [Structures for boto3 IoTAnalytics module](#structures-for-boto3-iotanalytics-module)
  - [AddAttributesActivityTypeDef](#addattributesactivitytypedef)
  - [BatchPutMessageErrorEntryTypeDef](#batchputmessageerrorentrytypedef)
  - [BatchPutMessageResponseTypeDef](#batchputmessageresponsetypedef)
  - [ChannelActivityTypeDef](#channelactivitytypedef)
  - [ChannelMessagesTypeDef](#channelmessagestypedef)
  - [ChannelStatisticsTypeDef](#channelstatisticstypedef)
  - [ChannelStorageSummaryTypeDef](#channelstoragesummarytypedef)
  - [ChannelStorageTypeDef](#channelstoragetypedef)
  - [ChannelSummaryTypeDef](#channelsummarytypedef)
  - [ChannelTypeDef](#channeltypedef)
  - [ColumnTypeDef](#columntypedef)
  - [ContainerDatasetActionTypeDef](#containerdatasetactiontypedef)
  - [CreateChannelResponseTypeDef](#createchannelresponsetypedef)
  - [CreateDatasetContentResponseTypeDef](#createdatasetcontentresponsetypedef)
  - [CreateDatasetResponseTypeDef](#createdatasetresponsetypedef)
  - [CreateDatastoreResponseTypeDef](#createdatastoreresponsetypedef)
  - [CreatePipelineResponseTypeDef](#createpipelineresponsetypedef)
  - [CustomerManagedChannelS3StorageSummaryTypeDef](#customermanagedchannels3storagesummarytypedef)
  - [CustomerManagedChannelS3StorageTypeDef](#customermanagedchannels3storagetypedef)
  - [CustomerManagedDatastoreS3StorageSummaryTypeDef](#customermanageddatastores3storagesummarytypedef)
  - [CustomerManagedDatastoreS3StorageTypeDef](#customermanageddatastores3storagetypedef)
  - [DatasetActionSummaryTypeDef](#datasetactionsummarytypedef)
  - [DatasetActionTypeDef](#datasetactiontypedef)
  - [DatasetContentDeliveryDestinationTypeDef](#datasetcontentdeliverydestinationtypedef)
  - [DatasetContentDeliveryRuleTypeDef](#datasetcontentdeliveryruletypedef)
  - [DatasetContentStatusTypeDef](#datasetcontentstatustypedef)
  - [DatasetContentSummaryTypeDef](#datasetcontentsummarytypedef)
  - [DatasetContentVersionValueTypeDef](#datasetcontentversionvaluetypedef)
  - [DatasetEntryTypeDef](#datasetentrytypedef)
  - [DatasetSummaryTypeDef](#datasetsummarytypedef)
  - [DatasetTriggerTypeDef](#datasettriggertypedef)
  - [DatasetTypeDef](#datasettypedef)
  - [DatastoreActivityTypeDef](#datastoreactivitytypedef)
  - [DatastoreStatisticsTypeDef](#datastorestatisticstypedef)
  - [DatastoreStorageSummaryTypeDef](#datastorestoragesummarytypedef)
  - [DatastoreStorageTypeDef](#datastorestoragetypedef)
  - [DatastoreSummaryTypeDef](#datastoresummarytypedef)
  - [DatastoreTypeDef](#datastoretypedef)
  - [DeltaTimeSessionWindowConfigurationTypeDef](#deltatimesessionwindowconfigurationtypedef)
  - [DeltaTimeTypeDef](#deltatimetypedef)
  - [DescribeChannelResponseTypeDef](#describechannelresponsetypedef)
  - [DescribeDatasetResponseTypeDef](#describedatasetresponsetypedef)
  - [DescribeDatastoreResponseTypeDef](#describedatastoreresponsetypedef)
  - [DescribeLoggingOptionsResponseTypeDef](#describeloggingoptionsresponsetypedef)
  - [DescribePipelineResponseTypeDef](#describepipelineresponsetypedef)
  - [DeviceRegistryEnrichActivityTypeDef](#deviceregistryenrichactivitytypedef)
  - [DeviceShadowEnrichActivityTypeDef](#deviceshadowenrichactivitytypedef)
  - [EstimatedResourceSizeTypeDef](#estimatedresourcesizetypedef)
  - [FileFormatConfigurationTypeDef](#fileformatconfigurationtypedef)
  - [FilterActivityTypeDef](#filteractivitytypedef)
  - [GetDatasetContentResponseTypeDef](#getdatasetcontentresponsetypedef)
  - [GlueConfigurationTypeDef](#glueconfigurationtypedef)
  - [IotEventsDestinationConfigurationTypeDef](#ioteventsdestinationconfigurationtypedef)
  - [LambdaActivityTypeDef](#lambdaactivitytypedef)
  - [LateDataRuleConfigurationTypeDef](#latedataruleconfigurationtypedef)
  - [LateDataRuleTypeDef](#latedataruletypedef)
  - [ListChannelsResponseTypeDef](#listchannelsresponsetypedef)
  - [ListDatasetContentsResponseTypeDef](#listdatasetcontentsresponsetypedef)
  - [ListDatasetsResponseTypeDef](#listdatasetsresponsetypedef)
  - [ListDatastoresResponseTypeDef](#listdatastoresresponsetypedef)
  - [ListPipelinesResponseTypeDef](#listpipelinesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [LoggingOptionsTypeDef](#loggingoptionstypedef)
  - [MathActivityTypeDef](#mathactivitytypedef)
  - [MessageTypeDef](#messagetypedef)
  - [OutputFileUriValueTypeDef](#outputfileurivaluetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParquetConfigurationTypeDef](#parquetconfigurationtypedef)
  - [PipelineActivityTypeDef](#pipelineactivitytypedef)
  - [PipelineSummaryTypeDef](#pipelinesummarytypedef)
  - [PipelineTypeDef](#pipelinetypedef)
  - [QueryFilterTypeDef](#queryfiltertypedef)
  - [RemoveAttributesActivityTypeDef](#removeattributesactivitytypedef)
  - [ReprocessingSummaryTypeDef](#reprocessingsummarytypedef)
  - [ResourceConfigurationTypeDef](#resourceconfigurationtypedef)
  - [RetentionPeriodTypeDef](#retentionperiodtypedef)
  - [RunPipelineActivityResponseTypeDef](#runpipelineactivityresponsetypedef)
  - [S3DestinationConfigurationTypeDef](#s3destinationconfigurationtypedef)
  - [SampleChannelDataResponseTypeDef](#samplechanneldataresponsetypedef)
  - [ScheduleTypeDef](#scheduletypedef)
  - [SchemaDefinitionTypeDef](#schemadefinitiontypedef)
  - [SelectAttributesActivityTypeDef](#selectattributesactivitytypedef)
  - [SqlQueryDatasetActionTypeDef](#sqlquerydatasetactiontypedef)
  - [StartPipelineReprocessingResponseTypeDef](#startpipelinereprocessingresponsetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TriggeringDatasetTypeDef](#triggeringdatasettypedef)
  - [VariableTypeDef](#variabletypedef)
  - [VersioningConfigurationTypeDef](#versioningconfigurationtypedef)

## AddAttributesActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityTypeDef
```


Required fields:
- `name`: `str`
- `attributes`: `Dict[str, str]`



Optional fields:
- `next`: `str`


## BatchPutMessageErrorEntryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import BatchPutMessageErrorEntryTypeDef
```




Optional fields:
- `messageId`: `str`
- `errorCode`: `str`
- `errorMessage`: `str`


## BatchPutMessageResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import BatchPutMessageResponseTypeDef
```




Optional fields:
- `batchPutMessageErrorEntries`: `List["BatchPutMessageErrorEntryTypeDef"]`


## ChannelActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelActivityTypeDef
```


Required fields:
- `name`: `str`
- `channelName`: `str`



Optional fields:
- `next`: `str`


## ChannelMessagesTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelMessagesTypeDef
```




Optional fields:
- `s3Paths`: `List[str]`


## ChannelStatisticsTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelStatisticsTypeDef
```




Optional fields:
- `size`: `"EstimatedResourceSizeTypeDef"`


## ChannelStorageSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelStorageSummaryTypeDef
```




Optional fields:
- `serviceManagedS3`: `Dict[str, Any]`
- `customerManagedS3`: `"CustomerManagedChannelS3StorageSummaryTypeDef"`


## ChannelStorageTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelStorageTypeDef
```




Optional fields:
- `serviceManagedS3`: `Dict[str, Any]`
- `customerManagedS3`: `"CustomerManagedChannelS3StorageTypeDef"`


## ChannelSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelSummaryTypeDef
```




Optional fields:
- `channelName`: `str`
- `channelStorage`: `"ChannelStorageSummaryTypeDef"`
- `status`: `ChannelStatus`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `lastMessageArrivalTime`: `datetime`


## ChannelTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ChannelTypeDef
```




Optional fields:
- `name`: `str`
- `storage`: `"ChannelStorageTypeDef"`
- `arn`: `str`
- `status`: `ChannelStatus`
- `retentionPeriod`: `"RetentionPeriodTypeDef"`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `lastMessageArrivalTime`: `datetime`


## ColumnTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ColumnTypeDef
```


Required fields:
- `name`: `str`
- `type`: `str`




## ContainerDatasetActionTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ContainerDatasetActionTypeDef
```


Required fields:
- `image`: `str`
- `executionRoleArn`: `str`
- `resourceConfiguration`: `"ResourceConfigurationTypeDef"`



Optional fields:
- `variables`: `List["VariableTypeDef"]`


## CreateChannelResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CreateChannelResponseTypeDef
```




Optional fields:
- `channelName`: `str`
- `channelArn`: `str`
- `retentionPeriod`: `"RetentionPeriodTypeDef"`


## CreateDatasetContentResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CreateDatasetContentResponseTypeDef
```




Optional fields:
- `versionId`: `str`


## CreateDatasetResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CreateDatasetResponseTypeDef
```




Optional fields:
- `datasetName`: `str`
- `datasetArn`: `str`
- `retentionPeriod`: `"RetentionPeriodTypeDef"`


## CreateDatastoreResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CreateDatastoreResponseTypeDef
```




Optional fields:
- `datastoreName`: `str`
- `datastoreArn`: `str`
- `retentionPeriod`: `"RetentionPeriodTypeDef"`


## CreatePipelineResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CreatePipelineResponseTypeDef
```




Optional fields:
- `pipelineName`: `str`
- `pipelineArn`: `str`


## CustomerManagedChannelS3StorageSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CustomerManagedChannelS3StorageSummaryTypeDef
```




Optional fields:
- `bucket`: `str`
- `keyPrefix`: `str`
- `roleArn`: `str`


## CustomerManagedChannelS3StorageTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CustomerManagedChannelS3StorageTypeDef
```


Required fields:
- `bucket`: `str`
- `roleArn`: `str`



Optional fields:
- `keyPrefix`: `str`


## CustomerManagedDatastoreS3StorageSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CustomerManagedDatastoreS3StorageSummaryTypeDef
```




Optional fields:
- `bucket`: `str`
- `keyPrefix`: `str`
- `roleArn`: `str`


## CustomerManagedDatastoreS3StorageTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import CustomerManagedDatastoreS3StorageTypeDef
```


Required fields:
- `bucket`: `str`
- `roleArn`: `str`



Optional fields:
- `keyPrefix`: `str`


## DatasetActionSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetActionSummaryTypeDef
```




Optional fields:
- `actionName`: `str`
- `actionType`: `DatasetActionType`


## DatasetActionTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetActionTypeDef
```




Optional fields:
- `actionName`: `str`
- `queryAction`: `"SqlQueryDatasetActionTypeDef"`
- `containerAction`: `"ContainerDatasetActionTypeDef"`


## DatasetContentDeliveryDestinationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetContentDeliveryDestinationTypeDef
```




Optional fields:
- `iotEventsDestinationConfiguration`: `"IotEventsDestinationConfigurationTypeDef"`
- `s3DestinationConfiguration`: `"S3DestinationConfigurationTypeDef"`


## DatasetContentDeliveryRuleTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetContentDeliveryRuleTypeDef
```


Required fields:
- `destination`: `"DatasetContentDeliveryDestinationTypeDef"`



Optional fields:
- `entryName`: `str`


## DatasetContentStatusTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetContentStatusTypeDef
```




Optional fields:
- `state`: `DatasetContentState`
- `reason`: `str`


## DatasetContentSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetContentSummaryTypeDef
```




Optional fields:
- `version`: `str`
- `status`: `"DatasetContentStatusTypeDef"`
- `creationTime`: `datetime`
- `scheduleTime`: `datetime`
- `completionTime`: `datetime`


## DatasetContentVersionValueTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetContentVersionValueTypeDef
```


Required fields:
- `datasetName`: `str`




## DatasetEntryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetEntryTypeDef
```




Optional fields:
- `entryName`: `str`
- `dataURI`: `str`


## DatasetSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetSummaryTypeDef
```




Optional fields:
- `datasetName`: `str`
- `status`: `DatasetStatus`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `triggers`: `List["DatasetTriggerTypeDef"]`
- `actions`: `List["DatasetActionSummaryTypeDef"]`


## DatasetTriggerTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetTriggerTypeDef
```




Optional fields:
- `schedule`: `"ScheduleTypeDef"`
- `dataset`: `"TriggeringDatasetTypeDef"`


## DatasetTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatasetTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `actions`: `List["DatasetActionTypeDef"]`
- `triggers`: `List["DatasetTriggerTypeDef"]`
- `contentDeliveryRules`: `List["DatasetContentDeliveryRuleTypeDef"]`
- `status`: `DatasetStatus`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `retentionPeriod`: `"RetentionPeriodTypeDef"`
- `versioningConfiguration`: `"VersioningConfigurationTypeDef"`
- `lateDataRules`: `List["LateDataRuleTypeDef"]`


## DatastoreActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatastoreActivityTypeDef
```


Required fields:
- `name`: `str`
- `datastoreName`: `str`




## DatastoreStatisticsTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatastoreStatisticsTypeDef
```




Optional fields:
- `size`: `"EstimatedResourceSizeTypeDef"`


## DatastoreStorageSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatastoreStorageSummaryTypeDef
```




Optional fields:
- `serviceManagedS3`: `Dict[str, Any]`
- `customerManagedS3`: `"CustomerManagedDatastoreS3StorageSummaryTypeDef"`


## DatastoreStorageTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatastoreStorageTypeDef
```




Optional fields:
- `serviceManagedS3`: `Dict[str, Any]`
- `customerManagedS3`: `"CustomerManagedDatastoreS3StorageTypeDef"`


## DatastoreSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatastoreSummaryTypeDef
```




Optional fields:
- `datastoreName`: `str`
- `datastoreStorage`: `"DatastoreStorageSummaryTypeDef"`
- `status`: `DatastoreStatus`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `lastMessageArrivalTime`: `datetime`
- `fileFormatType`: `FileFormatType`


## DatastoreTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DatastoreTypeDef
```




Optional fields:
- `name`: `str`
- `storage`: `"DatastoreStorageTypeDef"`
- `arn`: `str`
- `status`: `DatastoreStatus`
- `retentionPeriod`: `"RetentionPeriodTypeDef"`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `lastMessageArrivalTime`: `datetime`
- `fileFormatConfiguration`: `"FileFormatConfigurationTypeDef"`


## DeltaTimeSessionWindowConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DeltaTimeSessionWindowConfigurationTypeDef
```


Required fields:
- `timeoutInMinutes`: `int`




## DeltaTimeTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DeltaTimeTypeDef
```


Required fields:
- `offsetSeconds`: `int`
- `timeExpression`: `str`




## DescribeChannelResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DescribeChannelResponseTypeDef
```




Optional fields:
- `channel`: `"ChannelTypeDef"`
- `statistics`: `"ChannelStatisticsTypeDef"`


## DescribeDatasetResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DescribeDatasetResponseTypeDef
```




Optional fields:
- `dataset`: `"DatasetTypeDef"`


## DescribeDatastoreResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DescribeDatastoreResponseTypeDef
```




Optional fields:
- `datastore`: `"DatastoreTypeDef"`
- `statistics`: `"DatastoreStatisticsTypeDef"`


## DescribeLoggingOptionsResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DescribeLoggingOptionsResponseTypeDef
```




Optional fields:
- `loggingOptions`: `"LoggingOptionsTypeDef"`


## DescribePipelineResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DescribePipelineResponseTypeDef
```




Optional fields:
- `pipeline`: `"PipelineTypeDef"`


## DeviceRegistryEnrichActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DeviceRegistryEnrichActivityTypeDef
```


Required fields:
- `name`: `str`
- `attribute`: `str`
- `thingName`: `str`
- `roleArn`: `str`



Optional fields:
- `next`: `str`


## DeviceShadowEnrichActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import DeviceShadowEnrichActivityTypeDef
```


Required fields:
- `name`: `str`
- `attribute`: `str`
- `thingName`: `str`
- `roleArn`: `str`



Optional fields:
- `next`: `str`


## EstimatedResourceSizeTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import EstimatedResourceSizeTypeDef
```




Optional fields:
- `estimatedSizeInBytes`: `float`
- `estimatedOn`: `datetime`


## FileFormatConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import FileFormatConfigurationTypeDef
```




Optional fields:
- `jsonConfiguration`: `Dict[str, Any]`
- `parquetConfiguration`: `"ParquetConfigurationTypeDef"`


## FilterActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import FilterActivityTypeDef
```


Required fields:
- `name`: `str`
- `filter`: `str`



Optional fields:
- `next`: `str`


## GetDatasetContentResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import GetDatasetContentResponseTypeDef
```




Optional fields:
- `entries`: `List["DatasetEntryTypeDef"]`
- `timestamp`: `datetime`
- `status`: `"DatasetContentStatusTypeDef"`


## GlueConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import GlueConfigurationTypeDef
```


Required fields:
- `tableName`: `str`
- `databaseName`: `str`




## IotEventsDestinationConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import IotEventsDestinationConfigurationTypeDef
```


Required fields:
- `inputName`: `str`
- `roleArn`: `str`




## LambdaActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import LambdaActivityTypeDef
```


Required fields:
- `name`: `str`
- `lambdaName`: `str`
- `batchSize`: `int`



Optional fields:
- `next`: `str`


## LateDataRuleConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import LateDataRuleConfigurationTypeDef
```




Optional fields:
- `deltaTimeSessionWindowConfiguration`: `"DeltaTimeSessionWindowConfigurationTypeDef"`


## LateDataRuleTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import LateDataRuleTypeDef
```


Required fields:
- `ruleConfiguration`: `"LateDataRuleConfigurationTypeDef"`



Optional fields:
- `ruleName`: `str`


## ListChannelsResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ListChannelsResponseTypeDef
```




Optional fields:
- `channelSummaries`: `List["ChannelSummaryTypeDef"]`
- `nextToken`: `str`


## ListDatasetContentsResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ListDatasetContentsResponseTypeDef
```




Optional fields:
- `datasetContentSummaries`: `List["DatasetContentSummaryTypeDef"]`
- `nextToken`: `str`


## ListDatasetsResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ListDatasetsResponseTypeDef
```




Optional fields:
- `datasetSummaries`: `List["DatasetSummaryTypeDef"]`
- `nextToken`: `str`


## ListDatastoresResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ListDatastoresResponseTypeDef
```




Optional fields:
- `datastoreSummaries`: `List["DatastoreSummaryTypeDef"]`
- `nextToken`: `str`


## ListPipelinesResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ListPipelinesResponseTypeDef
```




Optional fields:
- `pipelineSummaries`: `List["PipelineSummaryTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`


## LoggingOptionsTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import LoggingOptionsTypeDef
```


Required fields:
- `roleArn`: `str`
- `level`: `Literal['ERROR']`
- `enabled`: `bool`




## MathActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import MathActivityTypeDef
```


Required fields:
- `name`: `str`
- `attribute`: `str`
- `math`: `str`



Optional fields:
- `next`: `str`


## MessageTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import MessageTypeDef
```


Required fields:
- `messageId`: `str`
- `payload`: `Union[bytes, IO[bytes]]`




## OutputFileUriValueTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import OutputFileUriValueTypeDef
```


Required fields:
- `fileName`: `str`




## PaginatorConfigTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParquetConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ParquetConfigurationTypeDef
```




Optional fields:
- `schemaDefinition`: `"SchemaDefinitionTypeDef"`


## PipelineActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import PipelineActivityTypeDef
```




Optional fields:
- `channel`: `"ChannelActivityTypeDef"`
- `lambda`: `"LambdaActivityTypeDef"`
- `datastore`: `"DatastoreActivityTypeDef"`
- `addAttributes`: `"AddAttributesActivityTypeDef"`
- `removeAttributes`: `"RemoveAttributesActivityTypeDef"`
- `selectAttributes`: `"SelectAttributesActivityTypeDef"`
- `filter`: `"FilterActivityTypeDef"`
- `math`: `"MathActivityTypeDef"`
- `deviceRegistryEnrich`: `"DeviceRegistryEnrichActivityTypeDef"`
- `deviceShadowEnrich`: `"DeviceShadowEnrichActivityTypeDef"`


## PipelineSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import PipelineSummaryTypeDef
```




Optional fields:
- `pipelineName`: `str`
- `reprocessingSummaries`: `List["ReprocessingSummaryTypeDef"]`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`


## PipelineTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import PipelineTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `activities`: `List["PipelineActivityTypeDef"]`
- `reprocessingSummaries`: `List["ReprocessingSummaryTypeDef"]`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`


## QueryFilterTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import QueryFilterTypeDef
```




Optional fields:
- `deltaTime`: `"DeltaTimeTypeDef"`


## RemoveAttributesActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import RemoveAttributesActivityTypeDef
```


Required fields:
- `name`: `str`
- `attributes`: `List[str]`



Optional fields:
- `next`: `str`


## ReprocessingSummaryTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ReprocessingSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `status`: `ReprocessingStatus`
- `creationTime`: `datetime`


## ResourceConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ResourceConfigurationTypeDef
```


Required fields:
- `computeType`: `ComputeType`
- `volumeSizeInGB`: `int`




## RetentionPeriodTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import RetentionPeriodTypeDef
```




Optional fields:
- `unlimited`: `bool`
- `numberOfDays`: `int`


## RunPipelineActivityResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import RunPipelineActivityResponseTypeDef
```




Optional fields:
- `payloads`: `List[Union[bytes, IO[bytes]]]`
- `logResult`: `str`


## S3DestinationConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import S3DestinationConfigurationTypeDef
```


Required fields:
- `bucket`: `str`
- `key`: `str`
- `roleArn`: `str`



Optional fields:
- `glueConfiguration`: `"GlueConfigurationTypeDef"`


## SampleChannelDataResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import SampleChannelDataResponseTypeDef
```




Optional fields:
- `payloads`: `List[Union[bytes, IO[bytes]]]`


## ScheduleTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import ScheduleTypeDef
```




Optional fields:
- `expression`: `str`


## SchemaDefinitionTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import SchemaDefinitionTypeDef
```




Optional fields:
- `columns`: `List["ColumnTypeDef"]`


## SelectAttributesActivityTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import SelectAttributesActivityTypeDef
```


Required fields:
- `name`: `str`
- `attributes`: `List[str]`



Optional fields:
- `next`: `str`


## SqlQueryDatasetActionTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import SqlQueryDatasetActionTypeDef
```


Required fields:
- `sqlQuery`: `str`



Optional fields:
- `filters`: `List["QueryFilterTypeDef"]`


## StartPipelineReprocessingResponseTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import StartPipelineReprocessingResponseTypeDef
```




Optional fields:
- `reprocessingId`: `str`


## TagTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import TagTypeDef
```


Required fields:
- `key`: `str`
- `value`: `str`




## TriggeringDatasetTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import TriggeringDatasetTypeDef
```


Required fields:
- `name`: `str`




## VariableTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import VariableTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `stringValue`: `str`
- `doubleValue`: `float`
- `datasetContentVersionValue`: `"DatasetContentVersionValueTypeDef"`
- `outputFileUriValue`: `"OutputFileUriValueTypeDef"`


## VersioningConfigurationTypeDef

```python
from mypy_boto3_iotanalytics.type_defs import VersioningConfigurationTypeDef
```




Optional fields:
- `unlimited`: `bool`
- `maxVersions`: `int`

