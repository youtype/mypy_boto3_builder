# Structures for boto3 AuditManager module

> [Index](../index.md) > [AuditManager](./index.md) > Structures

Auto-generated documentation for [AuditManager](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager)
type annotations stubs module [mypy_boto3_auditmanager](https://pypi.org/project/mypy-boto3-auditmanager/).

- [Structures for boto3 AuditManager module](#structures-for-boto3-auditmanager-module)
  - [AWSAccountTypeDef](#awsaccounttypedef)
  - [AWSServiceTypeDef](#awsservicetypedef)
  - [AssessmentControlSetTypeDef](#assessmentcontrolsettypedef)
  - [AssessmentControlTypeDef](#assessmentcontroltypedef)
  - [AssessmentEvidenceFolderTypeDef](#assessmentevidencefoldertypedef)
  - [AssessmentFrameworkMetadataTypeDef](#assessmentframeworkmetadatatypedef)
  - [AssessmentFrameworkTypeDef](#assessmentframeworktypedef)
  - [AssessmentMetadataItemTypeDef](#assessmentmetadataitemtypedef)
  - [AssessmentMetadataTypeDef](#assessmentmetadatatypedef)
  - [AssessmentReportEvidenceErrorTypeDef](#assessmentreportevidenceerrortypedef)
  - [AssessmentReportMetadataTypeDef](#assessmentreportmetadatatypedef)
  - [AssessmentReportTypeDef](#assessmentreporttypedef)
  - [AssessmentReportsDestinationTypeDef](#assessmentreportsdestinationtypedef)
  - [AssessmentTypeDef](#assessmenttypedef)
  - [BatchCreateDelegationByAssessmentErrorTypeDef](#batchcreatedelegationbyassessmenterrortypedef)
  - [BatchDeleteDelegationByAssessmentErrorTypeDef](#batchdeletedelegationbyassessmenterrortypedef)
  - [BatchImportEvidenceToAssessmentControlErrorTypeDef](#batchimportevidencetoassessmentcontrolerrortypedef)
  - [ChangeLogTypeDef](#changelogtypedef)
  - [ControlCommentTypeDef](#controlcommenttypedef)
  - [ControlMappingSourceTypeDef](#controlmappingsourcetypedef)
  - [ControlMetadataTypeDef](#controlmetadatatypedef)
  - [ControlSetTypeDef](#controlsettypedef)
  - [ControlTypeDef](#controltypedef)
  - [CreateAssessmentFrameworkControlTypeDef](#createassessmentframeworkcontroltypedef)
  - [CreateDelegationRequestTypeDef](#createdelegationrequesttypedef)
  - [DelegationMetadataTypeDef](#delegationmetadatatypedef)
  - [DelegationTypeDef](#delegationtypedef)
  - [EvidenceTypeDef](#evidencetypedef)
  - [FrameworkMetadataTypeDef](#frameworkmetadatatypedef)
  - [FrameworkTypeDef](#frameworktypedef)
  - [ManualEvidenceTypeDef](#manualevidencetypedef)
  - [NotificationTypeDef](#notificationtypedef)
  - [ResourceTypeDef](#resourcetypedef)
  - [RoleTypeDef](#roletypedef)
  - [ScopeTypeDef](#scopetypedef)
  - [ServiceMetadataTypeDef](#servicemetadatatypedef)
  - [SettingsTypeDef](#settingstypedef)
  - [SourceKeywordTypeDef](#sourcekeywordtypedef)
  - [URLTypeDef](#urltypedef)
  - [BatchAssociateAssessmentReportEvidenceResponseTypeDef](#batchassociateassessmentreportevidenceresponsetypedef)
  - [BatchCreateDelegationByAssessmentResponseTypeDef](#batchcreatedelegationbyassessmentresponsetypedef)
  - [BatchDeleteDelegationByAssessmentResponseTypeDef](#batchdeletedelegationbyassessmentresponsetypedef)
  - [BatchDisassociateAssessmentReportEvidenceResponseTypeDef](#batchdisassociateassessmentreportevidenceresponsetypedef)
  - [BatchImportEvidenceToAssessmentControlResponseTypeDef](#batchimportevidencetoassessmentcontrolresponsetypedef)
  - [CreateAssessmentFrameworkControlSetTypeDef](#createassessmentframeworkcontrolsettypedef)
  - [CreateAssessmentFrameworkResponseTypeDef](#createassessmentframeworkresponsetypedef)
  - [CreateAssessmentReportResponseTypeDef](#createassessmentreportresponsetypedef)
  - [CreateAssessmentResponseTypeDef](#createassessmentresponsetypedef)
  - [CreateControlMappingSourceTypeDef](#createcontrolmappingsourcetypedef)
  - [CreateControlResponseTypeDef](#createcontrolresponsetypedef)
  - [DeregisterAccountResponseTypeDef](#deregisteraccountresponsetypedef)
  - [GetAccountStatusResponseTypeDef](#getaccountstatusresponsetypedef)
  - [GetAssessmentFrameworkResponseTypeDef](#getassessmentframeworkresponsetypedef)
  - [GetAssessmentReportUrlResponseTypeDef](#getassessmentreporturlresponsetypedef)
  - [GetAssessmentResponseTypeDef](#getassessmentresponsetypedef)
  - [GetChangeLogsResponseTypeDef](#getchangelogsresponsetypedef)
  - [GetControlResponseTypeDef](#getcontrolresponsetypedef)
  - [GetDelegationsResponseTypeDef](#getdelegationsresponsetypedef)
  - [GetEvidenceByEvidenceFolderResponseTypeDef](#getevidencebyevidencefolderresponsetypedef)
  - [GetEvidenceFolderResponseTypeDef](#getevidencefolderresponsetypedef)
  - [GetEvidenceFoldersByAssessmentControlResponseTypeDef](#getevidencefoldersbyassessmentcontrolresponsetypedef)
  - [GetEvidenceFoldersByAssessmentResponseTypeDef](#getevidencefoldersbyassessmentresponsetypedef)
  - [GetEvidenceResponseTypeDef](#getevidenceresponsetypedef)
  - [GetOrganizationAdminAccountResponseTypeDef](#getorganizationadminaccountresponsetypedef)
  - [GetServicesInScopeResponseTypeDef](#getservicesinscoperesponsetypedef)
  - [GetSettingsResponseTypeDef](#getsettingsresponsetypedef)
  - [ListAssessmentFrameworksResponseTypeDef](#listassessmentframeworksresponsetypedef)
  - [ListAssessmentReportsResponseTypeDef](#listassessmentreportsresponsetypedef)
  - [ListAssessmentsResponseTypeDef](#listassessmentsresponsetypedef)
  - [ListControlsResponseTypeDef](#listcontrolsresponsetypedef)
  - [ListKeywordsForDataSourceResponseTypeDef](#listkeywordsfordatasourceresponsetypedef)
  - [ListNotificationsResponseTypeDef](#listnotificationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [RegisterAccountResponseTypeDef](#registeraccountresponsetypedef)
  - [RegisterOrganizationAdminAccountResponseTypeDef](#registerorganizationadminaccountresponsetypedef)
  - [UpdateAssessmentControlResponseTypeDef](#updateassessmentcontrolresponsetypedef)
  - [UpdateAssessmentControlSetStatusResponseTypeDef](#updateassessmentcontrolsetstatusresponsetypedef)
  - [UpdateAssessmentFrameworkControlSetTypeDef](#updateassessmentframeworkcontrolsettypedef)
  - [UpdateAssessmentFrameworkResponseTypeDef](#updateassessmentframeworkresponsetypedef)
  - [UpdateAssessmentResponseTypeDef](#updateassessmentresponsetypedef)
  - [UpdateAssessmentStatusResponseTypeDef](#updateassessmentstatusresponsetypedef)
  - [UpdateControlResponseTypeDef](#updatecontrolresponsetypedef)
  - [UpdateSettingsResponseTypeDef](#updatesettingsresponsetypedef)
  - [ValidateAssessmentReportIntegrityResponseTypeDef](#validateassessmentreportintegrityresponsetypedef)

## AWSAccountTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef
```




Optional fields:
- `id`: `str`
- `emailAddress`: `str`
- `name`: `str`


## AWSServiceTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AWSServiceTypeDef
```




Optional fields:
- `serviceName`: `str`


## AssessmentControlSetTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentControlSetTypeDef
```




Optional fields:
- `id`: `str`
- `description`: `str`
- `status`: `ControlSetStatus`
- `roles`: `List["RoleTypeDef"]`
- `controls`: `List["AssessmentControlTypeDef"]`
- `delegations`: `List["DelegationTypeDef"]`
- `systemEvidenceCount`: `int`
- `manualEvidenceCount`: `int`


## AssessmentControlTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentControlTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `description`: `str`
- `status`: `ControlStatus`
- `response`: `ControlResponse`
- `comments`: `List["ControlCommentTypeDef"]`
- `evidenceSources`: `List[str]`
- `evidenceCount`: `int`
- `assessmentReportEvidenceCount`: `int`


## AssessmentEvidenceFolderTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentEvidenceFolderTypeDef
```




Optional fields:
- `name`: `str`
- `date`: `datetime`
- `assessmentId`: `str`
- `controlSetId`: `str`
- `controlId`: `str`
- `id`: `str`
- `dataSource`: `str`
- `author`: `str`
- `totalEvidence`: `int`
- `assessmentReportSelectionCount`: `int`
- `controlName`: `str`
- `evidenceResourcesIncludedCount`: `int`
- `evidenceByTypeConfigurationDataCount`: `int`
- `evidenceByTypeManualCount`: `int`
- `evidenceByTypeComplianceCheckCount`: `int`
- `evidenceByTypeComplianceCheckIssuesCount`: `int`
- `evidenceByTypeUserActivityCount`: `int`
- `evidenceAwsServiceSourceCount`: `int`


## AssessmentFrameworkMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentFrameworkMetadataTypeDef
```




Optional fields:
- `arn`: `str`
- `id`: `str`
- `type`: `FrameworkType`
- `name`: `str`
- `description`: `str`
- `logo`: `str`
- `complianceType`: `str`
- `controlsCount`: `int`
- `controlSetsCount`: `int`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`


## AssessmentFrameworkTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentFrameworkTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `metadata`: `"FrameworkMetadataTypeDef"`
- `controlSets`: `List["AssessmentControlSetTypeDef"]`


## AssessmentMetadataItemTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentMetadataItemTypeDef
```




Optional fields:
- `name`: `str`
- `id`: `str`
- `complianceType`: `str`
- `status`: `AssessmentStatus`
- `roles`: `List["RoleTypeDef"]`
- `delegations`: `List["DelegationTypeDef"]`
- `creationTime`: `datetime`
- `lastUpdated`: `datetime`


## AssessmentMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `id`: `str`
- `description`: `str`
- `complianceType`: `str`
- `status`: `AssessmentStatus`
- `assessmentReportsDestination`: `"AssessmentReportsDestinationTypeDef"`
- `scope`: `"ScopeTypeDef"`
- `roles`: `List["RoleTypeDef"]`
- `delegations`: `List["DelegationTypeDef"]`
- `creationTime`: `datetime`
- `lastUpdated`: `datetime`


## AssessmentReportEvidenceErrorTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentReportEvidenceErrorTypeDef
```




Optional fields:
- `evidenceId`: `str`
- `errorCode`: `str`
- `errorMessage`: `str`


## AssessmentReportMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentReportMetadataTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `description`: `str`
- `assessmentId`: `str`
- `assessmentName`: `str`
- `author`: `str`
- `status`: `AssessmentReportStatus`
- `creationTime`: `datetime`


## AssessmentReportTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentReportTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `description`: `str`
- `awsAccountId`: `str`
- `assessmentId`: `str`
- `assessmentName`: `str`
- `author`: `str`
- `status`: `AssessmentReportStatus`
- `creationTime`: `datetime`


## AssessmentReportsDestinationTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentReportsDestinationTypeDef
```




Optional fields:
- `destinationType`: `AssessmentReportDestinationType`
- `destination`: `str`


## AssessmentTypeDef

```python
from mypy_boto3_auditmanager.type_defs import AssessmentTypeDef
```




Optional fields:
- `arn`: `str`
- `awsAccount`: `"AWSAccountTypeDef"`
- `metadata`: `"AssessmentMetadataTypeDef"`
- `framework`: `"AssessmentFrameworkTypeDef"`
- `tags`: `Dict[str, str]`


## BatchCreateDelegationByAssessmentErrorTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchCreateDelegationByAssessmentErrorTypeDef
```




Optional fields:
- `createDelegationRequest`: `"CreateDelegationRequestTypeDef"`
- `errorCode`: `str`
- `errorMessage`: `str`


## BatchDeleteDelegationByAssessmentErrorTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchDeleteDelegationByAssessmentErrorTypeDef
```




Optional fields:
- `delegationId`: `str`
- `errorCode`: `str`
- `errorMessage`: `str`


## BatchImportEvidenceToAssessmentControlErrorTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchImportEvidenceToAssessmentControlErrorTypeDef
```




Optional fields:
- `manualEvidence`: `"ManualEvidenceTypeDef"`
- `errorCode`: `str`
- `errorMessage`: `str`


## ChangeLogTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ChangeLogTypeDef
```




Optional fields:
- `objectType`: `ObjectTypeEnum`
- `objectName`: `str`
- `action`: `ActionEnum`
- `createdAt`: `datetime`
- `createdBy`: `str`


## ControlCommentTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ControlCommentTypeDef
```




Optional fields:
- `authorName`: `str`
- `commentBody`: `str`
- `postedDate`: `datetime`


## ControlMappingSourceTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ControlMappingSourceTypeDef
```




Optional fields:
- `sourceId`: `str`
- `sourceName`: `str`
- `sourceDescription`: `str`
- `sourceSetUpOption`: `SourceSetUpOption`
- `sourceType`: `SourceType`
- `sourceKeyword`: `"SourceKeywordTypeDef"`
- `sourceFrequency`: `SourceFrequency`
- `troubleshootingText`: `str`


## ControlMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ControlMetadataTypeDef
```




Optional fields:
- `arn`: `str`
- `id`: `str`
- `name`: `str`
- `controlSources`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`


## ControlSetTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ControlSetTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `controls`: `List["ControlTypeDef"]`


## ControlTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ControlTypeDef
```




Optional fields:
- `arn`: `str`
- `id`: `str`
- `type`: `ControlType`
- `name`: `str`
- `description`: `str`
- `testingInformation`: `str`
- `actionPlanTitle`: `str`
- `actionPlanInstructions`: `str`
- `controlSources`: `str`
- `controlMappingSources`: `List["ControlMappingSourceTypeDef"]`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `createdBy`: `str`
- `lastUpdatedBy`: `str`
- `tags`: `Dict[str, str]`


## CreateAssessmentFrameworkControlTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateAssessmentFrameworkControlTypeDef
```




Optional fields:
- `id`: `str`


## CreateDelegationRequestTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateDelegationRequestTypeDef
```




Optional fields:
- `comment`: `str`
- `controlSetId`: `str`
- `roleArn`: `str`
- `roleType`: `RoleType`


## DelegationMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import DelegationMetadataTypeDef
```




Optional fields:
- `id`: `str`
- `assessmentName`: `str`
- `assessmentId`: `str`
- `status`: `DelegationStatus`
- `roleArn`: `str`
- `creationTime`: `datetime`
- `controlSetName`: `str`


## DelegationTypeDef

```python
from mypy_boto3_auditmanager.type_defs import DelegationTypeDef
```




Optional fields:
- `id`: `str`
- `assessmentName`: `str`
- `assessmentId`: `str`
- `status`: `DelegationStatus`
- `roleArn`: `str`
- `roleType`: `RoleType`
- `creationTime`: `datetime`
- `lastUpdated`: `datetime`
- `controlSetId`: `str`
- `comment`: `str`
- `createdBy`: `str`


## EvidenceTypeDef

```python
from mypy_boto3_auditmanager.type_defs import EvidenceTypeDef
```




Optional fields:
- `dataSource`: `str`
- `evidenceAwsAccountId`: `str`
- `time`: `datetime`
- `eventSource`: `str`
- `eventName`: `str`
- `evidenceByType`: `str`
- `resourcesIncluded`: `List["ResourceTypeDef"]`
- `attributes`: `Dict[str, str]`
- `iamId`: `str`
- `complianceCheck`: `str`
- `awsOrganization`: `str`
- `awsAccountId`: `str`
- `evidenceFolderId`: `str`
- `id`: `str`
- `assessmentReportSelection`: `str`


## FrameworkMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import FrameworkMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `logo`: `str`
- `complianceType`: `str`


## FrameworkTypeDef

```python
from mypy_boto3_auditmanager.type_defs import FrameworkTypeDef
```




Optional fields:
- `arn`: `str`
- `id`: `str`
- `name`: `str`
- `type`: `FrameworkType`
- `complianceType`: `str`
- `description`: `str`
- `logo`: `str`
- `controlSources`: `str`
- `controlSets`: `List["ControlSetTypeDef"]`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `createdBy`: `str`
- `lastUpdatedBy`: `str`
- `tags`: `Dict[str, str]`


## ManualEvidenceTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ManualEvidenceTypeDef
```




Optional fields:
- `s3ResourcePath`: `str`


## NotificationTypeDef

```python
from mypy_boto3_auditmanager.type_defs import NotificationTypeDef
```




Optional fields:
- `id`: `str`
- `assessmentId`: `str`
- `assessmentName`: `str`
- `controlSetId`: `str`
- `controlSetName`: `str`
- `description`: `str`
- `eventTime`: `datetime`
- `source`: `str`


## ResourceTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ResourceTypeDef
```




Optional fields:
- `arn`: `str`
- `value`: `str`


## RoleTypeDef

```python
from mypy_boto3_auditmanager.type_defs import RoleTypeDef
```




Optional fields:
- `roleType`: `RoleType`
- `roleArn`: `str`


## ScopeTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ScopeTypeDef
```




Optional fields:
- `awsAccounts`: `List["AWSAccountTypeDef"]`
- `awsServices`: `List["AWSServiceTypeDef"]`


## ServiceMetadataTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ServiceMetadataTypeDef
```




Optional fields:
- `name`: `str`
- `displayName`: `str`
- `description`: `str`
- `category`: `str`


## SettingsTypeDef

```python
from mypy_boto3_auditmanager.type_defs import SettingsTypeDef
```




Optional fields:
- `isAwsOrgEnabled`: `bool`
- `snsTopic`: `str`
- `defaultAssessmentReportsDestination`: `"AssessmentReportsDestinationTypeDef"`
- `defaultProcessOwners`: `List["RoleTypeDef"]`
- `kmsKey`: `str`


## SourceKeywordTypeDef

```python
from mypy_boto3_auditmanager.type_defs import SourceKeywordTypeDef
```




Optional fields:
- `keywordInputType`: `KeywordInputType`
- `keywordValue`: `str`


## URLTypeDef

```python
from mypy_boto3_auditmanager.type_defs import URLTypeDef
```




Optional fields:
- `hyperlinkName`: `str`
- `link`: `str`


## BatchAssociateAssessmentReportEvidenceResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchAssociateAssessmentReportEvidenceResponseTypeDef
```




Optional fields:
- `evidenceIds`: `List[str]`
- `errors`: `List["AssessmentReportEvidenceErrorTypeDef"]`


## BatchCreateDelegationByAssessmentResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchCreateDelegationByAssessmentResponseTypeDef
```




Optional fields:
- `delegations`: `List["DelegationTypeDef"]`
- `errors`: `List["BatchCreateDelegationByAssessmentErrorTypeDef"]`


## BatchDeleteDelegationByAssessmentResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchDeleteDelegationByAssessmentResponseTypeDef
```




Optional fields:
- `errors`: `List["BatchDeleteDelegationByAssessmentErrorTypeDef"]`


## BatchDisassociateAssessmentReportEvidenceResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchDisassociateAssessmentReportEvidenceResponseTypeDef
```




Optional fields:
- `evidenceIds`: `List[str]`
- `errors`: `List["AssessmentReportEvidenceErrorTypeDef"]`


## BatchImportEvidenceToAssessmentControlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import BatchImportEvidenceToAssessmentControlResponseTypeDef
```




Optional fields:
- `errors`: `List["BatchImportEvidenceToAssessmentControlErrorTypeDef"]`


## CreateAssessmentFrameworkControlSetTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateAssessmentFrameworkControlSetTypeDef
```




Optional fields:
- `name`: `str`
- `controls`: `List["CreateAssessmentFrameworkControlTypeDef"]`


## CreateAssessmentFrameworkResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateAssessmentFrameworkResponseTypeDef
```




Optional fields:
- `framework`: `"FrameworkTypeDef"`


## CreateAssessmentReportResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateAssessmentReportResponseTypeDef
```




Optional fields:
- `assessmentReport`: `"AssessmentReportTypeDef"`


## CreateAssessmentResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateAssessmentResponseTypeDef
```




Optional fields:
- `assessment`: `"AssessmentTypeDef"`


## CreateControlMappingSourceTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateControlMappingSourceTypeDef
```




Optional fields:
- `sourceName`: `str`
- `sourceDescription`: `str`
- `sourceSetUpOption`: `SourceSetUpOption`
- `sourceType`: `SourceType`
- `sourceKeyword`: `"SourceKeywordTypeDef"`
- `sourceFrequency`: `SourceFrequency`
- `troubleshootingText`: `str`


## CreateControlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import CreateControlResponseTypeDef
```




Optional fields:
- `control`: `"ControlTypeDef"`


## DeregisterAccountResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import DeregisterAccountResponseTypeDef
```




Optional fields:
- `status`: `AccountStatus`


## GetAccountStatusResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetAccountStatusResponseTypeDef
```




Optional fields:
- `status`: `AccountStatus`


## GetAssessmentFrameworkResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetAssessmentFrameworkResponseTypeDef
```




Optional fields:
- `framework`: `"FrameworkTypeDef"`


## GetAssessmentReportUrlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetAssessmentReportUrlResponseTypeDef
```




Optional fields:
- `preSignedUrl`: `"URLTypeDef"`


## GetAssessmentResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetAssessmentResponseTypeDef
```




Optional fields:
- `assessment`: `"AssessmentTypeDef"`
- `userRole`: `"RoleTypeDef"`


## GetChangeLogsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetChangeLogsResponseTypeDef
```




Optional fields:
- `changeLogs`: `List["ChangeLogTypeDef"]`
- `nextToken`: `str`


## GetControlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetControlResponseTypeDef
```




Optional fields:
- `control`: `"ControlTypeDef"`


## GetDelegationsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetDelegationsResponseTypeDef
```




Optional fields:
- `delegations`: `List["DelegationMetadataTypeDef"]`
- `nextToken`: `str`


## GetEvidenceByEvidenceFolderResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetEvidenceByEvidenceFolderResponseTypeDef
```




Optional fields:
- `evidence`: `List["EvidenceTypeDef"]`
- `nextToken`: `str`


## GetEvidenceFolderResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetEvidenceFolderResponseTypeDef
```




Optional fields:
- `evidenceFolder`: `"AssessmentEvidenceFolderTypeDef"`


## GetEvidenceFoldersByAssessmentControlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetEvidenceFoldersByAssessmentControlResponseTypeDef
```




Optional fields:
- `evidenceFolders`: `List["AssessmentEvidenceFolderTypeDef"]`
- `nextToken`: `str`


## GetEvidenceFoldersByAssessmentResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetEvidenceFoldersByAssessmentResponseTypeDef
```




Optional fields:
- `evidenceFolders`: `List["AssessmentEvidenceFolderTypeDef"]`
- `nextToken`: `str`


## GetEvidenceResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetEvidenceResponseTypeDef
```




Optional fields:
- `evidence`: `"EvidenceTypeDef"`


## GetOrganizationAdminAccountResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetOrganizationAdminAccountResponseTypeDef
```




Optional fields:
- `adminAccountId`: `str`
- `organizationId`: `str`


## GetServicesInScopeResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetServicesInScopeResponseTypeDef
```




Optional fields:
- `serviceMetadata`: `List["ServiceMetadataTypeDef"]`


## GetSettingsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import GetSettingsResponseTypeDef
```




Optional fields:
- `settings`: `"SettingsTypeDef"`


## ListAssessmentFrameworksResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListAssessmentFrameworksResponseTypeDef
```




Optional fields:
- `frameworkMetadataList`: `List["AssessmentFrameworkMetadataTypeDef"]`
- `nextToken`: `str`


## ListAssessmentReportsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListAssessmentReportsResponseTypeDef
```




Optional fields:
- `assessmentReports`: `List["AssessmentReportMetadataTypeDef"]`
- `nextToken`: `str`


## ListAssessmentsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListAssessmentsResponseTypeDef
```




Optional fields:
- `assessmentMetadata`: `List["AssessmentMetadataItemTypeDef"]`
- `nextToken`: `str`


## ListControlsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListControlsResponseTypeDef
```




Optional fields:
- `controlMetadataList`: `List["ControlMetadataTypeDef"]`
- `nextToken`: `str`


## ListKeywordsForDataSourceResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListKeywordsForDataSourceResponseTypeDef
```




Optional fields:
- `keywords`: `List[str]`
- `nextToken`: `str`


## ListNotificationsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListNotificationsResponseTypeDef
```




Optional fields:
- `notifications`: `List["NotificationTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## RegisterAccountResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import RegisterAccountResponseTypeDef
```




Optional fields:
- `status`: `AccountStatus`


## RegisterOrganizationAdminAccountResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import RegisterOrganizationAdminAccountResponseTypeDef
```




Optional fields:
- `adminAccountId`: `str`
- `organizationId`: `str`


## UpdateAssessmentControlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateAssessmentControlResponseTypeDef
```




Optional fields:
- `control`: `"AssessmentControlTypeDef"`


## UpdateAssessmentControlSetStatusResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateAssessmentControlSetStatusResponseTypeDef
```




Optional fields:
- `controlSet`: `"AssessmentControlSetTypeDef"`


## UpdateAssessmentFrameworkControlSetTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateAssessmentFrameworkControlSetTypeDef
```




Optional fields:
- `id`: `str`
- `name`: `str`
- `controls`: `List["CreateAssessmentFrameworkControlTypeDef"]`


## UpdateAssessmentFrameworkResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateAssessmentFrameworkResponseTypeDef
```




Optional fields:
- `framework`: `"FrameworkTypeDef"`


## UpdateAssessmentResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateAssessmentResponseTypeDef
```




Optional fields:
- `assessment`: `"AssessmentTypeDef"`


## UpdateAssessmentStatusResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateAssessmentStatusResponseTypeDef
```




Optional fields:
- `assessment`: `"AssessmentTypeDef"`


## UpdateControlResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateControlResponseTypeDef
```




Optional fields:
- `control`: `"ControlTypeDef"`


## UpdateSettingsResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import UpdateSettingsResponseTypeDef
```




Optional fields:
- `settings`: `"SettingsTypeDef"`


## ValidateAssessmentReportIntegrityResponseTypeDef

```python
from mypy_boto3_auditmanager.type_defs import ValidateAssessmentReportIntegrityResponseTypeDef
```




Optional fields:
- `signatureValid`: `bool`
- `signatureAlgorithm`: `str`
- `signatureDateTime`: `str`
- `signatureKeyId`: `str`
- `validationErrors`: `List[str]`

