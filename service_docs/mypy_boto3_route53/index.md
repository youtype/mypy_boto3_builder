# Type annotations for boto3 Route53 module

> [Index](../index.md) > Route53

Auto-generated documentation for [Route53](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53)
type annotations stubs module [mypy_boto3_route53](https://pypi.org/project/mypy-boto3-route53/).

```bash
pip install mypy-boto3-route53
```

- [Type annotations for boto3 Route53 module](#type-annotations-for-boto3-route53-module)
  - [Route53Client](#route53client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## Route53Client

Type annotations for  `boto3.client("route53")` as [Route53Client](./client.md)

Can be used directly:

```python
from mypy_boto3_route53.client import Route53Client
```


Route53Client [exceptions](./client.md#exceptions)



### Methods
- [activate_key_signing_key](./client.md#activate-key-signing-key)
- [associate_vpc_with_hosted_zone](./client.md#associate-vpc-with-hosted-zone)
- [can_paginate](./client.md#can-paginate)
- [change_resource_record_sets](./client.md#change-resource-record-sets)
- [change_tags_for_resource](./client.md#change-tags-for-resource)
- [create_health_check](./client.md#create-health-check)
- [create_hosted_zone](./client.md#create-hosted-zone)
- [create_key_signing_key](./client.md#create-key-signing-key)
- [create_query_logging_config](./client.md#create-query-logging-config)
- [create_reusable_delegation_set](./client.md#create-reusable-delegation-set)
- [create_traffic_policy](./client.md#create-traffic-policy)
- [create_traffic_policy_instance](./client.md#create-traffic-policy-instance)
- [create_traffic_policy_version](./client.md#create-traffic-policy-version)
- [create_vpc_association_authorization](./client.md#create-vpc-association-authorization)
- [deactivate_key_signing_key](./client.md#deactivate-key-signing-key)
- [delete_health_check](./client.md#delete-health-check)
- [delete_hosted_zone](./client.md#delete-hosted-zone)
- [delete_key_signing_key](./client.md#delete-key-signing-key)
- [delete_query_logging_config](./client.md#delete-query-logging-config)
- [delete_reusable_delegation_set](./client.md#delete-reusable-delegation-set)
- [delete_traffic_policy](./client.md#delete-traffic-policy)
- [delete_traffic_policy_instance](./client.md#delete-traffic-policy-instance)
- [delete_vpc_association_authorization](./client.md#delete-vpc-association-authorization)
- [disable_hosted_zone_dnssec](./client.md#disable-hosted-zone-dnssec)
- [disassociate_vpc_from_hosted_zone](./client.md#disassociate-vpc-from-hosted-zone)
- [enable_hosted_zone_dnssec](./client.md#enable-hosted-zone-dnssec)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account_limit](./client.md#get-account-limit)
- [get_change](./client.md#get-change)
- [get_checker_ip_ranges](./client.md#get-checker-ip-ranges)
- [get_dnssec](./client.md#get-dnssec)
- [get_geo_location](./client.md#get-geo-location)
- [get_health_check](./client.md#get-health-check)
- [get_health_check_count](./client.md#get-health-check-count)
- [get_health_check_last_failure_reason](./client.md#get-health-check-last-failure-reason)
- [get_health_check_status](./client.md#get-health-check-status)
- [get_hosted_zone](./client.md#get-hosted-zone)
- [get_hosted_zone_count](./client.md#get-hosted-zone-count)
- [get_hosted_zone_limit](./client.md#get-hosted-zone-limit)
- [get_paginator](./client.md#get-paginator)
- [get_query_logging_config](./client.md#get-query-logging-config)
- [get_reusable_delegation_set](./client.md#get-reusable-delegation-set)
- [get_reusable_delegation_set_limit](./client.md#get-reusable-delegation-set-limit)
- [get_traffic_policy](./client.md#get-traffic-policy)
- [get_traffic_policy_instance](./client.md#get-traffic-policy-instance)
- [get_traffic_policy_instance_count](./client.md#get-traffic-policy-instance-count)
- [get_waiter](./client.md#get-waiter)
- [list_geo_locations](./client.md#list-geo-locations)
- [list_health_checks](./client.md#list-health-checks)
- [list_hosted_zones](./client.md#list-hosted-zones)
- [list_hosted_zones_by_name](./client.md#list-hosted-zones-by-name)
- [list_hosted_zones_by_vpc](./client.md#list-hosted-zones-by-vpc)
- [list_query_logging_configs](./client.md#list-query-logging-configs)
- [list_resource_record_sets](./client.md#list-resource-record-sets)
- [list_reusable_delegation_sets](./client.md#list-reusable-delegation-sets)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_tags_for_resources](./client.md#list-tags-for-resources)
- [list_traffic_policies](./client.md#list-traffic-policies)
- [list_traffic_policy_instances](./client.md#list-traffic-policy-instances)
- [list_traffic_policy_instances_by_hosted_zone](./client.md#list-traffic-policy-instances-by-hosted-zone)
- [list_traffic_policy_instances_by_policy](./client.md#list-traffic-policy-instances-by-policy)
- [list_traffic_policy_versions](./client.md#list-traffic-policy-versions)
- [list_vpc_association_authorizations](./client.md#list-vpc-association-authorizations)
- [test_dns_answer](./client.md#test-dns-answer)
- [update_health_check](./client.md#update-health-check)
- [update_hosted_zone_comment](./client.md#update-hosted-zone-comment)
- [update_traffic_policy_comment](./client.md#update-traffic-policy-comment)
- [update_traffic_policy_instance](./client.md#update-traffic-policy-instance)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConcurrentModification](./client.md#concurrentmodification)
- [ConflictingDomainExists](./client.md#conflictingdomainexists)
- [ConflictingTypes](./client.md#conflictingtypes)
- [DNSSECNotFound](./client.md#dnssecnotfound)
- [DelegationSetAlreadyCreated](./client.md#delegationsetalreadycreated)
- [DelegationSetAlreadyReusable](./client.md#delegationsetalreadyreusable)
- [DelegationSetInUse](./client.md#delegationsetinuse)
- [DelegationSetNotAvailable](./client.md#delegationsetnotavailable)
- [DelegationSetNotReusable](./client.md#delegationsetnotreusable)
- [HealthCheckAlreadyExists](./client.md#healthcheckalreadyexists)
- [HealthCheckInUse](./client.md#healthcheckinuse)
- [HealthCheckVersionMismatch](./client.md#healthcheckversionmismatch)
- [HostedZoneAlreadyExists](./client.md#hostedzonealreadyexists)
- [HostedZoneNotEmpty](./client.md#hostedzonenotempty)
- [HostedZoneNotFound](./client.md#hostedzonenotfound)
- [HostedZoneNotPrivate](./client.md#hostedzonenotprivate)
- [HostedZonePartiallyDelegated](./client.md#hostedzonepartiallydelegated)
- [IncompatibleVersion](./client.md#incompatibleversion)
- [InsufficientCloudWatchLogsResourcePolicy](./client.md#insufficientcloudwatchlogsresourcepolicy)
- [InvalidArgument](./client.md#invalidargument)
- [InvalidChangeBatch](./client.md#invalidchangebatch)
- [InvalidDomainName](./client.md#invaliddomainname)
- [InvalidInput](./client.md#invalidinput)
- [InvalidKMSArn](./client.md#invalidkmsarn)
- [InvalidKeySigningKeyName](./client.md#invalidkeysigningkeyname)
- [InvalidKeySigningKeyStatus](./client.md#invalidkeysigningkeystatus)
- [InvalidPaginationToken](./client.md#invalidpaginationtoken)
- [InvalidSigningStatus](./client.md#invalidsigningstatus)
- [InvalidTrafficPolicyDocument](./client.md#invalidtrafficpolicydocument)
- [InvalidVPCId](./client.md#invalidvpcid)
- [KeySigningKeyAlreadyExists](./client.md#keysigningkeyalreadyexists)
- [KeySigningKeyInParentDSRecord](./client.md#keysigningkeyinparentdsrecord)
- [KeySigningKeyInUse](./client.md#keysigningkeyinuse)
- [KeySigningKeyWithActiveStatusNotFound](./client.md#keysigningkeywithactivestatusnotfound)
- [LastVPCAssociation](./client.md#lastvpcassociation)
- [LimitsExceeded](./client.md#limitsexceeded)
- [NoSuchChange](./client.md#nosuchchange)
- [NoSuchCloudWatchLogsLogGroup](./client.md#nosuchcloudwatchlogsloggroup)
- [NoSuchDelegationSet](./client.md#nosuchdelegationset)
- [NoSuchGeoLocation](./client.md#nosuchgeolocation)
- [NoSuchHealthCheck](./client.md#nosuchhealthcheck)
- [NoSuchHostedZone](./client.md#nosuchhostedzone)
- [NoSuchKeySigningKey](./client.md#nosuchkeysigningkey)
- [NoSuchQueryLoggingConfig](./client.md#nosuchqueryloggingconfig)
- [NoSuchTrafficPolicy](./client.md#nosuchtrafficpolicy)
- [NoSuchTrafficPolicyInstance](./client.md#nosuchtrafficpolicyinstance)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [PriorRequestNotComplete](./client.md#priorrequestnotcomplete)
- [PublicZoneVPCAssociation](./client.md#publiczonevpcassociation)
- [QueryLoggingConfigAlreadyExists](./client.md#queryloggingconfigalreadyexists)
- [ThrottlingException](./client.md#throttlingexception)
- [TooManyHealthChecks](./client.md#toomanyhealthchecks)
- [TooManyHostedZones](./client.md#toomanyhostedzones)
- [TooManyKeySigningKeys](./client.md#toomanykeysigningkeys)
- [TooManyTrafficPolicies](./client.md#toomanytrafficpolicies)
- [TooManyTrafficPolicyInstances](./client.md#toomanytrafficpolicyinstances)
- [TooManyTrafficPolicyVersionsForCurrentPolicy](./client.md#toomanytrafficpolicyversionsforcurrentpolicy)
- [TooManyVPCAssociationAuthorizations](./client.md#toomanyvpcassociationauthorizations)
- [TrafficPolicyAlreadyExists](./client.md#trafficpolicyalreadyexists)
- [TrafficPolicyInUse](./client.md#trafficpolicyinuse)
- [TrafficPolicyInstanceAlreadyExists](./client.md#trafficpolicyinstancealreadyexists)
- [VPCAssociationAuthorizationNotFound](./client.md#vpcassociationauthorizationnotfound)
- [VPCAssociationNotFound](./client.md#vpcassociationnotfound)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("route53").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_route53.paginators import ListHealthChecksPaginator, ...
```

- [ListHealthChecksPaginator](./paginators.md#listhealthcheckspaginator)
- [ListHostedZonesPaginator](./paginators.md#listhostedzonespaginator)
- [ListQueryLoggingConfigsPaginator](./paginators.md#listqueryloggingconfigspaginator)
- [ListResourceRecordSetsPaginator](./paginators.md#listresourcerecordsetspaginator)
- [ListVPCAssociationAuthorizationsPaginator](./paginators.md#listvpcassociationauthorizationspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("route53").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_route53.waiters import ResourceRecordSetsChangedWaiter, ...
```

- [ResourceRecordSetsChangedWaiter](./waiters.md#resourcerecordsetschangedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_route53.literals import AccountLimitType, ...
```

- [AccountLimitType](./literals.md#accountlimittype)
- [ChangeAction](./literals.md#changeaction)
- [ChangeStatus](./literals.md#changestatus)
- [CloudWatchRegion](./literals.md#cloudwatchregion)
- [ComparisonOperator](./literals.md#comparisonoperator)
- [HealthCheckRegion](./literals.md#healthcheckregion)
- [HealthCheckType](./literals.md#healthchecktype)
- [HostedZoneLimitType](./literals.md#hostedzonelimittype)
- [InsufficientDataHealthStatus](./literals.md#insufficientdatahealthstatus)
- [ListHealthChecksPaginatorName](./literals.md#listhealthcheckspaginatorname)
- [ListHostedZonesPaginatorName](./literals.md#listhostedzonespaginatorname)
- [ListQueryLoggingConfigsPaginatorName](./literals.md#listqueryloggingconfigspaginatorname)
- [ListResourceRecordSetsPaginatorName](./literals.md#listresourcerecordsetspaginatorname)
- [ListVPCAssociationAuthorizationsPaginatorName](./literals.md#listvpcassociationauthorizationspaginatorname)
- [RRType](./literals.md#rrtype)
- [ResettableElementName](./literals.md#resettableelementname)
- [ResourceRecordSetFailover](./literals.md#resourcerecordsetfailover)
- [ResourceRecordSetRegion](./literals.md#resourcerecordsetregion)
- [ResourceRecordSetsChangedWaiterName](./literals.md#resourcerecordsetschangedwaitername)
- [ReusableDelegationSetLimitType](./literals.md#reusabledelegationsetlimittype)
- [Statistic](./literals.md#statistic)
- [TagResourceType](./literals.md#tagresourcetype)
- [VPCRegion](./literals.md#vpcregion)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_route53.type_defs import AccountLimitTypeDef, ...
```

- [AccountLimitTypeDef](./type_defs.md#accountlimittypedef)
- [ActivateKeySigningKeyResponseTypeDef](./type_defs.md#activatekeysigningkeyresponsetypedef)
- [AlarmIdentifierTypeDef](./type_defs.md#alarmidentifiertypedef)
- [AliasTargetTypeDef](./type_defs.md#aliastargettypedef)
- [AssociateVPCWithHostedZoneResponseTypeDef](./type_defs.md#associatevpcwithhostedzoneresponsetypedef)
- [ChangeBatchTypeDef](./type_defs.md#changebatchtypedef)
- [ChangeInfoTypeDef](./type_defs.md#changeinfotypedef)
- [ChangeResourceRecordSetsResponseTypeDef](./type_defs.md#changeresourcerecordsetsresponsetypedef)
- [ChangeTypeDef](./type_defs.md#changetypedef)
- [CloudWatchAlarmConfigurationTypeDef](./type_defs.md#cloudwatchalarmconfigurationtypedef)
- [CreateHealthCheckResponseTypeDef](./type_defs.md#createhealthcheckresponsetypedef)
- [CreateHostedZoneResponseTypeDef](./type_defs.md#createhostedzoneresponsetypedef)
- [CreateKeySigningKeyResponseTypeDef](./type_defs.md#createkeysigningkeyresponsetypedef)
- [CreateQueryLoggingConfigResponseTypeDef](./type_defs.md#createqueryloggingconfigresponsetypedef)
- [CreateReusableDelegationSetResponseTypeDef](./type_defs.md#createreusabledelegationsetresponsetypedef)
- [CreateTrafficPolicyInstanceResponseTypeDef](./type_defs.md#createtrafficpolicyinstanceresponsetypedef)
- [CreateTrafficPolicyResponseTypeDef](./type_defs.md#createtrafficpolicyresponsetypedef)
- [CreateTrafficPolicyVersionResponseTypeDef](./type_defs.md#createtrafficpolicyversionresponsetypedef)
- [CreateVPCAssociationAuthorizationResponseTypeDef](./type_defs.md#createvpcassociationauthorizationresponsetypedef)
- [DNSSECStatusTypeDef](./type_defs.md#dnssecstatustypedef)
- [DeactivateKeySigningKeyResponseTypeDef](./type_defs.md#deactivatekeysigningkeyresponsetypedef)
- [DelegationSetTypeDef](./type_defs.md#delegationsettypedef)
- [DeleteHostedZoneResponseTypeDef](./type_defs.md#deletehostedzoneresponsetypedef)
- [DeleteKeySigningKeyResponseTypeDef](./type_defs.md#deletekeysigningkeyresponsetypedef)
- [DimensionTypeDef](./type_defs.md#dimensiontypedef)
- [DisableHostedZoneDNSSECResponseTypeDef](./type_defs.md#disablehostedzonednssecresponsetypedef)
- [DisassociateVPCFromHostedZoneResponseTypeDef](./type_defs.md#disassociatevpcfromhostedzoneresponsetypedef)
- [EnableHostedZoneDNSSECResponseTypeDef](./type_defs.md#enablehostedzonednssecresponsetypedef)
- [GeoLocationDetailsTypeDef](./type_defs.md#geolocationdetailstypedef)
- [GeoLocationTypeDef](./type_defs.md#geolocationtypedef)
- [GetAccountLimitResponseTypeDef](./type_defs.md#getaccountlimitresponsetypedef)
- [GetChangeResponseTypeDef](./type_defs.md#getchangeresponsetypedef)
- [GetCheckerIpRangesResponseTypeDef](./type_defs.md#getcheckeriprangesresponsetypedef)
- [GetDNSSECResponseTypeDef](./type_defs.md#getdnssecresponsetypedef)
- [GetGeoLocationResponseTypeDef](./type_defs.md#getgeolocationresponsetypedef)
- [GetHealthCheckCountResponseTypeDef](./type_defs.md#gethealthcheckcountresponsetypedef)
- [GetHealthCheckLastFailureReasonResponseTypeDef](./type_defs.md#gethealthchecklastfailurereasonresponsetypedef)
- [GetHealthCheckResponseTypeDef](./type_defs.md#gethealthcheckresponsetypedef)
- [GetHealthCheckStatusResponseTypeDef](./type_defs.md#gethealthcheckstatusresponsetypedef)
- [GetHostedZoneCountResponseTypeDef](./type_defs.md#gethostedzonecountresponsetypedef)
- [GetHostedZoneLimitResponseTypeDef](./type_defs.md#gethostedzonelimitresponsetypedef)
- [GetHostedZoneResponseTypeDef](./type_defs.md#gethostedzoneresponsetypedef)
- [GetQueryLoggingConfigResponseTypeDef](./type_defs.md#getqueryloggingconfigresponsetypedef)
- [GetReusableDelegationSetLimitResponseTypeDef](./type_defs.md#getreusabledelegationsetlimitresponsetypedef)
- [GetReusableDelegationSetResponseTypeDef](./type_defs.md#getreusabledelegationsetresponsetypedef)
- [GetTrafficPolicyInstanceCountResponseTypeDef](./type_defs.md#gettrafficpolicyinstancecountresponsetypedef)
- [GetTrafficPolicyInstanceResponseTypeDef](./type_defs.md#gettrafficpolicyinstanceresponsetypedef)
- [GetTrafficPolicyResponseTypeDef](./type_defs.md#gettrafficpolicyresponsetypedef)
- [HealthCheckConfigTypeDef](./type_defs.md#healthcheckconfigtypedef)
- [HealthCheckObservationTypeDef](./type_defs.md#healthcheckobservationtypedef)
- [HealthCheckTypeDef](./type_defs.md#healthchecktypedef)
- [HostedZoneConfigTypeDef](./type_defs.md#hostedzoneconfigtypedef)
- [HostedZoneLimitTypeDef](./type_defs.md#hostedzonelimittypedef)
- [HostedZoneOwnerTypeDef](./type_defs.md#hostedzoneownertypedef)
- [HostedZoneSummaryTypeDef](./type_defs.md#hostedzonesummarytypedef)
- [HostedZoneTypeDef](./type_defs.md#hostedzonetypedef)
- [KeySigningKeyTypeDef](./type_defs.md#keysigningkeytypedef)
- [LinkedServiceTypeDef](./type_defs.md#linkedservicetypedef)
- [ListGeoLocationsResponseTypeDef](./type_defs.md#listgeolocationsresponsetypedef)
- [ListHealthChecksResponseTypeDef](./type_defs.md#listhealthchecksresponsetypedef)
- [ListHostedZonesByNameResponseTypeDef](./type_defs.md#listhostedzonesbynameresponsetypedef)
- [ListHostedZonesByVPCResponseTypeDef](./type_defs.md#listhostedzonesbyvpcresponsetypedef)
- [ListHostedZonesResponseTypeDef](./type_defs.md#listhostedzonesresponsetypedef)
- [ListQueryLoggingConfigsResponseTypeDef](./type_defs.md#listqueryloggingconfigsresponsetypedef)
- [ListResourceRecordSetsResponseTypeDef](./type_defs.md#listresourcerecordsetsresponsetypedef)
- [ListReusableDelegationSetsResponseTypeDef](./type_defs.md#listreusabledelegationsetsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTagsForResourcesResponseTypeDef](./type_defs.md#listtagsforresourcesresponsetypedef)
- [ListTrafficPoliciesResponseTypeDef](./type_defs.md#listtrafficpoliciesresponsetypedef)
- [ListTrafficPolicyInstancesByHostedZoneResponseTypeDef](./type_defs.md#listtrafficpolicyinstancesbyhostedzoneresponsetypedef)
- [ListTrafficPolicyInstancesByPolicyResponseTypeDef](./type_defs.md#listtrafficpolicyinstancesbypolicyresponsetypedef)
- [ListTrafficPolicyInstancesResponseTypeDef](./type_defs.md#listtrafficpolicyinstancesresponsetypedef)
- [ListTrafficPolicyVersionsResponseTypeDef](./type_defs.md#listtrafficpolicyversionsresponsetypedef)
- [ListVPCAssociationAuthorizationsResponseTypeDef](./type_defs.md#listvpcassociationauthorizationsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [QueryLoggingConfigTypeDef](./type_defs.md#queryloggingconfigtypedef)
- [ResourceRecordSetTypeDef](./type_defs.md#resourcerecordsettypedef)
- [ResourceRecordTypeDef](./type_defs.md#resourcerecordtypedef)
- [ResourceTagSetTypeDef](./type_defs.md#resourcetagsettypedef)
- [ReusableDelegationSetLimitTypeDef](./type_defs.md#reusabledelegationsetlimittypedef)
- [StatusReportTypeDef](./type_defs.md#statusreporttypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TestDNSAnswerResponseTypeDef](./type_defs.md#testdnsanswerresponsetypedef)
- [TrafficPolicyInstanceTypeDef](./type_defs.md#trafficpolicyinstancetypedef)
- [TrafficPolicySummaryTypeDef](./type_defs.md#trafficpolicysummarytypedef)
- [TrafficPolicyTypeDef](./type_defs.md#trafficpolicytypedef)
- [UpdateHealthCheckResponseTypeDef](./type_defs.md#updatehealthcheckresponsetypedef)
- [UpdateHostedZoneCommentResponseTypeDef](./type_defs.md#updatehostedzonecommentresponsetypedef)
- [UpdateTrafficPolicyCommentResponseTypeDef](./type_defs.md#updatetrafficpolicycommentresponsetypedef)
- [UpdateTrafficPolicyInstanceResponseTypeDef](./type_defs.md#updatetrafficpolicyinstanceresponsetypedef)
- [VPCTypeDef](./type_defs.md#vpctypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
