# Type annotations for boto3 AuditManager module

> [Index](../index.md) > AuditManager

Auto-generated documentation for [AuditManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager)
type annotations stubs module [mypy_boto3_auditmanager](https://pypi.org/project/mypy-boto3-auditmanager/).

```bash
pip install mypy-boto3-auditmanager
```

- [Type annotations for boto3 AuditManager module](#type-annotations-for-boto3-auditmanager-module)
  - [AuditManagerClient](#auditmanagerclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## AuditManagerClient

Type annotations for  `boto3.client("auditmanager")` as [AuditManagerClient](./client.md)

Can be used directly:

```python
from mypy_boto3_auditmanager.client import AuditManagerClient
```


AuditManagerClient [exceptions](./client.md#exceptions)



### Methods
- [associate_assessment_report_evidence_folder](./client.md#associate-assessment-report-evidence-folder)
- [batch_associate_assessment_report_evidence](./client.md#batch-associate-assessment-report-evidence)
- [batch_create_delegation_by_assessment](./client.md#batch-create-delegation-by-assessment)
- [batch_delete_delegation_by_assessment](./client.md#batch-delete-delegation-by-assessment)
- [batch_disassociate_assessment_report_evidence](./client.md#batch-disassociate-assessment-report-evidence)
- [batch_import_evidence_to_assessment_control](./client.md#batch-import-evidence-to-assessment-control)
- [can_paginate](./client.md#can-paginate)
- [create_assessment](./client.md#create-assessment)
- [create_assessment_framework](./client.md#create-assessment-framework)
- [create_assessment_report](./client.md#create-assessment-report)
- [create_control](./client.md#create-control)
- [delete_assessment](./client.md#delete-assessment)
- [delete_assessment_framework](./client.md#delete-assessment-framework)
- [delete_assessment_report](./client.md#delete-assessment-report)
- [delete_control](./client.md#delete-control)
- [deregister_account](./client.md#deregister-account)
- [deregister_organization_admin_account](./client.md#deregister-organization-admin-account)
- [disassociate_assessment_report_evidence_folder](./client.md#disassociate-assessment-report-evidence-folder)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account_status](./client.md#get-account-status)
- [get_assessment](./client.md#get-assessment)
- [get_assessment_framework](./client.md#get-assessment-framework)
- [get_assessment_report_url](./client.md#get-assessment-report-url)
- [get_change_logs](./client.md#get-change-logs)
- [get_control](./client.md#get-control)
- [get_delegations](./client.md#get-delegations)
- [get_evidence](./client.md#get-evidence)
- [get_evidence_by_evidence_folder](./client.md#get-evidence-by-evidence-folder)
- [get_evidence_folder](./client.md#get-evidence-folder)
- [get_evidence_folders_by_assessment](./client.md#get-evidence-folders-by-assessment)
- [get_evidence_folders_by_assessment_control](./client.md#get-evidence-folders-by-assessment-control)
- [get_organization_admin_account](./client.md#get-organization-admin-account)
- [get_services_in_scope](./client.md#get-services-in-scope)
- [get_settings](./client.md#get-settings)
- [list_assessment_frameworks](./client.md#list-assessment-frameworks)
- [list_assessment_reports](./client.md#list-assessment-reports)
- [list_assessments](./client.md#list-assessments)
- [list_controls](./client.md#list-controls)
- [list_keywords_for_data_source](./client.md#list-keywords-for-data-source)
- [list_notifications](./client.md#list-notifications)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [register_account](./client.md#register-account)
- [register_organization_admin_account](./client.md#register-organization-admin-account)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_assessment](./client.md#update-assessment)
- [update_assessment_control](./client.md#update-assessment-control)
- [update_assessment_control_set_status](./client.md#update-assessment-control-set-status)
- [update_assessment_framework](./client.md#update-assessment-framework)
- [update_assessment_status](./client.md#update-assessment-status)
- [update_control](./client.md#update-control)
- [update_settings](./client.md#update-settings)
- [validate_assessment_report_integrity](./client.md#validate-assessment-report-integrity)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_auditmanager.literals import AccountStatus, ...
```

- [AccountStatus](./literals.md#accountstatus)
- [ActionEnum](./literals.md#actionenum)
- [AssessmentReportDestinationType](./literals.md#assessmentreportdestinationtype)
- [AssessmentReportStatus](./literals.md#assessmentreportstatus)
- [AssessmentStatus](./literals.md#assessmentstatus)
- [ControlResponse](./literals.md#controlresponse)
- [ControlSetStatus](./literals.md#controlsetstatus)
- [ControlStatus](./literals.md#controlstatus)
- [ControlType](./literals.md#controltype)
- [DelegationStatus](./literals.md#delegationstatus)
- [FrameworkType](./literals.md#frameworktype)
- [KeywordInputType](./literals.md#keywordinputtype)
- [ObjectTypeEnum](./literals.md#objecttypeenum)
- [RoleType](./literals.md#roletype)
- [SettingAttribute](./literals.md#settingattribute)
- [SourceFrequency](./literals.md#sourcefrequency)
- [SourceSetUpOption](./literals.md#sourcesetupoption)
- [SourceType](./literals.md#sourcetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef, ...
```

- [AWSAccountTypeDef](./type_defs.md#awsaccounttypedef)
- [AWSServiceTypeDef](./type_defs.md#awsservicetypedef)
- [AssessmentControlSetTypeDef](./type_defs.md#assessmentcontrolsettypedef)
- [AssessmentControlTypeDef](./type_defs.md#assessmentcontroltypedef)
- [AssessmentEvidenceFolderTypeDef](./type_defs.md#assessmentevidencefoldertypedef)
- [AssessmentFrameworkMetadataTypeDef](./type_defs.md#assessmentframeworkmetadatatypedef)
- [AssessmentFrameworkTypeDef](./type_defs.md#assessmentframeworktypedef)
- [AssessmentMetadataItemTypeDef](./type_defs.md#assessmentmetadataitemtypedef)
- [AssessmentMetadataTypeDef](./type_defs.md#assessmentmetadatatypedef)
- [AssessmentReportEvidenceErrorTypeDef](./type_defs.md#assessmentreportevidenceerrortypedef)
- [AssessmentReportMetadataTypeDef](./type_defs.md#assessmentreportmetadatatypedef)
- [AssessmentReportTypeDef](./type_defs.md#assessmentreporttypedef)
- [AssessmentReportsDestinationTypeDef](./type_defs.md#assessmentreportsdestinationtypedef)
- [AssessmentTypeDef](./type_defs.md#assessmenttypedef)
- [BatchCreateDelegationByAssessmentErrorTypeDef](./type_defs.md#batchcreatedelegationbyassessmenterrortypedef)
- [BatchDeleteDelegationByAssessmentErrorTypeDef](./type_defs.md#batchdeletedelegationbyassessmenterrortypedef)
- [BatchImportEvidenceToAssessmentControlErrorTypeDef](./type_defs.md#batchimportevidencetoassessmentcontrolerrortypedef)
- [ChangeLogTypeDef](./type_defs.md#changelogtypedef)
- [ControlCommentTypeDef](./type_defs.md#controlcommenttypedef)
- [ControlMappingSourceTypeDef](./type_defs.md#controlmappingsourcetypedef)
- [ControlMetadataTypeDef](./type_defs.md#controlmetadatatypedef)
- [ControlSetTypeDef](./type_defs.md#controlsettypedef)
- [ControlTypeDef](./type_defs.md#controltypedef)
- [CreateAssessmentFrameworkControlTypeDef](./type_defs.md#createassessmentframeworkcontroltypedef)
- [CreateDelegationRequestTypeDef](./type_defs.md#createdelegationrequesttypedef)
- [DelegationMetadataTypeDef](./type_defs.md#delegationmetadatatypedef)
- [DelegationTypeDef](./type_defs.md#delegationtypedef)
- [EvidenceTypeDef](./type_defs.md#evidencetypedef)
- [FrameworkMetadataTypeDef](./type_defs.md#frameworkmetadatatypedef)
- [FrameworkTypeDef](./type_defs.md#frameworktypedef)
- [ManualEvidenceTypeDef](./type_defs.md#manualevidencetypedef)
- [NotificationTypeDef](./type_defs.md#notificationtypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [RoleTypeDef](./type_defs.md#roletypedef)
- [ScopeTypeDef](./type_defs.md#scopetypedef)
- [ServiceMetadataTypeDef](./type_defs.md#servicemetadatatypedef)
- [SettingsTypeDef](./type_defs.md#settingstypedef)
- [SourceKeywordTypeDef](./type_defs.md#sourcekeywordtypedef)
- [URLTypeDef](./type_defs.md#urltypedef)
- [BatchAssociateAssessmentReportEvidenceResponseTypeDef](./type_defs.md#batchassociateassessmentreportevidenceresponsetypedef)
- [BatchCreateDelegationByAssessmentResponseTypeDef](./type_defs.md#batchcreatedelegationbyassessmentresponsetypedef)
- [BatchDeleteDelegationByAssessmentResponseTypeDef](./type_defs.md#batchdeletedelegationbyassessmentresponsetypedef)
- [BatchDisassociateAssessmentReportEvidenceResponseTypeDef](./type_defs.md#batchdisassociateassessmentreportevidenceresponsetypedef)
- [BatchImportEvidenceToAssessmentControlResponseTypeDef](./type_defs.md#batchimportevidencetoassessmentcontrolresponsetypedef)
- [CreateAssessmentFrameworkControlSetTypeDef](./type_defs.md#createassessmentframeworkcontrolsettypedef)
- [CreateAssessmentFrameworkResponseTypeDef](./type_defs.md#createassessmentframeworkresponsetypedef)
- [CreateAssessmentReportResponseTypeDef](./type_defs.md#createassessmentreportresponsetypedef)
- [CreateAssessmentResponseTypeDef](./type_defs.md#createassessmentresponsetypedef)
- [CreateControlMappingSourceTypeDef](./type_defs.md#createcontrolmappingsourcetypedef)
- [CreateControlResponseTypeDef](./type_defs.md#createcontrolresponsetypedef)
- [DeregisterAccountResponseTypeDef](./type_defs.md#deregisteraccountresponsetypedef)
- [GetAccountStatusResponseTypeDef](./type_defs.md#getaccountstatusresponsetypedef)
- [GetAssessmentFrameworkResponseTypeDef](./type_defs.md#getassessmentframeworkresponsetypedef)
- [GetAssessmentReportUrlResponseTypeDef](./type_defs.md#getassessmentreporturlresponsetypedef)
- [GetAssessmentResponseTypeDef](./type_defs.md#getassessmentresponsetypedef)
- [GetChangeLogsResponseTypeDef](./type_defs.md#getchangelogsresponsetypedef)
- [GetControlResponseTypeDef](./type_defs.md#getcontrolresponsetypedef)
- [GetDelegationsResponseTypeDef](./type_defs.md#getdelegationsresponsetypedef)
- [GetEvidenceByEvidenceFolderResponseTypeDef](./type_defs.md#getevidencebyevidencefolderresponsetypedef)
- [GetEvidenceFolderResponseTypeDef](./type_defs.md#getevidencefolderresponsetypedef)
- [GetEvidenceFoldersByAssessmentControlResponseTypeDef](./type_defs.md#getevidencefoldersbyassessmentcontrolresponsetypedef)
- [GetEvidenceFoldersByAssessmentResponseTypeDef](./type_defs.md#getevidencefoldersbyassessmentresponsetypedef)
- [GetEvidenceResponseTypeDef](./type_defs.md#getevidenceresponsetypedef)
- [GetOrganizationAdminAccountResponseTypeDef](./type_defs.md#getorganizationadminaccountresponsetypedef)
- [GetServicesInScopeResponseTypeDef](./type_defs.md#getservicesinscoperesponsetypedef)
- [GetSettingsResponseTypeDef](./type_defs.md#getsettingsresponsetypedef)
- [ListAssessmentFrameworksResponseTypeDef](./type_defs.md#listassessmentframeworksresponsetypedef)
- [ListAssessmentReportsResponseTypeDef](./type_defs.md#listassessmentreportsresponsetypedef)
- [ListAssessmentsResponseTypeDef](./type_defs.md#listassessmentsresponsetypedef)
- [ListControlsResponseTypeDef](./type_defs.md#listcontrolsresponsetypedef)
- [ListKeywordsForDataSourceResponseTypeDef](./type_defs.md#listkeywordsfordatasourceresponsetypedef)
- [ListNotificationsResponseTypeDef](./type_defs.md#listnotificationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [RegisterAccountResponseTypeDef](./type_defs.md#registeraccountresponsetypedef)
- [RegisterOrganizationAdminAccountResponseTypeDef](./type_defs.md#registerorganizationadminaccountresponsetypedef)
- [UpdateAssessmentControlResponseTypeDef](./type_defs.md#updateassessmentcontrolresponsetypedef)
- [UpdateAssessmentControlSetStatusResponseTypeDef](./type_defs.md#updateassessmentcontrolsetstatusresponsetypedef)
- [UpdateAssessmentFrameworkControlSetTypeDef](./type_defs.md#updateassessmentframeworkcontrolsettypedef)
- [UpdateAssessmentFrameworkResponseTypeDef](./type_defs.md#updateassessmentframeworkresponsetypedef)
- [UpdateAssessmentResponseTypeDef](./type_defs.md#updateassessmentresponsetypedef)
- [UpdateAssessmentStatusResponseTypeDef](./type_defs.md#updateassessmentstatusresponsetypedef)
- [UpdateControlResponseTypeDef](./type_defs.md#updatecontrolresponsetypedef)
- [UpdateSettingsResponseTypeDef](./type_defs.md#updatesettingsresponsetypedef)
- [ValidateAssessmentReportIntegrityResponseTypeDef](./type_defs.md#validateassessmentreportintegrityresponsetypedef)
