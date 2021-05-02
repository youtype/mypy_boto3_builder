# Literals for boto3 RoboMaker module

> [Index](../index.md) > [RoboMaker](./index.md) > Literals

Auto-generated documentation for [RoboMaker](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html#RoboMaker)
type annotations stubs module [mypy_boto3_robomaker](https://pypi.org/project/mypy-boto3-robomaker/).

- [Literals for boto3 RoboMaker module](#literals-for-boto3-robomaker-module)
  - [Architecture](#architecture)
  - [DeploymentJobErrorCode](#deploymentjoberrorcode)
  - [DeploymentStatus](#deploymentstatus)
  - [ExitBehavior](#exitbehavior)
  - [FailureBehavior](#failurebehavior)
  - [ListDeploymentJobsPaginatorName](#listdeploymentjobspaginatorname)
  - [ListFleetsPaginatorName](#listfleetspaginatorname)
  - [ListRobotApplicationsPaginatorName](#listrobotapplicationspaginatorname)
  - [ListRobotsPaginatorName](#listrobotspaginatorname)
  - [ListSimulationApplicationsPaginatorName](#listsimulationapplicationspaginatorname)
  - [ListSimulationJobBatchesPaginatorName](#listsimulationjobbatchespaginatorname)
  - [ListSimulationJobsPaginatorName](#listsimulationjobspaginatorname)
  - [ListWorldExportJobsPaginatorName](#listworldexportjobspaginatorname)
  - [ListWorldGenerationJobsPaginatorName](#listworldgenerationjobspaginatorname)
  - [ListWorldTemplatesPaginatorName](#listworldtemplatespaginatorname)
  - [ListWorldsPaginatorName](#listworldspaginatorname)
  - [RenderingEngineType](#renderingenginetype)
  - [RobotDeploymentStep](#robotdeploymentstep)
  - [RobotSoftwareSuiteType](#robotsoftwaresuitetype)
  - [RobotSoftwareSuiteVersionType](#robotsoftwaresuiteversiontype)
  - [RobotStatus](#robotstatus)
  - [SimulationJobBatchErrorCode](#simulationjobbatcherrorcode)
  - [SimulationJobBatchStatus](#simulationjobbatchstatus)
  - [SimulationJobErrorCode](#simulationjoberrorcode)
  - [SimulationJobStatus](#simulationjobstatus)
  - [SimulationSoftwareSuiteType](#simulationsoftwaresuitetype)
  - [UploadBehavior](#uploadbehavior)
  - [WorldExportJobErrorCode](#worldexportjoberrorcode)
  - [WorldExportJobStatus](#worldexportjobstatus)
  - [WorldGenerationJobErrorCode](#worldgenerationjoberrorcode)
  - [WorldGenerationJobStatus](#worldgenerationjobstatus)

## Architecture

```python
from mypy_boto3_robomaker.literals import Architecture
```

Values:

- `ARM64`
- `ARMHF`
- `X86_64`

## DeploymentJobErrorCode

```python
from mypy_boto3_robomaker.literals import DeploymentJobErrorCode
```

Values:

- `BadLambdaAssociated`
- `BadPermissionError`
- `DeploymentFleetDoesNotExist`
- `DownloadConditionFailed`
- `EnvironmentSetupError`
- `EtagMismatch`
- `ExtractingBundleFailure`
- `FailureThresholdBreached`
- `FleetDeploymentTimeout`
- `GreengrassDeploymentFailed`
- `GreengrassGroupVersionDoesNotExist`
- `InternalServerError`
- `InvalidGreengrassGroup`
- `LambdaDeleted`
- `MissingRobotApplicationArchitecture`
- `MissingRobotArchitecture`
- `MissingRobotDeploymentResource`
- `PostLaunchFileFailure`
- `PreLaunchFileFailure`
- `ResourceNotFound`
- `RobotAgentConnectionTimeout`
- `RobotApplicationDoesNotExist`
- `RobotDeploymentAborted`
- `RobotDeploymentNoResponse`

## DeploymentStatus

```python
from mypy_boto3_robomaker.literals import DeploymentStatus
```

Values:

- `Canceled`
- `Failed`
- `InProgress`
- `Pending`
- `Preparing`
- `Succeeded`

## ExitBehavior

```python
from mypy_boto3_robomaker.literals import ExitBehavior
```

Values:

- `FAIL`
- `RESTART`

## FailureBehavior

```python
from mypy_boto3_robomaker.literals import FailureBehavior
```

Values:

- `Continue`
- `Fail`

## ListDeploymentJobsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListDeploymentJobsPaginatorName
```

Values:

- `list_deployment_jobs`

## ListFleetsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListFleetsPaginatorName
```

Values:

- `list_fleets`

## ListRobotApplicationsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListRobotApplicationsPaginatorName
```

Values:

- `list_robot_applications`

## ListRobotsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListRobotsPaginatorName
```

Values:

- `list_robots`

## ListSimulationApplicationsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListSimulationApplicationsPaginatorName
```

Values:

- `list_simulation_applications`

## ListSimulationJobBatchesPaginatorName

```python
from mypy_boto3_robomaker.literals import ListSimulationJobBatchesPaginatorName
```

Values:

- `list_simulation_job_batches`

## ListSimulationJobsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListSimulationJobsPaginatorName
```

Values:

- `list_simulation_jobs`

## ListWorldExportJobsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListWorldExportJobsPaginatorName
```

Values:

- `list_world_export_jobs`

## ListWorldGenerationJobsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListWorldGenerationJobsPaginatorName
```

Values:

- `list_world_generation_jobs`

## ListWorldTemplatesPaginatorName

```python
from mypy_boto3_robomaker.literals import ListWorldTemplatesPaginatorName
```

Values:

- `list_world_templates`

## ListWorldsPaginatorName

```python
from mypy_boto3_robomaker.literals import ListWorldsPaginatorName
```

Values:

- `list_worlds`

## RenderingEngineType

```python
from mypy_boto3_robomaker.literals import RenderingEngineType
```

Values:

- `OGRE`

## RobotDeploymentStep

```python
from mypy_boto3_robomaker.literals import RobotDeploymentStep
```

Values:

- `DownloadingExtracting`
- `ExecutingDownloadCondition`
- `ExecutingPostLaunch`
- `ExecutingPreLaunch`
- `Finished`
- `Launching`
- `Validating`

## RobotSoftwareSuiteType

```python
from mypy_boto3_robomaker.literals import RobotSoftwareSuiteType
```

Values:

- `ROS`
- `ROS2`

## RobotSoftwareSuiteVersionType

```python
from mypy_boto3_robomaker.literals import RobotSoftwareSuiteVersionType
```

Values:

- `Dashing`
- `Foxy`
- `Kinetic`
- `Melodic`

## RobotStatus

```python
from mypy_boto3_robomaker.literals import RobotStatus
```

Values:

- `Available`
- `Deploying`
- `Failed`
- `InSync`
- `NoResponse`
- `PendingNewDeployment`
- `Registered`

## SimulationJobBatchErrorCode

```python
from mypy_boto3_robomaker.literals import SimulationJobBatchErrorCode
```

Values:

- `InternalServiceError`

## SimulationJobBatchStatus

```python
from mypy_boto3_robomaker.literals import SimulationJobBatchStatus
```

Values:

- `Canceled`
- `Canceling`
- `Completed`
- `Completing`
- `Failed`
- `InProgress`
- `Pending`
- `TimedOut`
- `TimingOut`

## SimulationJobErrorCode

```python
from mypy_boto3_robomaker.literals import SimulationJobErrorCode
```

Values:

- `BadPermissionsCloudwatchLogs`
- `BadPermissionsRobotApplication`
- `BadPermissionsS3Object`
- `BadPermissionsS3Output`
- `BadPermissionsSimulationApplication`
- `BadPermissionsUserCredentials`
- `BatchCanceled`
- `BatchTimedOut`
- `ENILimitExceeded`
- `InternalServiceError`
- `InvalidBundleRobotApplication`
- `InvalidBundleSimulationApplication`
- `InvalidInput`
- `InvalidS3Resource`
- `LimitExceeded`
- `MismatchedEtag`
- `RequestThrottled`
- `ResourceNotFound`
- `RobotApplicationCrash`
- `RobotApplicationHealthCheckFailure`
- `RobotApplicationVersionMismatchedEtag`
- `SimulationApplicationCrash`
- `SimulationApplicationHealthCheckFailure`
- `SimulationApplicationVersionMismatchedEtag`
- `SubnetIpLimitExceeded`
- `ThrottlingError`
- `UploadContentMismatchError`
- `WrongRegionRobotApplication`
- `WrongRegionS3Bucket`
- `WrongRegionS3Output`
- `WrongRegionSimulationApplication`

## SimulationJobStatus

```python
from mypy_boto3_robomaker.literals import SimulationJobStatus
```

Values:

- `Canceled`
- `Completed`
- `Failed`
- `Pending`
- `Preparing`
- `Restarting`
- `Running`
- `RunningFailed`
- `Terminated`
- `Terminating`

## SimulationSoftwareSuiteType

```python
from mypy_boto3_robomaker.literals import SimulationSoftwareSuiteType
```

Values:

- `Gazebo`
- `RosbagPlay`

## UploadBehavior

```python
from mypy_boto3_robomaker.literals import UploadBehavior
```

Values:

- `UPLOAD_ON_TERMINATE`
- `UPLOAD_ROLLING_AUTO_REMOVE`

## WorldExportJobErrorCode

```python
from mypy_boto3_robomaker.literals import WorldExportJobErrorCode
```

Values:

- `AccessDenied`
- `InternalServiceError`
- `InvalidInput`
- `LimitExceeded`
- `RequestThrottled`
- `ResourceNotFound`

## WorldExportJobStatus

```python
from mypy_boto3_robomaker.literals import WorldExportJobStatus
```

Values:

- `Canceled`
- `Canceling`
- `Completed`
- `Failed`
- `Pending`
- `Running`

## WorldGenerationJobErrorCode

```python
from mypy_boto3_robomaker.literals import WorldGenerationJobErrorCode
```

Values:

- `AllWorldGenerationFailed`
- `InternalServiceError`
- `InvalidInput`
- `LimitExceeded`
- `RequestThrottled`
- `ResourceNotFound`

## WorldGenerationJobStatus

```python
from mypy_boto3_robomaker.literals import WorldGenerationJobStatus
```

Values:

- `Canceled`
- `Canceling`
- `Completed`
- `Failed`
- `PartialFailed`
- `Pending`
- `Running`
