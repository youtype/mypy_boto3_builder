# Type annotations for boto3 ElasticLoadBalancingv2 module

> [Index](../index.md) > ElasticLoadBalancingv2

Auto-generated documentation for [ElasticLoadBalancingv2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2)
type annotations stubs module [mypy_boto3_elbv2](https://pypi.org/project/mypy-boto3-elbv2/).

```bash
pip install mypy-boto3-elbv2
```

- [Type annotations for boto3 ElasticLoadBalancingv2 module](#type-annotations-for-boto3-elasticloadbalancingv2-module)
  - [ElasticLoadBalancingv2Client](#elasticloadbalancingv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## ElasticLoadBalancingv2Client

Type annotations for  `boto3.client("elbv2")` as [ElasticLoadBalancingv2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_elbv2.client import ElasticLoadBalancingv2Client
```


ElasticLoadBalancingv2Client [exceptions](./client.md#exceptions)



### Methods
- [add_listener_certificates](./client.md#add-listener-certificates)
- [add_tags](./client.md#add-tags)
- [can_paginate](./client.md#can-paginate)
- [create_listener](./client.md#create-listener)
- [create_load_balancer](./client.md#create-load-balancer)
- [create_rule](./client.md#create-rule)
- [create_target_group](./client.md#create-target-group)
- [delete_listener](./client.md#delete-listener)
- [delete_load_balancer](./client.md#delete-load-balancer)
- [delete_rule](./client.md#delete-rule)
- [delete_target_group](./client.md#delete-target-group)
- [deregister_targets](./client.md#deregister-targets)
- [describe_account_limits](./client.md#describe-account-limits)
- [describe_listener_certificates](./client.md#describe-listener-certificates)
- [describe_listeners](./client.md#describe-listeners)
- [describe_load_balancer_attributes](./client.md#describe-load-balancer-attributes)
- [describe_load_balancers](./client.md#describe-load-balancers)
- [describe_rules](./client.md#describe-rules)
- [describe_ssl_policies](./client.md#describe-ssl-policies)
- [describe_tags](./client.md#describe-tags)
- [describe_target_group_attributes](./client.md#describe-target-group-attributes)
- [describe_target_groups](./client.md#describe-target-groups)
- [describe_target_health](./client.md#describe-target-health)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_waiter](./client.md#get-waiter)
- [modify_listener](./client.md#modify-listener)
- [modify_load_balancer_attributes](./client.md#modify-load-balancer-attributes)
- [modify_rule](./client.md#modify-rule)
- [modify_target_group](./client.md#modify-target-group)
- [modify_target_group_attributes](./client.md#modify-target-group-attributes)
- [register_targets](./client.md#register-targets)
- [remove_listener_certificates](./client.md#remove-listener-certificates)
- [remove_tags](./client.md#remove-tags)
- [set_ip_address_type](./client.md#set-ip-address-type)
- [set_rule_priorities](./client.md#set-rule-priorities)
- [set_security_groups](./client.md#set-security-groups)
- [set_subnets](./client.md#set-subnets)




### Exceptions
- [ALPNPolicyNotSupportedException](./client.md#alpnpolicynotsupportedexception)
- [AllocationIdNotFoundException](./client.md#allocationidnotfoundexception)
- [AvailabilityZoneNotSupportedException](./client.md#availabilityzonenotsupportedexception)
- [CertificateNotFoundException](./client.md#certificatenotfoundexception)
- [ClientError](./client.md#clienterror)
- [DuplicateListenerException](./client.md#duplicatelistenerexception)
- [DuplicateLoadBalancerNameException](./client.md#duplicateloadbalancernameexception)
- [DuplicateTagKeysException](./client.md#duplicatetagkeysexception)
- [DuplicateTargetGroupNameException](./client.md#duplicatetargetgroupnameexception)
- [HealthUnavailableException](./client.md#healthunavailableexception)
- [IncompatibleProtocolsException](./client.md#incompatibleprotocolsexception)
- [InvalidConfigurationRequestException](./client.md#invalidconfigurationrequestexception)
- [InvalidLoadBalancerActionException](./client.md#invalidloadbalanceractionexception)
- [InvalidSchemeException](./client.md#invalidschemeexception)
- [InvalidSecurityGroupException](./client.md#invalidsecuritygroupexception)
- [InvalidSubnetException](./client.md#invalidsubnetexception)
- [InvalidTargetException](./client.md#invalidtargetexception)
- [ListenerNotFoundException](./client.md#listenernotfoundexception)
- [LoadBalancerNotFoundException](./client.md#loadbalancernotfoundexception)
- [OperationNotPermittedException](./client.md#operationnotpermittedexception)
- [PriorityInUseException](./client.md#priorityinuseexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [RuleNotFoundException](./client.md#rulenotfoundexception)
- [SSLPolicyNotFoundException](./client.md#sslpolicynotfoundexception)
- [SubnetNotFoundException](./client.md#subnetnotfoundexception)
- [TargetGroupAssociationLimitException](./client.md#targetgroupassociationlimitexception)
- [TargetGroupNotFoundException](./client.md#targetgroupnotfoundexception)
- [TooManyActionsException](./client.md#toomanyactionsexception)
- [TooManyCertificatesException](./client.md#toomanycertificatesexception)
- [TooManyListenersException](./client.md#toomanylistenersexception)
- [TooManyLoadBalancersException](./client.md#toomanyloadbalancersexception)
- [TooManyRegistrationsForTargetIdException](./client.md#toomanyregistrationsfortargetidexception)
- [TooManyRulesException](./client.md#toomanyrulesexception)
- [TooManyTagsException](./client.md#toomanytagsexception)
- [TooManyTargetGroupsException](./client.md#toomanytargetgroupsexception)
- [TooManyTargetsException](./client.md#toomanytargetsexception)
- [TooManyUniqueTargetGroupsPerLoadBalancerException](./client.md#toomanyuniquetargetgroupsperloadbalancerexception)
- [UnsupportedProtocolException](./client.md#unsupportedprotocolexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("elbv2").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_elbv2.paginators import DescribeAccountLimitsPaginator, ...
```

- [DescribeAccountLimitsPaginator](./paginators.md#describeaccountlimitspaginator)
- [DescribeListenerCertificatesPaginator](./paginators.md#describelistenercertificatespaginator)
- [DescribeListenersPaginator](./paginators.md#describelistenerspaginator)
- [DescribeLoadBalancersPaginator](./paginators.md#describeloadbalancerspaginator)
- [DescribeRulesPaginator](./paginators.md#describerulespaginator)
- [DescribeSSLPoliciesPaginator](./paginators.md#describesslpoliciespaginator)
- [DescribeTargetGroupsPaginator](./paginators.md#describetargetgroupspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("elbv2").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_elbv2.waiters import LoadBalancerAvailableWaiter, ...
```

- [LoadBalancerAvailableWaiter](./waiters.md#loadbalanceravailablewaiter)
- [LoadBalancerExistsWaiter](./waiters.md#loadbalancerexistswaiter)
- [LoadBalancersDeletedWaiter](./waiters.md#loadbalancersdeletedwaiter)
- [TargetDeregisteredWaiter](./waiters.md#targetderegisteredwaiter)
- [TargetInServiceWaiter](./waiters.md#targetinservicewaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elbv2.literals import ActionTypeEnum, ...
```

- [ActionTypeEnum](./literals.md#actiontypeenum)
- [AuthenticateCognitoActionConditionalBehaviorEnum](./literals.md#authenticatecognitoactionconditionalbehaviorenum)
- [AuthenticateOidcActionConditionalBehaviorEnum](./literals.md#authenticateoidcactionconditionalbehaviorenum)
- [DescribeAccountLimitsPaginatorName](./literals.md#describeaccountlimitspaginatorname)
- [DescribeListenerCertificatesPaginatorName](./literals.md#describelistenercertificatespaginatorname)
- [DescribeListenersPaginatorName](./literals.md#describelistenerspaginatorname)
- [DescribeLoadBalancersPaginatorName](./literals.md#describeloadbalancerspaginatorname)
- [DescribeRulesPaginatorName](./literals.md#describerulespaginatorname)
- [DescribeSSLPoliciesPaginatorName](./literals.md#describesslpoliciespaginatorname)
- [DescribeTargetGroupsPaginatorName](./literals.md#describetargetgroupspaginatorname)
- [IpAddressType](./literals.md#ipaddresstype)
- [LoadBalancerAvailableWaiterName](./literals.md#loadbalanceravailablewaitername)
- [LoadBalancerExistsWaiterName](./literals.md#loadbalancerexistswaitername)
- [LoadBalancerSchemeEnum](./literals.md#loadbalancerschemeenum)
- [LoadBalancerStateEnum](./literals.md#loadbalancerstateenum)
- [LoadBalancerTypeEnum](./literals.md#loadbalancertypeenum)
- [LoadBalancersDeletedWaiterName](./literals.md#loadbalancersdeletedwaitername)
- [ProtocolEnum](./literals.md#protocolenum)
- [RedirectActionStatusCodeEnum](./literals.md#redirectactionstatuscodeenum)
- [TargetDeregisteredWaiterName](./literals.md#targetderegisteredwaitername)
- [TargetHealthReasonEnum](./literals.md#targethealthreasonenum)
- [TargetHealthStateEnum](./literals.md#targethealthstateenum)
- [TargetInServiceWaiterName](./literals.md#targetinservicewaitername)
- [TargetTypeEnum](./literals.md#targettypeenum)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_elbv2.type_defs import ActionTypeDef, ...
```

- [ActionTypeDef](./type_defs.md#actiontypedef)
- [AddListenerCertificatesOutputTypeDef](./type_defs.md#addlistenercertificatesoutputtypedef)
- [AuthenticateCognitoActionConfigTypeDef](./type_defs.md#authenticatecognitoactionconfigtypedef)
- [AuthenticateOidcActionConfigTypeDef](./type_defs.md#authenticateoidcactionconfigtypedef)
- [AvailabilityZoneTypeDef](./type_defs.md#availabilityzonetypedef)
- [CertificateTypeDef](./type_defs.md#certificatetypedef)
- [CipherTypeDef](./type_defs.md#ciphertypedef)
- [CreateListenerOutputTypeDef](./type_defs.md#createlisteneroutputtypedef)
- [CreateLoadBalancerOutputTypeDef](./type_defs.md#createloadbalanceroutputtypedef)
- [CreateRuleOutputTypeDef](./type_defs.md#createruleoutputtypedef)
- [CreateTargetGroupOutputTypeDef](./type_defs.md#createtargetgroupoutputtypedef)
- [DescribeAccountLimitsOutputTypeDef](./type_defs.md#describeaccountlimitsoutputtypedef)
- [DescribeListenerCertificatesOutputTypeDef](./type_defs.md#describelistenercertificatesoutputtypedef)
- [DescribeListenersOutputTypeDef](./type_defs.md#describelistenersoutputtypedef)
- [DescribeLoadBalancerAttributesOutputTypeDef](./type_defs.md#describeloadbalancerattributesoutputtypedef)
- [DescribeLoadBalancersOutputTypeDef](./type_defs.md#describeloadbalancersoutputtypedef)
- [DescribeRulesOutputTypeDef](./type_defs.md#describerulesoutputtypedef)
- [DescribeSSLPoliciesOutputTypeDef](./type_defs.md#describesslpoliciesoutputtypedef)
- [DescribeTagsOutputTypeDef](./type_defs.md#describetagsoutputtypedef)
- [DescribeTargetGroupAttributesOutputTypeDef](./type_defs.md#describetargetgroupattributesoutputtypedef)
- [DescribeTargetGroupsOutputTypeDef](./type_defs.md#describetargetgroupsoutputtypedef)
- [DescribeTargetHealthOutputTypeDef](./type_defs.md#describetargethealthoutputtypedef)
- [FixedResponseActionConfigTypeDef](./type_defs.md#fixedresponseactionconfigtypedef)
- [ForwardActionConfigTypeDef](./type_defs.md#forwardactionconfigtypedef)
- [HostHeaderConditionConfigTypeDef](./type_defs.md#hostheaderconditionconfigtypedef)
- [HttpHeaderConditionConfigTypeDef](./type_defs.md#httpheaderconditionconfigtypedef)
- [HttpRequestMethodConditionConfigTypeDef](./type_defs.md#httprequestmethodconditionconfigtypedef)
- [LimitTypeDef](./type_defs.md#limittypedef)
- [ListenerTypeDef](./type_defs.md#listenertypedef)
- [LoadBalancerAddressTypeDef](./type_defs.md#loadbalanceraddresstypedef)
- [LoadBalancerAttributeTypeDef](./type_defs.md#loadbalancerattributetypedef)
- [LoadBalancerStateTypeDef](./type_defs.md#loadbalancerstatetypedef)
- [LoadBalancerTypeDef](./type_defs.md#loadbalancertypedef)
- [MatcherTypeDef](./type_defs.md#matchertypedef)
- [ModifyListenerOutputTypeDef](./type_defs.md#modifylisteneroutputtypedef)
- [ModifyLoadBalancerAttributesOutputTypeDef](./type_defs.md#modifyloadbalancerattributesoutputtypedef)
- [ModifyRuleOutputTypeDef](./type_defs.md#modifyruleoutputtypedef)
- [ModifyTargetGroupAttributesOutputTypeDef](./type_defs.md#modifytargetgroupattributesoutputtypedef)
- [ModifyTargetGroupOutputTypeDef](./type_defs.md#modifytargetgroupoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PathPatternConditionConfigTypeDef](./type_defs.md#pathpatternconditionconfigtypedef)
- [QueryStringConditionConfigTypeDef](./type_defs.md#querystringconditionconfigtypedef)
- [QueryStringKeyValuePairTypeDef](./type_defs.md#querystringkeyvaluepairtypedef)
- [RedirectActionConfigTypeDef](./type_defs.md#redirectactionconfigtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RuleConditionTypeDef](./type_defs.md#ruleconditiontypedef)
- [RulePriorityPairTypeDef](./type_defs.md#ruleprioritypairtypedef)
- [RuleTypeDef](./type_defs.md#ruletypedef)
- [SetIpAddressTypeOutputTypeDef](./type_defs.md#setipaddresstypeoutputtypedef)
- [SetRulePrioritiesOutputTypeDef](./type_defs.md#setruleprioritiesoutputtypedef)
- [SetSecurityGroupsOutputTypeDef](./type_defs.md#setsecuritygroupsoutputtypedef)
- [SetSubnetsOutputTypeDef](./type_defs.md#setsubnetsoutputtypedef)
- [SourceIpConditionConfigTypeDef](./type_defs.md#sourceipconditionconfigtypedef)
- [SslPolicyTypeDef](./type_defs.md#sslpolicytypedef)
- [SubnetMappingTypeDef](./type_defs.md#subnetmappingtypedef)
- [TagDescriptionTypeDef](./type_defs.md#tagdescriptiontypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TargetDescriptionTypeDef](./type_defs.md#targetdescriptiontypedef)
- [TargetGroupAttributeTypeDef](./type_defs.md#targetgroupattributetypedef)
- [TargetGroupStickinessConfigTypeDef](./type_defs.md#targetgroupstickinessconfigtypedef)
- [TargetGroupTupleTypeDef](./type_defs.md#targetgrouptupletypedef)
- [TargetGroupTypeDef](./type_defs.md#targetgrouptypedef)
- [TargetHealthDescriptionTypeDef](./type_defs.md#targethealthdescriptiontypedef)
- [TargetHealthTypeDef](./type_defs.md#targethealthtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
