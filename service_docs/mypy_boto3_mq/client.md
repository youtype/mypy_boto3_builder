# MQClient for boto3 MQ module

> [Index](../index.md) > [MQ](./index.md) > MQClient

Auto-generated documentation for [MQ](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ)
type annotations stubs module [mypy_boto3_mq](https://pypi.org/project/mypy-boto3-mq/).

- [MQClient for boto3 MQ module](#mqclient-for-boto3-mq-module)
  - [MQClient](#mqclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_broker](#create_broker)
    - [create_configuration](#create_configuration)
    - [create_tags](#create_tags)
    - [create_user](#create_user)
    - [delete_broker](#delete_broker)
    - [delete_tags](#delete_tags)
    - [delete_user](#delete_user)
    - [describe_broker](#describe_broker)
    - [describe_broker_engine_types](#describe_broker_engine_types)
    - [describe_broker_instance_options](#describe_broker_instance_options)
    - [describe_configuration](#describe_configuration)
    - [describe_configuration_revision](#describe_configuration_revision)
    - [describe_user](#describe_user)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_brokers](#list_brokers)
    - [list_configuration_revisions](#list_configuration_revisions)
    - [list_configurations](#list_configurations)
    - [list_tags](#list_tags)
    - [list_users](#list_users)
    - [reboot_broker](#reboot_broker)
    - [update_broker](#update_broker)
    - [update_configuration](#update_configuration)
    - [update_user](#update_user)
    - [get_paginator](#get_paginator)

## MQClient

Type annotations for `boto3.client("mq")`

Can be used directly:

```python
from mypy_boto3_mq.client import MQClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_mq.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.UnauthorizedException`


## Methods


### can_paginate

Type annotations for `boto3.client("mq").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_broker

Type annotations for `boto3.client("mq").create_broker` method.

[Client.create_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.create_broker)

```python
def create_broker(
    self,
    AuthenticationStrategy: AuthenticationStrategy = None,
    AutoMinorVersionUpgrade: bool = None,
    BrokerName: str = None,
    Configuration: "ConfigurationIdTypeDef" = None,
    CreatorRequestId: str = None,
    DeploymentMode: DeploymentMode = None,
    EncryptionOptions: "EncryptionOptionsTypeDef" = None,
    EngineType: EngineType = None,
    EngineVersion: str = None,
    HostInstanceType: str = None,
    LdapServerMetadata: LdapServerMetadataInputTypeDef = None,
    Logs: "LogsTypeDef" = None,
    MaintenanceWindowStartTime: "WeeklyStartTimeTypeDef" = None,
    PubliclyAccessible: bool = None,
    SecurityGroups: List[str] = None,
    StorageType: BrokerStorageType = None,
    SubnetIds: List[str] = None,
    Tags: Dict[str, str] = None,
    Users: List[UserTypeDef] = None
) -> CreateBrokerResponseTypeDef:
    pass
```

### create_configuration

Type annotations for `boto3.client("mq").create_configuration` method.

[Client.create_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.create_configuration)

```python
def create_configuration(
    self,
    AuthenticationStrategy: AuthenticationStrategy = None,
    EngineType: EngineType = None,
    EngineVersion: str = None,
    Name: str = None,
    Tags: Dict[str, str] = None
) -> CreateConfigurationResponseTypeDef:
    pass
```

### create_tags

Type annotations for `boto3.client("mq").create_tags` method.

[Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.create_tags)

```python
def create_tags(
    self,
    ResourceArn: str,
    Tags: Dict[str, str] = None
) -> None:
    pass
```

### create_user

Type annotations for `boto3.client("mq").create_user` method.

[Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.create_user)

```python
def create_user(
    self,
    BrokerId: str,
    Username: str,
    ConsoleAccess: bool = None,
    Groups: List[str] = None,
    Password: str = None
) -> Dict[str, Any]:
    pass
```

### delete_broker

Type annotations for `boto3.client("mq").delete_broker` method.

[Client.delete_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.delete_broker)

```python
def delete_broker(
    self,
    BrokerId: str
) -> DeleteBrokerResponseTypeDef:
    pass
```

### delete_tags

Type annotations for `boto3.client("mq").delete_tags` method.

[Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.delete_tags)

```python
def delete_tags(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### delete_user

Type annotations for `boto3.client("mq").delete_user` method.

[Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.delete_user)

```python
def delete_user(
    self,
    BrokerId: str,
    Username: str
) -> Dict[str, Any]:
    pass
```

### describe_broker

Type annotations for `boto3.client("mq").describe_broker` method.

[Client.describe_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.describe_broker)

```python
def describe_broker(
    self,
    BrokerId: str
) -> DescribeBrokerResponseTypeDef:
    pass
```

### describe_broker_engine_types

Type annotations for `boto3.client("mq").describe_broker_engine_types` method.

[Client.describe_broker_engine_types documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.describe_broker_engine_types)

```python
def describe_broker_engine_types(
    self,
    EngineType: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> DescribeBrokerEngineTypesResponseTypeDef:
    pass
```

### describe_broker_instance_options

Type annotations for `boto3.client("mq").describe_broker_instance_options` method.

[Client.describe_broker_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.describe_broker_instance_options)

```python
def describe_broker_instance_options(
    self,
    EngineType: str = None,
    HostInstanceType: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    StorageType: str = None
) -> DescribeBrokerInstanceOptionsResponseTypeDef:
    pass
```

### describe_configuration

Type annotations for `boto3.client("mq").describe_configuration` method.

[Client.describe_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.describe_configuration)

```python
def describe_configuration(
    self,
    ConfigurationId: str
) -> DescribeConfigurationResponseTypeDef:
    pass
```

### describe_configuration_revision

Type annotations for `boto3.client("mq").describe_configuration_revision` method.

[Client.describe_configuration_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.describe_configuration_revision)

```python
def describe_configuration_revision(
    self,
    ConfigurationId: str,
    ConfigurationRevision: str
) -> DescribeConfigurationRevisionResponseTypeDef:
    pass
```

### describe_user

Type annotations for `boto3.client("mq").describe_user` method.

[Client.describe_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.describe_user)

```python
def describe_user(
    self,
    BrokerId: str,
    Username: str
) -> DescribeUserResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("mq").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.generate_presigned_url)

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

### list_brokers

Type annotations for `boto3.client("mq").list_brokers` method.

[Client.list_brokers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.list_brokers)

```python
def list_brokers(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListBrokersResponseTypeDef:
    pass
```

### list_configuration_revisions

Type annotations for `boto3.client("mq").list_configuration_revisions` method.

[Client.list_configuration_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.list_configuration_revisions)

```python
def list_configuration_revisions(
    self,
    ConfigurationId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListConfigurationRevisionsResponseTypeDef:
    pass
```

### list_configurations

Type annotations for `boto3.client("mq").list_configurations` method.

[Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.list_configurations)

```python
def list_configurations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListConfigurationsResponseTypeDef:
    pass
```

### list_tags

Type annotations for `boto3.client("mq").list_tags` method.

[Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.list_tags)

```python
def list_tags(
    self,
    ResourceArn: str
) -> ListTagsResponseTypeDef:
    pass
```

### list_users

Type annotations for `boto3.client("mq").list_users` method.

[Client.list_users documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.list_users)

```python
def list_users(
    self,
    BrokerId: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListUsersResponseTypeDef:
    pass
```

### reboot_broker

Type annotations for `boto3.client("mq").reboot_broker` method.

[Client.reboot_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.reboot_broker)

```python
def reboot_broker(
    self,
    BrokerId: str
) -> Dict[str, Any]:
    pass
```

### update_broker

Type annotations for `boto3.client("mq").update_broker` method.

[Client.update_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.update_broker)

```python
def update_broker(
    self,
    BrokerId: str,
    AuthenticationStrategy: AuthenticationStrategy = None,
    AutoMinorVersionUpgrade: bool = None,
    Configuration: "ConfigurationIdTypeDef" = None,
    EngineVersion: str = None,
    HostInstanceType: str = None,
    LdapServerMetadata: LdapServerMetadataInputTypeDef = None,
    Logs: "LogsTypeDef" = None,
    SecurityGroups: List[str] = None
) -> UpdateBrokerResponseTypeDef:
    pass
```

### update_configuration

Type annotations for `boto3.client("mq").update_configuration` method.

[Client.update_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.update_configuration)

```python
def update_configuration(
    self,
    ConfigurationId: str,
    Data: str = None,
    Description: str = None
) -> UpdateConfigurationResponseTypeDef:
    pass
```

### update_user

Type annotations for `boto3.client("mq").update_user` method.

[Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ.Client.update_user)

```python
def update_user(
    self,
    BrokerId: str,
    Username: str,
    ConsoleAccess: bool = None,
    Groups: List[str] = None,
    Password: str = None
) -> Dict[str, Any]:
    pass
```



### get_paginator

Type annotations for `boto3.client("mq").get_paginator` method with overloads.

- `client.get_paginator("list_brokers")` -> [ListBrokersPaginator](./paginators.md#listbrokerspaginator)


