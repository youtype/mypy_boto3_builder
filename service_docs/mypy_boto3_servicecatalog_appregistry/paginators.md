# Paginators for boto3 AppRegistry module

> [Index](../index.md) > [AppRegistry](./index.md) > Paginators

Auto-generated documentation for [AppRegistry](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry)
type annotations stubs module [mypy_boto3_servicecatalog_appregistry](https://pypi.org/project/mypy-boto3-servicecatalog-appregistry/).

- [Paginators for boto3 AppRegistry module](#paginators-for-boto3-appregistry-module)
  - [ListApplicationsPaginator](#listapplicationspaginator)
  - [ListAssociatedAttributeGroupsPaginator](#listassociatedattributegroupspaginator)
  - [ListAssociatedResourcesPaginator](#listassociatedresourcespaginator)
  - [ListAttributeGroupsPaginator](#listattributegroupspaginator)

## ListApplicationsPaginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator("list_applications")`.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.paginators import ListApplicationsPaginator

def get_list_applications_paginator() -> ListApplicationsPaginator:
    return boto3.client("servicecatalog-appregistry").get_paginator("list_applications")
```

[Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListApplications)

```python
class ListApplicationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        pass
```
## ListAssociatedAttributeGroupsPaginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator("list_associated_attribute_groups")`.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.paginators import ListAssociatedAttributeGroupsPaginator

def get_list_associated_attribute_groups_paginator() -> ListAssociatedAttributeGroupsPaginator:
    return boto3.client("servicecatalog-appregistry").get_paginator("list_associated_attribute_groups")
```

[Paginator.ListAssociatedAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedAttributeGroups)

```python
class ListAssociatedAttributeGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        application: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedAttributeGroupsResponseTypeDef]:
        pass
```
## ListAssociatedResourcesPaginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator("list_associated_resources")`.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.paginators import ListAssociatedResourcesPaginator

def get_list_associated_resources_paginator() -> ListAssociatedResourcesPaginator:
    return boto3.client("servicecatalog-appregistry").get_paginator("list_associated_resources")
```

[Paginator.ListAssociatedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAssociatedResources)

```python
class ListAssociatedResourcesPaginator(Boto3Paginator):
    def paginate(
        self,
        application: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedResourcesResponseTypeDef]:
        pass
```
## ListAttributeGroupsPaginator

Type annotations for `boto3.client("servicecatalog-appregistry").get_paginator("list_attribute_groups")`.

Can be used directly:

```python
from mypy_boto3_servicecatalog_appregistry.paginators import ListAttributeGroupsPaginator

def get_list_attribute_groups_paginator() -> ListAttributeGroupsPaginator:
    return boto3.client("servicecatalog-appregistry").get_paginator("list_attribute_groups")
```

[Paginator.ListAttributeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry.Paginator.ListAttributeGroups)

```python
class ListAttributeGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAttributeGroupsResponseTypeDef]:
        pass
```