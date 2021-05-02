# ElasticsearchServiceClient for boto3 ElasticsearchService module

> [Index](../index.md) > [ElasticsearchService](./index.md) > ElasticsearchServiceClient

Auto-generated documentation for [ElasticsearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService)
type annotations stubs module [mypy_boto3_es](https://pypi.org/project/mypy-boto3-es/).

- [ElasticsearchServiceClient for boto3 ElasticsearchService module](#elasticsearchserviceclient-for-boto3-elasticsearchservice-module)
  - [ElasticsearchServiceClient](#elasticsearchserviceclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [accept_inbound_cross_cluster_search_connection](#accept_inbound_cross_cluster_search_connection)
    - [add_tags](#add_tags)
    - [associate_package](#associate_package)
    - [can_paginate](#can_paginate)
    - [cancel_elasticsearch_service_software_update](#cancel_elasticsearch_service_software_update)
    - [create_elasticsearch_domain](#create_elasticsearch_domain)
    - [create_outbound_cross_cluster_search_connection](#create_outbound_cross_cluster_search_connection)
    - [create_package](#create_package)
    - [delete_elasticsearch_domain](#delete_elasticsearch_domain)
    - [delete_elasticsearch_service_role](#delete_elasticsearch_service_role)
    - [delete_inbound_cross_cluster_search_connection](#delete_inbound_cross_cluster_search_connection)
    - [delete_outbound_cross_cluster_search_connection](#delete_outbound_cross_cluster_search_connection)
    - [delete_package](#delete_package)
    - [describe_domain_auto_tunes](#describe_domain_auto_tunes)
    - [describe_elasticsearch_domain](#describe_elasticsearch_domain)
    - [describe_elasticsearch_domain_config](#describe_elasticsearch_domain_config)
    - [describe_elasticsearch_domains](#describe_elasticsearch_domains)
    - [describe_elasticsearch_instance_type_limits](#describe_elasticsearch_instance_type_limits)
    - [describe_inbound_cross_cluster_search_connections](#describe_inbound_cross_cluster_search_connections)
    - [describe_outbound_cross_cluster_search_connections](#describe_outbound_cross_cluster_search_connections)
    - [describe_packages](#describe_packages)
    - [describe_reserved_elasticsearch_instance_offerings](#describe_reserved_elasticsearch_instance_offerings)
    - [describe_reserved_elasticsearch_instances](#describe_reserved_elasticsearch_instances)
    - [dissociate_package](#dissociate_package)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_compatible_elasticsearch_versions](#get_compatible_elasticsearch_versions)
    - [get_package_version_history](#get_package_version_history)
    - [get_upgrade_history](#get_upgrade_history)
    - [get_upgrade_status](#get_upgrade_status)
    - [list_domain_names](#list_domain_names)
    - [list_domains_for_package](#list_domains_for_package)
    - [list_elasticsearch_instance_types](#list_elasticsearch_instance_types)
    - [list_elasticsearch_versions](#list_elasticsearch_versions)
    - [list_packages_for_domain](#list_packages_for_domain)
    - [list_tags](#list_tags)
    - [purchase_reserved_elasticsearch_instance_offering](#purchase_reserved_elasticsearch_instance_offering)
    - [reject_inbound_cross_cluster_search_connection](#reject_inbound_cross_cluster_search_connection)
    - [remove_tags](#remove_tags)
    - [start_elasticsearch_service_software_update](#start_elasticsearch_service_software_update)
    - [update_elasticsearch_domain_config](#update_elasticsearch_domain_config)
    - [update_package](#update_package)
    - [upgrade_elasticsearch_domain](#upgrade_elasticsearch_domain)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)

## ElasticsearchServiceClient

Type annotations for `boto3.client("es")`

Can be used directly:

```python
from mypy_boto3_es.client import ElasticsearchServiceClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_es.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.BaseException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.DisabledOperationException`
- `Exceptions.InternalException`
- `Exceptions.InvalidPaginationTokenException`
- `Exceptions.InvalidTypeException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### accept_inbound_cross_cluster_search_connection

Type annotations for `boto3.client("es").accept_inbound_cross_cluster_search_connection` method.

[Client.accept_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.accept_inbound_cross_cluster_search_connection)

```python
def accept_inbound_cross_cluster_search_connection(
    self,
    CrossClusterSearchConnectionId: str
) -> AcceptInboundCrossClusterSearchConnectionResponseTypeDef:
    pass
```

### add_tags

Type annotations for `boto3.client("es").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.add_tags)

```python
def add_tags(
    self,
    ARN: str,
    TagList: List["TagTypeDef"]
) -> None:
    pass
```

### associate_package

Type annotations for `boto3.client("es").associate_package` method.

[Client.associate_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.associate_package)

```python
def associate_package(
    self,
    PackageID: str,
    DomainName: str
) -> AssociatePackageResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("es").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_elasticsearch_service_software_update

Type annotations for `boto3.client("es").cancel_elasticsearch_service_software_update` method.

[Client.cancel_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.cancel_elasticsearch_service_software_update)

```python
def cancel_elasticsearch_service_software_update(
    self,
    DomainName: str
) -> CancelElasticsearchServiceSoftwareUpdateResponseTypeDef:
    pass
```

### create_elasticsearch_domain

Type annotations for `boto3.client("es").create_elasticsearch_domain` method.

[Client.create_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.create_elasticsearch_domain)

```python
def create_elasticsearch_domain(
    self,
    DomainName: str,
    ElasticsearchVersion: str = None,
    ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
    EBSOptions: "EBSOptionsTypeDef" = None,
    AccessPolicies: str = None,
    SnapshotOptions: "SnapshotOptionsTypeDef" = None,
    VPCOptions: VPCOptionsTypeDef = None,
    CognitoOptions: "CognitoOptionsTypeDef" = None,
    EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
    NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
    AdvancedOptions: Dict[str, str] = None,
    LogPublishingOptions: Dict[LogType, "LogPublishingOptionTypeDef"] = None,
    DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
    AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
    AutoTuneOptions: AutoTuneOptionsInputTypeDef = None,
    TagList: List["TagTypeDef"] = None
) -> CreateElasticsearchDomainResponseTypeDef:
    pass
```

### create_outbound_cross_cluster_search_connection

Type annotations for `boto3.client("es").create_outbound_cross_cluster_search_connection` method.

[Client.create_outbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.create_outbound_cross_cluster_search_connection)

```python
def create_outbound_cross_cluster_search_connection(
    self,
    SourceDomainInfo: "DomainInformationTypeDef",
    DestinationDomainInfo: "DomainInformationTypeDef",
    ConnectionAlias: str
) -> CreateOutboundCrossClusterSearchConnectionResponseTypeDef:
    pass
```

### create_package

Type annotations for `boto3.client("es").create_package` method.

[Client.create_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.create_package)

```python
def create_package(
    self,
    PackageName: str,
    PackageType: PackageType,
    PackageSource: PackageSourceTypeDef,
    PackageDescription: str = None
) -> CreatePackageResponseTypeDef:
    pass
```

### delete_elasticsearch_domain

Type annotations for `boto3.client("es").delete_elasticsearch_domain` method.

[Client.delete_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_domain)

```python
def delete_elasticsearch_domain(
    self,
    DomainName: str
) -> DeleteElasticsearchDomainResponseTypeDef:
    pass
```

### delete_elasticsearch_service_role

Type annotations for `boto3.client("es").delete_elasticsearch_service_role` method.

[Client.delete_elasticsearch_service_role documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.delete_elasticsearch_service_role)

```python
def delete_elasticsearch_service_role(
    self
) -> None:
    pass
```

### delete_inbound_cross_cluster_search_connection

Type annotations for `boto3.client("es").delete_inbound_cross_cluster_search_connection` method.

[Client.delete_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.delete_inbound_cross_cluster_search_connection)

```python
def delete_inbound_cross_cluster_search_connection(
    self,
    CrossClusterSearchConnectionId: str
) -> DeleteInboundCrossClusterSearchConnectionResponseTypeDef:
    pass
```

### delete_outbound_cross_cluster_search_connection

Type annotations for `boto3.client("es").delete_outbound_cross_cluster_search_connection` method.

[Client.delete_outbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.delete_outbound_cross_cluster_search_connection)

```python
def delete_outbound_cross_cluster_search_connection(
    self,
    CrossClusterSearchConnectionId: str
) -> DeleteOutboundCrossClusterSearchConnectionResponseTypeDef:
    pass
```

### delete_package

Type annotations for `boto3.client("es").delete_package` method.

[Client.delete_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.delete_package)

```python
def delete_package(
    self,
    PackageID: str
) -> DeletePackageResponseTypeDef:
    pass
```

### describe_domain_auto_tunes

Type annotations for `boto3.client("es").describe_domain_auto_tunes` method.

[Client.describe_domain_auto_tunes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_domain_auto_tunes)

```python
def describe_domain_auto_tunes(
    self,
    DomainName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeDomainAutoTunesResponseTypeDef:
    pass
```

### describe_elasticsearch_domain

Type annotations for `boto3.client("es").describe_elasticsearch_domain` method.

[Client.describe_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain)

```python
def describe_elasticsearch_domain(
    self,
    DomainName: str
) -> DescribeElasticsearchDomainResponseTypeDef:
    pass
```

### describe_elasticsearch_domain_config

Type annotations for `boto3.client("es").describe_elasticsearch_domain_config` method.

[Client.describe_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domain_config)

```python
def describe_elasticsearch_domain_config(
    self,
    DomainName: str
) -> DescribeElasticsearchDomainConfigResponseTypeDef:
    pass
```

### describe_elasticsearch_domains

Type annotations for `boto3.client("es").describe_elasticsearch_domains` method.

[Client.describe_elasticsearch_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_domains)

```python
def describe_elasticsearch_domains(
    self,
    DomainNames: List[str]
) -> DescribeElasticsearchDomainsResponseTypeDef:
    pass
```

### describe_elasticsearch_instance_type_limits

Type annotations for `boto3.client("es").describe_elasticsearch_instance_type_limits` method.

[Client.describe_elasticsearch_instance_type_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_elasticsearch_instance_type_limits)

```python
def describe_elasticsearch_instance_type_limits(
    self,
    InstanceType: ESPartitionInstanceType,
    ElasticsearchVersion: str,
    DomainName: str = None
) -> DescribeElasticsearchInstanceTypeLimitsResponseTypeDef:
    pass
```

### describe_inbound_cross_cluster_search_connections

Type annotations for `boto3.client("es").describe_inbound_cross_cluster_search_connections` method.

[Client.describe_inbound_cross_cluster_search_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_inbound_cross_cluster_search_connections)

```python
def describe_inbound_cross_cluster_search_connections(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeInboundCrossClusterSearchConnectionsResponseTypeDef:
    pass
```

### describe_outbound_cross_cluster_search_connections

Type annotations for `boto3.client("es").describe_outbound_cross_cluster_search_connections` method.

[Client.describe_outbound_cross_cluster_search_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_outbound_cross_cluster_search_connections)

```python
def describe_outbound_cross_cluster_search_connections(
    self,
    Filters: List[FilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef:
    pass
```

### describe_packages

Type annotations for `boto3.client("es").describe_packages` method.

[Client.describe_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_packages)

```python
def describe_packages(
    self,
    Filters: List[DescribePackagesFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribePackagesResponseTypeDef:
    pass
```

### describe_reserved_elasticsearch_instance_offerings

Type annotations for `boto3.client("es").describe_reserved_elasticsearch_instance_offerings` method.

[Client.describe_reserved_elasticsearch_instance_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instance_offerings)

```python
def describe_reserved_elasticsearch_instance_offerings(
    self,
    ReservedElasticsearchInstanceOfferingId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
    pass
```

### describe_reserved_elasticsearch_instances

Type annotations for `boto3.client("es").describe_reserved_elasticsearch_instances` method.

[Client.describe_reserved_elasticsearch_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.describe_reserved_elasticsearch_instances)

```python
def describe_reserved_elasticsearch_instances(
    self,
    ReservedElasticsearchInstanceId: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
    pass
```

### dissociate_package

Type annotations for `boto3.client("es").dissociate_package` method.

[Client.dissociate_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.dissociate_package)

```python
def dissociate_package(
    self,
    PackageID: str,
    DomainName: str
) -> DissociatePackageResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("es").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.generate_presigned_url)

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

### get_compatible_elasticsearch_versions

Type annotations for `boto3.client("es").get_compatible_elasticsearch_versions` method.

[Client.get_compatible_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.get_compatible_elasticsearch_versions)

```python
def get_compatible_elasticsearch_versions(
    self,
    DomainName: str = None
) -> GetCompatibleElasticsearchVersionsResponseTypeDef:
    pass
```

### get_package_version_history

Type annotations for `boto3.client("es").get_package_version_history` method.

[Client.get_package_version_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.get_package_version_history)

```python
def get_package_version_history(
    self,
    PackageID: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetPackageVersionHistoryResponseTypeDef:
    pass
```

### get_upgrade_history

Type annotations for `boto3.client("es").get_upgrade_history` method.

[Client.get_upgrade_history documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.get_upgrade_history)

```python
def get_upgrade_history(
    self,
    DomainName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> GetUpgradeHistoryResponseTypeDef:
    pass
```

### get_upgrade_status

Type annotations for `boto3.client("es").get_upgrade_status` method.

[Client.get_upgrade_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.get_upgrade_status)

```python
def get_upgrade_status(
    self,
    DomainName: str
) -> GetUpgradeStatusResponseTypeDef:
    pass
```

### list_domain_names

Type annotations for `boto3.client("es").list_domain_names` method.

[Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.list_domain_names)

```python
def list_domain_names(
    self
) -> ListDomainNamesResponseTypeDef:
    pass
```

### list_domains_for_package

Type annotations for `boto3.client("es").list_domains_for_package` method.

[Client.list_domains_for_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.list_domains_for_package)

```python
def list_domains_for_package(
    self,
    PackageID: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListDomainsForPackageResponseTypeDef:
    pass
```

### list_elasticsearch_instance_types

Type annotations for `boto3.client("es").list_elasticsearch_instance_types` method.

[Client.list_elasticsearch_instance_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_instance_types)

```python
def list_elasticsearch_instance_types(
    self,
    ElasticsearchVersion: str,
    DomainName: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListElasticsearchInstanceTypesResponseTypeDef:
    pass
```

### list_elasticsearch_versions

Type annotations for `boto3.client("es").list_elasticsearch_versions` method.

[Client.list_elasticsearch_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.list_elasticsearch_versions)

```python
def list_elasticsearch_versions(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListElasticsearchVersionsResponseTypeDef:
    pass
```

### list_packages_for_domain

Type annotations for `boto3.client("es").list_packages_for_domain` method.

[Client.list_packages_for_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.list_packages_for_domain)

```python
def list_packages_for_domain(
    self,
    DomainName: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListPackagesForDomainResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("es").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.list_tags)

```python
def list_tags(
    self,
    ARN: str
) -> ListTagsResponseTypeDef:
    pass
```

### purchase_reserved_elasticsearch_instance_offering

Type annotations for `boto3.client("es").purchase_reserved_elasticsearch_instance_offering` method.

[Client.purchase_reserved_elasticsearch_instance_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.purchase_reserved_elasticsearch_instance_offering)

```python
def purchase_reserved_elasticsearch_instance_offering(
    self,
    ReservedElasticsearchInstanceOfferingId: str,
    ReservationName: str,
    InstanceCount: int = None
) -> PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef:
    pass
```

### reject_inbound_cross_cluster_search_connection

Type annotations for `boto3.client("es").reject_inbound_cross_cluster_search_connection` method.

[Client.reject_inbound_cross_cluster_search_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.reject_inbound_cross_cluster_search_connection)

```python
def reject_inbound_cross_cluster_search_connection(
    self,
    CrossClusterSearchConnectionId: str
) -> RejectInboundCrossClusterSearchConnectionResponseTypeDef:
    pass
```

### remove_tags

Type annotations for `boto3.client("es").remove_tags` method.

[Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.remove_tags)

```python
def remove_tags(
    self,
    ARN: str,
    TagKeys: List[str]
) -> None:
    pass
```

### start_elasticsearch_service_software_update

Type annotations for `boto3.client("es").start_elasticsearch_service_software_update` method.

[Client.start_elasticsearch_service_software_update documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.start_elasticsearch_service_software_update)

```python
def start_elasticsearch_service_software_update(
    self,
    DomainName: str
) -> StartElasticsearchServiceSoftwareUpdateResponseTypeDef:
    pass
```

### update_elasticsearch_domain_config

Type annotations for `boto3.client("es").update_elasticsearch_domain_config` method.

[Client.update_elasticsearch_domain_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.update_elasticsearch_domain_config)

```python
def update_elasticsearch_domain_config(
    self,
    DomainName: str,
    ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef" = None,
    EBSOptions: "EBSOptionsTypeDef" = None,
    SnapshotOptions: "SnapshotOptionsTypeDef" = None,
    VPCOptions: VPCOptionsTypeDef = None,
    CognitoOptions: "CognitoOptionsTypeDef" = None,
    AdvancedOptions: Dict[str, str] = None,
    AccessPolicies: str = None,
    LogPublishingOptions: Dict[LogType, "LogPublishingOptionTypeDef"] = None,
    DomainEndpointOptions: "DomainEndpointOptionsTypeDef" = None,
    AdvancedSecurityOptions: AdvancedSecurityOptionsInputTypeDef = None,
    NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef" = None,
    EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
    AutoTuneOptions: "AutoTuneOptionsTypeDef" = None
) -> UpdateElasticsearchDomainConfigResponseTypeDef:
    pass
```

### update_package

Type annotations for `boto3.client("es").update_package` method.

[Client.update_package documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.update_package)

```python
def update_package(
    self,
    PackageID: str,
    PackageSource: PackageSourceTypeDef,
    PackageDescription: str = None,
    CommitMessage: str = None
) -> UpdatePackageResponseTypeDef:
    pass
```

### upgrade_elasticsearch_domain

Type annotations for `boto3.client("es").upgrade_elasticsearch_domain` method.

[Client.upgrade_elasticsearch_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Client.upgrade_elasticsearch_domain)

```python
def upgrade_elasticsearch_domain(
    self,
    DomainName: str,
    TargetVersion: str,
    PerformCheckOnly: bool = None
) -> UpgradeElasticsearchDomainResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("es").get_paginator` method.

[Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReservedElasticsearchInstanceOfferingsPaginatorName
) -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("es").get_paginator` method.

[Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeReservedElasticsearchInstancesPaginatorName
) -> DescribeReservedElasticsearchInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("es").get_paginator` method.

[Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)

```python
@overload
def get_paginator(
    self,
    operation_name: GetUpgradeHistoryPaginatorName
) -> GetUpgradeHistoryPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("es").get_paginator` method.

[Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)

```python
@overload
def get_paginator(
    self,
    operation_name: ListElasticsearchInstanceTypesPaginatorName
) -> ListElasticsearchInstanceTypesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("es").get_paginator` method.

[Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)

```python
@overload
def get_paginator(
    self,
    operation_name: ListElasticsearchVersionsPaginatorName
) -> ListElasticsearchVersionsPaginator:
    pass
```