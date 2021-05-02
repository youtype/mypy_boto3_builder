# Type annotations for boto3 ElasticTranscoder module

> [Index](../index.md) > ElasticTranscoder

Auto-generated documentation for [ElasticTranscoder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html#ElasticTranscoder)
type annotations stubs module [mypy_boto3_elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/).

```bash
pip install mypy-boto3-elastictranscoder
```

- [Type annotations for boto3 ElasticTranscoder module](#type-annotations-for-boto3-elastictranscoder-module)
  - [ElasticTranscoderClient](#elastictranscoderclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ElasticTranscoderClient

Type annotations for  `boto3.client("elastictranscoder")` as [ElasticTranscoderClient](./client.md)

Can be used directly:

```python
from mypy_boto3_elastictranscoder.client import ElasticTranscoderClient
```


ElasticTranscoderClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_job](./client.md#cancel-job)
- [create_job](./client.md#create-job)
- [create_pipeline](./client.md#create-pipeline)
- [create_preset](./client.md#create-preset)
- [delete_pipeline](./client.md#delete-pipeline)
- [delete_preset](./client.md#delete-preset)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [list_jobs_by_pipeline](./client.md#list-jobs-by-pipeline)
- [list_jobs_by_status](./client.md#list-jobs-by-status)
- [list_pipelines](./client.md#list-pipelines)
- [list_presets](./client.md#list-presets)
- [read_job](./client.md#read-job)
- [read_pipeline](./client.md#read-pipeline)
- [read_preset](./client.md#read-preset)
- [test_role](./client.md#test-role)
- [update_pipeline](./client.md#update-pipeline)
- [update_pipeline_notifications](./client.md#update-pipeline-notifications)
- [update_pipeline_status](./client.md#update-pipeline-status)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [IncompatibleVersionException](./client.md#incompatibleversionexception)
- [InternalServiceException](./client.md#internalserviceexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("elastictranscoder").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.paginators import ListJobsByPipelinePaginator, ...
```

- [ListJobsByPipelinePaginator](./paginators.md#listjobsbypipelinepaginator)
- [ListJobsByStatusPaginator](./paginators.md#listjobsbystatuspaginator)
- [ListPipelinesPaginator](./paginators.md#listpipelinespaginator)
- [ListPresetsPaginator](./paginators.md#listpresetspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("elastictranscoder").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.waiters import JobCompleteWaiter, ...
```

- [JobCompleteWaiter](./waiters.md#jobcompletewaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.literals import JobCompleteWaiterName, ...
```

- [JobCompleteWaiterName](./literals.md#jobcompletewaitername)
- [ListJobsByPipelinePaginatorName](./literals.md#listjobsbypipelinepaginatorname)
- [ListJobsByStatusPaginatorName](./literals.md#listjobsbystatuspaginatorname)
- [ListPipelinesPaginatorName](./literals.md#listpipelinespaginatorname)
- [ListPresetsPaginatorName](./literals.md#listpresetspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elastictranscoder.type_defs import ArtworkTypeDef, ...
```

- [ArtworkTypeDef](./type_defs.md#artworktypedef)
- [AudioCodecOptionsTypeDef](./type_defs.md#audiocodecoptionstypedef)
- [AudioParametersTypeDef](./type_defs.md#audioparameterstypedef)
- [CaptionFormatTypeDef](./type_defs.md#captionformattypedef)
- [CaptionSourceTypeDef](./type_defs.md#captionsourcetypedef)
- [CaptionsTypeDef](./type_defs.md#captionstypedef)
- [ClipTypeDef](./type_defs.md#cliptypedef)
- [CreateJobOutputTypeDef](./type_defs.md#createjoboutputtypedef)
- [CreateJobPlaylistTypeDef](./type_defs.md#createjobplaylisttypedef)
- [CreateJobResponseTypeDef](./type_defs.md#createjobresponsetypedef)
- [CreatePipelineResponseTypeDef](./type_defs.md#createpipelineresponsetypedef)
- [CreatePresetResponseTypeDef](./type_defs.md#createpresetresponsetypedef)
- [DetectedPropertiesTypeDef](./type_defs.md#detectedpropertiestypedef)
- [EncryptionTypeDef](./type_defs.md#encryptiontypedef)
- [HlsContentProtectionTypeDef](./type_defs.md#hlscontentprotectiontypedef)
- [InputCaptionsTypeDef](./type_defs.md#inputcaptionstypedef)
- [JobAlbumArtTypeDef](./type_defs.md#jobalbumarttypedef)
- [JobInputTypeDef](./type_defs.md#jobinputtypedef)
- [JobOutputTypeDef](./type_defs.md#joboutputtypedef)
- [JobTypeDef](./type_defs.md#jobtypedef)
- [JobWatermarkTypeDef](./type_defs.md#jobwatermarktypedef)
- [ListJobsByPipelineResponseTypeDef](./type_defs.md#listjobsbypipelineresponsetypedef)
- [ListJobsByStatusResponseTypeDef](./type_defs.md#listjobsbystatusresponsetypedef)
- [ListPipelinesResponseTypeDef](./type_defs.md#listpipelinesresponsetypedef)
- [ListPresetsResponseTypeDef](./type_defs.md#listpresetsresponsetypedef)
- [NotificationsTypeDef](./type_defs.md#notificationstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PermissionTypeDef](./type_defs.md#permissiontypedef)
- [PipelineOutputConfigTypeDef](./type_defs.md#pipelineoutputconfigtypedef)
- [PipelineTypeDef](./type_defs.md#pipelinetypedef)
- [PlayReadyDrmTypeDef](./type_defs.md#playreadydrmtypedef)
- [PlaylistTypeDef](./type_defs.md#playlisttypedef)
- [PresetTypeDef](./type_defs.md#presettypedef)
- [PresetWatermarkTypeDef](./type_defs.md#presetwatermarktypedef)
- [ReadJobResponseTypeDef](./type_defs.md#readjobresponsetypedef)
- [ReadPipelineResponseTypeDef](./type_defs.md#readpipelineresponsetypedef)
- [ReadPresetResponseTypeDef](./type_defs.md#readpresetresponsetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [TestRoleResponseTypeDef](./type_defs.md#testroleresponsetypedef)
- [ThumbnailsTypeDef](./type_defs.md#thumbnailstypedef)
- [TimeSpanTypeDef](./type_defs.md#timespantypedef)
- [TimingTypeDef](./type_defs.md#timingtypedef)
- [UpdatePipelineNotificationsResponseTypeDef](./type_defs.md#updatepipelinenotificationsresponsetypedef)
- [UpdatePipelineResponseTypeDef](./type_defs.md#updatepipelineresponsetypedef)
- [UpdatePipelineStatusResponseTypeDef](./type_defs.md#updatepipelinestatusresponsetypedef)
- [VideoParametersTypeDef](./type_defs.md#videoparameterstypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
- [WarningTypeDef](./type_defs.md#warningtypedef)
