# Type annotations for boto3 IoTDeviceAdvisor module

> [Index](../index.md) > IoTDeviceAdvisor

Auto-generated documentation for [IoTDeviceAdvisor](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor)
type annotations stubs module [mypy_boto3_iotdeviceadvisor](https://pypi.org/project/mypy-boto3-iotdeviceadvisor/).

```bash
pip install mypy-boto3-iotdeviceadvisor
```

- [Type annotations for boto3 IoTDeviceAdvisor module](#type-annotations-for-boto3-iotdeviceadvisor-module)
  - [IoTDeviceAdvisorClient](#iotdeviceadvisorclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTDeviceAdvisorClient

Type annotations for  `boto3.client("iotdeviceadvisor")` as [IoTDeviceAdvisorClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient
```


IoTDeviceAdvisorClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_suite_definition](./client.md#create-suite-definition)
- [delete_suite_definition](./client.md#delete-suite-definition)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_suite_definition](./client.md#get-suite-definition)
- [get_suite_run](./client.md#get-suite-run)
- [get_suite_run_report](./client.md#get-suite-run-report)
- [list_suite_definitions](./client.md#list-suite-definitions)
- [list_suite_runs](./client.md#list-suite-runs)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [list_test_cases](./client.md#list-test-cases)
- [start_suite_run](./client.md#start-suite-run)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_suite_definition](./client.md#update-suite-definition)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotdeviceadvisor.literals import Status, ...
```

- [Status](./literals.md#status)
- [SuiteRunStatus](./literals.md#suiterunstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionResponseTypeDef, ...
```

- [CreateSuiteDefinitionResponseTypeDef](./type_defs.md#createsuitedefinitionresponsetypedef)
- [DeviceUnderTestTypeDef](./type_defs.md#deviceundertesttypedef)
- [GetSuiteDefinitionResponseTypeDef](./type_defs.md#getsuitedefinitionresponsetypedef)
- [GetSuiteRunReportResponseTypeDef](./type_defs.md#getsuiterunreportresponsetypedef)
- [GetSuiteRunResponseTypeDef](./type_defs.md#getsuiterunresponsetypedef)
- [GroupResultTypeDef](./type_defs.md#groupresulttypedef)
- [ListSuiteDefinitionsResponseTypeDef](./type_defs.md#listsuitedefinitionsresponsetypedef)
- [ListSuiteRunsResponseTypeDef](./type_defs.md#listsuiterunsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ListTestCasesResponseTypeDef](./type_defs.md#listtestcasesresponsetypedef)
- [StartSuiteRunResponseTypeDef](./type_defs.md#startsuiterunresponsetypedef)
- [SuiteDefinitionConfigurationTypeDef](./type_defs.md#suitedefinitionconfigurationtypedef)
- [SuiteDefinitionInformationTypeDef](./type_defs.md#suitedefinitioninformationtypedef)
- [SuiteRunConfigurationTypeDef](./type_defs.md#suiterunconfigurationtypedef)
- [SuiteRunInformationTypeDef](./type_defs.md#suiteruninformationtypedef)
- [TestCaseCategoryTypeDef](./type_defs.md#testcasecategorytypedef)
- [TestCaseDefinitionTypeDef](./type_defs.md#testcasedefinitiontypedef)
- [TestCaseRunTypeDef](./type_defs.md#testcaseruntypedef)
- [TestCaseTypeDef](./type_defs.md#testcasetypedef)
- [TestResultTypeDef](./type_defs.md#testresulttypedef)
- [UpdateSuiteDefinitionResponseTypeDef](./type_defs.md#updatesuitedefinitionresponsetypedef)
