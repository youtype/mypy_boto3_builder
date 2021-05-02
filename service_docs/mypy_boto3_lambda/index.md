# Type annotations for boto3 Lambda module

> [Index](../index.md) > Lambda

Auto-generated documentation for [Lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda)
type annotations stubs module [mypy_boto3_lambda](https://pypi.org/project/mypy-boto3-lambda/).

```bash
pip install mypy-boto3-lambda
```

- [Type annotations for boto3 Lambda module](#type-annotations-for-boto3-lambda-module)
  - [LambdaClient](#lambdaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## LambdaClient

Type annotations for  `boto3.client("lambda")` as [LambdaClient](./client.md)

Can be used directly:

```python
from mypy_boto3_lambda.client import LambdaClient
```


LambdaClient [exceptions](./client.md#exceptions)



### Methods
- [add_layer_version_permission](./client.md#add-layer-version-permission)
- [add_permission](./client.md#add-permission)
- [can_paginate](./client.md#can-paginate)
- [create_alias](./client.md#create-alias)
- [create_code_signing_config](./client.md#create-code-signing-config)
- [create_event_source_mapping](./client.md#create-event-source-mapping)
- [create_function](./client.md#create-function)
- [delete_alias](./client.md#delete-alias)
- [delete_code_signing_config](./client.md#delete-code-signing-config)
- [delete_event_source_mapping](./client.md#delete-event-source-mapping)
- [delete_function](./client.md#delete-function)
- [delete_function_code_signing_config](./client.md#delete-function-code-signing-config)
- [delete_function_concurrency](./client.md#delete-function-concurrency)
- [delete_function_event_invoke_config](./client.md#delete-function-event-invoke-config)
- [delete_layer_version](./client.md#delete-layer-version)
- [delete_provisioned_concurrency_config](./client.md#delete-provisioned-concurrency-config)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_account_settings](./client.md#get-account-settings)
- [get_alias](./client.md#get-alias)
- [get_code_signing_config](./client.md#get-code-signing-config)
- [get_event_source_mapping](./client.md#get-event-source-mapping)
- [get_function](./client.md#get-function)
- [get_function_code_signing_config](./client.md#get-function-code-signing-config)
- [get_function_concurrency](./client.md#get-function-concurrency)
- [get_function_configuration](./client.md#get-function-configuration)
- [get_function_event_invoke_config](./client.md#get-function-event-invoke-config)
- [get_layer_version](./client.md#get-layer-version)
- [get_layer_version_by_arn](./client.md#get-layer-version-by-arn)
- [get_layer_version_policy](./client.md#get-layer-version-policy)
- [get_paginator](./client.md#get-paginator)
- [get_policy](./client.md#get-policy)
- [get_provisioned_concurrency_config](./client.md#get-provisioned-concurrency-config)
- [get_waiter](./client.md#get-waiter)
- [invoke](./client.md#invoke)
- [invoke_async](./client.md#invoke-async)
- [list_aliases](./client.md#list-aliases)
- [list_code_signing_configs](./client.md#list-code-signing-configs)
- [list_event_source_mappings](./client.md#list-event-source-mappings)
- [list_function_event_invoke_configs](./client.md#list-function-event-invoke-configs)
- [list_functions](./client.md#list-functions)
- [list_functions_by_code_signing_config](./client.md#list-functions-by-code-signing-config)
- [list_layer_versions](./client.md#list-layer-versions)
- [list_layers](./client.md#list-layers)
- [list_provisioned_concurrency_configs](./client.md#list-provisioned-concurrency-configs)
- [list_tags](./client.md#list-tags)
- [list_versions_by_function](./client.md#list-versions-by-function)
- [publish_layer_version](./client.md#publish-layer-version)
- [publish_version](./client.md#publish-version)
- [put_function_code_signing_config](./client.md#put-function-code-signing-config)
- [put_function_concurrency](./client.md#put-function-concurrency)
- [put_function_event_invoke_config](./client.md#put-function-event-invoke-config)
- [put_provisioned_concurrency_config](./client.md#put-provisioned-concurrency-config)
- [remove_layer_version_permission](./client.md#remove-layer-version-permission)
- [remove_permission](./client.md#remove-permission)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_alias](./client.md#update-alias)
- [update_code_signing_config](./client.md#update-code-signing-config)
- [update_event_source_mapping](./client.md#update-event-source-mapping)
- [update_function_code](./client.md#update-function-code)
- [update_function_configuration](./client.md#update-function-configuration)
- [update_function_event_invoke_config](./client.md#update-function-event-invoke-config)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CodeSigningConfigNotFoundException](./client.md#codesigningconfignotfoundexception)
- [CodeStorageExceededException](./client.md#codestorageexceededexception)
- [CodeVerificationFailedException](./client.md#codeverificationfailedexception)
- [EC2AccessDeniedException](./client.md#ec2accessdeniedexception)
- [EC2ThrottledException](./client.md#ec2throttledexception)
- [EC2UnexpectedException](./client.md#ec2unexpectedexception)
- [EFSIOException](./client.md#efsioexception)
- [EFSMountConnectivityException](./client.md#efsmountconnectivityexception)
- [EFSMountFailureException](./client.md#efsmountfailureexception)
- [EFSMountTimeoutException](./client.md#efsmounttimeoutexception)
- [ENILimitReachedException](./client.md#enilimitreachedexception)
- [InvalidCodeSignatureException](./client.md#invalidcodesignatureexception)
- [InvalidParameterValueException](./client.md#invalidparametervalueexception)
- [InvalidRequestContentException](./client.md#invalidrequestcontentexception)
- [InvalidRuntimeException](./client.md#invalidruntimeexception)
- [InvalidSecurityGroupIDException](./client.md#invalidsecuritygroupidexception)
- [InvalidSubnetIDException](./client.md#invalidsubnetidexception)
- [InvalidZipFileException](./client.md#invalidzipfileexception)
- [KMSAccessDeniedException](./client.md#kmsaccessdeniedexception)
- [KMSDisabledException](./client.md#kmsdisabledexception)
- [KMSInvalidStateException](./client.md#kmsinvalidstateexception)
- [KMSNotFoundException](./client.md#kmsnotfoundexception)
- [PolicyLengthExceededException](./client.md#policylengthexceededexception)
- [PreconditionFailedException](./client.md#preconditionfailedexception)
- [ProvisionedConcurrencyConfigNotFoundException](./client.md#provisionedconcurrencyconfignotfoundexception)
- [RequestTooLargeException](./client.md#requesttoolargeexception)
- [ResourceConflictException](./client.md#resourceconflictexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceNotReadyException](./client.md#resourcenotreadyexception)
- [ServiceException](./client.md#serviceexception)
- [SubnetIPAddressLimitReachedException](./client.md#subnetipaddresslimitreachedexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnsupportedMediaTypeException](./client.md#unsupportedmediatypeexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("lambda").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_lambda.paginators import ListAliasesPaginator, ...
```

- [ListAliasesPaginator](./paginators.md#listaliasespaginator)
- [ListCodeSigningConfigsPaginator](./paginators.md#listcodesigningconfigspaginator)
- [ListEventSourceMappingsPaginator](./paginators.md#listeventsourcemappingspaginator)
- [ListFunctionEventInvokeConfigsPaginator](./paginators.md#listfunctioneventinvokeconfigspaginator)
- [ListFunctionsPaginator](./paginators.md#listfunctionspaginator)
- [ListFunctionsByCodeSigningConfigPaginator](./paginators.md#listfunctionsbycodesigningconfigpaginator)
- [ListLayerVersionsPaginator](./paginators.md#listlayerversionspaginator)
- [ListLayersPaginator](./paginators.md#listlayerspaginator)
- [ListProvisionedConcurrencyConfigsPaginator](./paginators.md#listprovisionedconcurrencyconfigspaginator)
- [ListVersionsByFunctionPaginator](./paginators.md#listversionsbyfunctionpaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("lambda").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_lambda.waiters import FunctionActiveWaiter, ...
```

- [FunctionActiveWaiter](./waiters.md#functionactivewaiter)
- [FunctionExistsWaiter](./waiters.md#functionexistswaiter)
- [FunctionUpdatedWaiter](./waiters.md#functionupdatedwaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lambda.literals import CodeSigningPolicy, ...
```

- [CodeSigningPolicy](./literals.md#codesigningpolicy)
- [EndPointType](./literals.md#endpointtype)
- [EventSourcePosition](./literals.md#eventsourceposition)
- [FunctionActiveWaiterName](./literals.md#functionactivewaitername)
- [FunctionExistsWaiterName](./literals.md#functionexistswaitername)
- [FunctionResponseType](./literals.md#functionresponsetype)
- [FunctionUpdatedWaiterName](./literals.md#functionupdatedwaitername)
- [FunctionVersion](./literals.md#functionversion)
- [InvocationType](./literals.md#invocationtype)
- [LastUpdateStatus](./literals.md#lastupdatestatus)
- [LastUpdateStatusReasonCode](./literals.md#lastupdatestatusreasoncode)
- [ListAliasesPaginatorName](./literals.md#listaliasespaginatorname)
- [ListCodeSigningConfigsPaginatorName](./literals.md#listcodesigningconfigspaginatorname)
- [ListEventSourceMappingsPaginatorName](./literals.md#listeventsourcemappingspaginatorname)
- [ListFunctionEventInvokeConfigsPaginatorName](./literals.md#listfunctioneventinvokeconfigspaginatorname)
- [ListFunctionsByCodeSigningConfigPaginatorName](./literals.md#listfunctionsbycodesigningconfigpaginatorname)
- [ListFunctionsPaginatorName](./literals.md#listfunctionspaginatorname)
- [ListLayerVersionsPaginatorName](./literals.md#listlayerversionspaginatorname)
- [ListLayersPaginatorName](./literals.md#listlayerspaginatorname)
- [ListProvisionedConcurrencyConfigsPaginatorName](./literals.md#listprovisionedconcurrencyconfigspaginatorname)
- [ListVersionsByFunctionPaginatorName](./literals.md#listversionsbyfunctionpaginatorname)
- [LogType](./literals.md#logtype)
- [PackageType](./literals.md#packagetype)
- [ProvisionedConcurrencyStatusEnum](./literals.md#provisionedconcurrencystatusenum)
- [Runtime](./literals.md#runtime)
- [SourceAccessType](./literals.md#sourceaccesstype)
- [State](./literals.md#state)
- [StateReasonCode](./literals.md#statereasoncode)
- [TracingMode](./literals.md#tracingmode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_lambda.type_defs import AccountLimitTypeDef, ...
```

- [AccountLimitTypeDef](./type_defs.md#accountlimittypedef)
- [AccountUsageTypeDef](./type_defs.md#accountusagetypedef)
- [AddLayerVersionPermissionResponseTypeDef](./type_defs.md#addlayerversionpermissionresponsetypedef)
- [AddPermissionResponseTypeDef](./type_defs.md#addpermissionresponsetypedef)
- [AliasConfigurationTypeDef](./type_defs.md#aliasconfigurationtypedef)
- [AliasRoutingConfigurationTypeDef](./type_defs.md#aliasroutingconfigurationtypedef)
- [AllowedPublishersTypeDef](./type_defs.md#allowedpublisherstypedef)
- [CodeSigningConfigTypeDef](./type_defs.md#codesigningconfigtypedef)
- [CodeSigningPoliciesTypeDef](./type_defs.md#codesigningpoliciestypedef)
- [ConcurrencyTypeDef](./type_defs.md#concurrencytypedef)
- [CreateCodeSigningConfigResponseTypeDef](./type_defs.md#createcodesigningconfigresponsetypedef)
- [DeadLetterConfigTypeDef](./type_defs.md#deadletterconfigtypedef)
- [DestinationConfigTypeDef](./type_defs.md#destinationconfigtypedef)
- [EnvironmentErrorTypeDef](./type_defs.md#environmenterrortypedef)
- [EnvironmentResponseTypeDef](./type_defs.md#environmentresponsetypedef)
- [EnvironmentTypeDef](./type_defs.md#environmenttypedef)
- [EventSourceMappingConfigurationTypeDef](./type_defs.md#eventsourcemappingconfigurationtypedef)
- [FileSystemConfigTypeDef](./type_defs.md#filesystemconfigtypedef)
- [FunctionCodeLocationTypeDef](./type_defs.md#functioncodelocationtypedef)
- [FunctionCodeTypeDef](./type_defs.md#functioncodetypedef)
- [FunctionConfigurationTypeDef](./type_defs.md#functionconfigurationtypedef)
- [FunctionEventInvokeConfigTypeDef](./type_defs.md#functioneventinvokeconfigtypedef)
- [GetAccountSettingsResponseTypeDef](./type_defs.md#getaccountsettingsresponsetypedef)
- [GetCodeSigningConfigResponseTypeDef](./type_defs.md#getcodesigningconfigresponsetypedef)
- [GetFunctionCodeSigningConfigResponseTypeDef](./type_defs.md#getfunctioncodesigningconfigresponsetypedef)
- [GetFunctionConcurrencyResponseTypeDef](./type_defs.md#getfunctionconcurrencyresponsetypedef)
- [GetFunctionResponseTypeDef](./type_defs.md#getfunctionresponsetypedef)
- [GetLayerVersionPolicyResponseTypeDef](./type_defs.md#getlayerversionpolicyresponsetypedef)
- [GetLayerVersionResponseTypeDef](./type_defs.md#getlayerversionresponsetypedef)
- [GetPolicyResponseTypeDef](./type_defs.md#getpolicyresponsetypedef)
- [GetProvisionedConcurrencyConfigResponseTypeDef](./type_defs.md#getprovisionedconcurrencyconfigresponsetypedef)
- [ImageConfigErrorTypeDef](./type_defs.md#imageconfigerrortypedef)
- [ImageConfigResponseTypeDef](./type_defs.md#imageconfigresponsetypedef)
- [ImageConfigTypeDef](./type_defs.md#imageconfigtypedef)
- [InvocationResponseTypeDef](./type_defs.md#invocationresponsetypedef)
- [InvokeAsyncResponseTypeDef](./type_defs.md#invokeasyncresponsetypedef)
- [LayerTypeDef](./type_defs.md#layertypedef)
- [LayerVersionContentInputTypeDef](./type_defs.md#layerversioncontentinputtypedef)
- [LayerVersionContentOutputTypeDef](./type_defs.md#layerversioncontentoutputtypedef)
- [LayerVersionsListItemTypeDef](./type_defs.md#layerversionslistitemtypedef)
- [LayersListItemTypeDef](./type_defs.md#layerslistitemtypedef)
- [ListAliasesResponseTypeDef](./type_defs.md#listaliasesresponsetypedef)
- [ListCodeSigningConfigsResponseTypeDef](./type_defs.md#listcodesigningconfigsresponsetypedef)
- [ListEventSourceMappingsResponseTypeDef](./type_defs.md#listeventsourcemappingsresponsetypedef)
- [ListFunctionEventInvokeConfigsResponseTypeDef](./type_defs.md#listfunctioneventinvokeconfigsresponsetypedef)
- [ListFunctionsByCodeSigningConfigResponseTypeDef](./type_defs.md#listfunctionsbycodesigningconfigresponsetypedef)
- [ListFunctionsResponseTypeDef](./type_defs.md#listfunctionsresponsetypedef)
- [ListLayerVersionsResponseTypeDef](./type_defs.md#listlayerversionsresponsetypedef)
- [ListLayersResponseTypeDef](./type_defs.md#listlayersresponsetypedef)
- [ListProvisionedConcurrencyConfigsResponseTypeDef](./type_defs.md#listprovisionedconcurrencyconfigsresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [ListVersionsByFunctionResponseTypeDef](./type_defs.md#listversionsbyfunctionresponsetypedef)
- [OnFailureTypeDef](./type_defs.md#onfailuretypedef)
- [OnSuccessTypeDef](./type_defs.md#onsuccesstypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ProvisionedConcurrencyConfigListItemTypeDef](./type_defs.md#provisionedconcurrencyconfiglistitemtypedef)
- [PublishLayerVersionResponseTypeDef](./type_defs.md#publishlayerversionresponsetypedef)
- [PutFunctionCodeSigningConfigResponseTypeDef](./type_defs.md#putfunctioncodesigningconfigresponsetypedef)
- [PutProvisionedConcurrencyConfigResponseTypeDef](./type_defs.md#putprovisionedconcurrencyconfigresponsetypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SelfManagedEventSourceTypeDef](./type_defs.md#selfmanagedeventsourcetypedef)
- [SourceAccessConfigurationTypeDef](./type_defs.md#sourceaccessconfigurationtypedef)
- [TracingConfigResponseTypeDef](./type_defs.md#tracingconfigresponsetypedef)
- [TracingConfigTypeDef](./type_defs.md#tracingconfigtypedef)
- [UpdateCodeSigningConfigResponseTypeDef](./type_defs.md#updatecodesigningconfigresponsetypedef)
- [VpcConfigResponseTypeDef](./type_defs.md#vpcconfigresponsetypedef)
- [VpcConfigTypeDef](./type_defs.md#vpcconfigtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
