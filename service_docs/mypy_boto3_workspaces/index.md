# Type annotations for boto3 WorkSpaces module

> [Index](../index.md) > WorkSpaces

Auto-generated documentation for [WorkSpaces](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces)
type annotations stubs module [mypy_boto3_workspaces](https://pypi.org/project/mypy-boto3-workspaces/).

```bash
pip install mypy-boto3-workspaces
```

- [Type annotations for boto3 WorkSpaces module](#type-annotations-for-boto3-workspaces-module)
  - [WorkSpacesClient](#workspacesclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## WorkSpacesClient

Type annotations for  `boto3.client("workspaces")` as [WorkSpacesClient](./client.md)

Can be used directly:

```python
from mypy_boto3_workspaces.client import WorkSpacesClient
```


WorkSpacesClient [exceptions](./client.md#exceptions)



### Methods
- [associate_connection_alias](./client.md#associate-connection-alias)
- [associate_ip_groups](./client.md#associate-ip-groups)
- [authorize_ip_rules](./client.md#authorize-ip-rules)
- [can_paginate](./client.md#can-paginate)
- [copy_workspace_image](./client.md#copy-workspace-image)
- [create_connection_alias](./client.md#create-connection-alias)
- [create_ip_group](./client.md#create-ip-group)
- [create_tags](./client.md#create-tags)
- [create_workspace_bundle](./client.md#create-workspace-bundle)
- [create_workspaces](./client.md#create-workspaces)
- [delete_connection_alias](./client.md#delete-connection-alias)
- [delete_ip_group](./client.md#delete-ip-group)
- [delete_tags](./client.md#delete-tags)
- [delete_workspace_bundle](./client.md#delete-workspace-bundle)
- [delete_workspace_image](./client.md#delete-workspace-image)
- [deregister_workspace_directory](./client.md#deregister-workspace-directory)
- [describe_account](./client.md#describe-account)
- [describe_account_modifications](./client.md#describe-account-modifications)
- [describe_client_properties](./client.md#describe-client-properties)
- [describe_connection_alias_permissions](./client.md#describe-connection-alias-permissions)
- [describe_connection_aliases](./client.md#describe-connection-aliases)
- [describe_ip_groups](./client.md#describe-ip-groups)
- [describe_tags](./client.md#describe-tags)
- [describe_workspace_bundles](./client.md#describe-workspace-bundles)
- [describe_workspace_directories](./client.md#describe-workspace-directories)
- [describe_workspace_image_permissions](./client.md#describe-workspace-image-permissions)
- [describe_workspace_images](./client.md#describe-workspace-images)
- [describe_workspace_snapshots](./client.md#describe-workspace-snapshots)
- [describe_workspaces](./client.md#describe-workspaces)
- [describe_workspaces_connection_status](./client.md#describe-workspaces-connection-status)
- [disassociate_connection_alias](./client.md#disassociate-connection-alias)
- [disassociate_ip_groups](./client.md#disassociate-ip-groups)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [import_workspace_image](./client.md#import-workspace-image)
- [list_available_management_cidr_ranges](./client.md#list-available-management-cidr-ranges)
- [migrate_workspace](./client.md#migrate-workspace)
- [modify_account](./client.md#modify-account)
- [modify_client_properties](./client.md#modify-client-properties)
- [modify_selfservice_permissions](./client.md#modify-selfservice-permissions)
- [modify_workspace_access_properties](./client.md#modify-workspace-access-properties)
- [modify_workspace_creation_properties](./client.md#modify-workspace-creation-properties)
- [modify_workspace_properties](./client.md#modify-workspace-properties)
- [modify_workspace_state](./client.md#modify-workspace-state)
- [reboot_workspaces](./client.md#reboot-workspaces)
- [rebuild_workspaces](./client.md#rebuild-workspaces)
- [register_workspace_directory](./client.md#register-workspace-directory)
- [restore_workspace](./client.md#restore-workspace)
- [revoke_ip_rules](./client.md#revoke-ip-rules)
- [start_workspaces](./client.md#start-workspaces)
- [stop_workspaces](./client.md#stop-workspaces)
- [terminate_workspaces](./client.md#terminate-workspaces)
- [update_connection_alias_permission](./client.md#update-connection-alias-permission)
- [update_rules_of_ip_group](./client.md#update-rules-of-ip-group)
- [update_workspace_bundle](./client.md#update-workspace-bundle)
- [update_workspace_image_permission](./client.md#update-workspace-image-permission)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InvalidParameterValuesException](./client.md#invalidparametervaluesexception)
- [InvalidResourceStateException](./client.md#invalidresourcestateexception)
- [OperationInProgressException](./client.md#operationinprogressexception)
- [OperationNotSupportedException](./client.md#operationnotsupportedexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceAssociatedException](./client.md#resourceassociatedexception)
- [ResourceCreationFailedException](./client.md#resourcecreationfailedexception)
- [ResourceLimitExceededException](./client.md#resourcelimitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceUnavailableException](./client.md#resourceunavailableexception)
- [UnsupportedNetworkConfigurationException](./client.md#unsupportednetworkconfigurationexception)
- [UnsupportedWorkspaceConfigurationException](./client.md#unsupportedworkspaceconfigurationexception)
- [WorkspacesDefaultRoleNotFoundException](./client.md#workspacesdefaultrolenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("workspaces").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_workspaces.paginators import DescribeAccountModificationsPaginator, ...
```

- [DescribeAccountModificationsPaginator](./paginators.md#describeaccountmodificationspaginator)
- [DescribeIpGroupsPaginator](./paginators.md#describeipgroupspaginator)
- [DescribeWorkspaceBundlesPaginator](./paginators.md#describeworkspacebundlespaginator)
- [DescribeWorkspaceDirectoriesPaginator](./paginators.md#describeworkspacedirectoriespaginator)
- [DescribeWorkspaceImagesPaginator](./paginators.md#describeworkspaceimagespaginator)
- [DescribeWorkspacesPaginator](./paginators.md#describeworkspacespaginator)
- [DescribeWorkspacesConnectionStatusPaginator](./paginators.md#describeworkspacesconnectionstatuspaginator)
- [ListAvailableManagementCidrRangesPaginator](./paginators.md#listavailablemanagementcidrrangespaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workspaces.literals import AccessPropertyValue, ...
```

- [AccessPropertyValue](./literals.md#accesspropertyvalue)
- [Application](./literals.md#application)
- [AssociationStatus](./literals.md#associationstatus)
- [Compute](./literals.md#compute)
- [ConnectionAliasState](./literals.md#connectionaliasstate)
- [ConnectionState](./literals.md#connectionstate)
- [DedicatedTenancyModificationStateEnum](./literals.md#dedicatedtenancymodificationstateenum)
- [DedicatedTenancySupportEnum](./literals.md#dedicatedtenancysupportenum)
- [DedicatedTenancySupportResultEnum](./literals.md#dedicatedtenancysupportresultenum)
- [DescribeAccountModificationsPaginatorName](./literals.md#describeaccountmodificationspaginatorname)
- [DescribeIpGroupsPaginatorName](./literals.md#describeipgroupspaginatorname)
- [DescribeWorkspaceBundlesPaginatorName](./literals.md#describeworkspacebundlespaginatorname)
- [DescribeWorkspaceDirectoriesPaginatorName](./literals.md#describeworkspacedirectoriespaginatorname)
- [DescribeWorkspaceImagesPaginatorName](./literals.md#describeworkspaceimagespaginatorname)
- [DescribeWorkspacesConnectionStatusPaginatorName](./literals.md#describeworkspacesconnectionstatuspaginatorname)
- [DescribeWorkspacesPaginatorName](./literals.md#describeworkspacespaginatorname)
- [ImageType](./literals.md#imagetype)
- [ListAvailableManagementCidrRangesPaginatorName](./literals.md#listavailablemanagementcidrrangespaginatorname)
- [ModificationResourceEnum](./literals.md#modificationresourceenum)
- [ModificationStateEnum](./literals.md#modificationstateenum)
- [OperatingSystemType](./literals.md#operatingsystemtype)
- [ReconnectEnum](./literals.md#reconnectenum)
- [RunningMode](./literals.md#runningmode)
- [TargetWorkspaceState](./literals.md#targetworkspacestate)
- [Tenancy](./literals.md#tenancy)
- [WorkspaceDirectoryState](./literals.md#workspacedirectorystate)
- [WorkspaceDirectoryType](./literals.md#workspacedirectorytype)
- [WorkspaceImageIngestionProcess](./literals.md#workspaceimageingestionprocess)
- [WorkspaceImageRequiredTenancy](./literals.md#workspaceimagerequiredtenancy)
- [WorkspaceImageState](./literals.md#workspaceimagestate)
- [WorkspaceState](./literals.md#workspacestate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_workspaces.type_defs import AccountModificationTypeDef, ...
```

- [AccountModificationTypeDef](./type_defs.md#accountmodificationtypedef)
- [AssociateConnectionAliasResultTypeDef](./type_defs.md#associateconnectionaliasresulttypedef)
- [ClientPropertiesResultTypeDef](./type_defs.md#clientpropertiesresulttypedef)
- [ClientPropertiesTypeDef](./type_defs.md#clientpropertiestypedef)
- [ComputeTypeTypeDef](./type_defs.md#computetypetypedef)
- [ConnectionAliasAssociationTypeDef](./type_defs.md#connectionaliasassociationtypedef)
- [ConnectionAliasPermissionTypeDef](./type_defs.md#connectionaliaspermissiontypedef)
- [ConnectionAliasTypeDef](./type_defs.md#connectionaliastypedef)
- [CopyWorkspaceImageResultTypeDef](./type_defs.md#copyworkspaceimageresulttypedef)
- [CreateConnectionAliasResultTypeDef](./type_defs.md#createconnectionaliasresulttypedef)
- [CreateIpGroupResultTypeDef](./type_defs.md#createipgroupresulttypedef)
- [CreateWorkspaceBundleResultTypeDef](./type_defs.md#createworkspacebundleresulttypedef)
- [CreateWorkspacesResultTypeDef](./type_defs.md#createworkspacesresulttypedef)
- [DefaultWorkspaceCreationPropertiesTypeDef](./type_defs.md#defaultworkspacecreationpropertiestypedef)
- [DescribeAccountModificationsResultTypeDef](./type_defs.md#describeaccountmodificationsresulttypedef)
- [DescribeAccountResultTypeDef](./type_defs.md#describeaccountresulttypedef)
- [DescribeClientPropertiesResultTypeDef](./type_defs.md#describeclientpropertiesresulttypedef)
- [DescribeConnectionAliasPermissionsResultTypeDef](./type_defs.md#describeconnectionaliaspermissionsresulttypedef)
- [DescribeConnectionAliasesResultTypeDef](./type_defs.md#describeconnectionaliasesresulttypedef)
- [DescribeIpGroupsResultTypeDef](./type_defs.md#describeipgroupsresulttypedef)
- [DescribeTagsResultTypeDef](./type_defs.md#describetagsresulttypedef)
- [DescribeWorkspaceBundlesResultTypeDef](./type_defs.md#describeworkspacebundlesresulttypedef)
- [DescribeWorkspaceDirectoriesResultTypeDef](./type_defs.md#describeworkspacedirectoriesresulttypedef)
- [DescribeWorkspaceImagePermissionsResultTypeDef](./type_defs.md#describeworkspaceimagepermissionsresulttypedef)
- [DescribeWorkspaceImagesResultTypeDef](./type_defs.md#describeworkspaceimagesresulttypedef)
- [DescribeWorkspaceSnapshotsResultTypeDef](./type_defs.md#describeworkspacesnapshotsresulttypedef)
- [DescribeWorkspacesConnectionStatusResultTypeDef](./type_defs.md#describeworkspacesconnectionstatusresulttypedef)
- [DescribeWorkspacesResultTypeDef](./type_defs.md#describeworkspacesresulttypedef)
- [FailedCreateWorkspaceRequestTypeDef](./type_defs.md#failedcreateworkspacerequesttypedef)
- [FailedWorkspaceChangeRequestTypeDef](./type_defs.md#failedworkspacechangerequesttypedef)
- [ImagePermissionTypeDef](./type_defs.md#imagepermissiontypedef)
- [ImportWorkspaceImageResultTypeDef](./type_defs.md#importworkspaceimageresulttypedef)
- [IpRuleItemTypeDef](./type_defs.md#ipruleitemtypedef)
- [ListAvailableManagementCidrRangesResultTypeDef](./type_defs.md#listavailablemanagementcidrrangesresulttypedef)
- [MigrateWorkspaceResultTypeDef](./type_defs.md#migrateworkspaceresulttypedef)
- [ModificationStateTypeDef](./type_defs.md#modificationstatetypedef)
- [OperatingSystemTypeDef](./type_defs.md#operatingsystemtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RebootRequestTypeDef](./type_defs.md#rebootrequesttypedef)
- [RebootWorkspacesResultTypeDef](./type_defs.md#rebootworkspacesresulttypedef)
- [RebuildRequestTypeDef](./type_defs.md#rebuildrequesttypedef)
- [RebuildWorkspacesResultTypeDef](./type_defs.md#rebuildworkspacesresulttypedef)
- [RootStorageTypeDef](./type_defs.md#rootstoragetypedef)
- [SelfservicePermissionsTypeDef](./type_defs.md#selfservicepermissionstypedef)
- [SnapshotTypeDef](./type_defs.md#snapshottypedef)
- [StartRequestTypeDef](./type_defs.md#startrequesttypedef)
- [StartWorkspacesResultTypeDef](./type_defs.md#startworkspacesresulttypedef)
- [StopRequestTypeDef](./type_defs.md#stoprequesttypedef)
- [StopWorkspacesResultTypeDef](./type_defs.md#stopworkspacesresulttypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TerminateRequestTypeDef](./type_defs.md#terminaterequesttypedef)
- [TerminateWorkspacesResultTypeDef](./type_defs.md#terminateworkspacesresulttypedef)
- [UserStorageTypeDef](./type_defs.md#userstoragetypedef)
- [WorkspaceAccessPropertiesTypeDef](./type_defs.md#workspaceaccesspropertiestypedef)
- [WorkspaceBundleTypeDef](./type_defs.md#workspacebundletypedef)
- [WorkspaceConnectionStatusTypeDef](./type_defs.md#workspaceconnectionstatustypedef)
- [WorkspaceCreationPropertiesTypeDef](./type_defs.md#workspacecreationpropertiestypedef)
- [WorkspaceDirectoryTypeDef](./type_defs.md#workspacedirectorytypedef)
- [WorkspaceImageTypeDef](./type_defs.md#workspaceimagetypedef)
- [WorkspacePropertiesTypeDef](./type_defs.md#workspacepropertiestypedef)
- [WorkspaceRequestTypeDef](./type_defs.md#workspacerequesttypedef)
- [WorkspaceTypeDef](./type_defs.md#workspacetypedef)
- [WorkspacesIpGroupTypeDef](./type_defs.md#workspacesipgrouptypedef)
