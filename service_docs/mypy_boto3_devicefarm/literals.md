# Literals for boto3 DeviceFarm module

> [Index](../index.md) > [DeviceFarm](./index.md) > Literals

Auto-generated documentation for [DeviceFarm](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm)
type annotations stubs module [mypy_boto3_devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/).

- [Literals for boto3 DeviceFarm module](#literals-for-boto3-devicefarm-module)
  - [ArtifactCategory](#artifactcategory)
  - [ArtifactType](#artifacttype)
  - [BillingMethod](#billingmethod)
  - [CurrencyCode](#currencycode)
  - [DeviceAttribute](#deviceattribute)
  - [DeviceAvailability](#deviceavailability)
  - [DeviceFilterAttribute](#devicefilterattribute)
  - [DeviceFormFactor](#deviceformfactor)
  - [DevicePlatform](#deviceplatform)
  - [DevicePoolType](#devicepooltype)
  - [ExecutionResult](#executionresult)
  - [ExecutionResultCode](#executionresultcode)
  - [ExecutionStatus](#executionstatus)
  - [GetOfferingStatusPaginatorName](#getofferingstatuspaginatorname)
  - [InstanceStatus](#instancestatus)
  - [InteractionMode](#interactionmode)
  - [ListArtifactsPaginatorName](#listartifactspaginatorname)
  - [ListDeviceInstancesPaginatorName](#listdeviceinstancespaginatorname)
  - [ListDevicePoolsPaginatorName](#listdevicepoolspaginatorname)
  - [ListDevicesPaginatorName](#listdevicespaginatorname)
  - [ListInstanceProfilesPaginatorName](#listinstanceprofilespaginatorname)
  - [ListJobsPaginatorName](#listjobspaginatorname)
  - [ListNetworkProfilesPaginatorName](#listnetworkprofilespaginatorname)
  - [ListOfferingPromotionsPaginatorName](#listofferingpromotionspaginatorname)
  - [ListOfferingTransactionsPaginatorName](#listofferingtransactionspaginatorname)
  - [ListOfferingsPaginatorName](#listofferingspaginatorname)
  - [ListProjectsPaginatorName](#listprojectspaginatorname)
  - [ListRemoteAccessSessionsPaginatorName](#listremoteaccesssessionspaginatorname)
  - [ListRunsPaginatorName](#listrunspaginatorname)
  - [ListSamplesPaginatorName](#listsamplespaginatorname)
  - [ListSuitesPaginatorName](#listsuitespaginatorname)
  - [ListTestsPaginatorName](#listtestspaginatorname)
  - [ListUniqueProblemsPaginatorName](#listuniqueproblemspaginatorname)
  - [ListUploadsPaginatorName](#listuploadspaginatorname)
  - [ListVPCEConfigurationsPaginatorName](#listvpceconfigurationspaginatorname)
  - [NetworkProfileType](#networkprofiletype)
  - [OfferingTransactionType](#offeringtransactiontype)
  - [OfferingType](#offeringtype)
  - [RecurringChargeFrequency](#recurringchargefrequency)
  - [RuleOperator](#ruleoperator)
  - [SampleType](#sampletype)
  - [TestGridSessionArtifactCategory](#testgridsessionartifactcategory)
  - [TestGridSessionArtifactType](#testgridsessionartifacttype)
  - [TestGridSessionStatus](#testgridsessionstatus)
  - [TestType](#testtype)
  - [UploadCategory](#uploadcategory)
  - [UploadStatus](#uploadstatus)
  - [UploadType](#uploadtype)

## ArtifactCategory

```python
from mypy_boto3_devicefarm.literals import ArtifactCategory
```

Values:

- `FILE`
- `LOG`
- `SCREENSHOT`

## ArtifactType

```python
from mypy_boto3_devicefarm.literals import ArtifactType
```

Values:

- `APPIUM_JAVA_OUTPUT`
- `APPIUM_JAVA_XML_OUTPUT`
- `APPIUM_PYTHON_OUTPUT`
- `APPIUM_PYTHON_XML_OUTPUT`
- `APPIUM_SERVER_OUTPUT`
- `APPLICATION_CRASH_REPORT`
- `AUTOMATION_OUTPUT`
- `CALABASH_JAVA_XML_OUTPUT`
- `CALABASH_JSON_OUTPUT`
- `CALABASH_PRETTY_OUTPUT`
- `CALABASH_STANDARD_OUTPUT`
- `CUSTOMER_ARTIFACT`
- `CUSTOMER_ARTIFACT_LOG`
- `DEVICE_LOG`
- `EXERCISER_MONKEY_OUTPUT`
- `EXPLORER_EVENT_LOG`
- `EXPLORER_SUMMARY_LOG`
- `INSTRUMENTATION_OUTPUT`
- `MESSAGE_LOG`
- `RESULT_LOG`
- `SCREENSHOT`
- `SERVICE_LOG`
- `TESTSPEC_OUTPUT`
- `UNKNOWN`
- `VIDEO`
- `VIDEO_LOG`
- `WEBKIT_LOG`
- `XCTEST_LOG`

## BillingMethod

```python
from mypy_boto3_devicefarm.literals import BillingMethod
```

Values:

- `METERED`
- `UNMETERED`

## CurrencyCode

```python
from mypy_boto3_devicefarm.literals import CurrencyCode
```

Values:

- `USD`

## DeviceAttribute

```python
from mypy_boto3_devicefarm.literals import DeviceAttribute
```

Values:

- `APPIUM_VERSION`
- `ARN`
- `AVAILABILITY`
- `FLEET_TYPE`
- `FORM_FACTOR`
- `INSTANCE_ARN`
- `INSTANCE_LABELS`
- `MANUFACTURER`
- `MODEL`
- `OS_VERSION`
- `PLATFORM`
- `REMOTE_ACCESS_ENABLED`
- `REMOTE_DEBUG_ENABLED`

## DeviceAvailability

```python
from mypy_boto3_devicefarm.literals import DeviceAvailability
```

Values:

- `AVAILABLE`
- `BUSY`
- `HIGHLY_AVAILABLE`
- `TEMPORARY_NOT_AVAILABLE`

## DeviceFilterAttribute

```python
from mypy_boto3_devicefarm.literals import DeviceFilterAttribute
```

Values:

- `ARN`
- `AVAILABILITY`
- `FLEET_TYPE`
- `FORM_FACTOR`
- `INSTANCE_ARN`
- `INSTANCE_LABELS`
- `MANUFACTURER`
- `MODEL`
- `OS_VERSION`
- `PLATFORM`
- `REMOTE_ACCESS_ENABLED`
- `REMOTE_DEBUG_ENABLED`

## DeviceFormFactor

```python
from mypy_boto3_devicefarm.literals import DeviceFormFactor
```

Values:

- `PHONE`
- `TABLET`

## DevicePlatform

```python
from mypy_boto3_devicefarm.literals import DevicePlatform
```

Values:

- `ANDROID`
- `IOS`

## DevicePoolType

```python
from mypy_boto3_devicefarm.literals import DevicePoolType
```

Values:

- `CURATED`
- `PRIVATE`

## ExecutionResult

```python
from mypy_boto3_devicefarm.literals import ExecutionResult
```

Values:

- `ERRORED`
- `FAILED`
- `PASSED`
- `PENDING`
- `SKIPPED`
- `STOPPED`
- `WARNED`

## ExecutionResultCode

```python
from mypy_boto3_devicefarm.literals import ExecutionResultCode
```

Values:

- `PARSING_FAILED`
- `VPC_ENDPOINT_SETUP_FAILED`

## ExecutionStatus

```python
from mypy_boto3_devicefarm.literals import ExecutionStatus
```

Values:

- `COMPLETED`
- `PENDING`
- `PENDING_CONCURRENCY`
- `PENDING_DEVICE`
- `PREPARING`
- `PROCESSING`
- `RUNNING`
- `SCHEDULING`
- `STOPPING`

## GetOfferingStatusPaginatorName

```python
from mypy_boto3_devicefarm.literals import GetOfferingStatusPaginatorName
```

Values:

- `get_offering_status`

## InstanceStatus

```python
from mypy_boto3_devicefarm.literals import InstanceStatus
```

Values:

- `AVAILABLE`
- `IN_USE`
- `NOT_AVAILABLE`
- `PREPARING`

## InteractionMode

```python
from mypy_boto3_devicefarm.literals import InteractionMode
```

Values:

- `INTERACTIVE`
- `NO_VIDEO`
- `VIDEO_ONLY`

## ListArtifactsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListArtifactsPaginatorName
```

Values:

- `list_artifacts`

## ListDeviceInstancesPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListDeviceInstancesPaginatorName
```

Values:

- `list_device_instances`

## ListDevicePoolsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListDevicePoolsPaginatorName
```

Values:

- `list_device_pools`

## ListDevicesPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListDevicesPaginatorName
```

Values:

- `list_devices`

## ListInstanceProfilesPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListInstanceProfilesPaginatorName
```

Values:

- `list_instance_profiles`

## ListJobsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListJobsPaginatorName
```

Values:

- `list_jobs`

## ListNetworkProfilesPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListNetworkProfilesPaginatorName
```

Values:

- `list_network_profiles`

## ListOfferingPromotionsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListOfferingPromotionsPaginatorName
```

Values:

- `list_offering_promotions`

## ListOfferingTransactionsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListOfferingTransactionsPaginatorName
```

Values:

- `list_offering_transactions`

## ListOfferingsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListOfferingsPaginatorName
```

Values:

- `list_offerings`

## ListProjectsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListProjectsPaginatorName
```

Values:

- `list_projects`

## ListRemoteAccessSessionsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListRemoteAccessSessionsPaginatorName
```

Values:

- `list_remote_access_sessions`

## ListRunsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListRunsPaginatorName
```

Values:

- `list_runs`

## ListSamplesPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListSamplesPaginatorName
```

Values:

- `list_samples`

## ListSuitesPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListSuitesPaginatorName
```

Values:

- `list_suites`

## ListTestsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListTestsPaginatorName
```

Values:

- `list_tests`

## ListUniqueProblemsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListUniqueProblemsPaginatorName
```

Values:

- `list_unique_problems`

## ListUploadsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListUploadsPaginatorName
```

Values:

- `list_uploads`

## ListVPCEConfigurationsPaginatorName

```python
from mypy_boto3_devicefarm.literals import ListVPCEConfigurationsPaginatorName
```

Values:

- `list_vpce_configurations`

## NetworkProfileType

```python
from mypy_boto3_devicefarm.literals import NetworkProfileType
```

Values:

- `CURATED`
- `PRIVATE`

## OfferingTransactionType

```python
from mypy_boto3_devicefarm.literals import OfferingTransactionType
```

Values:

- `PURCHASE`
- `RENEW`
- `SYSTEM`

## OfferingType

```python
from mypy_boto3_devicefarm.literals import OfferingType
```

Values:

- `RECURRING`

## RecurringChargeFrequency

```python
from mypy_boto3_devicefarm.literals import RecurringChargeFrequency
```

Values:

- `MONTHLY`

## RuleOperator

```python
from mypy_boto3_devicefarm.literals import RuleOperator
```

Values:

- `CONTAINS`
- `EQUALS`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUALS`
- `IN`
- `LESS_THAN`
- `LESS_THAN_OR_EQUALS`
- `NOT_IN`

## SampleType

```python
from mypy_boto3_devicefarm.literals import SampleType
```

Values:

- `CPU`
- `MEMORY`
- `NATIVE_AVG_DRAWTIME`
- `NATIVE_FPS`
- `NATIVE_FRAMES`
- `NATIVE_MAX_DRAWTIME`
- `NATIVE_MIN_DRAWTIME`
- `OPENGL_AVG_DRAWTIME`
- `OPENGL_FPS`
- `OPENGL_FRAMES`
- `OPENGL_MAX_DRAWTIME`
- `OPENGL_MIN_DRAWTIME`
- `RX`
- `RX_RATE`
- `THREADS`
- `TX`
- `TX_RATE`

## TestGridSessionArtifactCategory

```python
from mypy_boto3_devicefarm.literals import TestGridSessionArtifactCategory
```

Values:

- `LOG`
- `VIDEO`

## TestGridSessionArtifactType

```python
from mypy_boto3_devicefarm.literals import TestGridSessionArtifactType
```

Values:

- `SELENIUM_LOG`
- `UNKNOWN`
- `VIDEO`

## TestGridSessionStatus

```python
from mypy_boto3_devicefarm.literals import TestGridSessionStatus
```

Values:

- `ACTIVE`
- `CLOSED`
- `ERRORED`

## TestType

```python
from mypy_boto3_devicefarm.literals import TestType
```

Values:

- `APPIUM_JAVA_JUNIT`
- `APPIUM_JAVA_TESTNG`
- `APPIUM_NODE`
- `APPIUM_PYTHON`
- `APPIUM_RUBY`
- `APPIUM_WEB_JAVA_JUNIT`
- `APPIUM_WEB_JAVA_TESTNG`
- `APPIUM_WEB_NODE`
- `APPIUM_WEB_PYTHON`
- `APPIUM_WEB_RUBY`
- `BUILTIN_EXPLORER`
- `BUILTIN_FUZZ`
- `CALABASH`
- `INSTRUMENTATION`
- `REMOTE_ACCESS_RECORD`
- `REMOTE_ACCESS_REPLAY`
- `UIAUTOMATION`
- `UIAUTOMATOR`
- `WEB_PERFORMANCE_PROFILE`
- `XCTEST`
- `XCTEST_UI`

## UploadCategory

```python
from mypy_boto3_devicefarm.literals import UploadCategory
```

Values:

- `CURATED`
- `PRIVATE`

## UploadStatus

```python
from mypy_boto3_devicefarm.literals import UploadStatus
```

Values:

- `FAILED`
- `INITIALIZED`
- `PROCESSING`
- `SUCCEEDED`

## UploadType

```python
from mypy_boto3_devicefarm.literals import UploadType
```

Values:

- `ANDROID_APP`
- `APPIUM_JAVA_JUNIT_TEST_PACKAGE`
- `APPIUM_JAVA_JUNIT_TEST_SPEC`
- `APPIUM_JAVA_TESTNG_TEST_PACKAGE`
- `APPIUM_JAVA_TESTNG_TEST_SPEC`
- `APPIUM_NODE_TEST_PACKAGE`
- `APPIUM_NODE_TEST_SPEC`
- `APPIUM_PYTHON_TEST_PACKAGE`
- `APPIUM_PYTHON_TEST_SPEC`
- `APPIUM_RUBY_TEST_PACKAGE`
- `APPIUM_RUBY_TEST_SPEC`
- `APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE`
- `APPIUM_WEB_JAVA_JUNIT_TEST_SPEC`
- `APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE`
- `APPIUM_WEB_JAVA_TESTNG_TEST_SPEC`
- `APPIUM_WEB_NODE_TEST_PACKAGE`
- `APPIUM_WEB_NODE_TEST_SPEC`
- `APPIUM_WEB_PYTHON_TEST_PACKAGE`
- `APPIUM_WEB_PYTHON_TEST_SPEC`
- `APPIUM_WEB_RUBY_TEST_PACKAGE`
- `APPIUM_WEB_RUBY_TEST_SPEC`
- `CALABASH_TEST_PACKAGE`
- `EXTERNAL_DATA`
- `INSTRUMENTATION_TEST_PACKAGE`
- `INSTRUMENTATION_TEST_SPEC`
- `IOS_APP`
- `UIAUTOMATION_TEST_PACKAGE`
- `UIAUTOMATOR_TEST_PACKAGE`
- `WEB_APP`
- `XCTEST_TEST_PACKAGE`
- `XCTEST_UI_TEST_PACKAGE`
- `XCTEST_UI_TEST_SPEC`
