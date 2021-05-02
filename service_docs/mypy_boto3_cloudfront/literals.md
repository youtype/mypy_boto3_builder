# Literals for boto3 CloudFront module

> [Index](../index.md) > [CloudFront](./index.md) > Literals

Auto-generated documentation for [CloudFront](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront)
type annotations stubs module [mypy_boto3_cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/).

- [Literals for boto3 CloudFront module](#literals-for-boto3-cloudfront-module)
  - [CachePolicyCookieBehavior](#cachepolicycookiebehavior)
  - [CachePolicyHeaderBehavior](#cachepolicyheaderbehavior)
  - [CachePolicyQueryStringBehavior](#cachepolicyquerystringbehavior)
  - [CachePolicyType](#cachepolicytype)
  - [CertificateSource](#certificatesource)
  - [DistributionDeployedWaiterName](#distributiondeployedwaitername)
  - [EventType](#eventtype)
  - [Format](#format)
  - [FunctionRuntime](#functionruntime)
  - [FunctionStage](#functionstage)
  - [GeoRestrictionType](#georestrictiontype)
  - [HttpVersion](#httpversion)
  - [ICPRecordalStatus](#icprecordalstatus)
  - [InvalidationCompletedWaiterName](#invalidationcompletedwaitername)
  - [ItemSelection](#itemselection)
  - [ListCloudFrontOriginAccessIdentitiesPaginatorName](#listcloudfrontoriginaccessidentitiespaginatorname)
  - [ListDistributionsPaginatorName](#listdistributionspaginatorname)
  - [ListInvalidationsPaginatorName](#listinvalidationspaginatorname)
  - [ListStreamingDistributionsPaginatorName](#liststreamingdistributionspaginatorname)
  - [Method](#method)
  - [MinimumProtocolVersion](#minimumprotocolversion)
  - [OriginProtocolPolicy](#originprotocolpolicy)
  - [OriginRequestPolicyCookieBehavior](#originrequestpolicycookiebehavior)
  - [OriginRequestPolicyHeaderBehavior](#originrequestpolicyheaderbehavior)
  - [OriginRequestPolicyQueryStringBehavior](#originrequestpolicyquerystringbehavior)
  - [OriginRequestPolicyType](#originrequestpolicytype)
  - [PriceClass](#priceclass)
  - [RealtimeMetricsSubscriptionStatus](#realtimemetricssubscriptionstatus)
  - [SSLSupportMethod](#sslsupportmethod)
  - [SslProtocol](#sslprotocol)
  - [StreamingDistributionDeployedWaiterName](#streamingdistributiondeployedwaitername)
  - [ViewerProtocolPolicy](#viewerprotocolpolicy)

## CachePolicyCookieBehavior

```python
from mypy_boto3_cloudfront.literals import CachePolicyCookieBehavior
```

Values:

- `all`
- `allExcept`
- `none`
- `whitelist`

## CachePolicyHeaderBehavior

```python
from mypy_boto3_cloudfront.literals import CachePolicyHeaderBehavior
```

Values:

- `none`
- `whitelist`

## CachePolicyQueryStringBehavior

```python
from mypy_boto3_cloudfront.literals import CachePolicyQueryStringBehavior
```

Values:

- `all`
- `allExcept`
- `none`
- `whitelist`

## CachePolicyType

```python
from mypy_boto3_cloudfront.literals import CachePolicyType
```

Values:

- `custom`
- `managed`

## CertificateSource

```python
from mypy_boto3_cloudfront.literals import CertificateSource
```

Values:

- `acm`
- `cloudfront`
- `iam`

## DistributionDeployedWaiterName

```python
from mypy_boto3_cloudfront.literals import DistributionDeployedWaiterName
```

Values:

- `distribution_deployed`

## EventType

```python
from mypy_boto3_cloudfront.literals import EventType
```

Values:

- `origin-request`
- `origin-response`
- `viewer-request`
- `viewer-response`

## Format

```python
from mypy_boto3_cloudfront.literals import Format
```

Values:

- `URLEncoded`

## FunctionRuntime

```python
from mypy_boto3_cloudfront.literals import FunctionRuntime
```

Values:

- `cloudfront-js-1.0`

## FunctionStage

```python
from mypy_boto3_cloudfront.literals import FunctionStage
```

Values:

- `DEVELOPMENT`
- `LIVE`

## GeoRestrictionType

```python
from mypy_boto3_cloudfront.literals import GeoRestrictionType
```

Values:

- `blacklist`
- `none`
- `whitelist`

## HttpVersion

```python
from mypy_boto3_cloudfront.literals import HttpVersion
```

Values:

- `http1.1`
- `http2`

## ICPRecordalStatus

```python
from mypy_boto3_cloudfront.literals import ICPRecordalStatus
```

Values:

- `APPROVED`
- `PENDING`
- `SUSPENDED`

## InvalidationCompletedWaiterName

```python
from mypy_boto3_cloudfront.literals import InvalidationCompletedWaiterName
```

Values:

- `invalidation_completed`

## ItemSelection

```python
from mypy_boto3_cloudfront.literals import ItemSelection
```

Values:

- `all`
- `none`
- `whitelist`

## ListCloudFrontOriginAccessIdentitiesPaginatorName

```python
from mypy_boto3_cloudfront.literals import ListCloudFrontOriginAccessIdentitiesPaginatorName
```

Values:

- `list_cloud_front_origin_access_identities`

## ListDistributionsPaginatorName

```python
from mypy_boto3_cloudfront.literals import ListDistributionsPaginatorName
```

Values:

- `list_distributions`

## ListInvalidationsPaginatorName

```python
from mypy_boto3_cloudfront.literals import ListInvalidationsPaginatorName
```

Values:

- `list_invalidations`

## ListStreamingDistributionsPaginatorName

```python
from mypy_boto3_cloudfront.literals import ListStreamingDistributionsPaginatorName
```

Values:

- `list_streaming_distributions`

## Method

```python
from mypy_boto3_cloudfront.literals import Method
```

Values:

- `DELETE`
- `GET`
- `HEAD`
- `OPTIONS`
- `PATCH`
- `POST`
- `PUT`

## MinimumProtocolVersion

```python
from mypy_boto3_cloudfront.literals import MinimumProtocolVersion
```

Values:

- `SSLv3`
- `TLSv1`
- `TLSv1.1_2016`
- `TLSv1.2_2018`
- `TLSv1.2_2019`
- `TLSv1_2016`

## OriginProtocolPolicy

```python
from mypy_boto3_cloudfront.literals import OriginProtocolPolicy
```

Values:

- `http-only`
- `https-only`
- `match-viewer`

## OriginRequestPolicyCookieBehavior

```python
from mypy_boto3_cloudfront.literals import OriginRequestPolicyCookieBehavior
```

Values:

- `all`
- `none`
- `whitelist`

## OriginRequestPolicyHeaderBehavior

```python
from mypy_boto3_cloudfront.literals import OriginRequestPolicyHeaderBehavior
```

Values:

- `allViewer`
- `allViewerAndWhitelistCloudFront`
- `none`
- `whitelist`

## OriginRequestPolicyQueryStringBehavior

```python
from mypy_boto3_cloudfront.literals import OriginRequestPolicyQueryStringBehavior
```

Values:

- `all`
- `none`
- `whitelist`

## OriginRequestPolicyType

```python
from mypy_boto3_cloudfront.literals import OriginRequestPolicyType
```

Values:

- `custom`
- `managed`

## PriceClass

```python
from mypy_boto3_cloudfront.literals import PriceClass
```

Values:

- `PriceClass_100`
- `PriceClass_200`
- `PriceClass_All`

## RealtimeMetricsSubscriptionStatus

```python
from mypy_boto3_cloudfront.literals import RealtimeMetricsSubscriptionStatus
```

Values:

- `Disabled`
- `Enabled`

## SSLSupportMethod

```python
from mypy_boto3_cloudfront.literals import SSLSupportMethod
```

Values:

- `sni-only`
- `static-ip`
- `vip`

## SslProtocol

```python
from mypy_boto3_cloudfront.literals import SslProtocol
```

Values:

- `SSLv3`
- `TLSv1`
- `TLSv1.1`
- `TLSv1.2`

## StreamingDistributionDeployedWaiterName

```python
from mypy_boto3_cloudfront.literals import StreamingDistributionDeployedWaiterName
```

Values:

- `streaming_distribution_deployed`

## ViewerProtocolPolicy

```python
from mypy_boto3_cloudfront.literals import ViewerProtocolPolicy
```

Values:

- `allow-all`
- `https-only`
- `redirect-to-https`
