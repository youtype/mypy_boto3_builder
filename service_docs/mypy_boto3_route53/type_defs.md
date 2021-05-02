# Structures for boto3 Route53 module

> [Index](../index.md) > [Route53](./index.md) > Structures

Auto-generated documentation for [Route53](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53)
type annotations stubs module [mypy_boto3_route53](https://pypi.org/project/mypy-boto3-route53/).

- [Structures for boto3 Route53 module](#structures-for-boto3-route53-module)
  - [AccountLimitTypeDef](#accountlimittypedef)
  - [ActivateKeySigningKeyResponseTypeDef](#activatekeysigningkeyresponsetypedef)
  - [AlarmIdentifierTypeDef](#alarmidentifiertypedef)
  - [AliasTargetTypeDef](#aliastargettypedef)
  - [AssociateVPCWithHostedZoneResponseTypeDef](#associatevpcwithhostedzoneresponsetypedef)
  - [ChangeBatchTypeDef](#changebatchtypedef)
  - [ChangeInfoTypeDef](#changeinfotypedef)
  - [ChangeResourceRecordSetsResponseTypeDef](#changeresourcerecordsetsresponsetypedef)
  - [ChangeTypeDef](#changetypedef)
  - [CloudWatchAlarmConfigurationTypeDef](#cloudwatchalarmconfigurationtypedef)
  - [CreateHealthCheckResponseTypeDef](#createhealthcheckresponsetypedef)
  - [CreateHostedZoneResponseTypeDef](#createhostedzoneresponsetypedef)
  - [CreateKeySigningKeyResponseTypeDef](#createkeysigningkeyresponsetypedef)
  - [CreateQueryLoggingConfigResponseTypeDef](#createqueryloggingconfigresponsetypedef)
  - [CreateReusableDelegationSetResponseTypeDef](#createreusabledelegationsetresponsetypedef)
  - [CreateTrafficPolicyInstanceResponseTypeDef](#createtrafficpolicyinstanceresponsetypedef)
  - [CreateTrafficPolicyResponseTypeDef](#createtrafficpolicyresponsetypedef)
  - [CreateTrafficPolicyVersionResponseTypeDef](#createtrafficpolicyversionresponsetypedef)
  - [CreateVPCAssociationAuthorizationResponseTypeDef](#createvpcassociationauthorizationresponsetypedef)
  - [DNSSECStatusTypeDef](#dnssecstatustypedef)
  - [DeactivateKeySigningKeyResponseTypeDef](#deactivatekeysigningkeyresponsetypedef)
  - [DelegationSetTypeDef](#delegationsettypedef)
  - [DeleteHostedZoneResponseTypeDef](#deletehostedzoneresponsetypedef)
  - [DeleteKeySigningKeyResponseTypeDef](#deletekeysigningkeyresponsetypedef)
  - [DimensionTypeDef](#dimensiontypedef)
  - [DisableHostedZoneDNSSECResponseTypeDef](#disablehostedzonednssecresponsetypedef)
  - [DisassociateVPCFromHostedZoneResponseTypeDef](#disassociatevpcfromhostedzoneresponsetypedef)
  - [EnableHostedZoneDNSSECResponseTypeDef](#enablehostedzonednssecresponsetypedef)
  - [GeoLocationDetailsTypeDef](#geolocationdetailstypedef)
  - [GeoLocationTypeDef](#geolocationtypedef)
  - [GetAccountLimitResponseTypeDef](#getaccountlimitresponsetypedef)
  - [GetChangeResponseTypeDef](#getchangeresponsetypedef)
  - [GetCheckerIpRangesResponseTypeDef](#getcheckeriprangesresponsetypedef)
  - [GetDNSSECResponseTypeDef](#getdnssecresponsetypedef)
  - [GetGeoLocationResponseTypeDef](#getgeolocationresponsetypedef)
  - [GetHealthCheckCountResponseTypeDef](#gethealthcheckcountresponsetypedef)
  - [GetHealthCheckLastFailureReasonResponseTypeDef](#gethealthchecklastfailurereasonresponsetypedef)
  - [GetHealthCheckResponseTypeDef](#gethealthcheckresponsetypedef)
  - [GetHealthCheckStatusResponseTypeDef](#gethealthcheckstatusresponsetypedef)
  - [GetHostedZoneCountResponseTypeDef](#gethostedzonecountresponsetypedef)
  - [GetHostedZoneLimitResponseTypeDef](#gethostedzonelimitresponsetypedef)
  - [GetHostedZoneResponseTypeDef](#gethostedzoneresponsetypedef)
  - [GetQueryLoggingConfigResponseTypeDef](#getqueryloggingconfigresponsetypedef)
  - [GetReusableDelegationSetLimitResponseTypeDef](#getreusabledelegationsetlimitresponsetypedef)
  - [GetReusableDelegationSetResponseTypeDef](#getreusabledelegationsetresponsetypedef)
  - [GetTrafficPolicyInstanceCountResponseTypeDef](#gettrafficpolicyinstancecountresponsetypedef)
  - [GetTrafficPolicyInstanceResponseTypeDef](#gettrafficpolicyinstanceresponsetypedef)
  - [GetTrafficPolicyResponseTypeDef](#gettrafficpolicyresponsetypedef)
  - [HealthCheckConfigTypeDef](#healthcheckconfigtypedef)
  - [HealthCheckObservationTypeDef](#healthcheckobservationtypedef)
  - [HealthCheckTypeDef](#healthchecktypedef)
  - [HostedZoneConfigTypeDef](#hostedzoneconfigtypedef)
  - [HostedZoneLimitTypeDef](#hostedzonelimittypedef)
  - [HostedZoneOwnerTypeDef](#hostedzoneownertypedef)
  - [HostedZoneSummaryTypeDef](#hostedzonesummarytypedef)
  - [HostedZoneTypeDef](#hostedzonetypedef)
  - [KeySigningKeyTypeDef](#keysigningkeytypedef)
  - [LinkedServiceTypeDef](#linkedservicetypedef)
  - [ListGeoLocationsResponseTypeDef](#listgeolocationsresponsetypedef)
  - [ListHealthChecksResponseTypeDef](#listhealthchecksresponsetypedef)
  - [ListHostedZonesByNameResponseTypeDef](#listhostedzonesbynameresponsetypedef)
  - [ListHostedZonesByVPCResponseTypeDef](#listhostedzonesbyvpcresponsetypedef)
  - [ListHostedZonesResponseTypeDef](#listhostedzonesresponsetypedef)
  - [ListQueryLoggingConfigsResponseTypeDef](#listqueryloggingconfigsresponsetypedef)
  - [ListResourceRecordSetsResponseTypeDef](#listresourcerecordsetsresponsetypedef)
  - [ListReusableDelegationSetsResponseTypeDef](#listreusabledelegationsetsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTagsForResourcesResponseTypeDef](#listtagsforresourcesresponsetypedef)
  - [ListTrafficPoliciesResponseTypeDef](#listtrafficpoliciesresponsetypedef)
  - [ListTrafficPolicyInstancesByHostedZoneResponseTypeDef](#listtrafficpolicyinstancesbyhostedzoneresponsetypedef)
  - [ListTrafficPolicyInstancesByPolicyResponseTypeDef](#listtrafficpolicyinstancesbypolicyresponsetypedef)
  - [ListTrafficPolicyInstancesResponseTypeDef](#listtrafficpolicyinstancesresponsetypedef)
  - [ListTrafficPolicyVersionsResponseTypeDef](#listtrafficpolicyversionsresponsetypedef)
  - [ListVPCAssociationAuthorizationsResponseTypeDef](#listvpcassociationauthorizationsresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [QueryLoggingConfigTypeDef](#queryloggingconfigtypedef)
  - [ResourceRecordSetTypeDef](#resourcerecordsettypedef)
  - [ResourceRecordTypeDef](#resourcerecordtypedef)
  - [ResourceTagSetTypeDef](#resourcetagsettypedef)
  - [ReusableDelegationSetLimitTypeDef](#reusabledelegationsetlimittypedef)
  - [StatusReportTypeDef](#statusreporttypedef)
  - [TagTypeDef](#tagtypedef)
  - [TestDNSAnswerResponseTypeDef](#testdnsanswerresponsetypedef)
  - [TrafficPolicyInstanceTypeDef](#trafficpolicyinstancetypedef)
  - [TrafficPolicySummaryTypeDef](#trafficpolicysummarytypedef)
  - [TrafficPolicyTypeDef](#trafficpolicytypedef)
  - [UpdateHealthCheckResponseTypeDef](#updatehealthcheckresponsetypedef)
  - [UpdateHostedZoneCommentResponseTypeDef](#updatehostedzonecommentresponsetypedef)
  - [UpdateTrafficPolicyCommentResponseTypeDef](#updatetrafficpolicycommentresponsetypedef)
  - [UpdateTrafficPolicyInstanceResponseTypeDef](#updatetrafficpolicyinstanceresponsetypedef)
  - [VPCTypeDef](#vpctypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountLimitTypeDef

```python
from mypy_boto3_route53.type_defs import AccountLimitTypeDef
```


Required fields:
- `Type`: `AccountLimitType`
- `Value`: `int`




## ActivateKeySigningKeyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ActivateKeySigningKeyResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## AlarmIdentifierTypeDef

```python
from mypy_boto3_route53.type_defs import AlarmIdentifierTypeDef
```


Required fields:
- `Region`: `CloudWatchRegion`
- `Name`: `str`




## AliasTargetTypeDef

```python
from mypy_boto3_route53.type_defs import AliasTargetTypeDef
```


Required fields:
- `HostedZoneId`: `str`
- `DNSName`: `str`
- `EvaluateTargetHealth`: `bool`




## AssociateVPCWithHostedZoneResponseTypeDef

```python
from mypy_boto3_route53.type_defs import AssociateVPCWithHostedZoneResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## ChangeBatchTypeDef

```python
from mypy_boto3_route53.type_defs import ChangeBatchTypeDef
```


Required fields:
- `Changes`: `List["ChangeTypeDef"]`



Optional fields:
- `Comment`: `str`


## ChangeInfoTypeDef

```python
from mypy_boto3_route53.type_defs import ChangeInfoTypeDef
```


Required fields:
- `Id`: `str`
- `Status`: `ChangeStatus`
- `SubmittedAt`: `datetime`



Optional fields:
- `Comment`: `str`


## ChangeResourceRecordSetsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ChangeResourceRecordSetsResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## ChangeTypeDef

```python
from mypy_boto3_route53.type_defs import ChangeTypeDef
```


Required fields:
- `Action`: `ChangeAction`
- `ResourceRecordSet`: `"ResourceRecordSetTypeDef"`




## CloudWatchAlarmConfigurationTypeDef

```python
from mypy_boto3_route53.type_defs import CloudWatchAlarmConfigurationTypeDef
```


Required fields:
- `EvaluationPeriods`: `int`
- `Threshold`: `float`
- `ComparisonOperator`: `ComparisonOperator`
- `Period`: `int`
- `MetricName`: `str`
- `Namespace`: `str`
- `Statistic`: `Statistic`



Optional fields:
- `Dimensions`: `List["DimensionTypeDef"]`


## CreateHealthCheckResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateHealthCheckResponseTypeDef
```


Required fields:
- `HealthCheck`: `"HealthCheckTypeDef"`
- `Location`: `str`




## CreateHostedZoneResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateHostedZoneResponseTypeDef
```


Required fields:
- `HostedZone`: `"HostedZoneTypeDef"`
- `ChangeInfo`: `"ChangeInfoTypeDef"`
- `DelegationSet`: `"DelegationSetTypeDef"`
- `Location`: `str`



Optional fields:
- `VPC`: `"VPCTypeDef"`


## CreateKeySigningKeyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateKeySigningKeyResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`
- `KeySigningKey`: `"KeySigningKeyTypeDef"`
- `Location`: `str`




## CreateQueryLoggingConfigResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateQueryLoggingConfigResponseTypeDef
```


Required fields:
- `QueryLoggingConfig`: `"QueryLoggingConfigTypeDef"`
- `Location`: `str`




## CreateReusableDelegationSetResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateReusableDelegationSetResponseTypeDef
```


Required fields:
- `DelegationSet`: `"DelegationSetTypeDef"`
- `Location`: `str`




## CreateTrafficPolicyInstanceResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateTrafficPolicyInstanceResponseTypeDef
```


Required fields:
- `TrafficPolicyInstance`: `"TrafficPolicyInstanceTypeDef"`
- `Location`: `str`




## CreateTrafficPolicyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateTrafficPolicyResponseTypeDef
```


Required fields:
- `TrafficPolicy`: `"TrafficPolicyTypeDef"`
- `Location`: `str`




## CreateTrafficPolicyVersionResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateTrafficPolicyVersionResponseTypeDef
```


Required fields:
- `TrafficPolicy`: `"TrafficPolicyTypeDef"`
- `Location`: `str`




## CreateVPCAssociationAuthorizationResponseTypeDef

```python
from mypy_boto3_route53.type_defs import CreateVPCAssociationAuthorizationResponseTypeDef
```


Required fields:
- `HostedZoneId`: `str`
- `VPC`: `"VPCTypeDef"`




## DNSSECStatusTypeDef

```python
from mypy_boto3_route53.type_defs import DNSSECStatusTypeDef
```




Optional fields:
- `ServeSignature`: `str`
- `StatusMessage`: `str`


## DeactivateKeySigningKeyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import DeactivateKeySigningKeyResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## DelegationSetTypeDef

```python
from mypy_boto3_route53.type_defs import DelegationSetTypeDef
```


Required fields:
- `NameServers`: `List[str]`



Optional fields:
- `Id`: `str`
- `CallerReference`: `str`


## DeleteHostedZoneResponseTypeDef

```python
from mypy_boto3_route53.type_defs import DeleteHostedZoneResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## DeleteKeySigningKeyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import DeleteKeySigningKeyResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## DimensionTypeDef

```python
from mypy_boto3_route53.type_defs import DimensionTypeDef
```


Required fields:
- `Name`: `str`
- `Value`: `str`




## DisableHostedZoneDNSSECResponseTypeDef

```python
from mypy_boto3_route53.type_defs import DisableHostedZoneDNSSECResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## DisassociateVPCFromHostedZoneResponseTypeDef

```python
from mypy_boto3_route53.type_defs import DisassociateVPCFromHostedZoneResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## EnableHostedZoneDNSSECResponseTypeDef

```python
from mypy_boto3_route53.type_defs import EnableHostedZoneDNSSECResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## GeoLocationDetailsTypeDef

```python
from mypy_boto3_route53.type_defs import GeoLocationDetailsTypeDef
```




Optional fields:
- `ContinentCode`: `str`
- `ContinentName`: `str`
- `CountryCode`: `str`
- `CountryName`: `str`
- `SubdivisionCode`: `str`
- `SubdivisionName`: `str`


## GeoLocationTypeDef

```python
from mypy_boto3_route53.type_defs import GeoLocationTypeDef
```




Optional fields:
- `ContinentCode`: `str`
- `CountryCode`: `str`
- `SubdivisionCode`: `str`


## GetAccountLimitResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetAccountLimitResponseTypeDef
```


Required fields:
- `Limit`: `"AccountLimitTypeDef"`
- `Count`: `int`




## GetChangeResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetChangeResponseTypeDef
```


Required fields:
- `ChangeInfo`: `"ChangeInfoTypeDef"`




## GetCheckerIpRangesResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetCheckerIpRangesResponseTypeDef
```


Required fields:
- `CheckerIpRanges`: `List[str]`




## GetDNSSECResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetDNSSECResponseTypeDef
```


Required fields:
- `Status`: `"DNSSECStatusTypeDef"`
- `KeySigningKeys`: `List["KeySigningKeyTypeDef"]`




## GetGeoLocationResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetGeoLocationResponseTypeDef
```


Required fields:
- `GeoLocationDetails`: `"GeoLocationDetailsTypeDef"`




## GetHealthCheckCountResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHealthCheckCountResponseTypeDef
```


Required fields:
- `HealthCheckCount`: `int`




## GetHealthCheckLastFailureReasonResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHealthCheckLastFailureReasonResponseTypeDef
```


Required fields:
- `HealthCheckObservations`: `List["HealthCheckObservationTypeDef"]`




## GetHealthCheckResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHealthCheckResponseTypeDef
```


Required fields:
- `HealthCheck`: `"HealthCheckTypeDef"`




## GetHealthCheckStatusResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHealthCheckStatusResponseTypeDef
```


Required fields:
- `HealthCheckObservations`: `List["HealthCheckObservationTypeDef"]`




## GetHostedZoneCountResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHostedZoneCountResponseTypeDef
```


Required fields:
- `HostedZoneCount`: `int`




## GetHostedZoneLimitResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHostedZoneLimitResponseTypeDef
```


Required fields:
- `Limit`: `"HostedZoneLimitTypeDef"`
- `Count`: `int`




## GetHostedZoneResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetHostedZoneResponseTypeDef
```


Required fields:
- `HostedZone`: `"HostedZoneTypeDef"`



Optional fields:
- `DelegationSet`: `"DelegationSetTypeDef"`
- `VPCs`: `List["VPCTypeDef"]`


## GetQueryLoggingConfigResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetQueryLoggingConfigResponseTypeDef
```


Required fields:
- `QueryLoggingConfig`: `"QueryLoggingConfigTypeDef"`




## GetReusableDelegationSetLimitResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetReusableDelegationSetLimitResponseTypeDef
```


Required fields:
- `Limit`: `"ReusableDelegationSetLimitTypeDef"`
- `Count`: `int`




## GetReusableDelegationSetResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetReusableDelegationSetResponseTypeDef
```


Required fields:
- `DelegationSet`: `"DelegationSetTypeDef"`




## GetTrafficPolicyInstanceCountResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetTrafficPolicyInstanceCountResponseTypeDef
```


Required fields:
- `TrafficPolicyInstanceCount`: `int`




## GetTrafficPolicyInstanceResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetTrafficPolicyInstanceResponseTypeDef
```


Required fields:
- `TrafficPolicyInstance`: `"TrafficPolicyInstanceTypeDef"`




## GetTrafficPolicyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import GetTrafficPolicyResponseTypeDef
```


Required fields:
- `TrafficPolicy`: `"TrafficPolicyTypeDef"`




## HealthCheckConfigTypeDef

```python
from mypy_boto3_route53.type_defs import HealthCheckConfigTypeDef
```


Required fields:
- `Type`: `HealthCheckType`



Optional fields:
- `IPAddress`: `str`
- `Port`: `int`
- `ResourcePath`: `str`
- `FullyQualifiedDomainName`: `str`
- `SearchString`: `str`
- `RequestInterval`: `int`
- `FailureThreshold`: `int`
- `MeasureLatency`: `bool`
- `Inverted`: `bool`
- `Disabled`: `bool`
- `HealthThreshold`: `int`
- `ChildHealthChecks`: `List[str]`
- `EnableSNI`: `bool`
- `Regions`: `List[HealthCheckRegion]`
- `AlarmIdentifier`: `"AlarmIdentifierTypeDef"`
- `InsufficientDataHealthStatus`: `InsufficientDataHealthStatus`


## HealthCheckObservationTypeDef

```python
from mypy_boto3_route53.type_defs import HealthCheckObservationTypeDef
```




Optional fields:
- `Region`: `HealthCheckRegion`
- `IPAddress`: `str`
- `StatusReport`: `"StatusReportTypeDef"`


## HealthCheckTypeDef

```python
from mypy_boto3_route53.type_defs import HealthCheckTypeDef
```


Required fields:
- `Id`: `str`
- `CallerReference`: `str`
- `HealthCheckConfig`: `"HealthCheckConfigTypeDef"`
- `HealthCheckVersion`: `int`



Optional fields:
- `LinkedService`: `"LinkedServiceTypeDef"`
- `CloudWatchAlarmConfiguration`: `"CloudWatchAlarmConfigurationTypeDef"`


## HostedZoneConfigTypeDef

```python
from mypy_boto3_route53.type_defs import HostedZoneConfigTypeDef
```




Optional fields:
- `Comment`: `str`
- `PrivateZone`: `bool`


## HostedZoneLimitTypeDef

```python
from mypy_boto3_route53.type_defs import HostedZoneLimitTypeDef
```


Required fields:
- `Type`: `HostedZoneLimitType`
- `Value`: `int`




## HostedZoneOwnerTypeDef

```python
from mypy_boto3_route53.type_defs import HostedZoneOwnerTypeDef
```




Optional fields:
- `OwningAccount`: `str`
- `OwningService`: `str`


## HostedZoneSummaryTypeDef

```python
from mypy_boto3_route53.type_defs import HostedZoneSummaryTypeDef
```


Required fields:
- `HostedZoneId`: `str`
- `Name`: `str`
- `Owner`: `"HostedZoneOwnerTypeDef"`




## HostedZoneTypeDef

```python
from mypy_boto3_route53.type_defs import HostedZoneTypeDef
```


Required fields:
- `Id`: `str`
- `Name`: `str`
- `CallerReference`: `str`



Optional fields:
- `Config`: `"HostedZoneConfigTypeDef"`
- `ResourceRecordSetCount`: `int`
- `LinkedService`: `"LinkedServiceTypeDef"`


## KeySigningKeyTypeDef

```python
from mypy_boto3_route53.type_defs import KeySigningKeyTypeDef
```




Optional fields:
- `Name`: `str`
- `KmsArn`: `str`
- `Flag`: `int`
- `SigningAlgorithmMnemonic`: `str`
- `SigningAlgorithmType`: `int`
- `DigestAlgorithmMnemonic`: `str`
- `DigestAlgorithmType`: `int`
- `KeyTag`: `int`
- `DigestValue`: `str`
- `PublicKey`: `str`
- `DSRecord`: `str`
- `DNSKEYRecord`: `str`
- `Status`: `str`
- `StatusMessage`: `str`
- `CreatedDate`: `datetime`
- `LastModifiedDate`: `datetime`


## LinkedServiceTypeDef

```python
from mypy_boto3_route53.type_defs import LinkedServiceTypeDef
```




Optional fields:
- `ServicePrincipal`: `str`
- `Description`: `str`


## ListGeoLocationsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListGeoLocationsResponseTypeDef
```


Required fields:
- `GeoLocationDetailsList`: `List["GeoLocationDetailsTypeDef"]`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `NextContinentCode`: `str`
- `NextCountryCode`: `str`
- `NextSubdivisionCode`: `str`


## ListHealthChecksResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListHealthChecksResponseTypeDef
```


Required fields:
- `HealthChecks`: `List["HealthCheckTypeDef"]`
- `Marker`: `str`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `NextMarker`: `str`


## ListHostedZonesByNameResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListHostedZonesByNameResponseTypeDef
```


Required fields:
- `HostedZones`: `List["HostedZoneTypeDef"]`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `DNSName`: `str`
- `HostedZoneId`: `str`
- `NextDNSName`: `str`
- `NextHostedZoneId`: `str`


## ListHostedZonesByVPCResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListHostedZonesByVPCResponseTypeDef
```


Required fields:
- `HostedZoneSummaries`: `List["HostedZoneSummaryTypeDef"]`
- `MaxItems`: `str`



Optional fields:
- `NextToken`: `str`


## ListHostedZonesResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListHostedZonesResponseTypeDef
```


Required fields:
- `HostedZones`: `List["HostedZoneTypeDef"]`
- `Marker`: `str`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `NextMarker`: `str`


## ListQueryLoggingConfigsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListQueryLoggingConfigsResponseTypeDef
```


Required fields:
- `QueryLoggingConfigs`: `List["QueryLoggingConfigTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListResourceRecordSetsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListResourceRecordSetsResponseTypeDef
```


Required fields:
- `ResourceRecordSets`: `List["ResourceRecordSetTypeDef"]`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `NextRecordName`: `str`
- `NextRecordType`: `RRType`
- `NextRecordIdentifier`: `str`


## ListReusableDelegationSetsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListReusableDelegationSetsResponseTypeDef
```


Required fields:
- `DelegationSets`: `List["DelegationSetTypeDef"]`
- `Marker`: `str`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `NextMarker`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTagsForResourceResponseTypeDef
```


Required fields:
- `ResourceTagSet`: `"ResourceTagSetTypeDef"`




## ListTagsForResourcesResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTagsForResourcesResponseTypeDef
```


Required fields:
- `ResourceTagSets`: `List["ResourceTagSetTypeDef"]`




## ListTrafficPoliciesResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTrafficPoliciesResponseTypeDef
```


Required fields:
- `TrafficPolicySummaries`: `List["TrafficPolicySummaryTypeDef"]`
- `IsTruncated`: `bool`
- `TrafficPolicyIdMarker`: `str`
- `MaxItems`: `str`




## ListTrafficPolicyInstancesByHostedZoneResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTrafficPolicyInstancesByHostedZoneResponseTypeDef
```


Required fields:
- `TrafficPolicyInstances`: `List["TrafficPolicyInstanceTypeDef"]`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `TrafficPolicyInstanceNameMarker`: `str`
- `TrafficPolicyInstanceTypeMarker`: `RRType`


## ListTrafficPolicyInstancesByPolicyResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTrafficPolicyInstancesByPolicyResponseTypeDef
```


Required fields:
- `TrafficPolicyInstances`: `List["TrafficPolicyInstanceTypeDef"]`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `HostedZoneIdMarker`: `str`
- `TrafficPolicyInstanceNameMarker`: `str`
- `TrafficPolicyInstanceTypeMarker`: `RRType`


## ListTrafficPolicyInstancesResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTrafficPolicyInstancesResponseTypeDef
```


Required fields:
- `TrafficPolicyInstances`: `List["TrafficPolicyInstanceTypeDef"]`
- `IsTruncated`: `bool`
- `MaxItems`: `str`



Optional fields:
- `HostedZoneIdMarker`: `str`
- `TrafficPolicyInstanceNameMarker`: `str`
- `TrafficPolicyInstanceTypeMarker`: `RRType`


## ListTrafficPolicyVersionsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListTrafficPolicyVersionsResponseTypeDef
```


Required fields:
- `TrafficPolicies`: `List["TrafficPolicyTypeDef"]`
- `IsTruncated`: `bool`
- `TrafficPolicyVersionMarker`: `str`
- `MaxItems`: `str`




## ListVPCAssociationAuthorizationsResponseTypeDef

```python
from mypy_boto3_route53.type_defs import ListVPCAssociationAuthorizationsResponseTypeDef
```


Required fields:
- `HostedZoneId`: `str`
- `VPCs`: `List["VPCTypeDef"]`



Optional fields:
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_route53.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## QueryLoggingConfigTypeDef

```python
from mypy_boto3_route53.type_defs import QueryLoggingConfigTypeDef
```


Required fields:
- `Id`: `str`
- `HostedZoneId`: `str`
- `CloudWatchLogsLogGroupArn`: `str`




## ResourceRecordSetTypeDef

```python
from mypy_boto3_route53.type_defs import ResourceRecordSetTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `RRType`



Optional fields:
- `SetIdentifier`: `str`
- `Weight`: `int`
- `Region`: `ResourceRecordSetRegion`
- `GeoLocation`: `"GeoLocationTypeDef"`
- `Failover`: `ResourceRecordSetFailover`
- `MultiValueAnswer`: `bool`
- `TTL`: `int`
- `ResourceRecords`: `List["ResourceRecordTypeDef"]`
- `AliasTarget`: `"AliasTargetTypeDef"`
- `HealthCheckId`: `str`
- `TrafficPolicyInstanceId`: `str`


## ResourceRecordTypeDef

```python
from mypy_boto3_route53.type_defs import ResourceRecordTypeDef
```


Required fields:
- `Value`: `str`




## ResourceTagSetTypeDef

```python
from mypy_boto3_route53.type_defs import ResourceTagSetTypeDef
```




Optional fields:
- `ResourceType`: `TagResourceType`
- `ResourceId`: `str`
- `Tags`: `List["TagTypeDef"]`


## ReusableDelegationSetLimitTypeDef

```python
from mypy_boto3_route53.type_defs import ReusableDelegationSetLimitTypeDef
```


Required fields:
- `Type`: `Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']`
- `Value`: `int`




## StatusReportTypeDef

```python
from mypy_boto3_route53.type_defs import StatusReportTypeDef
```




Optional fields:
- `Status`: `str`
- `CheckedTime`: `datetime`


## TagTypeDef

```python
from mypy_boto3_route53.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TestDNSAnswerResponseTypeDef

```python
from mypy_boto3_route53.type_defs import TestDNSAnswerResponseTypeDef
```


Required fields:
- `Nameserver`: `str`
- `RecordName`: `str`
- `RecordType`: `RRType`
- `RecordData`: `List[str]`
- `ResponseCode`: `str`
- `Protocol`: `str`




## TrafficPolicyInstanceTypeDef

```python
from mypy_boto3_route53.type_defs import TrafficPolicyInstanceTypeDef
```


Required fields:
- `Id`: `str`
- `HostedZoneId`: `str`
- `Name`: `str`
- `TTL`: `int`
- `State`: `str`
- `Message`: `str`
- `TrafficPolicyId`: `str`
- `TrafficPolicyVersion`: `int`
- `TrafficPolicyType`: `RRType`




## TrafficPolicySummaryTypeDef

```python
from mypy_boto3_route53.type_defs import TrafficPolicySummaryTypeDef
```


Required fields:
- `Id`: `str`
- `Name`: `str`
- `Type`: `RRType`
- `LatestVersion`: `int`
- `TrafficPolicyCount`: `int`




## TrafficPolicyTypeDef

```python
from mypy_boto3_route53.type_defs import TrafficPolicyTypeDef
```


Required fields:
- `Id`: `str`
- `Version`: `int`
- `Name`: `str`
- `Type`: `RRType`
- `Document`: `str`



Optional fields:
- `Comment`: `str`


## UpdateHealthCheckResponseTypeDef

```python
from mypy_boto3_route53.type_defs import UpdateHealthCheckResponseTypeDef
```


Required fields:
- `HealthCheck`: `"HealthCheckTypeDef"`




## UpdateHostedZoneCommentResponseTypeDef

```python
from mypy_boto3_route53.type_defs import UpdateHostedZoneCommentResponseTypeDef
```


Required fields:
- `HostedZone`: `"HostedZoneTypeDef"`




## UpdateTrafficPolicyCommentResponseTypeDef

```python
from mypy_boto3_route53.type_defs import UpdateTrafficPolicyCommentResponseTypeDef
```


Required fields:
- `TrafficPolicy`: `"TrafficPolicyTypeDef"`




## UpdateTrafficPolicyInstanceResponseTypeDef

```python
from mypy_boto3_route53.type_defs import UpdateTrafficPolicyInstanceResponseTypeDef
```


Required fields:
- `TrafficPolicyInstance`: `"TrafficPolicyInstanceTypeDef"`




## VPCTypeDef

```python
from mypy_boto3_route53.type_defs import VPCTypeDef
```




Optional fields:
- `VPCRegion`: `VPCRegion`
- `VPCId`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_route53.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

