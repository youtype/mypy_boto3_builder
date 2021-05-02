# Paginators for boto3 SMS module

> [Index](../index.md) > [SMS](./index.md) > Paginators

Auto-generated documentation for [SMS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS)
type annotations stubs module [mypy_boto3_sms](https://pypi.org/project/mypy-boto3-sms/).

- [Paginators for boto3 SMS module](#paginators-for-boto3-sms-module)
  - [GetConnectorsPaginator](#getconnectorspaginator)
  - [GetReplicationJobsPaginator](#getreplicationjobspaginator)
  - [GetReplicationRunsPaginator](#getreplicationrunspaginator)
  - [GetServersPaginator](#getserverspaginator)
  - [ListAppsPaginator](#listappspaginator)

## GetConnectorsPaginator

Type annotations for `boto3.client("sms").get_paginator("get_connectors")`.

Can be used directly:

```python
from mypy_boto3_sms.paginators import GetConnectorsPaginator

def get_get_connectors_paginator() -> GetConnectorsPaginator:
    return boto3.client("sms").get_paginator("get_connectors")
```

[Paginator.GetConnectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Paginator.GetConnectors)

```python
class GetConnectorsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetConnectorsResponseTypeDef]:
        pass
```
## GetReplicationJobsPaginator

Type annotations for `boto3.client("sms").get_paginator("get_replication_jobs")`.

Can be used directly:

```python
from mypy_boto3_sms.paginators import GetReplicationJobsPaginator

def get_get_replication_jobs_paginator() -> GetReplicationJobsPaginator:
    return boto3.client("sms").get_paginator("get_replication_jobs")
```

[Paginator.GetReplicationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Paginator.GetReplicationJobs)

```python
class GetReplicationJobsPaginator(Boto3Paginator):
    def paginate(
        self,
        replicationJobId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReplicationJobsResponseTypeDef]:
        pass
```
## GetReplicationRunsPaginator

Type annotations for `boto3.client("sms").get_paginator("get_replication_runs")`.

Can be used directly:

```python
from mypy_boto3_sms.paginators import GetReplicationRunsPaginator

def get_get_replication_runs_paginator() -> GetReplicationRunsPaginator:
    return boto3.client("sms").get_paginator("get_replication_runs")
```

[Paginator.GetReplicationRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Paginator.GetReplicationRuns)

```python
class GetReplicationRunsPaginator(Boto3Paginator):
    def paginate(
        self,
        replicationJobId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetReplicationRunsResponseTypeDef]:
        pass
```
## GetServersPaginator

Type annotations for `boto3.client("sms").get_paginator("get_servers")`.

Can be used directly:

```python
from mypy_boto3_sms.paginators import GetServersPaginator

def get_get_servers_paginator() -> GetServersPaginator:
    return boto3.client("sms").get_paginator("get_servers")
```

[Paginator.GetServers documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Paginator.GetServers)

```python
class GetServersPaginator(Boto3Paginator):
    def paginate(
        self,
        vmServerAddressList: List["VmServerAddressTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetServersResponseTypeDef]:
        pass
```
## ListAppsPaginator

Type annotations for `boto3.client("sms").get_paginator("list_apps")`.

Can be used directly:

```python
from mypy_boto3_sms.paginators import ListAppsPaginator

def get_list_apps_paginator() -> ListAppsPaginator:
    return boto3.client("sms").get_paginator("list_apps")
```

[Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html#SMS.Paginator.ListApps)

```python
class ListAppsPaginator(Boto3Paginator):
    def paginate(
        self,
        appIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppsResponseTypeDef]:
        pass
```