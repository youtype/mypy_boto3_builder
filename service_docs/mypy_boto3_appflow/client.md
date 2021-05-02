# AppflowClient for boto3 Appflow module

> [Index](../index.md) > [Appflow](./index.md) > AppflowClient

Auto-generated documentation for [Appflow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow)
type annotations stubs module [mypy_boto3_appflow](https://pypi.org/project/mypy-boto3-appflow/).

- [AppflowClient for boto3 Appflow module](#appflowclient-for-boto3-appflow-module)
  - [AppflowClient](#appflowclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_connector_profile](#create_connector_profile)
    - [create_flow](#create_flow)
    - [delete_connector_profile](#delete_connector_profile)
    - [delete_flow](#delete_flow)
    - [describe_connector_entity](#describe_connector_entity)
    - [describe_connector_profiles](#describe_connector_profiles)
    - [describe_connectors](#describe_connectors)
    - [describe_flow](#describe_flow)
    - [describe_flow_execution_records](#describe_flow_execution_records)
    - [generate_presigned_url](#generate_presigned_url)
    - [list_connector_entities](#list_connector_entities)
    - [list_flows](#list_flows)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [start_flow](#start_flow)
    - [stop_flow](#stop_flow)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_connector_profile](#update_connector_profile)
    - [update_flow](#update_flow)

## AppflowClient

Type annotations for `boto3.client("appflow")`

Can be used directly:

```python
from mypy_boto3_appflow.client import AppflowClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_appflow.client import Exceptions

def handle_error(exc: Exceptions.ClientError) -> None:
    ...
```


Exceptions:

- `Exceptions.ClientError`
- `Exceptions.ConflictException`
- `Exceptions.ConnectorAuthenticationException`
- `Exceptions.ConnectorServerException`
- `Exceptions.InternalServerException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.UnsupportedOperationException`
- `Exceptions.ValidationException`


## Methods


### can_paginate

Type annotations for `boto3.client("appflow").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_connector_profile

Type annotations for `boto3.client("appflow").create_connector_profile` method.

[Client.create_connector_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.create_connector_profile)

```python
def create_connector_profile(
    self,
    connectorProfileName: str,
    connectorType: ConnectorType,
    connectionMode: ConnectionMode,
    connectorProfileConfig: ConnectorProfileConfigTypeDef,
    kmsArn: str = None
) -> CreateConnectorProfileResponseTypeDef:
    pass
```

### create_flow

Type annotations for `boto3.client("appflow").create_flow` method.

[Client.create_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.create_flow)

```python
def create_flow(
    self,
    flowName: str,
    triggerConfig: "TriggerConfigTypeDef",
    sourceFlowConfig: "SourceFlowConfigTypeDef",
    destinationFlowConfigList: List["DestinationFlowConfigTypeDef"],
    tasks: List["TaskTypeDef"],
    description: str = None,
    kmsArn: str = None,
    tags: Dict[str, str] = None
) -> CreateFlowResponseTypeDef:
    pass
```

### delete_connector_profile

Type annotations for `boto3.client("appflow").delete_connector_profile` method.

[Client.delete_connector_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.delete_connector_profile)

```python
def delete_connector_profile(
    self,
    connectorProfileName: str,
    forceDelete: bool = None
) -> Dict[str, Any]:
    pass
```

### delete_flow

Type annotations for `boto3.client("appflow").delete_flow` method.

[Client.delete_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.delete_flow)

```python
def delete_flow(
    self,
    flowName: str,
    forceDelete: bool = None
) -> Dict[str, Any]:
    pass
```

### describe_connector_entity

Type annotations for `boto3.client("appflow").describe_connector_entity` method.

[Client.describe_connector_entity documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connector_entity)

```python
def describe_connector_entity(
    self,
    connectorEntityName: str,
    connectorType: ConnectorType = None,
    connectorProfileName: str = None
) -> DescribeConnectorEntityResponseTypeDef:
    pass
```

### describe_connector_profiles

Type annotations for `boto3.client("appflow").describe_connector_profiles` method.

[Client.describe_connector_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connector_profiles)

```python
def describe_connector_profiles(
    self,
    connectorProfileNames: List[str] = None,
    connectorType: ConnectorType = None,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeConnectorProfilesResponseTypeDef:
    pass
```

### describe_connectors

Type annotations for `boto3.client("appflow").describe_connectors` method.

[Client.describe_connectors documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connectors)

```python
def describe_connectors(
    self,
    connectorTypes: List[ConnectorType] = None,
    nextToken: str = None
) -> DescribeConnectorsResponseTypeDef:
    pass
```

### describe_flow

Type annotations for `boto3.client("appflow").describe_flow` method.

[Client.describe_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_flow)

```python
def describe_flow(
    self,
    flowName: str
) -> DescribeFlowResponseTypeDef:
    pass
```

### describe_flow_execution_records

Type annotations for `boto3.client("appflow").describe_flow_execution_records` method.

[Client.describe_flow_execution_records documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_flow_execution_records)

```python
def describe_flow_execution_records(
    self,
    flowName: str,
    maxResults: int = None,
    nextToken: str = None
) -> DescribeFlowExecutionRecordsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("appflow").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.generate_presigned_url)

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

### list_connector_entities

Type annotations for `boto3.client("appflow").list_connector_entities` method.

[Client.list_connector_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_connector_entities)

```python
def list_connector_entities(
    self,
    connectorProfileName: str = None,
    connectorType: ConnectorType = None,
    entitiesPath: str = None
) -> ListConnectorEntitiesResponseTypeDef:
    pass
```

### list_flows

Type annotations for `boto3.client("appflow").list_flows` method.

[Client.list_flows documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_flows)

```python
def list_flows(
    self,
    maxResults: int = None,
    nextToken: str = None
) -> ListFlowsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("appflow").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### start_flow

Type annotations for `boto3.client("appflow").start_flow` method.

[Client.start_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.start_flow)

```python
def start_flow(
    self,
    flowName: str
) -> StartFlowResponseTypeDef:
    pass
```

### stop_flow

Type annotations for `boto3.client("appflow").stop_flow` method.

[Client.stop_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.stop_flow)

```python
def stop_flow(
    self,
    flowName: str
) -> StopFlowResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("appflow").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("appflow").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_connector_profile

Type annotations for `boto3.client("appflow").update_connector_profile` method.

[Client.update_connector_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.update_connector_profile)

```python
def update_connector_profile(
    self,
    connectorProfileName: str,
    connectionMode: ConnectionMode,
    connectorProfileConfig: ConnectorProfileConfigTypeDef
) -> UpdateConnectorProfileResponseTypeDef:
    pass
```

### update_flow

Type annotations for `boto3.client("appflow").update_flow` method.

[Client.update_flow documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.update_flow)

```python
def update_flow(
    self,
    flowName: str,
    triggerConfig: "TriggerConfigTypeDef",
    destinationFlowConfigList: List["DestinationFlowConfigTypeDef"],
    tasks: List["TaskTypeDef"],
    description: str = None,
    sourceFlowConfig: "SourceFlowConfigTypeDef" = None
) -> UpdateFlowResponseTypeDef:
    pass
```