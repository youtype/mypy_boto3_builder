# Paginators for boto3 CodeDeploy module

> [Index](../index.md) > [CodeDeploy](./index.md) > Paginators

Auto-generated documentation for [CodeDeploy](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy)
type annotations stubs module [mypy_boto3_codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/).

- [Paginators for boto3 CodeDeploy module](#paginators-for-boto3-codedeploy-module)
  - [ListApplicationRevisionsPaginator](#listapplicationrevisionspaginator)
  - [ListApplicationsPaginator](#listapplicationspaginator)
  - [ListDeploymentConfigsPaginator](#listdeploymentconfigspaginator)
  - [ListDeploymentGroupsPaginator](#listdeploymentgroupspaginator)
  - [ListDeploymentInstancesPaginator](#listdeploymentinstancespaginator)
  - [ListDeploymentTargetsPaginator](#listdeploymenttargetspaginator)
  - [ListDeploymentsPaginator](#listdeploymentspaginator)
  - [ListGitHubAccountTokenNamesPaginator](#listgithubaccounttokennamespaginator)
  - [ListOnPremisesInstancesPaginator](#listonpremisesinstancespaginator)

## ListApplicationRevisionsPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_application_revisions")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListApplicationRevisionsPaginator

def get_list_application_revisions_paginator() -> ListApplicationRevisionsPaginator:
    return boto3.client("codedeploy").get_paginator("list_application_revisions")
```

[Paginator.ListApplicationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplicationRevisions)

```python
class ListApplicationRevisionsPaginator(Boto3Paginator):
    def paginate(
        self,
        applicationName: str,
        sortBy: ApplicationRevisionSortBy = None,
        sortOrder: SortOrder = None,
        s3Bucket: str = None,
        s3KeyPrefix: str = None,
        deployed: ListStateFilterAction = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationRevisionsOutputTypeDef]:
        pass
```
## ListApplicationsPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_applications")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListApplicationsPaginator

def get_list_applications_paginator() -> ListApplicationsPaginator:
    return boto3.client("codedeploy").get_paginator("list_applications")
```

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListApplications)

```python
class ListApplicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsOutputTypeDef]:
        pass
```
## ListDeploymentConfigsPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_deployment_configs")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListDeploymentConfigsPaginator

def get_list_deployment_configs_paginator() -> ListDeploymentConfigsPaginator:
    return boto3.client("codedeploy").get_paginator("list_deployment_configs")
```

[Paginator.ListDeploymentConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentConfigs)

```python
class ListDeploymentConfigsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentConfigsOutputTypeDef]:
        pass
```
## ListDeploymentGroupsPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_deployment_groups")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListDeploymentGroupsPaginator

def get_list_deployment_groups_paginator() -> ListDeploymentGroupsPaginator:
    return boto3.client("codedeploy").get_paginator("list_deployment_groups")
```

[Paginator.ListDeploymentGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentGroups)

```python
class ListDeploymentGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        applicationName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentGroupsOutputTypeDef]:
        pass
```
## ListDeploymentInstancesPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_deployment_instances")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListDeploymentInstancesPaginator

def get_list_deployment_instances_paginator() -> ListDeploymentInstancesPaginator:
    return boto3.client("codedeploy").get_paginator("list_deployment_instances")
```

[Paginator.ListDeploymentInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentInstances)

```python
class ListDeploymentInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        deploymentId: str,
        instanceStatusFilter: List[InstanceStatus] = None,
        instanceTypeFilter: List[InstanceType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentInstancesOutputTypeDef]:
        pass
```
## ListDeploymentTargetsPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_deployment_targets")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListDeploymentTargetsPaginator

def get_list_deployment_targets_paginator() -> ListDeploymentTargetsPaginator:
    return boto3.client("codedeploy").get_paginator("list_deployment_targets")
```

[Paginator.ListDeploymentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeploymentTargets)

```python
class ListDeploymentTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        deploymentId: str = None,
        targetFilters: Dict[TargetFilterName, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentTargetsOutputTypeDef]:
        pass
```
## ListDeploymentsPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_deployments")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListDeploymentsPaginator

def get_list_deployments_paginator() -> ListDeploymentsPaginator:
    return boto3.client("codedeploy").get_paginator("list_deployments")
```

[Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListDeployments)

```python
class ListDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        applicationName: str = None,
        deploymentGroupName: str = None,
        externalId: str = None,
        includeOnlyStatuses: List[DeploymentStatus] = None,
        createTimeRange: TimeRangeTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsOutputTypeDef]:
        pass
```
## ListGitHubAccountTokenNamesPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_git_hub_account_token_names")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListGitHubAccountTokenNamesPaginator

def get_list_git_hub_account_token_names_paginator() -> ListGitHubAccountTokenNamesPaginator:
    return boto3.client("codedeploy").get_paginator("list_git_hub_account_token_names")
```

[Paginator.ListGitHubAccountTokenNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListGitHubAccountTokenNames)

```python
class ListGitHubAccountTokenNamesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGitHubAccountTokenNamesOutputTypeDef]:
        pass
```
## ListOnPremisesInstancesPaginator

Type annotations for `boto3.client("codedeploy").get_paginator("list_on_premises_instances")`.

Can be used directly:

```python
from mypy_boto3_codedeploy.paginators import ListOnPremisesInstancesPaginator

def get_list_on_premises_instances_paginator() -> ListOnPremisesInstancesPaginator:
    return boto3.client("codedeploy").get_paginator("list_on_premises_instances")
```

[Paginator.ListOnPremisesInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html#CodeDeploy.Paginator.ListOnPremisesInstances)

```python
class ListOnPremisesInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        registrationStatus: RegistrationStatus = None,
        tagFilters: List["TagFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOnPremisesInstancesOutputTypeDef]:
        pass
```