# Paginators for boto3 AppStream module

> [Index](../index.md) > [AppStream](./index.md) > Paginators

Auto-generated documentation for [AppStream](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream)
type annotations stubs module [mypy_boto3_appstream](https://pypi.org/project/mypy-boto3-appstream/).

- [Paginators for boto3 AppStream module](#paginators-for-boto3-appstream-module)
  - [DescribeDirectoryConfigsPaginator](#describedirectoryconfigspaginator)
  - [DescribeFleetsPaginator](#describefleetspaginator)
  - [DescribeImageBuildersPaginator](#describeimagebuilderspaginator)
  - [DescribeImagesPaginator](#describeimagespaginator)
  - [DescribeSessionsPaginator](#describesessionspaginator)
  - [DescribeStacksPaginator](#describestackspaginator)
  - [DescribeUserStackAssociationsPaginator](#describeuserstackassociationspaginator)
  - [DescribeUsersPaginator](#describeuserspaginator)
  - [ListAssociatedFleetsPaginator](#listassociatedfleetspaginator)
  - [ListAssociatedStacksPaginator](#listassociatedstackspaginator)

## DescribeDirectoryConfigsPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_directory_configs")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeDirectoryConfigsPaginator

def get_describe_directory_configs_paginator() -> DescribeDirectoryConfigsPaginator:
    return boto3.client("appstream").get_paginator("describe_directory_configs")
```

[Paginator.DescribeDirectoryConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)

```python
class DescribeDirectoryConfigsPaginator(Boto3Paginator):
    def paginate(
        self,
        DirectoryNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDirectoryConfigsResultTypeDef]:
        pass
```
## DescribeFleetsPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_fleets")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeFleetsPaginator

def get_describe_fleets_paginator() -> DescribeFleetsPaginator:
    return boto3.client("appstream").get_paginator("describe_fleets")
```

[Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)

```python
class DescribeFleetsPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetsResultTypeDef]:
        pass
```
## DescribeImageBuildersPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_image_builders")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeImageBuildersPaginator

def get_describe_image_builders_paginator() -> DescribeImageBuildersPaginator:
    return boto3.client("appstream").get_paginator("describe_image_builders")
```

[Paginator.DescribeImageBuilders documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)

```python
class DescribeImageBuildersPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImageBuildersResultTypeDef]:
        pass
```
## DescribeImagesPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_images")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeImagesPaginator

def get_describe_images_paginator() -> DescribeImagesPaginator:
    return boto3.client("appstream").get_paginator("describe_images")
```

[Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeImages)

```python
class DescribeImagesPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: VisibilityType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImagesResultTypeDef]:
        pass
```
## DescribeSessionsPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_sessions")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeSessionsPaginator

def get_describe_sessions_paginator() -> DescribeSessionsPaginator:
    return boto3.client("appstream").get_paginator("describe_sessions")
```

[Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)

```python
class DescribeSessionsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        AuthenticationType: AuthenticationType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSessionsResultTypeDef]:
        pass
```
## DescribeStacksPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_stacks")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeStacksPaginator

def get_describe_stacks_paginator() -> DescribeStacksPaginator:
    return boto3.client("appstream").get_paginator("describe_stacks")
```

[Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)

```python
class DescribeStacksPaginator(Boto3Paginator):
    def paginate(
        self,
        Names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStacksResultTypeDef]:
        pass
```
## DescribeUserStackAssociationsPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_user_stack_associations")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeUserStackAssociationsPaginator

def get_describe_user_stack_associations_paginator() -> DescribeUserStackAssociationsPaginator:
    return boto3.client("appstream").get_paginator("describe_user_stack_associations")
```

[Paginator.DescribeUserStackAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)

```python
class DescribeUserStackAssociationsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: AuthenticationType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUserStackAssociationsResultTypeDef]:
        pass
```
## DescribeUsersPaginator

Type annotations for `boto3.client("appstream").get_paginator("describe_users")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import DescribeUsersPaginator

def get_describe_users_paginator() -> DescribeUsersPaginator:
    return boto3.client("appstream").get_paginator("describe_users")
```

[Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)

```python
class DescribeUsersPaginator(Boto3Paginator):
    def paginate(
        self,
        AuthenticationType: AuthenticationType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUsersResultTypeDef]:
        pass
```
## ListAssociatedFleetsPaginator

Type annotations for `boto3.client("appstream").get_paginator("list_associated_fleets")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import ListAssociatedFleetsPaginator

def get_list_associated_fleets_paginator() -> ListAssociatedFleetsPaginator:
    return boto3.client("appstream").get_paginator("list_associated_fleets")
```

[Paginator.ListAssociatedFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)

```python
class ListAssociatedFleetsPaginator(Boto3Paginator):
    def paginate(
        self,
        StackName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedFleetsResultTypeDef]:
        pass
```
## ListAssociatedStacksPaginator

Type annotations for `boto3.client("appstream").get_paginator("list_associated_stacks")`.

Can be used directly:

```python
from mypy_boto3_appstream.paginators import ListAssociatedStacksPaginator

def get_list_associated_stacks_paginator() -> ListAssociatedStacksPaginator:
    return boto3.client("appstream").get_paginator("list_associated_stacks")
```

[Paginator.ListAssociatedStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)

```python
class ListAssociatedStacksPaginator(Boto3Paginator):
    def paginate(
        self,
        FleetName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedStacksResultTypeDef]:
        pass
```