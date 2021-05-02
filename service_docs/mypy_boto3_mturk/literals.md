# Literals for boto3 MTurk module

> [Index](../index.md) > [MTurk](./index.md) > Literals

Auto-generated documentation for [MTurk](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk)
type annotations stubs module [mypy_boto3_mturk](https://pypi.org/project/mypy-boto3-mturk/).

- [Literals for boto3 MTurk module](#literals-for-boto3-mturk-module)
  - [AssignmentStatus](#assignmentstatus)
  - [Comparator](#comparator)
  - [EventType](#eventtype)
  - [HITAccessActions](#hitaccessactions)
  - [HITReviewStatus](#hitreviewstatus)
  - [HITStatus](#hitstatus)
  - [ListAssignmentsForHITPaginatorName](#listassignmentsforhitpaginatorname)
  - [ListBonusPaymentsPaginatorName](#listbonuspaymentspaginatorname)
  - [ListHITsForQualificationTypePaginatorName](#listhitsforqualificationtypepaginatorname)
  - [ListHITsPaginatorName](#listhitspaginatorname)
  - [ListQualificationRequestsPaginatorName](#listqualificationrequestspaginatorname)
  - [ListQualificationTypesPaginatorName](#listqualificationtypespaginatorname)
  - [ListReviewableHITsPaginatorName](#listreviewablehitspaginatorname)
  - [ListWorkerBlocksPaginatorName](#listworkerblockspaginatorname)
  - [ListWorkersWithQualificationTypePaginatorName](#listworkerswithqualificationtypepaginatorname)
  - [NotificationTransport](#notificationtransport)
  - [NotifyWorkersFailureCode](#notifyworkersfailurecode)
  - [QualificationStatus](#qualificationstatus)
  - [QualificationTypeStatus](#qualificationtypestatus)
  - [ReviewActionStatus](#reviewactionstatus)
  - [ReviewPolicyLevel](#reviewpolicylevel)
  - [ReviewableHITStatus](#reviewablehitstatus)

## AssignmentStatus

```python
from mypy_boto3_mturk.literals import AssignmentStatus
```

Values:

- `Approved`
- `Rejected`
- `Submitted`

## Comparator

```python
from mypy_boto3_mturk.literals import Comparator
```

Values:

- `DoesNotExist`
- `EqualTo`
- `Exists`
- `GreaterThan`
- `GreaterThanOrEqualTo`
- `In`
- `LessThan`
- `LessThanOrEqualTo`
- `NotEqualTo`
- `NotIn`

## EventType

```python
from mypy_boto3_mturk.literals import EventType
```

Values:

- `AssignmentAbandoned`
- `AssignmentAccepted`
- `AssignmentApproved`
- `AssignmentRejected`
- `AssignmentReturned`
- `AssignmentSubmitted`
- `HITCreated`
- `HITDisposed`
- `HITExpired`
- `HITExtended`
- `HITReviewable`
- `Ping`

## HITAccessActions

```python
from mypy_boto3_mturk.literals import HITAccessActions
```

Values:

- `Accept`
- `DiscoverPreviewAndAccept`
- `PreviewAndAccept`

## HITReviewStatus

```python
from mypy_boto3_mturk.literals import HITReviewStatus
```

Values:

- `MarkedForReview`
- `NotReviewed`
- `ReviewedAppropriate`
- `ReviewedInappropriate`

## HITStatus

```python
from mypy_boto3_mturk.literals import HITStatus
```

Values:

- `Assignable`
- `Disposed`
- `Reviewable`
- `Reviewing`
- `Unassignable`

## ListAssignmentsForHITPaginatorName

```python
from mypy_boto3_mturk.literals import ListAssignmentsForHITPaginatorName
```

Values:

- `list_assignments_for_hit`

## ListBonusPaymentsPaginatorName

```python
from mypy_boto3_mturk.literals import ListBonusPaymentsPaginatorName
```

Values:

- `list_bonus_payments`

## ListHITsForQualificationTypePaginatorName

```python
from mypy_boto3_mturk.literals import ListHITsForQualificationTypePaginatorName
```

Values:

- `list_hits_for_qualification_type`

## ListHITsPaginatorName

```python
from mypy_boto3_mturk.literals import ListHITsPaginatorName
```

Values:

- `list_hits`

## ListQualificationRequestsPaginatorName

```python
from mypy_boto3_mturk.literals import ListQualificationRequestsPaginatorName
```

Values:

- `list_qualification_requests`

## ListQualificationTypesPaginatorName

```python
from mypy_boto3_mturk.literals import ListQualificationTypesPaginatorName
```

Values:

- `list_qualification_types`

## ListReviewableHITsPaginatorName

```python
from mypy_boto3_mturk.literals import ListReviewableHITsPaginatorName
```

Values:

- `list_reviewable_hits`

## ListWorkerBlocksPaginatorName

```python
from mypy_boto3_mturk.literals import ListWorkerBlocksPaginatorName
```

Values:

- `list_worker_blocks`

## ListWorkersWithQualificationTypePaginatorName

```python
from mypy_boto3_mturk.literals import ListWorkersWithQualificationTypePaginatorName
```

Values:

- `list_workers_with_qualification_type`

## NotificationTransport

```python
from mypy_boto3_mturk.literals import NotificationTransport
```

Values:

- `Email`
- `SNS`
- `SQS`

## NotifyWorkersFailureCode

```python
from mypy_boto3_mturk.literals import NotifyWorkersFailureCode
```

Values:

- `HardFailure`
- `SoftFailure`

## QualificationStatus

```python
from mypy_boto3_mturk.literals import QualificationStatus
```

Values:

- `Granted`
- `Revoked`

## QualificationTypeStatus

```python
from mypy_boto3_mturk.literals import QualificationTypeStatus
```

Values:

- `Active`
- `Inactive`

## ReviewActionStatus

```python
from mypy_boto3_mturk.literals import ReviewActionStatus
```

Values:

- `Cancelled`
- `Failed`
- `Intended`
- `Succeeded`

## ReviewPolicyLevel

```python
from mypy_boto3_mturk.literals import ReviewPolicyLevel
```

Values:

- `Assignment`
- `HIT`

## ReviewableHITStatus

```python
from mypy_boto3_mturk.literals import ReviewableHITStatus
```

Values:

- `Reviewable`
- `Reviewing`
