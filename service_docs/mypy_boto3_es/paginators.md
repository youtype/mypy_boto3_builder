# Paginators for boto3 ElasticsearchService module

> [Index](../index.md) > [ElasticsearchService](./index.md) > Paginators

Auto-generated documentation for [ElasticsearchService](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService)
type annotations stubs module [mypy_boto3_es](https://pypi.org/project/mypy-boto3-es/).

- [Paginators for boto3 ElasticsearchService module](#paginators-for-boto3-elasticsearchservice-module)
  - [DescribeReservedElasticsearchInstanceOfferingsPaginator](#describereservedelasticsearchinstanceofferingspaginator)
  - [DescribeReservedElasticsearchInstancesPaginator](#describereservedelasticsearchinstancespaginator)
  - [GetUpgradeHistoryPaginator](#getupgradehistorypaginator)
  - [ListElasticsearchInstanceTypesPaginator](#listelasticsearchinstancetypespaginator)
  - [ListElasticsearchVersionsPaginator](#listelasticsearchversionspaginator)

## DescribeReservedElasticsearchInstanceOfferingsPaginator

Type annotations for `boto3.client("es").get_paginator("describe_reserved_elasticsearch_instance_offerings")`.

Can be used directly:

```python
from mypy_boto3_es.paginators import DescribeReservedElasticsearchInstanceOfferingsPaginator

def get_describe_reserved_elasticsearch_instance_offerings_paginator() -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
    return boto3.client("es").get_paginator("describe_reserved_elasticsearch_instance_offerings")
```

[Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)

```python
class DescribeReservedElasticsearchInstanceOfferingsPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef]:
        pass
```
## DescribeReservedElasticsearchInstancesPaginator

Type annotations for `boto3.client("es").get_paginator("describe_reserved_elasticsearch_instances")`.

Can be used directly:

```python
from mypy_boto3_es.paginators import DescribeReservedElasticsearchInstancesPaginator

def get_describe_reserved_elasticsearch_instances_paginator() -> DescribeReservedElasticsearchInstancesPaginator:
    return boto3.client("es").get_paginator("describe_reserved_elasticsearch_instances")
```

[Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)

```python
class DescribeReservedElasticsearchInstancesPaginator(Boto3Paginator):
    def paginate(
        self,
        ReservedElasticsearchInstanceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedElasticsearchInstancesResponseTypeDef]:
        pass
```
## GetUpgradeHistoryPaginator

Type annotations for `boto3.client("es").get_paginator("get_upgrade_history")`.

Can be used directly:

```python
from mypy_boto3_es.paginators import GetUpgradeHistoryPaginator

def get_get_upgrade_history_paginator() -> GetUpgradeHistoryPaginator:
    return boto3.client("es").get_paginator("get_upgrade_history")
```

[Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)

```python
class GetUpgradeHistoryPaginator(Boto3Paginator):
    def paginate(
        self,
        DomainName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetUpgradeHistoryResponseTypeDef]:
        pass
```
## ListElasticsearchInstanceTypesPaginator

Type annotations for `boto3.client("es").get_paginator("list_elasticsearch_instance_types")`.

Can be used directly:

```python
from mypy_boto3_es.paginators import ListElasticsearchInstanceTypesPaginator

def get_list_elasticsearch_instance_types_paginator() -> ListElasticsearchInstanceTypesPaginator:
    return boto3.client("es").get_paginator("list_elasticsearch_instance_types")
```

[Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)

```python
class ListElasticsearchInstanceTypesPaginator(Boto3Paginator):
    def paginate(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListElasticsearchInstanceTypesResponseTypeDef]:
        pass
```
## ListElasticsearchVersionsPaginator

Type annotations for `boto3.client("es").get_paginator("list_elasticsearch_versions")`.

Can be used directly:

```python
from mypy_boto3_es.paginators import ListElasticsearchVersionsPaginator

def get_list_elasticsearch_versions_paginator() -> ListElasticsearchVersionsPaginator:
    return boto3.client("es").get_paginator("list_elasticsearch_versions")
```

[Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)

```python
class ListElasticsearchVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListElasticsearchVersionsResponseTypeDef]:
        pass
```