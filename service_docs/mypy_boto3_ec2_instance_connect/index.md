# Type annotations for boto3 EC2InstanceConnect module

> [Index](../index.md) > EC2InstanceConnect

Auto-generated documentation for [EC2InstanceConnect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect)
type annotations stubs module [mypy_boto3_ec2_instance_connect](https://pypi.org/project/mypy-boto3-ec2-instance-connect/).

```bash
pip install mypy-boto3-ec2-instance-connect
```

- [Type annotations for boto3 EC2InstanceConnect module](#type-annotations-for-boto3-ec2instanceconnect-module)
  - [EC2InstanceConnectClient](#ec2instanceconnectclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Structures](#structures)

## EC2InstanceConnectClient

Type annotations for  `boto3.client("ec2-instance-connect")` as [EC2InstanceConnectClient](./client.md)

Can be used directly:

```python
from mypy_boto3_ec2_instance_connect.client import EC2InstanceConnectClient
```


EC2InstanceConnectClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [send_serial_console_ssh_public_key](./client.md#send-serial-console-ssh-public-key)
- [send_ssh_public_key](./client.md#send-ssh-public-key)




### Exceptions
- [AuthException](./client.md#authexception)
- [ClientError](./client.md#clienterror)
- [EC2InstanceNotFoundException](./client.md#ec2instancenotfoundexception)
- [EC2InstanceTypeInvalidException](./client.md#ec2instancetypeinvalidexception)
- [InvalidArgsException](./client.md#invalidargsexception)
- [SerialConsoleAccessDisabledException](./client.md#serialconsoleaccessdisabledexception)
- [SerialConsoleSessionLimitExceededException](./client.md#serialconsolesessionlimitexceededexception)
- [SerialConsoleSessionUnavailableException](./client.md#serialconsolesessionunavailableexception)
- [ServiceException](./client.md#serviceexception)
- [ThrottlingException](./client.md#throttlingexception)












## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_ec2_instance_connect.type_defs import SendSSHPublicKeyResponseTypeDef, ...
```

- [SendSSHPublicKeyResponseTypeDef](./type_defs.md#sendsshpublickeyresponsetypedef)
- [SendSerialConsoleSSHPublicKeyResponseTypeDef](./type_defs.md#sendserialconsolesshpublickeyresponsetypedef)
