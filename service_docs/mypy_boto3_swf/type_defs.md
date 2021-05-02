# Structures for boto3 SWF module

> [Index](../index.md) > [SWF](./index.md) > Structures

Auto-generated documentation for [SWF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF)
type annotations stubs module [mypy_boto3_swf](https://pypi.org/project/mypy-boto3-swf/).

- [Structures for boto3 SWF module](#structures-for-boto3-swf-module)
  - [ActivityTaskCancelRequestedEventAttributesTypeDef](#activitytaskcancelrequestedeventattributestypedef)
  - [ActivityTaskCanceledEventAttributesTypeDef](#activitytaskcanceledeventattributestypedef)
  - [ActivityTaskCompletedEventAttributesTypeDef](#activitytaskcompletedeventattributestypedef)
  - [ActivityTaskFailedEventAttributesTypeDef](#activitytaskfailedeventattributestypedef)
  - [ActivityTaskScheduledEventAttributesTypeDef](#activitytaskscheduledeventattributestypedef)
  - [ActivityTaskStartedEventAttributesTypeDef](#activitytaskstartedeventattributestypedef)
  - [ActivityTaskStatusTypeDef](#activitytaskstatustypedef)
  - [ActivityTaskTimedOutEventAttributesTypeDef](#activitytasktimedouteventattributestypedef)
  - [ActivityTaskTypeDef](#activitytasktypedef)
  - [ActivityTypeConfigurationTypeDef](#activitytypeconfigurationtypedef)
  - [ActivityTypeDetailTypeDef](#activitytypedetailtypedef)
  - [ActivityTypeInfoTypeDef](#activitytypeinfotypedef)
  - [ActivityTypeInfosTypeDef](#activitytypeinfostypedef)
  - [ActivityTypeTypeDef](#activitytypetypedef)
  - [CancelTimerDecisionAttributesTypeDef](#canceltimerdecisionattributestypedef)
  - [CancelTimerFailedEventAttributesTypeDef](#canceltimerfailedeventattributestypedef)
  - [CancelWorkflowExecutionDecisionAttributesTypeDef](#cancelworkflowexecutiondecisionattributestypedef)
  - [CancelWorkflowExecutionFailedEventAttributesTypeDef](#cancelworkflowexecutionfailedeventattributestypedef)
  - [ChildWorkflowExecutionCanceledEventAttributesTypeDef](#childworkflowexecutioncanceledeventattributestypedef)
  - [ChildWorkflowExecutionCompletedEventAttributesTypeDef](#childworkflowexecutioncompletedeventattributestypedef)
  - [ChildWorkflowExecutionFailedEventAttributesTypeDef](#childworkflowexecutionfailedeventattributestypedef)
  - [ChildWorkflowExecutionStartedEventAttributesTypeDef](#childworkflowexecutionstartedeventattributestypedef)
  - [ChildWorkflowExecutionTerminatedEventAttributesTypeDef](#childworkflowexecutionterminatedeventattributestypedef)
  - [ChildWorkflowExecutionTimedOutEventAttributesTypeDef](#childworkflowexecutiontimedouteventattributestypedef)
  - [CloseStatusFilterTypeDef](#closestatusfiltertypedef)
  - [CompleteWorkflowExecutionDecisionAttributesTypeDef](#completeworkflowexecutiondecisionattributestypedef)
  - [CompleteWorkflowExecutionFailedEventAttributesTypeDef](#completeworkflowexecutionfailedeventattributestypedef)
  - [ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef](#continueasnewworkflowexecutiondecisionattributestypedef)
  - [ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef](#continueasnewworkflowexecutionfailedeventattributestypedef)
  - [DecisionTaskCompletedEventAttributesTypeDef](#decisiontaskcompletedeventattributestypedef)
  - [DecisionTaskScheduledEventAttributesTypeDef](#decisiontaskscheduledeventattributestypedef)
  - [DecisionTaskStartedEventAttributesTypeDef](#decisiontaskstartedeventattributestypedef)
  - [DecisionTaskTimedOutEventAttributesTypeDef](#decisiontasktimedouteventattributestypedef)
  - [DecisionTaskTypeDef](#decisiontasktypedef)
  - [DecisionTypeDef](#decisiontypedef)
  - [DomainConfigurationTypeDef](#domainconfigurationtypedef)
  - [DomainDetailTypeDef](#domaindetailtypedef)
  - [DomainInfoTypeDef](#domaininfotypedef)
  - [DomainInfosTypeDef](#domaininfostypedef)
  - [ExecutionTimeFilterTypeDef](#executiontimefiltertypedef)
  - [ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef](#externalworkflowexecutioncancelrequestedeventattributestypedef)
  - [ExternalWorkflowExecutionSignaledEventAttributesTypeDef](#externalworkflowexecutionsignaledeventattributestypedef)
  - [FailWorkflowExecutionDecisionAttributesTypeDef](#failworkflowexecutiondecisionattributestypedef)
  - [FailWorkflowExecutionFailedEventAttributesTypeDef](#failworkflowexecutionfailedeventattributestypedef)
  - [HistoryEventTypeDef](#historyeventtypedef)
  - [HistoryTypeDef](#historytypedef)
  - [LambdaFunctionCompletedEventAttributesTypeDef](#lambdafunctioncompletedeventattributestypedef)
  - [LambdaFunctionFailedEventAttributesTypeDef](#lambdafunctionfailedeventattributestypedef)
  - [LambdaFunctionScheduledEventAttributesTypeDef](#lambdafunctionscheduledeventattributestypedef)
  - [LambdaFunctionStartedEventAttributesTypeDef](#lambdafunctionstartedeventattributestypedef)
  - [LambdaFunctionTimedOutEventAttributesTypeDef](#lambdafunctiontimedouteventattributestypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [MarkerRecordedEventAttributesTypeDef](#markerrecordedeventattributestypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PendingTaskCountTypeDef](#pendingtaskcounttypedef)
  - [RecordMarkerDecisionAttributesTypeDef](#recordmarkerdecisionattributestypedef)
  - [RecordMarkerFailedEventAttributesTypeDef](#recordmarkerfailedeventattributestypedef)
  - [RequestCancelActivityTaskDecisionAttributesTypeDef](#requestcancelactivitytaskdecisionattributestypedef)
  - [RequestCancelActivityTaskFailedEventAttributesTypeDef](#requestcancelactivitytaskfailedeventattributestypedef)
  - [RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef](#requestcancelexternalworkflowexecutiondecisionattributestypedef)
  - [RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef](#requestcancelexternalworkflowexecutionfailedeventattributestypedef)
  - [RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef](#requestcancelexternalworkflowexecutioninitiatedeventattributestypedef)
  - [ResourceTagTypeDef](#resourcetagtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RunTypeDef](#runtypedef)
  - [ScheduleActivityTaskDecisionAttributesTypeDef](#scheduleactivitytaskdecisionattributestypedef)
  - [ScheduleActivityTaskFailedEventAttributesTypeDef](#scheduleactivitytaskfailedeventattributestypedef)
  - [ScheduleLambdaFunctionDecisionAttributesTypeDef](#schedulelambdafunctiondecisionattributestypedef)
  - [ScheduleLambdaFunctionFailedEventAttributesTypeDef](#schedulelambdafunctionfailedeventattributestypedef)
  - [SignalExternalWorkflowExecutionDecisionAttributesTypeDef](#signalexternalworkflowexecutiondecisionattributestypedef)
  - [SignalExternalWorkflowExecutionFailedEventAttributesTypeDef](#signalexternalworkflowexecutionfailedeventattributestypedef)
  - [SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef](#signalexternalworkflowexecutioninitiatedeventattributestypedef)
  - [StartChildWorkflowExecutionDecisionAttributesTypeDef](#startchildworkflowexecutiondecisionattributestypedef)
  - [StartChildWorkflowExecutionFailedEventAttributesTypeDef](#startchildworkflowexecutionfailedeventattributestypedef)
  - [StartChildWorkflowExecutionInitiatedEventAttributesTypeDef](#startchildworkflowexecutioninitiatedeventattributestypedef)
  - [StartLambdaFunctionFailedEventAttributesTypeDef](#startlambdafunctionfailedeventattributestypedef)
  - [StartTimerDecisionAttributesTypeDef](#starttimerdecisionattributestypedef)
  - [StartTimerFailedEventAttributesTypeDef](#starttimerfailedeventattributestypedef)
  - [TagFilterTypeDef](#tagfiltertypedef)
  - [TaskListTypeDef](#tasklisttypedef)
  - [TimerCanceledEventAttributesTypeDef](#timercanceledeventattributestypedef)
  - [TimerFiredEventAttributesTypeDef](#timerfiredeventattributestypedef)
  - [TimerStartedEventAttributesTypeDef](#timerstartedeventattributestypedef)
  - [WorkflowExecutionCancelRequestedEventAttributesTypeDef](#workflowexecutioncancelrequestedeventattributestypedef)
  - [WorkflowExecutionCanceledEventAttributesTypeDef](#workflowexecutioncanceledeventattributestypedef)
  - [WorkflowExecutionCompletedEventAttributesTypeDef](#workflowexecutioncompletedeventattributestypedef)
  - [WorkflowExecutionConfigurationTypeDef](#workflowexecutionconfigurationtypedef)
  - [WorkflowExecutionContinuedAsNewEventAttributesTypeDef](#workflowexecutioncontinuedasneweventattributestypedef)
  - [WorkflowExecutionCountTypeDef](#workflowexecutioncounttypedef)
  - [WorkflowExecutionDetailTypeDef](#workflowexecutiondetailtypedef)
  - [WorkflowExecutionFailedEventAttributesTypeDef](#workflowexecutionfailedeventattributestypedef)
  - [WorkflowExecutionFilterTypeDef](#workflowexecutionfiltertypedef)
  - [WorkflowExecutionInfoTypeDef](#workflowexecutioninfotypedef)
  - [WorkflowExecutionInfosTypeDef](#workflowexecutioninfostypedef)
  - [WorkflowExecutionOpenCountsTypeDef](#workflowexecutionopencountstypedef)
  - [WorkflowExecutionSignaledEventAttributesTypeDef](#workflowexecutionsignaledeventattributestypedef)
  - [WorkflowExecutionStartedEventAttributesTypeDef](#workflowexecutionstartedeventattributestypedef)
  - [WorkflowExecutionTerminatedEventAttributesTypeDef](#workflowexecutionterminatedeventattributestypedef)
  - [WorkflowExecutionTimedOutEventAttributesTypeDef](#workflowexecutiontimedouteventattributestypedef)
  - [WorkflowExecutionTypeDef](#workflowexecutiontypedef)
  - [WorkflowTypeConfigurationTypeDef](#workflowtypeconfigurationtypedef)
  - [WorkflowTypeDetailTypeDef](#workflowtypedetailtypedef)
  - [WorkflowTypeFilterTypeDef](#workflowtypefiltertypedef)
  - [WorkflowTypeInfoTypeDef](#workflowtypeinfotypedef)
  - [WorkflowTypeInfosTypeDef](#workflowtypeinfostypedef)
  - [WorkflowTypeTypeDef](#workflowtypetypedef)

## ActivityTaskCancelRequestedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskCancelRequestedEventAttributesTypeDef
```


Required fields:
- `decisionTaskCompletedEventId`: `int`
- `activityId`: `str`




## ActivityTaskCanceledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskCanceledEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `details`: `str`
- `latestCancelRequestedEventId`: `int`


## ActivityTaskCompletedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskCompletedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `result`: `str`


## ActivityTaskFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskFailedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `reason`: `str`
- `details`: `str`


## ActivityTaskScheduledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskScheduledEventAttributesTypeDef
```


Required fields:
- `activityType`: `"ActivityTypeTypeDef"`
- `activityId`: `str`
- `taskList`: `"TaskListTypeDef"`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `input`: `str`
- `control`: `str`
- `scheduleToStartTimeout`: `str`
- `scheduleToCloseTimeout`: `str`
- `startToCloseTimeout`: `str`
- `taskPriority`: `str`
- `heartbeatTimeout`: `str`


## ActivityTaskStartedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskStartedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`



Optional fields:
- `identity`: `str`


## ActivityTaskStatusTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskStatusTypeDef
```


Required fields:
- `cancelRequested`: `bool`




## ActivityTaskTimedOutEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskTimedOutEventAttributesTypeDef
```


Required fields:
- `timeoutType`: `ActivityTaskTimeoutType`
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `details`: `str`


## ActivityTaskTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTaskTypeDef
```


Required fields:
- `taskToken`: `str`
- `activityId`: `str`
- `startedEventId`: `int`
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `activityType`: `"ActivityTypeTypeDef"`



Optional fields:
- `input`: `str`


## ActivityTypeConfigurationTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTypeConfigurationTypeDef
```




Optional fields:
- `defaultTaskStartToCloseTimeout`: `str`
- `defaultTaskHeartbeatTimeout`: `str`
- `defaultTaskList`: `"TaskListTypeDef"`
- `defaultTaskPriority`: `str`
- `defaultTaskScheduleToStartTimeout`: `str`
- `defaultTaskScheduleToCloseTimeout`: `str`


## ActivityTypeDetailTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTypeDetailTypeDef
```


Required fields:
- `typeInfo`: `"ActivityTypeInfoTypeDef"`
- `configuration`: `"ActivityTypeConfigurationTypeDef"`




## ActivityTypeInfoTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTypeInfoTypeDef
```


Required fields:
- `activityType`: `"ActivityTypeTypeDef"`
- `status`: `RegistrationStatus`
- `creationDate`: `datetime`



Optional fields:
- `description`: `str`
- `deprecationDate`: `datetime`


## ActivityTypeInfosTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTypeInfosTypeDef
```


Required fields:
- `typeInfos`: `List["ActivityTypeInfoTypeDef"]`



Optional fields:
- `nextPageToken`: `str`


## ActivityTypeTypeDef

```python
from mypy_boto3_swf.type_defs import ActivityTypeTypeDef
```


Required fields:
- `name`: `str`
- `version`: `str`




## CancelTimerDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import CancelTimerDecisionAttributesTypeDef
```


Required fields:
- `timerId`: `str`




## CancelTimerFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import CancelTimerFailedEventAttributesTypeDef
```


Required fields:
- `timerId`: `str`
- `cause`: `CancelTimerFailedCause`
- `decisionTaskCompletedEventId`: `int`




## CancelWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import CancelWorkflowExecutionDecisionAttributesTypeDef
```




Optional fields:
- `details`: `str`


## CancelWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import CancelWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `cause`: `CancelWorkflowExecutionFailedCause`
- `decisionTaskCompletedEventId`: `int`




## ChildWorkflowExecutionCanceledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ChildWorkflowExecutionCanceledEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `initiatedEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `details`: `str`


## ChildWorkflowExecutionCompletedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ChildWorkflowExecutionCompletedEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `initiatedEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `result`: `str`


## ChildWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ChildWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `initiatedEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `reason`: `str`
- `details`: `str`


## ChildWorkflowExecutionStartedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ChildWorkflowExecutionStartedEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `initiatedEventId`: `int`




## ChildWorkflowExecutionTerminatedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ChildWorkflowExecutionTerminatedEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `initiatedEventId`: `int`
- `startedEventId`: `int`




## ChildWorkflowExecutionTimedOutEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ChildWorkflowExecutionTimedOutEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `timeoutType`: `Literal['START_TO_CLOSE']`
- `initiatedEventId`: `int`
- `startedEventId`: `int`




## CloseStatusFilterTypeDef

```python
from mypy_boto3_swf.type_defs import CloseStatusFilterTypeDef
```


Required fields:
- `status`: `CloseStatus`




## CompleteWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import CompleteWorkflowExecutionDecisionAttributesTypeDef
```




Optional fields:
- `result`: `str`


## CompleteWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import CompleteWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `cause`: `CompleteWorkflowExecutionFailedCause`
- `decisionTaskCompletedEventId`: `int`




## ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef
```




Optional fields:
- `input`: `str`
- `executionStartToCloseTimeout`: `str`
- `taskList`: `"TaskListTypeDef"`
- `taskPriority`: `str`
- `taskStartToCloseTimeout`: `str`
- `childPolicy`: `ChildPolicy`
- `tagList`: `List[str]`
- `workflowTypeVersion`: `str`
- `lambdaRole`: `str`


## ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `cause`: `ContinueAsNewWorkflowExecutionFailedCause`
- `decisionTaskCompletedEventId`: `int`




## DecisionTaskCompletedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import DecisionTaskCompletedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `executionContext`: `str`


## DecisionTaskScheduledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import DecisionTaskScheduledEventAttributesTypeDef
```


Required fields:
- `taskList`: `"TaskListTypeDef"`



Optional fields:
- `taskPriority`: `str`
- `startToCloseTimeout`: `str`


## DecisionTaskStartedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import DecisionTaskStartedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`



Optional fields:
- `identity`: `str`


## DecisionTaskTimedOutEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import DecisionTaskTimedOutEventAttributesTypeDef
```


Required fields:
- `timeoutType`: `Literal['START_TO_CLOSE']`
- `scheduledEventId`: `int`
- `startedEventId`: `int`




## DecisionTaskTypeDef

```python
from mypy_boto3_swf.type_defs import DecisionTaskTypeDef
```


Required fields:
- `taskToken`: `str`
- `startedEventId`: `int`
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `events`: `List["HistoryEventTypeDef"]`



Optional fields:
- `nextPageToken`: `str`
- `previousStartedEventId`: `int`


## DecisionTypeDef

```python
from mypy_boto3_swf.type_defs import DecisionTypeDef
```


Required fields:
- `decisionType`: `DecisionType`



Optional fields:
- `scheduleActivityTaskDecisionAttributes`: `"ScheduleActivityTaskDecisionAttributesTypeDef"`
- `requestCancelActivityTaskDecisionAttributes`: `"RequestCancelActivityTaskDecisionAttributesTypeDef"`
- `completeWorkflowExecutionDecisionAttributes`: `"CompleteWorkflowExecutionDecisionAttributesTypeDef"`
- `failWorkflowExecutionDecisionAttributes`: `"FailWorkflowExecutionDecisionAttributesTypeDef"`
- `cancelWorkflowExecutionDecisionAttributes`: `"CancelWorkflowExecutionDecisionAttributesTypeDef"`
- `continueAsNewWorkflowExecutionDecisionAttributes`: `"ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef"`
- `recordMarkerDecisionAttributes`: `"RecordMarkerDecisionAttributesTypeDef"`
- `startTimerDecisionAttributes`: `"StartTimerDecisionAttributesTypeDef"`
- `cancelTimerDecisionAttributes`: `"CancelTimerDecisionAttributesTypeDef"`
- `signalExternalWorkflowExecutionDecisionAttributes`: `"SignalExternalWorkflowExecutionDecisionAttributesTypeDef"`
- `requestCancelExternalWorkflowExecutionDecisionAttributes`: `"RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef"`
- `startChildWorkflowExecutionDecisionAttributes`: `"StartChildWorkflowExecutionDecisionAttributesTypeDef"`
- `scheduleLambdaFunctionDecisionAttributes`: `"ScheduleLambdaFunctionDecisionAttributesTypeDef"`


## DomainConfigurationTypeDef

```python
from mypy_boto3_swf.type_defs import DomainConfigurationTypeDef
```


Required fields:
- `workflowExecutionRetentionPeriodInDays`: `str`




## DomainDetailTypeDef

```python
from mypy_boto3_swf.type_defs import DomainDetailTypeDef
```


Required fields:
- `domainInfo`: `"DomainInfoTypeDef"`
- `configuration`: `"DomainConfigurationTypeDef"`




## DomainInfoTypeDef

```python
from mypy_boto3_swf.type_defs import DomainInfoTypeDef
```


Required fields:
- `name`: `str`
- `status`: `RegistrationStatus`



Optional fields:
- `description`: `str`
- `arn`: `str`


## DomainInfosTypeDef

```python
from mypy_boto3_swf.type_defs import DomainInfosTypeDef
```


Required fields:
- `domainInfos`: `List["DomainInfoTypeDef"]`



Optional fields:
- `nextPageToken`: `str`


## ExecutionTimeFilterTypeDef

```python
from mypy_boto3_swf.type_defs import ExecutionTimeFilterTypeDef
```


Required fields:
- `oldestDate`: `datetime`



Optional fields:
- `latestDate`: `datetime`


## ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `initiatedEventId`: `int`




## ExternalWorkflowExecutionSignaledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ExternalWorkflowExecutionSignaledEventAttributesTypeDef
```


Required fields:
- `workflowExecution`: `"WorkflowExecutionTypeDef"`
- `initiatedEventId`: `int`




## FailWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import FailWorkflowExecutionDecisionAttributesTypeDef
```




Optional fields:
- `reason`: `str`
- `details`: `str`


## FailWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import FailWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `cause`: `FailWorkflowExecutionFailedCause`
- `decisionTaskCompletedEventId`: `int`




## HistoryEventTypeDef

```python
from mypy_boto3_swf.type_defs import HistoryEventTypeDef
```


Required fields:
- `eventTimestamp`: `datetime`
- `eventType`: `EventType`
- `eventId`: `int`



Optional fields:
- `workflowExecutionStartedEventAttributes`: `"WorkflowExecutionStartedEventAttributesTypeDef"`
- `workflowExecutionCompletedEventAttributes`: `"WorkflowExecutionCompletedEventAttributesTypeDef"`
- `completeWorkflowExecutionFailedEventAttributes`: `"CompleteWorkflowExecutionFailedEventAttributesTypeDef"`
- `workflowExecutionFailedEventAttributes`: `"WorkflowExecutionFailedEventAttributesTypeDef"`
- `failWorkflowExecutionFailedEventAttributes`: `"FailWorkflowExecutionFailedEventAttributesTypeDef"`
- `workflowExecutionTimedOutEventAttributes`: `"WorkflowExecutionTimedOutEventAttributesTypeDef"`
- `workflowExecutionCanceledEventAttributes`: `"WorkflowExecutionCanceledEventAttributesTypeDef"`
- `cancelWorkflowExecutionFailedEventAttributes`: `"CancelWorkflowExecutionFailedEventAttributesTypeDef"`
- `workflowExecutionContinuedAsNewEventAttributes`: `"WorkflowExecutionContinuedAsNewEventAttributesTypeDef"`
- `continueAsNewWorkflowExecutionFailedEventAttributes`: `"ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef"`
- `workflowExecutionTerminatedEventAttributes`: `"WorkflowExecutionTerminatedEventAttributesTypeDef"`
- `workflowExecutionCancelRequestedEventAttributes`: `"WorkflowExecutionCancelRequestedEventAttributesTypeDef"`
- `decisionTaskScheduledEventAttributes`: `"DecisionTaskScheduledEventAttributesTypeDef"`
- `decisionTaskStartedEventAttributes`: `"DecisionTaskStartedEventAttributesTypeDef"`
- `decisionTaskCompletedEventAttributes`: `"DecisionTaskCompletedEventAttributesTypeDef"`
- `decisionTaskTimedOutEventAttributes`: `"DecisionTaskTimedOutEventAttributesTypeDef"`
- `activityTaskScheduledEventAttributes`: `"ActivityTaskScheduledEventAttributesTypeDef"`
- `activityTaskStartedEventAttributes`: `"ActivityTaskStartedEventAttributesTypeDef"`
- `activityTaskCompletedEventAttributes`: `"ActivityTaskCompletedEventAttributesTypeDef"`
- `activityTaskFailedEventAttributes`: `"ActivityTaskFailedEventAttributesTypeDef"`
- `activityTaskTimedOutEventAttributes`: `"ActivityTaskTimedOutEventAttributesTypeDef"`
- `activityTaskCanceledEventAttributes`: `"ActivityTaskCanceledEventAttributesTypeDef"`
- `activityTaskCancelRequestedEventAttributes`: `"ActivityTaskCancelRequestedEventAttributesTypeDef"`
- `workflowExecutionSignaledEventAttributes`: `"WorkflowExecutionSignaledEventAttributesTypeDef"`
- `markerRecordedEventAttributes`: `"MarkerRecordedEventAttributesTypeDef"`
- `recordMarkerFailedEventAttributes`: `"RecordMarkerFailedEventAttributesTypeDef"`
- `timerStartedEventAttributes`: `"TimerStartedEventAttributesTypeDef"`
- `timerFiredEventAttributes`: `"TimerFiredEventAttributesTypeDef"`
- `timerCanceledEventAttributes`: `"TimerCanceledEventAttributesTypeDef"`
- `startChildWorkflowExecutionInitiatedEventAttributes`: `"StartChildWorkflowExecutionInitiatedEventAttributesTypeDef"`
- `childWorkflowExecutionStartedEventAttributes`: `"ChildWorkflowExecutionStartedEventAttributesTypeDef"`
- `childWorkflowExecutionCompletedEventAttributes`: `"ChildWorkflowExecutionCompletedEventAttributesTypeDef"`
- `childWorkflowExecutionFailedEventAttributes`: `"ChildWorkflowExecutionFailedEventAttributesTypeDef"`
- `childWorkflowExecutionTimedOutEventAttributes`: `"ChildWorkflowExecutionTimedOutEventAttributesTypeDef"`
- `childWorkflowExecutionCanceledEventAttributes`: `"ChildWorkflowExecutionCanceledEventAttributesTypeDef"`
- `childWorkflowExecutionTerminatedEventAttributes`: `"ChildWorkflowExecutionTerminatedEventAttributesTypeDef"`
- `signalExternalWorkflowExecutionInitiatedEventAttributes`: `"SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef"`
- `externalWorkflowExecutionSignaledEventAttributes`: `"ExternalWorkflowExecutionSignaledEventAttributesTypeDef"`
- `signalExternalWorkflowExecutionFailedEventAttributes`: `"SignalExternalWorkflowExecutionFailedEventAttributesTypeDef"`
- `externalWorkflowExecutionCancelRequestedEventAttributes`: `"ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef"`
- `requestCancelExternalWorkflowExecutionInitiatedEventAttributes`: `"RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef"`
- `requestCancelExternalWorkflowExecutionFailedEventAttributes`: `"RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef"`
- `scheduleActivityTaskFailedEventAttributes`: `"ScheduleActivityTaskFailedEventAttributesTypeDef"`
- `requestCancelActivityTaskFailedEventAttributes`: `"RequestCancelActivityTaskFailedEventAttributesTypeDef"`
- `startTimerFailedEventAttributes`: `"StartTimerFailedEventAttributesTypeDef"`
- `cancelTimerFailedEventAttributes`: `"CancelTimerFailedEventAttributesTypeDef"`
- `startChildWorkflowExecutionFailedEventAttributes`: `"StartChildWorkflowExecutionFailedEventAttributesTypeDef"`
- `lambdaFunctionScheduledEventAttributes`: `"LambdaFunctionScheduledEventAttributesTypeDef"`
- `lambdaFunctionStartedEventAttributes`: `"LambdaFunctionStartedEventAttributesTypeDef"`
- `lambdaFunctionCompletedEventAttributes`: `"LambdaFunctionCompletedEventAttributesTypeDef"`
- `lambdaFunctionFailedEventAttributes`: `"LambdaFunctionFailedEventAttributesTypeDef"`
- `lambdaFunctionTimedOutEventAttributes`: `"LambdaFunctionTimedOutEventAttributesTypeDef"`
- `scheduleLambdaFunctionFailedEventAttributes`: `"ScheduleLambdaFunctionFailedEventAttributesTypeDef"`
- `startLambdaFunctionFailedEventAttributes`: `"StartLambdaFunctionFailedEventAttributesTypeDef"`


## HistoryTypeDef

```python
from mypy_boto3_swf.type_defs import HistoryTypeDef
```


Required fields:
- `events`: `List["HistoryEventTypeDef"]`



Optional fields:
- `nextPageToken`: `str`


## LambdaFunctionCompletedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import LambdaFunctionCompletedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `result`: `str`


## LambdaFunctionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import LambdaFunctionFailedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `reason`: `str`
- `details`: `str`


## LambdaFunctionScheduledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import LambdaFunctionScheduledEventAttributesTypeDef
```


Required fields:
- `id`: `str`
- `name`: `str`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `control`: `str`
- `input`: `str`
- `startToCloseTimeout`: `str`


## LambdaFunctionStartedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import LambdaFunctionStartedEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`




## LambdaFunctionTimedOutEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import LambdaFunctionTimedOutEventAttributesTypeDef
```


Required fields:
- `scheduledEventId`: `int`
- `startedEventId`: `int`



Optional fields:
- `timeoutType`: `Literal['START_TO_CLOSE']`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_swf.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `tags`: `List["ResourceTagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## MarkerRecordedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import MarkerRecordedEventAttributesTypeDef
```


Required fields:
- `markerName`: `str`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `details`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_swf.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PendingTaskCountTypeDef

```python
from mypy_boto3_swf.type_defs import PendingTaskCountTypeDef
```


Required fields:
- `count`: `int`



Optional fields:
- `truncated`: `bool`


## RecordMarkerDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RecordMarkerDecisionAttributesTypeDef
```


Required fields:
- `markerName`: `str`



Optional fields:
- `details`: `str`


## RecordMarkerFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RecordMarkerFailedEventAttributesTypeDef
```


Required fields:
- `markerName`: `str`
- `cause`: `Literal['OPERATION_NOT_PERMITTED']`
- `decisionTaskCompletedEventId`: `int`




## RequestCancelActivityTaskDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RequestCancelActivityTaskDecisionAttributesTypeDef
```


Required fields:
- `activityId`: `str`




## RequestCancelActivityTaskFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RequestCancelActivityTaskFailedEventAttributesTypeDef
```


Required fields:
- `activityId`: `str`
- `cause`: `RequestCancelActivityTaskFailedCause`
- `decisionTaskCompletedEventId`: `int`




## RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef
```


Required fields:
- `workflowId`: `str`



Optional fields:
- `runId`: `str`
- `control`: `str`


## RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `workflowId`: `str`
- `cause`: `RequestCancelExternalWorkflowExecutionFailedCause`
- `initiatedEventId`: `int`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `runId`: `str`
- `control`: `str`


## RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef
```


Required fields:
- `workflowId`: `str`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `runId`: `str`
- `control`: `str`


## ResourceTagTypeDef

```python
from mypy_boto3_swf.type_defs import ResourceTagTypeDef
```


Required fields:
- `key`: `str`



Optional fields:
- `value`: `str`


## ResponseMetadata

```python
from mypy_boto3_swf.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RunTypeDef

```python
from mypy_boto3_swf.type_defs import RunTypeDef
```




Optional fields:
- `runId`: `str`


## ScheduleActivityTaskDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ScheduleActivityTaskDecisionAttributesTypeDef
```


Required fields:
- `activityType`: `"ActivityTypeTypeDef"`
- `activityId`: `str`



Optional fields:
- `control`: `str`
- `input`: `str`
- `scheduleToCloseTimeout`: `str`
- `taskList`: `"TaskListTypeDef"`
- `taskPriority`: `str`
- `scheduleToStartTimeout`: `str`
- `startToCloseTimeout`: `str`
- `heartbeatTimeout`: `str`


## ScheduleActivityTaskFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ScheduleActivityTaskFailedEventAttributesTypeDef
```


Required fields:
- `activityType`: `"ActivityTypeTypeDef"`
- `activityId`: `str`
- `cause`: `ScheduleActivityTaskFailedCause`
- `decisionTaskCompletedEventId`: `int`




## ScheduleLambdaFunctionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ScheduleLambdaFunctionDecisionAttributesTypeDef
```


Required fields:
- `id`: `str`
- `name`: `str`



Optional fields:
- `control`: `str`
- `input`: `str`
- `startToCloseTimeout`: `str`


## ScheduleLambdaFunctionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import ScheduleLambdaFunctionFailedEventAttributesTypeDef
```


Required fields:
- `id`: `str`
- `name`: `str`
- `cause`: `ScheduleLambdaFunctionFailedCause`
- `decisionTaskCompletedEventId`: `int`




## SignalExternalWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import SignalExternalWorkflowExecutionDecisionAttributesTypeDef
```


Required fields:
- `workflowId`: `str`
- `signalName`: `str`



Optional fields:
- `runId`: `str`
- `input`: `str`
- `control`: `str`


## SignalExternalWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import SignalExternalWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `workflowId`: `str`
- `cause`: `SignalExternalWorkflowExecutionFailedCause`
- `initiatedEventId`: `int`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `runId`: `str`
- `control`: `str`


## SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef
```


Required fields:
- `workflowId`: `str`
- `signalName`: `str`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `runId`: `str`
- `input`: `str`
- `control`: `str`


## StartChildWorkflowExecutionDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import StartChildWorkflowExecutionDecisionAttributesTypeDef
```


Required fields:
- `workflowType`: `"WorkflowTypeTypeDef"`
- `workflowId`: `str`



Optional fields:
- `control`: `str`
- `input`: `str`
- `executionStartToCloseTimeout`: `str`
- `taskList`: `"TaskListTypeDef"`
- `taskPriority`: `str`
- `taskStartToCloseTimeout`: `str`
- `childPolicy`: `ChildPolicy`
- `tagList`: `List[str]`
- `lambdaRole`: `str`


## StartChildWorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import StartChildWorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `workflowType`: `"WorkflowTypeTypeDef"`
- `cause`: `StartChildWorkflowExecutionFailedCause`
- `workflowId`: `str`
- `initiatedEventId`: `int`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `control`: `str`


## StartChildWorkflowExecutionInitiatedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import StartChildWorkflowExecutionInitiatedEventAttributesTypeDef
```


Required fields:
- `workflowId`: `str`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `taskList`: `"TaskListTypeDef"`
- `decisionTaskCompletedEventId`: `int`
- `childPolicy`: `ChildPolicy`



Optional fields:
- `control`: `str`
- `input`: `str`
- `executionStartToCloseTimeout`: `str`
- `taskPriority`: `str`
- `taskStartToCloseTimeout`: `str`
- `tagList`: `List[str]`
- `lambdaRole`: `str`


## StartLambdaFunctionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import StartLambdaFunctionFailedEventAttributesTypeDef
```




Optional fields:
- `scheduledEventId`: `int`
- `cause`: `Literal['ASSUME_ROLE_FAILED']`
- `message`: `str`


## StartTimerDecisionAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import StartTimerDecisionAttributesTypeDef
```


Required fields:
- `timerId`: `str`
- `startToFireTimeout`: `str`



Optional fields:
- `control`: `str`


## StartTimerFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import StartTimerFailedEventAttributesTypeDef
```


Required fields:
- `timerId`: `str`
- `cause`: `StartTimerFailedCause`
- `decisionTaskCompletedEventId`: `int`




## TagFilterTypeDef

```python
from mypy_boto3_swf.type_defs import TagFilterTypeDef
```


Required fields:
- `tag`: `str`




## TaskListTypeDef

```python
from mypy_boto3_swf.type_defs import TaskListTypeDef
```


Required fields:
- `name`: `str`




## TimerCanceledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import TimerCanceledEventAttributesTypeDef
```


Required fields:
- `timerId`: `str`
- `startedEventId`: `int`
- `decisionTaskCompletedEventId`: `int`




## TimerFiredEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import TimerFiredEventAttributesTypeDef
```


Required fields:
- `timerId`: `str`
- `startedEventId`: `int`




## TimerStartedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import TimerStartedEventAttributesTypeDef
```


Required fields:
- `timerId`: `str`
- `startToFireTimeout`: `str`
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `control`: `str`


## WorkflowExecutionCancelRequestedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionCancelRequestedEventAttributesTypeDef
```




Optional fields:
- `externalWorkflowExecution`: `"WorkflowExecutionTypeDef"`
- `externalInitiatedEventId`: `int`
- `cause`: `Literal['CHILD_POLICY_APPLIED']`


## WorkflowExecutionCanceledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionCanceledEventAttributesTypeDef
```


Required fields:
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `details`: `str`


## WorkflowExecutionCompletedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionCompletedEventAttributesTypeDef
```


Required fields:
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `result`: `str`


## WorkflowExecutionConfigurationTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionConfigurationTypeDef
```


Required fields:
- `taskStartToCloseTimeout`: `str`
- `executionStartToCloseTimeout`: `str`
- `taskList`: `"TaskListTypeDef"`
- `childPolicy`: `ChildPolicy`



Optional fields:
- `taskPriority`: `str`
- `lambdaRole`: `str`


## WorkflowExecutionContinuedAsNewEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionContinuedAsNewEventAttributesTypeDef
```


Required fields:
- `decisionTaskCompletedEventId`: `int`
- `newExecutionRunId`: `str`
- `taskList`: `"TaskListTypeDef"`
- `childPolicy`: `ChildPolicy`
- `workflowType`: `"WorkflowTypeTypeDef"`



Optional fields:
- `input`: `str`
- `executionStartToCloseTimeout`: `str`
- `taskPriority`: `str`
- `taskStartToCloseTimeout`: `str`
- `tagList`: `List[str]`
- `lambdaRole`: `str`


## WorkflowExecutionCountTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionCountTypeDef
```


Required fields:
- `count`: `int`



Optional fields:
- `truncated`: `bool`


## WorkflowExecutionDetailTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionDetailTypeDef
```


Required fields:
- `executionInfo`: `"WorkflowExecutionInfoTypeDef"`
- `executionConfiguration`: `"WorkflowExecutionConfigurationTypeDef"`
- `openCounts`: `"WorkflowExecutionOpenCountsTypeDef"`



Optional fields:
- `latestActivityTaskTimestamp`: `datetime`
- `latestExecutionContext`: `str`


## WorkflowExecutionFailedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionFailedEventAttributesTypeDef
```


Required fields:
- `decisionTaskCompletedEventId`: `int`



Optional fields:
- `reason`: `str`
- `details`: `str`


## WorkflowExecutionFilterTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionFilterTypeDef
```


Required fields:
- `workflowId`: `str`




## WorkflowExecutionInfoTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionInfoTypeDef
```


Required fields:
- `execution`: `"WorkflowExecutionTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`
- `startTimestamp`: `datetime`
- `executionStatus`: `ExecutionStatus`



Optional fields:
- `closeTimestamp`: `datetime`
- `closeStatus`: `CloseStatus`
- `parent`: `"WorkflowExecutionTypeDef"`
- `tagList`: `List[str]`
- `cancelRequested`: `bool`


## WorkflowExecutionInfosTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionInfosTypeDef
```


Required fields:
- `executionInfos`: `List["WorkflowExecutionInfoTypeDef"]`



Optional fields:
- `nextPageToken`: `str`


## WorkflowExecutionOpenCountsTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionOpenCountsTypeDef
```


Required fields:
- `openActivityTasks`: `int`
- `openDecisionTasks`: `int`
- `openTimers`: `int`
- `openChildWorkflowExecutions`: `int`



Optional fields:
- `openLambdaFunctions`: `int`


## WorkflowExecutionSignaledEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionSignaledEventAttributesTypeDef
```


Required fields:
- `signalName`: `str`



Optional fields:
- `input`: `str`
- `externalWorkflowExecution`: `"WorkflowExecutionTypeDef"`
- `externalInitiatedEventId`: `int`


## WorkflowExecutionStartedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionStartedEventAttributesTypeDef
```


Required fields:
- `childPolicy`: `ChildPolicy`
- `taskList`: `"TaskListTypeDef"`
- `workflowType`: `"WorkflowTypeTypeDef"`



Optional fields:
- `input`: `str`
- `executionStartToCloseTimeout`: `str`
- `taskStartToCloseTimeout`: `str`
- `taskPriority`: `str`
- `tagList`: `List[str]`
- `continuedExecutionRunId`: `str`
- `parentWorkflowExecution`: `"WorkflowExecutionTypeDef"`
- `parentInitiatedEventId`: `int`
- `lambdaRole`: `str`


## WorkflowExecutionTerminatedEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionTerminatedEventAttributesTypeDef
```


Required fields:
- `childPolicy`: `ChildPolicy`



Optional fields:
- `reason`: `str`
- `details`: `str`
- `cause`: `WorkflowExecutionTerminatedCause`


## WorkflowExecutionTimedOutEventAttributesTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionTimedOutEventAttributesTypeDef
```


Required fields:
- `timeoutType`: `Literal['START_TO_CLOSE']`
- `childPolicy`: `ChildPolicy`




## WorkflowExecutionTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowExecutionTypeDef
```


Required fields:
- `workflowId`: `str`
- `runId`: `str`




## WorkflowTypeConfigurationTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowTypeConfigurationTypeDef
```




Optional fields:
- `defaultTaskStartToCloseTimeout`: `str`
- `defaultExecutionStartToCloseTimeout`: `str`
- `defaultTaskList`: `"TaskListTypeDef"`
- `defaultTaskPriority`: `str`
- `defaultChildPolicy`: `ChildPolicy`
- `defaultLambdaRole`: `str`


## WorkflowTypeDetailTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowTypeDetailTypeDef
```


Required fields:
- `typeInfo`: `"WorkflowTypeInfoTypeDef"`
- `configuration`: `"WorkflowTypeConfigurationTypeDef"`




## WorkflowTypeFilterTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowTypeFilterTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `version`: `str`


## WorkflowTypeInfoTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowTypeInfoTypeDef
```


Required fields:
- `workflowType`: `"WorkflowTypeTypeDef"`
- `status`: `RegistrationStatus`
- `creationDate`: `datetime`



Optional fields:
- `description`: `str`
- `deprecationDate`: `datetime`


## WorkflowTypeInfosTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowTypeInfosTypeDef
```


Required fields:
- `typeInfos`: `List["WorkflowTypeInfoTypeDef"]`



Optional fields:
- `nextPageToken`: `str`


## WorkflowTypeTypeDef

```python
from mypy_boto3_swf.type_defs import WorkflowTypeTypeDef
```


Required fields:
- `name`: `str`
- `version`: `str`



