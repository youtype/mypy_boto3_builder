# Type annotations for boto3 ElasticLoadBalancing module

> [Index](../index.md) > ElasticLoadBalancing

Auto-generated documentation for [ElasticLoadBalancing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing)
type annotations stubs module [mypy_boto3_elb](https://pypi.org/project/mypy-boto3-elb/).

```bash
pip install mypy-boto3-elb
```

- [Type annotations for boto3 ElasticLoadBalancing module](#type-annotations-for-boto3-elasticloadbalancing-module)
  - [ElasticLoadBalancingClient](#elasticloadbalancingclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ElasticLoadBalancingClient

Type annotations for  `boto3.client("elb")` as [ElasticLoadBalancingClient](./client.md)

Can be used directly:

```python
from mypy_boto3_elb.client import ElasticLoadBalancingClient
```


ElasticLoadBalancingClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags](./client.md#add-tags)
- [apply_security_groups_to_load_balancer](./client.md#apply-security-groups-to-load-balancer)
- [attach_load_balancer_to_subnets](./client.md#attach-load-balancer-to-subnets)
- [can_paginate](./client.md#can-paginate)
- [configure_health_check](./client.md#configure-health-check)
- [create_app_cookie_stickiness_policy](./client.md#create-app-cookie-stickiness-policy)
- [create_lb_cookie_stickiness_policy](./client.md#create-lb-cookie-stickiness-policy)
- [create_load_balancer](./client.md#create-load-balancer)
- [create_load_balancer_listeners](./client.md#create-load-balancer-listeners)
- [create_load_balancer_policy](./client.md#create-load-balancer-policy)
- [delete_load_balancer](./client.md#delete-load-balancer)
- [delete_load_balancer_listeners](./client.md#delete-load-balancer-listeners)
- [delete_load_balancer_policy](./client.md#delete-load-balancer-policy)
- [deregister_instances_from_load_balancer](./client.md#deregister-instances-from-load-balancer)
- [describe_account_limits](./client.md#describe-account-limits)
- [describe_instance_health](./client.md#describe-instance-health)
- [describe_load_balancer_attributes](./client.md#describe-load-balancer-attributes)
- [describe_load_balancer_policies](./client.md#describe-load-balancer-policies)
- [describe_load_balancer_policy_types](./client.md#describe-load-balancer-policy-types)
- [describe_load_balancers](./client.md#describe-load-balancers)
- [describe_tags](./client.md#describe-tags)
- [detach_load_balancer_from_subnets](./client.md#detach-load-balancer-from-subnets)
- [disable_availability_zones_for_load_balancer](./client.md#disable-availability-zones-for-load-balancer)
- [enable_availability_zones_for_load_balancer](./client.md#enable-availability-zones-for-load-balancer)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [modify_load_balancer_attributes](./client.md#modify-load-balancer-attributes)
- [register_instances_with_load_balancer](./client.md#register-instances-with-load-balancer)
- [remove_tags](./client.md#remove-tags)
- [set_load_balancer_listener_ssl_certificate](./client.md#set-load-balancer-listener-ssl-certificate)
- [set_load_balancer_policies_for_backend_server](./client.md#set-load-balancer-policies-for-backend-server)
- [set_load_balancer_policies_of_listener](./client.md#set-load-balancer-policies-of-listener)




### Exceptions
- [AccessPointNotFoundException](./client.md#accesspointnotfoundexception)
- [CertificateNotFoundException](./client.md#certificatenotfoundexception)
- [ClientError](./client.md#clienterror)
- [DependencyThrottleException](./client.md#dependencythrottleexception)
- [DuplicateAccessPointNameException](./client.md#duplicateaccesspointnameexception)
- [DuplicateListenerException](./client.md#duplicatelistenerexception)
- [DuplicatePolicyNameException](./client.md#duplicatepolicynameexception)
- [DuplicateTagKeysException](./client.md#duplicatetagkeysexception)
- [InvalidConfigurationRequestException](./client.md#invalidconfigurationrequestexception)
- [InvalidEndPointException](./client.md#invalidendpointexception)
- [InvalidSchemeException](./client.md#invalidschemeexception)
- [InvalidSecurityGroupException](./client.md#invalidsecuritygroupexception)
- [InvalidSubnetException](./client.md#invalidsubnetexception)
- [ListenerNotFoundException](./client.md#listenernotfoundexception)
- [LoadBalancerAttributeNotFoundException](./client.md#loadbalancerattributenotfoundexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [PolicyNotFoundException](./client.md#policynotfoundexception)
- [PolicyTypeNotFoundException](./client.md#policytypenotfoundexception)
- [SubnetNotFoundException](./client.md#subnetnotfoundexception)
- [TooManyAccessPointsException](./client.md#toomanyaccesspointsexception)
- [TooManyPoliciesException](./client.md#toomanypoliciesexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [UnsupportedProtocolException](./client.md#unsupportedprotocolexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("elb").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_elb.paginators import DescribeAccountLimitsPaginator, ...
```

- [DescribeAccountLimitsPaginator](./paginators.md#describeaccountlimitspaginator)
- [DescribeLoadBalancersPaginator](./paginators.md#describeloadbalancerspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("elb").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_elb.waiters import AnyInstanceInServiceWaiter, ...
```

- [AnyInstanceInServiceWaiter](./waiters.md#anyinstanceinservicewaiter)
- [InstanceDeregisteredWaiter](./waiters.md#instancederegisteredwaiter)
- [InstanceInServiceWaiter](./waiters.md#instanceinservicewaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elb.literals import AnyInstanceInServiceWaiterName, ...
```

- [AnyInstanceInServiceWaiterName](./literals.md#anyinstanceinservicewaitername)
- [DescribeAccountLimitsPaginatorName](./literals.md#describeaccountlimitspaginatorname)
- [DescribeLoadBalancersPaginatorName](./literals.md#describeloadbalancerspaginatorname)
- [InstanceDeregisteredWaiterName](./literals.md#instancederegisteredwaitername)
- [InstanceInServiceWaiterName](./literals.md#instanceinservicewaitername)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elb.type_defs import AccessLogTypeDef, ...
```

- [AccessLogTypeDef](./type_defs.md#accesslogtypedef)
- [AddAvailabilityZonesOutputTypeDef](./type_defs.md#addavailabilityzonesoutputtypedef)
- [AdditionalAttributeTypeDef](./type_defs.md#additionalattributetypedef)
- [AppCookieStickinessPolicyTypeDef](./type_defs.md#appcookiestickinesspolicytypedef)
- [ApplySecurityGroupsToLoadBalancerOutputTypeDef](./type_defs.md#applysecuritygroupstoloadbalanceroutputtypedef)
- [AttachLoadBalancerToSubnetsOutputTypeDef](./type_defs.md#attachloadbalancertosubnetsoutputtypedef)
- [BackendServerDescriptionTypeDef](./type_defs.md#backendserverdescriptiontypedef)
- [ConfigureHealthCheckOutputTypeDef](./type_defs.md#configurehealthcheckoutputtypedef)
- [ConnectionDrainingTypeDef](./type_defs.md#connectiondrainingtypedef)
- [ConnectionSettingsTypeDef](./type_defs.md#connectionsettingstypedef)
- [CreateAccessPointOutputTypeDef](./type_defs.md#createaccesspointoutputtypedef)
- [CrossZoneLoadBalancingTypeDef](./type_defs.md#crosszoneloadbalancingtypedef)
- [DeregisterEndPointsOutputTypeDef](./type_defs.md#deregisterendpointsoutputtypedef)
- [DescribeAccessPointsOutputTypeDef](./type_defs.md#describeaccesspointsoutputtypedef)
- [DescribeAccountLimitsOutputTypeDef](./type_defs.md#describeaccountlimitsoutputtypedef)
- [DescribeEndPointStateOutputTypeDef](./type_defs.md#describeendpointstateoutputtypedef)
- [DescribeLoadBalancerAttributesOutputTypeDef](./type_defs.md#describeloadbalancerattributesoutputtypedef)
- [DescribeLoadBalancerPoliciesOutputTypeDef](./type_defs.md#describeloadbalancerpoliciesoutputtypedef)
- [DescribeLoadBalancerPolicyTypesOutputTypeDef](./type_defs.md#describeloadbalancerpolicytypesoutputtypedef)
- [DescribeTagsOutputTypeDef](./type_defs.md#describetagsoutputtypedef)
- [DetachLoadBalancerFromSubnetsOutputTypeDef](./type_defs.md#detachloadbalancerfromsubnetsoutputtypedef)
- [HealthCheckTypeDef](./type_defs.md#healthchecktypedef)
- [InstanceStateTypeDef](./type_defs.md#instancestatetypedef)
- [InstanceTypeDef](./type_defs.md#instancetypedef)
- [LBCookieStickinessPolicyTypeDef](./type_defs.md#lbcookiestickinesspolicytypedef)
- [LimitTypeDef](./type_defs.md#limittypedef)
- [ListenerDescriptionTypeDef](./type_defs.md#listenerdescriptiontypedef)
- [ListenerTypeDef](./type_defs.md#listenertypedef)
- [LoadBalancerAttributesTypeDef](./type_defs.md#loadbalancerattributestypedef)
- [LoadBalancerDescriptionTypeDef](./type_defs.md#loadbalancerdescriptiontypedef)
- [ModifyLoadBalancerAttributesOutputTypeDef](./type_defs.md#modifyloadbalancerattributesoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PoliciesTypeDef](./type_defs.md#policiestypedef)
- [PolicyAttributeDescriptionTypeDef](./type_defs.md#policyattributedescriptiontypedef)
- [PolicyAttributeTypeDef](./type_defs.md#policyattributetypedef)
- [PolicyAttributeTypeDescriptionTypeDef](./type_defs.md#policyattributetypedescriptiontypedef)
- [PolicyDescriptionTypeDef](./type_defs.md#policydescriptiontypedef)
- [PolicyTypeDescriptionTypeDef](./type_defs.md#policytypedescriptiontypedef)
- [RegisterEndPointsOutputTypeDef](./type_defs.md#registerendpointsoutputtypedef)
- [RemoveAvailabilityZonesOutputTypeDef](./type_defs.md#removeavailabilityzonesoutputtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SourceSecurityGroupTypeDef](./type_defs.md#sourcesecuritygrouptypedef)
- [TagDescriptionTypeDef](./type_defs.md#tagdescriptiontypedef)
- [TagKeyOnlyTypeDef](./type_defs.md#tagkeyonlytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
