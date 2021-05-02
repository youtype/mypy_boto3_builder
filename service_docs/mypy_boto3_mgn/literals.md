# Literals for boto3 mgn module

> [Index](../index.md) > [mgn](./index.md) > Literals

Auto-generated documentation for [mgn](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn)
type annotations stubs module [mypy_boto3_mgn](https://pypi.org/project/mypy-boto3-mgn/).

- [Literals for boto3 mgn module](#literals-for-boto3-mgn-module)
  - [ChangeServerLifeCycleStateSourceServerLifecycleState](#changeserverlifecyclestatesourceserverlifecyclestate)
  - [DataReplicationErrorString](#datareplicationerrorstring)
  - [DataReplicationInitiationStepName](#datareplicationinitiationstepname)
  - [DataReplicationInitiationStepStatus](#datareplicationinitiationstepstatus)
  - [DataReplicationState](#datareplicationstate)
  - [DescribeJobLogItemsPaginatorName](#describejoblogitemspaginatorname)
  - [DescribeJobsPaginatorName](#describejobspaginatorname)
  - [DescribeReplicationConfigurationTemplatesPaginatorName](#describereplicationconfigurationtemplatespaginatorname)
  - [DescribeSourceServersPaginatorName](#describesourceserverspaginatorname)
  - [FirstBoot](#firstboot)
  - [InitiatedBy](#initiatedby)
  - [JobLogEvent](#joblogevent)
  - [JobStatus](#jobstatus)
  - [JobType](#jobtype)
  - [LaunchDisposition](#launchdisposition)
  - [LaunchStatus](#launchstatus)
  - [LifeCycleState](#lifecyclestate)
  - [ReplicationConfigurationDataPlaneRouting](#replicationconfigurationdataplanerouting)
  - [ReplicationConfigurationDefaultLargeStagingDiskType](#replicationconfigurationdefaultlargestagingdisktype)
  - [ReplicationConfigurationEbsEncryption](#replicationconfigurationebsencryption)
  - [ReplicationConfigurationReplicatedDiskStagingDiskType](#replicationconfigurationreplicateddiskstagingdisktype)
  - [TargetInstanceTypeRightSizingMethod](#targetinstancetyperightsizingmethod)

## ChangeServerLifeCycleStateSourceServerLifecycleState

```python
from mypy_boto3_mgn.literals import ChangeServerLifeCycleStateSourceServerLifecycleState
```

Values:

- `CUTOVER`
- `READY_FOR_CUTOVER`
- `READY_FOR_TEST`

## DataReplicationErrorString

```python
from mypy_boto3_mgn.literals import DataReplicationErrorString
```

Values:

- `AGENT_NOT_SEEN`
- `FAILED_TO_ATTACH_STAGING_DISKS`
- `FAILED_TO_AUTHENTICATE_WITH_SERVICE`
- `FAILED_TO_BOOT_REPLICATION_SERVER`
- `FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER`
- `FAILED_TO_CREATE_SECURITY_GROUP`
- `FAILED_TO_CREATE_STAGING_DISKS`
- `FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE`
- `FAILED_TO_LAUNCH_REPLICATION_SERVER`
- `FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT`
- `FAILED_TO_START_DATA_TRANSFER`
- `NOT_CONVERGING`
- `SNAPSHOTS_FAILURE`
- `UNSTABLE_NETWORK`

## DataReplicationInitiationStepName

```python
from mypy_boto3_mgn.literals import DataReplicationInitiationStepName
```

Values:

- `ATTACH_STAGING_DISKS`
- `AUTHENTICATE_WITH_SERVICE`
- `BOOT_REPLICATION_SERVER`
- `CONNECT_AGENT_TO_REPLICATION_SERVER`
- `CREATE_SECURITY_GROUP`
- `CREATE_STAGING_DISKS`
- `DOWNLOAD_REPLICATION_SOFTWARE`
- `LAUNCH_REPLICATION_SERVER`
- `PAIR_REPLICATION_SERVER_WITH_AGENT`
- `START_DATA_TRANSFER`
- `WAIT`

## DataReplicationInitiationStepStatus

```python
from mypy_boto3_mgn.literals import DataReplicationInitiationStepStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `NOT_STARTED`
- `SKIPPED`
- `SUCCEEDED`

## DataReplicationState

```python
from mypy_boto3_mgn.literals import DataReplicationState
```

Values:

- `BACKLOG`
- `CONTINUOUS`
- `CREATING_SNAPSHOT`
- `DISCONNECTED`
- `INITIAL_SYNC`
- `INITIATING`
- `PAUSED`
- `RESCAN`
- `STALLED`
- `STOPPED`

## DescribeJobLogItemsPaginatorName

```python
from mypy_boto3_mgn.literals import DescribeJobLogItemsPaginatorName
```

Values:

- `describe_job_log_items`

## DescribeJobsPaginatorName

```python
from mypy_boto3_mgn.literals import DescribeJobsPaginatorName
```

Values:

- `describe_jobs`

## DescribeReplicationConfigurationTemplatesPaginatorName

```python
from mypy_boto3_mgn.literals import DescribeReplicationConfigurationTemplatesPaginatorName
```

Values:

- `describe_replication_configuration_templates`

## DescribeSourceServersPaginatorName

```python
from mypy_boto3_mgn.literals import DescribeSourceServersPaginatorName
```

Values:

- `describe_source_servers`

## FirstBoot

```python
from mypy_boto3_mgn.literals import FirstBoot
```

Values:

- `STOPPED`
- `SUCCEEDED`
- `UNKNOWN`
- `WAITING`

## InitiatedBy

```python
from mypy_boto3_mgn.literals import InitiatedBy
```

Values:

- `DIAGNOSTIC`
- `START_CUTOVER`
- `START_TEST`
- `TERMINATE`

## JobLogEvent

```python
from mypy_boto3_mgn.literals import JobLogEvent
```

Values:

- `CLEANUP_END`
- `CLEANUP_FAIL`
- `CLEANUP_START`
- `CONVERSION_END`
- `CONVERSION_FAIL`
- `CONVERSION_START`
- `JOB_CANCEL`
- `JOB_END`
- `JOB_START`
- `LAUNCH_FAILED`
- `LAUNCH_START`
- `SERVER_SKIPPED`
- `SNAPSHOT_END`
- `SNAPSHOT_FAIL`
- `SNAPSHOT_START`
- `USING_PREVIOUS_SNAPSHOT`

## JobStatus

```python
from mypy_boto3_mgn.literals import JobStatus
```

Values:

- `COMPLETED`
- `PENDING`
- `STARTED`

## JobType

```python
from mypy_boto3_mgn.literals import JobType
```

Values:

- `LAUNCH`
- `TERMINATE`

## LaunchDisposition

```python
from mypy_boto3_mgn.literals import LaunchDisposition
```

Values:

- `STARTED`
- `STOPPED`

## LaunchStatus

```python
from mypy_boto3_mgn.literals import LaunchStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `LAUNCHED`
- `PENDING`
- `TERMINATED`

## LifeCycleState

```python
from mypy_boto3_mgn.literals import LifeCycleState
```

Values:

- `CUTOVER`
- `CUTTING_OVER`
- `DISCONNECTED`
- `NOT_READY`
- `READY_FOR_CUTOVER`
- `READY_FOR_TEST`
- `STOPPED`
- `TESTING`

## ReplicationConfigurationDataPlaneRouting

```python
from mypy_boto3_mgn.literals import ReplicationConfigurationDataPlaneRouting
```

Values:

- `PRIVATE_IP`
- `PUBLIC_IP`

## ReplicationConfigurationDefaultLargeStagingDiskType

```python
from mypy_boto3_mgn.literals import ReplicationConfigurationDefaultLargeStagingDiskType
```

Values:

- `GP2`
- `ST1`

## ReplicationConfigurationEbsEncryption

```python
from mypy_boto3_mgn.literals import ReplicationConfigurationEbsEncryption
```

Values:

- `CUSTOM`
- `DEFAULT`
- `NONE`

## ReplicationConfigurationReplicatedDiskStagingDiskType

```python
from mypy_boto3_mgn.literals import ReplicationConfigurationReplicatedDiskStagingDiskType
```

Values:

- `AUTO`
- `GP2`
- `IO1`
- `SC1`
- `ST1`
- `STANDARD`

## TargetInstanceTypeRightSizingMethod

```python
from mypy_boto3_mgn.literals import TargetInstanceTypeRightSizingMethod
```

Values:

- `BASIC`
- `NONE`
