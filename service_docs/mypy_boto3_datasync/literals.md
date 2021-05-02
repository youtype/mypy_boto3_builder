# Literals for boto3 DataSync module

> [Index](../index.md) > [DataSync](./index.md) > Literals

Auto-generated documentation for [DataSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html#DataSync)
type annotations stubs module [mypy_boto3_datasync](https://pypi.org/project/mypy-boto3-datasync/).

- [Literals for boto3 DataSync module](#literals-for-boto3-datasync-module)
  - [AgentStatus](#agentstatus)
  - [Atime](#atime)
  - [EndpointType](#endpointtype)
  - [FilterType](#filtertype)
  - [Gid](#gid)
  - [ListAgentsPaginatorName](#listagentspaginatorname)
  - [ListLocationsPaginatorName](#listlocationspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListTaskExecutionsPaginatorName](#listtaskexecutionspaginatorname)
  - [ListTasksPaginatorName](#listtaskspaginatorname)
  - [LocationFilterName](#locationfiltername)
  - [LogLevel](#loglevel)
  - [Mtime](#mtime)
  - [NfsVersion](#nfsversion)
  - [ObjectStorageServerProtocol](#objectstorageserverprotocol)
  - [Operator](#operator)
  - [OverwriteMode](#overwritemode)
  - [PhaseStatus](#phasestatus)
  - [PosixPermissions](#posixpermissions)
  - [PreserveDeletedFiles](#preservedeletedfiles)
  - [PreserveDevices](#preservedevices)
  - [S3StorageClass](#s3storageclass)
  - [SmbVersion](#smbversion)
  - [TaskExecutionStatus](#taskexecutionstatus)
  - [TaskFilterName](#taskfiltername)
  - [TaskQueueing](#taskqueueing)
  - [TaskStatus](#taskstatus)
  - [TransferMode](#transfermode)
  - [Uid](#uid)
  - [VerifyMode](#verifymode)

## AgentStatus

```python
from mypy_boto3_datasync.literals import AgentStatus
```

Values:

- `OFFLINE`
- `ONLINE`

## Atime

```python
from mypy_boto3_datasync.literals import Atime
```

Values:

- `BEST_EFFORT`
- `NONE`

## EndpointType

```python
from mypy_boto3_datasync.literals import EndpointType
```

Values:

- `FIPS`
- `PRIVATE_LINK`
- `PUBLIC`

## FilterType

```python
from mypy_boto3_datasync.literals import FilterType
```

Values:

- `SIMPLE_PATTERN`

## Gid

```python
from mypy_boto3_datasync.literals import Gid
```

Values:

- `BOTH`
- `INT_VALUE`
- `NAME`
- `NONE`

## ListAgentsPaginatorName

```python
from mypy_boto3_datasync.literals import ListAgentsPaginatorName
```

Values:

- `list_agents`

## ListLocationsPaginatorName

```python
from mypy_boto3_datasync.literals import ListLocationsPaginatorName
```

Values:

- `list_locations`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_datasync.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListTaskExecutionsPaginatorName

```python
from mypy_boto3_datasync.literals import ListTaskExecutionsPaginatorName
```

Values:

- `list_task_executions`

## ListTasksPaginatorName

```python
from mypy_boto3_datasync.literals import ListTasksPaginatorName
```

Values:

- `list_tasks`

## LocationFilterName

```python
from mypy_boto3_datasync.literals import LocationFilterName
```

Values:

- `CreationTime`
- `LocationType`
- `LocationUri`

## LogLevel

```python
from mypy_boto3_datasync.literals import LogLevel
```

Values:

- `BASIC`
- `OFF`
- `TRANSFER`

## Mtime

```python
from mypy_boto3_datasync.literals import Mtime
```

Values:

- `NONE`
- `PRESERVE`

## NfsVersion

```python
from mypy_boto3_datasync.literals import NfsVersion
```

Values:

- `AUTOMATIC`
- `NFS3`
- `NFS4_0`
- `NFS4_1`

## ObjectStorageServerProtocol

```python
from mypy_boto3_datasync.literals import ObjectStorageServerProtocol
```

Values:

- `HTTP`
- `HTTPS`

## Operator

```python
from mypy_boto3_datasync.literals import Operator
```

Values:

- `BeginsWith`
- `Contains`
- `Equals`
- `GreaterThan`
- `GreaterThanOrEqual`
- `In`
- `LessThan`
- `LessThanOrEqual`
- `NotContains`
- `NotEquals`

## OverwriteMode

```python
from mypy_boto3_datasync.literals import OverwriteMode
```

Values:

- `ALWAYS`
- `NEVER`

## PhaseStatus

```python
from mypy_boto3_datasync.literals import PhaseStatus
```

Values:

- `ERROR`
- `PENDING`
- `SUCCESS`

## PosixPermissions

```python
from mypy_boto3_datasync.literals import PosixPermissions
```

Values:

- `NONE`
- `PRESERVE`

## PreserveDeletedFiles

```python
from mypy_boto3_datasync.literals import PreserveDeletedFiles
```

Values:

- `PRESERVE`
- `REMOVE`

## PreserveDevices

```python
from mypy_boto3_datasync.literals import PreserveDevices
```

Values:

- `NONE`
- `PRESERVE`

## S3StorageClass

```python
from mypy_boto3_datasync.literals import S3StorageClass
```

Values:

- `DEEP_ARCHIVE`
- `GLACIER`
- `INTELLIGENT_TIERING`
- `ONEZONE_IA`
- `OUTPOSTS`
- `STANDARD`
- `STANDARD_IA`

## SmbVersion

```python
from mypy_boto3_datasync.literals import SmbVersion
```

Values:

- `AUTOMATIC`
- `SMB2`
- `SMB3`

## TaskExecutionStatus

```python
from mypy_boto3_datasync.literals import TaskExecutionStatus
```

Values:

- `ERROR`
- `LAUNCHING`
- `PREPARING`
- `QUEUED`
- `SUCCESS`
- `TRANSFERRING`
- `VERIFYING`

## TaskFilterName

```python
from mypy_boto3_datasync.literals import TaskFilterName
```

Values:

- `CreationTime`
- `LocationId`

## TaskQueueing

```python
from mypy_boto3_datasync.literals import TaskQueueing
```

Values:

- `DISABLED`
- `ENABLED`

## TaskStatus

```python
from mypy_boto3_datasync.literals import TaskStatus
```

Values:

- `AVAILABLE`
- `CREATING`
- `QUEUED`
- `RUNNING`
- `UNAVAILABLE`

## TransferMode

```python
from mypy_boto3_datasync.literals import TransferMode
```

Values:

- `ALL`
- `CHANGED`

## Uid

```python
from mypy_boto3_datasync.literals import Uid
```

Values:

- `BOTH`
- `INT_VALUE`
- `NAME`
- `NONE`

## VerifyMode

```python
from mypy_boto3_datasync.literals import VerifyMode
```

Values:

- `NONE`
- `ONLY_FILES_TRANSFERRED`
- `POINT_IN_TIME_CONSISTENT`
