# KafkaClient for boto3 Kafka module

> [Index](../index.md) > [Kafka](./index.md) > KafkaClient

Auto-generated documentation for [Kafka](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka)
type annotations stubs module [mypy_boto3_kafka](https://pypi.org/project/mypy-boto3-kafka/).

- [KafkaClient for boto3 Kafka module](#kafkaclient-for-boto3-kafka-module)
  - [KafkaClient](#kafkaclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [batch_associate_scram_secret](#batch_associate_scram_secret)
    - [batch_disassociate_scram_secret](#batch_disassociate_scram_secret)
    - [can_paginate](#can_paginate)
    - [create_cluster](#create_cluster)
    - [create_configuration](#create_configuration)
    - [delete_cluster](#delete_cluster)
    - [delete_configuration](#delete_configuration)
    - [describe_cluster](#describe_cluster)
    - [describe_cluster_operation](#describe_cluster_operation)
    - [describe_configuration](#describe_configuration)
    - [describe_configuration_revision](#describe_configuration_revision)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_bootstrap_brokers](#get_bootstrap_brokers)
    - [get_compatible_kafka_versions](#get_compatible_kafka_versions)
    - [list_cluster_operations](#list_cluster_operations)
    - [list_clusters](#list_clusters)
    - [list_configuration_revisions](#list_configuration_revisions)
    - [list_configurations](#list_configurations)
    - [list_kafka_versions](#list_kafka_versions)
    - [list_nodes](#list_nodes)
    - [list_scram_secrets](#list_scram_secrets)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [reboot_broker](#reboot_broker)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_broker_count](#update_broker_count)
    - [update_broker_storage](#update_broker_storage)
    - [update_broker_type](#update_broker_type)
    - [update_cluster_configuration](#update_cluster_configuration)
    - [update_cluster_kafka_version](#update_cluster_kafka_version)
    - [update_configuration](#update_configuration)
    - [update_monitoring](#update_monitoring)
    - [get_paginator](#get_paginator)

## KafkaClient

Type annotations for `boto3.client("kafka")`

Can be used directly:

```python
from mypy_boto3_kafka.client import KafkaClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_kafka.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ForbiddenException`
- `Exceptions.InternalServerErrorException`
- `Exceptions.NotFoundException`
- `Exceptions.ServiceUnavailableException`
- `Exceptions.TooManyRequestsException`
- `Exceptions.UnauthorizedException`


## Methods


### batch_associate_scram_secret

Type annotations for `boto3.client("kafka").batch_associate_scram_secret` method.

[Client.batch_associate_scram_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.batch_associate_scram_secret)

```python
def batch_associate_scram_secret(
    self,
    ClusterArn: str,
    SecretArnList: List[str]
) -> BatchAssociateScramSecretResponseTypeDef:
    pass
```

### batch_disassociate_scram_secret

Type annotations for `boto3.client("kafka").batch_disassociate_scram_secret` method.

[Client.batch_disassociate_scram_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.batch_disassociate_scram_secret)

```python
def batch_disassociate_scram_secret(
    self,
    ClusterArn: str,
    SecretArnList: List[str]
) -> BatchDisassociateScramSecretResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("kafka").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_cluster

Type annotations for `boto3.client("kafka").create_cluster` method.

[Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.create_cluster)

```python
def create_cluster(
    self,
    BrokerNodeGroupInfo: "BrokerNodeGroupInfoTypeDef",
    ClusterName: str,
    KafkaVersion: str,
    NumberOfBrokerNodes: int,
    ClientAuthentication: "ClientAuthenticationTypeDef" = None,
    ConfigurationInfo: "ConfigurationInfoTypeDef" = None,
    EncryptionInfo: "EncryptionInfoTypeDef" = None,
    EnhancedMonitoring: EnhancedMonitoring = None,
    OpenMonitoring: OpenMonitoringInfoTypeDef = None,
    LoggingInfo: "LoggingInfoTypeDef" = None,
    Tags: Dict[str, str] = None
) -> CreateClusterResponseTypeDef:
    pass
```

### create_configuration

Type annotations for `boto3.client("kafka").create_configuration` method.

[Client.create_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.create_configuration)

```python
def create_configuration(
    self,
    Name: str,
    ServerProperties: Union[bytes, IO[bytes]],
    Description: str = None,
    KafkaVersions: List[str] = None
) -> CreateConfigurationResponseTypeDef:
    pass
```

### delete_cluster

Type annotations for `boto3.client("kafka").delete_cluster` method.

[Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.delete_cluster)

```python
def delete_cluster(
    self,
    ClusterArn: str,
    CurrentVersion: str = None
) -> DeleteClusterResponseTypeDef:
    pass
```

### delete_configuration

Type annotations for `boto3.client("kafka").delete_configuration` method.

[Client.delete_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.delete_configuration)

```python
def delete_configuration(
    self,
    Arn: str
) -> DeleteConfigurationResponseTypeDef:
    pass
```

### describe_cluster

Type annotations for `boto3.client("kafka").describe_cluster` method.

[Client.describe_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.describe_cluster)

```python
def describe_cluster(
    self,
    ClusterArn: str
) -> DescribeClusterResponseTypeDef:
    pass
```

### describe_cluster_operation

Type annotations for `boto3.client("kafka").describe_cluster_operation` method.

[Client.describe_cluster_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.describe_cluster_operation)

```python
def describe_cluster_operation(
    self,
    ClusterOperationArn: str
) -> DescribeClusterOperationResponseTypeDef:
    pass
```

### describe_configuration

Type annotations for `boto3.client("kafka").describe_configuration` method.

[Client.describe_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.describe_configuration)

```python
def describe_configuration(
    self,
    Arn: str
) -> DescribeConfigurationResponseTypeDef:
    pass
```

### describe_configuration_revision

Type annotations for `boto3.client("kafka").describe_configuration_revision` method.

[Client.describe_configuration_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.describe_configuration_revision)

```python
def describe_configuration_revision(
    self,
    Arn: str,
    Revision: int
) -> DescribeConfigurationRevisionResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("kafka").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.generate_presigned_url)

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

### get_bootstrap_brokers

Type annotations for `boto3.client("kafka").get_bootstrap_brokers` method.

[Client.get_bootstrap_brokers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.get_bootstrap_brokers)

```python
def get_bootstrap_brokers(
    self,
    ClusterArn: str
) -> GetBootstrapBrokersResponseTypeDef:
    pass
```

### get_compatible_kafka_versions

Type annotations for `boto3.client("kafka").get_compatible_kafka_versions` method.

[Client.get_compatible_kafka_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.get_compatible_kafka_versions)

```python
def get_compatible_kafka_versions(
    self,
    ClusterArn: str = None
) -> GetCompatibleKafkaVersionsResponseTypeDef:
    pass
```

### list_cluster_operations

Type annotations for `boto3.client("kafka").list_cluster_operations` method.

[Client.list_cluster_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_cluster_operations)

```python
def list_cluster_operations(
    self,
    ClusterArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListClusterOperationsResponseTypeDef:
    pass
```

### list_clusters

Type annotations for `boto3.client("kafka").list_clusters` method.

[Client.list_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_clusters)

```python
def list_clusters(
    self,
    ClusterNameFilter: str = None,
    MaxResults: int = None,
    NextToken: str = None
) -> ListClustersResponseTypeDef:
    pass
```

### list_configuration_revisions

Type annotations for `boto3.client("kafka").list_configuration_revisions` method.

[Client.list_configuration_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_configuration_revisions)

```python
def list_configuration_revisions(
    self,
    Arn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListConfigurationRevisionsResponseTypeDef:
    pass
```

### list_configurations

Type annotations for `boto3.client("kafka").list_configurations` method.

[Client.list_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_configurations)

```python
def list_configurations(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListConfigurationsResponseTypeDef:
    pass
```

### list_kafka_versions

Type annotations for `boto3.client("kafka").list_kafka_versions` method.

[Client.list_kafka_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_kafka_versions)

```python
def list_kafka_versions(
    self,
    MaxResults: int = None,
    NextToken: str = None
) -> ListKafkaVersionsResponseTypeDef:
    pass
```

### list_nodes

Type annotations for `boto3.client("kafka").list_nodes` method.

[Client.list_nodes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_nodes)

```python
def list_nodes(
    self,
    ClusterArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListNodesResponseTypeDef:
    pass
```

### list_scram_secrets

Type annotations for `boto3.client("kafka").list_scram_secrets` method.

[Client.list_scram_secrets documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_scram_secrets)

```python
def list_scram_secrets(
    self,
    ClusterArn: str,
    MaxResults: int = None,
    NextToken: str = None
) -> ListScramSecretsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("kafka").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    ResourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### reboot_broker

Type annotations for `boto3.client("kafka").reboot_broker` method.

[Client.reboot_broker documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.reboot_broker)

```python
def reboot_broker(
    self,
    BrokerIds: List[str],
    ClusterArn: str
) -> RebootBrokerResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("kafka").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.tag_resource)

```python
def tag_resource(
    self,
    ResourceArn: str,
    Tags: Dict[str, str]
) -> None:
    pass
```

### untag_resource

Type annotations for `boto3.client("kafka").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.untag_resource)

```python
def untag_resource(
    self,
    ResourceArn: str,
    TagKeys: List[str]
) -> None:
    pass
```

### update_broker_count

Type annotations for `boto3.client("kafka").update_broker_count` method.

[Client.update_broker_count documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_broker_count)

```python
def update_broker_count(
    self,
    ClusterArn: str,
    CurrentVersion: str,
    TargetNumberOfBrokerNodes: int
) -> UpdateBrokerCountResponseTypeDef:
    pass
```

### update_broker_storage

Type annotations for `boto3.client("kafka").update_broker_storage` method.

[Client.update_broker_storage documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_broker_storage)

```python
def update_broker_storage(
    self,
    ClusterArn: str,
    CurrentVersion: str,
    TargetBrokerEBSVolumeInfo: List["BrokerEBSVolumeInfoTypeDef"]
) -> UpdateBrokerStorageResponseTypeDef:
    pass
```

### update_broker_type

Type annotations for `boto3.client("kafka").update_broker_type` method.

[Client.update_broker_type documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_broker_type)

```python
def update_broker_type(
    self,
    ClusterArn: str,
    CurrentVersion: str,
    TargetInstanceType: str
) -> UpdateBrokerTypeResponseTypeDef:
    pass
```

### update_cluster_configuration

Type annotations for `boto3.client("kafka").update_cluster_configuration` method.

[Client.update_cluster_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_cluster_configuration)

```python
def update_cluster_configuration(
    self,
    ClusterArn: str,
    ConfigurationInfo: "ConfigurationInfoTypeDef",
    CurrentVersion: str
) -> UpdateClusterConfigurationResponseTypeDef:
    pass
```

### update_cluster_kafka_version

Type annotations for `boto3.client("kafka").update_cluster_kafka_version` method.

[Client.update_cluster_kafka_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_cluster_kafka_version)

```python
def update_cluster_kafka_version(
    self,
    ClusterArn: str,
    CurrentVersion: str,
    TargetKafkaVersion: str,
    ConfigurationInfo: "ConfigurationInfoTypeDef" = None
) -> UpdateClusterKafkaVersionResponseTypeDef:
    pass
```

### update_configuration

Type annotations for `boto3.client("kafka").update_configuration` method.

[Client.update_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_configuration)

```python
def update_configuration(
    self,
    Arn: str,
    ServerProperties: Union[bytes, IO[bytes]],
    Description: str = None
) -> UpdateConfigurationResponseTypeDef:
    pass
```

### update_monitoring

Type annotations for `boto3.client("kafka").update_monitoring` method.

[Client.update_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka.Client.update_monitoring)

```python
def update_monitoring(
    self,
    ClusterArn: str,
    CurrentVersion: str,
    EnhancedMonitoring: EnhancedMonitoring = None,
    OpenMonitoring: OpenMonitoringInfoTypeDef = None,
    LoggingInfo: "LoggingInfoTypeDef" = None
) -> UpdateMonitoringResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("kafka").get_paginator` method with overloads.

- `client.get_paginator("list_cluster_operations")` -> [ListClusterOperationsPaginator](./paginators.md#listclusteroperationspaginator)
- `client.get_paginator("list_clusters")` -> [ListClustersPaginator](./paginators.md#listclusterspaginator)
- `client.get_paginator("list_configuration_revisions")` -> [ListConfigurationRevisionsPaginator](./paginators.md#listconfigurationrevisionspaginator)
- `client.get_paginator("list_configurations")` -> [ListConfigurationsPaginator](./paginators.md#listconfigurationspaginator)
- `client.get_paginator("list_kafka_versions")` -> [ListKafkaVersionsPaginator](./paginators.md#listkafkaversionspaginator)
- `client.get_paginator("list_nodes")` -> [ListNodesPaginator](./paginators.md#listnodespaginator)
- `client.get_paginator("list_scram_secrets")` -> [ListScramSecretsPaginator](./paginators.md#listscramsecretspaginator)


