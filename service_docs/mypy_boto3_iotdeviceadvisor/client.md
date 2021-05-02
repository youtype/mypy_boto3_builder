# IoTDeviceAdvisorClient for boto3 IoTDeviceAdvisor module

> [Index](../index.md) > [IoTDeviceAdvisor](./index.md) > IoTDeviceAdvisorClient

Auto-generated documentation for [IoTDeviceAdvisor](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor)
type annotations stubs module [mypy_boto3_iotdeviceadvisor](https://pypi.org/project/mypy-boto3-iotdeviceadvisor/).

- [IoTDeviceAdvisorClient for boto3 IoTDeviceAdvisor module](#iotdeviceadvisorclient-for-boto3-iotdeviceadvisor-module)
  - [IoTDeviceAdvisorClient](#iotdeviceadvisorclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_suite_definition](#create_suite_definition)
    - [delete_suite_definition](#delete_suite_definition)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_suite_definition](#get_suite_definition)
    - [get_suite_run](#get_suite_run)
    - [get_suite_run_report](#get_suite_run_report)
    - [list_suite_definitions](#list_suite_definitions)
    - [list_suite_runs](#list_suite_runs)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_test_cases](#list_test_cases)
    - [start_suite_run](#start_suite_run)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_suite_definition](#update_suite_definition)

## IoTDeviceAdvisorClient

Type annotations for `boto3.client("iotdeviceadvisor")`

Can be used directly:

```python
from mypy_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotdeviceadvisor.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("iotdeviceadvisor").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_suite_definition

Type annotations for `boto3.client("iotdeviceadvisor").create_suite_definition` method.

[Client.create_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.create_suite_definition)

```python
def create_suite_definition(
    self,
    suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
    tags: Dict[str, str] = None
) -> CreateSuiteDefinitionResponseTypeDef:
    pass
```

### delete_suite_definition

Type annotations for `boto3.client("iotdeviceadvisor").delete_suite_definition` method.

[Client.delete_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.delete_suite_definition)

```python
def delete_suite_definition(
    self,
    suiteDefinitionId: str
) -> Dict[str, Any]:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotdeviceadvisor").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.generate_presigned_url)

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

### get_suite_definition

Type annotations for `boto3.client("iotdeviceadvisor").get_suite_definition` method.

[Client.get_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_definition)

```python
def get_suite_definition(
    self,
    suiteDefinitionId: str,
    suiteDefinitionVersion: str = None
) -> GetSuiteDefinitionResponseTypeDef:
    pass
```

### get_suite_run

Type annotations for `boto3.client("iotdeviceadvisor").get_suite_run` method.

[Client.get_suite_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run)

```python
def get_suite_run(
    self,
    suiteDefinitionId: str,
    suiteRunId: str
) -> GetSuiteRunResponseTypeDef:
    pass
```

### get_suite_run_report

Type annotations for `boto3.client("iotdeviceadvisor").get_suite_run_report` method.

[Client.get_suite_run_report documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run_report)

```python
def get_suite_run_report(
    self,
    suiteDefinitionId: str,
    suiteRunId: str
) -> GetSuiteRunReportResponseTypeDef:
    pass
```

### list_suite_definitions

Type annotations for `boto3.client("iotdeviceadvisor").list_suite_definitions` method.

[Client.list_suite_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_definitions)

```python
def list_suite_definitions(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListSuiteDefinitionsResponseTypeDef:
    pass
```

### list_suite_runs

Type annotations for `boto3.client("iotdeviceadvisor").list_suite_runs` method.

[Client.list_suite_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_runs)

```python
def list_suite_runs(
    self,
    suiteDefinitionId: str = None,
    suiteDefinitionVersion: str = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListSuiteRunsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotdeviceadvisor").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_test_cases

Type annotations for `boto3.client("iotdeviceadvisor").list_test_cases` method.

[Client.list_test_cases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_test_cases)

```python
def list_test_cases(
    self,
    intendedForQualification: bool = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListTestCasesResponseTypeDef:
    pass
```

### start_suite_run

Type annotations for `boto3.client("iotdeviceadvisor").start_suite_run` method.

[Client.start_suite_run documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.start_suite_run)

```python
def start_suite_run(
    self,
    suiteDefinitionId: str,
    suiteDefinitionVersion: str = None,
    suiteRunConfiguration: "SuiteRunConfigurationTypeDef" = None,
    tags: Dict[str, str] = None
) -> StartSuiteRunResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotdeviceadvisor").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotdeviceadvisor").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_suite_definition

Type annotations for `boto3.client("iotdeviceadvisor").update_suite_definition` method.

[Client.update_suite_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.update_suite_definition)

```python
def update_suite_definition(
    self,
    suiteDefinitionId: str,
    suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None
) -> UpdateSuiteDefinitionResponseTypeDef:
    pass
```



