# DeviceFarmClient for boto3 DeviceFarm module

> [Index](../index.md) > [DeviceFarm](./index.md) > DeviceFarmClient

Auto-generated documentation for [DeviceFarm](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm)
type annotations stubs module [mypy_boto3_devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/).

- [DeviceFarmClient for boto3 DeviceFarm module](#devicefarmclient-for-boto3-devicefarm-module)
  - [DeviceFarmClient](#devicefarmclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_device_pool](#create_device_pool)
    - [create_instance_profile](#create_instance_profile)
    - [create_network_profile](#create_network_profile)
    - [create_project](#create_project)
    - [create_remote_access_session](#create_remote_access_session)
    - [create_test_grid_project](#create_test_grid_project)
    - [create_test_grid_url](#create_test_grid_url)
    - [create_upload](#create_upload)
    - [create_vpce_configuration](#create_vpce_configuration)
    - [delete_device_pool](#delete_device_pool)
    - [delete_instance_profile](#delete_instance_profile)
    - [delete_network_profile](#delete_network_profile)
    - [delete_project](#delete_project)
    - [delete_remote_access_session](#delete_remote_access_session)
    - [delete_run](#delete_run)
    - [delete_test_grid_project](#delete_test_grid_project)
    - [delete_upload](#delete_upload)
    - [delete_vpce_configuration](#delete_vpce_configuration)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_settings](#get_account_settings)
    - [get_device](#get_device)
    - [get_device_instance](#get_device_instance)
    - [get_device_pool](#get_device_pool)
    - [get_device_pool_compatibility](#get_device_pool_compatibility)
    - [get_instance_profile](#get_instance_profile)
    - [get_job](#get_job)
    - [get_network_profile](#get_network_profile)
    - [get_offering_status](#get_offering_status)
    - [get_project](#get_project)
    - [get_remote_access_session](#get_remote_access_session)
    - [get_run](#get_run)
    - [get_suite](#get_suite)
    - [get_test](#get_test)
    - [get_test_grid_project](#get_test_grid_project)
    - [get_test_grid_session](#get_test_grid_session)
    - [get_upload](#get_upload)
    - [get_vpce_configuration](#get_vpce_configuration)
    - [install_to_remote_access_session](#install_to_remote_access_session)
    - [list_artifacts](#list_artifacts)
    - [list_device_instances](#list_device_instances)
    - [list_device_pools](#list_device_pools)
    - [list_devices](#list_devices)
    - [list_instance_profiles](#list_instance_profiles)
    - [list_jobs](#list_jobs)
    - [list_network_profiles](#list_network_profiles)
    - [list_offering_promotions](#list_offering_promotions)
    - [list_offering_transactions](#list_offering_transactions)
    - [list_offerings](#list_offerings)
    - [list_projects](#list_projects)
    - [list_remote_access_sessions](#list_remote_access_sessions)
    - [list_runs](#list_runs)
    - [list_samples](#list_samples)
    - [list_suites](#list_suites)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_test_grid_projects](#list_test_grid_projects)
    - [list_test_grid_session_actions](#list_test_grid_session_actions)
    - [list_test_grid_session_artifacts](#list_test_grid_session_artifacts)
    - [list_test_grid_sessions](#list_test_grid_sessions)
    - [list_tests](#list_tests)
    - [list_unique_problems](#list_unique_problems)
    - [list_uploads](#list_uploads)
    - [list_vpce_configurations](#list_vpce_configurations)
    - [purchase_offering](#purchase_offering)
    - [renew_offering](#renew_offering)
    - [schedule_run](#schedule_run)
    - [stop_job](#stop_job)
    - [stop_remote_access_session](#stop_remote_access_session)
    - [stop_run](#stop_run)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_device_instance](#update_device_instance)
    - [update_device_pool](#update_device_pool)
    - [update_instance_profile](#update_instance_profile)
    - [update_network_profile](#update_network_profile)
    - [update_project](#update_project)
    - [update_test_grid_project](#update_test_grid_project)
    - [update_upload](#update_upload)
    - [update_vpce_configuration](#update_vpce_configuration)
    - [get_paginator](#get_paginator)

## DeviceFarmClient

Type annotations for `boto3.client("devicefarm")`

Can be used directly:

```python
from mypy_boto3_devicefarm.client import DeviceFarmClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_devicefarm.client import Exceptions

def handle_error(exc: Exceptions.ArgumentException) -> None:
    ...
```


Exceptions:

- `Exceptions.ArgumentException`
- `Exceptions.CannotDeleteException`
- `Exceptions.ClientError`
- `Exceptions.IdempotencyException`
- `Exceptions.InternalServiceException`
- `Exceptions.InvalidOperationException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotEligibleException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceAccountException`
- `Exceptions.TagOperationException`
- `Exceptions.TagPolicyException`
- `Exceptions.TooManyTagsException`


## Methods


### can_paginate

Type annotations for `boto3.client("devicefarm").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_device_pool

Type annotations for `boto3.client("devicefarm").create_device_pool` method.

[Client.create_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_device_pool)

```python
def create_device_pool(
    self,
    projectArn: str,
    name: str,
    rules: List["RuleTypeDef"],
    description: str = None,
    maxDevices: int = None
) -> CreateDevicePoolResultTypeDef:
    pass
```

### create_instance_profile

Type annotations for `boto3.client("devicefarm").create_instance_profile` method.

[Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_instance_profile)

```python
def create_instance_profile(
    self,
    name: str,
    description: str = None,
    packageCleanup: bool = None,
    excludeAppPackagesFromCleanup: List[str] = None,
    rebootAfterUse: bool = None
) -> CreateInstanceProfileResultTypeDef:
    pass
```

### create_network_profile

Type annotations for `boto3.client("devicefarm").create_network_profile` method.

[Client.create_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_network_profile)

```python
def create_network_profile(
    self,
    projectArn: str,
    name: str,
    description: str = None,
    type: NetworkProfileType = None,
    uplinkBandwidthBits: int = None,
    downlinkBandwidthBits: int = None,
    uplinkDelayMs: int = None,
    downlinkDelayMs: int = None,
    uplinkJitterMs: int = None,
    downlinkJitterMs: int = None,
    uplinkLossPercent: int = None,
    downlinkLossPercent: int = None
) -> CreateNetworkProfileResultTypeDef:
    pass
```

### create_project

Type annotations for `boto3.client("devicefarm").create_project` method.

[Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_project)

```python
def create_project(
    self,
    name: str,
    defaultJobTimeoutMinutes: int = None
) -> CreateProjectResultTypeDef:
    pass
```

### create_remote_access_session

Type annotations for `boto3.client("devicefarm").create_remote_access_session` method.

[Client.create_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_remote_access_session)

```python
def create_remote_access_session(
    self,
    projectArn: str,
    deviceArn: str,
    instanceArn: str = None,
    sshPublicKey: str = None,
    remoteDebugEnabled: bool = None,
    remoteRecordEnabled: bool = None,
    remoteRecordAppArn: str = None,
    name: str = None,
    clientId: str = None,
    configuration: CreateRemoteAccessSessionConfigurationTypeDef = None,
    interactionMode: InteractionMode = None,
    skipAppResign: bool = None
) -> CreateRemoteAccessSessionResultTypeDef:
    pass
```

### create_test_grid_project

Type annotations for `boto3.client("devicefarm").create_test_grid_project` method.

[Client.create_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_project)

```python
def create_test_grid_project(
    self,
    name: str,
    description: str = None
) -> CreateTestGridProjectResultTypeDef:
    pass
```

### create_test_grid_url

Type annotations for `boto3.client("devicefarm").create_test_grid_url` method.

[Client.create_test_grid_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_url)

```python
def create_test_grid_url(
    self,
    projectArn: str,
    expiresInSeconds: int
) -> CreateTestGridUrlResultTypeDef:
    pass
```

### create_upload

Type annotations for `boto3.client("devicefarm").create_upload` method.

[Client.create_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_upload)

```python
def create_upload(
    self,
    projectArn: str,
    name: str,
    type: UploadType,
    contentType: str = None
) -> CreateUploadResultTypeDef:
    pass
```

### create_vpce_configuration

Type annotations for `boto3.client("devicefarm").create_vpce_configuration` method.

[Client.create_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.create_vpce_configuration)

```python
def create_vpce_configuration(
    self,
    vpceConfigurationName: str,
    vpceServiceName: str,
    serviceDnsName: str,
    vpceConfigurationDescription: str = None
) -> CreateVPCEConfigurationResultTypeDef:
    pass
```

### delete_device_pool

Type annotations for `boto3.client("devicefarm").delete_device_pool` method.

[Client.delete_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_device_pool)

```python
def delete_device_pool(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_instance_profile

Type annotations for `boto3.client("devicefarm").delete_instance_profile` method.

[Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_instance_profile)

```python
def delete_instance_profile(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_network_profile

Type annotations for `boto3.client("devicefarm").delete_network_profile` method.

[Client.delete_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_network_profile)

```python
def delete_network_profile(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_project

Type annotations for `boto3.client("devicefarm").delete_project` method.

[Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_project)

```python
def delete_project(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_remote_access_session

Type annotations for `boto3.client("devicefarm").delete_remote_access_session` method.

[Client.delete_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_remote_access_session)

```python
def delete_remote_access_session(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_run

Type annotations for `boto3.client("devicefarm").delete_run` method.

[Client.delete_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_run)

```python
def delete_run(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_test_grid_project

Type annotations for `boto3.client("devicefarm").delete_test_grid_project` method.

[Client.delete_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_test_grid_project)

```python
def delete_test_grid_project(
    self,
    projectArn: str
) -> Dict[str, Any]:
    pass
```

### delete_upload

Type annotations for `boto3.client("devicefarm").delete_upload` method.

[Client.delete_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_upload)

```python
def delete_upload(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### delete_vpce_configuration

Type annotations for `boto3.client("devicefarm").delete_vpce_configuration` method.

[Client.delete_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.delete_vpce_configuration)

```python
def delete_vpce_configuration(
    self,
    arn: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("devicefarm").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.generate_presigned_url)

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

### get_account_settings

Type annotations for `boto3.client("devicefarm").get_account_settings` method.

[Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_account_settings)

```python
def get_account_settings(
    self
) -> GetAccountSettingsResultTypeDef:
    pass
```

### get_device

Type annotations for `boto3.client("devicefarm").get_device` method.

[Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device)

```python
def get_device(
    self,
    arn: str
) -> GetDeviceResultTypeDef:
    pass
```

### get_device_instance

Type annotations for `boto3.client("devicefarm").get_device_instance` method.

[Client.get_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device_instance)

```python
def get_device_instance(
    self,
    arn: str
) -> GetDeviceInstanceResultTypeDef:
    pass
```

### get_device_pool

Type annotations for `boto3.client("devicefarm").get_device_pool` method.

[Client.get_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool)

```python
def get_device_pool(
    self,
    arn: str
) -> GetDevicePoolResultTypeDef:
    pass
```

### get_device_pool_compatibility

Type annotations for `boto3.client("devicefarm").get_device_pool_compatibility` method.

[Client.get_device_pool_compatibility documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool_compatibility)

```python
def get_device_pool_compatibility(
    self,
    devicePoolArn: str,
    appArn: str = None,
    testType: TestType = None,
    test: ScheduleRunTestTypeDef = None,
    configuration: ScheduleRunConfigurationTypeDef = None
) -> GetDevicePoolCompatibilityResultTypeDef:
    pass
```

### get_instance_profile

Type annotations for `boto3.client("devicefarm").get_instance_profile` method.

[Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_instance_profile)

```python
def get_instance_profile(
    self,
    arn: str
) -> GetInstanceProfileResultTypeDef:
    pass
```

### get_job

Type annotations for `boto3.client("devicefarm").get_job` method.

[Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_job)

```python
def get_job(
    self,
    arn: str
) -> GetJobResultTypeDef:
    pass
```

### get_network_profile

Type annotations for `boto3.client("devicefarm").get_network_profile` method.

[Client.get_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_network_profile)

```python
def get_network_profile(
    self,
    arn: str
) -> GetNetworkProfileResultTypeDef:
    pass
```

### get_offering_status

Type annotations for `boto3.client("devicefarm").get_offering_status` method.

[Client.get_offering_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_offering_status)

```python
def get_offering_status(
    self,
    nextToken: str = None
) -> GetOfferingStatusResultTypeDef:
    pass
```

### get_project

Type annotations for `boto3.client("devicefarm").get_project` method.

[Client.get_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_project)

```python
def get_project(
    self,
    arn: str
) -> GetProjectResultTypeDef:
    pass
```

### get_remote_access_session

Type annotations for `boto3.client("devicefarm").get_remote_access_session` method.

[Client.get_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_remote_access_session)

```python
def get_remote_access_session(
    self,
    arn: str
) -> GetRemoteAccessSessionResultTypeDef:
    pass
```

### get_run

Type annotations for `boto3.client("devicefarm").get_run` method.

[Client.get_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_run)

```python
def get_run(
    self,
    arn: str
) -> GetRunResultTypeDef:
    pass
```

### get_suite

Type annotations for `boto3.client("devicefarm").get_suite` method.

[Client.get_suite documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_suite)

```python
def get_suite(
    self,
    arn: str
) -> GetSuiteResultTypeDef:
    pass
```

### get_test

Type annotations for `boto3.client("devicefarm").get_test` method.

[Client.get_test documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_test)

```python
def get_test(
    self,
    arn: str
) -> GetTestResultTypeDef:
    pass
```

### get_test_grid_project

Type annotations for `boto3.client("devicefarm").get_test_grid_project` method.

[Client.get_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_project)

```python
def get_test_grid_project(
    self,
    projectArn: str
) -> GetTestGridProjectResultTypeDef:
    pass
```

### get_test_grid_session

Type annotations for `boto3.client("devicefarm").get_test_grid_session` method.

[Client.get_test_grid_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_session)

```python
def get_test_grid_session(
    self,
    projectArn: str = None,
    sessionId: str = None,
    sessionArn: str = None
) -> GetTestGridSessionResultTypeDef:
    pass
```

### get_upload

Type annotations for `boto3.client("devicefarm").get_upload` method.

[Client.get_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_upload)

```python
def get_upload(
    self,
    arn: str
) -> GetUploadResultTypeDef:
    pass
```

### get_vpce_configuration

Type annotations for `boto3.client("devicefarm").get_vpce_configuration` method.

[Client.get_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.get_vpce_configuration)

```python
def get_vpce_configuration(
    self,
    arn: str
) -> GetVPCEConfigurationResultTypeDef:
    pass
```

### install_to_remote_access_session

Type annotations for `boto3.client("devicefarm").install_to_remote_access_session` method.

[Client.install_to_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.install_to_remote_access_session)

```python
def install_to_remote_access_session(
    self,
    remoteAccessSessionArn: str,
    appArn: str
) -> InstallToRemoteAccessSessionResultTypeDef:
    pass
```

### list_artifacts

Type annotations for `boto3.client("devicefarm").list_artifacts` method.

[Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_artifacts)

```python
def list_artifacts(
    self,
    arn: str,
    type: ArtifactCategory,
    nextToken: str = None
) -> ListArtifactsResultTypeDef:
    pass
```

### list_device_instances

Type annotations for `boto3.client("devicefarm").list_device_instances` method.

[Client.list_device_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_device_instances)

```python
def list_device_instances(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListDeviceInstancesResultTypeDef:
    pass
```

### list_device_pools

Type annotations for `boto3.client("devicefarm").list_device_pools` method.

[Client.list_device_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_device_pools)

```python
def list_device_pools(
    self,
    arn: str,
    type: DevicePoolType = None,
    nextToken: str = None
) -> ListDevicePoolsResultTypeDef:
    pass
```

### list_devices

Type annotations for `boto3.client("devicefarm").list_devices` method.

[Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_devices)

```python
def list_devices(
    self,
    arn: str = None,
    nextToken: str = None,
    filters: List["DeviceFilterTypeDef"] = None
) -> ListDevicesResultTypeDef:
    pass
```

### list_instance_profiles

Type annotations for `boto3.client("devicefarm").list_instance_profiles` method.

[Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_instance_profiles)

```python
def list_instance_profiles(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListInstanceProfilesResultTypeDef:
    pass
```

### list_jobs

Type annotations for `boto3.client("devicefarm").list_jobs` method.

[Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_jobs)

```python
def list_jobs(
    self,
    arn: str,
    nextToken: str = None
) -> ListJobsResultTypeDef:
    pass
```

### list_network_profiles

Type annotations for `boto3.client("devicefarm").list_network_profiles` method.

[Client.list_network_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_network_profiles)

```python
def list_network_profiles(
    self,
    arn: str,
    type: NetworkProfileType = None,
    nextToken: str = None
) -> ListNetworkProfilesResultTypeDef:
    pass
```

### list_offering_promotions

Type annotations for `boto3.client("devicefarm").list_offering_promotions` method.

[Client.list_offering_promotions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_promotions)

```python
def list_offering_promotions(
    self,
    nextToken: str = None
) -> ListOfferingPromotionsResultTypeDef:
    pass
```

### list_offering_transactions

Type annotations for `boto3.client("devicefarm").list_offering_transactions` method.

[Client.list_offering_transactions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_transactions)

```python
def list_offering_transactions(
    self,
    nextToken: str = None
) -> ListOfferingTransactionsResultTypeDef:
    pass
```

### list_offerings

Type annotations for `boto3.client("devicefarm").list_offerings` method.

[Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_offerings)

```python
def list_offerings(
    self,
    nextToken: str = None
) -> ListOfferingsResultTypeDef:
    pass
```

### list_projects

Type annotations for `boto3.client("devicefarm").list_projects` method.

[Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_projects)

```python
def list_projects(
    self,
    arn: str = None,
    nextToken: str = None
) -> ListProjectsResultTypeDef:
    pass
```

### list_remote_access_sessions

Type annotations for `boto3.client("devicefarm").list_remote_access_sessions` method.

[Client.list_remote_access_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_remote_access_sessions)

```python
def list_remote_access_sessions(
    self,
    arn: str,
    nextToken: str = None
) -> ListRemoteAccessSessionsResultTypeDef:
    pass
```

### list_runs

Type annotations for `boto3.client("devicefarm").list_runs` method.

[Client.list_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_runs)

```python
def list_runs(
    self,
    arn: str,
    nextToken: str = None
) -> ListRunsResultTypeDef:
    pass
```

### list_samples

Type annotations for `boto3.client("devicefarm").list_samples` method.

[Client.list_samples documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_samples)

```python
def list_samples(
    self,
    arn: str,
    nextToken: str = None
) -> ListSamplesResultTypeDef:
    pass
```

### list_suites

Type annotations for `boto3.client("devicefarm").list_suites` method.

[Client.list_suites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_suites)

```python
def list_suites(
    self,
    arn: str,
    nextToken: str = None
) -> ListSuitesResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("devicefarm").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_test_grid_projects

Type annotations for `boto3.client("devicefarm").list_test_grid_projects` method.

[Client.list_test_grid_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_projects)

```python
def list_test_grid_projects(
    self,
    maxResult: int = None,
    nextToken: str = None
) -> ListTestGridProjectsResultTypeDef:
    pass
```

### list_test_grid_session_actions

Type annotations for `boto3.client("devicefarm").list_test_grid_session_actions` method.

[Client.list_test_grid_session_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_actions)

```python
def list_test_grid_session_actions(
    self,
    sessionArn: str,
    maxResult: int = None,
    nextToken: str = None
) -> ListTestGridSessionActionsResultTypeDef:
    pass
```

### list_test_grid_session_artifacts

Type annotations for `boto3.client("devicefarm").list_test_grid_session_artifacts` method.

[Client.list_test_grid_session_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_artifacts)

```python
def list_test_grid_session_artifacts(
    self,
    sessionArn: str,
    type: TestGridSessionArtifactCategory = None,
    maxResult: int = None,
    nextToken: str = None
) -> ListTestGridSessionArtifactsResultTypeDef:
    pass
```

### list_test_grid_sessions

Type annotations for `boto3.client("devicefarm").list_test_grid_sessions` method.

[Client.list_test_grid_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_sessions)

```python
def list_test_grid_sessions(
    self,
    projectArn: str,
    status: TestGridSessionStatus = None,
    creationTimeAfter: datetime = None,
    creationTimeBefore: datetime = None,
    endTimeAfter: datetime = None,
    endTimeBefore: datetime = None,
    maxResult: int = None,
    nextToken: str = None
) -> ListTestGridSessionsResultTypeDef:
    pass
```

### list_tests

Type annotations for `boto3.client("devicefarm").list_tests` method.

[Client.list_tests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_tests)

```python
def list_tests(
    self,
    arn: str,
    nextToken: str = None
) -> ListTestsResultTypeDef:
    pass
```

### list_unique_problems

Type annotations for `boto3.client("devicefarm").list_unique_problems` method.

[Client.list_unique_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_unique_problems)

```python
def list_unique_problems(
    self,
    arn: str,
    nextToken: str = None
) -> ListUniqueProblemsResultTypeDef:
    pass
```

### list_uploads

Type annotations for `boto3.client("devicefarm").list_uploads` method.

[Client.list_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_uploads)

```python
def list_uploads(
    self,
    arn: str,
    type: UploadType = None,
    nextToken: str = None
) -> ListUploadsResultTypeDef:
    pass
```

### list_vpce_configurations

Type annotations for `boto3.client("devicefarm").list_vpce_configurations` method.

[Client.list_vpce_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.list_vpce_configurations)

```python
def list_vpce_configurations(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListVPCEConfigurationsResultTypeDef:
    pass
```

### purchase_offering

Type annotations for `boto3.client("devicefarm").purchase_offering` method.

[Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.purchase_offering)

```python
def purchase_offering(
    self,
    offeringId: str = None,
    quantity: int = None,
    offeringPromotionId: str = None
) -> PurchaseOfferingResultTypeDef:
    pass
```

### renew_offering

Type annotations for `boto3.client("devicefarm").renew_offering` method.

[Client.renew_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.renew_offering)

```python
def renew_offering(
    self,
    offeringId: str = None,
    quantity: int = None
) -> RenewOfferingResultTypeDef:
    pass
```

### schedule_run

Type annotations for `boto3.client("devicefarm").schedule_run` method.

[Client.schedule_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.schedule_run)

```python
def schedule_run(
    self,
    projectArn: str,
    test: ScheduleRunTestTypeDef,
    appArn: str = None,
    devicePoolArn: str = None,
    deviceSelectionConfiguration: DeviceSelectionConfigurationTypeDef = None,
    name: str = None,
    configuration: ScheduleRunConfigurationTypeDef = None,
    executionConfiguration: ExecutionConfigurationTypeDef = None
) -> ScheduleRunResultTypeDef:
    pass
```

### stop_job

Type annotations for `boto3.client("devicefarm").stop_job` method.

[Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.stop_job)

```python
def stop_job(
    self,
    arn: str
) -> StopJobResultTypeDef:
    pass
```

### stop_remote_access_session

Type annotations for `boto3.client("devicefarm").stop_remote_access_session` method.

[Client.stop_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.stop_remote_access_session)

```python
def stop_remote_access_session(
    self,
    arn: str
) -> StopRemoteAccessSessionResultTypeDef:
    pass
```

### stop_run

Type annotations for `boto3.client("devicefarm").stop_run` method.

[Client.stop_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.stop_run)

```python
def stop_run(
    self,
    arn: str
) -> StopRunResultTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("devicefarm").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("devicefarm").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_device_instance

Type annotations for `boto3.client("devicefarm").update_device_instance` method.

[Client.update_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_device_instance)

```python
def update_device_instance(
    self,
    arn: str,
    profileArn: str = None,
    labels: List[str] = None
) -> UpdateDeviceInstanceResultTypeDef:
    pass
```

### update_device_pool

Type annotations for `boto3.client("devicefarm").update_device_pool` method.

[Client.update_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_device_pool)

```python
def update_device_pool(
    self,
    arn: str,
    name: str = None,
    description: str = None,
    rules: List["RuleTypeDef"] = None,
    maxDevices: int = None,
    clearMaxDevices: bool = None
) -> UpdateDevicePoolResultTypeDef:
    pass
```

### update_instance_profile

Type annotations for `boto3.client("devicefarm").update_instance_profile` method.

[Client.update_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_instance_profile)

```python
def update_instance_profile(
    self,
    arn: str,
    name: str = None,
    description: str = None,
    packageCleanup: bool = None,
    excludeAppPackagesFromCleanup: List[str] = None,
    rebootAfterUse: bool = None
) -> UpdateInstanceProfileResultTypeDef:
    pass
```

### update_network_profile

Type annotations for `boto3.client("devicefarm").update_network_profile` method.

[Client.update_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_network_profile)

```python
def update_network_profile(
    self,
    arn: str,
    name: str = None,
    description: str = None,
    type: NetworkProfileType = None,
    uplinkBandwidthBits: int = None,
    downlinkBandwidthBits: int = None,
    uplinkDelayMs: int = None,
    downlinkDelayMs: int = None,
    uplinkJitterMs: int = None,
    downlinkJitterMs: int = None,
    uplinkLossPercent: int = None,
    downlinkLossPercent: int = None
) -> UpdateNetworkProfileResultTypeDef:
    pass
```

### update_project

Type annotations for `boto3.client("devicefarm").update_project` method.

[Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_project)

```python
def update_project(
    self,
    arn: str,
    name: str = None,
    defaultJobTimeoutMinutes: int = None
) -> UpdateProjectResultTypeDef:
    pass
```

### update_test_grid_project

Type annotations for `boto3.client("devicefarm").update_test_grid_project` method.

[Client.update_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_test_grid_project)

```python
def update_test_grid_project(
    self,
    projectArn: str,
    name: str = None,
    description: str = None
) -> UpdateTestGridProjectResultTypeDef:
    pass
```

### update_upload

Type annotations for `boto3.client("devicefarm").update_upload` method.

[Client.update_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_upload)

```python
def update_upload(
    self,
    arn: str,
    name: str = None,
    contentType: str = None,
    editContent: bool = None
) -> UpdateUploadResultTypeDef:
    pass
```

### update_vpce_configuration

Type annotations for `boto3.client("devicefarm").update_vpce_configuration` method.

[Client.update_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client.update_vpce_configuration)

```python
def update_vpce_configuration(
    self,
    arn: str,
    vpceConfigurationName: str = None,
    vpceServiceName: str = None,
    serviceDnsName: str = None,
    vpceConfigurationDescription: str = None
) -> UpdateVPCEConfigurationResultTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("devicefarm").get_paginator` method with overloads.

- `client.get_paginator("get_offering_status")` -> [GetOfferingStatusPaginator](./paginators.md#getofferingstatuspaginator)
- `client.get_paginator("list_artifacts")` -> [ListArtifactsPaginator](./paginators.md#listartifactspaginator)
- `client.get_paginator("list_device_instances")` -> [ListDeviceInstancesPaginator](./paginators.md#listdeviceinstancespaginator)
- `client.get_paginator("list_device_pools")` -> [ListDevicePoolsPaginator](./paginators.md#listdevicepoolspaginator)
- `client.get_paginator("list_devices")` -> [ListDevicesPaginator](./paginators.md#listdevicespaginator)
- `client.get_paginator("list_instance_profiles")` -> [ListInstanceProfilesPaginator](./paginators.md#listinstanceprofilespaginator)
- `client.get_paginator("list_jobs")` -> [ListJobsPaginator](./paginators.md#listjobspaginator)
- `client.get_paginator("list_network_profiles")` -> [ListNetworkProfilesPaginator](./paginators.md#listnetworkprofilespaginator)
- `client.get_paginator("list_offering_promotions")` -> [ListOfferingPromotionsPaginator](./paginators.md#listofferingpromotionspaginator)
- `client.get_paginator("list_offering_transactions")` -> [ListOfferingTransactionsPaginator](./paginators.md#listofferingtransactionspaginator)
- `client.get_paginator("list_offerings")` -> [ListOfferingsPaginator](./paginators.md#listofferingspaginator)
- `client.get_paginator("list_projects")` -> [ListProjectsPaginator](./paginators.md#listprojectspaginator)
- `client.get_paginator("list_remote_access_sessions")` -> [ListRemoteAccessSessionsPaginator](./paginators.md#listremoteaccesssessionspaginator)
- `client.get_paginator("list_runs")` -> [ListRunsPaginator](./paginators.md#listrunspaginator)
- `client.get_paginator("list_samples")` -> [ListSamplesPaginator](./paginators.md#listsamplespaginator)
- `client.get_paginator("list_suites")` -> [ListSuitesPaginator](./paginators.md#listsuitespaginator)
- `client.get_paginator("list_tests")` -> [ListTestsPaginator](./paginators.md#listtestspaginator)
- `client.get_paginator("list_unique_problems")` -> [ListUniqueProblemsPaginator](./paginators.md#listuniqueproblemspaginator)
- `client.get_paginator("list_uploads")` -> [ListUploadsPaginator](./paginators.md#listuploadspaginator)
- `client.get_paginator("list_vpce_configurations")` -> [ListVPCEConfigurationsPaginator](./paginators.md#listvpceconfigurationspaginator)


