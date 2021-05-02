# IoTAnalyticsClient for boto3 IoTAnalytics module

> [Index](../index.md) > [IoTAnalytics](./index.md) > IoTAnalyticsClient

Auto-generated documentation for [IoTAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics)
type annotations stubs module [mypy_boto3_iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics/).

- [IoTAnalyticsClient for boto3 IoTAnalytics module](#iotanalyticsclient-for-boto3-iotanalytics-module)
  - [IoTAnalyticsClient](#iotanalyticsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_put_message](#batch_put_message)
    - [can_paginate](#can_paginate)
    - [cancel_pipeline_reprocessing](#cancel_pipeline_reprocessing)
    - [create_channel](#create_channel)
    - [create_dataset](#create_dataset)
    - [create_dataset_content](#create_dataset_content)
    - [create_datastore](#create_datastore)
    - [create_pipeline](#create_pipeline)
    - [delete_channel](#delete_channel)
    - [delete_dataset](#delete_dataset)
    - [delete_dataset_content](#delete_dataset_content)
    - [delete_datastore](#delete_datastore)
    - [delete_pipeline](#delete_pipeline)
    - [describe_channel](#describe_channel)
    - [describe_dataset](#describe_dataset)
    - [describe_datastore](#describe_datastore)
    - [describe_logging_options](#describe_logging_options)
    - [describe_pipeline](#describe_pipeline)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_dataset_content](#get_dataset_content)
    - [list_channels](#list_channels)
    - [list_dataset_contents](#list_dataset_contents)
    - [list_datasets](#list_datasets)
    - [list_datastores](#list_datastores)
    - [list_pipelines](#list_pipelines)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_logging_options](#put_logging_options)
    - [run_pipeline_activity](#run_pipeline_activity)
    - [sample_channel_data](#sample_channel_data)
    - [start_pipeline_reprocessing](#start_pipeline_reprocessing)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_channel](#update_channel)
    - [update_dataset](#update_dataset)
    - [update_datastore](#update_datastore)
    - [update_pipeline](#update_pipeline)
    - [get_paginator](#get_paginator)

## IoTAnalyticsClient

Type annotations for `boto3.client("iotanalytics")`

Can be used directly:

```python
from mypy_boto3_iotanalytics.client import IoTAnalyticsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotanalytics.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`


## Methods


### batch_put_message

Type annotations for `boto3.client("iotanalytics").batch_put_message` method.

[Client.batch_put_message documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.batch_put_message)

```python
def batch_put_message(
    self,
    channelName: str,
    messages: List[MessageTypeDef]
) -> BatchPutMessageResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("iotanalytics").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_pipeline_reprocessing

Type annotations for `boto3.client("iotanalytics").cancel_pipeline_reprocessing` method.

[Client.cancel_pipeline_reprocessing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.cancel_pipeline_reprocessing)

```python
def cancel_pipeline_reprocessing(
    self,
    pipelineName: str,
    reprocessingId: str
) -> Dict[str, Any]:
    pass
```

### create_channel

Type annotations for `boto3.client("iotanalytics").create_channel` method.

[Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.create_channel)

```python
def create_channel(
    self,
    channelName: str,
    channelStorage: "ChannelStorageTypeDef" = None,
    retentionPeriod: "RetentionPeriodTypeDef" = None,
    tags: List["TagTypeDef"] = None
) -> CreateChannelResponseTypeDef:
    pass
```

### create_dataset

Type annotations for `boto3.client("iotanalytics").create_dataset` method.

[Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset)

```python
def create_dataset(
    self,
    datasetName: str,
    actions: List["DatasetActionTypeDef"],
    triggers: List["DatasetTriggerTypeDef"] = None,
    contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
    retentionPeriod: "RetentionPeriodTypeDef" = None,
    versioningConfiguration: "VersioningConfigurationTypeDef" = None,
    tags: List["TagTypeDef"] = None,
    lateDataRules: List["LateDataRuleTypeDef"] = None
) -> CreateDatasetResponseTypeDef:
    pass
```

### create_dataset_content

Type annotations for `boto3.client("iotanalytics").create_dataset_content` method.

[Client.create_dataset_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset_content)

```python
def create_dataset_content(
    self,
    datasetName: str,
    versionId: str = None
) -> CreateDatasetContentResponseTypeDef:
    pass
```

### create_datastore

Type annotations for `boto3.client("iotanalytics").create_datastore` method.

[Client.create_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.create_datastore)

```python
def create_datastore(
    self,
    datastoreName: str,
    datastoreStorage: "DatastoreStorageTypeDef" = None,
    retentionPeriod: "RetentionPeriodTypeDef" = None,
    tags: List["TagTypeDef"] = None,
    fileFormatConfiguration: "FileFormatConfigurationTypeDef" = None
) -> CreateDatastoreResponseTypeDef:
    pass
```

### create_pipeline

Type annotations for `boto3.client("iotanalytics").create_pipeline` method.

[Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.create_pipeline)

```python
def create_pipeline(
    self,
    pipelineName: str,
    pipelineActivities: List["PipelineActivityTypeDef"],
    tags: List["TagTypeDef"] = None
) -> CreatePipelineResponseTypeDef:
    pass
```

### delete_channel

Type annotations for `boto3.client("iotanalytics").delete_channel` method.

[Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_channel)

```python
def delete_channel(
    self,
    channelName: str
) -> None:
    pass
```

### delete_dataset

Type annotations for `boto3.client("iotanalytics").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset)

```python
def delete_dataset(
    self,
    datasetName: str
) -> None:
    pass
```

### delete_dataset_content

Type annotations for `boto3.client("iotanalytics").delete_dataset_content` method.

[Client.delete_dataset_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset_content)

```python
def delete_dataset_content(
    self,
    datasetName: str,
    versionId: str = None
) -> None:
    pass
```

### delete_datastore

Type annotations for `boto3.client("iotanalytics").delete_datastore` method.

[Client.delete_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_datastore)

```python
def delete_datastore(
    self,
    datastoreName: str
) -> None:
    pass
```

### delete_pipeline

Type annotations for `boto3.client("iotanalytics").delete_pipeline` method.

[Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_pipeline)

```python
def delete_pipeline(
    self,
    pipelineName: str
) -> None:
    pass
```

### describe_channel

Type annotations for `boto3.client("iotanalytics").describe_channel` method.

[Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_channel)

```python
def describe_channel(
    self,
    channelName: str,
    includeStatistics: bool = None
) -> DescribeChannelResponseTypeDef:
    pass
```

### describe_dataset

Type annotations for `boto3.client("iotanalytics").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_dataset)

```python
def describe_dataset(
    self,
    datasetName: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_datastore

Type annotations for `boto3.client("iotanalytics").describe_datastore` method.

[Client.describe_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_datastore)

```python
def describe_datastore(
    self,
    datastoreName: str,
    includeStatistics: bool = None
) -> DescribeDatastoreResponseTypeDef:
    pass
```

### describe_logging_options

Type annotations for `boto3.client("iotanalytics").describe_logging_options` method.

[Client.describe_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_logging_options)

```python
def describe_logging_options(
    self
) -> DescribeLoggingOptionsResponseTypeDef:
    pass
```

### describe_pipeline

Type annotations for `boto3.client("iotanalytics").describe_pipeline` method.

[Client.describe_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_pipeline)

```python
def describe_pipeline(
    self,
    pipelineName: str
) -> DescribePipelineResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotanalytics").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_dataset_content

Type annotations for `boto3.client("iotanalytics").get_dataset_content` method.

[Client.get_dataset_content documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.get_dataset_content)

```python
def get_dataset_content(
    self,
    datasetName: str,
    versionId: str = None
) -> GetDatasetContentResponseTypeDef:
    pass
```

### list_channels

Type annotations for `boto3.client("iotanalytics").list_channels` method.

[Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.list_channels)

```python
def list_channels(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListChannelsResponseTypeDef:
    pass
```

### list_dataset_contents

Type annotations for `boto3.client("iotanalytics").list_dataset_contents` method.

[Client.list_dataset_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.list_dataset_contents)

```python
def list_dataset_contents(
    self,
    datasetName: str,
    nextToken: str = None,
    maxResults: int = None,
    scheduledOnOrAfter: datetime = None,
    scheduledBefore: datetime = None
) -> ListDatasetContentsResponseTypeDef:
    pass
```

### list_datasets

Type annotations for `boto3.client("iotanalytics").list_datasets` method.

[Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datasets)

```python
def list_datasets(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListDatasetsResponseTypeDef:
    pass
```

### list_datastores

Type annotations for `boto3.client("iotanalytics").list_datastores` method.

[Client.list_datastores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datastores)

```python
def list_datastores(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListDatastoresResponseTypeDef:
    pass
```

### list_pipelines

Type annotations for `boto3.client("iotanalytics").list_pipelines` method.

[Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.list_pipelines)

```python
def list_pipelines(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListPipelinesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotanalytics").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_logging_options

Type annotations for `boto3.client("iotanalytics").put_logging_options` method.

[Client.put_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.put_logging_options)

```python
def put_logging_options(
    self,
    loggingOptions: "LoggingOptionsTypeDef"
) -> None:
    pass
```

### run_pipeline_activity

Type annotations for `boto3.client("iotanalytics").run_pipeline_activity` method.

[Client.run_pipeline_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.run_pipeline_activity)

```python
def run_pipeline_activity(
    self,
    pipelineActivity: "PipelineActivityTypeDef",
    payloads: List[Union[bytes, IO[bytes]]]
) -> RunPipelineActivityResponseTypeDef:
    pass
```

### sample_channel_data

Type annotations for `boto3.client("iotanalytics").sample_channel_data` method.

[Client.sample_channel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.sample_channel_data)

```python
def sample_channel_data(
    self,
    channelName: str,
    maxMessages: int = None,
    startTime: datetime = None,
    endTime: datetime = None
) -> SampleChannelDataResponseTypeDef:
    pass
```

### start_pipeline_reprocessing

Type annotations for `boto3.client("iotanalytics").start_pipeline_reprocessing` method.

[Client.start_pipeline_reprocessing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.start_pipeline_reprocessing)

```python
def start_pipeline_reprocessing(
    self,
    pipelineName: str,
    startTime: datetime = None,
    endTime: datetime = None,
    channelMessages: ChannelMessagesTypeDef = None
) -> StartPipelineReprocessingResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotanalytics").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotanalytics").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_channel

Type annotations for `boto3.client("iotanalytics").update_channel` method.

[Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.update_channel)

```python
def update_channel(
    self,
    channelName: str,
    channelStorage: "ChannelStorageTypeDef" = None,
    retentionPeriod: "RetentionPeriodTypeDef" = None
) -> None:
    pass
```

### update_dataset

Type annotations for `boto3.client("iotanalytics").update_dataset` method.

[Client.update_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.update_dataset)

```python
def update_dataset(
    self,
    datasetName: str,
    actions: List["DatasetActionTypeDef"],
    triggers: List["DatasetTriggerTypeDef"] = None,
    contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
    retentionPeriod: "RetentionPeriodTypeDef" = None,
    versioningConfiguration: "VersioningConfigurationTypeDef" = None,
    lateDataRules: List["LateDataRuleTypeDef"] = None
) -> None:
    pass
```

### update_datastore

Type annotations for `boto3.client("iotanalytics").update_datastore` method.

[Client.update_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.update_datastore)

```python
def update_datastore(
    self,
    datastoreName: str,
    retentionPeriod: "RetentionPeriodTypeDef" = None,
    datastoreStorage: "DatastoreStorageTypeDef" = None,
    fileFormatConfiguration: "FileFormatConfigurationTypeDef" = None
) -> None:
    pass
```

### update_pipeline

Type annotations for `boto3.client("iotanalytics").update_pipeline` method.

[Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client.update_pipeline)

```python
def update_pipeline(
    self,
    pipelineName: str,
    pipelineActivities: List["PipelineActivityTypeDef"]
) -> None:
    pass
```



### get_paginator

Type annotations for `boto3.client("iotanalytics").get_paginator` method with overloads.

- `client.get_paginator("list_channels")` -> [ListChannelsPaginator](./paginators.md#listchannelspaginator)
- `client.get_paginator("list_dataset_contents")` -> [ListDatasetContentsPaginator](./paginators.md#listdatasetcontentspaginator)
- `client.get_paginator("list_datasets")` -> [ListDatasetsPaginator](./paginators.md#listdatasetspaginator)
- `client.get_paginator("list_datastores")` -> [ListDatastoresPaginator](./paginators.md#listdatastorespaginator)
- `client.get_paginator("list_pipelines")` -> [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)


