# EC2InstanceConnectClient for boto3 EC2InstanceConnect module

> [Index](../index.md) > [EC2InstanceConnect](./index.md) > EC2InstanceConnectClient

Auto-generated documentation for [EC2InstanceConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect)
type annotations stubs module [mypy_boto3_ec2_instance_connect](https://pypi.org/project/mypy-boto3-ec2-instance-connect/).

- [EC2InstanceConnectClient for boto3 EC2InstanceConnect module](#ec2instanceconnectclient-for-boto3-ec2instanceconnect-module)
  - [EC2InstanceConnectClient](#ec2instanceconnectclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [generate_presigned_url](#generate_presigned_url)
    - [send_serial_console_ssh_public_key](#send_serial_console_ssh_public_key)
    - [send_ssh_public_key](#send_ssh_public_key)

## EC2InstanceConnectClient

Type annotations for `boto3.client("ec2-instance-connect")`

Can be used directly:

```python
from mypy_boto3_ec2_instance_connect.client import EC2InstanceConnectClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_ec2_instance_connect.client import Exceptions

def handle_error(exc: Exceptions.AuthException) -> None:
    ...
```


Exceptions:

- `Exceptions.AuthException`
- `Exceptions.ClientError`
- `Exceptions.EC2InstanceNotFoundException`
- `Exceptions.EC2InstanceTypeInvalidException`
- `Exceptions.InvalidArgsException`
- `Exceptions.SerialConsoleAccessDisabledException`
- `Exceptions.SerialConsoleSessionLimitExceededException`
- `Exceptions.SerialConsoleSessionUnavailableException`
- `Exceptions.ServiceException`
- `Exceptions.ThrottlingException`


## Methods


### can_paginate

Type annotations for `boto3.client("ec2-instance-connect").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("ec2-instance-connect").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)

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

### send_serial_console_ssh_public_key

Type annotations for `boto3.client("ec2-instance-connect").send_serial_console_ssh_public_key` method.

[Client.send_serial_console_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_serial_console_ssh_public_key)

```python
def send_serial_console_ssh_public_key(
    self,
    InstanceId: str,
    SSHPublicKey: str,
    SerialPort: int = None
) -> SendSerialConsoleSSHPublicKeyResponseTypeDef:
    pass
```

### send_ssh_public_key

Type annotations for `boto3.client("ec2-instance-connect").send_ssh_public_key` method.

[Client.send_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)

```python
def send_ssh_public_key(
    self,
    InstanceId: str,
    InstanceOSUser: str,
    SSHPublicKey: str,
    AvailabilityZone: str
) -> SendSSHPublicKeyResponseTypeDef:
    pass
```



