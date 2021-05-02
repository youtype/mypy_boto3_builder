# Type annotations for boto3 ElasticsearchService module

> [Index](../index.md) > ElasticsearchService

Auto-generated documentation for [ElasticsearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService)
type annotations stubs module [mypy_boto3_es](https://pypi.org/project/mypy-boto3-es/).

```bash
pip install mypy-boto3-es
```

- [Type annotations for boto3 ElasticsearchService module](#type-annotations-for-boto3-elasticsearchservice-module)
  - [ElasticsearchServiceClient](#elasticsearchserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ElasticsearchServiceClient

Type annotations for  `boto3.client("es")` as [ElasticsearchServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_es.client import ElasticsearchServiceClient
```


ElasticsearchServiceClient [exceptions](./client.md#exceptions)



### Methods
- [accept_inbound_cross_cluster_search_connection](./client.md#accept-inbound-cross-cluster-search-connection)
- [add_tags](./client.md#add-tags)
- [associate_package](./client.md#associate-package)
- [can_paginate](./client.md#can-paginate)
- [cancel_elasticsearch_service_software_update](./client.md#cancel-elasticsearch-service-software-update)
- [create_elasticsearch_domain](./client.md#create-elasticsearch-domain)
- [create_outbound_cross_cluster_search_connection](./client.md#create-outbound-cross-cluster-search-connection)
- [create_package](./client.md#create-package)
- [delete_elasticsearch_domain](./client.md#delete-elasticsearch-domain)
- [delete_elasticsearch_service_role](./client.md#delete-elasticsearch-service-role)
- [delete_inbound_cross_cluster_search_connection](./client.md#delete-inbound-cross-cluster-search-connection)
- [delete_outbound_cross_cluster_search_connection](./client.md#delete-outbound-cross-cluster-search-connection)
- [delete_package](./client.md#delete-package)
- [describe_domain_auto_tunes](./client.md#describe-domain-auto-tunes)
- [describe_elasticsearch_domain](./client.md#describe-elasticsearch-domain)
- [describe_elasticsearch_domain_config](./client.md#describe-elasticsearch-domain-config)
- [describe_elasticsearch_domains](./client.md#describe-elasticsearch-domains)
- [describe_elasticsearch_instance_type_limits](./client.md#describe-elasticsearch-instance-type-limits)
- [describe_inbound_cross_cluster_search_connections](./client.md#describe-inbound-cross-cluster-search-connections)
- [describe_outbound_cross_cluster_search_connections](./client.md#describe-outbound-cross-cluster-search-connections)
- [describe_packages](./client.md#describe-packages)
- [describe_reserved_elasticsearch_instance_offerings](./client.md#describe-reserved-elasticsearch-instance-offerings)
- [describe_reserved_elasticsearch_instances](./client.md#describe-reserved-elasticsearch-instances)
- [dissociate_package](./client.md#dissociate-package)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_compatible_elasticsearch_versions](./client.md#get-compatible-elasticsearch-versions)
- [get_package_version_history](./client.md#get-package-version-history)
- [get_paginator](./client.md#get-paginator)
- [get_upgrade_history](./client.md#get-upgrade-history)
- [get_upgrade_status](./client.md#get-upgrade-status)
- [list_domain_names](./client.md#list-domain-names)
- [list_domains_for_package](./client.md#list-domains-for-package)
- [list_elasticsearch_instance_types](./client.md#list-elasticsearch-instance-types)
- [list_elasticsearch_versions](./client.md#list-elasticsearch-versions)
- [list_packages_for_domain](./client.md#list-packages-for-domain)
- [list_tags](./client.md#list-tags)
- [purchase_reserved_elasticsearch_instance_offering](./client.md#purchase-reserved-elasticsearch-instance-offering)
- [reject_inbound_cross_cluster_search_connection](./client.md#reject-inbound-cross-cluster-search-connection)
- [remove_tags](./client.md#remove-tags)
- [start_elasticsearch_service_software_update](./client.md#start-elasticsearch-service-software-update)
- [update_elasticsearch_domain_config](./client.md#update-elasticsearch-domain-config)
- [update_package](./client.md#update-package)
- [upgrade_elasticsearch_domain](./client.md#upgrade-elasticsearch-domain)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BaseException](./client.md#baseexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [DisabledOperationException](./client.md#disabledoperationexception)
- [InternalException](./client.md#internalexception)
- [InvalidPaginationTokenException](./client.md#invalidpaginationtokenexception)
- [InvalidTypeException](./client.md#invalidtypeexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("es").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_es.paginators import DescribeReservedElasticsearchInstanceOfferingsPaginator, ...
```

- [DescribeReservedElasticsearchInstanceOfferingsPaginator](./paginators.md#describereservedelasticsearchinstanceofferingspaginator)
- [DescribeReservedElasticsearchInstancesPaginator](./paginators.md#describereservedelasticsearchinstancespaginator)
- [GetUpgradeHistoryPaginator](./paginators.md#getupgradehistorypaginator)
- [ListElasticsearchInstanceTypesPaginator](./paginators.md#listelasticsearchinstancetypespaginator)
- [ListElasticsearchVersionsPaginator](./paginators.md#listelasticsearchversionspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_es.literals import AutoTuneDesiredState, ...
```

- [AutoTuneDesiredState](./literals.md#autotunedesiredstate)
- [AutoTuneState](./literals.md#autotunestate)
- [AutoTuneType](./literals.md#autotunetype)
- [DeploymentStatus](./literals.md#deploymentstatus)
- [DescribePackagesFilterName](./literals.md#describepackagesfiltername)
- [DescribeReservedElasticsearchInstanceOfferingsPaginatorName](./literals.md#describereservedelasticsearchinstanceofferingspaginatorname)
- [DescribeReservedElasticsearchInstancesPaginatorName](./literals.md#describereservedelasticsearchinstancespaginatorname)
- [DomainPackageStatus](./literals.md#domainpackagestatus)
- [ESPartitionInstanceType](./literals.md#espartitioninstancetype)
- [ESWarmPartitionInstanceType](./literals.md#eswarmpartitioninstancetype)
- [GetUpgradeHistoryPaginatorName](./literals.md#getupgradehistorypaginatorname)
- [InboundCrossClusterSearchConnectionStatusCode](./literals.md#inboundcrossclustersearchconnectionstatuscode)
- [ListElasticsearchInstanceTypesPaginatorName](./literals.md#listelasticsearchinstancetypespaginatorname)
- [ListElasticsearchVersionsPaginatorName](./literals.md#listelasticsearchversionspaginatorname)
- [LogType](./literals.md#logtype)
- [OptionState](./literals.md#optionstate)
- [OutboundCrossClusterSearchConnectionStatusCode](./literals.md#outboundcrossclustersearchconnectionstatuscode)
- [PackageStatus](./literals.md#packagestatus)
- [PackageType](./literals.md#packagetype)
- [ReservedElasticsearchInstancePaymentOption](./literals.md#reservedelasticsearchinstancepaymentoption)
- [RollbackOnDisable](./literals.md#rollbackondisable)
- [ScheduledAutoTuneActionType](./literals.md#scheduledautotuneactiontype)
- [ScheduledAutoTuneSeverityType](./literals.md#scheduledautotuneseveritytype)
- [TLSSecurityPolicy](./literals.md#tlssecuritypolicy)
- [TimeUnit](./literals.md#timeunit)
- [UpgradeStatus](./literals.md#upgradestatus)
- [UpgradeStep](./literals.md#upgradestep)
- [VolumeType](./literals.md#volumetype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_es.type_defs import AccessPoliciesStatusTypeDef, ...
```

- [AccessPoliciesStatusTypeDef](./type_defs.md#accesspoliciesstatustypedef)
- [AdditionalLimitTypeDef](./type_defs.md#additionallimittypedef)
- [AdvancedOptionsStatusTypeDef](./type_defs.md#advancedoptionsstatustypedef)
- [AdvancedSecurityOptionsStatusTypeDef](./type_defs.md#advancedsecurityoptionsstatustypedef)
- [AdvancedSecurityOptionsTypeDef](./type_defs.md#advancedsecurityoptionstypedef)
- [AutoTuneDetailsTypeDef](./type_defs.md#autotunedetailstypedef)
- [AutoTuneMaintenanceScheduleTypeDef](./type_defs.md#autotunemaintenancescheduletypedef)
- [AutoTuneOptionsOutputTypeDef](./type_defs.md#autotuneoptionsoutputtypedef)
- [AutoTuneOptionsStatusTypeDef](./type_defs.md#autotuneoptionsstatustypedef)
- [AutoTuneOptionsTypeDef](./type_defs.md#autotuneoptionstypedef)
- [AutoTuneStatusTypeDef](./type_defs.md#autotunestatustypedef)
- [AutoTuneTypeDef](./type_defs.md#autotunetypedef)
- [CognitoOptionsStatusTypeDef](./type_defs.md#cognitooptionsstatustypedef)
- [CognitoOptionsTypeDef](./type_defs.md#cognitooptionstypedef)
- [CompatibleVersionsMapTypeDef](./type_defs.md#compatibleversionsmaptypedef)
- [DomainEndpointOptionsStatusTypeDef](./type_defs.md#domainendpointoptionsstatustypedef)
- [DomainEndpointOptionsTypeDef](./type_defs.md#domainendpointoptionstypedef)
- [DomainInfoTypeDef](./type_defs.md#domaininfotypedef)
- [DomainInformationTypeDef](./type_defs.md#domaininformationtypedef)
- [DomainPackageDetailsTypeDef](./type_defs.md#domainpackagedetailstypedef)
- [DurationTypeDef](./type_defs.md#durationtypedef)
- [EBSOptionsStatusTypeDef](./type_defs.md#ebsoptionsstatustypedef)
- [EBSOptionsTypeDef](./type_defs.md#ebsoptionstypedef)
- [ElasticsearchClusterConfigStatusTypeDef](./type_defs.md#elasticsearchclusterconfigstatustypedef)
- [ElasticsearchClusterConfigTypeDef](./type_defs.md#elasticsearchclusterconfigtypedef)
- [ElasticsearchDomainConfigTypeDef](./type_defs.md#elasticsearchdomainconfigtypedef)
- [ElasticsearchDomainStatusTypeDef](./type_defs.md#elasticsearchdomainstatustypedef)
- [ElasticsearchVersionStatusTypeDef](./type_defs.md#elasticsearchversionstatustypedef)
- [EncryptionAtRestOptionsStatusTypeDef](./type_defs.md#encryptionatrestoptionsstatustypedef)
- [EncryptionAtRestOptionsTypeDef](./type_defs.md#encryptionatrestoptionstypedef)
- [ErrorDetailsTypeDef](./type_defs.md#errordetailstypedef)
- [InboundCrossClusterSearchConnectionStatusTypeDef](./type_defs.md#inboundcrossclustersearchconnectionstatustypedef)
- [InboundCrossClusterSearchConnectionTypeDef](./type_defs.md#inboundcrossclustersearchconnectiontypedef)
- [InstanceCountLimitsTypeDef](./type_defs.md#instancecountlimitstypedef)
- [InstanceLimitsTypeDef](./type_defs.md#instancelimitstypedef)
- [LimitsTypeDef](./type_defs.md#limitstypedef)
- [LogPublishingOptionTypeDef](./type_defs.md#logpublishingoptiontypedef)
- [LogPublishingOptionsStatusTypeDef](./type_defs.md#logpublishingoptionsstatustypedef)
- [MasterUserOptionsTypeDef](./type_defs.md#masteruseroptionstypedef)
- [NodeToNodeEncryptionOptionsStatusTypeDef](./type_defs.md#nodetonodeencryptionoptionsstatustypedef)
- [NodeToNodeEncryptionOptionsTypeDef](./type_defs.md#nodetonodeencryptionoptionstypedef)
- [OptionStatusTypeDef](./type_defs.md#optionstatustypedef)
- [OutboundCrossClusterSearchConnectionStatusTypeDef](./type_defs.md#outboundcrossclustersearchconnectionstatustypedef)
- [OutboundCrossClusterSearchConnectionTypeDef](./type_defs.md#outboundcrossclustersearchconnectiontypedef)
- [PackageDetailsTypeDef](./type_defs.md#packagedetailstypedef)
- [PackageVersionHistoryTypeDef](./type_defs.md#packageversionhistorytypedef)
- [RecurringChargeTypeDef](./type_defs.md#recurringchargetypedef)
- [ReservedElasticsearchInstanceOfferingTypeDef](./type_defs.md#reservedelasticsearchinstanceofferingtypedef)
- [ReservedElasticsearchInstanceTypeDef](./type_defs.md#reservedelasticsearchinstancetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SAMLIdpTypeDef](./type_defs.md#samlidptypedef)
- [SAMLOptionsInputTypeDef](./type_defs.md#samloptionsinputtypedef)
- [SAMLOptionsOutputTypeDef](./type_defs.md#samloptionsoutputtypedef)
- [ScheduledAutoTuneDetailsTypeDef](./type_defs.md#scheduledautotunedetailstypedef)
- [ServiceSoftwareOptionsTypeDef](./type_defs.md#servicesoftwareoptionstypedef)
- [SnapshotOptionsStatusTypeDef](./type_defs.md#snapshotoptionsstatustypedef)
- [SnapshotOptionsTypeDef](./type_defs.md#snapshotoptionstypedef)
- [StorageTypeLimitTypeDef](./type_defs.md#storagetypelimittypedef)
- [StorageTypeTypeDef](./type_defs.md#storagetypetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [UpgradeHistoryTypeDef](./type_defs.md#upgradehistorytypedef)
- [UpgradeStepItemTypeDef](./type_defs.md#upgradestepitemtypedef)
- [VPCDerivedInfoStatusTypeDef](./type_defs.md#vpcderivedinfostatustypedef)
- [VPCDerivedInfoTypeDef](./type_defs.md#vpcderivedinfotypedef)
- [ZoneAwarenessConfigTypeDef](./type_defs.md#zoneawarenessconfigtypedef)
- [AcceptInboundCrossClusterSearchConnectionResponseTypeDef](./type_defs.md#acceptinboundcrossclustersearchconnectionresponsetypedef)
- [AdvancedSecurityOptionsInputTypeDef](./type_defs.md#advancedsecurityoptionsinputtypedef)
- [AssociatePackageResponseTypeDef](./type_defs.md#associatepackageresponsetypedef)
- [AutoTuneOptionsInputTypeDef](./type_defs.md#autotuneoptionsinputtypedef)
- [CancelElasticsearchServiceSoftwareUpdateResponseTypeDef](./type_defs.md#cancelelasticsearchservicesoftwareupdateresponsetypedef)
- [CreateElasticsearchDomainResponseTypeDef](./type_defs.md#createelasticsearchdomainresponsetypedef)
- [CreateOutboundCrossClusterSearchConnectionResponseTypeDef](./type_defs.md#createoutboundcrossclustersearchconnectionresponsetypedef)
- [CreatePackageResponseTypeDef](./type_defs.md#createpackageresponsetypedef)
- [DeleteElasticsearchDomainResponseTypeDef](./type_defs.md#deleteelasticsearchdomainresponsetypedef)
- [DeleteInboundCrossClusterSearchConnectionResponseTypeDef](./type_defs.md#deleteinboundcrossclustersearchconnectionresponsetypedef)
- [DeleteOutboundCrossClusterSearchConnectionResponseTypeDef](./type_defs.md#deleteoutboundcrossclustersearchconnectionresponsetypedef)
- [DeletePackageResponseTypeDef](./type_defs.md#deletepackageresponsetypedef)
- [DescribeDomainAutoTunesResponseTypeDef](./type_defs.md#describedomainautotunesresponsetypedef)
- [DescribeElasticsearchDomainConfigResponseTypeDef](./type_defs.md#describeelasticsearchdomainconfigresponsetypedef)
- [DescribeElasticsearchDomainResponseTypeDef](./type_defs.md#describeelasticsearchdomainresponsetypedef)
- [DescribeElasticsearchDomainsResponseTypeDef](./type_defs.md#describeelasticsearchdomainsresponsetypedef)
- [DescribeElasticsearchInstanceTypeLimitsResponseTypeDef](./type_defs.md#describeelasticsearchinstancetypelimitsresponsetypedef)
- [DescribeInboundCrossClusterSearchConnectionsResponseTypeDef](./type_defs.md#describeinboundcrossclustersearchconnectionsresponsetypedef)
- [DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef](./type_defs.md#describeoutboundcrossclustersearchconnectionsresponsetypedef)
- [DescribePackagesFilterTypeDef](./type_defs.md#describepackagesfiltertypedef)
- [DescribePackagesResponseTypeDef](./type_defs.md#describepackagesresponsetypedef)
- [DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef](./type_defs.md#describereservedelasticsearchinstanceofferingsresponsetypedef)
- [DescribeReservedElasticsearchInstancesResponseTypeDef](./type_defs.md#describereservedelasticsearchinstancesresponsetypedef)
- [DissociatePackageResponseTypeDef](./type_defs.md#dissociatepackageresponsetypedef)
- [FilterTypeDef](./type_defs.md#filtertypedef)
- [GetCompatibleElasticsearchVersionsResponseTypeDef](./type_defs.md#getcompatibleelasticsearchversionsresponsetypedef)
- [GetPackageVersionHistoryResponseTypeDef](./type_defs.md#getpackageversionhistoryresponsetypedef)
- [GetUpgradeHistoryResponseTypeDef](./type_defs.md#getupgradehistoryresponsetypedef)
- [GetUpgradeStatusResponseTypeDef](./type_defs.md#getupgradestatusresponsetypedef)
- [ListDomainNamesResponseTypeDef](./type_defs.md#listdomainnamesresponsetypedef)
- [ListDomainsForPackageResponseTypeDef](./type_defs.md#listdomainsforpackageresponsetypedef)
- [ListElasticsearchInstanceTypesResponseTypeDef](./type_defs.md#listelasticsearchinstancetypesresponsetypedef)
- [ListElasticsearchVersionsResponseTypeDef](./type_defs.md#listelasticsearchversionsresponsetypedef)
- [ListPackagesForDomainResponseTypeDef](./type_defs.md#listpackagesfordomainresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [PackageSourceTypeDef](./type_defs.md#packagesourcetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef](./type_defs.md#purchasereservedelasticsearchinstanceofferingresponsetypedef)
- [RejectInboundCrossClusterSearchConnectionResponseTypeDef](./type_defs.md#rejectinboundcrossclustersearchconnectionresponsetypedef)
- [StartElasticsearchServiceSoftwareUpdateResponseTypeDef](./type_defs.md#startelasticsearchservicesoftwareupdateresponsetypedef)
- [UpdateElasticsearchDomainConfigResponseTypeDef](./type_defs.md#updateelasticsearchdomainconfigresponsetypedef)
- [UpdatePackageResponseTypeDef](./type_defs.md#updatepackageresponsetypedef)
- [UpgradeElasticsearchDomainResponseTypeDef](./type_defs.md#upgradeelasticsearchdomainresponsetypedef)
- [VPCOptionsTypeDef](./type_defs.md#vpcoptionstypedef)
