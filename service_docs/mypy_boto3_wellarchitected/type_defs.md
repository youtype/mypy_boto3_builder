# Structures for boto3 WellArchitected module

> [Index](../index.md) > [WellArchitected](./index.md) > Structures

Auto-generated documentation for [WellArchitected](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected)
type annotations stubs module [mypy_boto3_wellarchitected](https://pypi.org/project/mypy-boto3-wellarchitected/).

- [Structures for boto3 WellArchitected module](#structures-for-boto3-wellarchitected-module)
  - [AnswerSummaryTypeDef](#answersummarytypedef)
  - [AnswerTypeDef](#answertypedef)
  - [ChoiceTypeDef](#choicetypedef)
  - [ImprovementSummaryTypeDef](#improvementsummarytypedef)
  - [LensReviewReportTypeDef](#lensreviewreporttypedef)
  - [LensReviewSummaryTypeDef](#lensreviewsummarytypedef)
  - [LensReviewTypeDef](#lensreviewtypedef)
  - [LensSummaryTypeDef](#lenssummarytypedef)
  - [LensUpgradeSummaryTypeDef](#lensupgradesummarytypedef)
  - [MilestoneSummaryTypeDef](#milestonesummarytypedef)
  - [MilestoneTypeDef](#milestonetypedef)
  - [NotificationSummaryTypeDef](#notificationsummarytypedef)
  - [PillarDifferenceTypeDef](#pillardifferencetypedef)
  - [PillarReviewSummaryTypeDef](#pillarreviewsummarytypedef)
  - [QuestionDifferenceTypeDef](#questiondifferencetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [ShareInvitationSummaryTypeDef](#shareinvitationsummarytypedef)
  - [ShareInvitationTypeDef](#shareinvitationtypedef)
  - [VersionDifferencesTypeDef](#versiondifferencestypedef)
  - [WorkloadShareSummaryTypeDef](#workloadsharesummarytypedef)
  - [WorkloadShareTypeDef](#workloadsharetypedef)
  - [WorkloadSummaryTypeDef](#workloadsummarytypedef)
  - [WorkloadTypeDef](#workloadtypedef)
  - [CreateMilestoneOutputTypeDef](#createmilestoneoutputtypedef)
  - [CreateWorkloadOutputTypeDef](#createworkloadoutputtypedef)
  - [CreateWorkloadShareOutputTypeDef](#createworkloadshareoutputtypedef)
  - [GetAnswerOutputTypeDef](#getansweroutputtypedef)
  - [GetLensReviewOutputTypeDef](#getlensreviewoutputtypedef)
  - [GetLensReviewReportOutputTypeDef](#getlensreviewreportoutputtypedef)
  - [GetLensVersionDifferenceOutputTypeDef](#getlensversiondifferenceoutputtypedef)
  - [GetMilestoneOutputTypeDef](#getmilestoneoutputtypedef)
  - [GetWorkloadOutputTypeDef](#getworkloadoutputtypedef)
  - [ListAnswersOutputTypeDef](#listanswersoutputtypedef)
  - [ListLensReviewImprovementsOutputTypeDef](#listlensreviewimprovementsoutputtypedef)
  - [ListLensReviewsOutputTypeDef](#listlensreviewsoutputtypedef)
  - [ListLensesOutputTypeDef](#listlensesoutputtypedef)
  - [ListMilestonesOutputTypeDef](#listmilestonesoutputtypedef)
  - [ListNotificationsOutputTypeDef](#listnotificationsoutputtypedef)
  - [ListShareInvitationsOutputTypeDef](#listshareinvitationsoutputtypedef)
  - [ListTagsForResourceOutputTypeDef](#listtagsforresourceoutputtypedef)
  - [ListWorkloadSharesOutputTypeDef](#listworkloadsharesoutputtypedef)
  - [ListWorkloadsOutputTypeDef](#listworkloadsoutputtypedef)
  - [UpdateAnswerOutputTypeDef](#updateansweroutputtypedef)
  - [UpdateLensReviewOutputTypeDef](#updatelensreviewoutputtypedef)
  - [UpdateShareInvitationOutputTypeDef](#updateshareinvitationoutputtypedef)
  - [UpdateWorkloadOutputTypeDef](#updateworkloadoutputtypedef)
  - [UpdateWorkloadShareOutputTypeDef](#updateworkloadshareoutputtypedef)

## AnswerSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import AnswerSummaryTypeDef
```




Optional fields:
- `QuestionId`: `str`
- `PillarId`: `str`
- `QuestionTitle`: `str`
- `Choices`: `List["ChoiceTypeDef"]`
- `SelectedChoices`: `List[str]`
- `IsApplicable`: `bool`
- `Risk`: `Risk`


## AnswerTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import AnswerTypeDef
```




Optional fields:
- `QuestionId`: `str`
- `PillarId`: `str`
- `QuestionTitle`: `str`
- `QuestionDescription`: `str`
- `ImprovementPlanUrl`: `str`
- `HelpfulResourceUrl`: `str`
- `Choices`: `List["ChoiceTypeDef"]`
- `SelectedChoices`: `List[str]`
- `IsApplicable`: `bool`
- `Risk`: `Risk`
- `Notes`: `str`


## ChoiceTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ChoiceTypeDef
```




Optional fields:
- `ChoiceId`: `str`
- `Title`: `str`
- `Description`: `str`


## ImprovementSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ImprovementSummaryTypeDef
```




Optional fields:
- `QuestionId`: `str`
- `PillarId`: `str`
- `QuestionTitle`: `str`
- `Risk`: `Risk`
- `ImprovementPlanUrl`: `str`


## LensReviewReportTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import LensReviewReportTypeDef
```




Optional fields:
- `LensAlias`: `str`
- `Base64String`: `str`


## LensReviewSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import LensReviewSummaryTypeDef
```




Optional fields:
- `LensAlias`: `str`
- `LensVersion`: `str`
- `LensName`: `str`
- `LensStatus`: `LensStatus`
- `UpdatedAt`: `datetime`
- `RiskCounts`: `Dict[Risk, int]`


## LensReviewTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import LensReviewTypeDef
```




Optional fields:
- `LensAlias`: `str`
- `LensVersion`: `str`
- `LensName`: `str`
- `LensStatus`: `LensStatus`
- `PillarReviewSummaries`: `List["PillarReviewSummaryTypeDef"]`
- `UpdatedAt`: `datetime`
- `Notes`: `str`
- `RiskCounts`: `Dict[Risk, int]`
- `NextToken`: `str`


## LensSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import LensSummaryTypeDef
```




Optional fields:
- `LensAlias`: `str`
- `LensVersion`: `str`
- `LensName`: `str`
- `Description`: `str`


## LensUpgradeSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import LensUpgradeSummaryTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `WorkloadName`: `str`
- `LensAlias`: `str`
- `CurrentLensVersion`: `str`
- `LatestLensVersion`: `str`


## MilestoneSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import MilestoneSummaryTypeDef
```




Optional fields:
- `MilestoneNumber`: `int`
- `MilestoneName`: `str`
- `RecordedAt`: `datetime`
- `WorkloadSummary`: `"WorkloadSummaryTypeDef"`


## MilestoneTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import MilestoneTypeDef
```




Optional fields:
- `MilestoneNumber`: `int`
- `MilestoneName`: `str`
- `RecordedAt`: `datetime`
- `Workload`: `"WorkloadTypeDef"`


## NotificationSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import NotificationSummaryTypeDef
```




Optional fields:
- `Type`: `NotificationType`
- `LensUpgradeSummary`: `"LensUpgradeSummaryTypeDef"`


## PillarDifferenceTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import PillarDifferenceTypeDef
```




Optional fields:
- `PillarId`: `str`
- `DifferenceStatus`: `DifferenceStatus`
- `QuestionDifferences`: `List["QuestionDifferenceTypeDef"]`


## PillarReviewSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import PillarReviewSummaryTypeDef
```




Optional fields:
- `PillarId`: `str`
- `PillarName`: `str`
- `Notes`: `str`
- `RiskCounts`: `Dict[Risk, int]`


## QuestionDifferenceTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import QuestionDifferenceTypeDef
```




Optional fields:
- `QuestionId`: `str`
- `QuestionTitle`: `str`
- `DifferenceStatus`: `DifferenceStatus`


## ResponseMetadata

```python
from mypy_boto3_wellarchitected.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## ShareInvitationSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ShareInvitationSummaryTypeDef
```




Optional fields:
- `ShareInvitationId`: `str`
- `SharedBy`: `str`
- `SharedWith`: `str`
- `PermissionType`: `PermissionType`
- `WorkloadName`: `str`
- `WorkloadId`: `str`


## ShareInvitationTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ShareInvitationTypeDef
```




Optional fields:
- `ShareInvitationId`: `str`
- `WorkloadId`: `str`


## VersionDifferencesTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import VersionDifferencesTypeDef
```




Optional fields:
- `PillarDifferences`: `List["PillarDifferenceTypeDef"]`


## WorkloadShareSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import WorkloadShareSummaryTypeDef
```




Optional fields:
- `ShareId`: `str`
- `SharedWith`: `str`
- `PermissionType`: `PermissionType`
- `Status`: `ShareStatus`


## WorkloadShareTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import WorkloadShareTypeDef
```




Optional fields:
- `ShareId`: `str`
- `SharedBy`: `str`
- `SharedWith`: `str`
- `PermissionType`: `PermissionType`
- `Status`: `ShareStatus`
- `WorkloadName`: `str`
- `WorkloadId`: `str`


## WorkloadSummaryTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import WorkloadSummaryTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `WorkloadArn`: `str`
- `WorkloadName`: `str`
- `Owner`: `str`
- `UpdatedAt`: `datetime`
- `Lenses`: `List[str]`
- `RiskCounts`: `Dict[Risk, int]`
- `ImprovementStatus`: `WorkloadImprovementStatus`


## WorkloadTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import WorkloadTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `WorkloadArn`: `str`
- `WorkloadName`: `str`
- `Description`: `str`
- `Environment`: `WorkloadEnvironment`
- `UpdatedAt`: `datetime`
- `AccountIds`: `List[str]`
- `AwsRegions`: `List[str]`
- `NonAwsRegions`: `List[str]`
- `ArchitecturalDesign`: `str`
- `ReviewOwner`: `str`
- `ReviewRestrictionDate`: `datetime`
- `IsReviewOwnerUpdateAcknowledged`: `bool`
- `IndustryType`: `str`
- `Industry`: `str`
- `Notes`: `str`
- `ImprovementStatus`: `WorkloadImprovementStatus`
- `RiskCounts`: `Dict[Risk, int]`
- `PillarPriorities`: `List[str]`
- `Lenses`: `List[str]`
- `Owner`: `str`
- `ShareInvitationId`: `str`
- `Tags`: `Dict[str, str]`


## CreateMilestoneOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import CreateMilestoneOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateWorkloadOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import CreateWorkloadOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `WorkloadArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateWorkloadShareOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import CreateWorkloadShareOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `ShareId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetAnswerOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import GetAnswerOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `LensAlias`: `str`
- `Answer`: `"AnswerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetLensReviewOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import GetLensReviewOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `LensReview`: `"LensReviewTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetLensReviewReportOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import GetLensReviewReportOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `LensReviewReport`: `"LensReviewReportTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetLensVersionDifferenceOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import GetLensVersionDifferenceOutputTypeDef
```




Optional fields:
- `LensAlias`: `str`
- `BaseLensVersion`: `str`
- `LatestLensVersion`: `str`
- `VersionDifferences`: `"VersionDifferencesTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetMilestoneOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import GetMilestoneOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `Milestone`: `"MilestoneTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetWorkloadOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import GetWorkloadOutputTypeDef
```




Optional fields:
- `Workload`: `"WorkloadTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListAnswersOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListAnswersOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `LensAlias`: `str`
- `AnswerSummaries`: `List["AnswerSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListLensReviewImprovementsOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListLensReviewImprovementsOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `LensAlias`: `str`
- `ImprovementSummaries`: `List["ImprovementSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListLensReviewsOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListLensReviewsOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneNumber`: `int`
- `LensReviewSummaries`: `List["LensReviewSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListLensesOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListLensesOutputTypeDef
```




Optional fields:
- `LensSummaries`: `List["LensSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListMilestonesOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListMilestonesOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `MilestoneSummaries`: `List["MilestoneSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListNotificationsOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListNotificationsOutputTypeDef
```




Optional fields:
- `NotificationSummaries`: `List["NotificationSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListShareInvitationsOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListShareInvitationsOutputTypeDef
```




Optional fields:
- `ShareInvitationSummaries`: `List["ShareInvitationSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagsForResourceOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListTagsForResourceOutputTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListWorkloadSharesOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListWorkloadSharesOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `WorkloadShareSummaries`: `List["WorkloadShareSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListWorkloadsOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import ListWorkloadsOutputTypeDef
```




Optional fields:
- `WorkloadSummaries`: `List["WorkloadSummaryTypeDef"]`
- `NextToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateAnswerOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import UpdateAnswerOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `LensAlias`: `str`
- `Answer`: `"AnswerTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateLensReviewOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import UpdateLensReviewOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `LensReview`: `"LensReviewTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateShareInvitationOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import UpdateShareInvitationOutputTypeDef
```




Optional fields:
- `ShareInvitation`: `"ShareInvitationTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateWorkloadOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import UpdateWorkloadOutputTypeDef
```




Optional fields:
- `Workload`: `"WorkloadTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateWorkloadShareOutputTypeDef

```python
from mypy_boto3_wellarchitected.type_defs import UpdateWorkloadShareOutputTypeDef
```




Optional fields:
- `WorkloadId`: `str`
- `WorkloadShare`: `"WorkloadShareTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`

