# Literals for boto3 AutoScaling module

> [Index](../index.md) > [AutoScaling](./index.md) > Literals

Auto-generated documentation for [AutoScaling](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html#AutoScaling)
type annotations stubs module [mypy_boto3_autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/).

- [Literals for boto3 AutoScaling module](#literals-for-boto3-autoscaling-module)
  - [DescribeAutoScalingGroupsPaginatorName](#describeautoscalinggroupspaginatorname)
  - [DescribeAutoScalingInstancesPaginatorName](#describeautoscalinginstancespaginatorname)
  - [DescribeLaunchConfigurationsPaginatorName](#describelaunchconfigurationspaginatorname)
  - [DescribeLoadBalancerTargetGroupsPaginatorName](#describeloadbalancertargetgroupspaginatorname)
  - [DescribeLoadBalancersPaginatorName](#describeloadbalancerspaginatorname)
  - [DescribeNotificationConfigurationsPaginatorName](#describenotificationconfigurationspaginatorname)
  - [DescribePoliciesPaginatorName](#describepoliciespaginatorname)
  - [DescribeScalingActivitiesPaginatorName](#describescalingactivitiespaginatorname)
  - [DescribeScheduledActionsPaginatorName](#describescheduledactionspaginatorname)
  - [DescribeTagsPaginatorName](#describetagspaginatorname)
  - [InstanceMetadataEndpointState](#instancemetadataendpointstate)
  - [InstanceMetadataHttpTokensState](#instancemetadatahttptokensstate)
  - [InstanceRefreshStatus](#instancerefreshstatus)
  - [LifecycleState](#lifecyclestate)
  - [MetricStatistic](#metricstatistic)
  - [MetricType](#metrictype)
  - [RefreshStrategy](#refreshstrategy)
  - [ScalingActivityStatusCode](#scalingactivitystatuscode)
  - [WarmPoolState](#warmpoolstate)
  - [WarmPoolStatus](#warmpoolstatus)

## DescribeAutoScalingGroupsPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeAutoScalingGroupsPaginatorName
```

Values:

- `describe_auto_scaling_groups`

## DescribeAutoScalingInstancesPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeAutoScalingInstancesPaginatorName
```

Values:

- `describe_auto_scaling_instances`

## DescribeLaunchConfigurationsPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeLaunchConfigurationsPaginatorName
```

Values:

- `describe_launch_configurations`

## DescribeLoadBalancerTargetGroupsPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeLoadBalancerTargetGroupsPaginatorName
```

Values:

- `describe_load_balancer_target_groups`

## DescribeLoadBalancersPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeLoadBalancersPaginatorName
```

Values:

- `describe_load_balancers`

## DescribeNotificationConfigurationsPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeNotificationConfigurationsPaginatorName
```

Values:

- `describe_notification_configurations`

## DescribePoliciesPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribePoliciesPaginatorName
```

Values:

- `describe_policies`

## DescribeScalingActivitiesPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeScalingActivitiesPaginatorName
```

Values:

- `describe_scaling_activities`

## DescribeScheduledActionsPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeScheduledActionsPaginatorName
```

Values:

- `describe_scheduled_actions`

## DescribeTagsPaginatorName

```python
from mypy_boto3_autoscaling.literals import DescribeTagsPaginatorName
```

Values:

- `describe_tags`

## InstanceMetadataEndpointState

```python
from mypy_boto3_autoscaling.literals import InstanceMetadataEndpointState
```

Values:

- `disabled`
- `enabled`

## InstanceMetadataHttpTokensState

```python
from mypy_boto3_autoscaling.literals import InstanceMetadataHttpTokensState
```

Values:

- `optional`
- `required`

## InstanceRefreshStatus

```python
from mypy_boto3_autoscaling.literals import InstanceRefreshStatus
```

Values:

- `Cancelled`
- `Cancelling`
- `Failed`
- `InProgress`
- `Pending`
- `Successful`

## LifecycleState

```python
from mypy_boto3_autoscaling.literals import LifecycleState
```

Values:

- `Detached`
- `Detaching`
- `EnteringStandby`
- `InService`
- `Pending`
- `Pending:Proceed`
- `Pending:Wait`
- `Quarantined`
- `Standby`
- `Terminated`
- `Terminating`
- `Terminating:Proceed`
- `Terminating:Wait`
- `Warmed:Pending`
- `Warmed:Pending:Proceed`
- `Warmed:Pending:Wait`
- `Warmed:Running`
- `Warmed:Stopped`
- `Warmed:Terminated`
- `Warmed:Terminating`
- `Warmed:Terminating:Proceed`
- `Warmed:Terminating:Wait`

## MetricStatistic

```python
from mypy_boto3_autoscaling.literals import MetricStatistic
```

Values:

- `Average`
- `Maximum`
- `Minimum`
- `SampleCount`
- `Sum`

## MetricType

```python
from mypy_boto3_autoscaling.literals import MetricType
```

Values:

- `ALBRequestCountPerTarget`
- `ASGAverageCPUUtilization`
- `ASGAverageNetworkIn`
- `ASGAverageNetworkOut`

## RefreshStrategy

```python
from mypy_boto3_autoscaling.literals import RefreshStrategy
```

Values:

- `Rolling`

## ScalingActivityStatusCode

```python
from mypy_boto3_autoscaling.literals import ScalingActivityStatusCode
```

Values:

- `Cancelled`
- `Failed`
- `InProgress`
- `MidLifecycleAction`
- `PendingSpotBidPlacement`
- `PreInService`
- `Successful`
- `WaitingForELBConnectionDraining`
- `WaitingForInstanceId`
- `WaitingForInstanceWarmup`
- `WaitingForSpotInstanceId`
- `WaitingForSpotInstanceRequestId`

## WarmPoolState

```python
from mypy_boto3_autoscaling.literals import WarmPoolState
```

Values:

- `Running`
- `Stopped`

## WarmPoolStatus

```python
from mypy_boto3_autoscaling.literals import WarmPoolStatus
```

Values:

- `PendingDelete`
