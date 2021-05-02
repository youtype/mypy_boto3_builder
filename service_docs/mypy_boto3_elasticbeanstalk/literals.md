# Literals for boto3 ElasticBeanstalk module

> [Index](../index.md) > [ElasticBeanstalk](./index.md) > Literals

Auto-generated documentation for [ElasticBeanstalk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html#ElasticBeanstalk)
type annotations stubs module [mypy_boto3_elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/).

- [Literals for boto3 ElasticBeanstalk module](#literals-for-boto3-elasticbeanstalk-module)
  - [ActionHistoryStatus](#actionhistorystatus)
  - [ActionStatus](#actionstatus)
  - [ActionType](#actiontype)
  - [ApplicationVersionStatus](#applicationversionstatus)
  - [ComputeType](#computetype)
  - [ConfigurationDeploymentStatus](#configurationdeploymentstatus)
  - [ConfigurationOptionValueType](#configurationoptionvaluetype)
  - [DescribeApplicationVersionsPaginatorName](#describeapplicationversionspaginatorname)
  - [DescribeEnvironmentManagedActionHistoryPaginatorName](#describeenvironmentmanagedactionhistorypaginatorname)
  - [DescribeEnvironmentsPaginatorName](#describeenvironmentspaginatorname)
  - [DescribeEventsPaginatorName](#describeeventspaginatorname)
  - [EnvironmentExistsWaiterName](#environmentexistswaitername)
  - [EnvironmentHealth](#environmenthealth)
  - [EnvironmentHealthAttribute](#environmenthealthattribute)
  - [EnvironmentHealthStatus](#environmenthealthstatus)
  - [EnvironmentInfoType](#environmentinfotype)
  - [EnvironmentStatus](#environmentstatus)
  - [EnvironmentTerminatedWaiterName](#environmentterminatedwaitername)
  - [EnvironmentUpdatedWaiterName](#environmentupdatedwaitername)
  - [EventSeverity](#eventseverity)
  - [FailureType](#failuretype)
  - [InstancesHealthAttribute](#instanceshealthattribute)
  - [ListPlatformVersionsPaginatorName](#listplatformversionspaginatorname)
  - [PlatformStatus](#platformstatus)
  - [SourceRepository](#sourcerepository)
  - [SourceType](#sourcetype)
  - [ValidationSeverity](#validationseverity)

## ActionHistoryStatus

```python
from mypy_boto3_elasticbeanstalk.literals import ActionHistoryStatus
```

Values:

- `Completed`
- `Failed`
- `Unknown`

## ActionStatus

```python
from mypy_boto3_elasticbeanstalk.literals import ActionStatus
```

Values:

- `Pending`
- `Running`
- `Scheduled`
- `Unknown`

## ActionType

```python
from mypy_boto3_elasticbeanstalk.literals import ActionType
```

Values:

- `InstanceRefresh`
- `PlatformUpdate`
- `Unknown`

## ApplicationVersionStatus

```python
from mypy_boto3_elasticbeanstalk.literals import ApplicationVersionStatus
```

Values:

- `Building`
- `Failed`
- `Processed`
- `Processing`
- `Unprocessed`

## ComputeType

```python
from mypy_boto3_elasticbeanstalk.literals import ComputeType
```

Values:

- `BUILD_GENERAL1_LARGE`
- `BUILD_GENERAL1_MEDIUM`
- `BUILD_GENERAL1_SMALL`

## ConfigurationDeploymentStatus

```python
from mypy_boto3_elasticbeanstalk.literals import ConfigurationDeploymentStatus
```

Values:

- `deployed`
- `failed`
- `pending`

## ConfigurationOptionValueType

```python
from mypy_boto3_elasticbeanstalk.literals import ConfigurationOptionValueType
```

Values:

- `List`
- `Scalar`

## DescribeApplicationVersionsPaginatorName

```python
from mypy_boto3_elasticbeanstalk.literals import DescribeApplicationVersionsPaginatorName
```

Values:

- `describe_application_versions`

## DescribeEnvironmentManagedActionHistoryPaginatorName

```python
from mypy_boto3_elasticbeanstalk.literals import DescribeEnvironmentManagedActionHistoryPaginatorName
```

Values:

- `describe_environment_managed_action_history`

## DescribeEnvironmentsPaginatorName

```python
from mypy_boto3_elasticbeanstalk.literals import DescribeEnvironmentsPaginatorName
```

Values:

- `describe_environments`

## DescribeEventsPaginatorName

```python
from mypy_boto3_elasticbeanstalk.literals import DescribeEventsPaginatorName
```

Values:

- `describe_events`

## EnvironmentExistsWaiterName

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentExistsWaiterName
```

Values:

- `environment_exists`

## EnvironmentHealth

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentHealth
```

Values:

- `Green`
- `Grey`
- `Red`
- `Yellow`

## EnvironmentHealthAttribute

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentHealthAttribute
```

Values:

- `All`
- `ApplicationMetrics`
- `Causes`
- `Color`
- `HealthStatus`
- `InstancesHealth`
- `RefreshedAt`
- `Status`

## EnvironmentHealthStatus

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentHealthStatus
```

Values:

- `Degraded`
- `Info`
- `NoData`
- `Ok`
- `Pending`
- `Severe`
- `Suspended`
- `Unknown`
- `Warning`

## EnvironmentInfoType

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentInfoType
```

Values:

- `bundle`
- `tail`

## EnvironmentStatus

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentStatus
```

Values:

- `Aborting`
- `Launching`
- `LinkingFrom`
- `LinkingTo`
- `Ready`
- `Terminated`
- `Terminating`
- `Updating`

## EnvironmentTerminatedWaiterName

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentTerminatedWaiterName
```

Values:

- `environment_terminated`

## EnvironmentUpdatedWaiterName

```python
from mypy_boto3_elasticbeanstalk.literals import EnvironmentUpdatedWaiterName
```

Values:

- `environment_updated`

## EventSeverity

```python
from mypy_boto3_elasticbeanstalk.literals import EventSeverity
```

Values:

- `DEBUG`
- `ERROR`
- `FATAL`
- `INFO`
- `TRACE`
- `WARN`

## FailureType

```python
from mypy_boto3_elasticbeanstalk.literals import FailureType
```

Values:

- `CancellationFailed`
- `InternalFailure`
- `InvalidEnvironmentState`
- `PermissionsError`
- `RollbackFailed`
- `RollbackSuccessful`
- `UpdateCancelled`

## InstancesHealthAttribute

```python
from mypy_boto3_elasticbeanstalk.literals import InstancesHealthAttribute
```

Values:

- `All`
- `ApplicationMetrics`
- `AvailabilityZone`
- `Causes`
- `Color`
- `Deployment`
- `HealthStatus`
- `InstanceType`
- `LaunchedAt`
- `RefreshedAt`
- `System`

## ListPlatformVersionsPaginatorName

```python
from mypy_boto3_elasticbeanstalk.literals import ListPlatformVersionsPaginatorName
```

Values:

- `list_platform_versions`

## PlatformStatus

```python
from mypy_boto3_elasticbeanstalk.literals import PlatformStatus
```

Values:

- `Creating`
- `Deleted`
- `Deleting`
- `Failed`
- `Ready`

## SourceRepository

```python
from mypy_boto3_elasticbeanstalk.literals import SourceRepository
```

Values:

- `CodeCommit`
- `S3`

## SourceType

```python
from mypy_boto3_elasticbeanstalk.literals import SourceType
```

Values:

- `Git`
- `Zip`

## ValidationSeverity

```python
from mypy_boto3_elasticbeanstalk.literals import ValidationSeverity
```

Values:

- `error`
- `warning`
