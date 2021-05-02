# Type annotations for boto3 AppIntegrationsService module

> [Index](../index.md) > AppIntegrationsService

Auto-generated documentation for [AppIntegrationsService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html#AppIntegrationsService)
type annotations stubs module [mypy_boto3_appintegrations](https://pypi.org/project/mypy-boto3-appintegrations/).

```bash
pip install mypy-boto3-appintegrations
```

- [Type annotations for boto3 AppIntegrationsService module](#type-annotations-for-boto3-appintegrationsservice-module)
  - [AppIntegrationsServiceClient](#appintegrationsserviceclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## AppIntegrationsServiceClient

Type annotations for  `boto3.client("appintegrations")` as [AppIntegrationsServiceClient](./client.md)

Can be used directly:

```python
from mypy_boto3_appintegrations.client import AppIntegrationsServiceClient
```


AppIntegrationsServiceClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_event_integration](./client.md#create-event-integration)
- [delete_event_integration](./client.md#delete-event-integration)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_event_integration](./client.md#get-event-integration)
- [list_event_integration_associations](./client.md#list-event-integration-associations)
- [list_event_integrations](./client.md#list-event-integrations)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_event_integration](./client.md#update-event-integration)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [DuplicateResourceException](./client.md#duplicateresourceexception)
- [InternalServiceError](./client.md#internalserviceerror)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ResourceQuotaExceededException](./client.md#resourcequotaexceededexception)
- [ThrottlingException](./client.md#throttlingexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appintegrations.type_defs import CreateEventIntegrationResponseTypeDef, ...
```

- [CreateEventIntegrationResponseTypeDef](./type_defs.md#createeventintegrationresponsetypedef)
- [EventFilterTypeDef](./type_defs.md#eventfiltertypedef)
- [EventIntegrationAssociationTypeDef](./type_defs.md#eventintegrationassociationtypedef)
- [EventIntegrationTypeDef](./type_defs.md#eventintegrationtypedef)
- [GetEventIntegrationResponseTypeDef](./type_defs.md#geteventintegrationresponsetypedef)
- [ListEventIntegrationAssociationsResponseTypeDef](./type_defs.md#listeventintegrationassociationsresponsetypedef)
- [ListEventIntegrationsResponseTypeDef](./type_defs.md#listeventintegrationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
