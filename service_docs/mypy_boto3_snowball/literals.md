# Literals for boto3 Snowball module

> [Index](../index.md) > [Snowball](./index.md) > Literals

Auto-generated documentation for [Snowball](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html#Snowball)
type annotations stubs module [mypy_boto3_snowball](https://pypi.org/project/mypy-boto3-snowball/).

- [Literals for boto3 Snowball module](#literals-for-boto3-snowball-module)
  - [ClusterState](#clusterstate)
  - [DescribeAddressesPaginatorName](#describeaddressespaginatorname)
  - [JobState](#jobstate)
  - [JobType](#jobtype)
  - [ListClusterJobsPaginatorName](#listclusterjobspaginatorname)
  - [ListClustersPaginatorName](#listclusterspaginatorname)
  - [ListCompatibleImagesPaginatorName](#listcompatibleimagespaginatorname)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [ShipmentState](#shipmentstate)
  - [ShippingLabelStatus](#shippinglabelstatus)
  - [ShippingOption](#shippingoption)
  - [SnowballCapacity](#snowballcapacity)
  - [SnowballType](#snowballtype)

## ClusterState

```python
from mypy_boto3_snowball.literals import ClusterState
```

Values:

- `AwaitingQuorum`
- `Cancelled`
- `Complete`
- `InUse`
- `Pending`

## DescribeAddressesPaginatorName

```python
from mypy_boto3_snowball.literals import DescribeAddressesPaginatorName
```

Values:

- `describe_addresses`

## JobState

```python
from mypy_boto3_snowball.literals import JobState
```

Values:

- `Cancelled`
- `Complete`
- `InProgress`
- `InTransitToAWS`
- `InTransitToCustomer`
- `Listing`
- `New`
- `Pending`
- `PreparingAppliance`
- `PreparingShipment`
- `WithAWS`
- `WithAWSSortingFacility`
- `WithCustomer`

## JobType

```python
from mypy_boto3_snowball.literals import JobType
```

Values:

- `EXPORT`
- `IMPORT`
- `LOCAL_USE`

## ListClusterJobsPaginatorName

```python
from mypy_boto3_snowball.literals import ListClusterJobsPaginatorName
```

Values:

- `list_cluster_jobs`

## ListClustersPaginatorName

```python
from mypy_boto3_snowball.literals import ListClustersPaginatorName
```

Values:

- `list_clusters`

## ListCompatibleImagesPaginatorName

```python
from mypy_boto3_snowball.literals import ListCompatibleImagesPaginatorName
```

Values:

- `list_compatible_images`

## ListJobsPaginatorName

```python
from mypy_boto3_snowball.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## ShipmentState

```python
from mypy_boto3_snowball.literals import ShipmentState
```

Values:

- `RECEIVED`
- `RETURNED`

## ShippingLabelStatus

```python
from mypy_boto3_snowball.literals import ShippingLabelStatus
```

Values:

- `Failed`
- `InProgress`
- `Succeeded`
- `TimedOut`

## ShippingOption

```python
from mypy_boto3_snowball.literals import ShippingOption
```

Values:

- `EXPRESS`
- `NEXT_DAY`
- `SECOND_DAY`
- `STANDARD`

## SnowballCapacity

```python
from mypy_boto3_snowball.literals import SnowballCapacity
```

Values:

- `NoPreference`
- `T100`
- `T42`
- `T50`
- `T8`
- `T80`
- `T98`

## SnowballType

```python
from mypy_boto3_snowball.literals import SnowballType
```

Values:

- `EDGE`
- `EDGE_C`
- `EDGE_CG`
- `EDGE_S`
- `SNC1_HDD`
- `STANDARD`
