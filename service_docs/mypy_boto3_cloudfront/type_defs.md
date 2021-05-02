# Structures for boto3 CloudFront module

> [Index](../index.md) > [CloudFront](./index.md) > Structures

Auto-generated documentation for [CloudFront](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#CloudFront)
type annotations stubs module [mypy_boto3_cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/).

- [Structures for boto3 CloudFront module](#structures-for-boto3-cloudfront-module)
  - [ActiveTrustedKeyGroupsTypeDef](#activetrustedkeygroupstypedef)
  - [ActiveTrustedSignersTypeDef](#activetrustedsignerstypedef)
  - [AliasICPRecordalTypeDef](#aliasicprecordaltypedef)
  - [AliasesTypeDef](#aliasestypedef)
  - [AllowedMethodsTypeDef](#allowedmethodstypedef)
  - [CacheBehaviorTypeDef](#cachebehaviortypedef)
  - [CacheBehaviorsTypeDef](#cachebehaviorstypedef)
  - [CachePolicyConfigTypeDef](#cachepolicyconfigtypedef)
  - [CachePolicyCookiesConfigTypeDef](#cachepolicycookiesconfigtypedef)
  - [CachePolicyHeadersConfigTypeDef](#cachepolicyheadersconfigtypedef)
  - [CachePolicyListTypeDef](#cachepolicylisttypedef)
  - [CachePolicyQueryStringsConfigTypeDef](#cachepolicyquerystringsconfigtypedef)
  - [CachePolicySummaryTypeDef](#cachepolicysummarytypedef)
  - [CachePolicyTypeDef](#cachepolicytypedef)
  - [CachedMethodsTypeDef](#cachedmethodstypedef)
  - [CloudFrontOriginAccessIdentityConfigTypeDef](#cloudfrontoriginaccessidentityconfigtypedef)
  - [CloudFrontOriginAccessIdentityListTypeDef](#cloudfrontoriginaccessidentitylisttypedef)
  - [CloudFrontOriginAccessIdentitySummaryTypeDef](#cloudfrontoriginaccessidentitysummarytypedef)
  - [CloudFrontOriginAccessIdentityTypeDef](#cloudfrontoriginaccessidentitytypedef)
  - [ContentTypeProfileConfigTypeDef](#contenttypeprofileconfigtypedef)
  - [ContentTypeProfileTypeDef](#contenttypeprofiletypedef)
  - [ContentTypeProfilesTypeDef](#contenttypeprofilestypedef)
  - [CookieNamesTypeDef](#cookienamestypedef)
  - [CookiePreferenceTypeDef](#cookiepreferencetypedef)
  - [CreateCachePolicyResultTypeDef](#createcachepolicyresulttypedef)
  - [CreateCloudFrontOriginAccessIdentityResultTypeDef](#createcloudfrontoriginaccessidentityresulttypedef)
  - [CreateDistributionResultTypeDef](#createdistributionresulttypedef)
  - [CreateDistributionWithTagsResultTypeDef](#createdistributionwithtagsresulttypedef)
  - [CreateFieldLevelEncryptionConfigResultTypeDef](#createfieldlevelencryptionconfigresulttypedef)
  - [CreateFieldLevelEncryptionProfileResultTypeDef](#createfieldlevelencryptionprofileresulttypedef)
  - [CreateFunctionResultTypeDef](#createfunctionresulttypedef)
  - [CreateInvalidationResultTypeDef](#createinvalidationresulttypedef)
  - [CreateKeyGroupResultTypeDef](#createkeygroupresulttypedef)
  - [CreateMonitoringSubscriptionResultTypeDef](#createmonitoringsubscriptionresulttypedef)
  - [CreateOriginRequestPolicyResultTypeDef](#createoriginrequestpolicyresulttypedef)
  - [CreatePublicKeyResultTypeDef](#createpublickeyresulttypedef)
  - [CreateRealtimeLogConfigResultTypeDef](#createrealtimelogconfigresulttypedef)
  - [CreateStreamingDistributionResultTypeDef](#createstreamingdistributionresulttypedef)
  - [CreateStreamingDistributionWithTagsResultTypeDef](#createstreamingdistributionwithtagsresulttypedef)
  - [CustomErrorResponseTypeDef](#customerrorresponsetypedef)
  - [CustomErrorResponsesTypeDef](#customerrorresponsestypedef)
  - [CustomHeadersTypeDef](#customheaderstypedef)
  - [CustomOriginConfigTypeDef](#customoriginconfigtypedef)
  - [DefaultCacheBehaviorTypeDef](#defaultcachebehaviortypedef)
  - [DescribeFunctionResultTypeDef](#describefunctionresulttypedef)
  - [DistributionConfigTypeDef](#distributionconfigtypedef)
  - [DistributionConfigWithTagsTypeDef](#distributionconfigwithtagstypedef)
  - [DistributionIdListTypeDef](#distributionidlisttypedef)
  - [DistributionListTypeDef](#distributionlisttypedef)
  - [DistributionSummaryTypeDef](#distributionsummarytypedef)
  - [DistributionTypeDef](#distributiontypedef)
  - [EncryptionEntitiesTypeDef](#encryptionentitiestypedef)
  - [EncryptionEntityTypeDef](#encryptionentitytypedef)
  - [EndPointTypeDef](#endpointtypedef)
  - [FieldLevelEncryptionConfigTypeDef](#fieldlevelencryptionconfigtypedef)
  - [FieldLevelEncryptionListTypeDef](#fieldlevelencryptionlisttypedef)
  - [FieldLevelEncryptionProfileConfigTypeDef](#fieldlevelencryptionprofileconfigtypedef)
  - [FieldLevelEncryptionProfileListTypeDef](#fieldlevelencryptionprofilelisttypedef)
  - [FieldLevelEncryptionProfileSummaryTypeDef](#fieldlevelencryptionprofilesummarytypedef)
  - [FieldLevelEncryptionProfileTypeDef](#fieldlevelencryptionprofiletypedef)
  - [FieldLevelEncryptionSummaryTypeDef](#fieldlevelencryptionsummarytypedef)
  - [FieldLevelEncryptionTypeDef](#fieldlevelencryptiontypedef)
  - [FieldPatternsTypeDef](#fieldpatternstypedef)
  - [ForwardedValuesTypeDef](#forwardedvaluestypedef)
  - [FunctionAssociationTypeDef](#functionassociationtypedef)
  - [FunctionAssociationsTypeDef](#functionassociationstypedef)
  - [FunctionConfigTypeDef](#functionconfigtypedef)
  - [FunctionListTypeDef](#functionlisttypedef)
  - [FunctionMetadataTypeDef](#functionmetadatatypedef)
  - [FunctionSummaryTypeDef](#functionsummarytypedef)
  - [GeoRestrictionTypeDef](#georestrictiontypedef)
  - [GetCachePolicyConfigResultTypeDef](#getcachepolicyconfigresulttypedef)
  - [GetCachePolicyResultTypeDef](#getcachepolicyresulttypedef)
  - [GetCloudFrontOriginAccessIdentityConfigResultTypeDef](#getcloudfrontoriginaccessidentityconfigresulttypedef)
  - [GetCloudFrontOriginAccessIdentityResultTypeDef](#getcloudfrontoriginaccessidentityresulttypedef)
  - [GetDistributionConfigResultTypeDef](#getdistributionconfigresulttypedef)
  - [GetDistributionResultTypeDef](#getdistributionresulttypedef)
  - [GetFieldLevelEncryptionConfigResultTypeDef](#getfieldlevelencryptionconfigresulttypedef)
  - [GetFieldLevelEncryptionProfileConfigResultTypeDef](#getfieldlevelencryptionprofileconfigresulttypedef)
  - [GetFieldLevelEncryptionProfileResultTypeDef](#getfieldlevelencryptionprofileresulttypedef)
  - [GetFieldLevelEncryptionResultTypeDef](#getfieldlevelencryptionresulttypedef)
  - [GetFunctionResultTypeDef](#getfunctionresulttypedef)
  - [GetInvalidationResultTypeDef](#getinvalidationresulttypedef)
  - [GetKeyGroupConfigResultTypeDef](#getkeygroupconfigresulttypedef)
  - [GetKeyGroupResultTypeDef](#getkeygroupresulttypedef)
  - [GetMonitoringSubscriptionResultTypeDef](#getmonitoringsubscriptionresulttypedef)
  - [GetOriginRequestPolicyConfigResultTypeDef](#getoriginrequestpolicyconfigresulttypedef)
  - [GetOriginRequestPolicyResultTypeDef](#getoriginrequestpolicyresulttypedef)
  - [GetPublicKeyConfigResultTypeDef](#getpublickeyconfigresulttypedef)
  - [GetPublicKeyResultTypeDef](#getpublickeyresulttypedef)
  - [GetRealtimeLogConfigResultTypeDef](#getrealtimelogconfigresulttypedef)
  - [GetStreamingDistributionConfigResultTypeDef](#getstreamingdistributionconfigresulttypedef)
  - [GetStreamingDistributionResultTypeDef](#getstreamingdistributionresulttypedef)
  - [HeadersTypeDef](#headerstypedef)
  - [InvalidationBatchTypeDef](#invalidationbatchtypedef)
  - [InvalidationListTypeDef](#invalidationlisttypedef)
  - [InvalidationSummaryTypeDef](#invalidationsummarytypedef)
  - [InvalidationTypeDef](#invalidationtypedef)
  - [KGKeyPairIdsTypeDef](#kgkeypairidstypedef)
  - [KeyGroupConfigTypeDef](#keygroupconfigtypedef)
  - [KeyGroupListTypeDef](#keygrouplisttypedef)
  - [KeyGroupSummaryTypeDef](#keygroupsummarytypedef)
  - [KeyGroupTypeDef](#keygrouptypedef)
  - [KeyPairIdsTypeDef](#keypairidstypedef)
  - [KinesisStreamConfigTypeDef](#kinesisstreamconfigtypedef)
  - [LambdaFunctionAssociationTypeDef](#lambdafunctionassociationtypedef)
  - [LambdaFunctionAssociationsTypeDef](#lambdafunctionassociationstypedef)
  - [ListCachePoliciesResultTypeDef](#listcachepoliciesresulttypedef)
  - [ListCloudFrontOriginAccessIdentitiesResultTypeDef](#listcloudfrontoriginaccessidentitiesresulttypedef)
  - [ListDistributionsByCachePolicyIdResultTypeDef](#listdistributionsbycachepolicyidresulttypedef)
  - [ListDistributionsByKeyGroupResultTypeDef](#listdistributionsbykeygroupresulttypedef)
  - [ListDistributionsByOriginRequestPolicyIdResultTypeDef](#listdistributionsbyoriginrequestpolicyidresulttypedef)
  - [ListDistributionsByRealtimeLogConfigResultTypeDef](#listdistributionsbyrealtimelogconfigresulttypedef)
  - [ListDistributionsByWebACLIdResultTypeDef](#listdistributionsbywebaclidresulttypedef)
  - [ListDistributionsResultTypeDef](#listdistributionsresulttypedef)
  - [ListFieldLevelEncryptionConfigsResultTypeDef](#listfieldlevelencryptionconfigsresulttypedef)
  - [ListFieldLevelEncryptionProfilesResultTypeDef](#listfieldlevelencryptionprofilesresulttypedef)
  - [ListFunctionsResultTypeDef](#listfunctionsresulttypedef)
  - [ListInvalidationsResultTypeDef](#listinvalidationsresulttypedef)
  - [ListKeyGroupsResultTypeDef](#listkeygroupsresulttypedef)
  - [ListOriginRequestPoliciesResultTypeDef](#listoriginrequestpoliciesresulttypedef)
  - [ListPublicKeysResultTypeDef](#listpublickeysresulttypedef)
  - [ListRealtimeLogConfigsResultTypeDef](#listrealtimelogconfigsresulttypedef)
  - [ListStreamingDistributionsResultTypeDef](#liststreamingdistributionsresulttypedef)
  - [ListTagsForResourceResultTypeDef](#listtagsforresourceresulttypedef)
  - [LoggingConfigTypeDef](#loggingconfigtypedef)
  - [MonitoringSubscriptionTypeDef](#monitoringsubscriptiontypedef)
  - [OriginCustomHeaderTypeDef](#origincustomheadertypedef)
  - [OriginGroupFailoverCriteriaTypeDef](#origingroupfailovercriteriatypedef)
  - [OriginGroupMemberTypeDef](#origingroupmembertypedef)
  - [OriginGroupMembersTypeDef](#origingroupmemberstypedef)
  - [OriginGroupTypeDef](#origingrouptypedef)
  - [OriginGroupsTypeDef](#origingroupstypedef)
  - [OriginRequestPolicyConfigTypeDef](#originrequestpolicyconfigtypedef)
  - [OriginRequestPolicyCookiesConfigTypeDef](#originrequestpolicycookiesconfigtypedef)
  - [OriginRequestPolicyHeadersConfigTypeDef](#originrequestpolicyheadersconfigtypedef)
  - [OriginRequestPolicyListTypeDef](#originrequestpolicylisttypedef)
  - [OriginRequestPolicyQueryStringsConfigTypeDef](#originrequestpolicyquerystringsconfigtypedef)
  - [OriginRequestPolicySummaryTypeDef](#originrequestpolicysummarytypedef)
  - [OriginRequestPolicyTypeDef](#originrequestpolicytypedef)
  - [OriginShieldTypeDef](#originshieldtypedef)
  - [OriginSslProtocolsTypeDef](#originsslprotocolstypedef)
  - [OriginTypeDef](#origintypedef)
  - [OriginsTypeDef](#originstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ParametersInCacheKeyAndForwardedToOriginTypeDef](#parametersincachekeyandforwardedtoorigintypedef)
  - [PathsTypeDef](#pathstypedef)
  - [PublicKeyConfigTypeDef](#publickeyconfigtypedef)
  - [PublicKeyListTypeDef](#publickeylisttypedef)
  - [PublicKeySummaryTypeDef](#publickeysummarytypedef)
  - [PublicKeyTypeDef](#publickeytypedef)
  - [PublishFunctionResultTypeDef](#publishfunctionresulttypedef)
  - [QueryArgProfileConfigTypeDef](#queryargprofileconfigtypedef)
  - [QueryArgProfileTypeDef](#queryargprofiletypedef)
  - [QueryArgProfilesTypeDef](#queryargprofilestypedef)
  - [QueryStringCacheKeysTypeDef](#querystringcachekeystypedef)
  - [QueryStringNamesTypeDef](#querystringnamestypedef)
  - [RealtimeLogConfigTypeDef](#realtimelogconfigtypedef)
  - [RealtimeLogConfigsTypeDef](#realtimelogconfigstypedef)
  - [RealtimeMetricsSubscriptionConfigTypeDef](#realtimemetricssubscriptionconfigtypedef)
  - [RestrictionsTypeDef](#restrictionstypedef)
  - [S3OriginConfigTypeDef](#s3originconfigtypedef)
  - [S3OriginTypeDef](#s3origintypedef)
  - [SignerTypeDef](#signertypedef)
  - [StatusCodesTypeDef](#statuscodestypedef)
  - [StreamingDistributionConfigTypeDef](#streamingdistributionconfigtypedef)
  - [StreamingDistributionConfigWithTagsTypeDef](#streamingdistributionconfigwithtagstypedef)
  - [StreamingDistributionListTypeDef](#streamingdistributionlisttypedef)
  - [StreamingDistributionSummaryTypeDef](#streamingdistributionsummarytypedef)
  - [StreamingDistributionTypeDef](#streamingdistributiontypedef)
  - [StreamingLoggingConfigTypeDef](#streamingloggingconfigtypedef)
  - [TagKeysTypeDef](#tagkeystypedef)
  - [TagTypeDef](#tagtypedef)
  - [TagsTypeDef](#tagstypedef)
  - [TestFunctionResultTypeDef](#testfunctionresulttypedef)
  - [TestResultTypeDef](#testresulttypedef)
  - [TrustedKeyGroupsTypeDef](#trustedkeygroupstypedef)
  - [TrustedSignersTypeDef](#trustedsignerstypedef)
  - [UpdateCachePolicyResultTypeDef](#updatecachepolicyresulttypedef)
  - [UpdateCloudFrontOriginAccessIdentityResultTypeDef](#updatecloudfrontoriginaccessidentityresulttypedef)
  - [UpdateDistributionResultTypeDef](#updatedistributionresulttypedef)
  - [UpdateFieldLevelEncryptionConfigResultTypeDef](#updatefieldlevelencryptionconfigresulttypedef)
  - [UpdateFieldLevelEncryptionProfileResultTypeDef](#updatefieldlevelencryptionprofileresulttypedef)
  - [UpdateFunctionResultTypeDef](#updatefunctionresulttypedef)
  - [UpdateKeyGroupResultTypeDef](#updatekeygroupresulttypedef)
  - [UpdateOriginRequestPolicyResultTypeDef](#updateoriginrequestpolicyresulttypedef)
  - [UpdatePublicKeyResultTypeDef](#updatepublickeyresulttypedef)
  - [UpdateRealtimeLogConfigResultTypeDef](#updaterealtimelogconfigresulttypedef)
  - [UpdateStreamingDistributionResultTypeDef](#updatestreamingdistributionresulttypedef)
  - [ViewerCertificateTypeDef](#viewercertificatetypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ActiveTrustedKeyGroupsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ActiveTrustedKeyGroupsTypeDef
```


Required fields:
- `Enabled`: `bool`
- `Quantity`: `int`



Optional fields:
- `Items`: `List["KGKeyPairIdsTypeDef"]`


## ActiveTrustedSignersTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ActiveTrustedSignersTypeDef
```


Required fields:
- `Enabled`: `bool`
- `Quantity`: `int`



Optional fields:
- `Items`: `List["SignerTypeDef"]`


## AliasICPRecordalTypeDef

```python
from mypy_boto3_cloudfront.type_defs import AliasICPRecordalTypeDef
```




Optional fields:
- `CNAME`: `str`
- `ICPRecordalStatus`: `ICPRecordalStatus`


## AliasesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import AliasesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## AllowedMethodsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import AllowedMethodsTypeDef
```


Required fields:
- `Quantity`: `int`
- `Items`: `List[Method]`



Optional fields:
- `CachedMethods`: `"CachedMethodsTypeDef"`


## CacheBehaviorTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CacheBehaviorTypeDef
```


Required fields:
- `PathPattern`: `str`
- `TargetOriginId`: `str`
- `ViewerProtocolPolicy`: `ViewerProtocolPolicy`



Optional fields:
- `TrustedSigners`: `"TrustedSignersTypeDef"`
- `TrustedKeyGroups`: `"TrustedKeyGroupsTypeDef"`
- `AllowedMethods`: `"AllowedMethodsTypeDef"`
- `SmoothStreaming`: `bool`
- `Compress`: `bool`
- `LambdaFunctionAssociations`: `"LambdaFunctionAssociationsTypeDef"`
- `FunctionAssociations`: `"FunctionAssociationsTypeDef"`
- `FieldLevelEncryptionId`: `str`
- `RealtimeLogConfigArn`: `str`
- `CachePolicyId`: `str`
- `OriginRequestPolicyId`: `str`
- `ForwardedValues`: `"ForwardedValuesTypeDef"`
- `MinTTL`: `int`
- `DefaultTTL`: `int`
- `MaxTTL`: `int`


## CacheBehaviorsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CacheBehaviorsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["CacheBehaviorTypeDef"]`


## CachePolicyConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicyConfigTypeDef
```


Required fields:
- `Name`: `str`
- `MinTTL`: `int`



Optional fields:
- `Comment`: `str`
- `DefaultTTL`: `int`
- `MaxTTL`: `int`
- `ParametersInCacheKeyAndForwardedToOrigin`: `"ParametersInCacheKeyAndForwardedToOriginTypeDef"`


## CachePolicyCookiesConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicyCookiesConfigTypeDef
```


Required fields:
- `CookieBehavior`: `CachePolicyCookieBehavior`



Optional fields:
- `Cookies`: `"CookieNamesTypeDef"`


## CachePolicyHeadersConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicyHeadersConfigTypeDef
```


Required fields:
- `HeaderBehavior`: `CachePolicyHeaderBehavior`



Optional fields:
- `Headers`: `"HeadersTypeDef"`


## CachePolicyListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicyListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["CachePolicySummaryTypeDef"]`


## CachePolicyQueryStringsConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicyQueryStringsConfigTypeDef
```


Required fields:
- `QueryStringBehavior`: `CachePolicyQueryStringBehavior`



Optional fields:
- `QueryStrings`: `"QueryStringNamesTypeDef"`


## CachePolicySummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicySummaryTypeDef
```


Required fields:
- `Type`: `CachePolicyType`
- `CachePolicy`: `"CachePolicyTypeDef"`




## CachePolicyTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachePolicyTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`
- `CachePolicyConfig`: `"CachePolicyConfigTypeDef"`




## CachedMethodsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CachedMethodsTypeDef
```


Required fields:
- `Quantity`: `int`
- `Items`: `List[Method]`




## CloudFrontOriginAccessIdentityConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CloudFrontOriginAccessIdentityConfigTypeDef
```


Required fields:
- `CallerReference`: `str`
- `Comment`: `str`




## CloudFrontOriginAccessIdentityListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CloudFrontOriginAccessIdentityListTypeDef
```


Required fields:
- `Marker`: `str`
- `MaxItems`: `int`
- `IsTruncated`: `bool`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["CloudFrontOriginAccessIdentitySummaryTypeDef"]`


## CloudFrontOriginAccessIdentitySummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CloudFrontOriginAccessIdentitySummaryTypeDef
```


Required fields:
- `Id`: `str`
- `S3CanonicalUserId`: `str`
- `Comment`: `str`




## CloudFrontOriginAccessIdentityTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CloudFrontOriginAccessIdentityTypeDef
```


Required fields:
- `Id`: `str`
- `S3CanonicalUserId`: `str`



Optional fields:
- `CloudFrontOriginAccessIdentityConfig`: `"CloudFrontOriginAccessIdentityConfigTypeDef"`


## ContentTypeProfileConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ContentTypeProfileConfigTypeDef
```


Required fields:
- `ForwardWhenContentTypeIsUnknown`: `bool`



Optional fields:
- `ContentTypeProfiles`: `"ContentTypeProfilesTypeDef"`


## ContentTypeProfileTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ContentTypeProfileTypeDef
```


Required fields:
- `Format`: `Literal['URLEncoded']`
- `ContentType`: `str`



Optional fields:
- `ProfileId`: `str`


## ContentTypeProfilesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ContentTypeProfilesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["ContentTypeProfileTypeDef"]`


## CookieNamesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CookieNamesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## CookiePreferenceTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CookiePreferenceTypeDef
```


Required fields:
- `Forward`: `ItemSelection`



Optional fields:
- `WhitelistedNames`: `"CookieNamesTypeDef"`


## CreateCachePolicyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateCachePolicyResultTypeDef
```




Optional fields:
- `CachePolicy`: `"CachePolicyTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateCloudFrontOriginAccessIdentityResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateCloudFrontOriginAccessIdentityResultTypeDef
```




Optional fields:
- `CloudFrontOriginAccessIdentity`: `"CloudFrontOriginAccessIdentityTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateDistributionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateDistributionResultTypeDef
```




Optional fields:
- `Distribution`: `"DistributionTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateDistributionWithTagsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateDistributionWithTagsResultTypeDef
```




Optional fields:
- `Distribution`: `"DistributionTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateFieldLevelEncryptionConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateFieldLevelEncryptionConfigResultTypeDef
```




Optional fields:
- `FieldLevelEncryption`: `"FieldLevelEncryptionTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateFieldLevelEncryptionProfileResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateFieldLevelEncryptionProfileResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionProfile`: `"FieldLevelEncryptionProfileTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateFunctionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateFunctionResultTypeDef
```




Optional fields:
- `FunctionSummary`: `"FunctionSummaryTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateInvalidationResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateInvalidationResultTypeDef
```




Optional fields:
- `Location`: `str`
- `Invalidation`: `"InvalidationTypeDef"`


## CreateKeyGroupResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateKeyGroupResultTypeDef
```




Optional fields:
- `KeyGroup`: `"KeyGroupTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateMonitoringSubscriptionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateMonitoringSubscriptionResultTypeDef
```




Optional fields:
- `MonitoringSubscription`: `"MonitoringSubscriptionTypeDef"`


## CreateOriginRequestPolicyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateOriginRequestPolicyResultTypeDef
```




Optional fields:
- `OriginRequestPolicy`: `"OriginRequestPolicyTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreatePublicKeyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreatePublicKeyResultTypeDef
```




Optional fields:
- `PublicKey`: `"PublicKeyTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateRealtimeLogConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateRealtimeLogConfigResultTypeDef
```




Optional fields:
- `RealtimeLogConfig`: `"RealtimeLogConfigTypeDef"`


## CreateStreamingDistributionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateStreamingDistributionResultTypeDef
```




Optional fields:
- `StreamingDistribution`: `"StreamingDistributionTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CreateStreamingDistributionWithTagsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CreateStreamingDistributionWithTagsResultTypeDef
```




Optional fields:
- `StreamingDistribution`: `"StreamingDistributionTypeDef"`
- `Location`: `str`
- `ETag`: `str`


## CustomErrorResponseTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CustomErrorResponseTypeDef
```


Required fields:
- `ErrorCode`: `int`



Optional fields:
- `ResponsePagePath`: `str`
- `ResponseCode`: `str`
- `ErrorCachingMinTTL`: `int`


## CustomErrorResponsesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CustomErrorResponsesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["CustomErrorResponseTypeDef"]`


## CustomHeadersTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CustomHeadersTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["OriginCustomHeaderTypeDef"]`


## CustomOriginConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import CustomOriginConfigTypeDef
```


Required fields:
- `HTTPPort`: `int`
- `HTTPSPort`: `int`
- `OriginProtocolPolicy`: `OriginProtocolPolicy`



Optional fields:
- `OriginSslProtocols`: `"OriginSslProtocolsTypeDef"`
- `OriginReadTimeout`: `int`
- `OriginKeepaliveTimeout`: `int`


## DefaultCacheBehaviorTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DefaultCacheBehaviorTypeDef
```


Required fields:
- `TargetOriginId`: `str`
- `ViewerProtocolPolicy`: `ViewerProtocolPolicy`



Optional fields:
- `TrustedSigners`: `"TrustedSignersTypeDef"`
- `TrustedKeyGroups`: `"TrustedKeyGroupsTypeDef"`
- `AllowedMethods`: `"AllowedMethodsTypeDef"`
- `SmoothStreaming`: `bool`
- `Compress`: `bool`
- `LambdaFunctionAssociations`: `"LambdaFunctionAssociationsTypeDef"`
- `FunctionAssociations`: `"FunctionAssociationsTypeDef"`
- `FieldLevelEncryptionId`: `str`
- `RealtimeLogConfigArn`: `str`
- `CachePolicyId`: `str`
- `OriginRequestPolicyId`: `str`
- `ForwardedValues`: `"ForwardedValuesTypeDef"`
- `MinTTL`: `int`
- `DefaultTTL`: `int`
- `MaxTTL`: `int`


## DescribeFunctionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DescribeFunctionResultTypeDef
```




Optional fields:
- `FunctionSummary`: `"FunctionSummaryTypeDef"`
- `ETag`: `str`


## DistributionConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DistributionConfigTypeDef
```


Required fields:
- `CallerReference`: `str`
- `Origins`: `"OriginsTypeDef"`
- `DefaultCacheBehavior`: `"DefaultCacheBehaviorTypeDef"`
- `Comment`: `str`
- `Enabled`: `bool`



Optional fields:
- `Aliases`: `"AliasesTypeDef"`
- `DefaultRootObject`: `str`
- `OriginGroups`: `"OriginGroupsTypeDef"`
- `CacheBehaviors`: `"CacheBehaviorsTypeDef"`
- `CustomErrorResponses`: `"CustomErrorResponsesTypeDef"`
- `Logging`: `"LoggingConfigTypeDef"`
- `PriceClass`: `PriceClass`
- `ViewerCertificate`: `"ViewerCertificateTypeDef"`
- `Restrictions`: `"RestrictionsTypeDef"`
- `WebACLId`: `str`
- `HttpVersion`: `HttpVersion`
- `IsIPV6Enabled`: `bool`


## DistributionConfigWithTagsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DistributionConfigWithTagsTypeDef
```


Required fields:
- `DistributionConfig`: `"DistributionConfigTypeDef"`
- `Tags`: `"TagsTypeDef"`




## DistributionIdListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DistributionIdListTypeDef
```


Required fields:
- `Marker`: `str`
- `MaxItems`: `int`
- `IsTruncated`: `bool`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List[str]`


## DistributionListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DistributionListTypeDef
```


Required fields:
- `Marker`: `str`
- `MaxItems`: `int`
- `IsTruncated`: `bool`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["DistributionSummaryTypeDef"]`


## DistributionSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DistributionSummaryTypeDef
```


Required fields:
- `Id`: `str`
- `ARN`: `str`
- `Status`: `str`
- `LastModifiedTime`: `datetime`
- `DomainName`: `str`
- `Aliases`: `"AliasesTypeDef"`
- `Origins`: `"OriginsTypeDef"`
- `DefaultCacheBehavior`: `"DefaultCacheBehaviorTypeDef"`
- `CacheBehaviors`: `"CacheBehaviorsTypeDef"`
- `CustomErrorResponses`: `"CustomErrorResponsesTypeDef"`
- `Comment`: `str`
- `PriceClass`: `PriceClass`
- `Enabled`: `bool`
- `ViewerCertificate`: `"ViewerCertificateTypeDef"`
- `Restrictions`: `"RestrictionsTypeDef"`
- `WebACLId`: `str`
- `HttpVersion`: `HttpVersion`
- `IsIPV6Enabled`: `bool`



Optional fields:
- `OriginGroups`: `"OriginGroupsTypeDef"`
- `AliasICPRecordals`: `List["AliasICPRecordalTypeDef"]`


## DistributionTypeDef

```python
from mypy_boto3_cloudfront.type_defs import DistributionTypeDef
```


Required fields:
- `Id`: `str`
- `ARN`: `str`
- `Status`: `str`
- `LastModifiedTime`: `datetime`
- `InProgressInvalidationBatches`: `int`
- `DomainName`: `str`
- `DistributionConfig`: `"DistributionConfigTypeDef"`



Optional fields:
- `ActiveTrustedSigners`: `"ActiveTrustedSignersTypeDef"`
- `ActiveTrustedKeyGroups`: `"ActiveTrustedKeyGroupsTypeDef"`
- `AliasICPRecordals`: `List["AliasICPRecordalTypeDef"]`


## EncryptionEntitiesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import EncryptionEntitiesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["EncryptionEntityTypeDef"]`


## EncryptionEntityTypeDef

```python
from mypy_boto3_cloudfront.type_defs import EncryptionEntityTypeDef
```


Required fields:
- `PublicKeyId`: `str`
- `ProviderId`: `str`
- `FieldPatterns`: `"FieldPatternsTypeDef"`




## EndPointTypeDef

```python
from mypy_boto3_cloudfront.type_defs import EndPointTypeDef
```


Required fields:
- `StreamType`: `str`



Optional fields:
- `KinesisStreamConfig`: `"KinesisStreamConfigTypeDef"`


## FieldLevelEncryptionConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionConfigTypeDef
```


Required fields:
- `CallerReference`: `str`



Optional fields:
- `Comment`: `str`
- `QueryArgProfileConfig`: `"QueryArgProfileConfigTypeDef"`
- `ContentTypeProfileConfig`: `"ContentTypeProfileConfigTypeDef"`


## FieldLevelEncryptionListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["FieldLevelEncryptionSummaryTypeDef"]`


## FieldLevelEncryptionProfileConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionProfileConfigTypeDef
```


Required fields:
- `Name`: `str`
- `CallerReference`: `str`
- `EncryptionEntities`: `"EncryptionEntitiesTypeDef"`



Optional fields:
- `Comment`: `str`


## FieldLevelEncryptionProfileListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionProfileListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["FieldLevelEncryptionProfileSummaryTypeDef"]`


## FieldLevelEncryptionProfileSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionProfileSummaryTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`
- `Name`: `str`
- `EncryptionEntities`: `"EncryptionEntitiesTypeDef"`



Optional fields:
- `Comment`: `str`


## FieldLevelEncryptionProfileTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionProfileTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`
- `FieldLevelEncryptionProfileConfig`: `"FieldLevelEncryptionProfileConfigTypeDef"`




## FieldLevelEncryptionSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionSummaryTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`



Optional fields:
- `Comment`: `str`
- `QueryArgProfileConfig`: `"QueryArgProfileConfigTypeDef"`
- `ContentTypeProfileConfig`: `"ContentTypeProfileConfigTypeDef"`


## FieldLevelEncryptionTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldLevelEncryptionTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`
- `FieldLevelEncryptionConfig`: `"FieldLevelEncryptionConfigTypeDef"`




## FieldPatternsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FieldPatternsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## ForwardedValuesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ForwardedValuesTypeDef
```


Required fields:
- `QueryString`: `bool`
- `Cookies`: `"CookiePreferenceTypeDef"`



Optional fields:
- `Headers`: `"HeadersTypeDef"`
- `QueryStringCacheKeys`: `"QueryStringCacheKeysTypeDef"`


## FunctionAssociationTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FunctionAssociationTypeDef
```


Required fields:
- `FunctionARN`: `str`
- `EventType`: `EventType`




## FunctionAssociationsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FunctionAssociationsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["FunctionAssociationTypeDef"]`


## FunctionConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FunctionConfigTypeDef
```


Required fields:
- `Comment`: `str`
- `Runtime`: `Literal['cloudfront-js-1.0']`




## FunctionListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FunctionListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["FunctionSummaryTypeDef"]`


## FunctionMetadataTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FunctionMetadataTypeDef
```


Required fields:
- `FunctionARN`: `str`
- `LastModifiedTime`: `datetime`



Optional fields:
- `Stage`: `FunctionStage`
- `CreatedTime`: `datetime`


## FunctionSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import FunctionSummaryTypeDef
```


Required fields:
- `Name`: `str`
- `FunctionConfig`: `"FunctionConfigTypeDef"`
- `FunctionMetadata`: `"FunctionMetadataTypeDef"`



Optional fields:
- `Status`: `str`


## GeoRestrictionTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GeoRestrictionTypeDef
```


Required fields:
- `RestrictionType`: `GeoRestrictionType`
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## GetCachePolicyConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetCachePolicyConfigResultTypeDef
```




Optional fields:
- `CachePolicyConfig`: `"CachePolicyConfigTypeDef"`
- `ETag`: `str`


## GetCachePolicyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetCachePolicyResultTypeDef
```




Optional fields:
- `CachePolicy`: `"CachePolicyTypeDef"`
- `ETag`: `str`


## GetCloudFrontOriginAccessIdentityConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetCloudFrontOriginAccessIdentityConfigResultTypeDef
```




Optional fields:
- `CloudFrontOriginAccessIdentityConfig`: `"CloudFrontOriginAccessIdentityConfigTypeDef"`
- `ETag`: `str`


## GetCloudFrontOriginAccessIdentityResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetCloudFrontOriginAccessIdentityResultTypeDef
```




Optional fields:
- `CloudFrontOriginAccessIdentity`: `"CloudFrontOriginAccessIdentityTypeDef"`
- `ETag`: `str`


## GetDistributionConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetDistributionConfigResultTypeDef
```




Optional fields:
- `DistributionConfig`: `"DistributionConfigTypeDef"`
- `ETag`: `str`


## GetDistributionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetDistributionResultTypeDef
```




Optional fields:
- `Distribution`: `"DistributionTypeDef"`
- `ETag`: `str`


## GetFieldLevelEncryptionConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetFieldLevelEncryptionConfigResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionConfig`: `"FieldLevelEncryptionConfigTypeDef"`
- `ETag`: `str`


## GetFieldLevelEncryptionProfileConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetFieldLevelEncryptionProfileConfigResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionProfileConfig`: `"FieldLevelEncryptionProfileConfigTypeDef"`
- `ETag`: `str`


## GetFieldLevelEncryptionProfileResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetFieldLevelEncryptionProfileResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionProfile`: `"FieldLevelEncryptionProfileTypeDef"`
- `ETag`: `str`


## GetFieldLevelEncryptionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetFieldLevelEncryptionResultTypeDef
```




Optional fields:
- `FieldLevelEncryption`: `"FieldLevelEncryptionTypeDef"`
- `ETag`: `str`


## GetFunctionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetFunctionResultTypeDef
```




Optional fields:
- `FunctionCode`: `Union[bytes, IO[bytes]]`
- `ETag`: `str`
- `ContentType`: `str`


## GetInvalidationResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetInvalidationResultTypeDef
```




Optional fields:
- `Invalidation`: `"InvalidationTypeDef"`


## GetKeyGroupConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetKeyGroupConfigResultTypeDef
```




Optional fields:
- `KeyGroupConfig`: `"KeyGroupConfigTypeDef"`
- `ETag`: `str`


## GetKeyGroupResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetKeyGroupResultTypeDef
```




Optional fields:
- `KeyGroup`: `"KeyGroupTypeDef"`
- `ETag`: `str`


## GetMonitoringSubscriptionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetMonitoringSubscriptionResultTypeDef
```




Optional fields:
- `MonitoringSubscription`: `"MonitoringSubscriptionTypeDef"`


## GetOriginRequestPolicyConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetOriginRequestPolicyConfigResultTypeDef
```




Optional fields:
- `OriginRequestPolicyConfig`: `"OriginRequestPolicyConfigTypeDef"`
- `ETag`: `str`


## GetOriginRequestPolicyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetOriginRequestPolicyResultTypeDef
```




Optional fields:
- `OriginRequestPolicy`: `"OriginRequestPolicyTypeDef"`
- `ETag`: `str`


## GetPublicKeyConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetPublicKeyConfigResultTypeDef
```




Optional fields:
- `PublicKeyConfig`: `"PublicKeyConfigTypeDef"`
- `ETag`: `str`


## GetPublicKeyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetPublicKeyResultTypeDef
```




Optional fields:
- `PublicKey`: `"PublicKeyTypeDef"`
- `ETag`: `str`


## GetRealtimeLogConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetRealtimeLogConfigResultTypeDef
```




Optional fields:
- `RealtimeLogConfig`: `"RealtimeLogConfigTypeDef"`


## GetStreamingDistributionConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetStreamingDistributionConfigResultTypeDef
```




Optional fields:
- `StreamingDistributionConfig`: `"StreamingDistributionConfigTypeDef"`
- `ETag`: `str`


## GetStreamingDistributionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import GetStreamingDistributionResultTypeDef
```




Optional fields:
- `StreamingDistribution`: `"StreamingDistributionTypeDef"`
- `ETag`: `str`


## HeadersTypeDef

```python
from mypy_boto3_cloudfront.type_defs import HeadersTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## InvalidationBatchTypeDef

```python
from mypy_boto3_cloudfront.type_defs import InvalidationBatchTypeDef
```


Required fields:
- `Paths`: `"PathsTypeDef"`
- `CallerReference`: `str`




## InvalidationListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import InvalidationListTypeDef
```


Required fields:
- `Marker`: `str`
- `MaxItems`: `int`
- `IsTruncated`: `bool`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["InvalidationSummaryTypeDef"]`


## InvalidationSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import InvalidationSummaryTypeDef
```


Required fields:
- `Id`: `str`
- `CreateTime`: `datetime`
- `Status`: `str`




## InvalidationTypeDef

```python
from mypy_boto3_cloudfront.type_defs import InvalidationTypeDef
```


Required fields:
- `Id`: `str`
- `Status`: `str`
- `CreateTime`: `datetime`
- `InvalidationBatch`: `"InvalidationBatchTypeDef"`




## KGKeyPairIdsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KGKeyPairIdsTypeDef
```




Optional fields:
- `KeyGroupId`: `str`
- `KeyPairIds`: `"KeyPairIdsTypeDef"`


## KeyGroupConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KeyGroupConfigTypeDef
```


Required fields:
- `Name`: `str`
- `Items`: `List[str]`



Optional fields:
- `Comment`: `str`


## KeyGroupListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KeyGroupListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["KeyGroupSummaryTypeDef"]`


## KeyGroupSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KeyGroupSummaryTypeDef
```


Required fields:
- `KeyGroup`: `"KeyGroupTypeDef"`




## KeyGroupTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KeyGroupTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`
- `KeyGroupConfig`: `"KeyGroupConfigTypeDef"`




## KeyPairIdsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KeyPairIdsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## KinesisStreamConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import KinesisStreamConfigTypeDef
```


Required fields:
- `RoleARN`: `str`
- `StreamARN`: `str`




## LambdaFunctionAssociationTypeDef

```python
from mypy_boto3_cloudfront.type_defs import LambdaFunctionAssociationTypeDef
```


Required fields:
- `LambdaFunctionARN`: `str`
- `EventType`: `EventType`



Optional fields:
- `IncludeBody`: `bool`


## LambdaFunctionAssociationsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import LambdaFunctionAssociationsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["LambdaFunctionAssociationTypeDef"]`


## ListCachePoliciesResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListCachePoliciesResultTypeDef
```




Optional fields:
- `CachePolicyList`: `"CachePolicyListTypeDef"`


## ListCloudFrontOriginAccessIdentitiesResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListCloudFrontOriginAccessIdentitiesResultTypeDef
```




Optional fields:
- `CloudFrontOriginAccessIdentityList`: `"CloudFrontOriginAccessIdentityListTypeDef"`


## ListDistributionsByCachePolicyIdResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListDistributionsByCachePolicyIdResultTypeDef
```




Optional fields:
- `DistributionIdList`: `"DistributionIdListTypeDef"`


## ListDistributionsByKeyGroupResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListDistributionsByKeyGroupResultTypeDef
```




Optional fields:
- `DistributionIdList`: `"DistributionIdListTypeDef"`


## ListDistributionsByOriginRequestPolicyIdResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListDistributionsByOriginRequestPolicyIdResultTypeDef
```




Optional fields:
- `DistributionIdList`: `"DistributionIdListTypeDef"`


## ListDistributionsByRealtimeLogConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListDistributionsByRealtimeLogConfigResultTypeDef
```




Optional fields:
- `DistributionList`: `"DistributionListTypeDef"`


## ListDistributionsByWebACLIdResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListDistributionsByWebACLIdResultTypeDef
```




Optional fields:
- `DistributionList`: `"DistributionListTypeDef"`


## ListDistributionsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListDistributionsResultTypeDef
```




Optional fields:
- `DistributionList`: `"DistributionListTypeDef"`


## ListFieldLevelEncryptionConfigsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListFieldLevelEncryptionConfigsResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionList`: `"FieldLevelEncryptionListTypeDef"`


## ListFieldLevelEncryptionProfilesResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListFieldLevelEncryptionProfilesResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionProfileList`: `"FieldLevelEncryptionProfileListTypeDef"`


## ListFunctionsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListFunctionsResultTypeDef
```




Optional fields:
- `FunctionList`: `"FunctionListTypeDef"`


## ListInvalidationsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListInvalidationsResultTypeDef
```




Optional fields:
- `InvalidationList`: `"InvalidationListTypeDef"`


## ListKeyGroupsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListKeyGroupsResultTypeDef
```




Optional fields:
- `KeyGroupList`: `"KeyGroupListTypeDef"`


## ListOriginRequestPoliciesResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListOriginRequestPoliciesResultTypeDef
```




Optional fields:
- `OriginRequestPolicyList`: `"OriginRequestPolicyListTypeDef"`


## ListPublicKeysResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListPublicKeysResultTypeDef
```




Optional fields:
- `PublicKeyList`: `"PublicKeyListTypeDef"`


## ListRealtimeLogConfigsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListRealtimeLogConfigsResultTypeDef
```




Optional fields:
- `RealtimeLogConfigs`: `"RealtimeLogConfigsTypeDef"`


## ListStreamingDistributionsResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListStreamingDistributionsResultTypeDef
```




Optional fields:
- `StreamingDistributionList`: `"StreamingDistributionListTypeDef"`


## ListTagsForResourceResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ListTagsForResourceResultTypeDef
```


Required fields:
- `Tags`: `"TagsTypeDef"`




## LoggingConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import LoggingConfigTypeDef
```


Required fields:
- `Enabled`: `bool`
- `IncludeCookies`: `bool`
- `Bucket`: `str`
- `Prefix`: `str`




## MonitoringSubscriptionTypeDef

```python
from mypy_boto3_cloudfront.type_defs import MonitoringSubscriptionTypeDef
```




Optional fields:
- `RealtimeMetricsSubscriptionConfig`: `"RealtimeMetricsSubscriptionConfigTypeDef"`


## OriginCustomHeaderTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginCustomHeaderTypeDef
```


Required fields:
- `HeaderName`: `str`
- `HeaderValue`: `str`




## OriginGroupFailoverCriteriaTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginGroupFailoverCriteriaTypeDef
```


Required fields:
- `StatusCodes`: `"StatusCodesTypeDef"`




## OriginGroupMemberTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginGroupMemberTypeDef
```


Required fields:
- `OriginId`: `str`




## OriginGroupMembersTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginGroupMembersTypeDef
```


Required fields:
- `Quantity`: `int`
- `Items`: `List["OriginGroupMemberTypeDef"]`




## OriginGroupTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginGroupTypeDef
```


Required fields:
- `Id`: `str`
- `FailoverCriteria`: `"OriginGroupFailoverCriteriaTypeDef"`
- `Members`: `"OriginGroupMembersTypeDef"`




## OriginGroupsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginGroupsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["OriginGroupTypeDef"]`


## OriginRequestPolicyConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicyConfigTypeDef
```


Required fields:
- `Name`: `str`
- `HeadersConfig`: `"OriginRequestPolicyHeadersConfigTypeDef"`
- `CookiesConfig`: `"OriginRequestPolicyCookiesConfigTypeDef"`
- `QueryStringsConfig`: `"OriginRequestPolicyQueryStringsConfigTypeDef"`



Optional fields:
- `Comment`: `str`


## OriginRequestPolicyCookiesConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicyCookiesConfigTypeDef
```


Required fields:
- `CookieBehavior`: `OriginRequestPolicyCookieBehavior`



Optional fields:
- `Cookies`: `"CookieNamesTypeDef"`


## OriginRequestPolicyHeadersConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicyHeadersConfigTypeDef
```


Required fields:
- `HeaderBehavior`: `OriginRequestPolicyHeaderBehavior`



Optional fields:
- `Headers`: `"HeadersTypeDef"`


## OriginRequestPolicyListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicyListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["OriginRequestPolicySummaryTypeDef"]`


## OriginRequestPolicyQueryStringsConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicyQueryStringsConfigTypeDef
```


Required fields:
- `QueryStringBehavior`: `OriginRequestPolicyQueryStringBehavior`



Optional fields:
- `QueryStrings`: `"QueryStringNamesTypeDef"`


## OriginRequestPolicySummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicySummaryTypeDef
```


Required fields:
- `Type`: `OriginRequestPolicyType`
- `OriginRequestPolicy`: `"OriginRequestPolicyTypeDef"`




## OriginRequestPolicyTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginRequestPolicyTypeDef
```


Required fields:
- `Id`: `str`
- `LastModifiedTime`: `datetime`
- `OriginRequestPolicyConfig`: `"OriginRequestPolicyConfigTypeDef"`




## OriginShieldTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginShieldTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `OriginShieldRegion`: `str`


## OriginSslProtocolsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginSslProtocolsTypeDef
```


Required fields:
- `Quantity`: `int`
- `Items`: `List[SslProtocol]`




## OriginTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginTypeDef
```


Required fields:
- `Id`: `str`
- `DomainName`: `str`



Optional fields:
- `OriginPath`: `str`
- `CustomHeaders`: `"CustomHeadersTypeDef"`
- `S3OriginConfig`: `"S3OriginConfigTypeDef"`
- `CustomOriginConfig`: `"CustomOriginConfigTypeDef"`
- `ConnectionAttempts`: `int`
- `ConnectionTimeout`: `int`
- `OriginShield`: `"OriginShieldTypeDef"`


## OriginsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import OriginsTypeDef
```


Required fields:
- `Quantity`: `int`
- `Items`: `List["OriginTypeDef"]`




## PaginatorConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ParametersInCacheKeyAndForwardedToOriginTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ParametersInCacheKeyAndForwardedToOriginTypeDef
```


Required fields:
- `EnableAcceptEncodingGzip`: `bool`
- `HeadersConfig`: `"CachePolicyHeadersConfigTypeDef"`
- `CookiesConfig`: `"CachePolicyCookiesConfigTypeDef"`
- `QueryStringsConfig`: `"CachePolicyQueryStringsConfigTypeDef"`



Optional fields:
- `EnableAcceptEncodingBrotli`: `bool`


## PathsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PathsTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## PublicKeyConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PublicKeyConfigTypeDef
```


Required fields:
- `CallerReference`: `str`
- `Name`: `str`
- `EncodedKey`: `str`



Optional fields:
- `Comment`: `str`


## PublicKeyListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PublicKeyListTypeDef
```


Required fields:
- `MaxItems`: `int`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["PublicKeySummaryTypeDef"]`


## PublicKeySummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PublicKeySummaryTypeDef
```


Required fields:
- `Id`: `str`
- `Name`: `str`
- `CreatedTime`: `datetime`
- `EncodedKey`: `str`



Optional fields:
- `Comment`: `str`


## PublicKeyTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PublicKeyTypeDef
```


Required fields:
- `Id`: `str`
- `CreatedTime`: `datetime`
- `PublicKeyConfig`: `"PublicKeyConfigTypeDef"`




## PublishFunctionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import PublishFunctionResultTypeDef
```




Optional fields:
- `FunctionSummary`: `"FunctionSummaryTypeDef"`


## QueryArgProfileConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import QueryArgProfileConfigTypeDef
```


Required fields:
- `ForwardWhenQueryArgProfileIsUnknown`: `bool`



Optional fields:
- `QueryArgProfiles`: `"QueryArgProfilesTypeDef"`


## QueryArgProfileTypeDef

```python
from mypy_boto3_cloudfront.type_defs import QueryArgProfileTypeDef
```


Required fields:
- `QueryArg`: `str`
- `ProfileId`: `str`




## QueryArgProfilesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import QueryArgProfilesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List["QueryArgProfileTypeDef"]`


## QueryStringCacheKeysTypeDef

```python
from mypy_boto3_cloudfront.type_defs import QueryStringCacheKeysTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## QueryStringNamesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import QueryStringNamesTypeDef
```


Required fields:
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## RealtimeLogConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import RealtimeLogConfigTypeDef
```


Required fields:
- `ARN`: `str`
- `Name`: `str`
- `SamplingRate`: `int`
- `EndPoints`: `List["EndPointTypeDef"]`
- `Fields`: `List[str]`




## RealtimeLogConfigsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import RealtimeLogConfigsTypeDef
```


Required fields:
- `MaxItems`: `int`
- `IsTruncated`: `bool`
- `Marker`: `str`



Optional fields:
- `Items`: `List["RealtimeLogConfigTypeDef"]`
- `NextMarker`: `str`


## RealtimeMetricsSubscriptionConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import RealtimeMetricsSubscriptionConfigTypeDef
```


Required fields:
- `RealtimeMetricsSubscriptionStatus`: `RealtimeMetricsSubscriptionStatus`




## RestrictionsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import RestrictionsTypeDef
```


Required fields:
- `GeoRestriction`: `"GeoRestrictionTypeDef"`




## S3OriginConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import S3OriginConfigTypeDef
```


Required fields:
- `OriginAccessIdentity`: `str`




## S3OriginTypeDef

```python
from mypy_boto3_cloudfront.type_defs import S3OriginTypeDef
```


Required fields:
- `DomainName`: `str`
- `OriginAccessIdentity`: `str`




## SignerTypeDef

```python
from mypy_boto3_cloudfront.type_defs import SignerTypeDef
```




Optional fields:
- `AwsAccountNumber`: `str`
- `KeyPairIds`: `"KeyPairIdsTypeDef"`


## StatusCodesTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StatusCodesTypeDef
```


Required fields:
- `Quantity`: `int`
- `Items`: `List[int]`




## StreamingDistributionConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StreamingDistributionConfigTypeDef
```


Required fields:
- `CallerReference`: `str`
- `S3Origin`: `"S3OriginTypeDef"`
- `Comment`: `str`
- `TrustedSigners`: `"TrustedSignersTypeDef"`
- `Enabled`: `bool`



Optional fields:
- `Aliases`: `"AliasesTypeDef"`
- `Logging`: `"StreamingLoggingConfigTypeDef"`
- `PriceClass`: `PriceClass`


## StreamingDistributionConfigWithTagsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StreamingDistributionConfigWithTagsTypeDef
```


Required fields:
- `StreamingDistributionConfig`: `"StreamingDistributionConfigTypeDef"`
- `Tags`: `"TagsTypeDef"`




## StreamingDistributionListTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StreamingDistributionListTypeDef
```


Required fields:
- `Marker`: `str`
- `MaxItems`: `int`
- `IsTruncated`: `bool`
- `Quantity`: `int`



Optional fields:
- `NextMarker`: `str`
- `Items`: `List["StreamingDistributionSummaryTypeDef"]`


## StreamingDistributionSummaryTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StreamingDistributionSummaryTypeDef
```


Required fields:
- `Id`: `str`
- `ARN`: `str`
- `Status`: `str`
- `LastModifiedTime`: `datetime`
- `DomainName`: `str`
- `S3Origin`: `"S3OriginTypeDef"`
- `Aliases`: `"AliasesTypeDef"`
- `TrustedSigners`: `"TrustedSignersTypeDef"`
- `Comment`: `str`
- `PriceClass`: `PriceClass`
- `Enabled`: `bool`




## StreamingDistributionTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StreamingDistributionTypeDef
```


Required fields:
- `Id`: `str`
- `ARN`: `str`
- `Status`: `str`
- `DomainName`: `str`
- `ActiveTrustedSigners`: `"ActiveTrustedSignersTypeDef"`
- `StreamingDistributionConfig`: `"StreamingDistributionConfigTypeDef"`



Optional fields:
- `LastModifiedTime`: `datetime`


## StreamingLoggingConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import StreamingLoggingConfigTypeDef
```


Required fields:
- `Enabled`: `bool`
- `Bucket`: `str`
- `Prefix`: `str`




## TagKeysTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TagKeysTypeDef
```




Optional fields:
- `Items`: `List[str]`


## TagTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## TagsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TagsTypeDef
```




Optional fields:
- `Items`: `List["TagTypeDef"]`


## TestFunctionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TestFunctionResultTypeDef
```




Optional fields:
- `TestResult`: `"TestResultTypeDef"`


## TestResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TestResultTypeDef
```




Optional fields:
- `FunctionSummary`: `"FunctionSummaryTypeDef"`
- `ComputeUtilization`: `str`
- `FunctionExecutionLogs`: `List[str]`
- `FunctionErrorMessage`: `str`
- `FunctionOutput`: `str`


## TrustedKeyGroupsTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TrustedKeyGroupsTypeDef
```


Required fields:
- `Enabled`: `bool`
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## TrustedSignersTypeDef

```python
from mypy_boto3_cloudfront.type_defs import TrustedSignersTypeDef
```


Required fields:
- `Enabled`: `bool`
- `Quantity`: `int`



Optional fields:
- `Items`: `List[str]`


## UpdateCachePolicyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateCachePolicyResultTypeDef
```




Optional fields:
- `CachePolicy`: `"CachePolicyTypeDef"`
- `ETag`: `str`


## UpdateCloudFrontOriginAccessIdentityResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateCloudFrontOriginAccessIdentityResultTypeDef
```




Optional fields:
- `CloudFrontOriginAccessIdentity`: `"CloudFrontOriginAccessIdentityTypeDef"`
- `ETag`: `str`


## UpdateDistributionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateDistributionResultTypeDef
```




Optional fields:
- `Distribution`: `"DistributionTypeDef"`
- `ETag`: `str`


## UpdateFieldLevelEncryptionConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateFieldLevelEncryptionConfigResultTypeDef
```




Optional fields:
- `FieldLevelEncryption`: `"FieldLevelEncryptionTypeDef"`
- `ETag`: `str`


## UpdateFieldLevelEncryptionProfileResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateFieldLevelEncryptionProfileResultTypeDef
```




Optional fields:
- `FieldLevelEncryptionProfile`: `"FieldLevelEncryptionProfileTypeDef"`
- `ETag`: `str`


## UpdateFunctionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateFunctionResultTypeDef
```




Optional fields:
- `FunctionSummary`: `"FunctionSummaryTypeDef"`
- `ETag`: `str`


## UpdateKeyGroupResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateKeyGroupResultTypeDef
```




Optional fields:
- `KeyGroup`: `"KeyGroupTypeDef"`
- `ETag`: `str`


## UpdateOriginRequestPolicyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateOriginRequestPolicyResultTypeDef
```




Optional fields:
- `OriginRequestPolicy`: `"OriginRequestPolicyTypeDef"`
- `ETag`: `str`


## UpdatePublicKeyResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdatePublicKeyResultTypeDef
```




Optional fields:
- `PublicKey`: `"PublicKeyTypeDef"`
- `ETag`: `str`


## UpdateRealtimeLogConfigResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateRealtimeLogConfigResultTypeDef
```




Optional fields:
- `RealtimeLogConfig`: `"RealtimeLogConfigTypeDef"`


## UpdateStreamingDistributionResultTypeDef

```python
from mypy_boto3_cloudfront.type_defs import UpdateStreamingDistributionResultTypeDef
```




Optional fields:
- `StreamingDistribution`: `"StreamingDistributionTypeDef"`
- `ETag`: `str`


## ViewerCertificateTypeDef

```python
from mypy_boto3_cloudfront.type_defs import ViewerCertificateTypeDef
```




Optional fields:
- `CloudFrontDefaultCertificate`: `bool`
- `IAMCertificateId`: `str`
- `ACMCertificateArn`: `str`
- `SSLSupportMethod`: `SSLSupportMethod`
- `MinimumProtocolVersion`: `MinimumProtocolVersion`
- `Certificate`: `str`
- `CertificateSource`: `CertificateSource`


## WaiterConfigTypeDef

```python
from mypy_boto3_cloudfront.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

