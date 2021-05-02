# Structures for boto3 ServiceCatalog module

> [Index](../index.md) > [ServiceCatalog](./index.md) > Structures

Auto-generated documentation for [ServiceCatalog](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog.html#ServiceCatalog)
type annotations stubs module [mypy_boto3_servicecatalog](https://pypi.org/project/mypy-boto3-servicecatalog/).

- [Structures for boto3 ServiceCatalog module](#structures-for-boto3-servicecatalog-module)
  - [BudgetDetailTypeDef](#budgetdetailtypedef)
  - [CloudWatchDashboardTypeDef](#cloudwatchdashboardtypedef)
  - [ConstraintDetailTypeDef](#constraintdetailtypedef)
  - [ConstraintSummaryTypeDef](#constraintsummarytypedef)
  - [ExecutionParameterTypeDef](#executionparametertypedef)
  - [FailedServiceActionAssociationTypeDef](#failedserviceactionassociationtypedef)
  - [LaunchPathSummaryTypeDef](#launchpathsummarytypedef)
  - [LaunchPathTypeDef](#launchpathtypedef)
  - [OrganizationNodeTypeDef](#organizationnodetypedef)
  - [ParameterConstraintsTypeDef](#parameterconstraintstypedef)
  - [PortfolioDetailTypeDef](#portfoliodetailtypedef)
  - [PortfolioShareDetailTypeDef](#portfoliosharedetailtypedef)
  - [PrincipalTypeDef](#principaltypedef)
  - [ProductViewAggregationValueTypeDef](#productviewaggregationvaluetypedef)
  - [ProductViewDetailTypeDef](#productviewdetailtypedef)
  - [ProductViewSummaryTypeDef](#productviewsummarytypedef)
  - [ProvisionedProductAttributeTypeDef](#provisionedproductattributetypedef)
  - [ProvisionedProductDetailTypeDef](#provisionedproductdetailtypedef)
  - [ProvisionedProductPlanDetailsTypeDef](#provisionedproductplandetailstypedef)
  - [ProvisionedProductPlanSummaryTypeDef](#provisionedproductplansummarytypedef)
  - [ProvisioningArtifactDetailTypeDef](#provisioningartifactdetailtypedef)
  - [ProvisioningArtifactOutputTypeDef](#provisioningartifactoutputtypedef)
  - [ProvisioningArtifactParameterTypeDef](#provisioningartifactparametertypedef)
  - [ProvisioningArtifactPreferencesTypeDef](#provisioningartifactpreferencestypedef)
  - [ProvisioningArtifactSummaryTypeDef](#provisioningartifactsummarytypedef)
  - [ProvisioningArtifactTypeDef](#provisioningartifacttypedef)
  - [ProvisioningArtifactViewTypeDef](#provisioningartifactviewtypedef)
  - [RecordDetailTypeDef](#recorddetailtypedef)
  - [RecordErrorTypeDef](#recorderrortypedef)
  - [RecordOutputTypeDef](#recordoutputtypedef)
  - [RecordTagTypeDef](#recordtagtypedef)
  - [ResourceChangeDetailTypeDef](#resourcechangedetailtypedef)
  - [ResourceChangeTypeDef](#resourcechangetypedef)
  - [ResourceDetailTypeDef](#resourcedetailtypedef)
  - [ResourceTargetDefinitionTypeDef](#resourcetargetdefinitiontypedef)
  - [ResponseMetadata](#responsemetadata)
  - [ServiceActionDetailTypeDef](#serviceactiondetailtypedef)
  - [ServiceActionSummaryTypeDef](#serviceactionsummarytypedef)
  - [ShareDetailsTypeDef](#sharedetailstypedef)
  - [ShareErrorTypeDef](#shareerrortypedef)
  - [StackInstanceTypeDef](#stackinstancetypedef)
  - [TagOptionDetailTypeDef](#tagoptiondetailtypedef)
  - [TagOptionSummaryTypeDef](#tagoptionsummarytypedef)
  - [TagTypeDef](#tagtypedef)
  - [UpdateProvisioningParameterTypeDef](#updateprovisioningparametertypedef)
  - [UsageInstructionTypeDef](#usageinstructiontypedef)
  - [AccessLevelFilterTypeDef](#accesslevelfiltertypedef)
  - [BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef](#batchassociateserviceactionwithprovisioningartifactoutputtypedef)
  - [BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef](#batchdisassociateserviceactionfromprovisioningartifactoutputtypedef)
  - [CopyProductOutputTypeDef](#copyproductoutputtypedef)
  - [CreateConstraintOutputTypeDef](#createconstraintoutputtypedef)
  - [CreatePortfolioOutputTypeDef](#createportfoliooutputtypedef)
  - [CreatePortfolioShareOutputTypeDef](#createportfolioshareoutputtypedef)
  - [CreateProductOutputTypeDef](#createproductoutputtypedef)
  - [CreateProvisionedProductPlanOutputTypeDef](#createprovisionedproductplanoutputtypedef)
  - [CreateProvisioningArtifactOutputTypeDef](#createprovisioningartifactoutputtypedef)
  - [CreateServiceActionOutputTypeDef](#createserviceactionoutputtypedef)
  - [CreateTagOptionOutputTypeDef](#createtagoptionoutputtypedef)
  - [DeletePortfolioShareOutputTypeDef](#deleteportfolioshareoutputtypedef)
  - [DescribeConstraintOutputTypeDef](#describeconstraintoutputtypedef)
  - [DescribeCopyProductStatusOutputTypeDef](#describecopyproductstatusoutputtypedef)
  - [DescribePortfolioOutputTypeDef](#describeportfoliooutputtypedef)
  - [DescribePortfolioShareStatusOutputTypeDef](#describeportfoliosharestatusoutputtypedef)
  - [DescribePortfolioSharesOutputTypeDef](#describeportfoliosharesoutputtypedef)
  - [DescribeProductAsAdminOutputTypeDef](#describeproductasadminoutputtypedef)
  - [DescribeProductOutputTypeDef](#describeproductoutputtypedef)
  - [DescribeProductViewOutputTypeDef](#describeproductviewoutputtypedef)
  - [DescribeProvisionedProductOutputTypeDef](#describeprovisionedproductoutputtypedef)
  - [DescribeProvisionedProductPlanOutputTypeDef](#describeprovisionedproductplanoutputtypedef)
  - [DescribeProvisioningArtifactOutputTypeDef](#describeprovisioningartifactoutputtypedef)
  - [DescribeProvisioningParametersOutputTypeDef](#describeprovisioningparametersoutputtypedef)
  - [DescribeRecordOutputTypeDef](#describerecordoutputtypedef)
  - [DescribeServiceActionExecutionParametersOutputTypeDef](#describeserviceactionexecutionparametersoutputtypedef)
  - [DescribeServiceActionOutputTypeDef](#describeserviceactionoutputtypedef)
  - [DescribeTagOptionOutputTypeDef](#describetagoptionoutputtypedef)
  - [ExecuteProvisionedProductPlanOutputTypeDef](#executeprovisionedproductplanoutputtypedef)
  - [ExecuteProvisionedProductServiceActionOutputTypeDef](#executeprovisionedproductserviceactionoutputtypedef)
  - [GetAWSOrganizationsAccessStatusOutputTypeDef](#getawsorganizationsaccessstatusoutputtypedef)
  - [GetProvisionedProductOutputsOutputTypeDef](#getprovisionedproductoutputsoutputtypedef)
  - [ImportAsProvisionedProductOutputTypeDef](#importasprovisionedproductoutputtypedef)
  - [ListAcceptedPortfolioSharesOutputTypeDef](#listacceptedportfoliosharesoutputtypedef)
  - [ListBudgetsForResourceOutputTypeDef](#listbudgetsforresourceoutputtypedef)
  - [ListConstraintsForPortfolioOutputTypeDef](#listconstraintsforportfoliooutputtypedef)
  - [ListLaunchPathsOutputTypeDef](#listlaunchpathsoutputtypedef)
  - [ListOrganizationPortfolioAccessOutputTypeDef](#listorganizationportfolioaccessoutputtypedef)
  - [ListPortfolioAccessOutputTypeDef](#listportfolioaccessoutputtypedef)
  - [ListPortfoliosForProductOutputTypeDef](#listportfoliosforproductoutputtypedef)
  - [ListPortfoliosOutputTypeDef](#listportfoliosoutputtypedef)
  - [ListPrincipalsForPortfolioOutputTypeDef](#listprincipalsforportfoliooutputtypedef)
  - [ListProvisionedProductPlansOutputTypeDef](#listprovisionedproductplansoutputtypedef)
  - [ListProvisioningArtifactsForServiceActionOutputTypeDef](#listprovisioningartifactsforserviceactionoutputtypedef)
  - [ListProvisioningArtifactsOutputTypeDef](#listprovisioningartifactsoutputtypedef)
  - [ListRecordHistoryOutputTypeDef](#listrecordhistoryoutputtypedef)
  - [ListRecordHistorySearchFilterTypeDef](#listrecordhistorysearchfiltertypedef)
  - [ListResourcesForTagOptionOutputTypeDef](#listresourcesfortagoptionoutputtypedef)
  - [ListServiceActionsForProvisioningArtifactOutputTypeDef](#listserviceactionsforprovisioningartifactoutputtypedef)
  - [ListServiceActionsOutputTypeDef](#listserviceactionsoutputtypedef)
  - [ListStackInstancesForProvisionedProductOutputTypeDef](#liststackinstancesforprovisionedproductoutputtypedef)
  - [ListTagOptionsFiltersTypeDef](#listtagoptionsfilterstypedef)
  - [ListTagOptionsOutputTypeDef](#listtagoptionsoutputtypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ProvisionProductOutputTypeDef](#provisionproductoutputtypedef)
  - [ProvisioningArtifactPropertiesTypeDef](#provisioningartifactpropertiestypedef)
  - [ProvisioningParameterTypeDef](#provisioningparametertypedef)
  - [ProvisioningPreferencesTypeDef](#provisioningpreferencestypedef)
  - [ScanProvisionedProductsOutputTypeDef](#scanprovisionedproductsoutputtypedef)
  - [SearchProductsAsAdminOutputTypeDef](#searchproductsasadminoutputtypedef)
  - [SearchProductsOutputTypeDef](#searchproductsoutputtypedef)
  - [SearchProvisionedProductsOutputTypeDef](#searchprovisionedproductsoutputtypedef)
  - [ServiceActionAssociationTypeDef](#serviceactionassociationtypedef)
  - [TerminateProvisionedProductOutputTypeDef](#terminateprovisionedproductoutputtypedef)
  - [UpdateConstraintOutputTypeDef](#updateconstraintoutputtypedef)
  - [UpdatePortfolioOutputTypeDef](#updateportfoliooutputtypedef)
  - [UpdatePortfolioShareOutputTypeDef](#updateportfolioshareoutputtypedef)
  - [UpdateProductOutputTypeDef](#updateproductoutputtypedef)
  - [UpdateProvisionedProductOutputTypeDef](#updateprovisionedproductoutputtypedef)
  - [UpdateProvisionedProductPropertiesOutputTypeDef](#updateprovisionedproductpropertiesoutputtypedef)
  - [UpdateProvisioningArtifactOutputTypeDef](#updateprovisioningartifactoutputtypedef)
  - [UpdateProvisioningPreferencesTypeDef](#updateprovisioningpreferencestypedef)
  - [UpdateServiceActionOutputTypeDef](#updateserviceactionoutputtypedef)
  - [UpdateTagOptionOutputTypeDef](#updatetagoptionoutputtypedef)

## BudgetDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import BudgetDetailTypeDef
```




Optional fields:
- `BudgetName`: `str`


## CloudWatchDashboardTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CloudWatchDashboardTypeDef
```




Optional fields:
- `Name`: `str`


## ConstraintDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ConstraintDetailTypeDef
```




Optional fields:
- `ConstraintId`: `str`
- `Type`: `str`
- `Description`: `str`
- `Owner`: `str`
- `ProductId`: `str`
- `PortfolioId`: `str`


## ConstraintSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ConstraintSummaryTypeDef
```




Optional fields:
- `Type`: `str`
- `Description`: `str`


## ExecutionParameterTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ExecutionParameterTypeDef
```




Optional fields:
- `Name`: `str`
- `Type`: `str`
- `DefaultValues`: `List[str]`


## FailedServiceActionAssociationTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import FailedServiceActionAssociationTypeDef
```




Optional fields:
- `ServiceActionId`: `str`
- `ProductId`: `str`
- `ProvisioningArtifactId`: `str`
- `ErrorCode`: `ServiceActionAssociationErrorCode`
- `ErrorMessage`: `str`


## LaunchPathSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import LaunchPathSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `ConstraintSummaries`: `List["ConstraintSummaryTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `Name`: `str`


## LaunchPathTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import LaunchPathTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`


## OrganizationNodeTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import OrganizationNodeTypeDef
```




Optional fields:
- `Type`: `OrganizationNodeType`
- `Value`: `str`


## ParameterConstraintsTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ParameterConstraintsTypeDef
```




Optional fields:
- `AllowedValues`: `List[str]`
- `AllowedPattern`: `str`
- `ConstraintDescription`: `str`
- `MaxLength`: `str`
- `MinLength`: `str`
- `MaxValue`: `str`
- `MinValue`: `str`


## PortfolioDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import PortfolioDetailTypeDef
```




Optional fields:
- `Id`: `str`
- `ARN`: `str`
- `DisplayName`: `str`
- `Description`: `str`
- `CreatedTime`: `datetime`
- `ProviderName`: `str`


## PortfolioShareDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import PortfolioShareDetailTypeDef
```




Optional fields:
- `PrincipalId`: `str`
- `Type`: `DescribePortfolioShareType`
- `Accepted`: `bool`
- `ShareTagOptions`: `bool`


## PrincipalTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import PrincipalTypeDef
```




Optional fields:
- `PrincipalARN`: `str`
- `PrincipalType`: `PrincipalType`


## ProductViewAggregationValueTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProductViewAggregationValueTypeDef
```




Optional fields:
- `Value`: `str`
- `ApproximateCount`: `int`


## ProductViewDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProductViewDetailTypeDef
```




Optional fields:
- `ProductViewSummary`: `"ProductViewSummaryTypeDef"`
- `Status`: `Status`
- `ProductARN`: `str`
- `CreatedTime`: `datetime`


## ProductViewSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProductViewSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `ProductId`: `str`
- `Name`: `str`
- `Owner`: `str`
- `ShortDescription`: `str`
- `Type`: `ProductType`
- `Distributor`: `str`
- `HasDefaultPath`: `bool`
- `SupportEmail`: `str`
- `SupportDescription`: `str`
- `SupportUrl`: `str`


## ProvisionedProductAttributeTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisionedProductAttributeTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `Type`: `str`
- `Id`: `str`
- `Status`: `ProvisionedProductStatus`
- `StatusMessage`: `str`
- `CreatedTime`: `datetime`
- `IdempotencyToken`: `str`
- `LastRecordId`: `str`
- `LastProvisioningRecordId`: `str`
- `LastSuccessfulProvisioningRecordId`: `str`
- `Tags`: `List["TagTypeDef"]`
- `PhysicalId`: `str`
- `ProductId`: `str`
- `ProductName`: `str`
- `ProvisioningArtifactId`: `str`
- `ProvisioningArtifactName`: `str`
- `UserArn`: `str`
- `UserArnSession`: `str`


## ProvisionedProductDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisionedProductDetailTypeDef
```




Optional fields:
- `Name`: `str`
- `Arn`: `str`
- `Type`: `str`
- `Id`: `str`
- `Status`: `ProvisionedProductStatus`
- `StatusMessage`: `str`
- `CreatedTime`: `datetime`
- `IdempotencyToken`: `str`
- `LastRecordId`: `str`
- `LastProvisioningRecordId`: `str`
- `LastSuccessfulProvisioningRecordId`: `str`
- `ProductId`: `str`
- `ProvisioningArtifactId`: `str`
- `LaunchRoleArn`: `str`


## ProvisionedProductPlanDetailsTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisionedProductPlanDetailsTypeDef
```




Optional fields:
- `CreatedTime`: `datetime`
- `PathId`: `str`
- `ProductId`: `str`
- `PlanName`: `str`
- `PlanId`: `str`
- `ProvisionProductId`: `str`
- `ProvisionProductName`: `str`
- `PlanType`: `ProvisionedProductPlanType`
- `ProvisioningArtifactId`: `str`
- `Status`: `ProvisionedProductPlanStatus`
- `UpdatedTime`: `datetime`
- `NotificationArns`: `List[str]`
- `ProvisioningParameters`: `List["UpdateProvisioningParameterTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `StatusMessage`: `str`


## ProvisionedProductPlanSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisionedProductPlanSummaryTypeDef
```




Optional fields:
- `PlanName`: `str`
- `PlanId`: `str`
- `ProvisionProductId`: `str`
- `ProvisionProductName`: `str`
- `PlanType`: `ProvisionedProductPlanType`
- `ProvisioningArtifactId`: `str`


## ProvisioningArtifactDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactDetailTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `Type`: `ProvisioningArtifactType`
- `CreatedTime`: `datetime`
- `Active`: `bool`
- `Guidance`: `ProvisioningArtifactGuidance`


## ProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactOutputTypeDef
```




Optional fields:
- `Key`: `str`
- `Description`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ProvisioningArtifactParameterTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactParameterTypeDef
```




Optional fields:
- `ParameterKey`: `str`
- `DefaultValue`: `str`
- `ParameterType`: `str`
- `IsNoEcho`: `bool`
- `Description`: `str`
- `ParameterConstraints`: `"ParameterConstraintsTypeDef"`


## ProvisioningArtifactPreferencesTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactPreferencesTypeDef
```




Optional fields:
- `StackSetAccounts`: `List[str]`
- `StackSetRegions`: `List[str]`


## ProvisioningArtifactSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `CreatedTime`: `datetime`
- `ProvisioningArtifactMetadata`: `Dict[str, str]`


## ProvisioningArtifactTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `CreatedTime`: `datetime`
- `Guidance`: `ProvisioningArtifactGuidance`


## ProvisioningArtifactViewTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactViewTypeDef
```




Optional fields:
- `ProductViewSummary`: `"ProductViewSummaryTypeDef"`
- `ProvisioningArtifact`: `"ProvisioningArtifactTypeDef"`


## RecordDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import RecordDetailTypeDef
```




Optional fields:
- `RecordId`: `str`
- `ProvisionedProductName`: `str`
- `Status`: `RecordStatus`
- `CreatedTime`: `datetime`
- `UpdatedTime`: `datetime`
- `ProvisionedProductType`: `str`
- `RecordType`: `str`
- `ProvisionedProductId`: `str`
- `ProductId`: `str`
- `ProvisioningArtifactId`: `str`
- `PathId`: `str`
- `RecordErrors`: `List["RecordErrorTypeDef"]`
- `RecordTags`: `List["RecordTagTypeDef"]`
- `LaunchRoleArn`: `str`


## RecordErrorTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import RecordErrorTypeDef
```




Optional fields:
- `Code`: `str`
- `Description`: `str`


## RecordOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import RecordOutputTypeDef
```




Optional fields:
- `OutputKey`: `str`
- `OutputValue`: `str`
- `Description`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## RecordTagTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import RecordTagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## ResourceChangeDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ResourceChangeDetailTypeDef
```




Optional fields:
- `Target`: `"ResourceTargetDefinitionTypeDef"`
- `Evaluation`: `EvaluationType`
- `CausingEntity`: `str`


## ResourceChangeTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ResourceChangeTypeDef
```




Optional fields:
- `Action`: `ChangeAction`
- `LogicalResourceId`: `str`
- `PhysicalResourceId`: `str`
- `ResourceType`: `str`
- `Replacement`: `Replacement`
- `Scope`: `List[ResourceAttribute]`
- `Details`: `List["ResourceChangeDetailTypeDef"]`


## ResourceDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ResourceDetailTypeDef
```




Optional fields:
- `Id`: `str`
- `ARN`: `str`
- `Name`: `str`
- `Description`: `str`
- `CreatedTime`: `datetime`


## ResourceTargetDefinitionTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ResourceTargetDefinitionTypeDef
```




Optional fields:
- `Attribute`: `ResourceAttribute`
- `Name`: `str`
- `RequiresRecreation`: `RequiresRecreation`


## ResponseMetadata

```python
from mypy_boto3_servicecatalog.type_defs import ResponseMetadata
```


Required fields:
- `RequestId`: `str`
- `HostId`: `str`
- `HTTPStatusCode`: `int`
- `HTTPHeaders`: `Dict[str, Any]`
- `RetryAttempts`: `int`




## ServiceActionDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ServiceActionDetailTypeDef
```




Optional fields:
- `ServiceActionSummary`: `"ServiceActionSummaryTypeDef"`
- `Definition`: `Dict[ServiceActionDefinitionKey, str]`


## ServiceActionSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ServiceActionSummaryTypeDef
```




Optional fields:
- `Id`: `str`
- `Name`: `str`
- `Description`: `str`
- `DefinitionType`: `ServiceActionDefinitionType`


## ShareDetailsTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ShareDetailsTypeDef
```




Optional fields:
- `SuccessfulShares`: `List[str]`
- `ShareErrors`: `List["ShareErrorTypeDef"]`


## ShareErrorTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ShareErrorTypeDef
```




Optional fields:
- `Accounts`: `List[str]`
- `Message`: `str`
- `Error`: `str`


## StackInstanceTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import StackInstanceTypeDef
```




Optional fields:
- `Account`: `str`
- `Region`: `str`
- `StackInstanceStatus`: `StackInstanceStatus`


## TagOptionDetailTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import TagOptionDetailTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `Active`: `bool`
- `Id`: `str`
- `Owner`: `str`


## TagOptionSummaryTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import TagOptionSummaryTypeDef
```




Optional fields:
- `Key`: `str`
- `Values`: `List[str]`


## TagTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import TagTypeDef
```


Required fields:
- `Key`: `str`
- `Value`: `str`




## UpdateProvisioningParameterTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateProvisioningParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `UsePreviousValue`: `bool`


## UsageInstructionTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UsageInstructionTypeDef
```




Optional fields:
- `Type`: `str`
- `Value`: `str`


## AccessLevelFilterTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import AccessLevelFilterTypeDef
```




Optional fields:
- `Key`: `AccessLevelFilterKey`
- `Value`: `str`


## BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef
```




Optional fields:
- `FailedServiceActionAssociations`: `List["FailedServiceActionAssociationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef
```




Optional fields:
- `FailedServiceActionAssociations`: `List["FailedServiceActionAssociationTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CopyProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CopyProductOutputTypeDef
```




Optional fields:
- `CopyProductToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateConstraintOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreateConstraintOutputTypeDef
```




Optional fields:
- `ConstraintDetail`: `"ConstraintDetailTypeDef"`
- `ConstraintParameters`: `str`
- `Status`: `Status`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePortfolioOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreatePortfolioOutputTypeDef
```




Optional fields:
- `PortfolioDetail`: `"PortfolioDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreatePortfolioShareOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreatePortfolioShareOutputTypeDef
```




Optional fields:
- `PortfolioShareToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreateProductOutputTypeDef
```




Optional fields:
- `ProductViewDetail`: `"ProductViewDetailTypeDef"`
- `ProvisioningArtifactDetail`: `"ProvisioningArtifactDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateProvisionedProductPlanOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreateProvisionedProductPlanOutputTypeDef
```




Optional fields:
- `PlanName`: `str`
- `PlanId`: `str`
- `ProvisionProductId`: `str`
- `ProvisionedProductName`: `str`
- `ProvisioningArtifactId`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreateProvisioningArtifactOutputTypeDef
```




Optional fields:
- `ProvisioningArtifactDetail`: `"ProvisioningArtifactDetailTypeDef"`
- `Info`: `Dict[str, str]`
- `Status`: `Status`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateServiceActionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreateServiceActionOutputTypeDef
```




Optional fields:
- `ServiceActionDetail`: `"ServiceActionDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## CreateTagOptionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import CreateTagOptionOutputTypeDef
```




Optional fields:
- `TagOptionDetail`: `"TagOptionDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DeletePortfolioShareOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DeletePortfolioShareOutputTypeDef
```




Optional fields:
- `PortfolioShareToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeConstraintOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeConstraintOutputTypeDef
```




Optional fields:
- `ConstraintDetail`: `"ConstraintDetailTypeDef"`
- `ConstraintParameters`: `str`
- `Status`: `Status`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeCopyProductStatusOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeCopyProductStatusOutputTypeDef
```




Optional fields:
- `CopyProductStatus`: `CopyProductStatus`
- `TargetProductId`: `str`
- `StatusDetail`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePortfolioOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribePortfolioOutputTypeDef
```




Optional fields:
- `PortfolioDetail`: `"PortfolioDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `TagOptions`: `List["TagOptionDetailTypeDef"]`
- `Budgets`: `List["BudgetDetailTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePortfolioShareStatusOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribePortfolioShareStatusOutputTypeDef
```




Optional fields:
- `PortfolioShareToken`: `str`
- `PortfolioId`: `str`
- `OrganizationNodeValue`: `str`
- `Status`: `ShareStatus`
- `ShareDetails`: `"ShareDetailsTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribePortfolioSharesOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribePortfolioSharesOutputTypeDef
```




Optional fields:
- `NextPageToken`: `str`
- `PortfolioShareDetails`: `List["PortfolioShareDetailTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProductAsAdminOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProductAsAdminOutputTypeDef
```




Optional fields:
- `ProductViewDetail`: `"ProductViewDetailTypeDef"`
- `ProvisioningArtifactSummaries`: `List["ProvisioningArtifactSummaryTypeDef"]`
- `Tags`: `List["TagTypeDef"]`
- `TagOptions`: `List["TagOptionDetailTypeDef"]`
- `Budgets`: `List["BudgetDetailTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProductOutputTypeDef
```




Optional fields:
- `ProductViewSummary`: `"ProductViewSummaryTypeDef"`
- `ProvisioningArtifacts`: `List["ProvisioningArtifactTypeDef"]`
- `Budgets`: `List["BudgetDetailTypeDef"]`
- `LaunchPaths`: `List["LaunchPathTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProductViewOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProductViewOutputTypeDef
```




Optional fields:
- `ProductViewSummary`: `"ProductViewSummaryTypeDef"`
- `ProvisioningArtifacts`: `List["ProvisioningArtifactTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProvisionedProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProvisionedProductOutputTypeDef
```




Optional fields:
- `ProvisionedProductDetail`: `"ProvisionedProductDetailTypeDef"`
- `CloudWatchDashboards`: `List["CloudWatchDashboardTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProvisionedProductPlanOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProvisionedProductPlanOutputTypeDef
```




Optional fields:
- `ProvisionedProductPlanDetails`: `"ProvisionedProductPlanDetailsTypeDef"`
- `ResourceChanges`: `List["ResourceChangeTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProvisioningArtifactOutputTypeDef
```




Optional fields:
- `ProvisioningArtifactDetail`: `"ProvisioningArtifactDetailTypeDef"`
- `Info`: `Dict[str, str]`
- `Status`: `Status`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeProvisioningParametersOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeProvisioningParametersOutputTypeDef
```




Optional fields:
- `ProvisioningArtifactParameters`: `List["ProvisioningArtifactParameterTypeDef"]`
- `ConstraintSummaries`: `List["ConstraintSummaryTypeDef"]`
- `UsageInstructions`: `List["UsageInstructionTypeDef"]`
- `TagOptions`: `List["TagOptionSummaryTypeDef"]`
- `ProvisioningArtifactPreferences`: `"ProvisioningArtifactPreferencesTypeDef"`
- `ProvisioningArtifactOutputs`: `List["ProvisioningArtifactOutputTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeRecordOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeRecordOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `RecordOutputs`: `List["RecordOutputTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeServiceActionExecutionParametersOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeServiceActionExecutionParametersOutputTypeDef
```




Optional fields:
- `ServiceActionParameters`: `List["ExecutionParameterTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeServiceActionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeServiceActionOutputTypeDef
```




Optional fields:
- `ServiceActionDetail`: `"ServiceActionDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## DescribeTagOptionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import DescribeTagOptionOutputTypeDef
```




Optional fields:
- `TagOptionDetail`: `"TagOptionDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ExecuteProvisionedProductPlanOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ExecuteProvisionedProductPlanOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ExecuteProvisionedProductServiceActionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ExecuteProvisionedProductServiceActionOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetAWSOrganizationsAccessStatusOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import GetAWSOrganizationsAccessStatusOutputTypeDef
```




Optional fields:
- `AccessStatus`: `AccessStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## GetProvisionedProductOutputsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import GetProvisionedProductOutputsOutputTypeDef
```




Optional fields:
- `Outputs`: `List["RecordOutputTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ImportAsProvisionedProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ImportAsProvisionedProductOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListAcceptedPortfolioSharesOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListAcceptedPortfolioSharesOutputTypeDef
```




Optional fields:
- `PortfolioDetails`: `List["PortfolioDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListBudgetsForResourceOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListBudgetsForResourceOutputTypeDef
```




Optional fields:
- `Budgets`: `List["BudgetDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListConstraintsForPortfolioOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListConstraintsForPortfolioOutputTypeDef
```




Optional fields:
- `ConstraintDetails`: `List["ConstraintDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListLaunchPathsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListLaunchPathsOutputTypeDef
```




Optional fields:
- `LaunchPathSummaries`: `List["LaunchPathSummaryTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListOrganizationPortfolioAccessOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListOrganizationPortfolioAccessOutputTypeDef
```




Optional fields:
- `OrganizationNodes`: `List["OrganizationNodeTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPortfolioAccessOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListPortfolioAccessOutputTypeDef
```




Optional fields:
- `AccountIds`: `List[str]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPortfoliosForProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListPortfoliosForProductOutputTypeDef
```




Optional fields:
- `PortfolioDetails`: `List["PortfolioDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPortfoliosOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListPortfoliosOutputTypeDef
```




Optional fields:
- `PortfolioDetails`: `List["PortfolioDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListPrincipalsForPortfolioOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListPrincipalsForPortfolioOutputTypeDef
```




Optional fields:
- `Principals`: `List["PrincipalTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProvisionedProductPlansOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListProvisionedProductPlansOutputTypeDef
```




Optional fields:
- `ProvisionedProductPlans`: `List["ProvisionedProductPlanSummaryTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProvisioningArtifactsForServiceActionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListProvisioningArtifactsForServiceActionOutputTypeDef
```




Optional fields:
- `ProvisioningArtifactViews`: `List["ProvisioningArtifactViewTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListProvisioningArtifactsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListProvisioningArtifactsOutputTypeDef
```




Optional fields:
- `ProvisioningArtifactDetails`: `List["ProvisioningArtifactDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRecordHistoryOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListRecordHistoryOutputTypeDef
```




Optional fields:
- `RecordDetails`: `List["RecordDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListRecordHistorySearchFilterTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListRecordHistorySearchFilterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## ListResourcesForTagOptionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListResourcesForTagOptionOutputTypeDef
```




Optional fields:
- `ResourceDetails`: `List["ResourceDetailTypeDef"]`
- `PageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListServiceActionsForProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListServiceActionsForProvisioningArtifactOutputTypeDef
```




Optional fields:
- `ServiceActionSummaries`: `List["ServiceActionSummaryTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListServiceActionsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListServiceActionsOutputTypeDef
```




Optional fields:
- `ServiceActionSummaries`: `List["ServiceActionSummaryTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListStackInstancesForProvisionedProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListStackInstancesForProvisionedProductOutputTypeDef
```




Optional fields:
- `StackInstances`: `List["StackInstanceTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ListTagOptionsFiltersTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListTagOptionsFiltersTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`
- `Active`: `bool`


## ListTagOptionsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ListTagOptionsOutputTypeDef
```




Optional fields:
- `TagOptionDetails`: `List["TagOptionDetailTypeDef"]`
- `PageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## PaginatorConfigTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ProvisionProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisionProductOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## ProvisioningArtifactPropertiesTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningArtifactPropertiesTypeDef
```


Required fields:
- `Info`: `Dict[str, str]`



Optional fields:
- `Name`: `str`
- `Description`: `str`
- `Type`: `ProvisioningArtifactType`
- `DisableTemplateValidation`: `bool`


## ProvisioningParameterTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningParameterTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## ProvisioningPreferencesTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ProvisioningPreferencesTypeDef
```




Optional fields:
- `StackSetAccounts`: `List[str]`
- `StackSetRegions`: `List[str]`
- `StackSetFailureToleranceCount`: `int`
- `StackSetFailureTolerancePercentage`: `int`
- `StackSetMaxConcurrencyCount`: `int`
- `StackSetMaxConcurrencyPercentage`: `int`


## ScanProvisionedProductsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ScanProvisionedProductsOutputTypeDef
```




Optional fields:
- `ProvisionedProducts`: `List["ProvisionedProductDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## SearchProductsAsAdminOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import SearchProductsAsAdminOutputTypeDef
```




Optional fields:
- `ProductViewDetails`: `List["ProductViewDetailTypeDef"]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## SearchProductsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import SearchProductsOutputTypeDef
```




Optional fields:
- `ProductViewSummaries`: `List["ProductViewSummaryTypeDef"]`
- `ProductViewAggregations`: `Dict[str, List["ProductViewAggregationValueTypeDef"]]`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## SearchProvisionedProductsOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import SearchProvisionedProductsOutputTypeDef
```




Optional fields:
- `ProvisionedProducts`: `List["ProvisionedProductAttributeTypeDef"]`
- `TotalResultsCount`: `int`
- `NextPageToken`: `str`
- `ResponseMetadata`: `"ResponseMetadata"`


## ServiceActionAssociationTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import ServiceActionAssociationTypeDef
```


Required fields:
- `ServiceActionId`: `str`
- `ProductId`: `str`
- `ProvisioningArtifactId`: `str`




## TerminateProvisionedProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import TerminateProvisionedProductOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateConstraintOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateConstraintOutputTypeDef
```




Optional fields:
- `ConstraintDetail`: `"ConstraintDetailTypeDef"`
- `ConstraintParameters`: `str`
- `Status`: `Status`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdatePortfolioOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdatePortfolioOutputTypeDef
```




Optional fields:
- `PortfolioDetail`: `"PortfolioDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdatePortfolioShareOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdatePortfolioShareOutputTypeDef
```




Optional fields:
- `PortfolioShareToken`: `str`
- `Status`: `ShareStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateProductOutputTypeDef
```




Optional fields:
- `ProductViewDetail`: `"ProductViewDetailTypeDef"`
- `Tags`: `List["TagTypeDef"]`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateProvisionedProductOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateProvisionedProductOutputTypeDef
```




Optional fields:
- `RecordDetail`: `"RecordDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateProvisionedProductPropertiesOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateProvisionedProductPropertiesOutputTypeDef
```




Optional fields:
- `ProvisionedProductId`: `str`
- `ProvisionedProductProperties`: `Dict[PropertyKey, str]`
- `RecordId`: `str`
- `Status`: `RecordStatus`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateProvisioningArtifactOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateProvisioningArtifactOutputTypeDef
```




Optional fields:
- `ProvisioningArtifactDetail`: `"ProvisioningArtifactDetailTypeDef"`
- `Info`: `Dict[str, str]`
- `Status`: `Status`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateProvisioningPreferencesTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateProvisioningPreferencesTypeDef
```




Optional fields:
- `StackSetAccounts`: `List[str]`
- `StackSetRegions`: `List[str]`
- `StackSetFailureToleranceCount`: `int`
- `StackSetFailureTolerancePercentage`: `int`
- `StackSetMaxConcurrencyCount`: `int`
- `StackSetMaxConcurrencyPercentage`: `int`
- `StackSetOperationType`: `StackSetOperationType`


## UpdateServiceActionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateServiceActionOutputTypeDef
```




Optional fields:
- `ServiceActionDetail`: `"ServiceActionDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`


## UpdateTagOptionOutputTypeDef

```python
from mypy_boto3_servicecatalog.type_defs import UpdateTagOptionOutputTypeDef
```




Optional fields:
- `TagOptionDetail`: `"TagOptionDetailTypeDef"`
- `ResponseMetadata`: `"ResponseMetadata"`

