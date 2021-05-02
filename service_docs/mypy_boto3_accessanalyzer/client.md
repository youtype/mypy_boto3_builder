# AccessAnalyzerClient for boto3 AccessAnalyzer module

> [Index](../index.md) > [AccessAnalyzer](./index.md) > AccessAnalyzerClient

Auto-generated documentation for [AccessAnalyzer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer)
type annotations stubs module [mypy_boto3_accessanalyzer](https://pypi.org/project/mypy-boto3-accessanalyzer/).

- [AccessAnalyzerClient for boto3 AccessAnalyzer module](#accessanalyzerclient-for-boto3-accessanalyzer-module)
  - [AccessAnalyzerClient](#accessanalyzerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [apply_archive_rule](#apply_archive_rule)
    - [can_paginate](#can_paginate)
    - [cancel_policy_generation](#cancel_policy_generation)
    - [create_access_preview](#create_access_preview)
    - [create_analyzer](#create_analyzer)
    - [create_archive_rule](#create_archive_rule)
    - [delete_analyzer](#delete_analyzer)
    - [delete_archive_rule](#delete_archive_rule)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_access_preview](#get_access_preview)
    - [get_analyzed_resource](#get_analyzed_resource)
    - [get_analyzer](#get_analyzer)
    - [get_archive_rule](#get_archive_rule)
    - [get_finding](#get_finding)
    - [get_generated_policy](#get_generated_policy)
    - [list_access_preview_findings](#list_access_preview_findings)
    - [list_access_previews](#list_access_previews)
    - [list_analyzed_resources](#list_analyzed_resources)
    - [list_analyzers](#list_analyzers)
    - [list_archive_rules](#list_archive_rules)
    - [list_findings](#list_findings)
    - [list_policy_generations](#list_policy_generations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_policy_generation](#start_policy_generation)
    - [start_resource_scan](#start_resource_scan)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_archive_rule](#update_archive_rule)
    - [update_findings](#update_findings)
    - [validate_policy](#validate_policy)
    - [get_paginator](#get_paginator)

## AccessAnalyzerClient

Type annotations for `boto3.client("accessanalyzer")`

Can be used directly:

```python
from mypy_boto3_accessanalyzer.client import AccessAnalyzerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_accessanalyzer.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### apply_archive_rule

Type annotations for `boto3.client("accessanalyzer").apply_archive_rule` method.

[Client.apply_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.apply_archive_rule)

```python
def apply_archive_rule(
    self,
    analyzerArn: str,
    ruleName: str,
    clientToken: str = None
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("accessanalyzer").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_policy_generation

Type annotations for `boto3.client("accessanalyzer").cancel_policy_generation` method.

[Client.cancel_policy_generation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.cancel_policy_generation)

```python
def cancel_policy_generation(
    self,
    jobId: str
) -> Dict[str, Any]:
    pass
```

### create_access_preview

Type annotations for `boto3.client("accessanalyzer").create_access_preview` method.

[Client.create_access_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_access_preview)

```python
def create_access_preview(
    self,
    analyzerArn: str,
    configurations: Dict[str, "ConfigurationTypeDef"],
    clientToken: str = None
) -> CreateAccessPreviewResponseTypeDef:
    pass
```

### create_analyzer

Type annotations for `boto3.client("accessanalyzer").create_analyzer` method.

[Client.create_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_analyzer)

```python
def create_analyzer(
    self,
    analyzerName: str,
    type: TypeType,
    archiveRules: List[InlineArchiveRuleTypeDef] = None,
    clientToken: str = None,
    tags: Dict[str, str] = None
) -> CreateAnalyzerResponseTypeDef:
    pass
```

### create_archive_rule

Type annotations for `boto3.client("accessanalyzer").create_archive_rule` method.

[Client.create_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_archive_rule)

```python
def create_archive_rule(
    self,
    analyzerName: str,
    filter: Dict[str, "CriterionTypeDef"],
    ruleName: str,
    clientToken: str = None
) -> None:
    pass
```

### delete_analyzer

Type annotations for `boto3.client("accessanalyzer").delete_analyzer` method.

[Client.delete_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_analyzer)

```python
def delete_analyzer(
    self,
    analyzerName: str,
    clientToken: str = None
) -> None:
    pass
```

### delete_archive_rule

Type annotations for `boto3.client("accessanalyzer").delete_archive_rule` method.

[Client.delete_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_archive_rule)

```python
def delete_archive_rule(
    self,
    analyzerName: str,
    ruleName: str,
    clientToken: str = None
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("accessanalyzer").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.generate_presigned_url)

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

### get_access_preview

Type annotations for `boto3.client("accessanalyzer").get_access_preview` method.

[Client.get_access_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_access_preview)

```python
def get_access_preview(
    self,
    accessPreviewId: str,
    analyzerArn: str
) -> GetAccessPreviewResponseTypeDef:
    pass
```

### get_analyzed_resource

Type annotations for `boto3.client("accessanalyzer").get_analyzed_resource` method.

[Client.get_analyzed_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzed_resource)

```python
def get_analyzed_resource(
    self,
    analyzerArn: str,
    resourceArn: str
) -> GetAnalyzedResourceResponseTypeDef:
    pass
```

### get_analyzer

Type annotations for `boto3.client("accessanalyzer").get_analyzer` method.

[Client.get_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzer)

```python
def get_analyzer(
    self,
    analyzerName: str
) -> GetAnalyzerResponseTypeDef:
    pass
```

### get_archive_rule

Type annotations for `boto3.client("accessanalyzer").get_archive_rule` method.

[Client.get_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_archive_rule)

```python
def get_archive_rule(
    self,
    analyzerName: str,
    ruleName: str
) -> GetArchiveRuleResponseTypeDef:
    pass
```

### get_finding

Type annotations for `boto3.client("accessanalyzer").get_finding` method.

[Client.get_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_finding)

```python
def get_finding(
    self,
    analyzerArn: str,
    id: str
) -> GetFindingResponseTypeDef:
    pass
```

### get_generated_policy

Type annotations for `boto3.client("accessanalyzer").get_generated_policy` method.

[Client.get_generated_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_generated_policy)

```python
def get_generated_policy(
    self,
    jobId: str,
    includeResourcePlaceholders: bool = None,
    includeServiceLevelTemplate: bool = None
) -> GetGeneratedPolicyResponseTypeDef:
    pass
```

### list_access_preview_findings

Type annotations for `boto3.client("accessanalyzer").list_access_preview_findings` method.

[Client.list_access_preview_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_access_preview_findings)

```python
def list_access_preview_findings(
    self,
    accessPreviewId: str,
    analyzerArn: str,
    filter: Dict[str, "CriterionTypeDef"] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListAccessPreviewFindingsResponseTypeDef:
    pass
```

### list_access_previews

Type annotations for `boto3.client("accessanalyzer").list_access_previews` method.

[Client.list_access_previews documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_access_previews)

```python
def list_access_previews(
    self,
    analyzerArn: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListAccessPreviewsResponseTypeDef:
    pass
```

### list_analyzed_resources

Type annotations for `boto3.client("accessanalyzer").list_analyzed_resources` method.

[Client.list_analyzed_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzed_resources)

```python
def list_analyzed_resources(
    self,
    analyzerArn: str,
    maxResults: int = None,
    nextToken: str = None,
    resourceType: ResourceType = None
) -> ListAnalyzedResourcesResponseTypeDef:
    pass
```

### list_analyzers

Type annotations for `boto3.client("accessanalyzer").list_analyzers` method.

[Client.list_analyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzers)

```python
def list_analyzers(
    self,
    maxResults: int = None,
    nextToken: str = None,
    type: TypeType = None
) -> ListAnalyzersResponseTypeDef:
    pass
```

### list_archive_rules

Type annotations for `boto3.client("accessanalyzer").list_archive_rules` method.

[Client.list_archive_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_archive_rules)

```python
def list_archive_rules(
    self,
    analyzerName: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListArchiveRulesResponseTypeDef:
    pass
```

### list_findings

Type annotations for `boto3.client("accessanalyzer").list_findings` method.

[Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_findings)

```python
def list_findings(
    self,
    analyzerArn: str,
    filter: Dict[str, "CriterionTypeDef"] = None,
    maxResults: int = None,
    nextToken: str = None,
    sort: SortCriteriaTypeDef = None
) -> ListFindingsResponseTypeDef:
    pass
```

### list_policy_generations

Type annotations for `boto3.client("accessanalyzer").list_policy_generations` method.

[Client.list_policy_generations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_policy_generations)

```python
def list_policy_generations(
    self,
    maxResults: int = None,
    nextToken: str = None,
    principalArn: str = None
) -> ListPolicyGenerationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("accessanalyzer").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_policy_generation

Type annotations for `boto3.client("accessanalyzer").start_policy_generation` method.

[Client.start_policy_generation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_policy_generation)

```python
def start_policy_generation(
    self,
    policyGenerationDetails: PolicyGenerationDetailsTypeDef,
    clientToken: str = None,
    cloudTrailDetails: CloudTrailDetailsTypeDef = None
) -> StartPolicyGenerationResponseTypeDef:
    pass
```

### start_resource_scan

Type annotations for `boto3.client("accessanalyzer").start_resource_scan` method.

[Client.start_resource_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_resource_scan)

```python
def start_resource_scan(
    self,
    analyzerArn: str,
    resourceArn: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("accessanalyzer").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("accessanalyzer").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_archive_rule

Type annotations for `boto3.client("accessanalyzer").update_archive_rule` method.

[Client.update_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_archive_rule)

```python
def update_archive_rule(
    self,
    analyzerName: str,
    filter: Dict[str, "CriterionTypeDef"],
    ruleName: str,
    clientToken: str = None
) -> None:
    pass
```

### update_findings

Type annotations for `boto3.client("accessanalyzer").update_findings` method.

[Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_findings)

```python
def update_findings(
    self,
    analyzerArn: str,
    status: FindingStatusUpdate,
    clientToken: str = None,
    ids: List[str] = None,
    resourceArn: str = None
) -> None:
    pass
```

### validate_policy

Type annotations for `boto3.client("accessanalyzer").validate_policy` method.

[Client.validate_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html#AccessAnalyzer.Client.validate_policy)

```python
def validate_policy(
    self,
    policyDocument: str,
    policyType: PolicyType,
    locale: Locale = None,
    maxResults: int = None,
    nextToken: str = None
) -> ValidatePolicyResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("accessanalyzer").get_paginator` method with overloads.

- `client.get_paginator("list_access_preview_findings")` -> [ListAccessPreviewFindingsPaginator](./paginators.md#listaccesspreviewfindingspaginator)
- `client.get_paginator("list_access_previews")` -> [ListAccessPreviewsPaginator](./paginators.md#listaccesspreviewspaginator)
- `client.get_paginator("list_analyzed_resources")` -> [ListAnalyzedResourcesPaginator](./paginators.md#listanalyzedresourcespaginator)
- `client.get_paginator("list_analyzers")` -> [ListAnalyzersPaginator](./paginators.md#listanalyzerspaginator)
- `client.get_paginator("list_archive_rules")` -> [ListArchiveRulesPaginator](./paginators.md#listarchiverulespaginator)
- `client.get_paginator("list_findings")` -> [ListFindingsPaginator](./paginators.md#listfindingspaginator)
- `client.get_paginator("list_policy_generations")` -> [ListPolicyGenerationsPaginator](./paginators.md#listpolicygenerationspaginator)
- `client.get_paginator("validate_policy")` -> [ValidatePolicyPaginator](./paginators.md#validatepolicypaginator)


