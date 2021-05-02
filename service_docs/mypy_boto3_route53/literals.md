# Literals for boto3 Route53 module

> [Index](../index.md) > [Route53](./index.md) > Literals

Auto-generated documentation for [Route53](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53)
type annotations stubs module [mypy_boto3_route53](https://pypi.org/project/mypy-boto3-route53/).

- [Literals for boto3 Route53 module](#literals-for-boto3-route53-module)
  - [AccountLimitType](#accountlimittype)
  - [ChangeAction](#changeaction)
  - [ChangeStatus](#changestatus)
  - [CloudWatchRegion](#cloudwatchregion)
  - [ComparisonOperator](#comparisonoperator)
  - [HealthCheckRegion](#healthcheckregion)
  - [HealthCheckType](#healthchecktype)
  - [HostedZoneLimitType](#hostedzonelimittype)
  - [InsufficientDataHealthStatus](#insufficientdatahealthstatus)
  - [ListHealthChecksPaginatorName](#listhealthcheckspaginatorname)
  - [ListHostedZonesPaginatorName](#listhostedzonespaginatorname)
  - [ListQueryLoggingConfigsPaginatorName](#listqueryloggingconfigspaginatorname)
  - [ListResourceRecordSetsPaginatorName](#listresourcerecordsetspaginatorname)
  - [ListVPCAssociationAuthorizationsPaginatorName](#listvpcassociationauthorizationspaginatorname)
  - [RRType](#rrtype)
  - [ResettableElementName](#resettableelementname)
  - [ResourceRecordSetFailover](#resourcerecordsetfailover)
  - [ResourceRecordSetRegion](#resourcerecordsetregion)
  - [ResourceRecordSetsChangedWaiterName](#resourcerecordsetschangedwaitername)
  - [ReusableDelegationSetLimitType](#reusabledelegationsetlimittype)
  - [Statistic](#statistic)
  - [TagResourceType](#tagresourcetype)
  - [VPCRegion](#vpcregion)

## AccountLimitType

```python
from mypy_boto3_route53.literals import AccountLimitType
```

Values:

- `MAX_HEALTH_CHECKS_BY_OWNER`
- `MAX_HOSTED_ZONES_BY_OWNER`
- `MAX_REUSABLE_DELEGATION_SETS_BY_OWNER`
- `MAX_TRAFFIC_POLICIES_BY_OWNER`
- `MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER`

## ChangeAction

```python
from mypy_boto3_route53.literals import ChangeAction
```

Values:

- `CREATE`
- `DELETE`
- `UPSERT`

## ChangeStatus

```python
from mypy_boto3_route53.literals import ChangeStatus
```

Values:

- `INSYNC`
- `PENDING`

## CloudWatchRegion

```python
from mypy_boto3_route53.literals import CloudWatchRegion
```

Values:

- `af-south-1`
- `ap-east-1`
- `ap-northeast-1`
- `ap-northeast-2`
- `ap-northeast-3`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ca-central-1`
- `cn-north-1`
- `cn-northwest-1`
- `eu-central-1`
- `eu-north-1`
- `eu-south-1`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `me-south-1`
- `sa-east-1`
- `us-east-1`
- `us-east-2`
- `us-gov-east-1`
- `us-gov-west-1`
- `us-iso-east-1`
- `us-isob-east-1`
- `us-west-1`
- `us-west-2`

## ComparisonOperator

```python
from mypy_boto3_route53.literals import ComparisonOperator
```

Values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanOrEqualToThreshold`
- `LessThanThreshold`

## HealthCheckRegion

```python
from mypy_boto3_route53.literals import HealthCheckRegion
```

Values:

- `ap-northeast-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `eu-west-1`
- `sa-east-1`
- `us-east-1`
- `us-west-1`
- `us-west-2`

## HealthCheckType

```python
from mypy_boto3_route53.literals import HealthCheckType
```

Values:

- `CALCULATED`
- `CLOUDWATCH_METRIC`
- `HTTP`
- `HTTP_STR_MATCH`
- `HTTPS`
- `HTTPS_STR_MATCH`
- `TCP`

## HostedZoneLimitType

```python
from mypy_boto3_route53.literals import HostedZoneLimitType
```

Values:

- `MAX_RRSETS_BY_ZONE`
- `MAX_VPCS_ASSOCIATED_BY_ZONE`

## InsufficientDataHealthStatus

```python
from mypy_boto3_route53.literals import InsufficientDataHealthStatus
```

Values:

- `Healthy`
- `LastKnownStatus`
- `Unhealthy`

## ListHealthChecksPaginatorName

```python
from mypy_boto3_route53.literals import ListHealthChecksPaginatorName
```

Values:

- `list_health_checks`

## ListHostedZonesPaginatorName

```python
from mypy_boto3_route53.literals import ListHostedZonesPaginatorName
```

Values:

- `list_hosted_zones`

## ListQueryLoggingConfigsPaginatorName

```python
from mypy_boto3_route53.literals import ListQueryLoggingConfigsPaginatorName
```

Values:

- `list_query_logging_configs`

## ListResourceRecordSetsPaginatorName

```python
from mypy_boto3_route53.literals import ListResourceRecordSetsPaginatorName
```

Values:

- `list_resource_record_sets`

## ListVPCAssociationAuthorizationsPaginatorName

```python
from mypy_boto3_route53.literals import ListVPCAssociationAuthorizationsPaginatorName
```

Values:

- `list_vpc_association_authorizations`

## RRType

```python
from mypy_boto3_route53.literals import RRType
```

Values:

- `A`
- `AAAA`
- `CAA`
- `CNAME`
- `DS`
- `MX`
- `NAPTR`
- `NS`
- `PTR`
- `SOA`
- `SPF`
- `SRV`
- `TXT`

## ResettableElementName

```python
from mypy_boto3_route53.literals import ResettableElementName
```

Values:

- `ChildHealthChecks`
- `FullyQualifiedDomainName`
- `Regions`
- `ResourcePath`

## ResourceRecordSetFailover

```python
from mypy_boto3_route53.literals import ResourceRecordSetFailover
```

Values:

- `PRIMARY`
- `SECONDARY`

## ResourceRecordSetRegion

```python
from mypy_boto3_route53.literals import ResourceRecordSetRegion
```

Values:

- `af-south-1`
- `ap-east-1`
- `ap-northeast-1`
- `ap-northeast-2`
- `ap-northeast-3`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ca-central-1`
- `cn-north-1`
- `cn-northwest-1`
- `eu-central-1`
- `eu-north-1`
- `eu-south-1`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `me-south-1`
- `sa-east-1`
- `us-east-1`
- `us-east-2`
- `us-west-1`
- `us-west-2`

## ResourceRecordSetsChangedWaiterName

```python
from mypy_boto3_route53.literals import ResourceRecordSetsChangedWaiterName
```

Values:

- `resource_record_sets_changed`

## ReusableDelegationSetLimitType

```python
from mypy_boto3_route53.literals import ReusableDelegationSetLimitType
```

Values:

- `MAX_ZONES_BY_REUSABLE_DELEGATION_SET`

## Statistic

```python
from mypy_boto3_route53.literals import Statistic
```

Values:

- `Average`
- `Maximum`
- `Minimum`
- `SampleCount`
- `Sum`

## TagResourceType

```python
from mypy_boto3_route53.literals import TagResourceType
```

Values:

- `healthcheck`
- `hostedzone`

## VPCRegion

```python
from mypy_boto3_route53.literals import VPCRegion
```

Values:

- `af-south-1`
- `ap-east-1`
- `ap-northeast-1`
- `ap-northeast-2`
- `ap-northeast-3`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ca-central-1`
- `cn-north-1`
- `eu-central-1`
- `eu-north-1`
- `eu-south-1`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `me-south-1`
- `sa-east-1`
- `us-east-1`
- `us-east-2`
- `us-gov-east-1`
- `us-gov-west-1`
- `us-iso-east-1`
- `us-isob-east-1`
- `us-west-1`
- `us-west-2`
