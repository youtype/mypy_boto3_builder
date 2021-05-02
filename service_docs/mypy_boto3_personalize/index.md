# Type annotations for boto3 Personalize module

> [Index](../index.md) > Personalize

Auto-generated documentation for [Personalize](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize)
type annotations stubs module [mypy_boto3_personalize](https://pypi.org/project/mypy-boto3-personalize/).

```bash
pip install mypy-boto3-personalize
```

- [Type annotations for boto3 Personalize module](#type-annotations-for-boto3-personalize-module)
  - [PersonalizeClient](#personalizeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## PersonalizeClient

Type annotations for  `boto3.client("personalize")` as [PersonalizeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_personalize.client import PersonalizeClient
```


PersonalizeClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_batch_inference_job](./client.md#create-batch-inference-job)
- [create_campaign](./client.md#create-campaign)
- [create_dataset](./client.md#create-dataset)
- [create_dataset_export_job](./client.md#create-dataset-export-job)
- [create_dataset_group](./client.md#create-dataset-group)
- [create_dataset_import_job](./client.md#create-dataset-import-job)
- [create_event_tracker](./client.md#create-event-tracker)
- [create_filter](./client.md#create-filter)
- [create_schema](./client.md#create-schema)
- [create_solution](./client.md#create-solution)
- [create_solution_version](./client.md#create-solution-version)
- [delete_campaign](./client.md#delete-campaign)
- [delete_dataset](./client.md#delete-dataset)
- [delete_dataset_group](./client.md#delete-dataset-group)
- [delete_event_tracker](./client.md#delete-event-tracker)
- [delete_filter](./client.md#delete-filter)
- [delete_schema](./client.md#delete-schema)
- [delete_solution](./client.md#delete-solution)
- [describe_algorithm](./client.md#describe-algorithm)
- [describe_batch_inference_job](./client.md#describe-batch-inference-job)
- [describe_campaign](./client.md#describe-campaign)
- [describe_dataset](./client.md#describe-dataset)
- [describe_dataset_export_job](./client.md#describe-dataset-export-job)
- [describe_dataset_group](./client.md#describe-dataset-group)
- [describe_dataset_import_job](./client.md#describe-dataset-import-job)
- [describe_event_tracker](./client.md#describe-event-tracker)
- [describe_feature_transformation](./client.md#describe-feature-transformation)
- [describe_filter](./client.md#describe-filter)
- [describe_recipe](./client.md#describe-recipe)
- [describe_schema](./client.md#describe-schema)
- [describe_solution](./client.md#describe-solution)
- [describe_solution_version](./client.md#describe-solution-version)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_solution_metrics](./client.md#get-solution-metrics)
- [list_batch_inference_jobs](./client.md#list-batch-inference-jobs)
- [list_campaigns](./client.md#list-campaigns)
- [list_dataset_export_jobs](./client.md#list-dataset-export-jobs)
- [list_dataset_groups](./client.md#list-dataset-groups)
- [list_dataset_import_jobs](./client.md#list-dataset-import-jobs)
- [list_datasets](./client.md#list-datasets)
- [list_event_trackers](./client.md#list-event-trackers)
- [list_filters](./client.md#list-filters)
- [list_recipes](./client.md#list-recipes)
- [list_schemas](./client.md#list-schemas)
- [list_solution_versions](./client.md#list-solution-versions)
- [list_solutions](./client.md#list-solutions)
- [update_campaign](./client.md#update-campaign)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InvalidInputException](./client.md#invalidinputexception)
- [InvalidNextTokenException](./client.md#invalidnexttokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("personalize").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_personalize.paginators import ListBatchInferenceJobsPaginator, ...
```

- [ListBatchInferenceJobsPaginator](./paginators.md#listbatchinferencejobspaginator)
- [ListCampaignsPaginator](./paginators.md#listcampaignspaginator)
- [ListDatasetExportJobsPaginator](./paginators.md#listdatasetexportjobspaginator)
- [ListDatasetGroupsPaginator](./paginators.md#listdatasetgroupspaginator)
- [ListDatasetImportJobsPaginator](./paginators.md#listdatasetimportjobspaginator)
- [ListDatasetsPaginator](./paginators.md#listdatasetspaginator)
- [ListEventTrackersPaginator](./paginators.md#listeventtrackerspaginator)
- [ListFiltersPaginator](./paginators.md#listfilterspaginator)
- [ListRecipesPaginator](./paginators.md#listrecipespaginator)
- [ListSchemasPaginator](./paginators.md#listschemaspaginator)
- [ListSolutionVersionsPaginator](./paginators.md#listsolutionversionspaginator)
- [ListSolutionsPaginator](./paginators.md#listsolutionspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_personalize.literals import IngestionMode, ...
```

- [IngestionMode](./literals.md#ingestionmode)
- [ListBatchInferenceJobsPaginatorName](./literals.md#listbatchinferencejobspaginatorname)
- [ListCampaignsPaginatorName](./literals.md#listcampaignspaginatorname)
- [ListDatasetExportJobsPaginatorName](./literals.md#listdatasetexportjobspaginatorname)
- [ListDatasetGroupsPaginatorName](./literals.md#listdatasetgroupspaginatorname)
- [ListDatasetImportJobsPaginatorName](./literals.md#listdatasetimportjobspaginatorname)
- [ListDatasetsPaginatorName](./literals.md#listdatasetspaginatorname)
- [ListEventTrackersPaginatorName](./literals.md#listeventtrackerspaginatorname)
- [ListFiltersPaginatorName](./literals.md#listfilterspaginatorname)
- [ListRecipesPaginatorName](./literals.md#listrecipespaginatorname)
- [ListSchemasPaginatorName](./literals.md#listschemaspaginatorname)
- [ListSolutionVersionsPaginatorName](./literals.md#listsolutionversionspaginatorname)
- [ListSolutionsPaginatorName](./literals.md#listsolutionspaginatorname)
- [RecipeProvider](./literals.md#recipeprovider)
- [TrainingMode](./literals.md#trainingmode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_personalize.type_defs import AlgorithmImageTypeDef, ...
```

- [AlgorithmImageTypeDef](./type_defs.md#algorithmimagetypedef)
- [AlgorithmTypeDef](./type_defs.md#algorithmtypedef)
- [AutoMLConfigTypeDef](./type_defs.md#automlconfigtypedef)
- [AutoMLResultTypeDef](./type_defs.md#automlresulttypedef)
- [BatchInferenceJobConfigTypeDef](./type_defs.md#batchinferencejobconfigtypedef)
- [BatchInferenceJobInputTypeDef](./type_defs.md#batchinferencejobinputtypedef)
- [BatchInferenceJobOutputTypeDef](./type_defs.md#batchinferencejoboutputtypedef)
- [BatchInferenceJobSummaryTypeDef](./type_defs.md#batchinferencejobsummarytypedef)
- [BatchInferenceJobTypeDef](./type_defs.md#batchinferencejobtypedef)
- [CampaignConfigTypeDef](./type_defs.md#campaignconfigtypedef)
- [CampaignSummaryTypeDef](./type_defs.md#campaignsummarytypedef)
- [CampaignTypeDef](./type_defs.md#campaigntypedef)
- [CampaignUpdateSummaryTypeDef](./type_defs.md#campaignupdatesummarytypedef)
- [CategoricalHyperParameterRangeTypeDef](./type_defs.md#categoricalhyperparameterrangetypedef)
- [ContinuousHyperParameterRangeTypeDef](./type_defs.md#continuoushyperparameterrangetypedef)
- [CreateBatchInferenceJobResponseTypeDef](./type_defs.md#createbatchinferencejobresponsetypedef)
- [CreateCampaignResponseTypeDef](./type_defs.md#createcampaignresponsetypedef)
- [CreateDatasetExportJobResponseTypeDef](./type_defs.md#createdatasetexportjobresponsetypedef)
- [CreateDatasetGroupResponseTypeDef](./type_defs.md#createdatasetgroupresponsetypedef)
- [CreateDatasetImportJobResponseTypeDef](./type_defs.md#createdatasetimportjobresponsetypedef)
- [CreateDatasetResponseTypeDef](./type_defs.md#createdatasetresponsetypedef)
- [CreateEventTrackerResponseTypeDef](./type_defs.md#createeventtrackerresponsetypedef)
- [CreateFilterResponseTypeDef](./type_defs.md#createfilterresponsetypedef)
- [CreateSchemaResponseTypeDef](./type_defs.md#createschemaresponsetypedef)
- [CreateSolutionResponseTypeDef](./type_defs.md#createsolutionresponsetypedef)
- [CreateSolutionVersionResponseTypeDef](./type_defs.md#createsolutionversionresponsetypedef)
- [DataSourceTypeDef](./type_defs.md#datasourcetypedef)
- [DatasetExportJobOutputTypeDef](./type_defs.md#datasetexportjoboutputtypedef)
- [DatasetExportJobSummaryTypeDef](./type_defs.md#datasetexportjobsummarytypedef)
- [DatasetExportJobTypeDef](./type_defs.md#datasetexportjobtypedef)
- [DatasetGroupSummaryTypeDef](./type_defs.md#datasetgroupsummarytypedef)
- [DatasetGroupTypeDef](./type_defs.md#datasetgrouptypedef)
- [DatasetImportJobSummaryTypeDef](./type_defs.md#datasetimportjobsummarytypedef)
- [DatasetImportJobTypeDef](./type_defs.md#datasetimportjobtypedef)
- [DatasetSchemaSummaryTypeDef](./type_defs.md#datasetschemasummarytypedef)
- [DatasetSchemaTypeDef](./type_defs.md#datasetschematypedef)
- [DatasetSummaryTypeDef](./type_defs.md#datasetsummarytypedef)
- [DatasetTypeDef](./type_defs.md#datasettypedef)
- [DefaultCategoricalHyperParameterRangeTypeDef](./type_defs.md#defaultcategoricalhyperparameterrangetypedef)
- [DefaultContinuousHyperParameterRangeTypeDef](./type_defs.md#defaultcontinuoushyperparameterrangetypedef)
- [DefaultHyperParameterRangesTypeDef](./type_defs.md#defaulthyperparameterrangestypedef)
- [DefaultIntegerHyperParameterRangeTypeDef](./type_defs.md#defaultintegerhyperparameterrangetypedef)
- [DescribeAlgorithmResponseTypeDef](./type_defs.md#describealgorithmresponsetypedef)
- [DescribeBatchInferenceJobResponseTypeDef](./type_defs.md#describebatchinferencejobresponsetypedef)
- [DescribeCampaignResponseTypeDef](./type_defs.md#describecampaignresponsetypedef)
- [DescribeDatasetExportJobResponseTypeDef](./type_defs.md#describedatasetexportjobresponsetypedef)
- [DescribeDatasetGroupResponseTypeDef](./type_defs.md#describedatasetgroupresponsetypedef)
- [DescribeDatasetImportJobResponseTypeDef](./type_defs.md#describedatasetimportjobresponsetypedef)
- [DescribeDatasetResponseTypeDef](./type_defs.md#describedatasetresponsetypedef)
- [DescribeEventTrackerResponseTypeDef](./type_defs.md#describeeventtrackerresponsetypedef)
- [DescribeFeatureTransformationResponseTypeDef](./type_defs.md#describefeaturetransformationresponsetypedef)
- [DescribeFilterResponseTypeDef](./type_defs.md#describefilterresponsetypedef)
- [DescribeRecipeResponseTypeDef](./type_defs.md#describereciperesponsetypedef)
- [DescribeSchemaResponseTypeDef](./type_defs.md#describeschemaresponsetypedef)
- [DescribeSolutionResponseTypeDef](./type_defs.md#describesolutionresponsetypedef)
- [DescribeSolutionVersionResponseTypeDef](./type_defs.md#describesolutionversionresponsetypedef)
- [EventTrackerSummaryTypeDef](./type_defs.md#eventtrackersummarytypedef)
- [EventTrackerTypeDef](./type_defs.md#eventtrackertypedef)
- [FeatureTransformationTypeDef](./type_defs.md#featuretransformationtypedef)
- [FilterSummaryTypeDef](./type_defs.md#filtersummarytypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetSolutionMetricsResponseTypeDef](./type_defs.md#getsolutionmetricsresponsetypedef)
- [HPOConfigTypeDef](./type_defs.md#hpoconfigtypedef)
- [HPOObjectiveTypeDef](./type_defs.md#hpoobjectivetypedef)
- [HPOResourceConfigTypeDef](./type_defs.md#hporesourceconfigtypedef)
- [HyperParameterRangesTypeDef](./type_defs.md#hyperparameterrangestypedef)
- [IntegerHyperParameterRangeTypeDef](./type_defs.md#integerhyperparameterrangetypedef)
- [ListBatchInferenceJobsResponseTypeDef](./type_defs.md#listbatchinferencejobsresponsetypedef)
- [ListCampaignsResponseTypeDef](./type_defs.md#listcampaignsresponsetypedef)
- [ListDatasetExportJobsResponseTypeDef](./type_defs.md#listdatasetexportjobsresponsetypedef)
- [ListDatasetGroupsResponseTypeDef](./type_defs.md#listdatasetgroupsresponsetypedef)
- [ListDatasetImportJobsResponseTypeDef](./type_defs.md#listdatasetimportjobsresponsetypedef)
- [ListDatasetsResponseTypeDef](./type_defs.md#listdatasetsresponsetypedef)
- [ListEventTrackersResponseTypeDef](./type_defs.md#listeventtrackersresponsetypedef)
- [ListFiltersResponseTypeDef](./type_defs.md#listfiltersresponsetypedef)
- [ListRecipesResponseTypeDef](./type_defs.md#listrecipesresponsetypedef)
- [ListSchemasResponseTypeDef](./type_defs.md#listschemasresponsetypedef)
- [ListSolutionVersionsResponseTypeDef](./type_defs.md#listsolutionversionsresponsetypedef)
- [ListSolutionsResponseTypeDef](./type_defs.md#listsolutionsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RecipeSummaryTypeDef](./type_defs.md#recipesummarytypedef)
- [RecipeTypeDef](./type_defs.md#recipetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3DataConfigTypeDef](./type_defs.md#s3dataconfigtypedef)
- [SolutionConfigTypeDef](./type_defs.md#solutionconfigtypedef)
- [SolutionSummaryTypeDef](./type_defs.md#solutionsummarytypedef)
- [SolutionTypeDef](./type_defs.md#solutiontypedef)
- [SolutionVersionSummaryTypeDef](./type_defs.md#solutionversionsummarytypedef)
- [SolutionVersionTypeDef](./type_defs.md#solutionversiontypedef)
- [TunedHPOParamsTypeDef](./type_defs.md#tunedhpoparamstypedef)
- [UpdateCampaignResponseTypeDef](./type_defs.md#updatecampaignresponsetypedef)
