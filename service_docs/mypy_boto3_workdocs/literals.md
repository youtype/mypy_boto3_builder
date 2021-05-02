# Literals for boto3 WorkDocs module

> [Index](../index.md) > [WorkDocs](./index.md) > Literals

Auto-generated documentation for [WorkDocs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs)
type annotations stubs module [mypy_boto3_workdocs](https://pypi.org/project/mypy-boto3-workdocs/).

- [Literals for boto3 WorkDocs module](#literals-for-boto3-workdocs-module)
  - [ActivityType](#activitytype)
  - [BooleanEnumType](#booleanenumtype)
  - [CommentStatusType](#commentstatustype)
  - [CommentVisibilityType](#commentvisibilitytype)
  - [DescribeActivitiesPaginatorName](#describeactivitiespaginatorname)
  - [DescribeCommentsPaginatorName](#describecommentspaginatorname)
  - [DescribeDocumentVersionsPaginatorName](#describedocumentversionspaginatorname)
  - [DescribeFolderContentsPaginatorName](#describefoldercontentspaginatorname)
  - [DescribeGroupsPaginatorName](#describegroupspaginatorname)
  - [DescribeNotificationSubscriptionsPaginatorName](#describenotificationsubscriptionspaginatorname)
  - [DescribeResourcePermissionsPaginatorName](#describeresourcepermissionspaginatorname)
  - [DescribeRootFoldersPaginatorName](#describerootfolderspaginatorname)
  - [DescribeUsersPaginatorName](#describeuserspaginatorname)
  - [DocumentSourceType](#documentsourcetype)
  - [DocumentStatusType](#documentstatustype)
  - [DocumentThumbnailType](#documentthumbnailtype)
  - [DocumentVersionStatus](#documentversionstatus)
  - [FolderContentType](#foldercontenttype)
  - [LocaleType](#localetype)
  - [OrderType](#ordertype)
  - [PrincipalType](#principaltype)
  - [ResourceCollectionType](#resourcecollectiontype)
  - [ResourceSortType](#resourcesorttype)
  - [ResourceStateType](#resourcestatetype)
  - [ResourceType](#resourcetype)
  - [RolePermissionType](#rolepermissiontype)
  - [RoleType](#roletype)
  - [ShareStatusType](#sharestatustype)
  - [StorageType](#storagetype)
  - [SubscriptionProtocolType](#subscriptionprotocoltype)
  - [SubscriptionType](#subscriptiontype)
  - [UserFilterType](#userfiltertype)
  - [UserSortType](#usersorttype)
  - [UserStatusType](#userstatustype)
  - [UserType](#usertype)

## ActivityType

```python
from mypy_boto3_workdocs.literals import ActivityType
```

Values:

- `DOCUMENT_ANNOTATION_ADDED`
- `DOCUMENT_ANNOTATION_DELETED`
- `DOCUMENT_CHECKED_IN`
- `DOCUMENT_CHECKED_OUT`
- `DOCUMENT_COMMENT_ADDED`
- `DOCUMENT_COMMENT_DELETED`
- `DOCUMENT_MOVED`
- `DOCUMENT_RECYCLED`
- `DOCUMENT_RENAMED`
- `DOCUMENT_RESTORED`
- `DOCUMENT_REVERTED`
- `DOCUMENT_SHARE_PERMISSION_CHANGED`
- `DOCUMENT_SHAREABLE_LINK_CREATED`
- `DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED`
- `DOCUMENT_SHAREABLE_LINK_REMOVED`
- `DOCUMENT_SHARED`
- `DOCUMENT_UNSHARED`
- `DOCUMENT_VERSION_DELETED`
- `DOCUMENT_VERSION_DOWNLOADED`
- `DOCUMENT_VERSION_UPLOADED`
- `DOCUMENT_VERSION_VIEWED`
- `FOLDER_CREATED`
- `FOLDER_DELETED`
- `FOLDER_MOVED`
- `FOLDER_RECYCLED`
- `FOLDER_RENAMED`
- `FOLDER_RESTORED`
- `FOLDER_SHARE_PERMISSION_CHANGED`
- `FOLDER_SHAREABLE_LINK_CREATED`
- `FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED`
- `FOLDER_SHAREABLE_LINK_REMOVED`
- `FOLDER_SHARED`
- `FOLDER_UNSHARED`

## BooleanEnumType

```python
from mypy_boto3_workdocs.literals import BooleanEnumType
```

Values:

- `FALSE`
- `TRUE`

## CommentStatusType

```python
from mypy_boto3_workdocs.literals import CommentStatusType
```

Values:

- `DELETED`
- `DRAFT`
- `PUBLISHED`

## CommentVisibilityType

```python
from mypy_boto3_workdocs.literals import CommentVisibilityType
```

Values:

- `PRIVATE`
- `PUBLIC`

## DescribeActivitiesPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeActivitiesPaginatorName
```

Values:

- `describe_activities`

## DescribeCommentsPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeCommentsPaginatorName
```

Values:

- `describe_comments`

## DescribeDocumentVersionsPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeDocumentVersionsPaginatorName
```

Values:

- `describe_document_versions`

## DescribeFolderContentsPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeFolderContentsPaginatorName
```

Values:

- `describe_folder_contents`

## DescribeGroupsPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeGroupsPaginatorName
```

Values:

- `describe_groups`

## DescribeNotificationSubscriptionsPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeNotificationSubscriptionsPaginatorName
```

Values:

- `describe_notification_subscriptions`

## DescribeResourcePermissionsPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeResourcePermissionsPaginatorName
```

Values:

- `describe_resource_permissions`

## DescribeRootFoldersPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeRootFoldersPaginatorName
```

Values:

- `describe_root_folders`

## DescribeUsersPaginatorName

```python
from mypy_boto3_workdocs.literals import DescribeUsersPaginatorName
```

Values:

- `describe_users`

## DocumentSourceType

```python
from mypy_boto3_workdocs.literals import DocumentSourceType
```

Values:

- `ORIGINAL`
- `WITH_COMMENTS`

## DocumentStatusType

```python
from mypy_boto3_workdocs.literals import DocumentStatusType
```

Values:

- `ACTIVE`
- `INITIALIZED`

## DocumentThumbnailType

```python
from mypy_boto3_workdocs.literals import DocumentThumbnailType
```

Values:

- `LARGE`
- `SMALL`
- `SMALL_HQ`

## DocumentVersionStatus

```python
from mypy_boto3_workdocs.literals import DocumentVersionStatus
```

Values:

- `ACTIVE`

## FolderContentType

```python
from mypy_boto3_workdocs.literals import FolderContentType
```

Values:

- `ALL`
- `DOCUMENT`
- `FOLDER`

## LocaleType

```python
from mypy_boto3_workdocs.literals import LocaleType
```

Values:

- `de`
- `default`
- `en`
- `es`
- `fr`
- `ja`
- `ko`
- `pt_BR`
- `ru`
- `zh_CN`
- `zh_TW`

## OrderType

```python
from mypy_boto3_workdocs.literals import OrderType
```

Values:

- `ASCENDING`
- `DESCENDING`

## PrincipalType

```python
from mypy_boto3_workdocs.literals import PrincipalType
```

Values:

- `ANONYMOUS`
- `GROUP`
- `INVITE`
- `ORGANIZATION`
- `USER`

## ResourceCollectionType

```python
from mypy_boto3_workdocs.literals import ResourceCollectionType
```

Values:

- `SHARED_WITH_ME`

## ResourceSortType

```python
from mypy_boto3_workdocs.literals import ResourceSortType
```

Values:

- `DATE`
- `NAME`

## ResourceStateType

```python
from mypy_boto3_workdocs.literals import ResourceStateType
```

Values:

- `ACTIVE`
- `RECYCLED`
- `RECYCLING`
- `RESTORING`

## ResourceType

```python
from mypy_boto3_workdocs.literals import ResourceType
```

Values:

- `DOCUMENT`
- `FOLDER`

## RolePermissionType

```python
from mypy_boto3_workdocs.literals import RolePermissionType
```

Values:

- `DIRECT`
- `INHERITED`

## RoleType

```python
from mypy_boto3_workdocs.literals import RoleType
```

Values:

- `CONTRIBUTOR`
- `COOWNER`
- `OWNER`
- `VIEWER`

## ShareStatusType

```python
from mypy_boto3_workdocs.literals import ShareStatusType
```

Values:

- `FAILURE`
- `SUCCESS`

## StorageType

```python
from mypy_boto3_workdocs.literals import StorageType
```

Values:

- `QUOTA`
- `UNLIMITED`

## SubscriptionProtocolType

```python
from mypy_boto3_workdocs.literals import SubscriptionProtocolType
```

Values:

- `HTTPS`

## SubscriptionType

```python
from mypy_boto3_workdocs.literals import SubscriptionType
```

Values:

- `ALL`

## UserFilterType

```python
from mypy_boto3_workdocs.literals import UserFilterType
```

Values:

- `ACTIVE_PENDING`
- `ALL`

## UserSortType

```python
from mypy_boto3_workdocs.literals import UserSortType
```

Values:

- `FULL_NAME`
- `STORAGE_LIMIT`
- `STORAGE_USED`
- `USER_NAME`
- `USER_STATUS`

## UserStatusType

```python
from mypy_boto3_workdocs.literals import UserStatusType
```

Values:

- `ACTIVE`
- `INACTIVE`
- `PENDING`

## UserType

```python
from mypy_boto3_workdocs.literals import UserType
```

Values:

- `ADMIN`
- `MINIMALUSER`
- `POWERUSER`
- `USER`
- `WORKSPACESUSER`
