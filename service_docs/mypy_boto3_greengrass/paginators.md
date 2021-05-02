# Paginators for boto3 Greengrass module

> [Index](../index.md) > [Greengrass](./index.md) > Paginators

Auto-generated documentation for [Greengrass](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass)
type annotations stubs module [mypy_boto3_greengrass](https://pypi.org/project/mypy-boto3-greengrass/).

- [Paginators for boto3 Greengrass module](#paginators-for-boto3-greengrass-module)
  - [ListBulkDeploymentDetailedReportsPaginator](#listbulkdeploymentdetailedreportspaginator)
  - [ListBulkDeploymentsPaginator](#listbulkdeploymentspaginator)
  - [ListConnectorDefinitionVersionsPaginator](#listconnectordefinitionversionspaginator)
  - [ListConnectorDefinitionsPaginator](#listconnectordefinitionspaginator)
  - [ListCoreDefinitionVersionsPaginator](#listcoredefinitionversionspaginator)
  - [ListCoreDefinitionsPaginator](#listcoredefinitionspaginator)
  - [ListDeploymentsPaginator](#listdeploymentspaginator)
  - [ListDeviceDefinitionVersionsPaginator](#listdevicedefinitionversionspaginator)
  - [ListDeviceDefinitionsPaginator](#listdevicedefinitionspaginator)
  - [ListFunctionDefinitionVersionsPaginator](#listfunctiondefinitionversionspaginator)
  - [ListFunctionDefinitionsPaginator](#listfunctiondefinitionspaginator)
  - [ListGroupVersionsPaginator](#listgroupversionspaginator)
  - [ListGroupsPaginator](#listgroupspaginator)
  - [ListLoggerDefinitionVersionsPaginator](#listloggerdefinitionversionspaginator)
  - [ListLoggerDefinitionsPaginator](#listloggerdefinitionspaginator)
  - [ListResourceDefinitionVersionsPaginator](#listresourcedefinitionversionspaginator)
  - [ListResourceDefinitionsPaginator](#listresourcedefinitionspaginator)
  - [ListSubscriptionDefinitionVersionsPaginator](#listsubscriptiondefinitionversionspaginator)
  - [ListSubscriptionDefinitionsPaginator](#listsubscriptiondefinitionspaginator)

## ListBulkDeploymentDetailedReportsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_bulk_deployment_detailed_reports")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListBulkDeploymentDetailedReportsPaginator

def get_list_bulk_deployment_detailed_reports_paginator() -> ListBulkDeploymentDetailedReportsPaginator:
    return boto3.client("greengrass").get_paginator("list_bulk_deployment_detailed_reports")
```

[Paginator.ListBulkDeploymentDetailedReports documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)

```python
class ListBulkDeploymentDetailedReportsPaginator(Boto3Paginator):
    def paginate(
        self,
        BulkDeploymentId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBulkDeploymentDetailedReportsResponseTypeDef]:
        pass
```
## ListBulkDeploymentsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_bulk_deployments")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListBulkDeploymentsPaginator

def get_list_bulk_deployments_paginator() -> ListBulkDeploymentsPaginator:
    return boto3.client("greengrass").get_paginator("list_bulk_deployments")
```

[Paginator.ListBulkDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)

```python
class ListBulkDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBulkDeploymentsResponseTypeDef]:
        pass
```
## ListConnectorDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_connector_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListConnectorDefinitionVersionsPaginator

def get_list_connector_definition_versions_paginator() -> ListConnectorDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_connector_definition_versions")
```

[Paginator.ListConnectorDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)

```python
class ListConnectorDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ConnectorDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorDefinitionVersionsResponseTypeDef]:
        pass
```
## ListConnectorDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_connector_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListConnectorDefinitionsPaginator

def get_list_connector_definitions_paginator() -> ListConnectorDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_connector_definitions")
```

[Paginator.ListConnectorDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)

```python
class ListConnectorDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConnectorDefinitionsResponseTypeDef]:
        pass
```
## ListCoreDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_core_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListCoreDefinitionVersionsPaginator

def get_list_core_definition_versions_paginator() -> ListCoreDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_core_definition_versions")
```

[Paginator.ListCoreDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)

```python
class ListCoreDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        CoreDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreDefinitionVersionsResponseTypeDef]:
        pass
```
## ListCoreDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_core_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListCoreDefinitionsPaginator

def get_list_core_definitions_paginator() -> ListCoreDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_core_definitions")
```

[Paginator.ListCoreDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)

```python
class ListCoreDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCoreDefinitionsResponseTypeDef]:
        pass
```
## ListDeploymentsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_deployments")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListDeploymentsPaginator

def get_list_deployments_paginator() -> ListDeploymentsPaginator:
    return boto3.client("greengrass").get_paginator("list_deployments")
```

[Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)

```python
class ListDeploymentsPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsResponseTypeDef]:
        pass
```
## ListDeviceDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_device_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListDeviceDefinitionVersionsPaginator

def get_list_device_definition_versions_paginator() -> ListDeviceDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_device_definition_versions")
```

[Paginator.ListDeviceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)

```python
class ListDeviceDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        DeviceDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceDefinitionVersionsResponseTypeDef]:
        pass
```
## ListDeviceDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_device_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListDeviceDefinitionsPaginator

def get_list_device_definitions_paginator() -> ListDeviceDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_device_definitions")
```

[Paginator.ListDeviceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)

```python
class ListDeviceDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceDefinitionsResponseTypeDef]:
        pass
```
## ListFunctionDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_function_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListFunctionDefinitionVersionsPaginator

def get_list_function_definition_versions_paginator() -> ListFunctionDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_function_definition_versions")
```

[Paginator.ListFunctionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)

```python
class ListFunctionDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        FunctionDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionDefinitionVersionsResponseTypeDef]:
        pass
```
## ListFunctionDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_function_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListFunctionDefinitionsPaginator

def get_list_function_definitions_paginator() -> ListFunctionDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_function_definitions")
```

[Paginator.ListFunctionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)

```python
class ListFunctionDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionDefinitionsResponseTypeDef]:
        pass
```
## ListGroupVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_group_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListGroupVersionsPaginator

def get_list_group_versions_paginator() -> ListGroupVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_group_versions")
```

[Paginator.ListGroupVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)

```python
class ListGroupVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        GroupId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupVersionsResponseTypeDef]:
        pass
```
## ListGroupsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_groups")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListGroupsPaginator

def get_list_groups_paginator() -> ListGroupsPaginator:
    return boto3.client("greengrass").get_paginator("list_groups")
```

[Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)

```python
class ListGroupsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroupsResponseTypeDef]:
        pass
```
## ListLoggerDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_logger_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListLoggerDefinitionVersionsPaginator

def get_list_logger_definition_versions_paginator() -> ListLoggerDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_logger_definition_versions")
```

[Paginator.ListLoggerDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)

```python
class ListLoggerDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        LoggerDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLoggerDefinitionVersionsResponseTypeDef]:
        pass
```
## ListLoggerDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_logger_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListLoggerDefinitionsPaginator

def get_list_logger_definitions_paginator() -> ListLoggerDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_logger_definitions")
```

[Paginator.ListLoggerDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)

```python
class ListLoggerDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLoggerDefinitionsResponseTypeDef]:
        pass
```
## ListResourceDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_resource_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListResourceDefinitionVersionsPaginator

def get_list_resource_definition_versions_paginator() -> ListResourceDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_resource_definition_versions")
```

[Paginator.ListResourceDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)

```python
class ListResourceDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        ResourceDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDefinitionVersionsResponseTypeDef]:
        pass
```
## ListResourceDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_resource_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListResourceDefinitionsPaginator

def get_list_resource_definitions_paginator() -> ListResourceDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_resource_definitions")
```

[Paginator.ListResourceDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)

```python
class ListResourceDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDefinitionsResponseTypeDef]:
        pass
```
## ListSubscriptionDefinitionVersionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_subscription_definition_versions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListSubscriptionDefinitionVersionsPaginator

def get_list_subscription_definition_versions_paginator() -> ListSubscriptionDefinitionVersionsPaginator:
    return boto3.client("greengrass").get_paginator("list_subscription_definition_versions")
```

[Paginator.ListSubscriptionDefinitionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)

```python
class ListSubscriptionDefinitionVersionsPaginator(Boto3Paginator):
    def paginate(
        self,
        SubscriptionDefinitionId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionDefinitionVersionsResponseTypeDef]:
        pass
```
## ListSubscriptionDefinitionsPaginator

Type annotations for `boto3.client("greengrass").get_paginator("list_subscription_definitions")`.

Can be used directly:

```python
from mypy_boto3_greengrass.paginators import ListSubscriptionDefinitionsPaginator

def get_list_subscription_definitions_paginator() -> ListSubscriptionDefinitionsPaginator:
    return boto3.client("greengrass").get_paginator("list_subscription_definitions")
```

[Paginator.ListSubscriptionDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)

```python
class ListSubscriptionDefinitionsPaginator(Boto3Paginator):
    def paginate(
        self,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscriptionDefinitionsResponseTypeDef]:
        pass
```