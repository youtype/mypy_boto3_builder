# Literals for boto3 KMS module

> [Index](../index.md) > [KMS](./index.md) > Literals

Auto-generated documentation for [KMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS)
type annotations stubs module [mypy_boto3_kms](https://pypi.org/project/mypy-boto3-kms/).

- [Literals for boto3 KMS module](#literals-for-boto3-kms-module)
  - [AlgorithmSpec](#algorithmspec)
  - [ConnectionErrorCodeType](#connectionerrorcodetype)
  - [ConnectionStateType](#connectionstatetype)
  - [CustomerMasterKeySpec](#customermasterkeyspec)
  - [DataKeyPairSpec](#datakeypairspec)
  - [DataKeySpec](#datakeyspec)
  - [EncryptionAlgorithmSpec](#encryptionalgorithmspec)
  - [ExpirationModelType](#expirationmodeltype)
  - [GrantOperation](#grantoperation)
  - [KeyManagerType](#keymanagertype)
  - [KeyState](#keystate)
  - [KeyUsageType](#keyusagetype)
  - [ListAliasesPaginatorName](#listaliasespaginatorname)
  - [ListGrantsPaginatorName](#listgrantspaginatorname)
  - [ListKeyPoliciesPaginatorName](#listkeypoliciespaginatorname)
  - [ListKeysPaginatorName](#listkeyspaginatorname)
  - [MessageType](#messagetype)
  - [OriginType](#origintype)
  - [SigningAlgorithmSpec](#signingalgorithmspec)
  - [WrappingKeySpec](#wrappingkeyspec)

## AlgorithmSpec

```python
from mypy_boto3_kms.literals import AlgorithmSpec
```

Values:

- `RSAES_OAEP_SHA_1`
- `RSAES_OAEP_SHA_256`
- `RSAES_PKCS1_V1_5`

## ConnectionErrorCodeType

```python
from mypy_boto3_kms.literals import ConnectionErrorCodeType
```

Values:

- `CLUSTER_NOT_FOUND`
- `INSUFFICIENT_CLOUDHSM_HSMS`
- `INTERNAL_ERROR`
- `INVALID_CREDENTIALS`
- `NETWORK_ERRORS`
- `SUBNET_NOT_FOUND`
- `USER_LOCKED_OUT`
- `USER_LOGGED_IN`
- `USER_NOT_FOUND`

## ConnectionStateType

```python
from mypy_boto3_kms.literals import ConnectionStateType
```

Values:

- `CONNECTED`
- `CONNECTING`
- `DISCONNECTED`
- `DISCONNECTING`
- `FAILED`

## CustomerMasterKeySpec

```python
from mypy_boto3_kms.literals import CustomerMasterKeySpec
```

Values:

- `ECC_NIST_P256`
- `ECC_NIST_P384`
- `ECC_NIST_P521`
- `ECC_SECG_P256K1`
- `RSA_2048`
- `RSA_3072`
- `RSA_4096`
- `SYMMETRIC_DEFAULT`

## DataKeyPairSpec

```python
from mypy_boto3_kms.literals import DataKeyPairSpec
```

Values:

- `ECC_NIST_P256`
- `ECC_NIST_P384`
- `ECC_NIST_P521`
- `ECC_SECG_P256K1`
- `RSA_2048`
- `RSA_3072`
- `RSA_4096`

## DataKeySpec

```python
from mypy_boto3_kms.literals import DataKeySpec
```

Values:

- `AES_128`
- `AES_256`

## EncryptionAlgorithmSpec

```python
from mypy_boto3_kms.literals import EncryptionAlgorithmSpec
```

Values:

- `RSAES_OAEP_SHA_1`
- `RSAES_OAEP_SHA_256`
- `SYMMETRIC_DEFAULT`

## ExpirationModelType

```python
from mypy_boto3_kms.literals import ExpirationModelType
```

Values:

- `KEY_MATERIAL_DOES_NOT_EXPIRE`
- `KEY_MATERIAL_EXPIRES`

## GrantOperation

```python
from mypy_boto3_kms.literals import GrantOperation
```

Values:

- `CreateGrant`
- `Decrypt`
- `DescribeKey`
- `Encrypt`
- `GenerateDataKey`
- `GenerateDataKeyPair`
- `GenerateDataKeyPairWithoutPlaintext`
- `GenerateDataKeyWithoutPlaintext`
- `GetPublicKey`
- `ReEncryptFrom`
- `ReEncryptTo`
- `RetireGrant`
- `Sign`
- `Verify`

## KeyManagerType

```python
from mypy_boto3_kms.literals import KeyManagerType
```

Values:

- `AWS`
- `CUSTOMER`

## KeyState

```python
from mypy_boto3_kms.literals import KeyState
```

Values:

- `Disabled`
- `Enabled`
- `PendingDeletion`
- `PendingImport`
- `Unavailable`

## KeyUsageType

```python
from mypy_boto3_kms.literals import KeyUsageType
```

Values:

- `ENCRYPT_DECRYPT`
- `SIGN_VERIFY`

## ListAliasesPaginatorName

```python
from mypy_boto3_kms.literals import ListAliasesPaginatorName
```

Values:

- `list_aliases`

## ListGrantsPaginatorName

```python
from mypy_boto3_kms.literals import ListGrantsPaginatorName
```

Values:

- `list_grants`

## ListKeyPoliciesPaginatorName

```python
from mypy_boto3_kms.literals import ListKeyPoliciesPaginatorName
```

Values:

- `list_key_policies`

## ListKeysPaginatorName

```python
from mypy_boto3_kms.literals import ListKeysPaginatorName
```

Values:

- `list_keys`

## MessageType

```python
from mypy_boto3_kms.literals import MessageType
```

Values:

- `DIGEST`
- `RAW`

## OriginType

```python
from mypy_boto3_kms.literals import OriginType
```

Values:

- `AWS_CLOUDHSM`
- `AWS_KMS`
- `EXTERNAL`

## SigningAlgorithmSpec

```python
from mypy_boto3_kms.literals import SigningAlgorithmSpec
```

Values:

- `ECDSA_SHA_256`
- `ECDSA_SHA_384`
- `ECDSA_SHA_512`
- `RSASSA_PKCS1_V1_5_SHA_256`
- `RSASSA_PKCS1_V1_5_SHA_384`
- `RSASSA_PKCS1_V1_5_SHA_512`
- `RSASSA_PSS_SHA_256`
- `RSASSA_PSS_SHA_384`
- `RSASSA_PSS_SHA_512`

## WrappingKeySpec

```python
from mypy_boto3_kms.literals import WrappingKeySpec
```

Values:

- `RSA_2048`
