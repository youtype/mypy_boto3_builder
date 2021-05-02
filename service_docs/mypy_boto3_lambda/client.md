# LambdaClient for boto3 Lambda module

> [Index](../index.md) > [Lambda](./index.md) > LambdaClient

Auto-generated documentation for [Lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda)
type annotations stubs module [mypy_boto3_lambda](https://pypi.org/project/mypy-boto3-lambda/).

- [LambdaClient for boto3 Lambda module](#lambdaclient-for-boto3-lambda-module)
  - [LambdaClient](#lambdaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_layer_version_permission](#add_layer_version_permission)
    - [add_permission](#add_permission)
    - [can_paginate](#can_paginate)
    - [create_alias](#create_alias)
    - [create_code_signing_config](#create_code_signing_config)
    - [create_event_source_mapping](#create_event_source_mapping)
    - [create_function](#create_function)
    - [delete_alias](#delete_alias)
    - [delete_code_signing_config](#delete_code_signing_config)
    - [delete_event_source_mapping](#delete_event_source_mapping)
    - [delete_function](#delete_function)
    - [delete_function_code_signing_config](#delete_function_code_signing_config)
    - [delete_function_concurrency](#delete_function_concurrency)
    - [delete_function_event_invoke_config](#delete_function_event_invoke_config)
    - [delete_layer_version](#delete_layer_version)
    - [delete_provisioned_concurrency_config](#delete_provisioned_concurrency_config)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_account_settings](#get_account_settings)
    - [get_alias](#get_alias)
    - [get_code_signing_config](#get_code_signing_config)
    - [get_event_source_mapping](#get_event_source_mapping)
    - [get_function](#get_function)
    - [get_function_code_signing_config](#get_function_code_signing_config)
    - [get_function_concurrency](#get_function_concurrency)
    - [get_function_configuration](#get_function_configuration)
    - [get_function_event_invoke_config](#get_function_event_invoke_config)
    - [get_layer_version](#get_layer_version)
    - [get_layer_version_by_arn](#get_layer_version_by_arn)
    - [get_layer_version_policy](#get_layer_version_policy)
    - [get_policy](#get_policy)
    - [get_provisioned_concurrency_config](#get_provisioned_concurrency_config)
    - [invoke](#invoke)
    - [invoke_async](#invoke_async)
    - [list_aliases](#list_aliases)
    - [list_code_signing_configs](#list_code_signing_configs)
    - [list_event_source_mappings](#list_event_source_mappings)
    - [list_function_event_invoke_configs](#list_function_event_invoke_configs)
    - [list_functions](#list_functions)
    - [list_functions_by_code_signing_config](#list_functions_by_code_signing_config)
    - [list_layer_versions](#list_layer_versions)
    - [list_layers](#list_layers)
    - [list_provisioned_concurrency_configs](#list_provisioned_concurrency_configs)
    - [list_tags](#list_tags)
    - [list_versions_by_function](#list_versions_by_function)
    - [publish_layer_version](#publish_layer_version)
    - [publish_version](#publish_version)
    - [put_function_code_signing_config](#put_function_code_signing_config)
    - [put_function_concurrency](#put_function_concurrency)
    - [put_function_event_invoke_config](#put_function_event_invoke_config)
    - [put_provisioned_concurrency_config](#put_provisioned_concurrency_config)
    - [remove_layer_version_permission](#remove_layer_version_permission)
    - [remove_permission](#remove_permission)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_alias](#update_alias)
    - [update_code_signing_config](#update_code_signing_config)
    - [update_event_source_mapping](#update_event_source_mapping)
    - [update_function_code](#update_function_code)
    - [update_function_configuration](#update_function_configuration)
    - [update_function_event_invoke_config](#update_function_event_invoke_config)
    - [get_paginator](#get_paginator)
    - [get_waiter](#get_waiter)

## LambdaClient

Type annotations for `boto3.client("lambda")`

Can be used directly:

```python
from mypy_boto3_lambda.client import LambdaClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_lambda.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CodeSigningConfigNotFoundException`
- `Exceptions.CodeStorageExceededException`
- `Exceptions.CodeVerificationFailedException`
- `Exceptions.EC2AccessDeniedException`
- `Exceptions.EC2ThrottledException`
- `Exceptions.EC2UnexpectedException`
- `Exceptions.EFSIOException`
- `Exceptions.EFSMountConnectivityException`
- `Exceptions.EFSMountFailureException`
- `Exceptions.EFSMountTimeoutException`
- `Exceptions.ENILimitReachedException`
- `Exceptions.InvalidCodeSignatureException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidRequestContentException`
- `Exceptions.InvalidRuntimeException`
- `Exceptions.InvalidSecurityGroupIDException`
- `Exceptions.InvalidSubnetIDException`
- `Exceptions.InvalidZipFileException`
- `Exceptions.KMSAccessDeniedException`
- `Exceptions.KMSDisabledException`
- `Exceptions.KMSInvalidStateException`
- `Exceptions.KMSNotFoundException`
- `Exceptions.PolicyLengthExceededException`
- `Exceptions.PreconditionFailedException`
- `Exceptions.ProvisionedConcurrencyConfigNotFoundException`
- `Exceptions.RequestTooLargeException`
- `Exceptions.ResourceConflictException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ResourceNotReadyException`
- `Exceptions.ServiceException`
- `Exceptions.SubnetIPAddressLimitReachedException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnsupportedMediaTypeException`


## Methods


### add_layer_version_permission

Type annotations for `boto3.client("lambda").add_layer_version_permission` method.

[Client.add_layer_version_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.add_layer_version_permission)

```python
def add_layer_version_permission(
    self,
    LayerName: str,
    VersionNumber: int,
    StatementId: str,
    Action: str,
    Principal: str,
    OrganizationId: str = None,
    RevisionId: str = None
) -> AddLayerVersionPermissionResponseTypeDef:
    pass
```

### add_permission

Type annotations for `boto3.client("lambda").add_permission` method.

[Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.add_permission)

```python
def add_permission(
    self,
    FunctionName: str,
    StatementId: str,
    Action: str,
    Principal: str,
    SourceArn: str = None,
    SourceAccount: str = None,
    EventSourceToken: str = None,
    Qualifier: str = None,
    RevisionId: str = None
) -> AddPermissionResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("lambda").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_alias

Type annotations for `boto3.client("lambda").create_alias` method.

[Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.create_alias)

```python
def create_alias(
    self,
    FunctionName: str,
    Name: str,
    FunctionVersion: str,
    Description: str = None,
    RoutingConfig: "AliasRoutingConfigurationTypeDef" = None
) -> "AliasConfigurationTypeDef":
    pass
```

### create_code_signing_config

Type annotations for `boto3.client("lambda").create_code_signing_config` method.

[Client.create_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.create_code_signing_config)

```python
def create_code_signing_config(
    self,
    AllowedPublishers: "AllowedPublishersTypeDef",
    Description: str = None,
    CodeSigningPolicies: "CodeSigningPoliciesTypeDef" = None
) -> CreateCodeSigningConfigResponseTypeDef:
    pass
```

### create_event_source_mapping

Type annotations for `boto3.client("lambda").create_event_source_mapping` method.

[Client.create_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.create_event_source_mapping)

```python
def create_event_source_mapping(
    self,
    FunctionName: str,
    EventSourceArn: str = None,
    Enabled: bool = None,
    BatchSize: int = None,
    MaximumBatchingWindowInSeconds: int = None,
    ParallelizationFactor: int = None,
    StartingPosition: EventSourcePosition = None,
    StartingPositionTimestamp: datetime = None,
    DestinationConfig: "DestinationConfigTypeDef" = None,
    MaximumRecordAgeInSeconds: int = None,
    BisectBatchOnFunctionError: bool = None,
    MaximumRetryAttempts: int = None,
    TumblingWindowInSeconds: int = None,
    Topics: List[str] = None,
    Queues: List[str] = None,
    SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"] = None,
    SelfManagedEventSource: "SelfManagedEventSourceTypeDef" = None,
    FunctionResponseTypes: List[Literal['ReportBatchItemFailures']] = None
) -> "EventSourceMappingConfigurationTypeDef":
    pass
```

### create_function

Type annotations for `boto3.client("lambda").create_function` method.

[Client.create_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.create_function)

```python
def create_function(
    self,
    FunctionName: str,
    Role: str,
    Code: FunctionCodeTypeDef,
    Runtime: Runtime = None,
    Handler: str = None,
    Description: str = None,
    Timeout: int = None,
    MemorySize: int = None,
    Publish: bool = None,
    VpcConfig: VpcConfigTypeDef = None,
    PackageType: PackageType = None,
    DeadLetterConfig: "DeadLetterConfigTypeDef" = None,
    Environment: EnvironmentTypeDef = None,
    KMSKeyArn: str = None,
    TracingConfig: TracingConfigTypeDef = None,
    Tags: Dict[str, str] = None,
    Layers: List[str] = None,
    FileSystemConfigs: List["FileSystemConfigTypeDef"] = None,
    ImageConfig: "ImageConfigTypeDef" = None,
    CodeSigningConfigArn: str = None
) -> "FunctionConfigurationTypeDef":
    pass
```

### delete_alias

Type annotations for `boto3.client("lambda").delete_alias` method.

[Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_alias)

```python
def delete_alias(
    self,
    FunctionName: str,
    Name: str
) -> None:
    pass
```

### delete_code_signing_config

Type annotations for `boto3.client("lambda").delete_code_signing_config` method.

[Client.delete_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_code_signing_config)

```python
def delete_code_signing_config(
    self,
    CodeSigningConfigArn: str
) -> Dict[str, Any]:
    pass
```

### delete_event_source_mapping

Type annotations for `boto3.client("lambda").delete_event_source_mapping` method.

[Client.delete_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_event_source_mapping)

```python
def delete_event_source_mapping(
    self,
    UUID: str
) -> "EventSourceMappingConfigurationTypeDef":
    pass
```

### delete_function

Type annotations for `boto3.client("lambda").delete_function` method.

[Client.delete_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_function)

```python
def delete_function(
    self,
    FunctionName: str,
    Qualifier: str = None
) -> None:
    pass
```

### delete_function_code_signing_config

Type annotations for `boto3.client("lambda").delete_function_code_signing_config` method.

[Client.delete_function_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_function_code_signing_config)

```python
def delete_function_code_signing_config(
    self,
    FunctionName: str
) -> None:
    pass
```

### delete_function_concurrency

Type annotations for `boto3.client("lambda").delete_function_concurrency` method.

[Client.delete_function_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_function_concurrency)

```python
def delete_function_concurrency(
    self,
    FunctionName: str
) -> None:
    pass
```

### delete_function_event_invoke_config

Type annotations for `boto3.client("lambda").delete_function_event_invoke_config` method.

[Client.delete_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_function_event_invoke_config)

```python
def delete_function_event_invoke_config(
    self,
    FunctionName: str,
    Qualifier: str = None
) -> None:
    pass
```

### delete_layer_version

Type annotations for `boto3.client("lambda").delete_layer_version` method.

[Client.delete_layer_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_layer_version)

```python
def delete_layer_version(
    self,
    LayerName: str,
    VersionNumber: int
) -> None:
    pass
```

### delete_provisioned_concurrency_config

Type annotations for `boto3.client("lambda").delete_provisioned_concurrency_config` method.

[Client.delete_provisioned_concurrency_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.delete_provisioned_concurrency_config)

```python
def delete_provisioned_concurrency_config(
    self,
    FunctionName: str,
    Qualifier: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("lambda").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.generate_presigned_url)

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

Type annotations for `boto3.client("lambda").get_account_settings` method.

[Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_account_settings)

```python
def get_account_settings(
    self
) -> GetAccountSettingsResponseTypeDef:
    pass
```

### get_alias

Type annotations for `boto3.client("lambda").get_alias` method.

[Client.get_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_alias)

```python
def get_alias(
    self,
    FunctionName: str,
    Name: str
) -> "AliasConfigurationTypeDef":
    pass
```

### get_code_signing_config

Type annotations for `boto3.client("lambda").get_code_signing_config` method.

[Client.get_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_code_signing_config)

```python
def get_code_signing_config(
    self,
    CodeSigningConfigArn: str
) -> GetCodeSigningConfigResponseTypeDef:
    pass
```

### get_event_source_mapping

Type annotations for `boto3.client("lambda").get_event_source_mapping` method.

[Client.get_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_event_source_mapping)

```python
def get_event_source_mapping(
    self,
    UUID: str
) -> "EventSourceMappingConfigurationTypeDef":
    pass
```

### get_function

Type annotations for `boto3.client("lambda").get_function` method.

[Client.get_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_function)

```python
def get_function(
    self,
    FunctionName: str,
    Qualifier: str = None
) -> GetFunctionResponseTypeDef:
    pass
```

### get_function_code_signing_config

Type annotations for `boto3.client("lambda").get_function_code_signing_config` method.

[Client.get_function_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_function_code_signing_config)

```python
def get_function_code_signing_config(
    self,
    FunctionName: str
) -> GetFunctionCodeSigningConfigResponseTypeDef:
    pass
```

### get_function_concurrency

Type annotations for `boto3.client("lambda").get_function_concurrency` method.

[Client.get_function_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_function_concurrency)

```python
def get_function_concurrency(
    self,
    FunctionName: str
) -> GetFunctionConcurrencyResponseTypeDef:
    pass
```

### get_function_configuration

Type annotations for `boto3.client("lambda").get_function_configuration` method.

[Client.get_function_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_function_configuration)

```python
def get_function_configuration(
    self,
    FunctionName: str,
    Qualifier: str = None
) -> "FunctionConfigurationTypeDef":
    pass
```

### get_function_event_invoke_config

Type annotations for `boto3.client("lambda").get_function_event_invoke_config` method.

[Client.get_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_function_event_invoke_config)

```python
def get_function_event_invoke_config(
    self,
    FunctionName: str,
    Qualifier: str = None
) -> "FunctionEventInvokeConfigTypeDef":
    pass
```

### get_layer_version

Type annotations for `boto3.client("lambda").get_layer_version` method.

[Client.get_layer_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_layer_version)

```python
def get_layer_version(
    self,
    LayerName: str,
    VersionNumber: int
) -> GetLayerVersionResponseTypeDef:
    pass
```

### get_layer_version_by_arn

Type annotations for `boto3.client("lambda").get_layer_version_by_arn` method.

[Client.get_layer_version_by_arn documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_layer_version_by_arn)

```python
def get_layer_version_by_arn(
    self,
    Arn: str
) -> GetLayerVersionResponseTypeDef:
    pass
```

### get_layer_version_policy

Type annotations for `boto3.client("lambda").get_layer_version_policy` method.

[Client.get_layer_version_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_layer_version_policy)

```python
def get_layer_version_policy(
    self,
    LayerName: str,
    VersionNumber: int
) -> GetLayerVersionPolicyResponseTypeDef:
    pass
```

### get_policy

Type annotations for `boto3.client("lambda").get_policy` method.

[Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_policy)

```python
def get_policy(
    self,
    FunctionName: str,
    Qualifier: str = None
) -> GetPolicyResponseTypeDef:
    pass
```

### get_provisioned_concurrency_config

Type annotations for `boto3.client("lambda").get_provisioned_concurrency_config` method.

[Client.get_provisioned_concurrency_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.get_provisioned_concurrency_config)

```python
def get_provisioned_concurrency_config(
    self,
    FunctionName: str,
    Qualifier: str
) -> GetProvisionedConcurrencyConfigResponseTypeDef:
    pass
```

### invoke

Type annotations for `boto3.client("lambda").invoke` method.

[Client.invoke documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke)

```python
def invoke(
    self,
    FunctionName: str,
    InvocationType: InvocationType = None,
    LogType: LogType = None,
    ClientContext: str = None,
    Payload: Union[bytes, IO[bytes]] = None,
    Qualifier: str = None
) -> InvocationResponseTypeDef:
    pass
```

### invoke_async

Type annotations for `boto3.client("lambda").invoke_async` method.

[Client.invoke_async documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke_async)

```python
def invoke_async(
    self,
    FunctionName: str,
    InvokeArgs: Union[bytes, IO[bytes]]
) -> InvokeAsyncResponseTypeDef:
    pass
```

### list_aliases

Type annotations for `boto3.client("lambda").list_aliases` method.

[Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_aliases)

```python
def list_aliases(
    self,
    FunctionName: str,
    FunctionVersion: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListAliasesResponseTypeDef:
    pass
```

### list_code_signing_configs

Type annotations for `boto3.client("lambda").list_code_signing_configs` method.

[Client.list_code_signing_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_code_signing_configs)

```python
def list_code_signing_configs(
    self,
    Marker: str = None,
    MaxItems: int = None
) -> ListCodeSigningConfigsResponseTypeDef:
    pass
```

### list_event_source_mappings

Type annotations for `boto3.client("lambda").list_event_source_mappings` method.

[Client.list_event_source_mappings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_event_source_mappings)

```python
def list_event_source_mappings(
    self,
    EventSourceArn: str = None,
    FunctionName: str = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListEventSourceMappingsResponseTypeDef:
    pass
```

### list_function_event_invoke_configs

Type annotations for `boto3.client("lambda").list_function_event_invoke_configs` method.

[Client.list_function_event_invoke_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_function_event_invoke_configs)

```python
def list_function_event_invoke_configs(
    self,
    FunctionName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListFunctionEventInvokeConfigsResponseTypeDef:
    pass
```

### list_functions

Type annotations for `boto3.client("lambda").list_functions` method.

[Client.list_functions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_functions)

```python
def list_functions(
    self,
    MasterRegion: str = None,
    FunctionVersion: Literal['ALL'] = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListFunctionsResponseTypeDef:
    pass
```

### list_functions_by_code_signing_config

Type annotations for `boto3.client("lambda").list_functions_by_code_signing_config` method.

[Client.list_functions_by_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_functions_by_code_signing_config)

```python
def list_functions_by_code_signing_config(
    self,
    CodeSigningConfigArn: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListFunctionsByCodeSigningConfigResponseTypeDef:
    pass
```

### list_layer_versions

Type annotations for `boto3.client("lambda").list_layer_versions` method.

[Client.list_layer_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_layer_versions)

```python
def list_layer_versions(
    self,
    LayerName: str,
    CompatibleRuntime: Runtime = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListLayerVersionsResponseTypeDef:
    pass
```

### list_layers

Type annotations for `boto3.client("lambda").list_layers` method.

[Client.list_layers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_layers)

```python
def list_layers(
    self,
    CompatibleRuntime: Runtime = None,
    Marker: str = None,
    MaxItems: int = None
) -> ListLayersResponseTypeDef:
    pass
```

### list_provisioned_concurrency_configs

Type annotations for `boto3.client("lambda").list_provisioned_concurrency_configs` method.

[Client.list_provisioned_concurrency_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_provisioned_concurrency_configs)

```python
def list_provisioned_concurrency_configs(
    self,
    FunctionName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListProvisionedConcurrencyConfigsResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("lambda").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_tags)

```python
def list_tags(
    self,
    Resource: str
) -> ListTagsResponseTypeDef:
    pass
```

### list_versions_by_function

Type annotations for `boto3.client("lambda").list_versions_by_function` method.

[Client.list_versions_by_function documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.list_versions_by_function)

```python
def list_versions_by_function(
    self,
    FunctionName: str,
    Marker: str = None,
    MaxItems: int = None
) -> ListVersionsByFunctionResponseTypeDef:
    pass
```

### publish_layer_version

Type annotations for `boto3.client("lambda").publish_layer_version` method.

[Client.publish_layer_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.publish_layer_version)

```python
def publish_layer_version(
    self,
    LayerName: str,
    Content: LayerVersionContentInputTypeDef,
    Description: str = None,
    CompatibleRuntimes: List[Runtime] = None,
    LicenseInfo: str = None
) -> PublishLayerVersionResponseTypeDef:
    pass
```

### publish_version

Type annotations for `boto3.client("lambda").publish_version` method.

[Client.publish_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.publish_version)

```python
def publish_version(
    self,
    FunctionName: str,
    CodeSha256: str = None,
    Description: str = None,
    RevisionId: str = None
) -> "FunctionConfigurationTypeDef":
    pass
```

### put_function_code_signing_config

Type annotations for `boto3.client("lambda").put_function_code_signing_config` method.

[Client.put_function_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.put_function_code_signing_config)

```python
def put_function_code_signing_config(
    self,
    CodeSigningConfigArn: str,
    FunctionName: str
) -> PutFunctionCodeSigningConfigResponseTypeDef:
    pass
```

### put_function_concurrency

Type annotations for `boto3.client("lambda").put_function_concurrency` method.

[Client.put_function_concurrency documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.put_function_concurrency)

```python
def put_function_concurrency(
    self,
    FunctionName: str,
    ReservedConcurrentExecutions: int
) -> "ConcurrencyTypeDef":
    pass
```

### put_function_event_invoke_config

Type annotations for `boto3.client("lambda").put_function_event_invoke_config` method.

[Client.put_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.put_function_event_invoke_config)

```python
def put_function_event_invoke_config(
    self,
    FunctionName: str,
    Qualifier: str = None,
    MaximumRetryAttempts: int = None,
    MaximumEventAgeInSeconds: int = None,
    DestinationConfig: "DestinationConfigTypeDef" = None
) -> "FunctionEventInvokeConfigTypeDef":
    pass
```

### put_provisioned_concurrency_config

Type annotations for `boto3.client("lambda").put_provisioned_concurrency_config` method.

[Client.put_provisioned_concurrency_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.put_provisioned_concurrency_config)

```python
def put_provisioned_concurrency_config(
    self,
    FunctionName: str,
    Qualifier: str,
    ProvisionedConcurrentExecutions: int
) -> PutProvisionedConcurrencyConfigResponseTypeDef:
    pass
```

### remove_layer_version_permission

Type annotations for `boto3.client("lambda").remove_layer_version_permission` method.

[Client.remove_layer_version_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.remove_layer_version_permission)

```python
def remove_layer_version_permission(
    self,
    LayerName: str,
    VersionNumber: int,
    StatementId: str,
    RevisionId: str = None
) -> None:
    pass
```

### remove_permission

Type annotations for `boto3.client("lambda").remove_permission` method.

[Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.remove_permission)

```python
def remove_permission(
    self,
    FunctionName: str,
    StatementId: str,
    Qualifier: str = None,
    RevisionId: str = None
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("lambda").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.tag_resource)

```python
def tag_resource(
    self,
    Resource: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("lambda").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.untag_resource)

```python
def untag_resource(
    self,
    Resource: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_alias

Type annotations for `boto3.client("lambda").update_alias` method.

[Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_alias)

```python
def update_alias(
    self,
    FunctionName: str,
    Name: str,
    FunctionVersion: str = None,
    Description: str = None,
    RoutingConfig: "AliasRoutingConfigurationTypeDef" = None,
    RevisionId: str = None
) -> "AliasConfigurationTypeDef":
    pass
```

### update_code_signing_config

Type annotations for `boto3.client("lambda").update_code_signing_config` method.

[Client.update_code_signing_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_code_signing_config)

```python
def update_code_signing_config(
    self,
    CodeSigningConfigArn: str,
    Description: str = None,
    AllowedPublishers: "AllowedPublishersTypeDef" = None,
    CodeSigningPolicies: "CodeSigningPoliciesTypeDef" = None
) -> UpdateCodeSigningConfigResponseTypeDef:
    pass
```

### update_event_source_mapping

Type annotations for `boto3.client("lambda").update_event_source_mapping` method.

[Client.update_event_source_mapping documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_event_source_mapping)

```python
def update_event_source_mapping(
    self,
    UUID: str,
    FunctionName: str = None,
    Enabled: bool = None,
    BatchSize: int = None,
    MaximumBatchingWindowInSeconds: int = None,
    DestinationConfig: "DestinationConfigTypeDef" = None,
    MaximumRecordAgeInSeconds: int = None,
    BisectBatchOnFunctionError: bool = None,
    MaximumRetryAttempts: int = None,
    ParallelizationFactor: int = None,
    SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"] = None,
    TumblingWindowInSeconds: int = None,
    FunctionResponseTypes: List[Literal['ReportBatchItemFailures']] = None
) -> "EventSourceMappingConfigurationTypeDef":
    pass
```

### update_function_code

Type annotations for `boto3.client("lambda").update_function_code` method.

[Client.update_function_code documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_function_code)

```python
def update_function_code(
    self,
    FunctionName: str,
    ZipFile: Union[bytes, IO[bytes]] = None,
    S3Bucket: str = None,
    S3Key: str = None,
    S3ObjectVersion: str = None,
    ImageUri: str = None,
    Publish: bool = None,
    DryRun: bool = None,
    RevisionId: str = None
) -> "FunctionConfigurationTypeDef":
    pass
```

### update_function_configuration

Type annotations for `boto3.client("lambda").update_function_configuration` method.

[Client.update_function_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_function_configuration)

```python
def update_function_configuration(
    self,
    FunctionName: str,
    Role: str = None,
    Handler: str = None,
    Description: str = None,
    Timeout: int = None,
    MemorySize: int = None,
    VpcConfig: VpcConfigTypeDef = None,
    Environment: EnvironmentTypeDef = None,
    Runtime: Runtime = None,
    DeadLetterConfig: "DeadLetterConfigTypeDef" = None,
    KMSKeyArn: str = None,
    TracingConfig: TracingConfigTypeDef = None,
    RevisionId: str = None,
    Layers: List[str] = None,
    FileSystemConfigs: List["FileSystemConfigTypeDef"] = None,
    ImageConfig: "ImageConfigTypeDef" = None
) -> "FunctionConfigurationTypeDef":
    pass
```

### update_function_event_invoke_config

Type annotations for `boto3.client("lambda").update_function_event_invoke_config` method.

[Client.update_function_event_invoke_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.update_function_event_invoke_config)

```python
def update_function_event_invoke_config(
    self,
    FunctionName: str,
    Qualifier: str = None,
    MaximumRetryAttempts: int = None,
    MaximumEventAgeInSeconds: int = None,
    DestinationConfig: "DestinationConfigTypeDef" = None
) -> "FunctionEventInvokeConfigTypeDef":
    pass
```



### get_paginator

Type annotations for `boto3.client("lambda").get_paginator` method with overloads.

- `client.get_paginator("list_aliases")` -> [ListAliasesPaginator](./paginators.md#listaliasespaginator)
- `client.get_paginator("list_code_signing_configs")` -> [ListCodeSigningConfigsPaginator](./paginators.md#listcodesigningconfigspaginator)
- `client.get_paginator("list_event_source_mappings")` -> [ListEventSourceMappingsPaginator](./paginators.md#listeventsourcemappingspaginator)
- `client.get_paginator("list_function_event_invoke_configs")` -> [ListFunctionEventInvokeConfigsPaginator](./paginators.md#listfunctioneventinvokeconfigspaginator)
- `client.get_paginator("list_functions")` -> [ListFunctionsPaginator](./paginators.md#listfunctionspaginator)
- `client.get_paginator("list_functions_by_code_signing_config")` -> [ListFunctionsByCodeSigningConfigPaginator](./paginators.md#listfunctionsbycodesigningconfigpaginator)
- `client.get_paginator("list_layer_versions")` -> [ListLayerVersionsPaginator](./paginators.md#listlayerversionspaginator)
- `client.get_paginator("list_layers")` -> [ListLayersPaginator](./paginators.md#listlayerspaginator)
- `client.get_paginator("list_provisioned_concurrency_configs")` -> [ListProvisionedConcurrencyConfigsPaginator](./paginators.md#listprovisionedconcurrencyconfigspaginator)
- `client.get_paginator("list_versions_by_function")` -> [ListVersionsByFunctionPaginator](./paginators.md#listversionsbyfunctionpaginator)




### get_waiter

Type annotations for `boto3.client("lambda").get_waiter` method with overloads.

- `client.get_waiter("function_active")` -> [FunctionActiveWaiter](./waiters.md#functionactivewaiter)
- `client.get_waiter("function_exists")` -> [FunctionExistsWaiter](./waiters.md#functionexistswaiter)
- `client.get_waiter("function_updated")` -> [FunctionUpdatedWaiter](./waiters.md#functionupdatedwaiter)
