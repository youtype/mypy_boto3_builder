# Type annotations for boto3 SWF module

> [Index](../index.md) > SWF

Auto-generated documentation for [SWF](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html#SWF)
type annotations stubs module [mypy_boto3_swf](https://pypi.org/project/mypy-boto3-swf/).

```bash
pip install mypy-boto3-swf
```

- [Type annotations for boto3 SWF module](#type-annotations-for-boto3-swf-module)
  - [SWFClient](#swfclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## SWFClient

Type annotations for  `boto3.client("swf")` as [SWFClient](./client.md)

Can be used directly:

```python
from mypy_boto3_swf.client import SWFClient
```


SWFClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [count_closed_workflow_executions](./client.md#count-closed-workflow-executions)
- [count_open_workflow_executions](./client.md#count-open-workflow-executions)
- [count_pending_activity_tasks](./client.md#count-pending-activity-tasks)
- [count_pending_decision_tasks](./client.md#count-pending-decision-tasks)
- [deprecate_activity_type](./client.md#deprecate-activity-type)
- [deprecate_domain](./client.md#deprecate-domain)
- [deprecate_workflow_type](./client.md#deprecate-workflow-type)
- [describe_activity_type](./client.md#describe-activity-type)
- [describe_domain](./client.md#describe-domain)
- [describe_workflow_execution](./client.md#describe-workflow-execution)
- [describe_workflow_type](./client.md#describe-workflow-type)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_workflow_execution_history](./client.md#get-workflow-execution-history)
- [list_activity_types](./client.md#list-activity-types)
- [list_closed_workflow_executions](./client.md#list-closed-workflow-executions)
- [list_domains](./client.md#list-domains)
- [list_open_workflow_executions](./client.md#list-open-workflow-executions)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_workflow_types](./client.md#list-workflow-types)
- [poll_for_activity_task](./client.md#poll-for-activity-task)
- [poll_for_decision_task](./client.md#poll-for-decision-task)
- [record_activity_task_heartbeat](./client.md#record-activity-task-heartbeat)
- [register_activity_type](./client.md#register-activity-type)
- [register_domain](./client.md#register-domain)
- [register_workflow_type](./client.md#register-workflow-type)
- [request_cancel_workflow_execution](./client.md#request-cancel-workflow-execution)
- [respond_activity_task_canceled](./client.md#respond-activity-task-canceled)
- [respond_activity_task_completed](./client.md#respond-activity-task-completed)
- [respond_activity_task_failed](./client.md#respond-activity-task-failed)
- [respond_decision_task_completed](./client.md#respond-decision-task-completed)
- [signal_workflow_execution](./client.md#signal-workflow-execution)
- [start_workflow_execution](./client.md#start-workflow-execution)
- [tag_resource](./client.md#tag-resource)
- [terminate_workflow_execution](./client.md#terminate-workflow-execution)
- [undeprecate_activity_type](./client.md#undeprecate-activity-type)
- [undeprecate_domain](./client.md#undeprecate-domain)
- [undeprecate_workflow_type](./client.md#undeprecate-workflow-type)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DefaultUndefinedFault](./client.md#defaultundefinedfault)
- [DomainAlreadyExistsFault](./client.md#domainalreadyexistsfault)
- [DomainDeprecatedFault](./client.md#domaindeprecatedfault)
- [LimitExceededFault](./client.md#limitexceededfault)
- [OperationNotPermittedFault](./client.md#operationnotpermittedfault)
- [TooManyTagsFault](./client.md#toomanytagsfault)
- [TypeAlreadyExistsFault](./client.md#typealreadyexistsfault)
- [TypeDeprecatedFault](./client.md#typedeprecatedfault)
- [UnknownResourceFault](./client.md#unknownresourcefault)
- [WorkflowExecutionAlreadyStartedFault](./client.md#workflowexecutionalreadystartedfault)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("swf").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_swf.paginators import GetWorkflowExecutionHistoryPaginator, ...
```

- [GetWorkflowExecutionHistoryPaginator](./paginators.md#getworkflowexecutionhistorypaginator)
- [ListActivityTypesPaginator](./paginators.md#listactivitytypespaginator)
- [ListClosedWorkflowExecutionsPaginator](./paginators.md#listclosedworkflowexecutionspaginator)
- [ListDomainsPaginator](./paginators.md#listdomainspaginator)
- [ListOpenWorkflowExecutionsPaginator](./paginators.md#listopenworkflowexecutionspaginator)
- [ListWorkflowTypesPaginator](./paginators.md#listworkflowtypespaginator)
- [PollForDecisionTaskPaginator](./paginators.md#pollfordecisiontaskpaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_swf.literals import ActivityTaskTimeoutType, ...
```

- [ActivityTaskTimeoutType](./literals.md#activitytasktimeouttype)
- [CancelTimerFailedCause](./literals.md#canceltimerfailedcause)
- [CancelWorkflowExecutionFailedCause](./literals.md#cancelworkflowexecutionfailedcause)
- [ChildPolicy](./literals.md#childpolicy)
- [CloseStatus](./literals.md#closestatus)
- [CompleteWorkflowExecutionFailedCause](./literals.md#completeworkflowexecutionfailedcause)
- [ContinueAsNewWorkflowExecutionFailedCause](./literals.md#continueasnewworkflowexecutionfailedcause)
- [DecisionTaskTimeoutType](./literals.md#decisiontasktimeouttype)
- [DecisionType](./literals.md#decisiontype)
- [EventType](./literals.md#eventtype)
- [ExecutionStatus](./literals.md#executionstatus)
- [FailWorkflowExecutionFailedCause](./literals.md#failworkflowexecutionfailedcause)
- [GetWorkflowExecutionHistoryPaginatorName](./literals.md#getworkflowexecutionhistorypaginatorname)
- [LambdaFunctionTimeoutType](./literals.md#lambdafunctiontimeouttype)
- [ListActivityTypesPaginatorName](./literals.md#listactivitytypespaginatorname)
- [ListClosedWorkflowExecutionsPaginatorName](./literals.md#listclosedworkflowexecutionspaginatorname)
- [ListDomainsPaginatorName](./literals.md#listdomainspaginatorname)
- [ListOpenWorkflowExecutionsPaginatorName](./literals.md#listopenworkflowexecutionspaginatorname)
- [ListWorkflowTypesPaginatorName](./literals.md#listworkflowtypespaginatorname)
- [PollForDecisionTaskPaginatorName](./literals.md#pollfordecisiontaskpaginatorname)
- [RecordMarkerFailedCause](./literals.md#recordmarkerfailedcause)
- [RegistrationStatus](./literals.md#registrationstatus)
- [RequestCancelActivityTaskFailedCause](./literals.md#requestcancelactivitytaskfailedcause)
- [RequestCancelExternalWorkflowExecutionFailedCause](./literals.md#requestcancelexternalworkflowexecutionfailedcause)
- [ScheduleActivityTaskFailedCause](./literals.md#scheduleactivitytaskfailedcause)
- [ScheduleLambdaFunctionFailedCause](./literals.md#schedulelambdafunctionfailedcause)
- [SignalExternalWorkflowExecutionFailedCause](./literals.md#signalexternalworkflowexecutionfailedcause)
- [StartChildWorkflowExecutionFailedCause](./literals.md#startchildworkflowexecutionfailedcause)
- [StartLambdaFunctionFailedCause](./literals.md#startlambdafunctionfailedcause)
- [StartTimerFailedCause](./literals.md#starttimerfailedcause)
- [WorkflowExecutionCancelRequestedCause](./literals.md#workflowexecutioncancelrequestedcause)
- [WorkflowExecutionTerminatedCause](./literals.md#workflowexecutionterminatedcause)
- [WorkflowExecutionTimeoutType](./literals.md#workflowexecutiontimeouttype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_swf.type_defs import ActivityTaskCancelRequestedEventAttributesTypeDef, ...
```

- [ActivityTaskCancelRequestedEventAttributesTypeDef](./type_defs.md#activitytaskcancelrequestedeventattributestypedef)
- [ActivityTaskCanceledEventAttributesTypeDef](./type_defs.md#activitytaskcanceledeventattributestypedef)
- [ActivityTaskCompletedEventAttributesTypeDef](./type_defs.md#activitytaskcompletedeventattributestypedef)
- [ActivityTaskFailedEventAttributesTypeDef](./type_defs.md#activitytaskfailedeventattributestypedef)
- [ActivityTaskScheduledEventAttributesTypeDef](./type_defs.md#activitytaskscheduledeventattributestypedef)
- [ActivityTaskStartedEventAttributesTypeDef](./type_defs.md#activitytaskstartedeventattributestypedef)
- [ActivityTaskStatusTypeDef](./type_defs.md#activitytaskstatustypedef)
- [ActivityTaskTimedOutEventAttributesTypeDef](./type_defs.md#activitytasktimedouteventattributestypedef)
- [ActivityTaskTypeDef](./type_defs.md#activitytasktypedef)
- [ActivityTypeConfigurationTypeDef](./type_defs.md#activitytypeconfigurationtypedef)
- [ActivityTypeDetailTypeDef](./type_defs.md#activitytypedetailtypedef)
- [ActivityTypeInfoTypeDef](./type_defs.md#activitytypeinfotypedef)
- [ActivityTypeInfosTypeDef](./type_defs.md#activitytypeinfostypedef)
- [ActivityTypeTypeDef](./type_defs.md#activitytypetypedef)
- [CancelTimerDecisionAttributesTypeDef](./type_defs.md#canceltimerdecisionattributestypedef)
- [CancelTimerFailedEventAttributesTypeDef](./type_defs.md#canceltimerfailedeventattributestypedef)
- [CancelWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#cancelworkflowexecutiondecisionattributestypedef)
- [CancelWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#cancelworkflowexecutionfailedeventattributestypedef)
- [ChildWorkflowExecutionCanceledEventAttributesTypeDef](./type_defs.md#childworkflowexecutioncanceledeventattributestypedef)
- [ChildWorkflowExecutionCompletedEventAttributesTypeDef](./type_defs.md#childworkflowexecutioncompletedeventattributestypedef)
- [ChildWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#childworkflowexecutionfailedeventattributestypedef)
- [ChildWorkflowExecutionStartedEventAttributesTypeDef](./type_defs.md#childworkflowexecutionstartedeventattributestypedef)
- [ChildWorkflowExecutionTerminatedEventAttributesTypeDef](./type_defs.md#childworkflowexecutionterminatedeventattributestypedef)
- [ChildWorkflowExecutionTimedOutEventAttributesTypeDef](./type_defs.md#childworkflowexecutiontimedouteventattributestypedef)
- [CloseStatusFilterTypeDef](./type_defs.md#closestatusfiltertypedef)
- [CompleteWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#completeworkflowexecutiondecisionattributestypedef)
- [CompleteWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#completeworkflowexecutionfailedeventattributestypedef)
- [ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#continueasnewworkflowexecutiondecisionattributestypedef)
- [ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#continueasnewworkflowexecutionfailedeventattributestypedef)
- [DecisionTaskCompletedEventAttributesTypeDef](./type_defs.md#decisiontaskcompletedeventattributestypedef)
- [DecisionTaskScheduledEventAttributesTypeDef](./type_defs.md#decisiontaskscheduledeventattributestypedef)
- [DecisionTaskStartedEventAttributesTypeDef](./type_defs.md#decisiontaskstartedeventattributestypedef)
- [DecisionTaskTimedOutEventAttributesTypeDef](./type_defs.md#decisiontasktimedouteventattributestypedef)
- [DecisionTaskTypeDef](./type_defs.md#decisiontasktypedef)
- [DecisionTypeDef](./type_defs.md#decisiontypedef)
- [DomainConfigurationTypeDef](./type_defs.md#domainconfigurationtypedef)
- [DomainDetailTypeDef](./type_defs.md#domaindetailtypedef)
- [DomainInfoTypeDef](./type_defs.md#domaininfotypedef)
- [DomainInfosTypeDef](./type_defs.md#domaininfostypedef)
- [ExecutionTimeFilterTypeDef](./type_defs.md#executiontimefiltertypedef)
- [ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef](./type_defs.md#externalworkflowexecutioncancelrequestedeventattributestypedef)
- [ExternalWorkflowExecutionSignaledEventAttributesTypeDef](./type_defs.md#externalworkflowexecutionsignaledeventattributestypedef)
- [FailWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#failworkflowexecutiondecisionattributestypedef)
- [FailWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#failworkflowexecutionfailedeventattributestypedef)
- [HistoryEventTypeDef](./type_defs.md#historyeventtypedef)
- [HistoryTypeDef](./type_defs.md#historytypedef)
- [LambdaFunctionCompletedEventAttributesTypeDef](./type_defs.md#lambdafunctioncompletedeventattributestypedef)
- [LambdaFunctionFailedEventAttributesTypeDef](./type_defs.md#lambdafunctionfailedeventattributestypedef)
- [LambdaFunctionScheduledEventAttributesTypeDef](./type_defs.md#lambdafunctionscheduledeventattributestypedef)
- [LambdaFunctionStartedEventAttributesTypeDef](./type_defs.md#lambdafunctionstartedeventattributestypedef)
- [LambdaFunctionTimedOutEventAttributesTypeDef](./type_defs.md#lambdafunctiontimedouteventattributestypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [MarkerRecordedEventAttributesTypeDef](./type_defs.md#markerrecordedeventattributestypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PendingTaskCountTypeDef](./type_defs.md#pendingtaskcounttypedef)
- [RecordMarkerDecisionAttributesTypeDef](./type_defs.md#recordmarkerdecisionattributestypedef)
- [RecordMarkerFailedEventAttributesTypeDef](./type_defs.md#recordmarkerfailedeventattributestypedef)
- [RequestCancelActivityTaskDecisionAttributesTypeDef](./type_defs.md#requestcancelactivitytaskdecisionattributestypedef)
- [RequestCancelActivityTaskFailedEventAttributesTypeDef](./type_defs.md#requestcancelactivitytaskfailedeventattributestypedef)
- [RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#requestcancelexternalworkflowexecutiondecisionattributestypedef)
- [RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#requestcancelexternalworkflowexecutionfailedeventattributestypedef)
- [RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef](./type_defs.md#requestcancelexternalworkflowexecutioninitiatedeventattributestypedef)
- [ResourceTagTypeDef](./type_defs.md#resourcetagtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RunTypeDef](./type_defs.md#runtypedef)
- [ScheduleActivityTaskDecisionAttributesTypeDef](./type_defs.md#scheduleactivitytaskdecisionattributestypedef)
- [ScheduleActivityTaskFailedEventAttributesTypeDef](./type_defs.md#scheduleactivitytaskfailedeventattributestypedef)
- [ScheduleLambdaFunctionDecisionAttributesTypeDef](./type_defs.md#schedulelambdafunctiondecisionattributestypedef)
- [ScheduleLambdaFunctionFailedEventAttributesTypeDef](./type_defs.md#schedulelambdafunctionfailedeventattributestypedef)
- [SignalExternalWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#signalexternalworkflowexecutiondecisionattributestypedef)
- [SignalExternalWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#signalexternalworkflowexecutionfailedeventattributestypedef)
- [SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef](./type_defs.md#signalexternalworkflowexecutioninitiatedeventattributestypedef)
- [StartChildWorkflowExecutionDecisionAttributesTypeDef](./type_defs.md#startchildworkflowexecutiondecisionattributestypedef)
- [StartChildWorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#startchildworkflowexecutionfailedeventattributestypedef)
- [StartChildWorkflowExecutionInitiatedEventAttributesTypeDef](./type_defs.md#startchildworkflowexecutioninitiatedeventattributestypedef)
- [StartLambdaFunctionFailedEventAttributesTypeDef](./type_defs.md#startlambdafunctionfailedeventattributestypedef)
- [StartTimerDecisionAttributesTypeDef](./type_defs.md#starttimerdecisionattributestypedef)
- [StartTimerFailedEventAttributesTypeDef](./type_defs.md#starttimerfailedeventattributestypedef)
- [TagFilterTypeDef](./type_defs.md#tagfiltertypedef)
- [TaskListTypeDef](./type_defs.md#tasklisttypedef)
- [TimerCanceledEventAttributesTypeDef](./type_defs.md#timercanceledeventattributestypedef)
- [TimerFiredEventAttributesTypeDef](./type_defs.md#timerfiredeventattributestypedef)
- [TimerStartedEventAttributesTypeDef](./type_defs.md#timerstartedeventattributestypedef)
- [WorkflowExecutionCancelRequestedEventAttributesTypeDef](./type_defs.md#workflowexecutioncancelrequestedeventattributestypedef)
- [WorkflowExecutionCanceledEventAttributesTypeDef](./type_defs.md#workflowexecutioncanceledeventattributestypedef)
- [WorkflowExecutionCompletedEventAttributesTypeDef](./type_defs.md#workflowexecutioncompletedeventattributestypedef)
- [WorkflowExecutionConfigurationTypeDef](./type_defs.md#workflowexecutionconfigurationtypedef)
- [WorkflowExecutionContinuedAsNewEventAttributesTypeDef](./type_defs.md#workflowexecutioncontinuedasneweventattributestypedef)
- [WorkflowExecutionCountTypeDef](./type_defs.md#workflowexecutioncounttypedef)
- [WorkflowExecutionDetailTypeDef](./type_defs.md#workflowexecutiondetailtypedef)
- [WorkflowExecutionFailedEventAttributesTypeDef](./type_defs.md#workflowexecutionfailedeventattributestypedef)
- [WorkflowExecutionFilterTypeDef](./type_defs.md#workflowexecutionfiltertypedef)
- [WorkflowExecutionInfoTypeDef](./type_defs.md#workflowexecutioninfotypedef)
- [WorkflowExecutionInfosTypeDef](./type_defs.md#workflowexecutioninfostypedef)
- [WorkflowExecutionOpenCountsTypeDef](./type_defs.md#workflowexecutionopencountstypedef)
- [WorkflowExecutionSignaledEventAttributesTypeDef](./type_defs.md#workflowexecutionsignaledeventattributestypedef)
- [WorkflowExecutionStartedEventAttributesTypeDef](./type_defs.md#workflowexecutionstartedeventattributestypedef)
- [WorkflowExecutionTerminatedEventAttributesTypeDef](./type_defs.md#workflowexecutionterminatedeventattributestypedef)
- [WorkflowExecutionTimedOutEventAttributesTypeDef](./type_defs.md#workflowexecutiontimedouteventattributestypedef)
- [WorkflowExecutionTypeDef](./type_defs.md#workflowexecutiontypedef)
- [WorkflowTypeConfigurationTypeDef](./type_defs.md#workflowtypeconfigurationtypedef)
- [WorkflowTypeDetailTypeDef](./type_defs.md#workflowtypedetailtypedef)
- [WorkflowTypeFilterTypeDef](./type_defs.md#workflowtypefiltertypedef)
- [WorkflowTypeInfoTypeDef](./type_defs.md#workflowtypeinfotypedef)
- [WorkflowTypeInfosTypeDef](./type_defs.md#workflowtypeinfostypedef)
- [WorkflowTypeTypeDef](./type_defs.md#workflowtypetypedef)
