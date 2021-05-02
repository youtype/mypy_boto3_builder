# Structures for boto3 Amplify module

> [Index](../index.md) > [Amplify](./index.md) > Structures

Auto-generated documentation for [Amplify](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify)
type annotations stubs module [mypy_boto3_amplify](https://pypi.org/project/mypy-boto3-amplify/).

- [Structures for boto3 Amplify module](#structures-for-boto3-amplify-module)
  - [AppTypeDef](#apptypedef)
  - [ArtifactTypeDef](#artifacttypedef)
  - [AutoBranchCreationConfigTypeDef](#autobranchcreationconfigtypedef)
  - [BackendEnvironmentTypeDef](#backendenvironmenttypedef)
  - [BranchTypeDef](#branchtypedef)
  - [CustomRuleTypeDef](#customruletypedef)
  - [DomainAssociationTypeDef](#domainassociationtypedef)
  - [JobSummaryTypeDef](#jobsummarytypedef)
  - [JobTypeDef](#jobtypedef)
  - [ProductionBranchTypeDef](#productionbranchtypedef)
  - [StepTypeDef](#steptypedef)
  - [SubDomainSettingTypeDef](#subdomainsettingtypedef)
  - [SubDomainTypeDef](#subdomaintypedef)
  - [WebhookTypeDef](#webhooktypedef)
  - [CreateAppResultTypeDef](#createappresulttypedef)
  - [CreateBackendEnvironmentResultTypeDef](#createbackendenvironmentresulttypedef)
  - [CreateBranchResultTypeDef](#createbranchresulttypedef)
  - [CreateDeploymentResultTypeDef](#createdeploymentresulttypedef)
  - [CreateDomainAssociationResultTypeDef](#createdomainassociationresulttypedef)
  - [CreateWebhookResultTypeDef](#createwebhookresulttypedef)
  - [DeleteAppResultTypeDef](#deleteappresulttypedef)
  - [DeleteBackendEnvironmentResultTypeDef](#deletebackendenvironmentresulttypedef)
  - [DeleteBranchResultTypeDef](#deletebranchresulttypedef)
  - [DeleteDomainAssociationResultTypeDef](#deletedomainassociationresulttypedef)
  - [DeleteJobResultTypeDef](#deletejobresulttypedef)
  - [DeleteWebhookResultTypeDef](#deletewebhookresulttypedef)
  - [GenerateAccessLogsResultTypeDef](#generateaccesslogsresulttypedef)
  - [GetAppResultTypeDef](#getappresulttypedef)
  - [GetArtifactUrlResultTypeDef](#getartifacturlresulttypedef)
  - [GetBackendEnvironmentResultTypeDef](#getbackendenvironmentresulttypedef)
  - [GetBranchResultTypeDef](#getbranchresulttypedef)
  - [GetDomainAssociationResultTypeDef](#getdomainassociationresulttypedef)
  - [GetJobResultTypeDef](#getjobresulttypedef)
  - [GetWebhookResultTypeDef](#getwebhookresulttypedef)
  - [ListAppsResultTypeDef](#listappsresulttypedef)
  - [ListArtifactsResultTypeDef](#listartifactsresulttypedef)
  - [ListBackendEnvironmentsResultTypeDef](#listbackendenvironmentsresulttypedef)
  - [ListBranchesResultTypeDef](#listbranchesresulttypedef)
  - [ListDomainAssociationsResultTypeDef](#listdomainassociationsresulttypedef)
  - [ListJobsResultTypeDef](#listjobsresulttypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListWebhooksResultTypeDef](#listwebhooksresulttypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [StartDeploymentResultTypeDef](#startdeploymentresulttypedef)
  - [StartJobResultTypeDef](#startjobresulttypedef)
  - [StopJobResultTypeDef](#stopjobresulttypedef)
  - [UpdateAppResultTypeDef](#updateappresulttypedef)
  - [UpdateBranchResultTypeDef](#updatebranchresulttypedef)
  - [UpdateDomainAssociationResultTypeDef](#updatedomainassociationresulttypedef)
  - [UpdateWebhookResultTypeDef](#updatewebhookresulttypedef)

## AppTypeDef

```python
from mypy_boto3_amplify.type_defs import AppTypeDef
```


Required fields:
- `appId`: `str`
- `appArn`: `str`
- `name`: `str`
- `description`: `str`
- `repository`: `str`
- `platform`: `Platform`
- `createTime`: `datetime`
- `updateTime`: `datetime`
- `environmentVariables`: `Dict[str, str]`
- `defaultDomain`: `str`
- `enableBranchAutoBuild`: `bool`
- `enableBasicAuth`: `bool`



Optional fields:
- `tags`: `Dict[str, str]`
- `iamServiceRoleArn`: `str`
- `enableBranchAutoDeletion`: `bool`
- `basicAuthCredentials`: `str`
- `customRules`: `List["CustomRuleTypeDef"]`
- `productionBranch`: `"ProductionBranchTypeDef"`
- `buildSpec`: `str`
- `customHeaders`: `str`
- `enableAutoBranchCreation`: `bool`
- `autoBranchCreationPatterns`: `List[str]`
- `autoBranchCreationConfig`: `"AutoBranchCreationConfigTypeDef"`


## ArtifactTypeDef

```python
from mypy_boto3_amplify.type_defs import ArtifactTypeDef
```


Required fields:
- `artifactFileName`: `str`
- `artifactId`: `str`




## AutoBranchCreationConfigTypeDef

```python
from mypy_boto3_amplify.type_defs import AutoBranchCreationConfigTypeDef
```




Optional fields:
- `stage`: `Stage`
- `framework`: `str`
- `enableAutoBuild`: `bool`
- `environmentVariables`: `Dict[str, str]`
- `basicAuthCredentials`: `str`
- `enableBasicAuth`: `bool`
- `enablePerformanceMode`: `bool`
- `buildSpec`: `str`
- `enablePullRequestPreview`: `bool`
- `pullRequestEnvironmentName`: `str`


## BackendEnvironmentTypeDef

```python
from mypy_boto3_amplify.type_defs import BackendEnvironmentTypeDef
```


Required fields:
- `backendEnvironmentArn`: `str`
- `environmentName`: `str`
- `createTime`: `datetime`
- `updateTime`: `datetime`



Optional fields:
- `stackName`: `str`
- `deploymentArtifacts`: `str`


## BranchTypeDef

```python
from mypy_boto3_amplify.type_defs import BranchTypeDef
```


Required fields:
- `branchArn`: `str`
- `branchName`: `str`
- `description`: `str`
- `stage`: `Stage`
- `displayName`: `str`
- `enableNotification`: `bool`
- `createTime`: `datetime`
- `updateTime`: `datetime`
- `environmentVariables`: `Dict[str, str]`
- `enableAutoBuild`: `bool`
- `customDomains`: `List[str]`
- `framework`: `str`
- `activeJobId`: `str`
- `totalNumberOfJobs`: `str`
- `enableBasicAuth`: `bool`
- `ttl`: `str`
- `enablePullRequestPreview`: `bool`



Optional fields:
- `tags`: `Dict[str, str]`
- `enablePerformanceMode`: `bool`
- `thumbnailUrl`: `str`
- `basicAuthCredentials`: `str`
- `buildSpec`: `str`
- `associatedResources`: `List[str]`
- `pullRequestEnvironmentName`: `str`
- `destinationBranch`: `str`
- `sourceBranch`: `str`
- `backendEnvironmentArn`: `str`


## CustomRuleTypeDef

```python
from mypy_boto3_amplify.type_defs import CustomRuleTypeDef
```


Required fields:
- `source`: `str`
- `target`: `str`



Optional fields:
- `status`: `str`
- `condition`: `str`


## DomainAssociationTypeDef

```python
from mypy_boto3_amplify.type_defs import DomainAssociationTypeDef
```


Required fields:
- `domainAssociationArn`: `str`
- `domainName`: `str`
- `enableAutoSubDomain`: `bool`
- `domainStatus`: `DomainStatus`
- `statusReason`: `str`
- `subDomains`: `List["SubDomainTypeDef"]`



Optional fields:
- `autoSubDomainCreationPatterns`: `List[str]`
- `autoSubDomainIAMRole`: `str`
- `certificateVerificationDNSRecord`: `str`


## JobSummaryTypeDef

```python
from mypy_boto3_amplify.type_defs import JobSummaryTypeDef
```


Required fields:
- `jobArn`: `str`
- `jobId`: `str`
- `commitId`: `str`
- `commitMessage`: `str`
- `commitTime`: `datetime`
- `startTime`: `datetime`
- `status`: `JobStatus`
- `jobType`: `JobType`



Optional fields:
- `endTime`: `datetime`


## JobTypeDef

```python
from mypy_boto3_amplify.type_defs import JobTypeDef
```


Required fields:
- `summary`: `"JobSummaryTypeDef"`
- `steps`: `List["StepTypeDef"]`




## ProductionBranchTypeDef

```python
from mypy_boto3_amplify.type_defs import ProductionBranchTypeDef
```




Optional fields:
- `lastDeployTime`: `datetime`
- `status`: `str`
- `thumbnailUrl`: `str`
- `branchName`: `str`


## StepTypeDef

```python
from mypy_boto3_amplify.type_defs import StepTypeDef
```


Required fields:
- `stepName`: `str`
- `startTime`: `datetime`
- `status`: `JobStatus`
- `endTime`: `datetime`



Optional fields:
- `logUrl`: `str`
- `artifactsUrl`: `str`
- `testArtifactsUrl`: `str`
- `testConfigUrl`: `str`
- `screenshots`: `Dict[str, str]`
- `statusReason`: `str`
- `context`: `str`


## SubDomainSettingTypeDef

```python
from mypy_boto3_amplify.type_defs import SubDomainSettingTypeDef
```


Required fields:
- `prefix`: `str`
- `branchName`: `str`




## SubDomainTypeDef

```python
from mypy_boto3_amplify.type_defs import SubDomainTypeDef
```


Required fields:
- `subDomainSetting`: `"SubDomainSettingTypeDef"`
- `verified`: `bool`
- `dnsRecord`: `str`




## WebhookTypeDef

```python
from mypy_boto3_amplify.type_defs import WebhookTypeDef
```


Required fields:
- `webhookArn`: `str`
- `webhookId`: `str`
- `webhookUrl`: `str`
- `branchName`: `str`
- `description`: `str`
- `createTime`: `datetime`
- `updateTime`: `datetime`




## CreateAppResultTypeDef

```python
from mypy_boto3_amplify.type_defs import CreateAppResultTypeDef
```


Required fields:
- `app`: `"AppTypeDef"`




## CreateBackendEnvironmentResultTypeDef

```python
from mypy_boto3_amplify.type_defs import CreateBackendEnvironmentResultTypeDef
```


Required fields:
- `backendEnvironment`: `"BackendEnvironmentTypeDef"`




## CreateBranchResultTypeDef

```python
from mypy_boto3_amplify.type_defs import CreateBranchResultTypeDef
```


Required fields:
- `branch`: `"BranchTypeDef"`




## CreateDeploymentResultTypeDef

```python
from mypy_boto3_amplify.type_defs import CreateDeploymentResultTypeDef
```


Required fields:
- `fileUploadUrls`: `Dict[str, str]`
- `zipUploadUrl`: `str`



Optional fields:
- `jobId`: `str`


## CreateDomainAssociationResultTypeDef

```python
from mypy_boto3_amplify.type_defs import CreateDomainAssociationResultTypeDef
```


Required fields:
- `domainAssociation`: `"DomainAssociationTypeDef"`




## CreateWebhookResultTypeDef

```python
from mypy_boto3_amplify.type_defs import CreateWebhookResultTypeDef
```


Required fields:
- `webhook`: `"WebhookTypeDef"`




## DeleteAppResultTypeDef

```python
from mypy_boto3_amplify.type_defs import DeleteAppResultTypeDef
```


Required fields:
- `app`: `"AppTypeDef"`




## DeleteBackendEnvironmentResultTypeDef

```python
from mypy_boto3_amplify.type_defs import DeleteBackendEnvironmentResultTypeDef
```


Required fields:
- `backendEnvironment`: `"BackendEnvironmentTypeDef"`




## DeleteBranchResultTypeDef

```python
from mypy_boto3_amplify.type_defs import DeleteBranchResultTypeDef
```


Required fields:
- `branch`: `"BranchTypeDef"`




## DeleteDomainAssociationResultTypeDef

```python
from mypy_boto3_amplify.type_defs import DeleteDomainAssociationResultTypeDef
```


Required fields:
- `domainAssociation`: `"DomainAssociationTypeDef"`




## DeleteJobResultTypeDef

```python
from mypy_boto3_amplify.type_defs import DeleteJobResultTypeDef
```


Required fields:
- `jobSummary`: `"JobSummaryTypeDef"`




## DeleteWebhookResultTypeDef

```python
from mypy_boto3_amplify.type_defs import DeleteWebhookResultTypeDef
```


Required fields:
- `webhook`: `"WebhookTypeDef"`




## GenerateAccessLogsResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GenerateAccessLogsResultTypeDef
```




Optional fields:
- `logUrl`: `str`


## GetAppResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetAppResultTypeDef
```


Required fields:
- `app`: `"AppTypeDef"`




## GetArtifactUrlResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetArtifactUrlResultTypeDef
```


Required fields:
- `artifactId`: `str`
- `artifactUrl`: `str`




## GetBackendEnvironmentResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetBackendEnvironmentResultTypeDef
```


Required fields:
- `backendEnvironment`: `"BackendEnvironmentTypeDef"`




## GetBranchResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetBranchResultTypeDef
```


Required fields:
- `branch`: `"BranchTypeDef"`




## GetDomainAssociationResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetDomainAssociationResultTypeDef
```


Required fields:
- `domainAssociation`: `"DomainAssociationTypeDef"`




## GetJobResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetJobResultTypeDef
```


Required fields:
- `job`: `"JobTypeDef"`




## GetWebhookResultTypeDef

```python
from mypy_boto3_amplify.type_defs import GetWebhookResultTypeDef
```


Required fields:
- `webhook`: `"WebhookTypeDef"`




## ListAppsResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListAppsResultTypeDef
```


Required fields:
- `apps`: `List["AppTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListArtifactsResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListArtifactsResultTypeDef
```


Required fields:
- `artifacts`: `List["ArtifactTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListBackendEnvironmentsResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListBackendEnvironmentsResultTypeDef
```


Required fields:
- `backendEnvironments`: `List["BackendEnvironmentTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListBranchesResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListBranchesResultTypeDef
```


Required fields:
- `branches`: `List["BranchTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListDomainAssociationsResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListDomainAssociationsResultTypeDef
```


Required fields:
- `domainAssociations`: `List["DomainAssociationTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListJobsResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListJobsResultTypeDef
```


Required fields:
- `jobSummaries`: `List["JobSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_amplify.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListWebhooksResultTypeDef

```python
from mypy_boto3_amplify.type_defs import ListWebhooksResultTypeDef
```


Required fields:
- `webhooks`: `List["WebhookTypeDef"]`



Optional fields:
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_amplify.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## StartDeploymentResultTypeDef

```python
from mypy_boto3_amplify.type_defs import StartDeploymentResultTypeDef
```


Required fields:
- `jobSummary`: `"JobSummaryTypeDef"`




## StartJobResultTypeDef

```python
from mypy_boto3_amplify.type_defs import StartJobResultTypeDef
```


Required fields:
- `jobSummary`: `"JobSummaryTypeDef"`




## StopJobResultTypeDef

```python
from mypy_boto3_amplify.type_defs import StopJobResultTypeDef
```


Required fields:
- `jobSummary`: `"JobSummaryTypeDef"`




## UpdateAppResultTypeDef

```python
from mypy_boto3_amplify.type_defs import UpdateAppResultTypeDef
```


Required fields:
- `app`: `"AppTypeDef"`




## UpdateBranchResultTypeDef

```python
from mypy_boto3_amplify.type_defs import UpdateBranchResultTypeDef
```


Required fields:
- `branch`: `"BranchTypeDef"`




## UpdateDomainAssociationResultTypeDef

```python
from mypy_boto3_amplify.type_defs import UpdateDomainAssociationResultTypeDef
```


Required fields:
- `domainAssociation`: `"DomainAssociationTypeDef"`




## UpdateWebhookResultTypeDef

```python
from mypy_boto3_amplify.type_defs import UpdateWebhookResultTypeDef
```


Required fields:
- `webhook`: `"WebhookTypeDef"`



