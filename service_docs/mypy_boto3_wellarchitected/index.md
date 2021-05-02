# Type annotations for boto3 WellArchitected module

> [Index](../index.md) > WellArchitected

Auto-generated documentation for [WellArchitected](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected)
type annotations stubs module [mypy_boto3_wellarchitected](https://pypi.org/project/mypy-boto3-wellarchitected/).

```bash
pip install mypy-boto3-wellarchitected
```

- [Type annotations for boto3 WellArchitected module](#type-annotations-for-boto3-wellarchitected-module)
  - [WellArchitectedClient](#wellarchitectedclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## WellArchitectedClient

Type annotations for  `boto3.client("wellarchitected")` as [WellArchitectedClient](./client.md)

Can be used directly:

```python
from mypy_boto3_wellarchitected.client import WellArchitectedClient
```


WellArchitectedClient [exceptions](./client.md#exceptions)



### Methods
- [associate_lenses](./client.md#associate-lenses)
- [can_paginate](./client.md#can-paginate)
- [create_milestone](./client.md#create-milestone)
- [create_workload](./client.md#create-workload)
- [create_workload_share](./client.md#create-workload-share)
- [delete_workload](./client.md#delete-workload)
- [delete_workload_share](./client.md#delete-workload-share)
- [disassociate_lenses](./client.md#disassociate-lenses)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_answer](./client.md#get-answer)
- [get_lens_review](./client.md#get-lens-review)
- [get_lens_review_report](./client.md#get-lens-review-report)
- [get_lens_version_difference](./client.md#get-lens-version-difference)
- [get_milestone](./client.md#get-milestone)
- [get_workload](./client.md#get-workload)
- [list_answers](./client.md#list-answers)
- [list_lens_review_improvements](./client.md#list-lens-review-improvements)
- [list_lens_reviews](./client.md#list-lens-reviews)
- [list_lenses](./client.md#list-lenses)
- [list_milestones](./client.md#list-milestones)
- [list_notifications](./client.md#list-notifications)
- [list_share_invitations](./client.md#list-share-invitations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_workload_shares](./client.md#list-workload-shares)
- [list_workloads](./client.md#list-workloads)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_answer](./client.md#update-answer)
- [update_lens_review](./client.md#update-lens-review)
- [update_share_invitation](./client.md#update-share-invitation)
- [update_workload](./client.md#update-workload)
- [update_workload_share](./client.md#update-workload-share)
- [upgrade_lens_review](./client.md#upgrade-lens-review)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_wellarchitected.literals import DifferenceStatus, ...
```

- [DifferenceStatus](./literals.md#differencestatus)
- [LensStatus](./literals.md#lensstatus)
- [NotificationType](./literals.md#notificationtype)
- [PermissionType](./literals.md#permissiontype)
- [Risk](./literals.md#risk)
- [ShareInvitationAction](./literals.md#shareinvitationaction)
- [ShareStatus](./literals.md#sharestatus)
- [WorkloadEnvironment](./literals.md#workloadenvironment)
- [WorkloadImprovementStatus](./literals.md#workloadimprovementstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_wellarchitected.type_defs import AnswerSummaryTypeDef, ...
```

- [AnswerSummaryTypeDef](./type_defs.md#answersummarytypedef)
- [AnswerTypeDef](./type_defs.md#answertypedef)
- [ChoiceTypeDef](./type_defs.md#choicetypedef)
- [CreateMilestoneOutputTypeDef](./type_defs.md#createmilestoneoutputtypedef)
- [CreateWorkloadOutputTypeDef](./type_defs.md#createworkloadoutputtypedef)
- [CreateWorkloadShareOutputTypeDef](./type_defs.md#createworkloadshareoutputtypedef)
- [GetAnswerOutputTypeDef](./type_defs.md#getansweroutputtypedef)
- [GetLensReviewOutputTypeDef](./type_defs.md#getlensreviewoutputtypedef)
- [GetLensReviewReportOutputTypeDef](./type_defs.md#getlensreviewreportoutputtypedef)
- [GetLensVersionDifferenceOutputTypeDef](./type_defs.md#getlensversiondifferenceoutputtypedef)
- [GetMilestoneOutputTypeDef](./type_defs.md#getmilestoneoutputtypedef)
- [GetWorkloadOutputTypeDef](./type_defs.md#getworkloadoutputtypedef)
- [ImprovementSummaryTypeDef](./type_defs.md#improvementsummarytypedef)
- [LensReviewReportTypeDef](./type_defs.md#lensreviewreporttypedef)
- [LensReviewSummaryTypeDef](./type_defs.md#lensreviewsummarytypedef)
- [LensReviewTypeDef](./type_defs.md#lensreviewtypedef)
- [LensSummaryTypeDef](./type_defs.md#lenssummarytypedef)
- [LensUpgradeSummaryTypeDef](./type_defs.md#lensupgradesummarytypedef)
- [ListAnswersOutputTypeDef](./type_defs.md#listanswersoutputtypedef)
- [ListLensReviewImprovementsOutputTypeDef](./type_defs.md#listlensreviewimprovementsoutputtypedef)
- [ListLensReviewsOutputTypeDef](./type_defs.md#listlensreviewsoutputtypedef)
- [ListLensesOutputTypeDef](./type_defs.md#listlensesoutputtypedef)
- [ListMilestonesOutputTypeDef](./type_defs.md#listmilestonesoutputtypedef)
- [ListNotificationsOutputTypeDef](./type_defs.md#listnotificationsoutputtypedef)
- [ListShareInvitationsOutputTypeDef](./type_defs.md#listshareinvitationsoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [ListWorkloadSharesOutputTypeDef](./type_defs.md#listworkloadsharesoutputtypedef)
- [ListWorkloadsOutputTypeDef](./type_defs.md#listworkloadsoutputtypedef)
- [MilestoneSummaryTypeDef](./type_defs.md#milestonesummarytypedef)
- [MilestoneTypeDef](./type_defs.md#milestonetypedef)
- [NotificationSummaryTypeDef](./type_defs.md#notificationsummarytypedef)
- [PillarDifferenceTypeDef](./type_defs.md#pillardifferencetypedef)
- [PillarReviewSummaryTypeDef](./type_defs.md#pillarreviewsummarytypedef)
- [QuestionDifferenceTypeDef](./type_defs.md#questiondifferencetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [ShareInvitationSummaryTypeDef](./type_defs.md#shareinvitationsummarytypedef)
- [ShareInvitationTypeDef](./type_defs.md#shareinvitationtypedef)
- [UpdateAnswerOutputTypeDef](./type_defs.md#updateansweroutputtypedef)
- [UpdateLensReviewOutputTypeDef](./type_defs.md#updatelensreviewoutputtypedef)
- [UpdateShareInvitationOutputTypeDef](./type_defs.md#updateshareinvitationoutputtypedef)
- [UpdateWorkloadOutputTypeDef](./type_defs.md#updateworkloadoutputtypedef)
- [UpdateWorkloadShareOutputTypeDef](./type_defs.md#updateworkloadshareoutputtypedef)
- [VersionDifferencesTypeDef](./type_defs.md#versiondifferencestypedef)
- [WorkloadShareSummaryTypeDef](./type_defs.md#workloadsharesummarytypedef)
- [WorkloadShareTypeDef](./type_defs.md#workloadsharetypedef)
- [WorkloadSummaryTypeDef](./type_defs.md#workloadsummarytypedef)
- [WorkloadTypeDef](./type_defs.md#workloadtypedef)
