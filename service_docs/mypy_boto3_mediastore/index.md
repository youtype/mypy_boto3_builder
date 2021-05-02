# Type annotations for boto3 MediaStore module

> [Index](../index.md) > MediaStore

Auto-generated documentation for [MediaStore](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html#MediaStore)
type annotations stubs module [mypy_boto3_mediastore](https://pypi.org/project/mypy-boto3-mediastore/).

```bash
pip install mypy-boto3-mediastore
```

- [Type annotations for boto3 MediaStore module](#type-annotations-for-boto3-mediastore-module)
  - [MediaStoreClient](#mediastoreclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MediaStoreClient

Type annotations for  `boto3.client("mediastore")` as [MediaStoreClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mediastore.client import MediaStoreClient
```


MediaStoreClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_container](./client.md#create-container)
- [delete_container](./client.md#delete-container)
- [delete_container_policy](./client.md#delete-container-policy)
- [delete_cors_policy](./client.md#delete-cors-policy)
- [delete_lifecycle_policy](./client.md#delete-lifecycle-policy)
- [delete_metric_policy](./client.md#delete-metric-policy)
- [describe_container](./client.md#describe-container)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_container_policy](./client.md#get-container-policy)
- [get_cors_policy](./client.md#get-cors-policy)
- [get_lifecycle_policy](./client.md#get-lifecycle-policy)
- [get_metric_policy](./client.md#get-metric-policy)
- [get_paginator](./client.md#get-paginator)
- [list_containers](./client.md#list-containers)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [put_container_policy](./client.md#put-container-policy)
- [put_cors_policy](./client.md#put-cors-policy)
- [put_lifecycle_policy](./client.md#put-lifecycle-policy)
- [put_metric_policy](./client.md#put-metric-policy)
- [start_access_logging](./client.md#start-access-logging)
- [stop_access_logging](./client.md#stop-access-logging)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ContainerInUseException](./client.md#containerinuseexception)
- [ContainerNotFoundException](./client.md#containernotfoundexception)
- [CorsPolicyNotFoundException](./client.md#corspolicynotfoundexception)
- [InternalServerError](./client.md#internalservererror)
- [LimitExceededException](./client.md#limitexceededexception)
- [PolicyNotFoundException](./client.md#policynotfoundexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mediastore").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mediastore.paginators import ListContainersPaginator, ...
```

- [ListContainersPaginator](./paginators.md#listcontainerspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediastore.literals import ContainerLevelMetrics, ...
```

- [ContainerLevelMetrics](./literals.md#containerlevelmetrics)
- [ContainerStatus](./literals.md#containerstatus)
- [ListContainersPaginatorName](./literals.md#listcontainerspaginatorname)
- [MethodName](./literals.md#methodname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mediastore.type_defs import ContainerTypeDef, ...
```

- [ContainerTypeDef](./type_defs.md#containertypedef)
- [CorsRuleTypeDef](./type_defs.md#corsruletypedef)
- [MetricPolicyRuleTypeDef](./type_defs.md#metricpolicyruletypedef)
- [MetricPolicyTypeDef](./type_defs.md#metricpolicytypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [TagTypeDef](./type_defs.md#tagtypedef)
- [CreateContainerOutputTypeDef](./type_defs.md#createcontaineroutputtypedef)
- [DescribeContainerOutputTypeDef](./type_defs.md#describecontaineroutputtypedef)
- [GetContainerPolicyOutputTypeDef](./type_defs.md#getcontainerpolicyoutputtypedef)
- [GetCorsPolicyOutputTypeDef](./type_defs.md#getcorspolicyoutputtypedef)
- [GetLifecyclePolicyOutputTypeDef](./type_defs.md#getlifecyclepolicyoutputtypedef)
- [GetMetricPolicyOutputTypeDef](./type_defs.md#getmetricpolicyoutputtypedef)
- [ListContainersOutputTypeDef](./type_defs.md#listcontainersoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
