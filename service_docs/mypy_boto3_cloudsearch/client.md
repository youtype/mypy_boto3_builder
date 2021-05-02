# CloudSearchClient for boto3 CloudSearch module

> [Index](../index.md) > [CloudSearch](./index.md) > CloudSearchClient

Auto-generated documentation for [CloudSearch](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch)
type annotations stubs module [mypy_boto3_cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch/).

- [CloudSearchClient for boto3 CloudSearch module](#cloudsearchclient-for-boto3-cloudsearch-module)
  - [CloudSearchClient](#cloudsearchclient)
  - [Exceptions](#exceptions)
  - [Methods](#methods)
    - [build_suggesters](#build_suggesters)
    - [can_paginate](#can_paginate)
    - [create_domain](#create_domain)
    - [define_analysis_scheme](#define_analysis_scheme)
    - [define_expression](#define_expression)
    - [define_index_field](#define_index_field)
    - [define_suggester](#define_suggester)
    - [delete_analysis_scheme](#delete_analysis_scheme)
    - [delete_domain](#delete_domain)
    - [delete_expression](#delete_expression)
    - [delete_index_field](#delete_index_field)
    - [delete_suggester](#delete_suggester)
    - [describe_analysis_schemes](#describe_analysis_schemes)
    - [describe_availability_options](#describe_availability_options)
    - [describe_domain_endpoint_options](#describe_domain_endpoint_options)
    - [describe_domains](#describe_domains)
    - [describe_expressions](#describe_expressions)
    - [describe_index_fields](#describe_index_fields)
    - [describe_scaling_parameters](#describe_scaling_parameters)
    - [describe_service_access_policies](#describe_service_access_policies)
    - [describe_suggesters](#describe_suggesters)
    - [generate_presigned_url](#generate_presigned_url)
    - [index_documents](#index_documents)
    - [list_domain_names](#list_domain_names)
    - [update_availability_options](#update_availability_options)
    - [update_domain_endpoint_options](#update_domain_endpoint_options)
    - [update_scaling_parameters](#update_scaling_parameters)
    - [update_service_access_policies](#update_service_access_policies)

## CloudSearchClient

Type annotations for `boto3.client("cloudsearch")`

Can be used directly:

```python
from mypy_boto3_cloudsearch.client import CloudSearchClient
```

## Exceptions


`boto3` client exceptions are generated in runtime. This class can be used for static analysis directly:

```python
from mypy_boto3_cloudsearch.client import Exceptions

def handle_error(exc: Exceptions.BaseException) -> None:
    ...
```


Exceptions:

- `Exceptions.BaseException`
- `Exceptions.ClientError`
- `Exceptions.DisabledOperationException`
- `Exceptions.InternalException`
- `Exceptions.InvalidTypeException`
- `Exceptions.LimitExceededException`
- `Exceptions.ResourceNotFoundException`
- `Exceptions.ValidationException`


## Methods


### build_suggesters

Type annotations for `boto3.client("cloudsearch").build_suggesters` method.

[Client.build_suggesters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.build_suggesters)

```python
def build_suggesters(
    self,
    DomainName: str
) -> BuildSuggestersResponseTypeDef:
    pass
```

### can_paginate

Type annotations for `boto3.client("cloudsearch").can_paginate` method.

[Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.can_paginate)

```python
def can_paginate(
    self,
    operation_name: str
) -> bool:
    pass
```

### create_domain

Type annotations for `boto3.client("cloudsearch").create_domain` method.

[Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.create_domain)

```python
def create_domain(
    self,
    DomainName: str
) -> CreateDomainResponseTypeDef:
    pass
```

### define_analysis_scheme

Type annotations for `boto3.client("cloudsearch").define_analysis_scheme` method.

[Client.define_analysis_scheme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.define_analysis_scheme)

```python
def define_analysis_scheme(
    self,
    DomainName: str,
    AnalysisScheme: "AnalysisSchemeTypeDef"
) -> DefineAnalysisSchemeResponseTypeDef:
    pass
```

### define_expression

Type annotations for `boto3.client("cloudsearch").define_expression` method.

[Client.define_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.define_expression)

```python
def define_expression(
    self,
    DomainName: str,
    Expression: "ExpressionTypeDef"
) -> DefineExpressionResponseTypeDef:
    pass
```

### define_index_field

Type annotations for `boto3.client("cloudsearch").define_index_field` method.

[Client.define_index_field documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.define_index_field)

```python
def define_index_field(
    self,
    DomainName: str,
    IndexField: "IndexFieldTypeDef"
) -> DefineIndexFieldResponseTypeDef:
    pass
```

### define_suggester

Type annotations for `boto3.client("cloudsearch").define_suggester` method.

[Client.define_suggester documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.define_suggester)

```python
def define_suggester(
    self,
    DomainName: str,
    Suggester: "SuggesterTypeDef"
) -> DefineSuggesterResponseTypeDef:
    pass
```

### delete_analysis_scheme

Type annotations for `boto3.client("cloudsearch").delete_analysis_scheme` method.

[Client.delete_analysis_scheme documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.delete_analysis_scheme)

```python
def delete_analysis_scheme(
    self,
    DomainName: str,
    AnalysisSchemeName: str
) -> DeleteAnalysisSchemeResponseTypeDef:
    pass
```

### delete_domain

Type annotations for `boto3.client("cloudsearch").delete_domain` method.

[Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.delete_domain)

```python
def delete_domain(
    self,
    DomainName: str
) -> DeleteDomainResponseTypeDef:
    pass
```

### delete_expression

Type annotations for `boto3.client("cloudsearch").delete_expression` method.

[Client.delete_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.delete_expression)

```python
def delete_expression(
    self,
    DomainName: str,
    ExpressionName: str
) -> DeleteExpressionResponseTypeDef:
    pass
```

### delete_index_field

Type annotations for `boto3.client("cloudsearch").delete_index_field` method.

[Client.delete_index_field documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.delete_index_field)

```python
def delete_index_field(
    self,
    DomainName: str,
    IndexFieldName: str
) -> DeleteIndexFieldResponseTypeDef:
    pass
```

### delete_suggester

Type annotations for `boto3.client("cloudsearch").delete_suggester` method.

[Client.delete_suggester documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.delete_suggester)

```python
def delete_suggester(
    self,
    DomainName: str,
    SuggesterName: str
) -> DeleteSuggesterResponseTypeDef:
    pass
```

### describe_analysis_schemes

Type annotations for `boto3.client("cloudsearch").describe_analysis_schemes` method.

[Client.describe_analysis_schemes documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_analysis_schemes)

```python
def describe_analysis_schemes(
    self,
    DomainName: str,
    AnalysisSchemeNames: List[str] = None,
    Deployed: bool = None
) -> DescribeAnalysisSchemesResponseTypeDef:
    pass
```

### describe_availability_options

Type annotations for `boto3.client("cloudsearch").describe_availability_options` method.

[Client.describe_availability_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_availability_options)

```python
def describe_availability_options(
    self,
    DomainName: str,
    Deployed: bool = None
) -> DescribeAvailabilityOptionsResponseTypeDef:
    pass
```

### describe_domain_endpoint_options

Type annotations for `boto3.client("cloudsearch").describe_domain_endpoint_options` method.

[Client.describe_domain_endpoint_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_domain_endpoint_options)

```python
def describe_domain_endpoint_options(
    self,
    DomainName: str,
    Deployed: bool = None
) -> DescribeDomainEndpointOptionsResponseTypeDef:
    pass
```

### describe_domains

Type annotations for `boto3.client("cloudsearch").describe_domains` method.

[Client.describe_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_domains)

```python
def describe_domains(
    self,
    DomainNames: List[str] = None
) -> DescribeDomainsResponseTypeDef:
    pass
```

### describe_expressions

Type annotations for `boto3.client("cloudsearch").describe_expressions` method.

[Client.describe_expressions documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_expressions)

```python
def describe_expressions(
    self,
    DomainName: str,
    ExpressionNames: List[str] = None,
    Deployed: bool = None
) -> DescribeExpressionsResponseTypeDef:
    pass
```

### describe_index_fields

Type annotations for `boto3.client("cloudsearch").describe_index_fields` method.

[Client.describe_index_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_index_fields)

```python
def describe_index_fields(
    self,
    DomainName: str,
    FieldNames: List[str] = None,
    Deployed: bool = None
) -> DescribeIndexFieldsResponseTypeDef:
    pass
```

### describe_scaling_parameters

Type annotations for `boto3.client("cloudsearch").describe_scaling_parameters` method.

[Client.describe_scaling_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_scaling_parameters)

```python
def describe_scaling_parameters(
    self,
    DomainName: str
) -> DescribeScalingParametersResponseTypeDef:
    pass
```

### describe_service_access_policies

Type annotations for `boto3.client("cloudsearch").describe_service_access_policies` method.

[Client.describe_service_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_service_access_policies)

```python
def describe_service_access_policies(
    self,
    DomainName: str,
    Deployed: bool = None
) -> DescribeServiceAccessPoliciesResponseTypeDef:
    pass
```

### describe_suggesters

Type annotations for `boto3.client("cloudsearch").describe_suggesters` method.

[Client.describe_suggesters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.describe_suggesters)

```python
def describe_suggesters(
    self,
    DomainName: str,
    SuggesterNames: List[str] = None,
    Deployed: bool = None
) -> DescribeSuggestersResponseTypeDef:
    pass
```

### generate_presigned_url

Type annotations for `boto3.client("cloudsearch").generate_presigned_url` method.

[Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.generate_presigned_url)

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

### index_documents

Type annotations for `boto3.client("cloudsearch").index_documents` method.

[Client.index_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.index_documents)

```python
def index_documents(
    self,
    DomainName: str
) -> IndexDocumentsResponseTypeDef:
    pass
```

### list_domain_names

Type annotations for `boto3.client("cloudsearch").list_domain_names` method.

[Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.list_domain_names)

```python
def list_domain_names(
    self
) -> ListDomainNamesResponseTypeDef:
    pass
```

### update_availability_options

Type annotations for `boto3.client("cloudsearch").update_availability_options` method.

[Client.update_availability_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.update_availability_options)

```python
def update_availability_options(
    self,
    DomainName: str,
    MultiAZ: bool
) -> UpdateAvailabilityOptionsResponseTypeDef:
    pass
```

### update_domain_endpoint_options

Type annotations for `boto3.client("cloudsearch").update_domain_endpoint_options` method.

[Client.update_domain_endpoint_options documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.update_domain_endpoint_options)

```python
def update_domain_endpoint_options(
    self,
    DomainName: str,
    DomainEndpointOptions: "DomainEndpointOptionsTypeDef"
) -> UpdateDomainEndpointOptionsResponseTypeDef:
    pass
```

### update_scaling_parameters

Type annotations for `boto3.client("cloudsearch").update_scaling_parameters` method.

[Client.update_scaling_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.update_scaling_parameters)

```python
def update_scaling_parameters(
    self,
    DomainName: str,
    ScalingParameters: "ScalingParametersTypeDef"
) -> UpdateScalingParametersResponseTypeDef:
    pass
```

### update_service_access_policies

Type annotations for `boto3.client("cloudsearch").update_service_access_policies` method.

[Client.update_service_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html#CloudSearch.Client.update_service_access_policies)

```python
def update_service_access_policies(
    self,
    DomainName: str,
    AccessPolicies: str
) -> UpdateServiceAccessPoliciesResponseTypeDef:
    pass
```