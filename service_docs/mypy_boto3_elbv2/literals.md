# Literals for boto3 ElasticLoadBalancingv2 module

> [Index](../index.md) > [ElasticLoadBalancingv2](./index.md) > Literals

Auto-generated documentation for [ElasticLoadBalancingv2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2)
type annotations stubs module [mypy_boto3_elbv2](https://pypi.org/project/mypy-boto3-elbv2/).

- [Literals for boto3 ElasticLoadBalancingv2 module](#literals-for-boto3-elasticloadbalancingv2-module)
  - [ActionTypeEnum](#actiontypeenum)
  - [AuthenticateCognitoActionConditionalBehaviorEnum](#authenticatecognitoactionconditionalbehaviorenum)
  - [AuthenticateOidcActionConditionalBehaviorEnum](#authenticateoidcactionconditionalbehaviorenum)
  - [DescribeAccountLimitsPaginatorName](#describeaccountlimitspaginatorname)
  - [DescribeListenerCertificatesPaginatorName](#describelistenercertificatespaginatorname)
  - [DescribeListenersPaginatorName](#describelistenerspaginatorname)
  - [DescribeLoadBalancersPaginatorName](#describeloadbalancerspaginatorname)
  - [DescribeRulesPaginatorName](#describerulespaginatorname)
  - [DescribeSSLPoliciesPaginatorName](#describesslpoliciespaginatorname)
  - [DescribeTargetGroupsPaginatorName](#describetargetgroupspaginatorname)
  - [IpAddressType](#ipaddresstype)
  - [LoadBalancerAvailableWaiterName](#loadbalanceravailablewaitername)
  - [LoadBalancerExistsWaiterName](#loadbalancerexistswaitername)
  - [LoadBalancerSchemeEnum](#loadbalancerschemeenum)
  - [LoadBalancerStateEnum](#loadbalancerstateenum)
  - [LoadBalancerTypeEnum](#loadbalancertypeenum)
  - [LoadBalancersDeletedWaiterName](#loadbalancersdeletedwaitername)
  - [ProtocolEnum](#protocolenum)
  - [RedirectActionStatusCodeEnum](#redirectactionstatuscodeenum)
  - [TargetDeregisteredWaiterName](#targetderegisteredwaitername)
  - [TargetHealthReasonEnum](#targethealthreasonenum)
  - [TargetHealthStateEnum](#targethealthstateenum)
  - [TargetInServiceWaiterName](#targetinservicewaitername)
  - [TargetTypeEnum](#targettypeenum)

## ActionTypeEnum

```python
from mypy_boto3_elbv2.literals import ActionTypeEnum
```

Values:

- `authenticate-cognito`
- `authenticate-oidc`
- `fixed-response`
- `forward`
- `redirect`

## AuthenticateCognitoActionConditionalBehaviorEnum

```python
from mypy_boto3_elbv2.literals import AuthenticateCognitoActionConditionalBehaviorEnum
```

Values:

- `allow`
- `authenticate`
- `deny`

## AuthenticateOidcActionConditionalBehaviorEnum

```python
from mypy_boto3_elbv2.literals import AuthenticateOidcActionConditionalBehaviorEnum
```

Values:

- `allow`
- `authenticate`
- `deny`

## DescribeAccountLimitsPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeAccountLimitsPaginatorName
```

Values:

- `describe_account_limits`

## DescribeListenerCertificatesPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeListenerCertificatesPaginatorName
```

Values:

- `describe_listener_certificates`

## DescribeListenersPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeListenersPaginatorName
```

Values:

- `describe_listeners`

## DescribeLoadBalancersPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeLoadBalancersPaginatorName
```

Values:

- `describe_load_balancers`

## DescribeRulesPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeRulesPaginatorName
```

Values:

- `describe_rules`

## DescribeSSLPoliciesPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeSSLPoliciesPaginatorName
```

Values:

- `describe_ssl_policies`

## DescribeTargetGroupsPaginatorName

```python
from mypy_boto3_elbv2.literals import DescribeTargetGroupsPaginatorName
```

Values:

- `describe_target_groups`

## IpAddressType

```python
from mypy_boto3_elbv2.literals import IpAddressType
```

Values:

- `dualstack`
- `ipv4`

## LoadBalancerAvailableWaiterName

```python
from mypy_boto3_elbv2.literals import LoadBalancerAvailableWaiterName
```

Values:

- `load_balancer_available`

## LoadBalancerExistsWaiterName

```python
from mypy_boto3_elbv2.literals import LoadBalancerExistsWaiterName
```

Values:

- `load_balancer_exists`

## LoadBalancerSchemeEnum

```python
from mypy_boto3_elbv2.literals import LoadBalancerSchemeEnum
```

Values:

- `internal`
- `internet-facing`

## LoadBalancerStateEnum

```python
from mypy_boto3_elbv2.literals import LoadBalancerStateEnum
```

Values:

- `active`
- `active_impaired`
- `failed`
- `provisioning`

## LoadBalancerTypeEnum

```python
from mypy_boto3_elbv2.literals import LoadBalancerTypeEnum
```

Values:

- `application`
- `gateway`
- `network`

## LoadBalancersDeletedWaiterName

```python
from mypy_boto3_elbv2.literals import LoadBalancersDeletedWaiterName
```

Values:

- `load_balancers_deleted`

## ProtocolEnum

```python
from mypy_boto3_elbv2.literals import ProtocolEnum
```

Values:

- `GENEVE`
- `HTTP`
- `HTTPS`
- `TCP`
- `TCP_UDP`
- `TLS`
- `UDP`

## RedirectActionStatusCodeEnum

```python
from mypy_boto3_elbv2.literals import RedirectActionStatusCodeEnum
```

Values:

- `HTTP_301`
- `HTTP_302`

## TargetDeregisteredWaiterName

```python
from mypy_boto3_elbv2.literals import TargetDeregisteredWaiterName
```

Values:

- `target_deregistered`

## TargetHealthReasonEnum

```python
from mypy_boto3_elbv2.literals import TargetHealthReasonEnum
```

Values:

- `Elb.InitialHealthChecking`
- `Elb.InternalError`
- `Elb.RegistrationInProgress`
- `Target.DeregistrationInProgress`
- `Target.FailedHealthChecks`
- `Target.HealthCheckDisabled`
- `Target.InvalidState`
- `Target.IpUnusable`
- `Target.NotInUse`
- `Target.NotRegistered`
- `Target.ResponseCodeMismatch`
- `Target.Timeout`

## TargetHealthStateEnum

```python
from mypy_boto3_elbv2.literals import TargetHealthStateEnum
```

Values:

- `draining`
- `healthy`
- `initial`
- `unavailable`
- `unhealthy`
- `unused`

## TargetInServiceWaiterName

```python
from mypy_boto3_elbv2.literals import TargetInServiceWaiterName
```

Values:

- `target_in_service`

## TargetTypeEnum

```python
from mypy_boto3_elbv2.literals import TargetTypeEnum
```

Values:

- `instance`
- `ip`
- `lambda`
