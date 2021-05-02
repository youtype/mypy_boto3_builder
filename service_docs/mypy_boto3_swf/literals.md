# Literals for boto3 SWF module

> [Index](../index.md) > [SWF](./index.md) > Literals

Auto-generated documentation for [SWF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF)
type annotations stubs module [mypy_boto3_swf](https://pypi.org/project/mypy-boto3-swf/).

- [Literals for boto3 SWF module](#literals-for-boto3-swf-module)
  - [ActivityTaskTimeoutType](#activitytasktimeouttype)
  - [CancelTimerFailedCause](#canceltimerfailedcause)
  - [CancelWorkflowExecutionFailedCause](#cancelworkflowexecutionfailedcause)
  - [ChildPolicy](#childpolicy)
  - [CloseStatus](#closestatus)
  - [CompleteWorkflowExecutionFailedCause](#completeworkflowexecutionfailedcause)
  - [ContinueAsNewWorkflowExecutionFailedCause](#continueasnewworkflowexecutionfailedcause)
  - [DecisionTaskTimeoutType](#decisiontasktimeouttype)
  - [DecisionType](#decisiontype)
  - [EventType](#eventtype)
  - [ExecutionStatus](#executionstatus)
  - [FailWorkflowExecutionFailedCause](#failworkflowexecutionfailedcause)
  - [GetWorkflowExecutionHistoryPaginatorName](#getworkflowexecutionhistorypaginatorname)
  - [LambdaFunctionTimeoutType](#lambdafunctiontimeouttype)
  - [ListActivityTypesPaginatorName](#listactivitytypespaginatorname)
  - [ListClosedWorkflowExecutionsPaginatorName](#listclosedworkflowexecutionspaginatorname)
  - [ListDomainsPaginatorName](#listdomainspaginatorname)
  - [ListOpenWorkflowExecutionsPaginatorName](#listopenworkflowexecutionspaginatorname)
  - [ListWorkflowTypesPaginatorName](#listworkflowtypespaginatorname)
  - [PollForDecisionTaskPaginatorName](#pollfordecisiontaskpaginatorname)
  - [RecordMarkerFailedCause](#recordmarkerfailedcause)
  - [RegistrationStatus](#registrationstatus)
  - [RequestCancelActivityTaskFailedCause](#requestcancelactivitytaskfailedcause)
  - [RequestCancelExternalWorkflowExecutionFailedCause](#requestcancelexternalworkflowexecutionfailedcause)
  - [ScheduleActivityTaskFailedCause](#scheduleactivitytaskfailedcause)
  - [ScheduleLambdaFunctionFailedCause](#schedulelambdafunctionfailedcause)
  - [SignalExternalWorkflowExecutionFailedCause](#signalexternalworkflowexecutionfailedcause)
  - [StartChildWorkflowExecutionFailedCause](#startchildworkflowexecutionfailedcause)
  - [StartLambdaFunctionFailedCause](#startlambdafunctionfailedcause)
  - [StartTimerFailedCause](#starttimerfailedcause)
  - [WorkflowExecutionCancelRequestedCause](#workflowexecutioncancelrequestedcause)
  - [WorkflowExecutionTerminatedCause](#workflowexecutionterminatedcause)
  - [WorkflowExecutionTimeoutType](#workflowexecutiontimeouttype)

## ActivityTaskTimeoutType

```python
from mypy_boto3_swf.literals import ActivityTaskTimeoutType
```

Values:

- `HEARTBEAT`
- `SCHEDULE_TO_CLOSE`
- `SCHEDULE_TO_START`
- `START_TO_CLOSE`

## CancelTimerFailedCause

```python
from mypy_boto3_swf.literals import CancelTimerFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`
- `TIMER_ID_UNKNOWN`

## CancelWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import CancelWorkflowExecutionFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`
- `UNHANDLED_DECISION`

## ChildPolicy

```python
from mypy_boto3_swf.literals import ChildPolicy
```

Values:

- `ABANDON`
- `REQUEST_CANCEL`
- `TERMINATE`

## CloseStatus

```python
from mypy_boto3_swf.literals import CloseStatus
```

Values:

- `CANCELED`
- `COMPLETED`
- `CONTINUED_AS_NEW`
- `FAILED`
- `TERMINATED`
- `TIMED_OUT`

## CompleteWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import CompleteWorkflowExecutionFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`
- `UNHANDLED_DECISION`

## ContinueAsNewWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import ContinueAsNewWorkflowExecutionFailedCause
```

Values:

- `CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED`
- `DEFAULT_CHILD_POLICY_UNDEFINED`
- `DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED`
- `DEFAULT_TASK_LIST_UNDEFINED`
- `DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED`
- `OPERATION_NOT_PERMITTED`
- `UNHANDLED_DECISION`
- `WORKFLOW_TYPE_DEPRECATED`
- `WORKFLOW_TYPE_DOES_NOT_EXIST`

## DecisionTaskTimeoutType

```python
from mypy_boto3_swf.literals import DecisionTaskTimeoutType
```

Values:

- `START_TO_CLOSE`

## DecisionType

```python
from mypy_boto3_swf.literals import DecisionType
```

Values:

- `CancelTimer`
- `CancelWorkflowExecution`
- `CompleteWorkflowExecution`
- `ContinueAsNewWorkflowExecution`
- `FailWorkflowExecution`
- `RecordMarker`
- `RequestCancelActivityTask`
- `RequestCancelExternalWorkflowExecution`
- `ScheduleActivityTask`
- `ScheduleLambdaFunction`
- `SignalExternalWorkflowExecution`
- `StartChildWorkflowExecution`
- `StartTimer`

## EventType

```python
from mypy_boto3_swf.literals import EventType
```

Values:

- `ActivityTaskCanceled`
- `ActivityTaskCancelRequested`
- `ActivityTaskCompleted`
- `ActivityTaskFailed`
- `ActivityTaskScheduled`
- `ActivityTaskStarted`
- `ActivityTaskTimedOut`
- `CancelTimerFailed`
- `CancelWorkflowExecutionFailed`
- `ChildWorkflowExecutionCanceled`
- `ChildWorkflowExecutionCompleted`
- `ChildWorkflowExecutionFailed`
- `ChildWorkflowExecutionStarted`
- `ChildWorkflowExecutionTerminated`
- `ChildWorkflowExecutionTimedOut`
- `CompleteWorkflowExecutionFailed`
- `ContinueAsNewWorkflowExecutionFailed`
- `DecisionTaskCompleted`
- `DecisionTaskScheduled`
- `DecisionTaskStarted`
- `DecisionTaskTimedOut`
- `ExternalWorkflowExecutionCancelRequested`
- `ExternalWorkflowExecutionSignaled`
- `FailWorkflowExecutionFailed`
- `LambdaFunctionCompleted`
- `LambdaFunctionFailed`
- `LambdaFunctionScheduled`
- `LambdaFunctionStarted`
- `LambdaFunctionTimedOut`
- `MarkerRecorded`
- `RecordMarkerFailed`
- `RequestCancelActivityTaskFailed`
- `RequestCancelExternalWorkflowExecutionFailed`
- `RequestCancelExternalWorkflowExecutionInitiated`
- `ScheduleActivityTaskFailed`
- `ScheduleLambdaFunctionFailed`
- `SignalExternalWorkflowExecutionFailed`
- `SignalExternalWorkflowExecutionInitiated`
- `StartChildWorkflowExecutionFailed`
- `StartChildWorkflowExecutionInitiated`
- `StartLambdaFunctionFailed`
- `StartTimerFailed`
- `TimerCanceled`
- `TimerFired`
- `TimerStarted`
- `WorkflowExecutionCanceled`
- `WorkflowExecutionCancelRequested`
- `WorkflowExecutionCompleted`
- `WorkflowExecutionContinuedAsNew`
- `WorkflowExecutionFailed`
- `WorkflowExecutionSignaled`
- `WorkflowExecutionStarted`
- `WorkflowExecutionTerminated`
- `WorkflowExecutionTimedOut`

## ExecutionStatus

```python
from mypy_boto3_swf.literals import ExecutionStatus
```

Values:

- `CLOSED`
- `OPEN`

## FailWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import FailWorkflowExecutionFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`
- `UNHANDLED_DECISION`

## GetWorkflowExecutionHistoryPaginatorName

```python
from mypy_boto3_swf.literals import GetWorkflowExecutionHistoryPaginatorName
```

Values:

- `get_workflow_execution_history`

## LambdaFunctionTimeoutType

```python
from mypy_boto3_swf.literals import LambdaFunctionTimeoutType
```

Values:

- `START_TO_CLOSE`

## ListActivityTypesPaginatorName

```python
from mypy_boto3_swf.literals import ListActivityTypesPaginatorName
```

Values:

- `list_activity_types`

## ListClosedWorkflowExecutionsPaginatorName

```python
from mypy_boto3_swf.literals import ListClosedWorkflowExecutionsPaginatorName
```

Values:

- `list_closed_workflow_executions`

## ListDomainsPaginatorName

```python
from mypy_boto3_swf.literals import ListDomainsPaginatorName
```

Values:

- `list_domains`

## ListOpenWorkflowExecutionsPaginatorName

```python
from mypy_boto3_swf.literals import ListOpenWorkflowExecutionsPaginatorName
```

Values:

- `list_open_workflow_executions`

## ListWorkflowTypesPaginatorName

```python
from mypy_boto3_swf.literals import ListWorkflowTypesPaginatorName
```

Values:

- `list_workflow_types`

## PollForDecisionTaskPaginatorName

```python
from mypy_boto3_swf.literals import PollForDecisionTaskPaginatorName
```

Values:

- `poll_for_decision_task`

## RecordMarkerFailedCause

```python
from mypy_boto3_swf.literals import RecordMarkerFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`

## RegistrationStatus

```python
from mypy_boto3_swf.literals import RegistrationStatus
```

Values:

- `DEPRECATED`
- `REGISTERED`

## RequestCancelActivityTaskFailedCause

```python
from mypy_boto3_swf.literals import RequestCancelActivityTaskFailedCause
```

Values:

- `ACTIVITY_ID_UNKNOWN`
- `OPERATION_NOT_PERMITTED`

## RequestCancelExternalWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import RequestCancelExternalWorkflowExecutionFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`
- `REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED`
- `UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION`

## ScheduleActivityTaskFailedCause

```python
from mypy_boto3_swf.literals import ScheduleActivityTaskFailedCause
```

Values:

- `ACTIVITY_CREATION_RATE_EXCEEDED`
- `ACTIVITY_ID_ALREADY_IN_USE`
- `ACTIVITY_TYPE_DEPRECATED`
- `ACTIVITY_TYPE_DOES_NOT_EXIST`
- `DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED`
- `DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED`
- `DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED`
- `DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED`
- `DEFAULT_TASK_LIST_UNDEFINED`
- `OPEN_ACTIVITIES_LIMIT_EXCEEDED`
- `OPERATION_NOT_PERMITTED`

## ScheduleLambdaFunctionFailedCause

```python
from mypy_boto3_swf.literals import ScheduleLambdaFunctionFailedCause
```

Values:

- `ID_ALREADY_IN_USE`
- `LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED`
- `LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION`
- `OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED`

## SignalExternalWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import SignalExternalWorkflowExecutionFailedCause
```

Values:

- `OPERATION_NOT_PERMITTED`
- `SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED`
- `UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION`

## StartChildWorkflowExecutionFailedCause

```python
from mypy_boto3_swf.literals import StartChildWorkflowExecutionFailedCause
```

Values:

- `CHILD_CREATION_RATE_EXCEEDED`
- `DEFAULT_CHILD_POLICY_UNDEFINED`
- `DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED`
- `DEFAULT_TASK_LIST_UNDEFINED`
- `DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED`
- `OPEN_CHILDREN_LIMIT_EXCEEDED`
- `OPEN_WORKFLOWS_LIMIT_EXCEEDED`
- `OPERATION_NOT_PERMITTED`
- `WORKFLOW_ALREADY_RUNNING`
- `WORKFLOW_TYPE_DEPRECATED`
- `WORKFLOW_TYPE_DOES_NOT_EXIST`

## StartLambdaFunctionFailedCause

```python
from mypy_boto3_swf.literals import StartLambdaFunctionFailedCause
```

Values:

- `ASSUME_ROLE_FAILED`

## StartTimerFailedCause

```python
from mypy_boto3_swf.literals import StartTimerFailedCause
```

Values:

- `OPEN_TIMERS_LIMIT_EXCEEDED`
- `OPERATION_NOT_PERMITTED`
- `TIMER_CREATION_RATE_EXCEEDED`
- `TIMER_ID_ALREADY_IN_USE`

## WorkflowExecutionCancelRequestedCause

```python
from mypy_boto3_swf.literals import WorkflowExecutionCancelRequestedCause
```

Values:

- `CHILD_POLICY_APPLIED`

## WorkflowExecutionTerminatedCause

```python
from mypy_boto3_swf.literals import WorkflowExecutionTerminatedCause
```

Values:

- `CHILD_POLICY_APPLIED`
- `EVENT_LIMIT_EXCEEDED`
- `OPERATOR_INITIATED`

## WorkflowExecutionTimeoutType

```python
from mypy_boto3_swf.literals import WorkflowExecutionTimeoutType
```

Values:

- `START_TO_CLOSE`
