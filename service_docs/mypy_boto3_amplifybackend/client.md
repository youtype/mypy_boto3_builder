# AmplifyBackendClient for boto3 AmplifyBackend module

> [Index](../index.md) > [AmplifyBackend](./index.md) > AmplifyBackendClient

Auto-generated documentation for [AmplifyBackend](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend)
type annotations stubs module [mypy_boto3_amplifybackend](https://pypi.org/project/mypy-boto3-amplifybackend/).

- [AmplifyBackendClient for boto3 AmplifyBackend module](#amplifybackendclient-for-boto3-amplifybackend-module)
  - [AmplifyBackendClient](#amplifybackendclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [clone_backend](#clone_backend)
    - [create_backend](#create_backend)
    - [create_backend_api](#create_backend_api)
    - [create_backend_auth](#create_backend_auth)
    - [create_backend_config](#create_backend_config)
    - [create_token](#create_token)
    - [delete_backend](#delete_backend)
    - [delete_backend_api](#delete_backend_api)
    - [delete_backend_auth](#delete_backend_auth)
    - [delete_token](#delete_token)
    - [generate_backend_api_models](#generate_backend_api_models)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_backend](#get_backend)
    - [get_backend_api](#get_backend_api)
    - [get_backend_api_models](#get_backend_api_models)
    - [get_backend_auth](#get_backend_auth)
    - [get_backend_job](#get_backend_job)
    - [get_token](#get_token)
    - [list_backend_jobs](#list_backend_jobs)
    - [remove_all_backends](#remove_all_backends)
    - [remove_backend_config](#remove_backend_config)
    - [update_backend_api](#update_backend_api)
    - [update_backend_auth](#update_backend_auth)
    - [update_backend_config](#update_backend_config)
    - [update_backend_job](#update_backend_job)
    - [get_paginator](#get_paginator)

## AmplifyBackendClient

Type annotations for `boto3.client("amplifybackend")`

Can be used directly:

```python
from mypy_boto3_amplifybackend.client import AmplifyBackendClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_amplifybackend.client import Exceptions

def handle_error(exc: Exceptions.BadRequestException) -> None:
    ...
```


Exceptions:

- `Exceptions.BadRequestException`
- `Exceptions.ClientError`
- `Exceptions.GatewayTimeoutException`
- `Exceptions.NotFoundException`
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("amplifybackend").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### clone_backend

Type annotations for `boto3.client("amplifybackend").clone_backend` method.

[Client.clone_backend documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.clone_backend)

```python
def clone_backend(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    TargetEnvironmentName: str
) -> CloneBackendResponseTypeDef:
    pass
```

### create_backend

Type annotations for `boto3.client("amplifybackend").create_backend` method.

[Client.create_backend documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend)

```python
def create_backend(
    self,
    AppId: str,
    AppName: str,
    BackendEnvironmentName: str,
    ResourceConfig: Dict[str, Any] = None,
    ResourceName: str = None
) -> CreateBackendResponseTypeDef:
    pass
```

### create_backend_api

Type annotations for `boto3.client("amplifybackend").create_backend_api` method.

[Client.create_backend_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_api)

```python
def create_backend_api(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceConfig: "BackendAPIResourceConfigTypeDef",
    ResourceName: str
) -> CreateBackendAPIResponseTypeDef:
    pass
```

### create_backend_auth

Type annotations for `boto3.client("amplifybackend").create_backend_auth` method.

[Client.create_backend_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_auth)

```python
def create_backend_auth(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceConfig: "CreateBackendAuthResourceConfigTypeDef",
    ResourceName: str
) -> CreateBackendAuthResponseTypeDef:
    pass
```

### create_backend_config

Type annotations for `boto3.client("amplifybackend").create_backend_config` method.

[Client.create_backend_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_config)

```python
def create_backend_config(
    self,
    AppId: str,
    BackendManagerAppId: str = None
) -> CreateBackendConfigResponseTypeDef:
    pass
```

### create_token

Type annotations for `boto3.client("amplifybackend").create_token` method.

[Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.create_token)

```python
def create_token(
    self,
    AppId: str
) -> CreateTokenResponseTypeDef:
    pass
```

### delete_backend

Type annotations for `boto3.client("amplifybackend").delete_backend` method.

[Client.delete_backend documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend)

```python
def delete_backend(
    self,
    AppId: str,
    BackendEnvironmentName: str
) -> DeleteBackendResponseTypeDef:
    pass
```

### delete_backend_api

Type annotations for `boto3.client("amplifybackend").delete_backend_api` method.

[Client.delete_backend_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_api)

```python
def delete_backend_api(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str,
    ResourceConfig: "BackendAPIResourceConfigTypeDef" = None
) -> DeleteBackendAPIResponseTypeDef:
    pass
```

### delete_backend_auth

Type annotations for `boto3.client("amplifybackend").delete_backend_auth` method.

[Client.delete_backend_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_auth)

```python
def delete_backend_auth(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str
) -> DeleteBackendAuthResponseTypeDef:
    pass
```

### delete_token

Type annotations for `boto3.client("amplifybackend").delete_token` method.

[Client.delete_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_token)

```python
def delete_token(
    self,
    AppId: str,
    SessionId: str
) -> DeleteTokenResponseTypeDef:
    pass
```

### generate_backend_api_models

Type annotations for `boto3.client("amplifybackend").generate_backend_api_models` method.

[Client.generate_backend_api_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.generate_backend_api_models)

```python
def generate_backend_api_models(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str
) -> GenerateBackendAPIModelsResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("amplifybackend").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.generate_presigned_url)

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

### get_backend

Type annotations for `boto3.client("amplifybackend").get_backend` method.

[Client.get_backend documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend)

```python
def get_backend(
    self,
    AppId: str,
    BackendEnvironmentName: str = None
) -> GetBackendResponseTypeDef:
    pass
```

### get_backend_api

Type annotations for `boto3.client("amplifybackend").get_backend_api` method.

[Client.get_backend_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_api)

```python
def get_backend_api(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str,
    ResourceConfig: "BackendAPIResourceConfigTypeDef" = None
) -> GetBackendAPIResponseTypeDef:
    pass
```

### get_backend_api_models

Type annotations for `boto3.client("amplifybackend").get_backend_api_models` method.

[Client.get_backend_api_models documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_api_models)

```python
def get_backend_api_models(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str
) -> GetBackendAPIModelsResponseTypeDef:
    pass
```

### get_backend_auth

Type annotations for `boto3.client("amplifybackend").get_backend_auth` method.

[Client.get_backend_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_auth)

```python
def get_backend_auth(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str
) -> GetBackendAuthResponseTypeDef:
    pass
```

### get_backend_job

Type annotations for `boto3.client("amplifybackend").get_backend_job` method.

[Client.get_backend_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_job)

```python
def get_backend_job(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    JobId: str
) -> GetBackendJobResponseTypeDef:
    pass
```

### get_token

Type annotations for `boto3.client("amplifybackend").get_token` method.

[Client.get_token documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.get_token)

```python
def get_token(
    self,
    AppId: str,
    SessionId: str
) -> GetTokenResponseTypeDef:
    pass
```

### list_backend_jobs

Type annotations for `boto3.client("amplifybackend").list_backend_jobs` method.

[Client.list_backend_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.list_backend_jobs)

```python
def list_backend_jobs(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    JobId: str = None,
    MaxResults: int = None,
    NextToken: str = None,
    Operation: str = None,
    Status: str = None
) -> ListBackendJobsResponseTypeDef:
    pass
```

### remove_all_backends

Type annotations for `boto3.client("amplifybackend").remove_all_backends` method.

[Client.remove_all_backends documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.remove_all_backends)

```python
def remove_all_backends(
    self,
    AppId: str,
    CleanAmplifyApp: bool = None
) -> RemoveAllBackendsResponseTypeDef:
    pass
```

### remove_backend_config

Type annotations for `boto3.client("amplifybackend").remove_backend_config` method.

[Client.remove_backend_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.remove_backend_config)

```python
def remove_backend_config(
    self,
    AppId: str
) -> RemoveBackendConfigResponseTypeDef:
    pass
```

### update_backend_api

Type annotations for `boto3.client("amplifybackend").update_backend_api` method.

[Client.update_backend_api documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_api)

```python
def update_backend_api(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceName: str,
    ResourceConfig: "BackendAPIResourceConfigTypeDef" = None
) -> UpdateBackendAPIResponseTypeDef:
    pass
```

### update_backend_auth

Type annotations for `boto3.client("amplifybackend").update_backend_auth` method.

[Client.update_backend_auth documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_auth)

```python
def update_backend_auth(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    ResourceConfig: UpdateBackendAuthResourceConfigTypeDef,
    ResourceName: str
) -> UpdateBackendAuthResponseTypeDef:
    pass
```

### update_backend_config

Type annotations for `boto3.client("amplifybackend").update_backend_config` method.

[Client.update_backend_config documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_config)

```python
def update_backend_config(
    self,
    AppId: str,
    LoginAuthConfig: "LoginAuthConfigReqObjTypeDef" = None
) -> UpdateBackendConfigResponseTypeDef:
    pass
```

### update_backend_job

Type annotations for `boto3.client("amplifybackend").update_backend_job` method.

[Client.update_backend_job documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_job)

```python
def update_backend_job(
    self,
    AppId: str,
    BackendEnvironmentName: str,
    JobId: str,
    Operation: str = None,
    Status: str = None
) -> UpdateBackendJobResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("amplifybackend").get_paginator` method with overloads.

- `client.get_paginator("list_backend_jobs")` -> [ListBackendJobsPaginator](./paginators.md#listbackendjobspaginator)


