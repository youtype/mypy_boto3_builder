# KinesisAnalyticsClient for boto3 KinesisAnalytics module

> [Index](../index.md) > [KinesisAnalytics](./index.md) > KinesisAnalyticsClient

Auto-generated documentation for [KinesisAnalytics](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics)
type annotations stubs module [mypy_boto3_kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics/).

- [KinesisAnalyticsClient for boto3 KinesisAnalytics module](#kinesisanalyticsclient-for-boto3-kinesisanalytics-module)
  - [KinesisAnalyticsClient](#kinesisanalyticsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_application_cloud_watch_logging_option](#add_application_cloud_watch_logging_option)
    - [add_application_input](#add_application_input)
    - [add_application_input_processing_configuration](#add_application_input_processing_configuration)
    - [add_application_output](#add_application_output)
    - [add_application_reference_data_source](#add_application_reference_data_source)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [delete_application](#delete_application)
    - [delete_application_cloud_watch_logging_option](#delete_application_cloud_watch_logging_option)
    - [delete_application_input_processing_configuration](#delete_application_input_processing_configuration)
    - [delete_application_output](#delete_application_output)
    - [delete_application_reference_data_source](#delete_application_reference_data_source)
    - [describe_application](#describe_application)
    - [discover_input_schema](#discover_input_schema)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_applications](#list_applications)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_application](#start_application)
    - [stop_application](#stop_application)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_application](#update_application)

## KinesisAnalyticsClient

Type annotations for `boto3.client("kinesisanalytics")`

Can be used directly:

```python
from mypy_boto3_kinesisanalytics.client import KinesisAnalyticsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kinesisanalytics.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CodeValidationException`
- `Exceptions.ConcurrentModificationException`
- `Exceptions.InvalidApplicationConfigurationException`
- `Exceptions.InvalidArgumentException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceProvisionedThroughputExceededException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyTagsException`
- `Exceptions.UnableToDetectSchemaException`
- `Exceptions.UnsupportedOperationException`


## Methods


### add_application_cloud_watch_logging_option

Type annotations for `boto3.client("kinesisanalytics").add_application_cloud_watch_logging_option` method.

[Client.add_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_cloud_watch_logging_option)

```python
def add_application_cloud_watch_logging_option(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef
) -> Dict[str, Any]:
    pass
```

### add_application_input

Type annotations for `boto3.client("kinesisanalytics").add_application_input` method.

[Client.add_application_input documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input)

```python
def add_application_input(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    Input: InputTypeDef
) -> Dict[str, Any]:
    pass
```

### add_application_input_processing_configuration

Type annotations for `boto3.client("kinesisanalytics").add_application_input_processing_configuration` method.

[Client.add_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input_processing_configuration)

```python
def add_application_input_processing_configuration(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    InputId: str,
    InputProcessingConfiguration: "InputProcessingConfigurationTypeDef"
) -> Dict[str, Any]:
    pass
```

### add_application_output

Type annotations for `boto3.client("kinesisanalytics").add_application_output` method.

[Client.add_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_output)

```python
def add_application_output(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    Output: OutputTypeDef
) -> Dict[str, Any]:
    pass
```

### add_application_reference_data_source

Type annotations for `boto3.client("kinesisanalytics").add_application_reference_data_source` method.

[Client.add_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_reference_data_source)

```python
def add_application_reference_data_source(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    ReferenceDataSource: ReferenceDataSourceTypeDef
) -> Dict[str, Any]:
    pass
```

### can_paginate

Type annotations for `boto3.client("kinesisanalytics").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("kinesisanalytics").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.create_application)

```python
def create_application(
    self,
    ApplicationName: str,
    ApplicationDescription: str = None,
    Inputs: List[InputTypeDef] = None,
    Outputs: List[OutputTypeDef] = None,
    CloudWatchLoggingOptions: List[CloudWatchLoggingOptionTypeDef] = None,
    ApplicationCode: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateApplicationResponseTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("kinesisanalytics").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application)

```python
def delete_application(
    self,
    ApplicationName: str,
    CreateTimestamp: datetime
) -> Dict[str, Any]:
    pass
```

### delete_application_cloud_watch_logging_option

Type annotations for `boto3.client("kinesisanalytics").delete_application_cloud_watch_logging_option` method.

[Client.delete_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_cloud_watch_logging_option)

```python
def delete_application_cloud_watch_logging_option(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    CloudWatchLoggingOptionId: str
) -> Dict[str, Any]:
    pass
```

### delete_application_input_processing_configuration

Type annotations for `boto3.client("kinesisanalytics").delete_application_input_processing_configuration` method.

[Client.delete_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_input_processing_configuration)

```python
def delete_application_input_processing_configuration(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    InputId: str
) -> Dict[str, Any]:
    pass
```

### delete_application_output

Type annotations for `boto3.client("kinesisanalytics").delete_application_output` method.

[Client.delete_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_output)

```python
def delete_application_output(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    OutputId: str
) -> Dict[str, Any]:
    pass
```

### delete_application_reference_data_source

Type annotations for `boto3.client("kinesisanalytics").delete_application_reference_data_source` method.

[Client.delete_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_reference_data_source)

```python
def delete_application_reference_data_source(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    ReferenceId: str
) -> Dict[str, Any]:
    pass
```

### describe_application

Type annotations for `boto3.client("kinesisanalytics").describe_application` method.

[Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.describe_application)

```python
def describe_application(
    self,
    ApplicationName: str
) -> DescribeApplicationResponseTypeDef:
    pass
```

### discover_input_schema

Type annotations for `boto3.client("kinesisanalytics").discover_input_schema` method.

[Client.discover_input_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.discover_input_schema)

```python
def discover_input_schema(
    self,
    ResourceARN: str = None,
    RoleARN: str = None,
    InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
    S3Configuration: S3ConfigurationTypeDef = None,
    InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None
) -> DiscoverInputSchemaResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kinesisanalytics").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.generate_presigned_url)

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

### list_applications

Type annotations for `boto3.client("kinesisanalytics").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_applications)

```python
def list_applications(
    self,
    Limit: int = None,
    ExclusiveStartApplicationName: str = None
) -> ListApplicationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("kinesisanalytics").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_application

Type annotations for `boto3.client("kinesisanalytics").start_application` method.

[Client.start_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.start_application)

```python
def start_application(
    self,
    ApplicationName: str,
    InputConfigurations: List[InputConfigurationTypeDef]
) -> Dict[str, Any]:
    pass
```

### stop_application

Type annotations for `boto3.client("kinesisanalytics").stop_application` method.

[Client.stop_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.stop_application)

```python
def stop_application(
    self,
    ApplicationName: str
) -> Dict[str, Any]:
    pass
```

### tag_resource

Type annotations for `boto3.client("kinesisanalytics").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("kinesisanalytics").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_application

Type annotations for `boto3.client("kinesisanalytics").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.update_application)

```python
def update_application(
    self,
    ApplicationName: str,
    CurrentApplicationVersionId: int,
    ApplicationUpdate: ApplicationUpdateTypeDef
) -> Dict[str, Any]:
    pass
```