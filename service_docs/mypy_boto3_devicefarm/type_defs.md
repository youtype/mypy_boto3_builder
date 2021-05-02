# Structures for boto3 DeviceFarm module

> [Index](../index.md) > [DeviceFarm](./index.md) > Structures

Auto-generated documentation for [DeviceFarm](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm)
type annotations stubs module [mypy_boto3_devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/).

- [Structures for boto3 DeviceFarm module](#structures-for-boto3-devicefarm-module)
  - [AccountSettingsTypeDef](#accountsettingstypedef)
  - [ArtifactTypeDef](#artifacttypedef)
  - [CPUTypeDef](#cputypedef)
  - [CountersTypeDef](#counterstypedef)
  - [CreateDevicePoolResultTypeDef](#createdevicepoolresulttypedef)
  - [CreateInstanceProfileResultTypeDef](#createinstanceprofileresulttypedef)
  - [CreateNetworkProfileResultTypeDef](#createnetworkprofileresulttypedef)
  - [CreateProjectResultTypeDef](#createprojectresulttypedef)
  - [CreateRemoteAccessSessionConfigurationTypeDef](#createremoteaccesssessionconfigurationtypedef)
  - [CreateRemoteAccessSessionResultTypeDef](#createremoteaccesssessionresulttypedef)
  - [CreateTestGridProjectResultTypeDef](#createtestgridprojectresulttypedef)
  - [CreateTestGridUrlResultTypeDef](#createtestgridurlresulttypedef)
  - [CreateUploadResultTypeDef](#createuploadresulttypedef)
  - [CreateVPCEConfigurationResultTypeDef](#createvpceconfigurationresulttypedef)
  - [CustomerArtifactPathsTypeDef](#customerartifactpathstypedef)
  - [DeviceFilterTypeDef](#devicefiltertypedef)
  - [DeviceInstanceTypeDef](#deviceinstancetypedef)
  - [DeviceMinutesTypeDef](#deviceminutestypedef)
  - [DevicePoolCompatibilityResultTypeDef](#devicepoolcompatibilityresulttypedef)
  - [DevicePoolTypeDef](#devicepooltypedef)
  - [DeviceSelectionConfigurationTypeDef](#deviceselectionconfigurationtypedef)
  - [DeviceSelectionResultTypeDef](#deviceselectionresulttypedef)
  - [DeviceTypeDef](#devicetypedef)
  - [ExecutionConfigurationTypeDef](#executionconfigurationtypedef)
  - [GetAccountSettingsResultTypeDef](#getaccountsettingsresulttypedef)
  - [GetDeviceInstanceResultTypeDef](#getdeviceinstanceresulttypedef)
  - [GetDevicePoolCompatibilityResultTypeDef](#getdevicepoolcompatibilityresulttypedef)
  - [GetDevicePoolResultTypeDef](#getdevicepoolresulttypedef)
  - [GetDeviceResultTypeDef](#getdeviceresulttypedef)
  - [GetInstanceProfileResultTypeDef](#getinstanceprofileresulttypedef)
  - [GetJobResultTypeDef](#getjobresulttypedef)
  - [GetNetworkProfileResultTypeDef](#getnetworkprofileresulttypedef)
  - [GetOfferingStatusResultTypeDef](#getofferingstatusresulttypedef)
  - [GetProjectResultTypeDef](#getprojectresulttypedef)
  - [GetRemoteAccessSessionResultTypeDef](#getremoteaccesssessionresulttypedef)
  - [GetRunResultTypeDef](#getrunresulttypedef)
  - [GetSuiteResultTypeDef](#getsuiteresulttypedef)
  - [GetTestGridProjectResultTypeDef](#gettestgridprojectresulttypedef)
  - [GetTestGridSessionResultTypeDef](#gettestgridsessionresulttypedef)
  - [GetTestResultTypeDef](#gettestresulttypedef)
  - [GetUploadResultTypeDef](#getuploadresulttypedef)
  - [GetVPCEConfigurationResultTypeDef](#getvpceconfigurationresulttypedef)
  - [IncompatibilityMessageTypeDef](#incompatibilitymessagetypedef)
  - [InstallToRemoteAccessSessionResultTypeDef](#installtoremoteaccesssessionresulttypedef)
  - [InstanceProfileTypeDef](#instanceprofiletypedef)
  - [JobTypeDef](#jobtypedef)
  - [ListArtifactsResultTypeDef](#listartifactsresulttypedef)
  - [ListDeviceInstancesResultTypeDef](#listdeviceinstancesresulttypedef)
  - [ListDevicePoolsResultTypeDef](#listdevicepoolsresulttypedef)
  - [ListDevicesResultTypeDef](#listdevicesresulttypedef)
  - [ListInstanceProfilesResultTypeDef](#listinstanceprofilesresulttypedef)
  - [ListJobsResultTypeDef](#listjobsresulttypedef)
  - [ListNetworkProfilesResultTypeDef](#listnetworkprofilesresulttypedef)
  - [ListOfferingPromotionsResultTypeDef](#listofferingpromotionsresulttypedef)
  - [ListOfferingTransactionsResultTypeDef](#listofferingtransactionsresulttypedef)
  - [ListOfferingsResultTypeDef](#listofferingsresulttypedef)
  - [ListProjectsResultTypeDef](#listprojectsresulttypedef)
  - [ListRemoteAccessSessionsResultTypeDef](#listremoteaccesssessionsresulttypedef)
  - [ListRunsResultTypeDef](#listrunsresulttypedef)
  - [ListSamplesResultTypeDef](#listsamplesresulttypedef)
  - [ListSuitesResultTypeDef](#listsuitesresulttypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTestGridProjectsResultTypeDef](#listtestgridprojectsresulttypedef)
  - [ListTestGridSessionActionsResultTypeDef](#listtestgridsessionactionsresulttypedef)
  - [ListTestGridSessionArtifactsResultTypeDef](#listtestgridsessionartifactsresulttypedef)
  - [ListTestGridSessionsResultTypeDef](#listtestgridsessionsresulttypedef)
  - [ListTestsResultTypeDef](#listtestsresulttypedef)
  - [ListUniqueProblemsResultTypeDef](#listuniqueproblemsresulttypedef)
  - [ListUploadsResultTypeDef](#listuploadsresulttypedef)
  - [ListVPCEConfigurationsResultTypeDef](#listvpceconfigurationsresulttypedef)
  - [LocationTypeDef](#locationtypedef)
  - [MonetaryAmountTypeDef](#monetaryamounttypedef)
  - [NetworkProfileTypeDef](#networkprofiletypedef)
  - [OfferingPromotionTypeDef](#offeringpromotiontypedef)
  - [OfferingStatusTypeDef](#offeringstatustypedef)
  - [OfferingTransactionTypeDef](#offeringtransactiontypedef)
  - [OfferingTypeDef](#offeringtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProblemDetailTypeDef](#problemdetailtypedef)
  - [ProblemTypeDef](#problemtypedef)
  - [ProjectTypeDef](#projecttypedef)
  - [PurchaseOfferingResultTypeDef](#purchaseofferingresulttypedef)
  - [RadiosTypeDef](#radiostypedef)
  - [RecurringChargeTypeDef](#recurringchargetypedef)
  - [RemoteAccessSessionTypeDef](#remoteaccesssessiontypedef)
  - [RenewOfferingResultTypeDef](#renewofferingresulttypedef)
  - [ResolutionTypeDef](#resolutiontypedef)
  - [RuleTypeDef](#ruletypedef)
  - [RunTypeDef](#runtypedef)
  - [SampleTypeDef](#sampletypedef)
  - [ScheduleRunConfigurationTypeDef](#schedulerunconfigurationtypedef)
  - [ScheduleRunResultTypeDef](#schedulerunresulttypedef)
  - [ScheduleRunTestTypeDef](#scheduleruntesttypedef)
  - [StopJobResultTypeDef](#stopjobresulttypedef)
  - [StopRemoteAccessSessionResultTypeDef](#stopremoteaccesssessionresulttypedef)
  - [StopRunResultTypeDef](#stoprunresulttypedef)
  - [SuiteTypeDef](#suitetypedef)
  - [TagTypeDef](#tagtypedef)
  - [TestGridProjectTypeDef](#testgridprojecttypedef)
  - [TestGridSessionActionTypeDef](#testgridsessionactiontypedef)
  - [TestGridSessionArtifactTypeDef](#testgridsessionartifacttypedef)
  - [TestGridSessionTypeDef](#testgridsessiontypedef)
  - [TestTypeDef](#testtypedef)
  - [TrialMinutesTypeDef](#trialminutestypedef)
  - [UniqueProblemTypeDef](#uniqueproblemtypedef)
  - [UpdateDeviceInstanceResultTypeDef](#updatedeviceinstanceresulttypedef)
  - [UpdateDevicePoolResultTypeDef](#updatedevicepoolresulttypedef)
  - [UpdateInstanceProfileResultTypeDef](#updateinstanceprofileresulttypedef)
  - [UpdateNetworkProfileResultTypeDef](#updatenetworkprofileresulttypedef)
  - [UpdateProjectResultTypeDef](#updateprojectresulttypedef)
  - [UpdateTestGridProjectResultTypeDef](#updatetestgridprojectresulttypedef)
  - [UpdateUploadResultTypeDef](#updateuploadresulttypedef)
  - [UpdateVPCEConfigurationResultTypeDef](#updatevpceconfigurationresulttypedef)
  - [UploadTypeDef](#uploadtypedef)
  - [VPCEConfigurationTypeDef](#vpceconfigurationtypedef)

## AccountSettingsTypeDef

```python
from mypy_boto3_devicefarm.type_defs import AccountSettingsTypeDef
```




Optional fields:
- `awsAccountNumber`: `str`
- `unmeteredDevices`: `Dict[DevicePlatform, int]`
- `unmeteredRemoteAccessDevices`: `Dict[DevicePlatform, int]`
- `maxJobTimeoutMinutes`: `int`
- `trialMinutes`: `"TrialMinutesTypeDef"`
- `maxSlots`: `Dict[str, int]`
- `defaultJobTimeoutMinutes`: `int`
- `skipAppResign`: `bool`


## ArtifactTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ArtifactTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `ArtifactType`
- `extension`: `str`
- `url`: `str`


## CPUTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CPUTypeDef
```




Optional fields:
- `frequency`: `str`
- `architecture`: `str`
- `clock`: `float`


## CountersTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CountersTypeDef
```




Optional fields:
- `total`: `int`
- `passed`: `int`
- `failed`: `int`
- `warned`: `int`
- `errored`: `int`
- `stopped`: `int`
- `skipped`: `int`


## CreateDevicePoolResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateDevicePoolResultTypeDef
```




Optional fields:
- `devicePool`: `"DevicePoolTypeDef"`


## CreateInstanceProfileResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateInstanceProfileResultTypeDef
```




Optional fields:
- `instanceProfile`: `"InstanceProfileTypeDef"`


## CreateNetworkProfileResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateNetworkProfileResultTypeDef
```




Optional fields:
- `networkProfile`: `"NetworkProfileTypeDef"`


## CreateProjectResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateProjectResultTypeDef
```




Optional fields:
- `project`: `"ProjectTypeDef"`


## CreateRemoteAccessSessionConfigurationTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateRemoteAccessSessionConfigurationTypeDef
```




Optional fields:
- `billingMethod`: `BillingMethod`
- `vpceConfigurationArns`: `List[str]`


## CreateRemoteAccessSessionResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateRemoteAccessSessionResultTypeDef
```




Optional fields:
- `remoteAccessSession`: `"RemoteAccessSessionTypeDef"`


## CreateTestGridProjectResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateTestGridProjectResultTypeDef
```




Optional fields:
- `testGridProject`: `"TestGridProjectTypeDef"`


## CreateTestGridUrlResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateTestGridUrlResultTypeDef
```




Optional fields:
- `url`: `str`
- `expires`: `datetime`


## CreateUploadResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateUploadResultTypeDef
```




Optional fields:
- `upload`: `"UploadTypeDef"`


## CreateVPCEConfigurationResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CreateVPCEConfigurationResultTypeDef
```




Optional fields:
- `vpceConfiguration`: `"VPCEConfigurationTypeDef"`


## CustomerArtifactPathsTypeDef

```python
from mypy_boto3_devicefarm.type_defs import CustomerArtifactPathsTypeDef
```




Optional fields:
- `iosPaths`: `List[str]`
- `androidPaths`: `List[str]`
- `deviceHostPaths`: `List[str]`


## DeviceFilterTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DeviceFilterTypeDef
```




Optional fields:
- `attribute`: `DeviceFilterAttribute`
- `operator`: `RuleOperator`
- `values`: `List[str]`


## DeviceInstanceTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DeviceInstanceTypeDef
```




Optional fields:
- `arn`: `str`
- `deviceArn`: `str`
- `labels`: `List[str]`
- `status`: `InstanceStatus`
- `udid`: `str`
- `instanceProfile`: `"InstanceProfileTypeDef"`


## DeviceMinutesTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DeviceMinutesTypeDef
```




Optional fields:
- `total`: `float`
- `metered`: `float`
- `unmetered`: `float`


## DevicePoolCompatibilityResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DevicePoolCompatibilityResultTypeDef
```




Optional fields:
- `device`: `"DeviceTypeDef"`
- `compatible`: `bool`
- `incompatibilityMessages`: `List["IncompatibilityMessageTypeDef"]`


## DevicePoolTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DevicePoolTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `type`: `DevicePoolType`
- `rules`: `List["RuleTypeDef"]`
- `maxDevices`: `int`


## DeviceSelectionConfigurationTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DeviceSelectionConfigurationTypeDef
```


Required fields:
- `filters`: `List["DeviceFilterTypeDef"]`
- `maxDevices`: `int`




## DeviceSelectionResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DeviceSelectionResultTypeDef
```




Optional fields:
- `filters`: `List["DeviceFilterTypeDef"]`
- `matchedDevicesCount`: `int`
- `maxDevices`: `int`


## DeviceTypeDef

```python
from mypy_boto3_devicefarm.type_defs import DeviceTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `manufacturer`: `str`
- `model`: `str`
- `modelId`: `str`
- `formFactor`: `DeviceFormFactor`
- `platform`: `DevicePlatform`
- `os`: `str`
- `cpu`: `"CPUTypeDef"`
- `resolution`: `"ResolutionTypeDef"`
- `heapSize`: `int`
- `memory`: `int`
- `image`: `str`
- `carrier`: `str`
- `radio`: `str`
- `remoteAccessEnabled`: `bool`
- `remoteDebugEnabled`: `bool`
- `fleetType`: `str`
- `fleetName`: `str`
- `instances`: `List["DeviceInstanceTypeDef"]`
- `availability`: `DeviceAvailability`


## ExecutionConfigurationTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ExecutionConfigurationTypeDef
```




Optional fields:
- `jobTimeoutMinutes`: `int`
- `accountsCleanup`: `bool`
- `appPackagesCleanup`: `bool`
- `videoCapture`: `bool`
- `skipAppResign`: `bool`


## GetAccountSettingsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetAccountSettingsResultTypeDef
```




Optional fields:
- `accountSettings`: `"AccountSettingsTypeDef"`


## GetDeviceInstanceResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetDeviceInstanceResultTypeDef
```




Optional fields:
- `deviceInstance`: `"DeviceInstanceTypeDef"`


## GetDevicePoolCompatibilityResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetDevicePoolCompatibilityResultTypeDef
```




Optional fields:
- `compatibleDevices`: `List["DevicePoolCompatibilityResultTypeDef"]`
- `incompatibleDevices`: `List["DevicePoolCompatibilityResultTypeDef"]`


## GetDevicePoolResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetDevicePoolResultTypeDef
```




Optional fields:
- `devicePool`: `"DevicePoolTypeDef"`


## GetDeviceResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetDeviceResultTypeDef
```




Optional fields:
- `device`: `"DeviceTypeDef"`


## GetInstanceProfileResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetInstanceProfileResultTypeDef
```




Optional fields:
- `instanceProfile`: `"InstanceProfileTypeDef"`


## GetJobResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetJobResultTypeDef
```




Optional fields:
- `job`: `"JobTypeDef"`


## GetNetworkProfileResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetNetworkProfileResultTypeDef
```




Optional fields:
- `networkProfile`: `"NetworkProfileTypeDef"`


## GetOfferingStatusResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetOfferingStatusResultTypeDef
```




Optional fields:
- `current`: `Dict[str, "OfferingStatusTypeDef"]`
- `nextPeriod`: `Dict[str, "OfferingStatusTypeDef"]`
- `nextToken`: `str`


## GetProjectResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetProjectResultTypeDef
```




Optional fields:
- `project`: `"ProjectTypeDef"`


## GetRemoteAccessSessionResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetRemoteAccessSessionResultTypeDef
```




Optional fields:
- `remoteAccessSession`: `"RemoteAccessSessionTypeDef"`


## GetRunResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetRunResultTypeDef
```




Optional fields:
- `run`: `"RunTypeDef"`


## GetSuiteResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetSuiteResultTypeDef
```




Optional fields:
- `suite`: `"SuiteTypeDef"`


## GetTestGridProjectResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetTestGridProjectResultTypeDef
```




Optional fields:
- `testGridProject`: `"TestGridProjectTypeDef"`


## GetTestGridSessionResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetTestGridSessionResultTypeDef
```




Optional fields:
- `testGridSession`: `"TestGridSessionTypeDef"`


## GetTestResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetTestResultTypeDef
```




Optional fields:
- `test`: `"TestTypeDef"`


## GetUploadResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetUploadResultTypeDef
```




Optional fields:
- `upload`: `"UploadTypeDef"`


## GetVPCEConfigurationResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import GetVPCEConfigurationResultTypeDef
```




Optional fields:
- `vpceConfiguration`: `"VPCEConfigurationTypeDef"`


## IncompatibilityMessageTypeDef

```python
from mypy_boto3_devicefarm.type_defs import IncompatibilityMessageTypeDef
```




Optional fields:
- `message`: `str`
- `type`: `DeviceAttribute`


## InstallToRemoteAccessSessionResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import InstallToRemoteAccessSessionResultTypeDef
```




Optional fields:
- `appUpload`: `"UploadTypeDef"`


## InstanceProfileTypeDef

```python
from mypy_boto3_devicefarm.type_defs import InstanceProfileTypeDef
```




Optional fields:
- `arn`: `str`
- `packageCleanup`: `bool`
- `excludeAppPackagesFromCleanup`: `List[str]`
- `rebootAfterUse`: `bool`
- `name`: `str`
- `description`: `str`


## JobTypeDef

```python
from mypy_boto3_devicefarm.type_defs import JobTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `TestType`
- `created`: `datetime`
- `status`: `ExecutionStatus`
- `result`: `ExecutionResult`
- `started`: `datetime`
- `stopped`: `datetime`
- `counters`: `"CountersTypeDef"`
- `message`: `str`
- `device`: `"DeviceTypeDef"`
- `instanceArn`: `str`
- `deviceMinutes`: `"DeviceMinutesTypeDef"`
- `videoEndpoint`: `str`
- `videoCapture`: `bool`


## ListArtifactsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListArtifactsResultTypeDef
```




Optional fields:
- `artifacts`: `List["ArtifactTypeDef"]`
- `nextToken`: `str`


## ListDeviceInstancesResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListDeviceInstancesResultTypeDef
```




Optional fields:
- `deviceInstances`: `List["DeviceInstanceTypeDef"]`
- `nextToken`: `str`


## ListDevicePoolsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListDevicePoolsResultTypeDef
```




Optional fields:
- `devicePools`: `List["DevicePoolTypeDef"]`
- `nextToken`: `str`


## ListDevicesResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListDevicesResultTypeDef
```




Optional fields:
- `devices`: `List["DeviceTypeDef"]`
- `nextToken`: `str`


## ListInstanceProfilesResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListInstanceProfilesResultTypeDef
```




Optional fields:
- `instanceProfiles`: `List["InstanceProfileTypeDef"]`
- `nextToken`: `str`


## ListJobsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListJobsResultTypeDef
```




Optional fields:
- `jobs`: `List["JobTypeDef"]`
- `nextToken`: `str`


## ListNetworkProfilesResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListNetworkProfilesResultTypeDef
```




Optional fields:
- `networkProfiles`: `List["NetworkProfileTypeDef"]`
- `nextToken`: `str`


## ListOfferingPromotionsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListOfferingPromotionsResultTypeDef
```




Optional fields:
- `offeringPromotions`: `List["OfferingPromotionTypeDef"]`
- `nextToken`: `str`


## ListOfferingTransactionsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListOfferingTransactionsResultTypeDef
```




Optional fields:
- `offeringTransactions`: `List["OfferingTransactionTypeDef"]`
- `nextToken`: `str`


## ListOfferingsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListOfferingsResultTypeDef
```




Optional fields:
- `offerings`: `List["OfferingTypeDef"]`
- `nextToken`: `str`


## ListProjectsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListProjectsResultTypeDef
```




Optional fields:
- `projects`: `List["ProjectTypeDef"]`
- `nextToken`: `str`


## ListRemoteAccessSessionsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListRemoteAccessSessionsResultTypeDef
```




Optional fields:
- `remoteAccessSessions`: `List["RemoteAccessSessionTypeDef"]`
- `nextToken`: `str`


## ListRunsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListRunsResultTypeDef
```




Optional fields:
- `runs`: `List["RunTypeDef"]`
- `nextToken`: `str`


## ListSamplesResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListSamplesResultTypeDef
```




Optional fields:
- `samples`: `List["SampleTypeDef"]`
- `nextToken`: `str`


## ListSuitesResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListSuitesResultTypeDef
```




Optional fields:
- `suites`: `List["SuiteTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## ListTestGridProjectsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListTestGridProjectsResultTypeDef
```




Optional fields:
- `testGridProjects`: `List["TestGridProjectTypeDef"]`
- `nextToken`: `str`


## ListTestGridSessionActionsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListTestGridSessionActionsResultTypeDef
```




Optional fields:
- `actions`: `List["TestGridSessionActionTypeDef"]`
- `nextToken`: `str`


## ListTestGridSessionArtifactsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListTestGridSessionArtifactsResultTypeDef
```




Optional fields:
- `artifacts`: `List["TestGridSessionArtifactTypeDef"]`
- `nextToken`: `str`


## ListTestGridSessionsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListTestGridSessionsResultTypeDef
```




Optional fields:
- `testGridSessions`: `List["TestGridSessionTypeDef"]`
- `nextToken`: `str`


## ListTestsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListTestsResultTypeDef
```




Optional fields:
- `tests`: `List["TestTypeDef"]`
- `nextToken`: `str`


## ListUniqueProblemsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListUniqueProblemsResultTypeDef
```




Optional fields:
- `uniqueProblems`: `Dict[ExecutionResult, List["UniqueProblemTypeDef"]]`
- `nextToken`: `str`


## ListUploadsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListUploadsResultTypeDef
```




Optional fields:
- `uploads`: `List["UploadTypeDef"]`
- `nextToken`: `str`


## ListVPCEConfigurationsResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ListVPCEConfigurationsResultTypeDef
```




Optional fields:
- `vpceConfigurations`: `List["VPCEConfigurationTypeDef"]`
- `nextToken`: `str`


## LocationTypeDef

```python
from mypy_boto3_devicefarm.type_defs import LocationTypeDef
```


Required fields:
- `latitude`: `float`
- `longitude`: `float`




## MonetaryAmountTypeDef

```python
from mypy_boto3_devicefarm.type_defs import MonetaryAmountTypeDef
```




Optional fields:
- `amount`: `float`
- `currencyCode`: `Literal['USD']`


## NetworkProfileTypeDef

```python
from mypy_boto3_devicefarm.type_defs import NetworkProfileTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `type`: `NetworkProfileType`
- `uplinkBandwidthBits`: `int`
- `downlinkBandwidthBits`: `int`
- `uplinkDelayMs`: `int`
- `downlinkDelayMs`: `int`
- `uplinkJitterMs`: `int`
- `downlinkJitterMs`: `int`
- `uplinkLossPercent`: `int`
- `downlinkLossPercent`: `int`


## OfferingPromotionTypeDef

```python
from mypy_boto3_devicefarm.type_defs import OfferingPromotionTypeDef
```




Optional fields:
- `id`: `str`
- `description`: `str`


## OfferingStatusTypeDef

```python
from mypy_boto3_devicefarm.type_defs import OfferingStatusTypeDef
```




Optional fields:
- `type`: `OfferingTransactionType`
- `offering`: `"OfferingTypeDef"`
- `quantity`: `int`
- `effectiveOn`: `datetime`


## OfferingTransactionTypeDef

```python
from mypy_boto3_devicefarm.type_defs import OfferingTransactionTypeDef
```




Optional fields:
- `offeringStatus`: `"OfferingStatusTypeDef"`
- `transactionId`: `str`
- `offeringPromotionId`: `str`
- `createdOn`: `datetime`
- `cost`: `"MonetaryAmountTypeDef"`


## OfferingTypeDef

```python
from mypy_boto3_devicefarm.type_defs import OfferingTypeDef
```




Optional fields:
- `id`: `str`
- `description`: `str`
- `type`: `Literal['RECURRING']`
- `platform`: `DevicePlatform`
- `recurringCharges`: `List["RecurringChargeTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_devicefarm.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProblemDetailTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ProblemDetailTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`


## ProblemTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ProblemTypeDef
```




Optional fields:
- `run`: `"ProblemDetailTypeDef"`
- `job`: `"ProblemDetailTypeDef"`
- `suite`: `"ProblemDetailTypeDef"`
- `test`: `"ProblemDetailTypeDef"`
- `device`: `"DeviceTypeDef"`
- `result`: `ExecutionResult`
- `message`: `str`


## ProjectTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ProjectTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `defaultJobTimeoutMinutes`: `int`
- `created`: `datetime`


## PurchaseOfferingResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import PurchaseOfferingResultTypeDef
```




Optional fields:
- `offeringTransaction`: `"OfferingTransactionTypeDef"`


## RadiosTypeDef

```python
from mypy_boto3_devicefarm.type_defs import RadiosTypeDef
```




Optional fields:
- `wifi`: `bool`
- `bluetooth`: `bool`
- `nfc`: `bool`
- `gps`: `bool`


## RecurringChargeTypeDef

```python
from mypy_boto3_devicefarm.type_defs import RecurringChargeTypeDef
```




Optional fields:
- `cost`: `"MonetaryAmountTypeDef"`
- `frequency`: `Literal['MONTHLY']`


## RemoteAccessSessionTypeDef

```python
from mypy_boto3_devicefarm.type_defs import RemoteAccessSessionTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `created`: `datetime`
- `status`: `ExecutionStatus`
- `result`: `ExecutionResult`
- `message`: `str`
- `started`: `datetime`
- `stopped`: `datetime`
- `device`: `"DeviceTypeDef"`
- `instanceArn`: `str`
- `remoteDebugEnabled`: `bool`
- `remoteRecordEnabled`: `bool`
- `remoteRecordAppArn`: `str`
- `hostAddress`: `str`
- `clientId`: `str`
- `billingMethod`: `BillingMethod`
- `deviceMinutes`: `"DeviceMinutesTypeDef"`
- `endpoint`: `str`
- `deviceUdid`: `str`
- `interactionMode`: `InteractionMode`
- `skipAppResign`: `bool`


## RenewOfferingResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import RenewOfferingResultTypeDef
```




Optional fields:
- `offeringTransaction`: `"OfferingTransactionTypeDef"`


## ResolutionTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ResolutionTypeDef
```




Optional fields:
- `width`: `int`
- `height`: `int`


## RuleTypeDef

```python
from mypy_boto3_devicefarm.type_defs import RuleTypeDef
```




Optional fields:
- `attribute`: `DeviceAttribute`
- `operator`: `RuleOperator`
- `value`: `str`


## RunTypeDef

```python
from mypy_boto3_devicefarm.type_defs import RunTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `TestType`
- `platform`: `DevicePlatform`
- `created`: `datetime`
- `status`: `ExecutionStatus`
- `result`: `ExecutionResult`
- `started`: `datetime`
- `stopped`: `datetime`
- `counters`: `"CountersTypeDef"`
- `message`: `str`
- `totalJobs`: `int`
- `completedJobs`: `int`
- `billingMethod`: `BillingMethod`
- `deviceMinutes`: `"DeviceMinutesTypeDef"`
- `networkProfile`: `"NetworkProfileTypeDef"`
- `parsingResultUrl`: `str`
- `resultCode`: `ExecutionResultCode`
- `seed`: `int`
- `appUpload`: `str`
- `eventCount`: `int`
- `jobTimeoutMinutes`: `int`
- `devicePoolArn`: `str`
- `locale`: `str`
- `radios`: `"RadiosTypeDef"`
- `location`: `"LocationTypeDef"`
- `customerArtifactPaths`: `"CustomerArtifactPathsTypeDef"`
- `webUrl`: `str`
- `skipAppResign`: `bool`
- `testSpecArn`: `str`
- `deviceSelectionResult`: `"DeviceSelectionResultTypeDef"`


## SampleTypeDef

```python
from mypy_boto3_devicefarm.type_defs import SampleTypeDef
```




Optional fields:
- `arn`: `str`
- `type`: `SampleType`
- `url`: `str`


## ScheduleRunConfigurationTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ScheduleRunConfigurationTypeDef
```




Optional fields:
- `extraDataPackageArn`: `str`
- `networkProfileArn`: `str`
- `locale`: `str`
- `location`: `"LocationTypeDef"`
- `vpceConfigurationArns`: `List[str]`
- `customerArtifactPaths`: `"CustomerArtifactPathsTypeDef"`
- `radios`: `"RadiosTypeDef"`
- `auxiliaryApps`: `List[str]`
- `billingMethod`: `BillingMethod`


## ScheduleRunResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ScheduleRunResultTypeDef
```




Optional fields:
- `run`: `"RunTypeDef"`


## ScheduleRunTestTypeDef

```python
from mypy_boto3_devicefarm.type_defs import ScheduleRunTestTypeDef
```


Required fields:
- `type`: `TestType`



Optional fields:
- `testPackageArn`: `str`
- `testSpecArn`: `str`
- `filter`: `str`
- `parameters`: `Dict[str, str]`


## StopJobResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import StopJobResultTypeDef
```




Optional fields:
- `job`: `"JobTypeDef"`


## StopRemoteAccessSessionResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import StopRemoteAccessSessionResultTypeDef
```




Optional fields:
- `remoteAccessSession`: `"RemoteAccessSessionTypeDef"`


## StopRunResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import StopRunResultTypeDef
```




Optional fields:
- `run`: `"RunTypeDef"`


## SuiteTypeDef

```python
from mypy_boto3_devicefarm.type_defs import SuiteTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `TestType`
- `created`: `datetime`
- `status`: `ExecutionStatus`
- `result`: `ExecutionResult`
- `started`: `datetime`
- `stopped`: `datetime`
- `counters`: `"CountersTypeDef"`
- `message`: `str`
- `deviceMinutes`: `"DeviceMinutesTypeDef"`


## TagTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TestGridProjectTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TestGridProjectTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `created`: `datetime`


## TestGridSessionActionTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TestGridSessionActionTypeDef
```




Optional fields:
- `action`: `str`
- `started`: `datetime`
- `duration`: `int`
- `statusCode`: `str`
- `requestMethod`: `str`


## TestGridSessionArtifactTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TestGridSessionArtifactTypeDef
```




Optional fields:
- `filename`: `str`
- `type`: `TestGridSessionArtifactType`
- `url`: `str`


## TestGridSessionTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TestGridSessionTypeDef
```




Optional fields:
- `arn`: `str`
- `status`: `TestGridSessionStatus`
- `created`: `datetime`
- `ended`: `datetime`
- `billingMinutes`: `float`
- `seleniumProperties`: `str`


## TestTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TestTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `TestType`
- `created`: `datetime`
- `status`: `ExecutionStatus`
- `result`: `ExecutionResult`
- `started`: `datetime`
- `stopped`: `datetime`
- `counters`: `"CountersTypeDef"`
- `message`: `str`
- `deviceMinutes`: `"DeviceMinutesTypeDef"`


## TrialMinutesTypeDef

```python
from mypy_boto3_devicefarm.type_defs import TrialMinutesTypeDef
```




Optional fields:
- `total`: `float`
- `remaining`: `float`


## UniqueProblemTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UniqueProblemTypeDef
```




Optional fields:
- `message`: `str`
- `problems`: `List["ProblemTypeDef"]`


## UpdateDeviceInstanceResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateDeviceInstanceResultTypeDef
```




Optional fields:
- `deviceInstance`: `"DeviceInstanceTypeDef"`


## UpdateDevicePoolResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateDevicePoolResultTypeDef
```




Optional fields:
- `devicePool`: `"DevicePoolTypeDef"`


## UpdateInstanceProfileResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateInstanceProfileResultTypeDef
```




Optional fields:
- `instanceProfile`: `"InstanceProfileTypeDef"`


## UpdateNetworkProfileResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateNetworkProfileResultTypeDef
```




Optional fields:
- `networkProfile`: `"NetworkProfileTypeDef"`


## UpdateProjectResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateProjectResultTypeDef
```




Optional fields:
- `project`: `"ProjectTypeDef"`


## UpdateTestGridProjectResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateTestGridProjectResultTypeDef
```




Optional fields:
- `testGridProject`: `"TestGridProjectTypeDef"`


## UpdateUploadResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateUploadResultTypeDef
```




Optional fields:
- `upload`: `"UploadTypeDef"`


## UpdateVPCEConfigurationResultTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UpdateVPCEConfigurationResultTypeDef
```




Optional fields:
- `vpceConfiguration`: `"VPCEConfigurationTypeDef"`


## UploadTypeDef

```python
from mypy_boto3_devicefarm.type_defs import UploadTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `created`: `datetime`
- `type`: `UploadType`
- `status`: `UploadStatus`
- `url`: `str`
- `metadata`: `str`
- `contentType`: `str`
- `message`: `str`
- `category`: `UploadCategory`


## VPCEConfigurationTypeDef

```python
from mypy_boto3_devicefarm.type_defs import VPCEConfigurationTypeDef
```




Optional fields:
- `arn`: `str`
- `vpceConfigurationName`: `str`
- `vpceServiceName`: `str`
- `serviceDnsName`: `str`
- `vpceConfigurationDescription`: `str`

