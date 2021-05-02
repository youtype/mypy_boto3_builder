# Literals for boto3 SESV2 module

> [Index](../index.md) > [SESV2](./index.md) > Literals

Auto-generated documentation for [SESV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html#SESV2)
type annotations stubs module [mypy_boto3_sesv2](https://pypi.org/project/mypy-boto3-sesv2/).

- [Literals for boto3 SESV2 module](#literals-for-boto3-sesv2-module)
  - [BehaviorOnMxFailure](#behavioronmxfailure)
  - [BulkEmailStatus](#bulkemailstatus)
  - [ContactLanguage](#contactlanguage)
  - [ContactListImportAction](#contactlistimportaction)
  - [DataFormat](#dataformat)
  - [DeliverabilityDashboardAccountStatus](#deliverabilitydashboardaccountstatus)
  - [DeliverabilityTestStatus](#deliverabilityteststatus)
  - [DimensionValueSource](#dimensionvaluesource)
  - [DkimSigningAttributesOrigin](#dkimsigningattributesorigin)
  - [DkimStatus](#dkimstatus)
  - [EventType](#eventtype)
  - [IdentityType](#identitytype)
  - [ImportDestinationType](#importdestinationtype)
  - [JobStatus](#jobstatus)
  - [MailFromDomainStatus](#mailfromdomainstatus)
  - [MailType](#mailtype)
  - [ReviewStatus](#reviewstatus)
  - [SubscriptionStatus](#subscriptionstatus)
  - [SuppressionListImportAction](#suppressionlistimportaction)
  - [SuppressionListReason](#suppressionlistreason)
  - [TlsPolicy](#tlspolicy)
  - [WarmupStatus](#warmupstatus)

## BehaviorOnMxFailure

```python
from mypy_boto3_sesv2.literals import BehaviorOnMxFailure
```

Values:

- `REJECT_MESSAGE`
- `USE_DEFAULT_VALUE`

## BulkEmailStatus

```python
from mypy_boto3_sesv2.literals import BulkEmailStatus
```

Values:

- `ACCOUNT_DAILY_QUOTA_EXCEEDED`
- `ACCOUNT_SENDING_PAUSED`
- `ACCOUNT_SUSPENDED`
- `ACCOUNT_THROTTLED`
- `CONFIGURATION_SET_NOT_FOUND`
- `CONFIGURATION_SET_SENDING_PAUSED`
- `FAILED`
- `INVALID_PARAMETER`
- `INVALID_SENDING_POOL_NAME`
- `MAIL_FROM_DOMAIN_NOT_VERIFIED`
- `MESSAGE_REJECTED`
- `SUCCESS`
- `TEMPLATE_NOT_FOUND`
- `TRANSIENT_FAILURE`

## ContactLanguage

```python
from mypy_boto3_sesv2.literals import ContactLanguage
```

Values:

- `EN`
- `JA`

## ContactListImportAction

```python
from mypy_boto3_sesv2.literals import ContactListImportAction
```

Values:

- `DELETE`
- `PUT`

## DataFormat

```python
from mypy_boto3_sesv2.literals import DataFormat
```

Values:

- `CSV`
- `JSON`

## DeliverabilityDashboardAccountStatus

```python
from mypy_boto3_sesv2.literals import DeliverabilityDashboardAccountStatus
```

Values:

- `ACTIVE`
- `DISABLED`
- `PENDING_EXPIRATION`

## DeliverabilityTestStatus

```python
from mypy_boto3_sesv2.literals import DeliverabilityTestStatus
```

Values:

- `COMPLETED`
- `IN_PROGRESS`

## DimensionValueSource

```python
from mypy_boto3_sesv2.literals import DimensionValueSource
```

Values:

- `EMAIL_HEADER`
- `LINK_TAG`
- `MESSAGE_TAG`

## DkimSigningAttributesOrigin

```python
from mypy_boto3_sesv2.literals import DkimSigningAttributesOrigin
```

Values:

- `AWS_SES`
- `EXTERNAL`

## DkimStatus

```python
from mypy_boto3_sesv2.literals import DkimStatus
```

Values:

- `FAILED`
- `NOT_STARTED`
- `PENDING`
- `SUCCESS`
- `TEMPORARY_FAILURE`

## EventType

```python
from mypy_boto3_sesv2.literals import EventType
```

Values:

- `BOUNCE`
- `CLICK`
- `COMPLAINT`
- `DELIVERY`
- `DELIVERY_DELAY`
- `OPEN`
- `REJECT`
- `RENDERING_FAILURE`
- `SEND`
- `SUBSCRIPTION`

## IdentityType

```python
from mypy_boto3_sesv2.literals import IdentityType
```

Values:

- `DOMAIN`
- `EMAIL_ADDRESS`
- `MANAGED_DOMAIN`

## ImportDestinationType

```python
from mypy_boto3_sesv2.literals import ImportDestinationType
```

Values:

- `CONTACT_LIST`
- `SUPPRESSION_LIST`

## JobStatus

```python
from mypy_boto3_sesv2.literals import JobStatus
```

Values:

- `COMPLETED`
- `CREATED`
- `FAILED`
- `PROCESSING`

## MailFromDomainStatus

```python
from mypy_boto3_sesv2.literals import MailFromDomainStatus
```

Values:

- `FAILED`
- `PENDING`
- `SUCCESS`
- `TEMPORARY_FAILURE`

## MailType

```python
from mypy_boto3_sesv2.literals import MailType
```

Values:

- `MARKETING`
- `TRANSACTIONAL`

## ReviewStatus

```python
from mypy_boto3_sesv2.literals import ReviewStatus
```

Values:

- `DENIED`
- `FAILED`
- `GRANTED`
- `PENDING`

## SubscriptionStatus

```python
from mypy_boto3_sesv2.literals import SubscriptionStatus
```

Values:

- `OPT_IN`
- `OPT_OUT`

## SuppressionListImportAction

```python
from mypy_boto3_sesv2.literals import SuppressionListImportAction
```

Values:

- `DELETE`
- `PUT`

## SuppressionListReason

```python
from mypy_boto3_sesv2.literals import SuppressionListReason
```

Values:

- `BOUNCE`
- `COMPLAINT`

## TlsPolicy

```python
from mypy_boto3_sesv2.literals import TlsPolicy
```

Values:

- `OPTIONAL`
- `REQUIRE`

## WarmupStatus

```python
from mypy_boto3_sesv2.literals import WarmupStatus
```

Values:

- `DONE`
- `IN_PROGRESS`
