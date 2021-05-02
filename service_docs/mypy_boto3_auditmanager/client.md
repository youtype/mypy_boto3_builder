# AuditManagerClient for boto3 AuditManager module

> [Index](../index.md) > [AuditManager](./index.md) > AuditManagerClient

Auto-generated documentation for [AuditManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager)
type annotations stubs module [mypy_boto3_auditmanager](https://pypi.org/project/mypy-boto3-auditmanager/).

- [AuditManagerClient for boto3 AuditManager module](#auditmanagerclient-for-boto3-auditmanager-module)
  - [AuditManagerClient](#auditmanagerclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_assessment_report_evidence_folder](#associate_assessment_report_evidence_folder)
    - [batch_associate_assessment_report_evidence](#batch_associate_assessment_report_evidence)
    - [batch_create_delegation_by_assessment](#batch_create_delegation_by_assessment)
    - [batch_delete_delegation_by_assessment](#batch_delete_delegation_by_assessment)
    - [batch_disassociate_assessment_report_evidence](#batch_disassociate_assessment_report_evidence)
    - [batch_import_evidence_to_assessment_control](#batch_import_evidence_to_assessment_control)
    - [can_paginate](#can_paginate)
    - [create_assessment](#create_assessment)
    - [create_assessment_framework](#create_assessment_framework)
    - [create_assessment_report](#create_assessment_report)
    - [create_control](#create_control)
    - [delete_assessment](#delete_assessment)
    - [delete_assessment_framework](#delete_assessment_framework)
    - [delete_assessment_report](#delete_assessment_report)
    - [delete_control](#delete_control)
    - [deregister_account](#deregister_account)
    - [deregister_organization_admin_account](#deregister_organization_admin_account)
    - [disassociate_assessment_report_evidence_folder](#disassociate_assessment_report_evidence_folder)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_status](#get_account_status)
    - [get_assessment](#get_assessment)
    - [get_assessment_framework](#get_assessment_framework)
    - [get_assessment_report_url](#get_assessment_report_url)
    - [get_change_logs](#get_change_logs)
    - [get_control](#get_control)
    - [get_delegations](#get_delegations)
    - [get_evidence](#get_evidence)
    - [get_evidence_by_evidence_folder](#get_evidence_by_evidence_folder)
    - [get_evidence_folder](#get_evidence_folder)
    - [get_evidence_folders_by_assessment](#get_evidence_folders_by_assessment)
    - [get_evidence_folders_by_assessment_control](#get_evidence_folders_by_assessment_control)
    - [get_organization_admin_account](#get_organization_admin_account)
    - [get_services_in_scope](#get_services_in_scope)
    - [get_settings](#get_settings)
    - [list_assessment_frameworks](#list_assessment_frameworks)
    - [list_assessment_reports](#list_assessment_reports)
    - [list_assessments](#list_assessments)
    - [list_controls](#list_controls)
    - [list_keywords_for_data_source](#list_keywords_for_data_source)
    - [list_notifications](#list_notifications)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [register_account](#register_account)
    - [register_organization_admin_account](#register_organization_admin_account)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_assessment](#update_assessment)
    - [update_assessment_control](#update_assessment_control)
    - [update_assessment_control_set_status](#update_assessment_control_set_status)
    - [update_assessment_framework](#update_assessment_framework)
    - [update_assessment_status](#update_assessment_status)
    - [update_control](#update_control)
    - [update_settings](#update_settings)
    - [validate_assessment_report_integrity](#validate_assessment_report_integrity)

## AuditManagerClient

Type annotations for `boto3.client("auditmanager")`

Can be used directly:

```python
from mypy_boto3_auditmanager.client import AuditManagerClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_auditmanager.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### associate_assessment_report_evidence_folder

Type annotations for `boto3.client("auditmanager").associate_assessment_report_evidence_folder` method.

[Client.associate_assessment_report_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.associate_assessment_report_evidence_folder)

```python
def associate_assessment_report_evidence_folder(
    self,
    assessmentId: str,
    evidenceFolderId: str
) -> Dict[str, Any]:
    pass
```

### batch_associate_assessment_report_evidence

Type annotations for `boto3.client("auditmanager").batch_associate_assessment_report_evidence` method.

[Client.batch_associate_assessment_report_evidence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.batch_associate_assessment_report_evidence)

```python
def batch_associate_assessment_report_evidence(
    self,
    assessmentId: str,
    evidenceFolderId: str,
    evidenceIds: List[str]
) -> BatchAssociateAssessmentReportEvidenceResponseTypeDef:
    pass
```

### batch_create_delegation_by_assessment

Type annotations for `boto3.client("auditmanager").batch_create_delegation_by_assessment` method.

[Client.batch_create_delegation_by_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.batch_create_delegation_by_assessment)

```python
def batch_create_delegation_by_assessment(
    self,
    createDelegationRequests: List["CreateDelegationRequestTypeDef"],
    assessmentId: str
) -> BatchCreateDelegationByAssessmentResponseTypeDef:
    pass
```

### batch_delete_delegation_by_assessment

Type annotations for `boto3.client("auditmanager").batch_delete_delegation_by_assessment` method.

[Client.batch_delete_delegation_by_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.batch_delete_delegation_by_assessment)

```python
def batch_delete_delegation_by_assessment(
    self,
    delegationIds: List[str],
    assessmentId: str
) -> BatchDeleteDelegationByAssessmentResponseTypeDef:
    pass
```

### batch_disassociate_assessment_report_evidence

Type annotations for `boto3.client("auditmanager").batch_disassociate_assessment_report_evidence` method.

[Client.batch_disassociate_assessment_report_evidence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.batch_disassociate_assessment_report_evidence)

```python
def batch_disassociate_assessment_report_evidence(
    self,
    assessmentId: str,
    evidenceFolderId: str,
    evidenceIds: List[str]
) -> BatchDisassociateAssessmentReportEvidenceResponseTypeDef:
    pass
```

### batch_import_evidence_to_assessment_control

Type annotations for `boto3.client("auditmanager").batch_import_evidence_to_assessment_control` method.

[Client.batch_import_evidence_to_assessment_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.batch_import_evidence_to_assessment_control)

```python
def batch_import_evidence_to_assessment_control(
    self,
    assessmentId: str,
    controlSetId: str,
    controlId: str,
    manualEvidence: List["ManualEvidenceTypeDef"]
) -> BatchImportEvidenceToAssessmentControlResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("auditmanager").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_assessment

Type annotations for `boto3.client("auditmanager").create_assessment` method.

[Client.create_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.create_assessment)

```python
def create_assessment(
    self,
    name: str,
    assessmentReportsDestination: "AssessmentReportsDestinationTypeDef",
    scope: "ScopeTypeDef",
    roles: List["RoleTypeDef"],
    frameworkId: str,
    description: str = None,
    tags: Dict[str, str] = None
) -> CreateAssessmentResponseTypeDef:
    pass
```

### create_assessment_framework

Type annotations for `boto3.client("auditmanager").create_assessment_framework` method.

[Client.create_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.create_assessment_framework)

```python
def create_assessment_framework(
    self,
    name: str,
    controlSets: List[CreateAssessmentFrameworkControlSetTypeDef],
    description: str = None,
    complianceType: str = None,
    tags: Dict[str, str] = None
) -> CreateAssessmentFrameworkResponseTypeDef:
    pass
```

### create_assessment_report

Type annotations for `boto3.client("auditmanager").create_assessment_report` method.

[Client.create_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.create_assessment_report)

```python
def create_assessment_report(
    self,
    name: str,
    assessmentId: str,
    description: str = None
) -> CreateAssessmentReportResponseTypeDef:
    pass
```

### create_control

Type annotations for `boto3.client("auditmanager").create_control` method.

[Client.create_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.create_control)

```python
def create_control(
    self,
    name: str,
    controlMappingSources: List[CreateControlMappingSourceTypeDef],
    description: str = None,
    testingInformation: str = None,
    actionPlanTitle: str = None,
    actionPlanInstructions: str = None,
    tags: Dict[str, str] = None
) -> CreateControlResponseTypeDef:
    pass
```

### delete_assessment

Type annotations for `boto3.client("auditmanager").delete_assessment` method.

[Client.delete_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.delete_assessment)

```python
def delete_assessment(
    self,
    assessmentId: str
) -> Dict[str, Any]:
    pass
```

### delete_assessment_framework

Type annotations for `boto3.client("auditmanager").delete_assessment_framework` method.

[Client.delete_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_framework)

```python
def delete_assessment_framework(
    self,
    frameworkId: str
) -> Dict[str, Any]:
    pass
```

### delete_assessment_report

Type annotations for `boto3.client("auditmanager").delete_assessment_report` method.

[Client.delete_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_report)

```python
def delete_assessment_report(
    self,
    assessmentId: str,
    assessmentReportId: str
) -> Dict[str, Any]:
    pass
```

### delete_control

Type annotations for `boto3.client("auditmanager").delete_control` method.

[Client.delete_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.delete_control)

```python
def delete_control(
    self,
    controlId: str
) -> Dict[str, Any]:
    pass
```

### deregister_account

Type annotations for `boto3.client("auditmanager").deregister_account` method.

[Client.deregister_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.deregister_account)

```python
def deregister_account(
    self
) -> DeregisterAccountResponseTypeDef:
    pass
```

### deregister_organization_admin_account

Type annotations for `boto3.client("auditmanager").deregister_organization_admin_account` method.

[Client.deregister_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.deregister_organization_admin_account)

```python
def deregister_organization_admin_account(
    self,
    adminAccountId: str = None
) -> Dict[str, Any]:
    pass
```

### disassociate_assessment_report_evidence_folder

Type annotations for `boto3.client("auditmanager").disassociate_assessment_report_evidence_folder` method.

[Client.disassociate_assessment_report_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.disassociate_assessment_report_evidence_folder)

```python
def disassociate_assessment_report_evidence_folder(
    self,
    assessmentId: str,
    evidenceFolderId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("auditmanager").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.generate_presigned_url)

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

### get_account_status

Type annotations for `boto3.client("auditmanager").get_account_status` method.

[Client.get_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_account_status)

```python
def get_account_status(
    self
) -> GetAccountStatusResponseTypeDef:
    pass
```

### get_assessment

Type annotations for `boto3.client("auditmanager").get_assessment` method.

[Client.get_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_assessment)

```python
def get_assessment(
    self,
    assessmentId: str
) -> GetAssessmentResponseTypeDef:
    pass
```

### get_assessment_framework

Type annotations for `boto3.client("auditmanager").get_assessment_framework` method.

[Client.get_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_assessment_framework)

```python
def get_assessment_framework(
    self,
    frameworkId: str
) -> GetAssessmentFrameworkResponseTypeDef:
    pass
```

### get_assessment_report_url

Type annotations for `boto3.client("auditmanager").get_assessment_report_url` method.

[Client.get_assessment_report_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_assessment_report_url)

```python
def get_assessment_report_url(
    self,
    assessmentReportId: str,
    assessmentId: str
) -> GetAssessmentReportUrlResponseTypeDef:
    pass
```

### get_change_logs

Type annotations for `boto3.client("auditmanager").get_change_logs` method.

[Client.get_change_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_change_logs)

```python
def get_change_logs(
    self,
    assessmentId: str,
    controlSetId: str = None,
    controlId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetChangeLogsResponseTypeDef:
    pass
```

### get_control

Type annotations for `boto3.client("auditmanager").get_control` method.

[Client.get_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_control)

```python
def get_control(
    self,
    controlId: str
) -> GetControlResponseTypeDef:
    pass
```

### get_delegations

Type annotations for `boto3.client("auditmanager").get_delegations` method.

[Client.get_delegations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_delegations)

```python
def get_delegations(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> GetDelegationsResponseTypeDef:
    pass
```

### get_evidence

Type annotations for `boto3.client("auditmanager").get_evidence` method.

[Client.get_evidence documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_evidence)

```python
def get_evidence(
    self,
    assessmentId: str,
    controlSetId: str,
    evidenceFolderId: str,
    evidenceId: str
) -> GetEvidenceResponseTypeDef:
    pass
```

### get_evidence_by_evidence_folder

Type annotations for `boto3.client("auditmanager").get_evidence_by_evidence_folder` method.

[Client.get_evidence_by_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_evidence_by_evidence_folder)

```python
def get_evidence_by_evidence_folder(
    self,
    assessmentId: str,
    controlSetId: str,
    evidenceFolderId: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetEvidenceByEvidenceFolderResponseTypeDef:
    pass
```

### get_evidence_folder

Type annotations for `boto3.client("auditmanager").get_evidence_folder` method.

[Client.get_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folder)

```python
def get_evidence_folder(
    self,
    assessmentId: str,
    controlSetId: str,
    evidenceFolderId: str
) -> GetEvidenceFolderResponseTypeDef:
    pass
```

### get_evidence_folders_by_assessment

Type annotations for `boto3.client("auditmanager").get_evidence_folders_by_assessment` method.

[Client.get_evidence_folders_by_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment)

```python
def get_evidence_folders_by_assessment(
    self,
    assessmentId: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetEvidenceFoldersByAssessmentResponseTypeDef:
    pass
```

### get_evidence_folders_by_assessment_control

Type annotations for `boto3.client("auditmanager").get_evidence_folders_by_assessment_control` method.

[Client.get_evidence_folders_by_assessment_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment_control)

```python
def get_evidence_folders_by_assessment_control(
    self,
    assessmentId: str,
    controlSetId: str,
    controlId: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetEvidenceFoldersByAssessmentControlResponseTypeDef:
    pass
```

### get_organization_admin_account

Type annotations for `boto3.client("auditmanager").get_organization_admin_account` method.

[Client.get_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_organization_admin_account)

```python
def get_organization_admin_account(
    self
) -> GetOrganizationAdminAccountResponseTypeDef:
    pass
```

### get_services_in_scope

Type annotations for `boto3.client("auditmanager").get_services_in_scope` method.

[Client.get_services_in_scope documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_services_in_scope)

```python
def get_services_in_scope(
    self
) -> GetServicesInScopeResponseTypeDef:
    pass
```

### get_settings

Type annotations for `boto3.client("auditmanager").get_settings` method.

[Client.get_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.get_settings)

```python
def get_settings(
    self,
    attribute: SettingAttribute
) -> GetSettingsResponseTypeDef:
    pass
```

### list_assessment_frameworks

Type annotations for `boto3.client("auditmanager").list_assessment_frameworks` method.

[Client.list_assessment_frameworks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_assessment_frameworks)

```python
def list_assessment_frameworks(
    self,
    frameworkType: FrameworkType,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentFrameworksResponseTypeDef:
    pass
```

### list_assessment_reports

Type annotations for `boto3.client("auditmanager").list_assessment_reports` method.

[Client.list_assessment_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_assessment_reports)

```python
def list_assessment_reports(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentReportsResponseTypeDef:
    pass
```

### list_assessments

Type annotations for `boto3.client("auditmanager").list_assessments` method.

[Client.list_assessments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_assessments)

```python
def list_assessments(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListAssessmentsResponseTypeDef:
    pass
```

### list_controls

Type annotations for `boto3.client("auditmanager").list_controls` method.

[Client.list_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_controls)

```python
def list_controls(
    self,
    controlType: ControlType,
    nextToken: str = None,
    maxResults: int = None
) -> ListControlsResponseTypeDef:
    pass
```

### list_keywords_for_data_source

Type annotations for `boto3.client("auditmanager").list_keywords_for_data_source` method.

[Client.list_keywords_for_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_keywords_for_data_source)

```python
def list_keywords_for_data_source(
    self,
    source: SourceType,
    nextToken: str = None,
    maxResults: int = None
) -> ListKeywordsForDataSourceResponseTypeDef:
    pass
```

### list_notifications

Type annotations for `boto3.client("auditmanager").list_notifications` method.

[Client.list_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_notifications)

```python
def list_notifications(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListNotificationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("auditmanager").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### register_account

Type annotations for `boto3.client("auditmanager").register_account` method.

[Client.register_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.register_account)

```python
def register_account(
    self,
    kmsKey: str = None,
    delegatedAdminAccount: str = None
) -> RegisterAccountResponseTypeDef:
    pass
```

### register_organization_admin_account

Type annotations for `boto3.client("auditmanager").register_organization_admin_account` method.

[Client.register_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.register_organization_admin_account)

```python
def register_organization_admin_account(
    self,
    adminAccountId: str
) -> RegisterOrganizationAdminAccountResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("auditmanager").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("auditmanager").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_assessment

Type annotations for `boto3.client("auditmanager").update_assessment` method.

[Client.update_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_assessment)

```python
def update_assessment(
    self,
    assessmentId: str,
    scope: "ScopeTypeDef",
    assessmentName: str = None,
    assessmentDescription: str = None,
    assessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
    roles: List["RoleTypeDef"] = None
) -> UpdateAssessmentResponseTypeDef:
    pass
```

### update_assessment_control

Type annotations for `boto3.client("auditmanager").update_assessment_control` method.

[Client.update_assessment_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control)

```python
def update_assessment_control(
    self,
    assessmentId: str,
    controlSetId: str,
    controlId: str,
    controlStatus: ControlStatus = None,
    commentBody: str = None
) -> UpdateAssessmentControlResponseTypeDef:
    pass
```

### update_assessment_control_set_status

Type annotations for `boto3.client("auditmanager").update_assessment_control_set_status` method.

[Client.update_assessment_control_set_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control_set_status)

```python
def update_assessment_control_set_status(
    self,
    assessmentId: str,
    controlSetId: str,
    status: ControlSetStatus,
    comment: str
) -> UpdateAssessmentControlSetStatusResponseTypeDef:
    pass
```

### update_assessment_framework

Type annotations for `boto3.client("auditmanager").update_assessment_framework` method.

[Client.update_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_assessment_framework)

```python
def update_assessment_framework(
    self,
    frameworkId: str,
    name: str,
    controlSets: List[UpdateAssessmentFrameworkControlSetTypeDef],
    description: str = None,
    complianceType: str = None
) -> UpdateAssessmentFrameworkResponseTypeDef:
    pass
```

### update_assessment_status

Type annotations for `boto3.client("auditmanager").update_assessment_status` method.

[Client.update_assessment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_assessment_status)

```python
def update_assessment_status(
    self,
    assessmentId: str,
    status: AssessmentStatus
) -> UpdateAssessmentStatusResponseTypeDef:
    pass
```

### update_control

Type annotations for `boto3.client("auditmanager").update_control` method.

[Client.update_control documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_control)

```python
def update_control(
    self,
    controlId: str,
    name: str,
    controlMappingSources: List["ControlMappingSourceTypeDef"],
    description: str = None,
    testingInformation: str = None,
    actionPlanTitle: str = None,
    actionPlanInstructions: str = None
) -> UpdateControlResponseTypeDef:
    pass
```

### update_settings

Type annotations for `boto3.client("auditmanager").update_settings` method.

[Client.update_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.update_settings)

```python
def update_settings(
    self,
    snsTopic: str = None,
    defaultAssessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
    defaultProcessOwners: List["RoleTypeDef"] = None,
    kmsKey: str = None
) -> UpdateSettingsResponseTypeDef:
    pass
```

### validate_assessment_report_integrity

Type annotations for `boto3.client("auditmanager").validate_assessment_report_integrity` method.

[Client.validate_assessment_report_integrity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client.validate_assessment_report_integrity)

```python
def validate_assessment_report_integrity(
    self,
    s3RelativePath: str
) -> ValidateAssessmentReportIntegrityResponseTypeDef:
    pass
```



