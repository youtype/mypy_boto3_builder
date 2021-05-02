# ConfigServiceClient for boto3 ConfigService module

> [Index](../index.md) > [ConfigService](./index.md) > ConfigServiceClient

Auto-generated documentation for [ConfigService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService)
type annotations stubs module [mypy_boto3_config](https://pypi.org/project/mypy-boto3-config/).

- [ConfigServiceClient for boto3 ConfigService module](#configserviceclient-for-boto3-configservice-module)
  - [ConfigServiceClient](#configserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_get_aggregate_resource_config](#batch_get_aggregate_resource_config)
    - [batch_get_resource_config](#batch_get_resource_config)
    - [can_paginate](#can_paginate)
    - [delete_aggregation_authorization](#delete_aggregation_authorization)
    - [delete_config_rule](#delete_config_rule)
    - [delete_configuration_aggregator](#delete_configuration_aggregator)
    - [delete_configuration_recorder](#delete_configuration_recorder)
    - [delete_conformance_pack](#delete_conformance_pack)
    - [delete_delivery_channel](#delete_delivery_channel)
    - [delete_evaluation_results](#delete_evaluation_results)
    - [delete_organization_config_rule](#delete_organization_config_rule)
    - [delete_organization_conformance_pack](#delete_organization_conformance_pack)
    - [delete_pending_aggregation_request](#delete_pending_aggregation_request)
    - [delete_remediation_configuration](#delete_remediation_configuration)
    - [delete_remediation_exceptions](#delete_remediation_exceptions)
    - [delete_resource_config](#delete_resource_config)
    - [delete_retention_configuration](#delete_retention_configuration)
    - [delete_stored_query](#delete_stored_query)
    - [deliver_config_snapshot](#deliver_config_snapshot)
    - [describe_aggregate_compliance_by_config_rules](#describe_aggregate_compliance_by_config_rules)
    - [describe_aggregate_compliance_by_conformance_packs](#describe_aggregate_compliance_by_conformance_packs)
    - [describe_aggregation_authorizations](#describe_aggregation_authorizations)
    - [describe_compliance_by_config_rule](#describe_compliance_by_config_rule)
    - [describe_compliance_by_resource](#describe_compliance_by_resource)
    - [describe_config_rule_evaluation_status](#describe_config_rule_evaluation_status)
    - [describe_config_rules](#describe_config_rules)
    - [describe_configuration_aggregator_sources_status](#describe_configuration_aggregator_sources_status)
    - [describe_configuration_aggregators](#describe_configuration_aggregators)
    - [describe_configuration_recorder_status](#describe_configuration_recorder_status)
    - [describe_configuration_recorders](#describe_configuration_recorders)
    - [describe_conformance_pack_compliance](#describe_conformance_pack_compliance)
    - [describe_conformance_pack_status](#describe_conformance_pack_status)
    - [describe_conformance_packs](#describe_conformance_packs)
    - [describe_delivery_channel_status](#describe_delivery_channel_status)
    - [describe_delivery_channels](#describe_delivery_channels)
    - [describe_organization_config_rule_statuses](#describe_organization_config_rule_statuses)
    - [describe_organization_config_rules](#describe_organization_config_rules)
    - [describe_organization_conformance_pack_statuses](#describe_organization_conformance_pack_statuses)
    - [describe_organization_conformance_packs](#describe_organization_conformance_packs)
    - [describe_pending_aggregation_requests](#describe_pending_aggregation_requests)
    - [describe_remediation_configurations](#describe_remediation_configurations)
    - [describe_remediation_exceptions](#describe_remediation_exceptions)
    - [describe_remediation_execution_status](#describe_remediation_execution_status)
    - [describe_retention_configurations](#describe_retention_configurations)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_aggregate_compliance_details_by_config_rule](#get_aggregate_compliance_details_by_config_rule)
    - [get_aggregate_config_rule_compliance_summary](#get_aggregate_config_rule_compliance_summary)
    - [get_aggregate_conformance_pack_compliance_summary](#get_aggregate_conformance_pack_compliance_summary)
    - [get_aggregate_discovered_resource_counts](#get_aggregate_discovered_resource_counts)
    - [get_aggregate_resource_config](#get_aggregate_resource_config)
    - [get_compliance_details_by_config_rule](#get_compliance_details_by_config_rule)
    - [get_compliance_details_by_resource](#get_compliance_details_by_resource)
    - [get_compliance_summary_by_config_rule](#get_compliance_summary_by_config_rule)
    - [get_compliance_summary_by_resource_type](#get_compliance_summary_by_resource_type)
    - [get_conformance_pack_compliance_details](#get_conformance_pack_compliance_details)
    - [get_conformance_pack_compliance_summary](#get_conformance_pack_compliance_summary)
    - [get_discovered_resource_counts](#get_discovered_resource_counts)
    - [get_organization_config_rule_detailed_status](#get_organization_config_rule_detailed_status)
    - [get_organization_conformance_pack_detailed_status](#get_organization_conformance_pack_detailed_status)
    - [get_resource_config_history](#get_resource_config_history)
    - [get_stored_query](#get_stored_query)
    - [list_aggregate_discovered_resources](#list_aggregate_discovered_resources)
    - [list_discovered_resources](#list_discovered_resources)
    - [list_stored_queries](#list_stored_queries)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_aggregation_authorization](#put_aggregation_authorization)
    - [put_config_rule](#put_config_rule)
    - [put_configuration_aggregator](#put_configuration_aggregator)
    - [put_configuration_recorder](#put_configuration_recorder)
    - [put_conformance_pack](#put_conformance_pack)
    - [put_delivery_channel](#put_delivery_channel)
    - [put_evaluations](#put_evaluations)
    - [put_external_evaluation](#put_external_evaluation)
    - [put_organization_config_rule](#put_organization_config_rule)
    - [put_organization_conformance_pack](#put_organization_conformance_pack)
    - [put_remediation_configurations](#put_remediation_configurations)
    - [put_remediation_exceptions](#put_remediation_exceptions)
    - [put_resource_config](#put_resource_config)
    - [put_retention_configuration](#put_retention_configuration)
    - [put_stored_query](#put_stored_query)
    - [select_aggregate_resource_config](#select_aggregate_resource_config)
    - [select_resource_config](#select_resource_config)
    - [start_config_rules_evaluation](#start_config_rules_evaluation)
    - [start_configuration_recorder](#start_configuration_recorder)
    - [start_remediation_execution](#start_remediation_execution)
    - [stop_configuration_recorder](#stop_configuration_recorder)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)

## ConfigServiceClient

Type annotations for `boto3.client("config")`

Can be used directly:

```python
from mypy_boto3_config.client import ConfigServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_config.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConformancePackTemplateValidationException`
- `Exceptions.InsufficientDeliveryPolicyException`
- `Exceptions.InsufficientPermissionsException`
- `Exceptions.InvalidConfigurationRecorderNameException`
- `Exceptions.InvalidDeliveryChannelNameException`
- `Exceptions.InvalidExpressionException`
- `Exceptions.InvalidLimitException`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidRecordingGroupException`
- `Exceptions.InvalidResultTokenException`
- `Exceptions.InvalidRoleException`
- `Exceptions.InvalidS3KeyPrefixException`
- `Exceptions.InvalidS3KmsKeyArnException`
- `Exceptions.InvalidSNSTopicARNException`
- `Exceptions.InvalidTimeRangeException`
- `Exceptions.LastDeliveryChannelDeleteFailedException`
- `Exceptions.LimitExceededException`
- `Exceptions.MaxActiveResourcesExceededException`
- `Exceptions.MaxNumberOfConfigRulesExceededException`
- `Exceptions.MaxNumberOfConfigurationRecordersExceededException`
- `Exceptions.MaxNumberOfConformancePacksExceededException`
- `Exceptions.MaxNumberOfDeliveryChannelsExceededException`
- `Exceptions.MaxNumberOfOrganizationConfigRulesExceededException`
- `Exceptions.MaxNumberOfOrganizationConformancePacksExceededException`
- `Exceptions.MaxNumberOfRetentionConfigurationsExceededException`
- `Exceptions.NoAvailableConfigurationRecorderException`
- `Exceptions.NoAvailableDeliveryChannelException`
- `Exceptions.NoAvailableOrganizationException`
- `Exceptions.NoRunningConfigurationRecorderException`
- `Exceptions.NoSuchBucketException`
- `Exceptions.NoSuchConfigRuleException`
- `Exceptions.NoSuchConfigRuleInConformancePackException`
- `Exceptions.NoSuchConfigurationAggregatorException`
- `Exceptions.NoSuchConfigurationRecorderException`
- `Exceptions.NoSuchConformancePackException`
- `Exceptions.NoSuchDeliveryChannelException`
- `Exceptions.NoSuchOrganizationConfigRuleException`
- `Exceptions.NoSuchOrganizationConformancePackException`
- `Exceptions.NoSuchRemediationConfigurationException`
- `Exceptions.NoSuchRemediationExceptionException`
- `Exceptions.NoSuchRetentionConfigurationException`
- `Exceptions.OrganizationAccessDeniedException`
- `Exceptions.OrganizationAllFeaturesNotEnabledException`
- `Exceptions.OrganizationConformancePackTemplateValidationException`
- `Exceptions.OversizedConfigurationItemException`
- `Exceptions.RemediationInProgressException`
- `Exceptions.ResourceConcurrentModificationException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotDiscoveredException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.TooManyTagsException`
- `Exceptions.ValidationException`


## Methods


### batch_get_aggregate_resource_config

Type annotations for `boto3.client("config").batch_get_aggregate_resource_config` method.

[Client.batch_get_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.batch_get_aggregate_resource_config)

```python
def batch_get_aggregate_resource_config(
    self,
    ConfigurationAggregatorName: str,
    ResourceIdentifiers: List["AggregateResourceIdentifierTypeDef"]
) -> BatchGetAggregateResourceConfigResponseTypeDef:
    pass
```

### batch_get_resource_config

Type annotations for `boto3.client("config").batch_get_resource_config` method.

[Client.batch_get_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.batch_get_resource_config)

```python
def batch_get_resource_config(
    self,
    resourceKeys: List["ResourceKeyTypeDef"]
) -> BatchGetResourceConfigResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("config").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### delete_aggregation_authorization

Type annotations for `boto3.client("config").delete_aggregation_authorization` method.

[Client.delete_aggregation_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_aggregation_authorization)

```python
def delete_aggregation_authorization(
    self,
    AuthorizedAccountId: str,
    AuthorizedAwsRegion: str
) -> None:
    pass
```

### delete_config_rule

Type annotations for `boto3.client("config").delete_config_rule` method.

[Client.delete_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_config_rule)

```python
def delete_config_rule(
    self,
    ConfigRuleName: str
) -> None:
    pass
```

### delete_configuration_aggregator

Type annotations for `boto3.client("config").delete_configuration_aggregator` method.

[Client.delete_configuration_aggregator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_configuration_aggregator)

```python
def delete_configuration_aggregator(
    self,
    ConfigurationAggregatorName: str
) -> None:
    pass
```

### delete_configuration_recorder

Type annotations for `boto3.client("config").delete_configuration_recorder` method.

[Client.delete_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_configuration_recorder)

```python
def delete_configuration_recorder(
    self,
    ConfigurationRecorderName: str
) -> None:
    pass
```

### delete_conformance_pack

Type annotations for `boto3.client("config").delete_conformance_pack` method.

[Client.delete_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_conformance_pack)

```python
def delete_conformance_pack(
    self,
    ConformancePackName: str
) -> None:
    pass
```

### delete_delivery_channel

Type annotations for `boto3.client("config").delete_delivery_channel` method.

[Client.delete_delivery_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_delivery_channel)

```python
def delete_delivery_channel(
    self,
    DeliveryChannelName: str
) -> None:
    pass
```

### delete_evaluation_results

Type annotations for `boto3.client("config").delete_evaluation_results` method.

[Client.delete_evaluation_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_evaluation_results)

```python
def delete_evaluation_results(
    self,
    ConfigRuleName: str
) -> Dict[str, Any]:
    pass
```

### delete_organization_config_rule

Type annotations for `boto3.client("config").delete_organization_config_rule` method.

[Client.delete_organization_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_organization_config_rule)

```python
def delete_organization_config_rule(
    self,
    OrganizationConfigRuleName: str
) -> None:
    pass
```

### delete_organization_conformance_pack

Type annotations for `boto3.client("config").delete_organization_conformance_pack` method.

[Client.delete_organization_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_organization_conformance_pack)

```python
def delete_organization_conformance_pack(
    self,
    OrganizationConformancePackName: str
) -> None:
    pass
```

### delete_pending_aggregation_request

Type annotations for `boto3.client("config").delete_pending_aggregation_request` method.

[Client.delete_pending_aggregation_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_pending_aggregation_request)

```python
def delete_pending_aggregation_request(
    self,
    RequesterAccountId: str,
    RequesterAwsRegion: str
) -> None:
    pass
```

### delete_remediation_configuration

Type annotations for `boto3.client("config").delete_remediation_configuration` method.

[Client.delete_remediation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_remediation_configuration)

```python
def delete_remediation_configuration(
    self,
    ConfigRuleName: str,
    ResourceType: str = None
) -> Dict[str, Any]:
    pass
```

### delete_remediation_exceptions

Type annotations for `boto3.client("config").delete_remediation_exceptions` method.

[Client.delete_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_remediation_exceptions)

```python
def delete_remediation_exceptions(
    self,
    ConfigRuleName: str,
    ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"]
) -> DeleteRemediationExceptionsResponseTypeDef:
    pass
```

### delete_resource_config

Type annotations for `boto3.client("config").delete_resource_config` method.

[Client.delete_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_resource_config)

```python
def delete_resource_config(
    self,
    ResourceType: str,
    ResourceId: str
) -> None:
    pass
```

### delete_retention_configuration

Type annotations for `boto3.client("config").delete_retention_configuration` method.

[Client.delete_retention_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_retention_configuration)

```python
def delete_retention_configuration(
    self,
    RetentionConfigurationName: str
) -> None:
    pass
```

### delete_stored_query

Type annotations for `boto3.client("config").delete_stored_query` method.

[Client.delete_stored_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.delete_stored_query)

```python
def delete_stored_query(
    self,
    QueryName: str
) -> Dict[str, Any]:
    pass
```

### deliver_config_snapshot

Type annotations for `boto3.client("config").deliver_config_snapshot` method.

[Client.deliver_config_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.deliver_config_snapshot)

```python
def deliver_config_snapshot(
    self,
    deliveryChannelName: str
) -> DeliverConfigSnapshotResponseTypeDef:
    pass
```

### describe_aggregate_compliance_by_config_rules

Type annotations for `boto3.client("config").describe_aggregate_compliance_by_config_rules` method.

[Client.describe_aggregate_compliance_by_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_aggregate_compliance_by_config_rules)

```python
def describe_aggregate_compliance_by_config_rules(
    self,
    ConfigurationAggregatorName: str,
    Filters: ConfigRuleComplianceFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeAggregateComplianceByConfigRulesResponseTypeDef:
    pass
```

### describe_aggregate_compliance_by_conformance_packs

Type annotations for `boto3.client("config").describe_aggregate_compliance_by_conformance_packs` method.

[Client.describe_aggregate_compliance_by_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_aggregate_compliance_by_conformance_packs)

```python
def describe_aggregate_compliance_by_conformance_packs(
    self,
    ConfigurationAggregatorName: str,
    Filters: AggregateConformancePackComplianceFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeAggregateComplianceByConformancePacksResponseTypeDef:
    pass
```

### describe_aggregation_authorizations

Type annotations for `boto3.client("config").describe_aggregation_authorizations` method.

[Client.describe_aggregation_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_aggregation_authorizations)

```python
def describe_aggregation_authorizations(
    self,
    Limit: int = None,
    NextToken: str = None
) -> DescribeAggregationAuthorizationsResponseTypeDef:
    pass
```

### describe_compliance_by_config_rule

Type annotations for `boto3.client("config").describe_compliance_by_config_rule` method.

[Client.describe_compliance_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_compliance_by_config_rule)

```python
def describe_compliance_by_config_rule(
    self,
    ConfigRuleNames: List[str] = None,
    ComplianceTypes: List[ComplianceType] = None,
    NextToken: str = None
) -> DescribeComplianceByConfigRuleResponseTypeDef:
    pass
```

### describe_compliance_by_resource

Type annotations for `boto3.client("config").describe_compliance_by_resource` method.

[Client.describe_compliance_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_compliance_by_resource)

```python
def describe_compliance_by_resource(
    self,
    ResourceType: str = None,
    ResourceId: str = None,
    ComplianceTypes: List[ComplianceType] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeComplianceByResourceResponseTypeDef:
    pass
```

### describe_config_rule_evaluation_status

Type annotations for `boto3.client("config").describe_config_rule_evaluation_status` method.

[Client.describe_config_rule_evaluation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_config_rule_evaluation_status)

```python
def describe_config_rule_evaluation_status(
    self,
    ConfigRuleNames: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeConfigRuleEvaluationStatusResponseTypeDef:
    pass
```

### describe_config_rules

Type annotations for `boto3.client("config").describe_config_rules` method.

[Client.describe_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_config_rules)

```python
def describe_config_rules(
    self,
    ConfigRuleNames: List[str] = None,
    NextToken: str = None
) -> DescribeConfigRulesResponseTypeDef:
    pass
```

### describe_configuration_aggregator_sources_status

Type annotations for `boto3.client("config").describe_configuration_aggregator_sources_status` method.

[Client.describe_configuration_aggregator_sources_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_configuration_aggregator_sources_status)

```python
def describe_configuration_aggregator_sources_status(
    self,
    ConfigurationAggregatorName: str,
    UpdateStatus: List[AggregatedSourceStatusType] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeConfigurationAggregatorSourcesStatusResponseTypeDef:
    pass
```

### describe_configuration_aggregators

Type annotations for `boto3.client("config").describe_configuration_aggregators` method.

[Client.describe_configuration_aggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_configuration_aggregators)

```python
def describe_configuration_aggregators(
    self,
    ConfigurationAggregatorNames: List[str] = None,
    NextToken: str = None,
    Limit: int = None
) -> DescribeConfigurationAggregatorsResponseTypeDef:
    pass
```

### describe_configuration_recorder_status

Type annotations for `boto3.client("config").describe_configuration_recorder_status` method.

[Client.describe_configuration_recorder_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_configuration_recorder_status)

```python
def describe_configuration_recorder_status(
    self,
    ConfigurationRecorderNames: List[str] = None
) -> DescribeConfigurationRecorderStatusResponseTypeDef:
    pass
```

### describe_configuration_recorders

Type annotations for `boto3.client("config").describe_configuration_recorders` method.

[Client.describe_configuration_recorders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_configuration_recorders)

```python
def describe_configuration_recorders(
    self,
    ConfigurationRecorderNames: List[str] = None
) -> DescribeConfigurationRecordersResponseTypeDef:
    pass
```

### describe_conformance_pack_compliance

Type annotations for `boto3.client("config").describe_conformance_pack_compliance` method.

[Client.describe_conformance_pack_compliance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_conformance_pack_compliance)

```python
def describe_conformance_pack_compliance(
    self,
    ConformancePackName: str,
    Filters: ConformancePackComplianceFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeConformancePackComplianceResponseTypeDef:
    pass
```

### describe_conformance_pack_status

Type annotations for `boto3.client("config").describe_conformance_pack_status` method.

[Client.describe_conformance_pack_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_conformance_pack_status)

```python
def describe_conformance_pack_status(
    self,
    ConformancePackNames: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeConformancePackStatusResponseTypeDef:
    pass
```

### describe_conformance_packs

Type annotations for `boto3.client("config").describe_conformance_packs` method.

[Client.describe_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_conformance_packs)

```python
def describe_conformance_packs(
    self,
    ConformancePackNames: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeConformancePacksResponseTypeDef:
    pass
```

### describe_delivery_channel_status

Type annotations for `boto3.client("config").describe_delivery_channel_status` method.

[Client.describe_delivery_channel_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_delivery_channel_status)

```python
def describe_delivery_channel_status(
    self,
    DeliveryChannelNames: List[str] = None
) -> DescribeDeliveryChannelStatusResponseTypeDef:
    pass
```

### describe_delivery_channels

Type annotations for `boto3.client("config").describe_delivery_channels` method.

[Client.describe_delivery_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_delivery_channels)

```python
def describe_delivery_channels(
    self,
    DeliveryChannelNames: List[str] = None
) -> DescribeDeliveryChannelsResponseTypeDef:
    pass
```

### describe_organization_config_rule_statuses

Type annotations for `boto3.client("config").describe_organization_config_rule_statuses` method.

[Client.describe_organization_config_rule_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_organization_config_rule_statuses)

```python
def describe_organization_config_rule_statuses(
    self,
    OrganizationConfigRuleNames: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeOrganizationConfigRuleStatusesResponseTypeDef:
    pass
```

### describe_organization_config_rules

Type annotations for `boto3.client("config").describe_organization_config_rules` method.

[Client.describe_organization_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_organization_config_rules)

```python
def describe_organization_config_rules(
    self,
    OrganizationConfigRuleNames: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeOrganizationConfigRulesResponseTypeDef:
    pass
```

### describe_organization_conformance_pack_statuses

Type annotations for `boto3.client("config").describe_organization_conformance_pack_statuses` method.

[Client.describe_organization_conformance_pack_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_organization_conformance_pack_statuses)

```python
def describe_organization_conformance_pack_statuses(
    self,
    OrganizationConformancePackNames: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeOrganizationConformancePackStatusesResponseTypeDef:
    pass
```

### describe_organization_conformance_packs

Type annotations for `boto3.client("config").describe_organization_conformance_packs` method.

[Client.describe_organization_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_organization_conformance_packs)

```python
def describe_organization_conformance_packs(
    self,
    OrganizationConformancePackNames: List[str] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeOrganizationConformancePacksResponseTypeDef:
    pass
```

### describe_pending_aggregation_requests

Type annotations for `boto3.client("config").describe_pending_aggregation_requests` method.

[Client.describe_pending_aggregation_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_pending_aggregation_requests)

```python
def describe_pending_aggregation_requests(
    self,
    Limit: int = None,
    NextToken: str = None
) -> DescribePendingAggregationRequestsResponseTypeDef:
    pass
```

### describe_remediation_configurations

Type annotations for `boto3.client("config").describe_remediation_configurations` method.

[Client.describe_remediation_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_remediation_configurations)

```python
def describe_remediation_configurations(
    self,
    ConfigRuleNames: List[str]
) -> DescribeRemediationConfigurationsResponseTypeDef:
    pass
```

### describe_remediation_exceptions

Type annotations for `boto3.client("config").describe_remediation_exceptions` method.

[Client.describe_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_remediation_exceptions)

```python
def describe_remediation_exceptions(
    self,
    ConfigRuleName: str,
    ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeRemediationExceptionsResponseTypeDef:
    pass
```

### describe_remediation_execution_status

Type annotations for `boto3.client("config").describe_remediation_execution_status` method.

[Client.describe_remediation_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_remediation_execution_status)

```python
def describe_remediation_execution_status(
    self,
    ConfigRuleName: str,
    ResourceKeys: List["ResourceKeyTypeDef"] = None,
    Limit: int = None,
    NextToken: str = None
) -> DescribeRemediationExecutionStatusResponseTypeDef:
    pass
```

### describe_retention_configurations

Type annotations for `boto3.client("config").describe_retention_configurations` method.

[Client.describe_retention_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_retention_configurations)

```python
def describe_retention_configurations(
    self,
    RetentionConfigurationNames: List[str] = None,
    NextToken: str = None
) -> DescribeRetentionConfigurationsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("config").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.generate_presigned_url)

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

### get_aggregate_compliance_details_by_config_rule

Type annotations for `boto3.client("config").get_aggregate_compliance_details_by_config_rule` method.

[Client.get_aggregate_compliance_details_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_aggregate_compliance_details_by_config_rule)

```python
def get_aggregate_compliance_details_by_config_rule(
    self,
    ConfigurationAggregatorName: str,
    ConfigRuleName: str,
    AccountId: str,
    AwsRegion: str,
    ComplianceType: ComplianceType = None,
    Limit: int = None,
    NextToken: str = None
) -> GetAggregateComplianceDetailsByConfigRuleResponseTypeDef:
    pass
```

### get_aggregate_config_rule_compliance_summary

Type annotations for `boto3.client("config").get_aggregate_config_rule_compliance_summary` method.

[Client.get_aggregate_config_rule_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_aggregate_config_rule_compliance_summary)

```python
def get_aggregate_config_rule_compliance_summary(
    self,
    ConfigurationAggregatorName: str,
    Filters: ConfigRuleComplianceSummaryFiltersTypeDef = None,
    GroupByKey: ConfigRuleComplianceSummaryGroupKey = None,
    Limit: int = None,
    NextToken: str = None
) -> GetAggregateConfigRuleComplianceSummaryResponseTypeDef:
    pass
```

### get_aggregate_conformance_pack_compliance_summary

Type annotations for `boto3.client("config").get_aggregate_conformance_pack_compliance_summary` method.

[Client.get_aggregate_conformance_pack_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_aggregate_conformance_pack_compliance_summary)

```python
def get_aggregate_conformance_pack_compliance_summary(
    self,
    ConfigurationAggregatorName: str,
    Filters: AggregateConformancePackComplianceSummaryFiltersTypeDef = None,
    GroupByKey: AggregateConformancePackComplianceSummaryGroupKey = None,
    Limit: int = None,
    NextToken: str = None
) -> GetAggregateConformancePackComplianceSummaryResponseTypeDef:
    pass
```

### get_aggregate_discovered_resource_counts

Type annotations for `boto3.client("config").get_aggregate_discovered_resource_counts` method.

[Client.get_aggregate_discovered_resource_counts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_aggregate_discovered_resource_counts)

```python
def get_aggregate_discovered_resource_counts(
    self,
    ConfigurationAggregatorName: str,
    Filters: ResourceCountFiltersTypeDef = None,
    GroupByKey: ResourceCountGroupKey = None,
    Limit: int = None,
    NextToken: str = None
) -> GetAggregateDiscoveredResourceCountsResponseTypeDef:
    pass
```

### get_aggregate_resource_config

Type annotations for `boto3.client("config").get_aggregate_resource_config` method.

[Client.get_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_aggregate_resource_config)

```python
def get_aggregate_resource_config(
    self,
    ConfigurationAggregatorName: str,
    ResourceIdentifier: "AggregateResourceIdentifierTypeDef"
) -> GetAggregateResourceConfigResponseTypeDef:
    pass
```

### get_compliance_details_by_config_rule

Type annotations for `boto3.client("config").get_compliance_details_by_config_rule` method.

[Client.get_compliance_details_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_compliance_details_by_config_rule)

```python
def get_compliance_details_by_config_rule(
    self,
    ConfigRuleName: str,
    ComplianceTypes: List[ComplianceType] = None,
    Limit: int = None,
    NextToken: str = None
) -> GetComplianceDetailsByConfigRuleResponseTypeDef:
    pass
```

### get_compliance_details_by_resource

Type annotations for `boto3.client("config").get_compliance_details_by_resource` method.

[Client.get_compliance_details_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_compliance_details_by_resource)

```python
def get_compliance_details_by_resource(
    self,
    ResourceType: str,
    ResourceId: str,
    ComplianceTypes: List[ComplianceType] = None,
    NextToken: str = None
) -> GetComplianceDetailsByResourceResponseTypeDef:
    pass
```

### get_compliance_summary_by_config_rule

Type annotations for `boto3.client("config").get_compliance_summary_by_config_rule` method.

[Client.get_compliance_summary_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_config_rule)

```python
def get_compliance_summary_by_config_rule(
    self
) -> GetComplianceSummaryByConfigRuleResponseTypeDef:
    pass
```

### get_compliance_summary_by_resource_type

Type annotations for `boto3.client("config").get_compliance_summary_by_resource_type` method.

[Client.get_compliance_summary_by_resource_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_resource_type)

```python
def get_compliance_summary_by_resource_type(
    self,
    ResourceTypes: List[str] = None
) -> GetComplianceSummaryByResourceTypeResponseTypeDef:
    pass
```

### get_conformance_pack_compliance_details

Type annotations for `boto3.client("config").get_conformance_pack_compliance_details` method.

[Client.get_conformance_pack_compliance_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_details)

```python
def get_conformance_pack_compliance_details(
    self,
    ConformancePackName: str,
    Filters: ConformancePackEvaluationFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> GetConformancePackComplianceDetailsResponseTypeDef:
    pass
```

### get_conformance_pack_compliance_summary

Type annotations for `boto3.client("config").get_conformance_pack_compliance_summary` method.

[Client.get_conformance_pack_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_summary)

```python
def get_conformance_pack_compliance_summary(
    self,
    ConformancePackNames: List[str],
    Limit: int = None,
    NextToken: str = None
) -> GetConformancePackComplianceSummaryResponseTypeDef:
    pass
```

### get_discovered_resource_counts

Type annotations for `boto3.client("config").get_discovered_resource_counts` method.

[Client.get_discovered_resource_counts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_discovered_resource_counts)

```python
def get_discovered_resource_counts(
    self,
    resourceTypes: List[str] = None,
    limit: int = None,
    nextToken: str = None
) -> GetDiscoveredResourceCountsResponseTypeDef:
    pass
```

### get_organization_config_rule_detailed_status

Type annotations for `boto3.client("config").get_organization_config_rule_detailed_status` method.

[Client.get_organization_config_rule_detailed_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_organization_config_rule_detailed_status)

```python
def get_organization_config_rule_detailed_status(
    self,
    OrganizationConfigRuleName: str,
    Filters: StatusDetailFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> GetOrganizationConfigRuleDetailedStatusResponseTypeDef:
    pass
```

### get_organization_conformance_pack_detailed_status

Type annotations for `boto3.client("config").get_organization_conformance_pack_detailed_status` method.

[Client.get_organization_conformance_pack_detailed_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_organization_conformance_pack_detailed_status)

```python
def get_organization_conformance_pack_detailed_status(
    self,
    OrganizationConformancePackName: str,
    Filters: OrganizationResourceDetailedStatusFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> GetOrganizationConformancePackDetailedStatusResponseTypeDef:
    pass
```

### get_resource_config_history

Type annotations for `boto3.client("config").get_resource_config_history` method.

[Client.get_resource_config_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_resource_config_history)

```python
def get_resource_config_history(
    self,
    resourceType: ResourceType,
    resourceId: str,
    laterTime: datetime = None,
    earlierTime: datetime = None,
    chronologicalOrder: ChronologicalOrder = None,
    limit: int = None,
    nextToken: str = None
) -> GetResourceConfigHistoryResponseTypeDef:
    pass
```

### get_stored_query

Type annotations for `boto3.client("config").get_stored_query` method.

[Client.get_stored_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.get_stored_query)

```python
def get_stored_query(
    self,
    QueryName: str
) -> GetStoredQueryResponseTypeDef:
    pass
```

### list_aggregate_discovered_resources

Type annotations for `boto3.client("config").list_aggregate_discovered_resources` method.

[Client.list_aggregate_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.list_aggregate_discovered_resources)

```python
def list_aggregate_discovered_resources(
    self,
    ConfigurationAggregatorName: str,
    ResourceType: ResourceType,
    Filters: ResourceFiltersTypeDef = None,
    Limit: int = None,
    NextToken: str = None
) -> ListAggregateDiscoveredResourcesResponseTypeDef:
    pass
```

### list_discovered_resources

Type annotations for `boto3.client("config").list_discovered_resources` method.

[Client.list_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.list_discovered_resources)

```python
def list_discovered_resources(
    self,
    resourceType: ResourceType,
    resourceIds: List[str] = None,
    resourceName: str = None,
    limit: int = None,
    includeDeletedResources: bool = None,
    nextToken: str = None
) -> ListDiscoveredResourcesResponseTypeDef:
    pass
```

### list_stored_queries

Type annotations for `boto3.client("config").list_stored_queries` method.

[Client.list_stored_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.list_stored_queries)

```python
def list_stored_queries(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListStoredQueriesResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("config").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str,
    Limit: int = None,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_aggregation_authorization

Type annotations for `boto3.client("config").put_aggregation_authorization` method.

[Client.put_aggregation_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_aggregation_authorization)

```python
def put_aggregation_authorization(
    self,
    AuthorizedAccountId: str,
    AuthorizedAwsRegion: str,
    Tags: List["TagTypeDef"] = None
) -> PutAggregationAuthorizationResponseTypeDef:
    pass
```

### put_config_rule

Type annotations for `boto3.client("config").put_config_rule` method.

[Client.put_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_config_rule)

```python
def put_config_rule(
    self,
    ConfigRule: "ConfigRuleTypeDef",
    Tags: List["TagTypeDef"] = None
) -> None:
    pass
```

### put_configuration_aggregator

Type annotations for `boto3.client("config").put_configuration_aggregator` method.

[Client.put_configuration_aggregator documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_configuration_aggregator)

```python
def put_configuration_aggregator(
    self,
    ConfigurationAggregatorName: str,
    AccountAggregationSources: List["AccountAggregationSourceTypeDef"] = None,
    OrganizationAggregationSource: "OrganizationAggregationSourceTypeDef" = None,
    Tags: List["TagTypeDef"] = None
) -> PutConfigurationAggregatorResponseTypeDef:
    pass
```

### put_configuration_recorder

Type annotations for `boto3.client("config").put_configuration_recorder` method.

[Client.put_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_configuration_recorder)

```python
def put_configuration_recorder(
    self,
    ConfigurationRecorder: "ConfigurationRecorderTypeDef"
) -> None:
    pass
```

### put_conformance_pack

Type annotations for `boto3.client("config").put_conformance_pack` method.

[Client.put_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_conformance_pack)

```python
def put_conformance_pack(
    self,
    ConformancePackName: str,
    TemplateS3Uri: str = None,
    TemplateBody: str = None,
    DeliveryS3Bucket: str = None,
    DeliveryS3KeyPrefix: str = None,
    ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"] = None
) -> PutConformancePackResponseTypeDef:
    pass
```

### put_delivery_channel

Type annotations for `boto3.client("config").put_delivery_channel` method.

[Client.put_delivery_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_delivery_channel)

```python
def put_delivery_channel(
    self,
    DeliveryChannel: "DeliveryChannelTypeDef"
) -> None:
    pass
```

### put_evaluations

Type annotations for `boto3.client("config").put_evaluations` method.

[Client.put_evaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_evaluations)

```python
def put_evaluations(
    self,
    ResultToken: str,
    Evaluations: List["EvaluationTypeDef"] = None,
    TestMode: bool = None
) -> PutEvaluationsResponseTypeDef:
    pass
```

### put_external_evaluation

Type annotations for `boto3.client("config").put_external_evaluation` method.

[Client.put_external_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_external_evaluation)

```python
def put_external_evaluation(
    self,
    ConfigRuleName: str,
    ExternalEvaluation: ExternalEvaluationTypeDef
) -> Dict[str, Any]:
    pass
```

### put_organization_config_rule

Type annotations for `boto3.client("config").put_organization_config_rule` method.

[Client.put_organization_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_organization_config_rule)

```python
def put_organization_config_rule(
    self,
    OrganizationConfigRuleName: str,
    OrganizationManagedRuleMetadata: "OrganizationManagedRuleMetadataTypeDef" = None,
    OrganizationCustomRuleMetadata: "OrganizationCustomRuleMetadataTypeDef" = None,
    ExcludedAccounts: List[str] = None
) -> PutOrganizationConfigRuleResponseTypeDef:
    pass
```

### put_organization_conformance_pack

Type annotations for `boto3.client("config").put_organization_conformance_pack` method.

[Client.put_organization_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_organization_conformance_pack)

```python
def put_organization_conformance_pack(
    self,
    OrganizationConformancePackName: str,
    TemplateS3Uri: str = None,
    TemplateBody: str = None,
    DeliveryS3Bucket: str = None,
    DeliveryS3KeyPrefix: str = None,
    ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"] = None,
    ExcludedAccounts: List[str] = None
) -> PutOrganizationConformancePackResponseTypeDef:
    pass
```

### put_remediation_configurations

Type annotations for `boto3.client("config").put_remediation_configurations` method.

[Client.put_remediation_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_remediation_configurations)

```python
def put_remediation_configurations(
    self,
    RemediationConfigurations: List["RemediationConfigurationTypeDef"]
) -> PutRemediationConfigurationsResponseTypeDef:
    pass
```

### put_remediation_exceptions

Type annotations for `boto3.client("config").put_remediation_exceptions` method.

[Client.put_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_remediation_exceptions)

```python
def put_remediation_exceptions(
    self,
    ConfigRuleName: str,
    ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"],
    Message: str = None,
    ExpirationTime: datetime = None
) -> PutRemediationExceptionsResponseTypeDef:
    pass
```

### put_resource_config

Type annotations for `boto3.client("config").put_resource_config` method.

[Client.put_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_resource_config)

```python
def put_resource_config(
    self,
    ResourceType: str,
    SchemaVersionId: str,
    ResourceId: str,
    Configuration: str,
    ResourceName: str = None,
    Tags: Dict[str, str] = None
) -> None:
    pass
```

### put_retention_configuration

Type annotations for `boto3.client("config").put_retention_configuration` method.

[Client.put_retention_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_retention_configuration)

```python
def put_retention_configuration(
    self,
    RetentionPeriodInDays: int
) -> PutRetentionConfigurationResponseTypeDef:
    pass
```

### put_stored_query

Type annotations for `boto3.client("config").put_stored_query` method.

[Client.put_stored_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.put_stored_query)

```python
def put_stored_query(
    self,
    StoredQuery: "StoredQueryTypeDef",
    Tags: List["TagTypeDef"] = None
) -> PutStoredQueryResponseTypeDef:
    pass
```

### select_aggregate_resource_config

Type annotations for `boto3.client("config").select_aggregate_resource_config` method.

[Client.select_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.select_aggregate_resource_config)

```python
def select_aggregate_resource_config(
    self,
    Expression: str,
    ConfigurationAggregatorName: str,
    Limit: int = None,
    MaxResults: int = None,
    NextToken: str = None
) -> SelectAggregateResourceConfigResponseTypeDef:
    pass
```

### select_resource_config

Type annotations for `boto3.client("config").select_resource_config` method.

[Client.select_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.select_resource_config)

```python
def select_resource_config(
    self,
    Expression: str,
    Limit: int = None,
    NextToken: str = None
) -> SelectResourceConfigResponseTypeDef:
    pass
```

### start_config_rules_evaluation

Type annotations for `boto3.client("config").start_config_rules_evaluation` method.

[Client.start_config_rules_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.start_config_rules_evaluation)

```python
def start_config_rules_evaluation(
    self,
    ConfigRuleNames: List[str] = None
) -> Dict[str, Any]:
    pass
```

### start_configuration_recorder

Type annotations for `boto3.client("config").start_configuration_recorder` method.

[Client.start_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.start_configuration_recorder)

```python
def start_configuration_recorder(
    self,
    ConfigurationRecorderName: str
) -> None:
    pass
```

### start_remediation_execution

Type annotations for `boto3.client("config").start_remediation_execution` method.

[Client.start_remediation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.start_remediation_execution)

```python
def start_remediation_execution(
    self,
    ConfigRuleName: str,
    ResourceKeys: List["ResourceKeyTypeDef"]
) -> StartRemediationExecutionResponseTypeDef:
    pass
```

### stop_configuration_recorder

Type annotations for `boto3.client("config").stop_configuration_recorder` method.

[Client.stop_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.stop_configuration_recorder)

```python
def stop_configuration_recorder(
    self,
    ConfigurationRecorderName: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("config").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("config").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeAggregateComplianceByConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAggregateComplianceByConfigRulesPaginatorName
) -> DescribeAggregateComplianceByConfigRulesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeAggregationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAggregationAuthorizationsPaginatorName
) -> DescribeAggregationAuthorizationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeComplianceByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeComplianceByConfigRulePaginatorName
) -> DescribeComplianceByConfigRulePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeComplianceByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeComplianceByResourcePaginatorName
) -> DescribeComplianceByResourcePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeConfigRuleEvaluationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeConfigRuleEvaluationStatusPaginatorName
) -> DescribeConfigRuleEvaluationStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeConfigRulesPaginatorName
) -> DescribeConfigRulesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeConfigurationAggregatorSourcesStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeConfigurationAggregatorSourcesStatusPaginatorName
) -> DescribeConfigurationAggregatorSourcesStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeConfigurationAggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeConfigurationAggregatorsPaginatorName
) -> DescribeConfigurationAggregatorsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribePendingAggregationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribePendingAggregationRequestsPaginatorName
) -> DescribePendingAggregationRequestsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeRemediationExecutionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeRemediationExecutionStatusPaginatorName
) -> DescribeRemediationExecutionStatusPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.DescribeRetentionConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeRetentionConfigurationsPaginatorName
) -> DescribeRetentionConfigurationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.GetAggregateComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)

```python
@overload
def get_paginator(
    self,
    operation_name: GetAggregateComplianceDetailsByConfigRulePaginatorName
) -> GetAggregateComplianceDetailsByConfigRulePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.GetComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)

```python
@overload
def get_paginator(
    self,
    operation_name: GetComplianceDetailsByConfigRulePaginatorName
) -> GetComplianceDetailsByConfigRulePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.GetComplianceDetailsByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)

```python
@overload
def get_paginator(
    self,
    operation_name: GetComplianceDetailsByResourcePaginatorName
) -> GetComplianceDetailsByResourcePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.GetResourceConfigHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetResourceConfigHistoryPaginatorName
) -> GetResourceConfigHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.ListAggregateDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAggregateDiscoveredResourcesPaginatorName
) -> ListAggregateDiscoveredResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("config").get_paginator` method.

[Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDiscoveredResourcesPaginatorName
) -> ListDiscoveredResourcesPaginator:
    pass
```