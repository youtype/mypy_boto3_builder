# CloudFrontClient for boto3 CloudFront module

> [Index](../index.md) > [CloudFront](./index.md) > CloudFrontClient

Auto-generated documentation for [CloudFront](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront)
type annotations stubs module [mypy_boto3_cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/).

- [CloudFrontClient for boto3 CloudFront module](#cloudfrontclient-for-boto3-cloudfront-module)
  - [CloudFrontClient](#cloudfrontclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_cache_policy](#create_cache_policy)
    - [create_cloud_front_origin_access_identity](#create_cloud_front_origin_access_identity)
    - [create_distribution](#create_distribution)
    - [create_distribution_with_tags](#create_distribution_with_tags)
    - [create_field_level_encryption_config](#create_field_level_encryption_config)
    - [create_field_level_encryption_profile](#create_field_level_encryption_profile)
    - [create_function](#create_function)
    - [create_invalidation](#create_invalidation)
    - [create_key_group](#create_key_group)
    - [create_monitoring_subscription](#create_monitoring_subscription)
    - [create_origin_request_policy](#create_origin_request_policy)
    - [create_public_key](#create_public_key)
    - [create_realtime_log_config](#create_realtime_log_config)
    - [create_streaming_distribution](#create_streaming_distribution)
    - [create_streaming_distribution_with_tags](#create_streaming_distribution_with_tags)
    - [delete_cache_policy](#delete_cache_policy)
    - [delete_cloud_front_origin_access_identity](#delete_cloud_front_origin_access_identity)
    - [delete_distribution](#delete_distribution)
    - [delete_field_level_encryption_config](#delete_field_level_encryption_config)
    - [delete_field_level_encryption_profile](#delete_field_level_encryption_profile)
    - [delete_function](#delete_function)
    - [delete_key_group](#delete_key_group)
    - [delete_monitoring_subscription](#delete_monitoring_subscription)
    - [delete_origin_request_policy](#delete_origin_request_policy)
    - [delete_public_key](#delete_public_key)
    - [delete_realtime_log_config](#delete_realtime_log_config)
    - [delete_streaming_distribution](#delete_streaming_distribution)
    - [describe_function](#describe_function)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_cache_policy](#get_cache_policy)
    - [get_cache_policy_config](#get_cache_policy_config)
    - [get_cloud_front_origin_access_identity](#get_cloud_front_origin_access_identity)
    - [get_cloud_front_origin_access_identity_config](#get_cloud_front_origin_access_identity_config)
    - [get_distribution](#get_distribution)
    - [get_distribution_config](#get_distribution_config)
    - [get_field_level_encryption](#get_field_level_encryption)
    - [get_field_level_encryption_config](#get_field_level_encryption_config)
    - [get_field_level_encryption_profile](#get_field_level_encryption_profile)
    - [get_field_level_encryption_profile_config](#get_field_level_encryption_profile_config)
    - [get_function](#get_function)
    - [get_invalidation](#get_invalidation)
    - [get_key_group](#get_key_group)
    - [get_key_group_config](#get_key_group_config)
    - [get_monitoring_subscription](#get_monitoring_subscription)
    - [get_origin_request_policy](#get_origin_request_policy)
    - [get_origin_request_policy_config](#get_origin_request_policy_config)
    - [get_public_key](#get_public_key)
    - [get_public_key_config](#get_public_key_config)
    - [get_realtime_log_config](#get_realtime_log_config)
    - [get_streaming_distribution](#get_streaming_distribution)
    - [get_streaming_distribution_config](#get_streaming_distribution_config)
    - [list_cache_policies](#list_cache_policies)
    - [list_cloud_front_origin_access_identities](#list_cloud_front_origin_access_identities)
    - [list_distributions](#list_distributions)
    - [list_distributions_by_cache_policy_id](#list_distributions_by_cache_policy_id)
    - [list_distributions_by_key_group](#list_distributions_by_key_group)
    - [list_distributions_by_origin_request_policy_id](#list_distributions_by_origin_request_policy_id)
    - [list_distributions_by_realtime_log_config](#list_distributions_by_realtime_log_config)
    - [list_distributions_by_web_acl_id](#list_distributions_by_web_acl_id)
    - [list_field_level_encryption_configs](#list_field_level_encryption_configs)
    - [list_field_level_encryption_profiles](#list_field_level_encryption_profiles)
    - [list_functions](#list_functions)
    - [list_invalidations](#list_invalidations)
    - [list_key_groups](#list_key_groups)
    - [list_origin_request_policies](#list_origin_request_policies)
    - [list_public_keys](#list_public_keys)
    - [list_realtime_log_configs](#list_realtime_log_configs)
    - [list_streaming_distributions](#list_streaming_distributions)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [publish_function](#publish_function)
    - [tag_resource](#tag_resource)
    - [test_function](#test_function)
    - [untag_resource](#untag_resource)
    - [update_cache_policy](#update_cache_policy)
    - [update_cloud_front_origin_access_identity](#update_cloud_front_origin_access_identity)
    - [update_distribution](#update_distribution)
    - [update_field_level_encryption_config](#update_field_level_encryption_config)
    - [update_field_level_encryption_profile](#update_field_level_encryption_profile)
    - [update_function](#update_function)
    - [update_key_group](#update_key_group)
    - [update_origin_request_policy](#update_origin_request_policy)
    - [update_public_key](#update_public_key)
    - [update_realtime_log_config](#update_realtime_log_config)
    - [update_streaming_distribution](#update_streaming_distribution)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)

## CloudFrontClient

Type annotations for `boto3.client("cloudfront")`

Can be used directly:

```python
from mypy_boto3_cloudfront.client import CloudFrontClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudfront.client import Exceptions

def handle_error(exc: Exceptions.AccessDenied) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDenied`
- `Exceptions.BatchTooLarge`
- `Exceptions.CNAMEAlreadyExists`
- `Exceptions.CachePolicyAlreadyExists`
- `Exceptions.CachePolicyInUse`
- `Exceptions.CannotChangeImmutablePublicKeyFields`
- `Exceptions.ClientError`
- `Exceptions.CloudFrontOriginAccessIdentityAlreadyExists`
- `Exceptions.CloudFrontOriginAccessIdentityInUse`
- `Exceptions.DistributionAlreadyExists`
- `Exceptions.DistributionNotDisabled`
- `Exceptions.FieldLevelEncryptionConfigAlreadyExists`
- `Exceptions.FieldLevelEncryptionConfigInUse`
- `Exceptions.FieldLevelEncryptionProfileAlreadyExists`
- `Exceptions.FieldLevelEncryptionProfileInUse`
- `Exceptions.FieldLevelEncryptionProfileSizeExceeded`
- `Exceptions.FunctionAlreadyExists`
- `Exceptions.FunctionInUse`
- `Exceptions.FunctionSizeLimitExceeded`
- `Exceptions.IllegalDelete`
- `Exceptions.IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior`
- `Exceptions.IllegalUpdate`
- `Exceptions.InconsistentQuantities`
- `Exceptions.InvalidArgument`
- `Exceptions.InvalidDefaultRootObject`
- `Exceptions.InvalidErrorCode`
- `Exceptions.InvalidForwardCookies`
- `Exceptions.InvalidFunctionAssociation`
- `Exceptions.InvalidGeoRestrictionParameter`
- `Exceptions.InvalidHeadersForS3Origin`
- `Exceptions.InvalidIfMatchVersion`
- `Exceptions.InvalidLambdaFunctionAssociation`
- `Exceptions.InvalidLocationCode`
- `Exceptions.InvalidMinimumProtocolVersion`
- `Exceptions.InvalidOrigin`
- `Exceptions.InvalidOriginAccessIdentity`
- `Exceptions.InvalidOriginKeepaliveTimeout`
- `Exceptions.InvalidOriginReadTimeout`
- `Exceptions.InvalidProtocolSettings`
- `Exceptions.InvalidQueryStringParameters`
- `Exceptions.InvalidRelativePath`
- `Exceptions.InvalidRequiredProtocol`
- `Exceptions.InvalidResponseCode`
- `Exceptions.InvalidTTLOrder`
- `Exceptions.InvalidTagging`
- `Exceptions.InvalidViewerCertificate`
- `Exceptions.InvalidWebACLId`
- `Exceptions.KeyGroupAlreadyExists`
- `Exceptions.MissingBody`
- `Exceptions.NoSuchCachePolicy`
- `Exceptions.NoSuchCloudFrontOriginAccessIdentity`
- `Exceptions.NoSuchDistribution`
- `Exceptions.NoSuchFieldLevelEncryptionConfig`
- `Exceptions.NoSuchFieldLevelEncryptionProfile`
- `Exceptions.NoSuchFunctionExists`
- `Exceptions.NoSuchInvalidation`
- `Exceptions.NoSuchOrigin`
- `Exceptions.NoSuchOriginRequestPolicy`
- `Exceptions.NoSuchPublicKey`
- `Exceptions.NoSuchRealtimeLogConfig`
- `Exceptions.NoSuchResource`
- `Exceptions.NoSuchStreamingDistribution`
- `Exceptions.OriginRequestPolicyAlreadyExists`
- `Exceptions.OriginRequestPolicyInUse`
- `Exceptions.PreconditionFailed`
- `Exceptions.PublicKeyAlreadyExists`
- `Exceptions.PublicKeyInUse`
- `Exceptions.QueryArgProfileEmpty`
- `Exceptions.RealtimeLogConfigAlreadyExists`
- `Exceptions.RealtimeLogConfigInUse`
- `Exceptions.RealtimeLogConfigOwnerMismatch`
- `Exceptions.ResourceInUse`
- `Exceptions.StreamingDistributionAlreadyExists`
- `Exceptions.StreamingDistributionNotDisabled`
- `Exceptions.TestFunctionFailed`
- `Exceptions.TooManyCacheBehaviors`
- `Exceptions.TooManyCachePolicies`
- `Exceptions.TooManyCertificates`
- `Exceptions.TooManyCloudFrontOriginAccessIdentities`
- `Exceptions.TooManyCookieNamesInWhiteList`
- `Exceptions.TooManyCookiesInCachePolicy`
- `Exceptions.TooManyCookiesInOriginRequestPolicy`
- `Exceptions.TooManyDistributionCNAMEs`
- `Exceptions.TooManyDistributions`
- `Exceptions.TooManyDistributionsAssociatedToCachePolicy`
- `Exceptions.TooManyDistributionsAssociatedToFieldLevelEncryptionConfig`
- `Exceptions.TooManyDistributionsAssociatedToKeyGroup`
- `Exceptions.TooManyDistributionsAssociatedToOriginRequestPolicy`
- `Exceptions.TooManyDistributionsWithFunctionAssociations`
- `Exceptions.TooManyDistributionsWithLambdaAssociations`
- `Exceptions.TooManyDistributionsWithSingleFunctionARN`
- `Exceptions.TooManyFieldLevelEncryptionConfigs`
- `Exceptions.TooManyFieldLevelEncryptionContentTypeProfiles`
- `Exceptions.TooManyFieldLevelEncryptionEncryptionEntities`
- `Exceptions.TooManyFieldLevelEncryptionFieldPatterns`
- `Exceptions.TooManyFieldLevelEncryptionProfiles`
- `Exceptions.TooManyFieldLevelEncryptionQueryArgProfiles`
- `Exceptions.TooManyFunctionAssociations`
- `Exceptions.TooManyFunctions`
- `Exceptions.TooManyHeadersInCachePolicy`
- `Exceptions.TooManyHeadersInForwardedValues`
- `Exceptions.TooManyHeadersInOriginRequestPolicy`
- `Exceptions.TooManyInvalidationsInProgress`
- `Exceptions.TooManyKeyGroups`
- `Exceptions.TooManyKeyGroupsAssociatedToDistribution`
- `Exceptions.TooManyLambdaFunctionAssociations`
- `Exceptions.TooManyOriginCustomHeaders`
- `Exceptions.TooManyOriginGroupsPerDistribution`
- `Exceptions.TooManyOriginRequestPolicies`
- `Exceptions.TooManyOrigins`
- `Exceptions.TooManyPublicKeys`
- `Exceptions.TooManyPublicKeysInKeyGroup`
- `Exceptions.TooManyQueryStringParameters`
- `Exceptions.TooManyQueryStringsInCachePolicy`
- `Exceptions.TooManyQueryStringsInOriginRequestPolicy`
- `Exceptions.TooManyRealtimeLogConfigs`
- `Exceptions.TooManyStreamingDistributionCNAMEs`
- `Exceptions.TooManyStreamingDistributions`
- `Exceptions.TooManyTrustedSigners`
- `Exceptions.TrustedKeyGroupDoesNotExist`
- `Exceptions.TrustedSignerDoesNotExist`
- `Exceptions.UnsupportedOperation`


## Methods


### can_paginate

Type annotations for `boto3.client("cloudfront").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_cache_policy

Type annotations for `boto3.client("cloudfront").create_cache_policy` method.

[Client.create_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_cache_policy)

```python
def create_cache_policy(
    self,
    CachePolicyConfig: "CachePolicyConfigTypeDef"
) -> CreateCachePolicyResultTypeDef:
    pass
```

### create_cloud_front_origin_access_identity

Type annotations for `boto3.client("cloudfront").create_cloud_front_origin_access_identity` method.

[Client.create_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_cloud_front_origin_access_identity)

```python
def create_cloud_front_origin_access_identity(
    self,
    CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef"
) -> CreateCloudFrontOriginAccessIdentityResultTypeDef:
    pass
```

### create_distribution

Type annotations for `boto3.client("cloudfront").create_distribution` method.

[Client.create_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_distribution)

```python
def create_distribution(
    self,
    DistributionConfig: "DistributionConfigTypeDef"
) -> CreateDistributionResultTypeDef:
    pass
```

### create_distribution_with_tags

Type annotations for `boto3.client("cloudfront").create_distribution_with_tags` method.

[Client.create_distribution_with_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_distribution_with_tags)

```python
def create_distribution_with_tags(
    self,
    DistributionConfigWithTags: DistributionConfigWithTagsTypeDef
) -> CreateDistributionWithTagsResultTypeDef:
    pass
```

### create_field_level_encryption_config

Type annotations for `boto3.client("cloudfront").create_field_level_encryption_config` method.

[Client.create_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_field_level_encryption_config)

```python
def create_field_level_encryption_config(
    self,
    FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef"
) -> CreateFieldLevelEncryptionConfigResultTypeDef:
    pass
```

### create_field_level_encryption_profile

Type annotations for `boto3.client("cloudfront").create_field_level_encryption_profile` method.

[Client.create_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_field_level_encryption_profile)

```python
def create_field_level_encryption_profile(
    self,
    FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef"
) -> CreateFieldLevelEncryptionProfileResultTypeDef:
    pass
```

### create_function

Type annotations for `boto3.client("cloudfront").create_function` method.

[Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_function)

```python
def create_function(
    self,
    Name: str,
    FunctionConfig: "FunctionConfigTypeDef",
    FunctionCode: Union[bytes, IO[bytes]]
) -> CreateFunctionResultTypeDef:
    pass
```

### create_invalidation

Type annotations for `boto3.client("cloudfront").create_invalidation` method.

[Client.create_invalidation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_invalidation)

```python
def create_invalidation(
    self,
    DistributionId: str,
    InvalidationBatch: "InvalidationBatchTypeDef"
) -> CreateInvalidationResultTypeDef:
    pass
```

### create_key_group

Type annotations for `boto3.client("cloudfront").create_key_group` method.

[Client.create_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_key_group)

```python
def create_key_group(
    self,
    KeyGroupConfig: "KeyGroupConfigTypeDef"
) -> CreateKeyGroupResultTypeDef:
    pass
```

### create_monitoring_subscription

Type annotations for `boto3.client("cloudfront").create_monitoring_subscription` method.

[Client.create_monitoring_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_monitoring_subscription)

```python
def create_monitoring_subscription(
    self,
    DistributionId: str,
    MonitoringSubscription: "MonitoringSubscriptionTypeDef"
) -> CreateMonitoringSubscriptionResultTypeDef:
    pass
```

### create_origin_request_policy

Type annotations for `boto3.client("cloudfront").create_origin_request_policy` method.

[Client.create_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_origin_request_policy)

```python
def create_origin_request_policy(
    self,
    OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef"
) -> CreateOriginRequestPolicyResultTypeDef:
    pass
```

### create_public_key

Type annotations for `boto3.client("cloudfront").create_public_key` method.

[Client.create_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_public_key)

```python
def create_public_key(
    self,
    PublicKeyConfig: "PublicKeyConfigTypeDef"
) -> CreatePublicKeyResultTypeDef:
    pass
```

### create_realtime_log_config

Type annotations for `boto3.client("cloudfront").create_realtime_log_config` method.

[Client.create_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_realtime_log_config)

```python
def create_realtime_log_config(
    self,
    EndPoints: List["EndPointTypeDef"],
    Fields: List[str],
    Name: str,
    SamplingRate: int
) -> CreateRealtimeLogConfigResultTypeDef:
    pass
```

### create_streaming_distribution

Type annotations for `boto3.client("cloudfront").create_streaming_distribution` method.

[Client.create_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_streaming_distribution)

```python
def create_streaming_distribution(
    self,
    StreamingDistributionConfig: "StreamingDistributionConfigTypeDef"
) -> CreateStreamingDistributionResultTypeDef:
    pass
```

### create_streaming_distribution_with_tags

Type annotations for `boto3.client("cloudfront").create_streaming_distribution_with_tags` method.

[Client.create_streaming_distribution_with_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.create_streaming_distribution_with_tags)

```python
def create_streaming_distribution_with_tags(
    self,
    StreamingDistributionConfigWithTags: StreamingDistributionConfigWithTagsTypeDef
) -> CreateStreamingDistributionWithTagsResultTypeDef:
    pass
```

### delete_cache_policy

Type annotations for `boto3.client("cloudfront").delete_cache_policy` method.

[Client.delete_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_cache_policy)

```python
def delete_cache_policy(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_cloud_front_origin_access_identity

Type annotations for `boto3.client("cloudfront").delete_cloud_front_origin_access_identity` method.

[Client.delete_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_cloud_front_origin_access_identity)

```python
def delete_cloud_front_origin_access_identity(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_distribution

Type annotations for `boto3.client("cloudfront").delete_distribution` method.

[Client.delete_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_distribution)

```python
def delete_distribution(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_field_level_encryption_config

Type annotations for `boto3.client("cloudfront").delete_field_level_encryption_config` method.

[Client.delete_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_field_level_encryption_config)

```python
def delete_field_level_encryption_config(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_field_level_encryption_profile

Type annotations for `boto3.client("cloudfront").delete_field_level_encryption_profile` method.

[Client.delete_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_field_level_encryption_profile)

```python
def delete_field_level_encryption_profile(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_function

Type annotations for `boto3.client("cloudfront").delete_function` method.

[Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_function)

```python
def delete_function(
    self,
    Name: str,
    IfMatch: str
) -> None:
    pass
```

### delete_key_group

Type annotations for `boto3.client("cloudfront").delete_key_group` method.

[Client.delete_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_key_group)

```python
def delete_key_group(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_monitoring_subscription

Type annotations for `boto3.client("cloudfront").delete_monitoring_subscription` method.

[Client.delete_monitoring_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_monitoring_subscription)

```python
def delete_monitoring_subscription(
    self,
    DistributionId: str
) -> Dict[str, Any]:
    pass
```

### delete_origin_request_policy

Type annotations for `boto3.client("cloudfront").delete_origin_request_policy` method.

[Client.delete_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_origin_request_policy)

```python
def delete_origin_request_policy(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_public_key

Type annotations for `boto3.client("cloudfront").delete_public_key` method.

[Client.delete_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_public_key)

```python
def delete_public_key(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### delete_realtime_log_config

Type annotations for `boto3.client("cloudfront").delete_realtime_log_config` method.

[Client.delete_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_realtime_log_config)

```python
def delete_realtime_log_config(
    self,
    Name: str = None,
    ARN: str = None
) -> None:
    pass
```

### delete_streaming_distribution

Type annotations for `boto3.client("cloudfront").delete_streaming_distribution` method.

[Client.delete_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.delete_streaming_distribution)

```python
def delete_streaming_distribution(
    self,
    Id: str,
    IfMatch: str = None
) -> None:
    pass
```

### describe_function

Type annotations for `boto3.client("cloudfront").describe_function` method.

[Client.describe_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.describe_function)

```python
def describe_function(
    self,
    Name: str,
    Stage: FunctionStage = None
) -> DescribeFunctionResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudfront").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_cache_policy

Type annotations for `boto3.client("cloudfront").get_cache_policy` method.

[Client.get_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_cache_policy)

```python
def get_cache_policy(
    self,
    Id: str
) -> GetCachePolicyResultTypeDef:
    pass
```

### get_cache_policy_config

Type annotations for `boto3.client("cloudfront").get_cache_policy_config` method.

[Client.get_cache_policy_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_cache_policy_config)

```python
def get_cache_policy_config(
    self,
    Id: str
) -> GetCachePolicyConfigResultTypeDef:
    pass
```

### get_cloud_front_origin_access_identity

Type annotations for `boto3.client("cloudfront").get_cloud_front_origin_access_identity` method.

[Client.get_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_cloud_front_origin_access_identity)

```python
def get_cloud_front_origin_access_identity(
    self,
    Id: str
) -> GetCloudFrontOriginAccessIdentityResultTypeDef:
    pass
```

### get_cloud_front_origin_access_identity_config

Type annotations for `boto3.client("cloudfront").get_cloud_front_origin_access_identity_config` method.

[Client.get_cloud_front_origin_access_identity_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_cloud_front_origin_access_identity_config)

```python
def get_cloud_front_origin_access_identity_config(
    self,
    Id: str
) -> GetCloudFrontOriginAccessIdentityConfigResultTypeDef:
    pass
```

### get_distribution

Type annotations for `boto3.client("cloudfront").get_distribution` method.

[Client.get_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_distribution)

```python
def get_distribution(
    self,
    Id: str
) -> GetDistributionResultTypeDef:
    pass
```

### get_distribution_config

Type annotations for `boto3.client("cloudfront").get_distribution_config` method.

[Client.get_distribution_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_distribution_config)

```python
def get_distribution_config(
    self,
    Id: str
) -> GetDistributionConfigResultTypeDef:
    pass
```

### get_field_level_encryption

Type annotations for `boto3.client("cloudfront").get_field_level_encryption` method.

[Client.get_field_level_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption)

```python
def get_field_level_encryption(
    self,
    Id: str
) -> GetFieldLevelEncryptionResultTypeDef:
    pass
```

### get_field_level_encryption_config

Type annotations for `boto3.client("cloudfront").get_field_level_encryption_config` method.

[Client.get_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_config)

```python
def get_field_level_encryption_config(
    self,
    Id: str
) -> GetFieldLevelEncryptionConfigResultTypeDef:
    pass
```

### get_field_level_encryption_profile

Type annotations for `boto3.client("cloudfront").get_field_level_encryption_profile` method.

[Client.get_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_profile)

```python
def get_field_level_encryption_profile(
    self,
    Id: str
) -> GetFieldLevelEncryptionProfileResultTypeDef:
    pass
```

### get_field_level_encryption_profile_config

Type annotations for `boto3.client("cloudfront").get_field_level_encryption_profile_config` method.

[Client.get_field_level_encryption_profile_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_field_level_encryption_profile_config)

```python
def get_field_level_encryption_profile_config(
    self,
    Id: str
) -> GetFieldLevelEncryptionProfileConfigResultTypeDef:
    pass
```

### get_function

Type annotations for `boto3.client("cloudfront").get_function` method.

[Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_function)

```python
def get_function(
    self,
    Name: str,
    Stage: FunctionStage = None
) -> GetFunctionResultTypeDef:
    pass
```

### get_invalidation

Type annotations for `boto3.client("cloudfront").get_invalidation` method.

[Client.get_invalidation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_invalidation)

```python
def get_invalidation(
    self,
    DistributionId: str,
    Id: str
) -> GetInvalidationResultTypeDef:
    pass
```

### get_key_group

Type annotations for `boto3.client("cloudfront").get_key_group` method.

[Client.get_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_key_group)

```python
def get_key_group(
    self,
    Id: str
) -> GetKeyGroupResultTypeDef:
    pass
```

### get_key_group_config

Type annotations for `boto3.client("cloudfront").get_key_group_config` method.

[Client.get_key_group_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_key_group_config)

```python
def get_key_group_config(
    self,
    Id: str
) -> GetKeyGroupConfigResultTypeDef:
    pass
```

### get_monitoring_subscription

Type annotations for `boto3.client("cloudfront").get_monitoring_subscription` method.

[Client.get_monitoring_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_monitoring_subscription)

```python
def get_monitoring_subscription(
    self,
    DistributionId: str
) -> GetMonitoringSubscriptionResultTypeDef:
    pass
```

### get_origin_request_policy

Type annotations for `boto3.client("cloudfront").get_origin_request_policy` method.

[Client.get_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_origin_request_policy)

```python
def get_origin_request_policy(
    self,
    Id: str
) -> GetOriginRequestPolicyResultTypeDef:
    pass
```

### get_origin_request_policy_config

Type annotations for `boto3.client("cloudfront").get_origin_request_policy_config` method.

[Client.get_origin_request_policy_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_origin_request_policy_config)

```python
def get_origin_request_policy_config(
    self,
    Id: str
) -> GetOriginRequestPolicyConfigResultTypeDef:
    pass
```

### get_public_key

Type annotations for `boto3.client("cloudfront").get_public_key` method.

[Client.get_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_public_key)

```python
def get_public_key(
    self,
    Id: str
) -> GetPublicKeyResultTypeDef:
    pass
```

### get_public_key_config

Type annotations for `boto3.client("cloudfront").get_public_key_config` method.

[Client.get_public_key_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_public_key_config)

```python
def get_public_key_config(
    self,
    Id: str
) -> GetPublicKeyConfigResultTypeDef:
    pass
```

### get_realtime_log_config

Type annotations for `boto3.client("cloudfront").get_realtime_log_config` method.

[Client.get_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_realtime_log_config)

```python
def get_realtime_log_config(
    self,
    Name: str = None,
    ARN: str = None
) -> GetRealtimeLogConfigResultTypeDef:
    pass
```

### get_streaming_distribution

Type annotations for `boto3.client("cloudfront").get_streaming_distribution` method.

[Client.get_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_streaming_distribution)

```python
def get_streaming_distribution(
    self,
    Id: str
) -> GetStreamingDistributionResultTypeDef:
    pass
```

### get_streaming_distribution_config

Type annotations for `boto3.client("cloudfront").get_streaming_distribution_config` method.

[Client.get_streaming_distribution_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.get_streaming_distribution_config)

```python
def get_streaming_distribution_config(
    self,
    Id: str
) -> GetStreamingDistributionConfigResultTypeDef:
    pass
```

### list_cache_policies

Type annotations for `boto3.client("cloudfront").list_cache_policies` method.

[Client.list_cache_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_cache_policies)

```python
def list_cache_policies(
    self,
    Type: CachePolicyType = None,
    Marker: str = None,
    MaxItems: str = None
) -> ListCachePoliciesResultTypeDef:
    pass
```

### list_cloud_front_origin_access_identities

Type annotations for `boto3.client("cloudfront").list_cloud_front_origin_access_identities` method.

[Client.list_cloud_front_origin_access_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_cloud_front_origin_access_identities)

```python
def list_cloud_front_origin_access_identities(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListCloudFrontOriginAccessIdentitiesResultTypeDef:
    pass
```

### list_distributions

Type annotations for `boto3.client("cloudfront").list_distributions` method.

[Client.list_distributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_distributions)

```python
def list_distributions(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListDistributionsResultTypeDef:
    pass
```

### list_distributions_by_cache_policy_id

Type annotations for `boto3.client("cloudfront").list_distributions_by_cache_policy_id` method.

[Client.list_distributions_by_cache_policy_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_cache_policy_id)

```python
def list_distributions_by_cache_policy_id(
    self,
    CachePolicyId: str,
    Marker: str = None,
    MaxItems: str = None
) -> ListDistributionsByCachePolicyIdResultTypeDef:
    pass
```

### list_distributions_by_key_group

Type annotations for `boto3.client("cloudfront").list_distributions_by_key_group` method.

[Client.list_distributions_by_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_key_group)

```python
def list_distributions_by_key_group(
    self,
    KeyGroupId: str,
    Marker: str = None,
    MaxItems: str = None
) -> ListDistributionsByKeyGroupResultTypeDef:
    pass
```

### list_distributions_by_origin_request_policy_id

Type annotations for `boto3.client("cloudfront").list_distributions_by_origin_request_policy_id` method.

[Client.list_distributions_by_origin_request_policy_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_origin_request_policy_id)

```python
def list_distributions_by_origin_request_policy_id(
    self,
    OriginRequestPolicyId: str,
    Marker: str = None,
    MaxItems: str = None
) -> ListDistributionsByOriginRequestPolicyIdResultTypeDef:
    pass
```

### list_distributions_by_realtime_log_config

Type annotations for `boto3.client("cloudfront").list_distributions_by_realtime_log_config` method.

[Client.list_distributions_by_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_realtime_log_config)

```python
def list_distributions_by_realtime_log_config(
    self,
    Marker: str = None,
    MaxItems: str = None,
    RealtimeLogConfigName: str = None,
    RealtimeLogConfigArn: str = None
) -> ListDistributionsByRealtimeLogConfigResultTypeDef:
    pass
```

### list_distributions_by_web_acl_id

Type annotations for `boto3.client("cloudfront").list_distributions_by_web_acl_id` method.

[Client.list_distributions_by_web_acl_id documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_distributions_by_web_acl_id)

```python
def list_distributions_by_web_acl_id(
    self,
    WebACLId: str,
    Marker: str = None,
    MaxItems: str = None
) -> ListDistributionsByWebACLIdResultTypeDef:
    pass
```

### list_field_level_encryption_configs

Type annotations for `boto3.client("cloudfront").list_field_level_encryption_configs` method.

[Client.list_field_level_encryption_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_field_level_encryption_configs)

```python
def list_field_level_encryption_configs(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListFieldLevelEncryptionConfigsResultTypeDef:
    pass
```

### list_field_level_encryption_profiles

Type annotations for `boto3.client("cloudfront").list_field_level_encryption_profiles` method.

[Client.list_field_level_encryption_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_field_level_encryption_profiles)

```python
def list_field_level_encryption_profiles(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListFieldLevelEncryptionProfilesResultTypeDef:
    pass
```

### list_functions

Type annotations for `boto3.client("cloudfront").list_functions` method.

[Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_functions)

```python
def list_functions(
    self,
    Marker: str = None,
    MaxItems: str = None,
    Stage: FunctionStage = None
) -> ListFunctionsResultTypeDef:
    pass
```

### list_invalidations

Type annotations for `boto3.client("cloudfront").list_invalidations` method.

[Client.list_invalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_invalidations)

```python
def list_invalidations(
    self,
    DistributionId: str,
    Marker: str = None,
    MaxItems: str = None
) -> ListInvalidationsResultTypeDef:
    pass
```

### list_key_groups

Type annotations for `boto3.client("cloudfront").list_key_groups` method.

[Client.list_key_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_key_groups)

```python
def list_key_groups(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListKeyGroupsResultTypeDef:
    pass
```

### list_origin_request_policies

Type annotations for `boto3.client("cloudfront").list_origin_request_policies` method.

[Client.list_origin_request_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_origin_request_policies)

```python
def list_origin_request_policies(
    self,
    Type: OriginRequestPolicyType = None,
    Marker: str = None,
    MaxItems: str = None
) -> ListOriginRequestPoliciesResultTypeDef:
    pass
```

### list_public_keys

Type annotations for `boto3.client("cloudfront").list_public_keys` method.

[Client.list_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_public_keys)

```python
def list_public_keys(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListPublicKeysResultTypeDef:
    pass
```

### list_realtime_log_configs

Type annotations for `boto3.client("cloudfront").list_realtime_log_configs` method.

[Client.list_realtime_log_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_realtime_log_configs)

```python
def list_realtime_log_configs(
    self,
    MaxItems: str = None,
    Marker: str = None
) -> ListRealtimeLogConfigsResultTypeDef:
    pass
```

### list_streaming_distributions

Type annotations for `boto3.client("cloudfront").list_streaming_distributions` method.

[Client.list_streaming_distributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_streaming_distributions)

```python
def list_streaming_distributions(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListStreamingDistributionsResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("cloudfront").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    Resource: str
) -> ListTagsForResourceResultTypeDef:
    pass
```

### publish_function

Type annotations for `boto3.client("cloudfront").publish_function` method.

[Client.publish_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.publish_function)

```python
def publish_function(
    self,
    Name: str,
    IfMatch: str
) -> PublishFunctionResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("cloudfront").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.tag_resource)

```python
def tag_resource(
    self,
    Resource: str,
    Tags: "TagsTypeDef"
) -> None:
    pass
```

### test_function

Type annotations for `boto3.client("cloudfront").test_function` method.

[Client.test_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.test_function)

```python
def test_function(
    self,
    Name: str,
    IfMatch: str,
    EventObject: Union[bytes, IO[bytes]],
    Stage: FunctionStage = None
) -> TestFunctionResultTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("cloudfront").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.untag_resource)

```python
def untag_resource(
    self,
    Resource: str,
    TagKeys: TagKeysTypeDef
) -> None:
    pass
```

### update_cache_policy

Type annotations for `boto3.client("cloudfront").update_cache_policy` method.

[Client.update_cache_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_cache_policy)

```python
def update_cache_policy(
    self,
    CachePolicyConfig: "CachePolicyConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateCachePolicyResultTypeDef:
    pass
```

### update_cloud_front_origin_access_identity

Type annotations for `boto3.client("cloudfront").update_cloud_front_origin_access_identity` method.

[Client.update_cloud_front_origin_access_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_cloud_front_origin_access_identity)

```python
def update_cloud_front_origin_access_identity(
    self,
    CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateCloudFrontOriginAccessIdentityResultTypeDef:
    pass
```

### update_distribution

Type annotations for `boto3.client("cloudfront").update_distribution` method.

[Client.update_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_distribution)

```python
def update_distribution(
    self,
    DistributionConfig: "DistributionConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateDistributionResultTypeDef:
    pass
```

### update_field_level_encryption_config

Type annotations for `boto3.client("cloudfront").update_field_level_encryption_config` method.

[Client.update_field_level_encryption_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_field_level_encryption_config)

```python
def update_field_level_encryption_config(
    self,
    FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateFieldLevelEncryptionConfigResultTypeDef:
    pass
```

### update_field_level_encryption_profile

Type annotations for `boto3.client("cloudfront").update_field_level_encryption_profile` method.

[Client.update_field_level_encryption_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_field_level_encryption_profile)

```python
def update_field_level_encryption_profile(
    self,
    FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateFieldLevelEncryptionProfileResultTypeDef:
    pass
```

### update_function

Type annotations for `boto3.client("cloudfront").update_function` method.

[Client.update_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_function)

```python
def update_function(
    self,
    Name: str,
    IfMatch: str,
    FunctionConfig: "FunctionConfigTypeDef",
    FunctionCode: Union[bytes, IO[bytes]]
) -> UpdateFunctionResultTypeDef:
    pass
```

### update_key_group

Type annotations for `boto3.client("cloudfront").update_key_group` method.

[Client.update_key_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_key_group)

```python
def update_key_group(
    self,
    KeyGroupConfig: "KeyGroupConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateKeyGroupResultTypeDef:
    pass
```

### update_origin_request_policy

Type annotations for `boto3.client("cloudfront").update_origin_request_policy` method.

[Client.update_origin_request_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_origin_request_policy)

```python
def update_origin_request_policy(
    self,
    OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateOriginRequestPolicyResultTypeDef:
    pass
```

### update_public_key

Type annotations for `boto3.client("cloudfront").update_public_key` method.

[Client.update_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_public_key)

```python
def update_public_key(
    self,
    PublicKeyConfig: "PublicKeyConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdatePublicKeyResultTypeDef:
    pass
```

### update_realtime_log_config

Type annotations for `boto3.client("cloudfront").update_realtime_log_config` method.

[Client.update_realtime_log_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_realtime_log_config)

```python
def update_realtime_log_config(
    self,
    EndPoints: List["EndPointTypeDef"] = None,
    Fields: List[str] = None,
    Name: str = None,
    ARN: str = None,
    SamplingRate: int = None
) -> UpdateRealtimeLogConfigResultTypeDef:
    pass
```

### update_streaming_distribution

Type annotations for `boto3.client("cloudfront").update_streaming_distribution` method.

[Client.update_streaming_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Client.update_streaming_distribution)

```python
def update_streaming_distribution(
    self,
    StreamingDistributionConfig: "StreamingDistributionConfigTypeDef",
    Id: str,
    IfMatch: str = None
) -> UpdateStreamingDistributionResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudfront").get_paginator` method.

[Paginator.ListCloudFrontOriginAccessIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListCloudFrontOriginAccessIdentities)

```python
@overload
def get_paginator(
    self,
    operation_name: ListCloudFrontOriginAccessIdentitiesPaginatorName
) -> ListCloudFrontOriginAccessIdentitiesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudfront").get_paginator` method.

[Paginator.ListDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListDistributions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListDistributionsPaginatorName
) -> ListDistributionsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudfront").get_paginator` method.

[Paginator.ListInvalidations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListInvalidations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListInvalidationsPaginatorName
) -> ListInvalidationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudfront").get_paginator` method.

[Paginator.ListStreamingDistributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Paginator.ListStreamingDistributions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStreamingDistributionsPaginatorName
) -> ListStreamingDistributionsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudfront").get_waiter` method.

[Waiter.DistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Waiter.DistributionDeployed)

```python
@overload
def get_waiter(
    self,
    waiter_name: DistributionDeployedWaiterName
) -> DistributionDeployedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudfront").get_waiter` method.

[Waiter.InvalidationCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Waiter.InvalidationCompleted)

```python
@overload
def get_waiter(
    self,
    waiter_name: InvalidationCompletedWaiterName
) -> InvalidationCompletedWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudfront").get_waiter` method.

[Waiter.StreamingDistributionDeployed documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront.Waiter.StreamingDistributionDeployed)

```python
@overload
def get_waiter(
    self,
    waiter_name: StreamingDistributionDeployedWaiterName
) -> StreamingDistributionDeployedWaiter:
    pass
```