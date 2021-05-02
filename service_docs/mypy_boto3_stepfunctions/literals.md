# Literals for boto3 SFN module

> [Index](../index.md) > [SFN](./index.md) > Literals

Auto-generated documentation for [SFN](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN)
type annotations stubs module [mypy_boto3_stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/).

- [Literals for boto3 SFN module](#literals-for-boto3-sfn-module)
  - [ExecutionStatus](#executionstatus)
  - [GetExecutionHistoryPaginatorName](#getexecutionhistorypaginatorname)
  - [HistoryEventType](#historyeventtype)
  - [ListActivitiesPaginatorName](#listactivitiespaginatorname)
  - [ListExecutionsPaginatorName](#listexecutionspaginatorname)
  - [ListStateMachinesPaginatorName](#liststatemachinespaginatorname)
  - [LogLevel](#loglevel)
  - [StateMachineStatus](#statemachinestatus)
  - [StateMachineType](#statemachinetype)
  - [SyncExecutionStatus](#syncexecutionstatus)

## ExecutionStatus

```python
from mypy_boto3_stepfunctions.literals import ExecutionStatus
```

Values:

- `ABORTED`
- `FAILED`
- `RUNNING`
- `SUCCEEDED`
- `TIMED_OUT`

## GetExecutionHistoryPaginatorName

```python
from mypy_boto3_stepfunctions.literals import GetExecutionHistoryPaginatorName
```

Values:

- `get_execution_history`

## HistoryEventType

```python
from mypy_boto3_stepfunctions.literals import HistoryEventType
```

Values:

- `ActivityFailed`
- `ActivityScheduled`
- `ActivityScheduleFailed`
- `ActivityStarted`
- `ActivitySucceeded`
- `ActivityTimedOut`
- `ChoiceStateEntered`
- `ChoiceStateExited`
- `ExecutionAborted`
- `ExecutionFailed`
- `ExecutionStarted`
- `ExecutionSucceeded`
- `ExecutionTimedOut`
- `FailStateEntered`
- `LambdaFunctionFailed`
- `LambdaFunctionScheduled`
- `LambdaFunctionScheduleFailed`
- `LambdaFunctionStarted`
- `LambdaFunctionStartFailed`
- `LambdaFunctionSucceeded`
- `LambdaFunctionTimedOut`
- `MapIterationAborted`
- `MapIterationFailed`
- `MapIterationStarted`
- `MapIterationSucceeded`
- `MapStateAborted`
- `MapStateEntered`
- `MapStateExited`
- `MapStateFailed`
- `MapStateStarted`
- `MapStateSucceeded`
- `ParallelStateAborted`
- `ParallelStateEntered`
- `ParallelStateExited`
- `ParallelStateFailed`
- `ParallelStateStarted`
- `ParallelStateSucceeded`
- `PassStateEntered`
- `PassStateExited`
- `SucceedStateEntered`
- `SucceedStateExited`
- `TaskFailed`
- `TaskScheduled`
- `TaskStarted`
- `TaskStartFailed`
- `TaskStateAborted`
- `TaskStateEntered`
- `TaskStateExited`
- `TaskSubmitFailed`
- `TaskSubmitted`
- `TaskSucceeded`
- `TaskTimedOut`
- `WaitStateAborted`
- `WaitStateEntered`
- `WaitStateExited`

## ListActivitiesPaginatorName

```python
from mypy_boto3_stepfunctions.literals import ListActivitiesPaginatorName
```

Values:

- `list_activities`

## ListExecutionsPaginatorName

```python
from mypy_boto3_stepfunctions.literals import ListExecutionsPaginatorName
```

Values:

- `list_executions`

## ListStateMachinesPaginatorName

```python
from mypy_boto3_stepfunctions.literals import ListStateMachinesPaginatorName
```

Values:

- `list_state_machines`

## LogLevel

```python
from mypy_boto3_stepfunctions.literals import LogLevel
```

Values:

- `ALL`
- `ERROR`
- `FATAL`
- `OFF`

## StateMachineStatus

```python
from mypy_boto3_stepfunctions.literals import StateMachineStatus
```

Values:

- `ACTIVE`
- `DELETING`

## StateMachineType

```python
from mypy_boto3_stepfunctions.literals import StateMachineType
```

Values:

- `EXPRESS`
- `STANDARD`

## SyncExecutionStatus

```python
from mypy_boto3_stepfunctions.literals import SyncExecutionStatus
```

Values:

- `FAILED`
- `SUCCEEDED`
- `TIMED_OUT`
