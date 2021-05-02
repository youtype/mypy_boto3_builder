# mgnClient for boto3 mgn module

> [Index](../index.md) > [mgn](./index.md) > mgnClient

Auto-generated documentation for [mgn](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn)
type annotations stubs module [mypy_boto3_mgn](https://pypi.org/project/mypy-boto3-mgn/).

- [mgnClient for boto3 mgn module](#mgnclient-for-boto3-mgn-module)
  - [mgnClient](#mgnclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [change_server_life_cycle_state](#change_server_life_cycle_state)
    - [create_replication_configuration_template](#create_replication_configuration_template)
    - [delete_job](#delete_job)
    - [delete_replication_configuration_template](#delete_replication_configuration_template)
    - [delete_source_server](#delete_source_server)
    - [describe_job_log_items](#describe_job_log_items)
    - [describe_jobs](#describe_jobs)
    - [describe_replication_configuration_templates](#describe_replication_configuration_templates)
    - [describe_source_servers](#describe_source_servers)
    - [disconnect_from_service](#disconnect_from_service)
    - [finalize_cutover](#finalize_cutover)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_launch_configuration](#get_launch_configuration)
    - [get_replication_configuration](#get_replication_configuration)
    - [initialize_service](#initialize_service)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [mark_as_archived](#mark_as_archived)
    - [retry_data_replication](#retry_data_replication)
    - [start_cutover](#start_cutover)
    - [start_test](#start_test)
    - [tag_resource](#tag_resource)
    - [terminate_target_instances](#terminate_target_instances)
    - [untag_resource](#untag_resource)
    - [update_launch_configuration](#update_launch_configuration)
    - [update_replication_configuration](#update_replication_configuration)
    - [update_replication_configuration_template](#update_replication_configuration_template)
    - [get_paginator](#get_paginator)

## mgnClient

Type annotations for `boto3.client("mgn")`

Can be used directly:

```python
from mypy_boto3_mgn.client import mgnClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mgn.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ThrottlingException`
- `Exceptions.UninitializedAccountException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("mgn").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### change_server_life_cycle_state

Type annotations for `boto3.client("mgn").change_server_life_cycle_state` method.

[Client.change_server_life_cycle_state documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.change_server_life_cycle_state)

```python
def change_server_life_cycle_state(
    self,
    lifeCycle: ChangeServerLifeCycleStateSourceServerLifecycleTypeDef,
    sourceServerID: str
) -> "SourceServerTypeDef":
    pass
```

### create_replication_configuration_template

Type annotations for `boto3.client("mgn").create_replication_configuration_template` method.

[Client.create_replication_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.create_replication_configuration_template)

```python
def create_replication_configuration_template(
    self,
    associateDefaultSecurityGroup: bool,
    bandwidthThrottling: int,
    createPublicIP: bool,
    dataPlaneRouting: ReplicationConfigurationDataPlaneRouting,
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskType,
    ebsEncryption: ReplicationConfigurationEbsEncryption,
    replicationServerInstanceType: str,
    replicationServersSecurityGroupsIDs: List[str],
    stagingAreaSubnetId: str,
    stagingAreaTags: Dict[str, str],
    useDedicatedReplicationServer: bool,
    ebsEncryptionKeyArn: str = None,
    tags: Dict[str, str] = None
) -> "ReplicationConfigurationTemplateTypeDef":
    pass
```

### delete_job

Type annotations for `boto3.client("mgn").delete_job` method.

[Client.delete_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.delete_job)

```python
def delete_job(
    self,
    jobID: str
) -> Dict[str, Any]:
    pass
```

### delete_replication_configuration_template

Type annotations for `boto3.client("mgn").delete_replication_configuration_template` method.

[Client.delete_replication_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.delete_replication_configuration_template)

```python
def delete_replication_configuration_template(
    self,
    replicationConfigurationTemplateID: str
) -> Dict[str, Any]:
    pass
```

### delete_source_server

Type annotations for `boto3.client("mgn").delete_source_server` method.

[Client.delete_source_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.delete_source_server)

```python
def delete_source_server(
    self,
    sourceServerID: str
) -> Dict[str, Any]:
    pass
```

### describe_job_log_items

Type annotations for `boto3.client("mgn").describe_job_log_items` method.

[Client.describe_job_log_items documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.describe_job_log_items)

```python
def describe_job_log_items(
    self,
    jobID: str,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeJobLogItemsResponseTypeDef:
    pass
```

### describe_jobs

Type annotations for `boto3.client("mgn").describe_jobs` method.

[Client.describe_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.describe_jobs)

```python
def describe_jobs(
    self,
    filters: DescribeJobsRequestFiltersTypeDef,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeJobsResponseTypeDef:
    pass
```

### describe_replication_configuration_templates

Type annotations for `boto3.client("mgn").describe_replication_configuration_templates` method.

[Client.describe_replication_configuration_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.describe_replication_configuration_templates)

```python
def describe_replication_configuration_templates(
    self,
    replicationConfigurationTemplateIDs: List[str],
    maxResults: int = None,
    nextToken: str = None
) -> DescribeReplicationConfigurationTemplatesResponseTypeDef:
    pass
```

### describe_source_servers

Type annotations for `boto3.client("mgn").describe_source_servers` method.

[Client.describe_source_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.describe_source_servers)

```python
def describe_source_servers(
    self,
    filters: DescribeSourceServersRequestFiltersTypeDef,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeSourceServersResponseTypeDef:
    pass
```

### disconnect_from_service

Type annotations for `boto3.client("mgn").disconnect_from_service` method.

[Client.disconnect_from_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.disconnect_from_service)

```python
def disconnect_from_service(
    self,
    sourceServerID: str
) -> "SourceServerTypeDef":
    pass
```

### finalize_cutover

Type annotations for `boto3.client("mgn").finalize_cutover` method.

[Client.finalize_cutover documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.finalize_cutover)

```python
def finalize_cutover(
    self,
    sourceServerID: str
) -> "SourceServerTypeDef":
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mgn").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.generate_presigned_url)

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

### get_launch_configuration

Type annotations for `boto3.client("mgn").get_launch_configuration` method.

[Client.get_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.get_launch_configuration)

```python
def get_launch_configuration(
    self,
    sourceServerID: str
) -> LaunchConfigurationTypeDef:
    pass
```

### get_replication_configuration

Type annotations for `boto3.client("mgn").get_replication_configuration` method.

[Client.get_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.get_replication_configuration)

```python
def get_replication_configuration(
    self,
    sourceServerID: str
) -> ReplicationConfigurationTypeDef:
    pass
```

### initialize_service

Type annotations for `boto3.client("mgn").initialize_service` method.

[Client.initialize_service documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.initialize_service)

```python
def initialize_service(
    self
) -> Dict[str, Any]:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("mgn").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### mark_as_archived

Type annotations for `boto3.client("mgn").mark_as_archived` method.

[Client.mark_as_archived documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.mark_as_archived)

```python
def mark_as_archived(
    self,
    sourceServerID: str
) -> "SourceServerTypeDef":
    pass
```

### retry_data_replication

Type annotations for `boto3.client("mgn").retry_data_replication` method.

[Client.retry_data_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.retry_data_replication)

```python
def retry_data_replication(
    self,
    sourceServerID: str
) -> "SourceServerTypeDef":
    pass
```

### start_cutover

Type annotations for `boto3.client("mgn").start_cutover` method.

[Client.start_cutover documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.start_cutover)

```python
def start_cutover(
    self,
    sourceServerIDs: List[str],
    tags: Dict[str, str] = None
) -> StartCutoverResponseTypeDef:
    pass
```

### start_test

Type annotations for `boto3.client("mgn").start_test` method.

[Client.start_test documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.start_test)

```python
def start_test(
    self,
    sourceServerIDs: List[str],
    tags: Dict[str, str] = None
) -> StartTestResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("mgn").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> None:
    pass
```

### terminate_target_instances

Type annotations for `boto3.client("mgn").terminate_target_instances` method.

[Client.terminate_target_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.terminate_target_instances)

```python
def terminate_target_instances(
    self,
    sourceServerIDs: List[str],
    tags: Dict[str, str] = None
) -> TerminateTargetInstancesResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("mgn").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> None:
    pass
```

### update_launch_configuration

Type annotations for `boto3.client("mgn").update_launch_configuration` method.

[Client.update_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.update_launch_configuration)

```python
def update_launch_configuration(
    self,
    sourceServerID: str,
    copyPrivateIp: bool = None,
    copyTags: bool = None,
    launchDisposition: LaunchDisposition = None,
    licensing: "LicensingTypeDef" = None,
    name: str = None,
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethod = None
) -> LaunchConfigurationTypeDef:
    pass
```

### update_replication_configuration

Type annotations for `boto3.client("mgn").update_replication_configuration` method.

[Client.update_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.update_replication_configuration)

```python
def update_replication_configuration(
    self,
    sourceServerID: str,
    associateDefaultSecurityGroup: bool = None,
    bandwidthThrottling: int = None,
    createPublicIP: bool = None,
    dataPlaneRouting: ReplicationConfigurationDataPlaneRouting = None,
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskType = None,
    ebsEncryption: ReplicationConfigurationEbsEncryption = None,
    ebsEncryptionKeyArn: str = None,
    name: str = None,
    replicatedDisks: List["ReplicationConfigurationReplicatedDiskTypeDef"] = None,
    replicationServerInstanceType: str = None,
    replicationServersSecurityGroupsIDs: List[str] = None,
    stagingAreaSubnetId: str = None,
    stagingAreaTags: Dict[str, str] = None,
    useDedicatedReplicationServer: bool = None
) -> ReplicationConfigurationTypeDef:
    pass
```

### update_replication_configuration_template

Type annotations for `boto3.client("mgn").update_replication_configuration_template` method.

[Client.update_replication_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html#mgn.Client.update_replication_configuration_template)

```python
def update_replication_configuration_template(
    self,
    replicationConfigurationTemplateID: str,
    arn: str = None,
    associateDefaultSecurityGroup: bool = None,
    bandwidthThrottling: int = None,
    createPublicIP: bool = None,
    dataPlaneRouting: ReplicationConfigurationDataPlaneRouting = None,
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskType = None,
    ebsEncryption: ReplicationConfigurationEbsEncryption = None,
    ebsEncryptionKeyArn: str = None,
    replicationServerInstanceType: str = None,
    replicationServersSecurityGroupsIDs: List[str] = None,
    stagingAreaSubnetId: str = None,
    stagingAreaTags: Dict[str, str] = None,
    useDedicatedReplicationServer: bool = None
) -> "ReplicationConfigurationTemplateTypeDef":
    pass
```



### get_paginator

Type annotations for `boto3.client("mgn").get_paginator` method with overloads.

- `client.get_paginator("describe_job_log_items")` -> [DescribeJobLogItemsPaginator](./paginators.md#describejoblogitemspaginator)
- `client.get_paginator("describe_jobs")` -> [DescribeJobsPaginator](./paginators.md#describejobspaginator)
- `client.get_paginator("describe_replication_configuration_templates")` -> [DescribeReplicationConfigurationTemplatesPaginator](./paginators.md#describereplicationconfigurationtemplatespaginator)
- `client.get_paginator("describe_source_servers")` -> [DescribeSourceServersPaginator](./paginators.md#describesourceserverspaginator)


