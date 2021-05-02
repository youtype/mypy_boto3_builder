# Paginators for boto3 Kafka module

> [Index](../index.md) > [Kafka](./index.md) > Paginators

Auto-generated documentation for [Kafka](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka)
type annotations stubs module [mypy_boto3_kafka](https://pypi.org/project/mypy-boto3-kafka/).

- [Paginators for boto3 Kafka module](#paginators-for-boto3-kafka-module)
  - [ListClusterOperationsPaginator](#listclusteroperationspaginator)
  - [ListClustersPaginator](#listclusterspaginator)
  - [ListConfigurationRevisionsPaginator](#listconfigurationrevisionspaginator)
  - [ListConfigurationsPaginator](#listconfigurationspaginator)
  - [ListKafkaVersionsPaginator](#listkafkaversionspaginator)
  - [ListNodesPaginator](#listnodespaginator)
  - [ListScramSecretsPaginator](#listscramsecretspaginator)

## ListClusterOperationsPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_cluster_operations")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListClusterOperationsPaginator

def get_list_cluster_operations_paginator() -> ListClusterOperationsPaginator:
    return boto3.client("kafka").get_paginator("list_cluster_operations")
```

[Paginator.ListClusterOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusterOperations)

```python
class ListClusterOperationsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClusterOperationsResponseTypeDef]:
        pass
```
## ListClustersPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_clusters")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListClustersPaginator

def get_list_clusters_paginator() -> ListClustersPaginator:
    return boto3.client("kafka").get_paginator("list_clusters")
```

[Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListClusters)

```python
class ListClustersPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterNameFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        pass
```
## ListConfigurationRevisionsPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_configuration_revisions")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListConfigurationRevisionsPaginator

def get_list_configuration_revisions_paginator() -> ListConfigurationRevisionsPaginator:
    return boto3.client("kafka").get_paginator("list_configuration_revisions")
```

[Paginator.ListConfigurationRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListConfigurationRevisions)

```python
class ListConfigurationRevisionsPaginator(Boto3Paginator):
    def paginate(
        self,
        Arn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationRevisionsResponseTypeDef]:
        pass
```
## ListConfigurationsPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_configurations")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListConfigurationsPaginator

def get_list_configurations_paginator() -> ListConfigurationsPaginator:
    return boto3.client("kafka").get_paginator("list_configurations")
```

[Paginator.ListConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListConfigurations)

```python
class ListConfigurationsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigurationsResponseTypeDef]:
        pass
```
## ListKafkaVersionsPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_kafka_versions")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListKafkaVersionsPaginator

def get_list_kafka_versions_paginator() -> ListKafkaVersionsPaginator:
    return boto3.client("kafka").get_paginator("list_kafka_versions")
```

[Paginator.ListKafkaVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListKafkaVersions)

```python
class ListKafkaVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKafkaVersionsResponseTypeDef]:
        pass
```
## ListNodesPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_nodes")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListNodesPaginator

def get_list_nodes_paginator() -> ListNodesPaginator:
    return boto3.client("kafka").get_paginator("list_nodes")
```

[Paginator.ListNodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListNodes)

```python
class ListNodesPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNodesResponseTypeDef]:
        pass
```
## ListScramSecretsPaginator

Type annotations for `boto3.client("kafka").get_paginator("list_scram_secrets")`.

Can be used directly:

```python
from mypy_boto3_kafka.paginators import ListScramSecretsPaginator

def get_list_scram_secrets_paginator() -> ListScramSecretsPaginator:
    return boto3.client("kafka").get_paginator("list_scram_secrets")
```

[Paginator.ListScramSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Paginator.ListScramSecrets)

```python
class ListScramSecretsPaginator(Boto3Paginator):
    def paginate(
        self,
        ClusterArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListScramSecretsResponseTypeDef]:
        pass
```