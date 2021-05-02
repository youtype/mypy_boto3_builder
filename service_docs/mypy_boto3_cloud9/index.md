# Type annotations for boto3 Cloud9 module

> [Index](../index.md) > Cloud9

Auto-generated documentation for [Cloud9](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9)
type annotations stubs module [mypy_boto3_cloud9](https://pypi.org/project/mypy-boto3-cloud9/).

```bash
pip install mypy-boto3-cloud9
```

- [Type annotations for boto3 Cloud9 module](#type-annotations-for-boto3-cloud9-module)
  - [Cloud9Client](#cloud9client)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## Cloud9Client

Type annotations for  `boto3.client("cloud9")` as [Cloud9Client](./client.md)

Can be used directly:

```python
from mypy_boto3_cloud9.client import Cloud9Client
```


Cloud9Client [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_environment_ec2](./client.md#create-environment-ec2)
- [create_environment_membership](./client.md#create-environment-membership)
- [delete_environment](./client.md#delete-environment)
- [delete_environment_membership](./client.md#delete-environment-membership)
- [describe_environment_memberships](./client.md#describe-environment-memberships)
- [describe_environment_status](./client.md#describe-environment-status)
- [describe_environments](./client.md#describe-environments)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_environments](./client.md#list-environments)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_environment](./client.md#update-environment)
- [update_environment_membership](./client.md#update-environment-membership)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentAccessException](./client.md#concurrentaccessexception)
- [ConflictException](./client.md#conflictexception)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cloud9").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cloud9.paginators import DescribeEnvironmentMembershipsPaginator, ...
```

- [DescribeEnvironmentMembershipsPaginator](./paginators.md#describeenvironmentmembershipspaginator)
- [ListEnvironmentsPaginator](./paginators.md#listenvironmentspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloud9.literals import ConnectionType, ...
```

- [ConnectionType](./literals.md#connectiontype)
- [DescribeEnvironmentMembershipsPaginatorName](./literals.md#describeenvironmentmembershipspaginatorname)
- [EnvironmentLifecycleStatus](./literals.md#environmentlifecyclestatus)
- [EnvironmentStatus](./literals.md#environmentstatus)
- [EnvironmentType](./literals.md#environmenttype)
- [ListEnvironmentsPaginatorName](./literals.md#listenvironmentspaginatorname)
- [ManagedCredentialsStatus](./literals.md#managedcredentialsstatus)
- [MemberPermissions](./literals.md#memberpermissions)
- [Permissions](./literals.md#permissions)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloud9.type_defs import EnvironmentLifecycleTypeDef, ...
```

- [EnvironmentLifecycleTypeDef](./type_defs.md#environmentlifecycletypedef)
- [EnvironmentMemberTypeDef](./type_defs.md#environmentmembertypedef)
- [EnvironmentTypeDef](./type_defs.md#environmenttypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CreateEnvironmentEC2ResultTypeDef](./type_defs.md#createenvironmentec2resulttypedef)
- [CreateEnvironmentMembershipResultTypeDef](./type_defs.md#createenvironmentmembershipresulttypedef)
- [DescribeEnvironmentMembershipsResultTypeDef](./type_defs.md#describeenvironmentmembershipsresulttypedef)
- [DescribeEnvironmentStatusResultTypeDef](./type_defs.md#describeenvironmentstatusresulttypedef)
- [DescribeEnvironmentsResultTypeDef](./type_defs.md#describeenvironmentsresulttypedef)
- [ListEnvironmentsResultTypeDef](./type_defs.md#listenvironmentsresulttypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateEnvironmentMembershipResultTypeDef](./type_defs.md#updateenvironmentmembershipresulttypedef)
