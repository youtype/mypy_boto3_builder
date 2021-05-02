# Type annotations for boto3 GreengrassV2 module

> [Index](../index.md) > GreengrassV2

Auto-generated documentation for [GreengrassV2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html#GreengrassV2)
type annotations stubs module [mypy_boto3_greengrassv2](https://pypi.org/project/mypy-boto3-greengrassv2/).

```bash
pip install mypy-boto3-greengrassv2
```

- [Type annotations for boto3 GreengrassV2 module](#type-annotations-for-boto3-greengrassv2-module)
  - [GreengrassV2Client](#greengrassv2client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## GreengrassV2Client

Type annotations for  `boto3.client("greengrassv2")` as [GreengrassV2Client](./client.md)

Can be used directly:

```python
from mypy_boto3_greengrassv2.client import GreengrassV2Client
```


GreengrassV2Client [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_deployment](./client.md#cancel-deployment)
- [create_component_version](./client.md#create-component-version)
- [create_deployment](./client.md#create-deployment)
- [delete_component](./client.md#delete-component)
- [delete_core_device](./client.md#delete-core-device)
- [describe_component](./client.md#describe-component)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_component](./client.md#get-component)
- [get_component_version_artifact](./client.md#get-component-version-artifact)
- [get_core_device](./client.md#get-core-device)
- [get_deployment](./client.md#get-deployment)
- [get_paginator](./client.md#get-paginator)
- [list_component_versions](./client.md#list-component-versions)
- [list_components](./client.md#list-components)
- [list_core_devices](./client.md#list-core-devices)
- [list_deployments](./client.md#list-deployments)
- [list_effective_deployments](./client.md#list-effective-deployments)
- [list_installed_components](./client.md#list-installed-components)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [resolve_component_candidates](./client.md#resolve-component-candidates)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("greengrassv2").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_greengrassv2.paginators import ListComponentVersionsPaginator, ...
```

- [ListComponentVersionsPaginator](./paginators.md#listcomponentversionspaginator)
- [ListComponentsPaginator](./paginators.md#listcomponentspaginator)
- [ListCoreDevicesPaginator](./paginators.md#listcoredevicespaginator)
- [ListDeploymentsPaginator](./paginators.md#listdeploymentspaginator)
- [ListEffectiveDeploymentsPaginator](./paginators.md#listeffectivedeploymentspaginator)
- [ListInstalledComponentsPaginator](./paginators.md#listinstalledcomponentspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_greengrassv2.literals import CloudComponentState, ...
```

- [CloudComponentState](./literals.md#cloudcomponentstate)
- [ComponentDependencyType](./literals.md#componentdependencytype)
- [ComponentVisibilityScope](./literals.md#componentvisibilityscope)
- [CoreDeviceStatus](./literals.md#coredevicestatus)
- [DeploymentComponentUpdatePolicyAction](./literals.md#deploymentcomponentupdatepolicyaction)
- [DeploymentFailureHandlingPolicy](./literals.md#deploymentfailurehandlingpolicy)
- [DeploymentHistoryFilter](./literals.md#deploymenthistoryfilter)
- [DeploymentStatus](./literals.md#deploymentstatus)
- [EffectiveDeploymentExecutionStatus](./literals.md#effectivedeploymentexecutionstatus)
- [InstalledComponentLifecycleState](./literals.md#installedcomponentlifecyclestate)
- [IoTJobAbortAction](./literals.md#iotjobabortaction)
- [IoTJobExecutionFailureType](./literals.md#iotjobexecutionfailuretype)
- [LambdaEventSourceType](./literals.md#lambdaeventsourcetype)
- [LambdaFilesystemPermission](./literals.md#lambdafilesystempermission)
- [LambdaInputPayloadEncodingType](./literals.md#lambdainputpayloadencodingtype)
- [LambdaIsolationMode](./literals.md#lambdaisolationmode)
- [ListComponentVersionsPaginatorName](./literals.md#listcomponentversionspaginatorname)
- [ListComponentsPaginatorName](./literals.md#listcomponentspaginatorname)
- [ListCoreDevicesPaginatorName](./literals.md#listcoredevicespaginatorname)
- [ListDeploymentsPaginatorName](./literals.md#listdeploymentspaginatorname)
- [ListEffectiveDeploymentsPaginatorName](./literals.md#listeffectivedeploymentspaginatorname)
- [ListInstalledComponentsPaginatorName](./literals.md#listinstalledcomponentspaginatorname)
- [RecipeOutputFormat](./literals.md#recipeoutputformat)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_greengrassv2.type_defs import CancelDeploymentResponseTypeDef, ...
```

- [CancelDeploymentResponseTypeDef](./type_defs.md#canceldeploymentresponsetypedef)
- [CloudComponentStatusTypeDef](./type_defs.md#cloudcomponentstatustypedef)
- [ComponentCandidateTypeDef](./type_defs.md#componentcandidatetypedef)
- [ComponentConfigurationUpdateTypeDef](./type_defs.md#componentconfigurationupdatetypedef)
- [ComponentDependencyRequirementTypeDef](./type_defs.md#componentdependencyrequirementtypedef)
- [ComponentDeploymentSpecificationTypeDef](./type_defs.md#componentdeploymentspecificationtypedef)
- [ComponentLatestVersionTypeDef](./type_defs.md#componentlatestversiontypedef)
- [ComponentPlatformTypeDef](./type_defs.md#componentplatformtypedef)
- [ComponentRunWithTypeDef](./type_defs.md#componentrunwithtypedef)
- [ComponentTypeDef](./type_defs.md#componenttypedef)
- [ComponentVersionListItemTypeDef](./type_defs.md#componentversionlistitemtypedef)
- [CoreDeviceTypeDef](./type_defs.md#coredevicetypedef)
- [CreateComponentVersionResponseTypeDef](./type_defs.md#createcomponentversionresponsetypedef)
- [CreateDeploymentResponseTypeDef](./type_defs.md#createdeploymentresponsetypedef)
- [DeploymentComponentUpdatePolicyTypeDef](./type_defs.md#deploymentcomponentupdatepolicytypedef)
- [DeploymentConfigurationValidationPolicyTypeDef](./type_defs.md#deploymentconfigurationvalidationpolicytypedef)
- [DeploymentIoTJobConfigurationTypeDef](./type_defs.md#deploymentiotjobconfigurationtypedef)
- [DeploymentPoliciesTypeDef](./type_defs.md#deploymentpoliciestypedef)
- [DeploymentTypeDef](./type_defs.md#deploymenttypedef)
- [DescribeComponentResponseTypeDef](./type_defs.md#describecomponentresponsetypedef)
- [EffectiveDeploymentTypeDef](./type_defs.md#effectivedeploymenttypedef)
- [GetComponentResponseTypeDef](./type_defs.md#getcomponentresponsetypedef)
- [GetComponentVersionArtifactResponseTypeDef](./type_defs.md#getcomponentversionartifactresponsetypedef)
- [GetCoreDeviceResponseTypeDef](./type_defs.md#getcoredeviceresponsetypedef)
- [GetDeploymentResponseTypeDef](./type_defs.md#getdeploymentresponsetypedef)
- [InstalledComponentTypeDef](./type_defs.md#installedcomponenttypedef)
- [IoTJobAbortConfigTypeDef](./type_defs.md#iotjobabortconfigtypedef)
- [IoTJobAbortCriteriaTypeDef](./type_defs.md#iotjobabortcriteriatypedef)
- [IoTJobExecutionsRolloutConfigTypeDef](./type_defs.md#iotjobexecutionsrolloutconfigtypedef)
- [IoTJobExponentialRolloutRateTypeDef](./type_defs.md#iotjobexponentialrolloutratetypedef)
- [IoTJobRateIncreaseCriteriaTypeDef](./type_defs.md#iotjobrateincreasecriteriatypedef)
- [IoTJobTimeoutConfigTypeDef](./type_defs.md#iotjobtimeoutconfigtypedef)
- [LambdaContainerParamsTypeDef](./type_defs.md#lambdacontainerparamstypedef)
- [LambdaDeviceMountTypeDef](./type_defs.md#lambdadevicemounttypedef)
- [LambdaEventSourceTypeDef](./type_defs.md#lambdaeventsourcetypedef)
- [LambdaExecutionParametersTypeDef](./type_defs.md#lambdaexecutionparameterstypedef)
- [LambdaFunctionRecipeSourceTypeDef](./type_defs.md#lambdafunctionrecipesourcetypedef)
- [LambdaLinuxProcessParamsTypeDef](./type_defs.md#lambdalinuxprocessparamstypedef)
- [LambdaVolumeMountTypeDef](./type_defs.md#lambdavolumemounttypedef)
- [ListComponentVersionsResponseTypeDef](./type_defs.md#listcomponentversionsresponsetypedef)
- [ListComponentsResponseTypeDef](./type_defs.md#listcomponentsresponsetypedef)
- [ListCoreDevicesResponseTypeDef](./type_defs.md#listcoredevicesresponsetypedef)
- [ListDeploymentsResponseTypeDef](./type_defs.md#listdeploymentsresponsetypedef)
- [ListEffectiveDeploymentsResponseTypeDef](./type_defs.md#listeffectivedeploymentsresponsetypedef)
- [ListInstalledComponentsResponseTypeDef](./type_defs.md#listinstalledcomponentsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResolveComponentCandidatesResponseTypeDef](./type_defs.md#resolvecomponentcandidatesresponsetypedef)
- [ResolvedComponentVersionTypeDef](./type_defs.md#resolvedcomponentversiontypedef)
