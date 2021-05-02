# Literals for boto3 CodeBuild module

> [Index](../index.md) > [CodeBuild](./index.md) > Literals

Auto-generated documentation for [CodeBuild](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild)
type annotations stubs module [mypy_boto3_codebuild](https://pypi.org/project/mypy-boto3-codebuild/).

- [Literals for boto3 CodeBuild module](#literals-for-boto3-codebuild-module)
  - [ArtifactNamespace](#artifactnamespace)
  - [ArtifactPackaging](#artifactpackaging)
  - [ArtifactsType](#artifactstype)
  - [AuthType](#authtype)
  - [BucketOwnerAccess](#bucketowneraccess)
  - [BuildBatchPhaseType](#buildbatchphasetype)
  - [BuildPhaseType](#buildphasetype)
  - [CacheMode](#cachemode)
  - [CacheType](#cachetype)
  - [ComputeType](#computetype)
  - [CredentialProviderType](#credentialprovidertype)
  - [DescribeCodeCoveragesPaginatorName](#describecodecoveragespaginatorname)
  - [DescribeTestCasesPaginatorName](#describetestcasespaginatorname)
  - [EnvironmentType](#environmenttype)
  - [EnvironmentVariableType](#environmentvariabletype)
  - [FileSystemType](#filesystemtype)
  - [ImagePullCredentialsType](#imagepullcredentialstype)
  - [LanguageType](#languagetype)
  - [ListBuildBatchesForProjectPaginatorName](#listbuildbatchesforprojectpaginatorname)
  - [ListBuildBatchesPaginatorName](#listbuildbatchespaginatorname)
  - [ListBuildsForProjectPaginatorName](#listbuildsforprojectpaginatorname)
  - [ListBuildsPaginatorName](#listbuildspaginatorname)
  - [ListProjectsPaginatorName](#listprojectspaginatorname)
  - [ListReportGroupsPaginatorName](#listreportgroupspaginatorname)
  - [ListReportsForReportGroupPaginatorName](#listreportsforreportgrouppaginatorname)
  - [ListReportsPaginatorName](#listreportspaginatorname)
  - [ListSharedProjectsPaginatorName](#listsharedprojectspaginatorname)
  - [ListSharedReportGroupsPaginatorName](#listsharedreportgroupspaginatorname)
  - [LogsConfigStatusType](#logsconfigstatustype)
  - [PlatformType](#platformtype)
  - [ProjectSortByType](#projectsortbytype)
  - [ReportCodeCoverageSortByType](#reportcodecoveragesortbytype)
  - [ReportExportConfigType](#reportexportconfigtype)
  - [ReportGroupSortByType](#reportgroupsortbytype)
  - [ReportGroupStatusType](#reportgroupstatustype)
  - [ReportGroupTrendFieldType](#reportgrouptrendfieldtype)
  - [ReportPackagingType](#reportpackagingtype)
  - [ReportStatusType](#reportstatustype)
  - [ReportType](#reporttype)
  - [RetryBuildBatchType](#retrybuildbatchtype)
  - [ServerType](#servertype)
  - [SharedResourceSortByType](#sharedresourcesortbytype)
  - [SortOrderType](#sortordertype)
  - [SourceAuthType](#sourceauthtype)
  - [SourceType](#sourcetype)
  - [StatusType](#statustype)
  - [WebhookBuildType](#webhookbuildtype)
  - [WebhookFilterType](#webhookfiltertype)

## ArtifactNamespace

```python
from mypy_boto3_codebuild.literals import ArtifactNamespace
```

Values:

- `BUILD_ID`
- `NONE`

## ArtifactPackaging

```python
from mypy_boto3_codebuild.literals import ArtifactPackaging
```

Values:

- `NONE`
- `ZIP`

## ArtifactsType

```python
from mypy_boto3_codebuild.literals import ArtifactsType
```

Values:

- `CODEPIPELINE`
- `NO_ARTIFACTS`
- `S3`

## AuthType

```python
from mypy_boto3_codebuild.literals import AuthType
```

Values:

- `BASIC_AUTH`
- `OAUTH`
- `PERSONAL_ACCESS_TOKEN`

## BucketOwnerAccess

```python
from mypy_boto3_codebuild.literals import BucketOwnerAccess
```

Values:

- `FULL`
- `NONE`
- `READ_ONLY`

## BuildBatchPhaseType

```python
from mypy_boto3_codebuild.literals import BuildBatchPhaseType
```

Values:

- `COMBINE_ARTIFACTS`
- `DOWNLOAD_BATCHSPEC`
- `FAILED`
- `IN_PROGRESS`
- `STOPPED`
- `SUBMITTED`
- `SUCCEEDED`

## BuildPhaseType

```python
from mypy_boto3_codebuild.literals import BuildPhaseType
```

Values:

- `BUILD`
- `COMPLETED`
- `DOWNLOAD_SOURCE`
- `FINALIZING`
- `INSTALL`
- `POST_BUILD`
- `PRE_BUILD`
- `PROVISIONING`
- `QUEUED`
- `SUBMITTED`
- `UPLOAD_ARTIFACTS`

## CacheMode

```python
from mypy_boto3_codebuild.literals import CacheMode
```

Values:

- `LOCAL_CUSTOM_CACHE`
- `LOCAL_DOCKER_LAYER_CACHE`
- `LOCAL_SOURCE_CACHE`

## CacheType

```python
from mypy_boto3_codebuild.literals import CacheType
```

Values:

- `LOCAL`
- `NO_CACHE`
- `S3`

## ComputeType

```python
from mypy_boto3_codebuild.literals import ComputeType
```

Values:

- `BUILD_GENERAL1_2XLARGE`
- `BUILD_GENERAL1_LARGE`
- `BUILD_GENERAL1_MEDIUM`
- `BUILD_GENERAL1_SMALL`

## CredentialProviderType

```python
from mypy_boto3_codebuild.literals import CredentialProviderType
```

Values:

- `SECRETS_MANAGER`

## DescribeCodeCoveragesPaginatorName

```python
from mypy_boto3_codebuild.literals import DescribeCodeCoveragesPaginatorName
```

Values:

- `describe_code_coverages`

## DescribeTestCasesPaginatorName

```python
from mypy_boto3_codebuild.literals import DescribeTestCasesPaginatorName
```

Values:

- `describe_test_cases`

## EnvironmentType

```python
from mypy_boto3_codebuild.literals import EnvironmentType
```

Values:

- `ARM_CONTAINER`
- `LINUX_CONTAINER`
- `LINUX_GPU_CONTAINER`
- `WINDOWS_CONTAINER`
- `WINDOWS_SERVER_2019_CONTAINER`

## EnvironmentVariableType

```python
from mypy_boto3_codebuild.literals import EnvironmentVariableType
```

Values:

- `PARAMETER_STORE`
- `PLAINTEXT`
- `SECRETS_MANAGER`

## FileSystemType

```python
from mypy_boto3_codebuild.literals import FileSystemType
```

Values:

- `EFS`

## ImagePullCredentialsType

```python
from mypy_boto3_codebuild.literals import ImagePullCredentialsType
```

Values:

- `CODEBUILD`
- `SERVICE_ROLE`

## LanguageType

```python
from mypy_boto3_codebuild.literals import LanguageType
```

Values:

- `ANDROID`
- `BASE`
- `DOCKER`
- `DOTNET`
- `GOLANG`
- `JAVA`
- `NODE_JS`
- `PHP`
- `PYTHON`
- `RUBY`

## ListBuildBatchesForProjectPaginatorName

```python
from mypy_boto3_codebuild.literals import ListBuildBatchesForProjectPaginatorName
```

Values:

- `list_build_batches_for_project`

## ListBuildBatchesPaginatorName

```python
from mypy_boto3_codebuild.literals import ListBuildBatchesPaginatorName
```

Values:

- `list_build_batches`

## ListBuildsForProjectPaginatorName

```python
from mypy_boto3_codebuild.literals import ListBuildsForProjectPaginatorName
```

Values:

- `list_builds_for_project`

## ListBuildsPaginatorName

```python
from mypy_boto3_codebuild.literals import ListBuildsPaginatorName
```

Values:

- `list_builds`

## ListProjectsPaginatorName

```python
from mypy_boto3_codebuild.literals import ListProjectsPaginatorName
```

Values:

- `list_projects`

## ListReportGroupsPaginatorName

```python
from mypy_boto3_codebuild.literals import ListReportGroupsPaginatorName
```

Values:

- `list_report_groups`

## ListReportsForReportGroupPaginatorName

```python
from mypy_boto3_codebuild.literals import ListReportsForReportGroupPaginatorName
```

Values:

- `list_reports_for_report_group`

## ListReportsPaginatorName

```python
from mypy_boto3_codebuild.literals import ListReportsPaginatorName
```

Values:

- `list_reports`

## ListSharedProjectsPaginatorName

```python
from mypy_boto3_codebuild.literals import ListSharedProjectsPaginatorName
```

Values:

- `list_shared_projects`

## ListSharedReportGroupsPaginatorName

```python
from mypy_boto3_codebuild.literals import ListSharedReportGroupsPaginatorName
```

Values:

- `list_shared_report_groups`

## LogsConfigStatusType

```python
from mypy_boto3_codebuild.literals import LogsConfigStatusType
```

Values:

- `DISABLED`
- `ENABLED`

## PlatformType

```python
from mypy_boto3_codebuild.literals import PlatformType
```

Values:

- `AMAZON_LINUX`
- `DEBIAN`
- `UBUNTU`
- `WINDOWS_SERVER`

## ProjectSortByType

```python
from mypy_boto3_codebuild.literals import ProjectSortByType
```

Values:

- `CREATED_TIME`
- `LAST_MODIFIED_TIME`
- `NAME`

## ReportCodeCoverageSortByType

```python
from mypy_boto3_codebuild.literals import ReportCodeCoverageSortByType
```

Values:

- `FILE_PATH`
- `LINE_COVERAGE_PERCENTAGE`

## ReportExportConfigType

```python
from mypy_boto3_codebuild.literals import ReportExportConfigType
```

Values:

- `NO_EXPORT`
- `S3`

## ReportGroupSortByType

```python
from mypy_boto3_codebuild.literals import ReportGroupSortByType
```

Values:

- `CREATED_TIME`
- `LAST_MODIFIED_TIME`
- `NAME`

## ReportGroupStatusType

```python
from mypy_boto3_codebuild.literals import ReportGroupStatusType
```

Values:

- `ACTIVE`
- `DELETING`

## ReportGroupTrendFieldType

```python
from mypy_boto3_codebuild.literals import ReportGroupTrendFieldType
```

Values:

- `BRANCH_COVERAGE`
- `BRANCHES_COVERED`
- `BRANCHES_MISSED`
- `DURATION`
- `LINE_COVERAGE`
- `LINES_COVERED`
- `LINES_MISSED`
- `PASS_RATE`
- `TOTAL`

## ReportPackagingType

```python
from mypy_boto3_codebuild.literals import ReportPackagingType
```

Values:

- `NONE`
- `ZIP`

## ReportStatusType

```python
from mypy_boto3_codebuild.literals import ReportStatusType
```

Values:

- `DELETING`
- `FAILED`
- `GENERATING`
- `INCOMPLETE`
- `SUCCEEDED`

## ReportType

```python
from mypy_boto3_codebuild.literals import ReportType
```

Values:

- `CODE_COVERAGE`
- `TEST`

## RetryBuildBatchType

```python
from mypy_boto3_codebuild.literals import RetryBuildBatchType
```

Values:

- `RETRY_ALL_BUILDS`
- `RETRY_FAILED_BUILDS`

## ServerType

```python
from mypy_boto3_codebuild.literals import ServerType
```

Values:

- `BITBUCKET`
- `GITHUB`
- `GITHUB_ENTERPRISE`

## SharedResourceSortByType

```python
from mypy_boto3_codebuild.literals import SharedResourceSortByType
```

Values:

- `ARN`
- `MODIFIED_TIME`

## SortOrderType

```python
from mypy_boto3_codebuild.literals import SortOrderType
```

Values:

- `ASCENDING`
- `DESCENDING`

## SourceAuthType

```python
from mypy_boto3_codebuild.literals import SourceAuthType
```

Values:

- `OAUTH`

## SourceType

```python
from mypy_boto3_codebuild.literals import SourceType
```

Values:

- `BITBUCKET`
- `CODECOMMIT`
- `CODEPIPELINE`
- `GITHUB`
- `GITHUB_ENTERPRISE`
- `NO_SOURCE`
- `S3`

## StatusType

```python
from mypy_boto3_codebuild.literals import StatusType
```

Values:

- `FAILED`
- `FAULT`
- `IN_PROGRESS`
- `STOPPED`
- `SUCCEEDED`
- `TIMED_OUT`

## WebhookBuildType

```python
from mypy_boto3_codebuild.literals import WebhookBuildType
```

Values:

- `BUILD`
- `BUILD_BATCH`

## WebhookFilterType

```python
from mypy_boto3_codebuild.literals import WebhookFilterType
```

Values:

- `ACTOR_ACCOUNT_ID`
- `BASE_REF`
- `COMMIT_MESSAGE`
- `EVENT`
- `FILE_PATH`
- `HEAD_REF`
