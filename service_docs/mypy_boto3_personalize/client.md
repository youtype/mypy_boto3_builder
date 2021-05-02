# PersonalizeClient for boto3 Personalize module

> [Index](../index.md) > [Personalize](./index.md) > PersonalizeClient

Auto-generated documentation for [Personalize](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize)
type annotations stubs module [mypy_boto3_personalize](https://pypi.org/project/mypy-boto3-personalize/).

- [PersonalizeClient for boto3 Personalize module](#personalizeclient-for-boto3-personalize-module)
  - [PersonalizeClient](#personalizeclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_batch_inference_job](#create_batch_inference_job)
    - [create_campaign](#create_campaign)
    - [create_dataset](#create_dataset)
    - [create_dataset_export_job](#create_dataset_export_job)
    - [create_dataset_group](#create_dataset_group)
    - [create_dataset_import_job](#create_dataset_import_job)
    - [create_event_tracker](#create_event_tracker)
    - [create_filter](#create_filter)
    - [create_schema](#create_schema)
    - [create_solution](#create_solution)
    - [create_solution_version](#create_solution_version)
    - [delete_campaign](#delete_campaign)
    - [delete_dataset](#delete_dataset)
    - [delete_dataset_group](#delete_dataset_group)
    - [delete_event_tracker](#delete_event_tracker)
    - [delete_filter](#delete_filter)
    - [delete_schema](#delete_schema)
    - [delete_solution](#delete_solution)
    - [describe_algorithm](#describe_algorithm)
    - [describe_batch_inference_job](#describe_batch_inference_job)
    - [describe_campaign](#describe_campaign)
    - [describe_dataset](#describe_dataset)
    - [describe_dataset_export_job](#describe_dataset_export_job)
    - [describe_dataset_group](#describe_dataset_group)
    - [describe_dataset_import_job](#describe_dataset_import_job)
    - [describe_event_tracker](#describe_event_tracker)
    - [describe_feature_transformation](#describe_feature_transformation)
    - [describe_filter](#describe_filter)
    - [describe_recipe](#describe_recipe)
    - [describe_schema](#describe_schema)
    - [describe_solution](#describe_solution)
    - [describe_solution_version](#describe_solution_version)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_solution_metrics](#get_solution_metrics)
    - [list_batch_inference_jobs](#list_batch_inference_jobs)
    - [list_campaigns](#list_campaigns)
    - [list_dataset_export_jobs](#list_dataset_export_jobs)
    - [list_dataset_groups](#list_dataset_groups)
    - [list_dataset_import_jobs](#list_dataset_import_jobs)
    - [list_datasets](#list_datasets)
    - [list_event_trackers](#list_event_trackers)
    - [list_filters](#list_filters)
    - [list_recipes](#list_recipes)
    - [list_schemas](#list_schemas)
    - [list_solution_versions](#list_solution_versions)
    - [list_solutions](#list_solutions)
    - [update_campaign](#update_campaign)
    - [get_paginator](#get_paginator)

## PersonalizeClient

Type annotations for `boto3.client("personalize")`

Can be used directly:

```python
from mypy_boto3_personalize.client import PersonalizeClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_personalize.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("personalize").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_batch_inference_job

Type annotations for `boto3.client("personalize").create_batch_inference_job` method.

[Client.create_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_batch_inference_job)

```python
def create_batch_inference_job(
    self,
    jobName: str,
    solutionVersionArn: str,
    jobInput: "BatchInferenceJobInputTypeDef",
    jobOutput: "BatchInferenceJobOutputTypeDef",
    roleArn: str,
    filterArn: str = None,
    numResults: int = None,
    batchInferenceJobConfig: "BatchInferenceJobConfigTypeDef" = None
) -> CreateBatchInferenceJobResponseTypeDef:
    pass
```

### create_campaign

Type annotations for `boto3.client("personalize").create_campaign` method.

[Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_campaign)

```python
def create_campaign(
    self,
    name: str,
    solutionVersionArn: str,
    minProvisionedTPS: int,
    campaignConfig: "CampaignConfigTypeDef" = None
) -> CreateCampaignResponseTypeDef:
    pass
```

### create_dataset

Type annotations for `boto3.client("personalize").create_dataset` method.

[Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_dataset)

```python
def create_dataset(
    self,
    name: str,
    schemaArn: str,
    datasetGroupArn: str,
    datasetType: str
) -> CreateDatasetResponseTypeDef:
    pass
```

### create_dataset_export_job

Type annotations for `boto3.client("personalize").create_dataset_export_job` method.

[Client.create_dataset_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_dataset_export_job)

```python
def create_dataset_export_job(
    self,
    jobName: str,
    datasetArn: str,
    roleArn: str,
    jobOutput: "DatasetExportJobOutputTypeDef",
    ingestionMode: IngestionMode = None
) -> CreateDatasetExportJobResponseTypeDef:
    pass
```

### create_dataset_group

Type annotations for `boto3.client("personalize").create_dataset_group` method.

[Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_dataset_group)

```python
def create_dataset_group(
    self,
    name: str,
    roleArn: str = None,
    kmsKeyArn: str = None
) -> CreateDatasetGroupResponseTypeDef:
    pass
```

### create_dataset_import_job

Type annotations for `boto3.client("personalize").create_dataset_import_job` method.

[Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_dataset_import_job)

```python
def create_dataset_import_job(
    self,
    jobName: str,
    datasetArn: str,
    dataSource: "DataSourceTypeDef",
    roleArn: str
) -> CreateDatasetImportJobResponseTypeDef:
    pass
```

### create_event_tracker

Type annotations for `boto3.client("personalize").create_event_tracker` method.

[Client.create_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_event_tracker)

```python
def create_event_tracker(
    self,
    name: str,
    datasetGroupArn: str
) -> CreateEventTrackerResponseTypeDef:
    pass
```

### create_filter

Type annotations for `boto3.client("personalize").create_filter` method.

[Client.create_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_filter)

```python
def create_filter(
    self,
    name: str,
    datasetGroupArn: str,
    filterExpression: str
) -> CreateFilterResponseTypeDef:
    pass
```

### create_schema

Type annotations for `boto3.client("personalize").create_schema` method.

[Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_schema)

```python
def create_schema(
    self,
    name: str,
    schema: str
) -> CreateSchemaResponseTypeDef:
    pass
```

### create_solution

Type annotations for `boto3.client("personalize").create_solution` method.

[Client.create_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_solution)

```python
def create_solution(
    self,
    name: str,
    datasetGroupArn: str,
    performHPO: bool = None,
    performAutoML: bool = None,
    recipeArn: str = None,
    eventType: str = None,
    solutionConfig: "SolutionConfigTypeDef" = None
) -> CreateSolutionResponseTypeDef:
    pass
```

### create_solution_version

Type annotations for `boto3.client("personalize").create_solution_version` method.

[Client.create_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.create_solution_version)

```python
def create_solution_version(
    self,
    solutionArn: str,
    trainingMode: TrainingMode = None
) -> CreateSolutionVersionResponseTypeDef:
    pass
```

### delete_campaign

Type annotations for `boto3.client("personalize").delete_campaign` method.

[Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_campaign)

```python
def delete_campaign(
    self,
    campaignArn: str
) -> None:
    pass
```

### delete_dataset

Type annotations for `boto3.client("personalize").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_dataset)

```python
def delete_dataset(
    self,
    datasetArn: str
) -> None:
    pass
```

### delete_dataset_group

Type annotations for `boto3.client("personalize").delete_dataset_group` method.

[Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_dataset_group)

```python
def delete_dataset_group(
    self,
    datasetGroupArn: str
) -> None:
    pass
```

### delete_event_tracker

Type annotations for `boto3.client("personalize").delete_event_tracker` method.

[Client.delete_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_event_tracker)

```python
def delete_event_tracker(
    self,
    eventTrackerArn: str
) -> None:
    pass
```

### delete_filter

Type annotations for `boto3.client("personalize").delete_filter` method.

[Client.delete_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_filter)

```python
def delete_filter(
    self,
    filterArn: str
) -> None:
    pass
```

### delete_schema

Type annotations for `boto3.client("personalize").delete_schema` method.

[Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_schema)

```python
def delete_schema(
    self,
    schemaArn: str
) -> None:
    pass
```

### delete_solution

Type annotations for `boto3.client("personalize").delete_solution` method.

[Client.delete_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.delete_solution)

```python
def delete_solution(
    self,
    solutionArn: str
) -> None:
    pass
```

### describe_algorithm

Type annotations for `boto3.client("personalize").describe_algorithm` method.

[Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_algorithm)

```python
def describe_algorithm(
    self,
    algorithmArn: str
) -> DescribeAlgorithmResponseTypeDef:
    pass
```

### describe_batch_inference_job

Type annotations for `boto3.client("personalize").describe_batch_inference_job` method.

[Client.describe_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_batch_inference_job)

```python
def describe_batch_inference_job(
    self,
    batchInferenceJobArn: str
) -> DescribeBatchInferenceJobResponseTypeDef:
    pass
```

### describe_campaign

Type annotations for `boto3.client("personalize").describe_campaign` method.

[Client.describe_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_campaign)

```python
def describe_campaign(
    self,
    campaignArn: str
) -> DescribeCampaignResponseTypeDef:
    pass
```

### describe_dataset

Type annotations for `boto3.client("personalize").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_dataset)

```python
def describe_dataset(
    self,
    datasetArn: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_dataset_export_job

Type annotations for `boto3.client("personalize").describe_dataset_export_job` method.

[Client.describe_dataset_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_dataset_export_job)

```python
def describe_dataset_export_job(
    self,
    datasetExportJobArn: str
) -> DescribeDatasetExportJobResponseTypeDef:
    pass
```

### describe_dataset_group

Type annotations for `boto3.client("personalize").describe_dataset_group` method.

[Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_dataset_group)

```python
def describe_dataset_group(
    self,
    datasetGroupArn: str
) -> DescribeDatasetGroupResponseTypeDef:
    pass
```

### describe_dataset_import_job

Type annotations for `boto3.client("personalize").describe_dataset_import_job` method.

[Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_dataset_import_job)

```python
def describe_dataset_import_job(
    self,
    datasetImportJobArn: str
) -> DescribeDatasetImportJobResponseTypeDef:
    pass
```

### describe_event_tracker

Type annotations for `boto3.client("personalize").describe_event_tracker` method.

[Client.describe_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_event_tracker)

```python
def describe_event_tracker(
    self,
    eventTrackerArn: str
) -> DescribeEventTrackerResponseTypeDef:
    pass
```

### describe_feature_transformation

Type annotations for `boto3.client("personalize").describe_feature_transformation` method.

[Client.describe_feature_transformation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_feature_transformation)

```python
def describe_feature_transformation(
    self,
    featureTransformationArn: str
) -> DescribeFeatureTransformationResponseTypeDef:
    pass
```

### describe_filter

Type annotations for `boto3.client("personalize").describe_filter` method.

[Client.describe_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_filter)

```python
def describe_filter(
    self,
    filterArn: str
) -> DescribeFilterResponseTypeDef:
    pass
```

### describe_recipe

Type annotations for `boto3.client("personalize").describe_recipe` method.

[Client.describe_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_recipe)

```python
def describe_recipe(
    self,
    recipeArn: str
) -> DescribeRecipeResponseTypeDef:
    pass
```

### describe_schema

Type annotations for `boto3.client("personalize").describe_schema` method.

[Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_schema)

```python
def describe_schema(
    self,
    schemaArn: str
) -> DescribeSchemaResponseTypeDef:
    pass
```

### describe_solution

Type annotations for `boto3.client("personalize").describe_solution` method.

[Client.describe_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_solution)

```python
def describe_solution(
    self,
    solutionArn: str
) -> DescribeSolutionResponseTypeDef:
    pass
```

### describe_solution_version

Type annotations for `boto3.client("personalize").describe_solution_version` method.

[Client.describe_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.describe_solution_version)

```python
def describe_solution_version(
    self,
    solutionVersionArn: str
) -> DescribeSolutionVersionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("personalize").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.generate_presigned_url)

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

### get_solution_metrics

Type annotations for `boto3.client("personalize").get_solution_metrics` method.

[Client.get_solution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.get_solution_metrics)

```python
def get_solution_metrics(
    self,
    solutionVersionArn: str
) -> GetSolutionMetricsResponseTypeDef:
    pass
```

### list_batch_inference_jobs

Type annotations for `boto3.client("personalize").list_batch_inference_jobs` method.

[Client.list_batch_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_batch_inference_jobs)

```python
def list_batch_inference_jobs(
    self,
    solutionVersionArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListBatchInferenceJobsResponseTypeDef:
    pass
```

### list_campaigns

Type annotations for `boto3.client("personalize").list_campaigns` method.

[Client.list_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_campaigns)

```python
def list_campaigns(
    self,
    solutionArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListCampaignsResponseTypeDef:
    pass
```

### list_dataset_export_jobs

Type annotations for `boto3.client("personalize").list_dataset_export_jobs` method.

[Client.list_dataset_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_dataset_export_jobs)

```python
def list_dataset_export_jobs(
    self,
    datasetArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListDatasetExportJobsResponseTypeDef:
    pass
```

### list_dataset_groups

Type annotations for `boto3.client("personalize").list_dataset_groups` method.

[Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_dataset_groups)

```python
def list_dataset_groups(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListDatasetGroupsResponseTypeDef:
    pass
```

### list_dataset_import_jobs

Type annotations for `boto3.client("personalize").list_dataset_import_jobs` method.

[Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_dataset_import_jobs)

```python
def list_dataset_import_jobs(
    self,
    datasetArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListDatasetImportJobsResponseTypeDef:
    pass
```

### list_datasets

Type annotations for `boto3.client("personalize").list_datasets` method.

[Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_datasets)

```python
def list_datasets(
    self,
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListDatasetsResponseTypeDef:
    pass
```

### list_event_trackers

Type annotations for `boto3.client("personalize").list_event_trackers` method.

[Client.list_event_trackers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_event_trackers)

```python
def list_event_trackers(
    self,
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListEventTrackersResponseTypeDef:
    pass
```

### list_filters

Type annotations for `boto3.client("personalize").list_filters` method.

[Client.list_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_filters)

```python
def list_filters(
    self,
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListFiltersResponseTypeDef:
    pass
```

### list_recipes

Type annotations for `boto3.client("personalize").list_recipes` method.

[Client.list_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_recipes)

```python
def list_recipes(
    self,
    recipeProvider: Literal['SERVICE'] = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListRecipesResponseTypeDef:
    pass
```

### list_schemas

Type annotations for `boto3.client("personalize").list_schemas` method.

[Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_schemas)

```python
def list_schemas(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListSchemasResponseTypeDef:
    pass
```

### list_solution_versions

Type annotations for `boto3.client("personalize").list_solution_versions` method.

[Client.list_solution_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_solution_versions)

```python
def list_solution_versions(
    self,
    solutionArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListSolutionVersionsResponseTypeDef:
    pass
```

### list_solutions

Type annotations for `boto3.client("personalize").list_solutions` method.

[Client.list_solutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.list_solutions)

```python
def list_solutions(
    self,
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListSolutionsResponseTypeDef:
    pass
```

### update_campaign

Type annotations for `boto3.client("personalize").update_campaign` method.

[Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html#Personalize.Client.update_campaign)

```python
def update_campaign(
    self,
    campaignArn: str,
    solutionVersionArn: str = None,
    minProvisionedTPS: int = None,
    campaignConfig: "CampaignConfigTypeDef" = None
) -> UpdateCampaignResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("personalize").get_paginator` method with overloads.

- `client.get_paginator("list_batch_inference_jobs")` -> [ListBatchInferenceJobsPaginator](./paginators.md#listbatchinferencejobspaginator)
- `client.get_paginator("list_campaigns")` -> [ListCampaignsPaginator](./paginators.md#listcampaignspaginator)
- `client.get_paginator("list_dataset_export_jobs")` -> [ListDatasetExportJobsPaginator](./paginators.md#listdatasetexportjobspaginator)
- `client.get_paginator("list_dataset_groups")` -> [ListDatasetGroupsPaginator](./paginators.md#listdatasetgroupspaginator)
- `client.get_paginator("list_dataset_import_jobs")` -> [ListDatasetImportJobsPaginator](./paginators.md#listdatasetimportjobspaginator)
- `client.get_paginator("list_datasets")` -> [ListDatasetsPaginator](./paginators.md#listdatasetspaginator)
- `client.get_paginator("list_event_trackers")` -> [ListEventTrackersPaginator](./paginators.md#listeventtrackerspaginator)
- `client.get_paginator("list_filters")` -> [ListFiltersPaginator](./paginators.md#listfilterspaginator)
- `client.get_paginator("list_recipes")` -> [ListRecipesPaginator](./paginators.md#listrecipespaginator)
- `client.get_paginator("list_schemas")` -> [ListSchemasPaginator](./paginators.md#listschemaspaginator)
- `client.get_paginator("list_solution_versions")` -> [ListSolutionVersionsPaginator](./paginators.md#listsolutionversionspaginator)
- `client.get_paginator("list_solutions")` -> [ListSolutionsPaginator](./paginators.md#listsolutionspaginator)


