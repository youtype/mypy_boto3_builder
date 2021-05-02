# ApplicationInsightsClient for boto3 ApplicationInsights module

> [Index](../index.md) > [ApplicationInsights](./index.md) > ApplicationInsightsClient

Auto-generated documentation for [ApplicationInsights](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights)
type annotations stubs module [mypy_boto3_application_insights](https://pypi.org/project/mypy-boto3-application-insights/).

- [ApplicationInsightsClient for boto3 ApplicationInsights module](#applicationinsightsclient-for-boto3-applicationinsights-module)
  - [ApplicationInsightsClient](#applicationinsightsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [create_component](#create_component)
    - [create_log_pattern](#create_log_pattern)
    - [delete_application](#delete_application)
    - [delete_component](#delete_component)
    - [delete_log_pattern](#delete_log_pattern)
    - [describe_application](#describe_application)
    - [describe_component](#describe_component)
    - [describe_component_configuration](#describe_component_configuration)
    - [describe_component_configuration_recommendation](#describe_component_configuration_recommendation)
    - [describe_log_pattern](#describe_log_pattern)
    - [describe_observation](#describe_observation)
    - [describe_problem](#describe_problem)
    - [describe_problem_observations](#describe_problem_observations)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_applications](#list_applications)
    - [list_components](#list_components)
    - [list_configuration_history](#list_configuration_history)
    - [list_log_pattern_sets](#list_log_pattern_sets)
    - [list_log_patterns](#list_log_patterns)
    - [list_problems](#list_problems)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_application](#update_application)
    - [update_component](#update_component)
    - [update_component_configuration](#update_component_configuration)
    - [update_log_pattern](#update_log_pattern)

## ApplicationInsightsClient

Type annotations for `boto3.client("application-insights")`

Can be used directly:

```python
from mypy_boto3_application_insights.client import ApplicationInsightsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_application_insights.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TagsAlreadyExistException`
- `Exceptions.TooManyTagsException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("application-insights").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("application-insights").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.create_application)

```python
def create_application(
    self,
    ResourceGroupName: str,
    OpsCenterEnabled: bool = None,
    CWEMonitorEnabled: bool = None,
    OpsItemSNSTopicArn: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateApplicationResponseTypeDef:
    pass
```

### create_component

Type annotations for `boto3.client("application-insights").create_component` method.

[Client.create_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.create_component)

```python
def create_component(
    self,
    ResourceGroupName: str,
    ComponentName: str,
    ResourceList: List[str]
) -> Dict[str, Any]:
    pass
```

### create_log_pattern

Type annotations for `boto3.client("application-insights").create_log_pattern` method.

[Client.create_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.create_log_pattern)

```python
def create_log_pattern(
    self,
    ResourceGroupName: str,
    PatternSetName: str,
    PatternName: str,
    Pattern: str,
    Rank: int
) -> CreateLogPatternResponseTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("application-insights").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.delete_application)

```python
def delete_application(
    self,
    ResourceGroupName: str
) -> Dict[str, Any]:
    pass
```

### delete_component

Type annotations for `boto3.client("application-insights").delete_component` method.

[Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.delete_component)

```python
def delete_component(
    self,
    ResourceGroupName: str,
    ComponentName: str
) -> Dict[str, Any]:
    pass
```

### delete_log_pattern

Type annotations for `boto3.client("application-insights").delete_log_pattern` method.

[Client.delete_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.delete_log_pattern)

```python
def delete_log_pattern(
    self,
    ResourceGroupName: str,
    PatternSetName: str,
    PatternName: str
) -> Dict[str, Any]:
    pass
```

### describe_application

Type annotations for `boto3.client("application-insights").describe_application` method.

[Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_application)

```python
def describe_application(
    self,
    ResourceGroupName: str
) -> DescribeApplicationResponseTypeDef:
    pass
```

### describe_component

Type annotations for `boto3.client("application-insights").describe_component` method.

[Client.describe_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_component)

```python
def describe_component(
    self,
    ResourceGroupName: str,
    ComponentName: str
) -> DescribeComponentResponseTypeDef:
    pass
```

### describe_component_configuration

Type annotations for `boto3.client("application-insights").describe_component_configuration` method.

[Client.describe_component_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration)

```python
def describe_component_configuration(
    self,
    ResourceGroupName: str,
    ComponentName: str
) -> DescribeComponentConfigurationResponseTypeDef:
    pass
```

### describe_component_configuration_recommendation

Type annotations for `boto3.client("application-insights").describe_component_configuration_recommendation` method.

[Client.describe_component_configuration_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration_recommendation)

```python
def describe_component_configuration_recommendation(
    self,
    ResourceGroupName: str,
    ComponentName: str,
    Tier: Tier
) -> DescribeComponentConfigurationRecommendationResponseTypeDef:
    pass
```

### describe_log_pattern

Type annotations for `boto3.client("application-insights").describe_log_pattern` method.

[Client.describe_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_log_pattern)

```python
def describe_log_pattern(
    self,
    ResourceGroupName: str,
    PatternSetName: str,
    PatternName: str
) -> DescribeLogPatternResponseTypeDef:
    pass
```

### describe_observation

Type annotations for `boto3.client("application-insights").describe_observation` method.

[Client.describe_observation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_observation)

```python
def describe_observation(
    self,
    ObservationId: str
) -> DescribeObservationResponseTypeDef:
    pass
```

### describe_problem

Type annotations for `boto3.client("application-insights").describe_problem` method.

[Client.describe_problem documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem)

```python
def describe_problem(
    self,
    ProblemId: str
) -> DescribeProblemResponseTypeDef:
    pass
```

### describe_problem_observations

Type annotations for `boto3.client("application-insights").describe_problem_observations` method.

[Client.describe_problem_observations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem_observations)

```python
def describe_problem_observations(
    self,
    ProblemId: str
) -> DescribeProblemObservationsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("application-insights").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### list_applications

Type annotations for `boto3.client("application-insights").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_applications)

```python
def list_applications(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListApplicationsResponseTypeDef:
    pass
```

### list_components

Type annotations for `boto3.client("application-insights").list_components` method.

[Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_components)

```python
def list_components(
    self,
    ResourceGroupName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListComponentsResponseTypeDef:
    pass
```

### list_configuration_history

Type annotations for `boto3.client("application-insights").list_configuration_history` method.

[Client.list_configuration_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_configuration_history)

```python
def list_configuration_history(
    self,
    ResourceGroupName: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    EventStatus: ConfigurationEventStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListConfigurationHistoryResponseTypeDef:
    pass
```

### list_log_pattern_sets

Type annotations for `boto3.client("application-insights").list_log_pattern_sets` method.

[Client.list_log_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_log_pattern_sets)

```python
def list_log_pattern_sets(
    self,
    ResourceGroupName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListLogPatternSetsResponseTypeDef:
    pass
```

### list_log_patterns

Type annotations for `boto3.client("application-insights").list_log_patterns` method.

[Client.list_log_patterns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_log_patterns)

```python
def list_log_patterns(
    self,
    ResourceGroupName: str,
    PatternSetName: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListLogPatternsResponseTypeDef:
    pass
```

### list_problems

Type annotations for `boto3.client("application-insights").list_problems` method.

[Client.list_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_problems)

```python
def list_problems(
    self,
    ResourceGroupName: str = None,
    StartTime: datetime = None,
    EndTime: datetime = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListProblemsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("application-insights").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("application-insights").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("application-insights").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_application

Type annotations for `boto3.client("application-insights").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.update_application)

```python
def update_application(
    self,
    ResourceGroupName: str,
    OpsCenterEnabled: bool = None,
    CWEMonitorEnabled: bool = None,
    OpsItemSNSTopicArn: str = None,
    RemoveSNSTopic: bool = None
) -> UpdateApplicationResponseTypeDef:
    pass
```

### update_component

Type annotations for `boto3.client("application-insights").update_component` method.

[Client.update_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.update_component)

```python
def update_component(
    self,
    ResourceGroupName: str,
    ComponentName: str,
    NewComponentName: str = None,
    ResourceList: List[str] = None
) -> Dict[str, Any]:
    pass
```

### update_component_configuration

Type annotations for `boto3.client("application-insights").update_component_configuration` method.

[Client.update_component_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.update_component_configuration)

```python
def update_component_configuration(
    self,
    ResourceGroupName: str,
    ComponentName: str,
    Monitor: bool = None,
    Tier: Tier = None,
    ComponentConfiguration: str = None
) -> Dict[str, Any]:
    pass
```

### update_log_pattern

Type annotations for `boto3.client("application-insights").update_log_pattern` method.

[Client.update_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client.update_log_pattern)

```python
def update_log_pattern(
    self,
    ResourceGroupName: str,
    PatternSetName: str,
    PatternName: str,
    Pattern: str = None,
    Rank: int = None
) -> UpdateLogPatternResponseTypeDef:
    pass
```