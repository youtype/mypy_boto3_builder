# SMSClient for boto3 SMS module

> [Index](../index.md) > [SMS](./index.md) > SMSClient

Auto-generated documentation for [SMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS)
type annotations stubs module [mypy_boto3_sms](https://pypi.org/project/mypy-boto3-sms/).

- [SMSClient for boto3 SMS module](#smsclient-for-boto3-sms-module)
  - [SMSClient](#smsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_app](#create_app)
    - [create_replication_job](#create_replication_job)
    - [delete_app](#delete_app)
    - [delete_app_launch_configuration](#delete_app_launch_configuration)
    - [delete_app_replication_configuration](#delete_app_replication_configuration)
    - [delete_app_validation_configuration](#delete_app_validation_configuration)
    - [delete_replication_job](#delete_replication_job)
    - [delete_server_catalog](#delete_server_catalog)
    - [disassociate_connector](#disassociate_connector)
    - [generate_change_set](#generate_change_set)
    - [generate_presigned_url](#generate_presigned_url)
    - [generate_template](#generate_template)
    - [get_app](#get_app)
    - [get_app_launch_configuration](#get_app_launch_configuration)
    - [get_app_replication_configuration](#get_app_replication_configuration)
    - [get_app_validation_configuration](#get_app_validation_configuration)
    - [get_app_validation_output](#get_app_validation_output)
    - [get_connectors](#get_connectors)
    - [get_replication_jobs](#get_replication_jobs)
    - [get_replication_runs](#get_replication_runs)
    - [get_servers](#get_servers)
    - [import_app_catalog](#import_app_catalog)
    - [import_server_catalog](#import_server_catalog)
    - [launch_app](#launch_app)
    - [list_apps](#list_apps)
    - [notify_app_validation_output](#notify_app_validation_output)
    - [put_app_launch_configuration](#put_app_launch_configuration)
    - [put_app_replication_configuration](#put_app_replication_configuration)
    - [put_app_validation_configuration](#put_app_validation_configuration)
    - [start_app_replication](#start_app_replication)
    - [start_on_demand_app_replication](#start_on_demand_app_replication)
    - [start_on_demand_replication_run](#start_on_demand_replication_run)
    - [stop_app_replication](#stop_app_replication)
    - [terminate_app](#terminate_app)
    - [update_app](#update_app)
    - [update_replication_job](#update_replication_job)
    - [get_paginator](#get_paginator)

## SMSClient

Type annotations for `boto3.client("sms")`

Can be used directly:

```python
from mypy_boto3_sms.client import SMSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_sms.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.DryRunOperationException`
- `Exceptions.InternalError`
- `Exceptions.InvalidParameterException`
- `Exceptions.MissingRequiredParameterException`
- `Exceptions.NoConnectorsAvailableException`
- `Exceptions.OperationNotPermittedException`
- `Exceptions.ReplicationJobAlreadyExistsException`
- `Exceptions.ReplicationJobNotFoundException`
- `Exceptions.ReplicationRunLimitExceededException`
- `Exceptions.ServerCannotBeReplicatedException`
- `Exceptions.TemporarilyUnavailableException`
- `Exceptions.UnauthorizedOperationException`


## Methods


### can_paginate

Type annotations for `boto3.client("sms").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_app

Type annotations for `boto3.client("sms").create_app` method.

[Client.create_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.create_app)

```python
def create_app(
    self,
    name: str = None,
    description: str = None,
    roleName: str = None,
    clientToken: str = None,
    serverGroups: List["ServerGroupTypeDef"] = None,
    tags: List["TagTypeDef"] = None
) -> CreateAppResponseTypeDef:
    pass
```

### create_replication_job

Type annotations for `boto3.client("sms").create_replication_job` method.

[Client.create_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.create_replication_job)

```python
def create_replication_job(
    self,
    serverId: str,
    seedReplicationTime: datetime,
    frequency: int = None,
    runOnce: bool = None,
    licenseType: LicenseType = None,
    roleName: str = None,
    description: str = None,
    numberOfRecentAmisToKeep: int = None,
    encrypted: bool = None,
    kmsKeyId: str = None
) -> CreateReplicationJobResponseTypeDef:
    pass
```

### delete_app

Type annotations for `boto3.client("sms").delete_app` method.

[Client.delete_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.delete_app)

```python
def delete_app(
    self,
    appId: str = None,
    forceStopAppReplication: bool = None,
    forceTerminateApp: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_app_launch_configuration

Type annotations for `boto3.client("sms").delete_app_launch_configuration` method.

[Client.delete_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.delete_app_launch_configuration)

```python
def delete_app_launch_configuration(
    self,
    appId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_app_replication_configuration

Type annotations for `boto3.client("sms").delete_app_replication_configuration` method.

[Client.delete_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.delete_app_replication_configuration)

```python
def delete_app_replication_configuration(
    self,
    appId: str = None
) -> Dict[str, Any]:
    pass
```

### delete_app_validation_configuration

Type annotations for `boto3.client("sms").delete_app_validation_configuration` method.

[Client.delete_app_validation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.delete_app_validation_configuration)

```python
def delete_app_validation_configuration(
    self,
    appId: str
) -> Dict[str, Any]:
    pass
```

### delete_replication_job

Type annotations for `boto3.client("sms").delete_replication_job` method.

[Client.delete_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.delete_replication_job)

```python
def delete_replication_job(
    self,
    replicationJobId: str
) -> Dict[str, Any]:
    pass
```

### delete_server_catalog

Type annotations for `boto3.client("sms").delete_server_catalog` method.

[Client.delete_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.delete_server_catalog)

```python
def delete_server_catalog(
    self
) -> Dict[str, Any]:
    pass
```

### disassociate_connector

Type annotations for `boto3.client("sms").disassociate_connector` method.

[Client.disassociate_connector documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.disassociate_connector)

```python
def disassociate_connector(
    self,
    connectorId: str
) -> Dict[str, Any]:
    pass
```

### generate_change_set

Type annotations for `boto3.client("sms").generate_change_set` method.

[Client.generate_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.generate_change_set)

```python
def generate_change_set(
    self,
    appId: str = None,
    changesetFormat: OutputFormat = None
) -> GenerateChangeSetResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("sms").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.generate_presigned_url)

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

### generate_template

Type annotations for `boto3.client("sms").generate_template` method.

[Client.generate_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.generate_template)

```python
def generate_template(
    self,
    appId: str = None,
    templateFormat: OutputFormat = None
) -> GenerateTemplateResponseTypeDef:
    pass
```

### get_app

Type annotations for `boto3.client("sms").get_app` method.

[Client.get_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_app)

```python
def get_app(
    self,
    appId: str = None
) -> GetAppResponseTypeDef:
    pass
```

### get_app_launch_configuration

Type annotations for `boto3.client("sms").get_app_launch_configuration` method.

[Client.get_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_app_launch_configuration)

```python
def get_app_launch_configuration(
    self,
    appId: str = None
) -> GetAppLaunchConfigurationResponseTypeDef:
    pass
```

### get_app_replication_configuration

Type annotations for `boto3.client("sms").get_app_replication_configuration` method.

[Client.get_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_app_replication_configuration)

```python
def get_app_replication_configuration(
    self,
    appId: str = None
) -> GetAppReplicationConfigurationResponseTypeDef:
    pass
```

### get_app_validation_configuration

Type annotations for `boto3.client("sms").get_app_validation_configuration` method.

[Client.get_app_validation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_app_validation_configuration)

```python
def get_app_validation_configuration(
    self,
    appId: str
) -> GetAppValidationConfigurationResponseTypeDef:
    pass
```

### get_app_validation_output

Type annotations for `boto3.client("sms").get_app_validation_output` method.

[Client.get_app_validation_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_app_validation_output)

```python
def get_app_validation_output(
    self,
    appId: str
) -> GetAppValidationOutputResponseTypeDef:
    pass
```

### get_connectors

Type annotations for `boto3.client("sms").get_connectors` method.

[Client.get_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_connectors)

```python
def get_connectors(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> GetConnectorsResponseTypeDef:
    pass
```

### get_replication_jobs

Type annotations for `boto3.client("sms").get_replication_jobs` method.

[Client.get_replication_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_replication_jobs)

```python
def get_replication_jobs(
    self,
    replicationJobId: str = None,
    nextToken: str = None,
    maxResults: int = None
) -> GetReplicationJobsResponseTypeDef:
    pass
```

### get_replication_runs

Type annotations for `boto3.client("sms").get_replication_runs` method.

[Client.get_replication_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_replication_runs)

```python
def get_replication_runs(
    self,
    replicationJobId: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetReplicationRunsResponseTypeDef:
    pass
```

### get_servers

Type annotations for `boto3.client("sms").get_servers` method.

[Client.get_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.get_servers)

```python
def get_servers(
    self,
    nextToken: str = None,
    maxResults: int = None,
    vmServerAddressList: List["VmServerAddressTypeDef"] = None
) -> GetServersResponseTypeDef:
    pass
```

### import_app_catalog

Type annotations for `boto3.client("sms").import_app_catalog` method.

[Client.import_app_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.import_app_catalog)

```python
def import_app_catalog(
    self,
    roleName: str = None
) -> Dict[str, Any]:
    pass
```

### import_server_catalog

Type annotations for `boto3.client("sms").import_server_catalog` method.

[Client.import_server_catalog documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.import_server_catalog)

```python
def import_server_catalog(
    self
) -> Dict[str, Any]:
    pass
```

### launch_app

Type annotations for `boto3.client("sms").launch_app` method.

[Client.launch_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.launch_app)

```python
def launch_app(
    self,
    appId: str = None
) -> Dict[str, Any]:
    pass
```

### list_apps

Type annotations for `boto3.client("sms").list_apps` method.

[Client.list_apps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.list_apps)

```python
def list_apps(
    self,
    appIds: List[str] = None,
    nextToken: str = None,
    maxResults: int = None
) -> ListAppsResponseTypeDef:
    pass
```

### notify_app_validation_output

Type annotations for `boto3.client("sms").notify_app_validation_output` method.

[Client.notify_app_validation_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.notify_app_validation_output)

```python
def notify_app_validation_output(
    self,
    appId: str,
    notificationContext: NotificationContextTypeDef = None
) -> Dict[str, Any]:
    pass
```

### put_app_launch_configuration

Type annotations for `boto3.client("sms").put_app_launch_configuration` method.

[Client.put_app_launch_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.put_app_launch_configuration)

```python
def put_app_launch_configuration(
    self,
    appId: str = None,
    roleName: str = None,
    autoLaunch: bool = None,
    serverGroupLaunchConfigurations: List["ServerGroupLaunchConfigurationTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_app_replication_configuration

Type annotations for `boto3.client("sms").put_app_replication_configuration` method.

[Client.put_app_replication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.put_app_replication_configuration)

```python
def put_app_replication_configuration(
    self,
    appId: str = None,
    serverGroupReplicationConfigurations: List["ServerGroupReplicationConfigurationTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### put_app_validation_configuration

Type annotations for `boto3.client("sms").put_app_validation_configuration` method.

[Client.put_app_validation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.put_app_validation_configuration)

```python
def put_app_validation_configuration(
    self,
    appId: str,
    appValidationConfigurations: List["AppValidationConfigurationTypeDef"] = None,
    serverGroupValidationConfigurations: List["ServerGroupValidationConfigurationTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### start_app_replication

Type annotations for `boto3.client("sms").start_app_replication` method.

[Client.start_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.start_app_replication)

```python
def start_app_replication(
    self,
    appId: str = None
) -> Dict[str, Any]:
    pass
```

### start_on_demand_app_replication

Type annotations for `boto3.client("sms").start_on_demand_app_replication` method.

[Client.start_on_demand_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.start_on_demand_app_replication)

```python
def start_on_demand_app_replication(
    self,
    appId: str,
    description: str = None
) -> Dict[str, Any]:
    pass
```

### start_on_demand_replication_run

Type annotations for `boto3.client("sms").start_on_demand_replication_run` method.

[Client.start_on_demand_replication_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.start_on_demand_replication_run)

```python
def start_on_demand_replication_run(
    self,
    replicationJobId: str,
    description: str = None
) -> StartOnDemandReplicationRunResponseTypeDef:
    pass
```

### stop_app_replication

Type annotations for `boto3.client("sms").stop_app_replication` method.

[Client.stop_app_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.stop_app_replication)

```python
def stop_app_replication(
    self,
    appId: str = None
) -> Dict[str, Any]:
    pass
```

### terminate_app

Type annotations for `boto3.client("sms").terminate_app` method.

[Client.terminate_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.terminate_app)

```python
def terminate_app(
    self,
    appId: str = None
) -> Dict[str, Any]:
    pass
```

### update_app

Type annotations for `boto3.client("sms").update_app` method.

[Client.update_app documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.update_app)

```python
def update_app(
    self,
    appId: str = None,
    name: str = None,
    description: str = None,
    roleName: str = None,
    serverGroups: List["ServerGroupTypeDef"] = None,
    tags: List["TagTypeDef"] = None
) -> UpdateAppResponseTypeDef:
    pass
```

### update_replication_job

Type annotations for `boto3.client("sms").update_replication_job` method.

[Client.update_replication_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Client.update_replication_job)

```python
def update_replication_job(
    self,
    replicationJobId: str,
    frequency: int = None,
    nextReplicationRunStartTime: datetime = None,
    licenseType: LicenseType = None,
    roleName: str = None,
    description: str = None,
    numberOfRecentAmisToKeep: int = None,
    encrypted: bool = None,
    kmsKeyId: str = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("sms").get_paginator` method with overloads.

- `client.get_paginator("get_connectors")` -> [GetConnectorsPaginator](./paginators.md#getconnectorspaginator)
- `client.get_paginator("get_replication_jobs")` -> [GetReplicationJobsPaginator](./paginators.md#getreplicationjobspaginator)
- `client.get_paginator("get_replication_runs")` -> [GetReplicationRunsPaginator](./paginators.md#getreplicationrunspaginator)
- `client.get_paginator("get_servers")` -> [GetServersPaginator](./paginators.md#getserverspaginator)
- `client.get_paginator("list_apps")` -> [ListAppsPaginator](./paginators.md#listappspaginator)


