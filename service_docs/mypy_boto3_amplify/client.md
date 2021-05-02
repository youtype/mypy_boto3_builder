# AmplifyClient for boto3 Amplify module

> [Index](../index.md) > [Amplify](./index.md) > AmplifyClient

Auto-generated documentation for [Amplify](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify)
type annotations stubs module [mypy_boto3_amplify](https://pypi.org/project/mypy-boto3-amplify/).

- [AmplifyClient for boto3 Amplify module](#amplifyclient-for-boto3-amplify-module)
  - [AmplifyClient](#amplifyclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_app](#create_app)
    - [create_backend_environment](#create_backend_environment)
    - [create_branch](#create_branch)
    - [create_deployment](#create_deployment)
    - [create_domain_association](#create_domain_association)
    - [create_webhook](#create_webhook)
    - [delete_app](#delete_app)
    - [delete_backend_environment](#delete_backend_environment)
    - [delete_branch](#delete_branch)
    - [delete_domain_association](#delete_domain_association)
    - [delete_job](#delete_job)
    - [delete_webhook](#delete_webhook)
    - [generate_access_logs](#generate_access_logs)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_app](#get_app)
    - [get_artifact_url](#get_artifact_url)
    - [get_backend_environment](#get_backend_environment)
    - [get_branch](#get_branch)
    - [get_domain_association](#get_domain_association)
    - [get_job](#get_job)
    - [get_webhook](#get_webhook)
    - [list_apps](#list_apps)
    - [list_artifacts](#list_artifacts)
    - [list_backend_environments](#list_backend_environments)
    - [list_branches](#list_branches)
    - [list_domain_associations](#list_domain_associations)
    - [list_jobs](#list_jobs)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_webhooks](#list_webhooks)
    - [start_deployment](#start_deployment)
    - [start_job](#start_job)
    - [stop_job](#stop_job)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_app](#update_app)
    - [update_branch](#update_branch)
    - [update_domain_association](#update_domain_association)
    - [update_webhook](#update_webhook)
    - [get_paginator](#get_paginator)

## AmplifyClient

Type annotations for `boto3.client("amplify")`

Can be used directly:

```python
from mypy_boto3_amplify.client import AmplifyClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_amplify.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.DependentServiceFailureException`
- `Exceptions.InternalFailureException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("amplify").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_app

Type annotations for `boto3.client("amplify").create_app` method.

[Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.create_app)

```python
def create_app(
    self,
    name: str,
    description: str = None,
    repository: str = None,
    platform: Literal['WEB'] = None,
    iamServiceRoleArn: str = None,
    oauthToken: str = None,
    accessToken: str = None,
    environmentVariables: Dict[str, str] = None,
    enableBranchAutoBuild: bool = None,
    enableBranchAutoDeletion: bool = None,
    enableBasicAuth: bool = None,
    basicAuthCredentials: str = None,
    customRules: List["CustomRuleTypeDef"] = None,
    tags: Dict[str, str] = None,
    buildSpec: str = None,
    customHeaders: str = None,
    enableAutoBranchCreation: bool = None,
    autoBranchCreationPatterns: List[str] = None,
    autoBranchCreationConfig: "AutoBranchCreationConfigTypeDef" = None
) -> CreateAppResultTypeDef:
    pass
```

### create_backend_environment

Type annotations for `boto3.client("amplify").create_backend_environment` method.

[Client.create_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.create_backend_environment)

```python
def create_backend_environment(
    self,
    appId: str,
    environmentName: str,
    stackName: str = None,
    deploymentArtifacts: str = None
) -> CreateBackendEnvironmentResultTypeDef:
    pass
```

### create_branch

Type annotations for `boto3.client("amplify").create_branch` method.

[Client.create_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.create_branch)

```python
def create_branch(
    self,
    appId: str,
    branchName: str,
    description: str = None,
    stage: Stage = None,
    framework: str = None,
    enableNotification: bool = None,
    enableAutoBuild: bool = None,
    environmentVariables: Dict[str, str] = None,
    basicAuthCredentials: str = None,
    enableBasicAuth: bool = None,
    enablePerformanceMode: bool = None,
    tags: Dict[str, str] = None,
    buildSpec: str = None,
    ttl: str = None,
    displayName: str = None,
    enablePullRequestPreview: bool = None,
    pullRequestEnvironmentName: str = None,
    backendEnvironmentArn: str = None
) -> CreateBranchResultTypeDef:
    pass
```

### create_deployment

Type annotations for `boto3.client("amplify").create_deployment` method.

[Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.create_deployment)

```python
def create_deployment(
    self,
    appId: str,
    branchName: str,
    fileMap: Dict[str, str] = None
) -> CreateDeploymentResultTypeDef:
    pass
```

### create_domain_association

Type annotations for `boto3.client("amplify").create_domain_association` method.

[Client.create_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.create_domain_association)

```python
def create_domain_association(
    self,
    appId: str,
    domainName: str,
    subDomainSettings: List["SubDomainSettingTypeDef"],
    enableAutoSubDomain: bool = None,
    autoSubDomainCreationPatterns: List[str] = None,
    autoSubDomainIAMRole: str = None
) -> CreateDomainAssociationResultTypeDef:
    pass
```

### create_webhook

Type annotations for `boto3.client("amplify").create_webhook` method.

[Client.create_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.create_webhook)

```python
def create_webhook(
    self,
    appId: str,
    branchName: str,
    description: str = None
) -> CreateWebhookResultTypeDef:
    pass
```

### delete_app

Type annotations for `boto3.client("amplify").delete_app` method.

[Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.delete_app)

```python
def delete_app(
    self,
    appId: str
) -> DeleteAppResultTypeDef:
    pass
```

### delete_backend_environment

Type annotations for `boto3.client("amplify").delete_backend_environment` method.

[Client.delete_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.delete_backend_environment)

```python
def delete_backend_environment(
    self,
    appId: str,
    environmentName: str
) -> DeleteBackendEnvironmentResultTypeDef:
    pass
```

### delete_branch

Type annotations for `boto3.client("amplify").delete_branch` method.

[Client.delete_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.delete_branch)

```python
def delete_branch(
    self,
    appId: str,
    branchName: str
) -> DeleteBranchResultTypeDef:
    pass
```

### delete_domain_association

Type annotations for `boto3.client("amplify").delete_domain_association` method.

[Client.delete_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.delete_domain_association)

```python
def delete_domain_association(
    self,
    appId: str,
    domainName: str
) -> DeleteDomainAssociationResultTypeDef:
    pass
```

### delete_job

Type annotations for `boto3.client("amplify").delete_job` method.

[Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.delete_job)

```python
def delete_job(
    self,
    appId: str,
    branchName: str,
    jobId: str
) -> DeleteJobResultTypeDef:
    pass
```

### delete_webhook

Type annotations for `boto3.client("amplify").delete_webhook` method.

[Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.delete_webhook)

```python
def delete_webhook(
    self,
    webhookId: str
) -> DeleteWebhookResultTypeDef:
    pass
```

### generate_access_logs

Type annotations for `boto3.client("amplify").generate_access_logs` method.

[Client.generate_access_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.generate_access_logs)

```python
def generate_access_logs(
    self,
    domainName: str,
    appId: str,
    startTime: datetime = None,
    endTime: datetime = None
) -> GenerateAccessLogsResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("amplify").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.generate_presigned_url)

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

### get_app

Type annotations for `boto3.client("amplify").get_app` method.

[Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_app)

```python
def get_app(
    self,
    appId: str
) -> GetAppResultTypeDef:
    pass
```

### get_artifact_url

Type annotations for `boto3.client("amplify").get_artifact_url` method.

[Client.get_artifact_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_artifact_url)

```python
def get_artifact_url(
    self,
    artifactId: str
) -> GetArtifactUrlResultTypeDef:
    pass
```

### get_backend_environment

Type annotations for `boto3.client("amplify").get_backend_environment` method.

[Client.get_backend_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_backend_environment)

```python
def get_backend_environment(
    self,
    appId: str,
    environmentName: str
) -> GetBackendEnvironmentResultTypeDef:
    pass
```

### get_branch

Type annotations for `boto3.client("amplify").get_branch` method.

[Client.get_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_branch)

```python
def get_branch(
    self,
    appId: str,
    branchName: str
) -> GetBranchResultTypeDef:
    pass
```

### get_domain_association

Type annotations for `boto3.client("amplify").get_domain_association` method.

[Client.get_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_domain_association)

```python
def get_domain_association(
    self,
    appId: str,
    domainName: str
) -> GetDomainAssociationResultTypeDef:
    pass
```

### get_job

Type annotations for `boto3.client("amplify").get_job` method.

[Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_job)

```python
def get_job(
    self,
    appId: str,
    branchName: str,
    jobId: str
) -> GetJobResultTypeDef:
    pass
```

### get_webhook

Type annotations for `boto3.client("amplify").get_webhook` method.

[Client.get_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.get_webhook)

```python
def get_webhook(
    self,
    webhookId: str
) -> GetWebhookResultTypeDef:
    pass
```

### list_apps

Type annotations for `boto3.client("amplify").list_apps` method.

[Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_apps)

```python
def list_apps(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListAppsResultTypeDef:
    pass
```

### list_artifacts

Type annotations for `boto3.client("amplify").list_artifacts` method.

[Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_artifacts)

```python
def list_artifacts(
    self,
    appId: str,
    branchName: str,
    jobId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListArtifactsResultTypeDef:
    pass
```

### list_backend_environments

Type annotations for `boto3.client("amplify").list_backend_environments` method.

[Client.list_backend_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_backend_environments)

```python
def list_backend_environments(
    self,
    appId: str,
    environmentName: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListBackendEnvironmentsResultTypeDef:
    pass
```

### list_branches

Type annotations for `boto3.client("amplify").list_branches` method.

[Client.list_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_branches)

```python
def list_branches(
    self,
    appId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListBranchesResultTypeDef:
    pass
```

### list_domain_associations

Type annotations for `boto3.client("amplify").list_domain_associations` method.

[Client.list_domain_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_domain_associations)

```python
def list_domain_associations(
    self,
    appId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListDomainAssociationsResultTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("amplify").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_jobs)

```python
def list_jobs(
    self,
    appId: str,
    branchName: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListJobsResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("amplify").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_webhooks

Type annotations for `boto3.client("amplify").list_webhooks` method.

[Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.list_webhooks)

```python
def list_webhooks(
    self,
    appId: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListWebhooksResultTypeDef:
    pass
```

### start_deployment

Type annotations for `boto3.client("amplify").start_deployment` method.

[Client.start_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.start_deployment)

```python
def start_deployment(
    self,
    appId: str,
    branchName: str,
    jobId: str = None,
    sourceUrl: str = None
) -> StartDeploymentResultTypeDef:
    pass
```

### start_job

Type annotations for `boto3.client("amplify").start_job` method.

[Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.start_job)

```python
def start_job(
    self,
    appId: str,
    branchName: str,
    jobType: JobType,
    jobId: str = None,
    jobReason: str = None,
    commitId: str = None,
    commitMessage: str = None,
    commitTime: datetime = None
) -> StartJobResultTypeDef:
    pass
```

### stop_job

Type annotations for `boto3.client("amplify").stop_job` method.

[Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.stop_job)

```python
def stop_job(
    self,
    appId: str,
    branchName: str,
    jobId: str
) -> StopJobResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("amplify").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("amplify").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_app

Type annotations for `boto3.client("amplify").update_app` method.

[Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.update_app)

```python
def update_app(
    self,
    appId: str,
    name: str = None,
    description: str = None,
    platform: Literal['WEB'] = None,
    iamServiceRoleArn: str = None,
    environmentVariables: Dict[str, str] = None,
    enableBranchAutoBuild: bool = None,
    enableBranchAutoDeletion: bool = None,
    enableBasicAuth: bool = None,
    basicAuthCredentials: str = None,
    customRules: List["CustomRuleTypeDef"] = None,
    buildSpec: str = None,
    customHeaders: str = None,
    enableAutoBranchCreation: bool = None,
    autoBranchCreationPatterns: List[str] = None,
    autoBranchCreationConfig: "AutoBranchCreationConfigTypeDef" = None,
    repository: str = None,
    oauthToken: str = None,
    accessToken: str = None
) -> UpdateAppResultTypeDef:
    pass
```

### update_branch

Type annotations for `boto3.client("amplify").update_branch` method.

[Client.update_branch documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.update_branch)

```python
def update_branch(
    self,
    appId: str,
    branchName: str,
    description: str = None,
    framework: str = None,
    stage: Stage = None,
    enableNotification: bool = None,
    enableAutoBuild: bool = None,
    environmentVariables: Dict[str, str] = None,
    basicAuthCredentials: str = None,
    enableBasicAuth: bool = None,
    enablePerformanceMode: bool = None,
    buildSpec: str = None,
    ttl: str = None,
    displayName: str = None,
    enablePullRequestPreview: bool = None,
    pullRequestEnvironmentName: str = None,
    backendEnvironmentArn: str = None
) -> UpdateBranchResultTypeDef:
    pass
```

### update_domain_association

Type annotations for `boto3.client("amplify").update_domain_association` method.

[Client.update_domain_association documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.update_domain_association)

```python
def update_domain_association(
    self,
    appId: str,
    domainName: str,
    subDomainSettings: List["SubDomainSettingTypeDef"],
    enableAutoSubDomain: bool = None,
    autoSubDomainCreationPatterns: List[str] = None,
    autoSubDomainIAMRole: str = None
) -> UpdateDomainAssociationResultTypeDef:
    pass
```

### update_webhook

Type annotations for `boto3.client("amplify").update_webhook` method.

[Client.update_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html#Amplify.Client.update_webhook)

```python
def update_webhook(
    self,
    webhookId: str,
    branchName: str = None,
    description: str = None
) -> UpdateWebhookResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("amplify").get_paginator` method with overloads.

- `client.get_paginator("list_apps")` -> [ListAppsPaginator](./paginators.md#listappspaginator)
- `client.get_paginator("list_branches")` -> [ListBranchesPaginator](./paginators.md#listbranchespaginator)
- `client.get_paginator("list_domain_associations")` -> [ListDomainAssociationsPaginator](./paginators.md#listdomainassociationspaginator)
- `client.get_paginator("list_jobs")` -> [ListJobsPaginator](./paginators.md#listjobspaginator)


