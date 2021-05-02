# Structures for boto3 CloudSearch module

> [Index](../index.md) > [CloudSearch](./index.md) > Structures

Auto-generated documentation for [CloudSearch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch)
type annotations stubs module [mypy_boto3_cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch/).

- [Structures for boto3 CloudSearch module](#structures-for-boto3-cloudsearch-module)
  - [AccessPoliciesStatusTypeDef](#accesspoliciesstatustypedef)
  - [AnalysisOptionsTypeDef](#analysisoptionstypedef)
  - [AnalysisSchemeStatusTypeDef](#analysisschemestatustypedef)
  - [AnalysisSchemeTypeDef](#analysisschemetypedef)
  - [AvailabilityOptionsStatusTypeDef](#availabilityoptionsstatustypedef)
  - [BuildSuggestersResponseTypeDef](#buildsuggestersresponsetypedef)
  - [CreateDomainResponseTypeDef](#createdomainresponsetypedef)
  - [DateArrayOptionsTypeDef](#datearrayoptionstypedef)
  - [DateOptionsTypeDef](#dateoptionstypedef)
  - [DefineAnalysisSchemeResponseTypeDef](#defineanalysisschemeresponsetypedef)
  - [DefineExpressionResponseTypeDef](#defineexpressionresponsetypedef)
  - [DefineIndexFieldResponseTypeDef](#defineindexfieldresponsetypedef)
  - [DefineSuggesterResponseTypeDef](#definesuggesterresponsetypedef)
  - [DeleteAnalysisSchemeResponseTypeDef](#deleteanalysisschemeresponsetypedef)
  - [DeleteDomainResponseTypeDef](#deletedomainresponsetypedef)
  - [DeleteExpressionResponseTypeDef](#deleteexpressionresponsetypedef)
  - [DeleteIndexFieldResponseTypeDef](#deleteindexfieldresponsetypedef)
  - [DeleteSuggesterResponseTypeDef](#deletesuggesterresponsetypedef)
  - [DescribeAnalysisSchemesResponseTypeDef](#describeanalysisschemesresponsetypedef)
  - [DescribeAvailabilityOptionsResponseTypeDef](#describeavailabilityoptionsresponsetypedef)
  - [DescribeDomainEndpointOptionsResponseTypeDef](#describedomainendpointoptionsresponsetypedef)
  - [DescribeDomainsResponseTypeDef](#describedomainsresponsetypedef)
  - [DescribeExpressionsResponseTypeDef](#describeexpressionsresponsetypedef)
  - [DescribeIndexFieldsResponseTypeDef](#describeindexfieldsresponsetypedef)
  - [DescribeScalingParametersResponseTypeDef](#describescalingparametersresponsetypedef)
  - [DescribeServiceAccessPoliciesResponseTypeDef](#describeserviceaccesspoliciesresponsetypedef)
  - [DescribeSuggestersResponseTypeDef](#describesuggestersresponsetypedef)
  - [DocumentSuggesterOptionsTypeDef](#documentsuggesteroptionstypedef)
  - [DomainEndpointOptionsStatusTypeDef](#domainendpointoptionsstatustypedef)
  - [DomainEndpointOptionsTypeDef](#domainendpointoptionstypedef)
  - [DomainStatusTypeDef](#domainstatustypedef)
  - [DoubleArrayOptionsTypeDef](#doublearrayoptionstypedef)
  - [DoubleOptionsTypeDef](#doubleoptionstypedef)
  - [ExpressionStatusTypeDef](#expressionstatustypedef)
  - [ExpressionTypeDef](#expressiontypedef)
  - [IndexDocumentsResponseTypeDef](#indexdocumentsresponsetypedef)
  - [IndexFieldStatusTypeDef](#indexfieldstatustypedef)
  - [IndexFieldTypeDef](#indexfieldtypedef)
  - [IntArrayOptionsTypeDef](#intarrayoptionstypedef)
  - [IntOptionsTypeDef](#intoptionstypedef)
  - [LatLonOptionsTypeDef](#latlonoptionstypedef)
  - [LimitsTypeDef](#limitstypedef)
  - [ListDomainNamesResponseTypeDef](#listdomainnamesresponsetypedef)
  - [LiteralArrayOptionsTypeDef](#literalarrayoptionstypedef)
  - [LiteralOptionsTypeDef](#literaloptionstypedef)
  - [OptionStatusTypeDef](#optionstatustypedef)
  - [ScalingParametersStatusTypeDef](#scalingparametersstatustypedef)
  - [ScalingParametersTypeDef](#scalingparameterstypedef)
  - [ServiceEndpointTypeDef](#serviceendpointtypedef)
  - [SuggesterStatusTypeDef](#suggesterstatustypedef)
  - [SuggesterTypeDef](#suggestertypedef)
  - [TextArrayOptionsTypeDef](#textarrayoptionstypedef)
  - [TextOptionsTypeDef](#textoptionstypedef)
  - [UpdateAvailabilityOptionsResponseTypeDef](#updateavailabilityoptionsresponsetypedef)
  - [UpdateDomainEndpointOptionsResponseTypeDef](#updatedomainendpointoptionsresponsetypedef)
  - [UpdateScalingParametersResponseTypeDef](#updatescalingparametersresponsetypedef)
  - [UpdateServiceAccessPoliciesResponseTypeDef](#updateserviceaccesspoliciesresponsetypedef)

## AccessPoliciesStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import AccessPoliciesStatusTypeDef
```


Required fields:
- `Options`: `str`
- `Status`: `"OptionStatusTypeDef"`




## AnalysisOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import AnalysisOptionsTypeDef
```




Optional fields:
- `Synonyms`: `str`
- `Stopwords`: `str`
- `StemmingDictionary`: `str`
- `JapaneseTokenizationDictionary`: `str`
- `AlgorithmicStemming`: `AlgorithmicStemming`


## AnalysisSchemeStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import AnalysisSchemeStatusTypeDef
```


Required fields:
- `Options`: `"AnalysisSchemeTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## AnalysisSchemeTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import AnalysisSchemeTypeDef
```


Required fields:
- `AnalysisSchemeName`: `str`
- `AnalysisSchemeLanguage`: `AnalysisSchemeLanguage`



Optional fields:
- `AnalysisOptions`: `"AnalysisOptionsTypeDef"`


## AvailabilityOptionsStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import AvailabilityOptionsStatusTypeDef
```


Required fields:
- `Options`: `bool`
- `Status`: `"OptionStatusTypeDef"`




## BuildSuggestersResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import BuildSuggestersResponseTypeDef
```




Optional fields:
- `FieldNames`: `List[str]`


## CreateDomainResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import CreateDomainResponseTypeDef
```




Optional fields:
- `DomainStatus`: `"DomainStatusTypeDef"`


## DateArrayOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DateArrayOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceFields`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`


## DateOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DateOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceField`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`
- `SortEnabled`: `bool`


## DefineAnalysisSchemeResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DefineAnalysisSchemeResponseTypeDef
```


Required fields:
- `AnalysisScheme`: `"AnalysisSchemeStatusTypeDef"`




## DefineExpressionResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DefineExpressionResponseTypeDef
```


Required fields:
- `Expression`: `"ExpressionStatusTypeDef"`




## DefineIndexFieldResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DefineIndexFieldResponseTypeDef
```


Required fields:
- `IndexField`: `"IndexFieldStatusTypeDef"`




## DefineSuggesterResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DefineSuggesterResponseTypeDef
```


Required fields:
- `Suggester`: `"SuggesterStatusTypeDef"`




## DeleteAnalysisSchemeResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DeleteAnalysisSchemeResponseTypeDef
```


Required fields:
- `AnalysisScheme`: `"AnalysisSchemeStatusTypeDef"`




## DeleteDomainResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DeleteDomainResponseTypeDef
```




Optional fields:
- `DomainStatus`: `"DomainStatusTypeDef"`


## DeleteExpressionResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DeleteExpressionResponseTypeDef
```


Required fields:
- `Expression`: `"ExpressionStatusTypeDef"`




## DeleteIndexFieldResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DeleteIndexFieldResponseTypeDef
```


Required fields:
- `IndexField`: `"IndexFieldStatusTypeDef"`




## DeleteSuggesterResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DeleteSuggesterResponseTypeDef
```


Required fields:
- `Suggester`: `"SuggesterStatusTypeDef"`




## DescribeAnalysisSchemesResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeAnalysisSchemesResponseTypeDef
```


Required fields:
- `AnalysisSchemes`: `List["AnalysisSchemeStatusTypeDef"]`




## DescribeAvailabilityOptionsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeAvailabilityOptionsResponseTypeDef
```




Optional fields:
- `AvailabilityOptions`: `"AvailabilityOptionsStatusTypeDef"`


## DescribeDomainEndpointOptionsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeDomainEndpointOptionsResponseTypeDef
```




Optional fields:
- `DomainEndpointOptions`: `"DomainEndpointOptionsStatusTypeDef"`


## DescribeDomainsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeDomainsResponseTypeDef
```


Required fields:
- `DomainStatusList`: `List["DomainStatusTypeDef"]`




## DescribeExpressionsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeExpressionsResponseTypeDef
```


Required fields:
- `Expressions`: `List["ExpressionStatusTypeDef"]`




## DescribeIndexFieldsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeIndexFieldsResponseTypeDef
```


Required fields:
- `IndexFields`: `List["IndexFieldStatusTypeDef"]`




## DescribeScalingParametersResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeScalingParametersResponseTypeDef
```


Required fields:
- `ScalingParameters`: `"ScalingParametersStatusTypeDef"`




## DescribeServiceAccessPoliciesResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeServiceAccessPoliciesResponseTypeDef
```


Required fields:
- `AccessPolicies`: `"AccessPoliciesStatusTypeDef"`




## DescribeSuggestersResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DescribeSuggestersResponseTypeDef
```


Required fields:
- `Suggesters`: `List["SuggesterStatusTypeDef"]`




## DocumentSuggesterOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DocumentSuggesterOptionsTypeDef
```


Required fields:
- `SourceField`: `str`



Optional fields:
- `FuzzyMatching`: `SuggesterFuzzyMatching`
- `SortExpression`: `str`


## DomainEndpointOptionsStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DomainEndpointOptionsStatusTypeDef
```


Required fields:
- `Options`: `"DomainEndpointOptionsTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## DomainEndpointOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DomainEndpointOptionsTypeDef
```




Optional fields:
- `EnforceHTTPS`: `bool`
- `TLSSecurityPolicy`: `TLSSecurityPolicy`


## DomainStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DomainStatusTypeDef
```


Required fields:
- `DomainId`: `str`
- `DomainName`: `str`
- `RequiresIndexDocuments`: `bool`



Optional fields:
- `ARN`: `str`
- `Created`: `bool`
- `Deleted`: `bool`
- `DocService`: `"ServiceEndpointTypeDef"`
- `SearchService`: `"ServiceEndpointTypeDef"`
- `Processing`: `bool`
- `SearchInstanceType`: `str`
- `SearchPartitionCount`: `int`
- `SearchInstanceCount`: `int`
- `Limits`: `"LimitsTypeDef"`


## DoubleArrayOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DoubleArrayOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `float`
- `SourceFields`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`


## DoubleOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import DoubleOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `float`
- `SourceField`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`
- `SortEnabled`: `bool`


## ExpressionStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import ExpressionStatusTypeDef
```


Required fields:
- `Options`: `"ExpressionTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## ExpressionTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import ExpressionTypeDef
```


Required fields:
- `ExpressionName`: `str`
- `ExpressionValue`: `str`




## IndexDocumentsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import IndexDocumentsResponseTypeDef
```




Optional fields:
- `FieldNames`: `List[str]`


## IndexFieldStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import IndexFieldStatusTypeDef
```


Required fields:
- `Options`: `"IndexFieldTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## IndexFieldTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import IndexFieldTypeDef
```


Required fields:
- `IndexFieldName`: `str`
- `IndexFieldType`: `IndexFieldType`



Optional fields:
- `IntOptions`: `"IntOptionsTypeDef"`
- `DoubleOptions`: `"DoubleOptionsTypeDef"`
- `LiteralOptions`: `"LiteralOptionsTypeDef"`
- `TextOptions`: `"TextOptionsTypeDef"`
- `DateOptions`: `"DateOptionsTypeDef"`
- `LatLonOptions`: `"LatLonOptionsTypeDef"`
- `IntArrayOptions`: `"IntArrayOptionsTypeDef"`
- `DoubleArrayOptions`: `"DoubleArrayOptionsTypeDef"`
- `LiteralArrayOptions`: `"LiteralArrayOptionsTypeDef"`
- `TextArrayOptions`: `"TextArrayOptionsTypeDef"`
- `DateArrayOptions`: `"DateArrayOptionsTypeDef"`


## IntArrayOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import IntArrayOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `int`
- `SourceFields`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`


## IntOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import IntOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `int`
- `SourceField`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`
- `SortEnabled`: `bool`


## LatLonOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import LatLonOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceField`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`
- `SortEnabled`: `bool`


## LimitsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import LimitsTypeDef
```


Required fields:
- `MaximumReplicationCount`: `int`
- `MaximumPartitionCount`: `int`




## ListDomainNamesResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import ListDomainNamesResponseTypeDef
```




Optional fields:
- `DomainNames`: `Dict[str, str]`


## LiteralArrayOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import LiteralArrayOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceFields`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`


## LiteralOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import LiteralOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceField`: `str`
- `FacetEnabled`: `bool`
- `SearchEnabled`: `bool`
- `ReturnEnabled`: `bool`
- `SortEnabled`: `bool`


## OptionStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import OptionStatusTypeDef
```


Required fields:
- `CreationDate`: `datetime`
- `UpdateDate`: `datetime`
- `State`: `OptionState`



Optional fields:
- `UpdateVersion`: `int`
- `PendingDeletion`: `bool`


## ScalingParametersStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import ScalingParametersStatusTypeDef
```


Required fields:
- `Options`: `"ScalingParametersTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## ScalingParametersTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import ScalingParametersTypeDef
```




Optional fields:
- `DesiredInstanceType`: `PartitionInstanceType`
- `DesiredReplicationCount`: `int`
- `DesiredPartitionCount`: `int`


## ServiceEndpointTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import ServiceEndpointTypeDef
```




Optional fields:
- `Endpoint`: `str`


## SuggesterStatusTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import SuggesterStatusTypeDef
```


Required fields:
- `Options`: `"SuggesterTypeDef"`
- `Status`: `"OptionStatusTypeDef"`




## SuggesterTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import SuggesterTypeDef
```


Required fields:
- `SuggesterName`: `str`
- `DocumentSuggesterOptions`: `"DocumentSuggesterOptionsTypeDef"`




## TextArrayOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import TextArrayOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceFields`: `str`
- `ReturnEnabled`: `bool`
- `HighlightEnabled`: `bool`
- `AnalysisScheme`: `str`


## TextOptionsTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import TextOptionsTypeDef
```




Optional fields:
- `DefaultValue`: `str`
- `SourceField`: `str`
- `ReturnEnabled`: `bool`
- `SortEnabled`: `bool`
- `HighlightEnabled`: `bool`
- `AnalysisScheme`: `str`


## UpdateAvailabilityOptionsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import UpdateAvailabilityOptionsResponseTypeDef
```




Optional fields:
- `AvailabilityOptions`: `"AvailabilityOptionsStatusTypeDef"`


## UpdateDomainEndpointOptionsResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import UpdateDomainEndpointOptionsResponseTypeDef
```




Optional fields:
- `DomainEndpointOptions`: `"DomainEndpointOptionsStatusTypeDef"`


## UpdateScalingParametersResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import UpdateScalingParametersResponseTypeDef
```


Required fields:
- `ScalingParameters`: `"ScalingParametersStatusTypeDef"`




## UpdateServiceAccessPoliciesResponseTypeDef

```python
from mypy_boto3_cloudsearch.type_defs import UpdateServiceAccessPoliciesResponseTypeDef
```


Required fields:
- `AccessPolicies`: `"AccessPoliciesStatusTypeDef"`



