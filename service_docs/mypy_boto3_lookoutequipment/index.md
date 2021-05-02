# Type annotations for boto3 LookoutEquipment module

> [Index](../index.md) > LookoutEquipment

Auto-generated documentation for [LookoutEquipment](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html#LookoutEquipment)
type annotations stubs module [mypy_boto3_lookoutequipment](https://pypi.org/project/mypy-boto3-lookoutequipment/).

```bash
pip install mypy-boto3-lookoutequipment
```

- [Type annotations for boto3 LookoutEquipment module](#type-annotations-for-boto3-lookoutequipment-module)
  - [LookoutEquipmentClient](#lookoutequipmentclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## LookoutEquipmentClient

Type annotations for  `boto3.client("lookoutequipment")` as [LookoutEquipmentClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lookoutequipment.client import LookoutEquipmentClient
```


LookoutEquipmentClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_dataset](./client.md#create-dataset)
- [create_inference_scheduler](./client.md#create-inference-scheduler)
- [create_model](./client.md#create-model)
- [delete_dataset](./client.md#delete-dataset)
- [delete_inference_scheduler](./client.md#delete-inference-scheduler)
- [delete_model](./client.md#delete-model)
- [describe_data_ingestion_job](./client.md#describe-data-ingestion-job)
- [describe_dataset](./client.md#describe-dataset)
- [describe_inference_scheduler](./client.md#describe-inference-scheduler)
- [describe_model](./client.md#describe-model)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_data_ingestion_jobs](./client.md#list-data-ingestion-jobs)
- [list_datasets](./client.md#list-datasets)
- [list_inference_executions](./client.md#list-inference-executions)
- [list_inference_schedulers](./client.md#list-inference-schedulers)
- [list_models](./client.md#list-models)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_data_ingestion_job](./client.md#start-data-ingestion-job)
- [start_inference_scheduler](./client.md#start-inference-scheduler)
- [stop_inference_scheduler](./client.md#stop-inference-scheduler)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_inference_scheduler](./client.md#update-inference-scheduler)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lookoutequipment.literals import DataUploadFrequency, ...
```

- [DataUploadFrequency](./literals.md#datauploadfrequency)
- [DatasetStatus](./literals.md#datasetstatus)
- [InferenceExecutionStatus](./literals.md#inferenceexecutionstatus)
- [InferenceSchedulerStatus](./literals.md#inferenceschedulerstatus)
- [IngestionJobStatus](./literals.md#ingestionjobstatus)
- [ModelStatus](./literals.md#modelstatus)
- [TargetSamplingRate](./literals.md#targetsamplingrate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lookoutequipment.type_defs import CreateDatasetResponseTypeDef, ...
```

- [CreateDatasetResponseTypeDef](./type_defs.md#createdatasetresponsetypedef)
- [CreateInferenceSchedulerResponseTypeDef](./type_defs.md#createinferenceschedulerresponsetypedef)
- [CreateModelResponseTypeDef](./type_defs.md#createmodelresponsetypedef)
- [DataIngestionJobSummaryTypeDef](./type_defs.md#dataingestionjobsummarytypedef)
- [DataPreProcessingConfigurationTypeDef](./type_defs.md#datapreprocessingconfigurationtypedef)
- [DatasetSchemaTypeDef](./type_defs.md#datasetschematypedef)
- [DatasetSummaryTypeDef](./type_defs.md#datasetsummarytypedef)
- [DescribeDataIngestionJobResponseTypeDef](./type_defs.md#describedataingestionjobresponsetypedef)
- [DescribeDatasetResponseTypeDef](./type_defs.md#describedatasetresponsetypedef)
- [DescribeInferenceSchedulerResponseTypeDef](./type_defs.md#describeinferenceschedulerresponsetypedef)
- [DescribeModelResponseTypeDef](./type_defs.md#describemodelresponsetypedef)
- [InferenceExecutionSummaryTypeDef](./type_defs.md#inferenceexecutionsummarytypedef)
- [InferenceInputConfigurationTypeDef](./type_defs.md#inferenceinputconfigurationtypedef)
- [InferenceInputNameConfigurationTypeDef](./type_defs.md#inferenceinputnameconfigurationtypedef)
- [InferenceOutputConfigurationTypeDef](./type_defs.md#inferenceoutputconfigurationtypedef)
- [InferenceS3InputConfigurationTypeDef](./type_defs.md#inferences3inputconfigurationtypedef)
- [InferenceS3OutputConfigurationTypeDef](./type_defs.md#inferences3outputconfigurationtypedef)
- [InferenceSchedulerSummaryTypeDef](./type_defs.md#inferenceschedulersummarytypedef)
- [IngestionInputConfigurationTypeDef](./type_defs.md#ingestioninputconfigurationtypedef)
- [IngestionS3InputConfigurationTypeDef](./type_defs.md#ingestions3inputconfigurationtypedef)
- [LabelsInputConfigurationTypeDef](./type_defs.md#labelsinputconfigurationtypedef)
- [LabelsS3InputConfigurationTypeDef](./type_defs.md#labelss3inputconfigurationtypedef)
- [ListDataIngestionJobsResponseTypeDef](./type_defs.md#listdataingestionjobsresponsetypedef)
- [ListDatasetsResponseTypeDef](./type_defs.md#listdatasetsresponsetypedef)
- [ListInferenceExecutionsResponseTypeDef](./type_defs.md#listinferenceexecutionsresponsetypedef)
- [ListInferenceSchedulersResponseTypeDef](./type_defs.md#listinferenceschedulersresponsetypedef)
- [ListModelsResponseTypeDef](./type_defs.md#listmodelsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ModelSummaryTypeDef](./type_defs.md#modelsummarytypedef)
- [S3ObjectTypeDef](./type_defs.md#s3objecttypedef)
- [StartDataIngestionJobResponseTypeDef](./type_defs.md#startdataingestionjobresponsetypedef)
- [StartInferenceSchedulerResponseTypeDef](./type_defs.md#startinferenceschedulerresponsetypedef)
- [StopInferenceSchedulerResponseTypeDef](./type_defs.md#stopinferenceschedulerresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
