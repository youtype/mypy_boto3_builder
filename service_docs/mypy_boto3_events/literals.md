# Literals for boto3 EventBridge module

> [Index](../index.md) > [EventBridge](./index.md) > Literals

Auto-generated documentation for [EventBridge](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge)
type annotations stubs module [mypy_boto3_events](https://pypi.org/project/mypy-boto3-events/).

- [Literals for boto3 EventBridge module](#literals-for-boto3-eventbridge-module)
  - [ApiDestinationHttpMethod](#apidestinationhttpmethod)
  - [ApiDestinationState](#apidestinationstate)
  - [ArchiveState](#archivestate)
  - [AssignPublicIp](#assignpublicip)
  - [ConnectionAuthorizationType](#connectionauthorizationtype)
  - [ConnectionOAuthHttpMethod](#connectionoauthhttpmethod)
  - [ConnectionState](#connectionstate)
  - [EventSourceState](#eventsourcestate)
  - [LaunchType](#launchtype)
  - [ListRuleNamesByTargetPaginatorName](#listrulenamesbytargetpaginatorname)
  - [ListRulesPaginatorName](#listrulespaginatorname)
  - [ListTargetsByRulePaginatorName](#listtargetsbyrulepaginatorname)
  - [ReplayState](#replaystate)
  - [RuleState](#rulestate)

## ApiDestinationHttpMethod

```python
from mypy_boto3_events.literals import ApiDestinationHttpMethod
```

Values:

- `DELETE`
- `GET`
- `HEAD`
- `OPTIONS`
- `PATCH`
- `POST`
- `PUT`

## ApiDestinationState

```python
from mypy_boto3_events.literals import ApiDestinationState
```

Values:

- `ACTIVE`
- `INACTIVE`

## ArchiveState

```python
from mypy_boto3_events.literals import ArchiveState
```

Values:

- `CREATE_FAILED`
- `CREATING`
- `DISABLED`
- `ENABLED`
- `UPDATE_FAILED`
- `UPDATING`

## AssignPublicIp

```python
from mypy_boto3_events.literals import AssignPublicIp
```

Values:

- `DISABLED`
- `ENABLED`

## ConnectionAuthorizationType

```python
from mypy_boto3_events.literals import ConnectionAuthorizationType
```

Values:

- `API_KEY`
- `BASIC`
- `OAUTH_CLIENT_CREDENTIALS`

## ConnectionOAuthHttpMethod

```python
from mypy_boto3_events.literals import ConnectionOAuthHttpMethod
```

Values:

- `GET`
- `POST`
- `PUT`

## ConnectionState

```python
from mypy_boto3_events.literals import ConnectionState
```

Values:

- `AUTHORIZED`
- `AUTHORIZING`
- `CREATING`
- `DEAUTHORIZED`
- `DEAUTHORIZING`
- `DELETING`
- `UPDATING`

## EventSourceState

```python
from mypy_boto3_events.literals import EventSourceState
```

Values:

- `ACTIVE`
- `DELETED`
- `PENDING`

## LaunchType

```python
from mypy_boto3_events.literals import LaunchType
```

Values:

- `EC2`
- `FARGATE`

## ListRuleNamesByTargetPaginatorName

```python
from mypy_boto3_events.literals import ListRuleNamesByTargetPaginatorName
```

Values:

- `list_rule_names_by_target`

## ListRulesPaginatorName

```python
from mypy_boto3_events.literals import ListRulesPaginatorName
```

Values:

- `list_rules`

## ListTargetsByRulePaginatorName

```python
from mypy_boto3_events.literals import ListTargetsByRulePaginatorName
```

Values:

- `list_targets_by_rule`

## ReplayState

```python
from mypy_boto3_events.literals import ReplayState
```

Values:

- `CANCELLED`
- `CANCELLING`
- `COMPLETED`
- `FAILED`
- `RUNNING`
- `STARTING`

## RuleState

```python
from mypy_boto3_events.literals import RuleState
```

Values:

- `DISABLED`
- `ENABLED`
