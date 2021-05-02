# Structures for boto3 SFN module

> [Index](../index.md) > [SFN](./index.md) > Structures

Auto-generated documentation for [SFN](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN)
type annotations stubs module [mypy_boto3_stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/).

- [Structures for boto3 SFN module](#structures-for-boto3-sfn-module)
  - [ActivityFailedEventDetailsTypeDef](#activityfailedeventdetailstypedef)
  - [ActivityListItemTypeDef](#activitylistitemtypedef)
  - [ActivityScheduleFailedEventDetailsTypeDef](#activityschedulefailedeventdetailstypedef)
  - [ActivityScheduledEventDetailsTypeDef](#activityscheduledeventdetailstypedef)
  - [ActivityStartedEventDetailsTypeDef](#activitystartedeventdetailstypedef)
  - [ActivitySucceededEventDetailsTypeDef](#activitysucceededeventdetailstypedef)
  - [ActivityTimedOutEventDetailsTypeDef](#activitytimedouteventdetailstypedef)
  - [BillingDetailsTypeDef](#billingdetailstypedef)
  - [CloudWatchEventsExecutionDataDetailsTypeDef](#cloudwatcheventsexecutiondatadetailstypedef)
  - [CloudWatchLogsLogGroupTypeDef](#cloudwatchlogsloggrouptypedef)
  - [CreateActivityOutputTypeDef](#createactivityoutputtypedef)
  - [CreateStateMachineOutputTypeDef](#createstatemachineoutputtypedef)
  - [DescribeActivityOutputTypeDef](#describeactivityoutputtypedef)
  - [DescribeExecutionOutputTypeDef](#describeexecutionoutputtypedef)
  - [DescribeStateMachineForExecutionOutputTypeDef](#describestatemachineforexecutionoutputtypedef)
  - [DescribeStateMachineOutputTypeDef](#describestatemachineoutputtypedef)
  - [ExecutionAbortedEventDetailsTypeDef](#executionabortedeventdetailstypedef)
  - [ExecutionFailedEventDetailsTypeDef](#executionfailedeventdetailstypedef)
  - [ExecutionListItemTypeDef](#executionlistitemtypedef)
  - [ExecutionStartedEventDetailsTypeDef](#executionstartedeventdetailstypedef)
  - [ExecutionSucceededEventDetailsTypeDef](#executionsucceededeventdetailstypedef)
  - [ExecutionTimedOutEventDetailsTypeDef](#executiontimedouteventdetailstypedef)
  - [GetActivityTaskOutputTypeDef](#getactivitytaskoutputtypedef)
  - [GetExecutionHistoryOutputTypeDef](#getexecutionhistoryoutputtypedef)
  - [HistoryEventExecutionDataDetailsTypeDef](#historyeventexecutiondatadetailstypedef)
  - [HistoryEventTypeDef](#historyeventtypedef)
  - [LambdaFunctionFailedEventDetailsTypeDef](#lambdafunctionfailedeventdetailstypedef)
  - [LambdaFunctionScheduleFailedEventDetailsTypeDef](#lambdafunctionschedulefailedeventdetailstypedef)
  - [LambdaFunctionScheduledEventDetailsTypeDef](#lambdafunctionscheduledeventdetailstypedef)
  - [LambdaFunctionStartFailedEventDetailsTypeDef](#lambdafunctionstartfailedeventdetailstypedef)
  - [LambdaFunctionSucceededEventDetailsTypeDef](#lambdafunctionsucceededeventdetailstypedef)
  - [LambdaFunctionTimedOutEventDetailsTypeDef](#lambdafunctiontimedouteventdetailstypedef)
  - [ListActivitiesOutputTypeDef](#listactivitiesoutputtypedef)
  - [ListExecutionsOutputTypeDef](#listexecutionsoutputtypedef)
  - [ListStateMachinesOutputTypeDef](#liststatemachinesoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [LogDestinationTypeDef](#logdestinationtypedef)
  - [LoggingConfigurationTypeDef](#loggingconfigurationtypedef)
  - [MapIterationEventDetailsTypeDef](#mapiterationeventdetailstypedef)
  - [MapStateStartedEventDetailsTypeDef](#mapstatestartedeventdetailstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [StartExecutionOutputTypeDef](#startexecutionoutputtypedef)
  - [StartSyncExecutionOutputTypeDef](#startsyncexecutionoutputtypedef)
  - [StateEnteredEventDetailsTypeDef](#stateenteredeventdetailstypedef)
  - [StateExitedEventDetailsTypeDef](#stateexitedeventdetailstypedef)
  - [StateMachineListItemTypeDef](#statemachinelistitemtypedef)
  - [StopExecutionOutputTypeDef](#stopexecutionoutputtypedef)
  - [TagTypeDef](#tagtypedef)
  - [TaskFailedEventDetailsTypeDef](#taskfailedeventdetailstypedef)
  - [TaskScheduledEventDetailsTypeDef](#taskscheduledeventdetailstypedef)
  - [TaskStartFailedEventDetailsTypeDef](#taskstartfailedeventdetailstypedef)
  - [TaskStartedEventDetailsTypeDef](#taskstartedeventdetailstypedef)
  - [TaskSubmitFailedEventDetailsTypeDef](#tasksubmitfailedeventdetailstypedef)
  - [TaskSubmittedEventDetailsTypeDef](#tasksubmittedeventdetailstypedef)
  - [TaskSucceededEventDetailsTypeDef](#tasksucceededeventdetailstypedef)
  - [TaskTimedOutEventDetailsTypeDef](#tasktimedouteventdetailstypedef)
  - [TracingConfigurationTypeDef](#tracingconfigurationtypedef)
  - [UpdateStateMachineOutputTypeDef](#updatestatemachineoutputtypedef)

## ActivityFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## ActivityListItemTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivityListItemTypeDef
```


Required fields:
- `activityArn`: `str`
- `name`: `str`
- `creationDate`: `datetime`




## ActivityScheduleFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivityScheduleFailedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## ActivityScheduledEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivityScheduledEventDetailsTypeDef
```


Required fields:
- `resource`: `str`



Optional fields:
- `input`: `str`
- `inputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`
- `timeoutInSeconds`: `int`
- `heartbeatInSeconds`: `int`


## ActivityStartedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivityStartedEventDetailsTypeDef
```




Optional fields:
- `workerName`: `str`


## ActivitySucceededEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivitySucceededEventDetailsTypeDef
```




Optional fields:
- `output`: `str`
- `outputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## ActivityTimedOutEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ActivityTimedOutEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## BillingDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import BillingDetailsTypeDef
```




Optional fields:
- `billedMemoryUsedInMB`: `int`
- `billedDurationInMilliseconds`: `int`


## CloudWatchEventsExecutionDataDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import CloudWatchEventsExecutionDataDetailsTypeDef
```




Optional fields:
- `included`: `bool`


## CloudWatchLogsLogGroupTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import CloudWatchLogsLogGroupTypeDef
```




Optional fields:
- `logGroupArn`: `str`


## CreateActivityOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import CreateActivityOutputTypeDef
```


Required fields:
- `activityArn`: `str`
- `creationDate`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateStateMachineOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import CreateStateMachineOutputTypeDef
```


Required fields:
- `stateMachineArn`: `str`
- `creationDate`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeActivityOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import DescribeActivityOutputTypeDef
```


Required fields:
- `activityArn`: `str`
- `name`: `str`
- `creationDate`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeExecutionOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import DescribeExecutionOutputTypeDef
```


Required fields:
- `executionArn`: `str`
- `stateMachineArn`: `str`
- `status`: `ExecutionStatus`
- `startDate`: `datetime`



Optional fields:
- `name`: `str`
- `stopDate`: `datetime`
- `input`: `str`
- `inputDetails`: `"CloudWatchEventsExecutionDataDetailsTypeDef"`
- `output`: `str`
- `outputDetails`: `"CloudWatchEventsExecutionDataDetailsTypeDef"`
- `traceHeader`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStateMachineForExecutionOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import DescribeStateMachineForExecutionOutputTypeDef
```


Required fields:
- `stateMachineArn`: `str`
- `name`: `str`
- `definition`: `str`
- `roleArn`: `str`
- `updateDate`: `datetime`



Optional fields:
- `loggingConfiguration`: `"LoggingConfigurationTypeDef"`
- `tracingConfiguration`: `"TracingConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeStateMachineOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import DescribeStateMachineOutputTypeDef
```


Required fields:
- `stateMachineArn`: `str`
- `name`: `str`
- `definition`: `str`
- `roleArn`: `str`
- `type`: `StateMachineType`
- `creationDate`: `datetime`



Optional fields:
- `status`: `StateMachineStatus`
- `loggingConfiguration`: `"LoggingConfigurationTypeDef"`
- `tracingConfiguration`: `"TracingConfigurationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ExecutionAbortedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ExecutionAbortedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## ExecutionFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ExecutionFailedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## ExecutionListItemTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ExecutionListItemTypeDef
```


Required fields:
- `executionArn`: `str`
- `stateMachineArn`: `str`
- `name`: `str`
- `status`: `ExecutionStatus`
- `startDate`: `datetime`



Optional fields:
- `stopDate`: `datetime`


## ExecutionStartedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ExecutionStartedEventDetailsTypeDef
```




Optional fields:
- `input`: `str`
- `inputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`
- `roleArn`: `str`


## ExecutionSucceededEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ExecutionSucceededEventDetailsTypeDef
```




Optional fields:
- `output`: `str`
- `outputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## ExecutionTimedOutEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ExecutionTimedOutEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## GetActivityTaskOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import GetActivityTaskOutputTypeDef
```




Optional fields:
- `taskToken`: `str`
- `input`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetExecutionHistoryOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import GetExecutionHistoryOutputTypeDef
```


Required fields:
- `events`: `List["HistoryEventTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## HistoryEventExecutionDataDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import HistoryEventExecutionDataDetailsTypeDef
```




Optional fields:
- `truncated`: `bool`


## HistoryEventTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import HistoryEventTypeDef
```


Required fields:
- `timestamp`: `datetime`
- `type`: `HistoryEventType`
- `id`: `int`



Optional fields:
- `previousEventId`: `int`
- `activityFailedEventDetails`: `"ActivityFailedEventDetailsTypeDef"`
- `activityScheduleFailedEventDetails`: `"ActivityScheduleFailedEventDetailsTypeDef"`
- `activityScheduledEventDetails`: `"ActivityScheduledEventDetailsTypeDef"`
- `activityStartedEventDetails`: `"ActivityStartedEventDetailsTypeDef"`
- `activitySucceededEventDetails`: `"ActivitySucceededEventDetailsTypeDef"`
- `activityTimedOutEventDetails`: `"ActivityTimedOutEventDetailsTypeDef"`
- `taskFailedEventDetails`: `"TaskFailedEventDetailsTypeDef"`
- `taskScheduledEventDetails`: `"TaskScheduledEventDetailsTypeDef"`
- `taskStartFailedEventDetails`: `"TaskStartFailedEventDetailsTypeDef"`
- `taskStartedEventDetails`: `"TaskStartedEventDetailsTypeDef"`
- `taskSubmitFailedEventDetails`: `"TaskSubmitFailedEventDetailsTypeDef"`
- `taskSubmittedEventDetails`: `"TaskSubmittedEventDetailsTypeDef"`
- `taskSucceededEventDetails`: `"TaskSucceededEventDetailsTypeDef"`
- `taskTimedOutEventDetails`: `"TaskTimedOutEventDetailsTypeDef"`
- `executionFailedEventDetails`: `"ExecutionFailedEventDetailsTypeDef"`
- `executionStartedEventDetails`: `"ExecutionStartedEventDetailsTypeDef"`
- `executionSucceededEventDetails`: `"ExecutionSucceededEventDetailsTypeDef"`
- `executionAbortedEventDetails`: `"ExecutionAbortedEventDetailsTypeDef"`
- `executionTimedOutEventDetails`: `"ExecutionTimedOutEventDetailsTypeDef"`
- `mapStateStartedEventDetails`: `"MapStateStartedEventDetailsTypeDef"`
- `mapIterationStartedEventDetails`: `"MapIterationEventDetailsTypeDef"`
- `mapIterationSucceededEventDetails`: `"MapIterationEventDetailsTypeDef"`
- `mapIterationFailedEventDetails`: `"MapIterationEventDetailsTypeDef"`
- `mapIterationAbortedEventDetails`: `"MapIterationEventDetailsTypeDef"`
- `lambdaFunctionFailedEventDetails`: `"LambdaFunctionFailedEventDetailsTypeDef"`
- `lambdaFunctionScheduleFailedEventDetails`: `"LambdaFunctionScheduleFailedEventDetailsTypeDef"`
- `lambdaFunctionScheduledEventDetails`: `"LambdaFunctionScheduledEventDetailsTypeDef"`
- `lambdaFunctionStartFailedEventDetails`: `"LambdaFunctionStartFailedEventDetailsTypeDef"`
- `lambdaFunctionSucceededEventDetails`: `"LambdaFunctionSucceededEventDetailsTypeDef"`
- `lambdaFunctionTimedOutEventDetails`: `"LambdaFunctionTimedOutEventDetailsTypeDef"`
- `stateEnteredEventDetails`: `"StateEnteredEventDetailsTypeDef"`
- `stateExitedEventDetails`: `"StateExitedEventDetailsTypeDef"`


## LambdaFunctionFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LambdaFunctionFailedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## LambdaFunctionScheduleFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LambdaFunctionScheduleFailedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## LambdaFunctionScheduledEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LambdaFunctionScheduledEventDetailsTypeDef
```


Required fields:
- `resource`: `str`



Optional fields:
- `input`: `str`
- `inputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`
- `timeoutInSeconds`: `int`


## LambdaFunctionStartFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LambdaFunctionStartFailedEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## LambdaFunctionSucceededEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LambdaFunctionSucceededEventDetailsTypeDef
```




Optional fields:
- `output`: `str`
- `outputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## LambdaFunctionTimedOutEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LambdaFunctionTimedOutEventDetailsTypeDef
```




Optional fields:
- `error`: `str`
- `cause`: `str`


## ListActivitiesOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ListActivitiesOutputTypeDef
```


Required fields:
- `activities`: `List["ActivityListItemTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListExecutionsOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ListExecutionsOutputTypeDef
```


Required fields:
- `executions`: `List["ExecutionListItemTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStateMachinesOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ListStateMachinesOutputTypeDef
```


Required fields:
- `stateMachines`: `List["StateMachineListItemTypeDef"]`



Optional fields:
- `nextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## LogDestinationTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LogDestinationTypeDef
```




Optional fields:
- `cloudWatchLogsLogGroup`: `"CloudWatchLogsLogGroupTypeDef"`


## LoggingConfigurationTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import LoggingConfigurationTypeDef
```




Optional fields:
- `level`: `LogLevel`
- `includeExecutionData`: `bool`
- `destinations`: `List["LogDestinationTypeDef"]`


## MapIterationEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import MapIterationEventDetailsTypeDef
```




Optional fields:
- `name`: `str`
- `index`: `int`


## MapStateStartedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import MapStateStartedEventDetailsTypeDef
```




Optional fields:
- `length`: `int`


## PaginatorConfigTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResponseMetadata

```python
from mypy_boto3_stepfunctions.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## StartExecutionOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import StartExecutionOutputTypeDef
```


Required fields:
- `executionArn`: `str`
- `startDate`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## StartSyncExecutionOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import StartSyncExecutionOutputTypeDef
```


Required fields:
- `executionArn`: `str`
- `startDate`: `datetime`
- `stopDate`: `datetime`
- `status`: `SyncExecutionStatus`



Optional fields:
- `stateMachineArn`: `str`
- `name`: `str`
- `error`: `str`
- `cause`: `str`
- `input`: `str`
- `inputDetails`: `"CloudWatchEventsExecutionDataDetailsTypeDef"`
- `output`: `str`
- `outputDetails`: `"CloudWatchEventsExecutionDataDetailsTypeDef"`
- `traceHeader`: `str`
- `billingDetails`: `"BillingDetailsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## StateEnteredEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import StateEnteredEventDetailsTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `input`: `str`
- `inputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## StateExitedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import StateExitedEventDetailsTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `output`: `str`
- `outputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## StateMachineListItemTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import StateMachineListItemTypeDef
```


Required fields:
- `stateMachineArn`: `str`
- `name`: `str`
- `type`: `StateMachineType`
- `creationDate`: `datetime`




## StopExecutionOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import StopExecutionOutputTypeDef
```


Required fields:
- `stopDate`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`


## TagTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TagTypeDef
```




Optional fields:
- `key`: `str`
- `value`: `str`


## TaskFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskFailedEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`



Optional fields:
- `error`: `str`
- `cause`: `str`


## TaskScheduledEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskScheduledEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`
- `region`: `str`
- `parameters`: `str`



Optional fields:
- `timeoutInSeconds`: `int`
- `heartbeatInSeconds`: `int`


## TaskStartFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskStartFailedEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`



Optional fields:
- `error`: `str`
- `cause`: `str`


## TaskStartedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskStartedEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`




## TaskSubmitFailedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskSubmitFailedEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`



Optional fields:
- `error`: `str`
- `cause`: `str`


## TaskSubmittedEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskSubmittedEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`



Optional fields:
- `output`: `str`
- `outputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## TaskSucceededEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskSucceededEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`



Optional fields:
- `output`: `str`
- `outputDetails`: `"HistoryEventExecutionDataDetailsTypeDef"`


## TaskTimedOutEventDetailsTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TaskTimedOutEventDetailsTypeDef
```


Required fields:
- `resourceType`: `str`
- `resource`: `str`



Optional fields:
- `error`: `str`
- `cause`: `str`


## TracingConfigurationTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import TracingConfigurationTypeDef
```




Optional fields:
- `enabled`: `bool`


## UpdateStateMachineOutputTypeDef

```python
from mypy_boto3_stepfunctions.type_defs import UpdateStateMachineOutputTypeDef
```


Required fields:
- `updateDate`: `datetime`



Optional fields:
- `ResponseMetadata`: `"ResponseMetadata"`

