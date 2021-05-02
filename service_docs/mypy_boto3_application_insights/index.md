# Type annotations for boto3 ApplicationInsights module

> [Index](../index.md) > ApplicationInsights

Auto-generated documentation for [ApplicationInsights](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights)
type annotations stubs module [mypy_boto3_application_insights](https://pypi.org/project/mypy-boto3-application-insights/).

```bash
pip install mypy-boto3-application-insights
```

- [Type annotations for boto3 ApplicationInsights module](#type-annotations-for-boto3-applicationinsights-module)
  - [ApplicationInsightsClient](#applicationinsightsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## ApplicationInsightsClient

Type annotations for  `boto3.client("application-insights")` as [ApplicationInsightsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_application_insights.client import ApplicationInsightsClient
```


ApplicationInsightsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [create_component](./client.md#create-component)
- [create_log_pattern](./client.md#create-log-pattern)
- [delete_application](./client.md#delete-application)
- [delete_component](./client.md#delete-component)
- [delete_log_pattern](./client.md#delete-log-pattern)
- [describe_application](./client.md#describe-application)
- [describe_component](./client.md#describe-component)
- [describe_component_configuration](./client.md#describe-component-configuration)
- [describe_component_configuration_recommendation](./client.md#describe-component-configuration-recommendation)
- [describe_log_pattern](./client.md#describe-log-pattern)
- [describe_observation](./client.md#describe-observation)
- [describe_problem](./client.md#describe-problem)
- [describe_problem_observations](./client.md#describe-problem-observations)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_applications](./client.md#list-applications)
- [list_components](./client.md#list-components)
- [list_configuration_history](./client.md#list-configuration-history)
- [list_log_pattern_sets](./client.md#list-log-pattern-sets)
- [list_log_patterns](./client.md#list-log-patterns)
- [list_problems](./client.md#list-problems)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)
- [update_component](./client.md#update-component)
- [update_component_configuration](./client.md#update-component-configuration)
- [update_log_pattern](./client.md#update-log-pattern)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TagsAlreadyExistException](./client.md#tagsalreadyexistexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_application_insights.literals import CloudWatchEventSource, ...
```

- [CloudWatchEventSource](./literals.md#cloudwatcheventsource)
- [ConfigurationEventResourceType](./literals.md#configurationeventresourcetype)
- [ConfigurationEventStatus](./literals.md#configurationeventstatus)
- [FeedbackKey](./literals.md#feedbackkey)
- [FeedbackValue](./literals.md#feedbackvalue)
- [LogFilter](./literals.md#logfilter)
- [OsType](./literals.md#ostype)
- [SeverityLevel](./literals.md#severitylevel)
- [Status](./literals.md#status)
- [Tier](./literals.md#tier)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_application_insights.type_defs import ApplicationComponentTypeDef, ...
```

- [ApplicationComponentTypeDef](./type_defs.md#applicationcomponenttypedef)
- [ApplicationInfoTypeDef](./type_defs.md#applicationinfotypedef)
- [ConfigurationEventTypeDef](./type_defs.md#configurationeventtypedef)
- [LogPatternTypeDef](./type_defs.md#logpatterntypedef)
- [ObservationTypeDef](./type_defs.md#observationtypedef)
- [ProblemTypeDef](./type_defs.md#problemtypedef)
- [RelatedObservationsTypeDef](./type_defs.md#relatedobservationstypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [CreateLogPatternResponseTypeDef](./type_defs.md#createlogpatternresponsetypedef)
- [DescribeApplicationResponseTypeDef](./type_defs.md#describeapplicationresponsetypedef)
- [DescribeComponentConfigurationRecommendationResponseTypeDef](./type_defs.md#describecomponentconfigurationrecommendationresponsetypedef)
- [DescribeComponentConfigurationResponseTypeDef](./type_defs.md#describecomponentconfigurationresponsetypedef)
- [DescribeComponentResponseTypeDef](./type_defs.md#describecomponentresponsetypedef)
- [DescribeLogPatternResponseTypeDef](./type_defs.md#describelogpatternresponsetypedef)
- [DescribeObservationResponseTypeDef](./type_defs.md#describeobservationresponsetypedef)
- [DescribeProblemObservationsResponseTypeDef](./type_defs.md#describeproblemobservationsresponsetypedef)
- [DescribeProblemResponseTypeDef](./type_defs.md#describeproblemresponsetypedef)
- [ListApplicationsResponseTypeDef](./type_defs.md#listapplicationsresponsetypedef)
- [ListComponentsResponseTypeDef](./type_defs.md#listcomponentsresponsetypedef)
- [ListConfigurationHistoryResponseTypeDef](./type_defs.md#listconfigurationhistoryresponsetypedef)
- [ListLogPatternSetsResponseTypeDef](./type_defs.md#listlogpatternsetsresponsetypedef)
- [ListLogPatternsResponseTypeDef](./type_defs.md#listlogpatternsresponsetypedef)
- [ListProblemsResponseTypeDef](./type_defs.md#listproblemsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [UpdateApplicationResponseTypeDef](./type_defs.md#updateapplicationresponsetypedef)
- [UpdateLogPatternResponseTypeDef](./type_defs.md#updatelogpatternresponsetypedef)
