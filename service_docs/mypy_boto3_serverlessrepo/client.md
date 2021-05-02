# ServerlessApplicationRepositoryClient for boto3 ServerlessApplicationRepository module

> [Index](../index.md) > [ServerlessApplicationRepository](./index.md) > ServerlessApplicationRepositoryClient

Auto-generated documentation for [ServerlessApplicationRepository](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository)
type annotations stubs module [mypy_boto3_serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo/).

- [ServerlessApplicationRepositoryClient for boto3 ServerlessApplicationRepository module](#serverlessapplicationrepositoryclient-for-boto3-serverlessapplicationrepository-module)
  - [ServerlessApplicationRepositoryClient](#serverlessapplicationrepositoryclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [create_application](#create_application)
    - [create_application_version](#create_application_version)
    - [create_cloud_formation_change_set](#create_cloud_formation_change_set)
    - [create_cloud_formation_template](#create_cloud_formation_template)
    - [delete_application](#delete_application)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_application](#get_application)
    - [get_application_policy](#get_application_policy)
    - [get_cloud_formation_template](#get_cloud_formation_template)
    - [list_application_dependencies](#list_application_dependencies)
    - [list_application_versions](#list_application_versions)
    - [list_applications](#list_applications)
    - [put_application_policy](#put_application_policy)
    - [unshare_application](#unshare_application)
    - [update_application](#update_application)
    - [get_paginator](#get_paginator)

## ServerlessApplicationRepositoryClient

Type annotations for `boto3.client("serverlessrepo")`

Can be used directly:

```python
from mypy_boto3_serverlessrepo.client import ServerlessApplicationRepositoryClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_serverlessrepo.client import Exceptions

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
- `Exceptions.TooManyRequestsException`


## Methods


### can_paginate

Type annotations for `boto3.client("serverlessrepo").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_application

Type annotations for `boto3.client("serverlessrepo").create_application` method.

[Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application)

```python
def create_application(
    self,
    Author: str,
    Description: str,
    Name: str,
    HomePageUrl: str = None,
    Labels: List[str] = None,
    LicenseBody: str = None,
    LicenseUrl: str = None,
    ReadmeBody: str = None,
    ReadmeUrl: str = None,
    SemanticVersion: str = None,
    SourceCodeArchiveUrl: str = None,
    SourceCodeUrl: str = None,
    SpdxLicenseId: str = None,
    TemplateBody: str = None,
    TemplateUrl: str = None
) -> CreateApplicationResponseTypeDef:
    pass
```

### create_application_version

Type annotations for `boto3.client("serverlessrepo").create_application_version` method.

[Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application_version)

```python
def create_application_version(
    self,
    ApplicationId: str,
    SemanticVersion: str,
    SourceCodeArchiveUrl: str = None,
    SourceCodeUrl: str = None,
    TemplateBody: str = None,
    TemplateUrl: str = None
) -> CreateApplicationVersionResponseTypeDef:
    pass
```

### create_cloud_formation_change_set

Type annotations for `boto3.client("serverlessrepo").create_cloud_formation_change_set` method.

[Client.create_cloud_formation_change_set documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_change_set)

```python
def create_cloud_formation_change_set(
    self,
    ApplicationId: str,
    StackName: str,
    Capabilities: List[str] = None,
    ChangeSetName: str = None,
    ClientToken: str = None,
    Description: str = None,
    NotificationArns: List[str] = None,
    ParameterOverrides: List[ParameterValueTypeDef] = None,
    ResourceTypes: List[str] = None,
    RollbackConfiguration: RollbackConfigurationTypeDef = None,
    SemanticVersion: str = None,
    Tags: List[TagTypeDef] = None,
    TemplateId: str = None
) -> CreateCloudFormationChangeSetResponseTypeDef:
    pass
```

### create_cloud_formation_template

Type annotations for `boto3.client("serverlessrepo").create_cloud_formation_template` method.

[Client.create_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_template)

```python
def create_cloud_formation_template(
    self,
    ApplicationId: str,
    SemanticVersion: str = None
) -> CreateCloudFormationTemplateResponseTypeDef:
    pass
```

### delete_application

Type annotations for `boto3.client("serverlessrepo").delete_application` method.

[Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.delete_application)

```python
def delete_application(
    self,
    ApplicationId: str
) -> None:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("serverlessrepo").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.generate_presigned_url)

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

### get_application

Type annotations for `boto3.client("serverlessrepo").get_application` method.

[Client.get_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application)

```python
def get_application(
    self,
    ApplicationId: str,
    SemanticVersion: str = None
) -> GetApplicationResponseTypeDef:
    pass
```

### get_application_policy

Type annotations for `boto3.client("serverlessrepo").get_application_policy` method.

[Client.get_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application_policy)

```python
def get_application_policy(
    self,
    ApplicationId: str
) -> GetApplicationPolicyResponseTypeDef:
    pass
```

### get_cloud_formation_template

Type annotations for `boto3.client("serverlessrepo").get_cloud_formation_template` method.

[Client.get_cloud_formation_template documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_cloud_formation_template)

```python
def get_cloud_formation_template(
    self,
    ApplicationId: str,
    TemplateId: str
) -> GetCloudFormationTemplateResponseTypeDef:
    pass
```

### list_application_dependencies

Type annotations for `boto3.client("serverlessrepo").list_application_dependencies` method.

[Client.list_application_dependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_dependencies)

```python
def list_application_dependencies(
    self,
    ApplicationId: str,
    MaxItems: int = None,
    NextToken: str = None,
    SemanticVersion: str = None
) -> ListApplicationDependenciesResponseTypeDef:
    pass
```

### list_application_versions

Type annotations for `boto3.client("serverlessrepo").list_application_versions` method.

[Client.list_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_versions)

```python
def list_application_versions(
    self,
    ApplicationId: str,
    MaxItems: int = None,
    NextToken: str = None
) -> ListApplicationVersionsResponseTypeDef:
    pass
```

### list_applications

Type annotations for `boto3.client("serverlessrepo").list_applications` method.

[Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_applications)

```python
def list_applications(
    self,
    MaxItems: int = None,
    NextToken: str = None
) -> ListApplicationsResponseTypeDef:
    pass
```

### put_application_policy

Type annotations for `boto3.client("serverlessrepo").put_application_policy` method.

[Client.put_application_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.put_application_policy)

```python
def put_application_policy(
    self,
    ApplicationId: str,
    Statements: List["ApplicationPolicyStatementTypeDef"]
) -> PutApplicationPolicyResponseTypeDef:
    pass
```

### unshare_application

Type annotations for `boto3.client("serverlessrepo").unshare_application` method.

[Client.unshare_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.unshare_application)

```python
def unshare_application(
    self,
    ApplicationId: str,
    OrganizationId: str
) -> None:
    pass
```

### update_application

Type annotations for `boto3.client("serverlessrepo").update_application` method.

[Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.update_application)

```python
def update_application(
    self,
    ApplicationId: str,
    Author: str = None,
    Description: str = None,
    HomePageUrl: str = None,
    Labels: List[str] = None,
    ReadmeBody: str = None,
    ReadmeUrl: str = None
) -> UpdateApplicationResponseTypeDef:
    pass
```



### get_paginator

Type annotations for `boto3.client("serverlessrepo").get_paginator` method with overloads.

- `client.get_paginator("list_application_dependencies")` -> [ListApplicationDependenciesPaginator](./paginators.md#listapplicationdependenciespaginator)
- `client.get_paginator("list_application_versions")` -> [ListApplicationVersionsPaginator](./paginators.md#listapplicationversionspaginator)
- `client.get_paginator("list_applications")` -> [ListApplicationsPaginator](./paginators.md#listapplicationspaginator)


