# Type annotations for boto3 IoTFleetHub module

> [Index](../index.md) > IoTFleetHub

Auto-generated documentation for [IoTFleetHub](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html#IoTFleetHub)
type annotations stubs module [mypy_boto3_iotfleethub](https://pypi.org/project/mypy-boto3-iotfleethub/).

```bash
pip install mypy-boto3-iotfleethub
```

- [Type annotations for boto3 IoTFleetHub module](#type-annotations-for-boto3-iotfleethub-module)
  - [IoTFleetHubClient](#iotfleethubclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## IoTFleetHubClient

Type annotations for  `boto3.client("iotfleethub")` as [IoTFleetHubClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iotfleethub.client import IoTFleetHubClient
```


IoTFleetHubClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_application](./client.md#create-application)
- [delete_application](./client.md#delete-application)
- [describe_application](./client.md#describe-application)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_applications](./client.md#list-applications)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_application](./client.md#update-application)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iotfleethub").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iotfleethub.paginators import ListApplicationsPaginator, ...
```

- [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotfleethub.literals import ApplicationState, ...
```

- [ApplicationState](./literals.md#applicationstate)
- [ListApplicationsPaginatorName](./literals.md#listapplicationspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iotfleethub.type_defs import ApplicationSummaryTypeDef, ...
```

- [ApplicationSummaryTypeDef](./type_defs.md#applicationsummarytypedef)
- [CreateApplicationResponseTypeDef](./type_defs.md#createapplicationresponsetypedef)
- [DescribeApplicationResponseTypeDef](./type_defs.md#describeapplicationresponsetypedef)
- [ListApplicationsResponseTypeDef](./type_defs.md#listapplicationsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
