# Literals for boto3 Lambda module

> [Index](../index.md) > [Lambda](./index.md) > Literals

Auto-generated documentation for [Lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda)
type annotations stubs module [mypy_boto3_lambda](https://pypi.org/project/mypy-boto3-lambda/).

- [Literals for boto3 Lambda module](#literals-for-boto3-lambda-module)
  - [CodeSigningPolicy](#codesigningpolicy)
  - [EndPointType](#endpointtype)
  - [EventSourcePosition](#eventsourceposition)
  - [FunctionActiveWaiterName](#functionactivewaitername)
  - [FunctionExistsWaiterName](#functionexistswaitername)
  - [FunctionResponseType](#functionresponsetype)
  - [FunctionUpdatedWaiterName](#functionupdatedwaitername)
  - [FunctionVersion](#functionversion)
  - [InvocationType](#invocationtype)
  - [LastUpdateStatus](#lastupdatestatus)
  - [LastUpdateStatusReasonCode](#lastupdatestatusreasoncode)
  - [ListAliasesPaginatorName](#listaliasespaginatorname)
  - [ListCodeSigningConfigsPaginatorName](#listcodesigningconfigspaginatorname)
  - [ListEventSourceMappingsPaginatorName](#listeventsourcemappingspaginatorname)
  - [ListFunctionEventInvokeConfigsPaginatorName](#listfunctioneventinvokeconfigspaginatorname)
  - [ListFunctionsByCodeSigningConfigPaginatorName](#listfunctionsbycodesigningconfigpaginatorname)
  - [ListFunctionsPaginatorName](#listfunctionspaginatorname)
  - [ListLayerVersionsPaginatorName](#listlayerversionspaginatorname)
  - [ListLayersPaginatorName](#listlayerspaginatorname)
  - [ListProvisionedConcurrencyConfigsPaginatorName](#listprovisionedconcurrencyconfigspaginatorname)
  - [ListVersionsByFunctionPaginatorName](#listversionsbyfunctionpaginatorname)
  - [LogType](#logtype)
  - [PackageType](#packagetype)
  - [ProvisionedConcurrencyStatusEnum](#provisionedconcurrencystatusenum)
  - [Runtime](#runtime)
  - [SourceAccessType](#sourceaccesstype)
  - [State](#state)
  - [StateReasonCode](#statereasoncode)
  - [TracingMode](#tracingmode)

## CodeSigningPolicy

```python
from mypy_boto3_lambda.literals import CodeSigningPolicy
```

Values:

- `Enforce`
- `Warn`

## EndPointType

```python
from mypy_boto3_lambda.literals import EndPointType
```

Values:

- `KAFKA_BOOTSTRAP_SERVERS`

## EventSourcePosition

```python
from mypy_boto3_lambda.literals import EventSourcePosition
```

Values:

- `AT_TIMESTAMP`
- `LATEST`
- `TRIM_HORIZON`

## FunctionActiveWaiterName

```python
from mypy_boto3_lambda.literals import FunctionActiveWaiterName
```

Values:

- `function_active`

## FunctionExistsWaiterName

```python
from mypy_boto3_lambda.literals import FunctionExistsWaiterName
```

Values:

- `function_exists`

## FunctionResponseType

```python
from mypy_boto3_lambda.literals import FunctionResponseType
```

Values:

- `ReportBatchItemFailures`

## FunctionUpdatedWaiterName

```python
from mypy_boto3_lambda.literals import FunctionUpdatedWaiterName
```

Values:

- `function_updated`

## FunctionVersion

```python
from mypy_boto3_lambda.literals import FunctionVersion
```

Values:

- `ALL`

## InvocationType

```python
from mypy_boto3_lambda.literals import InvocationType
```

Values:

- `DryRun`
- `Event`
- `RequestResponse`

## LastUpdateStatus

```python
from mypy_boto3_lambda.literals import LastUpdateStatus
```

Values:

- `Failed`
- `InProgress`
- `Successful`

## LastUpdateStatusReasonCode

```python
from mypy_boto3_lambda.literals import LastUpdateStatusReasonCode
```

Values:

- `EniLimitExceeded`
- `ImageAccessDenied`
- `ImageDeleted`
- `InsufficientRolePermissions`
- `InternalError`
- `InvalidConfiguration`
- `InvalidImage`
- `InvalidSecurityGroup`
- `InvalidSubnet`
- `SubnetOutOfIPAddresses`

## ListAliasesPaginatorName

```python
from mypy_boto3_lambda.literals import ListAliasesPaginatorName
```

Values:

- `list_aliases`

## ListCodeSigningConfigsPaginatorName

```python
from mypy_boto3_lambda.literals import ListCodeSigningConfigsPaginatorName
```

Values:

- `list_code_signing_configs`

## ListEventSourceMappingsPaginatorName

```python
from mypy_boto3_lambda.literals import ListEventSourceMappingsPaginatorName
```

Values:

- `list_event_source_mappings`

## ListFunctionEventInvokeConfigsPaginatorName

```python
from mypy_boto3_lambda.literals import ListFunctionEventInvokeConfigsPaginatorName
```

Values:

- `list_function_event_invoke_configs`

## ListFunctionsByCodeSigningConfigPaginatorName

```python
from mypy_boto3_lambda.literals import ListFunctionsByCodeSigningConfigPaginatorName
```

Values:

- `list_functions_by_code_signing_config`

## ListFunctionsPaginatorName

```python
from mypy_boto3_lambda.literals import ListFunctionsPaginatorName
```

Values:

- `list_functions`

## ListLayerVersionsPaginatorName

```python
from mypy_boto3_lambda.literals import ListLayerVersionsPaginatorName
```

Values:

- `list_layer_versions`

## ListLayersPaginatorName

```python
from mypy_boto3_lambda.literals import ListLayersPaginatorName
```

Values:

- `list_layers`

## ListProvisionedConcurrencyConfigsPaginatorName

```python
from mypy_boto3_lambda.literals import ListProvisionedConcurrencyConfigsPaginatorName
```

Values:

- `list_provisioned_concurrency_configs`

## ListVersionsByFunctionPaginatorName

```python
from mypy_boto3_lambda.literals import ListVersionsByFunctionPaginatorName
```

Values:

- `list_versions_by_function`

## LogType

```python
from mypy_boto3_lambda.literals import LogType
```

Values:

- `None`
- `Tail`

## PackageType

```python
from mypy_boto3_lambda.literals import PackageType
```

Values:

- `Image`
- `Zip`

## ProvisionedConcurrencyStatusEnum

```python
from mypy_boto3_lambda.literals import ProvisionedConcurrencyStatusEnum
```

Values:

- `FAILED`
- `IN_PROGRESS`
- `READY`

## Runtime

```python
from mypy_boto3_lambda.literals import Runtime
```

Values:

- `dotnetcore1.0`
- `dotnetcore2.0`
- `dotnetcore2.1`
- `dotnetcore3.1`
- `go1.x`
- `java11`
- `java8`
- `java8.al2`
- `nodejs`
- `nodejs10.x`
- `nodejs12.x`
- `nodejs14.x`
- `nodejs4.3`
- `nodejs4.3-edge`
- `nodejs6.10`
- `nodejs8.10`
- `provided`
- `provided.al2`
- `python2.7`
- `python3.6`
- `python3.7`
- `python3.8`
- `ruby2.5`
- `ruby2.7`

## SourceAccessType

```python
from mypy_boto3_lambda.literals import SourceAccessType
```

Values:

- `BASIC_AUTH`
- `SASL_SCRAM_256_AUTH`
- `SASL_SCRAM_512_AUTH`
- `VPC_SECURITY_GROUP`
- `VPC_SUBNET`

## State

```python
from mypy_boto3_lambda.literals import State
```

Values:

- `Active`
- `Failed`
- `Inactive`
- `Pending`

## StateReasonCode

```python
from mypy_boto3_lambda.literals import StateReasonCode
```

Values:

- `Creating`
- `EniLimitExceeded`
- `Idle`
- `ImageAccessDenied`
- `ImageDeleted`
- `InsufficientRolePermissions`
- `InternalError`
- `InvalidConfiguration`
- `InvalidImage`
- `InvalidSecurityGroup`
- `InvalidSubnet`
- `Restoring`
- `SubnetOutOfIPAddresses`

## TracingMode

```python
from mypy_boto3_lambda.literals import TracingMode
```

Values:

- `Active`
- `PassThrough`
