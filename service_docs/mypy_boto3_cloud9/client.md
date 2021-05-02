# Cloud9Client for boto3 Cloud9 module

> [Index](../index.md) > [Cloud9](./index.md) > Cloud9Client

Auto-generated documentation for [Cloud9](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9)
type annotations stubs module [mypy_boto3_cloud9](https://pypi.org/project/mypy-boto3-cloud9/).

- [Cloud9Client for boto3 Cloud9 module](#cloud9client-for-boto3-cloud9-module)
  - [Cloud9Client](#cloud9client)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_environment_ec2](#create_environment_ec2)
    - [create_environment_membership](#create_environment_membership)
    - [delete_environment](#delete_environment)
    - [delete_environment_membership](#delete_environment_membership)
    - [describe_environment_memberships](#describe_environment_memberships)
    - [describe_environment_status](#describe_environment_status)
    - [describe_environments](#describe_environments)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_environments](#list_environments)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_environment](#update_environment)
    - [update_environment_membership](#update_environment_membership)
    - [get_paginator](#get_paginator)
    - [get_paginator](#get_paginator-1)

## Cloud9Client

Type annotations for `boto3.client("cloud9")`

Can be used directly:

```python
from mypy_boto3_cloud9.client import Cloud9Client
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloud9.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConcurrentAccessException`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.LimitExceededException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("cloud9").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_environment_ec2

Type annotations for `boto3.client("cloud9").create_environment_ec2` method.

[Client.create_environment_ec2 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)

```python
def create_environment_ec2(
    self,
    name: str,
    instanceType: str,
    description: str = None,
    clientRequestToken: str = None,
    subnetId: str = None,
    imageId: str = None,
    automaticStopTimeMinutes: int = None,
    ownerArn: str = None,
    tags: List["TagTypeDef"] = None,
    connectionType: ConnectionType = None
) -> CreateEnvironmentEC2ResultTypeDef:
    pass
```

### create_environment_membership

Type annotations for `boto3.client("cloud9").create_environment_membership` method.

[Client.create_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.create_environment_membership)

```python
def create_environment_membership(
    self,
    environmentId: str,
    userArn: str,
    permissions: MemberPermissions
) -> CreateEnvironmentMembershipResultTypeDef:
    pass
```

### delete_environment

Type annotations for `boto3.client("cloud9").delete_environment` method.

[Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.delete_environment)

```python
def delete_environment(
    self,
    environmentId: str
) -> Dict[str, Any]:
    pass
```

### delete_environment_membership

Type annotations for `boto3.client("cloud9").delete_environment_membership` method.

[Client.delete_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)

```python
def delete_environment_membership(
    self,
    environmentId: str,
    userArn: str
) -> Dict[str, Any]:
    pass
```

### describe_environment_memberships

Type annotations for `boto3.client("cloud9").describe_environment_memberships` method.

[Client.describe_environment_memberships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.describe_environment_memberships)

```python
def describe_environment_memberships(
    self,
    userArn: str = None,
    environmentId: str = None,
    permissions: List[Permissions] = None,
    nextToken: str = None,
    maxResults: int = None
) -> DescribeEnvironmentMembershipsResultTypeDef:
    pass
```

### describe_environment_status

Type annotations for `boto3.client("cloud9").describe_environment_status` method.

[Client.describe_environment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.describe_environment_status)

```python
def describe_environment_status(
    self,
    environmentId: str
) -> DescribeEnvironmentStatusResultTypeDef:
    pass
```

### describe_environments

Type annotations for `boto3.client("cloud9").describe_environments` method.

[Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.describe_environments)

```python
def describe_environments(
    self,
    environmentIds: List[str]
) -> DescribeEnvironmentsResultTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloud9").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.generate_presigned_url)

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

### list_environments

Type annotations for `boto3.client("cloud9").list_environments` method.

[Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.list_environments)

```python
def list_environments(
    self,
    nextToken: str = None,
    maxResults: int = None
) -> ListEnvironmentsResultTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("cloud9").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceARN: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("cloud9").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceARN: str,
    Tags: List["TagTypeDef"]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("cloud9").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceARN: str,
    TagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_environment

Type annotations for `boto3.client("cloud9").update_environment` method.

[Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.update_environment)

```python
def update_environment(
    self,
    environmentId: str,
    name: str = None,
    description: str = None
) -> Dict[str, Any]:
    pass
```

### update_environment_membership

Type annotations for `boto3.client("cloud9").update_environment_membership` method.

[Client.update_environment_membership documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.update_environment_membership)

```python
def update_environment_membership(
    self,
    environmentId: str,
    userArn: str,
    permissions: MemberPermissions
) -> UpdateEnvironmentMembershipResultTypeDef:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloud9").get_paginator` method.

[Paginator.DescribeEnvironmentMemberships documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Paginator.DescribeEnvironmentMemberships)

```python
@overload
def get_paginator(
    self,
    operation_name: DescribeEnvironmentMembershipsPaginatorName
) -> DescribeEnvironmentMembershipsPaginator:
    pass
```

### get_paginator

Type annotations for `boto3.client("cloud9").get_paginator` method.

[Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Paginator.ListEnvironments)

```python
@overload
def get_paginator(
    self,
    operation_name: ListEnvironmentsPaginatorName
) -> ListEnvironmentsPaginator:
    pass
```