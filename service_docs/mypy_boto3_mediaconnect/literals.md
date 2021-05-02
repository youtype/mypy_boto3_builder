# Literals for boto3 MediaConnect module

> [Index](../index.md) > [MediaConnect](./index.md) > Literals

Auto-generated documentation for [MediaConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html#MediaConnect)
type annotations stubs module [mypy_boto3_mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/).

- [Literals for boto3 MediaConnect module](#literals-for-boto3-mediaconnect-module)
  - [Algorithm](#algorithm)
  - [DurationUnits](#durationunits)
  - [EntitlementStatus](#entitlementstatus)
  - [FlowActiveWaiterName](#flowactivewaitername)
  - [FlowDeletedWaiterName](#flowdeletedwaitername)
  - [FlowStandbyWaiterName](#flowstandbywaitername)
  - [KeyType](#keytype)
  - [ListEntitlementsPaginatorName](#listentitlementspaginatorname)
  - [ListFlowsPaginatorName](#listflowspaginatorname)
  - [ListOfferingsPaginatorName](#listofferingspaginatorname)
  - [ListReservationsPaginatorName](#listreservationspaginatorname)
  - [PriceUnits](#priceunits)
  - [ProtocolType](#protocoltype)
  - [ReservationState](#reservationstate)
  - [ResourceType](#resourcetype)
  - [SourceType](#sourcetype)
  - [State](#state)
  - [Status](#status)

## Algorithm

```python
from mypy_boto3_mediaconnect.literals import Algorithm
```

Values:

- `aes128`
- `aes192`
- `aes256`

## DurationUnits

```python
from mypy_boto3_mediaconnect.literals import DurationUnits
```

Values:

- `MONTHS`

## EntitlementStatus

```python
from mypy_boto3_mediaconnect.literals import EntitlementStatus
```

Values:

- `DISABLED`
- `ENABLED`

## FlowActiveWaiterName

```python
from mypy_boto3_mediaconnect.literals import FlowActiveWaiterName
```

Values:

- `flow_active`

## FlowDeletedWaiterName

```python
from mypy_boto3_mediaconnect.literals import FlowDeletedWaiterName
```

Values:

- `flow_deleted`

## FlowStandbyWaiterName

```python
from mypy_boto3_mediaconnect.literals import FlowStandbyWaiterName
```

Values:

- `flow_standby`

## KeyType

```python
from mypy_boto3_mediaconnect.literals import KeyType
```

Values:

- `speke`
- `srt-password`
- `static-key`

## ListEntitlementsPaginatorName

```python
from mypy_boto3_mediaconnect.literals import ListEntitlementsPaginatorName
```

Values:

- `list_entitlements`

## ListFlowsPaginatorName

```python
from mypy_boto3_mediaconnect.literals import ListFlowsPaginatorName
```

Values:

- `list_flows`

## ListOfferingsPaginatorName

```python
from mypy_boto3_mediaconnect.literals import ListOfferingsPaginatorName
```

Values:

- `list_offerings`

## ListReservationsPaginatorName

```python
from mypy_boto3_mediaconnect.literals import ListReservationsPaginatorName
```

Values:

- `list_reservations`

## PriceUnits

```python
from mypy_boto3_mediaconnect.literals import PriceUnits
```

Values:

- `HOURLY`

## ProtocolType

```python
from mypy_boto3_mediaconnect.literals import ProtocolType
```

Values:

- `rist`
- `rtp`
- `rtp-fec`
- `srt-listener`
- `zixi-pull`
- `zixi-push`

## ReservationState

```python
from mypy_boto3_mediaconnect.literals import ReservationState
```

Values:

- `ACTIVE`
- `CANCELED`
- `EXPIRED`
- `PROCESSING`

## ResourceType

```python
from mypy_boto3_mediaconnect.literals import ResourceType
```

Values:

- `Mbps_Outbound_Bandwidth`

## SourceType

```python
from mypy_boto3_mediaconnect.literals import SourceType
```

Values:

- `ENTITLED`
- `OWNED`

## State

```python
from mypy_boto3_mediaconnect.literals import State
```

Values:

- `DISABLED`
- `ENABLED`

## Status

```python
from mypy_boto3_mediaconnect.literals import Status
```

Values:

- `ACTIVE`
- `DELETING`
- `ERROR`
- `STANDBY`
- `STARTING`
- `STOPPING`
- `UPDATING`
