# EMRClient for boto3 EMR module

> [Index](../index.md) > [EMR](./index.md) > EMRClient

Auto-generated documentation for [EMR](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR)
type annotations stubs module [mypy_boto3_emr](https://pypi.org/project/mypy-boto3-emr/).

- [EMRClient for boto3 EMR module](#emrclient-for-boto3-emr-module)
  - [EMRClient](#emrclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_instance_fleet](#add_instance_fleet)
    - [add_instance_groups](#add_instance_groups)
    - [add_job_flow_steps](#add_job_flow_steps)
    - [add_tags](#add_tags)
    - [can_paginate](#can_paginate)
    - [cancel_steps](#cancel_steps)
    - [create_security_configuration](#create_security_configuration)
    - [create_studio](#create_studio)
    - [create_studio_session_mapping](#create_studio_session_mapping)
    - [delete_security_configuration](#delete_security_configuration)
    - [delete_studio](#delete_studio)
    - [delete_studio_session_mapping](#delete_studio_session_mapping)
    - [describe_cluster](#describe_cluster)
    - [describe_job_flows](#describe_job_flows)
    - [describe_notebook_execution](#describe_notebook_execution)
    - [describe_security_configuration](#describe_security_configuration)
    - [describe_step](#describe_step)
    - [describe_studio](#describe_studio)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_block_public_access_configuration](#get_block_public_access_configuration)
    - [get_managed_scaling_policy](#get_managed_scaling_policy)
    - [get_studio_session_mapping](#get_studio_session_mapping)
    - [list_bootstrap_actions](#list_bootstrap_actions)
    - [list_clusters](#list_clusters)
    - [list_instance_fleets](#list_instance_fleets)
    - [list_instance_groups](#list_instance_groups)
    - [list_instances](#list_instances)
    - [list_notebook_executions](#list_notebook_executions)
    - [list_security_configurations](#list_security_configurations)
    - [list_steps](#list_steps)
    - [list_studio_session_mappings](#list_studio_session_mappings)
    - [list_studios](#list_studios)
    - [modify_cluster](#modify_cluster)
    - [modify_instance_fleet](#modify_instance_fleet)
    - [modify_instance_groups](#modify_instance_groups)
    - [put_auto_scaling_policy](#put_auto_scaling_policy)
    - [put_block_public_access_configuration](#put_block_public_access_configuration)
    - [put_managed_scaling_policy](#put_managed_scaling_policy)
    - [remove_auto_scaling_policy](#remove_auto_scaling_policy)
    - [remove_managed_scaling_policy](#remove_managed_scaling_policy)
    - [remove_tags](#remove_tags)
    - [run_job_flow](#run_job_flow)
    - [set_termination_protection](#set_termination_protection)
    - [set_visible_to_all_users](#set_visible_to_all_users)
    - [start_notebook_execution](#start_notebook_execution)
    - [stop_notebook_execution](#stop_notebook_execution)
    - [terminate_job_flows](#terminate_job_flows)
    - [update_studio](#update_studio)
    - [update_studio_session_mapping](#update_studio_session_mapping)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## EMRClient

Type annotations for `boto3.client("emr")`

Can be used directly:

```python
from mypy_boto3_emr.client import EMRClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_emr.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalServerError`
- `Exceptions.InternalServerException`
- `Exceptions.InvalidRequestException`


## Methods


### add_instance_fleet

Type annotations for `boto3.client("emr").add_instance_fleet` method.

[Client.add_instance_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.add_instance_fleet)

```python
def add_instance_fleet(
    self,
    ClusterId: str,
    InstanceFleet: "InstanceFleetConfigTypeDef"
) -> AddInstanceFleetOutputTypeDef:
    pass
```

### add_instance_groups

Type annotations for `boto3.client("emr").add_instance_groups` method.

[Client.add_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.add_instance_groups)

```python
def add_instance_groups(
    self,
    InstanceGroups: List["InstanceGroupConfigTypeDef"],
    JobFlowId: str
) -> AddInstanceGroupsOutputTypeDef:
    pass
```

### add_job_flow_steps

Type annotations for `boto3.client("emr").add_job_flow_steps` method.

[Client.add_job_flow_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.add_job_flow_steps)

```python
def add_job_flow_steps(
    self,
    JobFlowId: str,
    Steps: List["StepConfigTypeDef"]
) -> AddJobFlowStepsOutputTypeDef:
    pass
```

### add_tags

Type annotations for `boto3.client("emr").add_tags` method.

[Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.add_tags)

```python
def add_tags(
    self,
    ResourceId: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("emr").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_steps

Type annotations for `boto3.client("emr").cancel_steps` method.

[Client.cancel_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.cancel_steps)

```python
def cancel_steps(
    self,
    ClusterId: str,
    StepIds: List[str],
    StepCancellationOption: StepCancellationOption = None
) -> CancelStepsOutputTypeDef:
    pass
```

### create_security_configuration

Type annotations for `boto3.client("emr").create_security_configuration` method.

[Client.create_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.create_security_configuration)

```python
def create_security_configuration(
    self,
    Name: str,
    SecurityConfiguration: str
) -> CreateSecurityConfigurationOutputTypeDef:
    pass
```

### create_studio

Type annotations for `boto3.client("emr").create_studio` method.

[Client.create_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.create_studio)

```python
def create_studio(
    self,
    Name: str,
    AuthMode: AuthMode,
    VpcId: str,
    SubnetIds: List[str],
    ServiceRole: str,
    UserRole: str,
    WorkspaceSecurityGroupId: str,
    EngineSecurityGroupId: str,
    DefaultS3Location: str,
    Description: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateStudioOutputTypeDef:
    pass
```

### create_studio_session_mapping

Type annotations for `boto3.client("emr").create_studio_session_mapping` method.

[Client.create_studio_session_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.create_studio_session_mapping)

```python
def create_studio_session_mapping(
    self,
    StudioId: str,
    IdentityType: IdentityType,
    SessionPolicyArn: str,
    IdentityId: str = None,
    IdentityName: str = None
) -> None:
    pass
```

### delete_security_configuration

Type annotations for `boto3.client("emr").delete_security_configuration` method.

[Client.delete_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.delete_security_configuration)

```python
def delete_security_configuration(
    self,
    Name: str
) -> Dict[str, Any]:
    pass
```

### delete_studio

Type annotations for `boto3.client("emr").delete_studio` method.

[Client.delete_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.delete_studio)

```python
def delete_studio(
    self,
    StudioId: str
) -> None:
    pass
```

### delete_studio_session_mapping

Type annotations for `boto3.client("emr").delete_studio_session_mapping` method.

[Client.delete_studio_session_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.delete_studio_session_mapping)

```python
def delete_studio_session_mapping(
    self,
    StudioId: str,
    IdentityType: IdentityType,
    IdentityId: str = None,
    IdentityName: str = None
) -> None:
    pass
```

### describe_cluster

Type annotations for `boto3.client("emr").describe_cluster` method.

[Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_cluster)

```python
def describe_cluster(
    self,
    ClusterId: str
) -> DescribeClusterOutputTypeDef:
    pass
```

### describe_job_flows

Type annotations for `boto3.client("emr").describe_job_flows` method.

[Client.describe_job_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_job_flows)

```python
def describe_job_flows(
    self,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    JobFlowIds: List[str] = None,
    JobFlowStates: List[JobFlowExecutionState] = None
) -> DescribeJobFlowsOutputTypeDef:
    pass
```

### describe_notebook_execution

Type annotations for `boto3.client("emr").describe_notebook_execution` method.

[Client.describe_notebook_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_notebook_execution)

```python
def describe_notebook_execution(
    self,
    NotebookExecutionId: str
) -> DescribeNotebookExecutionOutputTypeDef:
    pass
```

### describe_security_configuration

Type annotations for `boto3.client("emr").describe_security_configuration` method.

[Client.describe_security_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_security_configuration)

```python
def describe_security_configuration(
    self,
    Name: str
) -> DescribeSecurityConfigurationOutputTypeDef:
    pass
```

### describe_step

Type annotations for `boto3.client("emr").describe_step` method.

[Client.describe_step documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_step)

```python
def describe_step(
    self,
    ClusterId: str,
    StepId: str
) -> DescribeStepOutputTypeDef:
    pass
```

### describe_studio

Type annotations for `boto3.client("emr").describe_studio` method.

[Client.describe_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.describe_studio)

```python
def describe_studio(
    self,
    StudioId: str
) -> DescribeStudioOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("emr").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.generate_presigned_url)

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

### get_block_public_access_configuration

Type annotations for `boto3.client("emr").get_block_public_access_configuration` method.

[Client.get_block_public_access_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.get_block_public_access_configuration)

```python
def get_block_public_access_configuration(
    self
) -> GetBlockPublicAccessConfigurationOutputTypeDef:
    pass
```

### get_managed_scaling_policy

Type annotations for `boto3.client("emr").get_managed_scaling_policy` method.

[Client.get_managed_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.get_managed_scaling_policy)

```python
def get_managed_scaling_policy(
    self,
    ClusterId: str
) -> GetManagedScalingPolicyOutputTypeDef:
    pass
```

### get_studio_session_mapping

Type annotations for `boto3.client("emr").get_studio_session_mapping` method.

[Client.get_studio_session_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.get_studio_session_mapping)

```python
def get_studio_session_mapping(
    self,
    StudioId: str,
    IdentityType: IdentityType,
    IdentityId: str = None,
    IdentityName: str = None
) -> GetStudioSessionMappingOutputTypeDef:
    pass
```

### list_bootstrap_actions

Type annotations for `boto3.client("emr").list_bootstrap_actions` method.

[Client.list_bootstrap_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_bootstrap_actions)

```python
def list_bootstrap_actions(
    self,
    ClusterId: str,
    Marker: str = None
) -> ListBootstrapActionsOutputTypeDef:
    pass
```

### list_clusters

Type annotations for `boto3.client("emr").list_clusters` method.

[Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_clusters)

```python
def list_clusters(
    self,
    CreatedAfter: datetime = None,
    CreatedBefore: datetime = None,
    ClusterStates: List[ClusterState] = None,
    Marker: str = None
) -> ListClustersOutputTypeDef:
    pass
```

### list_instance_fleets

Type annotations for `boto3.client("emr").list_instance_fleets` method.

[Client.list_instance_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_instance_fleets)

```python
def list_instance_fleets(
    self,
    ClusterId: str,
    Marker: str = None
) -> ListInstanceFleetsOutputTypeDef:
    pass
```

### list_instance_groups

Type annotations for `boto3.client("emr").list_instance_groups` method.

[Client.list_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_instance_groups)

```python
def list_instance_groups(
    self,
    ClusterId: str,
    Marker: str = None
) -> ListInstanceGroupsOutputTypeDef:
    pass
```

### list_instances

Type annotations for `boto3.client("emr").list_instances` method.

[Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_instances)

```python
def list_instances(
    self,
    ClusterId: str,
    InstanceGroupId: str = None,
    InstanceGroupTypes: List[InstanceGroupType] = None,
    InstanceFleetId: str = None,
    InstanceFleetType: InstanceFleetType = None,
    InstanceStates: List[InstanceState] = None,
    Marker: str = None
) -> ListInstancesOutputTypeDef:
    pass
```

### list_notebook_executions

Type annotations for `boto3.client("emr").list_notebook_executions` method.

[Client.list_notebook_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_notebook_executions)

```python
def list_notebook_executions(
    self,
    EditorId: str = None,
    Status: NotebookExecutionStatus = None,
    From: datetime = None,
    To: datetime = None,
    Marker: str = None
) -> ListNotebookExecutionsOutputTypeDef:
    pass
```

### list_security_configurations

Type annotations for `boto3.client("emr").list_security_configurations` method.

[Client.list_security_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_security_configurations)

```python
def list_security_configurations(
    self,
    Marker: str = None
) -> ListSecurityConfigurationsOutputTypeDef:
    pass
```

### list_steps

Type annotations for `boto3.client("emr").list_steps` method.

[Client.list_steps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_steps)

```python
def list_steps(
    self,
    ClusterId: str,
    StepStates: List[StepState] = None,
    StepIds: List[str] = None,
    Marker: str = None
) -> ListStepsOutputTypeDef:
    pass
```

### list_studio_session_mappings

Type annotations for `boto3.client("emr").list_studio_session_mappings` method.

[Client.list_studio_session_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_studio_session_mappings)

```python
def list_studio_session_mappings(
    self,
    StudioId: str = None,
    IdentityType: IdentityType = None,
    Marker: str = None
) -> ListStudioSessionMappingsOutputTypeDef:
    pass
```

### list_studios

Type annotations for `boto3.client("emr").list_studios` method.

[Client.list_studios documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.list_studios)

```python
def list_studios(
    self,
    Marker: str = None
) -> ListStudiosOutputTypeDef:
    pass
```

### modify_cluster

Type annotations for `boto3.client("emr").modify_cluster` method.

[Client.modify_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.modify_cluster)

```python
def modify_cluster(
    self,
    ClusterId: str,
    StepConcurrencyLevel: int = None
) -> ModifyClusterOutputTypeDef:
    pass
```

### modify_instance_fleet

Type annotations for `boto3.client("emr").modify_instance_fleet` method.

[Client.modify_instance_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.modify_instance_fleet)

```python
def modify_instance_fleet(
    self,
    ClusterId: str,
    InstanceFleet: InstanceFleetModifyConfigTypeDef
) -> None:
    pass
```

### modify_instance_groups

Type annotations for `boto3.client("emr").modify_instance_groups` method.

[Client.modify_instance_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.modify_instance_groups)

```python
def modify_instance_groups(
    self,
    ClusterId: str = None,
    InstanceGroups: List[InstanceGroupModifyConfigTypeDef] = None
) -> None:
    pass
```

### put_auto_scaling_policy

Type annotations for `boto3.client("emr").put_auto_scaling_policy` method.

[Client.put_auto_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.put_auto_scaling_policy)

```python
def put_auto_scaling_policy(
    self,
    ClusterId: str,
    InstanceGroupId: str,
    AutoScalingPolicy: "AutoScalingPolicyTypeDef"
) -> PutAutoScalingPolicyOutputTypeDef:
    pass
```

### put_block_public_access_configuration

Type annotations for `boto3.client("emr").put_block_public_access_configuration` method.

[Client.put_block_public_access_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.put_block_public_access_configuration)

```python
def put_block_public_access_configuration(
    self,
    BlockPublicAccessConfiguration: "BlockPublicAccessConfigurationTypeDef"
) -> Dict[str, Any]:
    pass
```

### put_managed_scaling_policy

Type annotations for `boto3.client("emr").put_managed_scaling_policy` method.

[Client.put_managed_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.put_managed_scaling_policy)

```python
def put_managed_scaling_policy(
    self,
    ClusterId: str,
    ManagedScalingPolicy: "ManagedScalingPolicyTypeDef"
) -> Dict[str, Any]:
    pass
```

### remove_auto_scaling_policy

Type annotations for `boto3.client("emr").remove_auto_scaling_policy` method.

[Client.remove_auto_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.remove_auto_scaling_policy)

```python
def remove_auto_scaling_policy(
    self,
    ClusterId: str,
    InstanceGroupId: str
) -> Dict[str, Any]:
    pass
```

### remove_managed_scaling_policy

Type annotations for `boto3.client("emr").remove_managed_scaling_policy` method.

[Client.remove_managed_scaling_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.remove_managed_scaling_policy)

```python
def remove_managed_scaling_policy(
    self,
    ClusterId: str
) -> Dict[str, Any]:
    pass
```

### remove_tags

Type annotations for `boto3.client("emr").remove_tags` method.

[Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.remove_tags)

```python
def remove_tags(
    self,
    ResourceId: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### run_job_flow

Type annotations for `boto3.client("emr").run_job_flow` method.

[Client.run_job_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.run_job_flow)

```python
def run_job_flow(
    self,
    Name: str,
    Instances: JobFlowInstancesConfigTypeDef,
    LogUri: str = None,
    LogEncryptionKmsKeyId: str = None,
    AdditionalInfo: str = None,
    AmiVersion: str = None,
    ReleaseLabel: str = None,
    Steps: List["StepConfigTypeDef"] = None,
    BootstrapActions: List["BootstrapActionConfigTypeDef"] = None,
    SupportedProducts: List[str] = None,
    NewSupportedProducts: List[SupportedProductConfigTypeDef] = None,
    Applications: List["ApplicationTypeDef"] = None,
    Configurations: List[Dict[str, Any]] = None,
    VisibleToAllUsers: bool = None,
    JobFlowRole: str = None,
    ServiceRole: str = None,
    Tags: List["TagTypeDef"] = None,
    SecurityConfiguration: str = None,
    AutoScalingRole: str = None,
    ScaleDownBehavior: ScaleDownBehavior = None,
    CustomAmiId: str = None,
    EbsRootVolumeSize: int = None,
    RepoUpgradeOnBoot: RepoUpgradeOnBoot = None,
    KerberosAttributes: "KerberosAttributesTypeDef" = None,
    StepConcurrencyLevel: int = None,
    ManagedScalingPolicy: "ManagedScalingPolicyTypeDef" = None,
    PlacementGroupConfigs: List["PlacementGroupConfigTypeDef"] = None
) -> RunJobFlowOutputTypeDef:
    pass
```

### set_termination_protection

Type annotations for `boto3.client("emr").set_termination_protection` method.

[Client.set_termination_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.set_termination_protection)

```python
def set_termination_protection(
    self,
    JobFlowIds: List[str],
    TerminationProtected: bool
) -> None:
    pass
```

### set_visible_to_all_users

Type annotations for `boto3.client("emr").set_visible_to_all_users` method.

[Client.set_visible_to_all_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.set_visible_to_all_users)

```python
def set_visible_to_all_users(
    self,
    JobFlowIds: List[str],
    VisibleToAllUsers: bool
) -> None:
    pass
```

### start_notebook_execution

Type annotations for `boto3.client("emr").start_notebook_execution` method.

[Client.start_notebook_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.start_notebook_execution)

```python
def start_notebook_execution(
    self,
    EditorId: str,
    RelativePath: str,
    ExecutionEngine: "ExecutionEngineConfigTypeDef",
    ServiceRole: str,
    NotebookExecutionName: str = None,
    NotebookParams: str = None,
    NotebookInstanceSecurityGroupId: str = None,
    Tags: List["TagTypeDef"] = None
) -> StartNotebookExecutionOutputTypeDef:
    pass
```

### stop_notebook_execution

Type annotations for `boto3.client("emr").stop_notebook_execution` method.

[Client.stop_notebook_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.stop_notebook_execution)

```python
def stop_notebook_execution(
    self,
    NotebookExecutionId: str
) -> None:
    pass
```

### terminate_job_flows

Type annotations for `boto3.client("emr").terminate_job_flows` method.

[Client.terminate_job_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.terminate_job_flows)

```python
def terminate_job_flows(
    self,
    JobFlowIds: List[str]
) -> None:
    pass
```

### update_studio

Type annotations for `boto3.client("emr").update_studio` method.

[Client.update_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.update_studio)

```python
def update_studio(
    self,
    StudioId: str,
    Name: str = None,
    Description: str = None,
    SubnetIds: List[str] = None,
    DefaultS3Location: str = None
) -> None:
    pass
```

### update_studio_session_mapping

Type annotations for `boto3.client("emr").update_studio_session_mapping` method.

[Client.update_studio_session_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.update_studio_session_mapping)

```python
def update_studio_session_mapping(
    self,
    StudioId: str,
    IdentityType: IdentityType,
    SessionPolicyArn: str,
    IdentityId: str = None,
    IdentityName: str = None
) -> None:
    pass
```



### get_paginator

Type annotations for `boto3.client("emr").get_paginator` method with overloads.

- `client.get_paginator("list_bootstrap_actions")` -> [ListBootstrapActionsPaginator](./paginators.md#listbootstrapactionspaginator)
- `client.get_paginator("list_clusters")` -> [ListClustersPaginator](./paginators.md#listclusterspaginator)
- `client.get_paginator("list_instance_fleets")` -> [ListInstanceFleetsPaginator](./paginators.md#listinstancefleetspaginator)
- `client.get_paginator("list_instance_groups")` -> [ListInstanceGroupsPaginator](./paginators.md#listinstancegroupspaginator)
- `client.get_paginator("list_instances")` -> [ListInstancesPaginator](./paginators.md#listinstancespaginator)
- `client.get_paginator("list_notebook_executions")` -> [ListNotebookExecutionsPaginator](./paginators.md#listnotebookexecutionspaginator)
- `client.get_paginator("list_security_configurations")` -> [ListSecurityConfigurationsPaginator](./paginators.md#listsecurityconfigurationspaginator)
- `client.get_paginator("list_steps")` -> [ListStepsPaginator](./paginators.md#liststepspaginator)
- `client.get_paginator("list_studio_session_mappings")` -> [ListStudioSessionMappingsPaginator](./paginators.md#liststudiosessionmappingspaginator)
- `client.get_paginator("list_studios")` -> [ListStudiosPaginator](./paginators.md#liststudiospaginator)




### get_waiter

Type annotations for `boto3.client("emr").get_waiter` method with overloads.

- `client.get_waiter("cluster_running")` -> [ClusterRunningWaiter](./waiters.md#clusterrunningwaiter)
- `client.get_waiter("cluster_terminated")` -> [ClusterTerminatedWaiter](./waiters.md#clusterterminatedwaiter)
- `client.get_waiter("step_complete")` -> [StepCompleteWaiter](./waiters.md#stepcompletewaiter)
