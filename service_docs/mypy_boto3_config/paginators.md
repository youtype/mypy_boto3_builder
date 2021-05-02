# Paginators for boto3 ConfigService module

> [Index](../index.md) > [ConfigService](./index.md) > Paginators

Auto-generated documentation for [ConfigService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService)
type annotations stubs module [mypy_boto3_config](https://pypi.org/project/mypy-boto3-config/).

- [Paginators for boto3 ConfigService module](#paginators-for-boto3-configservice-module)
  - [DescribeAggregateComplianceByConfigRulesPaginator](#describeaggregatecompliancebyconfigrulespaginator)
  - [DescribeAggregationAuthorizationsPaginator](#describeaggregationauthorizationspaginator)
  - [DescribeComplianceByConfigRulePaginator](#describecompliancebyconfigrulepaginator)
  - [DescribeComplianceByResourcePaginator](#describecompliancebyresourcepaginator)
  - [DescribeConfigRuleEvaluationStatusPaginator](#describeconfigruleevaluationstatuspaginator)
  - [DescribeConfigRulesPaginator](#describeconfigrulespaginator)
  - [DescribeConfigurationAggregatorSourcesStatusPaginator](#describeconfigurationaggregatorsourcesstatuspaginator)
  - [DescribeConfigurationAggregatorsPaginator](#describeconfigurationaggregatorspaginator)
  - [DescribePendingAggregationRequestsPaginator](#describependingaggregationrequestspaginator)
  - [DescribeRemediationExecutionStatusPaginator](#describeremediationexecutionstatuspaginator)
  - [DescribeRetentionConfigurationsPaginator](#describeretentionconfigurationspaginator)
  - [GetAggregateComplianceDetailsByConfigRulePaginator](#getaggregatecompliancedetailsbyconfigrulepaginator)
  - [GetComplianceDetailsByConfigRulePaginator](#getcompliancedetailsbyconfigrulepaginator)
  - [GetComplianceDetailsByResourcePaginator](#getcompliancedetailsbyresourcepaginator)
  - [GetResourceConfigHistoryPaginator](#getresourceconfighistorypaginator)
  - [ListAggregateDiscoveredResourcesPaginator](#listaggregatediscoveredresourcespaginator)
  - [ListDiscoveredResourcesPaginator](#listdiscoveredresourcespaginator)

## DescribeAggregateComplianceByConfigRulesPaginator

Type annotations for `boto3.client("config").get_paginator("describe_aggregate_compliance_by_config_rules")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeAggregateComplianceByConfigRulesPaginator

def get_describe_aggregate_compliance_by_config_rules_paginator() -> DescribeAggregateComplianceByConfigRulesPaginator:
    return boto3.client("config").get_paginator("describe_aggregate_compliance_by_config_rules")
```

[Paginator.DescribeAggregateComplianceByConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)

```python
class DescribeAggregateComplianceByConfigRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAggregateComplianceByConfigRulesResponseTypeDef]:
        pass
```
## DescribeAggregationAuthorizationsPaginator

Type annotations for `boto3.client("config").get_paginator("describe_aggregation_authorizations")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeAggregationAuthorizationsPaginator

def get_describe_aggregation_authorizations_paginator() -> DescribeAggregationAuthorizationsPaginator:
    return boto3.client("config").get_paginator("describe_aggregation_authorizations")
```

[Paginator.DescribeAggregationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)

```python
class DescribeAggregationAuthorizationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAggregationAuthorizationsResponseTypeDef]:
        pass
```
## DescribeComplianceByConfigRulePaginator

Type annotations for `boto3.client("config").get_paginator("describe_compliance_by_config_rule")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeComplianceByConfigRulePaginator

def get_describe_compliance_by_config_rule_paginator() -> DescribeComplianceByConfigRulePaginator:
    return boto3.client("config").get_paginator("describe_compliance_by_config_rule")
```

[Paginator.DescribeComplianceByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)

```python
class DescribeComplianceByConfigRulePaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[ComplianceType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeComplianceByConfigRuleResponseTypeDef]:
        pass
```
## DescribeComplianceByResourcePaginator

Type annotations for `boto3.client("config").get_paginator("describe_compliance_by_resource")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeComplianceByResourcePaginator

def get_describe_compliance_by_resource_paginator() -> DescribeComplianceByResourcePaginator:
    return boto3.client("config").get_paginator("describe_compliance_by_resource")
```

[Paginator.DescribeComplianceByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)

```python
class DescribeComplianceByResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[ComplianceType] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeComplianceByResourceResponseTypeDef]:
        pass
```
## DescribeConfigRuleEvaluationStatusPaginator

Type annotations for `boto3.client("config").get_paginator("describe_config_rule_evaluation_status")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeConfigRuleEvaluationStatusPaginator

def get_describe_config_rule_evaluation_status_paginator() -> DescribeConfigRuleEvaluationStatusPaginator:
    return boto3.client("config").get_paginator("describe_config_rule_evaluation_status")
```

[Paginator.DescribeConfigRuleEvaluationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)

```python
class DescribeConfigRuleEvaluationStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigRuleEvaluationStatusResponseTypeDef]:
        pass
```
## DescribeConfigRulesPaginator

Type annotations for `boto3.client("config").get_paginator("describe_config_rules")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeConfigRulesPaginator

def get_describe_config_rules_paginator() -> DescribeConfigRulesPaginator:
    return boto3.client("config").get_paginator("describe_config_rules")
```

[Paginator.DescribeConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)

```python
class DescribeConfigRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigRuleNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigRulesResponseTypeDef]:
        pass
```
## DescribeConfigurationAggregatorSourcesStatusPaginator

Type annotations for `boto3.client("config").get_paginator("describe_configuration_aggregator_sources_status")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeConfigurationAggregatorSourcesStatusPaginator

def get_describe_configuration_aggregator_sources_status_paginator() -> DescribeConfigurationAggregatorSourcesStatusPaginator:
    return boto3.client("config").get_paginator("describe_configuration_aggregator_sources_status")
```

[Paginator.DescribeConfigurationAggregatorSourcesStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)

```python
class DescribeConfigurationAggregatorSourcesStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[AggregatedSourceStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigurationAggregatorSourcesStatusResponseTypeDef]:
        pass
```
## DescribeConfigurationAggregatorsPaginator

Type annotations for `boto3.client("config").get_paginator("describe_configuration_aggregators")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeConfigurationAggregatorsPaginator

def get_describe_configuration_aggregators_paginator() -> DescribeConfigurationAggregatorsPaginator:
    return boto3.client("config").get_paginator("describe_configuration_aggregators")
```

[Paginator.DescribeConfigurationAggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)

```python
class DescribeConfigurationAggregatorsPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeConfigurationAggregatorsResponseTypeDef]:
        pass
```
## DescribePendingAggregationRequestsPaginator

Type annotations for `boto3.client("config").get_paginator("describe_pending_aggregation_requests")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribePendingAggregationRequestsPaginator

def get_describe_pending_aggregation_requests_paginator() -> DescribePendingAggregationRequestsPaginator:
    return boto3.client("config").get_paginator("describe_pending_aggregation_requests")
```

[Paginator.DescribePendingAggregationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)

```python
class DescribePendingAggregationRequestsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePendingAggregationRequestsResponseTypeDef]:
        pass
```
## DescribeRemediationExecutionStatusPaginator

Type annotations for `boto3.client("config").get_paginator("describe_remediation_execution_status")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeRemediationExecutionStatusPaginator

def get_describe_remediation_execution_status_paginator() -> DescribeRemediationExecutionStatusPaginator:
    return boto3.client("config").get_paginator("describe_remediation_execution_status")
```

[Paginator.DescribeRemediationExecutionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)

```python
class DescribeRemediationExecutionStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigRuleName: str,
        ResourceKeys: List["ResourceKeyTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRemediationExecutionStatusResponseTypeDef]:
        pass
```
## DescribeRetentionConfigurationsPaginator

Type annotations for `boto3.client("config").get_paginator("describe_retention_configurations")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import DescribeRetentionConfigurationsPaginator

def get_describe_retention_configurations_paginator() -> DescribeRetentionConfigurationsPaginator:
    return boto3.client("config").get_paginator("describe_retention_configurations")
```

[Paginator.DescribeRetentionConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)

```python
class DescribeRetentionConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        RetentionConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRetentionConfigurationsResponseTypeDef]:
        pass
```
## GetAggregateComplianceDetailsByConfigRulePaginator

Type annotations for `boto3.client("config").get_paginator("get_aggregate_compliance_details_by_config_rule")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import GetAggregateComplianceDetailsByConfigRulePaginator

def get_get_aggregate_compliance_details_by_config_rule_paginator() -> GetAggregateComplianceDetailsByConfigRulePaginator:
    return boto3.client("config").get_paginator("get_aggregate_compliance_details_by_config_rule")
```

[Paginator.GetAggregateComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)

```python
class GetAggregateComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: ComplianceType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAggregateComplianceDetailsByConfigRuleResponseTypeDef]:
        pass
```
## GetComplianceDetailsByConfigRulePaginator

Type annotations for `boto3.client("config").get_paginator("get_compliance_details_by_config_rule")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import GetComplianceDetailsByConfigRulePaginator

def get_get_compliance_details_by_config_rule_paginator() -> GetComplianceDetailsByConfigRulePaginator:
    return boto3.client("config").get_paginator("get_compliance_details_by_config_rule")
```

[Paginator.GetComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)

```python
class GetComplianceDetailsByConfigRulePaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[ComplianceType] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetComplianceDetailsByConfigRuleResponseTypeDef]:
        pass
```
## GetComplianceDetailsByResourcePaginator

Type annotations for `boto3.client("config").get_paginator("get_compliance_details_by_resource")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import GetComplianceDetailsByResourcePaginator

def get_get_compliance_details_by_resource_paginator() -> GetComplianceDetailsByResourcePaginator:
    return boto3.client("config").get_paginator("get_compliance_details_by_resource")
```

[Paginator.GetComplianceDetailsByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)

```python
class GetComplianceDetailsByResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[ComplianceType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetComplianceDetailsByResourceResponseTypeDef]:
        pass
```
## GetResourceConfigHistoryPaginator

Type annotations for `boto3.client("config").get_paginator("get_resource_config_history")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import GetResourceConfigHistoryPaginator

def get_get_resource_config_history_paginator() -> GetResourceConfigHistoryPaginator:
    return boto3.client("config").get_paginator("get_resource_config_history")
```

[Paginator.GetResourceConfigHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)

```python
class GetResourceConfigHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceType: ResourceType,
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: ChronologicalOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceConfigHistoryResponseTypeDef]:
        pass
```
## ListAggregateDiscoveredResourcesPaginator

Type annotations for `boto3.client("config").get_paginator("list_aggregate_discovered_resources")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import ListAggregateDiscoveredResourcesPaginator

def get_list_aggregate_discovered_resources_paginator() -> ListAggregateDiscoveredResourcesPaginator:
    return boto3.client("config").get_paginator("list_aggregate_discovered_resources")
```

[Paginator.ListAggregateDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)

```python
class ListAggregateDiscoveredResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: ResourceType,
        Filters: ResourceFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAggregateDiscoveredResourcesResponseTypeDef]:
        pass
```
## ListDiscoveredResourcesPaginator

Type annotations for `boto3.client("config").get_paginator("list_discovered_resources")`.

Can be used directly:

```python
from mypy_boto3_config.paginators import ListDiscoveredResourcesPaginator

def get_list_discovered_resources_paginator() -> ListDiscoveredResourcesPaginator:
    return boto3.client("config").get_paginator("list_discovered_resources")
```

[Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)

```python
class ListDiscoveredResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        resourceType: ResourceType,
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDiscoveredResourcesResponseTypeDef]:
        pass
```