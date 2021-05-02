# Literals for boto3 SES module

> [Index](../index.md) > [SES](./index.md) > Literals

Auto-generated documentation for [SES](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES)
type annotations stubs module [mypy_boto3_ses](https://pypi.org/project/mypy-boto3-ses/).

- [Literals for boto3 SES module](#literals-for-boto3-ses-module)
  - [BehaviorOnMXFailure](#behavioronmxfailure)
  - [BounceType](#bouncetype)
  - [BulkEmailStatus](#bulkemailstatus)
  - [ConfigurationSetAttribute](#configurationsetattribute)
  - [CustomMailFromStatus](#custommailfromstatus)
  - [DimensionValueSource](#dimensionvaluesource)
  - [DsnAction](#dsnaction)
  - [EventType](#eventtype)
  - [IdentityExistsWaiterName](#identityexistswaitername)
  - [IdentityType](#identitytype)
  - [InvocationType](#invocationtype)
  - [ListConfigurationSetsPaginatorName](#listconfigurationsetspaginatorname)
  - [ListCustomVerificationEmailTemplatesPaginatorName](#listcustomverificationemailtemplatespaginatorname)
  - [ListIdentitiesPaginatorName](#listidentitiespaginatorname)
  - [ListReceiptRuleSetsPaginatorName](#listreceiptrulesetspaginatorname)
  - [ListTemplatesPaginatorName](#listtemplatespaginatorname)
  - [NotificationType](#notificationtype)
  - [ReceiptFilterPolicy](#receiptfilterpolicy)
  - [SNSActionEncoding](#snsactionencoding)
  - [StopScope](#stopscope)
  - [TlsPolicy](#tlspolicy)
  - [VerificationStatus](#verificationstatus)

## BehaviorOnMXFailure

```python
from mypy_boto3_ses.literals import BehaviorOnMXFailure
```

Values:

- `RejectMessage`
- `UseDefaultValue`

## BounceType

```python
from mypy_boto3_ses.literals import BounceType
```

Values:

- `ContentRejected`
- `DoesNotExist`
- `ExceededQuota`
- `MessageTooLarge`
- `TemporaryFailure`
- `Undefined`

## BulkEmailStatus

```python
from mypy_boto3_ses.literals import BulkEmailStatus
```

Values:

- `AccountDailyQuotaExceeded`
- `AccountSendingPaused`
- `AccountSuspended`
- `AccountThrottled`
- `ConfigurationSetDoesNotExist`
- `ConfigurationSetSendingPaused`
- `Failed`
- `InvalidParameterValue`
- `InvalidSendingPoolName`
- `MailFromDomainNotVerified`
- `MessageRejected`
- `Success`
- `TemplateDoesNotExist`
- `TransientFailure`

## ConfigurationSetAttribute

```python
from mypy_boto3_ses.literals import ConfigurationSetAttribute
```

Values:

- `deliveryOptions`
- `eventDestinations`
- `reputationOptions`
- `trackingOptions`

## CustomMailFromStatus

```python
from mypy_boto3_ses.literals import CustomMailFromStatus
```

Values:

- `Failed`
- `Pending`
- `Success`
- `TemporaryFailure`

## DimensionValueSource

```python
from mypy_boto3_ses.literals import DimensionValueSource
```

Values:

- `emailHeader`
- `linkTag`
- `messageTag`

## DsnAction

```python
from mypy_boto3_ses.literals import DsnAction
```

Values:

- `delayed`
- `delivered`
- `expanded`
- `failed`
- `relayed`

## EventType

```python
from mypy_boto3_ses.literals import EventType
```

Values:

- `bounce`
- `click`
- `complaint`
- `delivery`
- `open`
- `reject`
- `renderingFailure`
- `send`

## IdentityExistsWaiterName

```python
from mypy_boto3_ses.literals import IdentityExistsWaiterName
```

Values:

- `identity_exists`

## IdentityType

```python
from mypy_boto3_ses.literals import IdentityType
```

Values:

- `Domain`
- `EmailAddress`

## InvocationType

```python
from mypy_boto3_ses.literals import InvocationType
```

Values:

- `Event`
- `RequestResponse`

## ListConfigurationSetsPaginatorName

```python
from mypy_boto3_ses.literals import ListConfigurationSetsPaginatorName
```

Values:

- `list_configuration_sets`

## ListCustomVerificationEmailTemplatesPaginatorName

```python
from mypy_boto3_ses.literals import ListCustomVerificationEmailTemplatesPaginatorName
```

Values:

- `list_custom_verification_email_templates`

## ListIdentitiesPaginatorName

```python
from mypy_boto3_ses.literals import ListIdentitiesPaginatorName
```

Values:

- `list_identities`

## ListReceiptRuleSetsPaginatorName

```python
from mypy_boto3_ses.literals import ListReceiptRuleSetsPaginatorName
```

Values:

- `list_receipt_rule_sets`

## ListTemplatesPaginatorName

```python
from mypy_boto3_ses.literals import ListTemplatesPaginatorName
```

Values:

- `list_templates`

## NotificationType

```python
from mypy_boto3_ses.literals import NotificationType
```

Values:

- `Bounce`
- `Complaint`
- `Delivery`

## ReceiptFilterPolicy

```python
from mypy_boto3_ses.literals import ReceiptFilterPolicy
```

Values:

- `Allow`
- `Block`

## SNSActionEncoding

```python
from mypy_boto3_ses.literals import SNSActionEncoding
```

Values:

- `Base64`
- `UTF-8`

## StopScope

```python
from mypy_boto3_ses.literals import StopScope
```

Values:

- `RuleSet`

## TlsPolicy

```python
from mypy_boto3_ses.literals import TlsPolicy
```

Values:

- `Optional`
- `Require`

## VerificationStatus

```python
from mypy_boto3_ses.literals import VerificationStatus
```

Values:

- `Failed`
- `NotStarted`
- `Pending`
- `Success`
- `TemporaryFailure`
