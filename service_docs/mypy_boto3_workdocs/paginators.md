# Paginators for boto3 WorkDocs module

> [Index](../index.md) > [WorkDocs](./index.md) > Paginators

Auto-generated documentation for [WorkDocs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs)
type annotations stubs module [mypy_boto3_workdocs](https://pypi.org/project/mypy-boto3-workdocs/).

- [Paginators for boto3 WorkDocs module](#paginators-for-boto3-workdocs-module)
  - [DescribeActivitiesPaginator](#describeactivitiespaginator)
  - [DescribeCommentsPaginator](#describecommentspaginator)
  - [DescribeDocumentVersionsPaginator](#describedocumentversionspaginator)
  - [DescribeFolderContentsPaginator](#describefoldercontentspaginator)
  - [DescribeGroupsPaginator](#describegroupspaginator)
  - [DescribeNotificationSubscriptionsPaginator](#describenotificationsubscriptionspaginator)
  - [DescribeResourcePermissionsPaginator](#describeresourcepermissionspaginator)
  - [DescribeRootFoldersPaginator](#describerootfolderspaginator)
  - [DescribeUsersPaginator](#describeuserspaginator)

## DescribeActivitiesPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_activities")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeActivitiesPaginator

def get_describe_activities_paginator() -> DescribeActivitiesPaginator:
    return boto3.client("workdocs").get_paginator("describe_activities")
```

[Paginator.DescribeActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)

```python
class DescribeActivitiesPaginator(Boto3Paginator):
    def paginate(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeActivitiesResponseTypeDef]:
        pass
```
## DescribeCommentsPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_comments")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeCommentsPaginator

def get_describe_comments_paginator() -> DescribeCommentsPaginator:
    return boto3.client("workdocs").get_paginator("describe_comments")
```

[Paginator.DescribeComments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)

```python
class DescribeCommentsPaginator(Boto3Paginator):
    def paginate(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCommentsResponseTypeDef]:
        pass
```
## DescribeDocumentVersionsPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_document_versions")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeDocumentVersionsPaginator

def get_describe_document_versions_paginator() -> DescribeDocumentVersionsPaginator:
    return boto3.client("workdocs").get_paginator("describe_document_versions")
```

[Paginator.DescribeDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)

```python
class DescribeDocumentVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Include: str = None,
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDocumentVersionsResponseTypeDef]:
        pass
```
## DescribeFolderContentsPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_folder_contents")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeFolderContentsPaginator

def get_describe_folder_contents_paginator() -> DescribeFolderContentsPaginator:
    return boto3.client("workdocs").get_paginator("describe_folder_contents")
```

[Paginator.DescribeFolderContents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)

```python
class DescribeFolderContentsPaginator(Boto3Paginator):
    def paginate(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: ResourceSortType = None,
        Order: OrderType = None,
        Type: FolderContentType = None,
        Include: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFolderContentsResponseTypeDef]:
        pass
```
## DescribeGroupsPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_groups")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeGroupsPaginator

def get_describe_groups_paginator() -> DescribeGroupsPaginator:
    return boto3.client("workdocs").get_paginator("describe_groups")
```

[Paginator.DescribeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)

```python
class DescribeGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGroupsResponseTypeDef]:
        pass
```
## DescribeNotificationSubscriptionsPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_notification_subscriptions")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeNotificationSubscriptionsPaginator

def get_describe_notification_subscriptions_paginator() -> DescribeNotificationSubscriptionsPaginator:
    return boto3.client("workdocs").get_paginator("describe_notification_subscriptions")
```

[Paginator.DescribeNotificationSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)

```python
class DescribeNotificationSubscriptionsPaginator(Boto3Paginator):
    def paginate(
        self,
        OrganizationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNotificationSubscriptionsResponseTypeDef]:
        pass
```
## DescribeResourcePermissionsPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_resource_permissions")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeResourcePermissionsPaginator

def get_describe_resource_permissions_paginator() -> DescribeResourcePermissionsPaginator:
    return boto3.client("workdocs").get_paginator("describe_resource_permissions")
```

[Paginator.DescribeResourcePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)

```python
class DescribeResourcePermissionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourcePermissionsResponseTypeDef]:
        pass
```
## DescribeRootFoldersPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_root_folders")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeRootFoldersPaginator

def get_describe_root_folders_paginator() -> DescribeRootFoldersPaginator:
    return boto3.client("workdocs").get_paginator("describe_root_folders")
```

[Paginator.DescribeRootFolders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)

```python
class DescribeRootFoldersPaginator(Boto3Paginator):
    def paginate(
        self,
        AuthenticationToken: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRootFoldersResponseTypeDef]:
        pass
```
## DescribeUsersPaginator

Type annotations for `boto3.client("workdocs").get_paginator("describe_users")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeUsersPaginator

def get_describe_users_paginator() -> DescribeUsersPaginator:
    return boto3.client("workdocs").get_paginator("describe_users")
```

[Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)

```python
class DescribeUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: UserFilterType = None,
        Order: OrderType = None,
        Sort: UserSortType = None,
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUsersResponseTypeDef]:
        pass
```