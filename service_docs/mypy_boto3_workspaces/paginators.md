# Paginators for boto3 WorkSpaces module

> [Index](../index.md) > [WorkSpaces](./index.md) > Paginators

Auto-generated documentation for [WorkSpaces](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces)
type annotations stubs module [mypy_boto3_workspaces](https://pypi.org/project/mypy-boto3-workspaces/).

- [Paginators for boto3 WorkSpaces module](#paginators-for-boto3-workspaces-module)
  - [DescribeAccountModificationsPaginator](#describeaccountmodificationspaginator)
  - [DescribeIpGroupsPaginator](#describeipgroupspaginator)
  - [DescribeWorkspaceBundlesPaginator](#describeworkspacebundlespaginator)
  - [DescribeWorkspaceDirectoriesPaginator](#describeworkspacedirectoriespaginator)
  - [DescribeWorkspaceImagesPaginator](#describeworkspaceimagespaginator)
  - [DescribeWorkspacesPaginator](#describeworkspacespaginator)
  - [DescribeWorkspacesConnectionStatusPaginator](#describeworkspacesconnectionstatuspaginator)
  - [ListAvailableManagementCidrRangesPaginator](#listavailablemanagementcidrrangespaginator)

## DescribeAccountModificationsPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_account_modifications")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeAccountModificationsPaginator

def get_describe_account_modifications_paginator() -> DescribeAccountModificationsPaginator:
    return boto3.client("workspaces").get_paginator("describe_account_modifications")
```

[Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)

```python
class DescribeAccountModificationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountModificationsResultTypeDef]:
        pass
```
## DescribeIpGroupsPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_ip_groups")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeIpGroupsPaginator

def get_describe_ip_groups_paginator() -> DescribeIpGroupsPaginator:
    return boto3.client("workspaces").get_paginator("describe_ip_groups")
```

[Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)

```python
class DescribeIpGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpGroupsResultTypeDef]:
        pass
```
## DescribeWorkspaceBundlesPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_workspace_bundles")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeWorkspaceBundlesPaginator

def get_describe_workspace_bundles_paginator() -> DescribeWorkspaceBundlesPaginator:
    return boto3.client("workspaces").get_paginator("describe_workspace_bundles")
```

[Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)

```python
class DescribeWorkspaceBundlesPaginator(Boto3Paginator):
    def paginate(
        self,
        BundleIds: List[str] = None,
        Owner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspaceBundlesResultTypeDef]:
        pass
```
## DescribeWorkspaceDirectoriesPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_workspace_directories")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeWorkspaceDirectoriesPaginator

def get_describe_workspace_directories_paginator() -> DescribeWorkspaceDirectoriesPaginator:
    return boto3.client("workspaces").get_paginator("describe_workspace_directories")
```

[Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)

```python
class DescribeWorkspaceDirectoriesPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryIds: List[str] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspaceDirectoriesResultTypeDef]:
        pass
```
## DescribeWorkspaceImagesPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_workspace_images")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeWorkspaceImagesPaginator

def get_describe_workspace_images_paginator() -> DescribeWorkspaceImagesPaginator:
    return boto3.client("workspaces").get_paginator("describe_workspace_images")
```

[Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)

```python
class DescribeWorkspaceImagesPaginator(Boto3Paginator):
    def paginate(
        self,
        ImageIds: List[str] = None,
        ImageType: ImageType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspaceImagesResultTypeDef]:
        pass
```
## DescribeWorkspacesPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_workspaces")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeWorkspacesPaginator

def get_describe_workspaces_paginator() -> DescribeWorkspacesPaginator:
    return boto3.client("workspaces").get_paginator("describe_workspaces")
```

[Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)

```python
class DescribeWorkspacesPaginator(Boto3Paginator):
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspacesResultTypeDef]:
        pass
```
## DescribeWorkspacesConnectionStatusPaginator

Type annotations for `boto3.client("workspaces").get_paginator("describe_workspaces_connection_status")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeWorkspacesConnectionStatusPaginator

def get_describe_workspaces_connection_status_paginator() -> DescribeWorkspacesConnectionStatusPaginator:
    return boto3.client("workspaces").get_paginator("describe_workspaces_connection_status")
```

[Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)

```python
class DescribeWorkspacesConnectionStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspacesConnectionStatusResultTypeDef]:
        pass
```
## ListAvailableManagementCidrRangesPaginator

Type annotations for `boto3.client("workspaces").get_paginator("list_available_management_cidr_ranges")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import ListAvailableManagementCidrRangesPaginator

def get_list_available_management_cidr_ranges_paginator() -> ListAvailableManagementCidrRangesPaginator:
    return boto3.client("workspaces").get_paginator("list_available_management_cidr_ranges")
```

[Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)

```python
class ListAvailableManagementCidrRangesPaginator(Boto3Paginator):
    def paginate(
        self,
        ManagementCidrRangeConstraint: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAvailableManagementCidrRangesResultTypeDef]:
        pass
```