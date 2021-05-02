# KMSClient for boto3 KMS module

> [Index](../index.md) > [KMS](./index.md) > KMSClient

Auto-generated documentation for [KMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS)
type annotations stubs module [mypy_boto3_kms](https://pypi.org/project/mypy-boto3-kms/).

- [KMSClient for boto3 KMS module](#kmsclient-for-boto3-kms-module)
  - [KMSClient](#kmsclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_key_deletion](#cancel_key_deletion)
    - [connect_custom_key_store](#connect_custom_key_store)
    - [create_alias](#create_alias)
    - [create_custom_key_store](#create_custom_key_store)
    - [create_grant](#create_grant)
    - [create_key](#create_key)
    - [decrypt](#decrypt)
    - [delete_alias](#delete_alias)
    - [delete_custom_key_store](#delete_custom_key_store)
    - [delete_imported_key_material](#delete_imported_key_material)
    - [describe_custom_key_stores](#describe_custom_key_stores)
    - [describe_key](#describe_key)
    - [disable_key](#disable_key)
    - [disable_key_rotation](#disable_key_rotation)
    - [disconnect_custom_key_store](#disconnect_custom_key_store)
    - [enable_key](#enable_key)
    - [enable_key_rotation](#enable_key_rotation)
    - [encrypt](#encrypt)
    - [generate_data_key](#generate_data_key)
    - [generate_data_key_pair](#generate_data_key_pair)
    - [generate_data_key_pair_without_plaintext](#generate_data_key_pair_without_plaintext)
    - [generate_data_key_without_plaintext](#generate_data_key_without_plaintext)
    - [generate_presigned_url](#generate_presigned_url)
    - [generate_random](#generate_random)
    - [get_key_policy](#get_key_policy)
    - [get_key_rotation_status](#get_key_rotation_status)
    - [get_parameters_for_import](#get_parameters_for_import)
    - [get_public_key](#get_public_key)
    - [import_key_material](#import_key_material)
    - [list_aliases](#list_aliases)
    - [list_grants](#list_grants)
    - [list_key_policies](#list_key_policies)
    - [list_keys](#list_keys)
    - [list_resource_tags](#list_resource_tags)
    - [list_retirable_grants](#list_retirable_grants)
    - [put_key_policy](#put_key_policy)
    - [re_encrypt](#re_encrypt)
    - [retire_grant](#retire_grant)
    - [revoke_grant](#revoke_grant)
    - [schedule_key_deletion](#schedule_key_deletion)
    - [sign](#sign)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_alias](#update_alias)
    - [update_custom_key_store](#update_custom_key_store)
    - [update_key_description](#update_key_description)
    - [verify](#verify)
    - [get_paginator](#get_paginator)

## KMSClient

Type annotations for `boto3.client("kms")`

Can be used directly:

```python
from mypy_boto3_kms.client import KMSClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kms.client import Exceptions

def handle_error(exc: Exceptions.AlreadyExistsException) -> None:
    ...
```


Exceptions:

- `Exceptions.AlreadyExistsException`
- `Exceptions.ClientError`
- `Exceptions.CloudHsmClusterInUseException`
- `Exceptions.CloudHsmClusterInvalidConfigurationException`
- `Exceptions.CloudHsmClusterNotActiveException`
- `Exceptions.CloudHsmClusterNotFoundException`
- `Exceptions.CloudHsmClusterNotRelatedException`
- `Exceptions.CustomKeyStoreHasCMKsException`
- `Exceptions.CustomKeyStoreInvalidStateException`
- `Exceptions.CustomKeyStoreNameInUseException`
- `Exceptions.CustomKeyStoreNotFoundException`
- `Exceptions.DependencyTimeoutException`
- `Exceptions.DisabledException`
- `Exceptions.ExpiredImportTokenException`
- `Exceptions.IncorrectKeyException`
- `Exceptions.IncorrectKeyMaterialException`
- `Exceptions.IncorrectTrustAnchorException`
- `Exceptions.InvalidAliasNameException`
- `Exceptions.InvalidArnException`
- `Exceptions.InvalidCiphertextException`
- `Exceptions.InvalidGrantIdException`
- `Exceptions.InvalidGrantTokenException`
- `Exceptions.InvalidImportTokenException`
- `Exceptions.InvalidKeyUsageException`
- `Exceptions.InvalidMarkerException`
- `Exceptions.KMSInternalException`
- `Exceptions.KMSInvalidSignatureException`
- `Exceptions.KMSInvalidStateException`
- `Exceptions.KeyUnavailableException`
- `Exceptions.LimitExceededException`
- `Exceptions.MalformedPolicyDocumentException`
- `Exceptions.NotFoundException`
- `Exceptions.TagException`
- `Exceptions.UnsupportedOperationException`


## Methods


### can_paginate

Type annotations for `boto3.client("kms").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_key_deletion

Type annotations for `boto3.client("kms").cancel_key_deletion` method.

[Client.cancel_key_deletion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.cancel_key_deletion)

```python
def cancel_key_deletion(
    self,
    KeyId: str
) -> CancelKeyDeletionResponseTypeDef:
    pass
```

### connect_custom_key_store

Type annotations for `boto3.client("kms").connect_custom_key_store` method.

[Client.connect_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.connect_custom_key_store)

```python
def connect_custom_key_store(
    self,
    CustomKeyStoreId: str
) -> Dict[str, Any]:
    pass
```

### create_alias

Type annotations for `boto3.client("kms").create_alias` method.

[Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.create_alias)

```python
def create_alias(
    self,
    AliasName: str,
    TargetKeyId: str
) -> None:
    pass
```

### create_custom_key_store

Type annotations for `boto3.client("kms").create_custom_key_store` method.

[Client.create_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.create_custom_key_store)

```python
def create_custom_key_store(
    self,
    CustomKeyStoreName: str,
    CloudHsmClusterId: str,
    TrustAnchorCertificate: str,
    KeyStorePassword: str
) -> CreateCustomKeyStoreResponseTypeDef:
    pass
```

### create_grant

Type annotations for `boto3.client("kms").create_grant` method.

[Client.create_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.create_grant)

```python
def create_grant(
    self,
    KeyId: str,
    GranteePrincipal: str,
    Operations: List[GrantOperation],
    RetiringPrincipal: str = None,
    Constraints: "GrantConstraintsTypeDef" = None,
    GrantTokens: List[str] = None,
    Name: str = None
) -> CreateGrantResponseTypeDef:
    pass
```

### create_key

Type annotations for `boto3.client("kms").create_key` method.

[Client.create_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.create_key)

```python
def create_key(
    self,
    Policy: str = None,
    Description: str = None,
    KeyUsage: KeyUsageType = None,
    CustomerMasterKeySpec: CustomerMasterKeySpec = None,
    Origin: OriginType = None,
    CustomKeyStoreId: str = None,
    BypassPolicyLockoutSafetyCheck: bool = None,
    Tags: List["TagTypeDef"] = None
) -> CreateKeyResponseTypeDef:
    pass
```

### decrypt

Type annotations for `boto3.client("kms").decrypt` method.

[Client.decrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.decrypt)

```python
def decrypt(
    self,
    CiphertextBlob: Union[bytes, IO[bytes]],
    EncryptionContext: Dict[str, str] = None,
    GrantTokens: List[str] = None,
    KeyId: str = None,
    EncryptionAlgorithm: EncryptionAlgorithmSpec = None
) -> DecryptResponseTypeDef:
    pass
```

### delete_alias

Type annotations for `boto3.client("kms").delete_alias` method.

[Client.delete_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.delete_alias)

```python
def delete_alias(
    self,
    AliasName: str
) -> None:
    pass
```

### delete_custom_key_store

Type annotations for `boto3.client("kms").delete_custom_key_store` method.

[Client.delete_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.delete_custom_key_store)

```python
def delete_custom_key_store(
    self,
    CustomKeyStoreId: str
) -> Dict[str, Any]:
    pass
```

### delete_imported_key_material

Type annotations for `boto3.client("kms").delete_imported_key_material` method.

[Client.delete_imported_key_material documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.delete_imported_key_material)

```python
def delete_imported_key_material(
    self,
    KeyId: str
) -> None:
    pass
```

### describe_custom_key_stores

Type annotations for `boto3.client("kms").describe_custom_key_stores` method.

[Client.describe_custom_key_stores documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.describe_custom_key_stores)

```python
def describe_custom_key_stores(
    self,
    CustomKeyStoreId: str = None,
    CustomKeyStoreName: str = None,
    Limit: int = None,
    Marker: str = None
) -> DescribeCustomKeyStoresResponseTypeDef:
    pass
```

### describe_key

Type annotations for `boto3.client("kms").describe_key` method.

[Client.describe_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.describe_key)

```python
def describe_key(
    self,
    KeyId: str,
    GrantTokens: List[str] = None
) -> DescribeKeyResponseTypeDef:
    pass
```

### disable_key

Type annotations for `boto3.client("kms").disable_key` method.

[Client.disable_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.disable_key)

```python
def disable_key(
    self,
    KeyId: str
) -> None:
    pass
```

### disable_key_rotation

Type annotations for `boto3.client("kms").disable_key_rotation` method.

[Client.disable_key_rotation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.disable_key_rotation)

```python
def disable_key_rotation(
    self,
    KeyId: str
) -> None:
    pass
```

### disconnect_custom_key_store

Type annotations for `boto3.client("kms").disconnect_custom_key_store` method.

[Client.disconnect_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.disconnect_custom_key_store)

```python
def disconnect_custom_key_store(
    self,
    CustomKeyStoreId: str
) -> Dict[str, Any]:
    pass
```

### enable_key

Type annotations for `boto3.client("kms").enable_key` method.

[Client.enable_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.enable_key)

```python
def enable_key(
    self,
    KeyId: str
) -> None:
    pass
```

### enable_key_rotation

Type annotations for `boto3.client("kms").enable_key_rotation` method.

[Client.enable_key_rotation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.enable_key_rotation)

```python
def enable_key_rotation(
    self,
    KeyId: str
) -> None:
    pass
```

### encrypt

Type annotations for `boto3.client("kms").encrypt` method.

[Client.encrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.encrypt)

```python
def encrypt(
    self,
    KeyId: str,
    Plaintext: Union[bytes, IO[bytes]],
    EncryptionContext: Dict[str, str] = None,
    GrantTokens: List[str] = None,
    EncryptionAlgorithm: EncryptionAlgorithmSpec = None
) -> EncryptResponseTypeDef:
    pass
```

### generate_data_key

Type annotations for `boto3.client("kms").generate_data_key` method.

[Client.generate_data_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.generate_data_key)

```python
def generate_data_key(
    self,
    KeyId: str,
    EncryptionContext: Dict[str, str] = None,
    NumberOfBytes: int = None,
    KeySpec: DataKeySpec = None,
    GrantTokens: List[str] = None
) -> GenerateDataKeyResponseTypeDef:
    pass
```

### generate_data_key_pair

Type annotations for `boto3.client("kms").generate_data_key_pair` method.

[Client.generate_data_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.generate_data_key_pair)

```python
def generate_data_key_pair(
    self,
    KeyId: str,
    KeyPairSpec: DataKeyPairSpec,
    EncryptionContext: Dict[str, str] = None,
    GrantTokens: List[str] = None
) -> GenerateDataKeyPairResponseTypeDef:
    pass
```

### generate_data_key_pair_without_plaintext

Type annotations for `boto3.client("kms").generate_data_key_pair_without_plaintext` method.

[Client.generate_data_key_pair_without_plaintext documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.generate_data_key_pair_without_plaintext)

```python
def generate_data_key_pair_without_plaintext(
    self,
    KeyId: str,
    KeyPairSpec: DataKeyPairSpec,
    EncryptionContext: Dict[str, str] = None,
    GrantTokens: List[str] = None
) -> GenerateDataKeyPairWithoutPlaintextResponseTypeDef:
    pass
```

### generate_data_key_without_plaintext

Type annotations for `boto3.client("kms").generate_data_key_without_plaintext` method.

[Client.generate_data_key_without_plaintext documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.generate_data_key_without_plaintext)

```python
def generate_data_key_without_plaintext(
    self,
    KeyId: str,
    EncryptionContext: Dict[str, str] = None,
    KeySpec: DataKeySpec = None,
    NumberOfBytes: int = None,
    GrantTokens: List[str] = None
) -> GenerateDataKeyWithoutPlaintextResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kms").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.generate_presigned_url)

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

### generate_random

Type annotations for `boto3.client("kms").generate_random` method.

[Client.generate_random documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.generate_random)

```python
def generate_random(
    self,
    NumberOfBytes: int = None,
    CustomKeyStoreId: str = None
) -> GenerateRandomResponseTypeDef:
    pass
```

### get_key_policy

Type annotations for `boto3.client("kms").get_key_policy` method.

[Client.get_key_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.get_key_policy)

```python
def get_key_policy(
    self,
    KeyId: str,
    PolicyName: str
) -> GetKeyPolicyResponseTypeDef:
    pass
```

### get_key_rotation_status

Type annotations for `boto3.client("kms").get_key_rotation_status` method.

[Client.get_key_rotation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.get_key_rotation_status)

```python
def get_key_rotation_status(
    self,
    KeyId: str
) -> GetKeyRotationStatusResponseTypeDef:
    pass
```

### get_parameters_for_import

Type annotations for `boto3.client("kms").get_parameters_for_import` method.

[Client.get_parameters_for_import documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.get_parameters_for_import)

```python
def get_parameters_for_import(
    self,
    KeyId: str,
    WrappingAlgorithm: AlgorithmSpec,
    WrappingKeySpec: Literal['RSA_2048']
) -> GetParametersForImportResponseTypeDef:
    pass
```

### get_public_key

Type annotations for `boto3.client("kms").get_public_key` method.

[Client.get_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.get_public_key)

```python
def get_public_key(
    self,
    KeyId: str,
    GrantTokens: List[str] = None
) -> GetPublicKeyResponseTypeDef:
    pass
```

### import_key_material

Type annotations for `boto3.client("kms").import_key_material` method.

[Client.import_key_material documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.import_key_material)

```python
def import_key_material(
    self,
    KeyId: str,
    ImportToken: Union[bytes, IO[bytes]],
    EncryptedKeyMaterial: Union[bytes, IO[bytes]],
    ValidTo: datetime = None,
    ExpirationModel: ExpirationModelType = None
) -> Dict[str, Any]:
    pass
```

### list_aliases

Type annotations for `boto3.client("kms").list_aliases` method.

[Client.list_aliases documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.list_aliases)

```python
def list_aliases(
    self,
    KeyId: str = None,
    Limit: int = None,
    Marker: str = None
) -> ListAliasesResponseTypeDef:
    pass
```

### list_grants

Type annotations for `boto3.client("kms").list_grants` method.

[Client.list_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.list_grants)

```python
def list_grants(
    self,
    KeyId: str,
    Limit: int = None,
    Marker: str = None,
    GrantId: str = None,
    GranteePrincipal: str = None
) -> ListGrantsResponseTypeDef:
    pass
```

### list_key_policies

Type annotations for `boto3.client("kms").list_key_policies` method.

[Client.list_key_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.list_key_policies)

```python
def list_key_policies(
    self,
    KeyId: str,
    Limit: int = None,
    Marker: str = None
) -> ListKeyPoliciesResponseTypeDef:
    pass
```

### list_keys

Type annotations for `boto3.client("kms").list_keys` method.

[Client.list_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.list_keys)

```python
def list_keys(
    self,
    Limit: int = None,
    Marker: str = None
) -> ListKeysResponseTypeDef:
    pass
```

### list_resource_tags

Type annotations for `boto3.client("kms").list_resource_tags` method.

[Client.list_resource_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.list_resource_tags)

```python
def list_resource_tags(
    self,
    KeyId: str,
    Limit: int = None,
    Marker: str = None
) -> ListResourceTagsResponseTypeDef:
    pass
```

### list_retirable_grants

Type annotations for `boto3.client("kms").list_retirable_grants` method.

[Client.list_retirable_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.list_retirable_grants)

```python
def list_retirable_grants(
    self,
    RetiringPrincipal: str,
    Limit: int = None,
    Marker: str = None
) -> ListGrantsResponseTypeDef:
    pass
```

### put_key_policy

Type annotations for `boto3.client("kms").put_key_policy` method.

[Client.put_key_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.put_key_policy)

```python
def put_key_policy(
    self,
    KeyId: str,
    PolicyName: str,
    Policy: str,
    BypassPolicyLockoutSafetyCheck: bool = None
) -> None:
    pass
```

### re_encrypt

Type annotations for `boto3.client("kms").re_encrypt` method.

[Client.re_encrypt documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.re_encrypt)

```python
def re_encrypt(
    self,
    CiphertextBlob: Union[bytes, IO[bytes]],
    DestinationKeyId: str,
    SourceEncryptionContext: Dict[str, str] = None,
    SourceKeyId: str = None,
    DestinationEncryptionContext: Dict[str, str] = None,
    SourceEncryptionAlgorithm: EncryptionAlgorithmSpec = None,
    DestinationEncryptionAlgorithm: EncryptionAlgorithmSpec = None,
    GrantTokens: List[str] = None
) -> ReEncryptResponseTypeDef:
    pass
```

### retire_grant

Type annotations for `boto3.client("kms").retire_grant` method.

[Client.retire_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.retire_grant)

```python
def retire_grant(
    self,
    GrantToken: str = None,
    KeyId: str = None,
    GrantId: str = None
) -> None:
    pass
```

### revoke_grant

Type annotations for `boto3.client("kms").revoke_grant` method.

[Client.revoke_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.revoke_grant)

```python
def revoke_grant(
    self,
    KeyId: str,
    GrantId: str
) -> None:
    pass
```

### schedule_key_deletion

Type annotations for `boto3.client("kms").schedule_key_deletion` method.

[Client.schedule_key_deletion documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.schedule_key_deletion)

```python
def schedule_key_deletion(
    self,
    KeyId: str,
    PendingWindowInDays: int = None
) -> ScheduleKeyDeletionResponseTypeDef:
    pass
```

### sign

Type annotations for `boto3.client("kms").sign` method.

[Client.sign documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.sign)

```python
def sign(
    self,
    KeyId: str,
    Message: Union[bytes, IO[bytes]],
    SigningAlgorithm: SigningAlgorithmSpec,
    MessageType: MessageType = None,
    GrantTokens: List[str] = None
) -> SignResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("kms").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.tag_resource)

```python
def tag_resource(
    self,
    KeyId: str,
    Tags: List["TagTypeDef"]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("kms").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.untag_resource)

```python
def untag_resource(
    self,
    KeyId: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_alias

Type annotations for `boto3.client("kms").update_alias` method.

[Client.update_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.update_alias)

```python
def update_alias(
    self,
    AliasName: str,
    TargetKeyId: str
) -> None:
    pass
```

### update_custom_key_store

Type annotations for `boto3.client("kms").update_custom_key_store` method.

[Client.update_custom_key_store documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.update_custom_key_store)

```python
def update_custom_key_store(
    self,
    CustomKeyStoreId: str,
    NewCustomKeyStoreName: str = None,
    KeyStorePassword: str = None,
    CloudHsmClusterId: str = None
) -> Dict[str, Any]:
    pass
```

### update_key_description

Type annotations for `boto3.client("kms").update_key_description` method.

[Client.update_key_description documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.update_key_description)

```python
def update_key_description(
    self,
    KeyId: str,
    Description: str
) -> None:
    pass
```

### verify

Type annotations for `boto3.client("kms").verify` method.

[Client.verify documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS.Client.verify)

```python
def verify(
    self,
    KeyId: str,
    Message: Union[bytes, IO[bytes]],
    Signature: Union[bytes, IO[bytes]],
    SigningAlgorithm: SigningAlgorithmSpec,
    MessageType: MessageType = None,
    GrantTokens: List[str] = None
) -> VerifyResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("kms").get_paginator` method with overloads.

- `client.get_paginator("list_aliases")` -> [ListAliasesPaginator](./paginators.md#listaliasespaginator)
- `client.get_paginator("list_grants")` -> [ListGrantsPaginator](./paginators.md#listgrantspaginator)
- `client.get_paginator("list_key_policies")` -> [ListKeyPoliciesPaginator](./paginators.md#listkeypoliciespaginator)
- `client.get_paginator("list_keys")` -> [ListKeysPaginator](./paginators.md#listkeyspaginator)


