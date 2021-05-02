# Literals for boto3 GreengrassV2 module

> [Index](../index.md) > [GreengrassV2](./index.md) > Literals

Auto-generated documentation for [GreengrassV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2)
type annotations stubs module [mypy_boto3_greengrassv2](https://pypi.org/project/mypy-boto3-greengrassv2/).

- [Literals for boto3 GreengrassV2 module](#literals-for-boto3-greengrassv2-module)
  - [CloudComponentState](#cloudcomponentstate)
  - [ComponentDependencyType](#componentdependencytype)
  - [ComponentVisibilityScope](#componentvisibilityscope)
  - [CoreDeviceStatus](#coredevicestatus)
  - [DeploymentComponentUpdatePolicyAction](#deploymentcomponentupdatepolicyaction)
  - [DeploymentFailureHandlingPolicy](#deploymentfailurehandlingpolicy)
  - [DeploymentHistoryFilter](#deploymenthistoryfilter)
  - [DeploymentStatus](#deploymentstatus)
  - [EffectiveDeploymentExecutionStatus](#effectivedeploymentexecutionstatus)
  - [InstalledComponentLifecycleState](#installedcomponentlifecyclestate)
  - [IoTJobAbortAction](#iotjobabortaction)
  - [IoTJobExecutionFailureType](#iotjobexecutionfailuretype)
  - [LambdaEventSourceType](#lambdaeventsourcetype)
  - [LambdaFilesystemPermission](#lambdafilesystempermission)
  - [LambdaInputPayloadEncodingType](#lambdainputpayloadencodingtype)
  - [LambdaIsolationMode](#lambdaisolationmode)
  - [ListComponentVersionsPaginatorName](#listcomponentversionspaginatorname)
  - [ListComponentsPaginatorName](#listcomponentspaginatorname)
  - [ListCoreDevicesPaginatorName](#listcoredevicespaginatorname)
  - [ListDeploymentsPaginatorName](#listdeploymentspaginatorname)
  - [ListEffectiveDeploymentsPaginatorName](#listeffectivedeploymentspaginatorname)
  - [ListInstalledComponentsPaginatorName](#listinstalledcomponentspaginatorname)
  - [RecipeOutputFormat](#recipeoutputformat)

## CloudComponentState

```python
from mypy_boto3_greengrassv2.literals import CloudComponentState
```

Values:

- `DEPLOYABLE`
- `DEPRECATED`
- `FAILED`
- `INITIATED`
- `REQUESTED`

## ComponentDependencyType

```python
from mypy_boto3_greengrassv2.literals import ComponentDependencyType
```

Values:

- `HARD`
- `SOFT`

## ComponentVisibilityScope

```python
from mypy_boto3_greengrassv2.literals import ComponentVisibilityScope
```

Values:

- `PRIVATE`
- `PUBLIC`

## CoreDeviceStatus

```python
from mypy_boto3_greengrassv2.literals import CoreDeviceStatus
```

Values:

- `HEALTHY`
- `UNHEALTHY`

## DeploymentComponentUpdatePolicyAction

```python
from mypy_boto3_greengrassv2.literals import DeploymentComponentUpdatePolicyAction
```

Values:

- `NOTIFY_COMPONENTS`
- `SKIP_NOTIFY_COMPONENTS`

## DeploymentFailureHandlingPolicy

```python
from mypy_boto3_greengrassv2.literals import DeploymentFailureHandlingPolicy
```

Values:

- `DO_NOTHING`
- `ROLLBACK`

## DeploymentHistoryFilter

```python
from mypy_boto3_greengrassv2.literals import DeploymentHistoryFilter
```

Values:

- `ALL`
- `LATEST_ONLY`

## DeploymentStatus

```python
from mypy_boto3_greengrassv2.literals import DeploymentStatus
```

Values:

- `ACTIVE`
- `CANCELED`
- `COMPLETED`
- `FAILED`
- `INACTIVE`

## EffectiveDeploymentExecutionStatus

```python
from mypy_boto3_greengrassv2.literals import EffectiveDeploymentExecutionStatus
```

Values:

- `CANCELED`
- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`
- `QUEUED`
- `REJECTED`
- `TIMED_OUT`

## InstalledComponentLifecycleState

```python
from mypy_boto3_greengrassv2.literals import InstalledComponentLifecycleState
```

Values:

- `BROKEN`
- `ERRORED`
- `FINISHED`
- `INSTALLED`
- `NEW`
- `RUNNING`
- `STARTING`
- `STOPPING`

## IoTJobAbortAction

```python
from mypy_boto3_greengrassv2.literals import IoTJobAbortAction
```

Values:

- `CANCEL`

## IoTJobExecutionFailureType

```python
from mypy_boto3_greengrassv2.literals import IoTJobExecutionFailureType
```

Values:

- `ALL`
- `FAILED`
- `REJECTED`
- `TIMED_OUT`

## LambdaEventSourceType

```python
from mypy_boto3_greengrassv2.literals import LambdaEventSourceType
```

Values:

- `IOT_CORE`
- `PUB_SUB`

## LambdaFilesystemPermission

```python
from mypy_boto3_greengrassv2.literals import LambdaFilesystemPermission
```

Values:

- `ro`
- `rw`

## LambdaInputPayloadEncodingType

```python
from mypy_boto3_greengrassv2.literals import LambdaInputPayloadEncodingType
```

Values:

- `binary`
- `json`

## LambdaIsolationMode

```python
from mypy_boto3_greengrassv2.literals import LambdaIsolationMode
```

Values:

- `GreengrassContainer`
- `NoContainer`

## ListComponentVersionsPaginatorName

```python
from mypy_boto3_greengrassv2.literals import ListComponentVersionsPaginatorName
```

Values:

- `list_component_versions`

## ListComponentsPaginatorName

```python
from mypy_boto3_greengrassv2.literals import ListComponentsPaginatorName
```

Values:

- `list_components`

## ListCoreDevicesPaginatorName

```python
from mypy_boto3_greengrassv2.literals import ListCoreDevicesPaginatorName
```

Values:

- `list_core_devices`

## ListDeploymentsPaginatorName

```python
from mypy_boto3_greengrassv2.literals import ListDeploymentsPaginatorName
```

Values:

- `list_deployments`

## ListEffectiveDeploymentsPaginatorName

```python
from mypy_boto3_greengrassv2.literals import ListEffectiveDeploymentsPaginatorName
```

Values:

- `list_effective_deployments`

## ListInstalledComponentsPaginatorName

```python
from mypy_boto3_greengrassv2.literals import ListInstalledComponentsPaginatorName
```

Values:

- `list_installed_components`

## RecipeOutputFormat

```python
from mypy_boto3_greengrassv2.literals import RecipeOutputFormat
```

Values:

- `JSON`
- `YAML`
