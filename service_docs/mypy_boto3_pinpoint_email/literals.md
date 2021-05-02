# Literals for boto3 PinpointEmail module

> [Index](../index.md) > [PinpointEmail](./index.md) > Literals

Auto-generated documentation for [PinpointEmail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html#PinpointEmail)
type annotations stubs module [mypy_boto3_pinpoint_email](https://pypi.org/project/mypy-boto3-pinpoint-email/).

- [Literals for boto3 PinpointEmail module](#literals-for-boto3-pinpointemail-module)
  - [BehaviorOnMxFailure](#behavioronmxfailure)
  - [DeliverabilityDashboardAccountStatus](#deliverabilitydashboardaccountstatus)
  - [DeliverabilityTestStatus](#deliverabilityteststatus)
  - [DimensionValueSource](#dimensionvaluesource)
  - [DkimStatus](#dkimstatus)
  - [EventType](#eventtype)
  - [GetDedicatedIpsPaginatorName](#getdedicatedipspaginatorname)
  - [IdentityType](#identitytype)
  - [ListConfigurationSetsPaginatorName](#listconfigurationsetspaginatorname)
  - [ListDedicatedIpPoolsPaginatorName](#listdedicatedippoolspaginatorname)
  - [ListDeliverabilityTestReportsPaginatorName](#listdeliverabilitytestreportspaginatorname)
  - [ListEmailIdentitiesPaginatorName](#listemailidentitiespaginatorname)
  - [MailFromDomainStatus](#mailfromdomainstatus)
  - [TlsPolicy](#tlspolicy)
  - [WarmupStatus](#warmupstatus)

## BehaviorOnMxFailure

```python
from mypy_boto3_pinpoint_email.literals import BehaviorOnMxFailure
```

Values:

- `REJECT_MESSAGE`
- `USE_DEFAULT_VALUE`

## DeliverabilityDashboardAccountStatus

```python
from mypy_boto3_pinpoint_email.literals import DeliverabilityDashboardAccountStatus
```

Values:

- `ACTIVE`
- `DISABLED`
- `PENDING_EXPIRATION`

## DeliverabilityTestStatus

```python
from mypy_boto3_pinpoint_email.literals import DeliverabilityTestStatus
```

Values:

- `COMPLETED`
- `IN_PROGRESS`

## DimensionValueSource

```python
from mypy_boto3_pinpoint_email.literals import DimensionValueSource
```

Values:

- `EMAIL_HEADER`
- `LINK_TAG`
- `MESSAGE_TAG`

## DkimStatus

```python
from mypy_boto3_pinpoint_email.literals import DkimStatus
```

Values:

- `FAILED`
- `NOT_STARTED`
- `PENDING`
- `SUCCESS`
- `TEMPORARY_FAILURE`

## EventType

```python
from mypy_boto3_pinpoint_email.literals import EventType
```

Values:

- `BOUNCE`
- `CLICK`
- `COMPLAINT`
- `DELIVERY`
- `OPEN`
- `REJECT`
- `RENDERING_FAILURE`
- `SEND`

## GetDedicatedIpsPaginatorName

```python
from mypy_boto3_pinpoint_email.literals import GetDedicatedIpsPaginatorName
```

Values:

- `get_dedicated_ips`

## IdentityType

```python
from mypy_boto3_pinpoint_email.literals import IdentityType
```

Values:

- `DOMAIN`
- `EMAIL_ADDRESS`
- `MANAGED_DOMAIN`

## ListConfigurationSetsPaginatorName

```python
from mypy_boto3_pinpoint_email.literals import ListConfigurationSetsPaginatorName
```

Values:

- `list_configuration_sets`

## ListDedicatedIpPoolsPaginatorName

```python
from mypy_boto3_pinpoint_email.literals import ListDedicatedIpPoolsPaginatorName
```

Values:

- `list_dedicated_ip_pools`

## ListDeliverabilityTestReportsPaginatorName

```python
from mypy_boto3_pinpoint_email.literals import ListDeliverabilityTestReportsPaginatorName
```

Values:

- `list_deliverability_test_reports`

## ListEmailIdentitiesPaginatorName

```python
from mypy_boto3_pinpoint_email.literals import ListEmailIdentitiesPaginatorName
```

Values:

- `list_email_identities`

## MailFromDomainStatus

```python
from mypy_boto3_pinpoint_email.literals import MailFromDomainStatus
```

Values:

- `FAILED`
- `PENDING`
- `SUCCESS`
- `TEMPORARY_FAILURE`

## TlsPolicy

```python
from mypy_boto3_pinpoint_email.literals import TlsPolicy
```

Values:

- `OPTIONAL`
- `REQUIRE`

## WarmupStatus

```python
from mypy_boto3_pinpoint_email.literals import WarmupStatus
```

Values:

- `DONE`
- `IN_PROGRESS`
