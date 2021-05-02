# Type annotations for boto3 IoTThingsGraph module

> [Index](../index.md) > IoTThingsGraph

Auto-generated documentation for [IoTThingsGraph](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html#IoTThingsGraph)
type annotations stubs module [mypy_boto3_iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/).

```bash
pip install mypy-boto3-iotthingsgraph
```

- [Type annotations for boto3 IoTThingsGraph module](#type-annotations-for-boto3-iotthingsgraph-module)
  - [IoTThingsGraphClient](#iotthingsgraphclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTThingsGraphClient

Type annotations for  `boto3.client("iotthingsgraph")` as [IoTThingsGraphClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.client import IoTThingsGraphClient
```


IoTThingsGraphClient [exceptions](./client.md#exceptions)



### Methods
- [associate_entity_to_thing](./client.md#associate-entity-to-thing)
- [can_paginate](./client.md#can-paginate)
- [create_flow_template](./client.md#create-flow-template)
- [create_system_instance](./client.md#create-system-instance)
- [create_system_template](./client.md#create-system-template)
- [delete_flow_template](./client.md#delete-flow-template)
- [delete_namespace](./client.md#delete-namespace)
- [delete_system_instance](./client.md#delete-system-instance)
- [delete_system_template](./client.md#delete-system-template)
- [deploy_system_instance](./client.md#deploy-system-instance)
- [deprecate_flow_template](./client.md#deprecate-flow-template)
- [deprecate_system_template](./client.md#deprecate-system-template)
- [describe_namespace](./client.md#describe-namespace)
- [dissociate_entity_from_thing](./client.md#dissociate-entity-from-thing)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_entities](./client.md#get-entities)
- [get_flow_template](./client.md#get-flow-template)
- [get_flow_template_revisions](./client.md#get-flow-template-revisions)
- [get_namespace_deletion_status](./client.md#get-namespace-deletion-status)
- [get_paginator](./client.md#get-paginator)
- [get_system_instance](./client.md#get-system-instance)
- [get_system_template](./client.md#get-system-template)
- [get_system_template_revisions](./client.md#get-system-template-revisions)
- [get_upload_status](./client.md#get-upload-status)
- [list_flow_execution_messages](./client.md#list-flow-execution-messages)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [search_entities](./client.md#search-entities)
- [search_flow_executions](./client.md#search-flow-executions)
- [search_flow_templates](./client.md#search-flow-templates)
- [search_system_instances](./client.md#search-system-instances)
- [search_system_templates](./client.md#search-system-templates)
- [search_things](./client.md#search-things)
- [tag_resource](./client.md#tag-resource)
- [undeploy_system_instance](./client.md#undeploy-system-instance)
- [untag_resource](./client.md#untag-resource)
- [update_flow_template](./client.md#update-flow-template)
- [update_system_template](./client.md#update-system-template)
- [upload_entity_definitions](./client.md#upload-entity-definitions)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceAlreadyExistsException](./client.md#resourcealreadyexistsexception)
- [ResourceInUseException](./client.md#resourceinuseexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iotthingsgraph").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.paginators import GetFlowTemplateRevisionsPaginator, ...
```

- [GetFlowTemplateRevisionsPaginator](./paginators.md#getflowtemplaterevisionspaginator)
- [GetSystemTemplateRevisionsPaginator](./paginators.md#getsystemtemplaterevisionspaginator)
- [ListFlowExecutionMessagesPaginator](./paginators.md#listflowexecutionmessagespaginator)
- [ListTagsForResourcePaginator](./paginators.md#listtagsforresourcepaginator)
- [SearchEntitiesPaginator](./paginators.md#searchentitiespaginator)
- [SearchFlowExecutionsPaginator](./paginators.md#searchflowexecutionspaginator)
- [SearchFlowTemplatesPaginator](./paginators.md#searchflowtemplatespaginator)
- [SearchSystemInstancesPaginator](./paginators.md#searchsysteminstancespaginator)
- [SearchSystemTemplatesPaginator](./paginators.md#searchsystemtemplatespaginator)
- [SearchThingsPaginator](./paginators.md#searchthingspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.literals import DefinitionLanguage, ...
```

- [DefinitionLanguage](./literals.md#definitionlanguage)
- [DeploymentTarget](./literals.md#deploymenttarget)
- [EntityFilterName](./literals.md#entityfiltername)
- [EntityType](./literals.md#entitytype)
- [FlowExecutionEventType](./literals.md#flowexecutioneventtype)
- [FlowExecutionStatus](./literals.md#flowexecutionstatus)
- [FlowTemplateFilterName](./literals.md#flowtemplatefiltername)
- [GetFlowTemplateRevisionsPaginatorName](./literals.md#getflowtemplaterevisionspaginatorname)
- [GetSystemTemplateRevisionsPaginatorName](./literals.md#getsystemtemplaterevisionspaginatorname)
- [ListFlowExecutionMessagesPaginatorName](./literals.md#listflowexecutionmessagespaginatorname)
- [ListTagsForResourcePaginatorName](./literals.md#listtagsforresourcepaginatorname)
- [NamespaceDeletionStatus](./literals.md#namespacedeletionstatus)
- [NamespaceDeletionStatusErrorCodes](./literals.md#namespacedeletionstatuserrorcodes)
- [SearchEntitiesPaginatorName](./literals.md#searchentitiespaginatorname)
- [SearchFlowExecutionsPaginatorName](./literals.md#searchflowexecutionspaginatorname)
- [SearchFlowTemplatesPaginatorName](./literals.md#searchflowtemplatespaginatorname)
- [SearchSystemInstancesPaginatorName](./literals.md#searchsysteminstancespaginatorname)
- [SearchSystemTemplatesPaginatorName](./literals.md#searchsystemtemplatespaginatorname)
- [SearchThingsPaginatorName](./literals.md#searchthingspaginatorname)
- [SystemInstanceDeploymentStatus](./literals.md#systeminstancedeploymentstatus)
- [SystemInstanceFilterName](./literals.md#systeminstancefiltername)
- [SystemTemplateFilterName](./literals.md#systemtemplatefiltername)
- [UploadStatus](./literals.md#uploadstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotthingsgraph.type_defs import DefinitionDocumentTypeDef, ...
```

- [DefinitionDocumentTypeDef](./type_defs.md#definitiondocumenttypedef)
- [DependencyRevisionTypeDef](./type_defs.md#dependencyrevisiontypedef)
- [EntityDescriptionTypeDef](./type_defs.md#entitydescriptiontypedef)
- [FlowExecutionMessageTypeDef](./type_defs.md#flowexecutionmessagetypedef)
- [FlowExecutionSummaryTypeDef](./type_defs.md#flowexecutionsummarytypedef)
- [FlowTemplateDescriptionTypeDef](./type_defs.md#flowtemplatedescriptiontypedef)
- [FlowTemplateSummaryTypeDef](./type_defs.md#flowtemplatesummarytypedef)
- [MetricsConfigurationTypeDef](./type_defs.md#metricsconfigurationtypedef)
- [SystemInstanceDescriptionTypeDef](./type_defs.md#systeminstancedescriptiontypedef)
- [SystemInstanceSummaryTypeDef](./type_defs.md#systeminstancesummarytypedef)
- [SystemTemplateDescriptionTypeDef](./type_defs.md#systemtemplatedescriptiontypedef)
- [SystemTemplateSummaryTypeDef](./type_defs.md#systemtemplatesummarytypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [ThingTypeDef](./type_defs.md#thingtypedef)
- [CreateFlowTemplateResponseTypeDef](./type_defs.md#createflowtemplateresponsetypedef)
- [CreateSystemInstanceResponseTypeDef](./type_defs.md#createsysteminstanceresponsetypedef)
- [CreateSystemTemplateResponseTypeDef](./type_defs.md#createsystemtemplateresponsetypedef)
- [DeleteNamespaceResponseTypeDef](./type_defs.md#deletenamespaceresponsetypedef)
- [DeploySystemInstanceResponseTypeDef](./type_defs.md#deploysysteminstanceresponsetypedef)
- [DescribeNamespaceResponseTypeDef](./type_defs.md#describenamespaceresponsetypedef)
- [EntityFilterTypeDef](./type_defs.md#entityfiltertypedef)
- [FlowTemplateFilterTypeDef](./type_defs.md#flowtemplatefiltertypedef)
- [GetEntitiesResponseTypeDef](./type_defs.md#getentitiesresponsetypedef)
- [GetFlowTemplateResponseTypeDef](./type_defs.md#getflowtemplateresponsetypedef)
- [GetFlowTemplateRevisionsResponseTypeDef](./type_defs.md#getflowtemplaterevisionsresponsetypedef)
- [GetNamespaceDeletionStatusResponseTypeDef](./type_defs.md#getnamespacedeletionstatusresponsetypedef)
- [GetSystemInstanceResponseTypeDef](./type_defs.md#getsysteminstanceresponsetypedef)
- [GetSystemTemplateResponseTypeDef](./type_defs.md#getsystemtemplateresponsetypedef)
- [GetSystemTemplateRevisionsResponseTypeDef](./type_defs.md#getsystemtemplaterevisionsresponsetypedef)
- [GetUploadStatusResponseTypeDef](./type_defs.md#getuploadstatusresponsetypedef)
- [ListFlowExecutionMessagesResponseTypeDef](./type_defs.md#listflowexecutionmessagesresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [SearchEntitiesResponseTypeDef](./type_defs.md#searchentitiesresponsetypedef)
- [SearchFlowExecutionsResponseTypeDef](./type_defs.md#searchflowexecutionsresponsetypedef)
- [SearchFlowTemplatesResponseTypeDef](./type_defs.md#searchflowtemplatesresponsetypedef)
- [SearchSystemInstancesResponseTypeDef](./type_defs.md#searchsysteminstancesresponsetypedef)
- [SearchSystemTemplatesResponseTypeDef](./type_defs.md#searchsystemtemplatesresponsetypedef)
- [SearchThingsResponseTypeDef](./type_defs.md#searchthingsresponsetypedef)
- [SystemInstanceFilterTypeDef](./type_defs.md#systeminstancefiltertypedef)
- [SystemTemplateFilterTypeDef](./type_defs.md#systemtemplatefiltertypedef)
- [UndeploySystemInstanceResponseTypeDef](./type_defs.md#undeploysysteminstanceresponsetypedef)
- [UpdateFlowTemplateResponseTypeDef](./type_defs.md#updateflowtemplateresponsetypedef)
- [UpdateSystemTemplateResponseTypeDef](./type_defs.md#updatesystemtemplateresponsetypedef)
- [UploadEntityDefinitionsResponseTypeDef](./type_defs.md#uploadentitydefinitionsresponsetypedef)
