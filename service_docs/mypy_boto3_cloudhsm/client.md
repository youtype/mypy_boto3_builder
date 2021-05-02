# CloudHSMClient for boto3 CloudHSM module

> [Index](../index.md) > [CloudHSM](./index.md) > CloudHSMClient

Auto-generated documentation for [CloudHSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM)
type annotations stubs module [mypy_boto3_cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm/).

- [CloudHSMClient for boto3 CloudHSM module](#cloudhsmclient-for-boto3-cloudhsm-module)
  - [CloudHSMClient](#cloudhsmclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [add_tags_to_resource](#add_tags_to_resource)
    - [can_paginate](#can_paginate)
    - [create_hapg](#create_hapg)
    - [create_hsm](#create_hsm)
    - [create_luna_client](#create_luna_client)
    - [delete_hapg](#delete_hapg)
    - [delete_hsm](#delete_hsm)
    - [delete_luna_client](#delete_luna_client)
    - [describe_hapg](#describe_hapg)
    - [describe_hsm](#describe_hsm)
    - [describe_luna_client](#describe_luna_client)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_config](#get_config)
    - [list_available_zones](#list_available_zones)
    - [list_hapgs](#list_hapgs)
    - [list_hsms](#list_hsms)
    - [list_luna_clients](#list_luna_clients)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [modify_hapg](#modify_hapg)
    - [modify_hsm](#modify_hsm)
    - [modify_luna_client](#modify_luna_client)
    - [remove_tags_from_resource](#remove_tags_from_resource)
    - [get_paginator](#get_paginator)

## CloudHSMClient

Type annotations for `boto3.client("cloudhsm")`

Can be used directly:

```python
from mypy_boto3_cloudhsm.client import CloudHSMClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudhsm.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.CloudHsmInternalException`
- `Exceptions.CloudHsmServiceException`
- `Exceptions.InvalidRequestException`


## Methods


### add_tags_to_resource

Type annotations for `boto3.client("cloudhsm").add_tags_to_resource` method.

[Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.add_tags_to_resource)

```python
def add_tags_to_resource(
    self,
    ResourceArn: str,
    TagList: List["TagTypeDef"]
) -> AddTagsToResourceResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("cloudhsm").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_hapg

Type annotations for `boto3.client("cloudhsm").create_hapg` method.

[Client.create_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.create_hapg)

```python
def create_hapg(
    self,
    Label: str
) -> CreateHapgResponseTypeDef:
    pass
```

### create_hsm

Type annotations for `boto3.client("cloudhsm").create_hsm` method.

[Client.create_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.create_hsm)

```python
def create_hsm(
    self,
    SubnetId: str,
    SshKey: str,
    IamRoleArn: str,
    SubscriptionType: Literal['PRODUCTION'],
    EniIp: str = None,
    ExternalId: str = None,
    ClientToken: str = None,
    SyslogIp: str = None
) -> CreateHsmResponseTypeDef:
    pass
```

### create_luna_client

Type annotations for `boto3.client("cloudhsm").create_luna_client` method.

[Client.create_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.create_luna_client)

```python
def create_luna_client(
    self,
    Certificate: str,
    Label: str = None
) -> CreateLunaClientResponseTypeDef:
    pass
```

### delete_hapg

Type annotations for `boto3.client("cloudhsm").delete_hapg` method.

[Client.delete_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.delete_hapg)

```python
def delete_hapg(
    self,
    HapgArn: str
) -> DeleteHapgResponseTypeDef:
    pass
```

### delete_hsm

Type annotations for `boto3.client("cloudhsm").delete_hsm` method.

[Client.delete_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.delete_hsm)

```python
def delete_hsm(
    self,
    HsmArn: str
) -> DeleteHsmResponseTypeDef:
    pass
```

### delete_luna_client

Type annotations for `boto3.client("cloudhsm").delete_luna_client` method.

[Client.delete_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.delete_luna_client)

```python
def delete_luna_client(
    self,
    ClientArn: str
) -> DeleteLunaClientResponseTypeDef:
    pass
```

### describe_hapg

Type annotations for `boto3.client("cloudhsm").describe_hapg` method.

[Client.describe_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.describe_hapg)

```python
def describe_hapg(
    self,
    HapgArn: str
) -> DescribeHapgResponseTypeDef:
    pass
```

### describe_hsm

Type annotations for `boto3.client("cloudhsm").describe_hsm` method.

[Client.describe_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.describe_hsm)

```python
def describe_hsm(
    self,
    HsmArn: str = None,
    HsmSerialNumber: str = None
) -> DescribeHsmResponseTypeDef:
    pass
```

### describe_luna_client

Type annotations for `boto3.client("cloudhsm").describe_luna_client` method.

[Client.describe_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.describe_luna_client)

```python
def describe_luna_client(
    self,
    ClientArn: str = None,
    CertificateFingerprint: str = None
) -> DescribeLunaClientResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudhsm").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.generate_presigned_url)

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

### get_config

Type annotations for `boto3.client("cloudhsm").get_config` method.

[Client.get_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.get_config)

```python
def get_config(
    self,
    ClientArn: str,
    ClientVersion: ClientVersion,
    HapgList: List[str]
) -> GetConfigResponseTypeDef:
    pass
```

### list_available_zones

Type annotations for `boto3.client("cloudhsm").list_available_zones` method.

[Client.list_available_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.list_available_zones)

```python
def list_available_zones(
    self
) -> ListAvailableZonesResponseTypeDef:
    pass
```

### list_hapgs

Type annotations for `boto3.client("cloudhsm").list_hapgs` method.

[Client.list_hapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.list_hapgs)

```python
def list_hapgs(
    self,
    NextToken: str = None
) -> ListHapgsResponseTypeDef:
    pass
```

### list_hsms

Type annotations for `boto3.client("cloudhsm").list_hsms` method.

[Client.list_hsms documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.list_hsms)

```python
def list_hsms(
    self,
    NextToken: str = None
) -> ListHsmsResponseTypeDef:
    pass
```

### list_luna_clients

Type annotations for `boto3.client("cloudhsm").list_luna_clients` method.

[Client.list_luna_clients documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.list_luna_clients)

```python
def list_luna_clients(
    self,
    NextToken: str = None
) -> ListLunaClientsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("cloudhsm").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### modify_hapg

Type annotations for `boto3.client("cloudhsm").modify_hapg` method.

[Client.modify_hapg documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.modify_hapg)

```python
def modify_hapg(
    self,
    HapgArn: str,
    Label: str = None,
    PartitionSerialList: List[str] = None
) -> ModifyHapgResponseTypeDef:
    pass
```

### modify_hsm

Type annotations for `boto3.client("cloudhsm").modify_hsm` method.

[Client.modify_hsm documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.modify_hsm)

```python
def modify_hsm(
    self,
    HsmArn: str,
    SubnetId: str = None,
    EniIp: str = None,
    IamRoleArn: str = None,
    ExternalId: str = None,
    SyslogIp: str = None
) -> ModifyHsmResponseTypeDef:
    pass
```

### modify_luna_client

Type annotations for `boto3.client("cloudhsm").modify_luna_client` method.

[Client.modify_luna_client documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.modify_luna_client)

```python
def modify_luna_client(
    self,
    ClientArn: str,
    Certificate: str
) -> ModifyLunaClientResponseTypeDef:
    pass
```

### remove_tags_from_resource

Type annotations for `boto3.client("cloudhsm").remove_tags_from_resource` method.

[Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM.Client.remove_tags_from_resource)

```python
def remove_tags_from_resource(
    self,
    ResourceArn: str,
    TagKeyList: List[str]
) -> RemoveTagsFromResourceResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("cloudhsm").get_paginator` method with overloads.

- `client.get_paginator("list_hapgs")` -> [ListHapgsPaginator](./paginators.md#listhapgspaginator)
- `client.get_paginator("list_hsms")` -> [ListHsmsPaginator](./paginators.md#listhsmspaginator)
- `client.get_paginator("list_luna_clients")` -> [ListLunaClientsPaginator](./paginators.md#listlunaclientspaginator)


