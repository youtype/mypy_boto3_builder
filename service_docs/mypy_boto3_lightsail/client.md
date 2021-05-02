# LightsailClient for boto3 Lightsail module

> [Index](../index.md) > [Lightsail](./index.md) > LightsailClient

Auto-generated documentation for [Lightsail](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail)
type annotations stubs module [mypy_boto3_lightsail](https://pypi.org/project/mypy-boto3-lightsail/).

- [LightsailClient for boto3 Lightsail module](#lightsailclient-for-boto3-lightsail-module)
  - [LightsailClient](#lightsailclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [allocate_static_ip](#allocate_static_ip)
    - [attach_certificate_to_distribution](#attach_certificate_to_distribution)
    - [attach_disk](#attach_disk)
    - [attach_instances_to_load_balancer](#attach_instances_to_load_balancer)
    - [attach_load_balancer_tls_certificate](#attach_load_balancer_tls_certificate)
    - [attach_static_ip](#attach_static_ip)
    - [can_paginate](#can_paginate)
    - [close_instance_public_ports](#close_instance_public_ports)
    - [copy_snapshot](#copy_snapshot)
    - [create_certificate](#create_certificate)
    - [create_cloud_formation_stack](#create_cloud_formation_stack)
    - [create_contact_method](#create_contact_method)
    - [create_container_service](#create_container_service)
    - [create_container_service_deployment](#create_container_service_deployment)
    - [create_container_service_registry_login](#create_container_service_registry_login)
    - [create_disk](#create_disk)
    - [create_disk_from_snapshot](#create_disk_from_snapshot)
    - [create_disk_snapshot](#create_disk_snapshot)
    - [create_distribution](#create_distribution)
    - [create_domain](#create_domain)
    - [create_domain_entry](#create_domain_entry)
    - [create_instance_snapshot](#create_instance_snapshot)
    - [create_instances](#create_instances)
    - [create_instances_from_snapshot](#create_instances_from_snapshot)
    - [create_key_pair](#create_key_pair)
    - [create_load_balancer](#create_load_balancer)
    - [create_load_balancer_tls_certificate](#create_load_balancer_tls_certificate)
    - [create_relational_database](#create_relational_database)
    - [create_relational_database_from_snapshot](#create_relational_database_from_snapshot)
    - [create_relational_database_snapshot](#create_relational_database_snapshot)
    - [delete_alarm](#delete_alarm)
    - [delete_auto_snapshot](#delete_auto_snapshot)
    - [delete_certificate](#delete_certificate)
    - [delete_contact_method](#delete_contact_method)
    - [delete_container_image](#delete_container_image)
    - [delete_container_service](#delete_container_service)
    - [delete_disk](#delete_disk)
    - [delete_disk_snapshot](#delete_disk_snapshot)
    - [delete_distribution](#delete_distribution)
    - [delete_domain](#delete_domain)
    - [delete_domain_entry](#delete_domain_entry)
    - [delete_instance](#delete_instance)
    - [delete_instance_snapshot](#delete_instance_snapshot)
    - [delete_key_pair](#delete_key_pair)
    - [delete_known_host_keys](#delete_known_host_keys)
    - [delete_load_balancer](#delete_load_balancer)
    - [delete_load_balancer_tls_certificate](#delete_load_balancer_tls_certificate)
    - [delete_relational_database](#delete_relational_database)
    - [delete_relational_database_snapshot](#delete_relational_database_snapshot)
    - [detach_certificate_from_distribution](#detach_certificate_from_distribution)
    - [detach_disk](#detach_disk)
    - [detach_instances_from_load_balancer](#detach_instances_from_load_balancer)
    - [detach_static_ip](#detach_static_ip)
    - [disable_add_on](#disable_add_on)
    - [download_default_key_pair](#download_default_key_pair)
    - [enable_add_on](#enable_add_on)
    - [export_snapshot](#export_snapshot)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_active_names](#get_active_names)
    - [get_alarms](#get_alarms)
    - [get_auto_snapshots](#get_auto_snapshots)
    - [get_blueprints](#get_blueprints)
    - [get_bundles](#get_bundles)
    - [get_certificates](#get_certificates)
    - [get_cloud_formation_stack_records](#get_cloud_formation_stack_records)
    - [get_contact_methods](#get_contact_methods)
    - [get_container_api_metadata](#get_container_api_metadata)
    - [get_container_images](#get_container_images)
    - [get_container_log](#get_container_log)
    - [get_container_service_deployments](#get_container_service_deployments)
    - [get_container_service_metric_data](#get_container_service_metric_data)
    - [get_container_service_powers](#get_container_service_powers)
    - [get_container_services](#get_container_services)
    - [get_disk](#get_disk)
    - [get_disk_snapshot](#get_disk_snapshot)
    - [get_disk_snapshots](#get_disk_snapshots)
    - [get_disks](#get_disks)
    - [get_distribution_bundles](#get_distribution_bundles)
    - [get_distribution_latest_cache_reset](#get_distribution_latest_cache_reset)
    - [get_distribution_metric_data](#get_distribution_metric_data)
    - [get_distributions](#get_distributions)
    - [get_domain](#get_domain)
    - [get_domains](#get_domains)
    - [get_export_snapshot_records](#get_export_snapshot_records)
    - [get_instance](#get_instance)
    - [get_instance_access_details](#get_instance_access_details)
    - [get_instance_metric_data](#get_instance_metric_data)
    - [get_instance_port_states](#get_instance_port_states)
    - [get_instance_snapshot](#get_instance_snapshot)
    - [get_instance_snapshots](#get_instance_snapshots)
    - [get_instance_state](#get_instance_state)
    - [get_instances](#get_instances)
    - [get_key_pair](#get_key_pair)
    - [get_key_pairs](#get_key_pairs)
    - [get_load_balancer](#get_load_balancer)
    - [get_load_balancer_metric_data](#get_load_balancer_metric_data)
    - [get_load_balancer_tls_certificates](#get_load_balancer_tls_certificates)
    - [get_load_balancers](#get_load_balancers)
    - [get_operation](#get_operation)
    - [get_operations](#get_operations)
    - [get_operations_for_resource](#get_operations_for_resource)
    - [get_regions](#get_regions)
    - [get_relational_database](#get_relational_database)
    - [get_relational_database_blueprints](#get_relational_database_blueprints)
    - [get_relational_database_bundles](#get_relational_database_bundles)
    - [get_relational_database_events](#get_relational_database_events)
    - [get_relational_database_log_events](#get_relational_database_log_events)
    - [get_relational_database_log_streams](#get_relational_database_log_streams)
    - [get_relational_database_master_user_password](#get_relational_database_master_user_password)
    - [get_relational_database_metric_data](#get_relational_database_metric_data)
    - [get_relational_database_parameters](#get_relational_database_parameters)
    - [get_relational_database_snapshot](#get_relational_database_snapshot)
    - [get_relational_database_snapshots](#get_relational_database_snapshots)
    - [get_relational_databases](#get_relational_databases)
    - [get_static_ip](#get_static_ip)
    - [get_static_ips](#get_static_ips)
    - [import_key_pair](#import_key_pair)
    - [is_vpc_peered](#is_vpc_peered)
    - [open_instance_public_ports](#open_instance_public_ports)
    - [peer_vpc](#peer_vpc)
    - [put_alarm](#put_alarm)
    - [put_instance_public_ports](#put_instance_public_ports)
    - [reboot_instance](#reboot_instance)
    - [reboot_relational_database](#reboot_relational_database)
    - [register_container_image](#register_container_image)
    - [release_static_ip](#release_static_ip)
    - [reset_distribution_cache](#reset_distribution_cache)
    - [send_contact_method_verification](#send_contact_method_verification)
    - [set_ip_address_type](#set_ip_address_type)
    - [start_instance](#start_instance)
    - [start_relational_database](#start_relational_database)
    - [stop_instance](#stop_instance)
    - [stop_relational_database](#stop_relational_database)
    - [tag_resource](#tag_resource)
    - [test_alarm](#test_alarm)
    - [unpeer_vpc](#unpeer_vpc)
    - [untag_resource](#untag_resource)
    - [update_container_service](#update_container_service)
    - [update_distribution](#update_distribution)
    - [update_distribution_bundle](#update_distribution_bundle)
    - [update_domain_entry](#update_domain_entry)
    - [update_load_balancer_attribute](#update_load_balancer_attribute)
    - [update_relational_database](#update_relational_database)
    - [update_relational_database_parameters](#update_relational_database_parameters)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_paginator](#get_paginator-5)
    - [get_paginator](#get_paginator-6)
    - [get_paginator](#get_paginator-7)
    - [get_paginator](#get_paginator-8)
    - [get_paginator](#get_paginator-9)
    - [get_paginator](#get_paginator-10)
    - [get_paginator](#get_paginator-11)
    - [get_paginator](#get_paginator-12)
    - [get_paginator](#get_paginator-13)
    - [get_paginator](#get_paginator-14)
    - [get_paginator](#get_paginator-15)
    - [get_paginator](#get_paginator-16)
    - [get_paginator](#get_paginator-17)
    - [get_paginator](#get_paginator-18)
    - [get_paginator](#get_paginator-19)

## LightsailClient

Type annotations for `boto3.client("lightsail")`

Can be used directly:

```python
from mypy_boto3_lightsail.client import LightsailClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lightsail.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.AccountSetupInProgressException`
- `Exceptions.ClientError`
- `Exceptions.InvalidInputException`
- `Exceptions.NotFoundException`
- `Exceptions.OperationFailureException`
- `Exceptions.ServiceException`
- `Exceptions.UnauthenticatedException`


## Methods


### allocate_static_ip

Type annotations for `boto3.client("lightsail").allocate_static_ip` method.

[Client.allocate_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.allocate_static_ip)

```python
def allocate_static_ip(
    self,
    staticIpName: str
) -> AllocateStaticIpResultTypeDef:
    pass
```

### attach_certificate_to_distribution

Type annotations for `boto3.client("lightsail").attach_certificate_to_distribution` method.

[Client.attach_certificate_to_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.attach_certificate_to_distribution)

```python
def attach_certificate_to_distribution(
    self,
    distributionName: str,
    certificateName: str
) -> AttachCertificateToDistributionResultTypeDef:
    pass
```

### attach_disk

Type annotations for `boto3.client("lightsail").attach_disk` method.

[Client.attach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.attach_disk)

```python
def attach_disk(
    self,
    diskName: str,
    instanceName: str,
    diskPath: str
) -> AttachDiskResultTypeDef:
    pass
```

### attach_instances_to_load_balancer

Type annotations for `boto3.client("lightsail").attach_instances_to_load_balancer` method.

[Client.attach_instances_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.attach_instances_to_load_balancer)

```python
def attach_instances_to_load_balancer(
    self,
    loadBalancerName: str,
    instanceNames: List[str]
) -> AttachInstancesToLoadBalancerResultTypeDef:
    pass
```

### attach_load_balancer_tls_certificate

Type annotations for `boto3.client("lightsail").attach_load_balancer_tls_certificate` method.

[Client.attach_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.attach_load_balancer_tls_certificate)

```python
def attach_load_balancer_tls_certificate(
    self,
    loadBalancerName: str,
    certificateName: str
) -> AttachLoadBalancerTlsCertificateResultTypeDef:
    pass
```

### attach_static_ip

Type annotations for `boto3.client("lightsail").attach_static_ip` method.

[Client.attach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.attach_static_ip)

```python
def attach_static_ip(
    self,
    staticIpName: str,
    instanceName: str
) -> AttachStaticIpResultTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("lightsail").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### close_instance_public_ports

Type annotations for `boto3.client("lightsail").close_instance_public_ports` method.

[Client.close_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.close_instance_public_ports)

```python
def close_instance_public_ports(
    self,
    portInfo: PortInfoTypeDef,
    instanceName: str
) -> CloseInstancePublicPortsResultTypeDef:
    pass
```

### copy_snapshot

Type annotations for `boto3.client("lightsail").copy_snapshot` method.

[Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.copy_snapshot)

```python
def copy_snapshot(
    self,
    targetSnapshotName: str,
    sourceRegion: RegionName,
    sourceSnapshotName: str = None,
    sourceResourceName: str = None,
    restoreDate: str = None,
    useLatestRestorableAutoSnapshot: bool = None
) -> CopySnapshotResultTypeDef:
    pass
```

### create_certificate

Type annotations for `boto3.client("lightsail").create_certificate` method.

[Client.create_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_certificate)

```python
def create_certificate(
    self,
    certificateName: str,
    domainName: str,
    subjectAlternativeNames: List[str] = None,
    tags: List["TagTypeDef"] = None
) -> CreateCertificateResultTypeDef:
    pass
```

### create_cloud_formation_stack

Type annotations for `boto3.client("lightsail").create_cloud_formation_stack` method.

[Client.create_cloud_formation_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_cloud_formation_stack)

```python
def create_cloud_formation_stack(
    self,
    instances: List[InstanceEntryTypeDef]
) -> CreateCloudFormationStackResultTypeDef:
    pass
```

### create_contact_method

Type annotations for `boto3.client("lightsail").create_contact_method` method.

[Client.create_contact_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_contact_method)

```python
def create_contact_method(
    self,
    protocol: ContactProtocol,
    contactEndpoint: str
) -> CreateContactMethodResultTypeDef:
    pass
```

### create_container_service

Type annotations for `boto3.client("lightsail").create_container_service` method.

[Client.create_container_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_container_service)

```python
def create_container_service(
    self,
    serviceName: str,
    power: ContainerServicePowerName,
    scale: int,
    tags: List["TagTypeDef"] = None,
    publicDomainNames: Dict[str, List[str]] = None,
    deployment: ContainerServiceDeploymentRequestTypeDef = None
) -> CreateContainerServiceResultTypeDef:
    pass
```

### create_container_service_deployment

Type annotations for `boto3.client("lightsail").create_container_service_deployment` method.

[Client.create_container_service_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_container_service_deployment)

```python
def create_container_service_deployment(
    self,
    serviceName: str,
    containers: Dict[str, "ContainerTypeDef"] = None,
    publicEndpoint: "EndpointRequestTypeDef" = None
) -> CreateContainerServiceDeploymentResultTypeDef:
    pass
```

### create_container_service_registry_login

Type annotations for `boto3.client("lightsail").create_container_service_registry_login` method.

[Client.create_container_service_registry_login documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_container_service_registry_login)

```python
def create_container_service_registry_login(
    self
) -> CreateContainerServiceRegistryLoginResultTypeDef:
    pass
```

### create_disk

Type annotations for `boto3.client("lightsail").create_disk` method.

[Client.create_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_disk)

```python
def create_disk(
    self,
    diskName: str,
    availabilityZone: str,
    sizeInGb: int,
    tags: List["TagTypeDef"] = None,
    addOns: List[AddOnRequestTypeDef] = None
) -> CreateDiskResultTypeDef:
    pass
```

### create_disk_from_snapshot

Type annotations for `boto3.client("lightsail").create_disk_from_snapshot` method.

[Client.create_disk_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_disk_from_snapshot)

```python
def create_disk_from_snapshot(
    self,
    diskName: str,
    availabilityZone: str,
    sizeInGb: int,
    diskSnapshotName: str = None,
    tags: List["TagTypeDef"] = None,
    addOns: List[AddOnRequestTypeDef] = None,
    sourceDiskName: str = None,
    restoreDate: str = None,
    useLatestRestorableAutoSnapshot: bool = None
) -> CreateDiskFromSnapshotResultTypeDef:
    pass
```

### create_disk_snapshot

Type annotations for `boto3.client("lightsail").create_disk_snapshot` method.

[Client.create_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_disk_snapshot)

```python
def create_disk_snapshot(
    self,
    diskSnapshotName: str,
    diskName: str = None,
    instanceName: str = None,
    tags: List["TagTypeDef"] = None
) -> CreateDiskSnapshotResultTypeDef:
    pass
```

### create_distribution

Type annotations for `boto3.client("lightsail").create_distribution` method.

[Client.create_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_distribution)

```python
def create_distribution(
    self,
    distributionName: str,
    origin: InputOriginTypeDef,
    defaultCacheBehavior: "CacheBehaviorTypeDef",
    bundleId: str,
    cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
    cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
    ipAddressType: IpAddressType = None,
    tags: List["TagTypeDef"] = None
) -> CreateDistributionResultTypeDef:
    pass
```

### create_domain

Type annotations for `boto3.client("lightsail").create_domain` method.

[Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_domain)

```python
def create_domain(
    self,
    domainName: str,
    tags: List["TagTypeDef"] = None
) -> CreateDomainResultTypeDef:
    pass
```

### create_domain_entry

Type annotations for `boto3.client("lightsail").create_domain_entry` method.

[Client.create_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_domain_entry)

```python
def create_domain_entry(
    self,
    domainName: str,
    domainEntry: "DomainEntryTypeDef"
) -> CreateDomainEntryResultTypeDef:
    pass
```

### create_instance_snapshot

Type annotations for `boto3.client("lightsail").create_instance_snapshot` method.

[Client.create_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_instance_snapshot)

```python
def create_instance_snapshot(
    self,
    instanceSnapshotName: str,
    instanceName: str,
    tags: List["TagTypeDef"] = None
) -> CreateInstanceSnapshotResultTypeDef:
    pass
```

### create_instances

Type annotations for `boto3.client("lightsail").create_instances` method.

[Client.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_instances)

```python
def create_instances(
    self,
    instanceNames: List[str],
    availabilityZone: str,
    blueprintId: str,
    bundleId: str,
    customImageName: str = None,
    userData: str = None,
    keyPairName: str = None,
    tags: List["TagTypeDef"] = None,
    addOns: List[AddOnRequestTypeDef] = None,
    ipAddressType: IpAddressType = None
) -> CreateInstancesResultTypeDef:
    pass
```

### create_instances_from_snapshot

Type annotations for `boto3.client("lightsail").create_instances_from_snapshot` method.

[Client.create_instances_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_instances_from_snapshot)

```python
def create_instances_from_snapshot(
    self,
    instanceNames: List[str],
    availabilityZone: str,
    bundleId: str,
    attachedDiskMapping: Dict[str, List[DiskMapTypeDef]] = None,
    instanceSnapshotName: str = None,
    userData: str = None,
    keyPairName: str = None,
    tags: List["TagTypeDef"] = None,
    addOns: List[AddOnRequestTypeDef] = None,
    ipAddressType: IpAddressType = None,
    sourceInstanceName: str = None,
    restoreDate: str = None,
    useLatestRestorableAutoSnapshot: bool = None
) -> CreateInstancesFromSnapshotResultTypeDef:
    pass
```

### create_key_pair

Type annotations for `boto3.client("lightsail").create_key_pair` method.

[Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_key_pair)

```python
def create_key_pair(
    self,
    keyPairName: str,
    tags: List["TagTypeDef"] = None
) -> CreateKeyPairResultTypeDef:
    pass
```

### create_load_balancer

Type annotations for `boto3.client("lightsail").create_load_balancer` method.

[Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_load_balancer)

```python
def create_load_balancer(
    self,
    loadBalancerName: str,
    instancePort: int,
    healthCheckPath: str = None,
    certificateName: str = None,
    certificateDomainName: str = None,
    certificateAlternativeNames: List[str] = None,
    tags: List["TagTypeDef"] = None,
    ipAddressType: IpAddressType = None
) -> CreateLoadBalancerResultTypeDef:
    pass
```

### create_load_balancer_tls_certificate

Type annotations for `boto3.client("lightsail").create_load_balancer_tls_certificate` method.

[Client.create_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_load_balancer_tls_certificate)

```python
def create_load_balancer_tls_certificate(
    self,
    loadBalancerName: str,
    certificateName: str,
    certificateDomainName: str,
    certificateAlternativeNames: List[str] = None,
    tags: List["TagTypeDef"] = None
) -> CreateLoadBalancerTlsCertificateResultTypeDef:
    pass
```

### create_relational_database

Type annotations for `boto3.client("lightsail").create_relational_database` method.

[Client.create_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_relational_database)

```python
def create_relational_database(
    self,
    relationalDatabaseName: str,
    relationalDatabaseBlueprintId: str,
    relationalDatabaseBundleId: str,
    masterDatabaseName: str,
    masterUsername: str,
    availabilityZone: str = None,
    masterUserPassword: str = None,
    preferredBackupWindow: str = None,
    preferredMaintenanceWindow: str = None,
    publiclyAccessible: bool = None,
    tags: List["TagTypeDef"] = None
) -> CreateRelationalDatabaseResultTypeDef:
    pass
```

### create_relational_database_from_snapshot

Type annotations for `boto3.client("lightsail").create_relational_database_from_snapshot` method.

[Client.create_relational_database_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_relational_database_from_snapshot)

```python
def create_relational_database_from_snapshot(
    self,
    relationalDatabaseName: str,
    availabilityZone: str = None,
    publiclyAccessible: bool = None,
    relationalDatabaseSnapshotName: str = None,
    relationalDatabaseBundleId: str = None,
    sourceRelationalDatabaseName: str = None,
    restoreTime: datetime = None,
    useLatestRestorableTime: bool = None,
    tags: List["TagTypeDef"] = None
) -> CreateRelationalDatabaseFromSnapshotResultTypeDef:
    pass
```

### create_relational_database_snapshot

Type annotations for `boto3.client("lightsail").create_relational_database_snapshot` method.

[Client.create_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.create_relational_database_snapshot)

```python
def create_relational_database_snapshot(
    self,
    relationalDatabaseName: str,
    relationalDatabaseSnapshotName: str,
    tags: List["TagTypeDef"] = None
) -> CreateRelationalDatabaseSnapshotResultTypeDef:
    pass
```

### delete_alarm

Type annotations for `boto3.client("lightsail").delete_alarm` method.

[Client.delete_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_alarm)

```python
def delete_alarm(
    self,
    alarmName: str
) -> DeleteAlarmResultTypeDef:
    pass
```

### delete_auto_snapshot

Type annotations for `boto3.client("lightsail").delete_auto_snapshot` method.

[Client.delete_auto_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_auto_snapshot)

```python
def delete_auto_snapshot(
    self,
    resourceName: str,
    date: str
) -> DeleteAutoSnapshotResultTypeDef:
    pass
```

### delete_certificate

Type annotations for `boto3.client("lightsail").delete_certificate` method.

[Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_certificate)

```python
def delete_certificate(
    self,
    certificateName: str
) -> DeleteCertificateResultTypeDef:
    pass
```

### delete_contact_method

Type annotations for `boto3.client("lightsail").delete_contact_method` method.

[Client.delete_contact_method documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_contact_method)

```python
def delete_contact_method(
    self,
    protocol: ContactProtocol
) -> DeleteContactMethodResultTypeDef:
    pass
```

### delete_container_image

Type annotations for `boto3.client("lightsail").delete_container_image` method.

[Client.delete_container_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_container_image)

```python
def delete_container_image(
    self,
    serviceName: str,
    image: str
) -> Dict[str, Any]:
    pass
```

### delete_container_service

Type annotations for `boto3.client("lightsail").delete_container_service` method.

[Client.delete_container_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_container_service)

```python
def delete_container_service(
    self,
    serviceName: str
) -> Dict[str, Any]:
    pass
```

### delete_disk

Type annotations for `boto3.client("lightsail").delete_disk` method.

[Client.delete_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_disk)

```python
def delete_disk(
    self,
    diskName: str,
    forceDeleteAddOns: bool = None
) -> DeleteDiskResultTypeDef:
    pass
```

### delete_disk_snapshot

Type annotations for `boto3.client("lightsail").delete_disk_snapshot` method.

[Client.delete_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_disk_snapshot)

```python
def delete_disk_snapshot(
    self,
    diskSnapshotName: str
) -> DeleteDiskSnapshotResultTypeDef:
    pass
```

### delete_distribution

Type annotations for `boto3.client("lightsail").delete_distribution` method.

[Client.delete_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_distribution)

```python
def delete_distribution(
    self,
    distributionName: str = None
) -> DeleteDistributionResultTypeDef:
    pass
```

### delete_domain

Type annotations for `boto3.client("lightsail").delete_domain` method.

[Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_domain)

```python
def delete_domain(
    self,
    domainName: str
) -> DeleteDomainResultTypeDef:
    pass
```

### delete_domain_entry

Type annotations for `boto3.client("lightsail").delete_domain_entry` method.

[Client.delete_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_domain_entry)

```python
def delete_domain_entry(
    self,
    domainName: str,
    domainEntry: "DomainEntryTypeDef"
) -> DeleteDomainEntryResultTypeDef:
    pass
```

### delete_instance

Type annotations for `boto3.client("lightsail").delete_instance` method.

[Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_instance)

```python
def delete_instance(
    self,
    instanceName: str,
    forceDeleteAddOns: bool = None
) -> DeleteInstanceResultTypeDef:
    pass
```

### delete_instance_snapshot

Type annotations for `boto3.client("lightsail").delete_instance_snapshot` method.

[Client.delete_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_instance_snapshot)

```python
def delete_instance_snapshot(
    self,
    instanceSnapshotName: str
) -> DeleteInstanceSnapshotResultTypeDef:
    pass
```

### delete_key_pair

Type annotations for `boto3.client("lightsail").delete_key_pair` method.

[Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_key_pair)

```python
def delete_key_pair(
    self,
    keyPairName: str
) -> DeleteKeyPairResultTypeDef:
    pass
```

### delete_known_host_keys

Type annotations for `boto3.client("lightsail").delete_known_host_keys` method.

[Client.delete_known_host_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_known_host_keys)

```python
def delete_known_host_keys(
    self,
    instanceName: str
) -> DeleteKnownHostKeysResultTypeDef:
    pass
```

### delete_load_balancer

Type annotations for `boto3.client("lightsail").delete_load_balancer` method.

[Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer)

```python
def delete_load_balancer(
    self,
    loadBalancerName: str
) -> DeleteLoadBalancerResultTypeDef:
    pass
```

### delete_load_balancer_tls_certificate

Type annotations for `boto3.client("lightsail").delete_load_balancer_tls_certificate` method.

[Client.delete_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer_tls_certificate)

```python
def delete_load_balancer_tls_certificate(
    self,
    loadBalancerName: str,
    certificateName: str,
    force: bool = None
) -> DeleteLoadBalancerTlsCertificateResultTypeDef:
    pass
```

### delete_relational_database

Type annotations for `boto3.client("lightsail").delete_relational_database` method.

[Client.delete_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_relational_database)

```python
def delete_relational_database(
    self,
    relationalDatabaseName: str,
    skipFinalSnapshot: bool = None,
    finalRelationalDatabaseSnapshotName: str = None
) -> DeleteRelationalDatabaseResultTypeDef:
    pass
```

### delete_relational_database_snapshot

Type annotations for `boto3.client("lightsail").delete_relational_database_snapshot` method.

[Client.delete_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.delete_relational_database_snapshot)

```python
def delete_relational_database_snapshot(
    self,
    relationalDatabaseSnapshotName: str
) -> DeleteRelationalDatabaseSnapshotResultTypeDef:
    pass
```

### detach_certificate_from_distribution

Type annotations for `boto3.client("lightsail").detach_certificate_from_distribution` method.

[Client.detach_certificate_from_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.detach_certificate_from_distribution)

```python
def detach_certificate_from_distribution(
    self,
    distributionName: str
) -> DetachCertificateFromDistributionResultTypeDef:
    pass
```

### detach_disk

Type annotations for `boto3.client("lightsail").detach_disk` method.

[Client.detach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.detach_disk)

```python
def detach_disk(
    self,
    diskName: str
) -> DetachDiskResultTypeDef:
    pass
```

### detach_instances_from_load_balancer

Type annotations for `boto3.client("lightsail").detach_instances_from_load_balancer` method.

[Client.detach_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.detach_instances_from_load_balancer)

```python
def detach_instances_from_load_balancer(
    self,
    loadBalancerName: str,
    instanceNames: List[str]
) -> DetachInstancesFromLoadBalancerResultTypeDef:
    pass
```

### detach_static_ip

Type annotations for `boto3.client("lightsail").detach_static_ip` method.

[Client.detach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.detach_static_ip)

```python
def detach_static_ip(
    self,
    staticIpName: str
) -> DetachStaticIpResultTypeDef:
    pass
```

### disable_add_on

Type annotations for `boto3.client("lightsail").disable_add_on` method.

[Client.disable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.disable_add_on)

```python
def disable_add_on(
    self,
    addOnType: AddOnType,
    resourceName: str
) -> DisableAddOnResultTypeDef:
    pass
```

### download_default_key_pair

Type annotations for `boto3.client("lightsail").download_default_key_pair` method.

[Client.download_default_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.download_default_key_pair)

```python
def download_default_key_pair(
    self
) -> DownloadDefaultKeyPairResultTypeDef:
    pass
```

### enable_add_on

Type annotations for `boto3.client("lightsail").enable_add_on` method.

[Client.enable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.enable_add_on)

```python
def enable_add_on(
    self,
    resourceName: str,
    addOnRequest: AddOnRequestTypeDef
) -> EnableAddOnResultTypeDef:
    pass
```

### export_snapshot

Type annotations for `boto3.client("lightsail").export_snapshot` method.

[Client.export_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.export_snapshot)

```python
def export_snapshot(
    self,
    sourceSnapshotName: str
) -> ExportSnapshotResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lightsail").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.generate_presigned_url)

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

### get_active_names

Type annotations for `boto3.client("lightsail").get_active_names` method.

[Client.get_active_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_active_names)

```python
def get_active_names(
    self,
    pageToken: str = None
) -> GetActiveNamesResultTypeDef:
    pass
```

### get_alarms

Type annotations for `boto3.client("lightsail").get_alarms` method.

[Client.get_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_alarms)

```python
def get_alarms(
    self,
    alarmName: str = None,
    pageToken: str = None,
    monitoredResourceName: str = None
) -> GetAlarmsResultTypeDef:
    pass
```

### get_auto_snapshots

Type annotations for `boto3.client("lightsail").get_auto_snapshots` method.

[Client.get_auto_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_auto_snapshots)

```python
def get_auto_snapshots(
    self,
    resourceName: str
) -> GetAutoSnapshotsResultTypeDef:
    pass
```

### get_blueprints

Type annotations for `boto3.client("lightsail").get_blueprints` method.

[Client.get_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_blueprints)

```python
def get_blueprints(
    self,
    includeInactive: bool = None,
    pageToken: str = None
) -> GetBlueprintsResultTypeDef:
    pass
```

### get_bundles

Type annotations for `boto3.client("lightsail").get_bundles` method.

[Client.get_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_bundles)

```python
def get_bundles(
    self,
    includeInactive: bool = None,
    pageToken: str = None
) -> GetBundlesResultTypeDef:
    pass
```

### get_certificates

Type annotations for `boto3.client("lightsail").get_certificates` method.

[Client.get_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_certificates)

```python
def get_certificates(
    self,
    certificateStatuses: List[CertificateStatus] = None,
    includeCertificateDetails: bool = None,
    certificateName: str = None
) -> GetCertificatesResultTypeDef:
    pass
```

### get_cloud_formation_stack_records

Type annotations for `boto3.client("lightsail").get_cloud_formation_stack_records` method.

[Client.get_cloud_formation_stack_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_cloud_formation_stack_records)

```python
def get_cloud_formation_stack_records(
    self,
    pageToken: str = None
) -> GetCloudFormationStackRecordsResultTypeDef:
    pass
```

### get_contact_methods

Type annotations for `boto3.client("lightsail").get_contact_methods` method.

[Client.get_contact_methods documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_contact_methods)

```python
def get_contact_methods(
    self,
    protocols: List[ContactProtocol] = None
) -> GetContactMethodsResultTypeDef:
    pass
```

### get_container_api_metadata

Type annotations for `boto3.client("lightsail").get_container_api_metadata` method.

[Client.get_container_api_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_api_metadata)

```python
def get_container_api_metadata(
    self
) -> GetContainerAPIMetadataResultTypeDef:
    pass
```

### get_container_images

Type annotations for `boto3.client("lightsail").get_container_images` method.

[Client.get_container_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_images)

```python
def get_container_images(
    self,
    serviceName: str
) -> GetContainerImagesResultTypeDef:
    pass
```

### get_container_log

Type annotations for `boto3.client("lightsail").get_container_log` method.

[Client.get_container_log documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_log)

```python
def get_container_log(
    self,
    serviceName: str,
    containerName: str,
    startTime: datetime = None,
    endTime: datetime = None,
    filterPattern: str = None,
    pageToken: str = None
) -> GetContainerLogResultTypeDef:
    pass
```

### get_container_service_deployments

Type annotations for `boto3.client("lightsail").get_container_service_deployments` method.

[Client.get_container_service_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_service_deployments)

```python
def get_container_service_deployments(
    self,
    serviceName: str
) -> GetContainerServiceDeploymentsResultTypeDef:
    pass
```

### get_container_service_metric_data

Type annotations for `boto3.client("lightsail").get_container_service_metric_data` method.

[Client.get_container_service_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_service_metric_data)

```python
def get_container_service_metric_data(
    self,
    serviceName: str,
    metricName: ContainerServiceMetricName,
    startTime: datetime,
    endTime: datetime,
    period: int,
    statistics: List[MetricStatistic]
) -> GetContainerServiceMetricDataResultTypeDef:
    pass
```

### get_container_service_powers

Type annotations for `boto3.client("lightsail").get_container_service_powers` method.

[Client.get_container_service_powers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_service_powers)

```python
def get_container_service_powers(
    self
) -> GetContainerServicePowersResultTypeDef:
    pass
```

### get_container_services

Type annotations for `boto3.client("lightsail").get_container_services` method.

[Client.get_container_services documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_container_services)

```python
def get_container_services(
    self,
    serviceName: str = None
) -> ContainerServicesListResultTypeDef:
    pass
```

### get_disk

Type annotations for `boto3.client("lightsail").get_disk` method.

[Client.get_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_disk)

```python
def get_disk(
    self,
    diskName: str
) -> GetDiskResultTypeDef:
    pass
```

### get_disk_snapshot

Type annotations for `boto3.client("lightsail").get_disk_snapshot` method.

[Client.get_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshot)

```python
def get_disk_snapshot(
    self,
    diskSnapshotName: str
) -> GetDiskSnapshotResultTypeDef:
    pass
```

### get_disk_snapshots

Type annotations for `boto3.client("lightsail").get_disk_snapshots` method.

[Client.get_disk_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshots)

```python
def get_disk_snapshots(
    self,
    pageToken: str = None
) -> GetDiskSnapshotsResultTypeDef:
    pass
```

### get_disks

Type annotations for `boto3.client("lightsail").get_disks` method.

[Client.get_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_disks)

```python
def get_disks(
    self,
    pageToken: str = None
) -> GetDisksResultTypeDef:
    pass
```

### get_distribution_bundles

Type annotations for `boto3.client("lightsail").get_distribution_bundles` method.

[Client.get_distribution_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_distribution_bundles)

```python
def get_distribution_bundles(
    self
) -> GetDistributionBundlesResultTypeDef:
    pass
```

### get_distribution_latest_cache_reset

Type annotations for `boto3.client("lightsail").get_distribution_latest_cache_reset` method.

[Client.get_distribution_latest_cache_reset documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_distribution_latest_cache_reset)

```python
def get_distribution_latest_cache_reset(
    self,
    distributionName: str = None
) -> GetDistributionLatestCacheResetResultTypeDef:
    pass
```

### get_distribution_metric_data

Type annotations for `boto3.client("lightsail").get_distribution_metric_data` method.

[Client.get_distribution_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_distribution_metric_data)

```python
def get_distribution_metric_data(
    self,
    distributionName: str,
    metricName: DistributionMetricName,
    startTime: datetime,
    endTime: datetime,
    period: int,
    unit: MetricUnit,
    statistics: List[MetricStatistic]
) -> GetDistributionMetricDataResultTypeDef:
    pass
```

### get_distributions

Type annotations for `boto3.client("lightsail").get_distributions` method.

[Client.get_distributions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_distributions)

```python
def get_distributions(
    self,
    distributionName: str = None,
    pageToken: str = None
) -> GetDistributionsResultTypeDef:
    pass
```

### get_domain

Type annotations for `boto3.client("lightsail").get_domain` method.

[Client.get_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_domain)

```python
def get_domain(
    self,
    domainName: str
) -> GetDomainResultTypeDef:
    pass
```

### get_domains

Type annotations for `boto3.client("lightsail").get_domains` method.

[Client.get_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_domains)

```python
def get_domains(
    self,
    pageToken: str = None
) -> GetDomainsResultTypeDef:
    pass
```

### get_export_snapshot_records

Type annotations for `boto3.client("lightsail").get_export_snapshot_records` method.

[Client.get_export_snapshot_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_export_snapshot_records)

```python
def get_export_snapshot_records(
    self,
    pageToken: str = None
) -> GetExportSnapshotRecordsResultTypeDef:
    pass
```

### get_instance

Type annotations for `boto3.client("lightsail").get_instance` method.

[Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance)

```python
def get_instance(
    self,
    instanceName: str
) -> GetInstanceResultTypeDef:
    pass
```

### get_instance_access_details

Type annotations for `boto3.client("lightsail").get_instance_access_details` method.

[Client.get_instance_access_details documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance_access_details)

```python
def get_instance_access_details(
    self,
    instanceName: str,
    protocol: InstanceAccessProtocol = None
) -> GetInstanceAccessDetailsResultTypeDef:
    pass
```

### get_instance_metric_data

Type annotations for `boto3.client("lightsail").get_instance_metric_data` method.

[Client.get_instance_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance_metric_data)

```python
def get_instance_metric_data(
    self,
    instanceName: str,
    metricName: InstanceMetricName,
    period: int,
    startTime: datetime,
    endTime: datetime,
    unit: MetricUnit,
    statistics: List[MetricStatistic]
) -> GetInstanceMetricDataResultTypeDef:
    pass
```

### get_instance_port_states

Type annotations for `boto3.client("lightsail").get_instance_port_states` method.

[Client.get_instance_port_states documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance_port_states)

```python
def get_instance_port_states(
    self,
    instanceName: str
) -> GetInstancePortStatesResultTypeDef:
    pass
```

### get_instance_snapshot

Type annotations for `boto3.client("lightsail").get_instance_snapshot` method.

[Client.get_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshot)

```python
def get_instance_snapshot(
    self,
    instanceSnapshotName: str
) -> GetInstanceSnapshotResultTypeDef:
    pass
```

### get_instance_snapshots

Type annotations for `boto3.client("lightsail").get_instance_snapshots` method.

[Client.get_instance_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshots)

```python
def get_instance_snapshots(
    self,
    pageToken: str = None
) -> GetInstanceSnapshotsResultTypeDef:
    pass
```

### get_instance_state

Type annotations for `boto3.client("lightsail").get_instance_state` method.

[Client.get_instance_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instance_state)

```python
def get_instance_state(
    self,
    instanceName: str
) -> GetInstanceStateResultTypeDef:
    pass
```

### get_instances

Type annotations for `boto3.client("lightsail").get_instances` method.

[Client.get_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_instances)

```python
def get_instances(
    self,
    pageToken: str = None
) -> GetInstancesResultTypeDef:
    pass
```

### get_key_pair

Type annotations for `boto3.client("lightsail").get_key_pair` method.

[Client.get_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_key_pair)

```python
def get_key_pair(
    self,
    keyPairName: str
) -> GetKeyPairResultTypeDef:
    pass
```

### get_key_pairs

Type annotations for `boto3.client("lightsail").get_key_pairs` method.

[Client.get_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_key_pairs)

```python
def get_key_pairs(
    self,
    pageToken: str = None
) -> GetKeyPairsResultTypeDef:
    pass
```

### get_load_balancer

Type annotations for `boto3.client("lightsail").get_load_balancer` method.

[Client.get_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_load_balancer)

```python
def get_load_balancer(
    self,
    loadBalancerName: str
) -> GetLoadBalancerResultTypeDef:
    pass
```

### get_load_balancer_metric_data

Type annotations for `boto3.client("lightsail").get_load_balancer_metric_data` method.

[Client.get_load_balancer_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_metric_data)

```python
def get_load_balancer_metric_data(
    self,
    loadBalancerName: str,
    metricName: LoadBalancerMetricName,
    period: int,
    startTime: datetime,
    endTime: datetime,
    unit: MetricUnit,
    statistics: List[MetricStatistic]
) -> GetLoadBalancerMetricDataResultTypeDef:
    pass
```

### get_load_balancer_tls_certificates

Type annotations for `boto3.client("lightsail").get_load_balancer_tls_certificates` method.

[Client.get_load_balancer_tls_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_certificates)

```python
def get_load_balancer_tls_certificates(
    self,
    loadBalancerName: str
) -> GetLoadBalancerTlsCertificatesResultTypeDef:
    pass
```

### get_load_balancers

Type annotations for `boto3.client("lightsail").get_load_balancers` method.

[Client.get_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_load_balancers)

```python
def get_load_balancers(
    self,
    pageToken: str = None
) -> GetLoadBalancersResultTypeDef:
    pass
```

### get_operation

Type annotations for `boto3.client("lightsail").get_operation` method.

[Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_operation)

```python
def get_operation(
    self,
    operationId: str
) -> GetOperationResultTypeDef:
    pass
```

### get_operations

Type annotations for `boto3.client("lightsail").get_operations` method.

[Client.get_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_operations)

```python
def get_operations(
    self,
    pageToken: str = None
) -> GetOperationsResultTypeDef:
    pass
```

### get_operations_for_resource

Type annotations for `boto3.client("lightsail").get_operations_for_resource` method.

[Client.get_operations_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_operations_for_resource)

```python
def get_operations_for_resource(
    self,
    resourceName: str,
    pageToken: str = None
) -> GetOperationsForResourceResultTypeDef:
    pass
```

### get_regions

Type annotations for `boto3.client("lightsail").get_regions` method.

[Client.get_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_regions)

```python
def get_regions(
    self,
    includeAvailabilityZones: bool = None,
    includeRelationalDatabaseAvailabilityZones: bool = None
) -> GetRegionsResultTypeDef:
    pass
```

### get_relational_database

Type annotations for `boto3.client("lightsail").get_relational_database` method.

[Client.get_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database)

```python
def get_relational_database(
    self,
    relationalDatabaseName: str
) -> GetRelationalDatabaseResultTypeDef:
    pass
```

### get_relational_database_blueprints

Type annotations for `boto3.client("lightsail").get_relational_database_blueprints` method.

[Client.get_relational_database_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_blueprints)

```python
def get_relational_database_blueprints(
    self,
    pageToken: str = None
) -> GetRelationalDatabaseBlueprintsResultTypeDef:
    pass
```

### get_relational_database_bundles

Type annotations for `boto3.client("lightsail").get_relational_database_bundles` method.

[Client.get_relational_database_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_bundles)

```python
def get_relational_database_bundles(
    self,
    pageToken: str = None
) -> GetRelationalDatabaseBundlesResultTypeDef:
    pass
```

### get_relational_database_events

Type annotations for `boto3.client("lightsail").get_relational_database_events` method.

[Client.get_relational_database_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_events)

```python
def get_relational_database_events(
    self,
    relationalDatabaseName: str,
    durationInMinutes: int = None,
    pageToken: str = None
) -> GetRelationalDatabaseEventsResultTypeDef:
    pass
```

### get_relational_database_log_events

Type annotations for `boto3.client("lightsail").get_relational_database_log_events` method.

[Client.get_relational_database_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_events)

```python
def get_relational_database_log_events(
    self,
    relationalDatabaseName: str,
    logStreamName: str,
    startTime: datetime = None,
    endTime: datetime = None,
    startFromHead: bool = None,
    pageToken: str = None
) -> GetRelationalDatabaseLogEventsResultTypeDef:
    pass
```

### get_relational_database_log_streams

Type annotations for `boto3.client("lightsail").get_relational_database_log_streams` method.

[Client.get_relational_database_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_streams)

```python
def get_relational_database_log_streams(
    self,
    relationalDatabaseName: str
) -> GetRelationalDatabaseLogStreamsResultTypeDef:
    pass
```

### get_relational_database_master_user_password

Type annotations for `boto3.client("lightsail").get_relational_database_master_user_password` method.

[Client.get_relational_database_master_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_master_user_password)

```python
def get_relational_database_master_user_password(
    self,
    relationalDatabaseName: str,
    passwordVersion: RelationalDatabasePasswordVersion = None
) -> GetRelationalDatabaseMasterUserPasswordResultTypeDef:
    pass
```

### get_relational_database_metric_data

Type annotations for `boto3.client("lightsail").get_relational_database_metric_data` method.

[Client.get_relational_database_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_metric_data)

```python
def get_relational_database_metric_data(
    self,
    relationalDatabaseName: str,
    metricName: RelationalDatabaseMetricName,
    period: int,
    startTime: datetime,
    endTime: datetime,
    unit: MetricUnit,
    statistics: List[MetricStatistic]
) -> GetRelationalDatabaseMetricDataResultTypeDef:
    pass
```

### get_relational_database_parameters

Type annotations for `boto3.client("lightsail").get_relational_database_parameters` method.

[Client.get_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_parameters)

```python
def get_relational_database_parameters(
    self,
    relationalDatabaseName: str,
    pageToken: str = None
) -> GetRelationalDatabaseParametersResultTypeDef:
    pass
```

### get_relational_database_snapshot

Type annotations for `boto3.client("lightsail").get_relational_database_snapshot` method.

[Client.get_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshot)

```python
def get_relational_database_snapshot(
    self,
    relationalDatabaseSnapshotName: str
) -> GetRelationalDatabaseSnapshotResultTypeDef:
    pass
```

### get_relational_database_snapshots

Type annotations for `boto3.client("lightsail").get_relational_database_snapshots` method.

[Client.get_relational_database_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshots)

```python
def get_relational_database_snapshots(
    self,
    pageToken: str = None
) -> GetRelationalDatabaseSnapshotsResultTypeDef:
    pass
```

### get_relational_databases

Type annotations for `boto3.client("lightsail").get_relational_databases` method.

[Client.get_relational_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_relational_databases)

```python
def get_relational_databases(
    self,
    pageToken: str = None
) -> GetRelationalDatabasesResultTypeDef:
    pass
```

### get_static_ip

Type annotations for `boto3.client("lightsail").get_static_ip` method.

[Client.get_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_static_ip)

```python
def get_static_ip(
    self,
    staticIpName: str
) -> GetStaticIpResultTypeDef:
    pass
```

### get_static_ips

Type annotations for `boto3.client("lightsail").get_static_ips` method.

[Client.get_static_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.get_static_ips)

```python
def get_static_ips(
    self,
    pageToken: str = None
) -> GetStaticIpsResultTypeDef:
    pass
```

### import_key_pair

Type annotations for `boto3.client("lightsail").import_key_pair` method.

[Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.import_key_pair)

```python
def import_key_pair(
    self,
    keyPairName: str,
    publicKeyBase64: str
) -> ImportKeyPairResultTypeDef:
    pass
```

### is_vpc_peered

Type annotations for `boto3.client("lightsail").is_vpc_peered` method.

[Client.is_vpc_peered documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.is_vpc_peered)

```python
def is_vpc_peered(
    self
) -> IsVpcPeeredResultTypeDef:
    pass
```

### open_instance_public_ports

Type annotations for `boto3.client("lightsail").open_instance_public_ports` method.

[Client.open_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.open_instance_public_ports)

```python
def open_instance_public_ports(
    self,
    portInfo: PortInfoTypeDef,
    instanceName: str
) -> OpenInstancePublicPortsResultTypeDef:
    pass
```

### peer_vpc

Type annotations for `boto3.client("lightsail").peer_vpc` method.

[Client.peer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.peer_vpc)

```python
def peer_vpc(
    self
) -> PeerVpcResultTypeDef:
    pass
```

### put_alarm

Type annotations for `boto3.client("lightsail").put_alarm` method.

[Client.put_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.put_alarm)

```python
def put_alarm(
    self,
    alarmName: str,
    metricName: MetricName,
    monitoredResourceName: str,
    comparisonOperator: ComparisonOperator,
    threshold: float,
    evaluationPeriods: int,
    datapointsToAlarm: int = None,
    treatMissingData: TreatMissingData = None,
    contactProtocols: List[ContactProtocol] = None,
    notificationTriggers: List[AlarmState] = None,
    notificationEnabled: bool = None
) -> PutAlarmResultTypeDef:
    pass
```

### put_instance_public_ports

Type annotations for `boto3.client("lightsail").put_instance_public_ports` method.

[Client.put_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.put_instance_public_ports)

```python
def put_instance_public_ports(
    self,
    portInfos: List[PortInfoTypeDef],
    instanceName: str
) -> PutInstancePublicPortsResultTypeDef:
    pass
```

### reboot_instance

Type annotations for `boto3.client("lightsail").reboot_instance` method.

[Client.reboot_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.reboot_instance)

```python
def reboot_instance(
    self,
    instanceName: str
) -> RebootInstanceResultTypeDef:
    pass
```

### reboot_relational_database

Type annotations for `boto3.client("lightsail").reboot_relational_database` method.

[Client.reboot_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.reboot_relational_database)

```python
def reboot_relational_database(
    self,
    relationalDatabaseName: str
) -> RebootRelationalDatabaseResultTypeDef:
    pass
```

### register_container_image

Type annotations for `boto3.client("lightsail").register_container_image` method.

[Client.register_container_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.register_container_image)

```python
def register_container_image(
    self,
    serviceName: str,
    label: str,
    digest: str
) -> RegisterContainerImageResultTypeDef:
    pass
```

### release_static_ip

Type annotations for `boto3.client("lightsail").release_static_ip` method.

[Client.release_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.release_static_ip)

```python
def release_static_ip(
    self,
    staticIpName: str
) -> ReleaseStaticIpResultTypeDef:
    pass
```

### reset_distribution_cache

Type annotations for `boto3.client("lightsail").reset_distribution_cache` method.

[Client.reset_distribution_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.reset_distribution_cache)

```python
def reset_distribution_cache(
    self,
    distributionName: str = None
) -> ResetDistributionCacheResultTypeDef:
    pass
```

### send_contact_method_verification

Type annotations for `boto3.client("lightsail").send_contact_method_verification` method.

[Client.send_contact_method_verification documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.send_contact_method_verification)

```python
def send_contact_method_verification(
    self,
    protocol: ContactMethodVerificationProtocol
) -> SendContactMethodVerificationResultTypeDef:
    pass
```

### set_ip_address_type

Type annotations for `boto3.client("lightsail").set_ip_address_type` method.

[Client.set_ip_address_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.set_ip_address_type)

```python
def set_ip_address_type(
    self,
    resourceType: ResourceType,
    resourceName: str,
    ipAddressType: IpAddressType
) -> SetIpAddressTypeResultTypeDef:
    pass
```

### start_instance

Type annotations for `boto3.client("lightsail").start_instance` method.

[Client.start_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.start_instance)

```python
def start_instance(
    self,
    instanceName: str
) -> StartInstanceResultTypeDef:
    pass
```

### start_relational_database

Type annotations for `boto3.client("lightsail").start_relational_database` method.

[Client.start_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.start_relational_database)

```python
def start_relational_database(
    self,
    relationalDatabaseName: str
) -> StartRelationalDatabaseResultTypeDef:
    pass
```

### stop_instance

Type annotations for `boto3.client("lightsail").stop_instance` method.

[Client.stop_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.stop_instance)

```python
def stop_instance(
    self,
    instanceName: str,
    force: bool = None
) -> StopInstanceResultTypeDef:
    pass
```

### stop_relational_database

Type annotations for `boto3.client("lightsail").stop_relational_database` method.

[Client.stop_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.stop_relational_database)

```python
def stop_relational_database(
    self,
    relationalDatabaseName: str,
    relationalDatabaseSnapshotName: str = None
) -> StopRelationalDatabaseResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("lightsail").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceName: str,
    tags: List["TagTypeDef"],
    resourceArn: str = None
) -> TagResourceResultTypeDef:
    pass
```

### test_alarm

Type annotations for `boto3.client("lightsail").test_alarm` method.

[Client.test_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.test_alarm)

```python
def test_alarm(
    self,
    alarmName: str,
    state: AlarmState
) -> TestAlarmResultTypeDef:
    pass
```

### unpeer_vpc

Type annotations for `boto3.client("lightsail").unpeer_vpc` method.

[Client.unpeer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.unpeer_vpc)

```python
def unpeer_vpc(
    self
) -> UnpeerVpcResultTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("lightsail").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceName: str,
    tagKeys: List[str],
    resourceArn: str = None
) -> UntagResourceResultTypeDef:
    pass
```

### update_container_service

Type annotations for `boto3.client("lightsail").update_container_service` method.

[Client.update_container_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_container_service)

```python
def update_container_service(
    self,
    serviceName: str,
    power: ContainerServicePowerName = None,
    scale: int = None,
    isDisabled: bool = None,
    publicDomainNames: Dict[str, List[str]] = None
) -> UpdateContainerServiceResultTypeDef:
    pass
```

### update_distribution

Type annotations for `boto3.client("lightsail").update_distribution` method.

[Client.update_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_distribution)

```python
def update_distribution(
    self,
    distributionName: str,
    origin: InputOriginTypeDef = None,
    defaultCacheBehavior: "CacheBehaviorTypeDef" = None,
    cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
    cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
    isEnabled: bool = None
) -> UpdateDistributionResultTypeDef:
    pass
```

### update_distribution_bundle

Type annotations for `boto3.client("lightsail").update_distribution_bundle` method.

[Client.update_distribution_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_distribution_bundle)

```python
def update_distribution_bundle(
    self,
    distributionName: str = None,
    bundleId: str = None
) -> UpdateDistributionBundleResultTypeDef:
    pass
```

### update_domain_entry

Type annotations for `boto3.client("lightsail").update_domain_entry` method.

[Client.update_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_domain_entry)

```python
def update_domain_entry(
    self,
    domainName: str,
    domainEntry: "DomainEntryTypeDef"
) -> UpdateDomainEntryResultTypeDef:
    pass
```

### update_load_balancer_attribute

Type annotations for `boto3.client("lightsail").update_load_balancer_attribute` method.

[Client.update_load_balancer_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_load_balancer_attribute)

```python
def update_load_balancer_attribute(
    self,
    loadBalancerName: str,
    attributeName: LoadBalancerAttributeName,
    attributeValue: str
) -> UpdateLoadBalancerAttributeResultTypeDef:
    pass
```

### update_relational_database

Type annotations for `boto3.client("lightsail").update_relational_database` method.

[Client.update_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_relational_database)

```python
def update_relational_database(
    self,
    relationalDatabaseName: str,
    masterUserPassword: str = None,
    rotateMasterUserPassword: bool = None,
    preferredBackupWindow: str = None,
    preferredMaintenanceWindow: str = None,
    enableBackupRetention: bool = None,
    disableBackupRetention: bool = None,
    publiclyAccessible: bool = None,
    applyImmediately: bool = None,
    caCertificateIdentifier: str = None
) -> UpdateRelationalDatabaseResultTypeDef:
    pass
```

### update_relational_database_parameters

Type annotations for `boto3.client("lightsail").update_relational_database_parameters` method.

[Client.update_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Client.update_relational_database_parameters)

```python
def update_relational_database_parameters(
    self,
    relationalDatabaseName: str,
    parameters: List["RelationalDatabaseParameterTypeDef"]
) -> UpdateRelationalDatabaseParametersResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)

```python
@overload
def get_paginator(
    self,
    operation_name: GetActiveNamesPaginatorName
) -> GetActiveNamesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBlueprintsPaginatorName
) -> GetBlueprintsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)

```python
@overload
def get_paginator(
    self,
    operation_name: GetBundlesPaginatorName
) -> GetBundlesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)

```python
@overload
def get_paginator(
    self,
    operation_name: GetCloudFormationStackRecordsPaginatorName
) -> GetCloudFormationStackRecordsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDiskSnapshotsPaginatorName
) -> GetDiskSnapshotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDisksPaginatorName
) -> GetDisksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)

```python
@overload
def get_paginator(
    self,
    operation_name: GetDomainsPaginatorName
) -> GetDomainsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)

```python
@overload
def get_paginator(
    self,
    operation_name: GetExportSnapshotRecordsPaginatorName
) -> GetExportSnapshotRecordsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)

```python
@overload
def get_paginator(
    self,
    operation_name: GetInstanceSnapshotsPaginatorName
) -> GetInstanceSnapshotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: GetInstancesPaginatorName
) -> GetInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)

```python
@overload
def get_paginator(
    self,
    operation_name: GetKeyPairsPaginatorName
) -> GetKeyPairsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)

```python
@overload
def get_paginator(
    self,
    operation_name: GetLoadBalancersPaginatorName
) -> GetLoadBalancersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)

```python
@overload
def get_paginator(
    self,
    operation_name: GetOperationsPaginatorName
) -> GetOperationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRelationalDatabaseBlueprintsPaginatorName
) -> GetRelationalDatabaseBlueprintsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRelationalDatabaseBundlesPaginatorName
) -> GetRelationalDatabaseBundlesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRelationalDatabaseEventsPaginatorName
) -> GetRelationalDatabaseEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRelationalDatabaseParametersPaginatorName
) -> GetRelationalDatabaseParametersPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRelationalDatabaseSnapshotsPaginatorName
) -> GetRelationalDatabaseSnapshotsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)

```python
@overload
def get_paginator(
    self,
    operation_name: GetRelationalDatabasesPaginatorName
) -> GetRelationalDatabasesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("lightsail").get_paginator` method.

[Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)

```python
@overload
def get_paginator(
    self,
    operation_name: GetStaticIpsPaginatorName
) -> GetStaticIpsPaginator:
    pass
```