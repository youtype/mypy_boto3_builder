# Paginators for boto3 EMR module

> [Index](../index.md) > [EMR](./index.md) > Paginators

Auto-generated documentation for [EMR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR)
type annotations stubs module [mypy_boto3_emr](https://pypi.org/project/mypy-boto3-emr/).

- [Paginators for boto3 EMR module](#paginators-for-boto3-emr-module)
  - [ListBootstrapActionsPaginator](#listbootstrapactionspaginator)
  - [ListClustersPaginator](#listclusterspaginator)
  - [ListInstanceFleetsPaginator](#listinstancefleetspaginator)
  - [ListInstanceGroupsPaginator](#listinstancegroupspaginator)
  - [ListInstancesPaginator](#listinstancespaginator)
  - [ListNotebookExecutionsPaginator](#listnotebookexecutionspaginator)
  - [ListSecurityConfigurationsPaginator](#listsecurityconfigurationspaginator)
  - [ListStepsPaginator](#liststepspaginator)
  - [ListStudioSessionMappingsPaginator](#liststudiosessionmappingspaginator)
  - [ListStudiosPaginator](#liststudiospaginator)

## ListBootstrapActionsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_bootstrap_actions")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListBootstrapActionsPaginator

def get_list_bootstrap_actions_paginator() -> ListBootstrapActionsPaginator:
    return boto3.client("emr").get_paginator("list_bootstrap_actions")
```

[Paginator.ListBootstrapActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)

```python
class ListBootstrapActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBootstrapActionsOutputTypeDef]:
        pass
```
## ListClustersPaginator

Type annotations for `boto3.client("emr").get_paginator("list_clusters")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListClustersPaginator

def get_list_clusters_paginator() -> ListClustersPaginator:
    return boto3.client("emr").get_paginator("list_clusters")
```

[Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListClusters)

```python
class ListClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[ClusterState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersOutputTypeDef]:
        pass
```
## ListInstanceFleetsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_instance_fleets")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListInstanceFleetsPaginator

def get_list_instance_fleets_paginator() -> ListInstanceFleetsPaginator:
    return boto3.client("emr").get_paginator("list_instance_fleets")
```

[Paginator.ListInstanceFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)

```python
class ListInstanceFleetsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceFleetsOutputTypeDef]:
        pass
```
## ListInstanceGroupsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_instance_groups")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListInstanceGroupsPaginator

def get_list_instance_groups_paginator() -> ListInstanceGroupsPaginator:
    return boto3.client("emr").get_paginator("list_instance_groups")
```

[Paginator.ListInstanceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)

```python
class ListInstanceGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceGroupsOutputTypeDef]:
        pass
```
## ListInstancesPaginator

Type annotations for `boto3.client("emr").get_paginator("list_instances")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListInstancesPaginator

def get_list_instances_paginator() -> ListInstancesPaginator:
    return boto3.client("emr").get_paginator("list_instances")
```

[Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListInstances)

```python
class ListInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[InstanceGroupType] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: InstanceFleetType = None,
        InstanceStates: List[InstanceState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesOutputTypeDef]:
        pass
```
## ListNotebookExecutionsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_notebook_executions")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListNotebookExecutionsPaginator

def get_list_notebook_executions_paginator() -> ListNotebookExecutionsPaginator:
    return boto3.client("emr").get_paginator("list_notebook_executions")
```

[Paginator.ListNotebookExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions)

```python
class ListNotebookExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        EditorId: str = None,
        Status: NotebookExecutionStatus = None,
        From: datetime = None,
        To: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotebookExecutionsOutputTypeDef]:
        pass
```
## ListSecurityConfigurationsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_security_configurations")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListSecurityConfigurationsPaginator

def get_list_security_configurations_paginator() -> ListSecurityConfigurationsPaginator:
    return boto3.client("emr").get_paginator("list_security_configurations")
```

[Paginator.ListSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)

```python
class ListSecurityConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityConfigurationsOutputTypeDef]:
        pass
```
## ListStepsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_steps")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListStepsPaginator

def get_list_steps_paginator() -> ListStepsPaginator:
    return boto3.client("emr").get_paginator("list_steps")
```

[Paginator.ListSteps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListSteps)

```python
class ListStepsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterId: str,
        StepStates: List[StepState] = None,
        StepIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStepsOutputTypeDef]:
        pass
```
## ListStudioSessionMappingsPaginator

Type annotations for `boto3.client("emr").get_paginator("list_studio_session_mappings")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListStudioSessionMappingsPaginator

def get_list_studio_session_mappings_paginator() -> ListStudioSessionMappingsPaginator:
    return boto3.client("emr").get_paginator("list_studio_session_mappings")
```

[Paginator.ListStudioSessionMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings)

```python
class ListStudioSessionMappingsPaginator(Boto3Paginator):
    def paginate(
        self,
        StudioId: str = None,
        IdentityType: IdentityType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudioSessionMappingsOutputTypeDef]:
        pass
```
## ListStudiosPaginator

Type annotations for `boto3.client("emr").get_paginator("list_studios")`.

Can be used directly:

```python
from mypy_boto3_emr.paginators import ListStudiosPaginator

def get_list_studios_paginator() -> ListStudiosPaginator:
    return boto3.client("emr").get_paginator("list_studios")
```

[Paginator.ListStudios documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Paginator.ListStudios)

```python
class ListStudiosPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudiosOutputTypeDef]:
        pass
```