# Literals for boto3 Batch module

> [Index](../index.md) > [Batch](./index.md) > Literals

Auto-generated documentation for [Batch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch)
type annotations stubs module [mypy_boto3_batch](https://pypi.org/project/mypy-boto3-batch/).

- [Literals for boto3 Batch module](#literals-for-boto3-batch-module)
  - [ArrayJobDependency](#arrayjobdependency)
  - [AssignPublicIp](#assignpublicip)
  - [CEState](#cestate)
  - [CEStatus](#cestatus)
  - [CEType](#cetype)
  - [CRAllocationStrategy](#crallocationstrategy)
  - [CRType](#crtype)
  - [DescribeComputeEnvironmentsPaginatorName](#describecomputeenvironmentspaginatorname)
  - [DescribeJobDefinitionsPaginatorName](#describejobdefinitionspaginatorname)
  - [DescribeJobQueuesPaginatorName](#describejobqueuespaginatorname)
  - [DeviceCgroupPermission](#devicecgrouppermission)
  - [EFSAuthorizationConfigIAM](#efsauthorizationconfigiam)
  - [EFSTransitEncryption](#efstransitencryption)
  - [JQState](#jqstate)
  - [JQStatus](#jqstatus)
  - [JobDefinitionType](#jobdefinitiontype)
  - [JobStatus](#jobstatus)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [LogDriver](#logdriver)
  - [PlatformCapability](#platformcapability)
  - [ResourceType](#resourcetype)
  - [RetryAction](#retryaction)

## ArrayJobDependency

```python
from mypy_boto3_batch.literals import ArrayJobDependency
```

Values:

- `N_TO_N`
- `SEQUENTIAL`

## AssignPublicIp

```python
from mypy_boto3_batch.literals import AssignPublicIp
```

Values:

- `DISABLED`
- `ENABLED`

## CEState

```python
from mypy_boto3_batch.literals import CEState
```

Values:

- `DISABLED`
- `ENABLED`

## CEStatus

```python
from mypy_boto3_batch.literals import CEStatus
```

Values:

- `CREATING`
- `DELETED`
- `DELETING`
- `INVALID`
- `UPDATING`
- `VALID`

## CEType

```python
from mypy_boto3_batch.literals import CEType
```

Values:

- `MANAGED`
- `UNMANAGED`

## CRAllocationStrategy

```python
from mypy_boto3_batch.literals import CRAllocationStrategy
```

Values:

- `BEST_FIT`
- `BEST_FIT_PROGRESSIVE`
- `SPOT_CAPACITY_OPTIMIZED`

## CRType

```python
from mypy_boto3_batch.literals import CRType
```

Values:

- `EC2`
- `FARGATE`
- `FARGATE_SPOT`
- `SPOT`

## DescribeComputeEnvironmentsPaginatorName

```python
from mypy_boto3_batch.literals import DescribeComputeEnvironmentsPaginatorName
```

Values:

- `describe_compute_environments`

## DescribeJobDefinitionsPaginatorName

```python
from mypy_boto3_batch.literals import DescribeJobDefinitionsPaginatorName
```

Values:

- `describe_job_definitions`

## DescribeJobQueuesPaginatorName

```python
from mypy_boto3_batch.literals import DescribeJobQueuesPaginatorName
```

Values:

- `describe_job_queues`

## DeviceCgroupPermission

```python
from mypy_boto3_batch.literals import DeviceCgroupPermission
```

Values:

- `MKNOD`
- `READ`
- `WRITE`

## EFSAuthorizationConfigIAM

```python
from mypy_boto3_batch.literals import EFSAuthorizationConfigIAM
```

Values:

- `DISABLED`
- `ENABLED`

## EFSTransitEncryption

```python
from mypy_boto3_batch.literals import EFSTransitEncryption
```

Values:

- `DISABLED`
- `ENABLED`

## JQState

```python
from mypy_boto3_batch.literals import JQState
```

Values:

- `DISABLED`
- `ENABLED`

## JQStatus

```python
from mypy_boto3_batch.literals import JQStatus
```

Values:

- `CREATING`
- `DELETED`
- `DELETING`
- `INVALID`
- `UPDATING`
- `VALID`

## JobDefinitionType

```python
from mypy_boto3_batch.literals import JobDefinitionType
```

Values:

- `container`
- `multinode`

## JobStatus

```python
from mypy_boto3_batch.literals import JobStatus
```

Values:

- `FAILED`
- `PENDING`
- `RUNNABLE`
- `RUNNING`
- `STARTING`
- `SUBMITTED`
- `SUCCEEDED`

## ListJobsPaginatorName

```python
from mypy_boto3_batch.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## LogDriver

```python
from mypy_boto3_batch.literals import LogDriver
```

Values:

- `awslogs`
- `fluentd`
- `gelf`
- `journald`
- `json-file`
- `splunk`
- `syslog`

## PlatformCapability

```python
from mypy_boto3_batch.literals import PlatformCapability
```

Values:

- `EC2`
- `FARGATE`

## ResourceType

```python
from mypy_boto3_batch.literals import ResourceType
```

Values:

- `GPU`
- `MEMORY`
- `VCPU`

## RetryAction

```python
from mypy_boto3_batch.literals import RetryAction
```

Values:

- `EXIT`
- `RETRY`
