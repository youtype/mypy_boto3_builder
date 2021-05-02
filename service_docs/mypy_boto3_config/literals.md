# Literals for boto3 ConfigService module

> [Index](../index.md) > [ConfigService](./index.md) > Literals

Auto-generated documentation for [ConfigService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService)
type annotations stubs module [mypy_boto3_config](https://pypi.org/project/mypy-boto3-config/).

- [Literals for boto3 ConfigService module](#literals-for-boto3-configservice-module)
  - [AggregateConformancePackComplianceSummaryGroupKey](#aggregateconformancepackcompliancesummarygroupkey)
  - [AggregatedSourceStatusType](#aggregatedsourcestatustype)
  - [AggregatedSourceType](#aggregatedsourcetype)
  - [ChronologicalOrder](#chronologicalorder)
  - [ComplianceType](#compliancetype)
  - [ConfigRuleComplianceSummaryGroupKey](#configrulecompliancesummarygroupkey)
  - [ConfigRuleState](#configrulestate)
  - [ConfigurationItemStatus](#configurationitemstatus)
  - [ConformancePackComplianceType](#conformancepackcompliancetype)
  - [ConformancePackState](#conformancepackstate)
  - [DeliveryStatus](#deliverystatus)
  - [DescribeAggregateComplianceByConfigRulesPaginatorName](#describeaggregatecompliancebyconfigrulespaginatorname)
  - [DescribeAggregationAuthorizationsPaginatorName](#describeaggregationauthorizationspaginatorname)
  - [DescribeComplianceByConfigRulePaginatorName](#describecompliancebyconfigrulepaginatorname)
  - [DescribeComplianceByResourcePaginatorName](#describecompliancebyresourcepaginatorname)
  - [DescribeConfigRuleEvaluationStatusPaginatorName](#describeconfigruleevaluationstatuspaginatorname)
  - [DescribeConfigRulesPaginatorName](#describeconfigrulespaginatorname)
  - [DescribeConfigurationAggregatorSourcesStatusPaginatorName](#describeconfigurationaggregatorsourcesstatuspaginatorname)
  - [DescribeConfigurationAggregatorsPaginatorName](#describeconfigurationaggregatorspaginatorname)
  - [DescribePendingAggregationRequestsPaginatorName](#describependingaggregationrequestspaginatorname)
  - [DescribeRemediationExecutionStatusPaginatorName](#describeremediationexecutionstatuspaginatorname)
  - [DescribeRetentionConfigurationsPaginatorName](#describeretentionconfigurationspaginatorname)
  - [EventSource](#eventsource)
  - [GetAggregateComplianceDetailsByConfigRulePaginatorName](#getaggregatecompliancedetailsbyconfigrulepaginatorname)
  - [GetComplianceDetailsByConfigRulePaginatorName](#getcompliancedetailsbyconfigrulepaginatorname)
  - [GetComplianceDetailsByResourcePaginatorName](#getcompliancedetailsbyresourcepaginatorname)
  - [GetResourceConfigHistoryPaginatorName](#getresourceconfighistorypaginatorname)
  - [ListAggregateDiscoveredResourcesPaginatorName](#listaggregatediscoveredresourcespaginatorname)
  - [ListDiscoveredResourcesPaginatorName](#listdiscoveredresourcespaginatorname)
  - [MaximumExecutionFrequency](#maximumexecutionfrequency)
  - [MemberAccountRuleStatus](#memberaccountrulestatus)
  - [MessageType](#messagetype)
  - [OrganizationConfigRuleTriggerType](#organizationconfigruletriggertype)
  - [OrganizationResourceDetailedStatus](#organizationresourcedetailedstatus)
  - [OrganizationResourceStatus](#organizationresourcestatus)
  - [OrganizationRuleStatus](#organizationrulestatus)
  - [Owner](#owner)
  - [RecorderStatus](#recorderstatus)
  - [RemediationExecutionState](#remediationexecutionstate)
  - [RemediationExecutionStepState](#remediationexecutionstepstate)
  - [RemediationTargetType](#remediationtargettype)
  - [ResourceCountGroupKey](#resourcecountgroupkey)
  - [ResourceType](#resourcetype)
  - [ResourceValueType](#resourcevaluetype)

## AggregateConformancePackComplianceSummaryGroupKey

```python
from mypy_boto3_config.literals import AggregateConformancePackComplianceSummaryGroupKey
```

Values:

- `ACCOUNT_ID`
- `AWS_REGION`

## AggregatedSourceStatusType

```python
from mypy_boto3_config.literals import AggregatedSourceStatusType
```

Values:

- `FAILED`
- `OUTDATED`
- `SUCCEEDED`

## AggregatedSourceType

```python
from mypy_boto3_config.literals import AggregatedSourceType
```

Values:

- `ACCOUNT`
- `ORGANIZATION`

## ChronologicalOrder

```python
from mypy_boto3_config.literals import ChronologicalOrder
```

Values:

- `Forward`
- `Reverse`

## ComplianceType

```python
from mypy_boto3_config.literals import ComplianceType
```

Values:

- `COMPLIANT`
- `INSUFFICIENT_DATA`
- `NON_COMPLIANT`
- `NOT_APPLICABLE`

## ConfigRuleComplianceSummaryGroupKey

```python
from mypy_boto3_config.literals import ConfigRuleComplianceSummaryGroupKey
```

Values:

- `ACCOUNT_ID`
- `AWS_REGION`

## ConfigRuleState

```python
from mypy_boto3_config.literals import ConfigRuleState
```

Values:

- `ACTIVE`
- `DELETING`
- `DELETING_RESULTS`
- `EVALUATING`

## ConfigurationItemStatus

```python
from mypy_boto3_config.literals import ConfigurationItemStatus
```

Values:

- `OK`
- `ResourceDeleted`
- `ResourceDeletedNotRecorded`
- `ResourceDiscovered`
- `ResourceNotRecorded`

## ConformancePackComplianceType

```python
from mypy_boto3_config.literals import ConformancePackComplianceType
```

Values:

- `COMPLIANT`
- `INSUFFICIENT_DATA`
- `NON_COMPLIANT`

## ConformancePackState

```python
from mypy_boto3_config.literals import ConformancePackState
```

Values:

- `CREATE_COMPLETE`
- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`

## DeliveryStatus

```python
from mypy_boto3_config.literals import DeliveryStatus
```

Values:

- `Failure`
- `Not_Applicable`
- `Success`

## DescribeAggregateComplianceByConfigRulesPaginatorName

```python
from mypy_boto3_config.literals import DescribeAggregateComplianceByConfigRulesPaginatorName
```

Values:

- `describe_aggregate_compliance_by_config_rules`

## DescribeAggregationAuthorizationsPaginatorName

```python
from mypy_boto3_config.literals import DescribeAggregationAuthorizationsPaginatorName
```

Values:

- `describe_aggregation_authorizations`

## DescribeComplianceByConfigRulePaginatorName

```python
from mypy_boto3_config.literals import DescribeComplianceByConfigRulePaginatorName
```

Values:

- `describe_compliance_by_config_rule`

## DescribeComplianceByResourcePaginatorName

```python
from mypy_boto3_config.literals import DescribeComplianceByResourcePaginatorName
```

Values:

- `describe_compliance_by_resource`

## DescribeConfigRuleEvaluationStatusPaginatorName

```python
from mypy_boto3_config.literals import DescribeConfigRuleEvaluationStatusPaginatorName
```

Values:

- `describe_config_rule_evaluation_status`

## DescribeConfigRulesPaginatorName

```python
from mypy_boto3_config.literals import DescribeConfigRulesPaginatorName
```

Values:

- `describe_config_rules`

## DescribeConfigurationAggregatorSourcesStatusPaginatorName

```python
from mypy_boto3_config.literals import DescribeConfigurationAggregatorSourcesStatusPaginatorName
```

Values:

- `describe_configuration_aggregator_sources_status`

## DescribeConfigurationAggregatorsPaginatorName

```python
from mypy_boto3_config.literals import DescribeConfigurationAggregatorsPaginatorName
```

Values:

- `describe_configuration_aggregators`

## DescribePendingAggregationRequestsPaginatorName

```python
from mypy_boto3_config.literals import DescribePendingAggregationRequestsPaginatorName
```

Values:

- `describe_pending_aggregation_requests`

## DescribeRemediationExecutionStatusPaginatorName

```python
from mypy_boto3_config.literals import DescribeRemediationExecutionStatusPaginatorName
```

Values:

- `describe_remediation_execution_status`

## DescribeRetentionConfigurationsPaginatorName

```python
from mypy_boto3_config.literals import DescribeRetentionConfigurationsPaginatorName
```

Values:

- `describe_retention_configurations`

## EventSource

```python
from mypy_boto3_config.literals import EventSource
```

Values:

- `aws.config`

## GetAggregateComplianceDetailsByConfigRulePaginatorName

```python
from mypy_boto3_config.literals import GetAggregateComplianceDetailsByConfigRulePaginatorName
```

Values:

- `get_aggregate_compliance_details_by_config_rule`

## GetComplianceDetailsByConfigRulePaginatorName

```python
from mypy_boto3_config.literals import GetComplianceDetailsByConfigRulePaginatorName
```

Values:

- `get_compliance_details_by_config_rule`

## GetComplianceDetailsByResourcePaginatorName

```python
from mypy_boto3_config.literals import GetComplianceDetailsByResourcePaginatorName
```

Values:

- `get_compliance_details_by_resource`

## GetResourceConfigHistoryPaginatorName

```python
from mypy_boto3_config.literals import GetResourceConfigHistoryPaginatorName
```

Values:

- `get_resource_config_history`

## ListAggregateDiscoveredResourcesPaginatorName

```python
from mypy_boto3_config.literals import ListAggregateDiscoveredResourcesPaginatorName
```

Values:

- `list_aggregate_discovered_resources`

## ListDiscoveredResourcesPaginatorName

```python
from mypy_boto3_config.literals import ListDiscoveredResourcesPaginatorName
```

Values:

- `list_discovered_resources`

## MaximumExecutionFrequency

```python
from mypy_boto3_config.literals import MaximumExecutionFrequency
```

Values:

- `One_Hour`
- `Six_Hours`
- `Three_Hours`
- `Twelve_Hours`
- `TwentyFour_Hours`

## MemberAccountRuleStatus

```python
from mypy_boto3_config.literals import MemberAccountRuleStatus
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `CREATE_SUCCESSFUL`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETE_SUCCESSFUL`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`
- `UPDATE_SUCCESSFUL`

## MessageType

```python
from mypy_boto3_config.literals import MessageType
```

Values:

- `ConfigurationItemChangeNotification`
- `ConfigurationSnapshotDeliveryCompleted`
- `OversizedConfigurationItemChangeNotification`
- `ScheduledNotification`

## OrganizationConfigRuleTriggerType

```python
from mypy_boto3_config.literals import OrganizationConfigRuleTriggerType
```

Values:

- `ConfigurationItemChangeNotification`
- `OversizedConfigurationItemChangeNotification`
- `ScheduledNotification`

## OrganizationResourceDetailedStatus

```python
from mypy_boto3_config.literals import OrganizationResourceDetailedStatus
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `CREATE_SUCCESSFUL`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETE_SUCCESSFUL`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`
- `UPDATE_SUCCESSFUL`

## OrganizationResourceStatus

```python
from mypy_boto3_config.literals import OrganizationResourceStatus
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `CREATE_SUCCESSFUL`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETE_SUCCESSFUL`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`
- `UPDATE_SUCCESSFUL`

## OrganizationRuleStatus

```python
from mypy_boto3_config.literals import OrganizationRuleStatus
```

Values:

- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `CREATE_SUCCESSFUL`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `DELETE_SUCCESSFUL`
- `UPDATE_FAILED`
- `UPDATE_IN_PROGRESS`
- `UPDATE_SUCCESSFUL`

## Owner

```python
from mypy_boto3_config.literals import Owner
```

Values:

- `AWS`
- `CUSTOM_LAMBDA`

## RecorderStatus

```python
from mypy_boto3_config.literals import RecorderStatus
```

Values:

- `Failure`
- `Pending`
- `Success`

## RemediationExecutionState

```python
from mypy_boto3_config.literals import RemediationExecutionState
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `QUEUED`
- `SUCCEEDED`

## RemediationExecutionStepState

```python
from mypy_boto3_config.literals import RemediationExecutionStepState
```

Values:

- `FAILED`
- `PENDING`
- `SUCCEEDED`

## RemediationTargetType

```python
from mypy_boto3_config.literals import RemediationTargetType
```

Values:

- `SSM_DOCUMENT`

## ResourceCountGroupKey

```python
from mypy_boto3_config.literals import ResourceCountGroupKey
```

Values:

- `ACCOUNT_ID`
- `AWS_REGION`
- `RESOURCE_TYPE`

## ResourceType

```python
from mypy_boto3_config.literals import ResourceType
```

Values:

- `AWS::ACM::Certificate`
- `AWS::ApiGateway::RestApi`
- `AWS::ApiGateway::Stage`
- `AWS::ApiGatewayV2::Api`
- `AWS::ApiGatewayV2::Stage`
- `AWS::AutoScaling::AutoScalingGroup`
- `AWS::AutoScaling::LaunchConfiguration`
- `AWS::AutoScaling::ScalingPolicy`
- `AWS::AutoScaling::ScheduledAction`
- `AWS::CloudFormation::Stack`
- `AWS::CloudFront::Distribution`
- `AWS::CloudFront::StreamingDistribution`
- `AWS::CloudTrail::Trail`
- `AWS::CloudWatch::Alarm`
- `AWS::CodeBuild::Project`
- `AWS::CodePipeline::Pipeline`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ResourceCompliance`
- `AWS::DynamoDB::Table`
- `AWS::EC2::CustomerGateway`
- `AWS::EC2::EgressOnlyInternetGateway`
- `AWS::EC2::EIP`
- `AWS::EC2::FlowLog`
- `AWS::EC2::Host`
- `AWS::EC2::Instance`
- `AWS::EC2::InternetGateway`
- `AWS::EC2::NatGateway`
- `AWS::EC2::NetworkAcl`
- `AWS::EC2::NetworkInterface`
- `AWS::EC2::RegisteredHAInstance`
- `AWS::EC2::RouteTable`
- `AWS::EC2::SecurityGroup`
- `AWS::EC2::Subnet`
- `AWS::EC2::Volume`
- `AWS::EC2::VPC`
- `AWS::EC2::VPCEndpoint`
- `AWS::EC2::VPCEndpointService`
- `AWS::EC2::VPCPeeringConnection`
- `AWS::EC2::VPNConnection`
- `AWS::EC2::VPNGateway`
- `AWS::ElasticBeanstalk::Application`
- `AWS::ElasticBeanstalk::ApplicationVersion`
- `AWS::ElasticBeanstalk::Environment`
- `AWS::ElasticLoadBalancing::LoadBalancer`
- `AWS::ElasticLoadBalancingV2::LoadBalancer`
- `AWS::Elasticsearch::Domain`
- `AWS::IAM::Group`
- `AWS::IAM::Policy`
- `AWS::IAM::Role`
- `AWS::IAM::User`
- `AWS::KMS::Key`
- `AWS::Lambda::Function`
- `AWS::NetworkFirewall::Firewall`
- `AWS::NetworkFirewall::FirewallPolicy`
- `AWS::NetworkFirewall::RuleGroup`
- `AWS::QLDB::Ledger`
- `AWS::RDS::DBCluster`
- `AWS::RDS::DBClusterSnapshot`
- `AWS::RDS::DBInstance`
- `AWS::RDS::DBSecurityGroup`
- `AWS::RDS::DBSnapshot`
- `AWS::RDS::DBSubnetGroup`
- `AWS::RDS::EventSubscription`
- `AWS::Redshift::Cluster`
- `AWS::Redshift::ClusterParameterGroup`
- `AWS::Redshift::ClusterSecurityGroup`
- `AWS::Redshift::ClusterSnapshot`
- `AWS::Redshift::ClusterSubnetGroup`
- `AWS::Redshift::EventSubscription`
- `AWS::S3::AccountPublicAccessBlock`
- `AWS::S3::Bucket`
- `AWS::SecretsManager::Secret`
- `AWS::ServiceCatalog::CloudFormationProduct`
- `AWS::ServiceCatalog::CloudFormationProvisionedProduct`
- `AWS::ServiceCatalog::Portfolio`
- `AWS::Shield::Protection`
- `AWS::ShieldRegional::Protection`
- `AWS::SNS::Topic`
- `AWS::SQS::Queue`
- `AWS::SSM::AssociationCompliance`
- `AWS::SSM::FileData`
- `AWS::SSM::ManagedInstanceInventory`
- `AWS::SSM::PatchCompliance`
- `AWS::WAF::RateBasedRule`
- `AWS::WAF::Rule`
- `AWS::WAF::RuleGroup`
- `AWS::WAF::WebACL`
- `AWS::WAFRegional::RateBasedRule`
- `AWS::WAFRegional::Rule`
- `AWS::WAFRegional::RuleGroup`
- `AWS::WAFRegional::WebACL`
- `AWS::WAFv2::IPSet`
- `AWS::WAFv2::ManagedRuleSet`
- `AWS::WAFv2::RegexPatternSet`
- `AWS::WAFv2::RuleGroup`
- `AWS::WAFv2::WebACL`
- `AWS::XRay::EncryptionConfig`

## ResourceValueType

```python
from mypy_boto3_config.literals import ResourceValueType
```

Values:

- `RESOURCE_ID`
