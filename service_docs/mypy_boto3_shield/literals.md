# Literals for boto3 Shield module

> [Index](../index.md) > [Shield](./index.md) > Literals

Auto-generated documentation for [Shield](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield)
type annotations stubs module [mypy_boto3_shield](https://pypi.org/project/mypy-boto3-shield/).

- [Literals for boto3 Shield module](#literals-for-boto3-shield-module)
  - [AttackLayer](#attacklayer)
  - [AttackPropertyIdentifier](#attackpropertyidentifier)
  - [AutoRenew](#autorenew)
  - [ListAttacksPaginatorName](#listattackspaginatorname)
  - [ListProtectionsPaginatorName](#listprotectionspaginatorname)
  - [ProactiveEngagementStatus](#proactiveengagementstatus)
  - [ProtectedResourceType](#protectedresourcetype)
  - [ProtectionGroupAggregation](#protectiongroupaggregation)
  - [ProtectionGroupPattern](#protectiongrouppattern)
  - [SubResourceType](#subresourcetype)
  - [SubscriptionState](#subscriptionstate)
  - [Unit](#unit)

## AttackLayer

```python
from mypy_boto3_shield.literals import AttackLayer
```

Values:

- `APPLICATION`
- `NETWORK`

## AttackPropertyIdentifier

```python
from mypy_boto3_shield.literals import AttackPropertyIdentifier
```

Values:

- `DESTINATION_URL`
- `REFERRER`
- `SOURCE_ASN`
- `SOURCE_COUNTRY`
- `SOURCE_IP_ADDRESS`
- `SOURCE_USER_AGENT`
- `WORDPRESS_PINGBACK_REFLECTOR`
- `WORDPRESS_PINGBACK_SOURCE`

## AutoRenew

```python
from mypy_boto3_shield.literals import AutoRenew
```

Values:

- `DISABLED`
- `ENABLED`

## ListAttacksPaginatorName

```python
from mypy_boto3_shield.literals import ListAttacksPaginatorName
```

Values:

- `list_attacks`

## ListProtectionsPaginatorName

```python
from mypy_boto3_shield.literals import ListProtectionsPaginatorName
```

Values:

- `list_protections`

## ProactiveEngagementStatus

```python
from mypy_boto3_shield.literals import ProactiveEngagementStatus
```

Values:

- `DISABLED`
- `ENABLED`
- `PENDING`

## ProtectedResourceType

```python
from mypy_boto3_shield.literals import ProtectedResourceType
```

Values:

- `APPLICATION_LOAD_BALANCER`
- `CLASSIC_LOAD_BALANCER`
- `CLOUDFRONT_DISTRIBUTION`
- `ELASTIC_IP_ALLOCATION`
- `GLOBAL_ACCELERATOR`
- `ROUTE_53_HOSTED_ZONE`

## ProtectionGroupAggregation

```python
from mypy_boto3_shield.literals import ProtectionGroupAggregation
```

Values:

- `MAX`
- `MEAN`
- `SUM`

## ProtectionGroupPattern

```python
from mypy_boto3_shield.literals import ProtectionGroupPattern
```

Values:

- `ALL`
- `ARBITRARY`
- `BY_RESOURCE_TYPE`

## SubResourceType

```python
from mypy_boto3_shield.literals import SubResourceType
```

Values:

- `IP`
- `URL`

## SubscriptionState

```python
from mypy_boto3_shield.literals import SubscriptionState
```

Values:

- `ACTIVE`
- `INACTIVE`

## Unit

```python
from mypy_boto3_shield.literals import Unit
```

Values:

- `BITS`
- `BYTES`
- `PACKETS`
- `REQUESTS`
