# IoTEventsClient for boto3 IoTEvents module

> [Index](../index.md) > [IoTEvents](./index.md) > IoTEventsClient

Auto-generated documentation for [IoTEvents](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents)
type annotations stubs module [mypy_boto3_iotevents](https://pypi.org/project/mypy-boto3-iotevents/).

- [IoTEventsClient for boto3 IoTEvents module](#ioteventsclient-for-boto3-iotevents-module)
  - [IoTEventsClient](#ioteventsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_detector_model](#create_detector_model)
    - [create_input](#create_input)
    - [delete_detector_model](#delete_detector_model)
    - [delete_input](#delete_input)
    - [describe_detector_model](#describe_detector_model)
    - [describe_detector_model_analysis](#describe_detector_model_analysis)
    - [describe_input](#describe_input)
    - [describe_logging_options](#describe_logging_options)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_detector_model_analysis_results](#get_detector_model_analysis_results)
    - [list_detector_model_versions](#list_detector_model_versions)
    - [list_detector_models](#list_detector_models)
    - [list_inputs](#list_inputs)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_logging_options](#put_logging_options)
    - [start_detector_model_analysis](#start_detector_model_analysis)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_detector_model](#update_detector_model)
    - [update_input](#update_input)

## IoTEventsClient

Type annotations for `boto3.client("iotevents")`

Can be used directly:

```python
from mypy_boto3_iotevents.client import IoTEventsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_iotevents.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.InternalFailureException`
- `Exceptions.InvalidRequestException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`
- `Exceptions.UnsupportedOperationException`


## Methods


### can_paginate

Type annotations for `boto3.client("iotevents").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_detector_model

Type annotations for `boto3.client("iotevents").create_detector_model` method.

[Client.create_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.create_detector_model)

```python
def create_detector_model(
    self,
    detectorModelName: str,
    detectorModelDefinition: "DetectorModelDefinitionTypeDef",
    roleArn: str,
    detectorModelDescription: str = None,
    key: str = None,
    tags: List["TagTypeDef"] = None,
    evaluationMethod: EvaluationMethod = None
) -> CreateDetectorModelResponseTypeDef:
    pass
```

### create_input

Type annotations for `boto3.client("iotevents").create_input` method.

[Client.create_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.create_input)

```python
def create_input(
    self,
    inputName: str,
    inputDefinition: "InputDefinitionTypeDef",
    inputDescription: str = None,
    tags: List["TagTypeDef"] = None
) -> CreateInputResponseTypeDef:
    pass
```

### delete_detector_model

Type annotations for `boto3.client("iotevents").delete_detector_model` method.

[Client.delete_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.delete_detector_model)

```python
def delete_detector_model(
    self,
    detectorModelName: str
) -> Dict[str, Any]:
    pass
```

### delete_input

Type annotations for `boto3.client("iotevents").delete_input` method.

[Client.delete_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.delete_input)

```python
def delete_input(
    self,
    inputName: str
) -> Dict[str, Any]:
    pass
```

### describe_detector_model

Type annotations for `boto3.client("iotevents").describe_detector_model` method.

[Client.describe_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model)

```python
def describe_detector_model(
    self,
    detectorModelName: str,
    detectorModelVersion: str = None
) -> DescribeDetectorModelResponseTypeDef:
    pass
```

### describe_detector_model_analysis

Type annotations for `boto3.client("iotevents").describe_detector_model_analysis` method.

[Client.describe_detector_model_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model_analysis)

```python
def describe_detector_model_analysis(
    self,
    analysisId: str
) -> DescribeDetectorModelAnalysisResponseTypeDef:
    pass
```

### describe_input

Type annotations for `boto3.client("iotevents").describe_input` method.

[Client.describe_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.describe_input)

```python
def describe_input(
    self,
    inputName: str
) -> DescribeInputResponseTypeDef:
    pass
```

### describe_logging_options

Type annotations for `boto3.client("iotevents").describe_logging_options` method.

[Client.describe_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.describe_logging_options)

```python
def describe_logging_options(
    self
) -> DescribeLoggingOptionsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("iotevents").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.generate_presigned_url)

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

### get_detector_model_analysis_results

Type annotations for `boto3.client("iotevents").get_detector_model_analysis_results` method.

[Client.get_detector_model_analysis_results documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.get_detector_model_analysis_results)

```python
def get_detector_model_analysis_results(
    self,
    analysisId: str,
    nextToken: str = None,
    maxResults: int = None
) -> GetDetectorModelAnalysisResultsResponseTypeDef:
    pass
```

### list_detector_model_versions

Type annotations for `boto3.client("iotevents").list_detector_model_versions` method.

[Client.list_detector_model_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.list_detector_model_versions)

```python
def list_detector_model_versions(
    self,
    detectorModelName: str,
    nextToken: str = None,
    maxResults: int = None
) -> ListDetectorModelVersionsResponseTypeDef:
    pass
```

### list_detector_models

Type annotations for `boto3.client("iotevents").list_detector_models` method.

[Client.list_detector_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.list_detector_models)

```python
def list_detector_models(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListDetectorModelsResponseTypeDef:
    pass
```

### list_inputs

Type annotations for `boto3.client("iotevents").list_inputs` method.

[Client.list_inputs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.list_inputs)

```python
def list_inputs(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListInputsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("iotevents").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_logging_options

Type annotations for `boto3.client("iotevents").put_logging_options` method.

[Client.put_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.put_logging_options)

```python
def put_logging_options(
    self,
    loggingOptions: "LoggingOptionsTypeDef"
) -> None:
    pass
```

### start_detector_model_analysis

Type annotations for `boto3.client("iotevents").start_detector_model_analysis` method.

[Client.start_detector_model_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.start_detector_model_analysis)

```python
def start_detector_model_analysis(
    self,
    detectorModelDefinition: "DetectorModelDefinitionTypeDef"
) -> StartDetectorModelAnalysisResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("iotevents").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("iotevents").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_detector_model

Type annotations for `boto3.client("iotevents").update_detector_model` method.

[Client.update_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.update_detector_model)

```python
def update_detector_model(
    self,
    detectorModelName: str,
    detectorModelDefinition: "DetectorModelDefinitionTypeDef",
    roleArn: str,
    detectorModelDescription: str = None,
    evaluationMethod: EvaluationMethod = None
) -> UpdateDetectorModelResponseTypeDef:
    pass
```

### update_input

Type annotations for `boto3.client("iotevents").update_input` method.

[Client.update_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html#IoTEvents.Client.update_input)

```python
def update_input(
    self,
    inputName: str,
    inputDefinition: "InputDefinitionTypeDef",
    inputDescription: str = None
) -> UpdateInputResponseTypeDef:
    pass
```



