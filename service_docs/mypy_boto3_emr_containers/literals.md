# Literals for boto3 EMRContainers module

> [Index](../index.md) > [EMRContainers](./index.md) > Literals

Auto-generated documentation for [EMRContainers](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers)
type annotations stubs module [mypy_boto3_emr_containers](https://pypi.org/project/mypy-boto3-emr-containers/).

- [Literals for boto3 EMRContainers module](#literals-for-boto3-emrcontainers-module)
  - [ContainerProviderType](#containerprovidertype)
  - [EndpointState](#endpointstate)
  - [FailureReason](#failurereason)
  - [JobRunState](#jobrunstate)
  - [ListJobRunsPaginatorName](#listjobrunspaginatorname)
  - [ListManagedEndpointsPaginatorName](#listmanagedendpointspaginatorname)
  - [ListVirtualClustersPaginatorName](#listvirtualclusterspaginatorname)
  - [PersistentAppUI](#persistentappui)
  - [VirtualClusterState](#virtualclusterstate)

## ContainerProviderType

```python
from mypy_boto3_emr_containers.literals import ContainerProviderType
```

Values:

- `EKS`

## EndpointState

```python
from mypy_boto3_emr_containers.literals import EndpointState
```

Values:

- `ACTIVE`
- `CREATING`
- `TERMINATED`
- `TERMINATED_WITH_ERRORS`
- `TERMINATING`

## FailureReason

```python
from mypy_boto3_emr_containers.literals import FailureReason
```

Values:

- `CLUSTER_UNAVAILABLE`
- `INTERNAL_ERROR`
- `USER_ERROR`
- `VALIDATION_ERROR`

## JobRunState

```python
from mypy_boto3_emr_containers.literals import JobRunState
```

Values:

- `CANCEL_PENDING`
- `CANCELLED`
- `COMPLETED`
- `FAILED`
- `PENDING`
- `RUNNING`
- `SUBMITTED`

## ListJobRunsPaginatorName

```python
from mypy_boto3_emr_containers.literals import ListJobRunsPaginatorName
```

Values:

- `list_job_runs`

## ListManagedEndpointsPaginatorName

```python
from mypy_boto3_emr_containers.literals import ListManagedEndpointsPaginatorName
```

Values:

- `list_managed_endpoints`

## ListVirtualClustersPaginatorName

```python
from mypy_boto3_emr_containers.literals import ListVirtualClustersPaginatorName
```

Values:

- `list_virtual_clusters`

## PersistentAppUI

```python
from mypy_boto3_emr_containers.literals import PersistentAppUI
```

Values:

- `DISABLED`
- `ENABLED`

## VirtualClusterState

```python
from mypy_boto3_emr_containers.literals import VirtualClusterState
```

Values:

- `ARRESTED`
- `RUNNING`
- `TERMINATED`
- `TERMINATING`
