# Literals for boto3 Kafka module

> [Index](../index.md) > [Kafka](./index.md) > Literals

Auto-generated documentation for [Kafka](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html#Kafka)
type annotations stubs module [mypy_boto3_kafka](https://pypi.org/project/mypy-boto3-kafka/).

- [Literals for boto3 Kafka module](#literals-for-boto3-kafka-module)
  - [BrokerAZDistribution](#brokerazdistribution)
  - [ClientBroker](#clientbroker)
  - [ClusterState](#clusterstate)
  - [ConfigurationState](#configurationstate)
  - [EnhancedMonitoring](#enhancedmonitoring)
  - [KafkaVersionStatus](#kafkaversionstatus)
  - [ListClusterOperationsPaginatorName](#listclusteroperationspaginatorname)
  - [ListClustersPaginatorName](#listclusterspaginatorname)
  - [ListConfigurationRevisionsPaginatorName](#listconfigurationrevisionspaginatorname)
  - [ListConfigurationsPaginatorName](#listconfigurationspaginatorname)
  - [ListKafkaVersionsPaginatorName](#listkafkaversionspaginatorname)
  - [ListNodesPaginatorName](#listnodespaginatorname)
  - [ListScramSecretsPaginatorName](#listscramsecretspaginatorname)
  - [NodeType](#nodetype)

## BrokerAZDistribution

```python
from mypy_boto3_kafka.literals import BrokerAZDistribution
```

Values:

- `DEFAULT`

## ClientBroker

```python
from mypy_boto3_kafka.literals import ClientBroker
```

Values:

- `PLAINTEXT`
- `TLS`
- `TLS_PLAINTEXT`

## ClusterState

```python
from mypy_boto3_kafka.literals import ClusterState
```

Values:

- `ACTIVE`
- `CREATING`
- `DELETING`
- `FAILED`
- `HEALING`
- `MAINTENANCE`
- `REBOOTING_BROKER`
- `UPDATING`

## ConfigurationState

```python
from mypy_boto3_kafka.literals import ConfigurationState
```

Values:

- `ACTIVE`
- `DELETE_FAILED`
- `DELETING`

## EnhancedMonitoring

```python
from mypy_boto3_kafka.literals import EnhancedMonitoring
```

Values:

- `DEFAULT`
- `PER_BROKER`
- `PER_TOPIC_PER_BROKER`
- `PER_TOPIC_PER_PARTITION`

## KafkaVersionStatus

```python
from mypy_boto3_kafka.literals import KafkaVersionStatus
```

Values:

- `ACTIVE`
- `DEPRECATED`

## ListClusterOperationsPaginatorName

```python
from mypy_boto3_kafka.literals import ListClusterOperationsPaginatorName
```

Values:

- `list_cluster_operations`

## ListClustersPaginatorName

```python
from mypy_boto3_kafka.literals import ListClustersPaginatorName
```

Values:

- `list_clusters`

## ListConfigurationRevisionsPaginatorName

```python
from mypy_boto3_kafka.literals import ListConfigurationRevisionsPaginatorName
```

Values:

- `list_configuration_revisions`

## ListConfigurationsPaginatorName

```python
from mypy_boto3_kafka.literals import ListConfigurationsPaginatorName
```

Values:

- `list_configurations`

## ListKafkaVersionsPaginatorName

```python
from mypy_boto3_kafka.literals import ListKafkaVersionsPaginatorName
```

Values:

- `list_kafka_versions`

## ListNodesPaginatorName

```python
from mypy_boto3_kafka.literals import ListNodesPaginatorName
```

Values:

- `list_nodes`

## ListScramSecretsPaginatorName

```python
from mypy_boto3_kafka.literals import ListScramSecretsPaginatorName
```

Values:

- `list_scram_secrets`

## NodeType

```python
from mypy_boto3_kafka.literals import NodeType
```

Values:

- `BROKER`
