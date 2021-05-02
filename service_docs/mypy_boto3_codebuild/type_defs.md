# Structures for boto3 CodeBuild module

> [Index](../index.md) > [CodeBuild](./index.md) > Structures

Auto-generated documentation for [CodeBuild](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild)
type annotations stubs module [mypy_boto3_codebuild](https://pypi.org/project/mypy-boto3-codebuild/).

- [Structures for boto3 CodeBuild module](#structures-for-boto3-codebuild-module)
  - [BatchRestrictionsTypeDef](#batchrestrictionstypedef)
  - [BuildArtifactsTypeDef](#buildartifactstypedef)
  - [BuildBatchPhaseTypeDef](#buildbatchphasetypedef)
  - [BuildBatchTypeDef](#buildbatchtypedef)
  - [BuildGroupTypeDef](#buildgrouptypedef)
  - [BuildNotDeletedTypeDef](#buildnotdeletedtypedef)
  - [BuildPhaseTypeDef](#buildphasetypedef)
  - [BuildStatusConfigTypeDef](#buildstatusconfigtypedef)
  - [BuildSummaryTypeDef](#buildsummarytypedef)
  - [BuildTypeDef](#buildtypedef)
  - [CloudWatchLogsConfigTypeDef](#cloudwatchlogsconfigtypedef)
  - [CodeCoverageReportSummaryTypeDef](#codecoveragereportsummarytypedef)
  - [CodeCoverageTypeDef](#codecoveragetypedef)
  - [DebugSessionTypeDef](#debugsessiontypedef)
  - [EnvironmentImageTypeDef](#environmentimagetypedef)
  - [EnvironmentLanguageTypeDef](#environmentlanguagetypedef)
  - [EnvironmentPlatformTypeDef](#environmentplatformtypedef)
  - [EnvironmentVariableTypeDef](#environmentvariabletypedef)
  - [ExportedEnvironmentVariableTypeDef](#exportedenvironmentvariabletypedef)
  - [GitSubmodulesConfigTypeDef](#gitsubmodulesconfigtypedef)
  - [LogsConfigTypeDef](#logsconfigtypedef)
  - [LogsLocationTypeDef](#logslocationtypedef)
  - [NetworkInterfaceTypeDef](#networkinterfacetypedef)
  - [PhaseContextTypeDef](#phasecontexttypedef)
  - [ProjectArtifactsTypeDef](#projectartifactstypedef)
  - [ProjectBadgeTypeDef](#projectbadgetypedef)
  - [ProjectBuildBatchConfigTypeDef](#projectbuildbatchconfigtypedef)
  - [ProjectCacheTypeDef](#projectcachetypedef)
  - [ProjectEnvironmentTypeDef](#projectenvironmenttypedef)
  - [ProjectFileSystemLocationTypeDef](#projectfilesystemlocationtypedef)
  - [ProjectSourceTypeDef](#projectsourcetypedef)
  - [ProjectSourceVersionTypeDef](#projectsourceversiontypedef)
  - [ProjectTypeDef](#projecttypedef)
  - [RegistryCredentialTypeDef](#registrycredentialtypedef)
  - [ReportExportConfigTypeDef](#reportexportconfigtypedef)
  - [ReportGroupTrendStatsTypeDef](#reportgrouptrendstatstypedef)
  - [ReportGroupTypeDef](#reportgrouptypedef)
  - [ReportTypeDef](#reporttypedef)
  - [ReportWithRawDataTypeDef](#reportwithrawdatatypedef)
  - [ResolvedArtifactTypeDef](#resolvedartifacttypedef)
  - [ResponseMetadata](#responsemetadata)
  - [S3LogsConfigTypeDef](#s3logsconfigtypedef)
  - [S3ReportExportConfigTypeDef](#s3reportexportconfigtypedef)
  - [SourceAuthTypeDef](#sourceauthtypedef)
  - [SourceCredentialsInfoTypeDef](#sourcecredentialsinfotypedef)
  - [TagTypeDef](#tagtypedef)
  - [TestCaseTypeDef](#testcasetypedef)
  - [TestReportSummaryTypeDef](#testreportsummarytypedef)
  - [VpcConfigTypeDef](#vpcconfigtypedef)
  - [WebhookFilterTypeDef](#webhookfiltertypedef)
  - [WebhookTypeDef](#webhooktypedef)
  - [BatchDeleteBuildsOutputTypeDef](#batchdeletebuildsoutputtypedef)
  - [BatchGetBuildBatchesOutputTypeDef](#batchgetbuildbatchesoutputtypedef)
  - [BatchGetBuildsOutputTypeDef](#batchgetbuildsoutputtypedef)
  - [BatchGetProjectsOutputTypeDef](#batchgetprojectsoutputtypedef)
  - [BatchGetReportGroupsOutputTypeDef](#batchgetreportgroupsoutputtypedef)
  - [BatchGetReportsOutputTypeDef](#batchgetreportsoutputtypedef)
  - [BuildBatchFilterTypeDef](#buildbatchfiltertypedef)
  - [CreateProjectOutputTypeDef](#createprojectoutputtypedef)
  - [CreateReportGroupOutputTypeDef](#createreportgroupoutputtypedef)
  - [CreateWebhookOutputTypeDef](#createwebhookoutputtypedef)
  - [DeleteBuildBatchOutputTypeDef](#deletebuildbatchoutputtypedef)
  - [DeleteSourceCredentialsOutputTypeDef](#deletesourcecredentialsoutputtypedef)
  - [DescribeCodeCoveragesOutputTypeDef](#describecodecoveragesoutputtypedef)
  - [DescribeTestCasesOutputTypeDef](#describetestcasesoutputtypedef)
  - [GetReportGroupTrendOutputTypeDef](#getreportgrouptrendoutputtypedef)
  - [GetResourcePolicyOutputTypeDef](#getresourcepolicyoutputtypedef)
  - [ImportSourceCredentialsOutputTypeDef](#importsourcecredentialsoutputtypedef)
  - [ListBuildBatchesForProjectOutputTypeDef](#listbuildbatchesforprojectoutputtypedef)
  - [ListBuildBatchesOutputTypeDef](#listbuildbatchesoutputtypedef)
  - [ListBuildsForProjectOutputTypeDef](#listbuildsforprojectoutputtypedef)
  - [ListBuildsOutputTypeDef](#listbuildsoutputtypedef)
  - [ListCuratedEnvironmentImagesOutputTypeDef](#listcuratedenvironmentimagesoutputtypedef)
  - [ListProjectsOutputTypeDef](#listprojectsoutputtypedef)
  - [ListReportGroupsOutputTypeDef](#listreportgroupsoutputtypedef)
  - [ListReportsForReportGroupOutputTypeDef](#listreportsforreportgroupoutputtypedef)
  - [ListReportsOutputTypeDef](#listreportsoutputtypedef)
  - [ListSharedProjectsOutputTypeDef](#listsharedprojectsoutputtypedef)
  - [ListSharedReportGroupsOutputTypeDef](#listsharedreportgroupsoutputtypedef)
  - [ListSourceCredentialsOutputTypeDef](#listsourcecredentialsoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutResourcePolicyOutputTypeDef](#putresourcepolicyoutputtypedef)
  - [ReportFilterTypeDef](#reportfiltertypedef)
  - [RetryBuildBatchOutputTypeDef](#retrybuildbatchoutputtypedef)
  - [RetryBuildOutputTypeDef](#retrybuildoutputtypedef)
  - [StartBuildBatchOutputTypeDef](#startbuildbatchoutputtypedef)
  - [StartBuildOutputTypeDef](#startbuildoutputtypedef)
  - [StopBuildBatchOutputTypeDef](#stopbuildbatchoutputtypedef)
  - [StopBuildOutputTypeDef](#stopbuildoutputtypedef)
  - [TestCaseFilterTypeDef](#testcasefiltertypedef)
  - [UpdateProjectOutputTypeDef](#updateprojectoutputtypedef)
  - [UpdateReportGroupOutputTypeDef](#updatereportgroupoutputtypedef)
  - [UpdateWebhookOutputTypeDef](#updatewebhookoutputtypedef)

## BatchRestrictionsTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchRestrictionsTypeDef
```




Optional fields:
- `maximumBuildsAllowed`: `int`
- `computeTypesAllowed`: `List[str]`


## BuildArtifactsTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildArtifactsTypeDef
```




Optional fields:
- `location`: `str`
- `sha256sum`: `str`
- `md5sum`: `str`
- `overrideArtifactName`: `bool`
- `encryptionDisabled`: `bool`
- `artifactIdentifier`: `str`
- `bucketOwnerAccess`: `BucketOwnerAccess`


## BuildBatchPhaseTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildBatchPhaseTypeDef
```




Optional fields:
- `phaseType`: `BuildBatchPhaseType`
- `phaseStatus`: `StatusType`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `durationInSeconds`: `int`
- `contexts`: `List["PhaseContextTypeDef"]`


## BuildBatchTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildBatchTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `currentPhase`: `str`
- `buildBatchStatus`: `StatusType`
- `sourceVersion`: `str`
- `resolvedSourceVersion`: `str`
- `projectName`: `str`
- `phases`: `List["BuildBatchPhaseTypeDef"]`
- `source`: `"ProjectSourceTypeDef"`
- `secondarySources`: `List["ProjectSourceTypeDef"]`
- `secondarySourceVersions`: `List["ProjectSourceVersionTypeDef"]`
- `artifacts`: `"BuildArtifactsTypeDef"`
- `secondaryArtifacts`: `List["BuildArtifactsTypeDef"]`
- `cache`: `"ProjectCacheTypeDef"`
- `environment`: `"ProjectEnvironmentTypeDef"`
- `serviceRole`: `str`
- `logConfig`: `"LogsConfigTypeDef"`
- `buildTimeoutInMinutes`: `int`
- `queuedTimeoutInMinutes`: `int`
- `complete`: `bool`
- `initiator`: `str`
- `vpcConfig`: `"VpcConfigTypeDef"`
- `encryptionKey`: `str`
- `buildBatchNumber`: `int`
- `fileSystemLocations`: `List["ProjectFileSystemLocationTypeDef"]`
- `buildBatchConfig`: `"ProjectBuildBatchConfigTypeDef"`
- `buildGroups`: `List["BuildGroupTypeDef"]`
- `debugSessionEnabled`: `bool`


## BuildGroupTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildGroupTypeDef
```




Optional fields:
- `identifier`: `str`
- `dependsOn`: `List[str]`
- `ignoreFailure`: `bool`
- `currentBuildSummary`: `"BuildSummaryTypeDef"`
- `priorBuildSummaryList`: `List["BuildSummaryTypeDef"]`


## BuildNotDeletedTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildNotDeletedTypeDef
```




Optional fields:
- `id`: `str`
- `statusCode`: `str`


## BuildPhaseTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildPhaseTypeDef
```




Optional fields:
- `phaseType`: `BuildPhaseType`
- `phaseStatus`: `StatusType`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `durationInSeconds`: `int`
- `contexts`: `List["PhaseContextTypeDef"]`


## BuildStatusConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildStatusConfigTypeDef
```




Optional fields:
- `context`: `str`
- `targetUrl`: `str`


## BuildSummaryTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `requestedOn`: `datetime`
- `buildStatus`: `StatusType`
- `primaryArtifact`: `"ResolvedArtifactTypeDef"`
- `secondaryArtifacts`: `List["ResolvedArtifactTypeDef"]`


## BuildTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `buildNumber`: `int`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `currentPhase`: `str`
- `buildStatus`: `StatusType`
- `sourceVersion`: `str`
- `resolvedSourceVersion`: `str`
- `projectName`: `str`
- `phases`: `List["BuildPhaseTypeDef"]`
- `source`: `"ProjectSourceTypeDef"`
- `secondarySources`: `List["ProjectSourceTypeDef"]`
- `secondarySourceVersions`: `List["ProjectSourceVersionTypeDef"]`
- `artifacts`: `"BuildArtifactsTypeDef"`
- `secondaryArtifacts`: `List["BuildArtifactsTypeDef"]`
- `cache`: `"ProjectCacheTypeDef"`
- `environment`: `"ProjectEnvironmentTypeDef"`
- `serviceRole`: `str`
- `logs`: `"LogsLocationTypeDef"`
- `timeoutInMinutes`: `int`
- `queuedTimeoutInMinutes`: `int`
- `buildComplete`: `bool`
- `initiator`: `str`
- `vpcConfig`: `"VpcConfigTypeDef"`
- `networkInterface`: `"NetworkInterfaceTypeDef"`
- `encryptionKey`: `str`
- `exportedEnvironmentVariables`: `List["ExportedEnvironmentVariableTypeDef"]`
- `reportArns`: `List[str]`
- `fileSystemLocations`: `List["ProjectFileSystemLocationTypeDef"]`
- `debugSession`: `"DebugSessionTypeDef"`
- `buildBatchArn`: `str`


## CloudWatchLogsConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import CloudWatchLogsConfigTypeDef
```


Required fields:
- `status`: `LogsConfigStatusType`



Optional fields:
- `groupName`: `str`
- `streamName`: `str`


## CodeCoverageReportSummaryTypeDef

```python
from mypy_boto3_codebuild.type_defs import CodeCoverageReportSummaryTypeDef
```




Optional fields:
- `lineCoveragePercentage`: `float`
- `linesCovered`: `int`
- `linesMissed`: `int`
- `branchCoveragePercentage`: `float`
- `branchesCovered`: `int`
- `branchesMissed`: `int`


## CodeCoverageTypeDef

```python
from mypy_boto3_codebuild.type_defs import CodeCoverageTypeDef
```




Optional fields:
- `id`: `str`
- `reportARN`: `str`
- `filePath`: `str`
- `lineCoveragePercentage`: `float`
- `linesCovered`: `int`
- `linesMissed`: `int`
- `branchCoveragePercentage`: `float`
- `branchesCovered`: `int`
- `branchesMissed`: `int`
- `expired`: `datetime`


## DebugSessionTypeDef

```python
from mypy_boto3_codebuild.type_defs import DebugSessionTypeDef
```




Optional fields:
- `sessionEnabled`: `bool`
- `sessionTarget`: `str`


## EnvironmentImageTypeDef

```python
from mypy_boto3_codebuild.type_defs import EnvironmentImageTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `versions`: `List[str]`


## EnvironmentLanguageTypeDef

```python
from mypy_boto3_codebuild.type_defs import EnvironmentLanguageTypeDef
```




Optional fields:
- `language`: `LanguageType`
- `images`: `List["EnvironmentImageTypeDef"]`


## EnvironmentPlatformTypeDef

```python
from mypy_boto3_codebuild.type_defs import EnvironmentPlatformTypeDef
```




Optional fields:
- `platform`: `PlatformType`
- `languages`: `List["EnvironmentLanguageTypeDef"]`


## EnvironmentVariableTypeDef

```python
from mypy_boto3_codebuild.type_defs import EnvironmentVariableTypeDef
```


Required fields:
- `name`: `str`
- `value`: `str`



Optional fields:
- `type`: `EnvironmentVariableType`


## ExportedEnvironmentVariableTypeDef

```python
from mypy_boto3_codebuild.type_defs import ExportedEnvironmentVariableTypeDef
```




Optional fields:
- `name`: `str`
- `value`: `str`


## GitSubmodulesConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import GitSubmodulesConfigTypeDef
```


Required fields:
- `fetchSubmodules`: `bool`




## LogsConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import LogsConfigTypeDef
```




Optional fields:
- `cloudWatchLogs`: `"CloudWatchLogsConfigTypeDef"`
- `s3Logs`: `"S3LogsConfigTypeDef"`


## LogsLocationTypeDef

```python
from mypy_boto3_codebuild.type_defs import LogsLocationTypeDef
```




Optional fields:
- `groupName`: `str`
- `streamName`: `str`
- `deepLink`: `str`
- `s3DeepLink`: `str`
- `cloudWatchLogsArn`: `str`
- `s3LogsArn`: `str`
- `cloudWatchLogs`: `"CloudWatchLogsConfigTypeDef"`
- `s3Logs`: `"S3LogsConfigTypeDef"`


## NetworkInterfaceTypeDef

```python
from mypy_boto3_codebuild.type_defs import NetworkInterfaceTypeDef
```




Optional fields:
- `subnetId`: `str`
- `networkInterfaceId`: `str`


## PhaseContextTypeDef

```python
from mypy_boto3_codebuild.type_defs import PhaseContextTypeDef
```




Optional fields:
- `statusCode`: `str`
- `message`: `str`


## ProjectArtifactsTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectArtifactsTypeDef
```


Required fields:
- `type`: `ArtifactsType`



Optional fields:
- `location`: `str`
- `path`: `str`
- `namespaceType`: `ArtifactNamespace`
- `name`: `str`
- `packaging`: `ArtifactPackaging`
- `overrideArtifactName`: `bool`
- `encryptionDisabled`: `bool`
- `artifactIdentifier`: `str`
- `bucketOwnerAccess`: `BucketOwnerAccess`


## ProjectBadgeTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectBadgeTypeDef
```




Optional fields:
- `badgeEnabled`: `bool`
- `badgeRequestUrl`: `str`


## ProjectBuildBatchConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectBuildBatchConfigTypeDef
```




Optional fields:
- `serviceRole`: `str`
- `combineArtifacts`: `bool`
- `restrictions`: `"BatchRestrictionsTypeDef"`
- `timeoutInMins`: `int`


## ProjectCacheTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectCacheTypeDef
```


Required fields:
- `type`: `CacheType`



Optional fields:
- `location`: `str`
- `modes`: `List[CacheMode]`


## ProjectEnvironmentTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectEnvironmentTypeDef
```


Required fields:
- `type`: `EnvironmentType`
- `image`: `str`
- `computeType`: `ComputeType`



Optional fields:
- `environmentVariables`: `List["EnvironmentVariableTypeDef"]`
- `privilegedMode`: `bool`
- `certificate`: `str`
- `registryCredential`: `"RegistryCredentialTypeDef"`
- `imagePullCredentialsType`: `ImagePullCredentialsType`


## ProjectFileSystemLocationTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectFileSystemLocationTypeDef
```




Optional fields:
- `type`: `FileSystemType`
- `location`: `str`
- `mountPoint`: `str`
- `identifier`: `str`
- `mountOptions`: `str`


## ProjectSourceTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectSourceTypeDef
```


Required fields:
- `type`: `SourceType`



Optional fields:
- `location`: `str`
- `gitCloneDepth`: `int`
- `gitSubmodulesConfig`: `"GitSubmodulesConfigTypeDef"`
- `buildspec`: `str`
- `auth`: `"SourceAuthTypeDef"`
- `reportBuildStatus`: `bool`
- `buildStatusConfig`: `"BuildStatusConfigTypeDef"`
- `insecureSsl`: `bool`
- `sourceIdentifier`: `str`


## ProjectSourceVersionTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectSourceVersionTypeDef
```


Required fields:
- `sourceIdentifier`: `str`
- `sourceVersion`: `str`




## ProjectTypeDef

```python
from mypy_boto3_codebuild.type_defs import ProjectTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`
- `description`: `str`
- `source`: `"ProjectSourceTypeDef"`
- `secondarySources`: `List["ProjectSourceTypeDef"]`
- `sourceVersion`: `str`
- `secondarySourceVersions`: `List["ProjectSourceVersionTypeDef"]`
- `artifacts`: `"ProjectArtifactsTypeDef"`
- `secondaryArtifacts`: `List["ProjectArtifactsTypeDef"]`
- `cache`: `"ProjectCacheTypeDef"`
- `environment`: `"ProjectEnvironmentTypeDef"`
- `serviceRole`: `str`
- `timeoutInMinutes`: `int`
- `queuedTimeoutInMinutes`: `int`
- `encryptionKey`: `str`
- `tags`: `List["TagTypeDef"]`
- `created`: `datetime`
- `lastModified`: `datetime`
- `webhook`: `"WebhookTypeDef"`
- `vpcConfig`: `"VpcConfigTypeDef"`
- `badge`: `"ProjectBadgeTypeDef"`
- `logsConfig`: `"LogsConfigTypeDef"`
- `fileSystemLocations`: `List["ProjectFileSystemLocationTypeDef"]`
- `buildBatchConfig`: `"ProjectBuildBatchConfigTypeDef"`
- `concurrentBuildLimit`: `int`


## RegistryCredentialTypeDef

```python
from mypy_boto3_codebuild.type_defs import RegistryCredentialTypeDef
```


Required fields:
- `credential`: `str`
- `credentialProvider`: `CredentialProviderType`




## ReportExportConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import ReportExportConfigTypeDef
```




Optional fields:
- `exportConfigType`: `ReportExportConfigType`
- `s3Destination`: `"S3ReportExportConfigTypeDef"`


## ReportGroupTrendStatsTypeDef

```python
from mypy_boto3_codebuild.type_defs import ReportGroupTrendStatsTypeDef
```




Optional fields:
- `average`: `str`
- `max`: `str`
- `min`: `str`


## ReportGroupTypeDef

```python
from mypy_boto3_codebuild.type_defs import ReportGroupTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `ReportType`
- `exportConfig`: `"ReportExportConfigTypeDef"`
- `created`: `datetime`
- `lastModified`: `datetime`
- `tags`: `List["TagTypeDef"]`
- `status`: `ReportGroupStatusType`


## ReportTypeDef

```python
from mypy_boto3_codebuild.type_defs import ReportTypeDef
```




Optional fields:
- `arn`: `str`
- `type`: `ReportType`
- `name`: `str`
- `reportGroupArn`: `str`
- `executionId`: `str`
- `status`: `ReportStatusType`
- `created`: `datetime`
- `expired`: `datetime`
- `exportConfig`: `"ReportExportConfigTypeDef"`
- `truncated`: `bool`
- `testSummary`: `"TestReportSummaryTypeDef"`
- `codeCoverageSummary`: `"CodeCoverageReportSummaryTypeDef"`


## ReportWithRawDataTypeDef

```python
from mypy_boto3_codebuild.type_defs import ReportWithRawDataTypeDef
```




Optional fields:
- `reportArn`: `str`
- `data`: `str`


## ResolvedArtifactTypeDef

```python
from mypy_boto3_codebuild.type_defs import ResolvedArtifactTypeDef
```




Optional fields:
- `type`: `ArtifactsType`
- `location`: `str`
- `identifier`: `str`


## ResponseMetadata

```python
from mypy_boto3_codebuild.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## S3LogsConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import S3LogsConfigTypeDef
```


Required fields:
- `status`: `LogsConfigStatusType`



Optional fields:
- `location`: `str`
- `encryptionDisabled`: `bool`
- `bucketOwnerAccess`: `BucketOwnerAccess`


## S3ReportExportConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import S3ReportExportConfigTypeDef
```




Optional fields:
- `bucket`: `str`
- `bucketOwner`: `str`
- `path`: `str`
- `packaging`: `ReportPackagingType`
- `encryptionKey`: `str`
- `encryptionDisabled`: `bool`


## SourceAuthTypeDef

```python
from mypy_boto3_codebuild.type_defs import SourceAuthTypeDef
```


Required fields:
- `type`: `SourceAuthType`



Optional fields:
- `resource`: `str`


## SourceCredentialsInfoTypeDef

```python
from mypy_boto3_codebuild.type_defs import SourceCredentialsInfoTypeDef
```




Optional fields:
- `arn`: `str`
- `serverType`: `ServerType`
- `authType`: `AuthType`


## TagTypeDef

```python
from mypy_boto3_codebuild.type_defs import TagTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## TestCaseTypeDef

```python
from mypy_boto3_codebuild.type_defs import TestCaseTypeDef
```




Optional fields:
- `reportArn`: `str`
- `testRawDataPath`: `str`
- `prefix`: `str`
- `name`: `str`
- `status`: `str`
- `durationInNanoSeconds`: `int`
- `message`: `str`
- `expired`: `datetime`


## TestReportSummaryTypeDef

```python
from mypy_boto3_codebuild.type_defs import TestReportSummaryTypeDef
```


Required fields:
- `total`: `int`
- `statusCounts`: `Dict[str, int]`
- `durationInNanoSeconds`: `int`




## VpcConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import VpcConfigTypeDef
```




Optional fields:
- `vpcId`: `str`
- `subnets`: `List[str]`
- `securityGroupIds`: `List[str]`


## WebhookFilterTypeDef

```python
from mypy_boto3_codebuild.type_defs import WebhookFilterTypeDef
```


Required fields:
- `type`: `WebhookFilterType`
- `pattern`: `str`



Optional fields:
- `excludeMatchedPattern`: `bool`


## WebhookTypeDef

```python
from mypy_boto3_codebuild.type_defs import WebhookTypeDef
```




Optional fields:
- `url`: `str`
- `payloadUrl`: `str`
- `secret`: `str`
- `branchFilter`: `str`
- `filterGroups`: `List[List["WebhookFilterTypeDef"]]`
- `buildType`: `WebhookBuildType`
- `lastModifiedSecret`: `datetime`


## BatchDeleteBuildsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchDeleteBuildsOutputTypeDef
```




Optional fields:
- `buildsDeleted`: `List[str]`
- `buildsNotDeleted`: `List["BuildNotDeletedTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetBuildBatchesOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchGetBuildBatchesOutputTypeDef
```




Optional fields:
- `buildBatches`: `List["BuildBatchTypeDef"]`
- `buildBatchesNotFound`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetBuildsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchGetBuildsOutputTypeDef
```




Optional fields:
- `builds`: `List["BuildTypeDef"]`
- `buildsNotFound`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetProjectsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchGetProjectsOutputTypeDef
```




Optional fields:
- `projects`: `List["ProjectTypeDef"]`
- `projectsNotFound`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetReportGroupsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchGetReportGroupsOutputTypeDef
```




Optional fields:
- `reportGroups`: `List["ReportGroupTypeDef"]`
- `reportGroupsNotFound`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchGetReportsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import BatchGetReportsOutputTypeDef
```




Optional fields:
- `reports`: `List["ReportTypeDef"]`
- `reportsNotFound`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BuildBatchFilterTypeDef

```python
from mypy_boto3_codebuild.type_defs import BuildBatchFilterTypeDef
```




Optional fields:
- `status`: `StatusType`


## CreateProjectOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import CreateProjectOutputTypeDef
```




Optional fields:
- `project`: `"ProjectTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateReportGroupOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import CreateReportGroupOutputTypeDef
```




Optional fields:
- `reportGroup`: `"ReportGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateWebhookOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import CreateWebhookOutputTypeDef
```




Optional fields:
- `webhook`: `"WebhookTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteBuildBatchOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import DeleteBuildBatchOutputTypeDef
```




Optional fields:
- `statusCode`: `str`
- `buildsDeleted`: `List[str]`
- `buildsNotDeleted`: `List["BuildNotDeletedTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeleteSourceCredentialsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import DeleteSourceCredentialsOutputTypeDef
```




Optional fields:
- `arn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeCodeCoveragesOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import DescribeCodeCoveragesOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `codeCoverages`: `List["CodeCoverageTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTestCasesOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import DescribeTestCasesOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `testCases`: `List["TestCaseTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetReportGroupTrendOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import GetReportGroupTrendOutputTypeDef
```




Optional fields:
- `stats`: `"ReportGroupTrendStatsTypeDef"`
- `rawData`: `List["ReportWithRawDataTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetResourcePolicyOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import GetResourcePolicyOutputTypeDef
```




Optional fields:
- `policy`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ImportSourceCredentialsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ImportSourceCredentialsOutputTypeDef
```




Optional fields:
- `arn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBuildBatchesForProjectOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListBuildBatchesForProjectOutputTypeDef
```




Optional fields:
- `ids`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBuildBatchesOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListBuildBatchesOutputTypeDef
```




Optional fields:
- `ids`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBuildsForProjectOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListBuildsForProjectOutputTypeDef
```




Optional fields:
- `ids`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBuildsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListBuildsOutputTypeDef
```




Optional fields:
- `ids`: `List[str]`
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListCuratedEnvironmentImagesOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListCuratedEnvironmentImagesOutputTypeDef
```




Optional fields:
- `platforms`: `List["EnvironmentPlatformTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProjectsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListProjectsOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `projects`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListReportGroupsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListReportGroupsOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `reportGroups`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListReportsForReportGroupOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListReportsForReportGroupOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `reports`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListReportsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListReportsOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `reports`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSharedProjectsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListSharedProjectsOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `projects`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSharedReportGroupsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListSharedReportGroupsOutputTypeDef
```




Optional fields:
- `nextToken`: `str`
- `reportGroups`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListSourceCredentialsOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import ListSourceCredentialsOutputTypeDef
```




Optional fields:
- `sourceCredentialsInfos`: `List["SourceCredentialsInfoTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_codebuild.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutResourcePolicyOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import PutResourcePolicyOutputTypeDef
```




Optional fields:
- `resourceArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ReportFilterTypeDef

```python
from mypy_boto3_codebuild.type_defs import ReportFilterTypeDef
```




Optional fields:
- `status`: `ReportStatusType`


## RetryBuildBatchOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import RetryBuildBatchOutputTypeDef
```




Optional fields:
- `buildBatch`: `"BuildBatchTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## RetryBuildOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import RetryBuildOutputTypeDef
```




Optional fields:
- `build`: `"BuildTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartBuildBatchOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import StartBuildBatchOutputTypeDef
```




Optional fields:
- `buildBatch`: `"BuildBatchTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StartBuildOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import StartBuildOutputTypeDef
```




Optional fields:
- `build`: `"BuildTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StopBuildBatchOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import StopBuildBatchOutputTypeDef
```




Optional fields:
- `buildBatch`: `"BuildBatchTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StopBuildOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import StopBuildOutputTypeDef
```




Optional fields:
- `build`: `"BuildTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## TestCaseFilterTypeDef

```python
from mypy_boto3_codebuild.type_defs import TestCaseFilterTypeDef
```




Optional fields:
- `status`: `str`
- `keyword`: `str`


## UpdateProjectOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import UpdateProjectOutputTypeDef
```




Optional fields:
- `project`: `"ProjectTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateReportGroupOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import UpdateReportGroupOutputTypeDef
```




Optional fields:
- `reportGroup`: `"ReportGroupTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateWebhookOutputTypeDef

```python
from mypy_boto3_codebuild.type_defs import UpdateWebhookOutputTypeDef
```




Optional fields:
- `webhook`: `"WebhookTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`

