# Literals for boto3 Cloud9 module

> [Index](../index.md) > [Cloud9](./index.md) > Literals

Auto-generated documentation for [Cloud9](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9)
type annotations stubs module [mypy_boto3_cloud9](https://pypi.org/project/mypy-boto3-cloud9/).

- [Literals for boto3 Cloud9 module](#literals-for-boto3-cloud9-module)
  - [ConnectionType](#connectiontype)
  - [DescribeEnvironmentMembershipsPaginatorName](#describeenvironmentmembershipspaginatorname)
  - [EnvironmentLifecycleStatus](#environmentlifecyclestatus)
  - [EnvironmentStatus](#environmentstatus)
  - [EnvironmentType](#environmenttype)
  - [ListEnvironmentsPaginatorName](#listenvironmentspaginatorname)
  - [ManagedCredentialsStatus](#managedcredentialsstatus)
  - [MemberPermissions](#memberpermissions)
  - [Permissions](#permissions)

## ConnectionType

```python
from mypy_boto3_cloud9.literals import ConnectionType
```

Values:

- `CONNECT_SSH`
- `CONNECT_SSM`

## DescribeEnvironmentMembershipsPaginatorName

```python
from mypy_boto3_cloud9.literals import DescribeEnvironmentMembershipsPaginatorName
```

Values:

- `describe_environment_memberships`

## EnvironmentLifecycleStatus

```python
from mypy_boto3_cloud9.literals import EnvironmentLifecycleStatus
```

Values:

- `CREATE_FAILED`
- `CREATED`
- `CREATING`
- `DELETE_FAILED`
- `DELETING`

## EnvironmentStatus

```python
from mypy_boto3_cloud9.literals import EnvironmentStatus
```

Values:

- `connecting`
- `creating`
- `deleting`
- `error`
- `ready`
- `stopped`
- `stopping`

## EnvironmentType

```python
from mypy_boto3_cloud9.literals import EnvironmentType
```

Values:

- `ec2`
- `ssh`

## ListEnvironmentsPaginatorName

```python
from mypy_boto3_cloud9.literals import ListEnvironmentsPaginatorName
```

Values:

- `list_environments`

## ManagedCredentialsStatus

```python
from mypy_boto3_cloud9.literals import ManagedCredentialsStatus
```

Values:

- `DISABLED_BY_COLLABORATOR`
- `DISABLED_BY_DEFAULT`
- `DISABLED_BY_OWNER`
- `ENABLED_BY_OWNER`
- `ENABLED_ON_CREATE`
- `FAILED_REMOVAL_BY_COLLABORATOR`
- `FAILED_REMOVAL_BY_OWNER`
- `PENDING_REMOVAL_BY_COLLABORATOR`
- `PENDING_REMOVAL_BY_OWNER`
- `PENDING_START_REMOVAL_BY_COLLABORATOR`
- `PENDING_START_REMOVAL_BY_OWNER`

## MemberPermissions

```python
from mypy_boto3_cloud9.literals import MemberPermissions
```

Values:

- `read-only`
- `read-write`

## Permissions

```python
from mypy_boto3_cloud9.literals import Permissions
```

Values:

- `owner`
- `read-only`
- `read-write`
