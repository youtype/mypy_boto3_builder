# CodeBuildClient for boto3 CodeBuild module

> [Index](../index.md) > [CodeBuild](./index.md) > CodeBuildClient

Auto-generated documentation for [CodeBuild](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild)
type annotations stubs module [mypy_boto3_codebuild](https://pypi.org/project/mypy-boto3-codebuild/).

- [CodeBuildClient for boto3 CodeBuild module](#codebuildclient-for-boto3-codebuild-module)
  - [CodeBuildClient](#codebuildclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_delete_builds](#batch_delete_builds)
    - [batch_get_build_batches](#batch_get_build_batches)
    - [batch_get_builds](#batch_get_builds)
    - [batch_get_projects](#batch_get_projects)
    - [batch_get_report_groups](#batch_get_report_groups)
    - [batch_get_reports](#batch_get_reports)
    - [can_paginate](#can_paginate)
    - [create_project](#create_project)
    - [create_report_group](#create_report_group)
    - [create_webhook](#create_webhook)
    - [delete_build_batch](#delete_build_batch)
    - [delete_project](#delete_project)
    - [delete_report](#delete_report)
    - [delete_report_group](#delete_report_group)
    - [delete_resource_policy](#delete_resource_policy)
    - [delete_source_credentials](#delete_source_credentials)
    - [delete_webhook](#delete_webhook)
    - [describe_code_coverages](#describe_code_coverages)
    - [describe_test_cases](#describe_test_cases)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_report_group_trend](#get_report_group_trend)
    - [get_resource_policy](#get_resource_policy)
    - [import_source_credentials](#import_source_credentials)
    - [invalidate_project_cache](#invalidate_project_cache)
    - [list_build_batches](#list_build_batches)
    - [list_build_batches_for_project](#list_build_batches_for_project)
    - [list_builds](#list_builds)
    - [list_builds_for_project](#list_builds_for_project)
    - [list_curated_environment_images](#list_curated_environment_images)
    - [list_projects](#list_projects)
    - [list_report_groups](#list_report_groups)
    - [list_reports](#list_reports)
    - [list_reports_for_report_group](#list_reports_for_report_group)
    - [list_shared_projects](#list_shared_projects)
    - [list_shared_report_groups](#list_shared_report_groups)
    - [list_source_credentials](#list_source_credentials)
    - [put_resource_policy](#put_resource_policy)
    - [retry_build](#retry_build)
    - [retry_build_batch](#retry_build_batch)
    - [start_build](#start_build)
    - [start_build_batch](#start_build_batch)
    - [stop_build](#stop_build)
    - [stop_build_batch](#stop_build_batch)
    - [update_project](#update_project)
    - [update_report_group](#update_report_group)
    - [update_webhook](#update_webhook)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)

## CodeBuildClient

Type annotations for `boto3.client("codebuild")`

Can be used directly:

```python
from mypy_boto3_codebuild.client import CodeBuildClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_codebuild.client import Exceptions

def handle_error(exc: Exceptions.AccountLimitExceededException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccountLimitExceededException`
- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.OAuthProviderException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`


## Methods


### batch_delete_builds

Type annotations for `boto3.client("codebuild").batch_delete_builds` method.

[Client.batch_delete_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)

```python
def batch_delete_builds(
    self,
    ids: List[str]
) -> BatchDeleteBuildsOutputTypeDef:
    pass
```

### batch_get_build_batches

Type annotations for `boto3.client("codebuild").batch_get_build_batches` method.

[Client.batch_get_build_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_get_build_batches)

```python
def batch_get_build_batches(
    self,
    ids: List[str]
) -> BatchGetBuildBatchesOutputTypeDef:
    pass
```

### batch_get_builds

Type annotations for `boto3.client("codebuild").batch_get_builds` method.

[Client.batch_get_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)

```python
def batch_get_builds(
    self,
    ids: List[str]
) -> BatchGetBuildsOutputTypeDef:
    pass
```

### batch_get_projects

Type annotations for `boto3.client("codebuild").batch_get_projects` method.

[Client.batch_get_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)

```python
def batch_get_projects(
    self,
    names: List[str]
) -> BatchGetProjectsOutputTypeDef:
    pass
```

### batch_get_report_groups

Type annotations for `boto3.client("codebuild").batch_get_report_groups` method.

[Client.batch_get_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)

```python
def batch_get_report_groups(
    self,
    reportGroupArns: List[str]
) -> BatchGetReportGroupsOutputTypeDef:
    pass
```

### batch_get_reports

Type annotations for `boto3.client("codebuild").batch_get_reports` method.

[Client.batch_get_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)

```python
def batch_get_reports(
    self,
    reportArns: List[str]
) -> BatchGetReportsOutputTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("codebuild").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_project

Type annotations for `boto3.client("codebuild").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.create_project)

```python
def create_project(
    self,
    name: str,
    source: "ProjectSourceTypeDef",
    artifacts: "ProjectArtifactsTypeDef",
    environment: "ProjectEnvironmentTypeDef",
    serviceRole: str,
    description: str = None,
    secondarySources: List["ProjectSourceTypeDef"] = None,
    sourceVersion: str = None,
    secondarySourceVersions: List["ProjectSourceVersionTypeDef"] = None,
    secondaryArtifacts: List["ProjectArtifactsTypeDef"] = None,
    cache: "ProjectCacheTypeDef" = None,
    timeoutInMinutes: int = None,
    queuedTimeoutInMinutes: int = None,
    encryptionKey: str = None,
    tags: List["TagTypeDef"] = None,
    vpcConfig: "VpcConfigTypeDef" = None,
    badgeEnabled: bool = None,
    logsConfig: "LogsConfigTypeDef" = None,
    fileSystemLocations: List["ProjectFileSystemLocationTypeDef"] = None,
    buildBatchConfig: "ProjectBuildBatchConfigTypeDef" = None,
    concurrentBuildLimit: int = None
) -> CreateProjectOutputTypeDef:
    pass
```

### create_report_group

Type annotations for `boto3.client("codebuild").create_report_group` method.

[Client.create_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.create_report_group)

```python
def create_report_group(
    self,
    name: str,
    type: ReportType,
    exportConfig: "ReportExportConfigTypeDef",
    tags: List["TagTypeDef"] = None
) -> CreateReportGroupOutputTypeDef:
    pass
```

### create_webhook

Type annotations for `boto3.client("codebuild").create_webhook` method.

[Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.create_webhook)

```python
def create_webhook(
    self,
    projectName: str,
    branchFilter: str = None,
    filterGroups: List[List["WebhookFilterTypeDef"]] = None,
    buildType: WebhookBuildType = None
) -> CreateWebhookOutputTypeDef:
    pass
```

### delete_build_batch

Type annotations for `boto3.client("codebuild").delete_build_batch` method.

[Client.delete_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_build_batch)

```python
def delete_build_batch(
    self,
    id: str
) -> DeleteBuildBatchOutputTypeDef:
    pass
```

### delete_project

Type annotations for `boto3.client("codebuild").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_project)

```python
def delete_project(
    self,
    name: str
) -> Dict[str, Any]:
    pass
```

### delete_report

Type annotations for `boto3.client("codebuild").delete_report` method.

[Client.delete_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_report)

```python
def delete_report(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_report_group

Type annotations for `boto3.client("codebuild").delete_report_group` method.

[Client.delete_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)

```python
def delete_report_group(
    self,
    arn: str,
    deleteReports: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_resource_policy

Type annotations for `boto3.client("codebuild").delete_resource_policy` method.

[Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_resource_policy)

```python
def delete_resource_policy(
    self,
    resourceArn: str
) -> Dict[str, Any]:
    pass
```

### delete_source_credentials

Type annotations for `boto3.client("codebuild").delete_source_credentials` method.

[Client.delete_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)

```python
def delete_source_credentials(
    self,
    arn: str
) -> DeleteSourceCredentialsOutputTypeDef:
    pass
```

### delete_webhook

Type annotations for `boto3.client("codebuild").delete_webhook` method.

[Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)

```python
def delete_webhook(
    self,
    projectName: str
) -> Dict[str, Any]:
    pass
```

### describe_code_coverages

Type annotations for `boto3.client("codebuild").describe_code_coverages` method.

[Client.describe_code_coverages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.describe_code_coverages)

```python
def describe_code_coverages(
    self,
    reportArn: str,
    nextToken: str = None,
    maxResults: int = None,
    sortOrder: SortOrderType = None,
    sortBy: ReportCodeCoverageSortByType = None,
    minLineCoveragePercentage: float = None,
    maxLineCoveragePercentage: float = None
) -> DescribeCodeCoveragesOutputTypeDef:
    pass
```

### describe_test_cases

Type annotations for `boto3.client("codebuild").describe_test_cases` method.

[Client.describe_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)

```python
def describe_test_cases(
    self,
    reportArn: str,
    nextToken: str = None,
    maxResults: int = None,
    filter: TestCaseFilterTypeDef = None
) -> DescribeTestCasesOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("codebuild").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)

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

### get_report_group_trend

Type annotations for `boto3.client("codebuild").get_report_group_trend` method.

[Client.get_report_group_trend documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.get_report_group_trend)

```python
def get_report_group_trend(
    self,
    reportGroupArn: str,
    trendField: ReportGroupTrendFieldType,
    numOfReports: int = None
) -> GetReportGroupTrendOutputTypeDef:
    pass
```

### get_resource_policy

Type annotations for `boto3.client("codebuild").get_resource_policy` method.

[Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.get_resource_policy)

```python
def get_resource_policy(
    self,
    resourceArn: str
) -> GetResourcePolicyOutputTypeDef:
    pass
```

### import_source_credentials

Type annotations for `boto3.client("codebuild").import_source_credentials` method.

[Client.import_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)

```python
def import_source_credentials(
    self,
    token: str,
    serverType: ServerType,
    authType: AuthType,
    username: str = None,
    shouldOverwrite: bool = None
) -> ImportSourceCredentialsOutputTypeDef:
    pass
```

### invalidate_project_cache

Type annotations for `boto3.client("codebuild").invalidate_project_cache` method.

[Client.invalidate_project_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)

```python
def invalidate_project_cache(
    self,
    projectName: str
) -> Dict[str, Any]:
    pass
```

### list_build_batches

Type annotations for `boto3.client("codebuild").list_build_batches` method.

[Client.list_build_batches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_build_batches)

```python
def list_build_batches(
    self,
    filter: BuildBatchFilterTypeDef = None,
    maxResults: int = None,
    sortOrder: SortOrderType = None,
    nextToken: str = None
) -> ListBuildBatchesOutputTypeDef:
    pass
```

### list_build_batches_for_project

Type annotations for `boto3.client("codebuild").list_build_batches_for_project` method.

[Client.list_build_batches_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_build_batches_for_project)

```python
def list_build_batches_for_project(
    self,
    projectName: str = None,
    filter: BuildBatchFilterTypeDef = None,
    maxResults: int = None,
    sortOrder: SortOrderType = None,
    nextToken: str = None
) -> ListBuildBatchesForProjectOutputTypeDef:
    pass
```

### list_builds

Type annotations for `boto3.client("codebuild").list_builds` method.

[Client.list_builds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_builds)

```python
def list_builds(
    self,
    sortOrder: SortOrderType = None,
    nextToken: str = None
) -> ListBuildsOutputTypeDef:
    pass
```

### list_builds_for_project

Type annotations for `boto3.client("codebuild").list_builds_for_project` method.

[Client.list_builds_for_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)

```python
def list_builds_for_project(
    self,
    projectName: str,
    sortOrder: SortOrderType = None,
    nextToken: str = None
) -> ListBuildsForProjectOutputTypeDef:
    pass
```

### list_curated_environment_images

Type annotations for `boto3.client("codebuild").list_curated_environment_images` method.

[Client.list_curated_environment_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)

```python
def list_curated_environment_images(
    self
) -> ListCuratedEnvironmentImagesOutputTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("codebuild").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_projects)

```python
def list_projects(
    self,
    sortBy: ProjectSortByType = None,
    sortOrder: SortOrderType = None,
    nextToken: str = None
) -> ListProjectsOutputTypeDef:
    pass
```

### list_report_groups

Type annotations for `boto3.client("codebuild").list_report_groups` method.

[Client.list_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)

```python
def list_report_groups(
    self,
    sortOrder: SortOrderType = None,
    sortBy: ReportGroupSortByType = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListReportGroupsOutputTypeDef:
    pass
```

### list_reports

Type annotations for `boto3.client("codebuild").list_reports` method.

[Client.list_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_reports)

```python
def list_reports(
    self,
    sortOrder: SortOrderType = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: ReportFilterTypeDef = None
) -> ListReportsOutputTypeDef:
    pass
```

### list_reports_for_report_group

Type annotations for `boto3.client("codebuild").list_reports_for_report_group` method.

[Client.list_reports_for_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)

```python
def list_reports_for_report_group(
    self,
    reportGroupArn: str,
    nextToken: str = None,
    sortOrder: SortOrderType = None,
    maxResults: int = None,
    filter: ReportFilterTypeDef = None
) -> ListReportsForReportGroupOutputTypeDef:
    pass
```

### list_shared_projects

Type annotations for `boto3.client("codebuild").list_shared_projects` method.

[Client.list_shared_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_shared_projects)

```python
def list_shared_projects(
    self,
    sortBy: SharedResourceSortByType = None,
    sortOrder: SortOrderType = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListSharedProjectsOutputTypeDef:
    pass
```

### list_shared_report_groups

Type annotations for `boto3.client("codebuild").list_shared_report_groups` method.

[Client.list_shared_report_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_shared_report_groups)

```python
def list_shared_report_groups(
    self,
    sortOrder: SortOrderType = None,
    sortBy: SharedResourceSortByType = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListSharedReportGroupsOutputTypeDef:
    pass
```

### list_source_credentials

Type annotations for `boto3.client("codebuild").list_source_credentials` method.

[Client.list_source_credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)

```python
def list_source_credentials(
    self
) -> ListSourceCredentialsOutputTypeDef:
    pass
```

### put_resource_policy

Type annotations for `boto3.client("codebuild").put_resource_policy` method.

[Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.put_resource_policy)

```python
def put_resource_policy(
    self,
    policy: str,
    resourceArn: str
) -> PutResourcePolicyOutputTypeDef:
    pass
```

### retry_build

Type annotations for `boto3.client("codebuild").retry_build` method.

[Client.retry_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.retry_build)

```python
def retry_build(
    self,
    id: str = None,
    idempotencyToken: str = None
) -> RetryBuildOutputTypeDef:
    pass
```

### retry_build_batch

Type annotations for `boto3.client("codebuild").retry_build_batch` method.

[Client.retry_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.retry_build_batch)

```python
def retry_build_batch(
    self,
    id: str = None,
    idempotencyToken: str = None,
    retryType: RetryBuildBatchType = None
) -> RetryBuildBatchOutputTypeDef:
    pass
```

### start_build

Type annotations for `boto3.client("codebuild").start_build` method.

[Client.start_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build)

```python
def start_build(
    self,
    projectName: str,
    secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
    secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
    sourceVersion: str = None,
    artifactsOverride: "ProjectArtifactsTypeDef" = None,
    secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
    environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
    sourceTypeOverride: SourceType = None,
    sourceLocationOverride: str = None,
    sourceAuthOverride: "SourceAuthTypeDef" = None,
    gitCloneDepthOverride: int = None,
    gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
    buildspecOverride: str = None,
    insecureSslOverride: bool = None,
    reportBuildStatusOverride: bool = None,
    buildStatusConfigOverride: "BuildStatusConfigTypeDef" = None,
    environmentTypeOverride: EnvironmentType = None,
    imageOverride: str = None,
    computeTypeOverride: ComputeType = None,
    certificateOverride: str = None,
    cacheOverride: "ProjectCacheTypeDef" = None,
    serviceRoleOverride: str = None,
    privilegedModeOverride: bool = None,
    timeoutInMinutesOverride: int = None,
    queuedTimeoutInMinutesOverride: int = None,
    encryptionKeyOverride: str = None,
    idempotencyToken: str = None,
    logsConfigOverride: "LogsConfigTypeDef" = None,
    registryCredentialOverride: "RegistryCredentialTypeDef" = None,
    imagePullCredentialsTypeOverride: ImagePullCredentialsType = None,
    debugSessionEnabled: bool = None
) -> StartBuildOutputTypeDef:
    pass
```

### start_build_batch

Type annotations for `boto3.client("codebuild").start_build_batch` method.

[Client.start_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build_batch)

```python
def start_build_batch(
    self,
    projectName: str,
    secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
    secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
    sourceVersion: str = None,
    artifactsOverride: "ProjectArtifactsTypeDef" = None,
    secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
    environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
    sourceTypeOverride: SourceType = None,
    sourceLocationOverride: str = None,
    sourceAuthOverride: "SourceAuthTypeDef" = None,
    gitCloneDepthOverride: int = None,
    gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
    buildspecOverride: str = None,
    insecureSslOverride: bool = None,
    reportBuildBatchStatusOverride: bool = None,
    environmentTypeOverride: EnvironmentType = None,
    imageOverride: str = None,
    computeTypeOverride: ComputeType = None,
    certificateOverride: str = None,
    cacheOverride: "ProjectCacheTypeDef" = None,
    serviceRoleOverride: str = None,
    privilegedModeOverride: bool = None,
    buildTimeoutInMinutesOverride: int = None,
    queuedTimeoutInMinutesOverride: int = None,
    encryptionKeyOverride: str = None,
    idempotencyToken: str = None,
    logsConfigOverride: "LogsConfigTypeDef" = None,
    registryCredentialOverride: "RegistryCredentialTypeDef" = None,
    imagePullCredentialsTypeOverride: ImagePullCredentialsType = None,
    buildBatchConfigOverride: "ProjectBuildBatchConfigTypeDef" = None,
    debugSessionEnabled: bool = None
) -> StartBuildBatchOutputTypeDef:
    pass
```

### stop_build

Type annotations for `boto3.client("codebuild").stop_build` method.

[Client.stop_build documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.stop_build)

```python
def stop_build(
    self,
    id: str
) -> StopBuildOutputTypeDef:
    pass
```

### stop_build_batch

Type annotations for `boto3.client("codebuild").stop_build_batch` method.

[Client.stop_build_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.stop_build_batch)

```python
def stop_build_batch(
    self,
    id: str
) -> StopBuildBatchOutputTypeDef:
    pass
```

### update_project

Type annotations for `boto3.client("codebuild").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.update_project)

```python
def update_project(
    self,
    name: str,
    description: str = None,
    source: "ProjectSourceTypeDef" = None,
    secondarySources: List["ProjectSourceTypeDef"] = None,
    sourceVersion: str = None,
    secondarySourceVersions: List["ProjectSourceVersionTypeDef"] = None,
    artifacts: "ProjectArtifactsTypeDef" = None,
    secondaryArtifacts: List["ProjectArtifactsTypeDef"] = None,
    cache: "ProjectCacheTypeDef" = None,
    environment: "ProjectEnvironmentTypeDef" = None,
    serviceRole: str = None,
    timeoutInMinutes: int = None,
    queuedTimeoutInMinutes: int = None,
    encryptionKey: str = None,
    tags: List["TagTypeDef"] = None,
    vpcConfig: "VpcConfigTypeDef" = None,
    badgeEnabled: bool = None,
    logsConfig: "LogsConfigTypeDef" = None,
    fileSystemLocations: List["ProjectFileSystemLocationTypeDef"] = None,
    buildBatchConfig: "ProjectBuildBatchConfigTypeDef" = None,
    concurrentBuildLimit: int = None
) -> UpdateProjectOutputTypeDef:
    pass
```

### update_report_group

Type annotations for `boto3.client("codebuild").update_report_group` method.

[Client.update_report_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.update_report_group)

```python
def update_report_group(
    self,
    arn: str,
    exportConfig: "ReportExportConfigTypeDef" = None,
    tags: List["TagTypeDef"] = None
) -> UpdateReportGroupOutputTypeDef:
    pass
```

### update_webhook

Type annotations for `boto3.client("codebuild").update_webhook` method.

[Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.update_webhook)

```python
def update_webhook(
    self,
    projectName: str,
    branchFilter: str = None,
    rotateSecret: bool = None,
    filterGroups: List[List["WebhookFilterTypeDef"]] = None,
    buildType: WebhookBuildType = None
) -> UpdateWebhookOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.DescribeCodeCoverages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.DescribeCodeCoverages)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeCodeCoveragesPaginatorName
) -> DescribeCodeCoveragesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.DescribeTestCases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.DescribeTestCases)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeTestCasesPaginatorName
) -> DescribeTestCasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListBuildBatches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatches)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBuildBatchesPaginatorName
) -> ListBuildBatchesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListBuildBatchesForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatchesForProject)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBuildBatchesForProjectPaginatorName
) -> ListBuildBatchesForProjectPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListBuilds documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBuildsPaginatorName
) -> ListBuildsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListBuildsForProject documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBuildsForProjectPaginatorName
) -> ListBuildsForProjectPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListProjectsPaginatorName
) -> ListProjectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListReportGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListReportGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListReportGroupsPaginatorName
) -> ListReportGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListReports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListReports)

```python
@overload
def get_paginator(
    self,
    operation_name: ListReportsPaginatorName
) -> ListReportsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListReportsForReportGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListReportsForReportGroup)

```python
@overload
def get_paginator(
    self,
    operation_name: ListReportsForReportGroupPaginatorName
) -> ListReportsForReportGroupPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListSharedProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedProjects)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSharedProjectsPaginatorName
) -> ListSharedProjectsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("codebuild").get_paginator` method.

[Paginator.ListSharedReportGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedReportGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: ListSharedReportGroupsPaginatorName
) -> ListSharedReportGroupsPaginator:
    pass
```