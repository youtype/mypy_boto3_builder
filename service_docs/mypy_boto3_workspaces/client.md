# WorkSpacesClient for boto3 WorkSpaces module

> [Index](../index.md) > [WorkSpaces](./index.md) > WorkSpacesClient

Auto-generated documentation for [WorkSpaces](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces)
type annotations stubs module [mypy_boto3_workspaces](https://pypi.org/project/mypy-boto3-workspaces/).

- [WorkSpacesClient for boto3 WorkSpaces module](#workspacesclient-for-boto3-workspaces-module)
  - [WorkSpacesClient](#workspacesclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_connection_alias](#associate_connection_alias)
    - [associate_ip_groups](#associate_ip_groups)
    - [authorize_ip_rules](#authorize_ip_rules)
    - [can_paginate](#can_paginate)
    - [copy_workspace_image](#copy_workspace_image)
    - [create_connection_alias](#create_connection_alias)
    - [create_ip_group](#create_ip_group)
    - [create_tags](#create_tags)
    - [create_workspace_bundle](#create_workspace_bundle)
    - [create_workspaces](#create_workspaces)
    - [delete_connection_alias](#delete_connection_alias)
    - [delete_ip_group](#delete_ip_group)
    - [delete_tags](#delete_tags)
    - [delete_workspace_bundle](#delete_workspace_bundle)
    - [delete_workspace_image](#delete_workspace_image)
    - [deregister_workspace_directory](#deregister_workspace_directory)
    - [describe_account](#describe_account)
    - [describe_account_modifications](#describe_account_modifications)
    - [describe_client_properties](#describe_client_properties)
    - [describe_connection_alias_permissions](#describe_connection_alias_permissions)
    - [describe_connection_aliases](#describe_connection_aliases)
    - [describe_ip_groups](#describe_ip_groups)
    - [describe_tags](#describe_tags)
    - [describe_workspace_bundles](#describe_workspace_bundles)
    - [describe_workspace_directories](#describe_workspace_directories)
    - [describe_workspace_image_permissions](#describe_workspace_image_permissions)
    - [describe_workspace_images](#describe_workspace_images)
    - [describe_workspace_snapshots](#describe_workspace_snapshots)
    - [describe_workspaces](#describe_workspaces)
    - [describe_workspaces_connection_status](#describe_workspaces_connection_status)
    - [disassociate_connection_alias](#disassociate_connection_alias)
    - [disassociate_ip_groups](#disassociate_ip_groups)
    - [generate_presigned_url](#generate_presigned_url)
    - [import_workspace_image](#import_workspace_image)
    - [list_available_management_cidr_ranges](#list_available_management_cidr_ranges)
    - [migrate_workspace](#migrate_workspace)
    - [modify_account](#modify_account)
    - [modify_client_properties](#modify_client_properties)
    - [modify_selfservice_permissions](#modify_selfservice_permissions)
    - [modify_workspace_access_properties](#modify_workspace_access_properties)
    - [modify_workspace_creation_properties](#modify_workspace_creation_properties)
    - [modify_workspace_properties](#modify_workspace_properties)
    - [modify_workspace_state](#modify_workspace_state)
    - [reboot_workspaces](#reboot_workspaces)
    - [rebuild_workspaces](#rebuild_workspaces)
    - [register_workspace_directory](#register_workspace_directory)
    - [restore_workspace](#restore_workspace)
    - [revoke_ip_rules](#revoke_ip_rules)
    - [start_workspaces](#start_workspaces)
    - [stop_workspaces](#stop_workspaces)
    - [terminate_workspaces](#terminate_workspaces)
    - [update_connection_alias_permission](#update_connection_alias_permission)
    - [update_rules_of_ip_group](#update_rules_of_ip_group)
    - [update_workspace_bundle](#update_workspace_bundle)
    - [update_workspace_image_permission](#update_workspace_image_permission)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)

## WorkSpacesClient

Type annotations for `boto3.client("workspaces")`

Can be used directly:

```python
from mypy_boto3_workspaces.client import WorkSpacesClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_workspaces.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InvalidParameterValuesException`
- `Exceptions.InvalidResourceStateException`
- `Exceptions.OperationInProgressException`
- `Exceptions.OperationNotSupportedException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceAssociatedException`
- `Exceptions.ResourceCreationFailedException`
- `Exceptions.ResourceLimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceUnavailableException`
- `Exceptions.UnsupportedNetworkConfigurationException`
- `Exceptions.UnsupportedWorkspaceConfigurationException`
- `Exceptions.WorkspacesDefaultRoleNotFoundException`


## Methods


### associate_connection_alias

Type annotations for `boto3.client("workspaces").associate_connection_alias` method.

[Client.associate_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.associate_connection_alias)

```python
def associate_connection_alias(
    self,
    AliasId: str,
    ResourceId: str
) -> AssociateConnectionAliasResultTypeDef:
    pass
```

### associate_ip_groups

Type annotations for `boto3.client("workspaces").associate_ip_groups` method.

[Client.associate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.associate_ip_groups)

```python
def associate_ip_groups(
    self,
    DirectoryId: str,
    GroupIds: List[str]
) -> Dict[str, Any]:
    pass
```

### authorize_ip_rules

Type annotations for `boto3.client("workspaces").authorize_ip_rules` method.

[Client.authorize_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.authorize_ip_rules)

```python
def authorize_ip_rules(
    self,
    GroupId: str,
    UserRules: List["IpRuleItemTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("workspaces").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### copy_workspace_image

Type annotations for `boto3.client("workspaces").copy_workspace_image` method.

[Client.copy_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.copy_workspace_image)

```python
def copy_workspace_image(
    self,
    Name: str,
    SourceImageId: str,
    SourceRegion: str,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CopyWorkspaceImageResultTypeDef:
    pass
```

### create_connection_alias

Type annotations for `boto3.client("workspaces").create_connection_alias` method.

[Client.create_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.create_connection_alias)

```python
def create_connection_alias(
    self,
    ConnectionString: str,
    Tags: List["TagTypeDef"] = None
) -> CreateConnectionAliasResultTypeDef:
    pass
```

### create_ip_group

Type annotations for `boto3.client("workspaces").create_ip_group` method.

[Client.create_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.create_ip_group)

```python
def create_ip_group(
    self,
    GroupName: str,
    GroupDesc: str = None,
    UserRules: List["IpRuleItemTypeDef"] = None,
    Tags: List["TagTypeDef"] = None
) -> CreateIpGroupResultTypeDef:
    pass
```

### create_tags

Type annotations for `boto3.client("workspaces").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.create_tags)

```python
def create_tags(
    self,
    ResourceId: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### create_workspace_bundle

Type annotations for `boto3.client("workspaces").create_workspace_bundle` method.

[Client.create_workspace_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.create_workspace_bundle)

```python
def create_workspace_bundle(
    self,
    BundleName: str,
    BundleDescription: str,
    ImageId: str,
    ComputeType: "ComputeTypeTypeDef",
    UserStorage: "UserStorageTypeDef",
    RootStorage: "RootStorageTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> CreateWorkspaceBundleResultTypeDef:
    pass
```

### create_workspaces

Type annotations for `boto3.client("workspaces").create_workspaces` method.

[Client.create_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.create_workspaces)

```python
def create_workspaces(
    self,
    Workspaces: List["WorkspaceRequestTypeDef"]
) -> CreateWorkspacesResultTypeDef:
    pass
```

### delete_connection_alias

Type annotations for `boto3.client("workspaces").delete_connection_alias` method.

[Client.delete_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.delete_connection_alias)

```python
def delete_connection_alias(
    self,
    AliasId: str
) -> Dict[str, Any]:
    pass
```

### delete_ip_group

Type annotations for `boto3.client("workspaces").delete_ip_group` method.

[Client.delete_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.delete_ip_group)

```python
def delete_ip_group(
    self,
    GroupId: str
) -> Dict[str, Any]:
    pass
```

### delete_tags

Type annotations for `boto3.client("workspaces").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.delete_tags)

```python
def delete_tags(
    self,
    ResourceId: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### delete_workspace_bundle

Type annotations for `boto3.client("workspaces").delete_workspace_bundle` method.

[Client.delete_workspace_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_bundle)

```python
def delete_workspace_bundle(
    self,
    BundleId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_workspace_image

Type annotations for `boto3.client("workspaces").delete_workspace_image` method.

[Client.delete_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.delete_workspace_image)

```python
def delete_workspace_image(
    self,
    ImageId: str
) -> Dict[str, Any]:
    pass
```

### deregister_workspace_directory

Type annotations for `boto3.client("workspaces").deregister_workspace_directory` method.

[Client.deregister_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.deregister_workspace_directory)

```python
def deregister_workspace_directory(
    self,
    DirectoryId: str
) -> Dict[str, Any]:
    pass
```

### describe_account

Type annotations for `boto3.client("workspaces").describe_account` method.

[Client.describe_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_account)

```python
def describe_account(
    self
) -> DescribeAccountResultTypeDef:
    pass
```

### describe_account_modifications

Type annotations for `boto3.client("workspaces").describe_account_modifications` method.

[Client.describe_account_modifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_account_modifications)

```python
def describe_account_modifications(
    self,
    NextToken: str = None
) -> DescribeAccountModificationsResultTypeDef:
    pass
```

### describe_client_properties

Type annotations for `boto3.client("workspaces").describe_client_properties` method.

[Client.describe_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_client_properties)

```python
def describe_client_properties(
    self,
    ResourceIds: List[str]
) -> DescribeClientPropertiesResultTypeDef:
    pass
```

### describe_connection_alias_permissions

Type annotations for `boto3.client("workspaces").describe_connection_alias_permissions` method.

[Client.describe_connection_alias_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_alias_permissions)

```python
def describe_connection_alias_permissions(
    self,
    AliasId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeConnectionAliasPermissionsResultTypeDef:
    pass
```

### describe_connection_aliases

Type annotations for `boto3.client("workspaces").describe_connection_aliases` method.

[Client.describe_connection_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_connection_aliases)

```python
def describe_connection_aliases(
    self,
    AliasIds: List[str] = None,
    ResourceId: str = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeConnectionAliasesResultTypeDef:
    pass
```

### describe_ip_groups

Type annotations for `boto3.client("workspaces").describe_ip_groups` method.

[Client.describe_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_ip_groups)

```python
def describe_ip_groups(
    self,
    GroupIds: List[str] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeIpGroupsResultTypeDef:
    pass
```

### describe_tags

Type annotations for `boto3.client("workspaces").describe_tags` method.

[Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_tags)

```python
def describe_tags(
    self,
    ResourceId: str
) -> DescribeTagsResultTypeDef:
    pass
```

### describe_workspace_bundles

Type annotations for `boto3.client("workspaces").describe_workspace_bundles` method.

[Client.describe_workspace_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_bundles)

```python
def describe_workspace_bundles(
    self,
    BundleIds: List[str] = None,
    Owner: str = None,
    NextToken: str = None
) -> DescribeWorkspaceBundlesResultTypeDef:
    pass
```

### describe_workspace_directories

Type annotations for `boto3.client("workspaces").describe_workspace_directories` method.

[Client.describe_workspace_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_directories)

```python
def describe_workspace_directories(
    self,
    DirectoryIds: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeWorkspaceDirectoriesResultTypeDef:
    pass
```

### describe_workspace_image_permissions

Type annotations for `boto3.client("workspaces").describe_workspace_image_permissions` method.

[Client.describe_workspace_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_image_permissions)

```python
def describe_workspace_image_permissions(
    self,
    ImageId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeWorkspaceImagePermissionsResultTypeDef:
    pass
```

### describe_workspace_images

Type annotations for `boto3.client("workspaces").describe_workspace_images` method.

[Client.describe_workspace_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_images)

```python
def describe_workspace_images(
    self,
    ImageIds: List[str] = None,
    ImageType: ImageType = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeWorkspaceImagesResultTypeDef:
    pass
```

### describe_workspace_snapshots

Type annotations for `boto3.client("workspaces").describe_workspace_snapshots` method.

[Client.describe_workspace_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspace_snapshots)

```python
def describe_workspace_snapshots(
    self,
    WorkspaceId: str
) -> DescribeWorkspaceSnapshotsResultTypeDef:
    pass
```

### describe_workspaces

Type annotations for `boto3.client("workspaces").describe_workspaces` method.

[Client.describe_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces)

```python
def describe_workspaces(
    self,
    WorkspaceIds: List[str] = None,
    DirectoryId: str = None,
    UserName: str = None,
    BundleId: str = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeWorkspacesResultTypeDef:
    pass
```

### describe_workspaces_connection_status

Type annotations for `boto3.client("workspaces").describe_workspaces_connection_status` method.

[Client.describe_workspaces_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.describe_workspaces_connection_status)

```python
def describe_workspaces_connection_status(
    self,
    WorkspaceIds: List[str] = None,
    NextToken: str = None
) -> DescribeWorkspacesConnectionStatusResultTypeDef:
    pass
```

### disassociate_connection_alias

Type annotations for `boto3.client("workspaces").disassociate_connection_alias` method.

[Client.disassociate_connection_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.disassociate_connection_alias)

```python
def disassociate_connection_alias(
    self,
    AliasId: str
) -> Dict[str, Any]:
    pass
```

### disassociate_ip_groups

Type annotations for `boto3.client("workspaces").disassociate_ip_groups` method.

[Client.disassociate_ip_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.disassociate_ip_groups)

```python
def disassociate_ip_groups(
    self,
    DirectoryId: str,
    GroupIds: List[str]
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("workspaces").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.generate_presigned_url)

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

### import_workspace_image

Type annotations for `boto3.client("workspaces").import_workspace_image` method.

[Client.import_workspace_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.import_workspace_image)

```python
def import_workspace_image(
    self,
    Ec2ImageId: str,
    IngestionProcess: WorkspaceImageIngestionProcess,
    ImageName: str,
    ImageDescription: str,
    Tags: List["TagTypeDef"] = None,
    Applications: List[Application] = None
) -> ImportWorkspaceImageResultTypeDef:
    pass
```

### list_available_management_cidr_ranges

Type annotations for `boto3.client("workspaces").list_available_management_cidr_ranges` method.

[Client.list_available_management_cidr_ranges documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.list_available_management_cidr_ranges)

```python
def list_available_management_cidr_ranges(
    self,
    ManagementCidrRangeConstraint: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListAvailableManagementCidrRangesResultTypeDef:
    pass
```

### migrate_workspace

Type annotations for `boto3.client("workspaces").migrate_workspace` method.

[Client.migrate_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.migrate_workspace)

```python
def migrate_workspace(
    self,
    SourceWorkspaceId: str,
    BundleId: str
) -> MigrateWorkspaceResultTypeDef:
    pass
```

### modify_account

Type annotations for `boto3.client("workspaces").modify_account` method.

[Client.modify_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_account)

```python
def modify_account(
    self,
    DedicatedTenancySupport: DedicatedTenancySupportEnum = None,
    DedicatedTenancyManagementCidrRange: str = None
) -> Dict[str, Any]:
    pass
```

### modify_client_properties

Type annotations for `boto3.client("workspaces").modify_client_properties` method.

[Client.modify_client_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_client_properties)

```python
def modify_client_properties(
    self,
    ResourceId: str,
    ClientProperties: "ClientPropertiesTypeDef"
) -> Dict[str, Any]:
    pass
```

### modify_selfservice_permissions

Type annotations for `boto3.client("workspaces").modify_selfservice_permissions` method.

[Client.modify_selfservice_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_selfservice_permissions)

```python
def modify_selfservice_permissions(
    self,
    ResourceId: str,
    SelfservicePermissions: "SelfservicePermissionsTypeDef"
) -> Dict[str, Any]:
    pass
```

### modify_workspace_access_properties

Type annotations for `boto3.client("workspaces").modify_workspace_access_properties` method.

[Client.modify_workspace_access_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_access_properties)

```python
def modify_workspace_access_properties(
    self,
    ResourceId: str,
    WorkspaceAccessProperties: "WorkspaceAccessPropertiesTypeDef"
) -> Dict[str, Any]:
    pass
```

### modify_workspace_creation_properties

Type annotations for `boto3.client("workspaces").modify_workspace_creation_properties` method.

[Client.modify_workspace_creation_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_creation_properties)

```python
def modify_workspace_creation_properties(
    self,
    ResourceId: str,
    WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef
) -> Dict[str, Any]:
    pass
```

### modify_workspace_properties

Type annotations for `boto3.client("workspaces").modify_workspace_properties` method.

[Client.modify_workspace_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_properties)

```python
def modify_workspace_properties(
    self,
    WorkspaceId: str,
    WorkspaceProperties: "WorkspacePropertiesTypeDef"
) -> Dict[str, Any]:
    pass
```

### modify_workspace_state

Type annotations for `boto3.client("workspaces").modify_workspace_state` method.

[Client.modify_workspace_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.modify_workspace_state)

```python
def modify_workspace_state(
    self,
    WorkspaceId: str,
    WorkspaceState: TargetWorkspaceState
) -> Dict[str, Any]:
    pass
```

### reboot_workspaces

Type annotations for `boto3.client("workspaces").reboot_workspaces` method.

[Client.reboot_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.reboot_workspaces)

```python
def reboot_workspaces(
    self,
    RebootWorkspaceRequests: List[RebootRequestTypeDef]
) -> RebootWorkspacesResultTypeDef:
    pass
```

### rebuild_workspaces

Type annotations for `boto3.client("workspaces").rebuild_workspaces` method.

[Client.rebuild_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.rebuild_workspaces)

```python
def rebuild_workspaces(
    self,
    RebuildWorkspaceRequests: List[RebuildRequestTypeDef]
) -> RebuildWorkspacesResultTypeDef:
    pass
```

### register_workspace_directory

Type annotations for `boto3.client("workspaces").register_workspace_directory` method.

[Client.register_workspace_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.register_workspace_directory)

```python
def register_workspace_directory(
    self,
    DirectoryId: str,
    EnableWorkDocs: bool,
    SubnetIds: List[str] = None,
    EnableSelfService: bool = None,
    Tenancy: Tenancy = None,
    Tags: List["TagTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### restore_workspace

Type annotations for `boto3.client("workspaces").restore_workspace` method.

[Client.restore_workspace documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.restore_workspace)

```python
def restore_workspace(
    self,
    WorkspaceId: str
) -> Dict[str, Any]:
    pass
```

### revoke_ip_rules

Type annotations for `boto3.client("workspaces").revoke_ip_rules` method.

[Client.revoke_ip_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.revoke_ip_rules)

```python
def revoke_ip_rules(
    self,
    GroupId: str,
    UserRules: List[str]
) -> Dict[str, Any]:
    pass
```

### start_workspaces

Type annotations for `boto3.client("workspaces").start_workspaces` method.

[Client.start_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.start_workspaces)

```python
def start_workspaces(
    self,
    StartWorkspaceRequests: List[StartRequestTypeDef]
) -> StartWorkspacesResultTypeDef:
    pass
```

### stop_workspaces

Type annotations for `boto3.client("workspaces").stop_workspaces` method.

[Client.stop_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.stop_workspaces)

```python
def stop_workspaces(
    self,
    StopWorkspaceRequests: List[StopRequestTypeDef]
) -> StopWorkspacesResultTypeDef:
    pass
```

### terminate_workspaces

Type annotations for `boto3.client("workspaces").terminate_workspaces` method.

[Client.terminate_workspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.terminate_workspaces)

```python
def terminate_workspaces(
    self,
    TerminateWorkspaceRequests: List[TerminateRequestTypeDef]
) -> TerminateWorkspacesResultTypeDef:
    pass
```

### update_connection_alias_permission

Type annotations for `boto3.client("workspaces").update_connection_alias_permission` method.

[Client.update_connection_alias_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.update_connection_alias_permission)

```python
def update_connection_alias_permission(
    self,
    AliasId: str,
    ConnectionAliasPermission: "ConnectionAliasPermissionTypeDef"
) -> Dict[str, Any]:
    pass
```

### update_rules_of_ip_group

Type annotations for `boto3.client("workspaces").update_rules_of_ip_group` method.

[Client.update_rules_of_ip_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.update_rules_of_ip_group)

```python
def update_rules_of_ip_group(
    self,
    GroupId: str,
    UserRules: List["IpRuleItemTypeDef"]
) -> Dict[str, Any]:
    pass
```

### update_workspace_bundle

Type annotations for `boto3.client("workspaces").update_workspace_bundle` method.

[Client.update_workspace_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_bundle)

```python
def update_workspace_bundle(
    self,
    BundleId: str = None,
    ImageId: str = None
) -> Dict[str, Any]:
    pass
```

### update_workspace_image_permission

Type annotations for `boto3.client("workspaces").update_workspace_image_permission` method.

[Client.update_workspace_image_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Client.update_workspace_image_permission)

```python
def update_workspace_image_permission(
    self,
    ImageId: str,
    AllowCopyImage: bool,
    SharedAccountId: str
) -> Dict[str, Any]:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAccountModificationsPaginatorName
) -> DescribeAccountModificationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeIpGroupsPaginatorName
) -> DescribeIpGroupsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeWorkspaceBundlesPaginatorName
) -> DescribeWorkspaceBundlesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeWorkspaceDirectoriesPaginatorName
) -> DescribeWorkspaceDirectoriesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeWorkspaceImagesPaginatorName
) -> DescribeWorkspaceImagesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeWorkspacesPaginatorName
) -> DescribeWorkspacesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeWorkspacesConnectionStatusPaginatorName
) -> DescribeWorkspacesConnectionStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("workspaces").get_paginator` method.

[Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAvailableManagementCidrRangesPaginatorName
) -> ListAvailableManagementCidrRangesPaginator:
    pass
```