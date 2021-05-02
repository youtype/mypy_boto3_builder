# Type annotations for boto3 CloudHSM module

> [Index](../index.md) > CloudHSM

Auto-generated documentation for [CloudHSM](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html#CloudHSM)
type annotations stubs module [mypy_boto3_cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm/).

```bash
pip install mypy-boto3-cloudhsm
```

- [Type annotations for boto3 CloudHSM module](#type-annotations-for-boto3-cloudhsm-module)
  - [CloudHSMClient](#cloudhsmclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## CloudHSMClient

Type annotations for  `boto3.client("cloudhsm")` as [CloudHSMClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cloudhsm.client import CloudHSMClient
```


CloudHSMClient [exceptions](./client.md#exceptions)



### Methods
- [add_tags_to_resource](./client.md#add-tags-to-resource)
- [can_paginate](./client.md#can-paginate)
- [create_hapg](./client.md#create-hapg)
- [create_hsm](./client.md#create-hsm)
- [create_luna_client](./client.md#create-luna-client)
- [delete_hapg](./client.md#delete-hapg)
- [delete_hsm](./client.md#delete-hsm)
- [delete_luna_client](./client.md#delete-luna-client)
- [describe_hapg](./client.md#describe-hapg)
- [describe_hsm](./client.md#describe-hsm)
- [describe_luna_client](./client.md#describe-luna-client)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_config](./client.md#get-config)
- [get_paginator](./client.md#get-paginator)
- [list_available_zones](./client.md#list-available-zones)
- [list_hapgs](./client.md#list-hapgs)
- [list_hsms](./client.md#list-hsms)
- [list_luna_clients](./client.md#list-luna-clients)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [modify_hapg](./client.md#modify-hapg)
- [modify_hsm](./client.md#modify-hsm)
- [modify_luna_client](./client.md#modify-luna-client)
- [remove_tags_from_resource](./client.md#remove-tags-from-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [CloudHsmInternalException](./client.md#cloudhsminternalexception)
- [CloudHsmServiceException](./client.md#cloudhsmserviceexception)
- [InvalidRequestException](./client.md#invalidrequestexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("cloudhsm").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_cloudhsm.paginators import ListHapgsPaginator, ...
```

- [ListHapgsPaginator](./paginators.md#listhapgspaginator)
- [ListHsmsPaginator](./paginators.md#listhsmspaginator)
- [ListLunaClientsPaginator](./paginators.md#listlunaclientspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudhsm.literals import ClientVersion, ...
```

- [ClientVersion](./literals.md#clientversion)
- [CloudHsmObjectState](./literals.md#cloudhsmobjectstate)
- [HsmStatus](./literals.md#hsmstatus)
- [ListHapgsPaginatorName](./literals.md#listhapgspaginatorname)
- [ListHsmsPaginatorName](./literals.md#listhsmspaginatorname)
- [ListLunaClientsPaginatorName](./literals.md#listlunaclientspaginatorname)
- [SubscriptionType](./literals.md#subscriptiontype)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cloudhsm.type_defs import AddTagsToResourceResponseTypeDef, ...
```

- [AddTagsToResourceResponseTypeDef](./type_defs.md#addtagstoresourceresponsetypedef)
- [CreateHapgResponseTypeDef](./type_defs.md#createhapgresponsetypedef)
- [CreateHsmResponseTypeDef](./type_defs.md#createhsmresponsetypedef)
- [CreateLunaClientResponseTypeDef](./type_defs.md#createlunaclientresponsetypedef)
- [DeleteHapgResponseTypeDef](./type_defs.md#deletehapgresponsetypedef)
- [DeleteHsmResponseTypeDef](./type_defs.md#deletehsmresponsetypedef)
- [DeleteLunaClientResponseTypeDef](./type_defs.md#deletelunaclientresponsetypedef)
- [DescribeHapgResponseTypeDef](./type_defs.md#describehapgresponsetypedef)
- [DescribeHsmResponseTypeDef](./type_defs.md#describehsmresponsetypedef)
- [DescribeLunaClientResponseTypeDef](./type_defs.md#describelunaclientresponsetypedef)
- [GetConfigResponseTypeDef](./type_defs.md#getconfigresponsetypedef)
- [ListAvailableZonesResponseTypeDef](./type_defs.md#listavailablezonesresponsetypedef)
- [ListHapgsResponseTypeDef](./type_defs.md#listhapgsresponsetypedef)
- [ListHsmsResponseTypeDef](./type_defs.md#listhsmsresponsetypedef)
- [ListLunaClientsResponseTypeDef](./type_defs.md#listlunaclientsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [ModifyHapgResponseTypeDef](./type_defs.md#modifyhapgresponsetypedef)
- [ModifyHsmResponseTypeDef](./type_defs.md#modifyhsmresponsetypedef)
- [ModifyLunaClientResponseTypeDef](./type_defs.md#modifylunaclientresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [RemoveTagsFromResourceResponseTypeDef](./type_defs.md#removetagsfromresourceresponsetypedef)
- [TagTypeDef](./type_defs.md#tagtypedef)
