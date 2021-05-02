# Literals for boto3 Pinpoint module

> [Index](../index.md) > [Pinpoint](./index.md) > Literals

Auto-generated documentation for [Pinpoint](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html#Pinpoint)
type annotations stubs module [mypy_boto3_pinpoint](https://pypi.org/project/mypy-boto3-pinpoint/).

- [Literals for boto3 Pinpoint module](#literals-for-boto3-pinpoint-module)
  - [Action](#action)
  - [AttributeType](#attributetype)
  - [CampaignStatus](#campaignstatus)
  - [ChannelType](#channeltype)
  - [DeliveryStatus](#deliverystatus)
  - [DimensionType](#dimensiontype)
  - [Duration](#duration)
  - [FilterType](#filtertype)
  - [Format](#format)
  - [Frequency](#frequency)
  - [Include](#include)
  - [JobStatus](#jobstatus)
  - [MessageType](#messagetype)
  - [Mode](#mode)
  - [Operator](#operator)
  - [RecencyType](#recencytype)
  - [SegmentType](#segmenttype)
  - [SourceType](#sourcetype)
  - [State](#state)
  - [TemplateType](#templatetype)
  - [TypeType](#typetype)
  - [__EndpointTypesElement](#__endpointtypeselement)

## Action

```python
from mypy_boto3_pinpoint.literals import Action
```

Values:

- `DEEP_LINK`
- `OPEN_APP`
- `URL`

## AttributeType

```python
from mypy_boto3_pinpoint.literals import AttributeType
```

Values:

- `AFTER`
- `BEFORE`
- `BETWEEN`
- `CONTAINS`
- `EXCLUSIVE`
- `INCLUSIVE`
- `ON`

## CampaignStatus

```python
from mypy_boto3_pinpoint.literals import CampaignStatus
```

Values:

- `COMPLETED`
- `DELETED`
- `EXECUTING`
- `INVALID`
- `PAUSED`
- `PENDING_NEXT_RUN`
- `SCHEDULED`

## ChannelType

```python
from mypy_boto3_pinpoint.literals import ChannelType
```

Values:

- `ADM`
- `APNS`
- `APNS_SANDBOX`
- `APNS_VOIP`
- `APNS_VOIP_SANDBOX`
- `BAIDU`
- `CUSTOM`
- `EMAIL`
- `GCM`
- `PUSH`
- `SMS`
- `VOICE`

## DeliveryStatus

```python
from mypy_boto3_pinpoint.literals import DeliveryStatus
```

Values:

- `DUPLICATE`
- `OPT_OUT`
- `PERMANENT_FAILURE`
- `SUCCESSFUL`
- `TEMPORARY_FAILURE`
- `THROTTLED`
- `UNKNOWN_FAILURE`

## DimensionType

```python
from mypy_boto3_pinpoint.literals import DimensionType
```

Values:

- `EXCLUSIVE`
- `INCLUSIVE`

## Duration

```python
from mypy_boto3_pinpoint.literals import Duration
```

Values:

- `DAY_14`
- `DAY_30`
- `DAY_7`
- `HR_24`

## FilterType

```python
from mypy_boto3_pinpoint.literals import FilterType
```

Values:

- `ENDPOINT`
- `SYSTEM`

## Format

```python
from mypy_boto3_pinpoint.literals import Format
```

Values:

- `CSV`
- `JSON`

## Frequency

```python
from mypy_boto3_pinpoint.literals import Frequency
```

Values:

- `DAILY`
- `EVENT`
- `HOURLY`
- `MONTHLY`
- `ONCE`
- `WEEKLY`

## Include

```python
from mypy_boto3_pinpoint.literals import Include
```

Values:

- `ALL`
- `ANY`
- `NONE`

## JobStatus

```python
from mypy_boto3_pinpoint.literals import JobStatus
```

Values:

- `COMPLETED`
- `COMPLETING`
- `CREATED`
- `FAILED`
- `FAILING`
- `INITIALIZING`
- `PENDING_JOB`
- `PREPARING_FOR_INITIALIZATION`
- `PROCESSING`

## MessageType

```python
from mypy_boto3_pinpoint.literals import MessageType
```

Values:

- `PROMOTIONAL`
- `TRANSACTIONAL`

## Mode

```python
from mypy_boto3_pinpoint.literals import Mode
```

Values:

- `DELIVERY`
- `FILTER`

## Operator

```python
from mypy_boto3_pinpoint.literals import Operator
```

Values:

- `ALL`
- `ANY`

## RecencyType

```python
from mypy_boto3_pinpoint.literals import RecencyType
```

Values:

- `ACTIVE`
- `INACTIVE`

## SegmentType

```python
from mypy_boto3_pinpoint.literals import SegmentType
```

Values:

- `DIMENSIONAL`
- `IMPORT`

## SourceType

```python
from mypy_boto3_pinpoint.literals import SourceType
```

Values:

- `ALL`
- `ANY`
- `NONE`

## State

```python
from mypy_boto3_pinpoint.literals import State
```

Values:

- `ACTIVE`
- `CANCELLED`
- `CLOSED`
- `COMPLETED`
- `DRAFT`
- `PAUSED`

## TemplateType

```python
from mypy_boto3_pinpoint.literals import TemplateType
```

Values:

- `EMAIL`
- `PUSH`
- `SMS`
- `VOICE`

## TypeType

```python
from mypy_boto3_pinpoint.literals import TypeType
```

Values:

- `ALL`
- `ANY`
- `NONE`

## __EndpointTypesElement

```python
from mypy_boto3_pinpoint.literals import __EndpointTypesElement
```

Values:

- `ADM`
- `APNS`
- `APNS_SANDBOX`
- `APNS_VOIP`
- `APNS_VOIP_SANDBOX`
- `BAIDU`
- `CUSTOM`
- `EMAIL`
- `GCM`
- `PUSH`
- `SMS`
- `VOICE`
