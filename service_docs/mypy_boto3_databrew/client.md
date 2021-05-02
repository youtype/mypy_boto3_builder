# GlueDataBrewClient for boto3 GlueDataBrew module

> [Index](../index.md) > [GlueDataBrew](./index.md) > GlueDataBrewClient

Auto-generated documentation for [GlueDataBrew](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew)
type annotations stubs module [mypy_boto3_databrew](https://pypi.org/project/mypy-boto3-databrew/).

- [GlueDataBrewClient for boto3 GlueDataBrew module](#gluedatabrewclient-for-boto3-gluedatabrew-module)
  - [GlueDataBrewClient](#gluedatabrewclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_delete_recipe_version](#batch_delete_recipe_version)
    - [can_paginate](#can_paginate)
    - [create_dataset](#create_dataset)
    - [create_profile_job](#create_profile_job)
    - [create_project](#create_project)
    - [create_recipe](#create_recipe)
    - [create_recipe_job](#create_recipe_job)
    - [create_schedule](#create_schedule)
    - [delete_dataset](#delete_dataset)
    - [delete_job](#delete_job)
    - [delete_project](#delete_project)
    - [delete_recipe_version](#delete_recipe_version)
    - [delete_schedule](#delete_schedule)
    - [describe_dataset](#describe_dataset)
    - [describe_job](#describe_job)
    - [describe_job_run](#describe_job_run)
    - [describe_project](#describe_project)
    - [describe_recipe](#describe_recipe)
    - [describe_schedule](#describe_schedule)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_datasets](#list_datasets)
    - [list_job_runs](#list_job_runs)
    - [list_jobs](#list_jobs)
    - [list_projects](#list_projects)
    - [list_recipe_versions](#list_recipe_versions)
    - [list_recipes](#list_recipes)
    - [list_schedules](#list_schedules)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [publish_recipe](#publish_recipe)
    - [send_project_session_action](#send_project_session_action)
    - [start_job_run](#start_job_run)
    - [start_project_session](#start_project_session)
    - [stop_job_run](#stop_job_run)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_dataset](#update_dataset)
    - [update_profile_job](#update_profile_job)
    - [update_project](#update_project)
    - [update_recipe](#update_recipe)
    - [update_recipe_job](#update_recipe_job)
    - [update_schedule](#update_schedule)
    - [get_paginator](#get_paginator)

## GlueDataBrewClient

Type annotations for `boto3.client("databrew")`

Can be used directly:

```python
from mypy_boto3_databrew.client import GlueDataBrewClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_databrew.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ValidationException`


## Methods


### batch_delete_recipe_version

Type annotations for `boto3.client("databrew").batch_delete_recipe_version` method.

[Client.batch_delete_recipe_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.batch_delete_recipe_version)

```python
def batch_delete_recipe_version(
    self,
    Name: str,
    RecipeVersions: List[str]
) -> BatchDeleteRecipeVersionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("databrew").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_dataset

Type annotations for `boto3.client("databrew").create_dataset` method.

[Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.create_dataset)

```python
def create_dataset(
    self,
    Name: str,
    Input: "InputTypeDef",
    Format: InputFormat = None,
    FormatOptions: "FormatOptionsTypeDef" = None,
    PathOptions: "PathOptionsTypeDef" = None,
    Tags: Dict[str, str] = None
) -> CreateDatasetResponseTypeDef:
    pass
```

### create_profile_job

Type annotations for `boto3.client("databrew").create_profile_job` method.

[Client.create_profile_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.create_profile_job)

```python
def create_profile_job(
    self,
    DatasetName: str,
    Name: str,
    OutputLocation: "S3LocationTypeDef",
    RoleArn: str,
    EncryptionKeyArn: str = None,
    EncryptionMode: EncryptionMode = None,
    LogSubscription: LogSubscription = None,
    MaxCapacity: int = None,
    MaxRetries: int = None,
    Tags: Dict[str, str] = None,
    Timeout: int = None,
    JobSample: "JobSampleTypeDef" = None
) -> CreateProfileJobResponseTypeDef:
    pass
```

### create_project

Type annotations for `boto3.client("databrew").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.create_project)

```python
def create_project(
    self,
    DatasetName: str,
    Name: str,
    RecipeName: str,
    RoleArn: str,
    Sample: "SampleTypeDef" = None,
    Tags: Dict[str, str] = None
) -> CreateProjectResponseTypeDef:
    pass
```

### create_recipe

Type annotations for `boto3.client("databrew").create_recipe` method.

[Client.create_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.create_recipe)

```python
def create_recipe(
    self,
    Name: str,
    Steps: List["RecipeStepTypeDef"],
    Description: str = None,
    Tags: Dict[str, str] = None
) -> CreateRecipeResponseTypeDef:
    pass
```

### create_recipe_job

Type annotations for `boto3.client("databrew").create_recipe_job` method.

[Client.create_recipe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.create_recipe_job)

```python
def create_recipe_job(
    self,
    Name: str,
    Outputs: List["OutputTypeDef"],
    RoleArn: str,
    DatasetName: str = None,
    EncryptionKeyArn: str = None,
    EncryptionMode: EncryptionMode = None,
    LogSubscription: LogSubscription = None,
    MaxCapacity: int = None,
    MaxRetries: int = None,
    ProjectName: str = None,
    RecipeReference: "RecipeReferenceTypeDef" = None,
    Tags: Dict[str, str] = None,
    Timeout: int = None
) -> CreateRecipeJobResponseTypeDef:
    pass
```

### create_schedule

Type annotations for `boto3.client("databrew").create_schedule` method.

[Client.create_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.create_schedule)

```python
def create_schedule(
    self,
    CronExpression: str,
    Name: str,
    JobNames: List[str] = None,
    Tags: Dict[str, str] = None
) -> CreateScheduleResponseTypeDef:
    pass
```

### delete_dataset

Type annotations for `boto3.client("databrew").delete_dataset` method.

[Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.delete_dataset)

```python
def delete_dataset(
    self,
    Name: str
) -> DeleteDatasetResponseTypeDef:
    pass
```

### delete_job

Type annotations for `boto3.client("databrew").delete_job` method.

[Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.delete_job)

```python
def delete_job(
    self,
    Name: str
) -> DeleteJobResponseTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("databrew").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.delete_project)

```python
def delete_project(
    self,
    Name: str
) -> DeleteProjectResponseTypeDef:
    pass
```

### delete_recipe_version

Type annotations for `boto3.client("databrew").delete_recipe_version` method.

[Client.delete_recipe_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.delete_recipe_version)

```python
def delete_recipe_version(
    self,
    Name: str,
    RecipeVersion: str
) -> DeleteRecipeVersionResponseTypeDef:
    pass
```

### delete_schedule

Type annotations for `boto3.client("databrew").delete_schedule` method.

[Client.delete_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.delete_schedule)

```python
def delete_schedule(
    self,
    Name: str
) -> DeleteScheduleResponseTypeDef:
    pass
```

### describe_dataset

Type annotations for `boto3.client("databrew").describe_dataset` method.

[Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_dataset)

```python
def describe_dataset(
    self,
    Name: str
) -> DescribeDatasetResponseTypeDef:
    pass
```

### describe_job

Type annotations for `boto3.client("databrew").describe_job` method.

[Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_job)

```python
def describe_job(
    self,
    Name: str
) -> DescribeJobResponseTypeDef:
    pass
```

### describe_job_run

Type annotations for `boto3.client("databrew").describe_job_run` method.

[Client.describe_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_job_run)

```python
def describe_job_run(
    self,
    Name: str,
    RunId: str
) -> DescribeJobRunResponseTypeDef:
    pass
```

### describe_project

Type annotations for `boto3.client("databrew").describe_project` method.

[Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_project)

```python
def describe_project(
    self,
    Name: str
) -> DescribeProjectResponseTypeDef:
    pass
```

### describe_recipe

Type annotations for `boto3.client("databrew").describe_recipe` method.

[Client.describe_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_recipe)

```python
def describe_recipe(
    self,
    Name: str,
    RecipeVersion: str = None
) -> DescribeRecipeResponseTypeDef:
    pass
```

### describe_schedule

Type annotations for `boto3.client("databrew").describe_schedule` method.

[Client.describe_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.describe_schedule)

```python
def describe_schedule(
    self,
    Name: str
) -> DescribeScheduleResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("databrew").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.generate_presigned_url)

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

### list_datasets

Type annotations for `boto3.client("databrew").list_datasets` method.

[Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_datasets)

```python
def list_datasets(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDatasetsResponseTypeDef:
    pass
```

### list_job_runs

Type annotations for `boto3.client("databrew").list_job_runs` method.

[Client.list_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_job_runs)

```python
def list_job_runs(
    self,
    Name: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListJobRunsResponseTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("databrew").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_jobs)

```python
def list_jobs(
    self,
    DatasetName: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    ProjectName: str = None
) -> ListJobsResponseTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("databrew").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_projects)

```python
def list_projects(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListProjectsResponseTypeDef:
    pass
```

### list_recipe_versions

Type annotations for `boto3.client("databrew").list_recipe_versions` method.

[Client.list_recipe_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_recipe_versions)

```python
def list_recipe_versions(
    self,
    Name: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListRecipeVersionsResponseTypeDef:
    pass
```

### list_recipes

Type annotations for `boto3.client("databrew").list_recipes` method.

[Client.list_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_recipes)

```python
def list_recipes(
    self,
    MaxResults: int = None,
    NextToken: str = None,
    RecipeVersion: str = None
) -> ListRecipesResponseTypeDef:
    pass
```

### list_schedules

Type annotations for `boto3.client("databrew").list_schedules` method.

[Client.list_schedules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_schedules)

```python
def list_schedules(
    self,
    JobName: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSchedulesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("databrew").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### publish_recipe

Type annotations for `boto3.client("databrew").publish_recipe` method.

[Client.publish_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.publish_recipe)

```python
def publish_recipe(
    self,
    Name: str,
    Description: str = None
) -> PublishRecipeResponseTypeDef:
    pass
```

### send_project_session_action

Type annotations for `boto3.client("databrew").send_project_session_action` method.

[Client.send_project_session_action documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.send_project_session_action)

```python
def send_project_session_action(
    self,
    Name: str,
    Preview: bool = None,
    RecipeStep: "RecipeStepTypeDef" = None,
    StepIndex: int = None,
    ClientSessionId: str = None,
    ViewFrame: ViewFrameTypeDef = None
) -> SendProjectSessionActionResponseTypeDef:
    pass
```

### start_job_run

Type annotations for `boto3.client("databrew").start_job_run` method.

[Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.start_job_run)

```python
def start_job_run(
    self,
    Name: str
) -> StartJobRunResponseTypeDef:
    pass
```

### start_project_session

Type annotations for `boto3.client("databrew").start_project_session` method.

[Client.start_project_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.start_project_session)

```python
def start_project_session(
    self,
    Name: str,
    AssumeControl: bool = None
) -> StartProjectSessionResponseTypeDef:
    pass
```

### stop_job_run

Type annotations for `boto3.client("databrew").stop_job_run` method.

[Client.stop_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.stop_job_run)

```python
def stop_job_run(
    self,
    Name: str,
    RunId: str
) -> StopJobRunResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("databrew").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("databrew").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_dataset

Type annotations for `boto3.client("databrew").update_dataset` method.

[Client.update_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.update_dataset)

```python
def update_dataset(
    self,
    Name: str,
    Input: "InputTypeDef",
    Format: InputFormat = None,
    FormatOptions: "FormatOptionsTypeDef" = None,
    PathOptions: "PathOptionsTypeDef" = None
) -> UpdateDatasetResponseTypeDef:
    pass
```

### update_profile_job

Type annotations for `boto3.client("databrew").update_profile_job` method.

[Client.update_profile_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.update_profile_job)

```python
def update_profile_job(
    self,
    Name: str,
    OutputLocation: "S3LocationTypeDef",
    RoleArn: str,
    EncryptionKeyArn: str = None,
    EncryptionMode: EncryptionMode = None,
    LogSubscription: LogSubscription = None,
    MaxCapacity: int = None,
    MaxRetries: int = None,
    Timeout: int = None,
    JobSample: "JobSampleTypeDef" = None
) -> UpdateProfileJobResponseTypeDef:
    pass
```

### update_project

Type annotations for `boto3.client("databrew").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.update_project)

```python
def update_project(
    self,
    RoleArn: str,
    Name: str,
    Sample: "SampleTypeDef" = None
) -> UpdateProjectResponseTypeDef:
    pass
```

### update_recipe

Type annotations for `boto3.client("databrew").update_recipe` method.

[Client.update_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.update_recipe)

```python
def update_recipe(
    self,
    Name: str,
    Description: str = None,
    Steps: List["RecipeStepTypeDef"] = None
) -> UpdateRecipeResponseTypeDef:
    pass
```

### update_recipe_job

Type annotations for `boto3.client("databrew").update_recipe_job` method.

[Client.update_recipe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.update_recipe_job)

```python
def update_recipe_job(
    self,
    Name: str,
    Outputs: List["OutputTypeDef"],
    RoleArn: str,
    EncryptionKeyArn: str = None,
    EncryptionMode: EncryptionMode = None,
    LogSubscription: LogSubscription = None,
    MaxCapacity: int = None,
    MaxRetries: int = None,
    Timeout: int = None
) -> UpdateRecipeJobResponseTypeDef:
    pass
```

### update_schedule

Type annotations for `boto3.client("databrew").update_schedule` method.

[Client.update_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html#GlueDataBrew.Client.update_schedule)

```python
def update_schedule(
    self,
    CronExpression: str,
    Name: str,
    JobNames: List[str] = None
) -> UpdateScheduleResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("databrew").get_paginator` method with overloads.

- `client.get_paginator("list_datasets")` -> [ListDatasetsPaginator](./paginators.md#listdatasetspaginator)
- `client.get_paginator("list_job_runs")` -> [ListJobRunsPaginator](./paginators.md#listjobrunspaginator)
- `client.get_paginator("list_jobs")` -> [ListJobsPaginator](./paginators.md#listjobspaginator)
- `client.get_paginator("list_projects")` -> [ListProjectsPaginator](./paginators.md#listprojectspaginator)
- `client.get_paginator("list_recipe_versions")` -> [ListRecipeVersionsPaginator](./paginators.md#listrecipeversionspaginator)
- `client.get_paginator("list_recipes")` -> [ListRecipesPaginator](./paginators.md#listrecipespaginator)
- `client.get_paginator("list_schedules")` -> [ListSchedulesPaginator](./paginators.md#listschedulespaginator)


