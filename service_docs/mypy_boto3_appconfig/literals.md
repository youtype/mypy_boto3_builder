# Literals for boto3 AppConfig module

> [Index](../index.md) > [AppConfig](./index.md) > Literals

Auto-generated documentation for [AppConfig](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html#AppConfig)
type annotations stubs module [mypy_boto3_appconfig](https://pypi.org/project/mypy-boto3-appconfig/).

- [Literals for boto3 AppConfig module](#literals-for-boto3-appconfig-module)
  - [DeploymentEventType](#deploymenteventtype)
  - [DeploymentState](#deploymentstate)
  - [EnvironmentState](#environmentstate)
  - [GrowthType](#growthtype)
  - [ReplicateTo](#replicateto)
  - [TriggeredBy](#triggeredby)
  - [ValidatorType](#validatortype)

## DeploymentEventType

```python
from mypy_boto3_appconfig.literals import DeploymentEventType
```

Values:

- `BAKE_TIME_STARTED`
- `DEPLOYMENT_COMPLETED`
- `DEPLOYMENT_STARTED`
- `PERCENTAGE_UPDATED`
- `ROLLBACK_COMPLETED`
- `ROLLBACK_STARTED`

## DeploymentState

```python
from mypy_boto3_appconfig.literals import DeploymentState
```

Values:

- `BAKING`
- `COMPLETE`
- `DEPLOYING`
- `ROLLED_BACK`
- `ROLLING_BACK`
- `VALIDATING`

## EnvironmentState

```python
from mypy_boto3_appconfig.literals import EnvironmentState
```

Values:

- `DEPLOYING`
- `READY_FOR_DEPLOYMENT`
- `ROLLED_BACK`
- `ROLLING_BACK`

## GrowthType

```python
from mypy_boto3_appconfig.literals import GrowthType
```

Values:

- `EXPONENTIAL`
- `LINEAR`

## ReplicateTo

```python
from mypy_boto3_appconfig.literals import ReplicateTo
```

Values:

- `NONE`
- `SSM_DOCUMENT`

## TriggeredBy

```python
from mypy_boto3_appconfig.literals import TriggeredBy
```

Values:

- `APPCONFIG`
- `CLOUDWATCH_ALARM`
- `INTERNAL_ERROR`
- `USER`

## ValidatorType

```python
from mypy_boto3_appconfig.literals import ValidatorType
```

Values:

- `JSON_SCHEMA`
- `LAMBDA`
