# Structures for boto3 Detective module

> [Index](../index.md) > [Detective](./index.md) > Structures

Auto-generated documentation for [Detective](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html#Detective)
type annotations stubs module [mypy_boto3_detective](https://pypi.org/project/mypy-boto3-detective/).

- [Structures for boto3 Detective module](#structures-for-boto3-detective-module)
  - [GraphTypeDef](#graphtypedef)
  - [MemberDetailTypeDef](#memberdetailtypedef)
  - [UnprocessedAccountTypeDef](#unprocessedaccounttypedef)
  - [AccountTypeDef](#accounttypedef)
  - [CreateGraphResponseTypeDef](#creategraphresponsetypedef)
  - [CreateMembersResponseTypeDef](#createmembersresponsetypedef)
  - [DeleteMembersResponseTypeDef](#deletemembersresponsetypedef)
  - [GetMembersResponseTypeDef](#getmembersresponsetypedef)
  - [ListGraphsResponseTypeDef](#listgraphsresponsetypedef)
  - [ListInvitationsResponseTypeDef](#listinvitationsresponsetypedef)
  - [ListMembersResponseTypeDef](#listmembersresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)

## GraphTypeDef

```python
from mypy_boto3_detective.type_defs import GraphTypeDef
```




Optional fields:
- `Arn`: `str`
- `CreatedTime`: `datetime`


## MemberDetailTypeDef

```python
from mypy_boto3_detective.type_defs import MemberDetailTypeDef
```




Optional fields:
- `AccountId`: `str`
- `EmailAddress`: `str`
- `GraphArn`: `str`
- `MasterId`: `str`
- `AdministratorId`: `str`
- `Status`: `MemberStatus`
- `DisabledReason`: `MemberDisabledReason`
- `InvitedTime`: `datetime`
- `UpdatedTime`: `datetime`
- `VolumeUsageInBytes`: `int`
- `VolumeUsageUpdatedTime`: `datetime`
- `PercentOfGraphUtilization`: `float`
- `PercentOfGraphUtilizationUpdatedTime`: `datetime`


## UnprocessedAccountTypeDef

```python
from mypy_boto3_detective.type_defs import UnprocessedAccountTypeDef
```




Optional fields:
- `AccountId`: `str`
- `Reason`: `str`


## AccountTypeDef

```python
from mypy_boto3_detective.type_defs import AccountTypeDef
```


Required fields:
- `AccountId`: `str`
- `EmailAddress`: `str`




## CreateGraphResponseTypeDef

```python
from mypy_boto3_detective.type_defs import CreateGraphResponseTypeDef
```




Optional fields:
- `GraphArn`: `str`


## CreateMembersResponseTypeDef

```python
from mypy_boto3_detective.type_defs import CreateMembersResponseTypeDef
```




Optional fields:
- `Members`: `List["MemberDetailTypeDef"]`
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`


## DeleteMembersResponseTypeDef

```python
from mypy_boto3_detective.type_defs import DeleteMembersResponseTypeDef
```




Optional fields:
- `AccountIds`: `List[str]`
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`


## GetMembersResponseTypeDef

```python
from mypy_boto3_detective.type_defs import GetMembersResponseTypeDef
```




Optional fields:
- `MemberDetails`: `List["MemberDetailTypeDef"]`
- `UnprocessedAccounts`: `List["UnprocessedAccountTypeDef"]`


## ListGraphsResponseTypeDef

```python
from mypy_boto3_detective.type_defs import ListGraphsResponseTypeDef
```




Optional fields:
- `GraphList`: `List["GraphTypeDef"]`
- `NextToken`: `str`


## ListInvitationsResponseTypeDef

```python
from mypy_boto3_detective.type_defs import ListInvitationsResponseTypeDef
```




Optional fields:
- `Invitations`: `List["MemberDetailTypeDef"]`
- `NextToken`: `str`


## ListMembersResponseTypeDef

```python
from mypy_boto3_detective.type_defs import ListMembersResponseTypeDef
```




Optional fields:
- `MemberDetails`: `List["MemberDetailTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_detective.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `Dict[str, str]`

