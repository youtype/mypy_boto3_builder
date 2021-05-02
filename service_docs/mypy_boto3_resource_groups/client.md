# ResourceGroupsClient for boto3 ResourceGroups module

> [Index](../index.md) > [ResourceGroups](./index.md) > ResourceGroupsClient

Auto-generated documentation for [ResourceGroups](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups)
type annotations stubs module [mypy_boto3_resource_groups](https://pypi.org/project/mypy-boto3-resource-groups/).

- [ResourceGroupsClient for boto3 ResourceGroups module](#resourcegroupsclient-for-boto3-resourcegroups-module)
  - [ResourceGroupsClient](#resourcegroupsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_group](#create_group)
    - [delete_group](#delete_group)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_group](#get_group)
    - [get_group_configuration](#get_group_configuration)
    - [get_group_query](#get_group_query)
    - [get_tags](#get_tags)
    - [group_resources](#group_resources)
    - [list_group_resources](#list_group_resources)
    - [list_groups](#list_groups)
    - [put_group_configuration](#put_group_configuration)
    - [search_resources](#search_resources)
    - [tag](#tag)
    - [ungroup_resources](#ungroup_resources)
    - [untag](#untag)
    - [update_group](#update_group)
    - [update_group_query](#update_group_query)
    - [get_paginator](#get_paginator)

## ResourceGroupsClient

Type annotations for `boto3.client("resource-groups")`

Can be used directly:

```python
from mypy_boto3_resource_groups.client import ResourceGroupsClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_resource_groups.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.MethodNotAllowedException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("resource-groups").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_group

Type annotations for `boto3.client("resource-groups").create_group` method.

[Client.create_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.create_group)

```python
def create_group(
    self,
    Name: str,
    Description: str = None,
    ResourceQuery: "ResourceQueryTypeDef" = None,
    Tags: Dict[str, str] = None,
    Configuration: List["GroupConfigurationItemTypeDef"] = None
) -> CreateGroupOutputTypeDef:
    pass
```

### delete_group

Type annotations for `boto3.client("resource-groups").delete_group` method.

[Client.delete_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.delete_group)

```python
def delete_group(
    self,
    GroupName: str = None,
    Group: str = None
) -> DeleteGroupOutputTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("resource-groups").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.generate_presigned_url)

```python
def generate_presigned_url(
    self,
    ClientMethod: str,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = 3600,
    HttpMethod: str = None
) -> str:
    pass
```

### get_group

Type annotations for `boto3.client("resource-groups").get_group` method.

[Client.get_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.get_group)

```python
def get_group(
    self,
    GroupName: str = None,
    Group: str = None
) -> GetGroupOutputTypeDef:
    pass
```

### get_group_configuration

Type annotations for `boto3.client("resource-groups").get_group_configuration` method.

[Client.get_group_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.get_group_configuration)

```python
def get_group_configuration(
    self,
    Group: str = None
) -> GetGroupConfigurationOutputTypeDef:
    pass
```

### get_group_query

Type annotations for `boto3.client("resource-groups").get_group_query` method.

[Client.get_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.get_group_query)

```python
def get_group_query(
    self,
    GroupName: str = None,
    Group: str = None
) -> GetGroupQueryOutputTypeDef:
    pass
```

### get_tags

Type annotations for `boto3.client("resource-groups").get_tags` method.

[Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.get_tags)

```python
def get_tags(
    self,
    Arn: str
) -> GetTagsOutputTypeDef:
    pass
```

### group_resources

Type annotations for `boto3.client("resource-groups").group_resources` method.

[Client.group_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.group_resources)

```python
def group_resources(
    self,
    Group: str,
    ResourceArns: List[str]
) -> GroupResourcesOutputTypeDef:
    pass
```

### list_group_resources

Type annotations for `boto3.client("resource-groups").list_group_resources` method.

[Client.list_group_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.list_group_resources)

```python
def list_group_resources(
    self,
    GroupName: str = None,
    Group: str = None,
    Filters: List[ResourceFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListGroupResourcesOutputTypeDef:
    pass
```

### list_groups

Type annotations for `boto3.client("resource-groups").list_groups` method.

[Client.list_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.list_groups)

```python
def list_groups(
    self,
    Filters: List[GroupFilterTypeDef] = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListGroupsOutputTypeDef:
    pass
```

### put_group_configuration

Type annotations for `boto3.client("resource-groups").put_group_configuration` method.

[Client.put_group_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.put_group_configuration)

```python
def put_group_configuration(
    self,
    Group: str = None,
    Configuration: List["GroupConfigurationItemTypeDef"] = None
) -> Dict[str, Any]:
    pass
```

### search_resources

Type annotations for `boto3.client("resource-groups").search_resources` method.

[Client.search_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.search_resources)

```python
def search_resources(
    self,
    ResourceQuery: "ResourceQueryTypeDef",
    MaxResults: int = None,
    NextToken: str = None
) -> SearchResourcesOutputTypeDef:
    pass
```

### tag

Type annotations for `boto3.client("resource-groups").tag` method.

[Client.tag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.tag)

```python
def tag(
    self,
    Arn: str,
    Tags: Dict[str, str]
) -> TagOutputTypeDef:
    pass
```

### ungroup_resources

Type annotations for `boto3.client("resource-groups").ungroup_resources` method.

[Client.ungroup_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.ungroup_resources)

```python
def ungroup_resources(
    self,
    Group: str,
    ResourceArns: List[str]
) -> UngroupResourcesOutputTypeDef:
    pass
```

### untag

Type annotations for `boto3.client("resource-groups").untag` method.

[Client.untag documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.untag)

```python
def untag(
    self,
    Arn: str,
    Keys: List[str]
) -> UntagOutputTypeDef:
    pass
```

### update_group

Type annotations for `boto3.client("resource-groups").update_group` method.

[Client.update_group documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.update_group)

```python
def update_group(
    self,
    GroupName: str = None,
    Group: str = None,
    Description: str = None
) -> UpdateGroupOutputTypeDef:
    pass
```

### update_group_query

Type annotations for `boto3.client("resource-groups").update_group_query` method.

[Client.update_group_query documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html#ResourceGroups.Client.update_group_query)

```python
def update_group_query(
    self,
    ResourceQuery: "ResourceQueryTypeDef",
    GroupName: str = None,
    Group: str = None
) -> UpdateGroupQueryOutputTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("resource-groups").get_paginator` method with overloads.

- `client.get_paginator("list_group_resources")` -> [ListGroupResourcesPaginator](./paginators.md#listgroupresourcespaginator)
- `client.get_paginator("list_groups")` -> [ListGroupsPaginator](./paginators.md#listgroupspaginator)
- `client.get_paginator("search_resources")` -> [SearchResourcesPaginator](./paginators.md#searchresourcespaginator)


