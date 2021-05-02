# Structures for boto3 ElasticLoadBalancing module

> [Index](../index.md) > [ElasticLoadBalancing](./index.md) > Structures

Auto-generated documentation for [ElasticLoadBalancing](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html#ElasticLoadBalancing)
type annotations stubs module [mypy_boto3_elb](https://pypi.org/project/mypy-boto3-elb/).

- [Structures for boto3 ElasticLoadBalancing module](#structures-for-boto3-elasticloadbalancing-module)
  - [AccessLogTypeDef](#accesslogtypedef)
  - [AddAvailabilityZonesOutputTypeDef](#addavailabilityzonesoutputtypedef)
  - [AdditionalAttributeTypeDef](#additionalattributetypedef)
  - [AppCookieStickinessPolicyTypeDef](#appcookiestickinesspolicytypedef)
  - [ApplySecurityGroupsToLoadBalancerOutputTypeDef](#applysecuritygroupstoloadbalanceroutputtypedef)
  - [AttachLoadBalancerToSubnetsOutputTypeDef](#attachloadbalancertosubnetsoutputtypedef)
  - [BackendServerDescriptionTypeDef](#backendserverdescriptiontypedef)
  - [ConfigureHealthCheckOutputTypeDef](#configurehealthcheckoutputtypedef)
  - [ConnectionDrainingTypeDef](#connectiondrainingtypedef)
  - [ConnectionSettingsTypeDef](#connectionsettingstypedef)
  - [CreateAccessPointOutputTypeDef](#createaccesspointoutputtypedef)
  - [CrossZoneLoadBalancingTypeDef](#crosszoneloadbalancingtypedef)
  - [DeregisterEndPointsOutputTypeDef](#deregisterendpointsoutputtypedef)
  - [DescribeAccessPointsOutputTypeDef](#describeaccesspointsoutputtypedef)
  - [DescribeAccountLimitsOutputTypeDef](#describeaccountlimitsoutputtypedef)
  - [DescribeEndPointStateOutputTypeDef](#describeendpointstateoutputtypedef)
  - [DescribeLoadBalancerAttributesOutputTypeDef](#describeloadbalancerattributesoutputtypedef)
  - [DescribeLoadBalancerPoliciesOutputTypeDef](#describeloadbalancerpoliciesoutputtypedef)
  - [DescribeLoadBalancerPolicyTypesOutputTypeDef](#describeloadbalancerpolicytypesoutputtypedef)
  - [DescribeTagsOutputTypeDef](#describetagsoutputtypedef)
  - [DetachLoadBalancerFromSubnetsOutputTypeDef](#detachloadbalancerfromsubnetsoutputtypedef)
  - [HealthCheckTypeDef](#healthchecktypedef)
  - [InstanceStateTypeDef](#instancestatetypedef)
  - [InstanceTypeDef](#instancetypedef)
  - [LBCookieStickinessPolicyTypeDef](#lbcookiestickinesspolicytypedef)
  - [LimitTypeDef](#limittypedef)
  - [ListenerDescriptionTypeDef](#listenerdescriptiontypedef)
  - [ListenerTypeDef](#listenertypedef)
  - [LoadBalancerAttributesTypeDef](#loadbalancerattributestypedef)
  - [LoadBalancerDescriptionTypeDef](#loadbalancerdescriptiontypedef)
  - [ModifyLoadBalancerAttributesOutputTypeDef](#modifyloadbalancerattributesoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PoliciesTypeDef](#policiestypedef)
  - [PolicyAttributeDescriptionTypeDef](#policyattributedescriptiontypedef)
  - [PolicyAttributeTypeDef](#policyattributetypedef)
  - [PolicyAttributeTypeDescriptionTypeDef](#policyattributetypedescriptiontypedef)
  - [PolicyDescriptionTypeDef](#policydescriptiontypedef)
  - [PolicyTypeDescriptionTypeDef](#policytypedescriptiontypedef)
  - [RegisterEndPointsOutputTypeDef](#registerendpointsoutputtypedef)
  - [RemoveAvailabilityZonesOutputTypeDef](#removeavailabilityzonesoutputtypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SourceSecurityGroupTypeDef](#sourcesecuritygrouptypedef)
  - [TagDescriptionTypeDef](#tagdescriptiontypedef)
  - [TagKeyOnlyTypeDef](#tagkeyonlytypedef)
  - [TagTypeDef](#tagtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccessLogTypeDef

```python
from mypy_boto3_elb.type_defs import AccessLogTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `S3BucketName`: `str`
- `EmitInterval`: `int`
- `S3BucketPrefix`: `str`


## AddAvailabilityZonesOutputTypeDef

```python
from mypy_boto3_elb.type_defs import AddAvailabilityZonesOutputTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## AdditionalAttributeTypeDef

```python
from mypy_boto3_elb.type_defs import AdditionalAttributeTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## AppCookieStickinessPolicyTypeDef

```python
from mypy_boto3_elb.type_defs import AppCookieStickinessPolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `CookieName`: `str`


## ApplySecurityGroupsToLoadBalancerOutputTypeDef

```python
from mypy_boto3_elb.type_defs import ApplySecurityGroupsToLoadBalancerOutputTypeDef
```




Optional fields:
- `SecurityGroups`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## AttachLoadBalancerToSubnetsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import AttachLoadBalancerToSubnetsOutputTypeDef
```




Optional fields:
- `Subnets`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BackendServerDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import BackendServerDescriptionTypeDef
```




Optional fields:
- `InstancePort`: `int`
- `PolicyNames`: `List[str]`


## ConfigureHealthCheckOutputTypeDef

```python
from mypy_boto3_elb.type_defs import ConfigureHealthCheckOutputTypeDef
```




Optional fields:
- `HealthCheck`: `"HealthCheckTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ConnectionDrainingTypeDef

```python
from mypy_boto3_elb.type_defs import ConnectionDrainingTypeDef
```


Required fields:
- `Enabled`: `bool`



Optional fields:
- `Timeout`: `int`


## ConnectionSettingsTypeDef

```python
from mypy_boto3_elb.type_defs import ConnectionSettingsTypeDef
```


Required fields:
- `IdleTimeout`: `int`




## CreateAccessPointOutputTypeDef

```python
from mypy_boto3_elb.type_defs import CreateAccessPointOutputTypeDef
```




Optional fields:
- `DNSName`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CrossZoneLoadBalancingTypeDef

```python
from mypy_boto3_elb.type_defs import CrossZoneLoadBalancingTypeDef
```


Required fields:
- `Enabled`: `bool`




## DeregisterEndPointsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DeregisterEndPointsOutputTypeDef
```




Optional fields:
- `Instances`: `List["InstanceTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAccessPointsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeAccessPointsOutputTypeDef
```




Optional fields:
- `LoadBalancerDescriptions`: `List["LoadBalancerDescriptionTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeAccountLimitsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeAccountLimitsOutputTypeDef
```




Optional fields:
- `Limits`: `List["LimitTypeDef"]`
- `NextMarker`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeEndPointStateOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeEndPointStateOutputTypeDef
```




Optional fields:
- `InstanceStates`: `List["InstanceStateTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeLoadBalancerAttributesOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeLoadBalancerAttributesOutputTypeDef
```




Optional fields:
- `LoadBalancerAttributes`: `"LoadBalancerAttributesTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeLoadBalancerPoliciesOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeLoadBalancerPoliciesOutputTypeDef
```




Optional fields:
- `PolicyDescriptions`: `List["PolicyDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeLoadBalancerPolicyTypesOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeLoadBalancerPolicyTypesOutputTypeDef
```




Optional fields:
- `PolicyTypeDescriptions`: `List["PolicyTypeDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTagsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DescribeTagsOutputTypeDef
```




Optional fields:
- `TagDescriptions`: `List["TagDescriptionTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DetachLoadBalancerFromSubnetsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import DetachLoadBalancerFromSubnetsOutputTypeDef
```




Optional fields:
- `Subnets`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## HealthCheckTypeDef

```python
from mypy_boto3_elb.type_defs import HealthCheckTypeDef
```


Required fields:
- `Target`: `str`
- `Interval`: `int`
- `Timeout`: `int`
- `UnhealthyThreshold`: `int`
- `HealthyThreshold`: `int`




## InstanceStateTypeDef

```python
from mypy_boto3_elb.type_defs import InstanceStateTypeDef
```




Optional fields:
- `InstanceId`: `str`
- `State`: `str`
- `ReasonCode`: `str`
- `Description`: `str`


## InstanceTypeDef

```python
from mypy_boto3_elb.type_defs import InstanceTypeDef
```




Optional fields:
- `InstanceId`: `str`


## LBCookieStickinessPolicyTypeDef

```python
from mypy_boto3_elb.type_defs import LBCookieStickinessPolicyTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `CookieExpirationPeriod`: `int`


## LimitTypeDef

```python
from mypy_boto3_elb.type_defs import LimitTypeDef
```




Optional fields:
- `Name`: `str`
- `Max`: `str`


## ListenerDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import ListenerDescriptionTypeDef
```




Optional fields:
- `Listener`: `"ListenerTypeDef"`
- `PolicyNames`: `List[str]`


## ListenerTypeDef

```python
from mypy_boto3_elb.type_defs import ListenerTypeDef
```


Required fields:
- `Protocol`: `str`
- `LoadBalancerPort`: `int`
- `InstancePort`: `int`



Optional fields:
- `InstanceProtocol`: `str`
- `SSLCertificateId`: `str`


## LoadBalancerAttributesTypeDef

```python
from mypy_boto3_elb.type_defs import LoadBalancerAttributesTypeDef
```




Optional fields:
- `CrossZoneLoadBalancing`: `"CrossZoneLoadBalancingTypeDef"`
- `AccessLog`: `"AccessLogTypeDef"`
- `ConnectionDraining`: `"ConnectionDrainingTypeDef"`
- `ConnectionSettings`: `"ConnectionSettingsTypeDef"`
- `AdditionalAttributes`: `List["AdditionalAttributeTypeDef"]`


## LoadBalancerDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import LoadBalancerDescriptionTypeDef
```




Optional fields:
- `LoadBalancerName`: `str`
- `DNSName`: `str`
- `CanonicalHostedZoneName`: `str`
- `CanonicalHostedZoneNameID`: `str`
- `ListenerDescriptions`: `List["ListenerDescriptionTypeDef"]`
- `Policies`: `"PoliciesTypeDef"`
- `BackendServerDescriptions`: `List["BackendServerDescriptionTypeDef"]`
- `AvailabilityZones`: `List[str]`
- `Subnets`: `List[str]`
- `VPCId`: `str`
- `Instances`: `List["InstanceTypeDef"]`
- `HealthCheck`: `"HealthCheckTypeDef"`
- `SourceSecurityGroup`: `"SourceSecurityGroupTypeDef"`
- `SecurityGroups`: `List[str]`
- `CreatedTime`: `datetime`
- `Scheme`: `str`


## ModifyLoadBalancerAttributesOutputTypeDef

```python
from mypy_boto3_elb.type_defs import ModifyLoadBalancerAttributesOutputTypeDef
```




Optional fields:
- `LoadBalancerName`: `str`
- `LoadBalancerAttributes`: `"LoadBalancerAttributesTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_elb.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PoliciesTypeDef

```python
from mypy_boto3_elb.type_defs import PoliciesTypeDef
```




Optional fields:
- `AppCookieStickinessPolicies`: `List["AppCookieStickinessPolicyTypeDef"]`
- `LBCookieStickinessPolicies`: `List["LBCookieStickinessPolicyTypeDef"]`
- `OtherPolicies`: `List[str]`


## PolicyAttributeDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import PolicyAttributeDescriptionTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValue`: `str`


## PolicyAttributeTypeDef

```python
from mypy_boto3_elb.type_defs import PolicyAttributeTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeValue`: `str`


## PolicyAttributeTypeDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import PolicyAttributeTypeDescriptionTypeDef
```




Optional fields:
- `AttributeName`: `str`
- `AttributeType`: `str`
- `Description`: `str`
- `DefaultValue`: `str`
- `Cardinality`: `str`


## PolicyDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import PolicyDescriptionTypeDef
```




Optional fields:
- `PolicyName`: `str`
- `PolicyTypeName`: `str`
- `PolicyAttributeDescriptions`: `List["PolicyAttributeDescriptionTypeDef"]`


## PolicyTypeDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import PolicyTypeDescriptionTypeDef
```




Optional fields:
- `PolicyTypeName`: `str`
- `Description`: `str`
- `PolicyAttributeTypeDescriptions`: `List["PolicyAttributeTypeDescriptionTypeDef"]`


## RegisterEndPointsOutputTypeDef

```python
from mypy_boto3_elb.type_defs import RegisterEndPointsOutputTypeDef
```




Optional fields:
- `Instances`: `List["InstanceTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## RemoveAvailabilityZonesOutputTypeDef

```python
from mypy_boto3_elb.type_defs import RemoveAvailabilityZonesOutputTypeDef
```




Optional fields:
- `AvailabilityZones`: `List[str]`
- `ResponseMetadata`: `"ResponseMetadata"`


## ResponseMetadata

```python
from mypy_boto3_elb.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SourceSecurityGroupTypeDef

```python
from mypy_boto3_elb.type_defs import SourceSecurityGroupTypeDef
```




Optional fields:
- `OwnerAlias`: `str`
- `GroupName`: `str`


## TagDescriptionTypeDef

```python
from mypy_boto3_elb.type_defs import TagDescriptionTypeDef
```




Optional fields:
- `LoadBalancerName`: `str`
- `Tags`: `List["TagTypeDef"]`


## TagKeyOnlyTypeDef

```python
from mypy_boto3_elb.type_defs import TagKeyOnlyTypeDef
```




Optional fields:
- `Key`: `str`


## TagTypeDef

```python
from mypy_boto3_elb.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`



Optional fields:
- `Value`: `str`


## WaiterConfigTypeDef

```python
from mypy_boto3_elb.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

