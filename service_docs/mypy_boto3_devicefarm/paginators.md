# Paginators for boto3 DeviceFarm module

> [Index](../index.md) > [DeviceFarm](./index.md) > Paginators

Auto-generated documentation for [DeviceFarm](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm)
type annotations stubs module [mypy_boto3_devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/).

- [Paginators for boto3 DeviceFarm module](#paginators-for-boto3-devicefarm-module)
  - [GetOfferingStatusPaginator](#getofferingstatuspaginator)
  - [ListArtifactsPaginator](#listartifactspaginator)
  - [ListDeviceInstancesPaginator](#listdeviceinstancespaginator)
  - [ListDevicePoolsPaginator](#listdevicepoolspaginator)
  - [ListDevicesPaginator](#listdevicespaginator)
  - [ListInstanceProfilesPaginator](#listinstanceprofilespaginator)
  - [ListJobsPaginator](#listjobspaginator)
  - [ListNetworkProfilesPaginator](#listnetworkprofilespaginator)
  - [ListOfferingPromotionsPaginator](#listofferingpromotionspaginator)
  - [ListOfferingTransactionsPaginator](#listofferingtransactionspaginator)
  - [ListOfferingsPaginator](#listofferingspaginator)
  - [ListProjectsPaginator](#listprojectspaginator)
  - [ListRemoteAccessSessionsPaginator](#listremoteaccesssessionspaginator)
  - [ListRunsPaginator](#listrunspaginator)
  - [ListSamplesPaginator](#listsamplespaginator)
  - [ListSuitesPaginator](#listsuitespaginator)
  - [ListTestsPaginator](#listtestspaginator)
  - [ListUniqueProblemsPaginator](#listuniqueproblemspaginator)
  - [ListUploadsPaginator](#listuploadspaginator)
  - [ListVPCEConfigurationsPaginator](#listvpceconfigurationspaginator)

## GetOfferingStatusPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("get_offering_status")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import GetOfferingStatusPaginator

def get_get_offering_status_paginator() -> GetOfferingStatusPaginator:
    return boto3.client("devicefarm").get_paginator("get_offering_status")
```

[Paginator.GetOfferingStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)

```python
class GetOfferingStatusPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOfferingStatusResultTypeDef]:
        pass
```
## ListArtifactsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_artifacts")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListArtifactsPaginator

def get_list_artifacts_paginator() -> ListArtifactsPaginator:
    return boto3.client("devicefarm").get_paginator("list_artifacts")
```

[Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)

```python
class ListArtifactsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        type: ArtifactCategory,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListArtifactsResultTypeDef]:
        pass
```
## ListDeviceInstancesPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_device_instances")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListDeviceInstancesPaginator

def get_list_device_instances_paginator() -> ListDeviceInstancesPaginator:
    return boto3.client("devicefarm").get_paginator("list_device_instances")
```

[Paginator.ListDeviceInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)

```python
class ListDeviceInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceInstancesResultTypeDef]:
        pass
```
## ListDevicePoolsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_device_pools")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListDevicePoolsPaginator

def get_list_device_pools_paginator() -> ListDevicePoolsPaginator:
    return boto3.client("devicefarm").get_paginator("list_device_pools")
```

[Paginator.ListDevicePools documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)

```python
class ListDevicePoolsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        type: DevicePoolType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicePoolsResultTypeDef]:
        pass
```
## ListDevicesPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_devices")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListDevicesPaginator

def get_list_devices_paginator() -> ListDevicesPaginator:
    return boto3.client("devicefarm").get_paginator("list_devices")
```

[Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)

```python
class ListDevicesPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str = None,
        filters: List["DeviceFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDevicesResultTypeDef]:
        pass
```
## ListInstanceProfilesPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_instance_profiles")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListInstanceProfilesPaginator

def get_list_instance_profiles_paginator() -> ListInstanceProfilesPaginator:
    return boto3.client("devicefarm").get_paginator("list_instance_profiles")
```

[Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)

```python
class ListInstanceProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceProfilesResultTypeDef]:
        pass
```
## ListJobsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_jobs")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListJobsPaginator

def get_list_jobs_paginator() -> ListJobsPaginator:
    return boto3.client("devicefarm").get_paginator("list_jobs")
```

[Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)

```python
class ListJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResultTypeDef]:
        pass
```
## ListNetworkProfilesPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_network_profiles")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListNetworkProfilesPaginator

def get_list_network_profiles_paginator() -> ListNetworkProfilesPaginator:
    return boto3.client("devicefarm").get_paginator("list_network_profiles")
```

[Paginator.ListNetworkProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)

```python
class ListNetworkProfilesPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        type: NetworkProfileType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNetworkProfilesResultTypeDef]:
        pass
```
## ListOfferingPromotionsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_offering_promotions")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListOfferingPromotionsPaginator

def get_list_offering_promotions_paginator() -> ListOfferingPromotionsPaginator:
    return boto3.client("devicefarm").get_paginator("list_offering_promotions")
```

[Paginator.ListOfferingPromotions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)

```python
class ListOfferingPromotionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingPromotionsResultTypeDef]:
        pass
```
## ListOfferingTransactionsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_offering_transactions")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListOfferingTransactionsPaginator

def get_list_offering_transactions_paginator() -> ListOfferingTransactionsPaginator:
    return boto3.client("devicefarm").get_paginator("list_offering_transactions")
```

[Paginator.ListOfferingTransactions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)

```python
class ListOfferingTransactionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingTransactionsResultTypeDef]:
        pass
```
## ListOfferingsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_offerings")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListOfferingsPaginator

def get_list_offerings_paginator() -> ListOfferingsPaginator:
    return boto3.client("devicefarm").get_paginator("list_offerings")
```

[Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)

```python
class ListOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingsResultTypeDef]:
        pass
```
## ListProjectsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_projects")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListProjectsPaginator

def get_list_projects_paginator() -> ListProjectsPaginator:
    return boto3.client("devicefarm").get_paginator("list_projects")
```

[Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)

```python
class ListProjectsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        pass
```
## ListRemoteAccessSessionsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_remote_access_sessions")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListRemoteAccessSessionsPaginator

def get_list_remote_access_sessions_paginator() -> ListRemoteAccessSessionsPaginator:
    return boto3.client("devicefarm").get_paginator("list_remote_access_sessions")
```

[Paginator.ListRemoteAccessSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)

```python
class ListRemoteAccessSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRemoteAccessSessionsResultTypeDef]:
        pass
```
## ListRunsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_runs")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListRunsPaginator

def get_list_runs_paginator() -> ListRunsPaginator:
    return boto3.client("devicefarm").get_paginator("list_runs")
```

[Paginator.ListRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)

```python
class ListRunsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRunsResultTypeDef]:
        pass
```
## ListSamplesPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_samples")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListSamplesPaginator

def get_list_samples_paginator() -> ListSamplesPaginator:
    return boto3.client("devicefarm").get_paginator("list_samples")
```

[Paginator.ListSamples documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)

```python
class ListSamplesPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSamplesResultTypeDef]:
        pass
```
## ListSuitesPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_suites")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListSuitesPaginator

def get_list_suites_paginator() -> ListSuitesPaginator:
    return boto3.client("devicefarm").get_paginator("list_suites")
```

[Paginator.ListSuites documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)

```python
class ListSuitesPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSuitesResultTypeDef]:
        pass
```
## ListTestsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_tests")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListTestsPaginator

def get_list_tests_paginator() -> ListTestsPaginator:
    return boto3.client("devicefarm").get_paginator("list_tests")
```

[Paginator.ListTests documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)

```python
class ListTestsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestsResultTypeDef]:
        pass
```
## ListUniqueProblemsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_unique_problems")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListUniqueProblemsPaginator

def get_list_unique_problems_paginator() -> ListUniqueProblemsPaginator:
    return boto3.client("devicefarm").get_paginator("list_unique_problems")
```

[Paginator.ListUniqueProblems documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)

```python
class ListUniqueProblemsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUniqueProblemsResultTypeDef]:
        pass
```
## ListUploadsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_uploads")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListUploadsPaginator

def get_list_uploads_paginator() -> ListUploadsPaginator:
    return boto3.client("devicefarm").get_paginator("list_uploads")
```

[Paginator.ListUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)

```python
class ListUploadsPaginator(Boto3Paginator):
    def paginate(
        self,
        arn: str,
        type: UploadType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUploadsResultTypeDef]:
        pass
```
## ListVPCEConfigurationsPaginator

Type annotations for `boto3.client("devicefarm").get_paginator("list_vpce_configurations")`.

Can be used directly:

```python
from mypy_boto3_devicefarm.paginators import ListVPCEConfigurationsPaginator

def get_list_vpce_configurations_paginator() -> ListVPCEConfigurationsPaginator:
    return boto3.client("devicefarm").get_paginator("list_vpce_configurations")
```

[Paginator.ListVPCEConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)

```python
class ListVPCEConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVPCEConfigurationsResultTypeDef]:
        pass
```