# Structures for boto3 PrometheusService module

> [Index](../index.md) > [PrometheusService](./index.md) > Structures

Auto-generated documentation for [PrometheusService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html#PrometheusService)
type annotations stubs module [mypy_boto3_amp](https://pypi.org/project/mypy-boto3-amp/).

- [Structures for boto3 PrometheusService module](#structures-for-boto3-prometheusservice-module)
  - [WorkspaceDescriptionTypeDef](#workspacedescriptiontypedef)
  - [WorkspaceStatusTypeDef](#workspacestatustypedef)
  - [WorkspaceSummaryTypeDef](#workspacesummarytypedef)
  - [CreateWorkspaceResponseTypeDef](#createworkspaceresponsetypedef)
  - [DescribeWorkspaceResponseTypeDef](#describeworkspaceresponsetypedef)
  - [ListWorkspacesResponseTypeDef](#listworkspacesresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)

## WorkspaceDescriptionTypeDef

```python
from mypy_boto3_amp.type_defs import WorkspaceDescriptionTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `status`: `"WorkspaceStatusTypeDef"`
- `workspaceId`: `str`



Optional fields:
- `alias`: `str`
- `prometheusEndpoint`: `str`


## WorkspaceStatusTypeDef

```python
from mypy_boto3_amp.type_defs import WorkspaceStatusTypeDef
```


Required fields:
- `statusCode`: `WorkspaceStatusCode`




## WorkspaceSummaryTypeDef

```python
from mypy_boto3_amp.type_defs import WorkspaceSummaryTypeDef
```


Required fields:
- `arn`: `str`
- `createdAt`: `datetime`
- `status`: `"WorkspaceStatusTypeDef"`
- `workspaceId`: `str`



Optional fields:
- `alias`: `str`


## CreateWorkspaceResponseTypeDef

```python
from mypy_boto3_amp.type_defs import CreateWorkspaceResponseTypeDef
```


Required fields:
- `arn`: `str`
- `status`: `"WorkspaceStatusTypeDef"`
- `workspaceId`: `str`




## DescribeWorkspaceResponseTypeDef

```python
from mypy_boto3_amp.type_defs import DescribeWorkspaceResponseTypeDef
```


Required fields:
- `workspace`: `"WorkspaceDescriptionTypeDef"`




## ListWorkspacesResponseTypeDef

```python
from mypy_boto3_amp.type_defs import ListWorkspacesResponseTypeDef
```


Required fields:
- `workspaces`: `List["WorkspaceSummaryTypeDef"]`



Optional fields:
- `nextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_amp.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`

