# Route53Client for boto3 Route53 module

> [Index](../index.md) > [Route53](./index.md) > Route53Client

Auto-generated documentation for [Route53](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53)
type annotations stubs module [mypy_boto3_route53](https://pypi.org/project/mypy-boto3-route53/).

- [Route53Client for boto3 Route53 module](#route53client-for-boto3-route53-module)
  - [Route53Client](#route53client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [activate_key_signing_key](#activate_key_signing_key)
    - [associate_vpc_with_hosted_zone](#associate_vpc_with_hosted_zone)
    - [can_paginate](#can_paginate)
    - [change_resource_record_sets](#change_resource_record_sets)
    - [change_tags_for_resource](#change_tags_for_resource)
    - [create_health_check](#create_health_check)
    - [create_hosted_zone](#create_hosted_zone)
    - [create_key_signing_key](#create_key_signing_key)
    - [create_query_logging_config](#create_query_logging_config)
    - [create_reusable_delegation_set](#create_reusable_delegation_set)
    - [create_traffic_policy](#create_traffic_policy)
    - [create_traffic_policy_instance](#create_traffic_policy_instance)
    - [create_traffic_policy_version](#create_traffic_policy_version)
    - [create_vpc_association_authorization](#create_vpc_association_authorization)
    - [deactivate_key_signing_key](#deactivate_key_signing_key)
    - [delete_health_check](#delete_health_check)
    - [delete_hosted_zone](#delete_hosted_zone)
    - [delete_key_signing_key](#delete_key_signing_key)
    - [delete_query_logging_config](#delete_query_logging_config)
    - [delete_reusable_delegation_set](#delete_reusable_delegation_set)
    - [delete_traffic_policy](#delete_traffic_policy)
    - [delete_traffic_policy_instance](#delete_traffic_policy_instance)
    - [delete_vpc_association_authorization](#delete_vpc_association_authorization)
    - [disable_hosted_zone_dnssec](#disable_hosted_zone_dnssec)
    - [disassociate_vpc_from_hosted_zone](#disassociate_vpc_from_hosted_zone)
    - [enable_hosted_zone_dnssec](#enable_hosted_zone_dnssec)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_limit](#get_account_limit)
    - [get_change](#get_change)
    - [get_checker_ip_ranges](#get_checker_ip_ranges)
    - [get_dnssec](#get_dnssec)
    - [get_geo_location](#get_geo_location)
    - [get_health_check](#get_health_check)
    - [get_health_check_count](#get_health_check_count)
    - [get_health_check_last_failure_reason](#get_health_check_last_failure_reason)
    - [get_health_check_status](#get_health_check_status)
    - [get_hosted_zone](#get_hosted_zone)
    - [get_hosted_zone_count](#get_hosted_zone_count)
    - [get_hosted_zone_limit](#get_hosted_zone_limit)
    - [get_query_logging_config](#get_query_logging_config)
    - [get_reusable_delegation_set](#get_reusable_delegation_set)
    - [get_reusable_delegation_set_limit](#get_reusable_delegation_set_limit)
    - [get_traffic_policy](#get_traffic_policy)
    - [get_traffic_policy_instance](#get_traffic_policy_instance)
    - [get_traffic_policy_instance_count](#get_traffic_policy_instance_count)
    - [list_geo_locations](#list_geo_locations)
    - [list_health_checks](#list_health_checks)
    - [list_hosted_zones](#list_hosted_zones)
    - [list_hosted_zones_by_name](#list_hosted_zones_by_name)
    - [list_hosted_zones_by_vpc](#list_hosted_zones_by_vpc)
    - [list_query_logging_configs](#list_query_logging_configs)
    - [list_resource_record_sets](#list_resource_record_sets)
    - [list_reusable_delegation_sets](#list_reusable_delegation_sets)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_tags_for_resources](#list_tags_for_resources)
    - [list_traffic_policies](#list_traffic_policies)
    - [list_traffic_policy_instances](#list_traffic_policy_instances)
    - [list_traffic_policy_instances_by_hosted_zone](#list_traffic_policy_instances_by_hosted_zone)
    - [list_traffic_policy_instances_by_policy](#list_traffic_policy_instances_by_policy)
    - [list_traffic_policy_versions](#list_traffic_policy_versions)
    - [list_vpc_association_authorizations](#list_vpc_association_authorizations)
    - [test_dns_answer](#test_dns_answer)
    - [update_health_check](#update_health_check)
    - [update_hosted_zone_comment](#update_hosted_zone_comment)
    - [update_traffic_policy_comment](#update_traffic_policy_comment)
    - [update_traffic_policy_instance](#update_traffic_policy_instance)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)
    - [get_paginator](#get_paginator-2)
    - [get_paginator](#get_paginator-3)
    - [get_paginator](#get_paginator-4)
    - [get_waiter](#get_waiter)

## Route53Client

Type annotations for `boto3.client("route53")`

Can be used directly:

```python
from mypy_boto3_route53.client import Route53Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_route53.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConcurrentModification`
- `Exceptions.ConflictingDomainExists`
- `Exceptions.ConflictingTypes`
- `Exceptions.DNSSECNotFound`
- `Exceptions.DelegationSetAlreadyCreated`
- `Exceptions.DelegationSetAlreadyReusable`
- `Exceptions.DelegationSetInUse`
- `Exceptions.DelegationSetNotAvailable`
- `Exceptions.DelegationSetNotReusable`
- `Exceptions.HealthCheckAlreadyExists`
- `Exceptions.HealthCheckInUse`
- `Exceptions.HealthCheckVersionMismatch`
- `Exceptions.HostedZoneAlreadyExists`
- `Exceptions.HostedZoneNotEmpty`
- `Exceptions.HostedZoneNotFound`
- `Exceptions.HostedZoneNotPrivate`
- `Exceptions.HostedZonePartiallyDelegated`
- `Exceptions.IncompatibleVersion`
- `Exceptions.InsufficientCloudWatchLogsResourcePolicy`
- `Exceptions.InvalidArgument`
- `Exceptions.InvalidChangeBatch`
- `Exceptions.InvalidDomainName`
- `Exceptions.InvalidInput`
- `Exceptions.InvalidKMSArn`
- `Exceptions.InvalidKeySigningKeyName`
- `Exceptions.InvalidKeySigningKeyStatus`
- `Exceptions.InvalidPaginationToken`
- `Exceptions.InvalidSigningStatus`
- `Exceptions.InvalidTrafficPolicyDocument`
- `Exceptions.InvalidVPCId`
- `Exceptions.KeySigningKeyAlreadyExists`
- `Exceptions.KeySigningKeyInParentDSRecord`
- `Exceptions.KeySigningKeyInUse`
- `Exceptions.KeySigningKeyWithActiveStatusNotFound`
- `Exceptions.LastVPCAssociation`
- `Exceptions.LimitsExceeded`
- `Exceptions.NoSuchChange`
- `Exceptions.NoSuchCloudWatchLogsLogGroup`
- `Exceptions.NoSuchDelegationSet`
- `Exceptions.NoSuchGeoLocation`
- `Exceptions.NoSuchHealthCheck`
- `Exceptions.NoSuchHostedZone`
- `Exceptions.NoSuchKeySigningKey`
- `Exceptions.NoSuchQueryLoggingConfig`
- `Exceptions.NoSuchTrafficPolicy`
- `Exceptions.NoSuchTrafficPolicyInstance`
- `Exceptions.NotAuthorizedException`
- `Exceptions.PriorRequestNotComplete`
- `Exceptions.PublicZoneVPCAssociation`
- `Exceptions.QueryLoggingConfigAlreadyExists`
- `Exceptions.ThrottlingException`
- `Exceptions.TooManyHealthChecks`
- `Exceptions.TooManyHostedZones`
- `Exceptions.TooManyKeySigningKeys`
- `Exceptions.TooManyTrafficPolicies`
- `Exceptions.TooManyTrafficPolicyInstances`
- `Exceptions.TooManyTrafficPolicyVersionsForCurrentPolicy`
- `Exceptions.TooManyVPCAssociationAuthorizations`
- `Exceptions.TrafficPolicyAlreadyExists`
- `Exceptions.TrafficPolicyInUse`
- `Exceptions.TrafficPolicyInstanceAlreadyExists`
- `Exceptions.VPCAssociationAuthorizationNotFound`
- `Exceptions.VPCAssociationNotFound`


## Methods


### activate_key_signing_key

Type annotations for `boto3.client("route53").activate_key_signing_key` method.

[Client.activate_key_signing_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.activate_key_signing_key)

```python
def activate_key_signing_key(
    self,
    HostedZoneId: str,
    Name: str
) -> ActivateKeySigningKeyResponseTypeDef:
    pass
```

### associate_vpc_with_hosted_zone

Type annotations for `boto3.client("route53").associate_vpc_with_hosted_zone` method.

[Client.associate_vpc_with_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.associate_vpc_with_hosted_zone)

```python
def associate_vpc_with_hosted_zone(
    self,
    HostedZoneId: str,
    VPC: "VPCTypeDef",
    Comment: str = None
) -> AssociateVPCWithHostedZoneResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("route53").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### change_resource_record_sets

Type annotations for `boto3.client("route53").change_resource_record_sets` method.

[Client.change_resource_record_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.change_resource_record_sets)

```python
def change_resource_record_sets(
    self,
    HostedZoneId: str,
    ChangeBatch: ChangeBatchTypeDef
) -> ChangeResourceRecordSetsResponseTypeDef:
    pass
```

### change_tags_for_resource

Type annotations for `boto3.client("route53").change_tags_for_resource` method.

[Client.change_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.change_tags_for_resource)

```python
def change_tags_for_resource(
    self,
    ResourceType: TagResourceType,
    ResourceId: str,
    AddTags: List["TagTypeDef"] = None,
    RemoveTagKeys: List[str] = None
) -> Dict[str, Any]:
    pass
```

### create_health_check

Type annotations for `boto3.client("route53").create_health_check` method.

[Client.create_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_health_check)

```python
def create_health_check(
    self,
    CallerReference: str,
    HealthCheckConfig: "HealthCheckConfigTypeDef"
) -> CreateHealthCheckResponseTypeDef:
    pass
```

### create_hosted_zone

Type annotations for `boto3.client("route53").create_hosted_zone` method.

[Client.create_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_hosted_zone)

```python
def create_hosted_zone(
    self,
    Name: str,
    CallerReference: str,
    VPC: "VPCTypeDef" = None,
    HostedZoneConfig: "HostedZoneConfigTypeDef" = None,
    DelegationSetId: str = None
) -> CreateHostedZoneResponseTypeDef:
    pass
```

### create_key_signing_key

Type annotations for `boto3.client("route53").create_key_signing_key` method.

[Client.create_key_signing_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_key_signing_key)

```python
def create_key_signing_key(
    self,
    CallerReference: str,
    HostedZoneId: str,
    KeyManagementServiceArn: str,
    Name: str,
    Status: str
) -> CreateKeySigningKeyResponseTypeDef:
    pass
```

### create_query_logging_config

Type annotations for `boto3.client("route53").create_query_logging_config` method.

[Client.create_query_logging_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_query_logging_config)

```python
def create_query_logging_config(
    self,
    HostedZoneId: str,
    CloudWatchLogsLogGroupArn: str
) -> CreateQueryLoggingConfigResponseTypeDef:
    pass
```

### create_reusable_delegation_set

Type annotations for `boto3.client("route53").create_reusable_delegation_set` method.

[Client.create_reusable_delegation_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_reusable_delegation_set)

```python
def create_reusable_delegation_set(
    self,
    CallerReference: str,
    HostedZoneId: str = None
) -> CreateReusableDelegationSetResponseTypeDef:
    pass
```

### create_traffic_policy

Type annotations for `boto3.client("route53").create_traffic_policy` method.

[Client.create_traffic_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_traffic_policy)

```python
def create_traffic_policy(
    self,
    Name: str,
    Document: str,
    Comment: str = None
) -> CreateTrafficPolicyResponseTypeDef:
    pass
```

### create_traffic_policy_instance

Type annotations for `boto3.client("route53").create_traffic_policy_instance` method.

[Client.create_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_traffic_policy_instance)

```python
def create_traffic_policy_instance(
    self,
    HostedZoneId: str,
    Name: str,
    TTL: int,
    TrafficPolicyId: str,
    TrafficPolicyVersion: int
) -> CreateTrafficPolicyInstanceResponseTypeDef:
    pass
```

### create_traffic_policy_version

Type annotations for `boto3.client("route53").create_traffic_policy_version` method.

[Client.create_traffic_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_traffic_policy_version)

```python
def create_traffic_policy_version(
    self,
    Id: str,
    Document: str,
    Comment: str = None
) -> CreateTrafficPolicyVersionResponseTypeDef:
    pass
```

### create_vpc_association_authorization

Type annotations for `boto3.client("route53").create_vpc_association_authorization` method.

[Client.create_vpc_association_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.create_vpc_association_authorization)

```python
def create_vpc_association_authorization(
    self,
    HostedZoneId: str,
    VPC: "VPCTypeDef"
) -> CreateVPCAssociationAuthorizationResponseTypeDef:
    pass
```

### deactivate_key_signing_key

Type annotations for `boto3.client("route53").deactivate_key_signing_key` method.

[Client.deactivate_key_signing_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.deactivate_key_signing_key)

```python
def deactivate_key_signing_key(
    self,
    HostedZoneId: str,
    Name: str
) -> DeactivateKeySigningKeyResponseTypeDef:
    pass
```

### delete_health_check

Type annotations for `boto3.client("route53").delete_health_check` method.

[Client.delete_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_health_check)

```python
def delete_health_check(
    self,
    HealthCheckId: str
) -> Dict[str, Any]:
    pass
```

### delete_hosted_zone

Type annotations for `boto3.client("route53").delete_hosted_zone` method.

[Client.delete_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_hosted_zone)

```python
def delete_hosted_zone(
    self,
    Id: str
) -> DeleteHostedZoneResponseTypeDef:
    pass
```

### delete_key_signing_key

Type annotations for `boto3.client("route53").delete_key_signing_key` method.

[Client.delete_key_signing_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_key_signing_key)

```python
def delete_key_signing_key(
    self,
    HostedZoneId: str,
    Name: str
) -> DeleteKeySigningKeyResponseTypeDef:
    pass
```

### delete_query_logging_config

Type annotations for `boto3.client("route53").delete_query_logging_config` method.

[Client.delete_query_logging_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_query_logging_config)

```python
def delete_query_logging_config(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_reusable_delegation_set

Type annotations for `boto3.client("route53").delete_reusable_delegation_set` method.

[Client.delete_reusable_delegation_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_reusable_delegation_set)

```python
def delete_reusable_delegation_set(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_traffic_policy

Type annotations for `boto3.client("route53").delete_traffic_policy` method.

[Client.delete_traffic_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_traffic_policy)

```python
def delete_traffic_policy(
    self,
    Id: str,
    Version: int
) -> Dict[str, Any]:
    pass
```

### delete_traffic_policy_instance

Type annotations for `boto3.client("route53").delete_traffic_policy_instance` method.

[Client.delete_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_traffic_policy_instance)

```python
def delete_traffic_policy_instance(
    self,
    Id: str
) -> Dict[str, Any]:
    pass
```

### delete_vpc_association_authorization

Type annotations for `boto3.client("route53").delete_vpc_association_authorization` method.

[Client.delete_vpc_association_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.delete_vpc_association_authorization)

```python
def delete_vpc_association_authorization(
    self,
    HostedZoneId: str,
    VPC: "VPCTypeDef"
) -> Dict[str, Any]:
    pass
```

### disable_hosted_zone_dnssec

Type annotations for `boto3.client("route53").disable_hosted_zone_dnssec` method.

[Client.disable_hosted_zone_dnssec documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.disable_hosted_zone_dnssec)

```python
def disable_hosted_zone_dnssec(
    self,
    HostedZoneId: str
) -> DisableHostedZoneDNSSECResponseTypeDef:
    pass
```

### disassociate_vpc_from_hosted_zone

Type annotations for `boto3.client("route53").disassociate_vpc_from_hosted_zone` method.

[Client.disassociate_vpc_from_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.disassociate_vpc_from_hosted_zone)

```python
def disassociate_vpc_from_hosted_zone(
    self,
    HostedZoneId: str,
    VPC: "VPCTypeDef",
    Comment: str = None
) -> DisassociateVPCFromHostedZoneResponseTypeDef:
    pass
```

### enable_hosted_zone_dnssec

Type annotations for `boto3.client("route53").enable_hosted_zone_dnssec` method.

[Client.enable_hosted_zone_dnssec documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.enable_hosted_zone_dnssec)

```python
def enable_hosted_zone_dnssec(
    self,
    HostedZoneId: str
) -> EnableHostedZoneDNSSECResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("route53").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.generate_presigned_url)

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

### get_account_limit

Type annotations for `boto3.client("route53").get_account_limit` method.

[Client.get_account_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_account_limit)

```python
def get_account_limit(
    self,
    Type: AccountLimitType
) -> GetAccountLimitResponseTypeDef:
    pass
```

### get_change

Type annotations for `boto3.client("route53").get_change` method.

[Client.get_change documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_change)

```python
def get_change(
    self,
    Id: str
) -> GetChangeResponseTypeDef:
    pass
```

### get_checker_ip_ranges

Type annotations for `boto3.client("route53").get_checker_ip_ranges` method.

[Client.get_checker_ip_ranges documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_checker_ip_ranges)

```python
def get_checker_ip_ranges(
    self
) -> GetCheckerIpRangesResponseTypeDef:
    pass
```

### get_dnssec

Type annotations for `boto3.client("route53").get_dnssec` method.

[Client.get_dnssec documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_dnssec)

```python
def get_dnssec(
    self,
    HostedZoneId: str
) -> GetDNSSECResponseTypeDef:
    pass
```

### get_geo_location

Type annotations for `boto3.client("route53").get_geo_location` method.

[Client.get_geo_location documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_geo_location)

```python
def get_geo_location(
    self,
    ContinentCode: str = None,
    CountryCode: str = None,
    SubdivisionCode: str = None
) -> GetGeoLocationResponseTypeDef:
    pass
```

### get_health_check

Type annotations for `boto3.client("route53").get_health_check` method.

[Client.get_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_health_check)

```python
def get_health_check(
    self,
    HealthCheckId: str
) -> GetHealthCheckResponseTypeDef:
    pass
```

### get_health_check_count

Type annotations for `boto3.client("route53").get_health_check_count` method.

[Client.get_health_check_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_health_check_count)

```python
def get_health_check_count(
    self
) -> GetHealthCheckCountResponseTypeDef:
    pass
```

### get_health_check_last_failure_reason

Type annotations for `boto3.client("route53").get_health_check_last_failure_reason` method.

[Client.get_health_check_last_failure_reason documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_health_check_last_failure_reason)

```python
def get_health_check_last_failure_reason(
    self,
    HealthCheckId: str
) -> GetHealthCheckLastFailureReasonResponseTypeDef:
    pass
```

### get_health_check_status

Type annotations for `boto3.client("route53").get_health_check_status` method.

[Client.get_health_check_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_health_check_status)

```python
def get_health_check_status(
    self,
    HealthCheckId: str
) -> GetHealthCheckStatusResponseTypeDef:
    pass
```

### get_hosted_zone

Type annotations for `boto3.client("route53").get_hosted_zone` method.

[Client.get_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_hosted_zone)

```python
def get_hosted_zone(
    self,
    Id: str
) -> GetHostedZoneResponseTypeDef:
    pass
```

### get_hosted_zone_count

Type annotations for `boto3.client("route53").get_hosted_zone_count` method.

[Client.get_hosted_zone_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_hosted_zone_count)

```python
def get_hosted_zone_count(
    self
) -> GetHostedZoneCountResponseTypeDef:
    pass
```

### get_hosted_zone_limit

Type annotations for `boto3.client("route53").get_hosted_zone_limit` method.

[Client.get_hosted_zone_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_hosted_zone_limit)

```python
def get_hosted_zone_limit(
    self,
    Type: HostedZoneLimitType,
    HostedZoneId: str
) -> GetHostedZoneLimitResponseTypeDef:
    pass
```

### get_query_logging_config

Type annotations for `boto3.client("route53").get_query_logging_config` method.

[Client.get_query_logging_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_query_logging_config)

```python
def get_query_logging_config(
    self,
    Id: str
) -> GetQueryLoggingConfigResponseTypeDef:
    pass
```

### get_reusable_delegation_set

Type annotations for `boto3.client("route53").get_reusable_delegation_set` method.

[Client.get_reusable_delegation_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_reusable_delegation_set)

```python
def get_reusable_delegation_set(
    self,
    Id: str
) -> GetReusableDelegationSetResponseTypeDef:
    pass
```

### get_reusable_delegation_set_limit

Type annotations for `boto3.client("route53").get_reusable_delegation_set_limit` method.

[Client.get_reusable_delegation_set_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_reusable_delegation_set_limit)

```python
def get_reusable_delegation_set_limit(
    self,
    Type: ReusableDelegationSetLimitType,
    DelegationSetId: str
) -> GetReusableDelegationSetLimitResponseTypeDef:
    pass
```

### get_traffic_policy

Type annotations for `boto3.client("route53").get_traffic_policy` method.

[Client.get_traffic_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_traffic_policy)

```python
def get_traffic_policy(
    self,
    Id: str,
    Version: int
) -> GetTrafficPolicyResponseTypeDef:
    pass
```

### get_traffic_policy_instance

Type annotations for `boto3.client("route53").get_traffic_policy_instance` method.

[Client.get_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_traffic_policy_instance)

```python
def get_traffic_policy_instance(
    self,
    Id: str
) -> GetTrafficPolicyInstanceResponseTypeDef:
    pass
```

### get_traffic_policy_instance_count

Type annotations for `boto3.client("route53").get_traffic_policy_instance_count` method.

[Client.get_traffic_policy_instance_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.get_traffic_policy_instance_count)

```python
def get_traffic_policy_instance_count(
    self
) -> GetTrafficPolicyInstanceCountResponseTypeDef:
    pass
```

### list_geo_locations

Type annotations for `boto3.client("route53").list_geo_locations` method.

[Client.list_geo_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_geo_locations)

```python
def list_geo_locations(
    self,
    StartContinentCode: str = None,
    StartCountryCode: str = None,
    StartSubdivisionCode: str = None,
    MaxItems: str = None
) -> ListGeoLocationsResponseTypeDef:
    pass
```

### list_health_checks

Type annotations for `boto3.client("route53").list_health_checks` method.

[Client.list_health_checks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_health_checks)

```python
def list_health_checks(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListHealthChecksResponseTypeDef:
    pass
```

### list_hosted_zones

Type annotations for `boto3.client("route53").list_hosted_zones` method.

[Client.list_hosted_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_hosted_zones)

```python
def list_hosted_zones(
    self,
    Marker: str = None,
    MaxItems: str = None,
    DelegationSetId: str = None
) -> ListHostedZonesResponseTypeDef:
    pass
```

### list_hosted_zones_by_name

Type annotations for `boto3.client("route53").list_hosted_zones_by_name` method.

[Client.list_hosted_zones_by_name documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_hosted_zones_by_name)

```python
def list_hosted_zones_by_name(
    self,
    DNSName: str = None,
    HostedZoneId: str = None,
    MaxItems: str = None
) -> ListHostedZonesByNameResponseTypeDef:
    pass
```

### list_hosted_zones_by_vpc

Type annotations for `boto3.client("route53").list_hosted_zones_by_vpc` method.

[Client.list_hosted_zones_by_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_hosted_zones_by_vpc)

```python
def list_hosted_zones_by_vpc(
    self,
    VPCId: str,
    VPCRegion: VPCRegion,
    MaxItems: str = None,
    NextToken: str = None
) -> ListHostedZonesByVPCResponseTypeDef:
    pass
```

### list_query_logging_configs

Type annotations for `boto3.client("route53").list_query_logging_configs` method.

[Client.list_query_logging_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_query_logging_configs)

```python
def list_query_logging_configs(
    self,
    HostedZoneId: str = None,
    NextToken: str = None,
    MaxResults: str = None
) -> ListQueryLoggingConfigsResponseTypeDef:
    pass
```

### list_resource_record_sets

Type annotations for `boto3.client("route53").list_resource_record_sets` method.

[Client.list_resource_record_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_resource_record_sets)

```python
def list_resource_record_sets(
    self,
    HostedZoneId: str,
    StartRecordName: str = None,
    StartRecordType: RRType = None,
    StartRecordIdentifier: str = None,
    MaxItems: str = None
) -> ListResourceRecordSetsResponseTypeDef:
    pass
```

### list_reusable_delegation_sets

Type annotations for `boto3.client("route53").list_reusable_delegation_sets` method.

[Client.list_reusable_delegation_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_reusable_delegation_sets)

```python
def list_reusable_delegation_sets(
    self,
    Marker: str = None,
    MaxItems: str = None
) -> ListReusableDelegationSetsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("route53").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceType: TagResourceType,
    ResourceId: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_tags_for_resources

Type annotations for `boto3.client("route53").list_tags_for_resources` method.

[Client.list_tags_for_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_tags_for_resources)

```python
def list_tags_for_resources(
    self,
    ResourceType: TagResourceType,
    ResourceIds: List[str]
) -> ListTagsForResourcesResponseTypeDef:
    pass
```

### list_traffic_policies

Type annotations for `boto3.client("route53").list_traffic_policies` method.

[Client.list_traffic_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_traffic_policies)

```python
def list_traffic_policies(
    self,
    TrafficPolicyIdMarker: str = None,
    MaxItems: str = None
) -> ListTrafficPoliciesResponseTypeDef:
    pass
```

### list_traffic_policy_instances

Type annotations for `boto3.client("route53").list_traffic_policy_instances` method.

[Client.list_traffic_policy_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_traffic_policy_instances)

```python
def list_traffic_policy_instances(
    self,
    HostedZoneIdMarker: str = None,
    TrafficPolicyInstanceNameMarker: str = None,
    TrafficPolicyInstanceTypeMarker: RRType = None,
    MaxItems: str = None
) -> ListTrafficPolicyInstancesResponseTypeDef:
    pass
```

### list_traffic_policy_instances_by_hosted_zone

Type annotations for `boto3.client("route53").list_traffic_policy_instances_by_hosted_zone` method.

[Client.list_traffic_policy_instances_by_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_traffic_policy_instances_by_hosted_zone)

```python
def list_traffic_policy_instances_by_hosted_zone(
    self,
    HostedZoneId: str,
    TrafficPolicyInstanceNameMarker: str = None,
    TrafficPolicyInstanceTypeMarker: RRType = None,
    MaxItems: str = None
) -> ListTrafficPolicyInstancesByHostedZoneResponseTypeDef:
    pass
```

### list_traffic_policy_instances_by_policy

Type annotations for `boto3.client("route53").list_traffic_policy_instances_by_policy` method.

[Client.list_traffic_policy_instances_by_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_traffic_policy_instances_by_policy)

```python
def list_traffic_policy_instances_by_policy(
    self,
    TrafficPolicyId: str,
    TrafficPolicyVersion: int,
    HostedZoneIdMarker: str = None,
    TrafficPolicyInstanceNameMarker: str = None,
    TrafficPolicyInstanceTypeMarker: RRType = None,
    MaxItems: str = None
) -> ListTrafficPolicyInstancesByPolicyResponseTypeDef:
    pass
```

### list_traffic_policy_versions

Type annotations for `boto3.client("route53").list_traffic_policy_versions` method.

[Client.list_traffic_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_traffic_policy_versions)

```python
def list_traffic_policy_versions(
    self,
    Id: str,
    TrafficPolicyVersionMarker: str = None,
    MaxItems: str = None
) -> ListTrafficPolicyVersionsResponseTypeDef:
    pass
```

### list_vpc_association_authorizations

Type annotations for `boto3.client("route53").list_vpc_association_authorizations` method.

[Client.list_vpc_association_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.list_vpc_association_authorizations)

```python
def list_vpc_association_authorizations(
    self,
    HostedZoneId: str,
    NextToken: str = None,
    MaxResults: str = None
) -> ListVPCAssociationAuthorizationsResponseTypeDef:
    pass
```

### test_dns_answer

Type annotations for `boto3.client("route53").test_dns_answer` method.

[Client.test_dns_answer documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.test_dns_answer)

```python
def test_dns_answer(
    self,
    HostedZoneId: str,
    RecordName: str,
    RecordType: RRType,
    ResolverIP: str = None,
    EDNS0ClientSubnetIP: str = None,
    EDNS0ClientSubnetMask: str = None
) -> TestDNSAnswerResponseTypeDef:
    pass
```

### update_health_check

Type annotations for `boto3.client("route53").update_health_check` method.

[Client.update_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.update_health_check)

```python
def update_health_check(
    self,
    HealthCheckId: str,
    HealthCheckVersion: int = None,
    IPAddress: str = None,
    Port: int = None,
    ResourcePath: str = None,
    FullyQualifiedDomainName: str = None,
    SearchString: str = None,
    FailureThreshold: int = None,
    Inverted: bool = None,
    Disabled: bool = None,
    HealthThreshold: int = None,
    ChildHealthChecks: List[str] = None,
    EnableSNI: bool = None,
    Regions: List[HealthCheckRegion] = None,
    AlarmIdentifier: "AlarmIdentifierTypeDef" = None,
    InsufficientDataHealthStatus: InsufficientDataHealthStatus = None,
    ResetElements: List[ResettableElementName] = None
) -> UpdateHealthCheckResponseTypeDef:
    pass
```

### update_hosted_zone_comment

Type annotations for `boto3.client("route53").update_hosted_zone_comment` method.

[Client.update_hosted_zone_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.update_hosted_zone_comment)

```python
def update_hosted_zone_comment(
    self,
    Id: str,
    Comment: str = None
) -> UpdateHostedZoneCommentResponseTypeDef:
    pass
```

### update_traffic_policy_comment

Type annotations for `boto3.client("route53").update_traffic_policy_comment` method.

[Client.update_traffic_policy_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.update_traffic_policy_comment)

```python
def update_traffic_policy_comment(
    self,
    Id: str,
    Version: int,
    Comment: str
) -> UpdateTrafficPolicyCommentResponseTypeDef:
    pass
```

### update_traffic_policy_instance

Type annotations for `boto3.client("route53").update_traffic_policy_instance` method.

[Client.update_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Client.update_traffic_policy_instance)

```python
def update_traffic_policy_instance(
    self,
    Id: str,
    TTL: int,
    TrafficPolicyId: str,
    TrafficPolicyVersion: int
) -> UpdateTrafficPolicyInstanceResponseTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("route53").get_paginator` method.

[Paginator.ListHealthChecks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListHealthChecks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListHealthChecksPaginatorName
) -> ListHealthChecksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("route53").get_paginator` method.

[Paginator.ListHostedZones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListHostedZones)

```python
@overload
def get_paginator(
    self,
    operation_name: ListHostedZonesPaginatorName
) -> ListHostedZonesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("route53").get_paginator` method.

[Paginator.ListQueryLoggingConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)

```python
@overload
def get_paginator(
    self,
    operation_name: ListQueryLoggingConfigsPaginatorName
) -> ListQueryLoggingConfigsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("route53").get_paginator` method.

[Paginator.ListResourceRecordSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListResourceRecordSetsPaginatorName
) -> ListResourceRecordSetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("route53").get_paginator` method.

[Paginator.ListVPCAssociationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListVPCAssociationAuthorizationsPaginatorName
) -> ListVPCAssociationAuthorizationsPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("route53").get_waiter` method.

[Waiter.ResourceRecordSetsChanged documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)

```python
def get_waiter(
    self,
    waiter_name: ResourceRecordSetsChangedWaiterName
) -> ResourceRecordSetsChangedWaiter:
    pass
```