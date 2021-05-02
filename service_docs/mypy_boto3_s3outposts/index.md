# Type annotations for boto3 S3Outposts module

> [Index](../index.md) > S3Outposts

Auto-generated documentation for [S3Outposts](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html#S3Outposts)
type annotations stubs module [mypy_boto3_s3outposts](https://pypi.org/project/mypy-boto3-s3outposts/).

```bash
pip install mypy-boto3-s3outposts
```

- [Type annotations for boto3 S3Outposts module](#type-annotations-for-boto3-s3outposts-module)
  - [S3OutpostsClient](#s3outpostsclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## S3OutpostsClient

Type annotations for  `boto3.client("s3outposts")` as [S3OutpostsClient](./client.md)

Can be used directly:

```python
from mypy_boto3_s3outposts.client import S3OutpostsClient
```


S3OutpostsClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_endpoint](./client.md#create-endpoint)
- [delete_endpoint](./client.md#delete-endpoint)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_endpoints](./client.md#list-endpoints)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("s3outposts").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_s3outposts.paginators import ListEndpointsPaginator, ...
```

- [ListEndpointsPaginator](./paginators.md#listendpointspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_s3outposts.literals import EndpointStatus, ...
```

- [EndpointStatus](./literals.md#endpointstatus)
- [ListEndpointsPaginatorName](./literals.md#listendpointspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_s3outposts.type_defs import EndpointTypeDef, ...
```

- [EndpointTypeDef](./type_defs.md#endpointtypedef)
- [NetworkInterfaceTypeDef](./type_defs.md#networkinterfacetypedef)
- [CreateEndpointResultTypeDef](./type_defs.md#createendpointresulttypedef)
- [ListEndpointsResultTypeDef](./type_defs.md#listendpointsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
