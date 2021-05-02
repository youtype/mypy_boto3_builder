# Paginators for boto3 SSM module

> [Index](../index.md) > [SSM](./index.md) > Paginators

Auto-generated documentation for [SSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM)
type annotations stubs module [mypy_boto3_ssm](https://pypi.org/project/mypy-boto3-ssm/).

- [Paginators for boto3 SSM module](#paginators-for-boto3-ssm-module)
  - [DescribeActivationsPaginator](#describeactivationspaginator)
  - [DescribeAssociationExecutionTargetsPaginator](#describeassociationexecutiontargetspaginator)
  - [DescribeAssociationExecutionsPaginator](#describeassociationexecutionspaginator)
  - [DescribeAutomationExecutionsPaginator](#describeautomationexecutionspaginator)
  - [DescribeAutomationStepExecutionsPaginator](#describeautomationstepexecutionspaginator)
  - [DescribeAvailablePatchesPaginator](#describeavailablepatchespaginator)
  - [DescribeEffectiveInstanceAssociationsPaginator](#describeeffectiveinstanceassociationspaginator)
  - [DescribeEffectivePatchesForPatchBaselinePaginator](#describeeffectivepatchesforpatchbaselinepaginator)
  - [DescribeInstanceAssociationsStatusPaginator](#describeinstanceassociationsstatuspaginator)
  - [DescribeInstanceInformationPaginator](#describeinstanceinformationpaginator)
  - [DescribeInstancePatchStatesPaginator](#describeinstancepatchstatespaginator)
  - [DescribeInstancePatchStatesForPatchGroupPaginator](#describeinstancepatchstatesforpatchgrouppaginator)
  - [DescribeInstancePatchesPaginator](#describeinstancepatchespaginator)
  - [DescribeInventoryDeletionsPaginator](#describeinventorydeletionspaginator)
  - [DescribeMaintenanceWindowExecutionTaskInvocationsPaginator](#describemaintenancewindowexecutiontaskinvocationspaginator)
  - [DescribeMaintenanceWindowExecutionTasksPaginator](#describemaintenancewindowexecutiontaskspaginator)
  - [DescribeMaintenanceWindowExecutionsPaginator](#describemaintenancewindowexecutionspaginator)
  - [DescribeMaintenanceWindowSchedulePaginator](#describemaintenancewindowschedulepaginator)
  - [DescribeMaintenanceWindowTargetsPaginator](#describemaintenancewindowtargetspaginator)
  - [DescribeMaintenanceWindowTasksPaginator](#describemaintenancewindowtaskspaginator)
  - [DescribeMaintenanceWindowsPaginator](#describemaintenancewindowspaginator)
  - [DescribeMaintenanceWindowsForTargetPaginator](#describemaintenancewindowsfortargetpaginator)
  - [DescribeOpsItemsPaginator](#describeopsitemspaginator)
  - [DescribeParametersPaginator](#describeparameterspaginator)
  - [DescribePatchBaselinesPaginator](#describepatchbaselinespaginator)
  - [DescribePatchGroupsPaginator](#describepatchgroupspaginator)
  - [DescribePatchPropertiesPaginator](#describepatchpropertiespaginator)
  - [DescribeSessionsPaginator](#describesessionspaginator)
  - [GetInventoryPaginator](#getinventorypaginator)
  - [GetInventorySchemaPaginator](#getinventoryschemapaginator)
  - [GetOpsSummaryPaginator](#getopssummarypaginator)
  - [GetParameterHistoryPaginator](#getparameterhistorypaginator)
  - [GetParametersByPathPaginator](#getparametersbypathpaginator)
  - [ListAssociationVersionsPaginator](#listassociationversionspaginator)
  - [ListAssociationsPaginator](#listassociationspaginator)
  - [ListCommandInvocationsPaginator](#listcommandinvocationspaginator)
  - [ListCommandsPaginator](#listcommandspaginator)
  - [ListComplianceItemsPaginator](#listcomplianceitemspaginator)
  - [ListComplianceSummariesPaginator](#listcompliancesummariespaginator)
  - [ListDocumentVersionsPaginator](#listdocumentversionspaginator)
  - [ListDocumentsPaginator](#listdocumentspaginator)
  - [ListOpsItemEventsPaginator](#listopsitemeventspaginator)
  - [ListOpsMetadataPaginator](#listopsmetadatapaginator)
  - [ListResourceComplianceSummariesPaginator](#listresourcecompliancesummariespaginator)
  - [ListResourceDataSyncPaginator](#listresourcedatasyncpaginator)

## DescribeActivationsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_activations")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeActivationsPaginator

def get_describe_activations_paginator() -> DescribeActivationsPaginator:
    return boto3.client("ssm").get_paginator("describe_activations")
```

[Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeActivations)

```python
class DescribeActivationsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[DescribeActivationsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeActivationsResultTypeDef]:
        pass
```
## DescribeAssociationExecutionTargetsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_association_execution_targets")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeAssociationExecutionTargetsPaginator

def get_describe_association_execution_targets_paginator() -> DescribeAssociationExecutionTargetsPaginator:
    return boto3.client("ssm").get_paginator("describe_association_execution_targets")
```

[Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)

```python
class DescribeAssociationExecutionTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[AssociationExecutionTargetsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAssociationExecutionTargetsResultTypeDef]:
        pass
```
## DescribeAssociationExecutionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_association_executions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeAssociationExecutionsPaginator

def get_describe_association_executions_paginator() -> DescribeAssociationExecutionsPaginator:
    return boto3.client("ssm").get_paginator("describe_association_executions")
```

[Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)

```python
class DescribeAssociationExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AssociationId: str,
        Filters: List[AssociationExecutionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAssociationExecutionsResultTypeDef]:
        pass
```
## DescribeAutomationExecutionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_automation_executions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeAutomationExecutionsPaginator

def get_describe_automation_executions_paginator() -> DescribeAutomationExecutionsPaginator:
    return boto3.client("ssm").get_paginator("describe_automation_executions")
```

[Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)

```python
class DescribeAutomationExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[AutomationExecutionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAutomationExecutionsResultTypeDef]:
        pass
```
## DescribeAutomationStepExecutionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_automation_step_executions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeAutomationStepExecutionsPaginator

def get_describe_automation_step_executions_paginator() -> DescribeAutomationStepExecutionsPaginator:
    return boto3.client("ssm").get_paginator("describe_automation_step_executions")
```

[Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)

```python
class DescribeAutomationStepExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AutomationExecutionId: str,
        Filters: List[StepExecutionFilterTypeDef] = None,
        ReverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAutomationStepExecutionsResultTypeDef]:
        pass
```
## DescribeAvailablePatchesPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_available_patches")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeAvailablePatchesPaginator

def get_describe_available_patches_paginator() -> DescribeAvailablePatchesPaginator:
    return boto3.client("ssm").get_paginator("describe_available_patches")
```

[Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)

```python
class DescribeAvailablePatchesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAvailablePatchesResultTypeDef]:
        pass
```
## DescribeEffectiveInstanceAssociationsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_effective_instance_associations")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeEffectiveInstanceAssociationsPaginator

def get_describe_effective_instance_associations_paginator() -> DescribeEffectiveInstanceAssociationsPaginator:
    return boto3.client("ssm").get_paginator("describe_effective_instance_associations")
```

[Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)

```python
class DescribeEffectiveInstanceAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEffectiveInstanceAssociationsResultTypeDef]:
        pass
```
## DescribeEffectivePatchesForPatchBaselinePaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_effective_patches_for_patch_baseline")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeEffectivePatchesForPatchBaselinePaginator

def get_describe_effective_patches_for_patch_baseline_paginator() -> DescribeEffectivePatchesForPatchBaselinePaginator:
    return boto3.client("ssm").get_paginator("describe_effective_patches_for_patch_baseline")
```

[Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)

```python
class DescribeEffectivePatchesForPatchBaselinePaginator(Boto3Paginator):
    def paginate(
        self,
        BaselineId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEffectivePatchesForPatchBaselineResultTypeDef]:
        pass
```
## DescribeInstanceAssociationsStatusPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_instance_associations_status")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeInstanceAssociationsStatusPaginator

def get_describe_instance_associations_status_paginator() -> DescribeInstanceAssociationsStatusPaginator:
    return boto3.client("ssm").get_paginator("describe_instance_associations_status")
```

[Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)

```python
class DescribeInstanceAssociationsStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceAssociationsStatusResultTypeDef]:
        pass
```
## DescribeInstanceInformationPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_instance_information")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeInstanceInformationPaginator

def get_describe_instance_information_paginator() -> DescribeInstanceInformationPaginator:
    return boto3.client("ssm").get_paginator("describe_instance_information")
```

[Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)

```python
class DescribeInstanceInformationPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceInformationFilterList: List[InstanceInformationFilterTypeDef] = None,
        Filters: List[InstanceInformationStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceInformationResultTypeDef]:
        pass
```
## DescribeInstancePatchStatesPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_instance_patch_states")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeInstancePatchStatesPaginator

def get_describe_instance_patch_states_paginator() -> DescribeInstancePatchStatesPaginator:
    return boto3.client("ssm").get_paginator("describe_instance_patch_states")
```

[Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)

```python
class DescribeInstancePatchStatesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceIds: List[str],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchStatesResultTypeDef]:
        pass
```
## DescribeInstancePatchStatesForPatchGroupPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_instance_patch_states_for_patch_group")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeInstancePatchStatesForPatchGroupPaginator

def get_describe_instance_patch_states_for_patch_group_paginator() -> DescribeInstancePatchStatesForPatchGroupPaginator:
    return boto3.client("ssm").get_paginator("describe_instance_patch_states_for_patch_group")
```

[Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)

```python
class DescribeInstancePatchStatesForPatchGroupPaginator(Boto3Paginator):
    def paginate(
        self,
        PatchGroup: str,
        Filters: List[InstancePatchStateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchStatesForPatchGroupResultTypeDef]:
        pass
```
## DescribeInstancePatchesPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_instance_patches")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeInstancePatchesPaginator

def get_describe_instance_patches_paginator() -> DescribeInstancePatchesPaginator:
    return boto3.client("ssm").get_paginator("describe_instance_patches")
```

[Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)

```python
class DescribeInstancePatchesPaginator(Boto3Paginator):
    def paginate(
        self,
        InstanceId: str,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchesResultTypeDef]:
        pass
```
## DescribeInventoryDeletionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_inventory_deletions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeInventoryDeletionsPaginator

def get_describe_inventory_deletions_paginator() -> DescribeInventoryDeletionsPaginator:
    return boto3.client("ssm").get_paginator("describe_inventory_deletions")
```

[Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)

```python
class DescribeInventoryDeletionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DeletionId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInventoryDeletionsResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowExecutionTaskInvocationsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_window_execution_task_invocations")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowExecutionTaskInvocationsPaginator

def get_describe_maintenance_window_execution_task_invocations_paginator() -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_window_execution_task_invocations")
```

[Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)

```python
class DescribeMaintenanceWindowExecutionTaskInvocationsPaginator(Boto3Paginator):
    def paginate(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowExecutionTasksPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_window_execution_tasks")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowExecutionTasksPaginator

def get_describe_maintenance_window_execution_tasks_paginator() -> DescribeMaintenanceWindowExecutionTasksPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_window_execution_tasks")
```

[Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)

```python
class DescribeMaintenanceWindowExecutionTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        WindowExecutionId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowExecutionTasksResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowExecutionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_window_executions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowExecutionsPaginator

def get_describe_maintenance_window_executions_paginator() -> DescribeMaintenanceWindowExecutionsPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_window_executions")
```

[Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)

```python
class DescribeMaintenanceWindowExecutionsPaginator(Boto3Paginator):
    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowExecutionsResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowSchedulePaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_window_schedule")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowSchedulePaginator

def get_describe_maintenance_window_schedule_paginator() -> DescribeMaintenanceWindowSchedulePaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_window_schedule")
```

[Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)

```python
class DescribeMaintenanceWindowSchedulePaginator(Boto3Paginator):
    def paginate(
        self,
        WindowId: str = None,
        Targets: List["TargetTypeDef"] = None,
        ResourceType: MaintenanceWindowResourceType = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowScheduleResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowTargetsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_window_targets")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowTargetsPaginator

def get_describe_maintenance_window_targets_paginator() -> DescribeMaintenanceWindowTargetsPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_window_targets")
```

[Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)

```python
class DescribeMaintenanceWindowTargetsPaginator(Boto3Paginator):
    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowTargetsResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowTasksPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_window_tasks")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowTasksPaginator

def get_describe_maintenance_window_tasks_paginator() -> DescribeMaintenanceWindowTasksPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_window_tasks")
```

[Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)

```python
class DescribeMaintenanceWindowTasksPaginator(Boto3Paginator):
    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowTasksResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_windows")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowsPaginator

def get_describe_maintenance_windows_paginator() -> DescribeMaintenanceWindowsPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_windows")
```

[Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)

```python
class DescribeMaintenanceWindowsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowsResultTypeDef]:
        pass
```
## DescribeMaintenanceWindowsForTargetPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_maintenance_windows_for_target")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeMaintenanceWindowsForTargetPaginator

def get_describe_maintenance_windows_for_target_paginator() -> DescribeMaintenanceWindowsForTargetPaginator:
    return boto3.client("ssm").get_paginator("describe_maintenance_windows_for_target")
```

[Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)

```python
class DescribeMaintenanceWindowsForTargetPaginator(Boto3Paginator):
    def paginate(
        self,
        Targets: List["TargetTypeDef"],
        ResourceType: MaintenanceWindowResourceType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowsForTargetResultTypeDef]:
        pass
```
## DescribeOpsItemsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_ops_items")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeOpsItemsPaginator

def get_describe_ops_items_paginator() -> DescribeOpsItemsPaginator:
    return boto3.client("ssm").get_paginator("describe_ops_items")
```

[Paginator.DescribeOpsItems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems)

```python
class DescribeOpsItemsPaginator(Boto3Paginator):
    def paginate(
        self,
        OpsItemFilters: List[OpsItemFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOpsItemsResponseTypeDef]:
        pass
```
## DescribeParametersPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_parameters")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeParametersPaginator

def get_describe_parameters_paginator() -> DescribeParametersPaginator:
    return boto3.client("ssm").get_paginator("describe_parameters")
```

[Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeParameters)

```python
class DescribeParametersPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ParametersFilterTypeDef] = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParametersResultTypeDef]:
        pass
```
## DescribePatchBaselinesPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_patch_baselines")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribePatchBaselinesPaginator

def get_describe_patch_baselines_paginator() -> DescribePatchBaselinesPaginator:
    return boto3.client("ssm").get_paginator("describe_patch_baselines")
```

[Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)

```python
class DescribePatchBaselinesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePatchBaselinesResultTypeDef]:
        pass
```
## DescribePatchGroupsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_patch_groups")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribePatchGroupsPaginator

def get_describe_patch_groups_paginator() -> DescribePatchGroupsPaginator:
    return boto3.client("ssm").get_paginator("describe_patch_groups")
```

[Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)

```python
class DescribePatchGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePatchGroupsResultTypeDef]:
        pass
```
## DescribePatchPropertiesPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_patch_properties")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribePatchPropertiesPaginator

def get_describe_patch_properties_paginator() -> DescribePatchPropertiesPaginator:
    return boto3.client("ssm").get_paginator("describe_patch_properties")
```

[Paginator.DescribePatchProperties documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties)

```python
class DescribePatchPropertiesPaginator(Boto3Paginator):
    def paginate(
        self,
        OperatingSystem: OperatingSystem,
        Property: PatchProperty,
        PatchSet: PatchSet = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePatchPropertiesResultTypeDef]:
        pass
```
## DescribeSessionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("describe_sessions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import DescribeSessionsPaginator

def get_describe_sessions_paginator() -> DescribeSessionsPaginator:
    return boto3.client("ssm").get_paginator("describe_sessions")
```

[Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.DescribeSessions)

```python
class DescribeSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        State: SessionState,
        Filters: List[SessionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSessionsResponseTypeDef]:
        pass
```
## GetInventoryPaginator

Type annotations for `boto3.client("ssm").get_paginator("get_inventory")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import GetInventoryPaginator

def get_get_inventory_paginator() -> GetInventoryPaginator:
    return boto3.client("ssm").get_paginator("get_inventory")
```

[Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetInventory)

```python
class GetInventoryPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List["InventoryFilterTypeDef"] = None,
        Aggregators: List[Dict[str, Any]] = None,
        ResultAttributes: List[ResultAttributeTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInventoryResultTypeDef]:
        pass
```
## GetInventorySchemaPaginator

Type annotations for `boto3.client("ssm").get_paginator("get_inventory_schema")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import GetInventorySchemaPaginator

def get_get_inventory_schema_paginator() -> GetInventorySchemaPaginator:
    return boto3.client("ssm").get_paginator("get_inventory_schema")
```

[Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)

```python
class GetInventorySchemaPaginator(Boto3Paginator):
    def paginate(
        self,
        TypeName: str = None,
        Aggregator: bool = None,
        SubType: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInventorySchemaResultTypeDef]:
        pass
```
## GetOpsSummaryPaginator

Type annotations for `boto3.client("ssm").get_paginator("get_ops_summary")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import GetOpsSummaryPaginator

def get_get_ops_summary_paginator() -> GetOpsSummaryPaginator:
    return boto3.client("ssm").get_paginator("get_ops_summary")
```

[Paginator.GetOpsSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetOpsSummary)

```python
class GetOpsSummaryPaginator(Boto3Paginator):
    def paginate(
        self,
        SyncName: str = None,
        Filters: List["OpsFilterTypeDef"] = None,
        Aggregators: List[Dict[str, Any]] = None,
        ResultAttributes: List[OpsResultAttributeTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOpsSummaryResultTypeDef]:
        pass
```
## GetParameterHistoryPaginator

Type annotations for `boto3.client("ssm").get_paginator("get_parameter_history")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import GetParameterHistoryPaginator

def get_get_parameter_history_paginator() -> GetParameterHistoryPaginator:
    return boto3.client("ssm").get_paginator("get_parameter_history")
```

[Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)

```python
class GetParameterHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        Name: str,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetParameterHistoryResultTypeDef]:
        pass
```
## GetParametersByPathPaginator

Type annotations for `boto3.client("ssm").get_paginator("get_parameters_by_path")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import GetParametersByPathPaginator

def get_get_parameters_by_path_paginator() -> GetParametersByPathPaginator:
    return boto3.client("ssm").get_paginator("get_parameters_by_path")
```

[Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)

```python
class GetParametersByPathPaginator(Boto3Paginator):
    def paginate(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetParametersByPathResultTypeDef]:
        pass
```
## ListAssociationVersionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_association_versions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListAssociationVersionsPaginator

def get_list_association_versions_paginator() -> ListAssociationVersionsPaginator:
    return boto3.client("ssm").get_paginator("list_association_versions")
```

[Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)

```python
class ListAssociationVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        AssociationId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationVersionsResultTypeDef]:
        pass
```
## ListAssociationsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_associations")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListAssociationsPaginator

def get_list_associations_paginator() -> ListAssociationsPaginator:
    return boto3.client("ssm").get_paginator("list_associations")
```

[Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListAssociations)

```python
class ListAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        AssociationFilterList: List[AssociationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationsResultTypeDef]:
        pass
```
## ListCommandInvocationsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_command_invocations")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListCommandInvocationsPaginator

def get_list_command_invocations_paginator() -> ListCommandInvocationsPaginator:
    return boto3.client("ssm").get_paginator("list_command_invocations")
```

[Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)

```python
class ListCommandInvocationsPaginator(Boto3Paginator):
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        Details: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCommandInvocationsResultTypeDef]:
        pass
```
## ListCommandsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_commands")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListCommandsPaginator

def get_list_commands_paginator() -> ListCommandsPaginator:
    return boto3.client("ssm").get_paginator("list_commands")
```

[Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListCommands)

```python
class ListCommandsPaginator(Boto3Paginator):
    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCommandsResultTypeDef]:
        pass
```
## ListComplianceItemsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_compliance_items")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListComplianceItemsPaginator

def get_list_compliance_items_paginator() -> ListComplianceItemsPaginator:
    return boto3.client("ssm").get_paginator("list_compliance_items")
```

[Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)

```python
class ListComplianceItemsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComplianceItemsResultTypeDef]:
        pass
```
## ListComplianceSummariesPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_compliance_summaries")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListComplianceSummariesPaginator

def get_list_compliance_summaries_paginator() -> ListComplianceSummariesPaginator:
    return boto3.client("ssm").get_paginator("list_compliance_summaries")
```

[Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)

```python
class ListComplianceSummariesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComplianceSummariesResultTypeDef]:
        pass
```
## ListDocumentVersionsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_document_versions")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListDocumentVersionsPaginator

def get_list_document_versions_paginator() -> ListDocumentVersionsPaginator:
    return boto3.client("ssm").get_paginator("list_document_versions")
```

[Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)

```python
class ListDocumentVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Name: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentVersionsResultTypeDef]:
        pass
```
## ListDocumentsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_documents")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListDocumentsPaginator

def get_list_documents_paginator() -> ListDocumentsPaginator:
    return boto3.client("ssm").get_paginator("list_documents")
```

[Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListDocuments)

```python
class ListDocumentsPaginator(Boto3Paginator):
    def paginate(
        self,
        DocumentFilterList: List[DocumentFilterTypeDef] = None,
        Filters: List[DocumentKeyValuesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentsResultTypeDef]:
        pass
```
## ListOpsItemEventsPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_ops_item_events")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListOpsItemEventsPaginator

def get_list_ops_item_events_paginator() -> ListOpsItemEventsPaginator:
    return boto3.client("ssm").get_paginator("list_ops_item_events")
```

[Paginator.ListOpsItemEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListOpsItemEvents)

```python
class ListOpsItemEventsPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[OpsItemEventFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOpsItemEventsResponseTypeDef]:
        pass
```
## ListOpsMetadataPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_ops_metadata")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListOpsMetadataPaginator

def get_list_ops_metadata_paginator() -> ListOpsMetadataPaginator:
    return boto3.client("ssm").get_paginator("list_ops_metadata")
```

[Paginator.ListOpsMetadata documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListOpsMetadata)

```python
class ListOpsMetadataPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[OpsMetadataFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOpsMetadataResultTypeDef]:
        pass
```
## ListResourceComplianceSummariesPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_resource_compliance_summaries")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListResourceComplianceSummariesPaginator

def get_list_resource_compliance_summaries_paginator() -> ListResourceComplianceSummariesPaginator:
    return boto3.client("ssm").get_paginator("list_resource_compliance_summaries")
```

[Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)

```python
class ListResourceComplianceSummariesPaginator(Boto3Paginator):
    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceComplianceSummariesResultTypeDef]:
        pass
```
## ListResourceDataSyncPaginator

Type annotations for `boto3.client("ssm").get_paginator("list_resource_data_sync")`.

Can be used directly:

```python
from mypy_boto3_ssm.paginators import ListResourceDataSyncPaginator

def get_list_resource_data_sync_paginator() -> ListResourceDataSyncPaginator:
    return boto3.client("ssm").get_paginator("list_resource_data_sync")
```

[Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)

```python
class ListResourceDataSyncPaginator(Boto3Paginator):
    def paginate(
        self,
        SyncType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDataSyncResultTypeDef]:
        pass
```