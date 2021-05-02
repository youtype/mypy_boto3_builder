# Type annotations for boto3 WorkDocs module

> [Index](../index.md) > WorkDocs

Auto-generated documentation for [WorkDocs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs)
type annotations stubs module [mypy_boto3_workdocs](https://pypi.org/project/mypy-boto3-workdocs/).

```bash
pip install mypy-boto3-workdocs
```

- [Type annotations for boto3 WorkDocs module](#type-annotations-for-boto3-workdocs-module)
  - [WorkDocsClient](#workdocsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## WorkDocsClient

Type annotations for  `boto3.client("workdocs")` as [WorkDocsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_workdocs.client import WorkDocsClient
```


WorkDocsClient [exceptions](./client.md#exceptions)



### Methods
- [abort_document_version_upload](./client.md#abort-document-version-upload)
- [activate_user](./client.md#activate-user)
- [add_resource_permissions](./client.md#add-resource-permissions)
- [can_paginate](./client.md#can-paginate)
- [create_comment](./client.md#create-comment)
- [create_custom_metadata](./client.md#create-custom-metadata)
- [create_folder](./client.md#create-folder)
- [create_labels](./client.md#create-labels)
- [create_notification_subscription](./client.md#create-notification-subscription)
- [create_user](./client.md#create-user)
- [deactivate_user](./client.md#deactivate-user)
- [delete_comment](./client.md#delete-comment)
- [delete_custom_metadata](./client.md#delete-custom-metadata)
- [delete_document](./client.md#delete-document)
- [delete_folder](./client.md#delete-folder)
- [delete_folder_contents](./client.md#delete-folder-contents)
- [delete_labels](./client.md#delete-labels)
- [delete_notification_subscription](./client.md#delete-notification-subscription)
- [delete_user](./client.md#delete-user)
- [describe_activities](./client.md#describe-activities)
- [describe_comments](./client.md#describe-comments)
- [describe_document_versions](./client.md#describe-document-versions)
- [describe_folder_contents](./client.md#describe-folder-contents)
- [describe_groups](./client.md#describe-groups)
- [describe_notification_subscriptions](./client.md#describe-notification-subscriptions)
- [describe_resource_permissions](./client.md#describe-resource-permissions)
- [describe_root_folders](./client.md#describe-root-folders)
- [describe_users](./client.md#describe-users)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_current_user](./client.md#get-current-user)
- [get_document](./client.md#get-document)
- [get_document_path](./client.md#get-document-path)
- [get_document_version](./client.md#get-document-version)
- [get_folder](./client.md#get-folder)
- [get_folder_path](./client.md#get-folder-path)
- [get_paginator](./client.md#get-paginator)
- [get_resources](./client.md#get-resources)
- [initiate_document_version_upload](./client.md#initiate-document-version-upload)
- [remove_all_resource_permissions](./client.md#remove-all-resource-permissions)
- [remove_resource_permission](./client.md#remove-resource-permission)
- [update_document](./client.md#update-document)
- [update_document_version](./client.md#update-document-version)
- [update_folder](./client.md#update-folder)
- [update_user](./client.md#update-user)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [ConflictingOperationException](./client.md#conflictingoperationexception)
- [CustomMetadataLimitExceededException](./client.md#custommetadatalimitexceededexception)
- [DeactivatingLastSystemUserException](./client.md#deactivatinglastsystemuserexception)
- [DocumentLockedForCommentsException](./client.md#documentlockedforcommentsexception)
- [DraftUploadOutOfSyncException](./client.md#draftuploadoutofsyncexception)
- [EntityAlreadyExistsException](./client.md#entityalreadyexistsexception)
- [EntityNotExistsException](./client.md#entitynotexistsexception)
- [FailedDependencyException](./client.md#faileddependencyexception)
- [IllegalUserStateException](./client.md#illegaluserstateexception)
- [InvalidArgumentException](./client.md#invalidargumentexception)
- [InvalidCommentOperationException](./client.md#invalidcommentoperationexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidPasswordException](./client.md#invalidpasswordexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ProhibitedStateException](./client.md#prohibitedstateexception)
- [RequestedEntityTooLargeException](./client.md#requestedentitytoolargeexception)
- [ResourceAlreadyCheckedOutException](./client.md#resourcealreadycheckedoutexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [StorageLimitExceededException](./client.md#storagelimitexceededexception)
- [StorageLimitWillExceedException](./client.md#storagelimitwillexceedexception)
- [TooManyLabelsException](./client.md#toomanylabelsexception)
- [TooManySubscriptionsException](./client.md#toomanysubscriptionsexception)
- [UnauthorizedOperationException](./client.md#unauthorizedoperationexception)
- [UnauthorizedResourceAccessException](./client.md#unauthorizedresourceaccessexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("workdocs").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_workdocs.paginators import DescribeActivitiesPaginator, ...
```

- [DescribeActivitiesPaginator](./paginators.md#describeactivitiespaginator)
- [DescribeCommentsPaginator](./paginators.md#describecommentspaginator)
- [DescribeDocumentVersionsPaginator](./paginators.md#describedocumentversionspaginator)
- [DescribeFolderContentsPaginator](./paginators.md#describefoldercontentspaginator)
- [DescribeGroupsPaginator](./paginators.md#describegroupspaginator)
- [DescribeNotificationSubscriptionsPaginator](./paginators.md#describenotificationsubscriptionspaginator)
- [DescribeResourcePermissionsPaginator](./paginators.md#describeresourcepermissionspaginator)
- [DescribeRootFoldersPaginator](./paginators.md#describerootfolderspaginator)
- [DescribeUsersPaginator](./paginators.md#describeuserspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workdocs.literals import ActivityType, ...
```

- [ActivityType](./literals.md#activitytype)
- [BooleanEnumType](./literals.md#booleanenumtype)
- [CommentStatusType](./literals.md#commentstatustype)
- [CommentVisibilityType](./literals.md#commentvisibilitytype)
- [DescribeActivitiesPaginatorName](./literals.md#describeactivitiespaginatorname)
- [DescribeCommentsPaginatorName](./literals.md#describecommentspaginatorname)
- [DescribeDocumentVersionsPaginatorName](./literals.md#describedocumentversionspaginatorname)
- [DescribeFolderContentsPaginatorName](./literals.md#describefoldercontentspaginatorname)
- [DescribeGroupsPaginatorName](./literals.md#describegroupspaginatorname)
- [DescribeNotificationSubscriptionsPaginatorName](./literals.md#describenotificationsubscriptionspaginatorname)
- [DescribeResourcePermissionsPaginatorName](./literals.md#describeresourcepermissionspaginatorname)
- [DescribeRootFoldersPaginatorName](./literals.md#describerootfolderspaginatorname)
- [DescribeUsersPaginatorName](./literals.md#describeuserspaginatorname)
- [DocumentSourceType](./literals.md#documentsourcetype)
- [DocumentStatusType](./literals.md#documentstatustype)
- [DocumentThumbnailType](./literals.md#documentthumbnailtype)
- [DocumentVersionStatus](./literals.md#documentversionstatus)
- [FolderContentType](./literals.md#foldercontenttype)
- [LocaleType](./literals.md#localetype)
- [OrderType](./literals.md#ordertype)
- [PrincipalType](./literals.md#principaltype)
- [ResourceCollectionType](./literals.md#resourcecollectiontype)
- [ResourceSortType](./literals.md#resourcesorttype)
- [ResourceStateType](./literals.md#resourcestatetype)
- [ResourceType](./literals.md#resourcetype)
- [RolePermissionType](./literals.md#rolepermissiontype)
- [RoleType](./literals.md#roletype)
- [ShareStatusType](./literals.md#sharestatustype)
- [StorageType](./literals.md#storagetype)
- [SubscriptionProtocolType](./literals.md#subscriptionprotocoltype)
- [SubscriptionType](./literals.md#subscriptiontype)
- [UserFilterType](./literals.md#userfiltertype)
- [UserSortType](./literals.md#usersorttype)
- [UserStatusType](./literals.md#userstatustype)
- [UserType](./literals.md#usertype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workdocs.type_defs import ActivateUserResponseTypeDef, ...
```

- [ActivateUserResponseTypeDef](./type_defs.md#activateuserresponsetypedef)
- [ActivityTypeDef](./type_defs.md#activitytypedef)
- [AddResourcePermissionsResponseTypeDef](./type_defs.md#addresourcepermissionsresponsetypedef)
- [CommentMetadataTypeDef](./type_defs.md#commentmetadatatypedef)
- [CommentTypeDef](./type_defs.md#commenttypedef)
- [CreateCommentResponseTypeDef](./type_defs.md#createcommentresponsetypedef)
- [CreateFolderResponseTypeDef](./type_defs.md#createfolderresponsetypedef)
- [CreateNotificationSubscriptionResponseTypeDef](./type_defs.md#createnotificationsubscriptionresponsetypedef)
- [CreateUserResponseTypeDef](./type_defs.md#createuserresponsetypedef)
- [DescribeActivitiesResponseTypeDef](./type_defs.md#describeactivitiesresponsetypedef)
- [DescribeCommentsResponseTypeDef](./type_defs.md#describecommentsresponsetypedef)
- [DescribeDocumentVersionsResponseTypeDef](./type_defs.md#describedocumentversionsresponsetypedef)
- [DescribeFolderContentsResponseTypeDef](./type_defs.md#describefoldercontentsresponsetypedef)
- [DescribeGroupsResponseTypeDef](./type_defs.md#describegroupsresponsetypedef)
- [DescribeNotificationSubscriptionsResponseTypeDef](./type_defs.md#describenotificationsubscriptionsresponsetypedef)
- [DescribeResourcePermissionsResponseTypeDef](./type_defs.md#describeresourcepermissionsresponsetypedef)
- [DescribeRootFoldersResponseTypeDef](./type_defs.md#describerootfoldersresponsetypedef)
- [DescribeUsersResponseTypeDef](./type_defs.md#describeusersresponsetypedef)
- [DocumentMetadataTypeDef](./type_defs.md#documentmetadatatypedef)
- [DocumentVersionMetadataTypeDef](./type_defs.md#documentversionmetadatatypedef)
- [FolderMetadataTypeDef](./type_defs.md#foldermetadatatypedef)
- [GetCurrentUserResponseTypeDef](./type_defs.md#getcurrentuserresponsetypedef)
- [GetDocumentPathResponseTypeDef](./type_defs.md#getdocumentpathresponsetypedef)
- [GetDocumentResponseTypeDef](./type_defs.md#getdocumentresponsetypedef)
- [GetDocumentVersionResponseTypeDef](./type_defs.md#getdocumentversionresponsetypedef)
- [GetFolderPathResponseTypeDef](./type_defs.md#getfolderpathresponsetypedef)
- [GetFolderResponseTypeDef](./type_defs.md#getfolderresponsetypedef)
- [GetResourcesResponseTypeDef](./type_defs.md#getresourcesresponsetypedef)
- [GroupMetadataTypeDef](./type_defs.md#groupmetadatatypedef)
- [InitiateDocumentVersionUploadResponseTypeDef](./type_defs.md#initiatedocumentversionuploadresponsetypedef)
- [NotificationOptionsTypeDef](./type_defs.md#notificationoptionstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParticipantsTypeDef](./type_defs.md#participantstypedef)
- [PermissionInfoTypeDef](./type_defs.md#permissioninfotypedef)
- [PrincipalTypeDef](./type_defs.md#principaltypedef)
- [ResourceMetadataTypeDef](./type_defs.md#resourcemetadatatypedef)
- [ResourcePathComponentTypeDef](./type_defs.md#resourcepathcomponenttypedef)
- [ResourcePathTypeDef](./type_defs.md#resourcepathtypedef)
- [SharePrincipalTypeDef](./type_defs.md#shareprincipaltypedef)
- [ShareResultTypeDef](./type_defs.md#shareresulttypedef)
- [StorageRuleTypeTypeDef](./type_defs.md#storageruletypetypedef)
- [SubscriptionTypeDef](./type_defs.md#subscriptiontypedef)
- [UpdateUserResponseTypeDef](./type_defs.md#updateuserresponsetypedef)
- [UploadMetadataTypeDef](./type_defs.md#uploadmetadatatypedef)
- [UserMetadataTypeDef](./type_defs.md#usermetadatatypedef)
- [UserStorageMetadataTypeDef](./type_defs.md#userstoragemetadatatypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
