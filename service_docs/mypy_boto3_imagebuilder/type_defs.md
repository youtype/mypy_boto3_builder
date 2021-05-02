# Structures for boto3 Imagebuilder module

> [Index](../index.md) > [Imagebuilder](./index.md) > Structures

Auto-generated documentation for [Imagebuilder](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html#Imagebuilder)
type annotations stubs module [mypy_boto3_imagebuilder](https://pypi.org/project/mypy-boto3-imagebuilder/).

- [Structures for boto3 Imagebuilder module](#structures-for-boto3-imagebuilder-module)
  - [AmiDistributionConfigurationTypeDef](#amidistributionconfigurationtypedef)
  - [AmiTypeDef](#amitypedef)
  - [CancelImageCreationResponseTypeDef](#cancelimagecreationresponsetypedef)
  - [ComponentConfigurationTypeDef](#componentconfigurationtypedef)
  - [ComponentSummaryTypeDef](#componentsummarytypedef)
  - [ComponentTypeDef](#componenttypedef)
  - [ComponentVersionTypeDef](#componentversiontypedef)
  - [ContainerDistributionConfigurationTypeDef](#containerdistributionconfigurationtypedef)
  - [ContainerRecipeSummaryTypeDef](#containerrecipesummarytypedef)
  - [ContainerRecipeTypeDef](#containerrecipetypedef)
  - [ContainerTypeDef](#containertypedef)
  - [CreateComponentResponseTypeDef](#createcomponentresponsetypedef)
  - [CreateContainerRecipeResponseTypeDef](#createcontainerreciperesponsetypedef)
  - [CreateDistributionConfigurationResponseTypeDef](#createdistributionconfigurationresponsetypedef)
  - [CreateImagePipelineResponseTypeDef](#createimagepipelineresponsetypedef)
  - [CreateImageRecipeResponseTypeDef](#createimagereciperesponsetypedef)
  - [CreateImageResponseTypeDef](#createimageresponsetypedef)
  - [CreateInfrastructureConfigurationResponseTypeDef](#createinfrastructureconfigurationresponsetypedef)
  - [DeleteComponentResponseTypeDef](#deletecomponentresponsetypedef)
  - [DeleteContainerRecipeResponseTypeDef](#deletecontainerreciperesponsetypedef)
  - [DeleteDistributionConfigurationResponseTypeDef](#deletedistributionconfigurationresponsetypedef)
  - [DeleteImagePipelineResponseTypeDef](#deleteimagepipelineresponsetypedef)
  - [DeleteImageRecipeResponseTypeDef](#deleteimagereciperesponsetypedef)
  - [DeleteImageResponseTypeDef](#deleteimageresponsetypedef)
  - [DeleteInfrastructureConfigurationResponseTypeDef](#deleteinfrastructureconfigurationresponsetypedef)
  - [DistributionConfigurationSummaryTypeDef](#distributionconfigurationsummarytypedef)
  - [DistributionConfigurationTypeDef](#distributionconfigurationtypedef)
  - [DistributionTypeDef](#distributiontypedef)
  - [EbsInstanceBlockDeviceSpecificationTypeDef](#ebsinstanceblockdevicespecificationtypedef)
  - [FilterTypeDef](#filtertypedef)
  - [GetComponentPolicyResponseTypeDef](#getcomponentpolicyresponsetypedef)
  - [GetComponentResponseTypeDef](#getcomponentresponsetypedef)
  - [GetContainerRecipePolicyResponseTypeDef](#getcontainerrecipepolicyresponsetypedef)
  - [GetContainerRecipeResponseTypeDef](#getcontainerreciperesponsetypedef)
  - [GetDistributionConfigurationResponseTypeDef](#getdistributionconfigurationresponsetypedef)
  - [GetImagePipelineResponseTypeDef](#getimagepipelineresponsetypedef)
  - [GetImagePolicyResponseTypeDef](#getimagepolicyresponsetypedef)
  - [GetImageRecipePolicyResponseTypeDef](#getimagerecipepolicyresponsetypedef)
  - [GetImageRecipeResponseTypeDef](#getimagereciperesponsetypedef)
  - [GetImageResponseTypeDef](#getimageresponsetypedef)
  - [GetInfrastructureConfigurationResponseTypeDef](#getinfrastructureconfigurationresponsetypedef)
  - [ImagePackageTypeDef](#imagepackagetypedef)
  - [ImagePipelineTypeDef](#imagepipelinetypedef)
  - [ImageRecipeSummaryTypeDef](#imagerecipesummarytypedef)
  - [ImageRecipeTypeDef](#imagerecipetypedef)
  - [ImageStateTypeDef](#imagestatetypedef)
  - [ImageSummaryTypeDef](#imagesummarytypedef)
  - [ImageTestsConfigurationTypeDef](#imagetestsconfigurationtypedef)
  - [ImageTypeDef](#imagetypedef)
  - [ImageVersionTypeDef](#imageversiontypedef)
  - [ImportComponentResponseTypeDef](#importcomponentresponsetypedef)
  - [InfrastructureConfigurationSummaryTypeDef](#infrastructureconfigurationsummarytypedef)
  - [InfrastructureConfigurationTypeDef](#infrastructureconfigurationtypedef)
  - [InstanceBlockDeviceMappingTypeDef](#instanceblockdevicemappingtypedef)
  - [InstanceConfigurationTypeDef](#instanceconfigurationtypedef)
  - [LaunchPermissionConfigurationTypeDef](#launchpermissionconfigurationtypedef)
  - [LaunchTemplateConfigurationTypeDef](#launchtemplateconfigurationtypedef)
  - [ListComponentBuildVersionsResponseTypeDef](#listcomponentbuildversionsresponsetypedef)
  - [ListComponentsResponseTypeDef](#listcomponentsresponsetypedef)
  - [ListContainerRecipesResponseTypeDef](#listcontainerrecipesresponsetypedef)
  - [ListDistributionConfigurationsResponseTypeDef](#listdistributionconfigurationsresponsetypedef)
  - [ListImageBuildVersionsResponseTypeDef](#listimagebuildversionsresponsetypedef)
  - [ListImagePackagesResponseTypeDef](#listimagepackagesresponsetypedef)
  - [ListImagePipelineImagesResponseTypeDef](#listimagepipelineimagesresponsetypedef)
  - [ListImagePipelinesResponseTypeDef](#listimagepipelinesresponsetypedef)
  - [ListImageRecipesResponseTypeDef](#listimagerecipesresponsetypedef)
  - [ListImagesResponseTypeDef](#listimagesresponsetypedef)
  - [ListInfrastructureConfigurationsResponseTypeDef](#listinfrastructureconfigurationsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [LoggingTypeDef](#loggingtypedef)
  - [OutputResourcesTypeDef](#outputresourcestypedef)
  - [PutComponentPolicyResponseTypeDef](#putcomponentpolicyresponsetypedef)
  - [PutContainerRecipePolicyResponseTypeDef](#putcontainerrecipepolicyresponsetypedef)
  - [PutImagePolicyResponseTypeDef](#putimagepolicyresponsetypedef)
  - [PutImageRecipePolicyResponseTypeDef](#putimagerecipepolicyresponsetypedef)
  - [S3LogsTypeDef](#s3logstypedef)
  - [ScheduleTypeDef](#scheduletypedef)
  - [StartImagePipelineExecutionResponseTypeDef](#startimagepipelineexecutionresponsetypedef)
  - [TargetContainerRepositoryTypeDef](#targetcontainerrepositorytypedef)
  - [UpdateDistributionConfigurationResponseTypeDef](#updatedistributionconfigurationresponsetypedef)
  - [UpdateImagePipelineResponseTypeDef](#updateimagepipelineresponsetypedef)
  - [UpdateInfrastructureConfigurationResponseTypeDef](#updateinfrastructureconfigurationresponsetypedef)

## AmiDistributionConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import AmiDistributionConfigurationTypeDef
```




Optional fields:
- `name`: `str`
- `description`: `str`
- `targetAccountIds`: `List[str]`
- `amiTags`: `Dict[str, str]`
- `kmsKeyId`: `str`
- `launchPermission`: `"LaunchPermissionConfigurationTypeDef"`


## AmiTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import AmiTypeDef
```




Optional fields:
- `region`: `str`
- `image`: `str`
- `name`: `str`
- `description`: `str`
- `state`: `"ImageStateTypeDef"`
- `accountId`: `str`


## CancelImageCreationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CancelImageCreationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `imageBuildVersionArn`: `str`


## ComponentConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ComponentConfigurationTypeDef
```


Required fields:
- `componentArn`: `str`




## ComponentSummaryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ComponentSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `platform`: `Platform`
- `supportedOsVersions`: `List[str]`
- `type`: `ComponentType`
- `owner`: `str`
- `description`: `str`
- `changeDescription`: `str`
- `dateCreated`: `str`
- `tags`: `Dict[str, str]`


## ComponentTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ComponentTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `description`: `str`
- `changeDescription`: `str`
- `type`: `ComponentType`
- `platform`: `Platform`
- `supportedOsVersions`: `List[str]`
- `owner`: `str`
- `data`: `str`
- `kmsKeyId`: `str`
- `encrypted`: `bool`
- `dateCreated`: `str`
- `tags`: `Dict[str, str]`


## ComponentVersionTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ComponentVersionTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `version`: `str`
- `description`: `str`
- `platform`: `Platform`
- `supportedOsVersions`: `List[str]`
- `type`: `ComponentType`
- `owner`: `str`
- `dateCreated`: `str`


## ContainerDistributionConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ContainerDistributionConfigurationTypeDef
```


Required fields:
- `targetRepository`: `"TargetContainerRepositoryTypeDef"`



Optional fields:
- `description`: `str`
- `containerTags`: `List[str]`


## ContainerRecipeSummaryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ContainerRecipeSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `containerType`: `Literal['DOCKER']`
- `name`: `str`
- `platform`: `Platform`
- `owner`: `str`
- `parentImage`: `str`
- `dateCreated`: `str`
- `tags`: `Dict[str, str]`


## ContainerRecipeTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ContainerRecipeTypeDef
```




Optional fields:
- `arn`: `str`
- `containerType`: `Literal['DOCKER']`
- `name`: `str`
- `description`: `str`
- `platform`: `Platform`
- `owner`: `str`
- `version`: `str`
- `components`: `List["ComponentConfigurationTypeDef"]`
- `instanceConfiguration`: `"InstanceConfigurationTypeDef"`
- `dockerfileTemplateData`: `str`
- `kmsKeyId`: `str`
- `encrypted`: `bool`
- `parentImage`: `str`
- `dateCreated`: `str`
- `tags`: `Dict[str, str]`
- `workingDirectory`: `str`
- `targetRepository`: `"TargetContainerRepositoryTypeDef"`


## ContainerTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ContainerTypeDef
```




Optional fields:
- `region`: `str`
- `imageUris`: `List[str]`


## CreateComponentResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateComponentResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `componentBuildVersionArn`: `str`


## CreateContainerRecipeResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateContainerRecipeResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `containerRecipeArn`: `str`


## CreateDistributionConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateDistributionConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `distributionConfigurationArn`: `str`


## CreateImagePipelineResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateImagePipelineResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `imagePipelineArn`: `str`


## CreateImageRecipeResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateImageRecipeResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `imageRecipeArn`: `str`


## CreateImageResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateImageResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `imageBuildVersionArn`: `str`


## CreateInfrastructureConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import CreateInfrastructureConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `infrastructureConfigurationArn`: `str`


## DeleteComponentResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteComponentResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `componentBuildVersionArn`: `str`


## DeleteContainerRecipeResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteContainerRecipeResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `containerRecipeArn`: `str`


## DeleteDistributionConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteDistributionConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `distributionConfigurationArn`: `str`


## DeleteImagePipelineResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteImagePipelineResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imagePipelineArn`: `str`


## DeleteImageRecipeResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteImageRecipeResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageRecipeArn`: `str`


## DeleteImageResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteImageResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageBuildVersionArn`: `str`


## DeleteInfrastructureConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DeleteInfrastructureConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `infrastructureConfigurationArn`: `str`


## DistributionConfigurationSummaryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DistributionConfigurationSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `dateCreated`: `str`
- `dateUpdated`: `str`
- `tags`: `Dict[str, str]`
- `regions`: `List[str]`


## DistributionConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DistributionConfigurationTypeDef
```


Required fields:
- `timeoutMinutes`: `int`



Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `distributions`: `List["DistributionTypeDef"]`
- `dateCreated`: `str`
- `dateUpdated`: `str`
- `tags`: `Dict[str, str]`


## DistributionTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import DistributionTypeDef
```


Required fields:
- `region`: `str`



Optional fields:
- `amiDistributionConfiguration`: `"AmiDistributionConfigurationTypeDef"`
- `containerDistributionConfiguration`: `"ContainerDistributionConfigurationTypeDef"`
- `licenseConfigurationArns`: `List[str]`
- `launchTemplateConfigurations`: `List["LaunchTemplateConfigurationTypeDef"]`


## EbsInstanceBlockDeviceSpecificationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import EbsInstanceBlockDeviceSpecificationTypeDef
```




Optional fields:
- `encrypted`: `bool`
- `deleteOnTermination`: `bool`
- `iops`: `int`
- `kmsKeyId`: `str`
- `snapshotId`: `str`
- `volumeSize`: `int`
- `volumeType`: `EbsVolumeType`


## FilterTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import FilterTypeDef
```




Optional fields:
- `name`: `str`
- `values`: `List[str]`


## GetComponentPolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetComponentPolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `policy`: `str`


## GetComponentResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetComponentResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `component`: `"ComponentTypeDef"`


## GetContainerRecipePolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetContainerRecipePolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `policy`: `str`


## GetContainerRecipeResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetContainerRecipeResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `containerRecipe`: `"ContainerRecipeTypeDef"`


## GetDistributionConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetDistributionConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `distributionConfiguration`: `"DistributionConfigurationTypeDef"`


## GetImagePipelineResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetImagePipelineResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imagePipeline`: `"ImagePipelineTypeDef"`


## GetImagePolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetImagePolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `policy`: `str`


## GetImageRecipePolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetImageRecipePolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `policy`: `str`


## GetImageRecipeResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetImageRecipeResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageRecipe`: `"ImageRecipeTypeDef"`


## GetImageResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetImageResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `image`: `"ImageTypeDef"`


## GetInfrastructureConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import GetInfrastructureConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `infrastructureConfiguration`: `"InfrastructureConfigurationTypeDef"`


## ImagePackageTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImagePackageTypeDef
```




Optional fields:
- `packageName`: `str`
- `packageVersion`: `str`


## ImagePipelineTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImagePipelineTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `platform`: `Platform`
- `enhancedImageMetadataEnabled`: `bool`
- `imageRecipeArn`: `str`
- `containerRecipeArn`: `str`
- `infrastructureConfigurationArn`: `str`
- `distributionConfigurationArn`: `str`
- `imageTestsConfiguration`: `"ImageTestsConfigurationTypeDef"`
- `schedule`: `"ScheduleTypeDef"`
- `status`: `PipelineStatus`
- `dateCreated`: `str`
- `dateUpdated`: `str`
- `dateLastRun`: `str`
- `dateNextRun`: `str`
- `tags`: `Dict[str, str]`


## ImageRecipeSummaryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageRecipeSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `platform`: `Platform`
- `owner`: `str`
- `parentImage`: `str`
- `dateCreated`: `str`
- `tags`: `Dict[str, str]`


## ImageRecipeTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageRecipeTypeDef
```




Optional fields:
- `arn`: `str`
- `type`: `ImageType`
- `name`: `str`
- `description`: `str`
- `platform`: `Platform`
- `owner`: `str`
- `version`: `str`
- `components`: `List["ComponentConfigurationTypeDef"]`
- `parentImage`: `str`
- `blockDeviceMappings`: `List["InstanceBlockDeviceMappingTypeDef"]`
- `dateCreated`: `str`
- `tags`: `Dict[str, str]`
- `workingDirectory`: `str`


## ImageStateTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageStateTypeDef
```




Optional fields:
- `status`: `ImageStatus`
- `reason`: `str`


## ImageSummaryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `ImageType`
- `version`: `str`
- `platform`: `Platform`
- `osVersion`: `str`
- `state`: `"ImageStateTypeDef"`
- `owner`: `str`
- `dateCreated`: `str`
- `outputResources`: `"OutputResourcesTypeDef"`
- `tags`: `Dict[str, str]`


## ImageTestsConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageTestsConfigurationTypeDef
```




Optional fields:
- `imageTestsEnabled`: `bool`
- `timeoutMinutes`: `int`


## ImageTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageTypeDef
```




Optional fields:
- `arn`: `str`
- `type`: `ImageType`
- `name`: `str`
- `version`: `str`
- `platform`: `Platform`
- `enhancedImageMetadataEnabled`: `bool`
- `osVersion`: `str`
- `state`: `"ImageStateTypeDef"`
- `imageRecipe`: `"ImageRecipeTypeDef"`
- `containerRecipe`: `"ContainerRecipeTypeDef"`
- `sourcePipelineName`: `str`
- `sourcePipelineArn`: `str`
- `infrastructureConfiguration`: `"InfrastructureConfigurationTypeDef"`
- `distributionConfiguration`: `"DistributionConfigurationTypeDef"`
- `imageTestsConfiguration`: `"ImageTestsConfigurationTypeDef"`
- `dateCreated`: `str`
- `outputResources`: `"OutputResourcesTypeDef"`
- `tags`: `Dict[str, str]`


## ImageVersionTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImageVersionTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `type`: `ImageType`
- `version`: `str`
- `platform`: `Platform`
- `osVersion`: `str`
- `owner`: `str`
- `dateCreated`: `str`


## ImportComponentResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ImportComponentResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `componentBuildVersionArn`: `str`


## InfrastructureConfigurationSummaryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import InfrastructureConfigurationSummaryTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `dateCreated`: `str`
- `dateUpdated`: `str`
- `resourceTags`: `Dict[str, str]`
- `tags`: `Dict[str, str]`
- `instanceTypes`: `List[str]`
- `instanceProfileName`: `str`


## InfrastructureConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import InfrastructureConfigurationTypeDef
```




Optional fields:
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `instanceTypes`: `List[str]`
- `instanceProfileName`: `str`
- `securityGroupIds`: `List[str]`
- `subnetId`: `str`
- `logging`: `"LoggingTypeDef"`
- `keyPair`: `str`
- `terminateInstanceOnFailure`: `bool`
- `snsTopicArn`: `str`
- `dateCreated`: `str`
- `dateUpdated`: `str`
- `resourceTags`: `Dict[str, str]`
- `tags`: `Dict[str, str]`


## InstanceBlockDeviceMappingTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import InstanceBlockDeviceMappingTypeDef
```




Optional fields:
- `deviceName`: `str`
- `ebs`: `"EbsInstanceBlockDeviceSpecificationTypeDef"`
- `virtualName`: `str`
- `noDevice`: `str`


## InstanceConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import InstanceConfigurationTypeDef
```




Optional fields:
- `image`: `str`
- `blockDeviceMappings`: `List["InstanceBlockDeviceMappingTypeDef"]`


## LaunchPermissionConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import LaunchPermissionConfigurationTypeDef
```




Optional fields:
- `userIds`: `List[str]`
- `userGroups`: `List[str]`


## LaunchTemplateConfigurationTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import LaunchTemplateConfigurationTypeDef
```


Required fields:
- `launchTemplateId`: `str`



Optional fields:
- `accountId`: `str`
- `setDefaultVersion`: `bool`


## ListComponentBuildVersionsResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListComponentBuildVersionsResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `componentSummaryList`: `List["ComponentSummaryTypeDef"]`
- `nextToken`: `str`


## ListComponentsResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListComponentsResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `componentVersionList`: `List["ComponentVersionTypeDef"]`
- `nextToken`: `str`


## ListContainerRecipesResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListContainerRecipesResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `containerRecipeSummaryList`: `List["ContainerRecipeSummaryTypeDef"]`
- `nextToken`: `str`


## ListDistributionConfigurationsResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListDistributionConfigurationsResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `distributionConfigurationSummaryList`: `List["DistributionConfigurationSummaryTypeDef"]`
- `nextToken`: `str`


## ListImageBuildVersionsResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListImageBuildVersionsResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageSummaryList`: `List["ImageSummaryTypeDef"]`
- `nextToken`: `str`


## ListImagePackagesResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListImagePackagesResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imagePackageList`: `List["ImagePackageTypeDef"]`
- `nextToken`: `str`


## ListImagePipelineImagesResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListImagePipelineImagesResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageSummaryList`: `List["ImageSummaryTypeDef"]`
- `nextToken`: `str`


## ListImagePipelinesResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListImagePipelinesResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imagePipelineList`: `List["ImagePipelineTypeDef"]`
- `nextToken`: `str`


## ListImageRecipesResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListImageRecipesResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageRecipeSummaryList`: `List["ImageRecipeSummaryTypeDef"]`
- `nextToken`: `str`


## ListImagesResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListImagesResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageVersionList`: `List["ImageVersionTypeDef"]`
- `nextToken`: `str`


## ListInfrastructureConfigurationsResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListInfrastructureConfigurationsResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `infrastructureConfigurationSummaryList`: `List["InfrastructureConfigurationSummaryTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## LoggingTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import LoggingTypeDef
```




Optional fields:
- `s3Logs`: `"S3LogsTypeDef"`


## OutputResourcesTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import OutputResourcesTypeDef
```




Optional fields:
- `amis`: `List["AmiTypeDef"]`
- `containers`: `List["ContainerTypeDef"]`


## PutComponentPolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import PutComponentPolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `componentArn`: `str`


## PutContainerRecipePolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import PutContainerRecipePolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `containerRecipeArn`: `str`


## PutImagePolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import PutImagePolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageArn`: `str`


## PutImageRecipePolicyResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import PutImageRecipePolicyResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `imageRecipeArn`: `str`


## S3LogsTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import S3LogsTypeDef
```




Optional fields:
- `s3BucketName`: `str`
- `s3KeyPrefix`: `str`


## ScheduleTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import ScheduleTypeDef
```




Optional fields:
- `scheduleExpression`: `str`
- `timezone`: `str`
- `pipelineExecutionStartCondition`: `PipelineExecutionStartCondition`


## StartImagePipelineExecutionResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import StartImagePipelineExecutionResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `imageBuildVersionArn`: `str`


## TargetContainerRepositoryTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import TargetContainerRepositoryTypeDef
```


Required fields:
- `service`: `Literal['ECR']`
- `repositoryName`: `str`




## UpdateDistributionConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import UpdateDistributionConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `distributionConfigurationArn`: `str`


## UpdateImagePipelineResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import UpdateImagePipelineResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `imagePipelineArn`: `str`


## UpdateInfrastructureConfigurationResponseTypeDef

```python
from mypy_boto3_imagebuilder.type_defs import UpdateInfrastructureConfigurationResponseTypeDef
```




Optional fields:
- `requestId`: `str`
- `clientToken`: `str`
- `infrastructureConfigurationArn`: `str`

