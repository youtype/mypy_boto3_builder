# TransferClient for boto3 Transfer module

> [Index](../index.md) > [Transfer](./index.md) > TransferClient

Auto-generated documentation for [Transfer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer)
type annotations stubs module [mypy_boto3_transfer](https://pypi.org/project/mypy-boto3-transfer/).

- [TransferClient for boto3 Transfer module](#transferclient-for-boto3-transfer-module)
  - [TransferClient](#transferclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_server](#create_server)
    - [create_user](#create_user)
    - [delete_server](#delete_server)
    - [delete_ssh_public_key](#delete_ssh_public_key)
    - [delete_user](#delete_user)
    - [describe_security_policy](#describe_security_policy)
    - [describe_server](#describe_server)
    - [describe_user](#describe_user)
    - [generate_presigned_url](#generate_presigned_url)
    - [import_ssh_public_key](#import_ssh_public_key)
    - [list_security_policies](#list_security_policies)
    - [list_servers](#list_servers)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [list_users](#list_users)
    - [start_server](#start_server)
    - [stop_server](#stop_server)
    - [tag_resource](#tag_resource)
    - [test_identity_provider](#test_identity_provider)
    - [untag_resource](#untag_resource)
    - [update_server](#update_server)
    - [update_user](#update_user)
    - [get_paginator](#get_paginator)

## TransferClient

Type annotations for `boto3.client("transfer")`

Can be used directly:

```python
from mypy_boto3_transfer.client import TransferClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_transfer.client import Exceptions

def handle_error(exc: Exceptions.AccessDeniedException) -> None:
    ...
```


Exceptions:

- `Exceptions.AccessDeniedException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.InternalServiceError`
- `Exceptions.InvalidNextTokenException`
- `Exceptions.InvalidRequestException`
- `Exceptions.ResourceExistsException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("transfer").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_server

Type annotations for `boto3.client("transfer").create_server` method.

[Client.create_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_server)

```python
def create_server(
    self,
    Certificate: str = None,
    Domain: Domain = None,
    EndpointDetails: "EndpointDetailsTypeDef" = None,
    EndpointType: EndpointType = None,
    HostKey: str = None,
    IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
    IdentityProviderType: IdentityProviderType = None,
    LoggingRole: str = None,
    Protocols: List[ProtocolType] = None,
    SecurityPolicyName: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateServerResponseTypeDef:
    pass
```

### create_user

Type annotations for `boto3.client("transfer").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_user)

```python
def create_user(
    self,
    Role: str,
    ServerId: str,
    UserName: str,
    HomeDirectory: str = None,
    HomeDirectoryType: HomeDirectoryType = None,
    HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
    Policy: str = None,
    PosixProfile: "PosixProfileTypeDef" = None,
    SshPublicKeyBody: str = None,
    Tags: List["TagTypeDef"] = None
) -> CreateUserResponseTypeDef:
    pass
```

### delete_server

Type annotations for `boto3.client("transfer").delete_server` method.

[Client.delete_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_server)

```python
def delete_server(
    self,
    ServerId: str
) -> None:
    pass
```

### delete_ssh_public_key

Type annotations for `boto3.client("transfer").delete_ssh_public_key` method.

[Client.delete_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)

```python
def delete_ssh_public_key(
    self,
    ServerId: str,
    SshPublicKeyId: str,
    UserName: str
) -> None:
    pass
```

### delete_user

Type annotations for `boto3.client("transfer").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_user)

```python
def delete_user(
    self,
    ServerId: str,
    UserName: str
) -> None:
    pass
```

### describe_security_policy

Type annotations for `boto3.client("transfer").describe_security_policy` method.

[Client.describe_security_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_security_policy)

```python
def describe_security_policy(
    self,
    SecurityPolicyName: str
) -> DescribeSecurityPolicyResponseTypeDef:
    pass
```

### describe_server

Type annotations for `boto3.client("transfer").describe_server` method.

[Client.describe_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_server)

```python
def describe_server(
    self,
    ServerId: str
) -> DescribeServerResponseTypeDef:
    pass
```

### describe_user

Type annotations for `boto3.client("transfer").describe_user` method.

[Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_user)

```python
def describe_user(
    self,
    ServerId: str,
    UserName: str
) -> DescribeUserResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("transfer").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.generate_presigned_url)

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

### import_ssh_public_key

Type annotations for `boto3.client("transfer").import_ssh_public_key` method.

[Client.import_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)

```python
def import_ssh_public_key(
    self,
    ServerId: str,
    SshPublicKeyBody: str,
    UserName: str
) -> ImportSshPublicKeyResponseTypeDef:
    pass
```

### list_security_policies

Type annotations for `boto3.client("transfer").list_security_policies` method.

[Client.list_security_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_security_policies)

```python
def list_security_policies(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListSecurityPoliciesResponseTypeDef:
    pass
```

### list_servers

Type annotations for `boto3.client("transfer").list_servers` method.

[Client.list_servers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_servers)

```python
def list_servers(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListServersResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("transfer").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    Arn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("transfer").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_users)

```python
def list_users(
    self,
    ServerId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListUsersResponseTypeDef:
    pass
```

### start_server

Type annotations for `boto3.client("transfer").start_server` method.

[Client.start_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.start_server)

```python
def start_server(
    self,
    ServerId: str
) -> None:
    pass
```

### stop_server

Type annotations for `boto3.client("transfer").stop_server` method.

[Client.stop_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.stop_server)

```python
def stop_server(
    self,
    ServerId: str
) -> None:
    pass
```

### tag_resource

Type annotations for `boto3.client("transfer").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.tag_resource)

```python
def tag_resource(
    self,
    Arn: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### test_identity_provider

Type annotations for `boto3.client("transfer").test_identity_provider` method.

[Client.test_identity_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.test_identity_provider)

```python
def test_identity_provider(
    self,
    ServerId: str,
    UserName: str,
    ServerProtocol: ProtocolType = None,
    SourceIp: str = None,
    UserPassword: str = None
) -> TestIdentityProviderResponseTypeDef:
    pass
```

### untag_resource

Type annotations for `boto3.client("transfer").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.untag_resource)

```python
def untag_resource(
    self,
    Arn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_server

Type annotations for `boto3.client("transfer").update_server` method.

[Client.update_server documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_server)

```python
def update_server(
    self,
    ServerId: str,
    Certificate: str = None,
    EndpointDetails: "EndpointDetailsTypeDef" = None,
    EndpointType: EndpointType = None,
    HostKey: str = None,
    IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
    LoggingRole: str = None,
    Protocols: List[ProtocolType] = None,
    SecurityPolicyName: str = None
) -> UpdateServerResponseTypeDef:
    pass
```

### update_user

Type annotations for `boto3.client("transfer").update_user` method.

[Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_user)

```python
def update_user(
    self,
    ServerId: str,
    UserName: str,
    HomeDirectory: str = None,
    HomeDirectoryType: HomeDirectoryType = None,
    HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
    Policy: str = None,
    PosixProfile: "PosixProfileTypeDef" = None,
    Role: str = None
) -> UpdateUserResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("transfer").get_paginator` method with overloads.

- `client.get_paginator("list_servers")` -> [ListServersPaginator](./paginators.md#listserverspaginator)


