# MTurkClient for boto3 MTurk module

> [Index](../index.md) > [MTurk](./index.md) > MTurkClient

Auto-generated documentation for [MTurk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk)
type annotations stubs module [mypy_boto3_mturk](https://pypi.org/project/mypy-boto3-mturk/).

- [MTurkClient for boto3 MTurk module](#mturkclient-for-boto3-mturk-module)
  - [MTurkClient](#mturkclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_qualification_request](#accept_qualification_request)
    - [approve_assignment](#approve_assignment)
    - [associate_qualification_with_worker](#associate_qualification_with_worker)
    - [can_paginate](#can_paginate)
    - [create_additional_assignments_for_hit](#create_additional_assignments_for_hit)
    - [create_hit](#create_hit)
    - [create_hit_type](#create_hit_type)
    - [create_hit_with_hit_type](#create_hit_with_hit_type)
    - [create_qualification_type](#create_qualification_type)
    - [create_worker_block](#create_worker_block)
    - [delete_hit](#delete_hit)
    - [delete_qualification_type](#delete_qualification_type)
    - [delete_worker_block](#delete_worker_block)
    - [disassociate_qualification_from_worker](#disassociate_qualification_from_worker)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_balance](#get_account_balance)
    - [get_assignment](#get_assignment)
    - [get_file_upload_url](#get_file_upload_url)
    - [get_hit](#get_hit)
    - [get_qualification_score](#get_qualification_score)
    - [get_qualification_type](#get_qualification_type)
    - [list_assignments_for_hit](#list_assignments_for_hit)
    - [list_bonus_payments](#list_bonus_payments)
    - [list_hits](#list_hits)
    - [list_hits_for_qualification_type](#list_hits_for_qualification_type)
    - [list_qualification_requests](#list_qualification_requests)
    - [list_qualification_types](#list_qualification_types)
    - [list_review_policy_results_for_hit](#list_review_policy_results_for_hit)
    - [list_reviewable_hits](#list_reviewable_hits)
    - [list_worker_blocks](#list_worker_blocks)
    - [list_workers_with_qualification_type](#list_workers_with_qualification_type)
    - [notify_workers](#notify_workers)
    - [reject_assignment](#reject_assignment)
    - [reject_qualification_request](#reject_qualification_request)
    - [send_bonus](#send_bonus)
    - [send_test_event_notification](#send_test_event_notification)
    - [update_expiration_for_hit](#update_expiration_for_hit)
    - [update_hit_review_status](#update_hit_review_status)
    - [update_hit_type_of_hit](#update_hit_type_of_hit)
    - [update_notification_settings](#update_notification_settings)
    - [update_qualification_type](#update_qualification_type)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)

## MTurkClient

Type annotations for `boto3.client("mturk")`

Can be used directly:

```python
from mypy_boto3_mturk.client import MTurkClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mturk.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.RequestError`
- `Exceptions.ServiceFault`


## Methods


### accept_qualification_request

Type annotations for `boto3.client("mturk").accept_qualification_request` method.

[Client.accept_qualification_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.accept_qualification_request)

```python
def accept_qualification_request(
    self,
    QualificationRequestId: str,
    IntegerValue: int = None
) -> Dict[str, Any]:
    pass
```

### approve_assignment

Type annotations for `boto3.client("mturk").approve_assignment` method.

[Client.approve_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.approve_assignment)

```python
def approve_assignment(
    self,
    AssignmentId: str,
    RequesterFeedback: str = None,
    OverrideRejection: bool = None
) -> Dict[str, Any]:
    pass
```

### associate_qualification_with_worker

Type annotations for `boto3.client("mturk").associate_qualification_with_worker` method.

[Client.associate_qualification_with_worker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.associate_qualification_with_worker)

```python
def associate_qualification_with_worker(
    self,
    QualificationTypeId: str,
    WorkerId: str,
    IntegerValue: int = None,
    SendNotification: bool = None
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("mturk").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_additional_assignments_for_hit

Type annotations for `boto3.client("mturk").create_additional_assignments_for_hit` method.

[Client.create_additional_assignments_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_additional_assignments_for_hit)

```python
def create_additional_assignments_for_hit(
    self,
    HITId: str,
    NumberOfAdditionalAssignments: int,
    UniqueRequestToken: str = None
) -> Dict[str, Any]:
    pass
```

### create_hit

Type annotations for `boto3.client("mturk").create_hit` method.

[Client.create_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_hit)

```python
def create_hit(
    self,
    LifetimeInSeconds: int,
    AssignmentDurationInSeconds: int,
    Reward: str,
    Title: str,
    Description: str,
    MaxAssignments: int = None,
    AutoApprovalDelayInSeconds: int = None,
    Keywords: str = None,
    Question: str = None,
    RequesterAnnotation: str = None,
    QualificationRequirements: List["QualificationRequirementTypeDef"] = None,
    UniqueRequestToken: str = None,
    AssignmentReviewPolicy: "ReviewPolicyTypeDef" = None,
    HITReviewPolicy: "ReviewPolicyTypeDef" = None,
    HITLayoutId: str = None,
    HITLayoutParameters: List[HITLayoutParameterTypeDef] = None
) -> CreateHITResponseTypeDef:
    pass
```

### create_hit_type

Type annotations for `boto3.client("mturk").create_hit_type` method.

[Client.create_hit_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_hit_type)

```python
def create_hit_type(
    self,
    AssignmentDurationInSeconds: int,
    Reward: str,
    Title: str,
    Description: str,
    AutoApprovalDelayInSeconds: int = None,
    Keywords: str = None,
    QualificationRequirements: List["QualificationRequirementTypeDef"] = None
) -> CreateHITTypeResponseTypeDef:
    pass
```

### create_hit_with_hit_type

Type annotations for `boto3.client("mturk").create_hit_with_hit_type` method.

[Client.create_hit_with_hit_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_hit_with_hit_type)

```python
def create_hit_with_hit_type(
    self,
    HITTypeId: str,
    LifetimeInSeconds: int,
    MaxAssignments: int = None,
    Question: str = None,
    RequesterAnnotation: str = None,
    UniqueRequestToken: str = None,
    AssignmentReviewPolicy: "ReviewPolicyTypeDef" = None,
    HITReviewPolicy: "ReviewPolicyTypeDef" = None,
    HITLayoutId: str = None,
    HITLayoutParameters: List[HITLayoutParameterTypeDef] = None
) -> CreateHITWithHITTypeResponseTypeDef:
    pass
```

### create_qualification_type

Type annotations for `boto3.client("mturk").create_qualification_type` method.

[Client.create_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_qualification_type)

```python
def create_qualification_type(
    self,
    Name: str,
    Description: str,
    QualificationTypeStatus: QualificationTypeStatus,
    Keywords: str = None,
    RetryDelayInSeconds: int = None,
    Test: str = None,
    AnswerKey: str = None,
    TestDurationInSeconds: int = None,
    AutoGranted: bool = None,
    AutoGrantedValue: int = None
) -> CreateQualificationTypeResponseTypeDef:
    pass
```

### create_worker_block

Type annotations for `boto3.client("mturk").create_worker_block` method.

[Client.create_worker_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_worker_block)

```python
def create_worker_block(
    self,
    WorkerId: str,
    Reason: str
) -> Dict[str, Any]:
    pass
```

### delete_hit

Type annotations for `boto3.client("mturk").delete_hit` method.

[Client.delete_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.delete_hit)

```python
def delete_hit(
    self,
    HITId: str
) -> Dict[str, Any]:
    pass
```

### delete_qualification_type

Type annotations for `boto3.client("mturk").delete_qualification_type` method.

[Client.delete_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.delete_qualification_type)

```python
def delete_qualification_type(
    self,
    QualificationTypeId: str
) -> Dict[str, Any]:
    pass
```

### delete_worker_block

Type annotations for `boto3.client("mturk").delete_worker_block` method.

[Client.delete_worker_block documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.delete_worker_block)

```python
def delete_worker_block(
    self,
    WorkerId: str,
    Reason: str = None
) -> Dict[str, Any]:
    pass
```

### disassociate_qualification_from_worker

Type annotations for `boto3.client("mturk").disassociate_qualification_from_worker` method.

[Client.disassociate_qualification_from_worker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.disassociate_qualification_from_worker)

```python
def disassociate_qualification_from_worker(
    self,
    WorkerId: str,
    QualificationTypeId: str,
    Reason: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mturk").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.generate_presigned_url)

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

### get_account_balance

Type annotations for `boto3.client("mturk").get_account_balance` method.

[Client.get_account_balance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_account_balance)

```python
def get_account_balance(
    self
) -> GetAccountBalanceResponseTypeDef:
    pass
```

### get_assignment

Type annotations for `boto3.client("mturk").get_assignment` method.

[Client.get_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_assignment)

```python
def get_assignment(
    self,
    AssignmentId: str
) -> GetAssignmentResponseTypeDef:
    pass
```

### get_file_upload_url

Type annotations for `boto3.client("mturk").get_file_upload_url` method.

[Client.get_file_upload_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_file_upload_url)

```python
def get_file_upload_url(
    self,
    AssignmentId: str,
    QuestionIdentifier: str
) -> GetFileUploadURLResponseTypeDef:
    pass
```

### get_hit

Type annotations for `boto3.client("mturk").get_hit` method.

[Client.get_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_hit)

```python
def get_hit(
    self,
    HITId: str
) -> GetHITResponseTypeDef:
    pass
```

### get_qualification_score

Type annotations for `boto3.client("mturk").get_qualification_score` method.

[Client.get_qualification_score documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_qualification_score)

```python
def get_qualification_score(
    self,
    QualificationTypeId: str,
    WorkerId: str
) -> GetQualificationScoreResponseTypeDef:
    pass
```

### get_qualification_type

Type annotations for `boto3.client("mturk").get_qualification_type` method.

[Client.get_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_qualification_type)

```python
def get_qualification_type(
    self,
    QualificationTypeId: str
) -> GetQualificationTypeResponseTypeDef:
    pass
```

### list_assignments_for_hit

Type annotations for `boto3.client("mturk").list_assignments_for_hit` method.

[Client.list_assignments_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_assignments_for_hit)

```python
def list_assignments_for_hit(
    self,
    HITId: str,
    NextToken: str = None,
    MaxResults: int = None,
    AssignmentStatuses: List[AssignmentStatus] = None
) -> ListAssignmentsForHITResponseTypeDef:
    pass
```

### list_bonus_payments

Type annotations for `boto3.client("mturk").list_bonus_payments` method.

[Client.list_bonus_payments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_bonus_payments)

```python
def list_bonus_payments(
    self,
    HITId: str = None,
    AssignmentId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListBonusPaymentsResponseTypeDef:
    pass
```

### list_hits

Type annotations for `boto3.client("mturk").list_hits` method.

[Client.list_hits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_hits)

```python
def list_hits(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHITsResponseTypeDef:
    pass
```

### list_hits_for_qualification_type

Type annotations for `boto3.client("mturk").list_hits_for_qualification_type` method.

[Client.list_hits_for_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_hits_for_qualification_type)

```python
def list_hits_for_qualification_type(
    self,
    QualificationTypeId: str,
    NextToken: str = None,
    MaxResults: int = None
) -> ListHITsForQualificationTypeResponseTypeDef:
    pass
```

### list_qualification_requests

Type annotations for `boto3.client("mturk").list_qualification_requests` method.

[Client.list_qualification_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_qualification_requests)

```python
def list_qualification_requests(
    self,
    QualificationTypeId: str = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListQualificationRequestsResponseTypeDef:
    pass
```

### list_qualification_types

Type annotations for `boto3.client("mturk").list_qualification_types` method.

[Client.list_qualification_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_qualification_types)

```python
def list_qualification_types(
    self,
    MustBeRequestable: bool,
    Query: str = None,
    MustBeOwnedByCaller: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListQualificationTypesResponseTypeDef:
    pass
```

### list_review_policy_results_for_hit

Type annotations for `boto3.client("mturk").list_review_policy_results_for_hit` method.

[Client.list_review_policy_results_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_review_policy_results_for_hit)

```python
def list_review_policy_results_for_hit(
    self,
    HITId: str,
    PolicyLevels: List[ReviewPolicyLevel] = None,
    RetrieveActions: bool = None,
    RetrieveResults: bool = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListReviewPolicyResultsForHITResponseTypeDef:
    pass
```

### list_reviewable_hits

Type annotations for `boto3.client("mturk").list_reviewable_hits` method.

[Client.list_reviewable_hits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_reviewable_hits)

```python
def list_reviewable_hits(
    self,
    HITTypeId: str = None,
    Status: ReviewableHITStatus = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListReviewableHITsResponseTypeDef:
    pass
```

### list_worker_blocks

Type annotations for `boto3.client("mturk").list_worker_blocks` method.

[Client.list_worker_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_worker_blocks)

```python
def list_worker_blocks(
    self,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkerBlocksResponseTypeDef:
    pass
```

### list_workers_with_qualification_type

Type annotations for `boto3.client("mturk").list_workers_with_qualification_type` method.

[Client.list_workers_with_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_workers_with_qualification_type)

```python
def list_workers_with_qualification_type(
    self,
    QualificationTypeId: str,
    Status: QualificationStatus = None,
    NextToken: str = None,
    MaxResults: int = None
) -> ListWorkersWithQualificationTypeResponseTypeDef:
    pass
```

### notify_workers

Type annotations for `boto3.client("mturk").notify_workers` method.

[Client.notify_workers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.notify_workers)

```python
def notify_workers(
    self,
    Subject: str,
    MessageText: str,
    WorkerIds: List[str]
) -> NotifyWorkersResponseTypeDef:
    pass
```

### reject_assignment

Type annotations for `boto3.client("mturk").reject_assignment` method.

[Client.reject_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.reject_assignment)

```python
def reject_assignment(
    self,
    AssignmentId: str,
    RequesterFeedback: str
) -> Dict[str, Any]:
    pass
```

### reject_qualification_request

Type annotations for `boto3.client("mturk").reject_qualification_request` method.

[Client.reject_qualification_request documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.reject_qualification_request)

```python
def reject_qualification_request(
    self,
    QualificationRequestId: str,
    Reason: str = None
) -> Dict[str, Any]:
    pass
```

### send_bonus

Type annotations for `boto3.client("mturk").send_bonus` method.

[Client.send_bonus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.send_bonus)

```python
def send_bonus(
    self,
    WorkerId: str,
    BonusAmount: str,
    AssignmentId: str,
    Reason: str,
    UniqueRequestToken: str = None
) -> Dict[str, Any]:
    pass
```

### send_test_event_notification

Type annotations for `boto3.client("mturk").send_test_event_notification` method.

[Client.send_test_event_notification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.send_test_event_notification)

```python
def send_test_event_notification(
    self,
    Notification: NotificationSpecificationTypeDef,
    TestEventType: EventType
) -> Dict[str, Any]:
    pass
```

### update_expiration_for_hit

Type annotations for `boto3.client("mturk").update_expiration_for_hit` method.

[Client.update_expiration_for_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_expiration_for_hit)

```python
def update_expiration_for_hit(
    self,
    HITId: str,
    ExpireAt: datetime
) -> Dict[str, Any]:
    pass
```

### update_hit_review_status

Type annotations for `boto3.client("mturk").update_hit_review_status` method.

[Client.update_hit_review_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_hit_review_status)

```python
def update_hit_review_status(
    self,
    HITId: str,
    Revert: bool = None
) -> Dict[str, Any]:
    pass
```

### update_hit_type_of_hit

Type annotations for `boto3.client("mturk").update_hit_type_of_hit` method.

[Client.update_hit_type_of_hit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_hit_type_of_hit)

```python
def update_hit_type_of_hit(
    self,
    HITId: str,
    HITTypeId: str
) -> Dict[str, Any]:
    pass
```

### update_notification_settings

Type annotations for `boto3.client("mturk").update_notification_settings` method.

[Client.update_notification_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_notification_settings)

```python
def update_notification_settings(
    self,
    HITTypeId: str,
    Notification: NotificationSpecificationTypeDef = None,
    Active: bool = None
) -> Dict[str, Any]:
    pass
```

### update_qualification_type

Type annotations for `boto3.client("mturk").update_qualification_type` method.

[Client.update_qualification_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_qualification_type)

```python
def update_qualification_type(
    self,
    QualificationTypeId: str,
    Description: str = None,
    QualificationTypeStatus: QualificationTypeStatus = None,
    Test: str = None,
    AnswerKey: str = None,
    TestDurationInSeconds: int = None,
    RetryDelayInSeconds: int = None,
    AutoGranted: bool = None,
    AutoGrantedValue: int = None
) -> UpdateQualificationTypeResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListAssignmentsForHIT documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)

```python
@overload
def get_paginator(
    self,
    operation_name: ListAssignmentsForHITPaginatorName
) -> ListAssignmentsForHITPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListBonusPayments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)

```python
@overload
def get_paginator(
    self,
    operation_name: ListBonusPaymentsPaginatorName
) -> ListBonusPaymentsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListHITs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListHITsPaginatorName
) -> ListHITsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListHITsForQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)

```python
@overload
def get_paginator(
    self,
    operation_name: ListHITsForQualificationTypePaginatorName
) -> ListHITsForQualificationTypePaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListQualificationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQualificationRequestsPaginatorName
) -> ListQualificationRequestsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListQualificationTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQualificationTypesPaginatorName
) -> ListQualificationTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListReviewableHITs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListReviewableHITsPaginatorName
) -> ListReviewableHITsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListWorkerBlocks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListWorkerBlocksPaginatorName
) -> ListWorkerBlocksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("mturk").get_paginator` method.

[Paginator.ListWorkersWithQualificationType documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)

```python
@overload
def get_paginator(
    self,
    operation_name: ListWorkersWithQualificationTypePaginatorName
) -> ListWorkersWithQualificationTypePaginator:
    pass
```