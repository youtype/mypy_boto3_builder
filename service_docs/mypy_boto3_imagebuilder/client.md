# ImagebuilderClient for boto3 Imagebuilder module

> [Index](../index.md) > [Imagebuilder](./index.md) > ImagebuilderClient

Auto-generated documentation for [Imagebuilder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder)
type annotations stubs module [mypy_boto3_imagebuilder](https://pypi.org/project/mypy-boto3-imagebuilder/).

- [ImagebuilderClient for boto3 Imagebuilder module](#imagebuilderclient-for-boto3-imagebuilder-module)
  - [ImagebuilderClient](#imagebuilderclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [can_paginate](#can_paginate)
    - [cancel_image_creation](#cancel_image_creation)
    - [create_component](#create_component)
    - [create_container_recipe](#create_container_recipe)
    - [create_distribution_configuration](#create_distribution_configuration)
    - [create_image](#create_image)
    - [create_image_pipeline](#create_image_pipeline)
    - [create_image_recipe](#create_image_recipe)
    - [create_infrastructure_configuration](#create_infrastructure_configuration)
    - [delete_component](#delete_component)
    - [delete_container_recipe](#delete_container_recipe)
    - [delete_distribution_configuration](#delete_distribution_configuration)
    - [delete_image](#delete_image)
    - [delete_image_pipeline](#delete_image_pipeline)
    - [delete_image_recipe](#delete_image_recipe)
    - [delete_infrastructure_configuration](#delete_infrastructure_configuration)
    - [generate_presigned_url](#generate_presigned_url)
    - [get_component](#get_component)
    - [get_component_policy](#get_component_policy)
    - [get_container_recipe](#get_container_recipe)
    - [get_container_recipe_policy](#get_container_recipe_policy)
    - [get_distribution_configuration](#get_distribution_configuration)
    - [get_image](#get_image)
    - [get_image_pipeline](#get_image_pipeline)
    - [get_image_policy](#get_image_policy)
    - [get_image_recipe](#get_image_recipe)
    - [get_image_recipe_policy](#get_image_recipe_policy)
    - [get_infrastructure_configuration](#get_infrastructure_configuration)
    - [import_component](#import_component)
    - [list_component_build_versions](#list_component_build_versions)
    - [list_components](#list_components)
    - [list_container_recipes](#list_container_recipes)
    - [list_distribution_configurations](#list_distribution_configurations)
    - [list_image_build_versions](#list_image_build_versions)
    - [list_image_packages](#list_image_packages)
    - [list_image_pipeline_images](#list_image_pipeline_images)
    - [list_image_pipelines](#list_image_pipelines)
    - [list_image_recipes](#list_image_recipes)
    - [list_images](#list_images)
    - [list_infrastructure_configurations](#list_infrastructure_configurations)
    - [list_tags_for_resource](#list_tags_for_resource)
    - [put_component_policy](#put_component_policy)
    - [put_container_recipe_policy](#put_container_recipe_policy)
    - [put_image_policy](#put_image_policy)
    - [put_image_recipe_policy](#put_image_recipe_policy)
    - [start_image_pipeline_execution](#start_image_pipeline_execution)
    - [tag_resource](#tag_resource)
    - [untag_resource](#untag_resource)
    - [update_distribution_configuration](#update_distribution_configuration)
    - [update_image_pipeline](#update_image_pipeline)
    - [update_infrastructure_configuration](#update_infrastructure_configuration)

## ImagebuilderClient

Type annotations for `boto3.client("imagebuilder")`

Can be used directly:

```python
from mypy_boto3_imagebuilder.client import ImagebuilderClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_imagebuilder.client import Exceptions

def handle_error(exc: Exceptions.CallRateLimitExceededException) -> None:
    ...
```


Exceptions:

- `Exceptions.CallRateLimitExceededException`
- `Exceptions.ClientError`
- `Exceptions.ClientException`
- `Exceptions.ForbiddenException`
- `Exceptions.IdempotentParameterMismatchException`
- `Exceptions.InvalidPaginationTokenException`
- `Exceptions.InvalidParameterCombinationException`
- `Exceptions.InvalidParameterException`
- `Exceptions.InvalidParameterValueException`
- `Exceptions.InvalidRequestException`
- `Exceptions.InvalidVersionNumberException`
- `Exceptions.ResourceAlreadyExistsException`
- `Exceptions.ResourceDependencyException`
- `Exceptions.ResourceInUseException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ServiceException`
- `Exceptions.ServiceQuotaExceededException`
- `Exceptions.ServiceUnavailableException`


## Methods


### can_paginate

Type annotations for `boto3.client("imagebuilder").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### cancel_image_creation

Type annotations for `boto3.client("imagebuilder").cancel_image_creation` method.

[Client.cancel_image_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.cancel_image_creation)

```python
def cancel_image_creation(
    self,
    imageBuildVersionArn: str,
    clientToken: str
) -> CancelImageCreationResponseTypeDef:
    pass
```

### create_component

Type annotations for `boto3.client("imagebuilder").create_component` method.

[Client.create_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_component)

```python
def create_component(
    self,
    name: str,
    semanticVersion: str,
    platform: Platform,
    clientToken: str,
    description: str = None,
    changeDescription: str = None,
    supportedOsVersions: List[str] = None,
    data: str = None,
    uri: str = None,
    kmsKeyId: str = None,
    tags: Dict[str, str] = None
) -> CreateComponentResponseTypeDef:
    pass
```

### create_container_recipe

Type annotations for `boto3.client("imagebuilder").create_container_recipe` method.

[Client.create_container_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_container_recipe)

```python
def create_container_recipe(
    self,
    containerType: Literal['DOCKER'],
    name: str,
    semanticVersion: str,
    components: List["ComponentConfigurationTypeDef"],
    parentImage: str,
    targetRepository: "TargetContainerRepositoryTypeDef",
    clientToken: str,
    description: str = None,
    instanceConfiguration: "InstanceConfigurationTypeDef" = None,
    dockerfileTemplateData: str = None,
    dockerfileTemplateUri: str = None,
    platformOverride: Platform = None,
    imageOsVersionOverride: str = None,
    tags: Dict[str, str] = None,
    workingDirectory: str = None,
    kmsKeyId: str = None
) -> CreateContainerRecipeResponseTypeDef:
    pass
```

### create_distribution_configuration

Type annotations for `boto3.client("imagebuilder").create_distribution_configuration` method.

[Client.create_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_distribution_configuration)

```python
def create_distribution_configuration(
    self,
    name: str,
    distributions: List["DistributionTypeDef"],
    clientToken: str,
    description: str = None,
    tags: Dict[str, str] = None
) -> CreateDistributionConfigurationResponseTypeDef:
    pass
```

### create_image

Type annotations for `boto3.client("imagebuilder").create_image` method.

[Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_image)

```python
def create_image(
    self,
    infrastructureConfigurationArn: str,
    clientToken: str,
    imageRecipeArn: str = None,
    containerRecipeArn: str = None,
    distributionConfigurationArn: str = None,
    imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
    enhancedImageMetadataEnabled: bool = None,
    tags: Dict[str, str] = None
) -> CreateImageResponseTypeDef:
    pass
```

### create_image_pipeline

Type annotations for `boto3.client("imagebuilder").create_image_pipeline` method.

[Client.create_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_pipeline)

```python
def create_image_pipeline(
    self,
    name: str,
    infrastructureConfigurationArn: str,
    clientToken: str,
    description: str = None,
    imageRecipeArn: str = None,
    containerRecipeArn: str = None,
    distributionConfigurationArn: str = None,
    imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
    enhancedImageMetadataEnabled: bool = None,
    schedule: "ScheduleTypeDef" = None,
    status: PipelineStatus = None,
    tags: Dict[str, str] = None
) -> CreateImagePipelineResponseTypeDef:
    pass
```

### create_image_recipe

Type annotations for `boto3.client("imagebuilder").create_image_recipe` method.

[Client.create_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_recipe)

```python
def create_image_recipe(
    self,
    name: str,
    semanticVersion: str,
    components: List["ComponentConfigurationTypeDef"],
    parentImage: str,
    clientToken: str,
    description: str = None,
    blockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"] = None,
    tags: Dict[str, str] = None,
    workingDirectory: str = None
) -> CreateImageRecipeResponseTypeDef:
    pass
```

### create_infrastructure_configuration

Type annotations for `boto3.client("imagebuilder").create_infrastructure_configuration` method.

[Client.create_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.create_infrastructure_configuration)

```python
def create_infrastructure_configuration(
    self,
    name: str,
    instanceProfileName: str,
    clientToken: str,
    description: str = None,
    instanceTypes: List[str] = None,
    securityGroupIds: List[str] = None,
    subnetId: str = None,
    logging: "LoggingTypeDef" = None,
    keyPair: str = None,
    terminateInstanceOnFailure: bool = None,
    snsTopicArn: str = None,
    resourceTags: Dict[str, str] = None,
    tags: Dict[str, str] = None
) -> CreateInfrastructureConfigurationResponseTypeDef:
    pass
```

### delete_component

Type annotations for `boto3.client("imagebuilder").delete_component` method.

[Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_component)

```python
def delete_component(
    self,
    componentBuildVersionArn: str
) -> DeleteComponentResponseTypeDef:
    pass
```

### delete_container_recipe

Type annotations for `boto3.client("imagebuilder").delete_container_recipe` method.

[Client.delete_container_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_container_recipe)

```python
def delete_container_recipe(
    self,
    containerRecipeArn: str
) -> DeleteContainerRecipeResponseTypeDef:
    pass
```

### delete_distribution_configuration

Type annotations for `boto3.client("imagebuilder").delete_distribution_configuration` method.

[Client.delete_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_distribution_configuration)

```python
def delete_distribution_configuration(
    self,
    distributionConfigurationArn: str
) -> DeleteDistributionConfigurationResponseTypeDef:
    pass
```

### delete_image

Type annotations for `boto3.client("imagebuilder").delete_image` method.

[Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image)

```python
def delete_image(
    self,
    imageBuildVersionArn: str
) -> DeleteImageResponseTypeDef:
    pass
```

### delete_image_pipeline

Type annotations for `boto3.client("imagebuilder").delete_image_pipeline` method.

[Client.delete_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_pipeline)

```python
def delete_image_pipeline(
    self,
    imagePipelineArn: str
) -> DeleteImagePipelineResponseTypeDef:
    pass
```

### delete_image_recipe

Type annotations for `boto3.client("imagebuilder").delete_image_recipe` method.

[Client.delete_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_recipe)

```python
def delete_image_recipe(
    self,
    imageRecipeArn: str
) -> DeleteImageRecipeResponseTypeDef:
    pass
```

### delete_infrastructure_configuration

Type annotations for `boto3.client("imagebuilder").delete_infrastructure_configuration` method.

[Client.delete_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.delete_infrastructure_configuration)

```python
def delete_infrastructure_configuration(
    self,
    infrastructureConfigurationArn: str
) -> DeleteInfrastructureConfigurationResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("imagebuilder").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.generate_presigned_url)

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

### get_component

Type annotations for `boto3.client("imagebuilder").get_component` method.

[Client.get_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_component)

```python
def get_component(
    self,
    componentBuildVersionArn: str
) -> GetComponentResponseTypeDef:
    pass
```

### get_component_policy

Type annotations for `boto3.client("imagebuilder").get_component_policy` method.

[Client.get_component_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_component_policy)

```python
def get_component_policy(
    self,
    componentArn: str
) -> GetComponentPolicyResponseTypeDef:
    pass
```

### get_container_recipe

Type annotations for `boto3.client("imagebuilder").get_container_recipe` method.

[Client.get_container_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_container_recipe)

```python
def get_container_recipe(
    self,
    containerRecipeArn: str
) -> GetContainerRecipeResponseTypeDef:
    pass
```

### get_container_recipe_policy

Type annotations for `boto3.client("imagebuilder").get_container_recipe_policy` method.

[Client.get_container_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_container_recipe_policy)

```python
def get_container_recipe_policy(
    self,
    containerRecipeArn: str
) -> GetContainerRecipePolicyResponseTypeDef:
    pass
```

### get_distribution_configuration

Type annotations for `boto3.client("imagebuilder").get_distribution_configuration` method.

[Client.get_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_distribution_configuration)

```python
def get_distribution_configuration(
    self,
    distributionConfigurationArn: str
) -> GetDistributionConfigurationResponseTypeDef:
    pass
```

### get_image

Type annotations for `boto3.client("imagebuilder").get_image` method.

[Client.get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_image)

```python
def get_image(
    self,
    imageBuildVersionArn: str
) -> GetImageResponseTypeDef:
    pass
```

### get_image_pipeline

Type annotations for `boto3.client("imagebuilder").get_image_pipeline` method.

[Client.get_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_pipeline)

```python
def get_image_pipeline(
    self,
    imagePipelineArn: str
) -> GetImagePipelineResponseTypeDef:
    pass
```

### get_image_policy

Type annotations for `boto3.client("imagebuilder").get_image_policy` method.

[Client.get_image_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_policy)

```python
def get_image_policy(
    self,
    imageArn: str
) -> GetImagePolicyResponseTypeDef:
    pass
```

### get_image_recipe

Type annotations for `boto3.client("imagebuilder").get_image_recipe` method.

[Client.get_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe)

```python
def get_image_recipe(
    self,
    imageRecipeArn: str
) -> GetImageRecipeResponseTypeDef:
    pass
```

### get_image_recipe_policy

Type annotations for `boto3.client("imagebuilder").get_image_recipe_policy` method.

[Client.get_image_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe_policy)

```python
def get_image_recipe_policy(
    self,
    imageRecipeArn: str
) -> GetImageRecipePolicyResponseTypeDef:
    pass
```

### get_infrastructure_configuration

Type annotations for `boto3.client("imagebuilder").get_infrastructure_configuration` method.

[Client.get_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.get_infrastructure_configuration)

```python
def get_infrastructure_configuration(
    self,
    infrastructureConfigurationArn: str
) -> GetInfrastructureConfigurationResponseTypeDef:
    pass
```

### import_component

Type annotations for `boto3.client("imagebuilder").import_component` method.

[Client.import_component documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.import_component)

```python
def import_component(
    self,
    name: str,
    semanticVersion: str,
    type: ComponentType,
    format: Literal['SHELL'],
    platform: Platform,
    clientToken: str,
    description: str = None,
    changeDescription: str = None,
    data: str = None,
    uri: str = None,
    kmsKeyId: str = None,
    tags: Dict[str, str] = None
) -> ImportComponentResponseTypeDef:
    pass
```

### list_component_build_versions

Type annotations for `boto3.client("imagebuilder").list_component_build_versions` method.

[Client.list_component_build_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_component_build_versions)

```python
def list_component_build_versions(
    self,
    componentVersionArn: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListComponentBuildVersionsResponseTypeDef:
    pass
```

### list_components

Type annotations for `boto3.client("imagebuilder").list_components` method.

[Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_components)

```python
def list_components(
    self,
    owner: Ownership = None,
    filters: List[FilterTypeDef] = None,
    byName: bool = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListComponentsResponseTypeDef:
    pass
```

### list_container_recipes

Type annotations for `boto3.client("imagebuilder").list_container_recipes` method.

[Client.list_container_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_container_recipes)

```python
def list_container_recipes(
    self,
    owner: Ownership = None,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListContainerRecipesResponseTypeDef:
    pass
```

### list_distribution_configurations

Type annotations for `boto3.client("imagebuilder").list_distribution_configurations` method.

[Client.list_distribution_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_distribution_configurations)

```python
def list_distribution_configurations(
    self,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListDistributionConfigurationsResponseTypeDef:
    pass
```

### list_image_build_versions

Type annotations for `boto3.client("imagebuilder").list_image_build_versions` method.

[Client.list_image_build_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_build_versions)

```python
def list_image_build_versions(
    self,
    imageVersionArn: str,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListImageBuildVersionsResponseTypeDef:
    pass
```

### list_image_packages

Type annotations for `boto3.client("imagebuilder").list_image_packages` method.

[Client.list_image_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_packages)

```python
def list_image_packages(
    self,
    imageBuildVersionArn: str,
    maxResults: int = None,
    nextToken: str = None
) -> ListImagePackagesResponseTypeDef:
    pass
```

### list_image_pipeline_images

Type annotations for `boto3.client("imagebuilder").list_image_pipeline_images` method.

[Client.list_image_pipeline_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipeline_images)

```python
def list_image_pipeline_images(
    self,
    imagePipelineArn: str,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListImagePipelineImagesResponseTypeDef:
    pass
```

### list_image_pipelines

Type annotations for `boto3.client("imagebuilder").list_image_pipelines` method.

[Client.list_image_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipelines)

```python
def list_image_pipelines(
    self,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListImagePipelinesResponseTypeDef:
    pass
```

### list_image_recipes

Type annotations for `boto3.client("imagebuilder").list_image_recipes` method.

[Client.list_image_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_recipes)

```python
def list_image_recipes(
    self,
    owner: Ownership = None,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListImageRecipesResponseTypeDef:
    pass
```

### list_images

Type annotations for `boto3.client("imagebuilder").list_images` method.

[Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_images)

```python
def list_images(
    self,
    owner: Ownership = None,
    filters: List[FilterTypeDef] = None,
    byName: bool = None,
    maxResults: int = None,
    nextToken: str = None,
    includeDeprecated: bool = None
) -> ListImagesResponseTypeDef:
    pass
```

### list_infrastructure_configurations

Type annotations for `boto3.client("imagebuilder").list_infrastructure_configurations` method.

[Client.list_infrastructure_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_infrastructure_configurations)

```python
def list_infrastructure_configurations(
    self,
    filters: List[FilterTypeDef] = None,
    maxResults: int = None,
    nextToken: str = None
) -> ListInfrastructureConfigurationsResponseTypeDef:
    pass
```

### list_tags_for_resource

Type annotations for `boto3.client("imagebuilder").list_tags_for_resource` method.

[Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.list_tags_for_resource)

```python
def list_tags_for_resource(
    self,
    resourceArn: str
) -> ListTagsForResourceResponseTypeDef:
    pass
```

### put_component_policy

Type annotations for `boto3.client("imagebuilder").put_component_policy` method.

[Client.put_component_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.put_component_policy)

```python
def put_component_policy(
    self,
    componentArn: str,
    policy: str
) -> PutComponentPolicyResponseTypeDef:
    pass
```

### put_container_recipe_policy

Type annotations for `boto3.client("imagebuilder").put_container_recipe_policy` method.

[Client.put_container_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.put_container_recipe_policy)

```python
def put_container_recipe_policy(
    self,
    containerRecipeArn: str,
    policy: str
) -> PutContainerRecipePolicyResponseTypeDef:
    pass
```

### put_image_policy

Type annotations for `boto3.client("imagebuilder").put_image_policy` method.

[Client.put_image_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_policy)

```python
def put_image_policy(
    self,
    imageArn: str,
    policy: str
) -> PutImagePolicyResponseTypeDef:
    pass
```

### put_image_recipe_policy

Type annotations for `boto3.client("imagebuilder").put_image_recipe_policy` method.

[Client.put_image_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_recipe_policy)

```python
def put_image_recipe_policy(
    self,
    imageRecipeArn: str,
    policy: str
) -> PutImageRecipePolicyResponseTypeDef:
    pass
```

### start_image_pipeline_execution

Type annotations for `boto3.client("imagebuilder").start_image_pipeline_execution` method.

[Client.start_image_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.start_image_pipeline_execution)

```python
def start_image_pipeline_execution(
    self,
    imagePipelineArn: str,
    clientToken: str
) -> StartImagePipelineExecutionResponseTypeDef:
    pass
```

### tag_resource

Type annotations for `boto3.client("imagebuilder").tag_resource` method.

[Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.tag_resource)

```python
def tag_resource(
    self,
    resourceArn: str,
    tags: Dict[str, str]
) -> Dict[str, Any]:
    pass
```

### untag_resource

Type annotations for `boto3.client("imagebuilder").untag_resource` method.

[Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.untag_resource)

```python
def untag_resource(
    self,
    resourceArn: str,
    tagKeys: List[str]
) -> Dict[str, Any]:
    pass
```

### update_distribution_configuration

Type annotations for `boto3.client("imagebuilder").update_distribution_configuration` method.

[Client.update_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.update_distribution_configuration)

```python
def update_distribution_configuration(
    self,
    distributionConfigurationArn: str,
    distributions: List["DistributionTypeDef"],
    clientToken: str,
    description: str = None
) -> UpdateDistributionConfigurationResponseTypeDef:
    pass
```

### update_image_pipeline

Type annotations for `boto3.client("imagebuilder").update_image_pipeline` method.

[Client.update_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.update_image_pipeline)

```python
def update_image_pipeline(
    self,
    imagePipelineArn: str,
    infrastructureConfigurationArn: str,
    clientToken: str,
    description: str = None,
    imageRecipeArn: str = None,
    containerRecipeArn: str = None,
    distributionConfigurationArn: str = None,
    imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
    enhancedImageMetadataEnabled: bool = None,
    schedule: "ScheduleTypeDef" = None,
    status: PipelineStatus = None
) -> UpdateImagePipelineResponseTypeDef:
    pass
```

### update_infrastructure_configuration

Type annotations for `boto3.client("imagebuilder").update_infrastructure_configuration` method.

[Client.update_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder.Client.update_infrastructure_configuration)

```python
def update_infrastructure_configuration(
    self,
    infrastructureConfigurationArn: str,
    instanceProfileName: str,
    clientToken: str,
    description: str = None,
    instanceTypes: List[str] = None,
    securityGroupIds: List[str] = None,
    subnetId: str = None,
    logging: "LoggingTypeDef" = None,
    keyPair: str = None,
    terminateInstanceOnFailure: bool = None,
    snsTopicArn: str = None,
    resourceTags: Dict[str, str] = None
) -> UpdateInfrastructureConfigurationResponseTypeDef:
    pass
```



