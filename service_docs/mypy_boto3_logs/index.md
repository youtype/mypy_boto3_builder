# Type annotations for boto3 CloudWatchLogs module

> [Index](../index.md) > CloudWatchLogs

Auto-generated documentation for [CloudWatchLogs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html#CloudWatchLogs)
type annotations stubs module [mypy_boto3_logs](https://pypi.org/project/mypy-boto3-logs/).

```bash
pip install mypy-boto3-logs
```

- [Type annotations for boto3 CloudWatchLogs module](#type-annotations-for-boto3-cloudwatchlogs-module)
  - [CloudWatchLogsClient](#cloudwatchlogsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudWatchLogsClient

Type annotations for  `boto3.client("logs")` as [CloudWatchLogsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_logs.client import CloudWatchLogsClient
```


CloudWatchLogsClient [exceptions](./client.md#exceptions)



### Methods
- [associate_kms_key](./client.md#associate-kms-key)
- [can_paginate](./client.md#can-paginate)
- [cancel_export_task](./client.md#cancel-export-task)
- [create_export_task](./client.md#create-export-task)
- [create_log_group](./client.md#create-log-group)
- [create_log_stream](./client.md#create-log-stream)
- [delete_destination](./client.md#delete-destination)
- [delete_log_group](./client.md#delete-log-group)
- [delete_log_stream](./client.md#delete-log-stream)
- [delete_metric_filter](./client.md#delete-metric-filter)
- [delete_query_definition](./client.md#delete-query-definition)
- [delete_resource_policy](./client.md#delete-resource-policy)
- [delete_retention_policy](./client.md#delete-retention-policy)
- [delete_subscription_filter](./client.md#delete-subscription-filter)
- [describe_destinations](./client.md#describe-destinations)
- [describe_export_tasks](./client.md#describe-export-tasks)
- [describe_log_groups](./client.md#describe-log-groups)
- [describe_log_streams](./client.md#describe-log-streams)
- [describe_metric_filters](./client.md#describe-metric-filters)
- [describe_queries](./client.md#describe-queries)
- [describe_query_definitions](./client.md#describe-query-definitions)
- [describe_resource_policies](./client.md#describe-resource-policies)
- [describe_subscription_filters](./client.md#describe-subscription-filters)
- [disassociate_kms_key](./client.md#disassociate-kms-key)
- [filter_log_events](./client.md#filter-log-events)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_log_events](./client.md#get-log-events)
- [get_log_group_fields](./client.md#get-log-group-fields)
- [get_log_record](./client.md#get-log-record)
- [get_paginator](./client.md#get-paginator)
- [get_query_results](./client.md#get-query-results)
- [list_tags_log_group](./client.md#list-tags-log-group)
- [put_destination](./client.md#put-destination)
- [put_destination_policy](./client.md#put-destination-policy)
- [put_log_events](./client.md#put-log-events)
- [put_metric_filter](./client.md#put-metric-filter)
- [put_query_definition](./client.md#put-query-definition)
- [put_resource_policy](./client.md#put-resource-policy)
- [put_retention_policy](./client.md#put-retention-policy)
- [put_subscription_filter](./client.md#put-subscription-filter)
- [start_query](./client.md#start-query)
- [stop_query](./client.md#stop-query)
- [tag_log_group](./client.md#tag-log-group)
- [test_metric_filter](./client.md#test-metric-filter)
- [untag_log_group](./client.md#untag-log-group)




### Exceptions
- [ClientError](./client.md#clienterror)
- [DataAlreadyAcceptedException](./client.md#dataalreadyacceptedexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidSequenceTokenException](./client.md#invalidsequencetokenexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MalformedQueryException](./client.md#malformedqueryexception)
- [OperationAbortedException](./client.md#operationabortedexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [UnrecognizedClientException](./client.md#unrecognizedclientexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("logs").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_logs.paginators import DescribeDestinationsPaginator, ...
```

- [DescribeDestinationsPaginator](./paginators.md#describedestinationspaginator)
- [DescribeExportTasksPaginator](./paginators.md#describeexporttaskspaginator)
- [DescribeLogGroupsPaginator](./paginators.md#describeloggroupspaginator)
- [DescribeLogStreamsPaginator](./paginators.md#describelogstreamspaginator)
- [DescribeMetricFiltersPaginator](./paginators.md#describemetricfilterspaginator)
- [DescribeQueriesPaginator](./paginators.md#describequeriespaginator)
- [DescribeResourcePoliciesPaginator](./paginators.md#describeresourcepoliciespaginator)
- [DescribeSubscriptionFiltersPaginator](./paginators.md#describesubscriptionfilterspaginator)
- [FilterLogEventsPaginator](./paginators.md#filterlogeventspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_logs.literals import DescribeDestinationsPaginatorName, ...
```

- [DescribeDestinationsPaginatorName](./literals.md#describedestinationspaginatorname)
- [DescribeExportTasksPaginatorName](./literals.md#describeexporttaskspaginatorname)
- [DescribeLogGroupsPaginatorName](./literals.md#describeloggroupspaginatorname)
- [DescribeLogStreamsPaginatorName](./literals.md#describelogstreamspaginatorname)
- [DescribeMetricFiltersPaginatorName](./literals.md#describemetricfilterspaginatorname)
- [DescribeQueriesPaginatorName](./literals.md#describequeriespaginatorname)
- [DescribeResourcePoliciesPaginatorName](./literals.md#describeresourcepoliciespaginatorname)
- [DescribeSubscriptionFiltersPaginatorName](./literals.md#describesubscriptionfilterspaginatorname)
- [Distribution](./literals.md#distribution)
- [ExportTaskStatusCode](./literals.md#exporttaskstatuscode)
- [FilterLogEventsPaginatorName](./literals.md#filterlogeventspaginatorname)
- [OrderBy](./literals.md#orderby)
- [QueryStatus](./literals.md#querystatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_logs.type_defs import DestinationTypeDef, ...
```

- [DestinationTypeDef](./type_defs.md#destinationtypedef)
- [ExportTaskExecutionInfoTypeDef](./type_defs.md#exporttaskexecutioninfotypedef)
- [ExportTaskStatusTypeDef](./type_defs.md#exporttaskstatustypedef)
- [ExportTaskTypeDef](./type_defs.md#exporttasktypedef)
- [FilteredLogEventTypeDef](./type_defs.md#filteredlogeventtypedef)
- [LogGroupFieldTypeDef](./type_defs.md#loggroupfieldtypedef)
- [LogGroupTypeDef](./type_defs.md#loggrouptypedef)
- [LogStreamTypeDef](./type_defs.md#logstreamtypedef)
- [MetricFilterMatchRecordTypeDef](./type_defs.md#metricfiltermatchrecordtypedef)
- [MetricFilterTypeDef](./type_defs.md#metricfiltertypedef)
- [MetricTransformationTypeDef](./type_defs.md#metrictransformationtypedef)
- [OutputLogEventTypeDef](./type_defs.md#outputlogeventtypedef)
- [QueryDefinitionTypeDef](./type_defs.md#querydefinitiontypedef)
- [QueryInfoTypeDef](./type_defs.md#queryinfotypedef)
- [QueryStatisticsTypeDef](./type_defs.md#querystatisticstypedef)
- [RejectedLogEventsInfoTypeDef](./type_defs.md#rejectedlogeventsinfotypedef)
- [ResourcePolicyTypeDef](./type_defs.md#resourcepolicytypedef)
- [ResultFieldTypeDef](./type_defs.md#resultfieldtypedef)
- [SearchedLogStreamTypeDef](./type_defs.md#searchedlogstreamtypedef)
- [SubscriptionFilterTypeDef](./type_defs.md#subscriptionfiltertypedef)
- [CreateExportTaskResponseTypeDef](./type_defs.md#createexporttaskresponsetypedef)
- [DeleteQueryDefinitionResponseTypeDef](./type_defs.md#deletequerydefinitionresponsetypedef)
- [DescribeDestinationsResponseTypeDef](./type_defs.md#describedestinationsresponsetypedef)
- [DescribeExportTasksResponseTypeDef](./type_defs.md#describeexporttasksresponsetypedef)
- [DescribeLogGroupsResponseTypeDef](./type_defs.md#describeloggroupsresponsetypedef)
- [DescribeLogStreamsResponseTypeDef](./type_defs.md#describelogstreamsresponsetypedef)
- [DescribeMetricFiltersResponseTypeDef](./type_defs.md#describemetricfiltersresponsetypedef)
- [DescribeQueriesResponseTypeDef](./type_defs.md#describequeriesresponsetypedef)
- [DescribeQueryDefinitionsResponseTypeDef](./type_defs.md#describequerydefinitionsresponsetypedef)
- [DescribeResourcePoliciesResponseTypeDef](./type_defs.md#describeresourcepoliciesresponsetypedef)
- [DescribeSubscriptionFiltersResponseTypeDef](./type_defs.md#describesubscriptionfiltersresponsetypedef)
- [FilterLogEventsResponseTypeDef](./type_defs.md#filterlogeventsresponsetypedef)
- [GetLogEventsResponseTypeDef](./type_defs.md#getlogeventsresponsetypedef)
- [GetLogGroupFieldsResponseTypeDef](./type_defs.md#getloggroupfieldsresponsetypedef)
- [GetLogRecordResponseTypeDef](./type_defs.md#getlogrecordresponsetypedef)
- [GetQueryResultsResponseTypeDef](./type_defs.md#getqueryresultsresponsetypedef)
- [InputLogEventTypeDef](./type_defs.md#inputlogeventtypedef)
- [ListTagsLogGroupResponseTypeDef](./type_defs.md#listtagsloggroupresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PutDestinationResponseTypeDef](./type_defs.md#putdestinationresponsetypedef)
- [PutLogEventsResponseTypeDef](./type_defs.md#putlogeventsresponsetypedef)
- [PutQueryDefinitionResponseTypeDef](./type_defs.md#putquerydefinitionresponsetypedef)
- [PutResourcePolicyResponseTypeDef](./type_defs.md#putresourcepolicyresponsetypedef)
- [StartQueryResponseTypeDef](./type_defs.md#startqueryresponsetypedef)
- [StopQueryResponseTypeDef](./type_defs.md#stopqueryresponsetypedef)
- [TestMetricFilterResponseTypeDef](./type_defs.md#testmetricfilterresponsetypedef)
