# Type annotations for boto3 PrometheusService module

> [Index](../index.md) > PrometheusService

Auto-generated documentation for [PrometheusService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService)
type annotations stubs module [mypy_boto3_amp](https://pypi.org/project/mypy-boto3-amp/).

```bash
pip install mypy-boto3-amp
```

- [Type annotations for boto3 PrometheusService module](#type-annotations-for-boto3-prometheusservice-module)
  - [PrometheusServiceClient](#prometheusserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## PrometheusServiceClient

Type annotations for  `boto3.client("amp")` as [PrometheusServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_amp.client import PrometheusServiceClient
```


PrometheusServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_workspace](./client.md#create-workspace)
- [delete_workspace](./client.md#delete-workspace)
- [describe_workspace](./client.md#describe-workspace)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_workspaces](./client.md#list-workspaces)
- [update_workspace_alias](./client.md#update-workspace-alias)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("amp").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_amp.paginators import ListWorkspacesPaginator, ...
```

- [ListWorkspacesPaginator](./paginators.md#listworkspacespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_amp.literals import ListWorkspacesPaginatorName, ...
```

- [ListWorkspacesPaginatorName](./literals.md#listworkspacespaginatorname)
- [WorkspaceStatusCode](./literals.md#workspacestatuscode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_amp.type_defs import WorkspaceDescriptionTypeDef, ...
```

- [WorkspaceDescriptionTypeDef](./type_defs.md#workspacedescriptiontypedef)
- [WorkspaceStatusTypeDef](./type_defs.md#workspacestatustypedef)
- [WorkspaceSummaryTypeDef](./type_defs.md#workspacesummarytypedef)
- [CreateWorkspaceResponseTypeDef](./type_defs.md#createworkspaceresponsetypedef)
- [DescribeWorkspaceResponseTypeDef](./type_defs.md#describeworkspaceresponsetypedef)
- [ListWorkspacesResponseTypeDef](./type_defs.md#listworkspacesresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
