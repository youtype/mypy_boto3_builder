# Structures for boto3 ElasticLoadBalancingv2 module

> [Index](../index.md) > [ElasticLoadBalancingv2](./index.md) > Structures

Auto-generated documentation for [ElasticLoadBalancingv2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2)
type annotations stubs module [mypy_boto3_elbv2](https://pypi.org/project/mypy-boto3-elbv2/).

- [Structures for boto3 ElasticLoadBalancingv2 module](#structures-for-boto3-elasticloadbalancingv2-module)
  - [ActionTypeDef](#actiontypedef)
  - [AddListenerCertificatesOutputTypeDef](#addlistenercertificatesoutputtypedef)
  - [AuthenticateCognitoActionConfigTypeDef](#authenticatecognitoactionconfigtypedef)
  - [AuthenticateOidcActionConfigTypeDef](#authenticateoidcactionconfigtypedef)
  - [AvailabilityZoneTypeDef](#availabilityzonetypedef)
  - [CertificateTypeDef](#certificatetypedef)
  - [CipherTypeDef](#ciphertypedef)
  - [CreateListenerOutputTypeDef](#createlisteneroutputtypedef)
  - [CreateLoadBalancerOutputTypeDef](#createloadbalanceroutputtypedef)
  - [CreateRuleOutputTypeDef](#createruleoutputtypedef)
  - [CreateTargetGroupOutputTypeDef](#createtargetgroupoutputtypedef)
  - [DescribeAccountLimitsOutputTypeDef](#describeaccountlimitsoutputtypedef)
  - [DescribeListenerCertificatesOutputTypeDef](#describelistenercertificatesoutputtypedef)
  - [DescribeListenersOutputTypeDef](#describelistenersoutputtypedef)
  - [DescribeLoadBalancerAttributesOutputTypeDef](#describeloadbalancerattributesoutputtypedef)
  - [DescribeLoadBalancersOutputTypeDef](#describeloadbalancersoutputtypedef)
  - [DescribeRulesOutputTypeDef](#describerulesoutputtypedef)
  - [DescribeSSLPoliciesOutputTypeDef](#describesslpoliciesoutputtypedef)
  - [DescribeTagsOutputTypeDef](#describetagsoutputtypedef)
  - [DescribeTargetGroupAttributesOutputTypeDef](#describetargetgroupattributesoutputtypedef)
  - [DescribeTargetGroupsOutputTypeDef](#describetargetgroupsoutputtypedef)
  - [DescribeTargetHealthOutputTypeDef](#describetargethealthoutputtypedef)
  - [FixedResponseActionConfigTypeDef](#fixedresponseactionconfigtypedef)
  - [ForwardActionConfigTypeDef](#forwardactionconfigtypedef)
  - [HostHeaderConditionConfigTypeDef](#hostheaderconditionconfigtypedef)
  - [HttpHeaderConditionConfigTypeDef](#httpheaderconditionconfigtypedef)
  - [HttpRequestMethodConditionConfigTypeDef](#httprequestmethodconditionconfigtypedef)
  - [LimitTypeDef](#limittypedef)
  - [ListenerTypeDef](#listenertypedef)
  - [LoadBalancerAddressTypeDef](#loadbalanceraddresstypedef)
  - [LoadBalancerAttributeTypeDef](#loadbalancerattributetypedef)
  - [LoadBalancerStateTypeDef](#loadbalancerstatetypedef)
  - [LoadBalancerTypeDef](#loadbalancertypedef)
  - [MatcherTypeDef](#matchertypedef)
  - [ModifyListenerOutputTypeDef](#modifylisteneroutputtypedef)
  - [ModifyLoadBalancerAttributesOutputTypeDef](#modifyloadbalancerattributesoutputtypedef)
  - [ModifyRuleOutputTypeDef](#modifyruleoutputtypedef)
  - [ModifyTargetGroupAttributesOutputTypeDef](#modifytargetgroupattributesoutputtypedef)
  - [ModifyTargetGroupOutputTypeDef](#modifytargetgroupoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PathPatternConditionConfigTypeDef](#pathpatternconditionconfigtypedef)
  - [QueryStringConditionConfigTypeDef](#querystringconditionconfigtypedef)
  - [QueryStringKeyValuePairTypeDef](#querystringkeyvaluepairtypedef)
  - [RedirectActionConfigTypeDef](#redirectactionconfigtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [RuleConditionTypeDef](#ruleconditiontypedef)
  - [RulePriorityPairTypeDef](#ruleprioritypairtypedef)
  - [RuleTypeDef](#ruletypedef)
  - [SetIpAddressTypeOutputTypeDef](#setipaddresstypeoutputtypedef)
  - [SetRulePrioritiesOutputTypeDef](#setruleprioritiesoutputtypedef)
  - [SetSecurityGroupsOutputTypeDef](#setsecuritygroupsoutputtypedef)
  - [SetSubnetsOutputTypeDef](#setsubnetsoutputtypedef)
  - [SourceIpConditionConfigTypeDef](#sourceipconditionconfigtypedef)
  - [SslPolicyTypeDef](#sslpolicytypedef)
  - [SubnetMappingTypeDef](#subnetmappingtypedef)
  - [TagDescriptionTypeDef](#tagdescriptiontypedef)
  - [TagTypeDef](#tagtypedef)
  - [TargetDescriptionTypeDef](#targetdescriptiontypedef)
  - [TargetGroupAttributeTypeDef](#targetgroupattributetypedef)
  - [TargetGroupStickinessConfigTypeDef](#targetgroupstickinessconfigtypedef)
  - [TargetGroupTupleTypeDef](#targetgrouptupletypedef)
  - [TargetGroupTypeDef](#targetgrouptypedef)
  - [TargetHealthDescriptionTypeDef](#targethealthdescriptiontypedef)
  - [TargetHealthTypeDef](#targethealthtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## ActionTypeDef

```python
from mypy_boto3_elbv2.type_defs import ActionTypeDef
```


Required fields:
- `Type`: `ActionTypeEnum`



Optional fields:
- `TargetGroupArn`: `str`
- `AuthenticateOidcConfig`: `"AuthenticateOidcActionConfigTypeDef"`
- `AuthenticateCognitoConfig`: `"AuthenticateCognitoActionConfigTypeDef"`
- `Order`: `int`
- `RedirectConfig`: `"RedirectActionConfigTypeDef"`
- `FixedResponseConfig`: `"FixedResponseActionConfigTypeDef"`
- `ForwardConfig`: `"ForwardActionConfigTypeDef"`


## AddListenerCertificatesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import AddListenerCertificatesOutputTypeDef
```




Optional fields:
- `Certificates`: `List["CertificateTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## AuthenticateCognitoActionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import AuthenticateCognitoActionConfigTypeDef
```


Required fields:
- `UserPoolArn`: `str`
- `UserPoolClientId`: `str`
- `UserPoolDomain`: `str`



Optional fields:
- `SessionCookieName`: `str`
- `Scope`: `str`
- `SessionTimeout`: `int`
- `AuthenticationRequestExtraParams`: `Dict[str, str]`
- `OnUnauthenticatedRequest`: `AuthenticateCognitoActionConditionalBehaviorEnum`


## AuthenticateOidcActionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import AuthenticateOidcActionConfigTypeDef
```


Required fields:
- `Issuer`: `str`
- `AuthorizationEndpoint`: `str`
- `TokenEndpoint`: `str`
- `UserInfoEndpoint`: `str`
- `ClientId`: `str`



Optional fields:
- `ClientSecret`: `str`
- `SessionCookieName`: `str`
- `Scope`: `str`
- `SessionTimeout`: `int`
- `AuthenticationRequestExtraParams`: `Dict[str, str]`
- `OnUnauthenticatedRequest`: `AuthenticateOidcActionConditionalBehaviorEnum`
- `UseExistingClientSecret`: `bool`


## AvailabilityZoneTypeDef

```python
from mypy_boto3_elbv2.type_defs import AvailabilityZoneTypeDef
```




Optional fields:
- `ZoneName`: `str`
- `SubnetId`: `str`
- `OutpostId`: `str`
- `LoadBalancerAddresses`: `List["LoadBalancerAddressTypeDef"]`


## CertificateTypeDef

```python
from mypy_boto3_elbv2.type_defs import CertificateTypeDef
```




Optional fields:
- `CertificateArn`: `str`
- `IsDefault`: `bool`


## CipherTypeDef

```python
from mypy_boto3_elbv2.type_defs import CipherTypeDef
```




Optional fields:
- `Name`: `str`
- `Priority`: `int`


## CreateListenerOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import CreateListenerOutputTypeDef
```




Optional fields:
- `Listeners`: `List["ListenerTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateLoadBalancerOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import CreateLoadBalancerOutputTypeDef
```




Optional fields:
- `LoadBalancers`: `List["LoadBalancerTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateRuleOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import CreateRuleOutputTypeDef
```




Optional fields:
- `Rules`: `List["RuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateTargetGroupOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import CreateTargetGroupOutputTypeDef
```




Optional fields:
- `TargetGroups`: `List["TargetGroupTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAccountLimitsOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeAccountLimitsOutputTypeDef
```




Optional fields:
- `Limits`: `List["LimitTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeListenerCertificatesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeListenerCertificatesOutputTypeDef
```




Optional fields:
- `Certificates`: `List["CertificateTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeListenersOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeListenersOutputTypeDef
```




Optional fields:
- `Listeners`: `List["ListenerTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeLoadBalancerAttributesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeLoadBalancerAttributesOutputTypeDef
```




Optional fields:
- `Attributes`: `List["LoadBalancerAttributeTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeLoadBalancersOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeLoadBalancersOutputTypeDef
```




Optional fields:
- `LoadBalancers`: `List["LoadBalancerTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRulesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeRulesOutputTypeDef
```




Optional fields:
- `Rules`: `List["RuleTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeSSLPoliciesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeSSLPoliciesOutputTypeDef
```




Optional fields:
- `SslPolicies`: `List["SslPolicyTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTagsOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeTagsOutputTypeDef
```




Optional fields:
- `TagDescriptions`: `List["TagDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTargetGroupAttributesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeTargetGroupAttributesOutputTypeDef
```




Optional fields:
- `Attributes`: `List["TargetGroupAttributeTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTargetGroupsOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeTargetGroupsOutputTypeDef
```




Optional fields:
- `TargetGroups`: `List["TargetGroupTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTargetHealthOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import DescribeTargetHealthOutputTypeDef
```




Optional fields:
- `TargetHealthDescriptions`: `List["TargetHealthDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## FixedResponseActionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import FixedResponseActionConfigTypeDef
```


Required fields:
- `StatusCode`: `str`



Optional fields:
- `MessageBody`: `str`
- `ContentType`: `str`


## ForwardActionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import ForwardActionConfigTypeDef
```




Optional fields:
- `TargetGroups`: `List["TargetGroupTupleTypeDef"]`
- `TargetGroupStickinessConfig`: `"TargetGroupStickinessConfigTypeDef"`


## HostHeaderConditionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import HostHeaderConditionConfigTypeDef
```




Optional fields:
- `Values`: `List[str]`


## HttpHeaderConditionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import HttpHeaderConditionConfigTypeDef
```




Optional fields:
- `HttpHeaderName`: `str`
- `Values`: `List[str]`


## HttpRequestMethodConditionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import HttpRequestMethodConditionConfigTypeDef
```




Optional fields:
- `Values`: `List[str]`


## LimitTypeDef

```python
from mypy_boto3_elbv2.type_defs import LimitTypeDef
```




Optional fields:
- `Name`: `str`
- `Max`: `str`


## ListenerTypeDef

```python
from mypy_boto3_elbv2.type_defs import ListenerTypeDef
```




Optional fields:
- `ListenerArn`: `str`
- `LoadBalancerArn`: `str`
- `Port`: `int`
- `Protocol`: `ProtocolEnum`
- `Certificates`: `List["CertificateTypeDef"]`
- `SslPolicy`: `str`
- `DefaultActions`: `List["ActionTypeDef"]`
- `AlpnPolicy`: `List[str]`


## LoadBalancerAddressTypeDef

```python
from mypy_boto3_elbv2.type_defs import LoadBalancerAddressTypeDef
```




Optional fields:
- `IpAddress`: `str`
- `AllocationId`: `str`
- `PrivateIPv4Address`: `str`
- `IPv6Address`: `str`


## LoadBalancerAttributeTypeDef

```python
from mypy_boto3_elbv2.type_defs import LoadBalancerAttributeTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## LoadBalancerStateTypeDef

```python
from mypy_boto3_elbv2.type_defs import LoadBalancerStateTypeDef
```




Optional fields:
- `Code`: `LoadBalancerStateEnum`
- `Reason`: `str`


## LoadBalancerTypeDef

```python
from mypy_boto3_elbv2.type_defs import LoadBalancerTypeDef
```




Optional fields:
- `LoadBalancerArn`: `str`
- `DNSName`: `str`
- `CanonicalHostedZoneId`: `str`
- `CreatedTime`: `datetime`
- `LoadBalancerName`: `str`
- `Scheme`: `LoadBalancerSchemeEnum`
- `VpcId`: `str`
- `State`: `"LoadBalancerStateTypeDef"`
- `Type`: `LoadBalancerTypeEnum`
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`
- `SecurityGroups`: `List[str]`
- `IpAddressType`: `IpAddressType`
- `CustomerOwnedIpv4Pool`: `str`


## MatcherTypeDef

```python
from mypy_boto3_elbv2.type_defs import MatcherTypeDef
```




Optional fields:
- `HttpCode`: `str`
- `GrpcCode`: `str`


## ModifyListenerOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import ModifyListenerOutputTypeDef
```




Optional fields:
- `Listeners`: `List["ListenerTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ModifyLoadBalancerAttributesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import ModifyLoadBalancerAttributesOutputTypeDef
```




Optional fields:
- `Attributes`: `List["LoadBalancerAttributeTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ModifyRuleOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import ModifyRuleOutputTypeDef
```




Optional fields:
- `Rules`: `List["RuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ModifyTargetGroupAttributesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import ModifyTargetGroupAttributesOutputTypeDef
```




Optional fields:
- `Attributes`: `List["TargetGroupAttributeTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ModifyTargetGroupOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import ModifyTargetGroupOutputTypeDef
```




Optional fields:
- `TargetGroups`: `List["TargetGroupTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PathPatternConditionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import PathPatternConditionConfigTypeDef
```




Optional fields:
- `Values`: `List[str]`


## QueryStringConditionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import QueryStringConditionConfigTypeDef
```




Optional fields:
- `Values`: `List["QueryStringKeyValuePairTypeDef"]`


## QueryStringKeyValuePairTypeDef

```python
from mypy_boto3_elbv2.type_defs import QueryStringKeyValuePairTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## RedirectActionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import RedirectActionConfigTypeDef
```


Required fields:
- `StatusCode`: `RedirectActionStatusCodeEnum`



Optional fields:
- `Protocol`: `str`
- `Port`: `str`
- `Host`: `str`
- `Path`: `str`
- `Query`: `str`


## ResponseMetadata

```python
from mypy_boto3_elbv2.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## RuleConditionTypeDef

```python
from mypy_boto3_elbv2.type_defs import RuleConditionTypeDef
```




Optional fields:
- `Field`: `str`
- `Values`: `List[str]`
- `HostHeaderConfig`: `"HostHeaderConditionConfigTypeDef"`
- `PathPatternConfig`: `"PathPatternConditionConfigTypeDef"`
- `HttpHeaderConfig`: `"HttpHeaderConditionConfigTypeDef"`
- `QueryStringConfig`: `"QueryStringConditionConfigTypeDef"`
- `HttpRequestMethodConfig`: `"HttpRequestMethodConditionConfigTypeDef"`
- `SourceIpConfig`: `"SourceIpConditionConfigTypeDef"`


## RulePriorityPairTypeDef

```python
from mypy_boto3_elbv2.type_defs import RulePriorityPairTypeDef
```




Optional fields:
- `RuleArn`: `str`
- `Priority`: `int`


## RuleTypeDef

```python
from mypy_boto3_elbv2.type_defs import RuleTypeDef
```




Optional fields:
- `RuleArn`: `str`
- `Priority`: `str`
- `Conditions`: `List["RuleConditionTypeDef"]`
- `Actions`: `List["ActionTypeDef"]`
- `IsDefault`: `bool`


## SetIpAddressTypeOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import SetIpAddressTypeOutputTypeDef
```




Optional fields:
- `IpAddressType`: `IpAddressType`
- `ResponseMetadata`: `"ResponseMetadata"`


## SetRulePrioritiesOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import SetRulePrioritiesOutputTypeDef
```




Optional fields:
- `Rules`: `List["RuleTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## SetSecurityGroupsOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import SetSecurityGroupsOutputTypeDef
```




Optional fields:
- `SecurityGroupIds`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## SetSubnetsOutputTypeDef

```python
from mypy_boto3_elbv2.type_defs import SetSubnetsOutputTypeDef
```




Optional fields:
- `AvailabilityZones`: `List["AvailabilityZoneTypeDef"]`
- `IpAddressType`: `IpAddressType`
- `ResponseMetadata`: `"ResponseMetadata"`


## SourceIpConditionConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import SourceIpConditionConfigTypeDef
```




Optional fields:
- `Values`: `List[str]`


## SslPolicyTypeDef

```python
from mypy_boto3_elbv2.type_defs import SslPolicyTypeDef
```




Optional fields:
- `SslProtocols`: `List[str]`
- `Ciphers`: `List["CipherTypeDef"]`
- `Name`: `str`


## SubnetMappingTypeDef

```python
from mypy_boto3_elbv2.type_defs import SubnetMappingTypeDef
```




Optional fields:
- `SubnetId`: `str`
- `AllocationId`: `str`
- `PrivateIPv4Address`: `str`
- `IPv6Address`: `str`


## TagDescriptionTypeDef

```python
from mypy_boto3_elbv2.type_defs import TagDescriptionTypeDef
```




Optional fields:
- `ResourceArn`: `str`
- `Tags`: `List["TagTypeDef"]`


## TagTypeDef

```python
from mypy_boto3_elbv2.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## TargetDescriptionTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetDescriptionTypeDef
```


Required fields:
- `Id`: `str`



Optional fields:
- `Port`: `int`
- `AvailabilityZone`: `str`


## TargetGroupAttributeTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetGroupAttributeTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TargetGroupStickinessConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetGroupStickinessConfigTypeDef
```




Optional fields:
- `Enabled`: `bool`
- `DurationSeconds`: `int`


## TargetGroupTupleTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetGroupTupleTypeDef
```




Optional fields:
- `TargetGroupArn`: `str`
- `Weight`: `int`


## TargetGroupTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetGroupTypeDef
```




Optional fields:
- `TargetGroupArn`: `str`
- `TargetGroupName`: `str`
- `Protocol`: `ProtocolEnum`
- `Port`: `int`
- `VpcId`: `str`
- `HealthCheckProtocol`: `ProtocolEnum`
- `HealthCheckPort`: `str`
- `HealthCheckEnabled`: `bool`
- `HealthCheckIntervalSeconds`: `int`
- `HealthCheckTimeoutSeconds`: `int`
- `HealthyThresholdCount`: `int`
- `UnhealthyThresholdCount`: `int`
- `HealthCheckPath`: `str`
- `Matcher`: `"MatcherTypeDef"`
- `LoadBalancerArns`: `List[str]`
- `TargetType`: `TargetTypeEnum`
- `ProtocolVersion`: `str`


## TargetHealthDescriptionTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetHealthDescriptionTypeDef
```




Optional fields:
- `Target`: `"TargetDescriptionTypeDef"`
- `HealthCheckPort`: `str`
- `TargetHealth`: `"TargetHealthTypeDef"`


## TargetHealthTypeDef

```python
from mypy_boto3_elbv2.type_defs import TargetHealthTypeDef
```




Optional fields:
- `State`: `TargetHealthStateEnum`
- `Reason`: `TargetHealthReasonEnum`
- `Description`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_elbv2.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

