# Structures for boto3 Lambda module

> [Index](../index.md) > [Lambda](./index.md) > Structures

Auto-generated documentation for [Lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda)
type annotations stubs module [mypy_boto3_lambda](https://pypi.org/project/mypy-boto3-lambda/).

- [Structures for boto3 Lambda module](#structures-for-boto3-lambda-module)
  - [AccountLimitTypeDef](#accountlimittypedef)
  - [AccountUsageTypeDef](#accountusagetypedef)
  - [AddLayerVersionPermissionResponseTypeDef](#addlayerversionpermissionresponsetypedef)
  - [AddPermissionResponseTypeDef](#addpermissionresponsetypedef)
  - [AliasConfigurationTypeDef](#aliasconfigurationtypedef)
  - [AliasRoutingConfigurationTypeDef](#aliasroutingconfigurationtypedef)
  - [AllowedPublishersTypeDef](#allowedpublisherstypedef)
  - [CodeSigningConfigTypeDef](#codesigningconfigtypedef)
  - [CodeSigningPoliciesTypeDef](#codesigningpoliciestypedef)
  - [ConcurrencyTypeDef](#concurrencytypedef)
  - [CreateCodeSigningConfigResponseTypeDef](#createcodesigningconfigresponsetypedef)
  - [DeadLetterConfigTypeDef](#deadletterconfigtypedef)
  - [DestinationConfigTypeDef](#destinationconfigtypedef)
  - [EnvironmentErrorTypeDef](#environmenterrortypedef)
  - [EnvironmentResponseTypeDef](#environmentresponsetypedef)
  - [EnvironmentTypeDef](#environmenttypedef)
  - [EventSourceMappingConfigurationTypeDef](#eventsourcemappingconfigurationtypedef)
  - [FileSystemConfigTypeDef](#filesystemconfigtypedef)
  - [FunctionCodeLocationTypeDef](#functioncodelocationtypedef)
  - [FunctionCodeTypeDef](#functioncodetypedef)
  - [FunctionConfigurationTypeDef](#functionconfigurationtypedef)
  - [FunctionEventInvokeConfigTypeDef](#functioneventinvokeconfigtypedef)
  - [GetAccountSettingsResponseTypeDef](#getaccountsettingsresponsetypedef)
  - [GetCodeSigningConfigResponseTypeDef](#getcodesigningconfigresponsetypedef)
  - [GetFunctionCodeSigningConfigResponseTypeDef](#getfunctioncodesigningconfigresponsetypedef)
  - [GetFunctionConcurrencyResponseTypeDef](#getfunctionconcurrencyresponsetypedef)
  - [GetFunctionResponseTypeDef](#getfunctionresponsetypedef)
  - [GetLayerVersionPolicyResponseTypeDef](#getlayerversionpolicyresponsetypedef)
  - [GetLayerVersionResponseTypeDef](#getlayerversionresponsetypedef)
  - [GetPolicyResponseTypeDef](#getpolicyresponsetypedef)
  - [GetProvisionedConcurrencyConfigResponseTypeDef](#getprovisionedconcurrencyconfigresponsetypedef)
  - [ImageConfigErrorTypeDef](#imageconfigerrortypedef)
  - [ImageConfigResponseTypeDef](#imageconfigresponsetypedef)
  - [ImageConfigTypeDef](#imageconfigtypedef)
  - [InvocationResponseTypeDef](#invocationresponsetypedef)
  - [InvokeAsyncResponseTypeDef](#invokeasyncresponsetypedef)
  - [LayerTypeDef](#layertypedef)
  - [LayerVersionContentInputTypeDef](#layerversioncontentinputtypedef)
  - [LayerVersionContentOutputTypeDef](#layerversioncontentoutputtypedef)
  - [LayerVersionsListItemTypeDef](#layerversionslistitemtypedef)
  - [LayersListItemTypeDef](#layerslistitemtypedef)
  - [ListAliasesResponseTypeDef](#listaliasesresponsetypedef)
  - [ListCodeSigningConfigsResponseTypeDef](#listcodesigningconfigsresponsetypedef)
  - [ListEventSourceMappingsResponseTypeDef](#listeventsourcemappingsresponsetypedef)
  - [ListFunctionEventInvokeConfigsResponseTypeDef](#listfunctioneventinvokeconfigsresponsetypedef)
  - [ListFunctionsByCodeSigningConfigResponseTypeDef](#listfunctionsbycodesigningconfigresponsetypedef)
  - [ListFunctionsResponseTypeDef](#listfunctionsresponsetypedef)
  - [ListLayerVersionsResponseTypeDef](#listlayerversionsresponsetypedef)
  - [ListLayersResponseTypeDef](#listlayersresponsetypedef)
  - [ListProvisionedConcurrencyConfigsResponseTypeDef](#listprovisionedconcurrencyconfigsresponsetypedef)
  - [ListTagsResponseTypeDef](#listtagsresponsetypedef)
  - [ListVersionsByFunctionResponseTypeDef](#listversionsbyfunctionresponsetypedef)
  - [OnFailureTypeDef](#onfailuretypedef)
  - [OnSuccessTypeDef](#onsuccesstypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProvisionedConcurrencyConfigListItemTypeDef](#provisionedconcurrencyconfiglistitemtypedef)
  - [PublishLayerVersionResponseTypeDef](#publishlayerversionresponsetypedef)
  - [PutFunctionCodeSigningConfigResponseTypeDef](#putfunctioncodesigningconfigresponsetypedef)
  - [PutProvisionedConcurrencyConfigResponseTypeDef](#putprovisionedconcurrencyconfigresponsetypedef)
  - [ResponseMetadata](#responsemetadata)
  - [SelfManagedEventSourceTypeDef](#selfmanagedeventsourcetypedef)
  - [SourceAccessConfigurationTypeDef](#sourceaccessconfigurationtypedef)
  - [TracingConfigResponseTypeDef](#tracingconfigresponsetypedef)
  - [TracingConfigTypeDef](#tracingconfigtypedef)
  - [UpdateCodeSigningConfigResponseTypeDef](#updatecodesigningconfigresponsetypedef)
  - [VpcConfigResponseTypeDef](#vpcconfigresponsetypedef)
  - [VpcConfigTypeDef](#vpcconfigtypedef)
  - [WaiterConfigTypeDef](#waiterconfigtypedef)

## AccountLimitTypeDef

```python
from mypy_boto3_lambda.type_defs import AccountLimitTypeDef
```




Optional fields:
- `TotalCodeSize`: `int`
- `CodeSizeUnzipped`: `int`
- `CodeSizeZipped`: `int`
- `ConcurrentExecutions`: `int`
- `UnreservedConcurrentExecutions`: `int`


## AccountUsageTypeDef

```python
from mypy_boto3_lambda.type_defs import AccountUsageTypeDef
```




Optional fields:
- `TotalCodeSize`: `int`
- `FunctionCount`: `int`


## AddLayerVersionPermissionResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import AddLayerVersionPermissionResponseTypeDef
```




Optional fields:
- `Statement`: `str`
- `RevisionId`: `str`


## AddPermissionResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import AddPermissionResponseTypeDef
```




Optional fields:
- `Statement`: `str`


## AliasConfigurationTypeDef

```python
from mypy_boto3_lambda.type_defs import AliasConfigurationTypeDef
```




Optional fields:
- `AliasArn`: `str`
- `Name`: `str`
- `FunctionVersion`: `str`
- `Description`: `str`
- `RoutingConfig`: `"AliasRoutingConfigurationTypeDef"`
- `RevisionId`: `str`


## AliasRoutingConfigurationTypeDef

```python
from mypy_boto3_lambda.type_defs import AliasRoutingConfigurationTypeDef
```




Optional fields:
- `AdditionalVersionWeights`: `Dict[str, float]`


## AllowedPublishersTypeDef

```python
from mypy_boto3_lambda.type_defs import AllowedPublishersTypeDef
```


Required fields:
- `SigningProfileVersionArns`: `List[str]`




## CodeSigningConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import CodeSigningConfigTypeDef
```


Required fields:
- `CodeSigningConfigId`: `str`
- `CodeSigningConfigArn`: `str`
- `AllowedPublishers`: `"AllowedPublishersTypeDef"`
- `CodeSigningPolicies`: `"CodeSigningPoliciesTypeDef"`
- `LastModified`: `str`



Optional fields:
- `Description`: `str`


## CodeSigningPoliciesTypeDef

```python
from mypy_boto3_lambda.type_defs import CodeSigningPoliciesTypeDef
```




Optional fields:
- `UntrustedArtifactOnDeployment`: `CodeSigningPolicy`


## ConcurrencyTypeDef

```python
from mypy_boto3_lambda.type_defs import ConcurrencyTypeDef
```




Optional fields:
- `ReservedConcurrentExecutions`: `int`


## CreateCodeSigningConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import CreateCodeSigningConfigResponseTypeDef
```


Required fields:
- `CodeSigningConfig`: `"CodeSigningConfigTypeDef"`




## DeadLetterConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import DeadLetterConfigTypeDef
```




Optional fields:
- `TargetArn`: `str`


## DestinationConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import DestinationConfigTypeDef
```




Optional fields:
- `OnSuccess`: `"OnSuccessTypeDef"`
- `OnFailure`: `"OnFailureTypeDef"`


## EnvironmentErrorTypeDef

```python
from mypy_boto3_lambda.type_defs import EnvironmentErrorTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `Message`: `str`


## EnvironmentResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import EnvironmentResponseTypeDef
```




Optional fields:
- `Variables`: `Dict[str, str]`
- `Error`: `"EnvironmentErrorTypeDef"`


## EnvironmentTypeDef

```python
from mypy_boto3_lambda.type_defs import EnvironmentTypeDef
```




Optional fields:
- `Variables`: `Dict[str, str]`


## EventSourceMappingConfigurationTypeDef

```python
from mypy_boto3_lambda.type_defs import EventSourceMappingConfigurationTypeDef
```




Optional fields:
- `UUID`: `str`
- `StartingPosition`: `EventSourcePosition`
- `StartingPositionTimestamp`: `datetime`
- `BatchSize`: `int`
- `MaximumBatchingWindowInSeconds`: `int`
- `ParallelizationFactor`: `int`
- `EventSourceArn`: `str`
- `FunctionArn`: `str`
- `LastModified`: `datetime`
- `LastProcessingResult`: `str`
- `State`: `str`
- `StateTransitionReason`: `str`
- `DestinationConfig`: `"DestinationConfigTypeDef"`
- `Topics`: `List[str]`
- `Queues`: `List[str]`
- `SourceAccessConfigurations`: `List["SourceAccessConfigurationTypeDef"]`
- `SelfManagedEventSource`: `"SelfManagedEventSourceTypeDef"`
- `MaximumRecordAgeInSeconds`: `int`
- `BisectBatchOnFunctionError`: `bool`
- `MaximumRetryAttempts`: `int`
- `TumblingWindowInSeconds`: `int`
- `FunctionResponseTypes`: `List[Literal['ReportBatchItemFailures']]`


## FileSystemConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import FileSystemConfigTypeDef
```


Required fields:
- `Arn`: `str`
- `LocalMountPath`: `str`




## FunctionCodeLocationTypeDef

```python
from mypy_boto3_lambda.type_defs import FunctionCodeLocationTypeDef
```




Optional fields:
- `RepositoryType`: `str`
- `Location`: `str`
- `ImageUri`: `str`
- `ResolvedImageUri`: `str`


## FunctionCodeTypeDef

```python
from mypy_boto3_lambda.type_defs import FunctionCodeTypeDef
```




Optional fields:
- `ZipFile`: `Union[bytes, IO[bytes]]`
- `S3Bucket`: `str`
- `S3Key`: `str`
- `S3ObjectVersion`: `str`
- `ImageUri`: `str`


## FunctionConfigurationTypeDef

```python
from mypy_boto3_lambda.type_defs import FunctionConfigurationTypeDef
```




Optional fields:
- `FunctionName`: `str`
- `FunctionArn`: `str`
- `Runtime`: `Runtime`
- `Role`: `str`
- `Handler`: `str`
- `CodeSize`: `int`
- `Description`: `str`
- `Timeout`: `int`
- `MemorySize`: `int`
- `LastModified`: `str`
- `CodeSha256`: `str`
- `Version`: `str`
- `VpcConfig`: `"VpcConfigResponseTypeDef"`
- `DeadLetterConfig`: `"DeadLetterConfigTypeDef"`
- `Environment`: `"EnvironmentResponseTypeDef"`
- `KMSKeyArn`: `str`
- `TracingConfig`: `"TracingConfigResponseTypeDef"`
- `MasterArn`: `str`
- `RevisionId`: `str`
- `Layers`: `List["LayerTypeDef"]`
- `State`: `State`
- `StateReason`: `str`
- `StateReasonCode`: `StateReasonCode`
- `LastUpdateStatus`: `LastUpdateStatus`
- `LastUpdateStatusReason`: `str`
- `LastUpdateStatusReasonCode`: `LastUpdateStatusReasonCode`
- `FileSystemConfigs`: `List["FileSystemConfigTypeDef"]`
- `PackageType`: `PackageType`
- `ImageConfigResponse`: `"ImageConfigResponseTypeDef"`
- `SigningProfileVersionArn`: `str`
- `SigningJobArn`: `str`


## FunctionEventInvokeConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import FunctionEventInvokeConfigTypeDef
```




Optional fields:
- `LastModified`: `datetime`
- `FunctionArn`: `str`
- `MaximumRetryAttempts`: `int`
- `MaximumEventAgeInSeconds`: `int`
- `DestinationConfig`: `"DestinationConfigTypeDef"`


## GetAccountSettingsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetAccountSettingsResponseTypeDef
```




Optional fields:
- `AccountLimit`: `"AccountLimitTypeDef"`
- `AccountUsage`: `"AccountUsageTypeDef"`


## GetCodeSigningConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetCodeSigningConfigResponseTypeDef
```


Required fields:
- `CodeSigningConfig`: `"CodeSigningConfigTypeDef"`




## GetFunctionCodeSigningConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetFunctionCodeSigningConfigResponseTypeDef
```


Required fields:
- `CodeSigningConfigArn`: `str`
- `FunctionName`: `str`




## GetFunctionConcurrencyResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetFunctionConcurrencyResponseTypeDef
```




Optional fields:
- `ReservedConcurrentExecutions`: `int`


## GetFunctionResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetFunctionResponseTypeDef
```




Optional fields:
- `Configuration`: `"FunctionConfigurationTypeDef"`
- `Code`: `"FunctionCodeLocationTypeDef"`
- `Tags`: `Dict[str, str]`
- `Concurrency`: `"ConcurrencyTypeDef"`


## GetLayerVersionPolicyResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetLayerVersionPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`
- `RevisionId`: `str`


## GetLayerVersionResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetLayerVersionResponseTypeDef
```




Optional fields:
- `Content`: `"LayerVersionContentOutputTypeDef"`
- `LayerArn`: `str`
- `LayerVersionArn`: `str`
- `Description`: `str`
- `CreatedDate`: `str`
- `Version`: `int`
- `CompatibleRuntimes`: `List[Runtime]`
- `LicenseInfo`: `str`


## GetPolicyResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetPolicyResponseTypeDef
```




Optional fields:
- `Policy`: `str`
- `RevisionId`: `str`


## GetProvisionedConcurrencyConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import GetProvisionedConcurrencyConfigResponseTypeDef
```




Optional fields:
- `RequestedProvisionedConcurrentExecutions`: `int`
- `AvailableProvisionedConcurrentExecutions`: `int`
- `AllocatedProvisionedConcurrentExecutions`: `int`
- `Status`: `ProvisionedConcurrencyStatusEnum`
- `StatusReason`: `str`
- `LastModified`: `str`


## ImageConfigErrorTypeDef

```python
from mypy_boto3_lambda.type_defs import ImageConfigErrorTypeDef
```




Optional fields:
- `ErrorCode`: `str`
- `Message`: `str`


## ImageConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ImageConfigResponseTypeDef
```




Optional fields:
- `ImageConfig`: `"ImageConfigTypeDef"`
- `Error`: `"ImageConfigErrorTypeDef"`


## ImageConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import ImageConfigTypeDef
```




Optional fields:
- `EntryPoint`: `List[str]`
- `Command`: `List[str]`
- `WorkingDirectory`: `str`


## InvocationResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import InvocationResponseTypeDef
```




Optional fields:
- `StatusCode`: `int`
- `FunctionError`: `str`
- `LogResult`: `str`
- `Payload`: `IO[bytes]`
- `ExecutedVersion`: `str`


## InvokeAsyncResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import InvokeAsyncResponseTypeDef
```




Optional fields:
- `Status`: `int`


## LayerTypeDef

```python
from mypy_boto3_lambda.type_defs import LayerTypeDef
```




Optional fields:
- `Arn`: `str`
- `CodeSize`: `int`
- `SigningProfileVersionArn`: `str`
- `SigningJobArn`: `str`


## LayerVersionContentInputTypeDef

```python
from mypy_boto3_lambda.type_defs import LayerVersionContentInputTypeDef
```




Optional fields:
- `S3Bucket`: `str`
- `S3Key`: `str`
- `S3ObjectVersion`: `str`
- `ZipFile`: `Union[bytes, IO[bytes]]`


## LayerVersionContentOutputTypeDef

```python
from mypy_boto3_lambda.type_defs import LayerVersionContentOutputTypeDef
```




Optional fields:
- `Location`: `str`
- `CodeSha256`: `str`
- `CodeSize`: `int`
- `SigningProfileVersionArn`: `str`
- `SigningJobArn`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## LayerVersionsListItemTypeDef

```python
from mypy_boto3_lambda.type_defs import LayerVersionsListItemTypeDef
```




Optional fields:
- `LayerVersionArn`: `str`
- `Version`: `int`
- `Description`: `str`
- `CreatedDate`: `str`
- `CompatibleRuntimes`: `List[Runtime]`
- `LicenseInfo`: `str`


## LayersListItemTypeDef

```python
from mypy_boto3_lambda.type_defs import LayersListItemTypeDef
```




Optional fields:
- `LayerName`: `str`
- `LayerArn`: `str`
- `LatestMatchingVersion`: `"LayerVersionsListItemTypeDef"`


## ListAliasesResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListAliasesResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `Aliases`: `List["AliasConfigurationTypeDef"]`


## ListCodeSigningConfigsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListCodeSigningConfigsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `CodeSigningConfigs`: `List["CodeSigningConfigTypeDef"]`


## ListEventSourceMappingsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListEventSourceMappingsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `EventSourceMappings`: `List["EventSourceMappingConfigurationTypeDef"]`


## ListFunctionEventInvokeConfigsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListFunctionEventInvokeConfigsResponseTypeDef
```




Optional fields:
- `FunctionEventInvokeConfigs`: `List["FunctionEventInvokeConfigTypeDef"]`
- `NextMarker`: `str`


## ListFunctionsByCodeSigningConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListFunctionsByCodeSigningConfigResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `FunctionArns`: `List[str]`


## ListFunctionsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListFunctionsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `Functions`: `List["FunctionConfigurationTypeDef"]`


## ListLayerVersionsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListLayerVersionsResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `LayerVersions`: `List["LayerVersionsListItemTypeDef"]`


## ListLayersResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListLayersResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `Layers`: `List["LayersListItemTypeDef"]`


## ListProvisionedConcurrencyConfigsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListProvisionedConcurrencyConfigsResponseTypeDef
```




Optional fields:
- `ProvisionedConcurrencyConfigs`: `List["ProvisionedConcurrencyConfigListItemTypeDef"]`
- `NextMarker`: `str`


## ListTagsResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListTagsResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`


## ListVersionsByFunctionResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import ListVersionsByFunctionResponseTypeDef
```




Optional fields:
- `NextMarker`: `str`
- `Versions`: `List["FunctionConfigurationTypeDef"]`


## OnFailureTypeDef

```python
from mypy_boto3_lambda.type_defs import OnFailureTypeDef
```




Optional fields:
- `Destination`: `str`


## OnSuccessTypeDef

```python
from mypy_boto3_lambda.type_defs import OnSuccessTypeDef
```




Optional fields:
- `Destination`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProvisionedConcurrencyConfigListItemTypeDef

```python
from mypy_boto3_lambda.type_defs import ProvisionedConcurrencyConfigListItemTypeDef
```




Optional fields:
- `FunctionArn`: `str`
- `RequestedProvisionedConcurrentExecutions`: `int`
- `AvailableProvisionedConcurrentExecutions`: `int`
- `AllocatedProvisionedConcurrentExecutions`: `int`
- `Status`: `ProvisionedConcurrencyStatusEnum`
- `StatusReason`: `str`
- `LastModified`: `str`


## PublishLayerVersionResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import PublishLayerVersionResponseTypeDef
```




Optional fields:
- `Content`: `"LayerVersionContentOutputTypeDef"`
- `LayerArn`: `str`
- `LayerVersionArn`: `str`
- `Description`: `str`
- `CreatedDate`: `str`
- `Version`: `int`
- `CompatibleRuntimes`: `List[Runtime]`
- `LicenseInfo`: `str`


## PutFunctionCodeSigningConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import PutFunctionCodeSigningConfigResponseTypeDef
```


Required fields:
- `CodeSigningConfigArn`: `str`
- `FunctionName`: `str`




## PutProvisionedConcurrencyConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import PutProvisionedConcurrencyConfigResponseTypeDef
```




Optional fields:
- `RequestedProvisionedConcurrentExecutions`: `int`
- `AvailableProvisionedConcurrentExecutions`: `int`
- `AllocatedProvisionedConcurrentExecutions`: `int`
- `Status`: `ProvisionedConcurrencyStatusEnum`
- `StatusReason`: `str`
- `LastModified`: `str`


## ResponseMetadata

```python
from mypy_boto3_lambda.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## SelfManagedEventSourceTypeDef

```python
from mypy_boto3_lambda.type_defs import SelfManagedEventSourceTypeDef
```




Optional fields:
- `Endpoints`: `Dict[Literal['KAFKA_BOOTSTRAP_SERVERS'], List[str]]`


## SourceAccessConfigurationTypeDef

```python
from mypy_boto3_lambda.type_defs import SourceAccessConfigurationTypeDef
```




Optional fields:
- `Type`: `SourceAccessType`
- `URI`: `str`


## TracingConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import TracingConfigResponseTypeDef
```




Optional fields:
- `Mode`: `TracingMode`


## TracingConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import TracingConfigTypeDef
```




Optional fields:
- `Mode`: `TracingMode`


## UpdateCodeSigningConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import UpdateCodeSigningConfigResponseTypeDef
```


Required fields:
- `CodeSigningConfig`: `"CodeSigningConfigTypeDef"`




## VpcConfigResponseTypeDef

```python
from mypy_boto3_lambda.type_defs import VpcConfigResponseTypeDef
```




Optional fields:
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`
- `VpcId`: `str`


## VpcConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import VpcConfigTypeDef
```




Optional fields:
- `SubnetIds`: `List[str]`
- `SecurityGroupIds`: `List[str]`


## WaiterConfigTypeDef

```python
from mypy_boto3_lambda.type_defs import WaiterConfigTypeDef
```




Optional fields:
- `Delay`: `int`
- `MaxAttempts`: `int`

