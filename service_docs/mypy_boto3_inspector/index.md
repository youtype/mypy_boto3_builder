# Type annotations for boto3 Inspector module

> [Index](../index.md) > Inspector

Auto-generated documentation for [Inspector](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector)
type annotations stubs module [mypy_boto3_inspector](https://pypi.org/project/mypy-boto3-inspector/).

```bash
pip install mypy-boto3-inspector
```

- [Type annotations for boto3 Inspector module](#type-annotations-for-boto3-inspector-module)
  - [InspectorClient](#inspectorclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## InspectorClient

Type annotations for  `boto3.client("inspector")` as [InspectorClient](./client.md)

Can be used directly:

```python
from mypy_boto3_inspector.client import InspectorClient
```


InspectorClient [exceptions](./client.md#exceptions)



### Methods
- [add_attributes_to_findings](./client.md#add-attributes-to-findings)
- [can_paginate](./client.md#can-paginate)
- [create_assessment_target](./client.md#create-assessment-target)
- [create_assessment_template](./client.md#create-assessment-template)
- [create_exclusions_preview](./client.md#create-exclusions-preview)
- [create_resource_group](./client.md#create-resource-group)
- [delete_assessment_run](./client.md#delete-assessment-run)
- [delete_assessment_target](./client.md#delete-assessment-target)
- [delete_assessment_template](./client.md#delete-assessment-template)
- [describe_assessment_runs](./client.md#describe-assessment-runs)
- [describe_assessment_targets](./client.md#describe-assessment-targets)
- [describe_assessment_templates](./client.md#describe-assessment-templates)
- [describe_cross_account_access_role](./client.md#describe-cross-account-access-role)
- [describe_exclusions](./client.md#describe-exclusions)
- [describe_findings](./client.md#describe-findings)
- [describe_resource_groups](./client.md#describe-resource-groups)
- [describe_rules_packages](./client.md#describe-rules-packages)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_assessment_report](./client.md#get-assessment-report)
- [get_exclusions_preview](./client.md#get-exclusions-preview)
- [get_paginator](./client.md#get-paginator)
- [get_telemetry_metadata](./client.md#get-telemetry-metadata)
- [list_assessment_run_agents](./client.md#list-assessment-run-agents)
- [list_assessment_runs](./client.md#list-assessment-runs)
- [list_assessment_targets](./client.md#list-assessment-targets)
- [list_assessment_templates](./client.md#list-assessment-templates)
- [list_event_subscriptions](./client.md#list-event-subscriptions)
- [list_exclusions](./client.md#list-exclusions)
- [list_findings](./client.md#list-findings)
- [list_rules_packages](./client.md#list-rules-packages)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [preview_agents](./client.md#preview-agents)
- [register_cross_account_access_role](./client.md#register-cross-account-access-role)
- [remove_attributes_from_findings](./client.md#remove-attributes-from-findings)
- [set_tags_for_resource](./client.md#set-tags-for-resource)
- [start_assessment_run](./client.md#start-assessment-run)
- [stop_assessment_run](./client.md#stop-assessment-run)
- [subscribe_to_event](./client.md#subscribe-to-event)
- [unsubscribe_from_event](./client.md#unsubscribe-from-event)
- [update_assessment_target](./client.md#update-assessment-target)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [AgentsAlreadyRunningAssessmentException](./client.md#agentsalreadyrunningassessmentexception)
- [AssessmentRunInProgressException](./client.md#assessmentruninprogressexception)
- [ClientError](./client.md#clienterror)
- [InternalException](./client.md#internalexception)
- [InvalidCrossAccountRoleException](./client.md#invalidcrossaccountroleexception)
- [InvalidInputException](./client.md#invalidinputexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NoSuchEntityException](./client.md#nosuchentityexception)
- [PreviewGenerationInProgressException](./client.md#previewgenerationinprogressexception)
- [ServiceTemporarilyUnavailableException](./client.md#servicetemporarilyunavailableexception)
- [UnsupportedFeatureException](./client.md#unsupportedfeatureexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("inspector").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_inspector.paginators import ListAssessmentRunAgentsPaginator, ...
```

- [ListAssessmentRunAgentsPaginator](./paginators.md#listassessmentrunagentspaginator)
- [ListAssessmentRunsPaginator](./paginators.md#listassessmentrunspaginator)
- [ListAssessmentTargetsPaginator](./paginators.md#listassessmenttargetspaginator)
- [ListAssessmentTemplatesPaginator](./paginators.md#listassessmenttemplatespaginator)
- [ListEventSubscriptionsPaginator](./paginators.md#listeventsubscriptionspaginator)
- [ListExclusionsPaginator](./paginators.md#listexclusionspaginator)
- [ListFindingsPaginator](./paginators.md#listfindingspaginator)
- [ListRulesPackagesPaginator](./paginators.md#listrulespackagespaginator)
- [PreviewAgentsPaginator](./paginators.md#previewagentspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_inspector.literals import AgentHealth, ...
```

- [AgentHealth](./literals.md#agenthealth)
- [AgentHealthCode](./literals.md#agenthealthcode)
- [AssessmentRunNotificationSnsStatusCode](./literals.md#assessmentrunnotificationsnsstatuscode)
- [AssessmentRunState](./literals.md#assessmentrunstate)
- [AssetType](./literals.md#assettype)
- [FailedItemErrorCode](./literals.md#faileditemerrorcode)
- [InspectorEvent](./literals.md#inspectorevent)
- [ListAssessmentRunAgentsPaginatorName](./literals.md#listassessmentrunagentspaginatorname)
- [ListAssessmentRunsPaginatorName](./literals.md#listassessmentrunspaginatorname)
- [ListAssessmentTargetsPaginatorName](./literals.md#listassessmenttargetspaginatorname)
- [ListAssessmentTemplatesPaginatorName](./literals.md#listassessmenttemplatespaginatorname)
- [ListEventSubscriptionsPaginatorName](./literals.md#listeventsubscriptionspaginatorname)
- [ListExclusionsPaginatorName](./literals.md#listexclusionspaginatorname)
- [ListFindingsPaginatorName](./literals.md#listfindingspaginatorname)
- [ListRulesPackagesPaginatorName](./literals.md#listrulespackagespaginatorname)
- [Locale](./literals.md#locale)
- [PreviewAgentsPaginatorName](./literals.md#previewagentspaginatorname)
- [PreviewStatus](./literals.md#previewstatus)
- [ReportFileFormat](./literals.md#reportfileformat)
- [ReportStatus](./literals.md#reportstatus)
- [ReportType](./literals.md#reporttype)
- [ScopeType](./literals.md#scopetype)
- [Severity](./literals.md#severity)
- [StopAction](./literals.md#stopaction)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_inspector.type_defs import AddAttributesToFindingsResponseTypeDef, ...
```

- [AddAttributesToFindingsResponseTypeDef](./type_defs.md#addattributestofindingsresponsetypedef)
- [AgentFilterTypeDef](./type_defs.md#agentfiltertypedef)
- [AgentPreviewTypeDef](./type_defs.md#agentpreviewtypedef)
- [AssessmentRunAgentTypeDef](./type_defs.md#assessmentrunagenttypedef)
- [AssessmentRunFilterTypeDef](./type_defs.md#assessmentrunfiltertypedef)
- [AssessmentRunNotificationTypeDef](./type_defs.md#assessmentrunnotificationtypedef)
- [AssessmentRunStateChangeTypeDef](./type_defs.md#assessmentrunstatechangetypedef)
- [AssessmentRunTypeDef](./type_defs.md#assessmentruntypedef)
- [AssessmentTargetFilterTypeDef](./type_defs.md#assessmenttargetfiltertypedef)
- [AssessmentTargetTypeDef](./type_defs.md#assessmenttargettypedef)
- [AssessmentTemplateFilterTypeDef](./type_defs.md#assessmenttemplatefiltertypedef)
- [AssessmentTemplateTypeDef](./type_defs.md#assessmenttemplatetypedef)
- [AssetAttributesTypeDef](./type_defs.md#assetattributestypedef)
- [AttributeTypeDef](./type_defs.md#attributetypedef)
- [CreateAssessmentTargetResponseTypeDef](./type_defs.md#createassessmenttargetresponsetypedef)
- [CreateAssessmentTemplateResponseTypeDef](./type_defs.md#createassessmenttemplateresponsetypedef)
- [CreateExclusionsPreviewResponseTypeDef](./type_defs.md#createexclusionspreviewresponsetypedef)
- [CreateResourceGroupResponseTypeDef](./type_defs.md#createresourcegroupresponsetypedef)
- [DescribeAssessmentRunsResponseTypeDef](./type_defs.md#describeassessmentrunsresponsetypedef)
- [DescribeAssessmentTargetsResponseTypeDef](./type_defs.md#describeassessmenttargetsresponsetypedef)
- [DescribeAssessmentTemplatesResponseTypeDef](./type_defs.md#describeassessmenttemplatesresponsetypedef)
- [DescribeCrossAccountAccessRoleResponseTypeDef](./type_defs.md#describecrossaccountaccessroleresponsetypedef)
- [DescribeExclusionsResponseTypeDef](./type_defs.md#describeexclusionsresponsetypedef)
- [DescribeFindingsResponseTypeDef](./type_defs.md#describefindingsresponsetypedef)
- [DescribeResourceGroupsResponseTypeDef](./type_defs.md#describeresourcegroupsresponsetypedef)
- [DescribeRulesPackagesResponseTypeDef](./type_defs.md#describerulespackagesresponsetypedef)
- [DurationRangeTypeDef](./type_defs.md#durationrangetypedef)
- [EventSubscriptionTypeDef](./type_defs.md#eventsubscriptiontypedef)
- [ExclusionPreviewTypeDef](./type_defs.md#exclusionpreviewtypedef)
- [ExclusionTypeDef](./type_defs.md#exclusiontypedef)
- [FailedItemDetailsTypeDef](./type_defs.md#faileditemdetailstypedef)
- [FindingFilterTypeDef](./type_defs.md#findingfiltertypedef)
- [FindingTypeDef](./type_defs.md#findingtypedef)
- [GetAssessmentReportResponseTypeDef](./type_defs.md#getassessmentreportresponsetypedef)
- [GetExclusionsPreviewResponseTypeDef](./type_defs.md#getexclusionspreviewresponsetypedef)
- [GetTelemetryMetadataResponseTypeDef](./type_defs.md#gettelemetrymetadataresponsetypedef)
- [InspectorServiceAttributesTypeDef](./type_defs.md#inspectorserviceattributestypedef)
- [ListAssessmentRunAgentsResponseTypeDef](./type_defs.md#listassessmentrunagentsresponsetypedef)
- [ListAssessmentRunsResponseTypeDef](./type_defs.md#listassessmentrunsresponsetypedef)
- [ListAssessmentTargetsResponseTypeDef](./type_defs.md#listassessmenttargetsresponsetypedef)
- [ListAssessmentTemplatesResponseTypeDef](./type_defs.md#listassessmenttemplatesresponsetypedef)
- [ListEventSubscriptionsResponseTypeDef](./type_defs.md#listeventsubscriptionsresponsetypedef)
- [ListExclusionsResponseTypeDef](./type_defs.md#listexclusionsresponsetypedef)
- [ListFindingsResponseTypeDef](./type_defs.md#listfindingsresponsetypedef)
- [ListRulesPackagesResponseTypeDef](./type_defs.md#listrulespackagesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PreviewAgentsResponseTypeDef](./type_defs.md#previewagentsresponsetypedef)
- [PrivateIpTypeDef](./type_defs.md#privateiptypedef)
- [RemoveAttributesFromFindingsResponseTypeDef](./type_defs.md#removeattributesfromfindingsresponsetypedef)
- [ResourceGroupTagTypeDef](./type_defs.md#resourcegrouptagtypedef)
- [ResourceGroupTypeDef](./type_defs.md#resourcegrouptypedef)
- [RulesPackageTypeDef](./type_defs.md#rulespackagetypedef)
- [ScopeTypeDef](./type_defs.md#scopetypedef)
- [SecurityGroupTypeDef](./type_defs.md#securitygrouptypedef)
- [StartAssessmentRunResponseTypeDef](./type_defs.md#startassessmentrunresponsetypedef)
- [SubscriptionTypeDef](./type_defs.md#subscriptiontypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TelemetryMetadataTypeDef](./type_defs.md#telemetrymetadatatypedef)
- [TimestampRangeTypeDef](./type_defs.md#timestamprangetypedef)
