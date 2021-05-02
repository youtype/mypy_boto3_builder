# Literals for boto3 IoT module

> [Index](../index.md) > [IoT](./index.md) > Literals

Auto-generated documentation for [IoT](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT)
type annotations stubs module [mypy_boto3_iot](https://pypi.org/project/mypy-boto3-iot/).

- [Literals for boto3 IoT module](#literals-for-boto3-iot-module)
  - [AbortAction](#abortaction)
  - [ActionType](#actiontype)
  - [AlertTargetType](#alerttargettype)
  - [AuditCheckRunStatus](#auditcheckrunstatus)
  - [AuditFindingSeverity](#auditfindingseverity)
  - [AuditFrequency](#auditfrequency)
  - [AuditMitigationActionsExecutionStatus](#auditmitigationactionsexecutionstatus)
  - [AuditMitigationActionsTaskStatus](#auditmitigationactionstaskstatus)
  - [AuditNotificationType](#auditnotificationtype)
  - [AuditTaskStatus](#audittaskstatus)
  - [AuditTaskType](#audittasktype)
  - [AuthDecision](#authdecision)
  - [AuthorizerStatus](#authorizerstatus)
  - [AutoRegistrationStatus](#autoregistrationstatus)
  - [AwsJobAbortCriteriaAbortAction](#awsjobabortcriteriaabortaction)
  - [AwsJobAbortCriteriaFailureType](#awsjobabortcriteriafailuretype)
  - [BehaviorCriteriaType](#behaviorcriteriatype)
  - [CACertificateStatus](#cacertificatestatus)
  - [CACertificateUpdateAction](#cacertificateupdateaction)
  - [CannedAccessControlList](#cannedaccesscontrollist)
  - [CertificateMode](#certificatemode)
  - [CertificateStatus](#certificatestatus)
  - [ComparisonOperator](#comparisonoperator)
  - [ConfidenceLevel](#confidencelevel)
  - [CustomMetricType](#custommetrictype)
  - [DayOfWeek](#dayofweek)
  - [DetectMitigationActionExecutionStatus](#detectmitigationactionexecutionstatus)
  - [DetectMitigationActionsTaskStatus](#detectmitigationactionstaskstatus)
  - [DeviceCertificateUpdateAction](#devicecertificateupdateaction)
  - [DimensionType](#dimensiontype)
  - [DimensionValueOperator](#dimensionvalueoperator)
  - [DomainConfigurationStatus](#domainconfigurationstatus)
  - [DomainType](#domaintype)
  - [DynamicGroupStatus](#dynamicgroupstatus)
  - [DynamoKeyType](#dynamokeytype)
  - [EventType](#eventtype)
  - [FieldType](#fieldtype)
  - [GetBehaviorModelTrainingSummariesPaginatorName](#getbehaviormodeltrainingsummariespaginatorname)
  - [IndexStatus](#indexstatus)
  - [JobExecutionFailureType](#jobexecutionfailuretype)
  - [JobExecutionStatus](#jobexecutionstatus)
  - [JobStatus](#jobstatus)
  - [ListActiveViolationsPaginatorName](#listactiveviolationspaginatorname)
  - [ListAttachedPoliciesPaginatorName](#listattachedpoliciespaginatorname)
  - [ListAuditFindingsPaginatorName](#listauditfindingspaginatorname)
  - [ListAuditMitigationActionsExecutionsPaginatorName](#listauditmitigationactionsexecutionspaginatorname)
  - [ListAuditMitigationActionsTasksPaginatorName](#listauditmitigationactionstaskspaginatorname)
  - [ListAuditSuppressionsPaginatorName](#listauditsuppressionspaginatorname)
  - [ListAuditTasksPaginatorName](#listaudittaskspaginatorname)
  - [ListAuthorizersPaginatorName](#listauthorizerspaginatorname)
  - [ListBillingGroupsPaginatorName](#listbillinggroupspaginatorname)
  - [ListCACertificatesPaginatorName](#listcacertificatespaginatorname)
  - [ListCertificatesByCAPaginatorName](#listcertificatesbycapaginatorname)
  - [ListCertificatesPaginatorName](#listcertificatespaginatorname)
  - [ListCustomMetricsPaginatorName](#listcustommetricspaginatorname)
  - [ListDetectMitigationActionsExecutionsPaginatorName](#listdetectmitigationactionsexecutionspaginatorname)
  - [ListDetectMitigationActionsTasksPaginatorName](#listdetectmitigationactionstaskspaginatorname)
  - [ListDimensionsPaginatorName](#listdimensionspaginatorname)
  - [ListDomainConfigurationsPaginatorName](#listdomainconfigurationspaginatorname)
  - [ListIndicesPaginatorName](#listindicespaginatorname)
  - [ListJobExecutionsForJobPaginatorName](#listjobexecutionsforjobpaginatorname)
  - [ListJobExecutionsForThingPaginatorName](#listjobexecutionsforthingpaginatorname)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [ListMitigationActionsPaginatorName](#listmitigationactionspaginatorname)
  - [ListOTAUpdatesPaginatorName](#listotaupdatespaginatorname)
  - [ListOutgoingCertificatesPaginatorName](#listoutgoingcertificatespaginatorname)
  - [ListPoliciesPaginatorName](#listpoliciespaginatorname)
  - [ListPolicyPrincipalsPaginatorName](#listpolicyprincipalspaginatorname)
  - [ListPrincipalPoliciesPaginatorName](#listprincipalpoliciespaginatorname)
  - [ListPrincipalThingsPaginatorName](#listprincipalthingspaginatorname)
  - [ListProvisioningTemplateVersionsPaginatorName](#listprovisioningtemplateversionspaginatorname)
  - [ListProvisioningTemplatesPaginatorName](#listprovisioningtemplatespaginatorname)
  - [ListRoleAliasesPaginatorName](#listrolealiasespaginatorname)
  - [ListScheduledAuditsPaginatorName](#listscheduledauditspaginatorname)
  - [ListSecurityProfilesForTargetPaginatorName](#listsecurityprofilesfortargetpaginatorname)
  - [ListSecurityProfilesPaginatorName](#listsecurityprofilespaginatorname)
  - [ListStreamsPaginatorName](#liststreamspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListTargetsForPolicyPaginatorName](#listtargetsforpolicypaginatorname)
  - [ListTargetsForSecurityProfilePaginatorName](#listtargetsforsecurityprofilepaginatorname)
  - [ListThingGroupsForThingPaginatorName](#listthinggroupsforthingpaginatorname)
  - [ListThingGroupsPaginatorName](#listthinggroupspaginatorname)
  - [ListThingPrincipalsPaginatorName](#listthingprincipalspaginatorname)
  - [ListThingRegistrationTaskReportsPaginatorName](#listthingregistrationtaskreportspaginatorname)
  - [ListThingRegistrationTasksPaginatorName](#listthingregistrationtaskspaginatorname)
  - [ListThingTypesPaginatorName](#listthingtypespaginatorname)
  - [ListThingsInBillingGroupPaginatorName](#listthingsinbillinggrouppaginatorname)
  - [ListThingsInThingGroupPaginatorName](#listthingsinthinggrouppaginatorname)
  - [ListThingsPaginatorName](#listthingspaginatorname)
  - [ListTopicRuleDestinationsPaginatorName](#listtopicruledestinationspaginatorname)
  - [ListTopicRulesPaginatorName](#listtopicrulespaginatorname)
  - [ListV2LoggingLevelsPaginatorName](#listv2logginglevelspaginatorname)
  - [ListViolationEventsPaginatorName](#listviolationeventspaginatorname)
  - [LogLevel](#loglevel)
  - [LogTargetType](#logtargettype)
  - [MessageFormat](#messageformat)
  - [MitigationActionType](#mitigationactiontype)
  - [ModelStatus](#modelstatus)
  - [OTAUpdateStatus](#otaupdatestatus)
  - [PolicyTemplateName](#policytemplatename)
  - [ProtocolType](#protocoltype)
  - [ReportType](#reporttype)
  - [ResourceType](#resourcetype)
  - [ServerCertificateStatus](#servercertificatestatus)
  - [ServiceType](#servicetype)
  - [Status](#status)
  - [TargetSelection](#targetselection)
  - [ThingConnectivityIndexingMode](#thingconnectivityindexingmode)
  - [ThingGroupIndexingMode](#thinggroupindexingmode)
  - [ThingIndexingMode](#thingindexingmode)
  - [TopicRuleDestinationStatus](#topicruledestinationstatus)
  - [ViolationEventType](#violationeventtype)

## AbortAction

```python
from mypy_boto3_iot.literals import AbortAction
```

Values:

- `CANCEL`

## ActionType

```python
from mypy_boto3_iot.literals import ActionType
```

Values:

- `CONNECT`
- `PUBLISH`
- `RECEIVE`
- `SUBSCRIBE`

## AlertTargetType

```python
from mypy_boto3_iot.literals import AlertTargetType
```

Values:

- `SNS`

## AuditCheckRunStatus

```python
from mypy_boto3_iot.literals import AuditCheckRunStatus
```

Values:

- `CANCELED`
- `COMPLETED_COMPLIANT`
- `COMPLETED_NON_COMPLIANT`
- `FAILED`
- `IN_PROGRESS`
- `WAITING_FOR_DATA_COLLECTION`

## AuditFindingSeverity

```python
from mypy_boto3_iot.literals import AuditFindingSeverity
```

Values:

- `CRITICAL`
- `HIGH`
- `LOW`
- `MEDIUM`

## AuditFrequency

```python
from mypy_boto3_iot.literals import AuditFrequency
```

Values:

- `BIWEEKLY`
- `DAILY`
- `MONTHLY`
- `WEEKLY`

## AuditMitigationActionsExecutionStatus

```python
from mypy_boto3_iot.literals import AuditMitigationActionsExecutionStatus
```

Values:

- `CANCELED`
- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`
- `PENDING`
- `SKIPPED`

## AuditMitigationActionsTaskStatus

```python
from mypy_boto3_iot.literals import AuditMitigationActionsTaskStatus
```

Values:

- `CANCELED`
- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`

## AuditNotificationType

```python
from mypy_boto3_iot.literals import AuditNotificationType
```

Values:

- `SNS`

## AuditTaskStatus

```python
from mypy_boto3_iot.literals import AuditTaskStatus
```

Values:

- `CANCELED`
- `COMPLETED`
- `FAILED`
- `IN_PROGRESS`

## AuditTaskType

```python
from mypy_boto3_iot.literals import AuditTaskType
```

Values:

- `ON_DEMAND_AUDIT_TASK`
- `SCHEDULED_AUDIT_TASK`

## AuthDecision

```python
from mypy_boto3_iot.literals import AuthDecision
```

Values:

- `ALLOWED`
- `EXPLICIT_DENY`
- `IMPLICIT_DENY`

## AuthorizerStatus

```python
from mypy_boto3_iot.literals import AuthorizerStatus
```

Values:

- `ACTIVE`
- `INACTIVE`

## AutoRegistrationStatus

```python
from mypy_boto3_iot.literals import AutoRegistrationStatus
```

Values:

- `DISABLE`
- `ENABLE`

## AwsJobAbortCriteriaAbortAction

```python
from mypy_boto3_iot.literals import AwsJobAbortCriteriaAbortAction
```

Values:

- `CANCEL`

## AwsJobAbortCriteriaFailureType

```python
from mypy_boto3_iot.literals import AwsJobAbortCriteriaFailureType
```

Values:

- `ALL`
- `FAILED`
- `REJECTED`
- `TIMED_OUT`

## BehaviorCriteriaType

```python
from mypy_boto3_iot.literals import BehaviorCriteriaType
```

Values:

- `MACHINE_LEARNING`
- `STATIC`
- `STATISTICAL`

## CACertificateStatus

```python
from mypy_boto3_iot.literals import CACertificateStatus
```

Values:

- `ACTIVE`
- `INACTIVE`

## CACertificateUpdateAction

```python
from mypy_boto3_iot.literals import CACertificateUpdateAction
```

Values:

- `DEACTIVATE`

## CannedAccessControlList

```python
from mypy_boto3_iot.literals import CannedAccessControlList
```

Values:

- `authenticated-read`
- `aws-exec-read`
- `bucket-owner-full-control`
- `bucket-owner-read`
- `log-delivery-write`
- `private`
- `public-read`
- `public-read-write`

## CertificateMode

```python
from mypy_boto3_iot.literals import CertificateMode
```

Values:

- `DEFAULT`
- `SNI_ONLY`

## CertificateStatus

```python
from mypy_boto3_iot.literals import CertificateStatus
```

Values:

- `ACTIVE`
- `INACTIVE`
- `PENDING_ACTIVATION`
- `PENDING_TRANSFER`
- `REGISTER_INACTIVE`
- `REVOKED`

## ComparisonOperator

```python
from mypy_boto3_iot.literals import ComparisonOperator
```

Values:

- `greater-than`
- `greater-than-equals`
- `in-cidr-set`
- `in-port-set`
- `in-set`
- `less-than`
- `less-than-equals`
- `not-in-cidr-set`
- `not-in-port-set`
- `not-in-set`

## ConfidenceLevel

```python
from mypy_boto3_iot.literals import ConfidenceLevel
```

Values:

- `HIGH`
- `LOW`
- `MEDIUM`

## CustomMetricType

```python
from mypy_boto3_iot.literals import CustomMetricType
```

Values:

- `ip-address-list`
- `number`
- `number-list`
- `string-list`

## DayOfWeek

```python
from mypy_boto3_iot.literals import DayOfWeek
```

Values:

- `FRI`
- `MON`
- `SAT`
- `SUN`
- `THU`
- `TUE`
- `WED`

## DetectMitigationActionExecutionStatus

```python
from mypy_boto3_iot.literals import DetectMitigationActionExecutionStatus
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `SKIPPED`
- `SUCCESSFUL`

## DetectMitigationActionsTaskStatus

```python
from mypy_boto3_iot.literals import DetectMitigationActionsTaskStatus
```

Values:

- `CANCELED`
- `FAILED`
- `IN_PROGRESS`
- `SUCCESSFUL`

## DeviceCertificateUpdateAction

```python
from mypy_boto3_iot.literals import DeviceCertificateUpdateAction
```

Values:

- `DEACTIVATE`

## DimensionType

```python
from mypy_boto3_iot.literals import DimensionType
```

Values:

- `TOPIC_FILTER`

## DimensionValueOperator

```python
from mypy_boto3_iot.literals import DimensionValueOperator
```

Values:

- `IN`
- `NOT_IN`

## DomainConfigurationStatus

```python
from mypy_boto3_iot.literals import DomainConfigurationStatus
```

Values:

- `DISABLED`
- `ENABLED`

## DomainType

```python
from mypy_boto3_iot.literals import DomainType
```

Values:

- `AWS_MANAGED`
- `CUSTOMER_MANAGED`
- `ENDPOINT`

## DynamicGroupStatus

```python
from mypy_boto3_iot.literals import DynamicGroupStatus
```

Values:

- `ACTIVE`
- `BUILDING`
- `REBUILDING`

## DynamoKeyType

```python
from mypy_boto3_iot.literals import DynamoKeyType
```

Values:

- `NUMBER`
- `STRING`

## EventType

```python
from mypy_boto3_iot.literals import EventType
```

Values:

- `CA_CERTIFICATE`
- `CERTIFICATE`
- `JOB`
- `JOB_EXECUTION`
- `POLICY`
- `THING`
- `THING_GROUP`
- `THING_GROUP_HIERARCHY`
- `THING_GROUP_MEMBERSHIP`
- `THING_TYPE`
- `THING_TYPE_ASSOCIATION`

## FieldType

```python
from mypy_boto3_iot.literals import FieldType
```

Values:

- `Boolean`
- `Number`
- `String`

## GetBehaviorModelTrainingSummariesPaginatorName

```python
from mypy_boto3_iot.literals import GetBehaviorModelTrainingSummariesPaginatorName
```

Values:

- `get_behavior_model_training_summaries`

## IndexStatus

```python
from mypy_boto3_iot.literals import IndexStatus
```

Values:

- `ACTIVE`
- `BUILDING`
- `REBUILDING`

## JobExecutionFailureType

```python
from mypy_boto3_iot.literals import JobExecutionFailureType
```

Values:

- `ALL`
- `FAILED`
- `REJECTED`
- `TIMED_OUT`

## JobExecutionStatus

```python
from mypy_boto3_iot.literals import JobExecutionStatus
```

Values:

- `CANCELED`
- `FAILED`
- `IN_PROGRESS`
- `QUEUED`
- `REJECTED`
- `REMOVED`
- `SUCCEEDED`
- `TIMED_OUT`

## JobStatus

```python
from mypy_boto3_iot.literals import JobStatus
```

Values:

- `CANCELED`
- `COMPLETED`
- `DELETION_IN_PROGRESS`
- `IN_PROGRESS`

## ListActiveViolationsPaginatorName

```python
from mypy_boto3_iot.literals import ListActiveViolationsPaginatorName
```

Values:

- `list_active_violations`

## ListAttachedPoliciesPaginatorName

```python
from mypy_boto3_iot.literals import ListAttachedPoliciesPaginatorName
```

Values:

- `list_attached_policies`

## ListAuditFindingsPaginatorName

```python
from mypy_boto3_iot.literals import ListAuditFindingsPaginatorName
```

Values:

- `list_audit_findings`

## ListAuditMitigationActionsExecutionsPaginatorName

```python
from mypy_boto3_iot.literals import ListAuditMitigationActionsExecutionsPaginatorName
```

Values:

- `list_audit_mitigation_actions_executions`

## ListAuditMitigationActionsTasksPaginatorName

```python
from mypy_boto3_iot.literals import ListAuditMitigationActionsTasksPaginatorName
```

Values:

- `list_audit_mitigation_actions_tasks`

## ListAuditSuppressionsPaginatorName

```python
from mypy_boto3_iot.literals import ListAuditSuppressionsPaginatorName
```

Values:

- `list_audit_suppressions`

## ListAuditTasksPaginatorName

```python
from mypy_boto3_iot.literals import ListAuditTasksPaginatorName
```

Values:

- `list_audit_tasks`

## ListAuthorizersPaginatorName

```python
from mypy_boto3_iot.literals import ListAuthorizersPaginatorName
```

Values:

- `list_authorizers`

## ListBillingGroupsPaginatorName

```python
from mypy_boto3_iot.literals import ListBillingGroupsPaginatorName
```

Values:

- `list_billing_groups`

## ListCACertificatesPaginatorName

```python
from mypy_boto3_iot.literals import ListCACertificatesPaginatorName
```

Values:

- `list_ca_certificates`

## ListCertificatesByCAPaginatorName

```python
from mypy_boto3_iot.literals import ListCertificatesByCAPaginatorName
```

Values:

- `list_certificates_by_ca`

## ListCertificatesPaginatorName

```python
from mypy_boto3_iot.literals import ListCertificatesPaginatorName
```

Values:

- `list_certificates`

## ListCustomMetricsPaginatorName

```python
from mypy_boto3_iot.literals import ListCustomMetricsPaginatorName
```

Values:

- `list_custom_metrics`

## ListDetectMitigationActionsExecutionsPaginatorName

```python
from mypy_boto3_iot.literals import ListDetectMitigationActionsExecutionsPaginatorName
```

Values:

- `list_detect_mitigation_actions_executions`

## ListDetectMitigationActionsTasksPaginatorName

```python
from mypy_boto3_iot.literals import ListDetectMitigationActionsTasksPaginatorName
```

Values:

- `list_detect_mitigation_actions_tasks`

## ListDimensionsPaginatorName

```python
from mypy_boto3_iot.literals import ListDimensionsPaginatorName
```

Values:

- `list_dimensions`

## ListDomainConfigurationsPaginatorName

```python
from mypy_boto3_iot.literals import ListDomainConfigurationsPaginatorName
```

Values:

- `list_domain_configurations`

## ListIndicesPaginatorName

```python
from mypy_boto3_iot.literals import ListIndicesPaginatorName
```

Values:

- `list_indices`

## ListJobExecutionsForJobPaginatorName

```python
from mypy_boto3_iot.literals import ListJobExecutionsForJobPaginatorName
```

Values:

- `list_job_executions_for_job`

## ListJobExecutionsForThingPaginatorName

```python
from mypy_boto3_iot.literals import ListJobExecutionsForThingPaginatorName
```

Values:

- `list_job_executions_for_thing`

## ListJobsPaginatorName

```python
from mypy_boto3_iot.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## ListMitigationActionsPaginatorName

```python
from mypy_boto3_iot.literals import ListMitigationActionsPaginatorName
```

Values:

- `list_mitigation_actions`

## ListOTAUpdatesPaginatorName

```python
from mypy_boto3_iot.literals import ListOTAUpdatesPaginatorName
```

Values:

- `list_ota_updates`

## ListOutgoingCertificatesPaginatorName

```python
from mypy_boto3_iot.literals import ListOutgoingCertificatesPaginatorName
```

Values:

- `list_outgoing_certificates`

## ListPoliciesPaginatorName

```python
from mypy_boto3_iot.literals import ListPoliciesPaginatorName
```

Values:

- `list_policies`

## ListPolicyPrincipalsPaginatorName

```python
from mypy_boto3_iot.literals import ListPolicyPrincipalsPaginatorName
```

Values:

- `list_policy_principals`

## ListPrincipalPoliciesPaginatorName

```python
from mypy_boto3_iot.literals import ListPrincipalPoliciesPaginatorName
```

Values:

- `list_principal_policies`

## ListPrincipalThingsPaginatorName

```python
from mypy_boto3_iot.literals import ListPrincipalThingsPaginatorName
```

Values:

- `list_principal_things`

## ListProvisioningTemplateVersionsPaginatorName

```python
from mypy_boto3_iot.literals import ListProvisioningTemplateVersionsPaginatorName
```

Values:

- `list_provisioning_template_versions`

## ListProvisioningTemplatesPaginatorName

```python
from mypy_boto3_iot.literals import ListProvisioningTemplatesPaginatorName
```

Values:

- `list_provisioning_templates`

## ListRoleAliasesPaginatorName

```python
from mypy_boto3_iot.literals import ListRoleAliasesPaginatorName
```

Values:

- `list_role_aliases`

## ListScheduledAuditsPaginatorName

```python
from mypy_boto3_iot.literals import ListScheduledAuditsPaginatorName
```

Values:

- `list_scheduled_audits`

## ListSecurityProfilesForTargetPaginatorName

```python
from mypy_boto3_iot.literals import ListSecurityProfilesForTargetPaginatorName
```

Values:

- `list_security_profiles_for_target`

## ListSecurityProfilesPaginatorName

```python
from mypy_boto3_iot.literals import ListSecurityProfilesPaginatorName
```

Values:

- `list_security_profiles`

## ListStreamsPaginatorName

```python
from mypy_boto3_iot.literals import ListStreamsPaginatorName
```

Values:

- `list_streams`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_iot.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListTargetsForPolicyPaginatorName

```python
from mypy_boto3_iot.literals import ListTargetsForPolicyPaginatorName
```

Values:

- `list_targets_for_policy`

## ListTargetsForSecurityProfilePaginatorName

```python
from mypy_boto3_iot.literals import ListTargetsForSecurityProfilePaginatorName
```

Values:

- `list_targets_for_security_profile`

## ListThingGroupsForThingPaginatorName

```python
from mypy_boto3_iot.literals import ListThingGroupsForThingPaginatorName
```

Values:

- `list_thing_groups_for_thing`

## ListThingGroupsPaginatorName

```python
from mypy_boto3_iot.literals import ListThingGroupsPaginatorName
```

Values:

- `list_thing_groups`

## ListThingPrincipalsPaginatorName

```python
from mypy_boto3_iot.literals import ListThingPrincipalsPaginatorName
```

Values:

- `list_thing_principals`

## ListThingRegistrationTaskReportsPaginatorName

```python
from mypy_boto3_iot.literals import ListThingRegistrationTaskReportsPaginatorName
```

Values:

- `list_thing_registration_task_reports`

## ListThingRegistrationTasksPaginatorName

```python
from mypy_boto3_iot.literals import ListThingRegistrationTasksPaginatorName
```

Values:

- `list_thing_registration_tasks`

## ListThingTypesPaginatorName

```python
from mypy_boto3_iot.literals import ListThingTypesPaginatorName
```

Values:

- `list_thing_types`

## ListThingsInBillingGroupPaginatorName

```python
from mypy_boto3_iot.literals import ListThingsInBillingGroupPaginatorName
```

Values:

- `list_things_in_billing_group`

## ListThingsInThingGroupPaginatorName

```python
from mypy_boto3_iot.literals import ListThingsInThingGroupPaginatorName
```

Values:

- `list_things_in_thing_group`

## ListThingsPaginatorName

```python
from mypy_boto3_iot.literals import ListThingsPaginatorName
```

Values:

- `list_things`

## ListTopicRuleDestinationsPaginatorName

```python
from mypy_boto3_iot.literals import ListTopicRuleDestinationsPaginatorName
```

Values:

- `list_topic_rule_destinations`

## ListTopicRulesPaginatorName

```python
from mypy_boto3_iot.literals import ListTopicRulesPaginatorName
```

Values:

- `list_topic_rules`

## ListV2LoggingLevelsPaginatorName

```python
from mypy_boto3_iot.literals import ListV2LoggingLevelsPaginatorName
```

Values:

- `list_v2_logging_levels`

## ListViolationEventsPaginatorName

```python
from mypy_boto3_iot.literals import ListViolationEventsPaginatorName
```

Values:

- `list_violation_events`

## LogLevel

```python
from mypy_boto3_iot.literals import LogLevel
```

Values:

- `DEBUG`
- `DISABLED`
- `ERROR`
- `INFO`
- `WARN`

## LogTargetType

```python
from mypy_boto3_iot.literals import LogTargetType
```

Values:

- `DEFAULT`
- `THING_GROUP`

## MessageFormat

```python
from mypy_boto3_iot.literals import MessageFormat
```

Values:

- `JSON`
- `RAW`

## MitigationActionType

```python
from mypy_boto3_iot.literals import MitigationActionType
```

Values:

- `ADD_THINGS_TO_THING_GROUP`
- `ENABLE_IOT_LOGGING`
- `PUBLISH_FINDING_TO_SNS`
- `REPLACE_DEFAULT_POLICY_VERSION`
- `UPDATE_CA_CERTIFICATE`
- `UPDATE_DEVICE_CERTIFICATE`

## ModelStatus

```python
from mypy_boto3_iot.literals import ModelStatus
```

Values:

- `ACTIVE`
- `EXPIRED`
- `PENDING_BUILD`

## OTAUpdateStatus

```python
from mypy_boto3_iot.literals import OTAUpdateStatus
```

Values:

- `CREATE_COMPLETE`
- `CREATE_FAILED`
- `CREATE_IN_PROGRESS`
- `CREATE_PENDING`

## PolicyTemplateName

```python
from mypy_boto3_iot.literals import PolicyTemplateName
```

Values:

- `BLANK_POLICY`

## ProtocolType

```python
from mypy_boto3_iot.literals import ProtocolType
```

Values:

- `HTTP`
- `MQTT`

## ReportType

```python
from mypy_boto3_iot.literals import ReportType
```

Values:

- `ERRORS`
- `RESULTS`

## ResourceType

```python
from mypy_boto3_iot.literals import ResourceType
```

Values:

- `ACCOUNT_SETTINGS`
- `CA_CERTIFICATE`
- `CLIENT_ID`
- `COGNITO_IDENTITY_POOL`
- `DEVICE_CERTIFICATE`
- `IAM_ROLE`
- `IOT_POLICY`
- `ROLE_ALIAS`

## ServerCertificateStatus

```python
from mypy_boto3_iot.literals import ServerCertificateStatus
```

Values:

- `INVALID`
- `VALID`

## ServiceType

```python
from mypy_boto3_iot.literals import ServiceType
```

Values:

- `CREDENTIAL_PROVIDER`
- `DATA`
- `JOBS`

## Status

```python
from mypy_boto3_iot.literals import Status
```

Values:

- `Cancelled`
- `Cancelling`
- `Completed`
- `Failed`
- `InProgress`

## TargetSelection

```python
from mypy_boto3_iot.literals import TargetSelection
```

Values:

- `CONTINUOUS`
- `SNAPSHOT`

## ThingConnectivityIndexingMode

```python
from mypy_boto3_iot.literals import ThingConnectivityIndexingMode
```

Values:

- `OFF`
- `STATUS`

## ThingGroupIndexingMode

```python
from mypy_boto3_iot.literals import ThingGroupIndexingMode
```

Values:

- `OFF`
- `ON`

## ThingIndexingMode

```python
from mypy_boto3_iot.literals import ThingIndexingMode
```

Values:

- `OFF`
- `REGISTRY`
- `REGISTRY_AND_SHADOW`

## TopicRuleDestinationStatus

```python
from mypy_boto3_iot.literals import TopicRuleDestinationStatus
```

Values:

- `DELETING`
- `DISABLED`
- `ENABLED`
- `ERROR`
- `IN_PROGRESS`

## ViolationEventType

```python
from mypy_boto3_iot.literals import ViolationEventType
```

Values:

- `alarm-cleared`
- `alarm-invalidated`
- `in-alarm`
