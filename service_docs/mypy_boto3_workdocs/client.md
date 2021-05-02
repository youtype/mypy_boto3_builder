# WorkDocsClient for boto3 WorkDocs module

> [Index](../index.md) > [WorkDocs](./index.md) > WorkDocsClient

Auto-generated documentation for [WorkDocs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs)
type annotations stubs module [mypy_boto3_workdocs](https://pypi.org/project/mypy-boto3-workdocs/).

- [WorkDocsClient for boto3 WorkDocs module](#workdocsclient-for-boto3-workdocs-module)
  - [WorkDocsClient](#workdocsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [abort_document_version_upload](#abort_document_version_upload)
    - [activate_user](#activate_user)
    - [add_resource_permissions](#add_resource_permissions)
    - [can_paginate](#can_paginate)
    - [create_comment](#create_comment)
    - [create_custom_metadata](#create_custom_metadata)
    - [create_folder](#create_folder)
    - [create_labels](#create_labels)
    - [create_notification_subscription](#create_notification_subscription)
    - [create_user](#create_user)
    - [deactivate_user](#deactivate_user)
    - [delete_comment](#delete_comment)
    - [delete_custom_metadata](#delete_custom_metadata)
    - [delete_document](#delete_document)
    - [delete_folder](#delete_folder)
    - [delete_folder_contents](#delete_folder_contents)
    - [delete_labels](#delete_labels)
    - [delete_notification_subscription](#delete_notification_subscription)
    - [delete_user](#delete_user)
    - [describe_activities](#describe_activities)
    - [describe_comments](#describe_comments)
    - [describe_document_versions](#describe_document_versions)
    - [describe_folder_contents](#describe_folder_contents)
    - [describe_groups](#describe_groups)
    - [describe_notification_subscriptions](#describe_notification_subscriptions)
    - [describe_resource_permissions](#describe_resource_permissions)
    - [describe_root_folders](#describe_root_folders)
    - [describe_users](#describe_users)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_current_user](#get_current_user)
    - [get_document](#get_document)
    - [get_document_path](#get_document_path)
    - [get_document_version](#get_document_version)
    - [get_folder](#get_folder)
    - [get_folder_path](#get_folder_path)
    - [get_resources](#get_resources)
    - [initiate_document_version_upload](#initiate_document_version_upload)
    - [remove_all_resource_permissions](#remove_all_resource_permissions)
    - [remove_resource_permission](#remove_resource_permission)
    - [update_document](#update_document)
    - [update_document_version](#update_document_version)
    - [update_folder](#update_folder)
    - [update_user](#update_user)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)

## WorkDocsClient

Type annotations for `boto3.client("workdocs")`

Can be used directly:

```python
from mypy_boto3_workdocs.client import WorkDocsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_workdocs.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.ConflictingOperationException`
- `Exceptions.CustomMetadataLimitExceededException`
- `Exceptions.DeactivatingLastSystemUserException`
- `Exceptions.DocumentLockedForCommentsException`
- `Exceptions.DraftUploadOutOfSyncException`
- `Exceptions.EntityAlreadyExistsException`
- `Exceptions.EntityNotExistsException`
- `Exceptions.FailedDependencyException`
- `Exceptions.IllegalUserStateException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.InvalidCommentOperationException`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidPasswordException`
- `Exceptions.LimitExceededException`
- `Exceptions.ProhibitedStateException`
- `Exceptions.RequestedEntityTooLargeException`
- `Exceptions.ResourceAlreadyCheckedOutException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.StorageLimitExceededException`
- `Exceptions.StorageLimitWillExceedException`
- `Exceptions.TooManyLabelsException`
- `Exceptions.TooManySubscriptionsException`
- `Exceptions.UnauthorizedOperationException`
- `Exceptions.UnauthorizedResourceAccessException`


## Methods


### abort_document_version_upload

Type annotations for `boto3.client("workdocs").abort_document_version_upload` method.

[Client.abort_document_version_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.abort_document_version_upload)

```python
def abort_document_version_upload(
    self,
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### activate_user

Type annotations for `boto3.client("workdocs").activate_user` method.

[Client.activate_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.activate_user)

```python
def activate_user(
    self,
    UserId: str,
    AuthenticationToken: str = None
) -> ActivateUserResponseTypeDef:
    pass
```

### add_resource_permissions

Type annotations for `boto3.client("workdocs").add_resource_permissions` method.

[Client.add_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.add_resource_permissions)

```python
def add_resource_permissions(
    self,
    ResourceId: str,
    Principals: List[SharePrincipalTypeDef],
    AuthenticationToken: str = None,
    NotificationOptions: NotificationOptionsTypeDef = None
) -> AddResourcePermissionsResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("workdocs").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_comment

Type annotations for `boto3.client("workdocs").create_comment` method.

[Client.create_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.create_comment)

```python
def create_comment(
    self,
    DocumentId: str,
    VersionId: str,
    Text: str,
    AuthenticationToken: str = None,
    ParentId: str = None,
    ThreadId: str = None,
    Visibility: CommentVisibilityType = None,
    NotifyCollaborators: bool = None
) -> CreateCommentResponseTypeDef:
    pass
```

### create_custom_metadata

Type annotations for `boto3.client("workdocs").create_custom_metadata` method.

[Client.create_custom_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.create_custom_metadata)

```python
def create_custom_metadata(
    self,
    ResourceId: str,
    CustomMetadata: Dict[str, str],
    AuthenticationToken: str = None,
    VersionId: str = None
) -> Dict[str, Any]:
    pass
```

### create_folder

Type annotations for `boto3.client("workdocs").create_folder` method.

[Client.create_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.create_folder)

```python
def create_folder(
    self,
    ParentFolderId: str,
    AuthenticationToken: str = None,
    Name: str = None
) -> CreateFolderResponseTypeDef:
    pass
```

### create_labels

Type annotations for `boto3.client("workdocs").create_labels` method.

[Client.create_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.create_labels)

```python
def create_labels(
    self,
    ResourceId: str,
    Labels: List[str],
    AuthenticationToken: str = None
) -> Dict[str, Any]:
    pass
```

### create_notification_subscription

Type annotations for `boto3.client("workdocs").create_notification_subscription` method.

[Client.create_notification_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.create_notification_subscription)

```python
def create_notification_subscription(
    self,
    OrganizationId: str,
    Endpoint: str,
    Protocol: SubscriptionProtocolType,
    SubscriptionType: SubscriptionType
) -> CreateNotificationSubscriptionResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("workdocs").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.create_user)

```python
def create_user(
    self,
    Username: str,
    GivenName: str,
    Surname: str,
    Password: str,
    OrganizationId: str = None,
    EmailAddress: str = None,
    TimeZoneId: str = None,
    StorageRule: "StorageRuleTypeTypeDef" = None,
    AuthenticationToken: str = None
) -> CreateUserResponseTypeDef:
    pass
```

### deactivate_user

Type annotations for `boto3.client("workdocs").deactivate_user` method.

[Client.deactivate_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.deactivate_user)

```python
def deactivate_user(
    self,
    UserId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### delete_comment

Type annotations for `boto3.client("workdocs").delete_comment` method.

[Client.delete_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_comment)

```python
def delete_comment(
    self,
    DocumentId: str,
    VersionId: str,
    CommentId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### delete_custom_metadata

Type annotations for `boto3.client("workdocs").delete_custom_metadata` method.

[Client.delete_custom_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_custom_metadata)

```python
def delete_custom_metadata(
    self,
    ResourceId: str,
    AuthenticationToken: str = None,
    VersionId: str = None,
    Keys: List[str] = None,
    DeleteAll: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_document

Type annotations for `boto3.client("workdocs").delete_document` method.

[Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_document)

```python
def delete_document(
    self,
    DocumentId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### delete_folder

Type annotations for `boto3.client("workdocs").delete_folder` method.

[Client.delete_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_folder)

```python
def delete_folder(
    self,
    FolderId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### delete_folder_contents

Type annotations for `boto3.client("workdocs").delete_folder_contents` method.

[Client.delete_folder_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_folder_contents)

```python
def delete_folder_contents(
    self,
    FolderId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### delete_labels

Type annotations for `boto3.client("workdocs").delete_labels` method.

[Client.delete_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_labels)

```python
def delete_labels(
    self,
    ResourceId: str,
    AuthenticationToken: str = None,
    Labels: List[str] = None,
    DeleteAll: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_notification_subscription

Type annotations for `boto3.client("workdocs").delete_notification_subscription` method.

[Client.delete_notification_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_notification_subscription)

```python
def delete_notification_subscription(
    self,
    SubscriptionId: str,
    OrganizationId: str
) -> None:
    pass
```

### delete_user

Type annotations for `boto3.client("workdocs").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.delete_user)

```python
def delete_user(
    self,
    UserId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### describe_activities

Type annotations for `boto3.client("workdocs").describe_activities` method.

[Client.describe_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_activities)

```python
def describe_activities(
    self,
    AuthenticationToken: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    OrganizationId: str = None,
    ActivityTypes: str = None,
    ResourceId: str = None,
    UserId: str = None,
    IncludeIndirectActivities: bool = None,
    Limit: int = None,
    Marker: str = None
) -> DescribeActivitiesResponseTypeDef:
    pass
```

### describe_comments

Type annotations for `boto3.client("workdocs").describe_comments` method.

[Client.describe_comments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_comments)

```python
def describe_comments(
    self,
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    Limit: int = None,
    Marker: str = None
) -> DescribeCommentsResponseTypeDef:
    pass
```

### describe_document_versions

Type annotations for `boto3.client("workdocs").describe_document_versions` method.

[Client.describe_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_document_versions)

```python
def describe_document_versions(
    self,
    DocumentId: str,
    AuthenticationToken: str = None,
    Marker: str = None,
    Limit: int = None,
    Include: str = None,
    Fields: str = None
) -> DescribeDocumentVersionsResponseTypeDef:
    pass
```

### describe_folder_contents

Type annotations for `boto3.client("workdocs").describe_folder_contents` method.

[Client.describe_folder_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_folder_contents)

```python
def describe_folder_contents(
    self,
    FolderId: str,
    AuthenticationToken: str = None,
    Sort: ResourceSortType = None,
    Order: OrderType = None,
    Limit: int = None,
    Marker: str = None,
    Type: FolderContentType = None,
    Include: str = None
) -> DescribeFolderContentsResponseTypeDef:
    pass
```

### describe_groups

Type annotations for `boto3.client("workdocs").describe_groups` method.

[Client.describe_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_groups)

```python
def describe_groups(
    self,
    SearchQuery: str,
    AuthenticationToken: str = None,
    OrganizationId: str = None,
    Marker: str = None,
    Limit: int = None
) -> DescribeGroupsResponseTypeDef:
    pass
```

### describe_notification_subscriptions

Type annotations for `boto3.client("workdocs").describe_notification_subscriptions` method.

[Client.describe_notification_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_notification_subscriptions)

```python
def describe_notification_subscriptions(
    self,
    OrganizationId: str,
    Marker: str = None,
    Limit: int = None
) -> DescribeNotificationSubscriptionsResponseTypeDef:
    pass
```

### describe_resource_permissions

Type annotations for `boto3.client("workdocs").describe_resource_permissions` method.

[Client.describe_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_resource_permissions)

```python
def describe_resource_permissions(
    self,
    ResourceId: str,
    AuthenticationToken: str = None,
    PrincipalId: str = None,
    Limit: int = None,
    Marker: str = None
) -> DescribeResourcePermissionsResponseTypeDef:
    pass
```

### describe_root_folders

Type annotations for `boto3.client("workdocs").describe_root_folders` method.

[Client.describe_root_folders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_root_folders)

```python
def describe_root_folders(
    self,
    AuthenticationToken: str,
    Limit: int = None,
    Marker: str = None
) -> DescribeRootFoldersResponseTypeDef:
    pass
```

### describe_users

Type annotations for `boto3.client("workdocs").describe_users` method.

[Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.describe_users)

```python
def describe_users(
    self,
    AuthenticationToken: str = None,
    OrganizationId: str = None,
    UserIds: str = None,
    Query: str = None,
    Include: UserFilterType = None,
    Order: OrderType = None,
    Sort: UserSortType = None,
    Marker: str = None,
    Limit: int = None,
    Fields: str = None
) -> DescribeUsersResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("workdocs").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.generate_presigned_url)

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

### get_current_user

Type annotations for `boto3.client("workdocs").get_current_user` method.

[Client.get_current_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_current_user)

```python
def get_current_user(
    self,
    AuthenticationToken: str
) -> GetCurrentUserResponseTypeDef:
    pass
```

### get_document

Type annotations for `boto3.client("workdocs").get_document` method.

[Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_document)

```python
def get_document(
    self,
    DocumentId: str,
    AuthenticationToken: str = None,
    IncludeCustomMetadata: bool = None
) -> GetDocumentResponseTypeDef:
    pass
```

### get_document_path

Type annotations for `boto3.client("workdocs").get_document_path` method.

[Client.get_document_path documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_document_path)

```python
def get_document_path(
    self,
    DocumentId: str,
    AuthenticationToken: str = None,
    Limit: int = None,
    Fields: str = None,
    Marker: str = None
) -> GetDocumentPathResponseTypeDef:
    pass
```

### get_document_version

Type annotations for `boto3.client("workdocs").get_document_version` method.

[Client.get_document_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_document_version)

```python
def get_document_version(
    self,
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    Fields: str = None,
    IncludeCustomMetadata: bool = None
) -> GetDocumentVersionResponseTypeDef:
    pass
```

### get_folder

Type annotations for `boto3.client("workdocs").get_folder` method.

[Client.get_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_folder)

```python
def get_folder(
    self,
    FolderId: str,
    AuthenticationToken: str = None,
    IncludeCustomMetadata: bool = None
) -> GetFolderResponseTypeDef:
    pass
```

### get_folder_path

Type annotations for `boto3.client("workdocs").get_folder_path` method.

[Client.get_folder_path documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_folder_path)

```python
def get_folder_path(
    self,
    FolderId: str,
    AuthenticationToken: str = None,
    Limit: int = None,
    Fields: str = None,
    Marker: str = None
) -> GetFolderPathResponseTypeDef:
    pass
```

### get_resources

Type annotations for `boto3.client("workdocs").get_resources` method.

[Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.get_resources)

```python
def get_resources(
    self,
    AuthenticationToken: str = None,
    UserId: str = None,
    CollectionType: ResourceCollectionType = None,
    Limit: int = None,
    Marker: str = None
) -> GetResourcesResponseTypeDef:
    pass
```

### initiate_document_version_upload

Type annotations for `boto3.client("workdocs").initiate_document_version_upload` method.

[Client.initiate_document_version_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.initiate_document_version_upload)

```python
def initiate_document_version_upload(
    self,
    ParentFolderId: str,
    AuthenticationToken: str = None,
    Id: str = None,
    Name: str = None,
    ContentCreatedTimestamp: datetime = None,
    ContentModifiedTimestamp: datetime = None,
    ContentType: str = None,
    DocumentSizeInBytes: int = None
) -> InitiateDocumentVersionUploadResponseTypeDef:
    pass
```

### remove_all_resource_permissions

Type annotations for `boto3.client("workdocs").remove_all_resource_permissions` method.

[Client.remove_all_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.remove_all_resource_permissions)

```python
def remove_all_resource_permissions(
    self,
    ResourceId: str,
    AuthenticationToken: str = None
) -> None:
    pass
```

### remove_resource_permission

Type annotations for `boto3.client("workdocs").remove_resource_permission` method.

[Client.remove_resource_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.remove_resource_permission)

```python
def remove_resource_permission(
    self,
    ResourceId: str,
    PrincipalId: str,
    AuthenticationToken: str = None,
    PrincipalType: PrincipalType = None
) -> None:
    pass
```

### update_document

Type annotations for `boto3.client("workdocs").update_document` method.

[Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.update_document)

```python
def update_document(
    self,
    DocumentId: str,
    AuthenticationToken: str = None,
    Name: str = None,
    ParentFolderId: str = None,
    ResourceState: ResourceStateType = None
) -> None:
    pass
```

### update_document_version

Type annotations for `boto3.client("workdocs").update_document_version` method.

[Client.update_document_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.update_document_version)

```python
def update_document_version(
    self,
    DocumentId: str,
    VersionId: str,
    AuthenticationToken: str = None,
    VersionStatus: DocumentVersionStatus = None
) -> None:
    pass
```

### update_folder

Type annotations for `boto3.client("workdocs").update_folder` method.

[Client.update_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.update_folder)

```python
def update_folder(
    self,
    FolderId: str,
    AuthenticationToken: str = None,
    Name: str = None,
    ParentFolderId: str = None,
    ResourceState: ResourceStateType = None
) -> None:
    pass
```

### update_user

Type annotations for `boto3.client("workdocs").update_user` method.

[Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client.update_user)

```python
def update_user(
    self,
    UserId: str,
    AuthenticationToken: str = None,
    GivenName: str = None,
    Surname: str = None,
    Type: UserType = None,
    StorageRule: "StorageRuleTypeTypeDef" = None,
    TimeZoneId: str = None,
    Locale: LocaleType = None,
    GrantPoweruserPrivileges: BooleanEnumType = None
) -> UpdateUserResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeActivitiesPaginatorName
) -> DescribeActivitiesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeComments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeCommentsPaginatorName
) -> DescribeCommentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeDocumentVersionsPaginatorName
) -> DescribeDocumentVersionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeFolderContents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeFolderContentsPaginatorName
) -> DescribeFolderContentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeGroupsPaginatorName
) -> DescribeGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeNotificationSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeNotificationSubscriptionsPaginatorName
) -> DescribeNotificationSubscriptionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeResourcePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeResourcePermissionsPaginatorName
) -> DescribeResourcePermissionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeRootFolders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeRootFoldersPaginatorName
) -> DescribeRootFoldersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workdocs").get_paginator` method.

[Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeUsersPaginatorName
) -> DescribeUsersPaginator:
    pass
```