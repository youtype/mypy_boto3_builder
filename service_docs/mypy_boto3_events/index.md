# Type annotations for boto3 EventBridge module

> [Index](../index.md) > EventBridge

Auto-generated documentation for [EventBridge](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html#EventBridge)
type annotations stubs module [mypy_boto3_events](https://pypi.org/project/mypy-boto3-events/).

```bash
pip install mypy-boto3-events
```

- [Type annotations for boto3 EventBridge module](#type-annotations-for-boto3-eventbridge-module)
  - [EventBridgeClient](#eventbridgeclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## EventBridgeClient

Type annotations for  `boto3.client("events")` as [EventBridgeClient](./client.md)

Can be used directly:

```python
from mypy_boto3_events.client import EventBridgeClient
```


EventBridgeClient [exceptions](./client.md#exceptions)



### Methods
- [activate_event_source](./client.md#activate-event-source)
- [can_paginate](./client.md#can-paginate)
- [cancel_replay](./client.md#cancel-replay)
- [create_api_destination](./client.md#create-api-destination)
- [create_archive](./client.md#create-archive)
- [create_connection](./client.md#create-connection)
- [create_event_bus](./client.md#create-event-bus)
- [create_partner_event_source](./client.md#create-partner-event-source)
- [deactivate_event_source](./client.md#deactivate-event-source)
- [deauthorize_connection](./client.md#deauthorize-connection)
- [delete_api_destination](./client.md#delete-api-destination)
- [delete_archive](./client.md#delete-archive)
- [delete_connection](./client.md#delete-connection)
- [delete_event_bus](./client.md#delete-event-bus)
- [delete_partner_event_source](./client.md#delete-partner-event-source)
- [delete_rule](./client.md#delete-rule)
- [describe_api_destination](./client.md#describe-api-destination)
- [describe_archive](./client.md#describe-archive)
- [describe_connection](./client.md#describe-connection)
- [describe_event_bus](./client.md#describe-event-bus)
- [describe_event_source](./client.md#describe-event-source)
- [describe_partner_event_source](./client.md#describe-partner-event-source)
- [describe_replay](./client.md#describe-replay)
- [describe_rule](./client.md#describe-rule)
- [disable_rule](./client.md#disable-rule)
- [enable_rule](./client.md#enable-rule)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_api_destinations](./client.md#list-api-destinations)
- [list_archives](./client.md#list-archives)
- [list_connections](./client.md#list-connections)
- [list_event_buses](./client.md#list-event-buses)
- [list_event_sources](./client.md#list-event-sources)
- [list_partner_event_source_accounts](./client.md#list-partner-event-source-accounts)
- [list_partner_event_sources](./client.md#list-partner-event-sources)
- [list_replays](./client.md#list-replays)
- [list_rule_names_by_target](./client.md#list-rule-names-by-target)
- [list_rules](./client.md#list-rules)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_targets_by_rule](./client.md#list-targets-by-rule)
- [put_events](./client.md#put-events)
- [put_partner_events](./client.md#put-partner-events)
- [put_permission](./client.md#put-permission)
- [put_rule](./client.md#put-rule)
- [put_targets](./client.md#put-targets)
- [remove_permission](./client.md#remove-permission)
- [remove_targets](./client.md#remove-targets)
- [start_replay](./client.md#start-replay)
- [tag_resource](./client.md#tag-resource)
- [test_event_pattern](./client.md#test-event-pattern)
- [untag_resource](./client.md#untag-resource)
- [update_api_destination](./client.md#update-api-destination)
- [update_archive](./client.md#update-archive)
- [update_connection](./client.md#update-connection)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [IllegalStatusException](./client.md#illegalstatusexception)
- [InternalException](./client.md#internalexception)
- [InvalidEventPatternException](./client.md#invalideventpatternexception)
- [InvalidStateException](./client.md#invalidstateexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ManagedRuleException](./client.md#managedruleexception)
- [OperationDisabledException](./client.md#operationdisabledexception)
- [PolicyLengthExceededException](./client.md#policylengthexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("events").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_events.paginators import ListRuleNamesByTargetPaginator, ...
```

- [ListRuleNamesByTargetPaginator](./paginators.md#listrulenamesbytargetpaginator)
- [ListRulesPaginator](./paginators.md#listrulespaginator)
- [ListTargetsByRulePaginator](./paginators.md#listtargetsbyrulepaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_events.literals import ApiDestinationHttpMethod, ...
```

- [ApiDestinationHttpMethod](./literals.md#apidestinationhttpmethod)
- [ApiDestinationState](./literals.md#apidestinationstate)
- [ArchiveState](./literals.md#archivestate)
- [AssignPublicIp](./literals.md#assignpublicip)
- [ConnectionAuthorizationType](./literals.md#connectionauthorizationtype)
- [ConnectionOAuthHttpMethod](./literals.md#connectionoauthhttpmethod)
- [ConnectionState](./literals.md#connectionstate)
- [EventSourceState](./literals.md#eventsourcestate)
- [LaunchType](./literals.md#launchtype)
- [ListRuleNamesByTargetPaginatorName](./literals.md#listrulenamesbytargetpaginatorname)
- [ListRulesPaginatorName](./literals.md#listrulespaginatorname)
- [ListTargetsByRulePaginatorName](./literals.md#listtargetsbyrulepaginatorname)
- [ReplayState](./literals.md#replaystate)
- [RuleState](./literals.md#rulestate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_events.type_defs import ApiDestinationTypeDef, ...
```

- [ApiDestinationTypeDef](./type_defs.md#apidestinationtypedef)
- [ArchiveTypeDef](./type_defs.md#archivetypedef)
- [AwsVpcConfigurationTypeDef](./type_defs.md#awsvpcconfigurationtypedef)
- [BatchArrayPropertiesTypeDef](./type_defs.md#batcharraypropertiestypedef)
- [BatchParametersTypeDef](./type_defs.md#batchparameterstypedef)
- [BatchRetryStrategyTypeDef](./type_defs.md#batchretrystrategytypedef)
- [CancelReplayResponseTypeDef](./type_defs.md#cancelreplayresponsetypedef)
- [ConditionTypeDef](./type_defs.md#conditiontypedef)
- [ConnectionApiKeyAuthResponseParametersTypeDef](./type_defs.md#connectionapikeyauthresponseparameterstypedef)
- [ConnectionAuthResponseParametersTypeDef](./type_defs.md#connectionauthresponseparameterstypedef)
- [ConnectionBasicAuthResponseParametersTypeDef](./type_defs.md#connectionbasicauthresponseparameterstypedef)
- [ConnectionBodyParameterTypeDef](./type_defs.md#connectionbodyparametertypedef)
- [ConnectionHeaderParameterTypeDef](./type_defs.md#connectionheaderparametertypedef)
- [ConnectionHttpParametersTypeDef](./type_defs.md#connectionhttpparameterstypedef)
- [ConnectionOAuthClientResponseParametersTypeDef](./type_defs.md#connectionoauthclientresponseparameterstypedef)
- [ConnectionOAuthResponseParametersTypeDef](./type_defs.md#connectionoauthresponseparameterstypedef)
- [ConnectionQueryStringParameterTypeDef](./type_defs.md#connectionquerystringparametertypedef)
- [ConnectionTypeDef](./type_defs.md#connectiontypedef)
- [CreateApiDestinationResponseTypeDef](./type_defs.md#createapidestinationresponsetypedef)
- [CreateArchiveResponseTypeDef](./type_defs.md#createarchiveresponsetypedef)
- [CreateConnectionApiKeyAuthRequestParametersTypeDef](./type_defs.md#createconnectionapikeyauthrequestparameterstypedef)
- [CreateConnectionAuthRequestParametersTypeDef](./type_defs.md#createconnectionauthrequestparameterstypedef)
- [CreateConnectionBasicAuthRequestParametersTypeDef](./type_defs.md#createconnectionbasicauthrequestparameterstypedef)
- [CreateConnectionOAuthClientRequestParametersTypeDef](./type_defs.md#createconnectionoauthclientrequestparameterstypedef)
- [CreateConnectionOAuthRequestParametersTypeDef](./type_defs.md#createconnectionoauthrequestparameterstypedef)
- [CreateConnectionResponseTypeDef](./type_defs.md#createconnectionresponsetypedef)
- [CreateEventBusResponseTypeDef](./type_defs.md#createeventbusresponsetypedef)
- [CreatePartnerEventSourceResponseTypeDef](./type_defs.md#createpartnereventsourceresponsetypedef)
- [DeadLetterConfigTypeDef](./type_defs.md#deadletterconfigtypedef)
- [DeauthorizeConnectionResponseTypeDef](./type_defs.md#deauthorizeconnectionresponsetypedef)
- [DeleteConnectionResponseTypeDef](./type_defs.md#deleteconnectionresponsetypedef)
- [DescribeApiDestinationResponseTypeDef](./type_defs.md#describeapidestinationresponsetypedef)
- [DescribeArchiveResponseTypeDef](./type_defs.md#describearchiveresponsetypedef)
- [DescribeConnectionResponseTypeDef](./type_defs.md#describeconnectionresponsetypedef)
- [DescribeEventBusResponseTypeDef](./type_defs.md#describeeventbusresponsetypedef)
- [DescribeEventSourceResponseTypeDef](./type_defs.md#describeeventsourceresponsetypedef)
- [DescribePartnerEventSourceResponseTypeDef](./type_defs.md#describepartnereventsourceresponsetypedef)
- [DescribeReplayResponseTypeDef](./type_defs.md#describereplayresponsetypedef)
- [DescribeRuleResponseTypeDef](./type_defs.md#describeruleresponsetypedef)
- [EcsParametersTypeDef](./type_defs.md#ecsparameterstypedef)
- [EventBusTypeDef](./type_defs.md#eventbustypedef)
- [EventSourceTypeDef](./type_defs.md#eventsourcetypedef)
- [HttpParametersTypeDef](./type_defs.md#httpparameterstypedef)
- [InputTransformerTypeDef](./type_defs.md#inputtransformertypedef)
- [KinesisParametersTypeDef](./type_defs.md#kinesisparameterstypedef)
- [ListApiDestinationsResponseTypeDef](./type_defs.md#listapidestinationsresponsetypedef)
- [ListArchivesResponseTypeDef](./type_defs.md#listarchivesresponsetypedef)
- [ListConnectionsResponseTypeDef](./type_defs.md#listconnectionsresponsetypedef)
- [ListEventBusesResponseTypeDef](./type_defs.md#listeventbusesresponsetypedef)
- [ListEventSourcesResponseTypeDef](./type_defs.md#listeventsourcesresponsetypedef)
- [ListPartnerEventSourceAccountsResponseTypeDef](./type_defs.md#listpartnereventsourceaccountsresponsetypedef)
- [ListPartnerEventSourcesResponseTypeDef](./type_defs.md#listpartnereventsourcesresponsetypedef)
- [ListReplaysResponseTypeDef](./type_defs.md#listreplaysresponsetypedef)
- [ListRuleNamesByTargetResponseTypeDef](./type_defs.md#listrulenamesbytargetresponsetypedef)
- [ListRulesResponseTypeDef](./type_defs.md#listrulesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTargetsByRuleResponseTypeDef](./type_defs.md#listtargetsbyruleresponsetypedef)
- [NetworkConfigurationTypeDef](./type_defs.md#networkconfigurationtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PartnerEventSourceAccountTypeDef](./type_defs.md#partnereventsourceaccounttypedef)
- [PartnerEventSourceTypeDef](./type_defs.md#partnereventsourcetypedef)
- [PutEventsRequestEntryTypeDef](./type_defs.md#puteventsrequestentrytypedef)
- [PutEventsResponseTypeDef](./type_defs.md#puteventsresponsetypedef)
- [PutEventsResultEntryTypeDef](./type_defs.md#puteventsresultentrytypedef)
- [PutPartnerEventsRequestEntryTypeDef](./type_defs.md#putpartnereventsrequestentrytypedef)
- [PutPartnerEventsResponseTypeDef](./type_defs.md#putpartnereventsresponsetypedef)
- [PutPartnerEventsResultEntryTypeDef](./type_defs.md#putpartnereventsresultentrytypedef)
- [PutRuleResponseTypeDef](./type_defs.md#putruleresponsetypedef)
- [PutTargetsResponseTypeDef](./type_defs.md#puttargetsresponsetypedef)
- [PutTargetsResultEntryTypeDef](./type_defs.md#puttargetsresultentrytypedef)
- [RedshiftDataParametersTypeDef](./type_defs.md#redshiftdataparameterstypedef)
- [RemoveTargetsResponseTypeDef](./type_defs.md#removetargetsresponsetypedef)
- [RemoveTargetsResultEntryTypeDef](./type_defs.md#removetargetsresultentrytypedef)
- [ReplayDestinationTypeDef](./type_defs.md#replaydestinationtypedef)
- [ReplayTypeDef](./type_defs.md#replaytypedef)
- [RetryPolicyTypeDef](./type_defs.md#retrypolicytypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [RunCommandParametersTypeDef](./type_defs.md#runcommandparameterstypedef)
- [RunCommandTargetTypeDef](./type_defs.md#runcommandtargettypedef)
- [SageMakerPipelineParameterTypeDef](./type_defs.md#sagemakerpipelineparametertypedef)
- [SageMakerPipelineParametersTypeDef](./type_defs.md#sagemakerpipelineparameterstypedef)
- [SqsParametersTypeDef](./type_defs.md#sqsparameterstypedef)
- [StartReplayResponseTypeDef](./type_defs.md#startreplayresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TargetTypeDef](./type_defs.md#targettypedef)
- [TestEventPatternResponseTypeDef](./type_defs.md#testeventpatternresponsetypedef)
- [UpdateApiDestinationResponseTypeDef](./type_defs.md#updateapidestinationresponsetypedef)
- [UpdateArchiveResponseTypeDef](./type_defs.md#updatearchiveresponsetypedef)
- [UpdateConnectionApiKeyAuthRequestParametersTypeDef](./type_defs.md#updateconnectionapikeyauthrequestparameterstypedef)
- [UpdateConnectionAuthRequestParametersTypeDef](./type_defs.md#updateconnectionauthrequestparameterstypedef)
- [UpdateConnectionBasicAuthRequestParametersTypeDef](./type_defs.md#updateconnectionbasicauthrequestparameterstypedef)
- [UpdateConnectionOAuthClientRequestParametersTypeDef](./type_defs.md#updateconnectionoauthclientrequestparameterstypedef)
- [UpdateConnectionOAuthRequestParametersTypeDef](./type_defs.md#updateconnectionoauthrequestparameterstypedef)
- [UpdateConnectionResponseTypeDef](./type_defs.md#updateconnectionresponsetypedef)
