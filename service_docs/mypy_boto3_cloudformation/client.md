# CloudFormationClient for boto3 CloudFormation module

> [Index](../index.md) > [CloudFormation](./index.md) > CloudFormationClient

Auto-generated documentation for [CloudFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
type annotations stubs module [mypy_boto3_cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/).

- [CloudFormationClient for boto3 CloudFormation module](#cloudformationclient-for-boto3-cloudformation-module)
  - [CloudFormationClient](#cloudformationclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_update_stack](#cancel_update_stack)
    - [continue_update_rollback](#continue_update_rollback)
    - [create_change_set](#create_change_set)
    - [create_stack](#create_stack)
    - [create_stack_instances](#create_stack_instances)
    - [create_stack_set](#create_stack_set)
    - [delete_change_set](#delete_change_set)
    - [delete_stack](#delete_stack)
    - [delete_stack_instances](#delete_stack_instances)
    - [delete_stack_set](#delete_stack_set)
    - [deregister_type](#deregister_type)
    - [describe_account_limits](#describe_account_limits)
    - [describe_change_set](#describe_change_set)
    - [describe_stack_drift_detection_status](#describe_stack_drift_detection_status)
    - [describe_stack_events](#describe_stack_events)
    - [describe_stack_instance](#describe_stack_instance)
    - [describe_stack_resource](#describe_stack_resource)
    - [describe_stack_resource_drifts](#describe_stack_resource_drifts)
    - [describe_stack_resources](#describe_stack_resources)
    - [describe_stack_set](#describe_stack_set)
    - [describe_stack_set_operation](#describe_stack_set_operation)
    - [describe_stacks](#describe_stacks)
    - [describe_type](#describe_type)
    - [describe_type_registration](#describe_type_registration)
    - [detect_stack_drift](#detect_stack_drift)
    - [detect_stack_resource_drift](#detect_stack_resource_drift)
    - [detect_stack_set_drift](#detect_stack_set_drift)
    - [estimate_template_cost](#estimate_template_cost)
    - [execute_change_set](#execute_change_set)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_stack_policy](#get_stack_policy)
    - [get_template](#get_template)
    - [get_template_summary](#get_template_summary)
    - [list_change_sets](#list_change_sets)
    - [list_exports](#list_exports)
    - [list_imports](#list_imports)
    - [list_stack_instances](#list_stack_instances)
    - [list_stack_resources](#list_stack_resources)
    - [list_stack_set_operation_results](#list_stack_set_operation_results)
    - [list_stack_set_operations](#list_stack_set_operations)
    - [list_stack_sets](#list_stack_sets)
    - [list_stacks](#list_stacks)
    - [list_type_registrations](#list_type_registrations)
    - [list_type_versions](#list_type_versions)
    - [list_types](#list_types)
    - [record_handler_progress](#record_handler_progress)
    - [register_type](#register_type)
    - [set_stack_policy](#set_stack_policy)
    - [set_type_default_version](#set_type_default_version)
    - [signal_resource](#signal_resource)
    - [stop_stack_set_operation](#stop_stack_set_operation)
    - [update_stack](#update_stack)
    - [update_stack_instances](#update_stack_instances)
    - [update_stack_set](#update_stack_set)
    - [update_termination_protection](#update_termination_protection)
    - [validate_template](#validate_template)
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
    - [get_waiter](#get_waiter)
    - [get_waiter](#get_waiter-1)
    - [get_waiter](#get_waiter-2)
    - [get_waiter](#get_waiter-3)
    - [get_waiter](#get_waiter-4)
    - [get_waiter](#get_waiter-5)
    - [get_waiter](#get_waiter-6)
    - [get_waiter](#get_waiter-7)

## CloudFormationClient

Type annotations for `boto3.client("cloudformation")`

Can be used directly:

```python
from mypy_boto3_cloudformation.client import CloudFormationClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudformation.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.CFNRegistryException`
- `Exceptions.ChangeSetNotFoundException`
- `Exceptions.ClientError`
- `Exceptions.CreatedButModifiedException`
- `Exceptions.InsufficientCapabilitiesException`
- `Exceptions.InvalidChangeSetStatusException`
- `Exceptions.InvalidOperationException`
- `Exceptions.InvalidStateTransitionException`
- `Exceptions.LimitExceededException`
- `Exceptions.NameAlreadyExistsException`
- `Exceptions.OperationIdAlreadyExistsException`
- `Exceptions.OperationInProgressException`
- `Exceptions.OperationNotFoundException`
- `Exceptions.OperationStatusCheckFailedException`
- `Exceptions.StackInstanceNotFoundException`
- `Exceptions.StackSetNotEmptyException`
- `Exceptions.StackSetNotFoundException`
- `Exceptions.StaleRequestException`
- `Exceptions.TokenAlreadyExistsException`
- `Exceptions.TypeNotFoundException`


## Methods


### can_paginate

Type annotations for `boto3.client("cloudformation").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_update_stack

Type annotations for `boto3.client("cloudformation").cancel_update_stack` method.

[Client.cancel_update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.cancel_update_stack)

```python
def cancel_update_stack(
    self,
    StackName: str,
    ClientRequestToken: str = None
) -> None:
    pass
```

### continue_update_rollback

Type annotations for `boto3.client("cloudformation").continue_update_rollback` method.

[Client.continue_update_rollback documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.continue_update_rollback)

```python
def continue_update_rollback(
    self,
    StackName: str,
    RoleARN: str = None,
    ResourcesToSkip: List[str] = None,
    ClientRequestToken: str = None
) -> Dict[str, Any]:
    pass
```

### create_change_set

Type annotations for `boto3.client("cloudformation").create_change_set` method.

[Client.create_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.create_change_set)

```python
def create_change_set(
    self,
    StackName: str,
    ChangeSetName: str,
    TemplateBody: str = None,
    TemplateURL: str = None,
    UsePreviousTemplate: bool = None,
    Parameters: List["ParameterTypeDef"] = None,
    Capabilities: List[Capability] = None,
    ResourceTypes: List[str] = None,
    RoleARN: str = None,
    RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
    NotificationARNs: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    ClientToken: str = None,
    Description: str = None,
    ChangeSetType: ChangeSetType = None,
    ResourcesToImport: List[ResourceToImportTypeDef] = None,
    IncludeNestedStacks: bool = None
) -> CreateChangeSetOutputTypeDef:
    pass
```

### create_stack

Type annotations for `boto3.client("cloudformation").create_stack` method.

[Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.create_stack)

```python
def create_stack(
    self,
    StackName: str,
    TemplateBody: str = None,
    TemplateURL: str = None,
    Parameters: List["ParameterTypeDef"] = None,
    DisableRollback: bool = None,
    RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
    TimeoutInMinutes: int = None,
    NotificationARNs: List[str] = None,
    Capabilities: List[Capability] = None,
    ResourceTypes: List[str] = None,
    RoleARN: str = None,
    OnFailure: OnFailure = None,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None,
    EnableTerminationProtection: bool = None
) -> CreateStackOutputTypeDef:
    pass
```

### create_stack_instances

Type annotations for `boto3.client("cloudformation").create_stack_instances` method.

[Client.create_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.create_stack_instances)

```python
def create_stack_instances(
    self,
    StackSetName: str,
    Regions: List[str],
    Accounts: List[str] = None,
    DeploymentTargets: "DeploymentTargetsTypeDef" = None,
    ParameterOverrides: List["ParameterTypeDef"] = None,
    OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
    OperationId: str = None,
    CallAs: CallAs = None
) -> CreateStackInstancesOutputTypeDef:
    pass
```

### create_stack_set

Type annotations for `boto3.client("cloudformation").create_stack_set` method.

[Client.create_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.create_stack_set)

```python
def create_stack_set(
    self,
    StackSetName: str,
    Description: str = None,
    TemplateBody: str = None,
    TemplateURL: str = None,
    Parameters: List["ParameterTypeDef"] = None,
    Capabilities: List[Capability] = None,
    Tags: List["TagTypeDef"] = None,
    AdministrationRoleARN: str = None,
    ExecutionRoleName: str = None,
    PermissionModel: PermissionModels = None,
    AutoDeployment: "AutoDeploymentTypeDef" = None,
    CallAs: CallAs = None,
    ClientRequestToken: str = None
) -> CreateStackSetOutputTypeDef:
    pass
```

### delete_change_set

Type annotations for `boto3.client("cloudformation").delete_change_set` method.

[Client.delete_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.delete_change_set)

```python
def delete_change_set(
    self,
    ChangeSetName: str,
    StackName: str = None
) -> Dict[str, Any]:
    pass
```

### delete_stack

Type annotations for `boto3.client("cloudformation").delete_stack` method.

[Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.delete_stack)

```python
def delete_stack(
    self,
    StackName: str,
    RetainResources: List[str] = None,
    RoleARN: str = None,
    ClientRequestToken: str = None
) -> None:
    pass
```

### delete_stack_instances

Type annotations for `boto3.client("cloudformation").delete_stack_instances` method.

[Client.delete_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_instances)

```python
def delete_stack_instances(
    self,
    StackSetName: str,
    Regions: List[str],
    RetainStacks: bool,
    Accounts: List[str] = None,
    DeploymentTargets: "DeploymentTargetsTypeDef" = None,
    OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
    OperationId: str = None,
    CallAs: CallAs = None
) -> DeleteStackInstancesOutputTypeDef:
    pass
```

### delete_stack_set

Type annotations for `boto3.client("cloudformation").delete_stack_set` method.

[Client.delete_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.delete_stack_set)

```python
def delete_stack_set(
    self,
    StackSetName: str,
    CallAs: CallAs = None
) -> Dict[str, Any]:
    pass
```

### deregister_type

Type annotations for `boto3.client("cloudformation").deregister_type` method.

[Client.deregister_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.deregister_type)

```python
def deregister_type(
    self,
    Arn: str = None,
    Type: RegistryType = None,
    TypeName: str = None,
    VersionId: str = None
) -> Dict[str, Any]:
    pass
```

### describe_account_limits

Type annotations for `boto3.client("cloudformation").describe_account_limits` method.

[Client.describe_account_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_account_limits)

```python
def describe_account_limits(
    self,
    NextToken: str = None
) -> DescribeAccountLimitsOutputTypeDef:
    pass
```

### describe_change_set

Type annotations for `boto3.client("cloudformation").describe_change_set` method.

[Client.describe_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_change_set)

```python
def describe_change_set(
    self,
    ChangeSetName: str,
    StackName: str = None,
    NextToken: str = None
) -> DescribeChangeSetOutputTypeDef:
    pass
```

### describe_stack_drift_detection_status

Type annotations for `boto3.client("cloudformation").describe_stack_drift_detection_status` method.

[Client.describe_stack_drift_detection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_drift_detection_status)

```python
def describe_stack_drift_detection_status(
    self,
    StackDriftDetectionId: str
) -> DescribeStackDriftDetectionStatusOutputTypeDef:
    pass
```

### describe_stack_events

Type annotations for `boto3.client("cloudformation").describe_stack_events` method.

[Client.describe_stack_events documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_events)

```python
def describe_stack_events(
    self,
    StackName: str = None,
    NextToken: str = None
) -> DescribeStackEventsOutputTypeDef:
    pass
```

### describe_stack_instance

Type annotations for `boto3.client("cloudformation").describe_stack_instance` method.

[Client.describe_stack_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_instance)

```python
def describe_stack_instance(
    self,
    StackSetName: str,
    StackInstanceAccount: str,
    StackInstanceRegion: str,
    CallAs: CallAs = None
) -> DescribeStackInstanceOutputTypeDef:
    pass
```

### describe_stack_resource

Type annotations for `boto3.client("cloudformation").describe_stack_resource` method.

[Client.describe_stack_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource)

```python
def describe_stack_resource(
    self,
    StackName: str,
    LogicalResourceId: str
) -> DescribeStackResourceOutputTypeDef:
    pass
```

### describe_stack_resource_drifts

Type annotations for `boto3.client("cloudformation").describe_stack_resource_drifts` method.

[Client.describe_stack_resource_drifts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resource_drifts)

```python
def describe_stack_resource_drifts(
    self,
    StackName: str,
    StackResourceDriftStatusFilters: List[StackResourceDriftStatus] = None,
    NextToken: str = None,
    MaxResults: int = None
) -> DescribeStackResourceDriftsOutputTypeDef:
    pass
```

### describe_stack_resources

Type annotations for `boto3.client("cloudformation").describe_stack_resources` method.

[Client.describe_stack_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_resources)

```python
def describe_stack_resources(
    self,
    StackName: str = None,
    LogicalResourceId: str = None,
    PhysicalResourceId: str = None
) -> DescribeStackResourcesOutputTypeDef:
    pass
```

### describe_stack_set

Type annotations for `boto3.client("cloudformation").describe_stack_set` method.

[Client.describe_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set)

```python
def describe_stack_set(
    self,
    StackSetName: str,
    CallAs: CallAs = None
) -> DescribeStackSetOutputTypeDef:
    pass
```

### describe_stack_set_operation

Type annotations for `boto3.client("cloudformation").describe_stack_set_operation` method.

[Client.describe_stack_set_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stack_set_operation)

```python
def describe_stack_set_operation(
    self,
    StackSetName: str,
    OperationId: str,
    CallAs: CallAs = None
) -> DescribeStackSetOperationOutputTypeDef:
    pass
```

### describe_stacks

Type annotations for `boto3.client("cloudformation").describe_stacks` method.

[Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stacks)

```python
def describe_stacks(
    self,
    StackName: str = None,
    NextToken: str = None
) -> DescribeStacksOutputTypeDef:
    pass
```

### describe_type

Type annotations for `boto3.client("cloudformation").describe_type` method.

[Client.describe_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_type)

```python
def describe_type(
    self,
    Type: RegistryType = None,
    TypeName: str = None,
    Arn: str = None,
    VersionId: str = None
) -> DescribeTypeOutputTypeDef:
    pass
```

### describe_type_registration

Type annotations for `boto3.client("cloudformation").describe_type_registration` method.

[Client.describe_type_registration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_type_registration)

```python
def describe_type_registration(
    self,
    RegistrationToken: str
) -> DescribeTypeRegistrationOutputTypeDef:
    pass
```

### detect_stack_drift

Type annotations for `boto3.client("cloudformation").detect_stack_drift` method.

[Client.detect_stack_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_drift)

```python
def detect_stack_drift(
    self,
    StackName: str,
    LogicalResourceIds: List[str] = None
) -> DetectStackDriftOutputTypeDef:
    pass
```

### detect_stack_resource_drift

Type annotations for `boto3.client("cloudformation").detect_stack_resource_drift` method.

[Client.detect_stack_resource_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_resource_drift)

```python
def detect_stack_resource_drift(
    self,
    StackName: str,
    LogicalResourceId: str
) -> DetectStackResourceDriftOutputTypeDef:
    pass
```

### detect_stack_set_drift

Type annotations for `boto3.client("cloudformation").detect_stack_set_drift` method.

[Client.detect_stack_set_drift documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.detect_stack_set_drift)

```python
def detect_stack_set_drift(
    self,
    StackSetName: str,
    OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
    OperationId: str = None,
    CallAs: CallAs = None
) -> DetectStackSetDriftOutputTypeDef:
    pass
```

### estimate_template_cost

Type annotations for `boto3.client("cloudformation").estimate_template_cost` method.

[Client.estimate_template_cost documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.estimate_template_cost)

```python
def estimate_template_cost(
    self,
    TemplateBody: str = None,
    TemplateURL: str = None,
    Parameters: List["ParameterTypeDef"] = None
) -> EstimateTemplateCostOutputTypeDef:
    pass
```

### execute_change_set

Type annotations for `boto3.client("cloudformation").execute_change_set` method.

[Client.execute_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.execute_change_set)

```python
def execute_change_set(
    self,
    ChangeSetName: str,
    StackName: str = None,
    ClientRequestToken: str = None
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudformation").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.generate_presigned_url)

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

### get_stack_policy

Type annotations for `boto3.client("cloudformation").get_stack_policy` method.

[Client.get_stack_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.get_stack_policy)

```python
def get_stack_policy(
    self,
    StackName: str
) -> GetStackPolicyOutputTypeDef:
    pass
```

### get_template

Type annotations for `boto3.client("cloudformation").get_template` method.

[Client.get_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.get_template)

```python
def get_template(
    self,
    StackName: str = None,
    ChangeSetName: str = None,
    TemplateStage: TemplateStage = None
) -> GetTemplateOutputTypeDef:
    pass
```

### get_template_summary

Type annotations for `boto3.client("cloudformation").get_template_summary` method.

[Client.get_template_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.get_template_summary)

```python
def get_template_summary(
    self,
    TemplateBody: str = None,
    TemplateURL: str = None,
    StackName: str = None,
    StackSetName: str = None,
    CallAs: CallAs = None
) -> GetTemplateSummaryOutputTypeDef:
    pass
```

### list_change_sets

Type annotations for `boto3.client("cloudformation").list_change_sets` method.

[Client.list_change_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_change_sets)

```python
def list_change_sets(
    self,
    StackName: str,
    NextToken: str = None
) -> ListChangeSetsOutputTypeDef:
    pass
```

### list_exports

Type annotations for `boto3.client("cloudformation").list_exports` method.

[Client.list_exports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_exports)

```python
def list_exports(
    self,
    NextToken: str = None
) -> ListExportsOutputTypeDef:
    pass
```

### list_imports

Type annotations for `boto3.client("cloudformation").list_imports` method.

[Client.list_imports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_imports)

```python
def list_imports(
    self,
    ExportName: str,
    NextToken: str = None
) -> ListImportsOutputTypeDef:
    pass
```

### list_stack_instances

Type annotations for `boto3.client("cloudformation").list_stack_instances` method.

[Client.list_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_stack_instances)

```python
def list_stack_instances(
    self,
    StackSetName: str,
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[StackInstanceFilterTypeDef] = None,
    StackInstanceAccount: str = None,
    StackInstanceRegion: str = None,
    CallAs: CallAs = None
) -> ListStackInstancesOutputTypeDef:
    pass
```

### list_stack_resources

Type annotations for `boto3.client("cloudformation").list_stack_resources` method.

[Client.list_stack_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_stack_resources)

```python
def list_stack_resources(
    self,
    StackName: str,
    NextToken: str = None
) -> ListStackResourcesOutputTypeDef:
    pass
```

### list_stack_set_operation_results

Type annotations for `boto3.client("cloudformation").list_stack_set_operation_results` method.

[Client.list_stack_set_operation_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operation_results)

```python
def list_stack_set_operation_results(
    self,
    StackSetName: str,
    OperationId: str,
    NextToken: str = None,
    MaxResults: int = None,
    CallAs: CallAs = None
) -> ListStackSetOperationResultsOutputTypeDef:
    pass
```

### list_stack_set_operations

Type annotations for `boto3.client("cloudformation").list_stack_set_operations` method.

[Client.list_stack_set_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_stack_set_operations)

```python
def list_stack_set_operations(
    self,
    StackSetName: str,
    NextToken: str = None,
    MaxResults: int = None,
    CallAs: CallAs = None
) -> ListStackSetOperationsOutputTypeDef:
    pass
```

### list_stack_sets

Type annotations for `boto3.client("cloudformation").list_stack_sets` method.

[Client.list_stack_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_stack_sets)

```python
def list_stack_sets(
    self,
    NextToken: str = None,
    MaxResults: int = None,
    Status: StackSetStatus = None,
    CallAs: CallAs = None
) -> ListStackSetsOutputTypeDef:
    pass
```

### list_stacks

Type annotations for `boto3.client("cloudformation").list_stacks` method.

[Client.list_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_stacks)

```python
def list_stacks(
    self,
    NextToken: str = None,
    StackStatusFilter: List[StackStatus] = None
) -> ListStacksOutputTypeDef:
    pass
```

### list_type_registrations

Type annotations for `boto3.client("cloudformation").list_type_registrations` method.

[Client.list_type_registrations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_type_registrations)

```python
def list_type_registrations(
    self,
    Type: RegistryType = None,
    TypeName: str = None,
    TypeArn: str = None,
    RegistrationStatusFilter: RegistrationStatus = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTypeRegistrationsOutputTypeDef:
    pass
```

### list_type_versions

Type annotations for `boto3.client("cloudformation").list_type_versions` method.

[Client.list_type_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_type_versions)

```python
def list_type_versions(
    self,
    Type: RegistryType = None,
    TypeName: str = None,
    Arn: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    DeprecatedStatus: DeprecatedStatus = None
) -> ListTypeVersionsOutputTypeDef:
    pass
```

### list_types

Type annotations for `boto3.client("cloudformation").list_types` method.

[Client.list_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_types)

```python
def list_types(
    self,
    Visibility: Visibility = None,
    ProvisioningType: ProvisioningType = None,
    DeprecatedStatus: DeprecatedStatus = None,
    Type: RegistryType = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTypesOutputTypeDef:
    pass
```

### record_handler_progress

Type annotations for `boto3.client("cloudformation").record_handler_progress` method.

[Client.record_handler_progress documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.record_handler_progress)

```python
def record_handler_progress(
    self,
    BearerToken: str,
    OperationStatus: OperationStatus,
    CurrentOperationStatus: OperationStatus = None,
    StatusMessage: str = None,
    ErrorCode: HandlerErrorCode = None,
    ResourceModel: str = None,
    ClientRequestToken: str = None
) -> Dict[str, Any]:
    pass
```

### register_type

Type annotations for `boto3.client("cloudformation").register_type` method.

[Client.register_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.register_type)

```python
def register_type(
    self,
    TypeName: str,
    SchemaHandlerPackage: str,
    Type: RegistryType = None,
    LoggingConfig: "LoggingConfigTypeDef" = None,
    ExecutionRoleArn: str = None,
    ClientRequestToken: str = None
) -> RegisterTypeOutputTypeDef:
    pass
```

### set_stack_policy

Type annotations for `boto3.client("cloudformation").set_stack_policy` method.

[Client.set_stack_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.set_stack_policy)

```python
def set_stack_policy(
    self,
    StackName: str,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None
) -> None:
    pass
```

### set_type_default_version

Type annotations for `boto3.client("cloudformation").set_type_default_version` method.

[Client.set_type_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.set_type_default_version)

```python
def set_type_default_version(
    self,
    Arn: str = None,
    Type: RegistryType = None,
    TypeName: str = None,
    VersionId: str = None
) -> Dict[str, Any]:
    pass
```

### signal_resource

Type annotations for `boto3.client("cloudformation").signal_resource` method.

[Client.signal_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.signal_resource)

```python
def signal_resource(
    self,
    StackName: str,
    LogicalResourceId: str,
    UniqueId: str,
    Status: ResourceSignalStatus
) -> None:
    pass
```

### stop_stack_set_operation

Type annotations for `boto3.client("cloudformation").stop_stack_set_operation` method.

[Client.stop_stack_set_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.stop_stack_set_operation)

```python
def stop_stack_set_operation(
    self,
    StackSetName: str,
    OperationId: str,
    CallAs: CallAs = None
) -> Dict[str, Any]:
    pass
```

### update_stack

Type annotations for `boto3.client("cloudformation").update_stack` method.

[Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.update_stack)

```python
def update_stack(
    self,
    StackName: str,
    TemplateBody: str = None,
    TemplateURL: str = None,
    UsePreviousTemplate: bool = None,
    StackPolicyDuringUpdateBody: str = None,
    StackPolicyDuringUpdateURL: str = None,
    Parameters: List["ParameterTypeDef"] = None,
    Capabilities: List[Capability] = None,
    ResourceTypes: List[str] = None,
    RoleARN: str = None,
    RollbackConfiguration: "RollbackConfigurationTypeDef" = None,
    StackPolicyBody: str = None,
    StackPolicyURL: str = None,
    NotificationARNs: List[str] = None,
    Tags: List["TagTypeDef"] = None,
    ClientRequestToken: str = None
) -> UpdateStackOutputTypeDef:
    pass
```

### update_stack_instances

Type annotations for `boto3.client("cloudformation").update_stack_instances` method.

[Client.update_stack_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.update_stack_instances)

```python
def update_stack_instances(
    self,
    StackSetName: str,
    Regions: List[str],
    Accounts: List[str] = None,
    DeploymentTargets: "DeploymentTargetsTypeDef" = None,
    ParameterOverrides: List["ParameterTypeDef"] = None,
    OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
    OperationId: str = None,
    CallAs: CallAs = None
) -> UpdateStackInstancesOutputTypeDef:
    pass
```

### update_stack_set

Type annotations for `boto3.client("cloudformation").update_stack_set` method.

[Client.update_stack_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.update_stack_set)

```python
def update_stack_set(
    self,
    StackSetName: str,
    Description: str = None,
    TemplateBody: str = None,
    TemplateURL: str = None,
    UsePreviousTemplate: bool = None,
    Parameters: List["ParameterTypeDef"] = None,
    Capabilities: List[Capability] = None,
    Tags: List["TagTypeDef"] = None,
    OperationPreferences: "StackSetOperationPreferencesTypeDef" = None,
    AdministrationRoleARN: str = None,
    ExecutionRoleName: str = None,
    DeploymentTargets: "DeploymentTargetsTypeDef" = None,
    PermissionModel: PermissionModels = None,
    AutoDeployment: "AutoDeploymentTypeDef" = None,
    OperationId: str = None,
    Accounts: List[str] = None,
    Regions: List[str] = None,
    CallAs: CallAs = None
) -> UpdateStackSetOutputTypeDef:
    pass
```

### update_termination_protection

Type annotations for `boto3.client("cloudformation").update_termination_protection` method.

[Client.update_termination_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.update_termination_protection)

```python
def update_termination_protection(
    self,
    EnableTerminationProtection: bool,
    StackName: str
) -> UpdateTerminationProtectionOutputTypeDef:
    pass
```

### validate_template

Type annotations for `boto3.client("cloudformation").validate_template` method.

[Client.validate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.validate_template)

```python
def validate_template(
    self,
    TemplateBody: str = None,
    TemplateURL: str = None
) -> ValidateTemplateOutputTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeAccountLimits)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeAccountLimitsPaginatorName
) -> DescribeAccountLimitsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.DescribeChangeSet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeChangeSet)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeChangeSetPaginatorName
) -> DescribeChangeSetPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.DescribeStackEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStackEvents)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeStackEventsPaginatorName
) -> DescribeStackEventsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.DescribeStacks)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeStacksPaginatorName
) -> DescribeStacksPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListChangeSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListChangeSets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListChangeSetsPaginatorName
) -> ListChangeSetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListExports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListExports)

```python
@overload
def get_paginator(
    self,
    operation_name: ListExportsPaginatorName
) -> ListExportsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListImports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListImports)

```python
@overload
def get_paginator(
    self,
    operation_name: ListImportsPaginatorName
) -> ListImportsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListStackInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackInstances)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStackInstancesPaginatorName
) -> ListStackInstancesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListStackResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackResources)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStackResourcesPaginatorName
) -> ListStackResourcesPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListStackSetOperationResults documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperationResults)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStackSetOperationResultsPaginatorName
) -> ListStackSetOperationResultsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListStackSetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSetOperations)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStackSetOperationsPaginatorName
) -> ListStackSetOperationsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListStackSets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStackSets)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStackSetsPaginatorName
) -> ListStackSetsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloudformation").get_paginator` method.

[Paginator.ListStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Paginator.ListStacks)

```python
@overload
def get_paginator(
    self,
    operation_name: ListStacksPaginatorName
) -> ListStacksPaginator:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.ChangeSetCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.ChangeSetCreateComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: ChangeSetCreateCompleteWaiterName
) -> ChangeSetCreateCompleteWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.StackCreateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.StackCreateComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: StackCreateCompleteWaiterName
) -> StackCreateCompleteWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.StackDeleteComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.StackDeleteComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: StackDeleteCompleteWaiterName
) -> StackDeleteCompleteWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.StackExists documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.StackExists)

```python
@overload
def get_waiter(
    self,
    waiter_name: StackExistsWaiterName
) -> StackExistsWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.StackImportComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.StackImportComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: StackImportCompleteWaiterName
) -> StackImportCompleteWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.StackRollbackComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.StackRollbackComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: StackRollbackCompleteWaiterName
) -> StackRollbackCompleteWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.StackUpdateComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.StackUpdateComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: StackUpdateCompleteWaiterName
) -> StackUpdateCompleteWaiter:
    pass
```

### get_waiter

Type annotations for `boto3.client("cloudformation").get_waiter` method.

[Waiter.TypeRegistrationComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Waiter.TypeRegistrationComplete)

```python
@overload
def get_waiter(
    self,
    waiter_name: TypeRegistrationCompleteWaiterName
) -> TypeRegistrationCompleteWaiter:
    pass
```