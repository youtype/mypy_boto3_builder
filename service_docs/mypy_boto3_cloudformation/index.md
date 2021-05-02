# Type annotations for boto3 CloudFormation module

> [Index](../index.md) > CloudFormation

Auto-generated documentation for [CloudFormation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
type annotations stubs module [mypy_boto3_cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/).

```bash
pip install mypy-boto3-cloudformation
```

- [Type annotations for boto3 CloudFormation module](#type-annotations-for-boto3-cloudformation-module)
  - [CloudFormationClient](#cloudformationclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [CloudFormationServiceResource](#cloudformationserviceresource)
    - [Collections](#collections)
    - [Resources](#resources)
  - [Paginators](#paginators)
  - [Waiters](#waiters)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudFormationClient

Type annotations for  `boto3.client("cloudformation")` as [CloudFormationClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudformation.client import CloudFormationClient
```


CloudFormationClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_update_stack](./client.md#cancel-update-stack)
- [continue_update_rollback](./client.md#continue-update-rollback)
- [create_change_set](./client.md#create-change-set)
- [create_stack](./client.md#create-stack)
- [create_stack_instances](./client.md#create-stack-instances)
- [create_stack_set](./client.md#create-stack-set)
- [delete_change_set](./client.md#delete-change-set)
- [delete_stack](./client.md#delete-stack)
- [delete_stack_instances](./client.md#delete-stack-instances)
- [delete_stack_set](./client.md#delete-stack-set)
- [deregister_type](./client.md#deregister-type)
- [describe_account_limits](./client.md#describe-account-limits)
- [describe_change_set](./client.md#describe-change-set)
- [describe_stack_drift_detection_status](./client.md#describe-stack-drift-detection-status)
- [describe_stack_events](./client.md#describe-stack-events)
- [describe_stack_instance](./client.md#describe-stack-instance)
- [describe_stack_resource](./client.md#describe-stack-resource)
- [describe_stack_resource_drifts](./client.md#describe-stack-resource-drifts)
- [describe_stack_resources](./client.md#describe-stack-resources)
- [describe_stack_set](./client.md#describe-stack-set)
- [describe_stack_set_operation](./client.md#describe-stack-set-operation)
- [describe_stacks](./client.md#describe-stacks)
- [describe_type](./client.md#describe-type)
- [describe_type_registration](./client.md#describe-type-registration)
- [detect_stack_drift](./client.md#detect-stack-drift)
- [detect_stack_resource_drift](./client.md#detect-stack-resource-drift)
- [detect_stack_set_drift](./client.md#detect-stack-set-drift)
- [estimate_template_cost](./client.md#estimate-template-cost)
- [execute_change_set](./client.md#execute-change-set)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_stack_policy](./client.md#get-stack-policy)
- [get_template](./client.md#get-template)
- [get_template_summary](./client.md#get-template-summary)
- [get_waiter](./client.md#get-waiter)
- [list_change_sets](./client.md#list-change-sets)
- [list_exports](./client.md#list-exports)
- [list_imports](./client.md#list-imports)
- [list_stack_instances](./client.md#list-stack-instances)
- [list_stack_resources](./client.md#list-stack-resources)
- [list_stack_set_operation_results](./client.md#list-stack-set-operation-results)
- [list_stack_set_operations](./client.md#list-stack-set-operations)
- [list_stack_sets](./client.md#list-stack-sets)
- [list_stacks](./client.md#list-stacks)
- [list_type_registrations](./client.md#list-type-registrations)
- [list_type_versions](./client.md#list-type-versions)
- [list_types](./client.md#list-types)
- [record_handler_progress](./client.md#record-handler-progress)
- [register_type](./client.md#register-type)
- [set_stack_policy](./client.md#set-stack-policy)
- [set_type_default_version](./client.md#set-type-default-version)
- [signal_resource](./client.md#signal-resource)
- [stop_stack_set_operation](./client.md#stop-stack-set-operation)
- [update_stack](./client.md#update-stack)
- [update_stack_instances](./client.md#update-stack-instances)
- [update_stack_set](./client.md#update-stack-set)
- [update_termination_protection](./client.md#update-termination-protection)
- [validate_template](./client.md#validate-template)




### Exceptions
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [CFNRegistryException](./client.md#cfnregistryexception)
- [ChangeSetNotFoundException](./client.md#changesetnotfoundexception)
- [ClientError](./client.md#clienterror)
- [CreatedButModifiedException](./client.md#createdbutmodifiedexception)
- [InsufficientCapabilitiesException](./client.md#insufficientcapabilitiesexception)
- [InvalidChangeSetStatusException](./client.md#invalidchangesetstatusexception)
- [InvalidOperationException](./client.md#invalidoperationexception)
- [InvalidStateTransitionException](./client.md#invalidstatetransitionexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NameAlreadyExistsException](./client.md#namealreadyexistsexception)
- [OperationIdAlreadyExistsException](./client.md#operationidalreadyexistsexception)
- [OperationInProgressException](./client.md#operationinprogressexception)
- [OperationNotFoundException](./client.md#operationnotfoundexception)
- [OperationStatusCheckFailedException](./client.md#operationstatuscheckfailedexception)
- [StackInstanceNotFoundException](./client.md#stackinstancenotfoundexception)
- [StackSetNotEmptyException](./client.md#stacksetnotemptyexception)
- [StackSetNotFoundException](./client.md#stacksetnotfoundexception)
- [StaleRequestException](./client.md#stalerequestexception)
- [TokenAlreadyExistsException](./client.md#tokenalreadyexistsexception)
- [TypeNotFoundException](./client.md#typenotfoundexception)




## CloudFormationServiceResource

Type annotations for  `boto3.resource("cloudformation")` as [CloudFormationServiceResource](./service_resource.md)

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import CloudFormationServiceResource
```


### Collections

Type annotations for collections from `boto3.resource("cloudformation").*`.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import ServiceResourceStacksCollection, ...
```

- [ServiceResourceStacksCollection](./service_resource.md#cloudformationserviceresource.stacks)




### Resources

Type annotations for additional resources from `boto3.resource("cloudformation").*`.

Can be used directly:

```python
from mypy_boto3_cloudformation.service_resource import Event, ...
```

- [Event](./service_resource.md#event)
- [Stack](./service_resource.md#stack)
- [StackResource](./service_resource.md#stackresource)
- [StackResourceSummary](./service_resource.md#stackresourcesummary)





## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cloudformation").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.paginators import DescribeAccountLimitsPaginator, ...
```

- [DescribeAccountLimitsPaginator](./paginators.md#describeaccountlimitspaginator)
- [DescribeChangeSetPaginator](./paginators.md#describechangesetpaginator)
- [DescribeStackEventsPaginator](./paginators.md#describestackeventspaginator)
- [DescribeStacksPaginator](./paginators.md#describestackspaginator)
- [ListChangeSetsPaginator](./paginators.md#listchangesetspaginator)
- [ListExportsPaginator](./paginators.md#listexportspaginator)
- [ListImportsPaginator](./paginators.md#listimportspaginator)
- [ListStackInstancesPaginator](./paginators.md#liststackinstancespaginator)
- [ListStackResourcesPaginator](./paginators.md#liststackresourcespaginator)
- [ListStackSetOperationResultsPaginator](./paginators.md#liststacksetoperationresultspaginator)
- [ListStackSetOperationsPaginator](./paginators.md#liststacksetoperationspaginator)
- [ListStackSetsPaginator](./paginators.md#liststacksetspaginator)
- [ListStacksPaginator](./paginators.md#liststackspaginator)




## Waiters

Type annotations for [waiters](./waiters.md) from `boto3.client("cloudformation").get_waiter("...")`.

Can be used directly:

```python
from mypy_boto3_cloudformation.waiters import ChangeSetCreateCompleteWaiter, ...
```

- [ChangeSetCreateCompleteWaiter](./waiters.md#changesetcreatecompletewaiter)
- [StackCreateCompleteWaiter](./waiters.md#stackcreatecompletewaiter)
- [StackDeleteCompleteWaiter](./waiters.md#stackdeletecompletewaiter)
- [StackExistsWaiter](./waiters.md#stackexistswaiter)
- [StackImportCompleteWaiter](./waiters.md#stackimportcompletewaiter)
- [StackRollbackCompleteWaiter](./waiters.md#stackrollbackcompletewaiter)
- [StackUpdateCompleteWaiter](./waiters.md#stackupdatecompletewaiter)
- [TypeRegistrationCompleteWaiter](./waiters.md#typeregistrationcompletewaiter)




## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudformation.literals import AccountGateStatus, ...
```

- [AccountGateStatus](./literals.md#accountgatestatus)
- [CallAs](./literals.md#callas)
- [Capability](./literals.md#capability)
- [ChangeAction](./literals.md#changeaction)
- [ChangeSetCreateCompleteWaiterName](./literals.md#changesetcreatecompletewaitername)
- [ChangeSetStatus](./literals.md#changesetstatus)
- [ChangeSetType](./literals.md#changesettype)
- [ChangeSource](./literals.md#changesource)
- [ChangeType](./literals.md#changetype)
- [DeprecatedStatus](./literals.md#deprecatedstatus)
- [DescribeAccountLimitsPaginatorName](./literals.md#describeaccountlimitspaginatorname)
- [DescribeChangeSetPaginatorName](./literals.md#describechangesetpaginatorname)
- [DescribeStackEventsPaginatorName](./literals.md#describestackeventspaginatorname)
- [DescribeStacksPaginatorName](./literals.md#describestackspaginatorname)
- [DifferenceType](./literals.md#differencetype)
- [EvaluationType](./literals.md#evaluationtype)
- [ExecutionStatus](./literals.md#executionstatus)
- [HandlerErrorCode](./literals.md#handlererrorcode)
- [ListChangeSetsPaginatorName](./literals.md#listchangesetspaginatorname)
- [ListExportsPaginatorName](./literals.md#listexportspaginatorname)
- [ListImportsPaginatorName](./literals.md#listimportspaginatorname)
- [ListStackInstancesPaginatorName](./literals.md#liststackinstancespaginatorname)
- [ListStackResourcesPaginatorName](./literals.md#liststackresourcespaginatorname)
- [ListStackSetOperationResultsPaginatorName](./literals.md#liststacksetoperationresultspaginatorname)
- [ListStackSetOperationsPaginatorName](./literals.md#liststacksetoperationspaginatorname)
- [ListStackSetsPaginatorName](./literals.md#liststacksetspaginatorname)
- [ListStacksPaginatorName](./literals.md#liststackspaginatorname)
- [OnFailure](./literals.md#onfailure)
- [OperationStatus](./literals.md#operationstatus)
- [PermissionModels](./literals.md#permissionmodels)
- [ProvisioningType](./literals.md#provisioningtype)
- [RegionConcurrencyType](./literals.md#regionconcurrencytype)
- [RegistrationStatus](./literals.md#registrationstatus)
- [RegistryType](./literals.md#registrytype)
- [Replacement](./literals.md#replacement)
- [RequiresRecreation](./literals.md#requiresrecreation)
- [ResourceAttribute](./literals.md#resourceattribute)
- [ResourceSignalStatus](./literals.md#resourcesignalstatus)
- [ResourceStatus](./literals.md#resourcestatus)
- [StackCreateCompleteWaiterName](./literals.md#stackcreatecompletewaitername)
- [StackDeleteCompleteWaiterName](./literals.md#stackdeletecompletewaitername)
- [StackDriftDetectionStatus](./literals.md#stackdriftdetectionstatus)
- [StackDriftStatus](./literals.md#stackdriftstatus)
- [StackExistsWaiterName](./literals.md#stackexistswaitername)
- [StackImportCompleteWaiterName](./literals.md#stackimportcompletewaitername)
- [StackInstanceDetailedStatus](./literals.md#stackinstancedetailedstatus)
- [StackInstanceFilterName](./literals.md#stackinstancefiltername)
- [StackInstanceStatus](./literals.md#stackinstancestatus)
- [StackResourceDriftStatus](./literals.md#stackresourcedriftstatus)
- [StackRollbackCompleteWaiterName](./literals.md#stackrollbackcompletewaitername)
- [StackSetDriftDetectionStatus](./literals.md#stacksetdriftdetectionstatus)
- [StackSetDriftStatus](./literals.md#stacksetdriftstatus)
- [StackSetOperationAction](./literals.md#stacksetoperationaction)
- [StackSetOperationResultStatus](./literals.md#stacksetoperationresultstatus)
- [StackSetOperationStatus](./literals.md#stacksetoperationstatus)
- [StackSetStatus](./literals.md#stacksetstatus)
- [StackStatus](./literals.md#stackstatus)
- [StackUpdateCompleteWaiterName](./literals.md#stackupdatecompletewaitername)
- [TemplateStage](./literals.md#templatestage)
- [TypeRegistrationCompleteWaiterName](./literals.md#typeregistrationcompletewaitername)
- [Visibility](./literals.md#visibility)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef, ...
```

- [AccountGateResultTypeDef](./type_defs.md#accountgateresulttypedef)
- [AccountLimitTypeDef](./type_defs.md#accountlimittypedef)
- [AutoDeploymentTypeDef](./type_defs.md#autodeploymenttypedef)
- [ChangeSetSummaryTypeDef](./type_defs.md#changesetsummarytypedef)
- [ChangeTypeDef](./type_defs.md#changetypedef)
- [CreateChangeSetOutputTypeDef](./type_defs.md#createchangesetoutputtypedef)
- [CreateStackInstancesOutputTypeDef](./type_defs.md#createstackinstancesoutputtypedef)
- [CreateStackOutputTypeDef](./type_defs.md#createstackoutputtypedef)
- [CreateStackSetOutputTypeDef](./type_defs.md#createstacksetoutputtypedef)
- [DeleteStackInstancesOutputTypeDef](./type_defs.md#deletestackinstancesoutputtypedef)
- [DeploymentTargetsTypeDef](./type_defs.md#deploymenttargetstypedef)
- [DescribeAccountLimitsOutputTypeDef](./type_defs.md#describeaccountlimitsoutputtypedef)
- [DescribeChangeSetOutputTypeDef](./type_defs.md#describechangesetoutputtypedef)
- [DescribeStackDriftDetectionStatusOutputTypeDef](./type_defs.md#describestackdriftdetectionstatusoutputtypedef)
- [DescribeStackEventsOutputTypeDef](./type_defs.md#describestackeventsoutputtypedef)
- [DescribeStackInstanceOutputTypeDef](./type_defs.md#describestackinstanceoutputtypedef)
- [DescribeStackResourceDriftsOutputTypeDef](./type_defs.md#describestackresourcedriftsoutputtypedef)
- [DescribeStackResourceOutputTypeDef](./type_defs.md#describestackresourceoutputtypedef)
- [DescribeStackResourcesOutputTypeDef](./type_defs.md#describestackresourcesoutputtypedef)
- [DescribeStackSetOperationOutputTypeDef](./type_defs.md#describestacksetoperationoutputtypedef)
- [DescribeStackSetOutputTypeDef](./type_defs.md#describestacksetoutputtypedef)
- [DescribeStacksOutputTypeDef](./type_defs.md#describestacksoutputtypedef)
- [DescribeTypeOutputTypeDef](./type_defs.md#describetypeoutputtypedef)
- [DescribeTypeRegistrationOutputTypeDef](./type_defs.md#describetyperegistrationoutputtypedef)
- [DetectStackDriftOutputTypeDef](./type_defs.md#detectstackdriftoutputtypedef)
- [DetectStackResourceDriftOutputTypeDef](./type_defs.md#detectstackresourcedriftoutputtypedef)
- [DetectStackSetDriftOutputTypeDef](./type_defs.md#detectstacksetdriftoutputtypedef)
- [EstimateTemplateCostOutputTypeDef](./type_defs.md#estimatetemplatecostoutputtypedef)
- [ExportTypeDef](./type_defs.md#exporttypedef)
- [GetStackPolicyOutputTypeDef](./type_defs.md#getstackpolicyoutputtypedef)
- [GetTemplateOutputTypeDef](./type_defs.md#gettemplateoutputtypedef)
- [GetTemplateSummaryOutputTypeDef](./type_defs.md#gettemplatesummaryoutputtypedef)
- [ListChangeSetsOutputTypeDef](./type_defs.md#listchangesetsoutputtypedef)
- [ListExportsOutputTypeDef](./type_defs.md#listexportsoutputtypedef)
- [ListImportsOutputTypeDef](./type_defs.md#listimportsoutputtypedef)
- [ListStackInstancesOutputTypeDef](./type_defs.md#liststackinstancesoutputtypedef)
- [ListStackResourcesOutputTypeDef](./type_defs.md#liststackresourcesoutputtypedef)
- [ListStackSetOperationResultsOutputTypeDef](./type_defs.md#liststacksetoperationresultsoutputtypedef)
- [ListStackSetOperationsOutputTypeDef](./type_defs.md#liststacksetoperationsoutputtypedef)
- [ListStackSetsOutputTypeDef](./type_defs.md#liststacksetsoutputtypedef)
- [ListStacksOutputTypeDef](./type_defs.md#liststacksoutputtypedef)
- [ListTypeRegistrationsOutputTypeDef](./type_defs.md#listtyperegistrationsoutputtypedef)
- [ListTypeVersionsOutputTypeDef](./type_defs.md#listtypeversionsoutputtypedef)
- [ListTypesOutputTypeDef](./type_defs.md#listtypesoutputtypedef)
- [LoggingConfigTypeDef](./type_defs.md#loggingconfigtypedef)
- [ModuleInfoTypeDef](./type_defs.md#moduleinfotypedef)
- [OutputTypeDef](./type_defs.md#outputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ParameterConstraintsTypeDef](./type_defs.md#parameterconstraintstypedef)
- [ParameterDeclarationTypeDef](./type_defs.md#parameterdeclarationtypedef)
- [ParameterTypeDef](./type_defs.md#parametertypedef)
- [PhysicalResourceIdContextKeyValuePairTypeDef](./type_defs.md#physicalresourceidcontextkeyvaluepairtypedef)
- [PropertyDifferenceTypeDef](./type_defs.md#propertydifferencetypedef)
- [RegisterTypeOutputTypeDef](./type_defs.md#registertypeoutputtypedef)
- [ResourceChangeDetailTypeDef](./type_defs.md#resourcechangedetailtypedef)
- [ResourceChangeTypeDef](./type_defs.md#resourcechangetypedef)
- [ResourceIdentifierSummaryTypeDef](./type_defs.md#resourceidentifiersummarytypedef)
- [ResourceTargetDefinitionTypeDef](./type_defs.md#resourcetargetdefinitiontypedef)
- [ResourceToImportTypeDef](./type_defs.md#resourcetoimporttypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [RollbackConfigurationTypeDef](./type_defs.md#rollbackconfigurationtypedef)
- [RollbackTriggerTypeDef](./type_defs.md#rollbacktriggertypedef)
- [StackDriftInformationSummaryTypeDef](./type_defs.md#stackdriftinformationsummarytypedef)
- [StackDriftInformationTypeDef](./type_defs.md#stackdriftinformationtypedef)
- [StackEventTypeDef](./type_defs.md#stackeventtypedef)
- [StackInstanceComprehensiveStatusTypeDef](./type_defs.md#stackinstancecomprehensivestatustypedef)
- [StackInstanceFilterTypeDef](./type_defs.md#stackinstancefiltertypedef)
- [StackInstanceSummaryTypeDef](./type_defs.md#stackinstancesummarytypedef)
- [StackInstanceTypeDef](./type_defs.md#stackinstancetypedef)
- [StackResourceDetailTypeDef](./type_defs.md#stackresourcedetailtypedef)
- [StackResourceDriftInformationSummaryTypeDef](./type_defs.md#stackresourcedriftinformationsummarytypedef)
- [StackResourceDriftInformationTypeDef](./type_defs.md#stackresourcedriftinformationtypedef)
- [StackResourceDriftTypeDef](./type_defs.md#stackresourcedrifttypedef)
- [StackResourceSummaryTypeDef](./type_defs.md#stackresourcesummarytypedef)
- [StackResourceTypeDef](./type_defs.md#stackresourcetypedef)
- [StackSetDriftDetectionDetailsTypeDef](./type_defs.md#stacksetdriftdetectiondetailstypedef)
- [StackSetOperationPreferencesTypeDef](./type_defs.md#stacksetoperationpreferencestypedef)
- [StackSetOperationResultSummaryTypeDef](./type_defs.md#stacksetoperationresultsummarytypedef)
- [StackSetOperationSummaryTypeDef](./type_defs.md#stacksetoperationsummarytypedef)
- [StackSetOperationTypeDef](./type_defs.md#stacksetoperationtypedef)
- [StackSetSummaryTypeDef](./type_defs.md#stacksetsummarytypedef)
- [StackSetTypeDef](./type_defs.md#stacksettypedef)
- [StackSummaryTypeDef](./type_defs.md#stacksummarytypedef)
- [StackTypeDef](./type_defs.md#stacktypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [TemplateParameterTypeDef](./type_defs.md#templateparametertypedef)
- [TypeSummaryTypeDef](./type_defs.md#typesummarytypedef)
- [TypeVersionSummaryTypeDef](./type_defs.md#typeversionsummarytypedef)
- [UpdateStackInstancesOutputTypeDef](./type_defs.md#updatestackinstancesoutputtypedef)
- [UpdateStackOutputTypeDef](./type_defs.md#updatestackoutputtypedef)
- [UpdateStackSetOutputTypeDef](./type_defs.md#updatestacksetoutputtypedef)
- [UpdateTerminationProtectionOutputTypeDef](./type_defs.md#updateterminationprotectionoutputtypedef)
- [ValidateTemplateOutputTypeDef](./type_defs.md#validatetemplateoutputtypedef)
- [WaiterConfigTypeDef](./type_defs.md#waiterconfigtypedef)
