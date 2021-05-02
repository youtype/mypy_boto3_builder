# Structures for boto3 Transfer module

> [Index](../index.md) > [Transfer](./index.md) > Structures

Auto-generated documentation for [Transfer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer)
type annotations stubs module [mypy_boto3_transfer](https://pypi.org/project/mypy-boto3-transfer/).

- [Structures for boto3 Transfer module](#structures-for-boto3-transfer-module)
  - [CreateServerResponseTypeDef](#createserverresponsetypedef)
  - [CreateUserResponseTypeDef](#createuserresponsetypedef)
  - [DescribeSecurityPolicyResponseTypeDef](#describesecuritypolicyresponsetypedef)
  - [DescribeServerResponseTypeDef](#describeserverresponsetypedef)
  - [DescribeUserResponseTypeDef](#describeuserresponsetypedef)
  - [DescribedSecurityPolicyTypeDef](#describedsecuritypolicytypedef)
  - [DescribedServerTypeDef](#describedservertypedef)
  - [DescribedUserTypeDef](#describedusertypedef)
  - [EndpointDetailsTypeDef](#endpointdetailstypedef)
  - [HomeDirectoryMapEntryTypeDef](#homedirectorymapentrytypedef)
  - [IdentityProviderDetailsTypeDef](#identityproviderdetailstypedef)
  - [ImportSshPublicKeyResponseTypeDef](#importsshpublickeyresponsetypedef)
  - [ListSecurityPoliciesResponseTypeDef](#listsecuritypoliciesresponsetypedef)
  - [ListServersResponseTypeDef](#listserversresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListUsersResponseTypeDef](#listusersresponsetypedef)
  - [ListedServerTypeDef](#listedservertypedef)
  - [ListedUserTypeDef](#listedusertypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PosixProfileTypeDef](#posixprofiletypedef)
  - [SshPublicKeyTypeDef](#sshpublickeytypedef)
  - [TagTypeDef](#tagtypedef)
  - [TestIdentityProviderResponseTypeDef](#testidentityproviderresponsetypedef)
  - [UpdateServerResponseTypeDef](#updateserverresponsetypedef)
  - [UpdateUserResponseTypeDef](#updateuserresponsetypedef)

## CreateServerResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import CreateServerResponseTypeDef
```


Required fields:
- `ServerId`: `str`




## CreateUserResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import CreateUserResponseTypeDef
```


Required fields:
- `ServerId`: `str`
- `UserName`: `str`




## DescribeSecurityPolicyResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import DescribeSecurityPolicyResponseTypeDef
```


Required fields:
- `SecurityPolicy`: `"DescribedSecurityPolicyTypeDef"`




## DescribeServerResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import DescribeServerResponseTypeDef
```


Required fields:
- `Server`: `"DescribedServerTypeDef"`




## DescribeUserResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import DescribeUserResponseTypeDef
```


Required fields:
- `ServerId`: `str`
- `User`: `"DescribedUserTypeDef"`




## DescribedSecurityPolicyTypeDef

```python
from mypy_boto3_transfer.type_defs import DescribedSecurityPolicyTypeDef
```


Required fields:
- `SecurityPolicyName`: `str`



Optional fields:
- `Fips`: `bool`
- `SshCiphers`: `List[str]`
- `SshKexs`: `List[str]`
- `SshMacs`: `List[str]`
- `TlsCiphers`: `List[str]`


## DescribedServerTypeDef

```python
from mypy_boto3_transfer.type_defs import DescribedServerTypeDef
```


Required fields:
- `Arn`: `str`



Optional fields:
- `Certificate`: `str`
- `Domain`: `Domain`
- `EndpointDetails`: `"EndpointDetailsTypeDef"`
- `EndpointType`: `EndpointType`
- `HostKeyFingerprint`: `str`
- `IdentityProviderDetails`: `"IdentityProviderDetailsTypeDef"`
- `IdentityProviderType`: `IdentityProviderType`
- `LoggingRole`: `str`
- `Protocols`: `List[ProtocolType]`
- `SecurityPolicyName`: `str`
- `ServerId`: `str`
- `State`: `State`
- `Tags`: `List["TagTypeDef"]`
- `UserCount`: `int`


## DescribedUserTypeDef

```python
from mypy_boto3_transfer.type_defs import DescribedUserTypeDef
```


Required fields:
- `Arn`: `str`



Optional fields:
- `HomeDirectory`: `str`
- `HomeDirectoryMappings`: `List["HomeDirectoryMapEntryTypeDef"]`
- `HomeDirectoryType`: `HomeDirectoryType`
- `Policy`: `str`
- `PosixProfile`: `"PosixProfileTypeDef"`
- `Role`: `str`
- `SshPublicKeys`: `List["SshPublicKeyTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `UserName`: `str`


## EndpointDetailsTypeDef

```python
from mypy_boto3_transfer.type_defs import EndpointDetailsTypeDef
```




Optional fields:
- `AddressAllocationIds`: `List[str]`
- `SubnetIds`: `List[str]`
- `VpcEndpointId`: `str`
- `VpcId`: `str`
- `SecurityGroupIds`: `List[str]`


## HomeDirectoryMapEntryTypeDef

```python
from mypy_boto3_transfer.type_defs import HomeDirectoryMapEntryTypeDef
```


Required fields:
- `Entry`: `str`
- `Target`: `str`




## IdentityProviderDetailsTypeDef

```python
from mypy_boto3_transfer.type_defs import IdentityProviderDetailsTypeDef
```




Optional fields:
- `Url`: `str`
- `InvocationRole`: `str`


## ImportSshPublicKeyResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import ImportSshPublicKeyResponseTypeDef
```


Required fields:
- `ServerId`: `str`
- `SshPublicKeyId`: `str`
- `UserName`: `str`




## ListSecurityPoliciesResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import ListSecurityPoliciesResponseTypeDef
```


Required fields:
- `SecurityPolicyNames`: `List[str]`



Optional fields:
- `NextToken`: `str`


## ListServersResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import ListServersResponseTypeDef
```


Required fields:
- `Servers`: `List["ListedServerTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Arn`: `str`
- `NextToken`: `str`
- `Tags`: `List["TagTypeDef"]`


## ListUsersResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import ListUsersResponseTypeDef
```


Required fields:
- `ServerId`: `str`
- `Users`: `List["ListedUserTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListedServerTypeDef

```python
from mypy_boto3_transfer.type_defs import ListedServerTypeDef
```


Required fields:
- `Arn`: `str`



Optional fields:
- `Domain`: `Domain`
- `IdentityProviderType`: `IdentityProviderType`
- `EndpointType`: `EndpointType`
- `LoggingRole`: `str`
- `ServerId`: `str`
- `State`: `State`
- `UserCount`: `int`


## ListedUserTypeDef

```python
from mypy_boto3_transfer.type_defs import ListedUserTypeDef
```


Required fields:
- `Arn`: `str`



Optional fields:
- `HomeDirectory`: `str`
- `HomeDirectoryType`: `HomeDirectoryType`
- `Role`: `str`
- `SshPublicKeyCount`: `int`
- `UserName`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_transfer.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PosixProfileTypeDef

```python
from mypy_boto3_transfer.type_defs import PosixProfileTypeDef
```


Required fields:
- `Uid`: `int`
- `Gid`: `int`



Optional fields:
- `SecondaryGids`: `List[int]`


## SshPublicKeyTypeDef

```python
from mypy_boto3_transfer.type_defs import SshPublicKeyTypeDef
```


Required fields:
- `DateImported`: `datetime`
- `SshPublicKeyBody`: `str`
- `SshPublicKeyId`: `str`




## TagTypeDef

```python
from mypy_boto3_transfer.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## TestIdentityProviderResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import TestIdentityProviderResponseTypeDef
```


Required fields:
- `StatusCode`: `int`
- `Url`: `str`



Optional fields:
- `Response`: `str`
- `Message`: `str`


## UpdateServerResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import UpdateServerResponseTypeDef
```


Required fields:
- `ServerId`: `str`




## UpdateUserResponseTypeDef

```python
from mypy_boto3_transfer.type_defs import UpdateUserResponseTypeDef
```


Required fields:
- `ServerId`: `str`
- `UserName`: `str`



