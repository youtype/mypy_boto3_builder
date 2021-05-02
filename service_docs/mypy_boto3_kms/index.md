# Type annotations for boto3 KMS module

> [Index](../index.md) > KMS

Auto-generated documentation for [KMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#KMS)
type annotations stubs module [mypy_boto3_kms](https://pypi.org/project/mypy-boto3-kms/).

```bash
pip install mypy-boto3-kms
```

- [Type annotations for boto3 KMS module](#type-annotations-for-boto3-kms-module)
  - [KMSClient](#kmsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## KMSClient

Type annotations for  `boto3.client("kms")` as [KMSClient](./client.md)

Can be used directly:

```python
from mypy_boto3_kms.client import KMSClient
```


KMSClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_key_deletion](./client.md#cancel-key-deletion)
- [connect_custom_key_store](./client.md#connect-custom-key-store)
- [create_alias](./client.md#create-alias)
- [create_custom_key_store](./client.md#create-custom-key-store)
- [create_grant](./client.md#create-grant)
- [create_key](./client.md#create-key)
- [decrypt](./client.md#decrypt)
- [delete_alias](./client.md#delete-alias)
- [delete_custom_key_store](./client.md#delete-custom-key-store)
- [delete_imported_key_material](./client.md#delete-imported-key-material)
- [describe_custom_key_stores](./client.md#describe-custom-key-stores)
- [describe_key](./client.md#describe-key)
- [disable_key](./client.md#disable-key)
- [disable_key_rotation](./client.md#disable-key-rotation)
- [disconnect_custom_key_store](./client.md#disconnect-custom-key-store)
- [enable_key](./client.md#enable-key)
- [enable_key_rotation](./client.md#enable-key-rotation)
- [encrypt](./client.md#encrypt)
- [generate_data_key](./client.md#generate-data-key)
- [generate_data_key_pair](./client.md#generate-data-key-pair)
- [generate_data_key_pair_without_plaintext](./client.md#generate-data-key-pair-without-plaintext)
- [generate_data_key_without_plaintext](./client.md#generate-data-key-without-plaintext)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [generate_random](./client.md#generate-random)
- [get_key_policy](./client.md#get-key-policy)
- [get_key_rotation_status](./client.md#get-key-rotation-status)
- [get_paginator](./client.md#get-paginator)
- [get_parameters_for_import](./client.md#get-parameters-for-import)
- [get_public_key](./client.md#get-public-key)
- [import_key_material](./client.md#import-key-material)
- [list_aliases](./client.md#list-aliases)
- [list_grants](./client.md#list-grants)
- [list_key_policies](./client.md#list-key-policies)
- [list_keys](./client.md#list-keys)
- [list_resource_tags](./client.md#list-resource-tags)
- [list_retirable_grants](./client.md#list-retirable-grants)
- [put_key_policy](./client.md#put-key-policy)
- [re_encrypt](./client.md#re-encrypt)
- [retire_grant](./client.md#retire-grant)
- [revoke_grant](./client.md#revoke-grant)
- [schedule_key_deletion](./client.md#schedule-key-deletion)
- [sign](./client.md#sign)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_alias](./client.md#update-alias)
- [update_custom_key_store](./client.md#update-custom-key-store)
- [update_key_description](./client.md#update-key-description)
- [verify](./client.md#verify)




### Exceptions
- [AlreadyExistsException](./client.md#alreadyexistsexception)
- [ClientError](./client.md#clienterror)
- [CloudHsmClusterInUseException](./client.md#cloudhsmclusterinuseexception)
- [CloudHsmClusterInvalidConfigurationException](./client.md#cloudhsmclusterinvalidconfigurationexception)
- [CloudHsmClusterNotActiveException](./client.md#cloudhsmclusternotactiveexception)
- [CloudHsmClusterNotFoundException](./client.md#cloudhsmclusternotfoundexception)
- [CloudHsmClusterNotRelatedException](./client.md#cloudhsmclusternotrelatedexception)
- [CustomKeyStoreHasCMKsException](./client.md#customkeystorehascmksexception)
- [CustomKeyStoreInvalidStateException](./client.md#customkeystoreinvalidstateexception)
- [CustomKeyStoreNameInUseException](./client.md#customkeystorenameinuseexception)
- [CustomKeyStoreNotFoundException](./client.md#customkeystorenotfoundexception)
- [DependencyTimeoutException](./client.md#dependencytimeoutexception)
- [DisabledException](./client.md#disabledexception)
- [ExpiredImportTokenException](./client.md#expiredimporttokenexception)
- [IncorrectKeyException](./client.md#incorrectkeyexception)
- [IncorrectKeyMaterialException](./client.md#incorrectkeymaterialexception)
- [IncorrectTrustAnchorException](./client.md#incorrecttrustanchorexception)
- [InvalidAliasNameException](./client.md#invalidaliasnameexception)
- [InvalidArnException](./client.md#invalidarnexception)
- [InvalidCiphertextException](./client.md#invalidciphertextexception)
- [InvalidGrantIdException](./client.md#invalidgrantidexception)
- [InvalidGrantTokenException](./client.md#invalidgranttokenexception)
- [InvalidImportTokenException](./client.md#invalidimporttokenexception)
- [InvalidKeyUsageException](./client.md#invalidkeyusageexception)
- [InvalidMarkerException](./client.md#invalidmarkerexception)
- [KMSInternalException](./client.md#kmsinternalexception)
- [KMSInvalidSignatureException](./client.md#kmsinvalidsignatureexception)
- [KMSInvalidStateException](./client.md#kmsinvalidstateexception)
- [KeyUnavailableException](./client.md#keyunavailableexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [MalformedPolicyDocumentException](./client.md#malformedpolicydocumentexception)
- [NotFoundException](./client.md#notfoundexception)
- [TagException](./client.md#tagexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("kms").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_kms.paginators import ListAliasesPaginator, ...
```

- [ListAliasesPaginator](./paginators.md#listaliasespaginator)
- [ListGrantsPaginator](./paginators.md#listgrantspaginator)
- [ListKeyPoliciesPaginator](./paginators.md#listkeypoliciespaginator)
- [ListKeysPaginator](./paginators.md#listkeyspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kms.literals import AlgorithmSpec, ...
```

- [AlgorithmSpec](./literals.md#algorithmspec)
- [ConnectionErrorCodeType](./literals.md#connectionerrorcodetype)
- [ConnectionStateType](./literals.md#connectionstatetype)
- [CustomerMasterKeySpec](./literals.md#customermasterkeyspec)
- [DataKeyPairSpec](./literals.md#datakeypairspec)
- [DataKeySpec](./literals.md#datakeyspec)
- [EncryptionAlgorithmSpec](./literals.md#encryptionalgorithmspec)
- [ExpirationModelType](./literals.md#expirationmodeltype)
- [GrantOperation](./literals.md#grantoperation)
- [KeyManagerType](./literals.md#keymanagertype)
- [KeyState](./literals.md#keystate)
- [KeyUsageType](./literals.md#keyusagetype)
- [ListAliasesPaginatorName](./literals.md#listaliasespaginatorname)
- [ListGrantsPaginatorName](./literals.md#listgrantspaginatorname)
- [ListKeyPoliciesPaginatorName](./literals.md#listkeypoliciespaginatorname)
- [ListKeysPaginatorName](./literals.md#listkeyspaginatorname)
- [MessageType](./literals.md#messagetype)
- [OriginType](./literals.md#origintype)
- [SigningAlgorithmSpec](./literals.md#signingalgorithmspec)
- [WrappingKeySpec](./literals.md#wrappingkeyspec)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_kms.type_defs import AliasListEntryTypeDef, ...
```

- [AliasListEntryTypeDef](./type_defs.md#aliaslistentrytypedef)
- [CustomKeyStoresListEntryTypeDef](./type_defs.md#customkeystoreslistentrytypedef)
- [GrantConstraintsTypeDef](./type_defs.md#grantconstraintstypedef)
- [GrantListEntryTypeDef](./type_defs.md#grantlistentrytypedef)
- [KeyListEntryTypeDef](./type_defs.md#keylistentrytypedef)
- [KeyMetadataTypeDef](./type_defs.md#keymetadatatypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CancelKeyDeletionResponseTypeDef](./type_defs.md#cancelkeydeletionresponsetypedef)
- [CreateCustomKeyStoreResponseTypeDef](./type_defs.md#createcustomkeystoreresponsetypedef)
- [CreateGrantResponseTypeDef](./type_defs.md#creategrantresponsetypedef)
- [CreateKeyResponseTypeDef](./type_defs.md#createkeyresponsetypedef)
- [DecryptResponseTypeDef](./type_defs.md#decryptresponsetypedef)
- [DescribeCustomKeyStoresResponseTypeDef](./type_defs.md#describecustomkeystoresresponsetypedef)
- [DescribeKeyResponseTypeDef](./type_defs.md#describekeyresponsetypedef)
- [EncryptResponseTypeDef](./type_defs.md#encryptresponsetypedef)
- [GenerateDataKeyPairResponseTypeDef](./type_defs.md#generatedatakeypairresponsetypedef)
- [GenerateDataKeyPairWithoutPlaintextResponseTypeDef](./type_defs.md#generatedatakeypairwithoutplaintextresponsetypedef)
- [GenerateDataKeyResponseTypeDef](./type_defs.md#generatedatakeyresponsetypedef)
- [GenerateDataKeyWithoutPlaintextResponseTypeDef](./type_defs.md#generatedatakeywithoutplaintextresponsetypedef)
- [GenerateRandomResponseTypeDef](./type_defs.md#generaterandomresponsetypedef)
- [GetKeyPolicyResponseTypeDef](./type_defs.md#getkeypolicyresponsetypedef)
- [GetKeyRotationStatusResponseTypeDef](./type_defs.md#getkeyrotationstatusresponsetypedef)
- [GetParametersForImportResponseTypeDef](./type_defs.md#getparametersforimportresponsetypedef)
- [GetPublicKeyResponseTypeDef](./type_defs.md#getpublickeyresponsetypedef)
- [ListAliasesResponseTypeDef](./type_defs.md#listaliasesresponsetypedef)
- [ListGrantsResponseTypeDef](./type_defs.md#listgrantsresponsetypedef)
- [ListKeyPoliciesResponseTypeDef](./type_defs.md#listkeypoliciesresponsetypedef)
- [ListKeysResponseTypeDef](./type_defs.md#listkeysresponsetypedef)
- [ListResourceTagsResponseTypeDef](./type_defs.md#listresourcetagsresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ReEncryptResponseTypeDef](./type_defs.md#reencryptresponsetypedef)
- [ScheduleKeyDeletionResponseTypeDef](./type_defs.md#schedulekeydeletionresponsetypedef)
- [SignResponseTypeDef](./type_defs.md#signresponsetypedef)
- [VerifyResponseTypeDef](./type_defs.md#verifyresponsetypedef)
