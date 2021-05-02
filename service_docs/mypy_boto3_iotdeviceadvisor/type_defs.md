# Structures for boto3 IoTDeviceAdvisor module

> [Index](../index.md) > [IoTDeviceAdvisor](./index.md) > Structures

Auto-generated documentation for [IoTDeviceAdvisor](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor)
type annotations stubs module [mypy_boto3_iotdeviceadvisor](https://pypi.org/project/mypy-boto3-iotdeviceadvisor/).

- [Structures for boto3 IoTDeviceAdvisor module](#structures-for-boto3-iotdeviceadvisor-module)
  - [CreateSuiteDefinitionResponseTypeDef](#createsuitedefinitionresponsetypedef)
  - [DeviceUnderTestTypeDef](#deviceundertesttypedef)
  - [GetSuiteDefinitionResponseTypeDef](#getsuitedefinitionresponsetypedef)
  - [GetSuiteRunReportResponseTypeDef](#getsuiterunreportresponsetypedef)
  - [GetSuiteRunResponseTypeDef](#getsuiterunresponsetypedef)
  - [GroupResultTypeDef](#groupresulttypedef)
  - [ListSuiteDefinitionsResponseTypeDef](#listsuitedefinitionsresponsetypedef)
  - [ListSuiteRunsResponseTypeDef](#listsuiterunsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTestCasesResponseTypeDef](#listtestcasesresponsetypedef)
  - [StartSuiteRunResponseTypeDef](#startsuiterunresponsetypedef)
  - [SuiteDefinitionConfigurationTypeDef](#suitedefinitionconfigurationtypedef)
  - [SuiteDefinitionInformationTypeDef](#suitedefinitioninformationtypedef)
  - [SuiteRunConfigurationTypeDef](#suiterunconfigurationtypedef)
  - [SuiteRunInformationTypeDef](#suiteruninformationtypedef)
  - [TestCaseCategoryTypeDef](#testcasecategorytypedef)
  - [TestCaseDefinitionTypeDef](#testcasedefinitiontypedef)
  - [TestCaseRunTypeDef](#testcaseruntypedef)
  - [TestCaseTypeDef](#testcasetypedef)
  - [TestResultTypeDef](#testresulttypedef)
  - [UpdateSuiteDefinitionResponseTypeDef](#updatesuitedefinitionresponsetypedef)

## CreateSuiteDefinitionResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionResponseTypeDef
```




Optional fields:
- `suiteDefinitionId`: `str`
- `suiteDefinitionArn`: `str`
- `suiteDefinitionName`: `str`
- `createdAt`: `datetime`


## DeviceUnderTestTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import DeviceUnderTestTypeDef
```




Optional fields:
- `thingArn`: `str`
- `certificateArn`: `str`


## GetSuiteDefinitionResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import GetSuiteDefinitionResponseTypeDef
```




Optional fields:
- `suiteDefinitionId`: `str`
- `suiteDefinitionArn`: `str`
- `suiteDefinitionVersion`: `str`
- `latestVersion`: `str`
- `suiteDefinitionConfiguration`: `"SuiteDefinitionConfigurationTypeDef"`
- `createdAt`: `datetime`
- `lastModifiedAt`: `datetime`
- `tags`: `Dict[str, str]`


## GetSuiteRunReportResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import GetSuiteRunReportResponseTypeDef
```




Optional fields:
- `qualificationReportDownloadUrl`: `str`


## GetSuiteRunResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import GetSuiteRunResponseTypeDef
```




Optional fields:
- `suiteDefinitionId`: `str`
- `suiteDefinitionVersion`: `str`
- `suiteRunId`: `str`
- `suiteRunArn`: `str`
- `suiteRunConfiguration`: `"SuiteRunConfigurationTypeDef"`
- `testResult`: `"TestResultTypeDef"`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `status`: `SuiteRunStatus`
- `errorReason`: `str`
- `tags`: `Dict[str, str]`


## GroupResultTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import GroupResultTypeDef
```




Optional fields:
- `groupId`: `str`
- `groupName`: `str`
- `tests`: `List["TestCaseRunTypeDef"]`


## ListSuiteDefinitionsResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import ListSuiteDefinitionsResponseTypeDef
```




Optional fields:
- `suiteDefinitionInformationList`: `List["SuiteDefinitionInformationTypeDef"]`
- `nextToken`: `str`


## ListSuiteRunsResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import ListSuiteRunsResponseTypeDef
```




Optional fields:
- `suiteRunsList`: `List["SuiteRunInformationTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## ListTestCasesResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import ListTestCasesResponseTypeDef
```




Optional fields:
- `categories`: `List["TestCaseCategoryTypeDef"]`
- `rootGroupConfiguration`: `Dict[str, str]`
- `groupConfiguration`: `Dict[str, str]`
- `nextToken`: `str`


## StartSuiteRunResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import StartSuiteRunResponseTypeDef
```




Optional fields:
- `suiteRunId`: `str`
- `suiteRunArn`: `str`
- `createdAt`: `datetime`


## SuiteDefinitionConfigurationTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import SuiteDefinitionConfigurationTypeDef
```




Optional fields:
- `suiteDefinitionName`: `str`
- `devices`: `List["DeviceUnderTestTypeDef"]`
- `intendedForQualification`: `bool`
- `rootGroup`: `str`
- `devicePermissionRoleArn`: `str`


## SuiteDefinitionInformationTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import SuiteDefinitionInformationTypeDef
```




Optional fields:
- `suiteDefinitionId`: `str`
- `suiteDefinitionName`: `str`
- `defaultDevices`: `List["DeviceUnderTestTypeDef"]`
- `intendedForQualification`: `bool`
- `createdAt`: `datetime`


## SuiteRunConfigurationTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import SuiteRunConfigurationTypeDef
```




Optional fields:
- `primaryDevice`: `"DeviceUnderTestTypeDef"`
- `secondaryDevice`: `"DeviceUnderTestTypeDef"`
- `selectedTestList`: `List[str]`


## SuiteRunInformationTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import SuiteRunInformationTypeDef
```




Optional fields:
- `suiteDefinitionId`: `str`
- `suiteDefinitionVersion`: `str`
- `suiteDefinitionName`: `str`
- `suiteRunId`: `str`
- `createdAt`: `datetime`
- `startedAt`: `datetime`
- `endAt`: `datetime`
- `status`: `SuiteRunStatus`
- `passed`: `int`
- `failed`: `int`


## TestCaseCategoryTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import TestCaseCategoryTypeDef
```




Optional fields:
- `name`: `str`
- `tests`: `List["TestCaseTypeDef"]`


## TestCaseDefinitionTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import TestCaseDefinitionTypeDef
```




Optional fields:
- `id`: `str`
- `testCaseVersion`: `str`


## TestCaseRunTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import TestCaseRunTypeDef
```




Optional fields:
- `testCaseRunId`: `str`
- `testCaseDefinitionId`: `str`
- `testCaseDefinitionName`: `str`
- `status`: `Status`
- `startTime`: `datetime`
- `endTime`: `datetime`
- `logUrl`: `str`
- `warnings`: `str`
- `failure`: `str`


## TestCaseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import TestCaseTypeDef
```




Optional fields:
- `name`: `str`
- `configuration`: `Dict[str, str]`
- `test`: `"TestCaseDefinitionTypeDef"`


## TestResultTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import TestResultTypeDef
```




Optional fields:
- `groups`: `List["GroupResultTypeDef"]`


## UpdateSuiteDefinitionResponseTypeDef

```python
from mypy_boto3_iotdeviceadvisor.type_defs import UpdateSuiteDefinitionResponseTypeDef
```




Optional fields:
- `suiteDefinitionId`: `str`
- `suiteDefinitionArn`: `str`
- `suiteDefinitionName`: `str`
- `suiteDefinitionVersion`: `str`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`

