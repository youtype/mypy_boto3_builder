# Type annotations for boto3 IoT1ClickProjects module

> [Index](../index.md) > IoT1ClickProjects

Auto-generated documentation for [IoT1ClickProjects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html#IoT1ClickProjects)
type annotations stubs module [mypy_boto3_iot1click_projects](https://pypi.org/project/mypy-boto3-iot1click-projects/).

```bash
pip install mypy-boto3-iot1click-projects
```

- [Type annotations for boto3 IoT1ClickProjects module](#type-annotations-for-boto3-iot1clickprojects-module)
  - [IoT1ClickProjectsClient](#iot1clickprojectsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## IoT1ClickProjectsClient

Type annotations for  `boto3.client("iot1click-projects")` as [IoT1ClickProjectsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_iot1click_projects.client import IoT1ClickProjectsClient
```


IoT1ClickProjectsClient [exceptions](./client.md#exceptions)



### Methods
- [associate_device_with_placement](./client.md#associate-device-with-placement)
- [can_paginate](./client.md#can-paginate)
- [create_placement](./client.md#create-placement)
- [create_project](./client.md#create-project)
- [delete_placement](./client.md#delete-placement)
- [delete_project](./client.md#delete-project)
- [describe_placement](./client.md#describe-placement)
- [describe_project](./client.md#describe-project)
- [disassociate_device_from_placement](./client.md#disassociate-device-from-placement)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_devices_in_placement](./client.md#get-devices-in-placement)
- [get_paginator](./client.md#get-paginator)
- [list_placements](./client.md#list-placements)
- [list_projects](./client.md#list-projects)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_placement](./client.md#update-placement)
- [update_project](./client.md#update-project)




### Exceptions
- [ClientError](./client.md#clienterror)
- [InternalFailureException](./client.md#internalfailureexception)
- [InvalidRequestException](./client.md#invalidrequestexception)
- [ResourceConflictException](./client.md#resourceconflictexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("iot1click-projects").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_iot1click_projects.paginators import ListPlacementsPaginator, ...
```

- [ListPlacementsPaginator](./paginators.md#listplacementspaginator)
- [ListProjectsPaginator](./paginators.md#listprojectspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot1click_projects.literals import ListPlacementsPaginatorName, ...
```

- [ListPlacementsPaginatorName](./literals.md#listplacementspaginatorname)
- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_iot1click_projects.type_defs import DescribePlacementResponseTypeDef, ...
```

- [DescribePlacementResponseTypeDef](./type_defs.md#describeplacementresponsetypedef)
- [DescribeProjectResponseTypeDef](./type_defs.md#describeprojectresponsetypedef)
- [DeviceTemplateTypeDef](./type_defs.md#devicetemplatetypedef)
- [GetDevicesInPlacementResponseTypeDef](./type_defs.md#getdevicesinplacementresponsetypedef)
- [ListPlacementsResponseTypeDef](./type_defs.md#listplacementsresponsetypedef)
- [ListProjectsResponseTypeDef](./type_defs.md#listprojectsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [PlacementDescriptionTypeDef](./type_defs.md#placementdescriptiontypedef)
- [PlacementSummaryTypeDef](./type_defs.md#placementsummarytypedef)
- [PlacementTemplateTypeDef](./type_defs.md#placementtemplatetypedef)
- [ProjectDescriptionTypeDef](./type_defs.md#projectdescriptiontypedef)
- [ProjectSummaryTypeDef](./type_defs.md#projectsummarytypedef)
