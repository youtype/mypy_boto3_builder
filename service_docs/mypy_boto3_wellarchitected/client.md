# WellArchitectedClient for boto3 WellArchitected module

> [Index](../index.md) > [WellArchitected](./index.md) > WellArchitectedClient

Auto-generated documentation for [WellArchitected](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected)
type annotations stubs module [mypy_boto3_wellarchitected](https://pypi.org/project/mypy-boto3-wellarchitected/).

- [WellArchitectedClient for boto3 WellArchitected module](#wellarchitectedclient-for-boto3-wellarchitected-module)
  - [WellArchitectedClient](#wellarchitectedclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [associate_lenses](#associate_lenses)
    - [can_paginate](#can_paginate)
    - [create_milestone](#create_milestone)
    - [create_workload](#create_workload)
    - [create_workload_share](#create_workload_share)
    - [delete_workload](#delete_workload)
    - [delete_workload_share](#delete_workload_share)
    - [disassociate_lenses](#disassociate_lenses)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_answer](#get_answer)
    - [get_lens_review](#get_lens_review)
    - [get_lens_review_report](#get_lens_review_report)
    - [get_lens_version_difference](#get_lens_version_difference)
    - [get_milestone](#get_milestone)
    - [get_workload](#get_workload)
    - [list_answers](#list_answers)
    - [list_lens_review_improvements](#list_lens_review_improvements)
    - [list_lens_reviews](#list_lens_reviews)
    - [list_lenses](#list_lenses)
    - [list_milestones](#list_milestones)
    - [list_notifications](#list_notifications)
    - [list_share_invitations](#list_share_invitations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_workload_shares](#list_workload_shares)
    - [list_workloads](#list_workloads)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_answer](#update_answer)
    - [update_lens_review](#update_lens_review)
    - [update_share_invitation](#update_share_invitation)
    - [update_workload](#update_workload)
    - [update_workload_share](#update_workload_share)
    - [upgrade_lens_review](#upgrade_lens_review)

## WellArchitectedClient

Type annotations for `boto3.client("wellarchitected")`

Can be used directly:

```python
from mypy_boto3_wellarchitected.client import WellArchitectedClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_wellarchitected.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ThrottlingException`
- `Exceptions.ValidationException`


## Methods


### associate_lenses

Type annotations for `boto3.client("wellarchitected").associate_lenses` method.

[Client.associate_lenses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.associate_lenses)

```python
def associate_lenses(
    self,
    WorkloadId: str,
    LensAliases: List[str]
) -> None:
    pass
```

### can_paginate

Type annotations for `boto3.client("wellarchitected").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_milestone

Type annotations for `boto3.client("wellarchitected").create_milestone` method.

[Client.create_milestone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.create_milestone)

```python
def create_milestone(
    self,
    WorkloadId: str,
    MilestoneName: str,
    ClientRequestToken: str
) -> CreateMilestoneOutputTypeDef:
    pass
```

### create_workload

Type annotations for `boto3.client("wellarchitected").create_workload` method.

[Client.create_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.create_workload)

```python
def create_workload(
    self,
    WorkloadName: str,
    Description: str,
    Environment: WorkloadEnvironment,
    ReviewOwner: str,
    Lenses: List[str],
    ClientRequestToken: str,
    AccountIds: List[str] = None,
    AwsRegions: List[str] = None,
    NonAwsRegions: List[str] = None,
    PillarPriorities: List[str] = None,
    ArchitecturalDesign: str = None,
    IndustryType: str = None,
    Industry: str = None,
    Notes: str = None,
    Tags: Dict[str, str] = None
) -> CreateWorkloadOutputTypeDef:
    pass
```

### create_workload_share

Type annotations for `boto3.client("wellarchitected").create_workload_share` method.

[Client.create_workload_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.create_workload_share)

```python
def create_workload_share(
    self,
    WorkloadId: str,
    SharedWith: str,
    PermissionType: PermissionType,
    ClientRequestToken: str
) -> CreateWorkloadShareOutputTypeDef:
    pass
```

### delete_workload

Type annotations for `boto3.client("wellarchitected").delete_workload` method.

[Client.delete_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload)

```python
def delete_workload(
    self,
    WorkloadId: str,
    ClientRequestToken: str
) -> None:
    pass
```

### delete_workload_share

Type annotations for `boto3.client("wellarchitected").delete_workload_share` method.

[Client.delete_workload_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload_share)

```python
def delete_workload_share(
    self,
    ShareId: str,
    WorkloadId: str,
    ClientRequestToken: str
) -> None:
    pass
```

### disassociate_lenses

Type annotations for `boto3.client("wellarchitected").disassociate_lenses` method.

[Client.disassociate_lenses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.disassociate_lenses)

```python
def disassociate_lenses(
    self,
    WorkloadId: str,
    LensAliases: List[str]
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("wellarchitected").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.generate_presigned_url)

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

### get_answer

Type annotations for `boto3.client("wellarchitected").get_answer` method.

[Client.get_answer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.get_answer)

```python
def get_answer(
    self,
    WorkloadId: str,
    LensAlias: str,
    QuestionId: str,
    MilestoneNumber: int = None
) -> GetAnswerOutputTypeDef:
    pass
```

### get_lens_review

Type annotations for `boto3.client("wellarchitected").get_lens_review` method.

[Client.get_lens_review documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review)

```python
def get_lens_review(
    self,
    WorkloadId: str,
    LensAlias: str,
    MilestoneNumber: int = None
) -> GetLensReviewOutputTypeDef:
    pass
```

### get_lens_review_report

Type annotations for `boto3.client("wellarchitected").get_lens_review_report` method.

[Client.get_lens_review_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review_report)

```python
def get_lens_review_report(
    self,
    WorkloadId: str,
    LensAlias: str,
    MilestoneNumber: int = None
) -> GetLensReviewReportOutputTypeDef:
    pass
```

### get_lens_version_difference

Type annotations for `boto3.client("wellarchitected").get_lens_version_difference` method.

[Client.get_lens_version_difference documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_version_difference)

```python
def get_lens_version_difference(
    self,
    LensAlias: str,
    BaseLensVersion: str
) -> GetLensVersionDifferenceOutputTypeDef:
    pass
```

### get_milestone

Type annotations for `boto3.client("wellarchitected").get_milestone` method.

[Client.get_milestone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.get_milestone)

```python
def get_milestone(
    self,
    WorkloadId: str,
    MilestoneNumber: int
) -> GetMilestoneOutputTypeDef:
    pass
```

### get_workload

Type annotations for `boto3.client("wellarchitected").get_workload` method.

[Client.get_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.get_workload)

```python
def get_workload(
    self,
    WorkloadId: str
) -> GetWorkloadOutputTypeDef:
    pass
```

### list_answers

Type annotations for `boto3.client("wellarchitected").list_answers` method.

[Client.list_answers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_answers)

```python
def list_answers(
    self,
    WorkloadId: str,
    LensAlias: str,
    PillarId: str = None,
    MilestoneNumber: int = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListAnswersOutputTypeDef:
    pass
```

### list_lens_review_improvements

Type annotations for `boto3.client("wellarchitected").list_lens_review_improvements` method.

[Client.list_lens_review_improvements documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_review_improvements)

```python
def list_lens_review_improvements(
    self,
    WorkloadId: str,
    LensAlias: str,
    PillarId: str = None,
    MilestoneNumber: int = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLensReviewImprovementsOutputTypeDef:
    pass
```

### list_lens_reviews

Type annotations for `boto3.client("wellarchitected").list_lens_reviews` method.

[Client.list_lens_reviews documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_reviews)

```python
def list_lens_reviews(
    self,
    WorkloadId: str,
    MilestoneNumber: int = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLensReviewsOutputTypeDef:
    pass
```

### list_lenses

Type annotations for `boto3.client("wellarchitected").list_lenses` method.

[Client.list_lenses documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_lenses)

```python
def list_lenses(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListLensesOutputTypeDef:
    pass
```

### list_milestones

Type annotations for `boto3.client("wellarchitected").list_milestones` method.

[Client.list_milestones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_milestones)

```python
def list_milestones(
    self,
    WorkloadId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListMilestonesOutputTypeDef:
    pass
```

### list_notifications

Type annotations for `boto3.client("wellarchitected").list_notifications` method.

[Client.list_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_notifications)

```python
def list_notifications(
    self,
    WorkloadId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListNotificationsOutputTypeDef:
    pass
```

### list_share_invitations

Type annotations for `boto3.client("wellarchitected").list_share_invitations` method.

[Client.list_share_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_share_invitations)

```python
def list_share_invitations(
    self,
    WorkloadNamePrefix: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListShareInvitationsOutputTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("wellarchitected").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    WorkloadArn: str
) -> ListTagsForResourceOutputTypeDef:
    pass
```

### list_workload_shares

Type annotations for `boto3.client("wellarchitected").list_workload_shares` method.

[Client.list_workload_shares documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_workload_shares)

```python
def list_workload_shares(
    self,
    WorkloadId: str,
    SharedWithPrefix: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkloadSharesOutputTypeDef:
    pass
```

### list_workloads

Type annotations for `boto3.client("wellarchitected").list_workloads` method.

[Client.list_workloads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.list_workloads)

```python
def list_workloads(
    self,
    WorkloadNamePrefix: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkloadsOutputTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("wellarchitected").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.tag_resource)

```python
def tag_resource(
    self,
    WorkloadArn: str,
    Tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("wellarchitected").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.untag_resource)

```python
def untag_resource(
    self,
    WorkloadArn: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_answer

Type annotations for `boto3.client("wellarchitected").update_answer` method.

[Client.update_answer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.update_answer)

```python
def update_answer(
    self,
    WorkloadId: str,
    LensAlias: str,
    QuestionId: str,
    SelectedChoices: List[str] = None,
    Notes: str = None,
    IsApplicable: bool = None
) -> UpdateAnswerOutputTypeDef:
    pass
```

### update_lens_review

Type annotations for `boto3.client("wellarchitected").update_lens_review` method.

[Client.update_lens_review documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.update_lens_review)

```python
def update_lens_review(
    self,
    WorkloadId: str,
    LensAlias: str,
    LensNotes: str = None,
    PillarNotes: Dict[str, str] = None
) -> UpdateLensReviewOutputTypeDef:
    pass
```

### update_share_invitation

Type annotations for `boto3.client("wellarchitected").update_share_invitation` method.

[Client.update_share_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.update_share_invitation)

```python
def update_share_invitation(
    self,
    ShareInvitationId: str,
    ShareInvitationAction: ShareInvitationAction
) -> UpdateShareInvitationOutputTypeDef:
    pass
```

### update_workload

Type annotations for `boto3.client("wellarchitected").update_workload` method.

[Client.update_workload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.update_workload)

```python
def update_workload(
    self,
    WorkloadId: str,
    WorkloadName: str = None,
    Description: str = None,
    Environment: WorkloadEnvironment = None,
    AccountIds: List[str] = None,
    AwsRegions: List[str] = None,
    NonAwsRegions: List[str] = None,
    PillarPriorities: List[str] = None,
    ArchitecturalDesign: str = None,
    ReviewOwner: str = None,
    IsReviewOwnerUpdateAcknowledged: bool = None,
    IndustryType: str = None,
    Industry: str = None,
    Notes: str = None,
    ImprovementStatus: WorkloadImprovementStatus = None
) -> UpdateWorkloadOutputTypeDef:
    pass
```

### update_workload_share

Type annotations for `boto3.client("wellarchitected").update_workload_share` method.

[Client.update_workload_share documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.update_workload_share)

```python
def update_workload_share(
    self,
    ShareId: str,
    WorkloadId: str,
    PermissionType: PermissionType
) -> UpdateWorkloadShareOutputTypeDef:
    pass
```

### upgrade_lens_review

Type annotations for `boto3.client("wellarchitected").upgrade_lens_review` method.

[Client.upgrade_lens_review documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client.upgrade_lens_review)

```python
def upgrade_lens_review(
    self,
    WorkloadId: str,
    LensAlias: str,
    MilestoneName: str,
    ClientRequestToken: str = None
) -> None:
    pass
```



