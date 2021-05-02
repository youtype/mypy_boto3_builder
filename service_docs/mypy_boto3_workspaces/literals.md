# Literals for boto3 WorkSpaces module

> [Index](../index.md) > [WorkSpaces](./index.md) > Literals

Auto-generated documentation for [WorkSpaces](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html#WorkSpaces)
type annotations stubs module [mypy_boto3_workspaces](https://pypi.org/project/mypy-boto3-workspaces/).

- [Literals for boto3 WorkSpaces module](#literals-for-boto3-workspaces-module)
  - [AccessPropertyValue](#accesspropertyvalue)
  - [Application](#application)
  - [AssociationStatus](#associationstatus)
  - [Compute](#compute)
  - [ConnectionAliasState](#connectionaliasstate)
  - [ConnectionState](#connectionstate)
  - [DedicatedTenancyModificationStateEnum](#dedicatedtenancymodificationstateenum)
  - [DedicatedTenancySupportEnum](#dedicatedtenancysupportenum)
  - [DedicatedTenancySupportResultEnum](#dedicatedtenancysupportresultenum)
  - [DescribeAccountModificationsPaginatorName](#describeaccountmodificationspaginatorname)
  - [DescribeIpGroupsPaginatorName](#describeipgroupspaginatorname)
  - [DescribeWorkspaceBundlesPaginatorName](#describeworkspacebundlespaginatorname)
  - [DescribeWorkspaceDirectoriesPaginatorName](#describeworkspacedirectoriespaginatorname)
  - [DescribeWorkspaceImagesPaginatorName](#describeworkspaceimagespaginatorname)
  - [DescribeWorkspacesConnectionStatusPaginatorName](#describeworkspacesconnectionstatuspaginatorname)
  - [DescribeWorkspacesPaginatorName](#describeworkspacespaginatorname)
  - [ImageType](#imagetype)
  - [ListAvailableManagementCidrRangesPaginatorName](#listavailablemanagementcidrrangespaginatorname)
  - [ModificationResourceEnum](#modificationresourceenum)
  - [ModificationStateEnum](#modificationstateenum)
  - [OperatingSystemType](#operatingsystemtype)
  - [ReconnectEnum](#reconnectenum)
  - [RunningMode](#runningmode)
  - [TargetWorkspaceState](#targetworkspacestate)
  - [Tenancy](#tenancy)
  - [WorkspaceDirectoryState](#workspacedirectorystate)
  - [WorkspaceDirectoryType](#workspacedirectorytype)
  - [WorkspaceImageIngestionProcess](#workspaceimageingestionprocess)
  - [WorkspaceImageRequiredTenancy](#workspaceimagerequiredtenancy)
  - [WorkspaceImageState](#workspaceimagestate)
  - [WorkspaceState](#workspacestate)

## AccessPropertyValue

```python
from mypy_boto3_workspaces.literals import AccessPropertyValue
```

Values:

- `ALLOW`
- `DENY`

## Application

```python
from mypy_boto3_workspaces.literals import Application
```

Values:

- `Microsoft_Office_2016`
- `Microsoft_Office_2019`

## AssociationStatus

```python
from mypy_boto3_workspaces.literals import AssociationStatus
```

Values:

- `ASSOCIATED_WITH_OWNER_ACCOUNT`
- `ASSOCIATED_WITH_SHARED_ACCOUNT`
- `NOT_ASSOCIATED`
- `PENDING_ASSOCIATION`
- `PENDING_DISASSOCIATION`

## Compute

```python
from mypy_boto3_workspaces.literals import Compute
```

Values:

- `GRAPHICS`
- `GRAPHICSPRO`
- `PERFORMANCE`
- `POWER`
- `POWERPRO`
- `STANDARD`
- `VALUE`

## ConnectionAliasState

```python
from mypy_boto3_workspaces.literals import ConnectionAliasState
```

Values:

- `CREATED`
- `CREATING`
- `DELETING`

## ConnectionState

```python
from mypy_boto3_workspaces.literals import ConnectionState
```

Values:

- `CONNECTED`
- `DISCONNECTED`
- `UNKNOWN`

## DedicatedTenancyModificationStateEnum

```python
from mypy_boto3_workspaces.literals import DedicatedTenancyModificationStateEnum
```

Values:

- `COMPLETED`
- `FAILED`
- `PENDING`

## DedicatedTenancySupportEnum

```python
from mypy_boto3_workspaces.literals import DedicatedTenancySupportEnum
```

Values:

- `ENABLED`

## DedicatedTenancySupportResultEnum

```python
from mypy_boto3_workspaces.literals import DedicatedTenancySupportResultEnum
```

Values:

- `DISABLED`
- `ENABLED`

## DescribeAccountModificationsPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeAccountModificationsPaginatorName
```

Values:

- `describe_account_modifications`

## DescribeIpGroupsPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeIpGroupsPaginatorName
```

Values:

- `describe_ip_groups`

## DescribeWorkspaceBundlesPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeWorkspaceBundlesPaginatorName
```

Values:

- `describe_workspace_bundles`

## DescribeWorkspaceDirectoriesPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeWorkspaceDirectoriesPaginatorName
```

Values:

- `describe_workspace_directories`

## DescribeWorkspaceImagesPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeWorkspaceImagesPaginatorName
```

Values:

- `describe_workspace_images`

## DescribeWorkspacesConnectionStatusPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeWorkspacesConnectionStatusPaginatorName
```

Values:

- `describe_workspaces_connection_status`

## DescribeWorkspacesPaginatorName

```python
from mypy_boto3_workspaces.literals import DescribeWorkspacesPaginatorName
```

Values:

- `describe_workspaces`

## ImageType

```python
from mypy_boto3_workspaces.literals import ImageType
```

Values:

- `OWNED`
- `SHARED`

## ListAvailableManagementCidrRangesPaginatorName

```python
from mypy_boto3_workspaces.literals import ListAvailableManagementCidrRangesPaginatorName
```

Values:

- `list_available_management_cidr_ranges`

## ModificationResourceEnum

```python
from mypy_boto3_workspaces.literals import ModificationResourceEnum
```

Values:

- `COMPUTE_TYPE`
- `ROOT_VOLUME`
- `USER_VOLUME`

## ModificationStateEnum

```python
from mypy_boto3_workspaces.literals import ModificationStateEnum
```

Values:

- `UPDATE_IN_PROGRESS`
- `UPDATE_INITIATED`

## OperatingSystemType

```python
from mypy_boto3_workspaces.literals import OperatingSystemType
```

Values:

- `LINUX`
- `WINDOWS`

## ReconnectEnum

```python
from mypy_boto3_workspaces.literals import ReconnectEnum
```

Values:

- `DISABLED`
- `ENABLED`

## RunningMode

```python
from mypy_boto3_workspaces.literals import RunningMode
```

Values:

- `ALWAYS_ON`
- `AUTO_STOP`

## TargetWorkspaceState

```python
from mypy_boto3_workspaces.literals import TargetWorkspaceState
```

Values:

- `ADMIN_MAINTENANCE`
- `AVAILABLE`

## Tenancy

```python
from mypy_boto3_workspaces.literals import Tenancy
```

Values:

- `DEDICATED`
- `SHARED`

## WorkspaceDirectoryState

```python
from mypy_boto3_workspaces.literals import WorkspaceDirectoryState
```

Values:

- `DEREGISTERED`
- `DEREGISTERING`
- `ERROR`
- `REGISTERED`
- `REGISTERING`

## WorkspaceDirectoryType

```python
from mypy_boto3_workspaces.literals import WorkspaceDirectoryType
```

Values:

- `AD_CONNECTOR`
- `SIMPLE_AD`

## WorkspaceImageIngestionProcess

```python
from mypy_boto3_workspaces.literals import WorkspaceImageIngestionProcess
```

Values:

- `BYOL_GRAPHICS`
- `BYOL_GRAPHICSPRO`
- `BYOL_REGULAR`
- `BYOL_REGULAR_WSP`

## WorkspaceImageRequiredTenancy

```python
from mypy_boto3_workspaces.literals import WorkspaceImageRequiredTenancy
```

Values:

- `DEDICATED`
- `DEFAULT`

## WorkspaceImageState

```python
from mypy_boto3_workspaces.literals import WorkspaceImageState
```

Values:

- `AVAILABLE`
- `ERROR`
- `PENDING`

## WorkspaceState

```python
from mypy_boto3_workspaces.literals import WorkspaceState
```

Values:

- `ADMIN_MAINTENANCE`
- `AVAILABLE`
- `ERROR`
- `IMPAIRED`
- `MAINTENANCE`
- `PENDING`
- `REBOOTING`
- `REBUILDING`
- `RESTORING`
- `STARTING`
- `STOPPED`
- `STOPPING`
- `SUSPENDED`
- `TERMINATED`
- `TERMINATING`
- `UNHEALTHY`
- `UPDATING`
