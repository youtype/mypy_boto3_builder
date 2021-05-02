# Structures for boto3 EventBridge module

> [Index](../index.md) > [EventBridge](./index.md) > Structures

Auto-generated documentation for [EventBridge](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge)
type annotations stubs module [mypy_boto3_events](https://pypi.org/project/mypy-boto3-events/).

- [Structures for boto3 EventBridge module](#structures-for-boto3-eventbridge-module)
  - [ApiDestinationTypeDef](#apidestinationtypedef)
  - [ArchiveTypeDef](#archivetypedef)
  - [AwsVpcConfigurationTypeDef](#awsvpcconfigurationtypedef)
  - [BatchArrayPropertiesTypeDef](#batcharraypropertiestypedef)
  - [BatchParametersTypeDef](#batchparameterstypedef)
  - [BatchRetryStrategyTypeDef](#batchretrystrategytypedef)
  - [ConnectionApiKeyAuthResponseParametersTypeDef](#connectionapikeyauthresponseparameterstypedef)
  - [ConnectionAuthResponseParametersTypeDef](#connectionauthresponseparameterstypedef)
  - [ConnectionBasicAuthResponseParametersTypeDef](#connectionbasicauthresponseparameterstypedef)
  - [ConnectionBodyParameterTypeDef](#connectionbodyparametertypedef)
  - [ConnectionHeaderParameterTypeDef](#connectionheaderparametertypedef)
  - [ConnectionHttpParametersTypeDef](#connectionhttpparameterstypedef)
  - [ConnectionOAuthClientResponseParametersTypeDef](#connectionoauthclientresponseparameterstypedef)
  - [ConnectionOAuthResponseParametersTypeDef](#connectionoauthresponseparameterstypedef)
  - [ConnectionQueryStringParameterTypeDef](#connectionquerystringparametertypedef)
  - [ConnectionTypeDef](#connectiontypedef)
  - [CreateConnectionApiKeyAuthRequestParametersTypeDef](#createconnectionapikeyauthrequestparameterstypedef)
  - [CreateConnectionBasicAuthRequestParametersTypeDef](#createconnectionbasicauthrequestparameterstypedef)
  - [CreateConnectionOAuthClientRequestParametersTypeDef](#createconnectionoauthclientrequestparameterstypedef)
  - [CreateConnectionOAuthRequestParametersTypeDef](#createconnectionoauthrequestparameterstypedef)
  - [DeadLetterConfigTypeDef](#deadletterconfigtypedef)
  - [EcsParametersTypeDef](#ecsparameterstypedef)
  - [EventBusTypeDef](#eventbustypedef)
  - [EventSourceTypeDef](#eventsourcetypedef)
  - [HttpParametersTypeDef](#httpparameterstypedef)
  - [InputTransformerTypeDef](#inputtransformertypedef)
  - [KinesisParametersTypeDef](#kinesisparameterstypedef)
  - [NetworkConfigurationTypeDef](#networkconfigurationtypedef)
  - [PartnerEventSourceAccountTypeDef](#partnereventsourceaccounttypedef)
  - [PartnerEventSourceTypeDef](#partnereventsourcetypedef)
  - [PutEventsResultEntryTypeDef](#puteventsresultentrytypedef)
  - [PutPartnerEventsResultEntryTypeDef](#putpartnereventsresultentrytypedef)
  - [PutTargetsResultEntryTypeDef](#puttargetsresultentrytypedef)
  - [RedshiftDataParametersTypeDef](#redshiftdataparameterstypedef)
  - [RemoveTargetsResultEntryTypeDef](#removetargetsresultentrytypedef)
  - [ReplayDestinationTypeDef](#replaydestinationtypedef)
  - [ReplayTypeDef](#replaytypedef)
  - [RetryPolicyTypeDef](#retrypolicytypedef)
  - [RuleTypeDef](#ruletypedef)
  - [RunCommandParametersTypeDef](#runcommandparameterstypedef)
  - [RunCommandTargetTypeDef](#runcommandtargettypedef)
  - [SageMakerPipelineParameterTypeDef](#sagemakerpipelineparametertypedef)
  - [SageMakerPipelineParametersTypeDef](#sagemakerpipelineparameterstypedef)
  - [SqsParametersTypeDef](#sqsparameterstypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetTypeDef](#targettypedef)
  - [UpdateConnectionApiKeyAuthRequestParametersTypeDef](#updateconnectionapikeyauthrequestparameterstypedef)
  - [UpdateConnectionBasicAuthRequestParametersTypeDef](#updateconnectionbasicauthrequestparameterstypedef)
  - [UpdateConnectionOAuthClientRequestParametersTypeDef](#updateconnectionoauthclientrequestparameterstypedef)
  - [UpdateConnectionOAuthRequestParametersTypeDef](#updateconnectionoauthrequestparameterstypedef)
  - [CancelReplayResponseTypeDef](#cancelreplayresponsetypedef)
  - [ConditionTypeDef](#conditiontypedef)
  - [CreateApiDestinationResponseTypeDef](#createapidestinationresponsetypedef)
  - [CreateArchiveResponseTypeDef](#createarchiveresponsetypedef)
  - [CreateConnectionAuthRequestParametersTypeDef](#createconnectionauthrequestparameterstypedef)
  - [CreateConnectionResponseTypeDef](#createconnectionresponsetypedef)
  - [CreateEventBusResponseTypeDef](#createeventbusresponsetypedef)
  - [CreatePartnerEventSourceResponseTypeDef](#createpartnereventsourceresponsetypedef)
  - [DeauthorizeConnectionResponseTypeDef](#deauthorizeconnectionresponsetypedef)
  - [DeleteConnectionResponseTypeDef](#deleteconnectionresponsetypedef)
  - [DescribeApiDestinationResponseTypeDef](#describeapidestinationresponsetypedef)
  - [DescribeArchiveResponseTypeDef](#describearchiveresponsetypedef)
  - [DescribeConnectionResponseTypeDef](#describeconnectionresponsetypedef)
  - [DescribeEventBusResponseTypeDef](#describeeventbusresponsetypedef)
  - [DescribeEventSourceResponseTypeDef](#describeeventsourceresponsetypedef)
  - [DescribePartnerEventSourceResponseTypeDef](#describepartnereventsourceresponsetypedef)
  - [DescribeReplayResponseTypeDef](#describereplayresponsetypedef)
  - [DescribeRuleResponseTypeDef](#describeruleresponsetypedef)
  - [ListApiDestinationsResponseTypeDef](#listapidestinationsresponsetypedef)
  - [ListArchivesResponseTypeDef](#listarchivesresponsetypedef)
  - [ListConnectionsResponseTypeDef](#listconnectionsresponsetypedef)
  - [ListEventBusesResponseTypeDef](#listeventbusesresponsetypedef)
  - [ListEventSourcesResponseTypeDef](#listeventsourcesresponsetypedef)
  - [ListPartnerEventSourceAccountsResponseTypeDef](#listpartnereventsourceaccountsresponsetypedef)
  - [ListPartnerEventSourcesResponseTypeDef](#listpartnereventsourcesresponsetypedef)
  - [ListReplaysResponseTypeDef](#listreplaysresponsetypedef)
  - [ListRuleNamesByTargetResponseTypeDef](#listrulenamesbytargetresponsetypedef)
  - [ListRulesResponseTypeDef](#listrulesresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTargetsByRuleResponseTypeDef](#listtargetsbyruleresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PutEventsRequestEntryTypeDef](#puteventsrequestentrytypedef)
  - [PutEventsResponseTypeDef](#puteventsresponsetypedef)
  - [PutPartnerEventsRequestEntryTypeDef](#putpartnereventsrequestentrytypedef)
  - [PutPartnerEventsResponseTypeDef](#putpartnereventsresponsetypedef)
  - [PutRuleResponseTypeDef](#putruleresponsetypedef)
  - [PutTargetsResponseTypeDef](#puttargetsresponsetypedef)
  - [RemoveTargetsResponseTypeDef](#removetargetsresponsetypedef)
  - [StartReplayResponseTypeDef](#startreplayresponsetypedef)
  - [TestEventPatternResponseTypeDef](#testeventpatternresponsetypedef)
  - [UpdateApiDestinationResponseTypeDef](#updateapidestinationresponsetypedef)
  - [UpdateArchiveResponseTypeDef](#updatearchiveresponsetypedef)
  - [UpdateConnectionAuthRequestParametersTypeDef](#updateconnectionauthrequestparameterstypedef)
  - [UpdateConnectionResponseTypeDef](#updateconnectionresponsetypedef)

## ApiDestinationTypeDef

```python
from mypy_boto3_events.type_defs import ApiDestinationTypeDef
```




Optional fields:
- `ApiDestinationArn`: `str`
- `Name`: `str`
- `ApiDestinationState`: `ApiDestinationState`
- `ConnectionArn`: `str`
- `InvocationEndpoint`: `str`
- `HttpMethod`: `ApiDestinationHttpMethod`
- `InvocationRateLimitPerSecond`: `int`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## ArchiveTypeDef

```python
from mypy_boto3_events.type_defs import ArchiveTypeDef
```




Optional fields:
- `ArchiveName`: `str`
- `EventSourceArn`: `str`
- `State`: `ArchiveState`
- `StateReason`: `str`
- `RetentionDays`: `int`
- `SizeBytes`: `int`
- `EventCount`: `int`
- `CreationTime`: `datetime`


## AwsVpcConfigurationTypeDef

```python
from mypy_boto3_events.type_defs import AwsVpcConfigurationTypeDef
```


Required fields:
- `Subnets`: `List[str]`



Optional fields:
- `SecurityGroups`: `List[str]`
- `AssignPublicIp`: `AssignPublicIp`


## BatchArrayPropertiesTypeDef

```python
from mypy_boto3_events.type_defs import BatchArrayPropertiesTypeDef
```




Optional fields:
- `Size`: `int`


## BatchParametersTypeDef

```python
from mypy_boto3_events.type_defs import BatchParametersTypeDef
```


Required fields:
- `JobDefinition`: `str`
- `JobName`: `str`



Optional fields:
- `ArrayProperties`: `"BatchArrayPropertiesTypeDef"`
- `RetryStrategy`: `"BatchRetryStrategyTypeDef"`


## BatchRetryStrategyTypeDef

```python
from mypy_boto3_events.type_defs import BatchRetryStrategyTypeDef
```




Optional fields:
- `Attempts`: `int`


## ConnectionApiKeyAuthResponseParametersTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionApiKeyAuthResponseParametersTypeDef
```




Optional fields:
- `ApiKeyName`: `str`


## ConnectionAuthResponseParametersTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionAuthResponseParametersTypeDef
```




Optional fields:
- `BasicAuthParameters`: `"ConnectionBasicAuthResponseParametersTypeDef"`
- `OAuthParameters`: `"ConnectionOAuthResponseParametersTypeDef"`
- `ApiKeyAuthParameters`: `"ConnectionApiKeyAuthResponseParametersTypeDef"`
- `InvocationHttpParameters`: `"ConnectionHttpParametersTypeDef"`


## ConnectionBasicAuthResponseParametersTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionBasicAuthResponseParametersTypeDef
```




Optional fields:
- `Username`: `str`


## ConnectionBodyParameterTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionBodyParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `IsValueSecret`: `bool`


## ConnectionHeaderParameterTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionHeaderParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `IsValueSecret`: `bool`


## ConnectionHttpParametersTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionHttpParametersTypeDef
```




Optional fields:
- `HeaderParameters`: `List["ConnectionHeaderParameterTypeDef"]`
- `QueryStringParameters`: `List["ConnectionQueryStringParameterTypeDef"]`
- `BodyParameters`: `List["ConnectionBodyParameterTypeDef"]`


## ConnectionOAuthClientResponseParametersTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionOAuthClientResponseParametersTypeDef
```




Optional fields:
- `ClientID`: `str`


## ConnectionOAuthResponseParametersTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionOAuthResponseParametersTypeDef
```




Optional fields:
- `ClientParameters`: `"ConnectionOAuthClientResponseParametersTypeDef"`
- `AuthorizationEndpoint`: `str`
- `HttpMethod`: `ConnectionOAuthHttpMethod`
- `OAuthHttpParameters`: `"ConnectionHttpParametersTypeDef"`


## ConnectionQueryStringParameterTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionQueryStringParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `IsValueSecret`: `bool`


## ConnectionTypeDef

```python
from mypy_boto3_events.type_defs import ConnectionTypeDef
```




Optional fields:
- `ConnectionArn`: `str`
- `Name`: `str`
- `ConnectionState`: `ConnectionState`
- `StateReason`: `str`
- `AuthorizationType`: `ConnectionAuthorizationType`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastAuthorizedTime`: `datetime`


## CreateConnectionApiKeyAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import CreateConnectionApiKeyAuthRequestParametersTypeDef
```


Required fields:
- `ApiKeyName`: `str`
- `ApiKeyValue`: `str`




## CreateConnectionBasicAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import CreateConnectionBasicAuthRequestParametersTypeDef
```


Required fields:
- `Username`: `str`
- `Password`: `str`




## CreateConnectionOAuthClientRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import CreateConnectionOAuthClientRequestParametersTypeDef
```


Required fields:
- `ClientID`: `str`
- `ClientSecret`: `str`




## CreateConnectionOAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import CreateConnectionOAuthRequestParametersTypeDef
```


Required fields:
- `ClientParameters`: `"CreateConnectionOAuthClientRequestParametersTypeDef"`
- `AuthorizationEndpoint`: `str`
- `HttpMethod`: `ConnectionOAuthHttpMethod`



Optional fields:
- `OAuthHttpParameters`: `"ConnectionHttpParametersTypeDef"`


## DeadLetterConfigTypeDef

```python
from mypy_boto3_events.type_defs import DeadLetterConfigTypeDef
```




Optional fields:
- `Arn`: `str`


## EcsParametersTypeDef

```python
from mypy_boto3_events.type_defs import EcsParametersTypeDef
```


Required fields:
- `TaskDefinitionArn`: `str`



Optional fields:
- `TaskCount`: `int`
- `LaunchType`: `LaunchType`
- `NetworkConfiguration`: `"NetworkConfigurationTypeDef"`
- `PlatformVersion`: `str`
- `Group`: `str`


## EventBusTypeDef

```python
from mypy_boto3_events.type_defs import EventBusTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `Policy`: `str`


## EventSourceTypeDef

```python
from mypy_boto3_events.type_defs import EventSourceTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedBy`: `str`
- `CreationTime`: `datetime`
- `ExpirationTime`: `datetime`
- `Name`: `str`
- `State`: `EventSourceState`


## HttpParametersTypeDef

```python
from mypy_boto3_events.type_defs import HttpParametersTypeDef
```




Optional fields:
- `PathParameterValues`: `List[str]`
- `HeaderParameters`: `Dict[str, str]`
- `QueryStringParameters`: `Dict[str, str]`


## InputTransformerTypeDef

```python
from mypy_boto3_events.type_defs import InputTransformerTypeDef
```


Required fields:
- `InputTemplate`: `str`



Optional fields:
- `InputPathsMap`: `Dict[str, str]`


## KinesisParametersTypeDef

```python
from mypy_boto3_events.type_defs import KinesisParametersTypeDef
```


Required fields:
- `PartitionKeyPath`: `str`




## NetworkConfigurationTypeDef

```python
from mypy_boto3_events.type_defs import NetworkConfigurationTypeDef
```




Optional fields:
- `awsvpcConfiguration`: `"AwsVpcConfigurationTypeDef"`


## PartnerEventSourceAccountTypeDef

```python
from mypy_boto3_events.type_defs import PartnerEventSourceAccountTypeDef
```




Optional fields:
- `Account`: `str`
- `CreationTime`: `datetime`
- `ExpirationTime`: `datetime`
- `State`: `EventSourceState`


## PartnerEventSourceTypeDef

```python
from mypy_boto3_events.type_defs import PartnerEventSourceTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## PutEventsResultEntryTypeDef

```python
from mypy_boto3_events.type_defs import PutEventsResultEntryTypeDef
```




Optional fields:
- `EventId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## PutPartnerEventsResultEntryTypeDef

```python
from mypy_boto3_events.type_defs import PutPartnerEventsResultEntryTypeDef
```




Optional fields:
- `EventId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## PutTargetsResultEntryTypeDef

```python
from mypy_boto3_events.type_defs import PutTargetsResultEntryTypeDef
```




Optional fields:
- `TargetId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## RedshiftDataParametersTypeDef

```python
from mypy_boto3_events.type_defs import RedshiftDataParametersTypeDef
```


Required fields:
- `Database`: `str`
- `Sql`: `str`



Optional fields:
- `SecretManagerArn`: `str`
- `DbUser`: `str`
- `StatementName`: `str`
- `WithEvent`: `bool`


## RemoveTargetsResultEntryTypeDef

```python
from mypy_boto3_events.type_defs import RemoveTargetsResultEntryTypeDef
```




Optional fields:
- `TargetId`: `str`
- `ErrorCode`: `str`
- `ErrorMessage`: `str`


## ReplayDestinationTypeDef

```python
from mypy_boto3_events.type_defs import ReplayDestinationTypeDef
```


Required fields:
- `Arn`: `str`



Optional fields:
- `FilterArns`: `List[str]`


## ReplayTypeDef

```python
from mypy_boto3_events.type_defs import ReplayTypeDef
```




Optional fields:
- `ReplayName`: `str`
- `EventSourceArn`: `str`
- `State`: `ReplayState`
- `StateReason`: `str`
- `EventStartTime`: `datetime`
- `EventEndTime`: `datetime`
- `EventLastReplayedTime`: `datetime`
- `ReplayStartTime`: `datetime`
- `ReplayEndTime`: `datetime`


## RetryPolicyTypeDef

```python
from mypy_boto3_events.type_defs import RetryPolicyTypeDef
```




Optional fields:
- `MaximumRetryAttempts`: `int`
- `MaximumEventAgeInSeconds`: `int`


## RuleTypeDef

```python
from mypy_boto3_events.type_defs import RuleTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `EventPattern`: `str`
- `State`: `RuleState`
- `Description`: `str`
- `ScheduleExpression`: `str`
- `RoleArn`: `str`
- `ManagedBy`: `str`
- `EventBusName`: `str`


## RunCommandParametersTypeDef

```python
from mypy_boto3_events.type_defs import RunCommandParametersTypeDef
```


Required fields:
- `RunCommandTargets`: `List["RunCommandTargetTypeDef"]`




## RunCommandTargetTypeDef

```python
from mypy_boto3_events.type_defs import RunCommandTargetTypeDef
```


Required fields:
- `Key`: `str`
- `Values`: `List[str]`




## SageMakerPipelineParameterTypeDef

```python
from mypy_boto3_events.type_defs import SageMakerPipelineParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## SageMakerPipelineParametersTypeDef

```python
from mypy_boto3_events.type_defs import SageMakerPipelineParametersTypeDef
```




Optional fields:
- `PipelineParameterList`: `List["SageMakerPipelineParameterTypeDef"]`


## SqsParametersTypeDef

```python
from mypy_boto3_events.type_defs import SqsParametersTypeDef
```




Optional fields:
- `MessageGroupId`: `str`


## TagTypeDef

```python
from mypy_boto3_events.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TargetTypeDef

```python
from mypy_boto3_events.type_defs import TargetTypeDef
```


Required fields:
- `Id`: `str`
- `Arn`: `str`



Optional fields:
- `RoleArn`: `str`
- `Input`: `str`
- `InputPath`: `str`
- `InputTransformer`: `"InputTransformerTypeDef"`
- `KinesisParameters`: `"KinesisParametersTypeDef"`
- `RunCommandParameters`: `"RunCommandParametersTypeDef"`
- `EcsParameters`: `"EcsParametersTypeDef"`
- `BatchParameters`: `"BatchParametersTypeDef"`
- `SqsParameters`: `"SqsParametersTypeDef"`
- `HttpParameters`: `"HttpParametersTypeDef"`
- `RedshiftDataParameters`: `"RedshiftDataParametersTypeDef"`
- `SageMakerPipelineParameters`: `"SageMakerPipelineParametersTypeDef"`
- `DeadLetterConfig`: `"DeadLetterConfigTypeDef"`
- `RetryPolicy`: `"RetryPolicyTypeDef"`


## UpdateConnectionApiKeyAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import UpdateConnectionApiKeyAuthRequestParametersTypeDef
```




Optional fields:
- `ApiKeyName`: `str`
- `ApiKeyValue`: `str`


## UpdateConnectionBasicAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import UpdateConnectionBasicAuthRequestParametersTypeDef
```




Optional fields:
- `Username`: `str`
- `Password`: `str`


## UpdateConnectionOAuthClientRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import UpdateConnectionOAuthClientRequestParametersTypeDef
```




Optional fields:
- `ClientID`: `str`
- `ClientSecret`: `str`


## UpdateConnectionOAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import UpdateConnectionOAuthRequestParametersTypeDef
```




Optional fields:
- `ClientParameters`: `"UpdateConnectionOAuthClientRequestParametersTypeDef"`
- `AuthorizationEndpoint`: `str`
- `HttpMethod`: `ConnectionOAuthHttpMethod`
- `OAuthHttpParameters`: `"ConnectionHttpParametersTypeDef"`


## CancelReplayResponseTypeDef

```python
from mypy_boto3_events.type_defs import CancelReplayResponseTypeDef
```




Optional fields:
- `ReplayArn`: `str`
- `State`: `ReplayState`
- `StateReason`: `str`


## ConditionTypeDef

```python
from mypy_boto3_events.type_defs import ConditionTypeDef
```


Required fields:
- `Type`: `str`
- `Key`: `str`
- `Value`: `str`




## CreateApiDestinationResponseTypeDef

```python
from mypy_boto3_events.type_defs import CreateApiDestinationResponseTypeDef
```




Optional fields:
- `ApiDestinationArn`: `str`
- `ApiDestinationState`: `ApiDestinationState`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## CreateArchiveResponseTypeDef

```python
from mypy_boto3_events.type_defs import CreateArchiveResponseTypeDef
```




Optional fields:
- `ArchiveArn`: `str`
- `State`: `ArchiveState`
- `StateReason`: `str`
- `CreationTime`: `datetime`


## CreateConnectionAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import CreateConnectionAuthRequestParametersTypeDef
```




Optional fields:
- `BasicAuthParameters`: `"CreateConnectionBasicAuthRequestParametersTypeDef"`
- `OAuthParameters`: `"CreateConnectionOAuthRequestParametersTypeDef"`
- `ApiKeyAuthParameters`: `"CreateConnectionApiKeyAuthRequestParametersTypeDef"`
- `InvocationHttpParameters`: `"ConnectionHttpParametersTypeDef"`


## CreateConnectionResponseTypeDef

```python
from mypy_boto3_events.type_defs import CreateConnectionResponseTypeDef
```




Optional fields:
- `ConnectionArn`: `str`
- `ConnectionState`: `ConnectionState`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## CreateEventBusResponseTypeDef

```python
from mypy_boto3_events.type_defs import CreateEventBusResponseTypeDef
```




Optional fields:
- `EventBusArn`: `str`


## CreatePartnerEventSourceResponseTypeDef

```python
from mypy_boto3_events.type_defs import CreatePartnerEventSourceResponseTypeDef
```




Optional fields:
- `EventSourceArn`: `str`


## DeauthorizeConnectionResponseTypeDef

```python
from mypy_boto3_events.type_defs import DeauthorizeConnectionResponseTypeDef
```




Optional fields:
- `ConnectionArn`: `str`
- `ConnectionState`: `ConnectionState`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastAuthorizedTime`: `datetime`


## DeleteConnectionResponseTypeDef

```python
from mypy_boto3_events.type_defs import DeleteConnectionResponseTypeDef
```




Optional fields:
- `ConnectionArn`: `str`
- `ConnectionState`: `ConnectionState`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastAuthorizedTime`: `datetime`


## DescribeApiDestinationResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeApiDestinationResponseTypeDef
```




Optional fields:
- `ApiDestinationArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `ApiDestinationState`: `ApiDestinationState`
- `ConnectionArn`: `str`
- `InvocationEndpoint`: `str`
- `HttpMethod`: `ApiDestinationHttpMethod`
- `InvocationRateLimitPerSecond`: `int`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## DescribeArchiveResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeArchiveResponseTypeDef
```




Optional fields:
- `ArchiveArn`: `str`
- `ArchiveName`: `str`
- `EventSourceArn`: `str`
- `Description`: `str`
- `EventPattern`: `str`
- `State`: `ArchiveState`
- `StateReason`: `str`
- `RetentionDays`: `int`
- `SizeBytes`: `int`
- `EventCount`: `int`
- `CreationTime`: `datetime`


## DescribeConnectionResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeConnectionResponseTypeDef
```




Optional fields:
- `ConnectionArn`: `str`
- `Name`: `str`
- `Description`: `str`
- `ConnectionState`: `ConnectionState`
- `StateReason`: `str`
- `AuthorizationType`: `ConnectionAuthorizationType`
- `SecretArn`: `str`
- `AuthParameters`: `"ConnectionAuthResponseParametersTypeDef"`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastAuthorizedTime`: `datetime`


## DescribeEventBusResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeEventBusResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `Policy`: `str`


## DescribeEventSourceResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeEventSourceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedBy`: `str`
- `CreationTime`: `datetime`
- `ExpirationTime`: `datetime`
- `Name`: `str`
- `State`: `EventSourceState`


## DescribePartnerEventSourceResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribePartnerEventSourceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `Name`: `str`


## DescribeReplayResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeReplayResponseTypeDef
```




Optional fields:
- `ReplayName`: `str`
- `ReplayArn`: `str`
- `Description`: `str`
- `State`: `ReplayState`
- `StateReason`: `str`
- `EventSourceArn`: `str`
- `Destination`: `"ReplayDestinationTypeDef"`
- `EventStartTime`: `datetime`
- `EventEndTime`: `datetime`
- `EventLastReplayedTime`: `datetime`
- `ReplayStartTime`: `datetime`
- `ReplayEndTime`: `datetime`


## DescribeRuleResponseTypeDef

```python
from mypy_boto3_events.type_defs import DescribeRuleResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `EventPattern`: `str`
- `ScheduleExpression`: `str`
- `State`: `RuleState`
- `Description`: `str`
- `RoleArn`: `str`
- `ManagedBy`: `str`
- `EventBusName`: `str`
- `CreatedBy`: `str`


## ListApiDestinationsResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListApiDestinationsResponseTypeDef
```




Optional fields:
- `ApiDestinations`: `List["ApiDestinationTypeDef"]`
- `NextToken`: `str`


## ListArchivesResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListArchivesResponseTypeDef
```




Optional fields:
- `Archives`: `List["ArchiveTypeDef"]`
- `NextToken`: `str`


## ListConnectionsResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListConnectionsResponseTypeDef
```




Optional fields:
- `Connections`: `List["ConnectionTypeDef"]`
- `NextToken`: `str`


## ListEventBusesResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListEventBusesResponseTypeDef
```




Optional fields:
- `EventBuses`: `List["EventBusTypeDef"]`
- `NextToken`: `str`


## ListEventSourcesResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListEventSourcesResponseTypeDef
```




Optional fields:
- `EventSources`: `List["EventSourceTypeDef"]`
- `NextToken`: `str`


## ListPartnerEventSourceAccountsResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListPartnerEventSourceAccountsResponseTypeDef
```




Optional fields:
- `PartnerEventSourceAccounts`: `List["PartnerEventSourceAccountTypeDef"]`
- `NextToken`: `str`


## ListPartnerEventSourcesResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListPartnerEventSourcesResponseTypeDef
```




Optional fields:
- `PartnerEventSources`: `List["PartnerEventSourceTypeDef"]`
- `NextToken`: `str`


## ListReplaysResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListReplaysResponseTypeDef
```




Optional fields:
- `Replays`: `List["ReplayTypeDef"]`
- `NextToken`: `str`


## ListRuleNamesByTargetResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListRuleNamesByTargetResponseTypeDef
```




Optional fields:
- `RuleNames`: `List[str]`
- `NextToken`: `str`


## ListRulesResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListRulesResponseTypeDef
```




Optional fields:
- `Rules`: `List["RuleTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListTargetsByRuleResponseTypeDef

```python
from mypy_boto3_events.type_defs import ListTargetsByRuleResponseTypeDef
```




Optional fields:
- `Targets`: `List["TargetTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_events.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PutEventsRequestEntryTypeDef

```python
from mypy_boto3_events.type_defs import PutEventsRequestEntryTypeDef
```




Optional fields:
- `Time`: `datetime`
- `Source`: `str`
- `Resources`: `List[str]`
- `DetailType`: `str`
- `Detail`: `str`
- `EventBusName`: `str`
- `TraceHeader`: `str`


## PutEventsResponseTypeDef

```python
from mypy_boto3_events.type_defs import PutEventsResponseTypeDef
```




Optional fields:
- `FailedEntryCount`: `int`
- `Entries`: `List["PutEventsResultEntryTypeDef"]`


## PutPartnerEventsRequestEntryTypeDef

```python
from mypy_boto3_events.type_defs import PutPartnerEventsRequestEntryTypeDef
```




Optional fields:
- `Time`: `datetime`
- `Source`: `str`
- `Resources`: `List[str]`
- `DetailType`: `str`
- `Detail`: `str`


## PutPartnerEventsResponseTypeDef

```python
from mypy_boto3_events.type_defs import PutPartnerEventsResponseTypeDef
```




Optional fields:
- `FailedEntryCount`: `int`
- `Entries`: `List["PutPartnerEventsResultEntryTypeDef"]`


## PutRuleResponseTypeDef

```python
from mypy_boto3_events.type_defs import PutRuleResponseTypeDef
```




Optional fields:
- `RuleArn`: `str`


## PutTargetsResponseTypeDef

```python
from mypy_boto3_events.type_defs import PutTargetsResponseTypeDef
```




Optional fields:
- `FailedEntryCount`: `int`
- `FailedEntries`: `List["PutTargetsResultEntryTypeDef"]`


## RemoveTargetsResponseTypeDef

```python
from mypy_boto3_events.type_defs import RemoveTargetsResponseTypeDef
```




Optional fields:
- `FailedEntryCount`: `int`
- `FailedEntries`: `List["RemoveTargetsResultEntryTypeDef"]`


## StartReplayResponseTypeDef

```python
from mypy_boto3_events.type_defs import StartReplayResponseTypeDef
```




Optional fields:
- `ReplayArn`: `str`
- `State`: `ReplayState`
- `StateReason`: `str`
- `ReplayStartTime`: `datetime`


## TestEventPatternResponseTypeDef

```python
from mypy_boto3_events.type_defs import TestEventPatternResponseTypeDef
```




Optional fields:
- `Result`: `bool`


## UpdateApiDestinationResponseTypeDef

```python
from mypy_boto3_events.type_defs import UpdateApiDestinationResponseTypeDef
```




Optional fields:
- `ApiDestinationArn`: `str`
- `ApiDestinationState`: `ApiDestinationState`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`


## UpdateArchiveResponseTypeDef

```python
from mypy_boto3_events.type_defs import UpdateArchiveResponseTypeDef
```




Optional fields:
- `ArchiveArn`: `str`
- `State`: `ArchiveState`
- `StateReason`: `str`
- `CreationTime`: `datetime`


## UpdateConnectionAuthRequestParametersTypeDef

```python
from mypy_boto3_events.type_defs import UpdateConnectionAuthRequestParametersTypeDef
```




Optional fields:
- `BasicAuthParameters`: `"UpdateConnectionBasicAuthRequestParametersTypeDef"`
- `OAuthParameters`: `"UpdateConnectionOAuthRequestParametersTypeDef"`
- `ApiKeyAuthParameters`: `"UpdateConnectionApiKeyAuthRequestParametersTypeDef"`
- `InvocationHttpParameters`: `"ConnectionHttpParametersTypeDef"`


## UpdateConnectionResponseTypeDef

```python
from mypy_boto3_events.type_defs import UpdateConnectionResponseTypeDef
```




Optional fields:
- `ConnectionArn`: `str`
- `ConnectionState`: `ConnectionState`
- `CreationTime`: `datetime`
- `LastModifiedTime`: `datetime`
- `LastAuthorizedTime`: `datetime`

