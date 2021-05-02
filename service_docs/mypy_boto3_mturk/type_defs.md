# Structures for boto3 MTurk module

> [Index](../index.md) > [MTurk](./index.md) > Structures

Auto-generated documentation for [MTurk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk)
type annotations stubs module [mypy_boto3_mturk](https://pypi.org/project/mypy-boto3-mturk/).

- [Structures for boto3 MTurk module](#structures-for-boto3-mturk-module)
  - [AssignmentTypeDef](#assignmenttypedef)
  - [BonusPaymentTypeDef](#bonuspaymenttypedef)
  - [HITTypeDef](#hittypedef)
  - [LocaleTypeDef](#localetypedef)
  - [NotifyWorkersFailureStatusTypeDef](#notifyworkersfailurestatustypedef)
  - [ParameterMapEntryTypeDef](#parametermapentrytypedef)
  - [PolicyParameterTypeDef](#policyparametertypedef)
  - [QualificationRequestTypeDef](#qualificationrequesttypedef)
  - [QualificationRequirementTypeDef](#qualificationrequirementtypedef)
  - [QualificationTypeDef](#qualificationtypedef)
  - [QualificationTypeTypeDef](#qualificationtypetypedef)
  - [ReviewActionDetailTypeDef](#reviewactiondetailtypedef)
  - [ReviewPolicyTypeDef](#reviewpolicytypedef)
  - [ReviewReportTypeDef](#reviewreporttypedef)
  - [ReviewResultDetailTypeDef](#reviewresultdetailtypedef)
  - [WorkerBlockTypeDef](#workerblocktypedef)
  - [CreateHITResponseTypeDef](#createhitresponsetypedef)
  - [CreateHITTypeResponseTypeDef](#createhittyperesponsetypedef)
  - [CreateHITWithHITTypeResponseTypeDef](#createhitwithhittyperesponsetypedef)
  - [CreateQualificationTypeResponseTypeDef](#createqualificationtyperesponsetypedef)
  - [GetAccountBalanceResponseTypeDef](#getaccountbalanceresponsetypedef)
  - [GetAssignmentResponseTypeDef](#getassignmentresponsetypedef)
  - [GetFileUploadURLResponseTypeDef](#getfileuploadurlresponsetypedef)
  - [GetHITResponseTypeDef](#gethitresponsetypedef)
  - [GetQualificationScoreResponseTypeDef](#getqualificationscoreresponsetypedef)
  - [GetQualificationTypeResponseTypeDef](#getqualificationtyperesponsetypedef)
  - [HITLayoutParameterTypeDef](#hitlayoutparametertypedef)
  - [ListAssignmentsForHITResponseTypeDef](#listassignmentsforhitresponsetypedef)
  - [ListBonusPaymentsResponseTypeDef](#listbonuspaymentsresponsetypedef)
  - [ListHITsForQualificationTypeResponseTypeDef](#listhitsforqualificationtyperesponsetypedef)
  - [ListHITsResponseTypeDef](#listhitsresponsetypedef)
  - [ListQualificationRequestsResponseTypeDef](#listqualificationrequestsresponsetypedef)
  - [ListQualificationTypesResponseTypeDef](#listqualificationtypesresponsetypedef)
  - [ListReviewPolicyResultsForHITResponseTypeDef](#listreviewpolicyresultsforhitresponsetypedef)
  - [ListReviewableHITsResponseTypeDef](#listreviewablehitsresponsetypedef)
  - [ListWorkerBlocksResponseTypeDef](#listworkerblocksresponsetypedef)
  - [ListWorkersWithQualificationTypeResponseTypeDef](#listworkerswithqualificationtyperesponsetypedef)
  - [NotificationSpecificationTypeDef](#notificationspecificationtypedef)
  - [NotifyWorkersResponseTypeDef](#notifyworkersresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [UpdateQualificationTypeResponseTypeDef](#updatequalificationtyperesponsetypedef)

## AssignmentTypeDef

```python
from mypy_boto3_mturk.type_defs import AssignmentTypeDef
```




Optional fields:
- `AssignmentId`: `str`
- `WorkerId`: `str`
- `HITId`: `str`
- `AssignmentStatus`: `AssignmentStatus`
- `AutoApprovalTime`: `datetime`
- `AcceptTime`: `datetime`
- `SubmitTime`: `datetime`
- `ApprovalTime`: `datetime`
- `RejectionTime`: `datetime`
- `Deadline`: `datetime`
- `Answer`: `str`
- `RequesterFeedback`: `str`


## BonusPaymentTypeDef

```python
from mypy_boto3_mturk.type_defs import BonusPaymentTypeDef
```




Optional fields:
- `WorkerId`: `str`
- `BonusAmount`: `str`
- `AssignmentId`: `str`
- `Reason`: `str`
- `GrantTime`: `datetime`


## HITTypeDef

```python
from mypy_boto3_mturk.type_defs import HITTypeDef
```




Optional fields:
- `HITId`: `str`
- `HITTypeId`: `str`
- `HITGroupId`: `str`
- `HITLayoutId`: `str`
- `CreationTime`: `datetime`
- `Title`: `str`
- `Description`: `str`
- `Question`: `str`
- `Keywords`: `str`
- `HITStatus`: `HITStatus`
- `MaxAssignments`: `int`
- `Reward`: `str`
- `AutoApprovalDelayInSeconds`: `int`
- `Expiration`: `datetime`
- `AssignmentDurationInSeconds`: `int`
- `RequesterAnnotation`: `str`
- `QualificationRequirements`: `List["QualificationRequirementTypeDef"]`
- `HITReviewStatus`: `HITReviewStatus`
- `NumberOfAssignmentsPending`: `int`
- `NumberOfAssignmentsAvailable`: `int`
- `NumberOfAssignmentsCompleted`: `int`


## LocaleTypeDef

```python
from mypy_boto3_mturk.type_defs import LocaleTypeDef
```


Required fields:
- `Country`: `str`



Optional fields:
- `Subdivision`: `str`


## NotifyWorkersFailureStatusTypeDef

```python
from mypy_boto3_mturk.type_defs import NotifyWorkersFailureStatusTypeDef
```




Optional fields:
- `NotifyWorkersFailureCode`: `NotifyWorkersFailureCode`
- `NotifyWorkersFailureMessage`: `str`
- `WorkerId`: `str`


## ParameterMapEntryTypeDef

```python
from mypy_boto3_mturk.type_defs import ParameterMapEntryTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## PolicyParameterTypeDef

```python
from mypy_boto3_mturk.type_defs import PolicyParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`
- `MapEntries`: `List["ParameterMapEntryTypeDef"]`


## QualificationRequestTypeDef

```python
from mypy_boto3_mturk.type_defs import QualificationRequestTypeDef
```




Optional fields:
- `QualificationRequestId`: `str`
- `QualificationTypeId`: `str`
- `WorkerId`: `str`
- `Test`: `str`
- `Answer`: `str`
- `SubmitTime`: `datetime`


## QualificationRequirementTypeDef

```python
from mypy_boto3_mturk.type_defs import QualificationRequirementTypeDef
```


Required fields:
- `QualificationTypeId`: `str`
- `Comparator`: `Comparator`



Optional fields:
- `IntegerValues`: `List[int]`
- `LocaleValues`: `List["LocaleTypeDef"]`
- `RequiredToPreview`: `bool`
- `ActionsGuarded`: `HITAccessActions`


## QualificationTypeDef

```python
from mypy_boto3_mturk.type_defs import QualificationTypeDef
```




Optional fields:
- `QualificationTypeId`: `str`
- `WorkerId`: `str`
- `GrantTime`: `datetime`
- `IntegerValue`: `int`
- `LocaleValue`: `"LocaleTypeDef"`
- `Status`: `QualificationStatus`


## QualificationTypeTypeDef

```python
from mypy_boto3_mturk.type_defs import QualificationTypeTypeDef
```




Optional fields:
- `QualificationTypeId`: `str`
- `CreationTime`: `datetime`
- `Name`: `str`
- `Description`: `str`
- `Keywords`: `str`
- `QualificationTypeStatus`: `QualificationTypeStatus`
- `Test`: `str`
- `TestDurationInSeconds`: `int`
- `AnswerKey`: `str`
- `RetryDelayInSeconds`: `int`
- `IsRequestable`: `bool`
- `AutoGranted`: `bool`
- `AutoGrantedValue`: `int`


## ReviewActionDetailTypeDef

```python
from mypy_boto3_mturk.type_defs import ReviewActionDetailTypeDef
```




Optional fields:
- `ActionId`: `str`
- `ActionName`: `str`
- `TargetId`: `str`
- `TargetType`: `str`
- `Status`: `ReviewActionStatus`
- `CompleteTime`: `datetime`
- `Result`: `str`
- `ErrorCode`: `str`


## ReviewPolicyTypeDef

```python
from mypy_boto3_mturk.type_defs import ReviewPolicyTypeDef
```


Required fields:
- `PolicyName`: `str`



Optional fields:
- `Parameters`: `List["PolicyParameterTypeDef"]`


## ReviewReportTypeDef

```python
from mypy_boto3_mturk.type_defs import ReviewReportTypeDef
```




Optional fields:
- `ReviewResults`: `List["ReviewResultDetailTypeDef"]`
- `ReviewActions`: `List["ReviewActionDetailTypeDef"]`


## ReviewResultDetailTypeDef

```python
from mypy_boto3_mturk.type_defs import ReviewResultDetailTypeDef
```




Optional fields:
- `ActionId`: `str`
- `SubjectId`: `str`
- `SubjectType`: `str`
- `QuestionId`: `str`
- `Key`: `str`
- `Value`: `str`


## WorkerBlockTypeDef

```python
from mypy_boto3_mturk.type_defs import WorkerBlockTypeDef
```




Optional fields:
- `WorkerId`: `str`
- `Reason`: `str`


## CreateHITResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import CreateHITResponseTypeDef
```




Optional fields:
- `HIT`: `"HITTypeDef"`


## CreateHITTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import CreateHITTypeResponseTypeDef
```




Optional fields:
- `HITTypeId`: `str`


## CreateHITWithHITTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import CreateHITWithHITTypeResponseTypeDef
```




Optional fields:
- `HIT`: `"HITTypeDef"`


## CreateQualificationTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import CreateQualificationTypeResponseTypeDef
```




Optional fields:
- `QualificationType`: `"QualificationTypeTypeDef"`


## GetAccountBalanceResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import GetAccountBalanceResponseTypeDef
```




Optional fields:
- `AvailableBalance`: `str`
- `OnHoldBalance`: `str`


## GetAssignmentResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import GetAssignmentResponseTypeDef
```




Optional fields:
- `Assignment`: `"AssignmentTypeDef"`
- `HIT`: `"HITTypeDef"`


## GetFileUploadURLResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import GetFileUploadURLResponseTypeDef
```




Optional fields:
- `FileUploadURL`: `str`


## GetHITResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import GetHITResponseTypeDef
```




Optional fields:
- `HIT`: `"HITTypeDef"`


## GetQualificationScoreResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import GetQualificationScoreResponseTypeDef
```




Optional fields:
- `Qualification`: `"QualificationTypeDef"`


## GetQualificationTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import GetQualificationTypeResponseTypeDef
```




Optional fields:
- `QualificationType`: `"QualificationTypeTypeDef"`


## HITLayoutParameterTypeDef

```python
from mypy_boto3_mturk.type_defs import HITLayoutParameterTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## ListAssignmentsForHITResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListAssignmentsForHITResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NumResults`: `int`
- `Assignments`: `List["AssignmentTypeDef"]`


## ListBonusPaymentsResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListBonusPaymentsResponseTypeDef
```




Optional fields:
- `NumResults`: `int`
- `NextToken`: `str`
- `BonusPayments`: `List["BonusPaymentTypeDef"]`


## ListHITsForQualificationTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListHITsForQualificationTypeResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NumResults`: `int`
- `HITs`: `List["HITTypeDef"]`


## ListHITsResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListHITsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NumResults`: `int`
- `HITs`: `List["HITTypeDef"]`


## ListQualificationRequestsResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListQualificationRequestsResponseTypeDef
```




Optional fields:
- `NumResults`: `int`
- `NextToken`: `str`
- `QualificationRequests`: `List["QualificationRequestTypeDef"]`


## ListQualificationTypesResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListQualificationTypesResponseTypeDef
```




Optional fields:
- `NumResults`: `int`
- `NextToken`: `str`
- `QualificationTypes`: `List["QualificationTypeTypeDef"]`


## ListReviewPolicyResultsForHITResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListReviewPolicyResultsForHITResponseTypeDef
```




Optional fields:
- `HITId`: `str`
- `AssignmentReviewPolicy`: `"ReviewPolicyTypeDef"`
- `HITReviewPolicy`: `"ReviewPolicyTypeDef"`
- `AssignmentReviewReport`: `"ReviewReportTypeDef"`
- `HITReviewReport`: `"ReviewReportTypeDef"`
- `NextToken`: `str`


## ListReviewableHITsResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListReviewableHITsResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NumResults`: `int`
- `HITs`: `List["HITTypeDef"]`


## ListWorkerBlocksResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListWorkerBlocksResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NumResults`: `int`
- `WorkerBlocks`: `List["WorkerBlockTypeDef"]`


## ListWorkersWithQualificationTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import ListWorkersWithQualificationTypeResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `NumResults`: `int`
- `Qualifications`: `List["QualificationTypeDef"]`


## NotificationSpecificationTypeDef

```python
from mypy_boto3_mturk.type_defs import NotificationSpecificationTypeDef
```


Required fields:
- `Destination`: `str`
- `Transport`: `NotificationTransport`
- `Version`: `str`
- `EventTypes`: `List[EventType]`




## NotifyWorkersResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import NotifyWorkersResponseTypeDef
```




Optional fields:
- `NotifyWorkersFailureStatuses`: `List["NotifyWorkersFailureStatusTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_mturk.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## UpdateQualificationTypeResponseTypeDef

```python
from mypy_boto3_mturk.type_defs import UpdateQualificationTypeResponseTypeDef
```




Optional fields:
- `QualificationType`: `"QualificationTypeTypeDef"`

