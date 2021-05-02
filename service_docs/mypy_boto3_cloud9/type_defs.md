# Structures for boto3 Cloud9 module

> [Index](../index.md) > [Cloud9](./index.md) > Structures

Auto-generated documentation for [Cloud9](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9)
type annotations stubs module [mypy_boto3_cloud9](https://pypi.org/project/mypy-boto3-cloud9/).

- [Structures for boto3 Cloud9 module](#structures-for-boto3-cloud9-module)
  - [CreateEnvironmentEC2ResultTypeDef](#createenvironmentec2resulttypedef)
  - [CreateEnvironmentMembershipResultTypeDef](#createenvironmentmembershipresulttypedef)
  - [DescribeEnvironmentMembershipsResultTypeDef](#describeenvironmentmembershipsresulttypedef)
  - [DescribeEnvironmentStatusResultTypeDef](#describeenvironmentstatusresulttypedef)
  - [DescribeEnvironmentsResultTypeDef](#describeenvironmentsresulttypedef)
  - [EnvironmentLifecycleTypeDef](#environmentlifecycletypedef)
  - [EnvironmentMemberTypeDef](#environmentmembertypedef)
  - [EnvironmentTypeDef](#environmenttypedef)
  - [ListEnvironmentsResultTypeDef](#listenvironmentsresulttypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateEnvironmentMembershipResultTypeDef](#updateenvironmentmembershipresulttypedef)

## CreateEnvironmentEC2ResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import CreateEnvironmentEC2ResultTypeDef
```




Optional fields:
- `environmentId`: `str`


## CreateEnvironmentMembershipResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import CreateEnvironmentMembershipResultTypeDef
```


Required fields:
- `membership`: `"EnvironmentMemberTypeDef"`




## DescribeEnvironmentMembershipsResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import DescribeEnvironmentMembershipsResultTypeDef
```




Optional fields:
- `memberships`: `List["EnvironmentMemberTypeDef"]`
- `nextToken`: `str`


## DescribeEnvironmentStatusResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import DescribeEnvironmentStatusResultTypeDef
```


Required fields:
- `status`: `EnvironmentStatus`
- `message`: `str`




## DescribeEnvironmentsResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import DescribeEnvironmentsResultTypeDef
```




Optional fields:
- `environments`: `List["EnvironmentTypeDef"]`


## EnvironmentLifecycleTypeDef

```python
from mypy_boto3_cloud9.type_defs import EnvironmentLifecycleTypeDef
```




Optional fields:
- `status`: `EnvironmentLifecycleStatus`
- `reason`: `str`
- `failureResource`: `str`


## EnvironmentMemberTypeDef

```python
from mypy_boto3_cloud9.type_defs import EnvironmentMemberTypeDef
```


Required fields:
- `permissions`: `Permissions`
- `userId`: `str`
- `userArn`: `str`
- `environmentId`: `str`



Optional fields:
- `lastAccess`: `datetime`


## EnvironmentTypeDef

```python
from mypy_boto3_cloud9.type_defs import EnvironmentTypeDef
```


Required fields:
- `type`: `EnvironmentType`
- `arn`: `str`
- `ownerArn`: `str`



Optional fields:
- `id`: `str`
- `name`: `str`
- `description`: `str`
- `connectionType`: `ConnectionType`
- `lifecycle`: `"EnvironmentLifecycleTypeDef"`
- `managedCredentialsStatus`: `ManagedCredentialsStatus`


## ListEnvironmentsResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import ListEnvironmentsResultTypeDef
```




Optional fields:
- `nextToken`: `str`
- `environmentIds`: `List[str]`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_cloud9.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_cloud9.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## TagTypeDef

```python
from mypy_boto3_cloud9.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UpdateEnvironmentMembershipResultTypeDef

```python
from mypy_boto3_cloud9.type_defs import UpdateEnvironmentMembershipResultTypeDef
```




Optional fields:
- `membership`: `"EnvironmentMemberTypeDef"`

