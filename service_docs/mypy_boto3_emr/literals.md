# Literals for boto3 EMR module

> [Index](../index.md) > [EMR](./index.md) > Literals

Auto-generated documentation for [EMR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR)
type annotations stubs module [mypy_boto3_emr](https://pypi.org/project/mypy-boto3-emr/).

- [Literals for boto3 EMR module](#literals-for-boto3-emr-module)
  - [ActionOnFailure](#actiononfailure)
  - [AdjustmentType](#adjustmenttype)
  - [AuthMode](#authmode)
  - [AutoScalingPolicyState](#autoscalingpolicystate)
  - [AutoScalingPolicyStateChangeReasonCode](#autoscalingpolicystatechangereasoncode)
  - [CancelStepsRequestStatus](#cancelstepsrequeststatus)
  - [ClusterRunningWaiterName](#clusterrunningwaitername)
  - [ClusterState](#clusterstate)
  - [ClusterStateChangeReasonCode](#clusterstatechangereasoncode)
  - [ClusterTerminatedWaiterName](#clusterterminatedwaitername)
  - [ComparisonOperator](#comparisonoperator)
  - [ComputeLimitsUnitType](#computelimitsunittype)
  - [ExecutionEngineType](#executionenginetype)
  - [IdentityType](#identitytype)
  - [InstanceCollectionType](#instancecollectiontype)
  - [InstanceFleetState](#instancefleetstate)
  - [InstanceFleetStateChangeReasonCode](#instancefleetstatechangereasoncode)
  - [InstanceFleetType](#instancefleettype)
  - [InstanceGroupState](#instancegroupstate)
  - [InstanceGroupStateChangeReasonCode](#instancegroupstatechangereasoncode)
  - [InstanceGroupType](#instancegrouptype)
  - [InstanceRoleType](#instanceroletype)
  - [InstanceState](#instancestate)
  - [InstanceStateChangeReasonCode](#instancestatechangereasoncode)
  - [JobFlowExecutionState](#jobflowexecutionstate)
  - [ListBootstrapActionsPaginatorName](#listbootstrapactionspaginatorname)
  - [ListClustersPaginatorName](#listclusterspaginatorname)
  - [ListInstanceFleetsPaginatorName](#listinstancefleetspaginatorname)
  - [ListInstanceGroupsPaginatorName](#listinstancegroupspaginatorname)
  - [ListInstancesPaginatorName](#listinstancespaginatorname)
  - [ListNotebookExecutionsPaginatorName](#listnotebookexecutionspaginatorname)
  - [ListSecurityConfigurationsPaginatorName](#listsecurityconfigurationspaginatorname)
  - [ListStepsPaginatorName](#liststepspaginatorname)
  - [ListStudioSessionMappingsPaginatorName](#liststudiosessionmappingspaginatorname)
  - [ListStudiosPaginatorName](#liststudiospaginatorname)
  - [MarketType](#markettype)
  - [NotebookExecutionStatus](#notebookexecutionstatus)
  - [OnDemandCapacityReservationPreference](#ondemandcapacityreservationpreference)
  - [OnDemandCapacityReservationUsageStrategy](#ondemandcapacityreservationusagestrategy)
  - [OnDemandProvisioningAllocationStrategy](#ondemandprovisioningallocationstrategy)
  - [PlacementGroupStrategy](#placementgroupstrategy)
  - [RepoUpgradeOnBoot](#repoupgradeonboot)
  - [ScaleDownBehavior](#scaledownbehavior)
  - [SpotProvisioningAllocationStrategy](#spotprovisioningallocationstrategy)
  - [SpotProvisioningTimeoutAction](#spotprovisioningtimeoutaction)
  - [Statistic](#statistic)
  - [StepCancellationOption](#stepcancellationoption)
  - [StepCompleteWaiterName](#stepcompletewaitername)
  - [StepExecutionState](#stepexecutionstate)
  - [StepState](#stepstate)
  - [StepStateChangeReasonCode](#stepstatechangereasoncode)
  - [Unit](#unit)

## ActionOnFailure

```python
from mypy_boto3_emr.literals import ActionOnFailure
```

Values:

- `CANCEL_AND_WAIT`
- `CONTINUE`
- `TERMINATE_CLUSTER`
- `TERMINATE_JOB_FLOW`

## AdjustmentType

```python
from mypy_boto3_emr.literals import AdjustmentType
```

Values:

- `CHANGE_IN_CAPACITY`
- `EXACT_CAPACITY`
- `PERCENT_CHANGE_IN_CAPACITY`

## AuthMode

```python
from mypy_boto3_emr.literals import AuthMode
```

Values:

- `IAM`
- `SSO`

## AutoScalingPolicyState

```python
from mypy_boto3_emr.literals import AutoScalingPolicyState
```

Values:

- `ATTACHED`
- `ATTACHING`
- `DETACHED`
- `DETACHING`
- `FAILED`
- `PENDING`

## AutoScalingPolicyStateChangeReasonCode

```python
from mypy_boto3_emr.literals import AutoScalingPolicyStateChangeReasonCode
```

Values:

- `CLEANUP_FAILURE`
- `PROVISION_FAILURE`
- `USER_REQUEST`

## CancelStepsRequestStatus

```python
from mypy_boto3_emr.literals import CancelStepsRequestStatus
```

Values:

- `FAILED`
- `SUBMITTED`

## ClusterRunningWaiterName

```python
from mypy_boto3_emr.literals import ClusterRunningWaiterName
```

Values:

- `cluster_running`

## ClusterState

```python
from mypy_boto3_emr.literals import ClusterState
```

Values:

- `BOOTSTRAPPING`
- `RUNNING`
- `STARTING`
- `TERMINATED`
- `TERMINATED_WITH_ERRORS`
- `TERMINATING`
- `WAITING`

## ClusterStateChangeReasonCode

```python
from mypy_boto3_emr.literals import ClusterStateChangeReasonCode
```

Values:

- `ALL_STEPS_COMPLETED`
- `BOOTSTRAP_FAILURE`
- `INSTANCE_FAILURE`
- `INSTANCE_FLEET_TIMEOUT`
- `INTERNAL_ERROR`
- `STEP_FAILURE`
- `USER_REQUEST`
- `VALIDATION_ERROR`

## ClusterTerminatedWaiterName

```python
from mypy_boto3_emr.literals import ClusterTerminatedWaiterName
```

Values:

- `cluster_terminated`

## ComparisonOperator

```python
from mypy_boto3_emr.literals import ComparisonOperator
```

Values:

- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL`

## ComputeLimitsUnitType

```python
from mypy_boto3_emr.literals import ComputeLimitsUnitType
```

Values:

- `InstanceFleetUnits`
- `Instances`
- `VCPU`

## ExecutionEngineType

```python
from mypy_boto3_emr.literals import ExecutionEngineType
```

Values:

- `EMR`

## IdentityType

```python
from mypy_boto3_emr.literals import IdentityType
```

Values:

- `GROUP`
- `USER`

## InstanceCollectionType

```python
from mypy_boto3_emr.literals import InstanceCollectionType
```

Values:

- `INSTANCE_FLEET`
- `INSTANCE_GROUP`

## InstanceFleetState

```python
from mypy_boto3_emr.literals import InstanceFleetState
```

Values:

- `BOOTSTRAPPING`
- `PROVISIONING`
- `RESIZING`
- `RUNNING`
- `SUSPENDED`
- `TERMINATED`
- `TERMINATING`

## InstanceFleetStateChangeReasonCode

```python
from mypy_boto3_emr.literals import InstanceFleetStateChangeReasonCode
```

Values:

- `CLUSTER_TERMINATED`
- `INSTANCE_FAILURE`
- `INTERNAL_ERROR`
- `VALIDATION_ERROR`

## InstanceFleetType

```python
from mypy_boto3_emr.literals import InstanceFleetType
```

Values:

- `CORE`
- `MASTER`
- `TASK`

## InstanceGroupState

```python
from mypy_boto3_emr.literals import InstanceGroupState
```

Values:

- `ARRESTED`
- `BOOTSTRAPPING`
- `ENDED`
- `PROVISIONING`
- `RECONFIGURING`
- `RESIZING`
- `RUNNING`
- `SHUTTING_DOWN`
- `SUSPENDED`
- `TERMINATED`
- `TERMINATING`

## InstanceGroupStateChangeReasonCode

```python
from mypy_boto3_emr.literals import InstanceGroupStateChangeReasonCode
```

Values:

- `CLUSTER_TERMINATED`
- `INSTANCE_FAILURE`
- `INTERNAL_ERROR`
- `VALIDATION_ERROR`

## InstanceGroupType

```python
from mypy_boto3_emr.literals import InstanceGroupType
```

Values:

- `CORE`
- `MASTER`
- `TASK`

## InstanceRoleType

```python
from mypy_boto3_emr.literals import InstanceRoleType
```

Values:

- `CORE`
- `MASTER`
- `TASK`

## InstanceState

```python
from mypy_boto3_emr.literals import InstanceState
```

Values:

- `AWAITING_FULFILLMENT`
- `BOOTSTRAPPING`
- `PROVISIONING`
- `RUNNING`
- `TERMINATED`

## InstanceStateChangeReasonCode

```python
from mypy_boto3_emr.literals import InstanceStateChangeReasonCode
```

Values:

- `BOOTSTRAP_FAILURE`
- `CLUSTER_TERMINATED`
- `INSTANCE_FAILURE`
- `INTERNAL_ERROR`
- `VALIDATION_ERROR`

## JobFlowExecutionState

```python
from mypy_boto3_emr.literals import JobFlowExecutionState
```

Values:

- `BOOTSTRAPPING`
- `COMPLETED`
- `FAILED`
- `RUNNING`
- `SHUTTING_DOWN`
- `STARTING`
- `TERMINATED`
- `WAITING`

## ListBootstrapActionsPaginatorName

```python
from mypy_boto3_emr.literals import ListBootstrapActionsPaginatorName
```

Values:

- `list_bootstrap_actions`

## ListClustersPaginatorName

```python
from mypy_boto3_emr.literals import ListClustersPaginatorName
```

Values:

- `list_clusters`

## ListInstanceFleetsPaginatorName

```python
from mypy_boto3_emr.literals import ListInstanceFleetsPaginatorName
```

Values:

- `list_instance_fleets`

## ListInstanceGroupsPaginatorName

```python
from mypy_boto3_emr.literals import ListInstanceGroupsPaginatorName
```

Values:

- `list_instance_groups`

## ListInstancesPaginatorName

```python
from mypy_boto3_emr.literals import ListInstancesPaginatorName
```

Values:

- `list_instances`

## ListNotebookExecutionsPaginatorName

```python
from mypy_boto3_emr.literals import ListNotebookExecutionsPaginatorName
```

Values:

- `list_notebook_executions`

## ListSecurityConfigurationsPaginatorName

```python
from mypy_boto3_emr.literals import ListSecurityConfigurationsPaginatorName
```

Values:

- `list_security_configurations`

## ListStepsPaginatorName

```python
from mypy_boto3_emr.literals import ListStepsPaginatorName
```

Values:

- `list_steps`

## ListStudioSessionMappingsPaginatorName

```python
from mypy_boto3_emr.literals import ListStudioSessionMappingsPaginatorName
```

Values:

- `list_studio_session_mappings`

## ListStudiosPaginatorName

```python
from mypy_boto3_emr.literals import ListStudiosPaginatorName
```

Values:

- `list_studios`

## MarketType

```python
from mypy_boto3_emr.literals import MarketType
```

Values:

- `ON_DEMAND`
- `SPOT`

## NotebookExecutionStatus

```python
from mypy_boto3_emr.literals import NotebookExecutionStatus
```

Values:

- `FAILED`
- `FAILING`
- `FINISHED`
- `FINISHING`
- `RUNNING`
- `START_PENDING`
- `STARTING`
- `STOP_PENDING`
- `STOPPED`
- `STOPPING`

## OnDemandCapacityReservationPreference

```python
from mypy_boto3_emr.literals import OnDemandCapacityReservationPreference
```

Values:

- `none`
- `open`

## OnDemandCapacityReservationUsageStrategy

```python
from mypy_boto3_emr.literals import OnDemandCapacityReservationUsageStrategy
```

Values:

- `use-capacity-reservations-first`

## OnDemandProvisioningAllocationStrategy

```python
from mypy_boto3_emr.literals import OnDemandProvisioningAllocationStrategy
```

Values:

- `lowest-price`

## PlacementGroupStrategy

```python
from mypy_boto3_emr.literals import PlacementGroupStrategy
```

Values:

- `CLUSTER`
- `NONE`
- `PARTITION`
- `SPREAD`

## RepoUpgradeOnBoot

```python
from mypy_boto3_emr.literals import RepoUpgradeOnBoot
```

Values:

- `NONE`
- `SECURITY`

## ScaleDownBehavior

```python
from mypy_boto3_emr.literals import ScaleDownBehavior
```

Values:

- `TERMINATE_AT_INSTANCE_HOUR`
- `TERMINATE_AT_TASK_COMPLETION`

## SpotProvisioningAllocationStrategy

```python
from mypy_boto3_emr.literals import SpotProvisioningAllocationStrategy
```

Values:

- `capacity-optimized`

## SpotProvisioningTimeoutAction

```python
from mypy_boto3_emr.literals import SpotProvisioningTimeoutAction
```

Values:

- `SWITCH_TO_ON_DEMAND`
- `TERMINATE_CLUSTER`

## Statistic

```python
from mypy_boto3_emr.literals import Statistic
```

Values:

- `AVERAGE`
- `MAXIMUM`
- `MINIMUM`
- `SAMPLE_COUNT`
- `SUM`

## StepCancellationOption

```python
from mypy_boto3_emr.literals import StepCancellationOption
```

Values:

- `SEND_INTERRUPT`
- `TERMINATE_PROCESS`

## StepCompleteWaiterName

```python
from mypy_boto3_emr.literals import StepCompleteWaiterName
```

Values:

- `step_complete`

## StepExecutionState

```python
from mypy_boto3_emr.literals import StepExecutionState
```

Values:

- `CANCELLED`
- `COMPLETED`
- `CONTINUE`
- `FAILED`
- `INTERRUPTED`
- `PENDING`
- `RUNNING`

## StepState

```python
from mypy_boto3_emr.literals import StepState
```

Values:

- `CANCEL_PENDING`
- `CANCELLED`
- `COMPLETED`
- `FAILED`
- `INTERRUPTED`
- `PENDING`
- `RUNNING`

## StepStateChangeReasonCode

```python
from mypy_boto3_emr.literals import StepStateChangeReasonCode
```

Values:

- `NONE`

## Unit

```python
from mypy_boto3_emr.literals import Unit
```

Values:

- `BITS`
- `BITS_PER_SECOND`
- `BYTES`
- `BYTES_PER_SECOND`
- `COUNT`
- `COUNT_PER_SECOND`
- `GIGA_BITS`
- `GIGA_BITS_PER_SECOND`
- `GIGA_BYTES`
- `GIGA_BYTES_PER_SECOND`
- `KILO_BITS`
- `KILO_BITS_PER_SECOND`
- `KILO_BYTES`
- `KILO_BYTES_PER_SECOND`
- `MEGA_BITS`
- `MEGA_BITS_PER_SECOND`
- `MEGA_BYTES`
- `MEGA_BYTES_PER_SECOND`
- `MICRO_SECONDS`
- `MILLI_SECONDS`
- `NONE`
- `PERCENT`
- `SECONDS`
- `TERA_BITS`
- `TERA_BITS_PER_SECOND`
- `TERA_BYTES`
- `TERA_BYTES_PER_SECOND`
