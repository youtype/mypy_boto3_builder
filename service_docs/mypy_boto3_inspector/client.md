# InspectorClient for boto3 Inspector module

> [Index](../index.md) > [Inspector](./index.md) > InspectorClient

Auto-generated documentation for [Inspector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector)
type annotations stubs module [mypy_boto3_inspector](https://pypi.org/project/mypy-boto3-inspector/).

- [InspectorClient for boto3 Inspector module](#inspectorclient-for-boto3-inspector-module)
  - [InspectorClient](#inspectorclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_attributes_to_findings](#add_attributes_to_findings)
    - [can_paginate](#can_paginate)
    - [create_assessment_target](#create_assessment_target)
    - [create_assessment_template](#create_assessment_template)
    - [create_exclusions_preview](#create_exclusions_preview)
    - [create_resource_group](#create_resource_group)
    - [delete_assessment_run](#delete_assessment_run)
    - [delete_assessment_target](#delete_assessment_target)
    - [delete_assessment_template](#delete_assessment_template)
    - [describe_assessment_runs](#describe_assessment_runs)
    - [describe_assessment_targets](#describe_assessment_targets)
    - [describe_assessment_templates](#describe_assessment_templates)
    - [describe_cross_account_access_role](#describe_cross_account_access_role)
    - [describe_exclusions](#describe_exclusions)
    - [describe_findings](#describe_findings)
    - [describe_resource_groups](#describe_resource_groups)
    - [describe_rules_packages](#describe_rules_packages)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_assessment_report](#get_assessment_report)
    - [get_exclusions_preview](#get_exclusions_preview)
    - [get_telemetry_metadata](#get_telemetry_metadata)
    - [list_assessment_run_agents](#list_assessment_run_agents)
    - [list_assessment_runs](#list_assessment_runs)
    - [list_assessment_targets](#list_assessment_targets)
    - [list_assessment_templates](#list_assessment_templates)
    - [list_event_subscriptions](#list_event_subscriptions)
    - [list_exclusions](#list_exclusions)
    - [list_findings](#list_findings)
    - [list_rules_packages](#list_rules_packages)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [preview_agents](#preview_agents)
    - [register_cross_account_access_role](#register_cross_account_access_role)
    - [remove_attributes_from_findings](#remove_attributes_from_findings)
    - [set_tags_for_resource](#set_tags_for_resource)
    - [start_assessment_run](#start_assessment_run)
    - [stop_assessment_run](#stop_assessment_run)
    - [subscribe_to_event](#subscribe_to_event)
    - [unsubscribe_from_event](#unsubscribe_from_event)
    - [update_assessment_target](#update_assessment_target)
    - [get_paginator](#get_paginator)

## InspectorClient

Type annotations for `boto3.client("inspector")`

Can be used directly:

```python
from mypy_boto3_inspector.client import InspectorClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_inspector.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AgentsAlreadyRunningAssessmentException`
- `Exceptions.AssessmentRunInProgressException`
- `Exceptions.ClientError`
- `Exceptions.InternalException`
- `Exceptions.InvalidCrossAccountRoleException`
- `Exceptions.InvalidInputException`
- `Exceptions.LimitExceededException`
- `Exceptions.NoSuchEntityException`
- `Exceptions.PreviewGenerationInProgressException`
- `Exceptions.ServiceTemporarilyUnavailableException`
- `Exceptions.UnsupportedFeatureException`


## Methods


### add_attributes_to_findings

Type annotations for `boto3.client("inspector").add_attributes_to_findings` method.

[Client.add_attributes_to_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.add_attributes_to_findings)

```python
def add_attributes_to_findings(
    self,
    findingArns: List[str],
    attributes: List["AttributeTypeDef"]
) -> AddAttributesToFindingsResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("inspector").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_assessment_target

Type annotations for `boto3.client("inspector").create_assessment_target` method.

[Client.create_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.create_assessment_target)

```python
def create_assessment_target(
    self,
    assessmentTargetName: str,
    resourceGroupArn: str = None
) -> CreateAssessmentTargetResponseTypeDef:
    pass
```

### create_assessment_template

Type annotations for `boto3.client("inspector").create_assessment_template` method.

[Client.create_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.create_assessment_template)

```python
def create_assessment_template(
    self,
    assessmentTargetArn: str,
    assessmentTemplateName: str,
    durationInSeconds: int,
    rulesPackageArns: List[str],
    userAttributesForFindings: List["AttributeTypeDef"] = None
) -> CreateAssessmentTemplateResponseTypeDef:
    pass
```

### create_exclusions_preview

Type annotations for `boto3.client("inspector").create_exclusions_preview` method.

[Client.create_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.create_exclusions_preview)

```python
def create_exclusions_preview(
    self,
    assessmentTemplateArn: str
) -> CreateExclusionsPreviewResponseTypeDef:
    pass
```

### create_resource_group

Type annotations for `boto3.client("inspector").create_resource_group` method.

[Client.create_resource_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.create_resource_group)

```python
def create_resource_group(
    self,
    resourceGroupTags: List["ResourceGroupTagTypeDef"]
) -> CreateResourceGroupResponseTypeDef:
    pass
```

### delete_assessment_run

Type annotations for `boto3.client("inspector").delete_assessment_run` method.

[Client.delete_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.delete_assessment_run)

```python
def delete_assessment_run(
    self,
    assessmentRunArn: str
) -> None:
    pass
```

### delete_assessment_target

Type annotations for `boto3.client("inspector").delete_assessment_target` method.

[Client.delete_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.delete_assessment_target)

```python
def delete_assessment_target(
    self,
    assessmentTargetArn: str
) -> None:
    pass
```

### delete_assessment_template

Type annotations for `boto3.client("inspector").delete_assessment_template` method.

[Client.delete_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.delete_assessment_template)

```python
def delete_assessment_template(
    self,
    assessmentTemplateArn: str
) -> None:
    pass
```

### describe_assessment_runs

Type annotations for `boto3.client("inspector").describe_assessment_runs` method.

[Client.describe_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_assessment_runs)

```python
def describe_assessment_runs(
    self,
    assessmentRunArns: List[str]
) -> DescribeAssessmentRunsResponseTypeDef:
    pass
```

### describe_assessment_targets

Type annotations for `boto3.client("inspector").describe_assessment_targets` method.

[Client.describe_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_assessment_targets)

```python
def describe_assessment_targets(
    self,
    assessmentTargetArns: List[str]
) -> DescribeAssessmentTargetsResponseTypeDef:
    pass
```

### describe_assessment_templates

Type annotations for `boto3.client("inspector").describe_assessment_templates` method.

[Client.describe_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_assessment_templates)

```python
def describe_assessment_templates(
    self,
    assessmentTemplateArns: List[str]
) -> DescribeAssessmentTemplatesResponseTypeDef:
    pass
```

### describe_cross_account_access_role

Type annotations for `boto3.client("inspector").describe_cross_account_access_role` method.

[Client.describe_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_cross_account_access_role)

```python
def describe_cross_account_access_role(
    self
) -> DescribeCrossAccountAccessRoleResponseTypeDef:
    pass
```

### describe_exclusions

Type annotations for `boto3.client("inspector").describe_exclusions` method.

[Client.describe_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_exclusions)

```python
def describe_exclusions(
    self,
    exclusionArns: List[str],
    locale: Literal['EN_US'] = None
) -> DescribeExclusionsResponseTypeDef:
    pass
```

### describe_findings

Type annotations for `boto3.client("inspector").describe_findings` method.

[Client.describe_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_findings)

```python
def describe_findings(
    self,
    findingArns: List[str],
    locale: Literal['EN_US'] = None
) -> DescribeFindingsResponseTypeDef:
    pass
```

### describe_resource_groups

Type annotations for `boto3.client("inspector").describe_resource_groups` method.

[Client.describe_resource_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_resource_groups)

```python
def describe_resource_groups(
    self,
    resourceGroupArns: List[str]
) -> DescribeResourceGroupsResponseTypeDef:
    pass
```

### describe_rules_packages

Type annotations for `boto3.client("inspector").describe_rules_packages` method.

[Client.describe_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.describe_rules_packages)

```python
def describe_rules_packages(
    self,
    rulesPackageArns: List[str],
    locale: Literal['EN_US'] = None
) -> DescribeRulesPackagesResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("inspector").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.generate_presigned_url)

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

### get_assessment_report

Type annotations for `boto3.client("inspector").get_assessment_report` method.

[Client.get_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.get_assessment_report)

```python
def get_assessment_report(
    self,
    assessmentRunArn: str,
    reportFileFormat: ReportFileFormat,
    reportType: ReportType
) -> GetAssessmentReportResponseTypeDef:
    pass
```

### get_exclusions_preview

Type annotations for `boto3.client("inspector").get_exclusions_preview` method.

[Client.get_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.get_exclusions_preview)

```python
def get_exclusions_preview(
    self,
    assessmentTemplateArn: str,
    previewToken: str,
    nextToken: str = None,
    maxResults: int = None,
    locale: Literal['EN_US'] = None
) -> GetExclusionsPreviewResponseTypeDef:
    pass
```

### get_telemetry_metadata

Type annotations for `boto3.client("inspector").get_telemetry_metadata` method.

[Client.get_telemetry_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.get_telemetry_metadata)

```python
def get_telemetry_metadata(
    self,
    assessmentRunArn: str
) -> GetTelemetryMetadataResponseTypeDef:
    pass
```

### list_assessment_run_agents

Type annotations for `boto3.client("inspector").list_assessment_run_agents` method.

[Client.list_assessment_run_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_assessment_run_agents)

```python
def list_assessment_run_agents(
    self,
    assessmentRunArn: str,
    filter: AgentFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentRunAgentsResponseTypeDef:
    pass
```

### list_assessment_runs

Type annotations for `boto3.client("inspector").list_assessment_runs` method.

[Client.list_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_assessment_runs)

```python
def list_assessment_runs(
    self,
    assessmentTemplateArns: List[str] = None,
    filter: AssessmentRunFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentRunsResponseTypeDef:
    pass
```

### list_assessment_targets

Type annotations for `boto3.client("inspector").list_assessment_targets` method.

[Client.list_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_assessment_targets)

```python
def list_assessment_targets(
    self,
    filter: AssessmentTargetFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentTargetsResponseTypeDef:
    pass
```

### list_assessment_templates

Type annotations for `boto3.client("inspector").list_assessment_templates` method.

[Client.list_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_assessment_templates)

```python
def list_assessment_templates(
    self,
    assessmentTargetArns: List[str] = None,
    filter: AssessmentTemplateFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentTemplatesResponseTypeDef:
    pass
```

### list_event_subscriptions

Type annotations for `boto3.client("inspector").list_event_subscriptions` method.

[Client.list_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_event_subscriptions)

```python
def list_event_subscriptions(
    self,
    resourceArn: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListEventSubscriptionsResponseTypeDef:
    pass
```

### list_exclusions

Type annotations for `boto3.client("inspector").list_exclusions` method.

[Client.list_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_exclusions)

```python
def list_exclusions(
    self,
    assessmentRunArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListExclusionsResponseTypeDef:
    pass
```

### list_findings

Type annotations for `boto3.client("inspector").list_findings` method.

[Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_findings)

```python
def list_findings(
    self,
    assessmentRunArns: List[str] = None,
    filter: FindingFilterTypeDef = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListFindingsResponseTypeDef:
    pass
```

### list_rules_packages

Type annotations for `boto3.client("inspector").list_rules_packages` method.

[Client.list_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_rules_packages)

```python
def list_rules_packages(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListRulesPackagesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("inspector").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### preview_agents

Type annotations for `boto3.client("inspector").preview_agents` method.

[Client.preview_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.preview_agents)

```python
def preview_agents(
    self,
    previewAgentsArn: str,
    nextToken: str = None,
    maxResults: int = None
) -> PreviewAgentsResponseTypeDef:
    pass
```

### register_cross_account_access_role

Type annotations for `boto3.client("inspector").register_cross_account_access_role` method.

[Client.register_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.register_cross_account_access_role)

```python
def register_cross_account_access_role(
    self,
    roleArn: str
) -> None:
    pass
```

### remove_attributes_from_findings

Type annotations for `boto3.client("inspector").remove_attributes_from_findings` method.

[Client.remove_attributes_from_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.remove_attributes_from_findings)

```python
def remove_attributes_from_findings(
    self,
    findingArns: List[str],
    attributeKeys: List[str]
) -> RemoveAttributesFromFindingsResponseTypeDef:
    pass
```

### set_tags_for_resource

Type annotations for `boto3.client("inspector").set_tags_for_resource` method.

[Client.set_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.set_tags_for_resource)

```python
def set_tags_for_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"] = None
) -> None:
    pass
```

### start_assessment_run

Type annotations for `boto3.client("inspector").start_assessment_run` method.

[Client.start_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.start_assessment_run)

```python
def start_assessment_run(
    self,
    assessmentTemplateArn: str,
    assessmentRunName: str = None
) -> StartAssessmentRunResponseTypeDef:
    pass
```

### stop_assessment_run

Type annotations for `boto3.client("inspector").stop_assessment_run` method.

[Client.stop_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.stop_assessment_run)

```python
def stop_assessment_run(
    self,
    assessmentRunArn: str,
    stopAction: StopAction = None
) -> None:
    pass
```

### subscribe_to_event

Type annotations for `boto3.client("inspector").subscribe_to_event` method.

[Client.subscribe_to_event documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.subscribe_to_event)

```python
def subscribe_to_event(
    self,
    resourceArn: str,
    event: InspectorEvent,
    topicArn: str
) -> None:
    pass
```

### unsubscribe_from_event

Type annotations for `boto3.client("inspector").unsubscribe_from_event` method.

[Client.unsubscribe_from_event documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.unsubscribe_from_event)

```python
def unsubscribe_from_event(
    self,
    resourceArn: str,
    event: InspectorEvent,
    topicArn: str
) -> None:
    pass
```

### update_assessment_target

Type annotations for `boto3.client("inspector").update_assessment_target` method.

[Client.update_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client.update_assessment_target)

```python
def update_assessment_target(
    self,
    assessmentTargetArn: str,
    assessmentTargetName: str,
    resourceGroupArn: str = None
) -> None:
    pass
```



### get_paginator

Type annotations for `boto3.client("inspector").get_paginator` method with overloads.

- `client.get_paginator("list_assessment_run_agents")` -> [ListAssessmentRunAgentsPaginator](./paginators.md#listassessmentrunagentspaginator)
- `client.get_paginator("list_assessment_runs")` -> [ListAssessmentRunsPaginator](./paginators.md#listassessmentrunspaginator)
- `client.get_paginator("list_assessment_targets")` -> [ListAssessmentTargetsPaginator](./paginators.md#listassessmenttargetspaginator)
- `client.get_paginator("list_assessment_templates")` -> [ListAssessmentTemplatesPaginator](./paginators.md#listassessmenttemplatespaginator)
- `client.get_paginator("list_event_subscriptions")` -> [ListEventSubscriptionsPaginator](./paginators.md#listeventsubscriptionspaginator)
- `client.get_paginator("list_exclusions")` -> [ListExclusionsPaginator](./paginators.md#listexclusionspaginator)
- `client.get_paginator("list_findings")` -> [ListFindingsPaginator](./paginators.md#listfindingspaginator)
- `client.get_paginator("list_rules_packages")` -> [ListRulesPackagesPaginator](./paginators.md#listrulespackagespaginator)
- `client.get_paginator("preview_agents")` -> [PreviewAgentsPaginator](./paginators.md#previewagentspaginator)


