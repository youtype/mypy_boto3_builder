# Type annotations for boto3 Amplify module

> [Index](../index.md) > Amplify

Auto-generated documentation for [Amplify](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify)
type annotations stubs module [mypy_boto3_amplify](https://pypi.org/project/mypy-boto3-amplify/).

```bash
pip install mypy-boto3-amplify
```

- [Type annotations for boto3 Amplify module](#type-annotations-for-boto3-amplify-module)
  - [AmplifyClient](#amplifyclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## AmplifyClient

Type annotations for  `boto3.client("amplify")` as [AmplifyClient](./client.md)

Can be used directly:

```python
from mypy_boto3_amplify.client import AmplifyClient
```


AmplifyClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_app](./client.md#create-app)
- [create_backend_environment](./client.md#create-backend-environment)
- [create_branch](./client.md#create-branch)
- [create_deployment](./client.md#create-deployment)
- [create_domain_association](./client.md#create-domain-association)
- [create_webhook](./client.md#create-webhook)
- [delete_app](./client.md#delete-app)
- [delete_backend_environment](./client.md#delete-backend-environment)
- [delete_branch](./client.md#delete-branch)
- [delete_domain_association](./client.md#delete-domain-association)
- [delete_job](./client.md#delete-job)
- [delete_webhook](./client.md#delete-webhook)
- [generate_access_logs](./client.md#generate-access-logs)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_app](./client.md#get-app)
- [get_artifact_url](./client.md#get-artifact-url)
- [get_backend_environment](./client.md#get-backend-environment)
- [get_branch](./client.md#get-branch)
- [get_domain_association](./client.md#get-domain-association)
- [get_job](./client.md#get-job)
- [get_paginator](./client.md#get-paginator)
- [get_webhook](./client.md#get-webhook)
- [list_apps](./client.md#list-apps)
- [list_artifacts](./client.md#list-artifacts)
- [list_backend_environments](./client.md#list-backend-environments)
- [list_branches](./client.md#list-branches)
- [list_domain_associations](./client.md#list-domain-associations)
- [list_jobs](./client.md#list-jobs)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_webhooks](./client.md#list-webhooks)
- [start_deployment](./client.md#start-deployment)
- [start_job](./client.md#start-job)
- [stop_job](./client.md#stop-job)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_app](./client.md#update-app)
- [update_branch](./client.md#update-branch)
- [update_domain_association](./client.md#update-domain-association)
- [update_webhook](./client.md#update-webhook)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [DependentServiceFailureException](./client.md#dependentservicefailureexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("amplify").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_amplify.paginators import ListAppsPaginator, ...
```

- [ListAppsPaginator](./paginators.md#listappspaginator)
- [ListBranchesPaginator](./paginators.md#listbranchespaginator)
- [ListDomainAssociationsPaginator](./paginators.md#listdomainassociationspaginator)
- [ListJobsPaginator](./paginators.md#listjobspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_amplify.literals import DomainStatus, ...
```

- [DomainStatus](./literals.md#domainstatus)
- [JobStatus](./literals.md#jobstatus)
- [JobType](./literals.md#jobtype)
- [ListAppsPaginatorName](./literals.md#listappspaginatorname)
- [ListBranchesPaginatorName](./literals.md#listbranchespaginatorname)
- [ListDomainAssociationsPaginatorName](./literals.md#listdomainassociationspaginatorname)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)
- [Platform](./literals.md#platform)
- [Stage](./literals.md#stage)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_amplify.type_defs import AppTypeDef, ...
```

- [AppTypeDef](./type_defs.md#apptypedef)
- [ArtifactTypeDef](./type_defs.md#artifacttypedef)
- [AutoBranchCreationConfigTypeDef](./type_defs.md#autobranchcreationconfigtypedef)
- [BackendEnvironmentTypeDef](./type_defs.md#backendenvironmenttypedef)
- [BranchTypeDef](./type_defs.md#branchtypedef)
- [CustomRuleTypeDef](./type_defs.md#customruletypedef)
- [DomainAssociationTypeDef](./type_defs.md#domainassociationtypedef)
- [JobSummaryTypeDef](./type_defs.md#jobsummarytypedef)
- [JobTypeDef](./type_defs.md#jobtypedef)
- [ProductionBranchTypeDef](./type_defs.md#productionbranchtypedef)
- [StepTypeDef](./type_defs.md#steptypedef)
- [SubDomainSettingTypeDef](./type_defs.md#subdomainsettingtypedef)
- [SubDomainTypeDef](./type_defs.md#subdomaintypedef)
- [WebhookTypeDef](./type_defs.md#webhooktypedef)
- [CreateAppResultTypeDef](./type_defs.md#createappresulttypedef)
- [CreateBackendEnvironmentResultTypeDef](./type_defs.md#createbackendenvironmentresulttypedef)
- [CreateBranchResultTypeDef](./type_defs.md#createbranchresulttypedef)
- [CreateDeploymentResultTypeDef](./type_defs.md#createdeploymentresulttypedef)
- [CreateDomainAssociationResultTypeDef](./type_defs.md#createdomainassociationresulttypedef)
- [CreateWebhookResultTypeDef](./type_defs.md#createwebhookresulttypedef)
- [DeleteAppResultTypeDef](./type_defs.md#deleteappresulttypedef)
- [DeleteBackendEnvironmentResultTypeDef](./type_defs.md#deletebackendenvironmentresulttypedef)
- [DeleteBranchResultTypeDef](./type_defs.md#deletebranchresulttypedef)
- [DeleteDomainAssociationResultTypeDef](./type_defs.md#deletedomainassociationresulttypedef)
- [DeleteJobResultTypeDef](./type_defs.md#deletejobresulttypedef)
- [DeleteWebhookResultTypeDef](./type_defs.md#deletewebhookresulttypedef)
- [GenerateAccessLogsResultTypeDef](./type_defs.md#generateaccesslogsresulttypedef)
- [GetAppResultTypeDef](./type_defs.md#getappresulttypedef)
- [GetArtifactUrlResultTypeDef](./type_defs.md#getartifacturlresulttypedef)
- [GetBackendEnvironmentResultTypeDef](./type_defs.md#getbackendenvironmentresulttypedef)
- [GetBranchResultTypeDef](./type_defs.md#getbranchresulttypedef)
- [GetDomainAssociationResultTypeDef](./type_defs.md#getdomainassociationresulttypedef)
- [GetJobResultTypeDef](./type_defs.md#getjobresulttypedef)
- [GetWebhookResultTypeDef](./type_defs.md#getwebhookresulttypedef)
- [ListAppsResultTypeDef](./type_defs.md#listappsresulttypedef)
- [ListArtifactsResultTypeDef](./type_defs.md#listartifactsresulttypedef)
- [ListBackendEnvironmentsResultTypeDef](./type_defs.md#listbackendenvironmentsresulttypedef)
- [ListBranchesResultTypeDef](./type_defs.md#listbranchesresulttypedef)
- [ListDomainAssociationsResultTypeDef](./type_defs.md#listdomainassociationsresulttypedef)
- [ListJobsResultTypeDef](./type_defs.md#listjobsresulttypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListWebhooksResultTypeDef](./type_defs.md#listwebhooksresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [StartDeploymentResultTypeDef](./type_defs.md#startdeploymentresulttypedef)
- [StartJobResultTypeDef](./type_defs.md#startjobresulttypedef)
- [StopJobResultTypeDef](./type_defs.md#stopjobresulttypedef)
- [UpdateAppResultTypeDef](./type_defs.md#updateappresulttypedef)
- [UpdateBranchResultTypeDef](./type_defs.md#updatebranchresulttypedef)
- [UpdateDomainAssociationResultTypeDef](./type_defs.md#updatedomainassociationresulttypedef)
- [UpdateWebhookResultTypeDef](./type_defs.md#updatewebhookresulttypedef)
