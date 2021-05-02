# Type annotations for boto3 LookoutforVision module

> [Index](../index.md) > LookoutforVision

Auto-generated documentation for [LookoutforVision](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html#LookoutforVision)
type annotations stubs module [mypy_boto3_lookoutvision](https://pypi.org/project/mypy-boto3-lookoutvision/).

```bash
pip install mypy-boto3-lookoutvision
```

- [Type annotations for boto3 LookoutforVision module](#type-annotations-for-boto3-lookoutforvision-module)
  - [LookoutforVisionClient](#lookoutforvisionclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## LookoutforVisionClient

Type annotations for  `boto3.client("lookoutvision")` as [LookoutforVisionClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lookoutvision.client import LookoutforVisionClient
```


LookoutforVisionClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_dataset](./client.md#create-dataset)
- [create_model](./client.md#create-model)
- [create_project](./client.md#create-project)
- [delete_dataset](./client.md#delete-dataset)
- [delete_model](./client.md#delete-model)
- [delete_project](./client.md#delete-project)
- [describe_dataset](./client.md#describe-dataset)
- [describe_model](./client.md#describe-model)
- [describe_project](./client.md#describe-project)
- [detect_anomalies](./client.md#detect-anomalies)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_dataset_entries](./client.md#list-dataset-entries)
- [list_models](./client.md#list-models)
- [list_projects](./client.md#list-projects)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_model](./client.md#start-model)
- [stop_model](./client.md#stop-model)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_dataset_entries](./client.md#update-dataset-entries)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("lookoutvision").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_lookoutvision.paginators import ListDatasetEntriesPaginator, ...
```

- [ListDatasetEntriesPaginator](./paginators.md#listdatasetentriespaginator)
- [ListModelsPaginator](./paginators.md#listmodelspaginator)
- [ListProjectsPaginator](./paginators.md#listprojectspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lookoutvision.literals import DatasetStatus, ...
```

- [DatasetStatus](./literals.md#datasetstatus)
- [ListDatasetEntriesPaginatorName](./literals.md#listdatasetentriespaginatorname)
- [ListModelsPaginatorName](./literals.md#listmodelspaginatorname)
- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)
- [ModelHostingStatus](./literals.md#modelhostingstatus)
- [ModelStatus](./literals.md#modelstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lookoutvision.type_defs import CreateDatasetResponseTypeDef, ...
```

- [CreateDatasetResponseTypeDef](./type_defs.md#createdatasetresponsetypedef)
- [CreateModelResponseTypeDef](./type_defs.md#createmodelresponsetypedef)
- [CreateProjectResponseTypeDef](./type_defs.md#createprojectresponsetypedef)
- [DatasetDescriptionTypeDef](./type_defs.md#datasetdescriptiontypedef)
- [DatasetGroundTruthManifestTypeDef](./type_defs.md#datasetgroundtruthmanifesttypedef)
- [DatasetImageStatsTypeDef](./type_defs.md#datasetimagestatstypedef)
- [DatasetMetadataTypeDef](./type_defs.md#datasetmetadatatypedef)
- [DatasetSourceTypeDef](./type_defs.md#datasetsourcetypedef)
- [DeleteModelResponseTypeDef](./type_defs.md#deletemodelresponsetypedef)
- [DeleteProjectResponseTypeDef](./type_defs.md#deleteprojectresponsetypedef)
- [DescribeDatasetResponseTypeDef](./type_defs.md#describedatasetresponsetypedef)
- [DescribeModelResponseTypeDef](./type_defs.md#describemodelresponsetypedef)
- [DescribeProjectResponseTypeDef](./type_defs.md#describeprojectresponsetypedef)
- [DetectAnomaliesResponseTypeDef](./type_defs.md#detectanomaliesresponsetypedef)
- [DetectAnomalyResultTypeDef](./type_defs.md#detectanomalyresulttypedef)
- [ImageSourceTypeDef](./type_defs.md#imagesourcetypedef)
- [InputS3ObjectTypeDef](./type_defs.md#inputs3objecttypedef)
- [ListDatasetEntriesResponseTypeDef](./type_defs.md#listdatasetentriesresponsetypedef)
- [ListModelsResponseTypeDef](./type_defs.md#listmodelsresponsetypedef)
- [ListProjectsResponseTypeDef](./type_defs.md#listprojectsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ModelDescriptionTypeDef](./type_defs.md#modeldescriptiontypedef)
- [ModelMetadataTypeDef](./type_defs.md#modelmetadatatypedef)
- [ModelPerformanceTypeDef](./type_defs.md#modelperformancetypedef)
- [OutputConfigTypeDef](./type_defs.md#outputconfigtypedef)
- [OutputS3ObjectTypeDef](./type_defs.md#outputs3objecttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProjectDescriptionTypeDef](./type_defs.md#projectdescriptiontypedef)
- [ProjectMetadataTypeDef](./type_defs.md#projectmetadatatypedef)
- [S3LocationTypeDef](./type_defs.md#s3locationtypedef)
- [StartModelResponseTypeDef](./type_defs.md#startmodelresponsetypedef)
- [StopModelResponseTypeDef](./type_defs.md#stopmodelresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpdateDatasetEntriesResponseTypeDef](./type_defs.md#updatedatasetentriesresponsetypedef)
