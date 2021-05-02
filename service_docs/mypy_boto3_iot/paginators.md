# Paginators for boto3 IoT module

> [Index](../index.md) > [IoT](./index.md) > Paginators

Auto-generated documentation for [IoT](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT)
type annotations stubs module [mypy_boto3_iot](https://pypi.org/project/mypy-boto3-iot/).

- [Paginators for boto3 IoT module](#paginators-for-boto3-iot-module)
  - [GetBehaviorModelTrainingSummariesPaginator](#getbehaviormodeltrainingsummariespaginator)
  - [ListActiveViolationsPaginator](#listactiveviolationspaginator)
  - [ListAttachedPoliciesPaginator](#listattachedpoliciespaginator)
  - [ListAuditFindingsPaginator](#listauditfindingspaginator)
  - [ListAuditMitigationActionsExecutionsPaginator](#listauditmitigationactionsexecutionspaginator)
  - [ListAuditMitigationActionsTasksPaginator](#listauditmitigationactionstaskspaginator)
  - [ListAuditSuppressionsPaginator](#listauditsuppressionspaginator)
  - [ListAuditTasksPaginator](#listaudittaskspaginator)
  - [ListAuthorizersPaginator](#listauthorizerspaginator)
  - [ListBillingGroupsPaginator](#listbillinggroupspaginator)
  - [ListCACertificatesPaginator](#listcacertificatespaginator)
  - [ListCertificatesPaginator](#listcertificatespaginator)
  - [ListCertificatesByCAPaginator](#listcertificatesbycapaginator)
  - [ListCustomMetricsPaginator](#listcustommetricspaginator)
  - [ListDetectMitigationActionsExecutionsPaginator](#listdetectmitigationactionsexecutionspaginator)
  - [ListDetectMitigationActionsTasksPaginator](#listdetectmitigationactionstaskspaginator)
  - [ListDimensionsPaginator](#listdimensionspaginator)
  - [ListDomainConfigurationsPaginator](#listdomainconfigurationspaginator)
  - [ListIndicesPaginator](#listindicespaginator)
  - [ListJobExecutionsForJobPaginator](#listjobexecutionsforjobpaginator)
  - [ListJobExecutionsForThingPaginator](#listjobexecutionsforthingpaginator)
  - [ListJobsPaginator](#listjobspaginator)
  - [ListMitigationActionsPaginator](#listmitigationactionspaginator)
  - [ListOTAUpdatesPaginator](#listotaupdatespaginator)
  - [ListOutgoingCertificatesPaginator](#listoutgoingcertificatespaginator)
  - [ListPoliciesPaginator](#listpoliciespaginator)
  - [ListPolicyPrincipalsPaginator](#listpolicyprincipalspaginator)
  - [ListPrincipalPoliciesPaginator](#listprincipalpoliciespaginator)
  - [ListPrincipalThingsPaginator](#listprincipalthingspaginator)
  - [ListProvisioningTemplateVersionsPaginator](#listprovisioningtemplateversionspaginator)
  - [ListProvisioningTemplatesPaginator](#listprovisioningtemplatespaginator)
  - [ListRoleAliasesPaginator](#listrolealiasespaginator)
  - [ListScheduledAuditsPaginator](#listscheduledauditspaginator)
  - [ListSecurityProfilesPaginator](#listsecurityprofilespaginator)
  - [ListSecurityProfilesForTargetPaginator](#listsecurityprofilesfortargetpaginator)
  - [ListStreamsPaginator](#liststreamspaginator)
  - [ListTagsForResourcePaginator](#listtagsforresourcepaginator)
  - [ListTargetsForPolicyPaginator](#listtargetsforpolicypaginator)
  - [ListTargetsForSecurityProfilePaginator](#listtargetsforsecurityprofilepaginator)
  - [ListThingGroupsPaginator](#listthinggroupspaginator)
  - [ListThingGroupsForThingPaginator](#listthinggroupsforthingpaginator)
  - [ListThingPrincipalsPaginator](#listthingprincipalspaginator)
  - [ListThingRegistrationTaskReportsPaginator](#listthingregistrationtaskreportspaginator)
  - [ListThingRegistrationTasksPaginator](#listthingregistrationtaskspaginator)
  - [ListThingTypesPaginator](#listthingtypespaginator)
  - [ListThingsPaginator](#listthingspaginator)
  - [ListThingsInBillingGroupPaginator](#listthingsinbillinggrouppaginator)
  - [ListThingsInThingGroupPaginator](#listthingsinthinggrouppaginator)
  - [ListTopicRuleDestinationsPaginator](#listtopicruledestinationspaginator)
  - [ListTopicRulesPaginator](#listtopicrulespaginator)
  - [ListV2LoggingLevelsPaginator](#listv2logginglevelspaginator)
  - [ListViolationEventsPaginator](#listviolationeventspaginator)

## GetBehaviorModelTrainingSummariesPaginator

Type annotations for `boto3.client("iot").get_paginator("get_behavior_model_training_summaries")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import GetBehaviorModelTrainingSummariesPaginator

def get_get_behavior_model_training_summaries_paginator() -> GetBehaviorModelTrainingSummariesPaginator:
    return boto3.client("iot").get_paginator("get_behavior_model_training_summaries")
```

[Paginator.GetBehaviorModelTrainingSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.GetBehaviorModelTrainingSummaries)

```python
class GetBehaviorModelTrainingSummariesPaginator(Boto3Paginator):
    def paginate(
        self,
        securityProfileName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetBehaviorModelTrainingSummariesResponseTypeDef]:
        pass
```
## ListActiveViolationsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_active_violations")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListActiveViolationsPaginator

def get_list_active_violations_paginator() -> ListActiveViolationsPaginator:
    return boto3.client("iot").get_paginator("list_active_violations")
```

[Paginator.ListActiveViolations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListActiveViolations)

```python
class ListActiveViolationsPaginator(Boto3Paginator):
    def paginate(
        self,
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaType = None,
        listSuppressedAlerts: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListActiveViolationsResponseTypeDef]:
        pass
```
## ListAttachedPoliciesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_attached_policies")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAttachedPoliciesPaginator

def get_list_attached_policies_paginator() -> ListAttachedPoliciesPaginator:
    return boto3.client("iot").get_paginator("list_attached_policies")
```

[Paginator.ListAttachedPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAttachedPolicies)

```python
class ListAttachedPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        target: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttachedPoliciesResponseTypeDef]:
        pass
```
## ListAuditFindingsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_audit_findings")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAuditFindingsPaginator

def get_list_audit_findings_paginator() -> ListAuditFindingsPaginator:
    return boto3.client("iot").get_paginator("list_audit_findings")
```

[Paginator.ListAuditFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAuditFindings)

```python
class ListAuditFindingsPaginator(Boto3Paginator):
    def paginate(
        self,
        taskId: str = None,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        startTime: datetime = None,
        endTime: datetime = None,
        listSuppressedFindings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditFindingsResponseTypeDef]:
        pass
```
## ListAuditMitigationActionsExecutionsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_audit_mitigation_actions_executions")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAuditMitigationActionsExecutionsPaginator

def get_list_audit_mitigation_actions_executions_paginator() -> ListAuditMitigationActionsExecutionsPaginator:
    return boto3.client("iot").get_paginator("list_audit_mitigation_actions_executions")
```

[Paginator.ListAuditMitigationActionsExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsExecutions)

```python
class ListAuditMitigationActionsExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        taskId: str,
        findingId: str,
        actionStatus: AuditMitigationActionsExecutionStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditMitigationActionsExecutionsResponseTypeDef]:
        pass
```
## ListAuditMitigationActionsTasksPaginator

Type annotations for `boto3.client("iot").get_paginator("list_audit_mitigation_actions_tasks")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAuditMitigationActionsTasksPaginator

def get_list_audit_mitigation_actions_tasks_paginator() -> ListAuditMitigationActionsTasksPaginator:
    return boto3.client("iot").get_paginator("list_audit_mitigation_actions_tasks")
```

[Paginator.ListAuditMitigationActionsTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAuditMitigationActionsTasks)

```python
class ListAuditMitigationActionsTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        auditTaskId: str = None,
        findingId: str = None,
        taskStatus: AuditMitigationActionsTaskStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditMitigationActionsTasksResponseTypeDef]:
        pass
```
## ListAuditSuppressionsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_audit_suppressions")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAuditSuppressionsPaginator

def get_list_audit_suppressions_paginator() -> ListAuditSuppressionsPaginator:
    return boto3.client("iot").get_paginator("list_audit_suppressions")
```

[Paginator.ListAuditSuppressions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAuditSuppressions)

```python
class ListAuditSuppressionsPaginator(Boto3Paginator):
    def paginate(
        self,
        checkName: str = None,
        resourceIdentifier: "ResourceIdentifierTypeDef" = None,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditSuppressionsResponseTypeDef]:
        pass
```
## ListAuditTasksPaginator

Type annotations for `boto3.client("iot").get_paginator("list_audit_tasks")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAuditTasksPaginator

def get_list_audit_tasks_paginator() -> ListAuditTasksPaginator:
    return boto3.client("iot").get_paginator("list_audit_tasks")
```

[Paginator.ListAuditTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAuditTasks)

```python
class ListAuditTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        taskType: AuditTaskType = None,
        taskStatus: AuditTaskStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuditTasksResponseTypeDef]:
        pass
```
## ListAuthorizersPaginator

Type annotations for `boto3.client("iot").get_paginator("list_authorizers")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListAuthorizersPaginator

def get_list_authorizers_paginator() -> ListAuthorizersPaginator:
    return boto3.client("iot").get_paginator("list_authorizers")
```

[Paginator.ListAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListAuthorizers)

```python
class ListAuthorizersPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        status: AuthorizerStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAuthorizersResponseTypeDef]:
        pass
```
## ListBillingGroupsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_billing_groups")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListBillingGroupsPaginator

def get_list_billing_groups_paginator() -> ListBillingGroupsPaginator:
    return boto3.client("iot").get_paginator("list_billing_groups")
```

[Paginator.ListBillingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListBillingGroups)

```python
class ListBillingGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        namePrefixFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBillingGroupsResponseTypeDef]:
        pass
```
## ListCACertificatesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_ca_certificates")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListCACertificatesPaginator

def get_list_ca_certificates_paginator() -> ListCACertificatesPaginator:
    return boto3.client("iot").get_paginator("list_ca_certificates")
```

[Paginator.ListCACertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListCACertificates)

```python
class ListCACertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCACertificatesResponseTypeDef]:
        pass
```
## ListCertificatesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_certificates")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListCertificatesPaginator

def get_list_certificates_paginator() -> ListCertificatesPaginator:
    return boto3.client("iot").get_paginator("list_certificates")
```

[Paginator.ListCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListCertificates)

```python
class ListCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesResponseTypeDef]:
        pass
```
## ListCertificatesByCAPaginator

Type annotations for `boto3.client("iot").get_paginator("list_certificates_by_ca")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListCertificatesByCAPaginator

def get_list_certificates_by_ca_paginator() -> ListCertificatesByCAPaginator:
    return boto3.client("iot").get_paginator("list_certificates_by_ca")
```

[Paginator.ListCertificatesByCA documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListCertificatesByCA)

```python
class ListCertificatesByCAPaginator(Boto3Paginator):
    def paginate(
        self,
        caCertificateId: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesByCAResponseTypeDef]:
        pass
```
## ListCustomMetricsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_custom_metrics")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListCustomMetricsPaginator

def get_list_custom_metrics_paginator() -> ListCustomMetricsPaginator:
    return boto3.client("iot").get_paginator("list_custom_metrics")
```

[Paginator.ListCustomMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListCustomMetrics)

```python
class ListCustomMetricsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomMetricsResponseTypeDef]:
        pass
```
## ListDetectMitigationActionsExecutionsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_detect_mitigation_actions_executions")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListDetectMitigationActionsExecutionsPaginator

def get_list_detect_mitigation_actions_executions_paginator() -> ListDetectMitigationActionsExecutionsPaginator:
    return boto3.client("iot").get_paginator("list_detect_mitigation_actions_executions")
```

[Paginator.ListDetectMitigationActionsExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsExecutions)

```python
class ListDetectMitigationActionsExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        taskId: str = None,
        violationId: str = None,
        thingName: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDetectMitigationActionsExecutionsResponseTypeDef]:
        pass
```
## ListDetectMitigationActionsTasksPaginator

Type annotations for `boto3.client("iot").get_paginator("list_detect_mitigation_actions_tasks")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListDetectMitigationActionsTasksPaginator

def get_list_detect_mitigation_actions_tasks_paginator() -> ListDetectMitigationActionsTasksPaginator:
    return boto3.client("iot").get_paginator("list_detect_mitigation_actions_tasks")
```

[Paginator.ListDetectMitigationActionsTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListDetectMitigationActionsTasks)

```python
class ListDetectMitigationActionsTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDetectMitigationActionsTasksResponseTypeDef]:
        pass
```
## ListDimensionsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_dimensions")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListDimensionsPaginator

def get_list_dimensions_paginator() -> ListDimensionsPaginator:
    return boto3.client("iot").get_paginator("list_dimensions")
```

[Paginator.ListDimensions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListDimensions)

```python
class ListDimensionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDimensionsResponseTypeDef]:
        pass
```
## ListDomainConfigurationsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_domain_configurations")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListDomainConfigurationsPaginator

def get_list_domain_configurations_paginator() -> ListDomainConfigurationsPaginator:
    return boto3.client("iot").get_paginator("list_domain_configurations")
```

[Paginator.ListDomainConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListDomainConfigurations)

```python
class ListDomainConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        serviceType: ServiceType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainConfigurationsResponseTypeDef]:
        pass
```
## ListIndicesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_indices")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListIndicesPaginator

def get_list_indices_paginator() -> ListIndicesPaginator:
    return boto3.client("iot").get_paginator("list_indices")
```

[Paginator.ListIndices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListIndices)

```python
class ListIndicesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIndicesResponseTypeDef]:
        pass
```
## ListJobExecutionsForJobPaginator

Type annotations for `boto3.client("iot").get_paginator("list_job_executions_for_job")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListJobExecutionsForJobPaginator

def get_list_job_executions_for_job_paginator() -> ListJobExecutionsForJobPaginator:
    return boto3.client("iot").get_paginator("list_job_executions_for_job")
```

[Paginator.ListJobExecutionsForJob documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForJob)

```python
class ListJobExecutionsForJobPaginator(Boto3Paginator):
    def paginate(
        self,
        jobId: str,
        status: JobExecutionStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobExecutionsForJobResponseTypeDef]:
        pass
```
## ListJobExecutionsForThingPaginator

Type annotations for `boto3.client("iot").get_paginator("list_job_executions_for_thing")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListJobExecutionsForThingPaginator

def get_list_job_executions_for_thing_paginator() -> ListJobExecutionsForThingPaginator:
    return boto3.client("iot").get_paginator("list_job_executions_for_thing")
```

[Paginator.ListJobExecutionsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListJobExecutionsForThing)

```python
class ListJobExecutionsForThingPaginator(Boto3Paginator):
    def paginate(
        self,
        thingName: str,
        status: JobExecutionStatus = None,
        namespaceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobExecutionsForThingResponseTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("iot").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        status: JobStatus = None,
        targetSelection: TargetSelection = None,
        thingGroupName: str = None,
        thingGroupId: str = None,
        namespaceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResponseTypeDef]:
        pass
```
## ListMitigationActionsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_mitigation_actions")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListMitigationActionsPaginator

def get_list_mitigation_actions_paginator() -> ListMitigationActionsPaginator:
    return boto3.client("iot").get_paginator("list_mitigation_actions")
```

[Paginator.ListMitigationActions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListMitigationActions)

```python
class ListMitigationActionsPaginator(Boto3Paginator):
    def paginate(
        self,
        actionType: MitigationActionType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMitigationActionsResponseTypeDef]:
        pass
```
## ListOTAUpdatesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_ota_updates")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListOTAUpdatesPaginator

def get_list_ota_updates_paginator() -> ListOTAUpdatesPaginator:
    return boto3.client("iot").get_paginator("list_ota_updates")
```

[Paginator.ListOTAUpdates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListOTAUpdates)

```python
class ListOTAUpdatesPaginator(Boto3Paginator):
    def paginate(
        self,
        otaUpdateStatus: OTAUpdateStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOTAUpdatesResponseTypeDef]:
        pass
```
## ListOutgoingCertificatesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_outgoing_certificates")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListOutgoingCertificatesPaginator

def get_list_outgoing_certificates_paginator() -> ListOutgoingCertificatesPaginator:
    return boto3.client("iot").get_paginator("list_outgoing_certificates")
```

[Paginator.ListOutgoingCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListOutgoingCertificates)

```python
class ListOutgoingCertificatesPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOutgoingCertificatesResponseTypeDef]:
        pass
```
## ListPoliciesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_policies")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListPoliciesPaginator

def get_list_policies_paginator() -> ListPoliciesPaginator:
    return boto3.client("iot").get_paginator("list_policies")
```

[Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListPolicies)

```python
class ListPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPoliciesResponseTypeDef]:
        pass
```
## ListPolicyPrincipalsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_policy_principals")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListPolicyPrincipalsPaginator

def get_list_policy_principals_paginator() -> ListPolicyPrincipalsPaginator:
    return boto3.client("iot").get_paginator("list_policy_principals")
```

[Paginator.ListPolicyPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListPolicyPrincipals)

```python
class ListPolicyPrincipalsPaginator(Boto3Paginator):
    def paginate(
        self,
        policyName: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPolicyPrincipalsResponseTypeDef]:
        pass
```
## ListPrincipalPoliciesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_principal_policies")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListPrincipalPoliciesPaginator

def get_list_principal_policies_paginator() -> ListPrincipalPoliciesPaginator:
    return boto3.client("iot").get_paginator("list_principal_policies")
```

[Paginator.ListPrincipalPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListPrincipalPolicies)

```python
class ListPrincipalPoliciesPaginator(Boto3Paginator):
    def paginate(
        self,
        principal: str,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrincipalPoliciesResponseTypeDef]:
        pass
```
## ListPrincipalThingsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_principal_things")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListPrincipalThingsPaginator

def get_list_principal_things_paginator() -> ListPrincipalThingsPaginator:
    return boto3.client("iot").get_paginator("list_principal_things")
```

[Paginator.ListPrincipalThings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListPrincipalThings)

```python
class ListPrincipalThingsPaginator(Boto3Paginator):
    def paginate(
        self,
        principal: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrincipalThingsResponseTypeDef]:
        pass
```
## ListProvisioningTemplateVersionsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_provisioning_template_versions")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListProvisioningTemplateVersionsPaginator

def get_list_provisioning_template_versions_paginator() -> ListProvisioningTemplateVersionsPaginator:
    return boto3.client("iot").get_paginator("list_provisioning_template_versions")
```

[Paginator.ListProvisioningTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplateVersions)

```python
class ListProvisioningTemplateVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        templateName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisioningTemplateVersionsResponseTypeDef]:
        pass
```
## ListProvisioningTemplatesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_provisioning_templates")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListProvisioningTemplatesPaginator

def get_list_provisioning_templates_paginator() -> ListProvisioningTemplatesPaginator:
    return boto3.client("iot").get_paginator("list_provisioning_templates")
```

[Paginator.ListProvisioningTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListProvisioningTemplates)

```python
class ListProvisioningTemplatesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisioningTemplatesResponseTypeDef]:
        pass
```
## ListRoleAliasesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_role_aliases")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListRoleAliasesPaginator

def get_list_role_aliases_paginator() -> ListRoleAliasesPaginator:
    return boto3.client("iot").get_paginator("list_role_aliases")
```

[Paginator.ListRoleAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListRoleAliases)

```python
class ListRoleAliasesPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRoleAliasesResponseTypeDef]:
        pass
```
## ListScheduledAuditsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_scheduled_audits")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListScheduledAuditsPaginator

def get_list_scheduled_audits_paginator() -> ListScheduledAuditsPaginator:
    return boto3.client("iot").get_paginator("list_scheduled_audits")
```

[Paginator.ListScheduledAudits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListScheduledAudits)

```python
class ListScheduledAuditsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScheduledAuditsResponseTypeDef]:
        pass
```
## ListSecurityProfilesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_security_profiles")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListSecurityProfilesPaginator

def get_list_security_profiles_paginator() -> ListSecurityProfilesPaginator:
    return boto3.client("iot").get_paginator("list_security_profiles")
```

[Paginator.ListSecurityProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListSecurityProfiles)

```python
class ListSecurityProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        dimensionName: str = None,
        metricName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesResponseTypeDef]:
        pass
```
## ListSecurityProfilesForTargetPaginator

Type annotations for `boto3.client("iot").get_paginator("list_security_profiles_for_target")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListSecurityProfilesForTargetPaginator

def get_list_security_profiles_for_target_paginator() -> ListSecurityProfilesForTargetPaginator:
    return boto3.client("iot").get_paginator("list_security_profiles_for_target")
```

[Paginator.ListSecurityProfilesForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListSecurityProfilesForTarget)

```python
class ListSecurityProfilesForTargetPaginator(Boto3Paginator):
    def paginate(
        self,
        securityProfileTargetArn: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityProfilesForTargetResponseTypeDef]:
        pass
```
## ListStreamsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_streams")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListStreamsPaginator

def get_list_streams_paginator() -> ListStreamsPaginator:
    return boto3.client("iot").get_paginator("list_streams")
```

[Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListStreams)

```python
class ListStreamsPaginator(Boto3Paginator):
    def paginate(
        self,
        ascendingOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamsResponseTypeDef]:
        pass
```
## ListTagsForResourcePaginator

Type annotations for `boto3.client("iot").get_paginator("list_tags_for_resource")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListTagsForResourcePaginator

def get_list_tags_for_resource_paginator() -> ListTagsForResourcePaginator:
    return boto3.client("iot").get_paginator("list_tags_for_resource")
```

[Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListTagsForResource)

```python
class ListTagsForResourcePaginator(Boto3Paginator):
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        pass
```
## ListTargetsForPolicyPaginator

Type annotations for `boto3.client("iot").get_paginator("list_targets_for_policy")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListTargetsForPolicyPaginator

def get_list_targets_for_policy_paginator() -> ListTargetsForPolicyPaginator:
    return boto3.client("iot").get_paginator("list_targets_for_policy")
```

[Paginator.ListTargetsForPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListTargetsForPolicy)

```python
class ListTargetsForPolicyPaginator(Boto3Paginator):
    def paginate(
        self,
        policyName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForPolicyResponseTypeDef]:
        pass
```
## ListTargetsForSecurityProfilePaginator

Type annotations for `boto3.client("iot").get_paginator("list_targets_for_security_profile")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListTargetsForSecurityProfilePaginator

def get_list_targets_for_security_profile_paginator() -> ListTargetsForSecurityProfilePaginator:
    return boto3.client("iot").get_paginator("list_targets_for_security_profile")
```

[Paginator.ListTargetsForSecurityProfile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListTargetsForSecurityProfile)

```python
class ListTargetsForSecurityProfilePaginator(Boto3Paginator):
    def paginate(
        self,
        securityProfileName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTargetsForSecurityProfileResponseTypeDef]:
        pass
```
## ListThingGroupsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_thing_groups")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingGroupsPaginator

def get_list_thing_groups_paginator() -> ListThingGroupsPaginator:
    return boto3.client("iot").get_paginator("list_thing_groups")
```

[Paginator.ListThingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingGroups)

```python
class ListThingGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        parentGroup: str = None,
        namePrefixFilter: str = None,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingGroupsResponseTypeDef]:
        pass
```
## ListThingGroupsForThingPaginator

Type annotations for `boto3.client("iot").get_paginator("list_thing_groups_for_thing")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingGroupsForThingPaginator

def get_list_thing_groups_for_thing_paginator() -> ListThingGroupsForThingPaginator:
    return boto3.client("iot").get_paginator("list_thing_groups_for_thing")
```

[Paginator.ListThingGroupsForThing documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingGroupsForThing)

```python
class ListThingGroupsForThingPaginator(Boto3Paginator):
    def paginate(
        self,
        thingName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingGroupsForThingResponseTypeDef]:
        pass
```
## ListThingPrincipalsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_thing_principals")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingPrincipalsPaginator

def get_list_thing_principals_paginator() -> ListThingPrincipalsPaginator:
    return boto3.client("iot").get_paginator("list_thing_principals")
```

[Paginator.ListThingPrincipals documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingPrincipals)

```python
class ListThingPrincipalsPaginator(Boto3Paginator):
    def paginate(
        self,
        thingName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingPrincipalsResponseTypeDef]:
        pass
```
## ListThingRegistrationTaskReportsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_thing_registration_task_reports")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingRegistrationTaskReportsPaginator

def get_list_thing_registration_task_reports_paginator() -> ListThingRegistrationTaskReportsPaginator:
    return boto3.client("iot").get_paginator("list_thing_registration_task_reports")
```

[Paginator.ListThingRegistrationTaskReports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTaskReports)

```python
class ListThingRegistrationTaskReportsPaginator(Boto3Paginator):
    def paginate(
        self,
        taskId: str,
        reportType: ReportType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingRegistrationTaskReportsResponseTypeDef]:
        pass
```
## ListThingRegistrationTasksPaginator

Type annotations for `boto3.client("iot").get_paginator("list_thing_registration_tasks")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingRegistrationTasksPaginator

def get_list_thing_registration_tasks_paginator() -> ListThingRegistrationTasksPaginator:
    return boto3.client("iot").get_paginator("list_thing_registration_tasks")
```

[Paginator.ListThingRegistrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingRegistrationTasks)

```python
class ListThingRegistrationTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        status: Status = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingRegistrationTasksResponseTypeDef]:
        pass
```
## ListThingTypesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_thing_types")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingTypesPaginator

def get_list_thing_types_paginator() -> ListThingTypesPaginator:
    return boto3.client("iot").get_paginator("list_thing_types")
```

[Paginator.ListThingTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingTypes)

```python
class ListThingTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        thingTypeName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingTypesResponseTypeDef]:
        pass
```
## ListThingsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_things")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingsPaginator

def get_list_things_paginator() -> ListThingsPaginator:
    return boto3.client("iot").get_paginator("list_things")
```

[Paginator.ListThings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThings)

```python
class ListThingsPaginator(Boto3Paginator):
    def paginate(
        self,
        attributeName: str = None,
        attributeValue: str = None,
        thingTypeName: str = None,
        usePrefixAttributeValue: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsResponseTypeDef]:
        pass
```
## ListThingsInBillingGroupPaginator

Type annotations for `boto3.client("iot").get_paginator("list_things_in_billing_group")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingsInBillingGroupPaginator

def get_list_things_in_billing_group_paginator() -> ListThingsInBillingGroupPaginator:
    return boto3.client("iot").get_paginator("list_things_in_billing_group")
```

[Paginator.ListThingsInBillingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingsInBillingGroup)

```python
class ListThingsInBillingGroupPaginator(Boto3Paginator):
    def paginate(
        self,
        billingGroupName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsInBillingGroupResponseTypeDef]:
        pass
```
## ListThingsInThingGroupPaginator

Type annotations for `boto3.client("iot").get_paginator("list_things_in_thing_group")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListThingsInThingGroupPaginator

def get_list_things_in_thing_group_paginator() -> ListThingsInThingGroupPaginator:
    return boto3.client("iot").get_paginator("list_things_in_thing_group")
```

[Paginator.ListThingsInThingGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListThingsInThingGroup)

```python
class ListThingsInThingGroupPaginator(Boto3Paginator):
    def paginate(
        self,
        thingGroupName: str,
        recursive: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThingsInThingGroupResponseTypeDef]:
        pass
```
## ListTopicRuleDestinationsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_topic_rule_destinations")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListTopicRuleDestinationsPaginator

def get_list_topic_rule_destinations_paginator() -> ListTopicRuleDestinationsPaginator:
    return boto3.client("iot").get_paginator("list_topic_rule_destinations")
```

[Paginator.ListTopicRuleDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListTopicRuleDestinations)

```python
class ListTopicRuleDestinationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicRuleDestinationsResponseTypeDef]:
        pass
```
## ListTopicRulesPaginator

Type annotations for `boto3.client("iot").get_paginator("list_topic_rules")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListTopicRulesPaginator

def get_list_topic_rules_paginator() -> ListTopicRulesPaginator:
    return boto3.client("iot").get_paginator("list_topic_rules")
```

[Paginator.ListTopicRules documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListTopicRules)

```python
class ListTopicRulesPaginator(Boto3Paginator):
    def paginate(
        self,
        topic: str = None,
        ruleDisabled: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTopicRulesResponseTypeDef]:
        pass
```
## ListV2LoggingLevelsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_v2_logging_levels")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListV2LoggingLevelsPaginator

def get_list_v2_logging_levels_paginator() -> ListV2LoggingLevelsPaginator:
    return boto3.client("iot").get_paginator("list_v2_logging_levels")
```

[Paginator.ListV2LoggingLevels documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListV2LoggingLevels)

```python
class ListV2LoggingLevelsPaginator(Boto3Paginator):
    def paginate(
        self,
        targetType: LogTargetType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListV2LoggingLevelsResponseTypeDef]:
        pass
```
## ListViolationEventsPaginator

Type annotations for `boto3.client("iot").get_paginator("list_violation_events")`.

Can be used directly:

```python
from mypy_boto3_iot.paginators import ListViolationEventsPaginator

def get_list_violation_events_paginator() -> ListViolationEventsPaginator:
    return boto3.client("iot").get_paginator("list_violation_events")
```

[Paginator.ListViolationEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Paginator.ListViolationEvents)

```python
class ListViolationEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        startTime: datetime,
        endTime: datetime,
        thingName: str = None,
        securityProfileName: str = None,
        behaviorCriteriaType: BehaviorCriteriaType = None,
        listSuppressedAlerts: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListViolationEventsResponseTypeDef]:
        pass
```