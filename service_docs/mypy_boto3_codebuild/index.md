# Type annotations for boto3 CodeBuild module

> [Index](../index.md) > CodeBuild

Auto-generated documentation for [CodeBuild](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild)
type annotations stubs module [mypy_boto3_codebuild](https://pypi.org/project/mypy-boto3-codebuild/).

```bash
pip install mypy-boto3-codebuild
```

- [Type annotations for boto3 CodeBuild module](#type-annotations-for-boto3-codebuild-module)
  - [CodeBuildClient](#codebuildclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CodeBuildClient

Type annotations for  `boto3.client("codebuild")` as [CodeBuildClient](./client.md)

Can be used directly:

```python
from mypy_boto3_codebuild.client import CodeBuildClient
```


CodeBuildClient [exceptions](./client.md#exceptions)



### Methods
- [batch_delete_builds](./client.md#batch-delete-builds)
- [batch_get_build_batches](./client.md#batch-get-build-batches)
- [batch_get_builds](./client.md#batch-get-builds)
- [batch_get_projects](./client.md#batch-get-projects)
- [batch_get_report_groups](./client.md#batch-get-report-groups)
- [batch_get_reports](./client.md#batch-get-reports)
- [can_paginate](./client.md#can-paginate)
- [create_project](./client.md#create-project)
- [create_report_group](./client.md#create-report-group)
- [create_webhook](./client.md#create-webhook)
- [delete_build_batch](./client.md#delete-build-batch)
- [delete_project](./client.md#delete-project)
- [delete_report](./client.md#delete-report)
- [delete_report_group](./client.md#delete-report-group)
- [delete_resource_policy](./client.md#delete-resource-policy)
- [delete_source_credentials](./client.md#delete-source-credentials)
- [delete_webhook](./client.md#delete-webhook)
- [describe_code_coverages](./client.md#describe-code-coverages)
- [describe_test_cases](./client.md#describe-test-cases)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_report_group_trend](./client.md#get-report-group-trend)
- [get_resource_policy](./client.md#get-resource-policy)
- [import_source_credentials](./client.md#import-source-credentials)
- [invalidate_project_cache](./client.md#invalidate-project-cache)
- [list_build_batches](./client.md#list-build-batches)
- [list_build_batches_for_project](./client.md#list-build-batches-for-project)
- [list_builds](./client.md#list-builds)
- [list_builds_for_project](./client.md#list-builds-for-project)
- [list_curated_environment_images](./client.md#list-curated-environment-images)
- [list_projects](./client.md#list-projects)
- [list_report_groups](./client.md#list-report-groups)
- [list_reports](./client.md#list-reports)
- [list_reports_for_report_group](./client.md#list-reports-for-report-group)
- [list_shared_projects](./client.md#list-shared-projects)
- [list_shared_report_groups](./client.md#list-shared-report-groups)
- [list_source_credentials](./client.md#list-source-credentials)
- [put_resource_policy](./client.md#put-resource-policy)
- [retry_build](./client.md#retry-build)
- [retry_build_batch](./client.md#retry-build-batch)
- [start_build](./client.md#start-build)
- [start_build_batch](./client.md#start-build-batch)
- [stop_build](./client.md#stop-build)
- [stop_build_batch](./client.md#stop-build-batch)
- [update_project](./client.md#update-project)
- [update_report_group](./client.md#update-report-group)
- [update_webhook](./client.md#update-webhook)




### Exceptions
- [AccountLimitExceededException](./client.md#accountlimitexceededexception)
- [ClientError](./client.md#clienterror)
- [InvalidInputException](./client.md#invalidinputexception)
- [OAuthProviderException](./client.md#oauthproviderexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("codebuild").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_codebuild.paginators import DescribeCodeCoveragesPaginator, ...
```

- [DescribeCodeCoveragesPaginator](./paginators.md#describecodecoveragespaginator)
- [DescribeTestCasesPaginator](./paginators.md#describetestcasespaginator)
- [ListBuildBatchesPaginator](./paginators.md#listbuildbatchespaginator)
- [ListBuildBatchesForProjectPaginator](./paginators.md#listbuildbatchesforprojectpaginator)
- [ListBuildsPaginator](./paginators.md#listbuildspaginator)
- [ListBuildsForProjectPaginator](./paginators.md#listbuildsforprojectpaginator)
- [ListProjectsPaginator](./paginators.md#listprojectspaginator)
- [ListReportGroupsPaginator](./paginators.md#listreportgroupspaginator)
- [ListReportsPaginator](./paginators.md#listreportspaginator)
- [ListReportsForReportGroupPaginator](./paginators.md#listreportsforreportgrouppaginator)
- [ListSharedProjectsPaginator](./paginators.md#listsharedprojectspaginator)
- [ListSharedReportGroupsPaginator](./paginators.md#listsharedreportgroupspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codebuild.literals import ArtifactNamespace, ...
```

- [ArtifactNamespace](./literals.md#artifactnamespace)
- [ArtifactPackaging](./literals.md#artifactpackaging)
- [ArtifactsType](./literals.md#artifactstype)
- [AuthType](./literals.md#authtype)
- [BucketOwnerAccess](./literals.md#bucketowneraccess)
- [BuildBatchPhaseType](./literals.md#buildbatchphasetype)
- [BuildPhaseType](./literals.md#buildphasetype)
- [CacheMode](./literals.md#cachemode)
- [CacheType](./literals.md#cachetype)
- [ComputeType](./literals.md#computetype)
- [CredentialProviderType](./literals.md#credentialprovidertype)
- [DescribeCodeCoveragesPaginatorName](./literals.md#describecodecoveragespaginatorname)
- [DescribeTestCasesPaginatorName](./literals.md#describetestcasespaginatorname)
- [EnvironmentType](./literals.md#environmenttype)
- [EnvironmentVariableType](./literals.md#environmentvariabletype)
- [FileSystemType](./literals.md#filesystemtype)
- [ImagePullCredentialsType](./literals.md#imagepullcredentialstype)
- [LanguageType](./literals.md#languagetype)
- [ListBuildBatchesForProjectPaginatorName](./literals.md#listbuildbatchesforprojectpaginatorname)
- [ListBuildBatchesPaginatorName](./literals.md#listbuildbatchespaginatorname)
- [ListBuildsForProjectPaginatorName](./literals.md#listbuildsforprojectpaginatorname)
- [ListBuildsPaginatorName](./literals.md#listbuildspaginatorname)
- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)
- [ListReportGroupsPaginatorName](./literals.md#listreportgroupspaginatorname)
- [ListReportsForReportGroupPaginatorName](./literals.md#listreportsforreportgrouppaginatorname)
- [ListReportsPaginatorName](./literals.md#listreportspaginatorname)
- [ListSharedProjectsPaginatorName](./literals.md#listsharedprojectspaginatorname)
- [ListSharedReportGroupsPaginatorName](./literals.md#listsharedreportgroupspaginatorname)
- [LogsConfigStatusType](./literals.md#logsconfigstatustype)
- [PlatformType](./literals.md#platformtype)
- [ProjectSortByType](./literals.md#projectsortbytype)
- [ReportCodeCoverageSortByType](./literals.md#reportcodecoveragesortbytype)
- [ReportExportConfigType](./literals.md#reportexportconfigtype)
- [ReportGroupSortByType](./literals.md#reportgroupsortbytype)
- [ReportGroupStatusType](./literals.md#reportgroupstatustype)
- [ReportGroupTrendFieldType](./literals.md#reportgrouptrendfieldtype)
- [ReportPackagingType](./literals.md#reportpackagingtype)
- [ReportStatusType](./literals.md#reportstatustype)
- [ReportType](./literals.md#reporttype)
- [RetryBuildBatchType](./literals.md#retrybuildbatchtype)
- [ServerType](./literals.md#servertype)
- [SharedResourceSortByType](./literals.md#sharedresourcesortbytype)
- [SortOrderType](./literals.md#sortordertype)
- [SourceAuthType](./literals.md#sourceauthtype)
- [SourceType](./literals.md#sourcetype)
- [StatusType](./literals.md#statustype)
- [WebhookBuildType](./literals.md#webhookbuildtype)
- [WebhookFilterType](./literals.md#webhookfiltertype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_codebuild.type_defs import BatchRestrictionsTypeDef, ...
```

- [BatchRestrictionsTypeDef](./type_defs.md#batchrestrictionstypedef)
- [BuildArtifactsTypeDef](./type_defs.md#buildartifactstypedef)
- [BuildBatchPhaseTypeDef](./type_defs.md#buildbatchphasetypedef)
- [BuildBatchTypeDef](./type_defs.md#buildbatchtypedef)
- [BuildGroupTypeDef](./type_defs.md#buildgrouptypedef)
- [BuildNotDeletedTypeDef](./type_defs.md#buildnotdeletedtypedef)
- [BuildPhaseTypeDef](./type_defs.md#buildphasetypedef)
- [BuildStatusConfigTypeDef](./type_defs.md#buildstatusconfigtypedef)
- [BuildSummaryTypeDef](./type_defs.md#buildsummarytypedef)
- [BuildTypeDef](./type_defs.md#buildtypedef)
- [CloudWatchLogsConfigTypeDef](./type_defs.md#cloudwatchlogsconfigtypedef)
- [CodeCoverageReportSummaryTypeDef](./type_defs.md#codecoveragereportsummarytypedef)
- [CodeCoverageTypeDef](./type_defs.md#codecoveragetypedef)
- [DebugSessionTypeDef](./type_defs.md#debugsessiontypedef)
- [EnvironmentImageTypeDef](./type_defs.md#environmentimagetypedef)
- [EnvironmentLanguageTypeDef](./type_defs.md#environmentlanguagetypedef)
- [EnvironmentPlatformTypeDef](./type_defs.md#environmentplatformtypedef)
- [EnvironmentVariableTypeDef](./type_defs.md#environmentvariabletypedef)
- [ExportedEnvironmentVariableTypeDef](./type_defs.md#exportedenvironmentvariabletypedef)
- [GitSubmodulesConfigTypeDef](./type_defs.md#gitsubmodulesconfigtypedef)
- [LogsConfigTypeDef](./type_defs.md#logsconfigtypedef)
- [LogsLocationTypeDef](./type_defs.md#logslocationtypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [PhaseContextTypeDef](./type_defs.md#phasecontexttypedef)
- [ProjectArtifactsTypeDef](./type_defs.md#projectartifactstypedef)
- [ProjectBadgeTypeDef](./type_defs.md#projectbadgetypedef)
- [ProjectBuildBatchConfigTypeDef](./type_defs.md#projectbuildbatchconfigtypedef)
- [ProjectCacheTypeDef](./type_defs.md#projectcachetypedef)
- [ProjectEnvironmentTypeDef](./type_defs.md#projectenvironmenttypedef)
- [ProjectFileSystemLocationTypeDef](./type_defs.md#projectfilesystemlocationtypedef)
- [ProjectSourceTypeDef](./type_defs.md#projectsourcetypedef)
- [ProjectSourceVersionTypeDef](./type_defs.md#projectsourceversiontypedef)
- [ProjectTypeDef](./type_defs.md#projecttypedef)
- [RegistryCredentialTypeDef](./type_defs.md#registrycredentialtypedef)
- [ReportExportConfigTypeDef](./type_defs.md#reportexportconfigtypedef)
- [ReportGroupTrendStatsTypeDef](./type_defs.md#reportgrouptrendstatstypedef)
- [ReportGroupTypeDef](./type_defs.md#reportgrouptypedef)
- [ReportTypeDef](./type_defs.md#reporttypedef)
- [ReportWithRawDataTypeDef](./type_defs.md#reportwithrawdatatypedef)
- [ResolvedArtifactTypeDef](./type_defs.md#resolvedartifacttypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [S3LogsConfigTypeDef](./type_defs.md#s3logsconfigtypedef)
- [S3ReportExportConfigTypeDef](./type_defs.md#s3reportexportconfigtypedef)
- [SourceAuthTypeDef](./type_defs.md#sourceauthtypedef)
- [SourceCredentialsInfoTypeDef](./type_defs.md#sourcecredentialsinfotypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TestCaseTypeDef](./type_defs.md#testcasetypedef)
- [TestReportSummaryTypeDef](./type_defs.md#testreportsummarytypedef)
- [VpcConfigTypeDef](./type_defs.md#vpcconfigtypedef)
- [WebhookFilterTypeDef](./type_defs.md#webhookfiltertypedef)
- [WebhookTypeDef](./type_defs.md#webhooktypedef)
- [BatchDeleteBuildsOutputTypeDef](./type_defs.md#batchdeletebuildsoutputtypedef)
- [BatchGetBuildBatchesOutputTypeDef](./type_defs.md#batchgetbuildbatchesoutputtypedef)
- [BatchGetBuildsOutputTypeDef](./type_defs.md#batchgetbuildsoutputtypedef)
- [BatchGetProjectsOutputTypeDef](./type_defs.md#batchgetprojectsoutputtypedef)
- [BatchGetReportGroupsOutputTypeDef](./type_defs.md#batchgetreportgroupsoutputtypedef)
- [BatchGetReportsOutputTypeDef](./type_defs.md#batchgetreportsoutputtypedef)
- [BuildBatchFilterTypeDef](./type_defs.md#buildbatchfiltertypedef)
- [CreateProjectOutputTypeDef](./type_defs.md#createprojectoutputtypedef)
- [CreateReportGroupOutputTypeDef](./type_defs.md#createreportgroupoutputtypedef)
- [CreateWebhookOutputTypeDef](./type_defs.md#createwebhookoutputtypedef)
- [DeleteBuildBatchOutputTypeDef](./type_defs.md#deletebuildbatchoutputtypedef)
- [DeleteSourceCredentialsOutputTypeDef](./type_defs.md#deletesourcecredentialsoutputtypedef)
- [DescribeCodeCoveragesOutputTypeDef](./type_defs.md#describecodecoveragesoutputtypedef)
- [DescribeTestCasesOutputTypeDef](./type_defs.md#describetestcasesoutputtypedef)
- [GetReportGroupTrendOutputTypeDef](./type_defs.md#getreportgrouptrendoutputtypedef)
- [GetResourcePolicyOutputTypeDef](./type_defs.md#getresourcepolicyoutputtypedef)
- [ImportSourceCredentialsOutputTypeDef](./type_defs.md#importsourcecredentialsoutputtypedef)
- [ListBuildBatchesForProjectOutputTypeDef](./type_defs.md#listbuildbatchesforprojectoutputtypedef)
- [ListBuildBatchesOutputTypeDef](./type_defs.md#listbuildbatchesoutputtypedef)
- [ListBuildsForProjectOutputTypeDef](./type_defs.md#listbuildsforprojectoutputtypedef)
- [ListBuildsOutputTypeDef](./type_defs.md#listbuildsoutputtypedef)
- [ListCuratedEnvironmentImagesOutputTypeDef](./type_defs.md#listcuratedenvironmentimagesoutputtypedef)
- [ListProjectsOutputTypeDef](./type_defs.md#listprojectsoutputtypedef)
- [ListReportGroupsOutputTypeDef](./type_defs.md#listreportgroupsoutputtypedef)
- [ListReportsForReportGroupOutputTypeDef](./type_defs.md#listreportsforreportgroupoutputtypedef)
- [ListReportsOutputTypeDef](./type_defs.md#listreportsoutputtypedef)
- [ListSharedProjectsOutputTypeDef](./type_defs.md#listsharedprojectsoutputtypedef)
- [ListSharedReportGroupsOutputTypeDef](./type_defs.md#listsharedreportgroupsoutputtypedef)
- [ListSourceCredentialsOutputTypeDef](./type_defs.md#listsourcecredentialsoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutResourcePolicyOutputTypeDef](./type_defs.md#putresourcepolicyoutputtypedef)
- [ReportFilterTypeDef](./type_defs.md#reportfiltertypedef)
- [RetryBuildBatchOutputTypeDef](./type_defs.md#retrybuildbatchoutputtypedef)
- [RetryBuildOutputTypeDef](./type_defs.md#retrybuildoutputtypedef)
- [StartBuildBatchOutputTypeDef](./type_defs.md#startbuildbatchoutputtypedef)
- [StartBuildOutputTypeDef](./type_defs.md#startbuildoutputtypedef)
- [StopBuildBatchOutputTypeDef](./type_defs.md#stopbuildbatchoutputtypedef)
- [StopBuildOutputTypeDef](./type_defs.md#stopbuildoutputtypedef)
- [TestCaseFilterTypeDef](./type_defs.md#testcasefiltertypedef)
- [UpdateProjectOutputTypeDef](./type_defs.md#updateprojectoutputtypedef)
- [UpdateReportGroupOutputTypeDef](./type_defs.md#updatereportgroupoutputtypedef)
- [UpdateWebhookOutputTypeDef](./type_defs.md#updatewebhookoutputtypedef)
