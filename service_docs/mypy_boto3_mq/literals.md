# Literals for boto3 MQ module

> [Index](../index.md) > [MQ](./index.md) > Literals

Auto-generated documentation for [MQ](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ)
type annotations stubs module [mypy_boto3_mq](https://pypi.org/project/mypy-boto3-mq/).

- [Literals for boto3 MQ module](#literals-for-boto3-mq-module)
  - [AuthenticationStrategy](#authenticationstrategy)
  - [BrokerState](#brokerstate)
  - [BrokerStorageType](#brokerstoragetype)
  - [ChangeType](#changetype)
  - [DayOfWeek](#dayofweek)
  - [DeploymentMode](#deploymentmode)
  - [EngineType](#enginetype)
  - [ListBrokersPaginatorName](#listbrokerspaginatorname)
  - [SanitizationWarningReason](#sanitizationwarningreason)

## AuthenticationStrategy

```python
from mypy_boto3_mq.literals import AuthenticationStrategy
```

Values:

- `LDAP`
- `SIMPLE`

## BrokerState

```python
from mypy_boto3_mq.literals import BrokerState
```

Values:

- `CREATION_FAILED`
- `CREATION_IN_PROGRESS`
- `DELETION_IN_PROGRESS`
- `REBOOT_IN_PROGRESS`
- `RUNNING`

## BrokerStorageType

```python
from mypy_boto3_mq.literals import BrokerStorageType
```

Values:

- `EBS`
- `EFS`

## ChangeType

```python
from mypy_boto3_mq.literals import ChangeType
```

Values:

- `CREATE`
- `DELETE`
- `UPDATE`

## DayOfWeek

```python
from mypy_boto3_mq.literals import DayOfWeek
```

Values:

- `FRIDAY`
- `MONDAY`
- `SATURDAY`
- `SUNDAY`
- `THURSDAY`
- `TUESDAY`
- `WEDNESDAY`

## DeploymentMode

```python
from mypy_boto3_mq.literals import DeploymentMode
```

Values:

- `ACTIVE_STANDBY_MULTI_AZ`
- `CLUSTER_MULTI_AZ`
- `SINGLE_INSTANCE`

## EngineType

```python
from mypy_boto3_mq.literals import EngineType
```

Values:

- `ACTIVEMQ`
- `RABBITMQ`

## ListBrokersPaginatorName

```python
from mypy_boto3_mq.literals import ListBrokersPaginatorName
```

Values:

- `list_brokers`

## SanitizationWarningReason

```python
from mypy_boto3_mq.literals import SanitizationWarningReason
```

Values:

- `DISALLOWED_ATTRIBUTE_REMOVED`
- `DISALLOWED_ELEMENT_REMOVED`
- `INVALID_ATTRIBUTE_VALUE_REMOVED`
