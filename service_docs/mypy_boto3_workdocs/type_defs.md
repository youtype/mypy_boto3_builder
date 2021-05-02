# Structures for boto3 WorkDocs module

> [Index](../index.md) > [WorkDocs](./index.md) > Structures

Auto-generated documentation for [WorkDocs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs)
type annotations stubs module [mypy_boto3_workdocs](https://pypi.org/project/mypy-boto3-workdocs/).

- [Structures for boto3 WorkDocs module](#structures-for-boto3-workdocs-module)
  - [ActivateUserResponseTypeDef](#activateuserresponsetypedef)
  - [ActivityTypeDef](#activitytypedef)
  - [AddResourcePermissionsResponseTypeDef](#addresourcepermissionsresponsetypedef)
  - [CommentMetadataTypeDef](#commentmetadatatypedef)
  - [CommentTypeDef](#commenttypedef)
  - [CreateCommentResponseTypeDef](#createcommentresponsetypedef)
  - [CreateFolderResponseTypeDef](#createfolderresponsetypedef)
  - [CreateNotificationSubscriptionResponseTypeDef](#createnotificationsubscriptionresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [DescribeActivitiesResponseTypeDef](#describeactivitiesresponsetypedef)
  - [DescribeCommentsResponseTypeDef](#describecommentsresponsetypedef)
  - [DescribeDocumentVersionsResponseTypeDef](#describedocumentversionsresponsetypedef)
  - [DescribeFolderContentsResponseTypeDef](#describefoldercontentsresponsetypedef)
  - [DescribeGroupsResponseTypeDef](#describegroupsresponsetypedef)
  - [DescribeNotificationSubscriptionsResponseTypeDef](#describenotificationsubscriptionsresponsetypedef)
  - [DescribeResourcePermissionsResponseTypeDef](#describeresourcepermissionsresponsetypedef)
  - [DescribeRootFoldersResponseTypeDef](#describerootfoldersresponsetypedef)
  - [DescribeUsersResponseTypeDef](#describeusersresponsetypedef)
  - [DocumentMetadataTypeDef](#documentmetadatatypedef)
  - [DocumentVersionMetadataTypeDef](#documentversionmetadatatypedef)
  - [FolderMetadataTypeDef](#foldermetadatatypedef)
  - [GetCurrentUserResponseTypeDef](#getcurrentuserresponsetypedef)
  - [GetDocumentPathResponseTypeDef](#getdocumentpathresponsetypedef)
  - [GetDocumentResponseTypeDef](#getdocumentresponsetypedef)
  - [GetDocumentVersionResponseTypeDef](#getdocumentversionresponsetypedef)
  - [GetFolderPathResponseTypeDef](#getfolderpathresponsetypedef)
  - [GetFolderResponseTypeDef](#getfolderresponsetypedef)
  - [GetResourcesResponseTypeDef](#getresourcesresponsetypedef)
  - [GroupMetadataTypeDef](#groupmetadatatypedef)
  - [InitiateDocumentVersionUploadResponseTypeDef](#initiatedocumentversionuploadresponsetypedef)
  - [NotificationOptionsTypeDef](#notificationoptionstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParticipantsTypeDef](#participantstypedef)
  - [PermissionInfoTypeDef](#permissioninfotypedef)
  - [PrincipalTypeDef](#principaltypedef)
  - [ResourceMetadataTypeDef](#resourcemetadatatypedef)
  - [ResourcePathComponentTypeDef](#resourcepathcomponenttypedef)
  - [ResourcePathTypeDef](#resourcepathtypedef)
  - [SharePrincipalTypeDef](#shareprincipaltypedef)
  - [ShareResultTypeDef](#shareresulttypedef)
  - [StorageRuleTypeTypeDef](#storageruletypetypedef)
  - [SubscriptionTypeDef](#subscriptiontypedef)
  - [UpdateUserResponseTypeDef](#updateuserresponsetypedef)
  - [UploadMetadataTypeDef](#uploadmetadatatypedef)
  - [UserMetadataTypeDef](#usermetadatatypedef)
  - [UserStorageMetadataTypeDef](#userstoragemetadatatypedef)
  - [UserTypeDef](#usertypedef)

## ActivateUserResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import ActivateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## ActivityTypeDef

```python
from mypy_boto3_workdocs.type_defs import ActivityTypeDef
```




Optional fields:
- `Type`: `ActivityType`
- `TimeStamp`: `datetime`
- `IsIndirectActivity`: `bool`
- `OrganizationId`: `str`
- `Initiator`: `"UserMetadataTypeDef"`
- `Participants`: `"ParticipantsTypeDef"`
- `ResourceMetadata`: `"ResourceMetadataTypeDef"`
- `OriginalParent`: `"ResourceMetadataTypeDef"`
- `CommentMetadata`: `"CommentMetadataTypeDef"`


## AddResourcePermissionsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import AddResourcePermissionsResponseTypeDef
```




Optional fields:
- `ShareResults`: `List["ShareResultTypeDef"]`


## CommentMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import CommentMetadataTypeDef
```




Optional fields:
- `CommentId`: `str`
- `Contributor`: `"UserTypeDef"`
- `CreatedTimestamp`: `datetime`
- `CommentStatus`: `CommentStatusType`
- `RecipientId`: `str`


## CommentTypeDef

```python
from mypy_boto3_workdocs.type_defs import CommentTypeDef
```


Required fields:
- `CommentId`: `str`



Optional fields:
- `ParentId`: `str`
- `ThreadId`: `str`
- `Text`: `str`
- `Contributor`: `"UserTypeDef"`
- `CreatedTimestamp`: `datetime`
- `Status`: `CommentStatusType`
- `Visibility`: `CommentVisibilityType`
- `RecipientId`: `str`


## CreateCommentResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import CreateCommentResponseTypeDef
```




Optional fields:
- `Comment`: `"CommentTypeDef"`


## CreateFolderResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import CreateFolderResponseTypeDef
```




Optional fields:
- `Metadata`: `"FolderMetadataTypeDef"`


## CreateNotificationSubscriptionResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import CreateNotificationSubscriptionResponseTypeDef
```




Optional fields:
- `Subscription`: `"SubscriptionTypeDef"`


## CreateUserResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import CreateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## DescribeActivitiesResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeActivitiesResponseTypeDef
```




Optional fields:
- `UserActivities`: `List["ActivityTypeDef"]`
- `Marker`: `str`


## DescribeCommentsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeCommentsResponseTypeDef
```




Optional fields:
- `Comments`: `List["CommentTypeDef"]`
- `Marker`: `str`


## DescribeDocumentVersionsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeDocumentVersionsResponseTypeDef
```




Optional fields:
- `DocumentVersions`: `List["DocumentVersionMetadataTypeDef"]`
- `Marker`: `str`


## DescribeFolderContentsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeFolderContentsResponseTypeDef
```




Optional fields:
- `Folders`: `List["FolderMetadataTypeDef"]`
- `Documents`: `List["DocumentMetadataTypeDef"]`
- `Marker`: `str`


## DescribeGroupsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeGroupsResponseTypeDef
```




Optional fields:
- `Groups`: `List["GroupMetadataTypeDef"]`
- `Marker`: `str`


## DescribeNotificationSubscriptionsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeNotificationSubscriptionsResponseTypeDef
```




Optional fields:
- `Subscriptions`: `List["SubscriptionTypeDef"]`
- `Marker`: `str`


## DescribeResourcePermissionsResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeResourcePermissionsResponseTypeDef
```




Optional fields:
- `Principals`: `List["PrincipalTypeDef"]`
- `Marker`: `str`


## DescribeRootFoldersResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeRootFoldersResponseTypeDef
```




Optional fields:
- `Folders`: `List["FolderMetadataTypeDef"]`
- `Marker`: `str`


## DescribeUsersResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import DescribeUsersResponseTypeDef
```




Optional fields:
- `Users`: `List["UserTypeDef"]`
- `TotalNumberOfUsers`: `int`
- `Marker`: `str`


## DocumentMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import DocumentMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `CreatorId`: `str`
- `ParentFolderId`: `str`
- `CreatedTimestamp`: `datetime`
- `ModifiedTimestamp`: `datetime`
- `LatestVersionMetadata`: `"DocumentVersionMetadataTypeDef"`
- `ResourceState`: `ResourceStateType`
- `Labels`: `List[str]`


## DocumentVersionMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import DocumentVersionMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `ContentType`: `str`
- `Size`: `int`
- `Signature`: `str`
- `Status`: `DocumentStatusType`
- `CreatedTimestamp`: `datetime`
- `ModifiedTimestamp`: `datetime`
- `ContentCreatedTimestamp`: `datetime`
- `ContentModifiedTimestamp`: `datetime`
- `CreatorId`: `str`
- `Thumbnail`: `Dict[DocumentThumbnailType, str]`
- `Source`: `Dict[DocumentSourceType, str]`


## FolderMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import FolderMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `CreatorId`: `str`
- `ParentFolderId`: `str`
- `CreatedTimestamp`: `datetime`
- `ModifiedTimestamp`: `datetime`
- `ResourceState`: `ResourceStateType`
- `Signature`: `str`
- `Labels`: `List[str]`
- `Size`: `int`
- `LatestVersionSize`: `int`


## GetCurrentUserResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetCurrentUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## GetDocumentPathResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetDocumentPathResponseTypeDef
```




Optional fields:
- `Path`: `"ResourcePathTypeDef"`


## GetDocumentResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetDocumentResponseTypeDef
```




Optional fields:
- `Metadata`: `"DocumentMetadataTypeDef"`
- `CustomMetadata`: `Dict[str, str]`


## GetDocumentVersionResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetDocumentVersionResponseTypeDef
```




Optional fields:
- `Metadata`: `"DocumentVersionMetadataTypeDef"`
- `CustomMetadata`: `Dict[str, str]`


## GetFolderPathResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetFolderPathResponseTypeDef
```




Optional fields:
- `Path`: `"ResourcePathTypeDef"`


## GetFolderResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetFolderResponseTypeDef
```




Optional fields:
- `Metadata`: `"FolderMetadataTypeDef"`
- `CustomMetadata`: `Dict[str, str]`


## GetResourcesResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import GetResourcesResponseTypeDef
```




Optional fields:
- `Folders`: `List["FolderMetadataTypeDef"]`
- `Documents`: `List["DocumentMetadataTypeDef"]`
- `Marker`: `str`


## GroupMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import GroupMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`


## InitiateDocumentVersionUploadResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import InitiateDocumentVersionUploadResponseTypeDef
```




Optional fields:
- `Metadata`: `"DocumentMetadataTypeDef"`
- `UploadMetadata`: `"UploadMetadataTypeDef"`


## NotificationOptionsTypeDef

```python
from mypy_boto3_workdocs.type_defs import NotificationOptionsTypeDef
```




Optional fields:
- `SendEmail`: `bool`
- `EmailMessage`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_workdocs.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParticipantsTypeDef

```python
from mypy_boto3_workdocs.type_defs import ParticipantsTypeDef
```




Optional fields:
- `Users`: `List["UserMetadataTypeDef"]`
- `Groups`: `List["GroupMetadataTypeDef"]`


## PermissionInfoTypeDef

```python
from mypy_boto3_workdocs.type_defs import PermissionInfoTypeDef
```




Optional fields:
- `Role`: `RoleType`
- `Type`: `RolePermissionType`


## PrincipalTypeDef

```python
from mypy_boto3_workdocs.type_defs import PrincipalTypeDef
```




Optional fields:
- `Id`: `str`
- `Type`: `PrincipalType`
- `Roles`: `List["PermissionInfoTypeDef"]`


## ResourceMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import ResourceMetadataTypeDef
```




Optional fields:
- `Type`: `ResourceType`
- `Name`: `str`
- `OriginalName`: `str`
- `Id`: `str`
- `VersionId`: `str`
- `Owner`: `"UserMetadataTypeDef"`
- `ParentId`: `str`


## ResourcePathComponentTypeDef

```python
from mypy_boto3_workdocs.type_defs import ResourcePathComponentTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`


## ResourcePathTypeDef

```python
from mypy_boto3_workdocs.type_defs import ResourcePathTypeDef
```




Optional fields:
- `Components`: `List["ResourcePathComponentTypeDef"]`


## SharePrincipalTypeDef

```python
from mypy_boto3_workdocs.type_defs import SharePrincipalTypeDef
```


Required fields:
- `Id`: `str`
- `Type`: `PrincipalType`
- `Role`: `RoleType`




## ShareResultTypeDef

```python
from mypy_boto3_workdocs.type_defs import ShareResultTypeDef
```




Optional fields:
- `PrincipalId`: `str`
- `InviteePrincipalId`: `str`
- `Role`: `RoleType`
- `Status`: `ShareStatusType`
- `ShareId`: `str`
- `StatusMessage`: `str`


## StorageRuleTypeTypeDef

```python
from mypy_boto3_workdocs.type_defs import StorageRuleTypeTypeDef
```




Optional fields:
- `StorageAllocatedInBytes`: `int`
- `StorageType`: `StorageType`


## SubscriptionTypeDef

```python
from mypy_boto3_workdocs.type_defs import SubscriptionTypeDef
```




Optional fields:
- `SubscriptionId`: `str`
- `EndPoint`: `str`
- `Protocol`: `Literal['HTTPS']`


## UpdateUserResponseTypeDef

```python
from mypy_boto3_workdocs.type_defs import UpdateUserResponseTypeDef
```




Optional fields:
- `User`: `"UserTypeDef"`


## UploadMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import UploadMetadataTypeDef
```




Optional fields:
- `UploadUrl`: `str`
- `SignedHeaders`: `Dict[str, str]`


## UserMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import UserMetadataTypeDef
```




Optional fields:
- `Id`: `str`
- `Username`: `str`
- `GivenName`: `str`
- `Surname`: `str`
- `EmailAddress`: `str`


## UserStorageMetadataTypeDef

```python
from mypy_boto3_workdocs.type_defs import UserStorageMetadataTypeDef
```




Optional fields:
- `StorageUtilizedInBytes`: `int`
- `StorageRule`: `"StorageRuleTypeTypeDef"`


## UserTypeDef

```python
from mypy_boto3_workdocs.type_defs import UserTypeDef
```




Optional fields:
- `Id`: `str`
- `Username`: `str`
- `EmailAddress`: `str`
- `GivenName`: `str`
- `Surname`: `str`
- `OrganizationId`: `str`
- `RootFolderId`: `str`
- `RecycleBinFolderId`: `str`
- `Status`: `UserStatusType`
- `Type`: `UserType`
- `CreatedTimestamp`: `datetime`
- `ModifiedTimestamp`: `datetime`
- `TimeZoneId`: `str`
- `Locale`: `LocaleType`
- `Storage`: `"UserStorageMetadataTypeDef"`

